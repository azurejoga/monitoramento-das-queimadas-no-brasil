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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3cc71a3a-0983-33a3-a382-5d6664caed6d | -3.249 | -50.96846 | 2024-12-21 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ba2f9b-32ec-3d4c-bf71-d8e89528fae7 | -2.85589 | -46.73171 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b45b6662-6339-3188-a97e-ebf8c92d3346 | -2.80034 | -46.70753 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec411be1-280d-341a-a334-c0358822fcf9 | -3.09225 | -44.872 | 2024-12-21 04:46:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52a6a15b-fbd7-3932-a673-0bb8ec454fcf | -2.87345 | -45.24257 | 2024-12-21 04:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ec9b150-718d-3580-88e4-083798c97568 | -2.44241 | -47.48157 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3ddc59b-d665-3b8b-ae7c-88e2db01fc5b | -1.60795 | -53.88359 | 2024-12-21 04:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f943dcb-c2d0-3ffd-a246-3c2737050acf | -1.87127 | -45.55774 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83635eda-07ca-35d9-b64b-930b239333b3 | -2.67924 | -46.93635 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a979ac27-1867-30c2-9a3e-dae00d92dab4 | -1.29131 | -53.0998 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a6aa91d-2215-3fc3-871d-dd778b5aa85d | -3.87899 | -47.05065 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79b988c7-f899-3ab3-925e-31b53a419b97 | -2.06036 | -52.06033 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6790032-8120-3c01-a507-612ccc26e65c | -2.50073 | -51.83182 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7720bb0c-3f1b-396e-a758-d8ce55010602 | -2.58881 | -51.91899 | 2024-12-21 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b25c51a-7e78-37c8-acda-aefb39e88b9c | -2.5041 | -51.83233 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 934f34a2-be8e-3298-a186-e7e9de32a80c | -5.60997 | -42.82569 | 2024-12-21 04:46:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb1d0283-5fe6-308e-bb08-aba7f1e927d7 | -1.87913 | -45.55899 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e87d90b4-3d8f-3624-bf04-66089c8fa22e | -2.44535 | -47.4861 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2f9e5ad-0ef4-3e65-bb84-9730f9721af9 | -3.99228 | -46.64406 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 198eed06-43ff-3950-a984-258fc9cb1dc7 | -3.98145 | -46.40245 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ad54c66-d84d-37f1-b5d5-baab81b9d1f0 | -5.23255 | -37.73111 | 2024-12-21 04:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 58320474-146b-373c-b4f9-91c86e09f42f | -4.06494 | -46.72763 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6c6be428-7627-35e4-bfff-5c1be119e2d9 | -4.09818 | -46.73742 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba0c3f86-b4b4-39a3-b9f5-b32dd04bb810 | -1.22225 | -53.68352 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b1d08e-66ea-39d1-8721-ceaca573209b | -1.88775 | -45.55523 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ba8b5fa-040f-3964-a2ff-708b866b8c9b | -1.74165 | -52.16636 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 31836257-6a1f-3ff8-96f5-22a83464ff04 | -2.70607 | -46.1526 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4bb16ea-f044-34de-b8f9-bcad02f3dbf2 | -2.50937 | -48.05482 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b837bd0-465b-301c-84ad-81764c8d40cf | -2.88472 | -48.28023 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20bb62f5-e801-3a71-a20b-4f49068ef087 | -1.25914 | -53.68961 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4812134-6eee-347a-a6d8-c36c5ea753ad | -2.8999 | -54.5034 | 2024-12-21 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6624140c-2edd-3c5a-9a8e-6fc32dfc936a | -2.67889 | -46.91441 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd29f345-2737-3774-a7d0-9f24ca2d21e7 | -3.88538 | -47.03378 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aae5db9b-2967-309b-8be3-8224a66a7461 | -4.094 | -46.81584 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48aedfea-185e-3e3e-8e62-2cade1b1e287 | -1.56529 | -46.77615 | 2024-12-21 04:46:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 54c5a22e-ef55-3f7d-9f19-94f9450b3ba5 | -2.53551 | -51.89608 | 2024-12-21 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f72f3dd-508c-3e9e-a36e-08af3eb94e8d | -2.05917 | -45.48099 | 2024-12-21 04:46:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f8d7683-e2a1-35b1-ab32-fca13dfd8ac2 | -2.05811 | -52.05248 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ec29b55-e1f3-3d35-bee5-40c17ebff219 | -3.86936 | -46.58491 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbfdd837-9711-37b0-bc75-545df8c8d63d | -2.70991 | -46.13611 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21d9218b-e6f3-3af5-a6f0-ada27054a7b0 | -2.54565 | -51.89764 | 2024-12-21 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f8e7ab9-fe8c-3d78-8e73-60eaad4f284f | -3.80309 | -46.84954 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02ca20a8-9061-3507-8b7f-850a98902867 | -2.70771 | -46.15029 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ab8fde6-6477-3085-a578-390c495c5b20 | -2.79018 | -52.95121 | 2024-12-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 077680ca-7ea0-39b1-98bf-30230e3616bc | -3.90754 | -47.15564 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df6a72e-3a11-365b-8a3a-c45a3a00d506 | -3.90694 | -47.00888 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5920f365-f0ef-3d4f-bc58-1e806a52e899 | -1.74224 | -52.16265 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| c0d14cfa-dfbd-3071-a941-4c162b72bdb7 | -6.12359 | -46.86544 | 2024-12-21 04:46:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1210473-4572-36f5-877d-d818bcd06a31 | -5.91864 | -43.48179 | 2024-12-21 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8511156a-e583-345d-beb9-4a406a9bce18 | -2.62793 | -48.03716 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 17b63657-131b-3037-bd05-adc3c2e87056 | -1.80962 | -52.04855 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2912f018-fa13-3e7e-ac85-1f2003ad9e65 | -3.98904 | -46.74228 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| beca2f14-abcb-36aa-b381-2ef729f290fa | -3.80842 | -46.70531 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a2ca76b-55ff-309a-acc4-97d937c4e768 | -3.75305 | -47.18655 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c35c0b0d-e3bf-3318-8830-0c9edf36a3a9 | -5.22565 | -37.73011 | 2024-12-21 04:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9e48487a-5976-361d-9a59-2de04ee3274b | -2.6154 | -47.46626 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28e0ebd6-0842-3315-a990-ed8019245653 | -2.67522 | -46.91385 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e4e7a13-3e82-3658-ace7-76e9e8198105 | -1.29404 | -53.12954 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8af0f7f6-99b2-3f47-81af-b3f7f23ebbe3 | -1.25456 | -53.48175 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f843a99-ac34-388e-844e-7f404930c02d | -2.07968 | -52.04831 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 45b59153-8ba4-3b61-b38c-95f95fb1b26c | -2.87699 | -45.24681 | 2024-12-21 04:46:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 681491b0-42d7-3fba-afa7-4afb3dc93548 | -2.90442 | -54.4994 | 2024-12-21 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5d3f9b5-26c0-318e-9410-12b5622a2795 | -2.65525 | -46.10828 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 382253cb-5747-3edd-bd25-e93f04d90e07 | -2.58486 | -51.92208 | 2024-12-21 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa8ae4e6-e22f-35c4-9fbe-78b1e5a9f103 | -4.0575 | -47.10564 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87c1d90d-2d83-33fa-a4d6-9eaf43810136 | -2.50819 | -48.06244 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6263381-2362-322e-ba70-2d024a2ca2db | -1.88306 | -45.5596 | 2024-12-21 04:46:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40395aae-934c-3fd5-af4c-79fab53e5c74 | -1.46245 | -53.6832 | 2024-12-21 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e36ce24c-71d8-3d4f-91f1-fe01317a4518 | -1.73823 | -52.16584 | 2024-12-21 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae3b86e7-f000-3aa2-8fbc-c29ff1403f86 | -2.70375 | -45.57204 | 2024-12-21 04:46:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80ae0130-2cb6-3ca6-ad2a-a11195d12ff0 | -2.50467 | -51.82874 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edb6d420-1d96-3097-8587-33f8904cbeb0 | -4.53688 | -44.05522 | 2024-12-21 04:46:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8805e913-cc5f-3040-8921-d8fac7a9f3ff | -3.90386 | -47.15511 | 2024-12-21 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c893b91-3dda-3af6-b07f-1d891c424efd | -2.8853 | -48.27647 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1e04154-35bf-3c7a-87c8-1e0200d9b822 | -3.1732 | -45.97332 | 2024-12-21 04:46:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df15bde2-aa9d-377d-b6f0-dc086eadcb3e | -1.28836 | -53.09519 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 705a3d4d-b6cb-3840-a366-57694b068c70 | -4.05581 | -47.09196 | 2024-12-21 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9612f99b-b5c1-3197-8409-53ea6554a0f9 | -1.29173 | -53.12074 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34af6a2e-fc73-3cdc-a625-4855e999d044 | -3.15236 | -44.26898 | 2024-12-21 04:46:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 546f227c-700b-3b51-a2c7-bc727d120566 | -1.51082 | -47.27407 | 2024-12-21 04:46:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddc80020-8748-368d-9d7f-82ba4d2eaa32 | -9.72948 | -43.493 | 2024-12-21 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f3a5acd-b19d-3d28-8bbf-6df327ade826 | -2.84235 | -54.54672 | 2024-12-21 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4ca659f-7ac7-3276-b706-82c246151993 | -2.79141 | -52.94346 | 2024-12-21 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 875688f9-6cdb-3884-884d-78a4352b51bb | -2.46299 | -51.84032 | 2024-12-21 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f85cb838-a4ad-33bd-991c-0c609d9817c4 | -2.78551 | -48.07974 | 2024-12-21 04:46:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf9d1e94-5f9c-3c48-87e5-e6a958c704f2 | -2.19589 | -48.4244 | 2024-12-21 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 288c6bf5-5ebf-3ed1-906c-43325344353e | -3.07249 | -47.48031 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 413d0c03-1893-3481-a6c7-0f8208abd897 | -2.76334 | -47.39484 | 2024-12-21 04:46:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2e54349-00bc-39bd-b09e-79c3528f5359 | -4.0199 | -46.90151 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dd03c83-dede-342b-91b4-a42b36c50d5b | -2.70817 | -46.13839 | 2024-12-21 04:46:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bd9b0759-42bf-3ec4-bb39-69144ed418b0 | -1.29109 | -53.12487 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 129ea811-833a-3b5c-9145-b4b01bf0ef3a | -5.55801 | -46.34678 | 2024-12-21 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dd553e1-a7c3-3520-a3ee-3ab18451aff1 | -2.44924 | -48.57534 | 2024-12-21 04:46:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d3db4c2-bea8-367b-8a68-0304c05d4968 | -1.25504 | -53.52559 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c62df4c5-9991-3f69-bb82-64779440ee97 | -1.26373 | -53.51818 | 2024-12-21 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36d0a655-7d8c-31ed-8542-8412102cdc50 | -5.22566 | -37.73099 | 2024-12-21 04:46:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 25c0b202-8e2a-3242-9c79-c4fe5f34d191 | -4.06185 | -46.72248 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 595e3a23-c12f-3e58-a33b-92fe5b55a066 | -2.8071 | -46.71309 | 2024-12-21 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebb7714e-2bc2-3cc7-b4fb-10ad8e3139ef | -4.10468 | -46.72 | 2024-12-21 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64affb48-e198-303d-a164-9ee6cd28a18d | -3.83362 | -41.5703 | 2024-12-21 04:46:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README8.md)
