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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdf714cd-936a-33d6-a639-1b3d748abbfb | -4.9472 | -41.1895 | 2025-11-28 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 125.6 |
| 4afeba2a-e45a-3df2-886d-6ffe2014a899 | -5.0825 | -40.7425 | 2025-11-28 14:00:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 86e6c395-bf70-30ad-886b-3a6b3b24caec | -19.0522 | -57.5148 | 2025-11-28 14:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 89.8 |
| 4c72ac62-53c8-3c78-849a-7f9e24fe4113 | -6.4778 | -38.8542 | 2025-11-28 14:00:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 146.9 |
| ca3d212c-1d65-3ad4-ac82-b2cde0066e47 | -4.966 | -41.1881 | 2025-11-28 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 10e1da09-6f00-362e-89c1-6cc27a7cffd6 | -3.5083 | -43.6837 | 2025-11-28 14:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 5caef385-6a62-3ccf-b4f5-674254d63a8c | -19.2151 | -57.3275 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.9 |
| 4a0cc82c-01a0-357c-a1ef-8480c860842c | -4.9472 | -41.1895 | 2025-11-28 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 162.5 |
| 12010d8a-c9bf-326d-b0ed-a6626ec11fc0 | -6.4778 | -38.8542 | 2025-11-28 14:10:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 152.3 |
| a7f09135-e69a-3176-ab4d-35135ed1285b | -20.387 | -57.9814 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 83ed1de4-9a63-3f65-8e9a-eed9040e1331 | -20.3874 | -57.9605 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 6dd89e5d-1345-3dfe-a992-600b248e86cb | -3.5269 | -43.6828 | 2025-11-28 14:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 10bb45a1-3dd9-31c5-a778-cac78f787e30 | -2.9572 | -41.9974 | 2025-11-28 14:10:00 | GOES-19 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 212.5 |
| 4e9bad17-5774-3e12-80b9-8919b73a4571 | -4.3872 | -43.406 | 2025-11-28 14:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 142b2a2a-d255-360e-9f36-c35511cdee19 | -4.9662 | -41.1639 | 2025-11-28 14:10:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 116.8 |
| 0f08c5e2-c5ad-316e-951c-cfcff891e407 | -6.6711 | -40.1357 | 2025-11-28 14:10:00 | GOES-19 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 107.3 |
| 50c31d9d-7e3e-3a55-8bce-5b651b18fa0a | -20.3878 | -57.9396 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 897aecf5-9883-3015-a39b-5f577fdd4e27 | -19.2347 | -57.3456 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| b4a5e462-f8be-3e17-b9ff-eea9e69046cc | -19.0722 | -57.5122 | 2025-11-28 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 3350beec-0a5b-3492-81f8-cd0b466de23d | -19.2343 | -57.3665 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |
| bfb075c8-2d82-38d8-857c-2e9f63e0183d | -19.2143 | -57.3691 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 66078358-e5ee-3868-ba6c-aea2e4ab00b2 | -20.4076 | -57.9577 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 25d7756c-408c-3bf7-96aa-b9ac789bbbde | -19.0522 | -57.5148 | 2025-11-28 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| d2d604d2-0fec-32dd-b748-caad473ea2a4 | -3.5271 | -43.6597 | 2025-11-28 14:10:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 949412c0-abd0-3612-8182-c8b805dc6114 | -19.2351 | -57.3248 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.2 |
| b55215d1-a900-3af6-ba56-47ca008176e7 | -2.9563 | -42.1636 | 2025-11-28 14:10:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 758e5a3c-3cf3-3c5a-9d46-c7c9674bd8a0 | -4.2024 | -43.1138 | 2025-11-28 14:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| e0a538ac-54aa-3a3f-b811-4b1ac70c593e | -4.9474 | -41.1653 | 2025-11-28 14:10:00 | GOES-19 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 137.0 |
| 19035bcd-696a-3986-b9d3-2d583cbb5b78 | -20.4073 | -57.9786 | 2025-11-28 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.4 |


