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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f61efd7b-b5ef-3acb-9405-d6d23d9f3b25 | -7.22928 | -43.59088 | 2025-06-14 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa3f98f0-652e-35b7-8b7d-e85d88c4c04b | -9.56401 | -50.77721 | 2025-06-14 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c8b6317-f604-37c8-af68-d9a6aca75ce2 | -9.85809 | -48.20167 | 2025-06-14 05:04:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbe90451-f0fc-32f7-b4a3-bb09dc4e10c5 | -7.4605 | -45.50607 | 2025-06-14 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6b010a83-57ff-3abb-b5ff-7af962f1da3f | -8.72625 | -47.99482 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b3dea7d-e12d-3442-828d-48989999b3f8 | -4.3381 | -55.77791 | 2025-06-14 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3095f76f-8bab-3b3c-8059-e77cfb226228 | -6.96038 | -42.80958 | 2025-06-14 05:04:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2cef9206-8127-3011-95d8-cae6f799d860 | -7.2314 | -43.10879 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0ae9cfa8-2166-3349-9c24-39f1dee244e1 | -7.22347 | -43.58413 | 2025-06-14 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 83a3e0a7-fcd7-3292-bca0-df107e4793e0 | -9.56758 | -46.74057 | 2025-06-14 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddfccf46-db01-350b-b79c-87c42e76b623 | -6.60503 | -43.89782 | 2025-06-14 05:04:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 8666db3d-4d84-3f63-b439-d662c93c0d2b | -5.91417 | -43.46185 | 2025-06-14 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 508a1c29-bdc8-31f8-ab10-c3db8c755e01 | -9.40737 | -50.42072 | 2025-06-14 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f6ae9d1b-2b87-3a55-91a6-6fa17e9087ed | -8.92192 | -49.84616 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3bd7a570-3dde-34dd-bf93-9fd0d5eaa8be | -9.84449 | -44.69346 | 2025-06-14 05:04:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7ccaac5-4411-3cd1-b9c3-d503a6dbe6b2 | -8.07685 | -43.10458 | 2025-06-14 05:04:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 637621bc-0ae1-39c8-b58a-74d3344e313e | -6.9488 | -42.89845 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 3a047e24-39ed-3578-aad0-3826b72da56d | -9.71648 | -48.61608 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 36e5fddc-0d79-3acb-adb8-bb25a31d93d2 | -6.95659 | -42.89865 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 8a9ef435-18d9-3222-8b8c-7b690407e998 | -8.73171 | -47.99262 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4eb4f78-52eb-313e-8cce-93754c815eda | -6.95644 | -42.89335 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 28b5d350-dcc5-317a-b38f-0d642f3da7c8 | -9.40951 | -50.419 | 2025-06-14 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c3aa975-63e2-38bc-8b85-829fd5237158 | -9.53743 | -46.29983 | 2025-06-14 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 498711e6-e13b-33c1-a54b-d880dd8456f3 | -7.21786 | -43.10659 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bf25c542-b7e3-36d4-921f-cd98c26caf59 | -5.88639 | -44.35621 | 2025-06-14 05:04:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96a5189f-666e-3517-b44a-6e9f48b5c0a9 | -9.53168 | -46.29911 | 2025-06-14 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20d5f8ac-34fb-34bf-bb61-66c9700d2384 | -7.45993 | -45.51037 | 2025-06-14 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a9cf9139-eb16-3a73-8d3b-664aea8a1c74 | -8.92577 | -49.85124 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8b162dd-0f1d-3d38-ac1c-4e054a578a2c | -5.90182 | -43.45459 | 2025-06-14 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7c69ed4-158f-3a5a-b475-e3d3c1e4864a | -5.77278 | -43.4783 | 2025-06-14 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e484866c-cf06-3b90-8d4d-7e537783b8d2 | -9.40691 | -48.40898 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 902f1f55-1c7a-36a2-82e7-2ffce93cedbc | -9.4111 | -48.41554 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9a78cea-e661-35e9-b03a-1514e757b552 | -8.92129 | -49.85065 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1dc5493d-cdf1-31f1-a8c9-6d6173c9e93e | -7.07458 | -43.55441 | 2025-06-14 05:04:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88e7f486-ae62-3a39-8d4c-d88627a7be6e | -9.40614 | -48.41484 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 15290b66-3799-3bec-8744-5f4465440790 | -9.55979 | -50.77658 | 2025-06-14 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41881616-16a3-37ff-989d-36817f9578a5 | -6.9496 | -42.89229 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| eb075fee-906a-3ade-a012-69eb862dc3a3 | -8.91745 | -49.84557 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fda3d3aa-5ae2-36a8-98d4-c425b22ece0a | -9.57265 | -46.74513 | 2025-06-14 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d0f8d35-8017-3fcf-b467-8c04082e4189 | -9.71157 | -48.61528 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8cf1a06-5593-3247-a65e-710df139632f | -6.95737 | -42.89241 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 59f13a16-e774-3200-a3f9-57ce15850360 | -8.91682 | -49.85008 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3818006f-e146-38da-a553-d764de62afed | -9.4004 | -48.41995 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67aebf7c-50fc-3a10-89b1-4b1d24966589 | -6.95042 | -42.88601 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 1233111a-a2ef-3f8d-a746-b3058734609e | -9.53043 | -46.2972 | 2025-06-14 05:04:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f7b1966-cf2d-32e2-bed8-2108e7b3ffa9 | -7.45407 | -45.50945 | 2025-06-14 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43029415-f526-3d61-aa81-a4348bd7dddb | -6.95563 | -42.89953 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 1dc8ab9c-e155-3cf8-9f48-b61632359ce7 | -6.21667 | -43.32783 | 2025-06-14 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b607fe5-ca6f-3bf1-b714-5c53b1447ccb | -7.239 | -43.10342 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0f44a47b-849a-3b8c-a89b-b03faa1bf25f | -6.21592 | -43.33358 | 2025-06-14 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 330e04e9-ac16-3d49-97b1-14965c06e106 | -5.90257 | -43.44908 | 2025-06-14 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3edb6b9-be94-33f5-9423-23aebc0044b0 | -7.45464 | -45.50518 | 2025-06-14 05:04:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3f3b1e14-8a74-3965-ae51-45da8f3adfc0 | -8.5614 | -50.07698 | 2025-06-14 05:04:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3cdd882-4479-3cc3-9732-ea14f5a4afbd | -9.4046 | -48.42641 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 893282bf-1b04-34c2-beb2-593ef771b04f | -9.55798 | -46.76497 | 2025-06-14 05:04:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82f7ddea-ca87-3226-94df-1cec9a51d888 | -5.77929 | -43.47931 | 2025-06-14 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 464dffe0-d98f-3654-8f10-e6c181b79639 | -6.5993 | -43.89169 | 2025-06-14 05:04:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 767958ac-5376-3199-9fc2-62a15183da42 | -7.22463 | -43.10771 | 2025-06-14 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6f5e284d-3d72-3f67-98b7-ebbe36fc630e | -9.40796 | -50.41656 | 2025-06-14 05:04:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db5ef410-6125-35bb-b21c-665b0b6d0b88 | -9.39965 | -48.42566 | 2025-06-14 05:04:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8fc56f81-1d00-3ed3-8c28-8a6782e5356b | -11.01341 | -55.09072 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bfff9e3e-f40f-3a52-af4a-0a3359d7b227 | -11.91303 | -57.47278 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a68c6ddf-583a-3e8a-aa62-48ca86c6723a | -12.59634 | -47.06928 | 2025-06-14 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 785ccdbf-9ee4-3a0e-b3a5-401b139f96db | -10.92459 | -56.83222 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09b1435e-f399-3c33-b9a0-6ecbfe4a988c | -12.61339 | -57.8873 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1277945b-a536-39b1-8082-198864f76c88 | -14.21283 | -57.40849 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 27b5d9e7-7d48-3562-86a0-b6962ecf2211 | -10.29716 | -60.54801 | 2025-06-14 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33c3713a-3062-3848-9f71-83cfb51cf5ef | -9.25179 | -57.53389 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c862202-6325-39c0-8c76-518f93f26835 | -10.07346 | -52.74393 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7d7972b8-3916-3e45-948d-b8299a78eaac | -10.93946 | -56.84532 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9c044e09-325d-3068-8078-ec1817790999 | -10.24133 | -52.23508 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3afe7fd4-93b3-32fe-8cb6-4cf6c98435c1 | -13.90072 | -54.6138 | 2025-06-14 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6371aa81-d0f2-3f63-9f70-e95a824f0129 | -11.81564 | -54.5011 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d6647af5-12a2-3166-a4dc-098f755a9e7b | -15.39919 | -47.86545 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d53ab78-7a94-3dd3-b093-973eb82d2ab7 | -14.0372 | -55.13744 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6fc9fa8-4567-3ffe-bd76-223f73c0f498 | -14.04069 | -55.13795 | 2025-06-14 05:06:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e5b5f93e-dbcb-3ad3-8141-331f7378f684 | -9.46769 | -57.84667 | 2025-06-14 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe1cd1e0-06e5-36b5-9a96-65b746f4fbef | -12.569 | -57.76059 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15b767fb-276a-3c16-b979-79d837f063ae | -13.72234 | -58.67974 | 2025-06-14 05:06:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 01f65cb6-75cf-3d13-bf99-72ade68590d3 | -10.93286 | -56.84427 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| ac9144f7-94dc-3130-8b03-a1378768797a | -10.23993 | -52.23745 | 2025-06-14 05:06:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c26ccb4-0bbe-3afe-be49-b41b77d4c128 | -11.80252 | -57.35432 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a370db11-d049-3559-8ca0-3d294f75da58 | -16.20189 | -46.46623 | 2025-06-14 05:06:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1985c0f-d376-3cca-a4ca-03d20a3d57c5 | -11.00571 | -55.0904 | 2025-06-14 05:06:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e9d6c2ee-02a0-3794-8fe0-6b8b060cd906 | -11.98411 | -51.61247 | 2025-06-14 05:06:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b16e49d7-ad33-3309-a958-905d398e91dd | -15.3988 | -47.86907 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dad540d4-1d7b-3d1a-a823-35804d2dfeae | -10.366 | -57.22792 | 2025-06-14 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05f67999-a0e1-3435-878f-81e8bfe54118 | -12.61613 | -57.89137 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21f819b1-77a7-36b1-9ceb-cd06e59653f3 | -15.39843 | -47.8726 | 2025-06-14 05:06:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df8b0ca6-705d-3dde-921b-e5b2dab20fd8 | -12.28224 | -57.26695 | 2025-06-14 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db82dc27-746c-32b3-8fa5-6135f29a99a6 | -14.67197 | -53.38513 | 2025-06-14 05:06:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 501f014b-7216-3672-93d0-eae35bf7823c | -12.10964 | -48.87172 | 2025-06-14 05:06:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 333f1cce-c9d7-32d6-b32c-fc4f3800206c | -12.59593 | -47.07268 | 2025-06-14 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79b7758a-8a7c-3516-8274-9bad300772ee | -10.85202 | -46.71116 | 2025-06-14 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 139c70f1-7087-34a4-85ed-a2db59a28e1d | -10.10045 | -58.22705 | 2025-06-14 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 048bae23-74c3-300b-94f4-99258ad91b6e | -12.62275 | -57.89246 | 2025-06-14 05:06:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c9158fd-5ad2-3ab3-94b7-090b4b1d35a1 | -10.91703 | -54.77271 | 2025-06-14 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5b4b1e79-1a5c-3ed8-acb6-24e489af54b8 | -14.68551 | -53.3722 | 2025-06-14 05:06:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b11ac446-c944-3576-906f-24777988560b | -11.5697 | -54.57523 | 2025-06-14 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74ae8429-e61b-3b66-896b-2608e0f44c67 | -11.89785 | -47.46367 | 2025-06-14 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
