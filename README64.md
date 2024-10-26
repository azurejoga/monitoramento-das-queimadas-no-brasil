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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eaf4473-8986-3599-8114-1786bf4245ba | -1.02193 | -48.07292 | 2024-10-26 04:42:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 11de54a6-4f89-3f3d-b7b7-530b966e4ba1 | -1.0191 | -48.06875 | 2024-10-26 04:42:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99b4580f-8a3c-3a9a-9612-00242c3ec9b8 | -1.01853 | -48.0724 | 2024-10-26 04:42:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dd853ae-d362-3ebc-a897-120829137516 | -0.88942 | -47.88768 | 2024-10-26 04:42:00 | NOAA-20 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1ce96fc-d2c0-3862-9334-a24d67792e7e | -0.73583 | -48.04066 | 2024-10-26 04:42:00 | NOAA-20 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbfee6f6-e12f-317e-9d35-b03be96d4b18 | -2.10786 | -47.69664 | 2024-10-26 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06adade3-4c66-3733-accf-b97d3e14824c | -1.534 | -47.29135 | 2024-10-26 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 563507cf-c1b3-352d-8dbc-2d44b3b64264 | -1.53048 | -47.2908 | 2024-10-26 04:42:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f448126-abb9-3d1a-ac7d-d9e01d48ea5a | -1.53002 | -47.20184 | 2024-10-26 04:42:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b30c5523-a20a-3cbc-8d03-69e31548d1ef | -1.5294 | -47.20579 | 2024-10-26 04:42:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dbece41d-e09d-36da-bd8d-b7ddd1223ced | -1.05461 | -47.642 | 2024-10-26 04:42:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b65379b0-3930-3601-9bed-f4d552b5c965 | -2.05144 | -48.68352 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3487b4a3-69cf-32e9-92fd-7db71aca3e9b | -2.01533 | -48.51663 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b9eba5b-ba05-3ff5-be56-652b99d52380 | -2.00545 | -48.52641 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09652af8-93f8-3a1c-8085-27d00fab31b8 | -2.00489 | -48.53 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d2b63ae-5aa9-321b-812b-9a4a54f14acf | -1.97729 | -48.68322 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44707dae-0acd-3a20-baed-3c6748a7d92e | -1.80554 | -48.62378 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a7d5eee-1984-3ca7-8675-9fa277b4a818 | -3.48657 | -48.24542 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c3da1b4-5423-346b-b36d-6ea360e60140 | -3.48313 | -48.24486 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1624cab7-9d8f-3083-894c-66174b4c6ad6 | -2.97203 | -47.99114 | 2024-10-26 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4808e583-e164-33b3-b310-f14387e3f740 | -2.89349 | -48.27563 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| feb74e96-d667-39ee-88f0-68db67245764 | -2.89117 | -48.29046 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1b2af1e-548f-37a3-9b8a-42b2e390b625 | -2.89006 | -48.27511 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fbeadcd-ea9a-3689-acd4-7c7be7293d82 | -2.88833 | -48.28623 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 19b4ba48-2a71-3563-ad05-0124ce8d361a | -2.88775 | -48.28994 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4c0e45d2-a3b1-3c41-93c5-2fb9cdb1b8c6 | -2.87628 | -48.61398 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61e71e9e-a907-3eda-9ba3-fc3ee9fce343 | -2.85447 | -48.45818 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41949dbb-d770-3e5f-8420-bec02175a854 | -2.77809 | -48.56948 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddcf43f8-3907-307c-8f08-8030d38bac30 | -2.74621 | -48.70874 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 532fb530-9051-3cf6-8a5f-6b8abe1a87a5 | -2.74565 | -48.71234 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70b52449-6922-373e-b634-cc62a1a65020 | -2.70173 | -48.29177 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe5a6ec2-1b3f-3f0a-a1c6-de405a619149 | -2.68945 | -48.64096 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b275a265-79dd-3f2d-93af-34a167b896a4 | -2.68607 | -48.64045 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56c4ef5a-1279-3cb0-a3ef-e2ea80cc0e90 | -2.6188 | -48.53104 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76cd0cfb-c88a-3e5d-9ec9-ac63968be818 | -2.57638 | -48.44634 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e7e2b3d-2666-38fd-a046-60d3a0019856 | -2.57582 | -48.44999 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 030df995-1719-330b-b1a6-2d13aa0a4a23 | -2.56938 | -48.12831 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30e1beed-eeb4-300b-99b5-db9cba1a485a | -2.5688 | -48.13203 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91c50891-6161-3571-b89e-46fb789866fc | -2.47605 | -48.05326 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4eefc8f3-4673-3020-9136-ef24af1f6ae6 | -2.4732 | -48.04898 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c71b1245-0427-3b0e-9119-239f37181822 | -2.47262 | -48.05273 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61325fc9-6d2d-3b02-8d27-7b56e3b88800 | -2.44396 | -48.39261 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf2979c2-02ab-37c2-93ff-4b79c5aad0f2 | -2.44338 | -48.39626 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 824c24d0-7c8d-3782-8d6c-bdf366677643 | -2.43989 | -48.46279 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d4ad4f-684f-3e9d-ac06-320f1e32db02 | -2.43707 | -48.45864 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54a2dc4a-f79a-361d-b5d9-4f4eeeb137dd | -2.4365 | -48.46227 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8dba16f-8162-3612-a21a-4057ec0d86be | -2.41846 | -48.3999 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b39530f6-7e37-373e-a17a-299f1dc4cefa | -2.41615 | -48.45914 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10514bb7-8334-3a2c-b118-636160c754ba | -2.41275 | -48.45868 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e484568-aa07-33d7-a9ed-408841e38863 | -2.3958 | -48.54501 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c6e2d65-e163-303f-a58a-792e9a54a7f4 | -2.39241 | -48.54449 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9868690-02dd-3e1e-ae1b-88ab84407d9e | -2.36856 | -48.29107 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d990226-ec25-339a-8b01-c3bfa7f804fb | -2.36515 | -48.29055 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 33113687-f43c-310c-9d71-1448058506f1 | -2.32803 | -48.43811 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5071e18-580a-3f7e-b5c2-f36381022cc2 | -2.32464 | -48.43758 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9aa51c93-df43-3270-802d-ebf77a8a58cd | -2.31749 | -48.23808 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b6be278-c6f5-3a98-b85c-8621c129b81b | -2.26991 | -48.07193 | 2024-10-26 04:42:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8cea5a5-4683-3f92-8825-c797a1f7cc98 | -2.17509 | -48.56646 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eff795b1-3dab-3fa8-ab5e-a51e24199f44 | -3.45819 | -47.6736 | 2024-10-26 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 795b06fb-eb5e-39a9-a0ad-6e579338e37d | -2.66778 | -47.40235 | 2024-10-26 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ed1094d-59c2-36da-b42b-d76853938c46 | -2.66423 | -47.40181 | 2024-10-26 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7863627d-2918-36c5-81cc-2ae629660fa8 | -2.51303 | -47.58544 | 2024-10-26 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f0df8598-4ad4-36a5-bf37-806c9905c82e | -2.34551 | -47.4971 | 2024-10-26 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8c1f60b-2775-34a3-aa91-77d44e06c90c | -2.3449 | -47.50101 | 2024-10-26 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a2fbbd0-6a53-38d8-a769-25db73c6fcd2 | -2.3443 | -47.50493 | 2024-10-26 04:42:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb5cbfac-55a2-340d-8486-c4195587343d | -3.11902 | -48.65105 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c5a740b-aca8-3d11-9e6c-794056f373e2 | -2.95101 | -48.94516 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35a594c7-5877-3570-ae1b-c48efadd361f | -2.94852 | -48.61766 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce2fb4db-9444-3efe-9eda-76f03a5290ad | -2.9456 | -48.74659 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa737e1-a1d0-3194-ab64-ecfa2f7326a9 | -2.92141 | -48.95879 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c65441f-b4e8-39f3-a66b-e992744a50b2 | -2.79061 | -48.6898 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67b464aa-c0c7-347b-a740-3f948cc6f32f | -2.77865 | -48.56586 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2281de5-5342-3a84-a4ef-6b924e4e1ef1 | -2.74903 | -48.71286 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e463ea4c-ae3e-347f-adbf-fb98c6f464a0 | -2.63854 | -48.56004 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d06a20a8-cfe9-3538-a0d2-f5bd9752da82 | -2.61937 | -48.52742 | 2024-10-26 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adc16cd5-c48e-36a0-a161-f412b3739ac5 | -2.44503 | -48.61512 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96bab5ca-041c-38b1-8cde-a669ee9404a4 | -2.42525 | -48.85354 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54f87b93-6676-3079-9077-3bfaee5772a7 | -2.24397 | -48.5326 | 2024-10-26 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d8f8157-7cb6-3851-b47a-b2c1a065bfa0 | -2.19625 | -48.81809 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 0ab345c9-e412-39b3-85d7-227a45fcc660 | -2.1957 | -48.82164 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0cb73bc2-8cf0-3571-99c7-572a721021cf | -2.19289 | -48.81758 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 015ad295-d003-38cb-b8d0-dfd0f95e7a74 | -2.16953 | -48.82134 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc98f74e-60c3-332b-841a-f84b715cce34 | -2.16898 | -48.82488 | 2024-10-26 04:42:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 244579bf-c2be-35eb-8ffb-814a7de0c784 | -3.9353 | -48.35802 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aaa148f7-4ff0-3c11-857b-da86e2da5a6a | -3.93472 | -48.36176 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a65bd0c4-d207-3fd4-8a3d-cc7fe722e506 | -3.93129 | -48.33826 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a56a1fd-60e5-353a-b5bc-13a6b3d68b8d | -3.93071 | -48.34202 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6fe73b05-1da2-3d6b-b056-412522b2c887 | -3.93013 | -48.34578 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6bc40be8-f290-3fd0-9daf-2f0e9a0469bb | -3.92785 | -48.33773 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fbd820d9-4bcd-37b0-aa2b-a755663db26a | -3.92727 | -48.3415 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4417f933-0fb0-3798-9e59-ab85f8ce262c | -3.92669 | -48.34524 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 483c2134-eefb-30d3-9f20-ff44dfc2d27c | -3.92383 | -48.34094 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8759e710-403c-3dda-8868-fcd3a8c6f72e | -3.91193 | -47.94418 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7f2e3ba-f53c-382b-b21a-654c8586956f | -3.90947 | -48.36558 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e65c066-704c-3701-8f2f-012a48e0a8fc | -3.90889 | -48.36931 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 35c9e0a6-c36e-31f1-b63f-4dc67b3ebfe5 | -3.90783 | -47.94754 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08b96e0c-6e2e-3216-9811-689a52347afc | -3.90723 | -47.9514 | 2024-10-26 04:42:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85988e47-6929-3da9-a29a-bdfac95348ac | -3.86746 | -48.36703 | 2024-10-26 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fffeef17-f98b-3ce7-a250-62d7841207a2 | -3.83183 | -48.89214 | 2024-10-26 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e04cd699-6912-347f-9d9b-ae0e5ef81948 | -3.82845 | -48.89163 | 2024-10-26 04:42:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README65.md)
