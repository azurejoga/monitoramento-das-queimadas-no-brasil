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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8166262a-415f-3df9-9a88-0d8f88b244db | -11.1428 | -48.1043 | 2026-05-21 15:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 3af096ff-87ae-30f8-a7a1-98bc755556cb | -10.4798 | -49.3587 | 2026-05-21 15:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b1b3bc79-6274-386c-9324-d5d4f9114e30 | -10.4988 | -49.3567 | 2026-05-21 15:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6027b653-eb8c-3d1d-a530-f870426b231e | -10.666 | -48.249 | 2026-05-21 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| 18af6853-b396-3543-b40b-a732cf1e46a9 | -12.6011 | -44.521 | 2026-05-21 15:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 6f3f9b64-a48f-3186-8e89-76faa16be642 | -9.7368 | -47.029 | 2026-05-21 15:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| d5b2ae80-2182-3590-81b7-a8da87c11a93 | -11.1428 | -48.1043 | 2026-05-21 15:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 6900a372-eee7-3163-8300-6563293091ba | -10.4988 | -49.3567 | 2026-05-21 15:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 99d2b445-1e52-3c5f-8a42-4af753ea991d | -9.7368 | -47.029 | 2026-05-21 15:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 79b039d2-bb8d-3a7b-82ed-242688f23997 | -10.666 | -48.249 | 2026-05-21 15:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 87f774a9-13e1-36f7-9318-3570e3891154 | -9.7368 | -47.029 | 2026-05-21 15:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d7a00cd1-2db8-3980-b98d-f90386a81e2e | -10.4988 | -49.3567 | 2026-05-21 15:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 6fcffc12-f218-3839-879c-cd38f9c3d6fb | -12.6011 | -44.521 | 2026-05-21 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 4f94d3bf-887f-3ceb-b763-774f4d2e4a09 | -11.1428 | -48.1043 | 2026-05-21 15:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| c868536e-2f4c-3502-93bb-7e22e8cea808 | -10.4798 | -49.3587 | 2026-05-21 15:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 083bf5ad-fe30-3f86-a20d-459244de0487 | -11.2743 | -49.4642 | 2026-05-21 15:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 1ac8f6a0-9c7d-336a-9360-d82ab0d262b1 | -12.6011 | -44.521 | 2026-05-21 15:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4ff14803-ee90-3d91-910c-e1487b144ea5 | -10.4988 | -49.3567 | 2026-05-21 15:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 826658d1-c5c8-327c-a0ac-cd95e0229f26 | -10.4798 | -49.3587 | 2026-05-21 15:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| afa4e186-f416-341e-afd6-dc6649cb66d7 | -12.6011 | -44.521 | 2026-05-21 15:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e0d1c198-a890-3a4b-9759-012b245f00d7 | -11.2743 | -49.4642 | 2026-05-21 15:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 8aa3a196-ff74-3881-8d76-f67abfb6bb95 | -10.4988 | -49.3567 | 2026-05-21 15:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| cb348062-23fd-3272-be9a-de38c78eaa6f | -11.2743 | -49.4642 | 2026-05-21 16:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 3d48c9fa-2567-39af-95a4-2bc2234ab839 | -10.4988 | -49.3567 | 2026-05-21 16:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 0644873b-88d1-3063-9a46-718ea23d6662 | -11.2743 | -49.4642 | 2026-05-21 16:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| d9f6c28d-7f53-3981-809c-17f4657cb599 | -10.4988 | -49.3567 | 2026-05-21 16:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| dd6384f5-d902-337d-8d62-fcd9816ec4f4 | -12.0682 | -45.2768 | 2026-05-21 16:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7ba8ae94-fdd1-31d4-bb46-43cfddf87735 | -11.2743 | -49.4642 | 2026-05-21 16:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 6c05a8ff-55d5-36a1-82de-f30bdf682b65 | -10.4798 | -49.3587 | 2026-05-21 16:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 30db6cf5-9e2c-38e2-a703-2cfb234fd272 | -11.1428 | -48.1043 | 2026-05-21 16:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 4bb575e4-675f-33ca-8924-2ea5b8d1a444 | -11.2743 | -49.4642 | 2026-05-21 16:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 150.9 |
| e9cf33ac-3ec0-34c9-8a3e-6adee2aa6cb9 | -11.2743 | -49.4642 | 2026-05-21 16:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 147.0 |


