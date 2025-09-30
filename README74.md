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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcd6b0e4-6ff3-3041-bf06-e96ace417e93 | -14.68643 | -48.17109 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a1a5ba5-4b3b-3f1d-98a4-34c8177d66bc | -15.27178 | -49.26691 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a3ec8ba-8f57-3abd-9f86-9070a6931b26 | -15.19861 | -50.18753 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7e261ee6-7357-3f6f-9e8f-cc250e4c5c64 | -15.39907 | -44.97717 | 2025-09-30 04:42:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5730813f-fd04-3da1-ba90-a5fef806d911 | -13.76597 | -54.7365 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8448e3c5-9a61-3a56-872c-69992ed92835 | -16.38885 | -47.03829 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10a96fb6-d5b6-3523-86a2-2308a0ef90a1 | -14.51474 | -48.43135 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5034752a-4d71-3e15-aea9-f3d4524ff045 | -14.30116 | -57.76241 | 2025-09-30 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3b4d70a-b5c5-3125-8e63-1e916f8c7f05 | -15.27983 | -47.86337 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 90ed0f3c-e268-3b00-841b-70f2f5337d4a | -17.70679 | -46.66132 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5f8e9ce-1459-34d1-a492-6f7828c80249 | -15.71553 | -59.52087 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb83551d-56e6-3408-aa41-7248927d71cb | -19.73516 | -49.65398 | 2025-09-30 04:42:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8ebe6585-037e-36ea-91e3-820a0b1187d8 | -14.56949 | -48.22942 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bdbfe2d5-c6e0-31e5-b069-7b5858bda605 | -20.62406 | -46.17897 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aaed8d98-0e96-3501-b03a-8678ac3daf8a | -14.51415 | -48.46057 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9cd34e55-5936-37bd-970c-caab3ed0ef2f | -15.28031 | -47.88638 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0f248771-584b-30de-99bf-d82ee748cb1b | -17.70946 | -46.66833 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad9f74dd-9dfb-3a8b-b6be-5b28903bedf0 | -14.81402 | -48.76136 | 2025-09-30 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e099039-ee7b-31bb-b06d-da15384aaff6 | -15.59307 | -53.13734 | 2025-09-30 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 141509cf-e840-3e99-8dce-8e198c13417e | -19.86386 | -44.56295 | 2025-09-30 04:42:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 7415ab95-83d9-3afa-b41f-4026e3d39c60 | -15.26214 | -49.71361 | 2025-09-30 04:42:00 | NOAA-21 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e160f3f8-a342-3b2c-a878-d3b551b338b5 | -16.42376 | -47.0165 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7335037-2817-36b8-8ccf-6b9d1356c4a4 | -14.67205 | -48.14292 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a24e1e34-f7c5-3abe-b0e5-d078eeb10144 | -15.84348 | -54.97234 | 2025-09-30 04:42:00 | NOAA-21 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1bc5ed24-e3b4-3177-8af3-f843b28a7275 | -15.1283 | -48.38293 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d47f0a07-7952-330d-9fbd-8826efeedd4c | -16.41632 | -47.04232 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5a23aac-ab47-32d5-8ff6-d8ec2698bd40 | -15.97728 | -57.23563 | 2025-09-30 04:42:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dfad8780-5e4a-31ff-8e1e-a243a260ce3b | -15.28377 | -49.49442 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df0f8c40-6daf-3ab4-b0fb-de36d52dbb17 | -14.57011 | -48.22517 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3730d8d2-3825-3652-b556-e26f71f2bb52 | -14.51889 | -48.45292 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4a1ff89a-e2bd-37d9-a01d-6927e9cc4276 | -17.39663 | -47.12919 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 332bcd3c-f822-3d95-9e42-1ae9d58d1b25 | -15.90989 | -46.22474 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5a2ffd84-0788-33b6-a431-1090bacca720 | -17.73353 | -46.67563 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa275384-8e45-3e0f-93f4-40f43117d37c | -15.3008 | -46.40873 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb310cff-f5e3-3249-8d11-825bb75dfdfc | -15.28176 | -47.84979 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fedd8958-43fd-3057-8383-281941b3d050 | -20.22991 | -41.34293 | 2025-09-30 04:42:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 3371239f-f17b-3d0b-a082-b152626f71f7 | -18.1235 | -42.1922 | 2025-09-30 04:42:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 301b1496-b0e7-3d4e-ab29-dc744e952064 | -15.20197 | -50.18804 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6164ecb1-668d-388e-ae9c-6fa7803d8afb | -17.4134 | -47.15461 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e69d87b0-5aea-3de4-a474-47885e8f746f | -15.85519 | -46.22752 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f9b340d-5f0b-3a3d-9a71-5d16bed2c73f | -15.27968 | -47.89079 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 54e036f9-3012-35dc-98ed-4f67e2a55c1b | -19.86339 | -43.8158 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b2d3b0a-0d69-3a77-b16f-87e6211bc622 | -14.70672 | -48.16842 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0990ca67-2b02-3ec1-92ca-aee1d7c6c280 | -15.27349 | -49.25525 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ce5e84e-2a91-319d-8c6b-749688ac1663 | -15.72386 | -47.59637 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d184ca97-4f05-3072-8e30-7e2d9ee60f67 | -15.276 | -47.89023 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 140ad98d-8aa5-300a-85ad-6a2c34a08872 | -14.5371 | -48.25071 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06c3d881-bb45-383e-a234-8309cdedc878 | -14.61306 | -48.29889 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 532e98d9-7717-321d-ba94-77750d4eeb4d | -19.33651 | -43.81444 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d702a71c-0517-3d87-b0b0-d25cb78b8e3e | -15.93402 | -43.30968 | 2025-09-30 04:42:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67b0274a-3062-3f68-b757-e69ccd261a97 | -17.3977 | -47.15155 | 2025-09-30 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cba83feb-74c5-3b56-8919-743c01d6084b | -14.55428 | -48.48232 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 45c8fb5e-ee66-35d7-b543-27d8130c1592 | -13.73311 | -54.73079 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a0c55d2-911e-3dee-8706-83e4a7a84c30 | -15.91765 | -59.50012 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5d2b4445-76b9-350f-8867-f488965ea812 | -15.72251 | -59.5102 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a634e9a-dbb1-3165-8acb-3b885f80b349 | -15.2483 | -56.83515 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 430c0643-3438-3011-9fb0-c0017a1a64cb | -14.70961 | -48.14785 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5c419744-aa52-3819-9693-fbe89d06bf9b | -14.53534 | -48.23742 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc8a620f-e254-362d-a2e8-473616e01229 | -14.55131 | -48.47775 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 09def07c-390e-3583-9452-8e551fbb197c | -15.1767 | -46.40687 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09c09b02-e3f7-3ea7-9504-90e35f242b80 | -15.25612 | -56.79113 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6223cb39-e0d5-3042-b519-5e04ad537995 | -14.70369 | -45.70179 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f46fb95-20c9-350f-b9dc-ac0a4eae87d6 | -15.2457 | -48.75242 | 2025-09-30 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6a81a0df-6c1d-38b7-85ba-8faf9505b332 | -15.30481 | -46.4094 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f104cb9-a05b-3248-8c0f-39aadcc45422 | -19.55796 | -44.95318 | 2025-09-30 04:42:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da328cbc-bbf1-3c72-9901-084a872ac00a | -14.5177 | -48.43606 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc5e7d2b-86f3-3791-9ba4-a62bba8aec8f | -15.27696 | -49.49305 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd5bb9b6-1b57-3d03-b53a-9fe63a312c33 | -15.68501 | -46.26237 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2947b38d-bfc7-3cb3-ba27-66c23625c989 | -14.70668 | -45.69997 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e2e19a9-889e-393d-8385-88f0791ff6f9 | -14.52655 | -48.47504 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f4769fb-4b10-3a2e-b6ee-0c2083148b95 | -14.56314 | -48.47095 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c93e98f9-f569-3121-9a96-89c7b557d72e | -16.06826 | -51.04128 | 2025-09-30 04:42:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ea180d4-a370-3151-9a96-c5370d522211 | -14.70729 | -48.16441 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4d3f1907-5ff2-36c8-8c68-851501c37fc1 | -16.00906 | -59.51493 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 712e276d-a87c-3365-b356-7dacb1dae519 | -20.28677 | -46.23416 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d70417b8-571b-3030-a616-e378d12951d7 | -20.04689 | -41.33041 | 2025-09-30 04:42:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 57f9528c-c0c4-355f-bddc-68f5f5e72957 | -16.42768 | -47.01716 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f0a1eed-4169-3c90-b592-6a91381814e7 | -15.46551 | -47.92253 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10fdbd9c-1613-3fb0-8892-26dcf4a6ba99 | -20.06981 | -46.7915 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4db3786c-8eda-34c2-a0ce-0a47569f3c9d | -15.92023 | -46.24133 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9ca6cf2a-cd8e-3c33-abec-8cb5b965b229 | -14.52303 | -48.44933 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b05ad4c2-b171-3e62-984c-7ec16ee5a1f2 | -16.35417 | -48.16051 | 2025-09-30 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b7ed9120-d5dc-3e08-bd40-4f3c88b9414b | -18.91097 | -48.06982 | 2025-09-30 04:42:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 74b660c8-54d3-31f0-b711-92e0c8bb2ac6 | -14.59636 | -48.28763 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef2ec49a-569e-3496-9585-9b63970e502c | -16.61547 | -43.35939 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 857ba9f6-03bc-3e61-8023-d15489ddd210 | -15.49128 | -48.55428 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fcf9507f-311f-304a-ab09-c825746d5da1 | -17.70537 | -46.66773 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91d2e468-4933-32c6-beba-c06ded7331ca | -17.92121 | -57.60097 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 04ed09a8-0ebb-3ba8-9a5e-4ecba1a0bb0d | -15.28162 | -49.27206 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4175a2ce-4d96-3114-a279-08c2f8d5a6e1 | -20.6201 | -46.17472 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 203c326e-2632-331b-b03e-4f5577dc3b77 | -16.74069 | -44.92678 | 2025-09-30 04:42:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5174ab58-c2e2-3edb-8aca-1486323ba5c5 | -15.26898 | -49.49967 | 2025-09-30 04:42:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02c43a01-888e-344b-b129-bec6fd423c0d | -14.78851 | -48.30656 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 834113f1-a041-38f0-a8bf-8b130037e5d7 | -16.23172 | -41.72911 | 2025-09-30 04:42:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ce0a25d-3f4a-3842-a560-bca0a960ba9d | -14.58918 | -48.28674 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1778d07b-cc52-3ecd-89f2-ddb4d24ea665 | -13.73385 | -54.72646 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c682f078-94b2-3d33-8fd6-83172d20e5be | -15.20252 | -50.18437 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 663f1307-6aa9-3868-a510-3000b50c9922 | -19.85013 | -43.80867 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5ab5d355-a4c6-3a2f-9ade-9336bb66039a | -15.11974 | -46.45427 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5deb2d59-61da-3a5a-a38d-0e03561b9a52 | -15.28305 | -47.86126 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README75.md)
