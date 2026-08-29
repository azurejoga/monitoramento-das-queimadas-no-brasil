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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc2f1a1c-20e4-3694-8c14-4fca749c2d91 | -8.943 | -63.28336 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cfa4dafd-a81e-30be-849b-62b21041284f | -8.95108 | -63.27712 | 2026-08-29 06:31:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70572b41-65b9-3269-ac4c-7ce70d78245f | -8.98983 | -65.43861 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba4945d4-204d-37c5-9a5c-70d969ce7a1a | -9.0663 | -65.41772 | 2026-08-29 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 114169a6-ac22-3750-a937-24f21d39e7bc | -8.22299 | -69.84197 | 2026-08-29 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e955bc6e-4f9c-3c31-bd74-322ad3349236 | -9.1001 | -68.62553 | 2026-08-29 06:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0a2cbb6-eaa0-30b5-a8fd-2eecdaee4240 | -8.90228 | -71.39932 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df5f6378-50e3-314a-89ba-19f77d750990 | -8.89862 | -71.39471 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5177167-c8bb-3c38-a824-96e25f729294 | -9.10051 | -68.62248 | 2026-08-29 06:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 874aae1a-a36b-36cf-a6ca-d3774726106e | -10.5042 | -64.313 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5afeb8a-e281-3e97-a45a-5d722c23691b | -10.48141 | -64.49237 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0aa08aa7-6490-312f-a861-fe1f3267b5d1 | -10.4762 | -64.4937 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 38a7c4e9-7c61-3333-98cd-edb09520a37f | -9.86717 | -65.02541 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6b73901-cec4-3062-b91d-72e023499358 | -10.47547 | -64.4999 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| df8e1935-8535-37e3-b996-77ac868692ec | -9.86646 | -65.03101 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d34000f8-03a5-356b-bbfd-05a69a80ecba | -10.48908 | -64.50155 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 573b7386-bc36-3fb1-9b21-58e2fb88e8ba | -9.20794 | -71.85959 | 2026-08-29 06:33:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e0da36b-7194-3944-b726-b823f26367ea | -8.82386 | -70.63225 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edabe3da-4ca3-33a9-8be2-fdc557aacf60 | -9.50762 | -65.5825 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 714e081c-6626-3491-9551-2e3638167c22 | -10.28136 | -68.86601 | 2026-08-29 06:33:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c95f2f17-143b-39d5-9e88-2c682e7a45df | -8.86675 | -70.90538 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4256c01d-87fd-31df-8027-c746fee1b924 | -10.46703 | -64.49695 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d09aa8b5-dd45-3491-8a93-f2d047ba3b92 | -10.47989 | -64.50462 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 94f556a8-60f1-3d5c-989b-8af3d9ca7b25 | -8.65468 | -70.75398 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3900f410-4d09-3e71-8673-9192f5a67b31 | -9.8737 | -65.0263 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c29a067-53c9-3113-9cf1-2a160f4e43da | -9.17756 | -70.89436 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6178548a-2c8d-3515-ba7e-fb7791ee62c1 | -9.86576 | -65.03658 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| baef41d6-8b6f-3a80-8e4e-84c1b83a598d | -9.38386 | -66.52009 | 2026-08-29 06:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 542877cf-3e5a-3030-a4f8-f41df59739e9 | -9.34094 | -68.88993 | 2026-08-29 06:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7086f2c8-e619-32d2-bba8-fc15714f933b | -9.86611 | -65.02618 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4af5662b-5141-3c53-aca5-4575679ae63a | -9.38331 | -66.52442 | 2026-08-29 06:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2abe8f8e-6de8-3804-84ef-51d00e34989f | -10.46627 | -64.50319 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4942f0d3-39d6-3b28-90b6-cd817ef969fa | -9.86544 | -65.03178 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0802fd21-40e4-3923-9b3e-2e33825ad83a | -10.47462 | -64.49145 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4b435033-43fd-35d1-99e3-fb15d3a46a80 | -10.483 | -64.49461 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 404f6918-6c1b-3ee2-9663-b3fb24363673 | -9.50824 | -65.57745 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7b1d031-1850-3944-b4a1-5ad941a001fa | -9.51392 | -65.58327 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0df062fb-dd42-3a5c-8856-91f39a2b45d1 | -10.51191 | -64.30676 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 199fc3ea-45eb-3da3-8513-89ace99d6ace | -10.48064 | -64.49857 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b06fb6e4-af9a-3d10-8f94-1ddd3e123d62 | -8.82832 | -70.6329 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46c2b031-e0ca-3fb7-9d20-ec3d3e31c944 | -10.51116 | -64.31321 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba22238a-6e38-3a61-9e59-0c25eaa6e7c8 | -9.86477 | -65.03737 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b018103-6ba6-3d51-8ae8-08f2412ab405 | -9.38978 | -66.52095 | 2026-08-29 06:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b2a8c4c-ad08-34d0-b81e-16b11742d10c | -10.46867 | -64.49908 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b79ac30d-7c3e-37b7-83a1-ba29a798a70f | -9.02628 | -70.91846 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa27fcdc-ec66-36b1-8ecb-90d1dc646a27 | -9.87197 | -65.03267 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f5a38b3-0471-3998-a38c-f188d083c2dc | -9.35321 | -67.80283 | 2026-08-29 06:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07faf75d-91d5-3e04-8fa9-a1153a705161 | -10.4678 | -64.49068 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60afa9a3-d6bc-3158-acd4-d692f9e4b8af | -10.46098 | -64.49001 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f27f0b35-2e10-347f-a9d0-a98850b0ca20 | -8.84948 | -71.31462 | 2026-08-29 06:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a255b924-d347-3cc8-83a9-c9d6d6382f18 | -10.4694 | -64.49278 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6a1b9842-31c5-39e2-8111-0be58a1da02a | -8.82325 | -70.63669 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6565f7f1-4205-3718-a10a-aba0cc0a8914 | -9.51455 | -65.57822 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef5cd679-939e-3291-bb9b-4ecf00abfdf0 | -9.873 | -65.03188 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8147cfad-c9ce-3998-8931-ae521b3890e7 | -9.87264 | -65.02708 | 2026-08-29 06:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1e625ad-2e68-35c7-82b8-bcb444042e3b | -9.34777 | -67.80205 | 2026-08-29 06:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c387ced-9e73-3f11-a225-7cdf39f71ba8 | -8.89805 | -71.39869 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0918d67-e661-3d05-94d6-7cbeca90e606 | -10.27664 | -68.86217 | 2026-08-29 06:33:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a235de6b-490a-3031-835c-4d80e7eeda53 | -10.48228 | -64.50072 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5face522-1c44-3c42-a3c9-e8294fe5438d | -9.02688 | -70.91417 | 2026-08-29 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1658cccb-bdbd-34d4-9e62-418e23197625 | -9.27947 | -68.78265 | 2026-08-29 06:33:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d08d5ac-6d62-3ab2-844f-ba617856c7d5 | -10.47384 | -64.49773 | 2026-08-29 06:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a4e9ba30-83d5-33df-abb9-ff37aae6a04d | -9.39033 | -66.5166 | 2026-08-29 06:33:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b4a9c7d-1dac-3eae-b4b4-cc7cf38e9499 | -6.7884 | -55.6635 | 2026-08-29 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 384c0498-e8ca-3d76-bed8-01a3d47a5ef8 | -6.6315 | -43.7533 | 2026-08-29 06:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 7b90c57f-8907-31f9-acd5-1818d20f8412 | -5.8895 | -57.7513 | 2026-08-29 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 9c63651f-0624-3083-ada5-2e0a92116428 | -6.7885 | -55.6436 | 2026-08-29 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| d622e4c6-d875-3d36-8fab-08c79a8ef07a | -6.7699 | -55.6644 | 2026-08-29 06:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 3708dc3b-08a1-3fb5-b8cf-29274a061e10 | -10.4795 | -64.4824 | 2026-08-29 06:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f159669d-c0f8-361e-8652-002d54f44d2d | -6.6317 | -43.73 | 2026-08-29 06:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 141.1 |
| ad94f24c-d45d-34ea-8222-9936b824a3e9 | -10.4794 | -64.5012 | 2026-08-29 06:40:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 325b3703-ed06-37bc-afad-0b35d6b73e5d | -5.8894 | -57.7708 | 2026-08-29 06:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 158d6646-ac5e-3ff3-834b-d167697dab08 | -10.4608 | -64.502 | 2026-08-29 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.8 |
| abd0447d-e522-37dc-b0cd-b3a5a86f589e | -10.4794 | -64.5012 | 2026-08-29 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 9778ca5a-64c7-322e-a863-f5186aad9efc | -6.6315 | -43.7533 | 2026-08-29 06:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 17873124-fc7b-3a31-983f-84ca32e4661c | -6.7884 | -55.6635 | 2026-08-29 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 149.5 |
| ab2b2b5d-9c5e-32eb-b2d9-70c783de0623 | -6.7699 | -55.6644 | 2026-08-29 06:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4c4d2c4e-2f49-3019-b626-e786ec38f7f6 | -5.8895 | -57.7513 | 2026-08-29 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0fe4eb89-471c-396b-8e94-97aa4f966d60 | -5.8894 | -57.7708 | 2026-08-29 06:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b51ef85d-6f6b-3634-9705-458ce4fa51f8 | -6.6317 | -43.73 | 2026-08-29 06:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 6c93c328-4f2f-3771-86ef-1a9e1cf56da4 | -10.4795 | -64.4824 | 2026-08-29 06:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8fe8a9ec-e318-3223-92ab-1d860eb973ea | -6.7699 | -55.6644 | 2026-08-29 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2383de4b-3477-33ae-bebd-4642d306c624 | -6.7884 | -55.6635 | 2026-08-29 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 94166223-e48e-3e4e-bda6-3910500cc4f3 | -6.6317 | -43.73 | 2026-08-29 07:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| b7e5a50d-b94b-38c1-960e-767b13211e0f | -5.8894 | -57.7708 | 2026-08-29 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 7a1c5dac-6905-3ab9-a1d9-905f75f70551 | -10.4794 | -64.5012 | 2026-08-29 07:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 91.8 |
| b8a83f13-2abd-3b86-8f02-61ab093b04e7 | -5.8895 | -57.7513 | 2026-08-29 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 20ae3920-d445-3718-92df-0af04111cc4e | -6.6315 | -43.7533 | 2026-08-29 07:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f5774f08-493c-3469-a1e9-42f7fcca6c2c | -6.7885 | -55.6436 | 2026-08-29 07:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 90930901-b638-3f25-8b60-b247c78d2271 | 0.14467 | -60.40091 | 2026-08-29 07:09:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 60f2bfb1-fc8d-39d2-ae0d-926db7119f04 | 2.51944 | -50.85263 | 2026-08-29 07:09:00 | AQUA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 2d6040fe-0a07-30ae-ae1a-35ae01f2dad5 | -6.7885 | -55.6436 | 2026-08-29 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b2dfab5c-85c2-3604-96b9-b0ed96fa3e0a | -6.6317 | -43.73 | 2026-08-29 07:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 1c862a15-18d3-38d5-ad56-376ed1b62b24 | -6.8069 | -55.6626 | 2026-08-29 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4dbd5c35-7983-3e07-be67-072d1ffb5795 | -6.77 | -55.6445 | 2026-08-29 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 1b8613ba-a844-3de0-9c5a-f6865e27a9da | -5.8894 | -57.7708 | 2026-08-29 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 707df71e-34ba-30ce-a3bc-fa5bf1fa1507 | -6.6315 | -43.7533 | 2026-08-29 07:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| df062ffa-36f3-36da-a166-4642637906ac | -6.7884 | -55.6635 | 2026-08-29 07:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 179.5 |
| 887d1d86-a716-3d04-9ab7-4f7fe018b3c3 | -10.4794 | -64.5012 | 2026-08-29 07:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 68c6ae87-37d7-3a6d-a7e0-a34ee001e3ea | -10.4981 | -64.5005 | 2026-08-29 07:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |


[Clique aqui para ver as próximas entradas](README73.md)
