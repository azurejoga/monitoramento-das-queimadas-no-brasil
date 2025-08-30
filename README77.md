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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b3b4eec-63bd-3361-b2d4-3a7116131f60 | -12.0148 | -44.0054 | 2025-08-30 05:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| b68d35c8-973f-3cfe-aa75-ada87c147fae | -9.462 | -60.549 | 2025-08-30 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7ae66fd1-e4a7-3213-84c5-828007dd6671 | -9.4432 | -60.5692 | 2025-08-30 05:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 5b096323-d60e-36c7-8741-67184aea378d | -9.4495 | -62.3675 | 2025-08-30 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 095758c8-c456-34df-a549-bb8aa16d4e8c | -12.0153 | -43.9818 | 2025-08-30 05:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 1159a8d2-ce9b-3d08-8255-345810a5defa | -9.4684 | -62.3286 | 2025-08-30 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 186.5 |
| 4a7705e4-f7ca-34bd-a71d-5cc71396f347 | -9.1155 | -65.7699 | 2025-08-30 05:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 71d59e49-448a-3006-80a8-64f106c1c479 | -11.8556 | -46.4714 | 2025-08-30 05:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e85fcde9-d5a3-3982-9b50-0c31604da400 | -9.4498 | -62.3294 | 2025-08-30 05:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 266.0 |
| 89db6328-5571-35e7-810d-e09a9eb55719 | -11.8369 | -46.4514 | 2025-08-30 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 173.3 |
| e508d611-6f96-3139-966a-8fe2de389d0e | -11.8572 | -46.3807 | 2025-08-30 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 8b490fda-386e-3dc7-9f1d-98a9847ccf21 | -11.876 | -46.4007 | 2025-08-30 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 77682130-7b45-3643-b166-71763cb7af7f | -9.4498 | -62.3294 | 2025-08-30 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 266.7 |
| 0dfc7fe4-550a-33f7-bf3d-32a678aca79a | -13.3817 | -47.015 | 2025-08-30 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6d682934-3f33-3992-9d6d-709ea5ca9fcf | -9.4432 | -60.5692 | 2025-08-30 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c99ecbb8-8f8f-31e3-835b-54d823e1a49e | -9.1155 | -65.7699 | 2025-08-30 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 598b2221-b221-3b64-a79d-86f399a5136d | -6.5451 | -44.8643 | 2025-08-30 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3734a92b-2867-38e4-ac71-b05ce7f4cdc8 | -12.0148 | -44.0054 | 2025-08-30 05:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 6d1cf937-f70d-3e77-911c-a56f13dbfa32 | -13.3821 | -46.9924 | 2025-08-30 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 607228db-749e-3b3e-888c-34d941c498a4 | -6.1665 | -43.3273 | 2025-08-30 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 413a5e69-2b6e-317e-aad4-1ba29ee2eb96 | -11.856 | -46.4487 | 2025-08-30 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4bcd8709-f33a-37f4-8ad7-e9501fe38f88 | -12.0153 | -43.9818 | 2025-08-30 05:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9434d661-ebdb-31db-9e1c-b8512121ab36 | -13.5373 | -46.9456 | 2025-08-30 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 03c3de59-c568-3a10-834c-762bf013d3f1 | -6.1853 | -43.3257 | 2025-08-30 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 720a5301-982e-3c8f-8964-0724dd8e65ba | -9.4497 | -62.3485 | 2025-08-30 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 213.3 |
| 74445374-24d8-30b2-a994-b76104e821fb | -6.185 | -43.3491 | 2025-08-30 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 9c9fdba8-cf04-328f-ba07-d6c4ba12f6bd | -6.5263 | -44.8659 | 2025-08-30 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 388.7 |
| 1df10db8-d917-3d86-86e2-fc5717408d55 | -9.4683 | -62.3476 | 2025-08-30 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 4856ef34-c9b9-3582-80b2-ca8117b73644 | -11.8764 | -46.378 | 2025-08-30 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 37071bfe-1669-376a-adbe-3dae099488d1 | -6.5266 | -44.843 | 2025-08-30 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| 628d2de9-b923-3736-a98f-31119d9cde4e | -9.4684 | -62.3286 | 2025-08-30 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 70d3a8af-44e7-3867-bdc6-30a5b5fa2c4f | -9.4495 | -62.3675 | 2025-08-30 05:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7ef90015-aef3-30ec-a437-d60baca5c0f1 | -6.5453 | -44.8415 | 2025-08-30 05:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 5193ea9c-bda1-3c3b-9ed1-72e0beeb6531 | -13.3623 | -47.018 | 2025-08-30 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 60.3 |
| ec2117e8-2e58-3911-b236-9a69c669c12b | -6.1663 | -43.3506 | 2025-08-30 05:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| ec02498b-b96b-3417-a7e6-9886c196a810 | -13.3825 | -46.9697 | 2025-08-30 05:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ad4c9f80-fecc-38e0-8b7b-4043eba1cf8e | -11.8365 | -46.4741 | 2025-08-30 05:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 9b253f42-dd09-3385-931e-6915620da376 | -9.4433 | -60.5499 | 2025-08-30 05:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |
| a8d7635e-0e7e-3190-8581-50d99c0b03b1 | -9.0799 | -65.4536 | 2025-08-30 05:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 5d7e9e14-2363-3411-a310-191b9b3eba32 | -6.5451 | -44.8643 | 2025-08-30 05:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 36d23ad5-b561-37be-8dc2-c5bc704b171c | -6.185 | -43.3491 | 2025-08-30 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 202.1 |
| 00e32b57-61b7-301e-9712-0c1ed022f8f7 | -9.0614 | -65.4355 | 2025-08-30 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| e1e1dbe9-3aff-3199-b7cf-e13ee6e30f07 | -13.3628 | -46.9953 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 22448735-7d88-3683-a177-ad90ede66fad | -13.3645 | -46.9047 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b7925473-9428-3b17-9f36-76b4e20e8970 | -6.4253 | -45.6214 | 2025-08-30 05:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 2a284587-ff94-3166-b28f-421f52804957 | -13.3843 | -46.879 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c335b3ec-5743-3e4e-ab7c-ce13a96216d9 | -11.8369 | -46.4514 | 2025-08-30 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 1e7543f4-f5b5-3ff5-9f79-ed6a52b965f3 | -12.0148 | -44.0054 | 2025-08-30 05:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2d30b7b4-d64c-3dea-8b58-2627e3724f76 | -13.3649 | -46.882 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 64ee3400-7a42-39cc-a7ba-43c62c847f87 | -13.5373 | -46.9456 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 78e4710d-8df2-30c0-830e-dc6b61e064d8 | -9.4683 | -62.3476 | 2025-08-30 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 173.2 |
| e98b6707-40fa-35d5-b161-68dfcd17c42a | -13.3817 | -47.015 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| e85d23f8-54f9-36b5-9b7f-1758c7c77047 | -6.4255 | -45.5989 | 2025-08-30 05:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| faf99b3f-e249-3041-99b5-1e24aceeafb3 | -13.3821 | -46.9924 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 822c8277-ba0c-3309-8d9e-8512aebe4ad8 | -6.4066 | -45.6229 | 2025-08-30 05:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 143f054a-ddec-3e49-b498-530e9b3edf04 | -9.0613 | -65.4542 | 2025-08-30 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 33b21d6c-b557-3750-a9cd-22ba6e2593d1 | -9.1155 | -65.7699 | 2025-08-30 05:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 70c82b8d-d627-3036-96af-d98c96fb591c | -6.5263 | -44.8659 | 2025-08-30 05:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 61e9ed35-f3d8-3a5f-80d5-86759b38804c | -6.1853 | -43.3257 | 2025-08-30 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 54b51b10-4bdc-34e8-8cac-f0ebeb43cefe | -6.1663 | -43.3506 | 2025-08-30 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d587a4ce-46e2-3663-8dcc-c83c385242df | -9.4432 | -60.5692 | 2025-08-30 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 27fcb636-ac22-3237-a545-07a53b0969bf | -6.1665 | -43.3273 | 2025-08-30 05:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| f4762161-694d-37d4-b13e-cdb08c1eb44d | -13.3825 | -46.9697 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 849707fe-9a6e-3b71-8320-dd01b92a467b | -9.4684 | -62.3286 | 2025-08-30 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 184.4 |
| 82c54196-1f6f-3dc9-bc5e-4e23ec9b3028 | -13.5369 | -46.9683 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 936b46b4-128e-3e52-be50-f6f7bb0bb919 | -9.4498 | -62.3294 | 2025-08-30 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 234.9 |
| 290feed3-3080-3c01-b7b0-a53b016193bf | -11.8365 | -46.4741 | 2025-08-30 05:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 31f6c8c7-c784-3d13-a70d-4ba6b3d3c2e4 | -12.0153 | -43.9818 | 2025-08-30 05:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| bc89a315-0b08-35f8-a5f2-eebe82523296 | -9.4497 | -62.3485 | 2025-08-30 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 26bac6fa-3b84-3efb-b122-bbb75241fcd1 | -13.518 | -46.9486 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 393f3732-c8ff-3acb-bd2c-6de2a8d78bc5 | -9.4311 | -62.3493 | 2025-08-30 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 6e55ed43-8df4-36f5-90e9-10850cf1b544 | -13.3623 | -47.018 | 2025-08-30 05:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 186.7 |
| b8707770-874f-3a22-9f56-9df2f3622cd6 | -9.4495 | -62.3675 | 2025-08-30 05:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b781ea09-17ba-3e20-80dc-4e3663cc1133 | -9.4433 | -60.5499 | 2025-08-30 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 5c76c715-a735-3930-b888-77477f385647 | -9.462 | -60.549 | 2025-08-30 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 51acbe38-1034-360d-9ee0-3e146e025b16 | -7.43351 | -44.81675 | 2025-08-30 05:55:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7feab8fe-ffe7-3eaf-b0d5-1012d97d9fae | -6.17828 | -44.0027 | 2025-08-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| a3a30d05-f75f-36ec-bca3-bfe5742702ac | -9.48633 | -45.40358 | 2025-08-30 05:55:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 30d7277a-cfc5-3b5a-bdda-c76d646c478a | -5.87864 | -42.9549 | 2025-08-30 05:55:00 | AQUA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a71a3992-48cd-3a46-a0ea-4552d541ecba | -6.52878 | -44.86665 | 2025-08-30 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 84bac4a4-7853-3d7e-8020-025320b02482 | -6.11832 | -43.29319 | 2025-08-30 05:55:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 7.2 |
| cf2f9440-03e6-3a72-8aae-7090fdb54dd9 | -7.08977 | -44.30891 | 2025-08-30 05:55:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| a6b08844-b4b2-3864-8b6b-586bd9bd6ab9 | -3.42292 | -49.04697 | 2025-08-30 05:55:00 | AQUA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 97a4c875-4cc1-3ae2-b051-60f7001d521f | -6.41996 | -45.61469 | 2025-08-30 05:55:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c0332914-eda8-313d-a7c4-0c53d623221b | -7.95966 | -46.38604 | 2025-08-30 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb9b0904-cb93-3715-b253-9dee8b38adf9 | -5.996 | -44.72236 | 2025-08-30 05:55:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 0a3b7e57-a5c7-3ed4-b678-1cce875e5a84 | -6.17579 | -43.32558 | 2025-08-30 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 269.3 |
| ab39c533-b836-3ba4-b002-3fd0b8da1887 | -6.18594 | -43.32697 | 2025-08-30 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 9585c58e-7723-3d15-9c1d-46f656b07fe7 | -9.13907 | -49.61696 | 2025-08-30 05:55:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fbe63056-da81-3c7f-b610-d1d4351c4249 | -6.00528 | -44.72366 | 2025-08-30 05:55:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5f206d71-d1ab-39cf-a786-4485d84b861e | -9.48491 | -45.41358 | 2025-08-30 05:55:00 | AQUA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| f80d581f-eee9-3f22-a671-8fd0d842c87c | -5.69376 | -45.95705 | 2025-08-30 05:55:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4d69a391-ca9f-3ba4-965f-7c52fe29183c | -5.81845 | -46.35838 | 2025-08-30 05:55:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 449b2f14-2154-31bb-86c2-a1a6c8e4f0fb | -7.12063 | -44.59828 | 2025-08-30 05:55:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4e3b6bf7-76e4-3d37-9bce-1cfd7adc859f | -6.18118 | -44.00879 | 2025-08-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 13d536f8-1ee5-3851-9af7-db4f3b897d68 | -7.11919 | -44.60835 | 2025-08-30 05:55:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f4489fc0-8a51-3780-9a19-7e29973c091b | -6.0067 | -44.71383 | 2025-08-30 05:55:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b10e3bd1-cbda-3a42-9555-128b69f0adcd | -7.43496 | -44.80686 | 2025-08-30 05:55:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a2258007-bd71-3771-bfb4-742317c32d06 | -7.74147 | -50.26073 | 2025-08-30 05:55:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 516cbe42-744b-34a6-a0d8-12b72061ac60 | -6.17404 | -43.33756 | 2025-08-30 05:55:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 249.1 |


[Clique aqui para ver as próximas entradas](README78.md)
