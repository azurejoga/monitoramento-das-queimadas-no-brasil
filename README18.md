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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c9f8946-93b2-3b12-88e9-52cf6cefd706 | -10.5976 | -60.488602 | 2026-10-10 01:26:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dceeec64-5c4e-3a98-927f-2a966dade06b | -8.6845 | -62.396099 | 2026-10-10 01:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a94c4f89-8862-3438-bc68-d4a66635e0b7 | -12.3092 | -63.3759 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d58a151-e60b-357a-95fd-9f099cc1b98b | -12.2874 | -63.371201 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbcb209-da9b-3d9a-a1b9-a0385ab68bdd | -8.6322 | -66.768097 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eedae077-57a7-3d3d-9cd9-7b56bdaddf70 | -7.5557 | -61.527401 | 2026-10-10 01:26:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3dae09f7-250a-346c-8f24-2554ad41fb22 | -8.6693 | -67.110603 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 790bda04-ab5c-3c8a-b126-41819e914574 | -8.653 | -67.174599 | 2026-10-10 01:26:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81f75ca8-cceb-3c38-8008-829329fa4bba | -7.9228 | -63.691299 | 2026-10-10 01:26:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7fade5ac-4f32-3fdf-a0c7-d97ab3425b2b | -12.2897 | -63.380798 | 2026-10-10 01:26:00 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1aec89aa-2041-3ede-9e24-cc3a38f0735f | -7.4555 | -63.634399 | 2026-10-10 01:26:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fd0342ff-bd5a-3aa4-ab48-54d37dedd948 | -8.5351 | -66.974503 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 946e6a1e-9cd4-3883-a586-5b1d3b8eb030 | -8.5172 | -67.031898 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aafe4b76-83de-34f3-bf0d-d55409955e6a | -7.9131 | -63.6936 | 2026-10-10 01:26:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22ab69c6-7ec8-3e6a-8c01-cf5012e21545 | -8.6912 | -62.381302 | 2026-10-10 01:26:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e1e0a6b0-92ea-3ccb-85da-2f6a8bc1aeb0 | 2.7411 | -60.235001 | 2026-10-10 01:26:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| da4c4093-3fac-3568-ac5e-2fb6f81dde08 | -8.6546 | -67.181801 | 2026-10-10 01:26:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e04ae259-9e3e-3445-b6d2-1425c894b20c | -8.5694 | -66.989502 | 2026-10-10 01:26:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e4b02fbd-d427-325a-92ed-cf1b0d6496ae | -7.9086 | -54.7194 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b2ae322d-06d2-3e2f-b6f6-3c37b0c5ceb1 | -3.1114 | -53.7839 | 2026-10-10 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| d70c28e7-2ab7-3f2d-9025-0bed5334ae2f | -7.1997 | -55.1427 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 23e78197-9b21-33bd-a0fe-5d0f96c476d0 | -6.9319 | -59.2412 | 2026-10-10 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 76725b72-0b8c-3029-8fd9-80c270ba0371 | -8.6301 | -66.7886 | 2026-10-10 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 20d89715-9b15-3b6a-a473-49eea19dbc43 | -4.4025 | -49.7774 | 2026-10-10 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7bf7b405-b14f-372f-bdd6-acf4127c34a1 | -3.9912 | -59.356 | 2026-10-10 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| df1d6ca9-8e90-352d-8a6c-c6e3c4678e99 | -3.9911 | -59.3752 | 2026-10-10 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 7a9e60aa-34ca-341c-aec0-02a7d724da91 | -12.2324 | -44.6961 | 2026-10-10 01:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 39ffff84-eadf-3ef8-839a-55bf027d84f1 | -13.3666 | -43.8979 | 2026-10-10 01:30:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 196e34f1-0bdf-342e-a37d-7962996c3859 | -7.9084 | -54.7396 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| fc51d82f-271f-3533-8b64-e22067b17f05 | -10.6013 | -60.4669 | 2026-10-10 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 6a214044-b171-378c-97ea-6045def45b27 | -5.7565 | -45.1293 | 2026-10-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 77a12a1e-c822-341f-a5e3-3d80b047f3d1 | -3.6048 | -54.5936 | 2026-10-10 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 46aba1a5-573b-3812-97f2-4c015dcf57d3 | -7.0228 | -47.661 | 2026-10-10 01:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 965aa0cb-9eb8-34d1-87ef-65a7db18d816 | -22.0909 | -48.9738 | 2026-10-10 01:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 187.1 |
| a5bdf137-e6e6-32ac-b581-9e6bc5c273b9 | -3.2031 | -53.8621 | 2026-10-10 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 35479388-4aa5-3f88-b2e5-b287ab9645a5 | -7.5159 | -45.3251 | 2026-10-10 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| a2140118-568f-307c-99cd-0d889ca92dfb | -10.6201 | -60.4658 | 2026-10-10 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 79c6942f-859f-3723-860b-f45271b14cd8 | -3.5491 | -54.7351 | 2026-10-10 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 98c20ad3-746b-350f-83c2-f53ec771f046 | -3.5864 | -54.5942 | 2026-10-10 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| de1f6abd-35a5-3460-b715-fa4869f47d72 | -3.2204 | -49.4205 | 2026-10-10 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 456e9790-17e8-31ea-b4e5-10cdcd7da57b | -3.7311 | -60.6018 | 2026-10-10 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b90e96f2-f83d-39c0-8693-dda5df8867dc | -3.5676 | -54.6946 | 2026-10-10 01:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| c245ec56-1346-3684-be12-52b5f03be0be | -3.839 | -55.7997 | 2026-10-10 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 5395ebe2-416a-3c97-8188-132b3d1ae834 | -22.0701 | -48.9788 | 2026-10-10 01:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 251.6 |
| ce95ae6a-0075-3a96-876a-c7554c60ae0e | -10.8909 | -44.8001 | 2026-10-10 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 32873fb2-6ba4-312e-bac0-edf579ae17b6 | -3.1285 | -54.1657 | 2026-10-10 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 109329be-c4dc-3e4d-8d80-a69c60b720d0 | -2.618 | -59.9747 | 2026-10-10 01:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 20.5 |
| bd1914c3-fcce-3231-bc1b-e22154f45db5 | -6.9611 | -35.1117 | 2026-10-10 01:30:00 | GOES-19 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 67.6 |
| 831c53ea-2708-3d32-ae90-5cc9a2bb6cdd | -3.7494 | -60.6014 | 2026-10-10 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 5e2c7803-bc65-30fe-857f-465b606ccc07 | -12.2877 | -63.3711 | 2026-10-10 01:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 65de6f1d-b343-3de8-8d9d-5250cb2e581f | -3.2203 | -49.4417 | 2026-10-10 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 98619799-c6fa-3c59-a04e-f16c5572a402 | -7.9272 | -54.7182 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c54f68a6-b2a9-3a88-b7a4-bdb0fad27a31 | -4.5929 | -55.7366 | 2026-10-10 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| b885562e-2ceb-31f3-bf95-083c644e7870 | -10.6012 | -60.4863 | 2026-10-10 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 185.3 |
| 4e8380d1-4867-3c85-87fe-05dcd79c17da | -1.2723 | -55.7494 | 2026-10-10 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 4086bd72-7175-3ee7-abdd-ee54e7ec1f70 | -22.0694 | -49.0021 | 2026-10-10 01:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 131.1 |
| b2120ad2-a9f3-3c58-94e0-dbe9b04851b1 | -11.0332 | -45.4246 | 2026-10-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 69508d1c-3f30-376b-b409-d49616f6ab66 | -7.4975 | -55.0055 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 76af226a-7f32-3cb7-9fe9-b01a842fb33c | -4.5929 | -55.7168 | 2026-10-10 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 957bb54a-f2d2-3488-81ac-b2d7a0cfcc40 | -2.618 | -59.9938 | 2026-10-10 01:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| efa3c4d0-4240-36cc-bfa6-beeb70efae1f | -12.2329 | -44.6728 | 2026-10-10 01:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| b8722edf-7a46-3e1c-aa2a-9b82b03ce2de | -12.3066 | -63.3701 | 2026-10-10 01:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c0ef536b-5f3f-358b-acef-55189135f10e | -4.4507 | -47.9112 | 2026-10-10 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 6c7a4a84-eabc-3703-b1bc-c243ae254bf9 | -7.1995 | -55.1627 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| a73d8596-47b5-3e56-9b6d-d0d527434338 | -3.8391 | -55.7799 | 2026-10-10 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b00eafc6-349a-3a91-8eaf-51c0cce7e769 | -6.2026 | -45.4357 | 2026-10-10 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| beac4626-587f-34d1-83d6-7457ecb5de15 | 1.6755 | -55.6068 | 2026-10-10 01:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 29ea36f9-f86e-32e3-b44a-e5a1b7ddde76 | -7.2187 | -55.0815 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8802e415-96f8-3f8e-a68d-8800bd609d7b | -2.945 | -54.0899 | 2026-10-10 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8b2356fb-8920-3097-b957-1b2fc4b091f7 | -7.5347 | -45.3233 | 2026-10-10 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 3bd9650f-8937-37fd-9e81-3acdf72453a6 | -10.6199 | -60.4852 | 2026-10-10 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 6283f8ec-b3bb-323a-a355-3ad7b8865533 | -7.535 | -45.3006 | 2026-10-10 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 8c42a546-f34e-35ef-a445-d4e25e1a61b8 | -13.386 | -43.8945 | 2026-10-10 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 66a4d482-2769-34a6-b57b-e014da36e8a7 | -7.0225 | -47.6829 | 2026-10-10 01:30:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 99602a52-6dcc-3a1d-a266-da15a0a36f93 | -6.4411 | -55.0424 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 0cbbb4fa-0094-3b44-bf48-beed0e1fb5a8 | -6.478 | -55.0606 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 02636493-d6f5-3d81-acaa-779cbd644b15 | -2.9451 | -54.0698 | 2026-10-10 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 72cfcbee-e922-3eaa-b312-79b9471565ac | -5.7378 | -45.1307 | 2026-10-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 4a264e90-55d5-3a71-8a16-c465746e65ef | -6.4595 | -55.0615 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d0eb78da-dda4-3440-8c99-d0408c058e43 | -7.927 | -54.7384 | 2026-10-10 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 5d05ec89-2126-32ea-92cf-dbc94ee83644 | -22.0903 | -48.9972 | 2026-10-10 01:30:00 | GOES-19 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2800b457-52a6-3327-a6fc-ca789aa01fc0 | -3.1284 | -54.1857 | 2026-10-10 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5f766e37-bfec-3e15-9ecc-16bd0914b3ff | -7.5162 | -45.3024 | 2026-10-10 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a1e062f1-b1f5-3fb4-a650-24c3ec7777c1 | -6.9318 | -59.2605 | 2026-10-10 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 26766160-66c4-3d83-bfde-aa3a7be3417a | -14.453 | -43.9598 | 2026-10-10 01:30:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 57140168-ab1a-356f-bb84-4c925561fa5f | -2.618 | -59.9747 | 2026-10-10 01:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 31.0 |
| d17aca9c-66e6-3b81-b97e-75ce49debba4 | -3.9911 | -59.3752 | 2026-10-10 01:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d6a18088-c839-3b4e-ad9c-4f5a09dffa6a | -7.9084 | -54.7396 | 2026-10-10 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| b28df30e-b96c-3e1b-b8c7-8e97df3477db | -11.0741 | -44.1237 | 2026-10-10 01:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 51c07b1a-6339-3837-9248-7c1d93d3b525 | -9.9384 | -44.8791 | 2026-10-10 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 235.2 |
| b3e2b050-b4f7-3a50-9a07-adc43e0487ef | -7.0228 | -47.661 | 2026-10-10 01:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 8888c389-c09c-390b-bc7b-5e20a6a3227e | 1.6755 | -55.6068 | 2026-10-10 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 0289c889-46f8-3c45-9979-6de2eeff2e36 | -3.839 | -55.7997 | 2026-10-10 01:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b502579a-e782-3c86-a004-dbc433624d51 | -3.2203 | -49.4417 | 2026-10-10 01:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| a2ff2cc4-b58b-3b6d-b713-ad495ac8d42d | -10.6012 | -60.4863 | 2026-10-10 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 37121f75-3dbf-3af4-9c84-60dd5c4a66cc | -7.5347 | -45.3233 | 2026-10-10 01:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| ea328ffa-c1ce-3c85-aff7-94259fa5e53a | -9.9388 | -44.8561 | 2026-10-10 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4bac30eb-a4f6-3f58-a0f4-46b5a25408c4 | -4.93 | -45.7915 | 2026-10-10 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| c27a661a-b1c2-31ff-9ff3-56ace44fa85a | -5.7565 | -45.1293 | 2026-10-10 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 681734a6-41db-3d32-896e-beb77385c369 | -12.2877 | -63.3711 | 2026-10-10 01:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |


[Clique aqui para ver as próximas entradas](README19.md)
