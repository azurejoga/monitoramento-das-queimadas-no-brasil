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
| c926af45-5e98-38df-b633-72e7f9fb79e9 | 0.67945 | -59.56015 | 2026-02-20 00:49:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6346bcdd-a0a1-3920-bcd0-7c8ceca1a342 | 0.96569 | -60.24479 | 2026-02-20 00:49:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4e55603-d4bd-3eed-8c0e-ad39dba02b0a | 1.97576 | -60.69475 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 630267ba-83e0-35ae-b3c7-56856cdfa04d | 1.37417 | -60.31555 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 2b4ef38a-7c6b-3c95-91b0-4826115ba6b9 | 2.55521 | -60.57341 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 1073123c-8a33-357f-8468-6634d70a3ff6 | 4.07457 | -60.17857 | 2026-02-20 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 33.8 |
| b9f9f711-3715-3679-8fc9-d9aafd1d2822 | 2.67792 | -60.21336 | 2026-02-20 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 71e6e3f6-e58d-33a1-a223-9082a6598961 | 1.14808 | -60.32798 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d64688a1-b8eb-3ec4-ae5d-9b374339ed71 | 0.94188 | -60.25822 | 2026-02-20 00:49:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| fbc03c3a-b9fe-3cb4-8ad6-fcd001c1c752 | 2.54335 | -60.73096 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 256.0 |
| b99c0642-e057-35ad-9631-b03d9e8e7bd9 | 1.83012 | -60.85657 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2d202795-0170-3ad6-aa96-84d57c1425fe | 2.535 | -60.71829 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 8b0d63cf-8dd3-3c4e-a395-2a762ae2a87b | 2.69416 | -60.23705 | 2026-02-20 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 4256cd52-1870-3c6a-a15e-f74bb269b0e8 | 2.6875 | -60.21471 | 2026-02-20 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 31ed6a69-3d3d-32a1-9b3a-f6526fcedd9c | 2.67645 | -60.22384 | 2026-02-20 00:49:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.3 |
| c6a79318-71b4-3bbe-bea7-dc56e7fad6ee | 4.07317 | -60.18857 | 2026-02-20 00:49:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 19.4 |
| dcafc3f7-6437-30f9-9ac8-5e5cd70f812c | 1.83178 | -60.84487 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 55eb8e89-fc5c-356c-94c0-5a47ad5665a9 | 4.26568 | -59.79615 | 2026-02-20 00:49:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| be158e0f-e688-393d-adb1-f0d256ad9444 | 3.22544 | -61.19492 | 2026-02-20 00:49:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 9942e22a-899c-34dd-afd3-1f71c796a37d | 4.37724 | -60.64619 | 2026-02-20 00:49:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3f6d294d-d2c8-3db7-8c85-6fd330279218 | 1.73522 | -60.58435 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bdf4e0bb-61bb-30a8-a7d5-4d018b56f4f0 | 4.0672 | -61.10467 | 2026-02-20 00:49:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 88d5f126-fd38-33ab-b2de-4ccee4930a4f | 4.06563 | -61.10964 | 2026-02-20 00:49:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a44f9cb-0515-31f5-8510-2b9e1a2ddd86 | 1.13084 | -60.52042 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 16b31cb6-1d54-3063-8681-d43a4ad35376 | 0.45357 | -60.38837 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 16.0 |
| d1f84d0f-a92e-3acb-8e1c-df50bbf54b34 | 1.27909 | -60.40953 | 2026-02-20 00:49:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3567b3f7-24a1-3dc5-8806-5a4ae60782d8 | 0.4504 | -60.41129 | 2026-02-20 00:49:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 5ecabf0e-686f-3019-856b-77b27c116007 | 2.54491 | -60.7197 | 2026-02-20 00:49:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 314.3 |
| 232b792d-7e44-3308-af1b-a2e217a1cb12 | 3.23371 | -61.20198 | 2026-02-20 00:49:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 75f823ee-9ca3-3d4a-a749-03aff04dc485 | -1.59849 | -53.9902 | 2026-02-20 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 8277d460-b0ae-32be-9fe4-b0083afe950a | 0.4466 | -60.3925 | 2026-02-20 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 8ac2fa10-8b86-35de-8f98-628045cbe3a7 | 0.4648 | -60.3925 | 2026-02-20 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 4f5bc594-46d5-3154-843f-d47d09adc7ab | 2.562 | -60.5648 | 2026-02-20 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 352a4bcf-ea28-353b-8570-4468037a82f6 | 2.5434 | -60.7357 | 2026-02-20 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.9 |
| a12fb526-4d97-398c-a50a-170ebfe54b5b | 0.4648 | -60.4114 | 2026-02-20 00:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| ecd7ad5d-67ea-3c28-a02b-7e694f083dd0 | 2.5621 | -60.5458 | 2026-02-20 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b7b181b7-ff0f-33d1-9f81-b89d6ea50f34 | 2.5252 | -60.717 | 2026-02-20 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 61c5dd21-888f-3a02-8a61-e5d190b31d3b | 2.5438 | -60.5651 | 2026-02-20 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 789e7e9d-9c0f-300b-8cc0-69ce68fea1f2 | 2.5435 | -60.7167 | 2026-02-20 00:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 1bcfeee9-1025-3d17-88cf-6be0b7cfbd58 | 2.5434 | -60.7357 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 130.3 |
| ad36492b-0b08-31ee-9110-9b736d81b122 | 2.5438 | -60.5651 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 08235dfc-1c75-3cc6-a856-18264f898ec0 | 0.4648 | -60.4114 | 2026-02-20 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 2a2ada80-8cc9-34a7-9198-278fb0798fab | 2.562 | -60.5648 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 181.9 |
| c30063ce-00e0-3c10-8d90-03674e9b5ce3 | 0.4648 | -60.3925 | 2026-02-20 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 66a827d4-d1c2-3b56-b3bc-7e9dfc083b53 | 2.5252 | -60.717 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 105.6 |
| c5735526-bcc4-3c1f-b853-b6d88b444d0f | 2.5435 | -60.7167 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 75fa49ce-2918-36cf-adc8-17a3e968dfc4 | 0.4466 | -60.4115 | 2026-02-20 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 58.4 |
| e8c1dd8a-757f-3f0a-b334-7d5d9e528c12 | 2.5252 | -60.7359 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.4 |
| da6905c6-9503-3073-ac21-1cf794b4e707 | 2.5621 | -60.5458 | 2026-02-20 01:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d4385235-d5b3-3cd3-af0b-7ec285041b0b | 0.4466 | -60.3925 | 2026-02-20 01:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 48561594-b133-3059-8a01-e097357488ea | 0.4466 | -60.3925 | 2026-02-20 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c4de5f59-f6a8-36c7-81cb-2e6248b35afa | 2.5252 | -60.717 | 2026-02-20 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 47a5b446-5b14-3597-9817-85b30ea93b1d | 2.5621 | -60.5458 | 2026-02-20 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 1e1302bb-751f-3ad6-a7c0-cde19a4091e7 | 0.4648 | -60.4114 | 2026-02-20 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 6a9c7718-efcd-3121-9fb7-5145a99cc04e | 0.4648 | -60.3925 | 2026-02-20 01:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 95.9 |
| ae073ece-55e9-3750-8815-647db7d5a866 | 2.5434 | -60.7357 | 2026-02-20 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 677f656a-2daa-3cc2-aa67-029e68a14f1a | 2.562 | -60.5648 | 2026-02-20 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 6ad9eb80-ae74-3498-ae46-38f49f3d8d54 | 2.5438 | -60.5651 | 2026-02-20 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| bfd49994-213e-3a8c-b62f-9599bea5dd8a | 2.5435 | -60.7167 | 2026-02-20 01:10:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 210.8 |
| be597b54-aea5-3cfa-b2ae-7a1bda92400d | 0.4466 | -60.3925 | 2026-02-20 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f48462b5-3ac9-31ae-839c-fe1fd3afc895 | 2.5435 | -60.7167 | 2026-02-20 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 8607f282-42f2-34d7-b373-eeb06eadefc7 | 2.5438 | -60.5651 | 2026-02-20 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| e0cbcaf6-c189-3017-bebe-7d58f16fffa3 | 2.6905 | -60.2211 | 2026-02-20 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 671f9fe8-fed8-3fba-9a66-59d0575fd2db | 0.4648 | -60.3925 | 2026-02-20 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 6a9e790e-a00f-3bd1-ab73-32898f51d3ef | 2.5434 | -60.7357 | 2026-02-20 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 1bc0edab-2b96-361b-b560-fb58cff76b0f | 2.562 | -60.5648 | 2026-02-20 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 495a2351-e291-3004-b4eb-9cb5ac0913aa | 2.6723 | -60.2214 | 2026-02-20 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e48c4f7a-1f37-3623-b72c-b382393463a7 | 0.4648 | -60.4114 | 2026-02-20 01:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f1edfa43-b5d9-3ad5-bf99-dc446d7ae20a | 2.5252 | -60.717 | 2026-02-20 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.5 |
| b117c657-c7b8-322d-bf67-7bbfd4d4b02d | 2.5621 | -60.5458 | 2026-02-20 01:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 9744481d-d924-38e7-8e90-c136977ae2f4 | 0.4466 | -60.3925 | 2026-02-20 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| c9a9de23-f1f1-36b7-b684-8599bad5d183 | 2.5435 | -60.7167 | 2026-02-20 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 123.6 |
| b4c41e1a-ca6a-3c02-b146-8c5fcd7ec878 | 2.6723 | -60.2214 | 2026-02-20 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 53.0 |
| f2f7ba74-deb3-3063-99e0-30328182ffe2 | 2.6905 | -60.2211 | 2026-02-20 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8e52273a-01f3-3141-b6f9-5fba1eaffe24 | 2.5438 | -60.5651 | 2026-02-20 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fecd5191-e241-3839-83c2-da2918fefb7e | 0.4648 | -60.3925 | 2026-02-20 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 859e83f4-808e-3d62-b71d-e1489061b2d0 | 2.5252 | -60.717 | 2026-02-20 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| f7d16d37-02c6-3be9-b498-1343b48644e5 | 2.5434 | -60.7357 | 2026-02-20 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 5bb534b5-bdd8-3964-be2b-7c98ef4594ae | 0.4648 | -60.4114 | 2026-02-20 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 30dbed71-68a2-3a46-90be-bad872c4f104 | 2.5621 | -60.5458 | 2026-02-20 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 38536d88-74bd-39d3-95e9-268a8f62fbf7 | 2.562 | -60.5648 | 2026-02-20 01:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 200.3 |
| 758a8194-950c-35af-b484-450c232fb716 | 2.5434 | -60.7357 | 2026-02-20 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 9ae61e96-7480-332f-942d-0a72b9b1a8be | 2.5438 | -60.5651 | 2026-02-20 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2a0b7a90-3398-3754-ad7e-5328c2128b21 | 2.5435 | -60.7167 | 2026-02-20 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 113.6 |
| ce97fff1-c4d2-3fdf-87dc-2a35ceda6830 | 0.4466 | -60.3925 | 2026-02-20 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6311950b-8bb8-30f6-a99e-edc77451394b | 2.5621 | -60.5458 | 2026-02-20 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 900642fd-9136-3b74-8448-ec1d60b7c8c2 | 0.4648 | -60.3925 | 2026-02-20 01:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 2b676422-b831-335c-83f3-00372ca5580b | 2.562 | -60.5648 | 2026-02-20 01:40:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 196.2 |
| cc87a22a-ba42-3b5e-9b09-9202c8705921 | 2.5438 | -60.5651 | 2026-02-20 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 3cb88340-3e29-38be-a37f-85a553a221e8 | 2.562 | -60.5648 | 2026-02-20 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 168.2 |
| fcb3f450-179c-3674-9a58-856749728420 | 0.4648 | -60.3925 | 2026-02-20 01:50:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 747e636e-2204-32cd-a829-226cb6753a00 | 2.5435 | -60.7167 | 2026-02-20 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 042ead0b-a5f0-3137-9f32-c9f3f2963222 | 2.5621 | -60.5458 | 2026-02-20 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| fa055e05-2b98-3e7c-8fcf-6f055de55306 | 2.5434 | -60.7357 | 2026-02-20 01:50:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 73357fba-9bc0-3678-a4fa-5eeb7bd6874a | 0.4648 | -60.3925 | 2026-02-20 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 73.7 |
| e9e12041-44c9-31db-a7ee-446ae89cdc3d | 2.5434 | -60.7357 | 2026-02-20 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0cde14ad-c6fa-3a47-900d-45d5c5b6e8fe | 2.5435 | -60.7167 | 2026-02-20 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 91d49087-acec-3869-b49e-a53f9d1bc279 | 0.4466 | -60.3925 | 2026-02-20 02:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 87ffd3e9-04de-3ee7-b217-41d3e6ab9fe1 | 2.562 | -60.5648 | 2026-02-20 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 17afb704-f242-3540-9e97-7d0917006f94 | 2.5621 | -60.5458 | 2026-02-20 02:00:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.9 |


[Clique aqui para ver as próximas entradas](README3.md)
