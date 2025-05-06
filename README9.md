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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 76826f36-8442-3624-a5df-184750c8b4c9 | -6.6208 | -44.7896 | 2025-05-06 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f0d2288a-cbb9-3a03-bc68-9f7c7683742b | -6.6208 | -44.7896 | 2025-05-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 9a65b98e-56ec-31f8-afe3-732f6c598183 | -6.6211 | -44.7668 | 2025-05-06 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 768489ca-d9f5-34cf-a39f-f6126c2e142c | -9.193 | -45.3342 | 2025-05-06 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 90ca448e-4f18-3847-96dc-aa3cff7910f5 | -18.4279 | -54.7129 | 2025-05-06 13:50:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 47d4192b-40d3-359e-b439-7d0f15ea40f8 | -6.8485 | -42.7979 | 2025-05-06 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| b485444f-332d-39ca-b137-2ab02db6ef71 | -12.8355 | -47.4117 | 2025-05-06 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.7 |
| ee6273f0-305c-37b3-8fee-1417f270f1e5 | -6.6211 | -44.7668 | 2025-05-06 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| fa103645-21e6-3103-bc48-07a130153fc2 | -20.7222 | -54.4124 | 2025-05-06 14:00:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 94.2 |
| de05e6b2-cd34-3a03-b3e4-3f9363e055c4 | -9.193 | -45.3342 | 2025-05-06 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 612446bd-98e6-3ed2-a1af-cedc84a0fc4d | -12.8355 | -47.4117 | 2025-05-06 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| a1d2341c-7db2-35fa-9479-447e1110602d | -20.7222 | -54.4124 | 2025-05-06 14:10:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a5e9258f-2881-3515-8dd3-119ce3d60b6f | -9.193 | -45.3342 | 2025-05-06 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ecb726c3-9dad-3f8e-85c1-1f46390be112 | -20.2744 | -55.4714 | 2025-05-06 14:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f99264aa-98a0-3c37-bb10-a14a9cf0cf15 | -12.8355 | -47.4117 | 2025-05-06 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 93ee89e0-aa47-3aa0-bab0-4d797091b1f4 | -12.8355 | -47.4117 | 2025-05-06 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 1075c4c8-8207-3939-a1dc-5de91b9cdff1 | -9.193 | -45.3342 | 2025-05-06 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| a74d1c02-917b-3b21-b378-636b23059891 | -20.7222 | -54.4124 | 2025-05-06 14:20:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 113.9 |
| dcab39b8-b443-3559-8628-0c02436a4c2a | -6.6211 | -44.7668 | 2025-05-06 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| aae01e94-3c8b-3474-9dbc-9fb7c93ca761 | -9.193 | -45.3342 | 2025-05-06 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 257bc5fb-2b38-3d2b-b6d4-d3ce4530f2d2 | -20.2744 | -55.4714 | 2025-05-06 14:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 6fbd4a71-d37b-3e93-8c8e-d02689ae3227 | -20.7222 | -54.4124 | 2025-05-06 14:30:00 | GOES-19 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 5672c301-8ab9-39c5-84af-ff3c7ce5deb4 | -20.2947 | -55.4682 | 2025-05-06 14:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 97.4 |


