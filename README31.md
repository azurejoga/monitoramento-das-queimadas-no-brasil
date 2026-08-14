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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c86b47cd-56d8-304e-af2d-5500135c31c4 | -11.50454 | -54.61258 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e80de21-dff7-3432-a24a-7e07bfd15569 | -11.5009 | -54.60818 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 144795cc-cf6b-3bb8-8254-70763c11e630 | -8.0234 | -55.11689 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b30e87bf-71c7-3db7-9dbd-fe04f41fc6c2 | -7.60421 | -46.47194 | 2026-08-14 05:18:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 492801d5-b25a-392b-a3c3-4f9f513b65f9 | -6.6328 | -56.26521 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beb1c3e1-97c1-3379-b431-40499057af65 | -6.60707 | -56.3395 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce0eaec8-b898-3ed1-9be1-1bc5e25dde2f | -8.50407 | -64.04065 | 2026-08-14 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1099a75-114d-3f22-8bd9-e10b51eee015 | -6.86477 | -56.40763 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e40042fb-f02c-30de-bf37-df2f7af0971a | -6.83427 | -56.41664 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4cae6473-c437-33dc-a531-cf3a13e7e8fc | -11.06684 | -50.94701 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 954968a4-cf16-3304-9efa-a23c68f581d1 | -9.77382 | -66.61333 | 2026-08-14 05:18:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0162806-6040-3828-b211-472784f097a0 | -7.70376 | -46.2314 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f1938c7-8685-3d9f-b422-647f2f11e1b8 | -9.60046 | -60.51113 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9afcca72-bc83-3ee1-bbaf-a02406f1723d | -11.22989 | -54.82804 | 2026-08-14 05:18:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28dd2c92-202a-365f-9f1d-5884f72b9b48 | -7.71053 | -46.23285 | 2026-08-14 05:18:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0d370125-6cd9-3c31-a9de-8ddadca9ce45 | -6.61639 | -59.04655 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8b23d6cf-8496-3b88-a2f4-38bee74b774f | -6.85808 | -58.95739 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a307d1fb-ca6f-3d42-91a7-d0a9592a2c1f | -11.07787 | -50.94513 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a418a60-b111-31fc-bfb1-87193bdf3436 | -11.06239 | -50.94758 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c8d01c84-8950-33b4-a7d8-ed056f744803 | -6.61016 | -58.99957 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d320caaf-9077-3943-8ff5-ef7c1e4f267d | -6.60061 | -56.33437 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dab7dc6-954e-3b66-9458-9ed421d731c1 | -11.49463 | -54.62299 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 76bda512-c335-3339-bc9a-3a8167706769 | -6.9169 | -45.73575 | 2026-08-14 05:18:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94c91d17-d297-3f46-b6c2-94f67d2c053c | -6.96287 | -59.28967 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8b8a163f-02c3-3342-9d5f-20d990356f62 | -6.59202 | -59.00736 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab29acd5-2b4c-3851-ae1c-b427a325db48 | -7.40617 | -59.9968 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1497220-14e0-3fa0-8c41-fa921f1e303c | -11.50142 | -54.60434 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 663cd756-6e3f-39b0-b719-fa88b6d5e87c | -7.3757 | -59.97422 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58e38e29-2d62-3ad9-bed7-a8725f64124b | -8.95726 | -60.53392 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e749472-e243-312a-b681-633f2d17584d | -11.85982 | -51.95514 | 2026-08-14 05:18:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fa30813-4202-3310-8aed-42f7347cecee | -8.95614 | -60.541 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c068b2a-4e4e-3ef4-956d-b4a7632d7947 | -11.59423 | -54.68303 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3aea343-70b4-38d0-a8ce-40ebebed2741 | -6.59532 | -59.00788 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cd96b26-b27a-398a-a173-089769324900 | -9.08297 | -61.38976 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d180afe5-0579-3d9a-846c-332dd06a66da | -8.55579 | -54.60954 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad5d9894-9b3f-3a28-a9e2-d50149558c1f | -8.55677 | -54.60261 | 2026-08-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d57a296-f578-3e3b-85d3-a11e5d69761a | -10.70847 | -50.52038 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68152225-82f4-361a-926e-1748562020c8 | -6.61585 | -59.05 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53b3f816-0ade-3c9a-b3fd-5ca08483936d | -11.06643 | -50.95036 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc3d094b-1e1d-3086-83e1-7e6f4c6b2346 | -6.59991 | -56.36303 | 2026-08-14 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff9ca8d4-4fcb-3459-a0ba-e6a07a7d6157 | -11.49151 | -54.61473 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce296f64-aeac-3315-bc77-739b1c38ebdf | -6.95517 | -59.29555 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6fc5f786-3004-37f1-8720-9709f8124486 | -9.5999 | -60.51465 | 2026-08-14 05:18:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1acdf9d-0c52-3581-a00f-50f49ef343d7 | -7.58846 | -61.22707 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a64baef6-d8a8-365f-8d83-53e4a72ab148 | -6.62354 | -59.04412 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 23788271-7690-3315-ae5c-4b0e7bce0eca | -9.76795 | -60.76625 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c7fdea6-9304-3fcb-a1c4-dad192ab2816 | -7.58564 | -61.22281 | 2026-08-14 05:18:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f961d57-c7aa-3806-be1b-55e5f61efa50 | -6.60122 | -59.12204 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1772c3fc-81a2-370f-8695-c6fe30d4eaa3 | -7.03897 | -55.50349 | 2026-08-14 05:18:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d8d9faf-fa7c-34b3-9cc3-598a6c85e7da | -10.96922 | -50.54037 | 2026-08-14 05:18:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b0fcb23-ce61-3e89-8f07-e27d76839bbc | -6.70728 | -58.94448 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7248ed4e-7d5f-319c-9541-fe7bdb1e111a | -8.95769 | -60.59567 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7ad32ba-f21b-31e8-8cd2-0df899f9ec60 | -6.71059 | -58.945 | 2026-08-14 05:18:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 124ff8c6-f389-3c13-8a11-275bebbd363c | -11.06724 | -50.94368 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9d140970-ce78-35aa-a955-8820ccdc3c21 | -8.95341 | -60.5152 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46a12d26-dcee-3400-9147-ff576fbf28e5 | -11.97662 | -48.66059 | 2026-08-14 05:18:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6edd221-05e7-334c-a97a-aec84ac5a7bd | -11.59475 | -54.67923 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| daf5ed1d-3166-3b4b-916e-8f4217430283 | -11.48943 | -54.63005 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2a9b0f4b-adf5-32e4-93d6-f59f557363ea | -6.79587 | -58.76693 | 2026-08-14 05:18:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b227a25a-63ee-36cb-8c39-b76a51467f0c | -8.98392 | -60.53816 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eabea7de-c7a3-391c-bc94-660a04c29ac3 | -9.98542 | -53.95514 | 2026-08-14 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 8889e071-9b1b-35ff-a4a4-3d119e16e0e6 | -9.73628 | -60.75024 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5e82aa3-1d7c-3a6f-9f21-c0b70d0d57f3 | -11.07296 | -50.9411 | 2026-08-14 05:18:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90098823-adef-3105-ba6d-14e37c8e81cf | -9.75738 | -60.76818 | 2026-08-14 05:18:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3c81697-2cd2-38c0-adf2-b98f9e07f3d0 | -11.49047 | -54.62242 | 2026-08-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 51eaccc8-96fb-3b61-bc2b-4d8314d64cf3 | -9.07898 | -61.39289 | 2026-08-14 05:18:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 494563c0-4064-344d-a000-0cacbfdcbfd5 | -11.4885 | -54.6273 | 2026-08-14 05:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 85f25bdd-b24b-3359-b20b-c836707f8b16 | -15.3583 | -49.66427 | 2026-08-14 05:21:00 | NOAA-21 | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e64984fc-1cff-3750-a7bc-f03a8432b0e1 | -16.87915 | -54.12848 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aed291cc-8ccb-3dfa-b45f-bad9e883029f | -16.9175 | -54.15292 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0c6cfcf5-ecf8-37b3-afab-08d9690e7a12 | -13.90838 | -53.77563 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ea6dade-c949-32b6-95c4-a2463023a6fe | -14.28595 | -51.97126 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e1dcddf-1db3-361a-bc37-4020fa2405c3 | -12.35655 | -50.89469 | 2026-08-14 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc65aa4-3640-3ae5-946b-3f2307b845b0 | -14.44773 | -51.86428 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a495e85e-f69a-322b-9fd3-a6ef79e21d16 | -13.81492 | -53.81895 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4df5fc63-e3e2-3b69-b123-567364c8f87f | -14.35829 | -53.69179 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63f9f26d-ce1a-32eb-9886-a552de51f95c | -13.82004 | -53.81495 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a2c5dd7-a602-39cb-8029-920e98525dd6 | -14.46241 | -51.91867 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3b721d4-9e9f-31a0-8314-a34980512b24 | -14.29225 | -51.9624 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7fad419e-9611-3800-8460-0e638e235991 | -14.04864 | -53.58707 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d820fc3-02bf-3071-80e1-af0666f007c2 | -14.21746 | -53.35532 | 2026-08-14 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b1c19e1f-0c8d-3f5f-afec-5b9f4f1e0a89 | -14.28669 | -51.96489 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 39aa3dbf-ba4a-32ec-9dbc-61633644e3f6 | -13.75094 | -53.42948 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9b44398-caa2-3b92-9aae-89652f877816 | -16.90871 | -54.14766 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff2b7391-d6e2-3dcb-94a7-beb640c4b980 | -13.2853 | -54.22178 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b077bb3b-8eb0-3cbc-bcf0-48c21a53c790 | -12.3515 | -53.13804 | 2026-08-14 05:21:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1e7bac6-7909-3467-94f6-b587e7b9d8b1 | -18.54837 | -48.18381 | 2026-08-14 05:21:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a9afe03-e6fc-3ef8-b3c0-3ea830461157 | -14.3587 | -53.68402 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37e91023-8f8e-3ed8-8f39-a05f1934fa48 | -15.1679 | -50.05181 | 2026-08-14 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dd1f7dd-7f1d-3d94-8242-842d96906686 | -13.82175 | -53.80119 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6ed5423-7fbb-3262-ac1f-48d6cb2c09c4 | -13.76084 | -53.42599 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e552d65-05c8-39f2-9999-d917cc9333db | -15.50751 | -52.99966 | 2026-08-14 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60070519-3992-3348-874c-ad070dd25018 | -13.76025 | -53.43081 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 780a0f37-686e-3c29-ac35-1d35adaab70b | -14.09807 | -53.6434 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5930838-3385-31db-b599-4ff336c33748 | -16.91338 | -54.14796 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf4d12f5-2c41-3dbb-8ac2-3618c5497d2f | -13.8229 | -53.79192 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51678524-6867-3e59-9342-0339daa1041e | -14.4628 | -51.91544 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2affcc60-ba5c-31d0-8f54-fc157043a74a | -13.92332 | -53.95963 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 416af745-19e9-33f9-abc7-368fa93fe66d | -14.07619 | -53.6307 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e62f755-97ee-34e4-8d62-139a5d63cdb5 | -13.28206 | -54.21241 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README32.md)
