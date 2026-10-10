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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 981efeb8-8ea6-33e7-938a-36cd70f91acc | -5.96323 | -55.38402 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2a2ec3b-2907-39fa-bc05-58141df3364b | -5.70719 | -53.48542 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb95ae0-bbbe-32d8-b404-9d1b93ff73da | -5.79552 | -53.80919 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7533361a-1f11-32eb-add3-3b83b59ee847 | -2.84052 | -49.88155 | 2026-10-10 05:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 201e02c4-e474-3a58-a818-f2c16a84d813 | -2.85664 | -51.27603 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cd2d6a5-4c67-3436-af58-44d3b5be7c0b | -2.83109 | -54.12072 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3e7b21d-0cab-31c1-9d81-d29c848a74ba | -3.16606 | -50.45123 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d51db65-69db-3723-84c4-7bcaf6bae884 | -2.9933 | -51.04701 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf9b4573-8810-339e-8557-d98477ff7abe | -3.48957 | -50.48884 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c8dfccc-9790-3993-8f3d-3d321aebffd0 | -6.13805 | -53.10198 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90d49fb0-ef67-3331-a5f5-e06060011f33 | -3.95543 | -56.11425 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe3fa56-c1b8-39f0-a927-7209f1f28199 | -2.81618 | -51.96058 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94d52381-879a-3081-8762-5ab1989ae8e5 | -7.20994 | -55.1521 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2a21027-310a-3c43-9294-f4ec652ed8ae | -1.92018 | -57.03994 | 2026-10-10 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d5bf005-8370-30ee-afa2-8d51c36abe3b | -2.05118 | -54.49398 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87aafd25-5ed0-3d58-97ad-d349bd29a784 | -6.6475 | -55.33473 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc34e2cb-1bd0-32eb-b67f-e43feda84060 | -3.42363 | -54.06927 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5ab50bf-a7e8-3759-bde0-b62ee88237e8 | -6.44185 | -55.04675 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5863b4d0-7bd7-3b86-951b-61a7e4de9345 | -2.56823 | -57.41575 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d44cde8a-f0f9-3750-846f-ad2db103915c | -3.92691 | -55.85847 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61c3acb3-fa11-39a0-bca7-2d5b01ae968e | -3.52802 | -54.67233 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18b905f0-ff27-31ec-9e03-580ba41701cb | -3.00607 | -54.10935 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 87bf3749-d93c-3d79-8f66-a64c1b5732e9 | -2.39792 | -57.89655 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 880a1f30-aa2c-351e-9dff-1c240be34fd2 | -3.83994 | -55.78807 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e3d577bd-0ba3-3a0c-8e24-cfdbd29435e3 | -3.583 | -54.71341 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fa35943-40e5-36ab-b011-242dda97681a | -3.60022 | -54.58344 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 059e54ef-408f-3047-9d14-259cbe26bdda | -6.02481 | -55.33576 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 995db58f-26a9-38f3-a5b4-72144af879d6 | -2.44319 | -58.01623 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d301690-3b8d-300d-abcb-7f2c493a7cb0 | -6.46871 | -55.49392 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddac9ad7-1ad4-3c64-942b-c8519ed29bf2 | -7.23872 | -55.16348 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7aa1b50d-6d42-3b28-9985-4f3f0ce4854c | -3.28293 | -54.07885 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51f9a5ff-bd82-32ac-bfe0-3bc651fbe083 | -3.31299 | -54.67825 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae58113f-edd2-31d6-b975-a984d8d9962d | -6.73171 | -55.10351 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9901fbbd-7f69-342d-be01-9f57090903b2 | -3.27483 | -54.68675 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9ac7506-ed6f-36de-81be-4b901bbfe4ae | -5.96723 | -55.33759 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8265083f-1c92-3db4-9440-e592bee9fa81 | -1.18772 | -54.17464 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86dbe3a5-66a6-33c7-894d-76b6afe3852c | -3.89907 | -55.90009 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a619ae1b-565c-3b72-a96a-df4879a1d881 | -6.31675 | -58.30699 | 2026-10-10 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4932ebe-04d6-31c4-890d-310a6fb29968 | -5.23571 | -50.68609 | 2026-10-10 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0f2a87-cb2b-3922-b475-10bee5d265a8 | -2.58524 | -56.1843 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2842210e-8469-3e6a-995e-9716e1207dc3 | -6.73779 | -55.10804 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff3bb78c-d4df-3dd5-b113-84a353392591 | -2.97234 | -54.04393 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9460615-2a68-3594-b9b0-13ba640d263b | -1.19073 | -55.66486 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67fdfe74-b15d-31df-8a88-35a3b1b8e133 | -1.96361 | -54.38303 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72d1e1a2-43e3-349e-abc6-f8120d14a598 | -2.98901 | -54.17401 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5a11602-d512-3743-a9d2-84bc3bb477fb | -6.16167 | -52.79763 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c1adede-01fb-384b-b0fa-c9181b594091 | -2.47114 | -56.08202 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aed04d08-f18d-3b82-9a74-317794698015 | -3.07958 | -53.96873 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8467eb2a-0e49-3eb6-820e-cae0958dddbe | -6.11515 | -53.09476 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c83e370-7295-3288-be50-9ab4a65964ca | -1.20545 | -54.21341 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5241082-0fc8-3617-9d0c-5495d0c2b4d4 | -2.77377 | -56.50356 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d57dd0af-e056-3300-85b8-0076dd1b2dbf | -3.26233 | -50.38787 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf3378d5-db09-352f-9570-02fe42a5cdfe | -1.96471 | -54.39758 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b52a4ae-112b-3e2c-934e-bfe9a8968de9 | -6.6219 | -59.94419 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04a675a6-e29b-3099-a456-85032b958415 | -3.06875 | -54.25012 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89bb5288-4175-3968-9e5d-752ccc948be6 | -3.02254 | -54.04828 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61f84fc5-f9fe-3077-9bf7-f7d4d4fd9a32 | -7.20915 | -44.35207 | 2026-10-10 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ef69176-19df-3655-b67f-a143535b9bd8 | -2.75369 | -54.09399 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9797c474-c078-356d-bb52-1441e6fae2b1 | -2.05068 | -56.86401 | 2026-10-10 05:04:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e073fa7-6e43-3ff4-8712-d7393ea7c99c | -3.0339 | -53.8912 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c61550d-b9d2-3d96-893e-6b24d89ad0f1 | -2.816 | -57.61138 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50adb051-6d05-369b-bd10-53f1d86a5133 | -6.02538 | -55.33224 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d78f641a-805e-3537-9f22-02f74372a87d | -3.16456 | -58.62514 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f917ebbc-65e6-35f9-9e58-ee8a9b363cf7 | -6.33217 | -55.30889 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 780b3c1a-697b-3c06-ad59-794805dafc6e | -3.56801 | -54.6787 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b221a34-584a-314b-9cb6-a0f2cf9efea9 | -4.10115 | -54.01785 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 073f9564-1846-354a-951c-1f53bc6774db | -2.99994 | -54.0624 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3230487d-7c50-30c6-9ab7-625dabc828d8 | -1.73891 | -55.24252 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61c08520-2cb2-3fa2-8d7c-0fe60c7c55cc | -3.15541 | -50.58919 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 663eebd5-6edf-36fb-a407-52acbcc4ccb7 | -6.48243 | -55.9556 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 75e58d09-6ab1-336a-944c-e424e35f4a58 | -6.32656 | -55.3441 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f108d0c1-999b-3e75-aa50-f1e669312314 | -4.46179 | -54.97527 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9008630b-2dbb-38c2-9e76-120ece467ec0 | -7.02181 | -47.65696 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 3a6ca5e3-b179-3507-8fe6-4d17e4725e95 | -3.74191 | -58.50066 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c22cd9b-4ef8-330a-89d9-5dde035ed981 | -3.67473 | -54.49916 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a195722-de8e-367e-bff0-908fbf2d33de | -2.56498 | -56.15274 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31d097b7-0209-3497-823c-e0cd82e78d0c | -7.23954 | -44.1678 | 2026-10-10 05:04:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4712a80a-7058-3272-98a2-b94f0a47332e | -3.63983 | -54.52575 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee83ba59-769b-3e12-ad33-672dacd2f2db | -5.55638 | -43.96453 | 2026-10-10 05:04:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ab8e2d7-045c-384c-8707-72c02b4bc022 | -3.80605 | -59.2195 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7860ddaa-e40d-38b2-a538-b76569b9fa54 | -3.19679 | -50.54831 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b57c714c-4178-3fe0-a249-d96bfdec6d28 | -3.86749 | -55.9644 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9aabc650-c35f-3f8c-bd09-4049b367e574 | -3.22177 | -54.86995 | 2026-10-10 05:04:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ee6fe8-dcf4-3902-96aa-253d538eb5f6 | -2.22153 | -50.49245 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ee8b9cd-d7cb-3079-8b23-59e788a7061c | -2.95916 | -54.12677 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9e9b9c95-1af7-3aaf-8b19-7120e3bf4090 | -3.8701 | -55.99209 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c697a0-ccc0-3122-9270-fb6141006263 | -5.10363 | -46.22643 | 2026-10-10 05:04:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 055eae73-15ba-3f2f-992a-dc52f8aa241d | -4.09784 | -54.01733 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1a6154c1-35ba-391c-a491-0a65ac83f096 | -3.76933 | -58.53115 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f19e55a-3cb9-3753-8933-fac34449fb32 | -3.51085 | -54.63019 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1d0187b-24a1-3c30-8b36-bc4eba6028e8 | -7.03026 | -47.66294 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 134869b9-7e4c-3464-8a4c-a3fe105f11a1 | -2.85099 | -54.1451 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f18a12c0-1250-305c-be28-b52c66e363fa | -2.39714 | -57.90142 | 2026-10-10 05:04:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fd8ac7c5-5137-337d-9db4-03163ebf4d93 | -7.19723 | -55.14649 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2af9477f-4afa-3333-a934-039b55d20f39 | -7.49896 | -55.00229 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b8b37d2f-2c04-33e7-865b-c2125d911ec2 | -5.18875 | -60.30647 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb0e0e7a-a781-3eb4-b106-2112ee96e8da | -3.186 | -49.253 | 2026-10-10 05:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03c3625f-f88c-3158-a6fb-187c91231e90 | -2.75314 | -54.09744 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35388021-c23c-3177-ae93-e6b7ce8601d4 | -3.09552 | -53.93242 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c2eccc-156b-3295-a8d3-390e2cbb2493 | -3.56768 | -59.09294 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README111.md)
