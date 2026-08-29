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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dce72b6-c1bd-30f7-b2c9-d3e85b8a39eb | -6.1526 | -57.789101 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94f85c61-4ac5-39ca-895b-fe4527910827 | -4.373 | -47.7742 | 2026-08-29 01:16:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 959f1743-7797-34f7-ac5f-af9c658133cd | -11.034 | -57.2215 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9338383f-0b01-34cb-89fd-ea7770b8e44d | -9.9627 | -53.930099 | 2026-08-29 01:16:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7e0adae-6f37-3afb-8aef-8c6f06250b4c | -7.2817 | -45.830898 | 2026-08-29 01:16:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ee970a5b-83bb-3e8f-af54-4f32da9a9261 | -14.2776 | -57.034698 | 2026-08-29 01:16:00 | METOP-C | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc23a9f1-4e18-3ba2-a40e-11b9a32d81c7 | -6.4996 | -53.2603 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9603fc2-80e0-3df2-993b-110a87a030c6 | -6.9321 | -58.952499 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e287f34d-bd1c-3035-9f59-f78aa8b11324 | -9.2808 | -57.081902 | 2026-08-29 01:16:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 27a84bd4-639f-317a-a34c-43f08f45b186 | -20.951 | -57.578899 | 2026-08-29 01:16:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| c335d6c9-2059-3769-9021-544d95ec76f3 | -8.5284 | -55.34 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd37ce4-cea2-3456-bcca-a99ccca3b78f | -5.887 | -57.755001 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a9ed8c8-5335-3357-82d7-d8e878d47ab0 | -9.2129 | -51.549099 | 2026-08-29 01:16:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 695f7aab-4da1-3f61-829f-b59368ce98d8 | -6.8901 | -59.406799 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9110977e-88ce-33a4-8ce9-1459020e51d2 | -7.4963 | -55.296299 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ee73f49-bd0c-3ad0-902c-a2640840eb62 | -11.6241 | -54.579399 | 2026-08-29 01:16:00 | METOP-C | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c226d7d1-c2c5-38f6-ab32-a9f42801117f | -11.0304 | -57.2514 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98bb8e28-dd4f-36ea-8d9d-e4e4a72f8560 | -2.7536 | -58.168301 | 2026-08-29 01:16:00 | METOP-C | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a3b4c26-5d0c-3661-be4c-4baeb3ff2f6a | -9.9315 | -60.4235 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6226c007-053c-3703-99df-04b2cf70a176 | -6.8803 | -59.408901 | 2026-08-29 01:16:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a1d9e25-a031-39f8-96a7-71ca38f81389 | -10.471 | -64.487602 | 2026-08-29 01:16:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3501e06-acc3-32f3-ae69-1828cd48c31b | -10.7633 | -54.038601 | 2026-08-29 01:16:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bbbf04cb-89e4-3efc-97dd-b0fcb860bfa9 | -6.7692 | -55.674801 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e98f6662-b96d-3e8a-9f11-229fc9a6bc91 | -7.0495 | -55.682201 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1b4f0a6-bd15-3044-b0f5-ae556d07cf8a | -14.2119 | -52.848499 | 2026-08-29 01:16:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b801320-229e-32e3-b150-4ef25641c1e3 | -18.9953 | -47.426498 | 2026-08-29 01:16:00 | METOP-C | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 000efbb0-00f3-3efa-b1d1-9eb5b91084aa | -7.5158 | -55.291801 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c009a976-2f90-3b39-a961-f6348e3252ee | -15.5726 | -56.2812 | 2026-08-29 01:16:00 | METOP-C | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f02cc43c-7426-3c56-b917-7378d9d120d0 | -9.9352 | -60.440201 | 2026-08-29 01:16:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b86936bf-5429-36d7-abb3-e36466227617 | -8.5867 | -54.751099 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd439e9c-ef26-3ef4-9339-c5629c2fb2bd | -11.1891 | -55.105099 | 2026-08-29 01:16:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 344cc19f-a801-328e-a760-ba33a3d07556 | -8.5302 | -55.2593 | 2026-08-29 01:16:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c2bc97d-7b60-36ac-b395-affa2acc9221 | -8.5886 | -54.759102 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b83950bb-3eb3-38f0-a943-542992dda76c | -11.0402 | -57.249199 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71e6294c-b855-3b33-b997-fe679482d313 | -6.1511 | -57.7822 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81048338-ec7a-36fc-9ac6-425ef2e3d8db | -7.6215 | -61.359001 | 2026-08-29 01:16:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63c4ea9c-5294-3980-8f5a-fbdb95b30d8c | -8.5984 | -54.756802 | 2026-08-29 01:16:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccfc8d2a-9e22-3554-8d99-dbd3bf3f4e31 | -8.9539 | -63.2654 | 2026-08-29 01:16:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 251b3a9e-8de7-369e-8ed5-62ad7c7ea38e | -6.1821 | -57.782501 | 2026-08-29 01:16:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a19f3965-ff1c-375a-943f-be407bb9a38c | -6.8258 | -59.946999 | 2026-08-29 01:16:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f3ec083a-72a2-30e3-a7c1-821a6e695eff | -11.0422 | -57.212299 | 2026-08-29 01:16:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4c9a9d8-8d49-3c60-812c-8dd9a474aaad | -20.233801 | -47.3881 | 2026-08-29 01:16:00 | METOP-C | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a161b1f-e20e-31ab-9580-57036ae7734f | -11.0254 | -57.2237 | 2026-08-29 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| f900cc44-af39-3fa8-96d1-55a78977635d | -8.9428 | -63.2797 | 2026-08-29 01:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 846df603-c3dc-3dc3-bae5-299951ac0b0f | -4.3774 | -47.7627 | 2026-08-29 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e9d981f1-d6ac-3915-9063-8426a1fcaca0 | -5.8894 | -57.7708 | 2026-08-29 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 84619a9e-62a1-3a5b-ad75-349408cf788b | -7.2847 | -45.8652 | 2026-08-29 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 8f28652d-e62e-35c8-b95f-9d7bd42eb7c4 | -11.0441 | -57.2421 | 2026-08-29 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| f52d9cce-b14e-3ccc-92ba-e1e878f72fb4 | -10.4795 | -64.4824 | 2026-08-29 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 99333aea-87a8-3daf-b339-fc454be2f2de | -6.7699 | -55.6644 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 155.8 |
| acedf8e8-4443-3c8d-9d70-b6fb5727da1e | -6.7343 | -55.4671 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 6c7d8ae5-9444-391e-be3f-7c6b396cef8a | -10.4981 | -64.5005 | 2026-08-29 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 202d0fd4-a839-340c-9681-75cad5a8ea23 | -7.5137 | -55.3051 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3779bb9d-9c55-34ea-808c-faba86e4b083 | -8.9614 | -63.2601 | 2026-08-29 01:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 5d3061b6-ba05-3aa2-923b-83114fb22c47 | -11.1913 | -51.292 | 2026-08-29 01:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 24d21250-17d7-36ea-b330-23ab60a4cd3a | -5.4179 | -43.1752 | 2026-08-29 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 6eacf117-186c-35e3-8587-ba622fba2d10 | -5.9079 | -57.7506 | 2026-08-29 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 3b3d0080-5250-3263-98d1-dca1ef80cfd7 | -6.77 | -55.6445 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| b64e93ef-bf61-3a64-a147-cfae65096b32 | -5.8895 | -57.7513 | 2026-08-29 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 162.8 |
| a80227ed-0e4e-3d6a-a19c-c3173486616c | -5.4177 | -43.1986 | 2026-08-29 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| c2b6ca31-a8ed-3f1b-9938-a0ab3a5872eb | -8.9613 | -63.279 | 2026-08-29 01:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| e4cf31e4-24e8-3917-ae15-edd00e8b9b7e | -7.6069 | -47.2837 | 2026-08-29 01:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 43.3 |
| cdd5fba9-25fb-360f-832d-d246f26b96ee | -11.0252 | -57.2436 | 2026-08-29 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 6bd3c549-d62f-3f20-8fac-a30cd7d5af84 | -5.9078 | -57.77 | 2026-08-29 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 65db1573-f20c-364b-abf6-6b0ddaab6118 | -10.4794 | -64.5012 | 2026-08-29 01:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 8a4922b0-8e79-3f52-a49f-5d414dd1a12c | -6.7698 | -55.6844 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 59299521-b8c6-3b8a-9992-72dfde22f34f | -11.0443 | -57.2222 | 2026-08-29 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 3ec4cc61-4228-3d1a-a997-3184baf939ab | -20.2295 | -47.3875 | 2026-08-29 01:20:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 37ea3a21-5316-3325-92db-c0a6c3d96600 | -6.7884 | -55.6635 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 678a0667-e702-32a7-bd33-6396b237237b | -7.2849 | -45.8427 | 2026-08-29 01:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 7c6fc12c-55bd-3315-9f9f-81d2b37312c2 | -6.7528 | -55.4661 | 2026-08-29 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ddb6b12f-c885-306b-bb1f-8b7e1e67eae3 | -5.9819 | -57.6892 | 2026-08-29 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 675312de-aae3-3fbc-82a5-73d53d26efb6 | -6.7698 | -55.6844 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 445f6eaa-aaa0-31a9-bab6-d0d1cde8c902 | -10.4795 | -64.4824 | 2026-08-29 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f87b8231-fb0e-3220-ab7b-5f032b187144 | -6.7699 | -55.6644 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 7df42006-e411-36ee-990e-3d6a0fdb73e6 | -20.2295 | -47.3875 | 2026-08-29 01:30:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 56.0 |
| ba44e1f4-137e-3af5-8b06-04bd624312b9 | -6.7883 | -55.6834 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3d13bec2-866b-3496-96fe-bbef30b8e0c3 | -8.9428 | -63.2797 | 2026-08-29 01:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| d87d71cc-ad69-35b4-9654-be596dc8303e | -5.8895 | -57.7513 | 2026-08-29 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 181.9 |
| a7964933-0257-35ae-a6e5-f09fe59a3f90 | -4.3774 | -47.7627 | 2026-08-29 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| c0abafe6-c965-3a0c-baa1-f2948d192813 | -8.9614 | -63.2601 | 2026-08-29 01:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 782f00c6-04e5-3b5e-bdaf-8ca2ac38f89b | -6.7884 | -55.6635 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 9e827da6-4a54-3ab9-b600-b3267d972583 | -8.9429 | -63.2608 | 2026-08-29 01:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 91010d13-d355-32d4-9f83-29837546ef95 | -7.5137 | -55.3051 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e6de72f9-6472-3e5e-bc2d-13c2a2f9f17e | -6.7343 | -55.4671 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| ee90238c-ef6e-3a7e-87a7-be1254a8bb74 | -10.4794 | -64.5012 | 2026-08-29 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 656920b1-98db-3abe-a4a4-7d1c231ee42c | -11.0254 | -57.2237 | 2026-08-29 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 4923899f-d3b8-362b-8c49-4733167ed5cb | -7.2847 | -45.8652 | 2026-08-29 01:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 4de95091-16b3-3955-8f3c-29fc56c89487 | -5.9079 | -57.7506 | 2026-08-29 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 927c80b3-6554-3d9e-8299-8084bff0bc86 | -5.8894 | -57.7708 | 2026-08-29 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 852d8660-f6e5-3e94-b4a7-607e03a281c0 | -11.0441 | -57.2421 | 2026-08-29 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5a0aaa53-bc49-3ed4-b3e3-8f409ee876e0 | -11.0252 | -57.2436 | 2026-08-29 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 30eef7a6-9354-31cb-9e60-42979b602587 | -10.4608 | -64.502 | 2026-08-29 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 8c9e2dc6-4760-3993-8487-591fdd3a2100 | -11.0443 | -57.2222 | 2026-08-29 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ec7a62bd-c90c-37a4-914b-ddcda3f9239b | -10.4981 | -64.5005 | 2026-08-29 01:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 93.5 |
| b2833805-244e-343e-9878-ce80a2769573 | -6.77 | -55.6445 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 481c924e-46c9-322e-b7a1-3191383a546d | -20.941 | -57.5694 | 2026-08-29 01:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 56.8 |
| 25038031-536b-3944-b3aa-a14c91830eeb | -6.7528 | -55.4661 | 2026-08-29 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 587dbf51-75cb-3140-b9f8-4a926af8f28e | -8.9613 | -63.279 | 2026-08-29 01:30:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 03021562-cc96-34df-90df-bc425d485929 | -7.5139 | -55.2851 | 2026-08-29 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |


[Clique aqui para ver as próximas entradas](README18.md)
