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
| 7e40b4d9-0b11-3abf-9704-fc98bd2a7333 | -19.6418 | -56.9569 | 2026-01-21 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| e4266b72-7cca-34d8-996e-1c37c024f4be | -20.3481 | -57.9033 | 2026-01-21 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 4d103b0f-31ee-3496-84cf-9d254fd52817 | -19.6619 | -56.9541 | 2026-01-21 14:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 204.1 |
| 3176e6d3-903b-3435-b452-5bdc07f2b21c | -20.3283 | -57.8851 | 2026-01-21 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 0c4710a8-be7d-3264-ab59-5c615a890c1f | -19.4562 | -57.2536 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 180.8 |
| 0dd23abf-7fd7-3196-bbd4-f607510fc9d2 | -20.3481 | -57.9033 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 124.1 |
| b15a09b0-a6f6-331b-bfca-4cd7dcdd69ea | -20.3683 | -57.9005 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 1b9b5c6d-1104-35b6-8333-ff3b9067006e | -20.429 | -57.8922 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 4c4f746e-6907-3dc3-a500-c1e7709f5e5e | -20.3279 | -57.906 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.1 |
| 02acfe31-6dd6-349a-9fb9-0a3b1791f795 | -19.4161 | -57.259 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 3696bc88-5165-33c4-85ef-bbd179182e0a | -19.4365 | -57.2354 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.9 |
| b6220c77-2266-348a-b2bd-bba33c256e4f | -20.3485 | -57.8824 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 38799379-fce3-3b13-9d9b-27c3d1a5552a | -19.4369 | -57.2145 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| d013bbd6-43d3-323b-a978-6bf3e09529a1 | -19.4357 | -57.2771 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.5 |
| 9a978db8-4b34-3236-8bbb-621e8f79a8a7 | -19.4361 | -57.2563 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.1 |
| 68ca6eac-58b8-3a35-a2c5-600c934def34 | -20.3283 | -57.8851 | 2026-01-21 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.6 |
| 18481086-86cc-3f53-932f-ed3286fca371 | -20.41 | -57.8323 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.6 |
| 94233b2c-deba-33a0-bdf9-8240b0114181 | -19.4161 | -57.259 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.1 |
| ee94a1e8-21d3-39ae-bcbb-159b1722362f | -19.4361 | -57.2563 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.3 |
| db84ad6d-23b1-3eaf-aea5-398ae0b32d3f | -19.4365 | -57.2354 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 115471e3-17e0-3349-9b51-46b134ccab1c | -20.3283 | -57.8851 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 63c5c6d1-7bde-3890-9f83-a386863df75f | -20.3886 | -57.8978 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 146009a2-bb69-32fe-b5b7-67132d7aa39c | -20.3481 | -57.9033 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.3 |
| 264175e1-bf70-3a82-911b-0aa823d65a1f | -20.429 | -57.8922 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 2f570981-9664-3c6c-8619-6c468060ad51 | -19.4369 | -57.2145 | 2026-01-21 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.6 |
| 2080ee25-b030-38c5-8213-11e57b4f94f0 | -20.3283 | -57.8851 | 2026-01-21 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.6 |
| fa45a866-166e-35bb-b1cd-4fd1111b46ee | -19.4369 | -57.2145 | 2026-01-21 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.3 |
| 21b60630-92a2-380b-a991-8fb378f8572d | -20.3481 | -57.9033 | 2026-01-21 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| b475e076-2a68-3d33-90e6-1b2465563126 | -20.3279 | -57.906 | 2026-01-21 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| d3e9692a-f26c-3399-80d6-ad9ae664dfcb | -19.4365 | -57.2354 | 2026-01-21 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.9 |
| afaf1a6c-a8a2-3771-a5ce-21940c3aebc0 | -19.6627 | -56.9122 | 2026-01-21 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| f1216c29-f6ea-3210-b7d5-40fd7699fc56 | -19.6631 | -56.8912 | 2026-01-21 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 70.8 |
| b073ee35-f8d6-3ec4-b956-c1c59a78c142 | -19.6623 | -56.9331 | 2026-01-21 14:40:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 88.1 |


