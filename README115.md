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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec0fc82d-e4db-3cfe-8d16-43bad2ee35da | -3.98028 | -48.14044 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bec68e36-2a6e-3f4c-95ec-74263a41ca6d | -2.81685 | -46.64708 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dffe37c-ed8b-376f-b27a-391119db56c5 | -2.85022 | -48.44214 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7111c485-2507-3f22-a4da-28a6fd2c67c1 | -2.56103 | -48.23851 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35bb301c-a19f-30cb-91e8-f7139b69ede9 | -4.15988 | -48.24653 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 943744a2-8afb-3377-b4fb-01d673fb6b65 | -4.79267 | -48.65818 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 688b013b-3adf-378c-bb41-9361ada96c93 | -4.20555 | -49.76392 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc3b67f-1bf6-3c17-afac-2df12feb5f1e | -2.46101 | -48.83036 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c40d63f-179a-38d3-951b-9acfb521be85 | -3.22584 | -50.67803 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b57339af-de79-33a2-823a-292726cfa11e | -2.89128 | -49.51096 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c80e6f9-f8e1-394f-8831-106351862d05 | -4.06514 | -48.31373 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20092c57-dd55-350c-b201-b33aedd84de0 | -2.42393 | -50.42916 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cc716747-4039-37d3-acbc-1bf3cde8a12f | -4.27238 | -47.07286 | 2024-11-10 04:38:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42df640f-df12-3e10-9792-2d8a86d0ba2c | -2.95855 | -48.03445 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8149ed6e-4d7c-3153-afb5-50b59636284f | -3.78401 | -47.73727 | 2024-11-10 04:38:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c695c53d-9b08-3760-914e-1bea61522da3 | -2.91516 | -49.36032 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 389bca5b-0251-3a88-9f22-25bf130694fd | -2.93471 | -49.43149 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70da6275-5792-36d3-85fc-e66636ef3a6e | -5.23803 | -48.16308 | 2024-11-10 04:38:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac90411-3ad2-34e3-9ecd-affaa082acdb | -2.94564 | -46.78301 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d261f688-1d61-3ff5-8607-1204a3aa8368 | -4.39539 | -41.90659 | 2024-11-10 04:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9aa8a39e-9364-3997-879f-e3ea91149e52 | -4.00653 | -54.38354 | 2024-11-10 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3d75eeb-f0e6-3ead-a8cd-7da86bfb3db4 | -2.65427 | -51.7659 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96804d96-dc3c-3cfd-b78e-1022fab4b472 | -4.04654 | -51.07143 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c136cef5-afde-3830-82a9-d2603b912597 | -4.40002 | -41.90725 | 2024-11-10 04:38:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 13f382c1-321f-3847-a631-e2918004872c | -3.30988 | -50.08928 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85ba60dc-bca9-3f33-baa5-4f022ecf507f | -3.60034 | -50.45466 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f141e0c-d765-3560-8b09-ee9a968d22fe | -8.375 | -44.14437 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25e9930c-6a1d-3d7a-81eb-c8ef27ea9290 | -4.10709 | -45.70484 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 756eff51-d4d4-31b6-86d3-7fab5c1610de | -2.31722 | -50.57446 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 735cba4f-5786-3473-b1b7-11ed371dd814 | -3.23858 | -50.44802 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3476d5a-9561-3b0b-905b-a5d76b568f47 | -2.80626 | -49.34348 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 9623e78e-f364-3df2-aef2-80484dcdc261 | -3.05426 | -54.00024 | 2024-11-10 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25a51244-aae7-3e57-b38a-3489f618afc6 | -2.73028 | -49.18097 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ab47c74-1d4e-3297-b287-877873a15e98 | -2.81473 | -52.9594 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 44676f62-9510-3874-bc33-56552e15302d | -2.46081 | -50.3968 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22d5b029-eb64-33e6-a8e7-841e53d1fbd0 | -4.11039 | -49.12083 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| f07849fc-69bf-349a-b029-907177d53f3a | -3.1727 | -50.59735 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 936bd268-0f19-3bd4-a20e-a1d920cf8f39 | -1.48961 | -55.43985 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f5d5ca13-274c-3af1-a62d-915af37394f4 | -4.1919 | -48.3901 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e153ee6-af0d-369c-9b6a-39bab2fcb0a5 | -2.60236 | -48.19193 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 181ea5f9-f86d-3c8e-bf9c-db810e43ce80 | -2.85462 | -46.63012 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 539a19f3-b93e-3b31-b23e-5c692b29b784 | -3.68822 | -48.83834 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ac758f7-f90d-3045-a04c-634eabe2f299 | -3.13819 | -50.44416 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 110e76b0-75c2-325f-ad47-4dc2bfcdf72f | -4.10953 | -46.8861 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff25b08c-b3f0-3b70-b6d2-fc848519dab5 | -3.02854 | -51.09567 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ccd1866-8057-302c-aa8b-839b74ffef8e | -3.60329 | -48.92408 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af0ccd64-8bf3-396b-8ff5-54627b8d1203 | -2.62144 | -54.40339 | 2024-11-10 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c0b18d3-db84-374f-8fe4-4edabf0529f3 | -3.24236 | -50.31315 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cc701fcd-062f-37bb-90e3-74fe88b0cb59 | -3.86892 | -49.94966 | 2024-11-10 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ef7672a4-7378-3c40-a680-282ed3e902b8 | -5.55163 | -44.69504 | 2024-11-10 04:38:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 773f8d52-c1f6-3da0-945d-65e33aac6909 | -4.11256 | -48.50536 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 592f192a-e406-305c-bb13-ce470ad7971c | -2.65867 | -48.56406 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d93ef4e9-c082-36f5-8e79-584ac5f3d459 | -3.14913 | -52.97048 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 423fc2b1-a6b1-351c-b9b4-47023284b3ca | -4.30359 | -48.6455 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 207a4bbc-63b9-3bb0-af1e-46fccb901c9a | -2.68556 | -48.50119 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f39b6153-18c3-3ce9-b75c-216c82000678 | -2.97546 | -47.92694 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 940d5a3a-185f-3432-b4ee-a0b10f47d417 | -2.60127 | -48.19883 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee307c92-ee08-34ed-aaa3-82bead05cb93 | -3.86711 | -50.07683 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20ac6e78-e343-3d25-bac7-6f7647d5741e | -2.46488 | -48.82742 | 2024-11-10 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 11ef1d0c-a33c-3292-9235-77eada246d8b | -2.641 | -49.89706 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a01b2c1a-4a6f-342a-9a06-eb7a00eb2e65 | -2.59664 | -48.31469 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e7c730d7-4b99-342e-8f6a-a18828c71227 | -4.12683 | -46.84297 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98444b2e-0716-3714-9470-3d9288f678e7 | -2.87233 | -49.27157 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3691fc55-d749-3c6d-b819-71f84651fe06 | -2.43589 | -53.66373 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6326f10-66b0-3bff-8390-8cd054e97b6c | -2.61189 | -51.75051 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d065607-4cc3-3094-84ec-6074591ea1e4 | -3.70948 | -40.70942 | 2024-11-10 04:38:00 | NPP-375D | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b5aa8fa7-a44d-37e9-ad6c-e158ad066df5 | -2.60776 | -47.96262 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6faf902b-b52a-3f05-a7b7-2a7c9f026929 | -2.32881 | -50.56852 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d10c0214-8993-348e-a8cd-ece6dc531a21 | -3.46201 | -50.18307 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 794d3e35-de4d-3f0d-a9f7-9eaa2bd0e9cb | -7.79416 | -49.3214 | 2024-11-10 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 108bf716-77b6-393b-bed2-fe882f94995e | -3.10106 | -53.32351 | 2024-11-10 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38617875-19e4-3cd6-90cf-c4184623c332 | -3.53683 | -49.26482 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06dca114-4550-3b3c-8612-a8af03e48349 | -3.24352 | -50.30585 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 0373f112-9b0a-3d74-abb8-cc2d7aee5bd5 | -2.8631 | -49.39537 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc9597da-2a9b-3a85-a2a2-3d875669ea6c | -2.94157 | -49.15038 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7358767-1ab3-3363-ac92-92de6e256454 | -2.94371 | -49.50478 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5e51418-744d-3360-bf68-e34b88a4f69a | -4.13106 | -49.5509 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b7fd72-0790-3cde-90a5-680a9549ae5e | -2.66805 | -49.90131 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73b5990b-6742-3381-868e-2b3ec8bf1762 | -2.92215 | -51.67684 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d27d343f-b2b4-3737-88de-cc06eb88d988 | -3.95708 | -49.00112 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 64ce3f31-9288-3cc4-9ba7-f552e77e2cc1 | -3.97267 | -48.1891 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 82575536-94c0-3bdd-87bd-510731e2c70c | -3.18884 | -50.58461 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 612cdcf5-4d7e-3510-ae2e-9190e8aabf83 | -17.6266 | -57.5281 | 2024-11-10 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 185.9 |
| 17cfbb52-aaf9-3342-856b-2138378ed77b | -3.2352 | -50.3065 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.3 |
| 737e7610-b714-341f-80b2-ca5494f8aeff | -17.6069 | -57.5304 | 2024-11-10 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 301.0 |
| 260a1eba-0c71-3f09-92cf-49f112c35f28 | -8.4159 | -44.1112 | 2024-11-10 04:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7be9be24-7191-3291-a9f6-61ebe3b20803 | -17.2933 | -57.4857 | 2024-11-10 04:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 107.0 |
| 5e0db061-87a4-358d-b81c-09c5b31afb3e | -3.2243 | -53.0727 | 2024-11-10 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a1fec839-200b-332f-9e4e-f0b786cd1f26 | -3.2353 | -50.2645 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 7b114f5b-1565-326a-82ab-2d4c46a17f1b | -3.2536 | -50.3059 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c4fd411b-e567-3d4f-966a-ccc30b9f1f08 | -17.627 | -57.5075 | 2024-11-10 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 187.3 |
| b09ee2e4-d651-3ad0-a664-730896726d0c | -1.5347 | -52.2104 | 2024-11-10 04:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| a3ba43eb-4708-319b-ba55-6df84c5ee543 | -8.3781 | -44.1154 | 2024-11-10 04:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 4689d8b5-6157-31b2-823b-ecf2f44d433e | -3.525 | -44.0286 | 2024-11-10 04:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 8f1f0cc2-fddf-3627-9322-91aea3a825cf | -3.1422 | -50.4562 | 2024-11-10 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 39d7fa76-4c00-30be-8899-9cd4bff1fc55 | -8.4156 | -44.1344 | 2024-11-10 04:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| d3ab157b-4cb5-3f3a-97cc-9eb7a363de26 | -8.3778 | -44.1386 | 2024-11-10 04:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 9d8d1ce8-41d1-38fe-9811-555cbf07757a | -2.8618 | -51.484 | 2024-11-10 04:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 63996d6c-2655-360f-91a8-7ff9c0e88fb7 | -3.9669 | -48.1716 | 2024-11-10 04:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| de201d20-41fe-3b24-a727-0b89f2ebbc40 | -2.931 | -52.7753 | 2024-11-10 04:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |


[Clique aqui para ver as próximas entradas](README116.md)
