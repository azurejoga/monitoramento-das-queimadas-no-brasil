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
| 77516783-9f33-3aac-84f0-d4c13805fa21 | -19.6836 | -57.9712 | 2025-01-17 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.9 |
| d34dccdf-2f0e-305f-b4a6-802956fa141c | -19.6832 | -57.992 | 2025-01-17 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 06074d41-6657-3fa7-8056-5b2471e92946 | -19.7022 | -58.0517 | 2025-01-17 13:40:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.5 |
| a0966445-c2be-34fe-81ad-e6eec67f698a | -19.7033 | -57.9894 | 2025-01-17 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.0 |
| dbb88986-42c5-3941-9230-15f98d8157cb | -19.7022 | -58.0517 | 2025-01-17 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 46ac3bf8-922b-3887-8f93-8febdefa21cc | -19.7223 | -58.0491 | 2025-01-17 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| 53c40793-277d-3b7c-9e9b-b12018a6f25b | -19.6836 | -57.9712 | 2025-01-17 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.8 |
| 325c09cc-9e5f-33a4-bf04-38ff259fc473 | -19.6832 | -57.992 | 2025-01-17 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.2 |
| ff87f5cf-9b5d-3143-82f0-958875ef3c34 | -19.7022 | -58.0517 | 2025-01-17 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.4 |
| 69dddcc2-3da5-34b5-b534-75f8b4318eaa | -19.7223 | -58.0491 | 2025-01-17 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 966fd2a1-7955-3039-98b0-cbc5acc45e84 | -19.6836 | -57.9712 | 2025-01-17 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.5 |
| 1fea7828-4a63-3710-9f96-4a2e903e14d7 | -19.7022 | -58.0517 | 2025-01-17 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| bcc960ef-17e2-3f91-b656-9fa77292017b | -19.7033 | -57.9894 | 2025-01-17 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.5 |
| e3980f1c-0e0d-3c5c-9d75-30bb1b008294 | -19.7424 | -58.0465 | 2025-01-17 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |
| ec1d98e5-6645-3dca-98ec-968aadc6d49b | -19.7223 | -58.0491 | 2025-01-17 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 1582520f-e3ba-316a-81ae-1052c7030f4b | -19.6832 | -57.992 | 2025-01-17 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.1 |
| f037ac64-e764-3c0e-be5e-c24a3e77e920 | -28.7599 | -55.6114 | 2025-01-17 14:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 86.5 |


