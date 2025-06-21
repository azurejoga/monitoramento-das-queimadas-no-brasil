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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dadb4fd1-d877-3153-ae45-423ccd38f8b7 | -5.78086 | -45.90495 | 2025-06-21 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d29f6954-77b2-3cc6-8830-8e3541e04474 | -4.54441 | -48.01445 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 33d9c888-fdea-3495-8ec1-a9de146b7410 | -6.862 | -44.41789 | 2025-06-21 03:40:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c45ff0d9-8634-35d1-80a9-20ecb73c1810 | -5.7741 | -45.90843 | 2025-06-21 03:40:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f4b88d5-df45-3662-9795-75cebd280d03 | -3.62436 | -47.52237 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7053dc18-bad9-36b2-9d44-dac4b20ce49d | -6.41978 | -45.31181 | 2025-06-21 03:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f289197-846a-3f23-a956-fa3dcf155596 | -3.62185 | -47.52616 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6a4e07e-c0dc-32be-b3e2-5fccc099e865 | -4.37777 | -48.07056 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fa05723-7ec8-3782-a28d-4900af46fbf8 | -8.0728 | -34.97511 | 2025-06-21 03:40:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 93aec1b4-3f8f-3ff3-a05d-a06a5ee58b3c | -4.53038 | -48.01276 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 5917f32f-50a0-3ae6-8c68-53fd719a9ec1 | -4.54217 | -48.02736 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 670a9673-4baa-3345-a248-207a7305e1d2 | -7.22872 | -43.0694 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 8f5926a8-c727-3018-a95f-667584874697 | -7.22683 | -43.07541 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5edd10f7-0113-3740-a998-a2b2ad5f126e | -4.53857 | -48.00722 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 36bb8ac1-1368-38f2-99bc-f41972cff676 | -7.22201 | -43.07458 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| bc1f146a-4371-3e82-b4c5-99efe7ec4646 | -4.54544 | -48.008 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 0ede12ee-522e-34e6-a8aa-0685114522bd | -3.96208 | -48.13208 | 2025-06-21 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2bdb65d9-e227-3fa0-9eb0-f7c8176b6642 | -7.2239 | -43.0686 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 7b2baa91-c2d9-37a1-81c7-528193441c7f | -3.96912 | -48.13302 | 2025-06-21 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 343befbc-573d-32af-9d41-63efe21622d3 | -7.22778 | -43.07007 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c22c73b6-b534-3f77-b235-e6780db34c1f | -3.62075 | -47.53257 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37ff3b25-8ab3-39a2-a958-4a26b10764e4 | -7.21472 | -43.57323 | 2025-06-21 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 032a512f-a57a-3d57-9369-8706dacd5341 | -3.62319 | -47.52891 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ea6d19b9-bea9-364e-81c8-d615a53ade84 | -3.62549 | -47.51611 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 377c5756-3f0e-315d-903f-0455307098ff | -7.21426 | -43.067 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 89496222-9cca-3dea-bfbc-4a1af2764d4f | -3.6286 | -47.52757 | 2025-06-21 03:40:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b59de75b-9689-32a1-8938-d331eef1d19e | -3.9609 | -48.13861 | 2025-06-21 03:40:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c7175218-672f-3e97-8fb0-c77830b751dd | -4.5305 | -48.01283 | 2025-06-21 03:40:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| c656637b-7181-31ed-8c60-3614313f92db | -7.4561 | -43.0601 | 2025-06-21 03:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7f32e89-5f50-3e94-8897-d090a6c03663 | -6.53443 | -44.22265 | 2025-06-21 03:40:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e83040-a301-322e-ad9e-81b2edd64fef | -7.22781 | -43.07475 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 6f6fe5fd-7cc1-3323-96ed-09d5e3e9c1da | -7.21517 | -43.06169 | 2025-06-21 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| df96f8bd-1b27-3012-a80d-5097eddfd9ad | -12.26153 | -44.59901 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df9b7ce0-99fb-3491-93cd-689e21e35aeb | -8.98084 | -49.86353 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 865b398e-37ce-3430-81b0-ea315b389abd | -9.73949 | -48.33445 | 2025-06-21 03:42:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca1b703f-120e-3424-a5d2-7b09099c95df | -8.1976 | -47.77314 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 055f66ff-322e-3d96-886b-42a0ed36d9c6 | -10.14434 | -48.99495 | 2025-06-21 03:42:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d0cd3b6-a219-3feb-9877-2e0bbb69ea71 | -11.32391 | -45.22552 | 2025-06-21 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 585359f8-2f4d-30f0-8757-1b466e9adc0a | -8.02421 | -47.65993 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5d8c3ab-4f7c-38d0-a47f-e61faa52e25c | -12.2664 | -44.60003 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75184e80-b60c-36b5-9de8-27e0e2cb6392 | -7.26769 | -45.35736 | 2025-06-21 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae73c74d-1df7-39b3-a951-a73fe907f9d8 | -7.27257 | -45.3623 | 2025-06-21 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5bfb999-f321-317e-9087-27e996b06070 | -8.19182 | -47.77339 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae53e5f3-b756-3549-8231-c412b334db01 | -12.76361 | -44.41222 | 2025-06-21 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b78664a1-37a4-3277-9757-0851def66db4 | -12.25773 | -44.60384 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 621cc571-3b75-3a50-94f5-31da352239bf | -10.95606 | -44.546 | 2025-06-21 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13b9c4ca-9f38-3a94-9aa1-1ff93b28d16d | -10.50981 | -47.5735 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8cf7d9c-9db4-3f4c-acce-d32ab716202b | -8.01044 | -47.66291 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 779d1ab5-8046-31bf-b0de-97dca611a13c | -12.2626 | -44.60481 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf69edbc-4ee7-318f-8699-58dffe66a27e | -8.37699 | -46.9785 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 46a81048-ed0a-3da7-b777-4609227c511f | -10.51441 | -47.58123 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dbd2eddd-17a6-31ba-8191-52a6b178c795 | -8.00944 | -47.66828 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3e7c255-99fc-351e-96a5-ddae03181631 | -7.97613 | -46.21859 | 2025-06-21 03:42:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ee5686d-6788-33f5-aa1e-b252192c380e | -11.93789 | -48.42616 | 2025-06-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f1d10c8-4be6-3db0-847a-f32c018dd838 | -9.73411 | -48.32776 | 2025-06-21 03:42:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7c15cf1-0b28-3f75-909a-c44296064c88 | -8.37177 | -46.97283 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89405fbe-f284-31c6-af50-4035ff065313 | -10.44703 | -47.04775 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf39c79d-aa48-34f2-bd54-c7d21bf95a00 | -8.97943 | -49.87074 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a9df5b6d-94a1-32e7-8459-d6137c291e8a | -10.58439 | -46.92556 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44203ae3-e5c8-3f11-8ffc-fc183756cd72 | -8.01735 | -47.66812 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4802293-1321-3897-a8fc-a07056fad1e4 | -11.9346 | -48.427 | 2025-06-21 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a408fddc-e4bc-34d0-9a4a-b407e1542c96 | -8.01941 | -47.65738 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5d4053d-f1da-32da-9614-0dc0a210133e | -8.18917 | -47.78273 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 295dfbe6-7560-3ba3-9c0b-5f062b9868d9 | -10.44617 | -47.05225 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3ef5993-4916-353a-8c1d-bc4b8868b37e | -8.73324 | -47.99002 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 083a60da-bc7a-3b5f-a707-09bc1518e6f8 | -8.98356 | -49.86554 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c7808210-11f7-3209-a46a-44b421b623f5 | -8.19118 | -47.77199 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 079bd100-6f20-3872-b3ca-4a9438209ccc | -10.54152 | -46.77589 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df7333e9-1edf-338f-8915-239aa2e77988 | -13.00436 | -42.66976 | 2025-06-21 03:42:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 95d9e6b5-584a-387b-9fca-74f5de1bb66f | -9.33343 | -40.21344 | 2025-06-21 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| f23c0a33-822d-316c-9e3e-04a6f8b6b6dd | -10.46815 | -47.03344 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3647d3ce-d939-32c5-a3fc-0e8436da544d | -7.26699 | -45.36118 | 2025-06-21 03:42:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56d15507-1ef7-3681-9877-308feaa350da | -10.5364 | -46.76894 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c7c018d-b200-300c-a19c-13e283442947 | -10.54075 | -46.77996 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4030245d-e43f-3ed2-9e05-3262ce9fb5c5 | -10.45629 | -47.03149 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ee96fe7-623d-3974-91ee-6ce18b7500a3 | -10.55389 | -46.77402 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a8a90e0-b571-37e1-9aca-0cd27982e7c3 | -12.26537 | -44.60567 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 350d6352-68e2-314f-95ac-2f574f802c8b | -12.6363 | -44.32829 | 2025-06-21 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae422b0f-9f82-3a1d-bf79-24a6f777df9a | -12.16398 | -48.67862 | 2025-06-21 03:42:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d9bd9fb-bd72-3c77-8e1b-1ce6605f03d8 | -10.44873 | -47.03894 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4030f7a0-4354-37cc-ba85-301180b71eb3 | -10.44789 | -47.04332 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bb86aaf0-84cf-3e3a-992c-8de3f787c8bb | -11.20517 | -47.83973 | 2025-06-21 03:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 514e5045-8688-3c59-b32d-6147919d2e36 | -9.73292 | -48.33376 | 2025-06-21 03:42:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0d9fe7c-b38f-3535-a344-49705131e8f1 | -10.44282 | -47.03786 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a7f3b773-15b3-39d9-acd9-9f212402450a | -11.33425 | -45.22757 | 2025-06-21 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 405f72e0-4ca4-33f6-a860-0f74b27b966f | -10.9556 | -44.54848 | 2025-06-21 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5f0f4f0-67ac-35c5-9bf2-8efd434872f8 | -11.20535 | -47.83643 | 2025-06-21 03:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d22165a6-c62c-36b3-ae81-81cbb6569414 | -8.02477 | -47.66393 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95924186-34e1-30b0-8a39-f3bdb6a7b35d | -9.33261 | -40.21831 | 2025-06-21 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 3f85aeb6-f036-3904-aa98-de2a434954f3 | -10.50787 | -47.58327 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d47aa614-87fd-3186-95e0-5c24ec0b1e26 | -8.37788 | -46.97382 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a0c71899-6f16-31d4-b601-9f960b43c3f6 | -8.19078 | -47.77876 | 2025-06-21 03:42:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b620b513-b124-301c-b954-bcbb052b91c7 | -11.32908 | -45.22654 | 2025-06-21 03:42:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c15e906c-9929-327e-b562-b8e2cae5b9ce | -8.13208 | -46.83377 | 2025-06-21 03:42:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2f00846-3f0a-315f-86d9-e1dd5999f47e | -12.26049 | -44.60465 | 2025-06-21 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2b1a40e1-afb3-3907-af87-e8b179511930 | -8.98211 | -49.87271 | 2025-06-21 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6eefe08d-4417-3274-a639-f8524e676612 | -10.15219 | -48.99039 | 2025-06-21 03:42:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 910bd091-b4d3-3cab-a471-be667af2f68c | -10.52708 | -47.58214 | 2025-06-21 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6173812d-0bb7-38bb-8aa8-9baa0fda5c13 | -10.44957 | -47.03461 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8067e80b-42e6-3d5c-942b-3ca8401736eb | -10.46139 | -47.03681 | 2025-06-21 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README9.md)
