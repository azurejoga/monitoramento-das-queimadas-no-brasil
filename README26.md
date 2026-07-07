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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21ead13b-b29b-329d-a96e-5aaee6f730a2 | -6.9323 | -43.7264 | 2026-07-07 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 5982371a-4ae5-38e8-bf86-fec6ae867d36 | -11.6592 | -44.5741 | 2026-07-07 16:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 2c16e66f-131f-36f0-a7fe-3e7c97ba7955 | -13.3352 | -54.382 | 2026-07-07 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 7bdce49a-d57d-3544-85af-d47c73a35017 | -11.6789 | -44.5479 | 2026-07-07 16:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 366b2045-91d3-36c8-9577-0cf64aba524c | -13.278 | -54.3675 | 2026-07-07 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| af2208bc-1b90-3484-9186-d172726cc43c | -6.9135 | -43.7281 | 2026-07-07 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 152.4 |
| b9b7820e-63f8-37b8-8485-7f031f51225b | -14.3896 | -58.5162 | 2026-07-07 16:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| fe8da382-29b8-367a-8262-9886df9d8a12 | -13.2783 | -54.3469 | 2026-07-07 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| fdcf8850-75f5-351e-a5fc-2b87da5c1037 | -13.2777 | -54.3882 | 2026-07-07 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d4074e7e-3d58-3cc6-b6dc-82e9a8d644df | -13.3163 | -54.3634 | 2026-07-07 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 95767eca-747c-354f-82e1-45a4196ae5c2 | -13.5289 | -52.9459 | 2026-07-07 16:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 4b9a867c-c53a-39db-baa4-243d99acf2d5 | -11.6785 | -44.5712 | 2026-07-07 16:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 145.6 |
| d9930116-b0b9-351d-bfdd-3176ff46138b | -11.6785 | -44.5712 | 2026-07-07 16:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 807e808d-c422-3bd9-8c8a-00fd43c2813b | -13.2783 | -54.3469 | 2026-07-07 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 50984f2c-d5d5-3763-b428-059dac5e0ef4 | -11.6789 | -44.5479 | 2026-07-07 16:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b7b2d5ac-d437-316d-b199-d1181cc5eaa4 | -6.9323 | -43.7264 | 2026-07-07 16:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 5add17ab-1bd1-369e-b1c0-abf894725cc2 | -13.5289 | -52.9459 | 2026-07-07 16:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 03c9e4ff-a7bb-3384-b21d-890df5a848e8 | -13.2969 | -54.3861 | 2026-07-07 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 4ac036f3-9694-3546-9fa0-ae6a68eab7a8 | -6.9135 | -43.7281 | 2026-07-07 16:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 263.9 |
| 87cdff33-c1de-31b0-ad12-4e77c05f9f7c | -13.3157 | -54.4047 | 2026-07-07 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |


