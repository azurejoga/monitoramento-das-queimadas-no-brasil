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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2be57335-b292-317f-897b-73211a958eb4 | -20.99947 | -51.79726 | 2025-03-15 05:14:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bc0a083d-b480-3b17-80ff-e8821fed69c3 | -15.26558 | -51.47704 | 2025-03-15 05:14:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94f6b41c-b0bc-3e1c-a341-182bccbd9081 | -18.30194 | -54.57153 | 2025-03-15 05:14:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b9feee0-9e72-37db-ad8c-ca1e464a66fa | -15.62885 | -57.31212 | 2025-03-15 05:14:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45267d6f-e917-3b5e-b8f5-cf67f9eaa740 | -21.99483 | -48.79499 | 2025-03-15 05:14:00 | NOAA-21 | ITAJU | SÃO PAULO | Brasil | 3522000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 1f1108df-eda4-3089-a40a-192bd508c3e9 | -16.07526 | -53.75632 | 2025-03-15 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee13a860-71e8-3ef9-b8fd-6e301aeb022b | -16.07104 | -53.75565 | 2025-03-15 05:14:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a11cc1c-c13a-3712-a53c-9fbf25b6b7ee | -15.63137 | -57.31153 | 2025-03-15 05:14:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f46b63f4-0949-3f68-b3cb-3354b9d25715 | -18.53125 | -56.17383 | 2025-03-15 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7cf0d8de-d617-3ae8-86d6-9d53ce112c74 | -7.30849 | -55.31181 | 2025-03-15 05:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff4d555f-93db-3637-8f1f-dfd55d55c186 | -16.07539 | -53.75284 | 2025-03-15 05:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8cfeff0d-755a-3cae-82bc-43a5acdfeb5a | -16.07486 | -53.75819 | 2025-03-15 05:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 069dd996-d425-3607-a112-2ea092365999 | -16.07289 | -53.75755 | 2025-03-15 05:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f59a85e9-7013-39f3-83f3-7ce5227d6d54 | -16.07344 | -53.75221 | 2025-03-15 05:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0240fc1-6d1a-3ebd-a6fa-9da4a57a250e | -16.06901 | -53.75193 | 2025-03-15 05:38:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8cf3ba6-2f89-3f6b-90d2-55414bf7b2d4 | -12.7218 | -46.2773 | 2025-03-15 12:30:00 | GOES-16 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| cf1289b9-75e9-32ce-ab0e-c28ee8df5653 | -12.547 | -45.342 | 2025-03-15 12:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5489398d-e1dc-3d65-89ce-92d22f9879af | -12.547 | -45.342 | 2025-03-15 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| f98e0c73-21b1-3658-abca-b6b3e23b09a0 | -12.547 | -45.342 | 2025-03-15 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 98927d0f-b16d-3508-b6d1-7898b76508db | -12.547 | -45.342 | 2025-03-15 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7952133d-b98b-3ec3-9089-7b957023572b | -12.547 | -45.342 | 2025-03-15 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 54bb18d7-94c4-357e-be7e-3379432b1411 | -12.547 | -45.342 | 2025-03-15 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 4a806843-c374-34b5-8378-f5d4286a55e1 | -12.547 | -45.342 | 2025-03-15 13:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 201.5 |
| ca500573-c162-3eae-897d-1364079159d9 | -12.547 | -45.342 | 2025-03-15 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 162.2 |
| a4a06e78-7791-3a77-8989-c6fa699e4854 | -12.5277 | -45.345 | 2025-03-15 13:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e3216feb-235f-36ee-abc3-210b74173cf8 | -10.5806 | -45.1413 | 2025-03-15 13:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 00c7ab51-3c4a-3d52-81b9-365d02f43184 | -12.547 | -45.342 | 2025-03-15 14:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 68c90053-0781-33f9-acbb-c5864087013e | -10.5806 | -45.1413 | 2025-03-15 14:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 06b3b36d-f157-33d5-b6dd-9ade311c3bc2 | -12.547 | -45.342 | 2025-03-15 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 4c61c8ad-53ed-338e-b308-6f1194fa1c62 | -10.5806 | -45.1413 | 2025-03-15 14:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 842371ad-0989-3e4c-8df3-3cb69c6a1c4b | -12.547 | -45.342 | 2025-03-15 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 754d3623-dac0-3d3b-a7b4-1e1f0dd983d6 | -12.547 | -45.342 | 2025-03-15 14:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 01dd87d0-8b16-335c-9090-1ecf39bdcaba | -10.5806 | -45.1413 | 2025-03-15 14:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8a9f069f-482d-3640-b3c4-5d5898d50e81 | -14.2128 | -47.0183 | 2025-03-15 14:30:00 | GOES-16 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |


