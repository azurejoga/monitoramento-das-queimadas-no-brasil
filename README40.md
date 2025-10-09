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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fa995c1-5aa6-380d-b549-ffbd4638c7de | -8.60437 | -45.09758 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a302e36-77e8-35a2-9345-7ca339213a82 | -3.10711 | -44.49862 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6fd37148-e539-3529-a7e6-6b0ad6c9e235 | -13.27018 | -42.5006 | 2025-10-09 04:19:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 86714155-d71b-3dca-9246-b64c60355702 | -11.75889 | -45.1438 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aae47e37-028e-35e4-b874-a39ab03d61d8 | -4.14661 | -38.70684 | 2025-10-09 04:19:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee47f7c3-53f5-3cf7-8576-cbffd86838f0 | -14.42251 | -43.97082 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 272514e8-5657-36c3-b280-4207d7c0382e | -13.80384 | -45.83134 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e10af95f-c3a0-33fe-a9bb-fce32033f3e5 | -12.42632 | -45.71663 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d1fb5bf2-19ff-3d13-b083-6e22b05fafb4 | -14.41496 | -43.97368 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0728257-919e-30a7-951f-bc2473ea64d3 | -11.7517 | -45.14626 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0cf51b7f-e8cc-3ea1-a085-a4d742175616 | -8.53953 | -46.20953 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 232dadee-bc42-3271-aae9-bb78fe4fb398 | -11.82008 | -45.14191 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 85a8e701-34e6-3373-8b67-e00ae8e021bf | -7.33131 | -44.79168 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 29968c7c-16d3-3f73-95c9-0aec50fcc9e5 | -9.40591 | -45.99704 | 2025-10-09 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db8586a6-967b-3f73-a43f-e1db163c14bc | -10.19968 | -44.55989 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc9dc44a-99cf-3be8-a786-8009cddb14ed | -9.22276 | -47.85053 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6928732-ae64-3d92-9a14-c34c40da6f76 | -13.82648 | -45.81684 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 051c7759-e4b6-3d10-bb6b-02e76bb29c14 | -13.67549 | -48.74669 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f06117f-5d2a-3e3e-a6a1-db7faadfb73d | -8.19318 | -43.33218 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| ed848f22-da67-3199-84a9-74a6b0bf8d6a | -12.42853 | -45.70255 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ceb2e2ce-fc18-3cf4-9752-fa918e838587 | -1.18458 | -49.14013 | 2025-10-09 04:19:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cba9e15-9b33-3504-b593-caa28b379c8b | -11.7528 | -45.13921 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d0ab6c2a-a164-3a33-8e6f-b85dcb51a924 | -7.80908 | -46.71568 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d343be38-2294-363e-bc5e-99ec372895ef | -8.36186 | -44.95596 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9311d14b-c236-3054-a6c2-8df23599438a | -9.61394 | -40.33285 | 2025-10-09 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 096f4de4-5bbf-3ee5-ad79-d57a863a2f26 | -8.59623 | -47.98073 | 2025-10-09 04:19:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b9567a21-f60b-39cf-afa1-8b75b18d90d7 | -7.72229 | -42.38211 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3d414740-f70a-30d8-87ba-bf2e3d5ccee7 | -7.53522 | -44.31632 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b5b35b1-5e95-30fc-85f0-98c1b10cb185 | -12.42687 | -45.71311 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6c3ca421-094f-3840-8ea9-3f29940d9eb4 | -14.4377 | -47.50593 | 2025-10-09 04:19:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b3617c7d-6352-3c24-a3f2-a15a90888448 | -7.33022 | -44.7986 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61732ae2-f0f6-38f9-8704-3f83b9b4600c | -10.87888 | -45.08245 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8fa4c4a9-0fb2-3833-9fc5-1bd8ed7d1a97 | -7.76881 | -44.03798 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| aa79a42a-2126-3ef7-90d9-ba626fbc5d8f | -14.50877 | -46.6385 | 2025-10-09 04:19:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c5fd37d-0b0a-3de9-aecd-39c54fb656f0 | -12.83069 | -41.03205 | 2025-10-09 04:19:00 | NOAA-20 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9acc00b9-97d9-3b3d-8470-7da8cc6a7666 | -11.31367 | -44.88398 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d19d190-1e8a-345f-a643-7eb003bf5627 | -11.15059 | -47.74148 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58f20217-9096-39f6-9a3c-fd71b2b003b8 | -11.74948 | -45.13868 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f501ab07-aa03-3dfc-9fe7-f5c528e7e8ef | -2.27579 | -47.2001 | 2025-10-09 04:19:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ef4ac2c7-3a02-3ebf-b98d-282d59e69fa9 | -10.19189 | -44.54414 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef29573a-8f26-3611-b10f-1b3c58cdea2c | -9.61843 | -40.32995 | 2025-10-09 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| aef8dd65-7339-3f5d-bf20-8b7d2740e6d7 | -8.2378 | -47.86568 | 2025-10-09 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5a9008e-40eb-33bc-a1ad-9e13191de728 | -13.79942 | -45.83789 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2c102d1-e57f-3eee-b60a-8290b8b77a63 | -12.58238 | -41.28637 | 2025-10-09 04:19:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cccdd9fc-83c4-342b-822b-bccb9486e787 | -11.23971 | -40.33752 | 2025-10-09 04:19:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f11e691e-752b-32dd-902f-e3f4b2190f25 | -7.63292 | -43.05613 | 2025-10-09 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 47417d04-bb9b-3bb6-9ff0-464a829c4e5f | -14.45154 | -47.29316 | 2025-10-09 04:19:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 63ef1f31-d51d-3ad7-b911-2c279058a614 | -11.75115 | -45.1498 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 773e3e61-12a0-3814-82fe-0c81198c61ce | -9.40439 | -45.94266 | 2025-10-09 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3400bfd2-b0bf-32c6-82f7-2d8ef197eb43 | -11.57134 | -44.66575 | 2025-10-09 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7f2058d-c09b-3e29-bd3e-167adb311a7c | -13.93767 | -42.35499 | 2025-10-09 04:19:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3e55231-53f4-38bc-8fcd-307899c257d8 | -11.79535 | -45.04085 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b112e64a-a8b3-3414-b151-c9f89b205b06 | -7.66693 | -42.58231 | 2025-10-09 04:19:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5d151e13-b234-39ed-93cf-c62caa24fe4d | -13.64916 | -46.80912 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c544c65b-bc34-3553-85ce-158785f438e4 | -7.7732 | -42.4093 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 11a4236f-9139-3967-b2df-20fd600aaf38 | -13.78616 | -45.85757 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22ea0662-905e-3d48-9b53-2883258d9729 | -14.41322 | -43.98552 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7199e1bf-343c-3dd4-870d-10bb8de18a94 | -11.79147 | -45.04388 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 860ac414-a72e-3ceb-ba20-410d09b0de6c | -12.16802 | -47.78374 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80809d93-fc5d-3810-bee1-e12680aa9195 | -15.05945 | -42.3355 | 2025-10-09 04:19:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 74a750aa-f8f0-3e20-85eb-916526215f62 | -14.20477 | -46.60567 | 2025-10-09 04:19:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c2b71e1-af43-3afc-8f7a-bd6f32d6daef | -7.68447 | -42.39613 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7e003a7e-bcce-38eb-90ac-959653d53cec | -10.53046 | -50.02568 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb599cd5-90bd-373a-8042-9917f22d0524 | -11.84769 | -45.09553 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 815fee05-e96b-34eb-8766-71b9474fb641 | -9.16939 | -40.30779 | 2025-10-09 04:19:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| eda49676-4b8d-3947-a953-7d2cf2dd8178 | -10.72901 | -49.33547 | 2025-10-09 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d23e9204-8898-3296-8cd2-7da37688d366 | -8.58115 | -48.73434 | 2025-10-09 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 257a0e15-1fc2-3d4c-bd5c-d87758971ed4 | -13.33782 | -43.07153 | 2025-10-09 04:19:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 63478970-0106-311c-95eb-e1355a8ee339 | -1.40657 | -46.71046 | 2025-10-09 04:19:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f912f712-44e2-3067-9597-7bf3b85c75d1 | -11.7788 | -45.147 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 88b7db0d-a0dd-359c-a8c1-e3edaf365569 | -0.90599 | -47.55008 | 2025-10-09 04:19:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b808d6f7-0a7b-31f4-a9cd-4678e790bda3 | -14.25742 | -45.86179 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f0c3a93-9777-3cdc-a840-20b8d14a1ef1 | -7.48437 | -47.02737 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d7be4ac0-13a6-357d-b5d5-d478c8a7a2ea | -13.79277 | -45.88046 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30dc5fde-f4b4-3dc7-8e36-4e14cb75f98c | -11.74561 | -45.14168 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a047948d-c8a8-364c-8335-5ba4bfc77956 | -14.41438 | -43.97763 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d71fa5d-b583-3956-a74d-c68be1deaf3f | -7.7933 | -42.60519 | 2025-10-09 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b569a9c5-9bd4-3131-ad9d-29ef8abc254f | -11.13337 | -47.73863 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a966d6a3-6cf9-3334-93c3-8425c0791b29 | -11.79297 | -45.14124 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dcf29541-4ffa-320b-bb46-dddbe4597859 | -13.36574 | -47.21829 | 2025-10-09 04:19:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20dcdae6-24fb-3578-938a-d3b5702da5dc | -11.97881 | -48.89168 | 2025-10-09 04:19:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4388cc65-c871-3f28-b996-58efb8cca36f | -7.77437 | -42.40152 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 77951664-91d3-3ae3-9fd4-4b5536747341 | -11.78766 | -45.15561 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140437ad-5bd9-31bd-bb93-deeecb895ed3 | -12.24755 | -43.782 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b333ef59-afc3-32cc-b487-c0c30bfb0458 | -12.82844 | -41.03151 | 2025-10-09 04:19:00 | NOAA-20 | NOVA REDENÇÃO | BAHIA | Brasil | 2922854 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 29bec16c-ad1a-345f-9660-4f60d7c1b5bb | -7.33076 | -44.79514 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 47a6423f-8cd7-3f27-923a-63a9275ac291 | -10.65913 | -44.15208 | 2025-10-09 04:19:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fbcae11-354f-31b0-a6c7-fb2905fafed9 | -7.79529 | -42.40477 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b7230935-47bf-3b18-98f6-78caa4dffaa2 | -12.42577 | -45.6985 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b21247e8-f6cc-3060-9499-90d7f7a21832 | -9.21857 | -47.85394 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0a763ecd-d7a0-369d-b3ab-466929f11b44 | -14.4254 | -43.9753 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 19f0fb46-423c-3620-b588-9cab5a137996 | -7.32587 | -44.84761 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3008cc8e-0e6c-31e8-8450-8d9a03ea8a5f | -11.86783 | -45.51108 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b29d50c7-7bd9-383a-b36b-8328109c5fda | -13.76466 | -45.79948 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6854b8e8-ea65-3390-8427-7d5c9a0fd18d | -13.79112 | -45.86928 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 458d48f5-86f7-33c8-b7cc-1d595b4f99b8 | -7.69242 | -42.96727 | 2025-10-09 04:19:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f25d7c8f-69ac-3260-9274-3efd2b58ba51 | -7.32691 | -44.79808 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2fd1a4e-a073-3ba0-98ea-b5b27b876a27 | -11.88406 | -44.94888 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1efa84e-87cf-3fe4-9418-addf9d6df37f | -7.79181 | -44.19579 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7581937-701c-3fab-967a-4725254063e2 | -14.29173 | -47.41725 | 2025-10-09 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README41.md)
