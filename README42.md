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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c03aa339-9f9e-35df-abde-5fa688bca6c2 | -7.02093 | -39.22237 | 2024-11-23 04:18:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| df3766a7-2dc3-35fd-ba2e-2823937b335d | -4.53176 | -42.91783 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1245bbd6-a9a8-35b5-9db2-cfdb56657d17 | -6.34736 | -39.7961 | 2024-11-23 04:18:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 121c1c4c-a25e-3b3b-b4ed-9afc1fdc4269 | -4.0804 | -46.8368 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eefdf15a-3004-38fe-815d-8a2d65995581 | -5.10836 | -43.15909 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9b8533c2-b54f-36dc-93fb-e538a9289ae0 | -6.48003 | -47.50102 | 2024-11-23 04:18:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f8a1907a-f10c-3202-800d-5255b1b3e7c8 | -6.14675 | -46.67994 | 2024-11-23 04:18:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 470909b6-f547-3e08-9e39-acb928698bde | -4.24752 | -48.70037 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fa0a894e-f935-35ad-a759-57a71fde8a5c | -4.44894 | -48.19749 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 60d5e324-5695-3cc2-bba8-cdda819fb965 | -4.69688 | -45.66365 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c0e0ea-c4b8-33d4-b774-6ba72c5481ff | -4.35512 | -46.79453 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7221edf5-1250-3305-85b0-516f53e62485 | -5.54314 | -45.79016 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d1c88fc-399e-37ac-831e-3cf815876474 | -5.75587 | -46.25378 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a79fbdd-8765-3bb8-8363-11ae054a6a51 | -3.89371 | -46.10065 | 2024-11-23 04:18:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 838c0159-bc7d-39e6-8dfd-2dce515965cc | -6.25248 | -43.5527 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 503f931b-5d08-34fc-ba9b-a5a88001bcf7 | -5.82168 | -49.32708 | 2024-11-23 04:18:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d89d3e6-526c-36de-84c0-214276cc7822 | -4.91099 | -47.8606 | 2024-11-23 04:18:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 310b0049-1523-3b96-8c47-f96c56c2eeb2 | -3.25333 | -53.27821 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d958d066-0e4d-3ec5-9d99-9aa1985dd9d9 | -4.69789 | -45.85234 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dee5bfb5-d0f2-3966-b9b7-94a72c21e56f | -3.94761 | -47.96403 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4243d19-8aa3-360a-9ae5-5aa459ac2741 | -4.35684 | -48.69472 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7f20f89-92f2-32f9-99c4-39aad6fb25c7 | -4.21722 | -46.16166 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 82dc4dbe-a693-3268-bbf9-ef0caac12ca5 | -4.24832 | -48.69542 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41abdc60-267d-3fed-bd95-6b1387b73fd3 | -4.5312 | -42.92139 | 2024-11-23 04:18:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4c105d5e-cdf3-3fb0-a8d4-4d37219db20d | -4.60291 | -46.49155 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a0deeef-3b08-33c5-8f52-e039911cbc53 | -3.88595 | -43.15767 | 2024-11-23 04:18:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e795fc0-4ec2-3538-afc3-9c4dd3ab5d5d | -3.24691 | -54.23641 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a9497847-5781-3559-bea7-9fa6014dcf5e | -5.75471 | -46.26109 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b886478d-e45e-3207-afc4-a9fc3155e6ba | -3.75965 | -49.93797 | 2024-11-23 04:18:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4cf0ecea-b896-3458-aca3-90b53c447edb | -3.30056 | -52.57242 | 2024-11-23 04:18:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0c84149-e63e-3945-8b27-5058cd680637 | -5.69643 | -46.31988 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0623d711-aab8-33e4-8a3a-1723d1fb3ea9 | -6.25139 | -43.55976 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc9d19e6-b9c6-3e3e-afe0-018e72ede47f | -3.80463 | -51.26752 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09e6ca88-545a-34e5-87d5-8ecb16b521ea | -3.8103 | -52.00253 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1b1ec26-a9be-380e-a321-c282b987abcd | -4.2725 | -46.29674 | 2024-11-23 04:18:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dd0ff32-9f81-387d-9247-23dee2ca61e1 | -4.12106 | -48.51644 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 961183a5-048f-39ef-8e3c-ed0640a8503e | -2.15984 | -53.7789 | 2024-11-23 04:18:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9323baa7-a0f8-30b6-81e3-f6d492efb116 | -6.7445 | -43.24794 | 2024-11-23 04:18:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| af029e7a-7afd-363e-9a27-61d55b3f9ee9 | -4.41594 | -44.11245 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a35781bf-a8f0-3add-b215-99db8490b93d | -3.22612 | -54.25458 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54c09174-b3b7-3d3b-9067-6ebc3bf4d008 | -4.60756 | -48.48697 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d4a220-8c40-344c-99c4-1df925d87bc3 | -2.88308 | -51.58361 | 2024-11-23 04:18:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cc8c10e8-f448-303d-8563-e961c5492061 | -4.55969 | -48.01781 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 873e75cb-43d9-382b-8106-74e97ea06c42 | -3.95727 | -46.72455 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e934b86e-5249-3615-b9db-16c8820930af | -4.02908 | -41.80165 | 2024-11-23 04:18:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9f44c757-9184-3e44-9631-46a5b09aed4c | -4.36637 | -45.84178 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a144f7a3-0807-32cd-815a-ba27968a9224 | -4.65579 | -45.67189 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 47a3f3f2-4b6a-37e3-8423-19920dd296e3 | -4.45422 | -48.56844 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5934193c-ea94-3b77-8b49-050b60ae68a8 | -6.47938 | -47.50502 | 2024-11-23 04:18:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a365814b-770c-3c98-9a60-c39a075a0e08 | -3.76504 | -51.6839 | 2024-11-23 04:18:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 762b6b7e-f97b-3213-b3dc-2bc14e712e28 | -5.57108 | -46.29218 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd3e1a85-6651-3b6d-9e29-9620be44438f | -3.96431 | -46.72562 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0ff8e94-94da-32d0-a892-0049be32e1f6 | -4.42656 | -46.55753 | 2024-11-23 04:18:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d04d5b3-ff4f-38a7-a3a2-e72961d28485 | -3.99585 | -43.71505 | 2024-11-23 04:18:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c96d05d-1c1d-39d7-87fb-05823a99a549 | -4.25142 | -48.70105 | 2024-11-23 04:18:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 8c51c9ce-db98-32ab-9778-7736928c1063 | -3.24845 | -54.23248 | 2024-11-23 04:18:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 71f31794-5a53-3642-b52d-2049bf1a9293 | -3.89111 | -46.66253 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65e45efd-2df3-36c6-8a3d-c3e69061b0e7 | -4.94654 | -47.80406 | 2024-11-23 04:18:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9663d0e4-8555-38b2-8d96-ae9a68950450 | -3.93647 | -48.15216 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a93be0d5-2580-3788-a9d7-902f6cbb09ff | -3.95065 | -47.9691 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0d5ac0cf-264f-33af-a5e2-4bc23c4edf1b | -8.15474 | -38.24306 | 2024-11-23 04:18:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1f2fdc29-25da-3153-a87b-fb923cb19518 | -2.6844 | -52.07046 | 2024-11-23 04:18:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bbb37aeb-a8e4-3657-b27a-6e74548d39be | -3.77733 | -45.20631 | 2024-11-23 04:18:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b54327df-9ddb-3146-b5fb-abdd3835841e | -5.00833 | -45.50519 | 2024-11-23 04:18:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66093593-5540-36de-b9d7-988e533e558f | -3.2017 | -54.25871 | 2024-11-23 04:18:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 618daaee-31ef-3989-98e3-98ee5e2035b3 | -4.67159 | -45.67075 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d1c4219f-7e08-3a11-8ad3-16b08b45d430 | -3.94945 | -46.90653 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4df230dd-48b1-3677-9006-0e6c890b5582 | -4.67216 | -45.66718 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25c3a0fa-cf3d-3117-b96d-6a7dfd0655af | -3.84759 | -45.28265 | 2024-11-23 04:18:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2345af20-9c78-346b-9131-19d3c2fc253b | -5.11798 | -45.83667 | 2024-11-23 04:18:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f8c5ca4f-4b94-3105-bdbd-44bec657fc14 | -3.75179 | -50.01108 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e87cc27e-ef0d-3c49-ad58-65e1770fc9c8 | -6.91083 | -47.5262 | 2024-11-23 04:18:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 946240a7-dd8b-37a9-b1be-62e597272234 | -3.31031 | -46.66946 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6abd9a9-5ecf-3243-8696-10fe864629e8 | -4.66822 | -45.67023 | 2024-11-23 04:18:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81e27170-d13d-398c-a6c0-68317aa99581 | -7.05004 | -40.41347 | 2024-11-23 04:18:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1aff3bc-cdeb-3aa6-8d89-c93f6d4a2527 | -3.95654 | -46.9077 | 2024-11-23 04:18:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0046637-f26b-302c-895e-66a2b2ae2a0d | -3.24852 | -53.27381 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b826296-1007-35b9-a37e-e1d8068986d4 | -4.41539 | -44.11589 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96969733-5fb3-3c19-8c84-3887ad9aac60 | -3.22209 | -53.93049 | 2024-11-23 04:18:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 445606e7-5ca2-3bba-b0cf-4e19615fd703 | -7.64251 | -40.38637 | 2024-11-23 04:18:00 | NOAA-20 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7ede869c-6056-390c-b73c-e64e2dd3d088 | -5.55429 | -42.71918 | 2024-11-23 04:18:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 28171001-be7a-39fe-9f0e-9d00f2785dcd | -5.9277 | -39.81991 | 2024-11-23 04:18:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4cf8ccb0-e28c-3136-b4e2-8fcd413620ca | -5.94575 | -46.1865 | 2024-11-23 04:18:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7fd0e264-c651-3e5f-8983-ca8269991ff2 | -4.42146 | -44.12036 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf111bed-bcc6-3728-9ee8-0ebeb5f1db0f | -7.19407 | -44.67759 | 2024-11-23 04:18:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3885a80d-42a6-3386-a5ad-8ceda0423364 | -6.40796 | -44.18884 | 2024-11-23 04:18:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83a18624-dc63-3d92-9f54-1df48e4c0a2b | -3.86845 | -51.25845 | 2024-11-23 04:18:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ece6e09-4c40-309a-b31d-89412e1cb0f9 | -5.12109 | -45.15534 | 2024-11-23 04:18:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f7dfb44b-4235-33f1-a023-8b9e1ce3bd0e | -3.67191 | -47.14086 | 2024-11-23 04:18:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88527ca2-cb72-3060-84ce-fe5b5c3864dc | -4.0727 | -46.83964 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404c066d-470c-3b95-8bb2-05f18be772e9 | -6.0024 | -44.63086 | 2024-11-23 04:18:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b441310c-623d-38bf-9691-685954adfc25 | -4.41209 | -44.11538 | 2024-11-23 04:18:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfea4e8e-9f57-35f4-b4f8-90377b92710c | -4.08456 | -46.83349 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c593cfad-d996-34ab-b633-1be9c4c079bc | -7.58251 | -39.84272 | 2024-11-23 04:18:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9251898b-4b70-3b92-94aa-ac67d8a7a2fe | -5.15967 | -47.04132 | 2024-11-23 04:18:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3a2bd24-49c1-3c17-985a-ae55386aeb8e | -4.54696 | -45.87688 | 2024-11-23 04:18:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d4f8d071-3233-3d99-aa4e-e7df5e3c7215 | -4.05541 | -48.32759 | 2024-11-23 04:18:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b35518d9-fdb5-3c79-8d59-e9b1fb75c41c | -9.72467 | -37.03445 | 2024-11-23 04:18:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a84444ef-57a4-3840-b9c6-8b4d76fcb5a8 | -3.79811 | -46.6091 | 2024-11-23 04:18:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 752989d7-ceb3-3b6b-a79d-0d43c6769f62 | -3.24793 | -53.27732 | 2024-11-23 04:18:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README43.md)
