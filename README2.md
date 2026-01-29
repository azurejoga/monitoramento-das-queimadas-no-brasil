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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9b4971d-eff4-3fa4-bf3f-68d696c1b0b9 | -10.00354 | -36.26001 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 83da4141-e504-3e38-8fff-c84667fc3261 | -10.01859 | -36.25804 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4d875a72-6ba0-3786-905d-dad7b87b5228 | -9.99993 | -36.25947 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 6d8301ff-e7b2-3e45-8295-d7824bb8b52c | -10.02157 | -36.26275 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9e05118-46ad-396e-8c88-34649357521e | -9.99271 | -36.25839 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e84291a1-6fc0-316d-bb7d-e8a7498a44f4 | -10.01561 | -36.25333 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 87b662f1-7dcf-32ca-a07d-37aa236e1adb | -11.51729 | -47.71051 | 2026-01-29 04:01:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 435f2431-d8ff-3a71-8b06-7ee9770a13ec | -10.00714 | -36.26056 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| fa130c34-9860-3b43-84e0-d391c42db5e9 | -10.00055 | -36.25531 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bd8b3b15-6782-3c90-8efa-0be22020bbc5 | -9.99931 | -36.26362 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 50ec85a4-b847-3c27-8285-ff0b1782b384 | -9.99508 | -36.26724 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 86b072be-4fde-380d-8219-40b57db9892d | -10.00291 | -36.26416 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 67d1f5b5-b7ec-386f-b364-51919df89132 | -9.81562 | -38.10698 | 2026-01-29 04:01:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31c34317-c040-3f70-9645-c6efd5a32352 | -10.02219 | -36.25858 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 533d4e70-4f07-3fa2-b742-4093a08e7887 | -8.59262 | -40.44703 | 2026-01-29 04:01:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 04ee180e-1da9-3e27-b3e2-125ee9771c3e | -10.01311 | -36.26995 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4aacd26-64c9-3e73-ac70-21821835f2f6 | -10.01671 | -36.2705 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 416127a9-2712-3f96-a991-9b5c65fc0c2f | -10.00416 | -36.25585 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0abc3aa5-495b-3e94-b6e1-6d8bfdf0c762 | -9.81618 | -38.10337 | 2026-01-29 04:01:00 | NPP-375D | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f8f76339-e887-3d94-82ae-ea317d6fa087 | -9.99806 | -36.27192 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2fa05fa5-acc1-3b58-bda9-ca9c882abef1 | -9.99869 | -36.26777 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 96de0f35-8316-39d9-a4dd-5f2b950cd6f1 | -10.00777 | -36.2564 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a676fe29-e619-397a-8b8c-95bdf51703b1 | -9.09885 | -40.05637 | 2026-01-29 04:01:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 72320269-abd1-390f-a857-c7781d6cfb5e | -10.01137 | -36.25695 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 70ad1176-f3ee-30be-879d-11a00d089f09 | -8.59601 | -40.44759 | 2026-01-29 04:01:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7fc1a967-a44f-33e1-8aee-c95522274523 | -9.99632 | -36.25893 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3deb40ca-cc87-36cc-9823-07a8cb857b6b | -10.01733 | -36.26636 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48e8fd2a-f4ae-3f4e-94fc-4b08266b5a69 | -8.88544 | -36.72585 | 2026-01-29 04:01:00 | NPP-375D | PARANATAMA | PERNAMBUCO | Brasil | 2610301 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c60a53d-1aab-3966-8dda-ed21b62f4208 | -10.00888 | -36.27352 | 2026-01-29 04:01:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8c6136b0-0fde-3373-9065-3d11b47e49bc | -17.59279 | -43.89697 | 2026-01-29 04:04:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9beeeb1-32c4-3784-b754-2204446e56c7 | -22.8565 | -43.49907 | 2026-01-29 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5502ec78-7a06-3d11-a3cc-ee2c47d461b0 | -21.77757 | -52.73844 | 2026-01-29 04:06:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90ca1324-7f1c-3ed0-9896-2eda83c71c32 | -21.81037 | -52.73668 | 2026-01-29 04:06:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1708d08e-3a44-359d-a584-58042b786775 | -21.804 | -52.73892 | 2026-01-29 04:06:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4bade43-2ab0-3eae-a5ac-80ed31f4c075 | -22.02535 | -49.50138 | 2026-01-29 04:06:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b74c5cae-5a6a-3f0d-baf0-099290420e74 | -21.77846 | -52.73447 | 2026-01-29 04:06:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d952a8c-fe70-3bf4-b4a3-6fece34aa926 | -29.68421 | -50.78292 | 2026-01-29 04:08:00 | NPP-375D | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 41ce1563-1294-395f-ab2b-b3b7d462b221 | -1.30892 | -53.20657 | 2026-01-29 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c3ff5c44-be48-3f7f-adad-6ebf84c0cdd7 | -1.19644 | -53.66164 | 2026-01-29 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dc403c69-4c3b-3f58-a1f1-bfec332e7aec | -1.32861 | -53.22399 | 2026-01-29 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1d42dec-951b-3882-8054-601bf72a1535 | -3.9763 | -49.10883 | 2026-01-29 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbb2dc96-6d47-3a43-b82f-897dbe74d798 | -1.30951 | -53.203 | 2026-01-29 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2a7e4566-0d3f-3d58-a0e9-f7176f77d331 | -4.67385 | -45.80095 | 2026-01-29 04:21:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba317a5d-e8c6-315b-8e9d-b4039718a7d8 | -1.67278 | -45.79432 | 2026-01-29 04:21:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0b3fc0bf-aba2-31aa-a5c2-f459c49fdde1 | -3.05019 | -48.47784 | 2026-01-29 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1ba924-da9c-33aa-85d7-7c67b0412d98 | -1.3101 | -53.19941 | 2026-01-29 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 205e5be9-eba8-316c-931e-9a6fc6472cb8 | -3.5932 | -49.43972 | 2026-01-29 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18dc14d9-ddb2-3abe-9b42-9ae0e357df36 | -1.32802 | -53.22758 | 2026-01-29 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb2f3ffb-8a85-3d08-89a6-6b021dfe645f | -2.5363 | -47.80009 | 2026-01-29 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cada084a-154f-32c6-83cd-86a1094fa717 | -1.30401 | -53.20214 | 2026-01-29 04:21:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f299e609-1efd-3711-999e-eb423461c82b | -1.19906 | -53.66219 | 2026-01-29 04:21:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea081ebb-7d8b-3bb0-aef6-7071bc724e01 | -11.52061 | -47.70867 | 2026-01-29 04:23:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35fd6e95-c2e2-31f4-97e5-b1351dba00b4 | -5.52884 | -45.95816 | 2026-01-29 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3309accf-3d06-3b67-941b-81a1d2411ed3 | -6.10324 | -45.852 | 2026-01-29 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34d89211-02f7-300a-9956-31a2bfce6047 | -11.51721 | -47.70811 | 2026-01-29 04:23:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3758e7b-f51a-3097-a28c-c8728fdd6a91 | -5.5322 | -45.95871 | 2026-01-29 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4e246bbf-da50-3f5d-9819-abfabee8f916 | -8.5949 | -40.44518 | 2026-01-29 04:23:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 15.3 |
| ad5ab6bc-7ddb-3968-bfed-671718854f2a | -17.59497 | -43.89684 | 2026-01-29 04:23:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1e36549-8c00-3339-bab1-78bd217a1c75 | -8.59426 | -40.44955 | 2026-01-29 04:23:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| d9185fcf-7f8f-3252-b1e5-421f01af5c42 | -7.86661 | -39.09629 | 2026-01-29 04:23:00 | NOAA-20 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 780f86d8-ed4f-314b-b74c-038ea545bdfe | -17.59801 | -43.90178 | 2026-01-29 04:23:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 573dc60d-a99b-37a7-b94d-51f2de39b183 | -21.77899 | -52.73611 | 2026-01-29 04:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e7012a44-3bcb-3759-8d43-65912feda35f | -23.52101 | -46.97443 | 2026-01-29 04:25:00 | NOAA-20 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 93467721-21cd-34d6-9021-5b63b51270dd | -22.02664 | -49.50154 | 2026-01-29 04:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6aa8225a-5b24-32f6-b8a6-f899620d1591 | -21.81001 | -52.73759 | 2026-01-29 04:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ef4711-12ff-3965-a620-9ccb393019ed | -22.84383 | -48.64824 | 2026-01-29 04:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dd785ec-635b-3724-9f9e-55b6b2f7f592 | -22.80204 | -49.33372 | 2026-01-29 04:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1851c91d-da9f-3d55-a19b-9c8671312cd4 | -22.84442 | -48.6445 | 2026-01-29 04:25:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a50a30a4-4fce-329f-ba25-fbce7e9137a6 | -22.02331 | -49.5009 | 2026-01-29 04:25:00 | NOAA-20 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a8df660c-3371-3c8d-9da5-3d575bb4eb2d | -23.18733 | -50.77026 | 2026-01-29 04:25:00 | NOAA-20 | CORNÉLIO PROCÓPIO | PARANÁ | Brasil | 4106407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 981c767c-17e3-34e8-8a81-f8d529febf9e | -21.8025 | -52.73592 | 2026-01-29 04:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b952fbbb-7aa8-3484-b8fd-77e03f92fccf | -21.90393 | -49.23598 | 2026-01-29 04:25:00 | NOAA-20 | REGINÓPOLIS | SÃO PAULO | Brasil | 3542503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f767f523-b068-3b29-a330-d13b8fe3fbc4 | -21.80339 | -52.73109 | 2026-01-29 04:25:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bfae8a6-9d17-39a7-912a-aff4a3fb037c | -22.79872 | -49.33309 | 2026-01-29 04:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e16835af-ad10-37b6-9ffa-2668c909f31c | -22.7954 | -49.33246 | 2026-01-29 04:25:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eafb68f0-154e-3faf-a29a-a65605825ffe | -23.48908 | -47.21679 | 2026-01-29 04:25:00 | NOAA-20 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1853d951-1ae9-3cf2-93de-db9efb2aaafd | -15.8498 | -43.50733 | 2026-01-29 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52748453-db97-36b8-9e8f-93d9a4179558 | -30.4834 | -52.97032 | 2026-01-29 04:27:00 | NOAA-20 | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 580b16fa-b316-3b32-a1e6-3776b1d7177b | -29.68623 | -50.78458 | 2026-01-29 04:27:00 | NOAA-20 | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de2a5b0d-0363-3e41-86aa-641ca534a608 | -30.20911 | -51.77365 | 2026-01-29 04:27:00 | NOAA-20 | ARROIO DOS RATOS | RIO GRANDE DO SUL | Brasil | 4301107 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 1967f7b9-3d0b-307b-bd24-188329b0250f | -30.20578 | -51.77286 | 2026-01-29 04:27:00 | NOAA-20 | ARROIO DOS RATOS | RIO GRANDE DO SUL | Brasil | 4301107 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 422f9f7f-c7d9-35f2-b15a-95d4edcf9954 | 3.12384 | -60.13264 | 2026-01-29 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 000ec3a9-a850-33bd-af6a-84fd51c5d985 | -1.31013 | -53.19711 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2d10c9ee-8dca-314c-942b-8c965326778b | -1.30949 | -53.20124 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a1a6de2b-6d9c-3938-ae9b-b74bdb4aefd5 | 3.8244 | -60.80302 | 2026-01-29 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c5bf9c8-4806-3191-ac56-afb9b42a428f | -1.47797 | -54.10907 | 2026-01-29 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d034e05a-d651-332f-ae58-2efc1f8bd917 | -3.97437 | -49.10939 | 2026-01-29 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d66593f-975b-3dd7-82fa-5905e723e8ad | -1.31373 | -53.19767 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b78b6198-a1ad-3c63-8f4e-190f311fd7b8 | -1.8082 | -54.4925 | 2026-01-29 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 907cb402-a5b5-313e-9438-fafcb01799c6 | 1.4882 | -55.91544 | 2026-01-29 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4ec5dc2-484a-37d3-9f41-62acfdb7f6d3 | -1.73345 | -52.71263 | 2026-01-29 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3defdeee-e703-3894-a006-1b2500b0bc46 | -1.85534 | -54.55214 | 2026-01-29 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60717580-955c-3179-8c1a-11f957a05530 | -1.31309 | -53.20181 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 55ba103f-9d59-3a14-8de8-0975d692a9b2 | -1.30885 | -53.20538 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1ce60539-b8e7-3bcb-9da7-0629450ea1bf | -3.61985 | -54.15371 | 2026-01-29 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9cfa319-7e9a-34ad-bd13-99af697b328f | -1.33147 | -53.22598 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2fbc875-93d6-3061-aaba-0fbffdea54ad | -1.33211 | -53.22186 | 2026-01-29 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70579e88-2713-3a6b-aa2b-e531373772ab | -0.82113 | -51.8463 | 2026-01-29 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6548c095-c347-3c81-b0b9-e2af7306e4cd | 3.47436 | -60.16361 | 2026-01-29 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c38950ef-a2cb-3678-b1c3-1f8b3e9f18e8 | -2.81105 | -52.53855 | 2026-01-29 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
