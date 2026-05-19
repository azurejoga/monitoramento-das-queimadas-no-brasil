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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9408f145-e625-378f-b309-24a05095c6bc | -12.2215 | -44.2543 | 2026-05-19 13:40:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8f991d1e-a91b-33af-a23f-6b4ae7e4eb13 | -12.6011 | -44.521 | 2026-05-19 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| c9fd975b-0a4d-34f1-ab93-3bb7e381ffd8 | -12.2215 | -44.2543 | 2026-05-19 13:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| e5ae7282-723e-31a0-ae2c-1209e08c21b2 | -12.6205 | -44.5179 | 2026-05-19 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e6a08b30-25c9-3eb0-8c63-f124b3a392d3 | -12.6011 | -44.521 | 2026-05-19 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 281434c8-cd3e-3e59-9cbe-9e730710bd4a | -12.6205 | -44.5179 | 2026-05-19 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 1d3f86fe-1532-33aa-956b-92d9a49547d8 | -12.6011 | -44.521 | 2026-05-19 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| aaa4c023-b2dd-357e-ae6b-d6c885391a07 | -12.6205 | -44.5179 | 2026-05-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 135.5 |
| 7262d017-5678-35aa-91b6-d0193914fdef | -12.6011 | -44.521 | 2026-05-19 14:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 5e3a1714-5e78-386b-a8a4-f7835b52b6b3 | -12.6011 | -44.521 | 2026-05-19 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 999400ae-fbba-3c2c-ac66-b742e05830e6 | -12.6205 | -44.5179 | 2026-05-19 14:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| fa216d0b-322f-3f33-b68c-98e1c9085bbc | -12.6011 | -44.521 | 2026-05-19 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 9a902552-e67a-3087-be3f-3f6f8411a20e | -10.4535 | -49.8999 | 2026-05-19 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 103db796-f7e4-3465-818d-4d504696169f | -12.6205 | -44.5179 | 2026-05-19 14:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 38aefa8b-4508-396a-88b9-866be8ecc923 | -12.6011 | -44.521 | 2026-05-19 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 194.9 |
| 249177f7-0d52-3b76-987e-52ec6825db09 | -12.6205 | -44.5179 | 2026-05-19 14:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 153.8 |
| 61fc0c4d-24e7-39d3-b658-0cb3cc8e8ba7 | -10.4928 | -49.7884 | 2026-05-19 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| cd74128e-60e7-337b-83ae-afc71f9e087f | -15.6121 | -48.0471 | 2026-05-19 15:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 131.0 |
| bbbd8ad4-c07a-31d4-b14a-4a83bfbe2c2d | -12.6011 | -44.521 | 2026-05-19 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 679005cc-6214-3f1c-ab66-f26b1e8e03b7 | -12.6205 | -44.5179 | 2026-05-19 15:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| daf6a0ae-d9c1-395d-ba0c-772282e876ef | -12.6205 | -44.5179 | 2026-05-19 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| dc6bd7a1-1a1e-3c64-9151-9a994dd72b86 | -12.6011 | -44.521 | 2026-05-19 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 191.8 |
| 963e1792-590b-3f4a-9b89-369a7d17d0df | -12.6011 | -44.521 | 2026-05-19 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 220.7 |
| c60e5faa-4767-388f-a4f0-d8bd277fd001 | -12.6205 | -44.5179 | 2026-05-19 15:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 0b61c3c7-75df-3f6d-bd9f-0a5938a25b72 | -12.6205 | -44.5179 | 2026-05-19 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 32778398-1e5e-3463-8646-c7092f4fbd6f | -12.6205 | -44.5179 | 2026-05-19 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 35b3d418-7382-3811-8082-aa85eee47f0a | -12.6011 | -44.521 | 2026-05-19 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 216.5 |
| 03610718-8f26-3797-89fe-d05213fa0d4e | -12.6011 | -44.521 | 2026-05-19 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 247.0 |
| 5a05b555-f411-307c-83ef-852f558c7f13 | -12.6205 | -44.5179 | 2026-05-19 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| fa4baace-e482-3ace-b2b5-2b406513d7fc | -12.6011 | -44.521 | 2026-05-19 16:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 227.1 |
| af63a640-3275-3431-ada0-1f517acfc247 | -12.6205 | -44.5179 | 2026-05-19 16:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 194.9 |
| b8dddd67-fce2-3274-8b07-ff0d975cc9f8 | -12.6011 | -44.521 | 2026-05-19 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 0fd4cafe-e463-34ca-8fbd-1241bc1fa100 | -12.6205 | -44.5179 | 2026-05-19 16:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 74c5240c-1e51-3596-ab73-39ddab736b25 | -10.8548 | -49.6199 | 2026-05-19 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 1e2eaf2e-9b51-3901-9612-fa9a08ff2e79 | -10.8548 | -49.6199 | 2026-05-19 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| f6a3a4a3-c2ca-365f-839a-991833f3f0b3 | -10.8211 | -49.3211 | 2026-05-19 16:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |


