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
| 9800e5ed-16a2-3deb-86d2-448ffc914632 | -28.7367 | -55.6396 | 2025-01-13 02:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 138.2 |
| a9022092-8159-3f6f-810f-349dbceb5979 | -28.7599 | -55.6114 | 2025-01-13 02:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 306.3 |
| 215eb610-e8e0-3936-aa3f-7e537fbf452a | -28.7367 | -55.6396 | 2025-01-13 02:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 194.8 |
| 34ee0788-59f6-3370-bc31-5f802882ac0d | -28.7585 | -55.6576 | 2025-01-13 02:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 64.0 |
| 4e7e9d9e-8d8f-3e0e-a8f2-9fb3361402d8 | -28.7374 | -55.6165 | 2025-01-13 02:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 147.4 |
| 93fd5c82-a581-3afc-8bcf-31b511a5bff4 | -28.7592 | -55.6345 | 2025-01-13 02:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 335.6 |
| 8283846c-a92e-39e4-89b3-c6fa24a1fc9b | -28.7599 | -55.6114 | 2025-01-13 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 427.0 |
| c7d39db6-ef32-349c-9012-5273d867f7c2 | -28.7374 | -55.6165 | 2025-01-13 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 104.4 |
| 012529ec-788b-3811-a387-de59cb274e51 | -28.7367 | -55.6396 | 2025-01-13 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 188.1 |
| 53f21192-3f57-35e1-bb91-0979f175d751 | -28.7585 | -55.6576 | 2025-01-13 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 72.5 |
| feba3c6d-8218-3fa8-bd76-34f3cdac97a7 | -28.7592 | -55.6345 | 2025-01-13 02:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 518.1 |
| 67987246-4009-3268-ae30-f48d1c9fb052 | -28.7592 | -55.6345 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 500.1 |
| 97e011d6-cb4b-331b-96cf-bee5c75d2c14 | -28.7824 | -55.6063 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 111.2 |
| a334dad6-80e7-3be3-a2ff-4b1a16dad3f0 | -28.7817 | -55.6294 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 73.3 |
| 913d9a23-76ce-34f5-986d-82fcf760eea4 | -28.7374 | -55.6165 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 198.2 |
| fb66047c-64cc-32fe-b8d2-d125e648bd80 | -28.736 | -55.6627 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 187.8 |
| 60707212-9ec5-3038-aa98-6f459f5eaa65 | -28.7585 | -55.6576 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 131.6 |
| 511c6460-2858-380f-b822-a7956f2cd811 | -28.7367 | -55.6396 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 465.4 |
| 6e3c8d0e-5b85-3699-bccd-2b36960d6eca | -28.7599 | -55.6114 | 2025-01-13 03:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 445.3 |
| 96683f9d-7200-3071-bb6e-5e36813559f3 | -28.74 | -55.62 | 2025-01-13 03:00:00 | MSG-03 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 00324af3-bf93-3dec-ba6c-846c32456678 | -28.7367 | -55.6396 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 297.9 |
| 46237f1d-7e72-3ef9-b378-7fa0ea6bdeb6 | -28.7605 | -55.5883 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 78.3 |
| d24aef6d-f3d0-3647-a61b-aa8678cf8e3c | -28.7599 | -55.6114 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 568.6 |
| 5b757f8d-35da-3507-8f36-f8127ee695f3 | -28.7592 | -55.6345 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 482.4 |
| f3da637d-dfc4-3983-ad14-9711edb55488 | -28.7374 | -55.6165 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 185.7 |
| e776ed72-0bda-3dab-96b2-129f286fd045 | -28.7824 | -55.6063 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 161.3 |
| b792e3fb-b4e5-33d6-9a5b-a2d835223946 | -28.7817 | -55.6294 | 2025-01-13 03:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 100.9 |
| 830ac06e-fd26-3237-b9bd-7ab1a2d51de1 | -3.32358 | -39.7002 | 2025-01-13 03:19:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 166c46b0-6604-3bbf-b500-b4cf12f4c1be | -28.7817 | -55.6294 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 83.7 |
| 2ae69227-e07f-32bb-9b2a-05e4f9f9016c | -28.7824 | -55.6063 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 106.8 |
| b5beb8a6-fa5d-3a22-811d-0573d2333610 | -28.7374 | -55.6165 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 108.7 |
| aaaf8988-c2d0-3db6-8f7a-8a6f187f0c32 | -28.7605 | -55.5883 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 87.2 |
| e2017112-eb83-37bb-b622-0aaf4369290a | -28.7367 | -55.6396 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 158.6 |
| 638b11e3-7156-3ac9-b662-f698f0f6f02d | -28.7599 | -55.6114 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 581.3 |
| 6751a095-78ba-384a-bb3a-89e065b87b75 | -28.7592 | -55.6345 | 2025-01-13 03:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 498.0 |
| 40ead609-a470-30ca-ab34-4eba1fb0155e | -21.44324 | -48.61111 | 2025-01-13 03:25:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0af8a0af-fdee-32ac-a35f-71980427b344 | -20.71214 | -48.63859 | 2025-01-13 03:25:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1cdee8bb-ccfa-3f49-a1b3-4d6e13391ac4 | -22.20499 | -47.70799 | 2025-01-13 03:25:00 | NOAA-20 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13d8d98c-3e0c-315c-980b-aa9808ab7bc1 | -21.4414 | -48.61827 | 2025-01-13 03:25:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1ee71e61-fa8a-329d-8590-f7902ad48a0a | -21.44287 | -48.61939 | 2025-01-13 03:25:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c94640e4-e337-3b05-b996-b99b606153cf | -22.19847 | -47.70644 | 2025-01-13 03:25:00 | NOAA-20 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d40d37e9-a2d9-3c00-b286-4055a6b8ae09 | -21.44465 | -48.61225 | 2025-01-13 03:25:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a5d3b38-f314-30a6-88e8-cdbfd4012f0d | -28.7367 | -55.6396 | 2025-01-13 03:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 98.1 |
| b4e116d6-0282-3dbf-94d7-59bb1079a0eb | -28.7592 | -55.6345 | 2025-01-13 03:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 484.0 |
| f9800cc6-bb44-3b8f-95da-31aaeda13fdb | -28.7374 | -55.6165 | 2025-01-13 03:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 67.4 |
| 1a2a5f7f-3f2d-3fab-8a1f-2f79301c85eb | -28.7599 | -55.6114 | 2025-01-13 03:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 431.0 |
| 33044405-50fd-3c1b-abde-09157811e9b0 | -28.7817 | -55.6294 | 2025-01-13 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 64.2 |
| 74c2d8c2-6c49-355a-8a53-7cf4cb3955d2 | -28.7367 | -55.6396 | 2025-01-13 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 93.5 |
| 1fccaa37-91d4-331b-8697-19ba75453099 | -28.7592 | -55.6345 | 2025-01-13 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 296.1 |
| 8b758ab4-6296-3113-887c-06c4555313d8 | -28.7824 | -55.6063 | 2025-01-13 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 75.5 |
| 5f0c0944-02a9-323d-9207-2833861ff4bf | -28.7605 | -55.5883 | 2025-01-13 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 64.0 |
| 22c59ed3-bf44-3e20-b598-af4640a1bf7b | -28.7599 | -55.6114 | 2025-01-13 03:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 338.2 |
| 99e8e992-8335-322a-85c4-a1ca674b958b | -28.7374 | -55.6165 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 73.2 |
| 5b0d8290-6cd3-3861-ba75-7bbbb1838e16 | -28.7599 | -55.6114 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 368.3 |
| cbb2c536-5b5a-373b-9ad9-937584e85ad8 | -28.7605 | -55.5883 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 68.1 |
| bdcfd800-423e-383f-86f3-2b781a17c4da | -28.7367 | -55.6396 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 126.8 |
| ec0b3960-ce82-39c5-ba47-8ea5218b914e | -28.7817 | -55.6294 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 108.7 |
| 83265f6a-59fd-3041-9288-44114bac9e7c | -28.7592 | -55.6345 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 355.6 |
| fd679a6a-0881-30da-8c60-5916b7f76649 | -28.7824 | -55.6063 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 133.0 |
| acd0e349-2663-3894-9d92-59b7da17abdd | -28.7585 | -55.6576 | 2025-01-13 03:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 67.0 |
| 630e2eb8-8773-3c7b-8fe4-24a53b70a439 | -28.7374 | -55.6165 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 101.9 |
| 7258c4b6-447f-34b4-a4fa-eee23efd1fe9 | -28.7817 | -55.6294 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 92.3 |
| b44a691e-4157-399c-9502-9b5bb32ab2f0 | -28.7599 | -55.6114 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 300.8 |
| fa2fcd67-8361-379d-a7e5-c6349f9c6abf | -28.7592 | -55.6345 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 437.8 |
| fef7f485-bfb3-367a-8838-2c973630bdac | -28.7824 | -55.6063 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 120.3 |
| 228f96bb-5a61-3c91-b3ee-a915927a7abe | -28.7367 | -55.6396 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 183.9 |
| 229d7710-6f22-33ed-a6bc-5413aed8c540 | -28.7585 | -55.6576 | 2025-01-13 04:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 70.5 |
| 630aa5b0-89ce-36e8-adc1-a6d09bbac1f7 | -28.7374 | -55.6165 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 80.6 |
| c802d135-d648-3b5d-8867-0a9816a06225 | -28.7817 | -55.6294 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 106.6 |
| f4880a1b-a506-383e-889d-ead2e13d6d6c | -28.7592 | -55.6345 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 323.7 |
| 3c626802-27f7-3c3f-9776-a3f8fbfa525c | -28.7824 | -55.6063 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 121.0 |
| e1315b53-b0bf-32f5-9561-7ff4859d40be | -28.7599 | -55.6114 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 263.0 |
| 3391250d-2919-396b-8e12-dab09b3fe6f2 | -28.7585 | -55.6576 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 64.9 |
| b27f6326-35fe-313e-8977-892661bb9242 | -28.7367 | -55.6396 | 2025-01-13 04:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 134.4 |
| f0201f2e-5a80-34d4-b77e-b035bf4b21c4 | -1.46719 | -45.71148 | 2025-01-13 04:12:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| ff977585-e152-3ecc-b85f-50f9a4190545 | -1.4709 | -45.71207 | 2025-01-13 04:12:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 70362b75-18ee-3bcd-952a-ef68d26cc9d2 | -5.21595 | -43.30051 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d5c886a-eea0-3799-84eb-c881142cc8f8 | -5.21541 | -43.30396 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cacf0721-6380-319e-95ec-6145598dd28f | -2.42786 | -48.05434 | 2025-01-13 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31b410ed-362f-3c89-8bc2-4752c2942b0b | -1.87805 | -48.71416 | 2025-01-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34bb2569-3eca-354a-b090-29c8cddb0dcc | -5.21926 | -43.30101 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e7f1b1a-4db7-307a-9c2b-edd4fa4e6a15 | -5.21157 | -43.3069 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0de36aa6-3cfc-3d67-b7bd-380f2764419d | -5.20881 | -43.30294 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cdb8967-e55c-31fd-bb2b-91c8c2facdc8 | -5.21649 | -43.29705 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c68558-509b-3c74-825b-7962d62999b6 | -2.42772 | -48.05453 | 2025-01-13 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8dec90ab-3e6e-38f9-a36f-abfc25b6f3a1 | -2.01534 | -52.07689 | 2025-01-13 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9694546c-0c0b-3693-bf24-0ffddc355e18 | -5.21319 | -43.29655 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7e92032-b5c1-3551-b048-6c360594952d | -2.606 | -47.52885 | 2025-01-13 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f97d46c0-dc0b-3078-8b71-a1fac618b62e | -5.2055 | -43.30243 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 96b30c43-de23-3693-95f5-b10dcf6a66a2 | -5.21211 | -43.30345 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d1c6da4d-0253-37c2-b89a-4c652cc22c3d | -5.20826 | -43.30639 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7034bee-176e-331f-ac2f-cd328771f45c | -5.20604 | -43.29898 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aae3e606-ddd2-3d40-a907-90d3afde6d74 | -3.28901 | -46.5903 | 2025-01-13 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee031508-207b-34a2-97f0-942fccd220f1 | -5.20935 | -43.29948 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95b44cee-1768-36ce-aa64-c6857fcbec7f | -5.21265 | -43.3 | 2025-01-13 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c61dc7c-861f-360a-aca5-c50c50f08969 | -2.60543 | -47.53249 | 2025-01-13 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10f43717-f0d2-3dd5-94e8-d38ba544628b | -3.50481 | -39.3097 | 2025-01-13 04:14:00 | NOAA-21 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| af576ac7-37e6-3ad3-a975-824ce6a98828 | -15.07936 | -48.94407 | 2025-01-13 04:16:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a32c8e9-bb70-3942-aba5-e4bd00ad603a | -19.81949 | -53.83143 | 2025-01-13 04:18:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff49c85d-1aa0-3589-9e58-0fa2bdade7e4 | -21.44613 | -48.6079 | 2025-01-13 04:18:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
