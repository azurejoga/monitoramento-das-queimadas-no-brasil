# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78c4803e-e4b8-321d-bb56-41afb7761599 | -12.69264 | -52.4011 | 2024-11-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08ab9a63-63aa-3ae6-ba4b-c47ab6fea2ed | -10.3926 | -44.46638 | 2024-11-21 04:10:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2acf94af-1d56-34dc-9aba-7210aa20c2b3 | -8.33783 | -43.89663 | 2024-11-21 04:10:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 870d05ea-5b7b-3b49-9575-f46108fe426b | -8.59679 | -40.64437 | 2024-11-21 04:10:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0a56b0f7-46bf-35c1-afe5-6369e423fd8b | -7.39238 | -42.78051 | 2024-11-21 04:10:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cfa47cb6-c382-3720-8fff-442b8ad71abb | -6.8205 | -46.77847 | 2024-11-21 04:10:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a332ae3a-5882-395f-a432-21c7a208ead2 | -9.97364 | -36.0808 | 2024-11-21 04:10:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 722a9b39-543b-3abb-a06c-7d8c5c41ee33 | -6.31671 | -49.67469 | 2024-11-21 04:10:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44c5d321-ab6a-36c2-8848-003d7e48765f | -13.53274 | -40.686 | 2024-11-21 04:10:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc711db6-785b-39f2-8448-9d5eb92f3ef1 | -8.22127 | -41.01452 | 2024-11-21 04:10:00 | NOAA-21 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6b918be4-5ce2-30e1-b9a1-2f49cd1a6926 | -18.16202 | -42.46018 | 2024-11-21 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 422f855e-0052-35b9-a8bd-d02bbe1b0a07 | -18.89268 | -43.18185 | 2024-11-21 04:12:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6da637af-788e-3334-80c6-8a86bd0039af | -17.59977 | -40.63637 | 2024-11-21 04:12:00 | NOAA-21 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7788a2c7-ab65-3750-b223-0391c4e1181e | -15.78064 | -46.62756 | 2024-11-21 04:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 976558e7-9f93-3399-8b71-0a71ef9f6fd9 | -18.44485 | -43.11036 | 2024-11-21 04:12:00 | NOAA-21 | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6fec2133-38db-35e1-9846-b302193b51c2 | -15.91703 | -44.78079 | 2024-11-21 04:12:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9077877c-14cd-30c6-8eb5-8db185d70903 | -18.15859 | -42.45964 | 2024-11-21 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 54ca97e5-4b3a-3aba-8581-968f713749bc | -16.68063 | -43.88438 | 2024-11-21 04:12:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5497d759-4338-34a6-bbcd-8ee10f8de098 | -18.15916 | -42.45577 | 2024-11-21 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95cff9a1-66ee-3737-bd17-5f638c2db94c | -18.43288 | -40.54972 | 2024-11-21 04:12:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 23ac940c-5019-3ce3-9b6c-25025096823f | -18.42913 | -40.54916 | 2024-11-21 04:12:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d490e66f-2658-32af-b1e0-d0d5870dc7a6 | -16.58903 | -41.42228 | 2024-11-21 04:12:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 93ac8e91-6bdc-3eff-af68-38bcc521f33b | -17.59745 | -43.19737 | 2024-11-21 04:12:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 904e3716-b84d-3e69-90fa-a86804315394 | -16.74517 | -45.76321 | 2024-11-21 04:12:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81575a66-9d0d-3617-8e05-51f9347e5b7f | -19.60715 | -40.05625 | 2024-11-21 04:12:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4f07b791-f67e-3478-8aab-27d20d7f83be | -17.35131 | -39.58599 | 2024-11-21 04:12:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fdac9ccd-2638-38f1-bc9d-b4f8e48e5cb1 | -16.00666 | -46.08389 | 2024-11-21 04:12:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a06b543a-190b-3791-b95b-3fe960e77005 | -18.42538 | -40.5486 | 2024-11-21 04:12:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c42a08e-76b7-3ad1-ad1d-83c3c2b3b6ba | -17.74823 | -42.63348 | 2024-11-21 04:12:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e51156ad-a4a1-34d1-8d78-96b4f60886d6 | -17.58749 | -43.28616 | 2024-11-21 04:12:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a444360d-d4f1-30b5-8fce-67cdf141abb7 | -18.42474 | -40.55331 | 2024-11-21 04:12:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| acd8278c-93bb-36bb-8291-70bae344f2a7 | -18.42848 | -40.55389 | 2024-11-21 04:12:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| c72b3a87-497b-3354-9593-951213ba1fa9 | -17.59083 | -43.2867 | 2024-11-21 04:12:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d96bfb1-43aa-3995-8835-b74654189b8f | -17.78114 | -42.81013 | 2024-11-21 04:12:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 96c4129f-09a8-31f7-ad88-d54c26aacc0f | -15.78009 | -46.6284 | 2024-11-21 04:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a93f8dc4-435c-38eb-b4f1-2a48dad4ae1f | -18.16259 | -42.45631 | 2024-11-21 04:12:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b631b363-9ade-3d3a-a172-bd017f7ab5a7 | -16.58834 | -41.42359 | 2024-11-21 04:12:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 649441fe-9af6-3d91-8550-2663cac03b15 | -16.74456 | -45.76697 | 2024-11-21 04:12:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 30f29630-598f-326e-a496-cd28822f38ee | -22.04363 | -44.71525 | 2024-11-21 04:14:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2e980dc1-7e93-32b7-a4ee-301d18334271 | -20.76575 | -46.77031 | 2024-11-21 04:14:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c82e14b2-2970-3c11-a0cf-c37d7c452d35 | -23.98383 | -48.91762 | 2024-11-21 04:14:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a28bc744-f85e-3621-847f-c53e17a46e4e | -20.48283 | -45.76428 | 2024-11-21 04:14:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25edf487-b743-37e1-908a-ea19c422d080 | -4.58 | -48.0132 | 2024-11-21 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| ccaa5469-e0c7-381b-b6ab-f58a4bbe8a4a | -4.5799 | -48.0349 | 2024-11-21 04:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 03201bd4-6f7c-388e-ad04-43bf127da6e3 | -4.2575 | -46.1188 | 2024-11-21 04:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f0c368f9-1946-38be-a012-1e5519694e23 | -3.2768 | -53.8199 | 2024-11-21 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 2016f48a-fad7-38b5-8f51-c7177095e4c4 | -3.295 | -53.8597 | 2024-11-21 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| c2735b83-abf5-3007-8221-dd9eb04f469f | -3.2767 | -53.84 | 2024-11-21 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| c7fa9632-33fd-3a82-9277-507ace598a44 | -3.2951 | -53.8395 | 2024-11-21 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 408b3de2-c213-3d6c-943a-a8f0420adfc8 | -2.0259 | -54.5289 | 2024-11-21 04:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 9a07586d-c3cd-3364-a724-638997da22d3 | -2.7676 | -52.1045 | 2024-11-21 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 33194eff-2fc9-3127-8140-762b9e67c51f | -4.2388 | -46.1197 | 2024-11-21 04:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 103.0 |
| bbbaad2f-8d2d-3807-a47e-da9818af9c52 | -2.68534 | -46.17442 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cafdaa7-3bcd-37b9-9ce1-24d4f7f5e8ac | -2.94756 | -48.33394 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1457bf13-5632-309b-9bf3-9cb18f19d91b | 1.78954 | -50.42771 | 2024-11-21 04:29:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dae4b39a-7fb9-3d6c-89d9-0c37aed27e84 | -2.14447 | -53.57416 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa396b3e-2fd4-3b77-9c2c-2be9dcc94746 | -1.13657 | -51.68014 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 408ca248-08e4-35bb-9d8e-30583b29af3a | -2.92727 | -48.33075 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1108fbfa-1ce5-3832-b662-58090942b63f | -3.39427 | -50.10392 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f024ade0-0ca0-3441-9de3-06e1967ae711 | -2.84565 | -46.68555 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a28d093c-bf5e-36ba-abcb-2d93bc645ec9 | -2.76006 | -52.11721 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| f0d4ffb0-1032-3133-9b4e-4086ccaa8800 | -2.43036 | -46.52864 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8686102-6476-3891-916c-2c181cf67ea9 | -1.22661 | -51.79461 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a667c317-bf0b-3af8-bf67-3ebbcc51574c | -3.0032 | -51.30654 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5fca0681-1851-3db7-88a9-4ae048731da7 | -3.06512 | -53.28603 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 032ba196-8837-3574-94f2-b31ecc4a6110 | -0.95567 | -51.71816 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74bc6660-ee9e-369d-8f62-df2a2490aa2f | -2.62696 | -48.48476 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 828c0508-158d-390d-8a0f-ed4e4a9124c7 | -1.48224 | -52.03559 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa6016c7-05d0-3213-b5d6-6b95e063200d | -3.29246 | -45.54436 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fa249bf-57c7-3d6d-a9e2-d89b29abd7a8 | 0.01504 | -51.19374 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a02fb447-0cc8-35ee-bf87-3503cf6d0110 | -1.13356 | -48.34534 | 2024-11-21 04:29:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f2a47d3-ff0e-3a13-b806-17ef8f77ff08 | -1.46466 | -52.68291 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c845e3e-dc00-31ce-9454-4808e134f86b | -1.25695 | -51.76207 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c0d9d025-9d70-3390-a9c1-330887f9d754 | -4.15174 | -43.88124 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c0d8885-41d6-31d3-af42-5e8f3030714d | -2.18586 | -46.40523 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d773b771-a4d3-3f40-af21-18efef7cc2ee | -2.85937 | -51.28034 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b4ea7ebc-8284-3536-b164-6f13f4f1ac36 | -1.20724 | -53.69733 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 361f7a25-930d-3770-ad31-fda99e7ed986 | -2.63508 | -46.21651 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 989f1edd-3319-35ad-b659-649407635f32 | -2.62009 | -48.1771 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6ab2908-0883-3db0-8fdd-c1732dbc2c94 | -1.14852 | -53.51218 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6edf70d7-53ef-3814-8869-a5b52c98a3cf | -0.17324 | -51.63568 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a21932b1-deb9-3e9d-94b1-e8be4dab8361 | -1.36068 | -55.51061 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 870e12ef-502e-3214-a6cb-bccfdb9005dd | -2.94609 | -48.5634 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd988bee-0f1f-33e9-8a58-04909b92f4bd | -1.42492 | -46.01439 | 2024-11-21 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 540e26d1-d1c2-3d9a-aadb-d918f6600251 | -2.62023 | -48.06763 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fef21b5d-ddfe-3f38-8c87-4dd3f89fa610 | -2.16942 | -51.97206 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 392b6e35-c86b-31dc-a38e-912090e0e930 | -1.63894 | -52.69097 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cfa0941-f995-3197-a086-7b560534e97d | -1.39492 | -46.50814 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e96e02d-dc6c-3e5e-85e8-7a96ebcde12c | -2.61957 | -54.27504 | 2024-11-21 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b42aeed0-b369-3abf-84d6-54bf4e0bb7c3 | -2.68893 | -51.71283 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14490bb2-08d1-3c5b-88ec-a64b3fe12f03 | -2.53284 | -46.37471 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbe8d24c-ff50-357a-99ba-3e12328faf39 | 0.13945 | -51.08897 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b0c2aed7-9ca3-3154-bbd7-e8ca8040675b | -1.25838 | -51.769 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c56812e4-1b17-3ba9-9ee7-10ca3a369514 | -2.69554 | -46.24008 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 182b0b15-d1cd-3fb6-a7ad-381c62c1f1d4 | -1.52687 | -55.37661 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e23e69c-d8d1-3e1c-b0be-279b16bb6e2f | -0.33781 | -51.55909 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39901919-46e5-3d73-9ddf-57239fbd86be | -2.95568 | -49.21447 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a56a7215-4da2-3cd2-876f-ee1f66efe7e6 | -2.25021 | -53.67722 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a018472-e5ff-3274-8e32-dbab80374963 | -0.64431 | -52.33834 | 2024-11-21 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0564716-86f6-3ef1-bf48-f3b0b60c82a2 | -3.18516 | -46.52574 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README24.md)
