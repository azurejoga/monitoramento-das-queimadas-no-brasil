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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d783bc8-679b-37a5-8303-bdd6b56d974f | -16.60053 | -58.23412 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 69762d0a-6103-393b-8c04-64adfbe41537 | -14.77545 | -52.68002 | 2026-06-06 05:48:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7efdcd8-e2a5-3f14-ba1a-898b2eb07253 | -13.49311 | -56.57063 | 2026-06-06 05:48:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| adeec85f-33cd-3e43-8fc4-1d677f31561b | -16.14038 | -58.49586 | 2026-06-06 05:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 92241650-3695-3732-a23e-4e17a481ad64 | -19.74883 | -53.54635 | 2026-06-06 05:50:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 98ffc6f3-70e6-35d3-ad4d-5b6291dcd04b | -19.74147 | -53.55209 | 2026-06-06 05:50:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f15459f2-2a1b-36df-8feb-cbddfc147a7d | -19.74199 | -53.54584 | 2026-06-06 05:50:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b56792c-1013-373a-b88b-52b1ec2c6516 | -19.74833 | -53.55242 | 2026-06-06 05:50:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f1f2390-fb30-3550-a334-73aff237e7cf | -9.1696 | -58.06603 | 2026-06-06 06:03:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1e4126a-2d3d-3251-b543-5843bcb13141 | -9.33344 | -67.68497 | 2026-06-06 06:05:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 469f1409-1415-37f8-aedd-72ec19f8cb59 | -10.5747 | -57.31751 | 2026-06-06 06:05:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 448f963e-37a0-3c7b-a8ce-ab8d2f4c5a88 | -12.77281 | -59.0054 | 2026-06-06 06:05:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10ccb3d1-4a6b-32bc-94d2-ab9893829cd9 | -10.57391 | -57.32426 | 2026-06-06 06:05:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f245fe-090b-3031-be86-76833738bc00 | -16.59801 | -58.24013 | 2026-06-06 06:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 12382b48-2429-300c-8464-4bcbdf5cf557 | -16.59867 | -58.23311 | 2026-06-06 06:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 825f1d99-2918-3d6a-be49-b559d4b15687 | -16.59433 | -58.23543 | 2026-06-06 06:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e54c8799-f60c-3370-84ac-f9763c0f4a8f | -16.60148 | -58.23619 | 2026-06-06 06:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a7695a4e-df1c-3c9d-a05c-6ca8166d47a7 | -6.44449 | -44.58113 | 2026-06-06 06:22:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b8588a67-1a72-31cd-a0c8-44bb7323c7c7 | -6.98352 | -42.8823 | 2026-06-06 06:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f9ea538e-eb52-3b36-9900-e635563e1888 | -6.53286 | -45.64601 | 2026-06-06 06:22:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 234851ed-38f9-33ef-9f16-58d91065db2a | -5.92603 | -43.47498 | 2026-06-06 06:22:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5ffeb53e-c875-30e9-878e-6203f21c057e | -6.72576 | -44.3714 | 2026-06-06 06:22:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8e32d16c-6765-3bb7-bfaa-631b39fc8cda | -5.35348 | -45.18408 | 2026-06-06 06:22:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d4d1de2e-284b-383d-8241-51983203d23e | -5.92467 | -43.48415 | 2026-06-06 06:22:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8e1ee37-2180-3e36-8c1a-79d6103eeecb | -8.93345 | -45.672 | 2026-06-06 06:22:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 189e87a3-f638-3064-9a45-4928f8a3bc91 | -6.98499 | -42.87232 | 2026-06-06 06:22:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b097c61a-f470-320f-8942-b28a8ad08daf | -6.04919 | -47.88933 | 2026-06-06 06:22:00 | AQUA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5a72940a-9a73-37f5-bde4-2ca237ea7a79 | -6.44713 | -44.56357 | 2026-06-06 06:22:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 07b9b608-aec7-3874-9d6d-bcfad7a41b33 | -6.5315 | -45.65485 | 2026-06-06 06:22:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 766a9f71-b420-3166-a3b7-5b63eb6d8d9f | -12.50196 | -46.27646 | 2026-06-06 06:25:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 431ccb8f-a350-3b2a-95c8-f837bb17e6a9 | -13.36237 | -43.20001 | 2026-06-06 06:25:00 | AQUA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 40131ee1-a284-34ca-bcf8-2143ea16c059 | -14.22688 | -45.80531 | 2026-06-06 06:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dbbabead-a13d-3c40-91df-839f31664c75 | -12.0673 | -48.07018 | 2026-06-06 06:25:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ffae4b2-1232-3bc9-9e4e-af19801b772e | -14.22824 | -45.79614 | 2026-06-06 06:25:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3b563392-5b0b-3a54-ae1e-e930173f5255 | -12.50062 | -46.28538 | 2026-06-06 06:25:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 5585bb05-777d-3f87-810e-6db170209786 | -12.49927 | -46.2943 | 2026-06-06 06:25:00 | AQUA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 50764994-5edd-3a6b-abbf-1431ee93023e | -9.08418 | -50.60279 | 2026-06-06 06:25:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5c4db365-cfff-3e18-8fda-d6c68302fdd0 | -12.06735 | -48.42906 | 2026-06-06 06:25:00 | AQUA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 013ff5c6-4309-3533-a5d8-7a6d24b935b9 | -14.2754 | -58.4467 | 2026-06-06 09:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| e2948947-393d-3212-ab74-a3a4f18e5c71 | -12.6428 | -52.1242 | 2026-06-06 10:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| d7ef3406-1bd4-31cd-89f1-52f08a233409 | -12.6428 | -52.1242 | 2026-06-06 10:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| c42f27eb-d162-3428-9aec-8b80993f78d2 | -12.6425 | -52.1453 | 2026-06-06 10:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 6d119308-b545-371b-af52-74e4fe0d6ba5 | -12.6428 | -52.1242 | 2026-06-06 10:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 553b75d4-0dea-35e0-971e-ffca9adc4573 | -14.3593 | -45.5726 | 2026-06-06 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| a9f5132e-7b48-314a-90a4-cb828bed817f | -14.3593 | -45.5726 | 2026-06-06 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| dec433ba-66d9-3f6e-8ee9-f5e0ca08c48c | -14.2754 | -58.4467 | 2026-06-06 11:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ed69a574-5820-340a-94ac-dbf49de602a5 | -6.43711 | -44.58281 | 2026-06-06 11:51:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d0380644-868c-3148-befb-ae7ef79b89bc | -5.81753 | -45.12654 | 2026-06-06 11:51:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 92fde06f-22e6-3c91-97f5-01484ab74b1c | -5.81882 | -45.11737 | 2026-06-06 11:51:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 07388f6b-105a-3488-b278-ea79e1a9b427 | -5.8098 | -45.11621 | 2026-06-06 11:51:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 7c544f3f-b958-396a-a5fc-10702c2d75c0 | -5.80852 | -45.12539 | 2026-06-06 11:51:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 34764f38-3c8d-3cbe-834d-14f7da0323b2 | -5.34876 | -45.18085 | 2026-06-06 11:51:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b8c83219-00c0-35c9-b077-98cf2466ed81 | -7.10023 | -46.9462 | 2026-06-06 11:51:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 02edc8d0-b5cc-373a-8eb8-c0e71506d461 | -7.16291 | -44.06184 | 2026-06-06 11:51:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4b016207-c35c-3c39-85b6-4dec0fd86da3 | -7.02076 | -45.41945 | 2026-06-06 11:51:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 44d3dda0-5327-342e-94ea-73e1b530ef16 | -5.52925 | -44.41686 | 2026-06-06 11:51:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a2cfe967-6cc1-3764-975d-d73db1b77ff3 | -6.98646 | -42.88154 | 2026-06-06 11:51:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 3c4f695d-d837-37a3-bb88-ae76bdf5391a | -6.04887 | -47.89185 | 2026-06-06 11:51:00 | TERRA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2bb01e3f-89d4-3009-b051-99212fb6023f | -5.92405 | -43.4783 | 2026-06-06 11:51:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 33dafa79-b6a5-3307-a461-afd5bde7598c | -9.03493 | -46.11052 | 2026-06-06 11:53:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e74df9c7-b584-38fe-8cd9-5317ee0e30bb | -9.14272 | -47.75088 | 2026-06-06 11:53:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1026729a-c161-3edc-936a-a18988107f81 | -9.15157 | -47.75214 | 2026-06-06 11:53:00 | TERRA_M-M | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dcdfcc53-7505-3464-a43c-7013d774e15a | -9.03622 | -46.10136 | 2026-06-06 11:53:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dbfbbbec-f84b-379a-be57-29ff33a9682d | -8.94422 | -45.64079 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 4e234d54-7f49-31d8-a363-68285ee31541 | -8.5154 | -51.56864 | 2026-06-06 11:53:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| bf694550-ca7b-338e-a0fb-1c9bbc1ddee6 | -12.07173 | -48.42806 | 2026-06-06 11:53:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a85c75fe-3fb0-34be-a423-5bace2f2adda | -8.27919 | -48.22895 | 2026-06-06 11:53:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3a4e25c9-b8a3-39fe-9fb8-cca979bb04b9 | -15.06353 | -41.35384 | 2026-06-06 11:53:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.6 |
| 22c0aa23-e060-31b6-82ec-cf8af138b520 | -11.04195 | -44.32175 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 43966c05-9597-317d-b1a7-c001c2e570bd | -10.45415 | -47.94189 | 2026-06-06 11:53:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| be3c104e-dc8f-31de-bfab-332324575f6c | -10.66041 | -49.29605 | 2026-06-06 11:53:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0b1193d1-fd65-3d06-a106-8e617a05acf7 | -10.81705 | -49.23274 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4522b9ac-786b-3f2d-b46a-f9f195f0d989 | -9.42311 | -50.69328 | 2026-06-06 11:53:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 1aaecbc4-b9ff-3a78-acb7-5c07f1dc2752 | -12.63478 | -52.13548 | 2026-06-06 11:53:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 06c7bde0-e136-3eb4-b2f4-e627299257ae | -8.93518 | -45.63951 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b9aed3b4-6494-3e8b-a1a0-ae075a578de5 | -12.77318 | -47.12723 | 2026-06-06 11:53:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e35af798-72e0-3d22-bc29-51502f4a4ab0 | -12.51802 | -48.26949 | 2026-06-06 11:53:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 62e35e55-36b5-3ab7-8c01-4658392b02a0 | -13.35828 | -43.20571 | 2026-06-06 11:53:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 297403bc-77d1-38f6-bd03-1021b3cb4c60 | -11.47224 | -47.98401 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a4f8cbf-8010-32ad-b13f-893cd41fafbb | -8.28053 | -48.21969 | 2026-06-06 11:53:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aebcb827-8cc6-3403-9ba4-c0f896b467f1 | -12.06652 | -45.97995 | 2026-06-06 11:53:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4d1981fc-fc5e-336c-ac5a-88dfb5578848 | -12.06519 | -45.98968 | 2026-06-06 11:53:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 254f9916-dd49-349c-80b3-c67e6ca4232a | -8.93131 | -45.66764 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 1fc49907-06d5-3e46-9c78-520200d76317 | -8.93647 | -45.63014 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ad1275b7-69fd-336a-a8e5-924e1bbb5c2a | -15.05453 | -41.34705 | 2026-06-06 11:53:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| ba786759-baf7-31b8-b423-cedbf98e6094 | -12.49447 | -46.28516 | 2026-06-06 11:53:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 55436cf5-8378-3b83-b79a-003e6d3bb033 | -10.13533 | -50.73091 | 2026-06-06 11:53:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| da77e882-59bd-3d6d-bb51-41b1e199f1e3 | -10.82622 | -49.23406 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 28a14f7f-6ee2-3dd9-8f2e-a66afc01a4e3 | -12.50484 | -46.27709 | 2026-06-06 11:53:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cafadbca-0b33-3301-974c-81c97a11c1eb | -10.82476 | -49.24375 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 06b9000e-aa5e-3eea-8940-fb628b3140df | -9.90174 | -47.48195 | 2026-06-06 11:53:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8b8a14f8-9430-3b2e-bdf7-f353933c2d1c | -12.50356 | -46.28643 | 2026-06-06 11:53:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 10268249-5666-336e-81d4-454c38475caa | -14.22645 | -45.8022 | 2026-06-06 11:53:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 22549e6f-9cf1-34b5-b2d5-20897d6830bb | -10.86227 | -53.73967 | 2026-06-06 11:53:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4a2b008e-53a7-3048-85ef-55846c7e40b4 | -11.6973 | -45.38054 | 2026-06-06 11:53:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f510d047-87f6-3019-8b68-d37ed21e99d0 | -11.56002 | -52.79319 | 2026-06-06 11:53:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 4636efa6-bd9a-308a-878a-3c391b19d3a2 | -12.51672 | -48.27849 | 2026-06-06 11:53:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 812cd0d7-795a-3fb7-88a6-60e1f2a66bed | -9.42494 | -50.68136 | 2026-06-06 11:53:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| a1a639dd-ff51-3e81-bf1d-d4423defacb0 | -8.05161 | -50.67802 | 2026-06-06 11:53:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 2f87daa9-ca1b-3403-9216-226c0c129bfc | -8.9326 | -45.65826 | 2026-06-06 11:53:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |


[Clique aqui para ver as próximas entradas](README14.md)
