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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a16a3d0-a885-386f-a01f-6fd45f9260c6 | -12.57102 | -53.06483 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| ed7cc37f-c8ea-3cb5-8d01-43742224b021 | -12.57026 | -53.06929 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 29568275-92ab-3369-96b3-5748728a243b | -12.56731 | -53.06418 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 18d33df1-b622-3c53-9fc9-b039b7e99f2e | -12.56656 | -53.06865 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 590ccee3-415c-3afe-8d7c-babcc404c549 | -12.55618 | -53.06225 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 783023c1-955b-36cb-857e-484287f8922c | -12.48781 | -53.14835 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f10705af-b332-3263-920f-cedde8d50d93 | -12.48408 | -53.14769 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3128145f-5ec7-324b-b0eb-f83b9c00d111 | -12.48036 | -53.14703 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07f8fe2e-cc60-32b9-b1f4-d86199b694d0 | -12.47741 | -53.14187 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fb719b4-e0e8-3b86-a924-537102cc9786 | -12.47663 | -53.14638 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f12daeb-7f28-3adb-8adc-28cc93a626e1 | -12.47478 | -53.17911 | 2024-10-08 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84c1acd0-f2e3-3307-97f8-7d0d8600b013 | -11.33382 | -55.23077 | 2024-10-08 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c547c2c-d4c7-333e-ae86-8daa5d70678d | -11.33179 | -55.23173 | 2024-10-08 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de755e4b-196c-33c0-8955-76fa4e4b635c | -11.3295 | -55.22995 | 2024-10-08 04:34:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b67a6614-5534-3017-b762-1e9d51d25577 | -12.44651 | -54.45392 | 2024-10-08 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a51b4a6-bc86-3960-bc13-83a16de6de3c | -12.44589 | -54.45749 | 2024-10-08 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fd9b788-a787-309b-bec3-9d5b48733cff | -7.97741 | -54.78413 | 2024-10-08 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cbf4f88d-8a5d-3682-90e4-cd153802211a | -7.97372 | -54.77905 | 2024-10-08 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 56c9c221-ae13-3246-b618-e47ffe68670f | -7.97297 | -54.78334 | 2024-10-08 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e155aaed-e680-3c91-acda-233aa91fd7ba | -8.62162 | -54.93353 | 2024-10-08 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9af01f8-5409-314d-b9ff-8e8d58b88ed5 | -10.82172 | -55.72489 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6682b2c-5621-3643-b609-e355c0977107 | -10.81148 | -56.26671 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d14ded47-91f4-3b3b-8043-31113db313a3 | -10.66258 | -56.05111 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f26fb1dc-f6ce-3432-b4e9-32f4b0a2276c | -10.63138 | -55.9119 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| a0114568-65f1-36a5-bb06-efd2df5ea70a | -10.63054 | -55.9166 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5956c403-fb43-36c5-809f-e36021541841 | -10.62969 | -55.92133 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78693be8-9e56-3fb6-b9b6-1af3e62161ee | -10.62882 | -55.92621 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af6436ff-e8a3-3c2b-b195-d5a7a18f4578 | -10.62764 | -55.9064 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c33819b1-34d7-3e70-9773-8b40fa8fdaca | -10.6268 | -55.91111 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 32e94365-7729-3231-a25d-a6c82fc9a1e8 | -10.62595 | -55.91583 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7be2f128-1828-32fd-a526-d6cdca27adcc | -10.6251 | -55.92057 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2277f7a1-fc3f-3dd4-b459-02bdf5456f97 | -10.62425 | -55.92533 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63c38888-06bc-33e4-b20b-2d243061bc5a | -10.6222 | -55.91035 | 2024-10-08 04:34:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 554322ee-2140-361b-b823-e075e2610ea2 | -10.33877 | -55.59353 | 2024-10-08 04:34:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1728f052-9ea6-3a29-a4f7-5c16197371c3 | -9.8146 | -56.4224 | 2024-10-08 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0046b748-3b1c-30bf-ae8e-05de808c6f90 | -9.81368 | -56.42411 | 2024-10-08 04:34:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44ac3d08-2cdc-3239-9a6a-5dcf1d196b1d | -11.47479 | -56.76473 | 2024-10-08 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf4179a2-7d7e-349f-9fc6-79d104671687 | -11.4744 | -56.76663 | 2024-10-08 04:34:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d5dde0a-ed00-3970-94a9-7c04a5d462df | -11.38121 | -55.59637 | 2024-10-08 04:34:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f76aa72a-366a-356a-9485-130d1dd6cced | -9.36267 | -57.5018 | 2024-10-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 420ac140-362a-3bf0-9008-e805a4691598 | -9.35744 | -57.50093 | 2024-10-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 138119f9-b368-3233-b90c-58a8b2e90a00 | -9.35686 | -57.50416 | 2024-10-08 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f12953dc-001c-3f26-8b91-aada18a1405c | -10.56326 | -57.69416 | 2024-10-08 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5eb78ef1-a4ff-39d0-a59c-ae1106e39263 | -10.562 | -57.69308 | 2024-10-08 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e25b5be-abd5-365c-a1c0-5805d62eb671 | -10.55807 | -57.6933 | 2024-10-08 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99848b07-1815-3e9e-b5f0-6e2a0cb34a25 | -10.55683 | -57.69216 | 2024-10-08 04:34:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d0ff87a-53c9-30e6-9ecc-60ef250decac | -10.32767 | -57.79201 | 2024-10-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 543605fc-ac7f-370e-b002-910e477df308 | -10.24576 | -57.73764 | 2024-10-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50b1849b-abe2-3dd7-a6a4-d1eb210fdc8d | -10.24056 | -57.73659 | 2024-10-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63394f26-3afb-38c5-be62-650e41a5f766 | -9.54415 | -57.90364 | 2024-10-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3234357d-dd50-3de9-900c-08847b27fd97 | -9.54223 | -57.90361 | 2024-10-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b79a0b8-98a1-3c2d-9603-2065c343f253 | -9.48385 | -57.93148 | 2024-10-08 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36610f84-dd5a-320c-8b73-a7307e92e96a | -9.51821 | -59.50676 | 2024-10-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 69c7482b-7de7-3c81-9861-6bcf619329a0 | -11.49235 | -59.09545 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03ee8eaa-bb15-32b8-9dcf-1381e79c6ba7 | -11.49165 | -59.09916 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d3e1b23-0011-3f81-8222-1bc750938de1 | -11.49088 | -59.09676 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57e851b1-9998-326e-b91d-27118a3e4b62 | -11.49015 | -59.10046 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd302f08-d6f2-3aa2-a254-27cb15ac4ed0 | -11.48679 | -59.09435 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99be38ce-448d-3562-9495-aa3890d5ec70 | -11.48608 | -59.09809 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 739d47e1-7255-3b38-91ad-5b4e5abeb3c8 | -11.48531 | -59.09571 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53fcaafa-a736-3fc3-980b-bbf76bfc8122 | -11.48458 | -59.09943 | 2024-10-08 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6511e31-49ac-3041-8a87-545f1c7324db | -7.13534 | -59.29839 | 2024-10-08 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2147d14a-f60c-3de4-b30f-5a7748339283 | -7.06366 | -59.4506 | 2024-10-08 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f641e9f1-df6d-3879-8420-6ae018f68d40 | -7.06277 | -59.45544 | 2024-10-08 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 47358903-90b1-37da-91e9-cb89e1ba4443 | -7.02684 | -59.4098 | 2024-10-08 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a46b7311-b4cf-3ee9-92d6-090c7a728f0d | -7.0207 | -59.40879 | 2024-10-08 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0719ddad-fa52-38b7-8bc9-da6b88b6cbb4 | -7.01457 | -59.40773 | 2024-10-08 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96a30bef-5a66-3fd5-8403-79d78e5044df | -9.02452 | -60.43187 | 2024-10-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e1ae810a-3f1f-307f-81bd-5803760b0663 | -9.02355 | -60.43696 | 2024-10-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd5b5f11-7047-3d6c-b4b6-a138598b9946 | -9.01289 | -60.42439 | 2024-10-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d9a1ac9-88e6-3dd4-b072-2887c2d3614f | -9.00654 | -60.42344 | 2024-10-08 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 995a2911-a24c-3ee9-86fe-01a972681a77 | -10.42181 | -60.99378 | 2024-10-08 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14923d3f-90e0-33b4-b724-dfa8694117b0 | -10.37911 | -61.17561 | 2024-10-08 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc079955-d9a6-33d6-b894-e954c471c7b7 | -10.37804 | -61.18103 | 2024-10-08 04:34:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0eebe75a-418e-3270-bd19-20d8c63d3869 | -9.95591 | -59.84322 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f328ee75-3f90-3834-9188-b4e0c934738e | -9.95504 | -59.84769 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b7a9a9-4a19-383b-af4b-a5dd89454047 | -9.92365 | -59.93647 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eca11821-1468-3a1b-a52f-e73e223de89f | -9.92277 | -59.94112 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8b7d3f3-fa0e-335b-a30d-ba668f33cb2e | -9.9106 | -60.17208 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73ced41f-48a5-308b-8ea0-81f5fc7a1395 | -9.90966 | -60.17686 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00677632-3bc3-3016-bb71-d99eca7f7ca5 | -9.90446 | -60.17104 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5937771e-daf6-3dfa-b2de-4087484fb096 | -9.88436 | -60.30652 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| be9ff71f-6a29-3e98-98e1-ed70458b4a64 | -9.87817 | -60.30543 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6257fbd5-5ae0-36b4-9ae4-b38ef9eb030b | -9.87721 | -60.31034 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1ab5f76-03bb-300e-beda-2e906cc05787 | -9.87105 | -60.30911 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 946142a6-cad7-3254-b347-1759be4db12b | -9.87057 | -60.14983 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d87f78b9-ec04-3921-952e-f185a83be9c5 | -9.81496 | -60.46291 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bae397b0-6759-373b-ba70-f22ab9101e56 | -9.81179 | -60.4463 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dafd3634-e5c5-388e-a54f-ae097a3f2003 | -9.81096 | -60.46202 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9aaab383-d68b-3cc2-bd1d-e9b085f2db23 | -9.81 | -60.46704 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 567c0adf-0884-3ac7-b6aa-bfd7363da6f4 | -9.80863 | -60.44051 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cda9cbc1-aaec-36c0-8c46-3cc5e3f4f836 | -9.80776 | -60.46659 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21ddb733-863c-3869-a3de-247b1bdb0bf4 | -9.80766 | -60.44553 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b62d623-c9cc-320f-bda5-8a9629f2a65c | -9.80671 | -60.45048 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed56ed34-bc9e-338c-8af0-70e6d3b69c8c | -9.80555 | -60.44518 | 2024-10-08 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19a99152-6ed9-3cc3-bb33-889ce12ffe78 | -11.2589 | -60.4822 | 2024-10-08 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90cb136e-0c6c-35f8-9bf2-530fe0b1eeb1 | -11.25807 | -60.4864 | 2024-10-08 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb1f6cec-8313-3efb-a06e-d9b7ef20b4c8 | -3.89043 | -60.59212 | 2024-10-08 04:34:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4e942c6-d0e6-330e-83c5-c7270a99f34c | -10.20885 | -61.95654 | 2024-10-08 04:34:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df1eff02-c70a-328a-8ef8-3c6561e79f1f | -10.20772 | -61.96214 | 2024-10-08 04:34:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README60.md)
