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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdf2c694-a434-353e-94f7-4f08acf7514c | -10.9522 | -49.77061 | 2026-09-01 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90c31cdd-c863-360d-a0b2-c8bdbd6912ac | -8.11911 | -51.66275 | 2026-09-01 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 196cb723-59f8-300b-8118-be1e2fde87e2 | -5.95614 | -57.68393 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6ba71c2e-12ac-317c-9a29-169582b13fc2 | -6.81971 | -43.53092 | 2026-09-01 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e058c2b4-d897-3b7f-a81d-1d566aa920c6 | -9.48395 | -57.02749 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5dd42623-02f3-37a3-9ca0-12116036bd27 | -6.16022 | -52.63981 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ec06256-2b01-306d-aece-8110f41dc4ae | -7.6366 | -55.28697 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c85efda-db2b-311d-99b4-8034bd58691b | -7.18907 | -60.69183 | 2026-09-01 04:40:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 16dfed3b-15ab-355b-83f1-b259d265f1fd | -6.10423 | -57.86761 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14f5b09b-5061-3ded-a97f-de8e0251f1c7 | -6.17953 | -57.73197 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c4c3b796-931e-3556-924c-cc423cb290d7 | -10.95553 | -49.77113 | 2026-09-01 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc0a438c-ec32-3dd4-9655-97c4ae183ef4 | -11.06262 | -51.52547 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e2c0a66-c5cd-38fa-92f4-736a137720e8 | -8.62693 | -54.85059 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b513c1e-c5fe-3ac0-99b6-f68c71434c8f | -11.48709 | -45.09946 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5056e04f-3119-37f7-a610-55b5b2289758 | -11.67189 | -47.60566 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1f5b394-9e34-320b-b172-1c2f609d9e8e | -8.20886 | -54.94464 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5146d45-4217-3de9-8692-9104db398976 | -6.16062 | -57.78175 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 209e8ffb-3bcc-3d7f-8674-c5625eec1cbb | -6.9827 | -59.59374 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ea0a349-f14b-3a54-b3d2-64676fe3eff4 | -8.77153 | -45.37611 | 2026-09-01 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6661123b-ddd6-324e-8003-4818a03d000d | -7.5239 | -55.3339 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a81fc012-17bd-3bd2-b1d9-ba7c0f2bd86d | -6.36037 | -51.75155 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32c5455d-ad42-36af-b4dd-c497ac3b8e76 | -5.88645 | -52.15757 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9759a2f-c0c9-3241-880c-0b243edcc8a4 | -9.18339 | -51.55419 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a2e96b3-614b-3505-a6d0-d3a44cf1802f | -7.90429 | -44.25154 | 2026-09-01 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de502940-ac1c-3ea3-9bfc-29d36cd29cde | -11.26376 | -45.11286 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9942af37-6bd3-38e9-ba30-e6e9133e3ed4 | -6.81057 | -59.09671 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| bf5e91fb-2a5f-33be-9351-6e2081053945 | -11.67017 | -47.5923 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62bd2e63-8f1a-38f4-a9e9-5c294726ae82 | -7.34465 | -60.58483 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0cccb18f-455c-309e-bc14-aa80fab6a9a3 | -11.20714 | -45.09246 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f27065e-baba-3855-8002-a558f32d0d8f | -7.34974 | -60.59017 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 915602c1-cbf1-30a2-aa2d-aa48a0d912b9 | -7.68262 | -55.34058 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4af7705e-eeb1-3b99-a24d-5828c72451bf | -7.33114 | -55.14678 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a698ded6-d142-300d-aa47-0d3a498f9def | -11.24461 | -50.58538 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1792b7a-bfee-35ba-b24a-9c62617904fd | -6.1203 | -53.54988 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1f24a0f-4e6c-3c7d-b36f-a803d59ce385 | -11.3805 | -45.18689 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fbb79bc-9071-383b-9b71-3ef887e0ae91 | -11.25726 | -50.56946 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df9f50fb-4f94-33db-b35c-78e289285f44 | -11.66954 | -47.59663 | 2026-09-01 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8dc6b9c8-5178-3f03-aec7-0251710bd94c | -4.95905 | -55.85595 | 2026-09-01 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 313a6cae-7f32-362f-b65e-56c56222863b | -7.52976 | -61.38516 | 2026-09-01 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df330ffa-acfb-3745-9047-dbd30967b7b9 | -11.91261 | -45.07225 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f836585-2684-3ae1-a5dd-b814f90ffe3a | -6.05579 | -57.64411 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d210df70-b386-37b2-ad78-d1ffe67af07c | -9.98215 | -53.93437 | 2026-09-01 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9aefb62f-9a87-3d88-8762-e042d04da6e1 | -7.29313 | -56.68229 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4e59926-0c21-30c7-82e9-87ec770e9054 | -11.09978 | -51.56843 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8495f4d-3acf-3ae2-ae54-0b13186d53b3 | -10.3681 | -50.01117 | 2026-09-01 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e4318a28-cb47-3aa9-81df-588b4a44cba4 | -9.15741 | -59.53022 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e73ef0-1b28-3dea-a766-27d57056c108 | -10.06423 | -59.40368 | 2026-09-01 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8443b488-05ae-3d52-8a0c-00a34bb27aa0 | -4.15026 | -60.69558 | 2026-09-01 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0aca7a2-5076-3512-8eee-697a77564610 | -7.62492 | -55.28926 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12e970f5-48bc-3d33-8976-420c8370f7da | -7.28994 | -49.84332 | 2026-09-01 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42857fba-123a-392b-a936-5c36065cf7b6 | -11.3087 | -45.20094 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0a9df567-00cc-306a-932f-11ffe895ea39 | -6.78298 | -55.67873 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c0399df-60d0-345f-9fc1-46f4e652831a | -12.07028 | -44.99083 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5588b932-3b65-35f1-aa69-6ae70009a689 | -6.15662 | -52.63922 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ec56e3a-c10a-376d-a45b-531a14b1cb63 | -6.87595 | -45.97414 | 2026-09-01 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50d2093c-71f9-381b-b91a-a3e3e7ffb7c9 | -11.3014 | -50.59085 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b1c6988-6fee-37bf-bcdf-371ccb61fbab | -9.67188 | -46.53945 | 2026-09-01 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06aa0a21-3e11-3315-9514-568e0ec5950b | -7.90314 | -44.25958 | 2026-09-01 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2fe3ee7-7fc4-3e20-8b64-917e439160ed | -9.47499 | -57.02583 | 2026-09-01 04:40:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a8a2b47-fd8a-3afe-8785-e70b8384cb65 | -8.50177 | -55.3165 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8889d53a-6d6f-3eae-91f6-c0fdc06064e2 | -6.60045 | -58.60353 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4f229e6-c036-3646-93c2-e27ca860b433 | -6.81766 | -59.43966 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbf9a1fd-e916-39fa-b9b4-922c1ef94b6e | -6.13366 | -55.64211 | 2026-09-01 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| aa5fc164-e2bf-3fd0-a285-5e517ef36c63 | -8.13007 | -54.9726 | 2026-09-01 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95b2d87f-a8f6-37cb-b49e-043fa3d5de19 | -10.77466 | -54.04564 | 2026-09-01 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f87ee1b-0d14-39b7-9f3e-cbd3980b4f36 | -11.49034 | -45.09737 | 2026-09-01 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ec5e809-5b5b-3198-a95b-328b0d7728de | -6.95693 | -55.64803 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ffdd5cf-a408-3c26-bdf5-66ba49b413a0 | -10.99099 | -48.39448 | 2026-09-01 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4cafb9d-e6a7-3bc9-9e0a-23d4133eace1 | -6.74287 | -55.45019 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c55e607f-536f-33b7-9cbf-85b54a8866ab | -6.88612 | -59.40662 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ffed169-f03d-3437-81cc-24dbd6fb2f61 | -7.35539 | -55.19655 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 62cd72fa-54e7-3bd0-adb0-558c29c98ab7 | -11.92614 | -45.09855 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2996ad52-05da-3359-b0b1-0add423becdd | -9.40938 | -51.67549 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a870ffd1-7212-3b7f-a1cc-a639b0f2680c | -6.18451 | -57.7328 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e3902166-9f7a-3e45-b0cc-e4162cfe27e4 | -3.11385 | -61.23731 | 2026-09-01 04:40:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ccddce4a-885e-339a-8386-20b3110b8e45 | -9.15202 | -60.94903 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4e47f061-6149-3290-8f3b-1aeeb09a9593 | -6.95625 | -55.65202 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 165bf59d-3686-3739-ab75-e1f866925d0f | -5.95564 | -57.68679 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02375acd-ae2a-3f94-9bb9-a7d335ffd2b0 | -6.148 | -57.91404 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fa62177-175a-34fd-86b7-30d3fff7c2b2 | -5.88587 | -52.07246 | 2026-09-01 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca4fc307-d1c6-3020-a14c-38a0f156d1f1 | -11.2821 | -50.58419 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 41ba87ac-f906-3458-bcaf-e7b844f45b65 | -6.95829 | -55.64003 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 38595f52-a179-3619-82a0-081642f2f52a | -9.45461 | -45.61666 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 731daf94-d4dd-3057-ade9-9a2607380b6b | -11.12444 | -51.49953 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 158fd5f9-4d56-35e1-94ab-805ece492af1 | -9.15678 | -59.53357 | 2026-09-01 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2edacef7-6cc0-3fed-a805-2b852a1f5c44 | -11.29311 | -50.57877 | 2026-09-01 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 02e3e103-592f-3179-b947-0ace89ced36f | -11.81386 | -46.03518 | 2026-09-01 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd66290a-7dd2-332d-8839-6ea32d043c0e | -6.15515 | -57.7836 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 709c0025-a017-3b0c-bf3f-f508b62519c6 | -11.52297 | -46.93221 | 2026-09-01 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29c0ad5a-0e0b-3961-8bdf-57f61ce2c429 | -6.70099 | -55.41486 | 2026-09-01 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 57200d6e-4932-3e5c-a085-bd268a073336 | -11.12111 | -51.49899 | 2026-09-01 04:40:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1609cbe8-5d3d-3b83-9566-d89d7bd44320 | -7.35939 | -60.58019 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| a3520c92-c82a-39c8-8f50-76a540ba72c6 | -9.46528 | -45.62503 | 2026-09-01 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 45ec99d6-a6cd-334e-9ad1-1d59e5bbf88f | -5.44738 | -45.87291 | 2026-09-01 04:40:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c802e47b-9f20-3eaf-b0fc-2709fa3a7fb0 | -7.35788 | -60.58865 | 2026-09-01 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| df1d3033-a62f-3cab-8381-0c88651f6b0a | -6.60325 | -58.58743 | 2026-09-01 04:40:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7b868d6-fa1a-37e4-8f71-06cb3ea06ce4 | -11.21129 | -46.13679 | 2026-09-01 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bf7b604b-5d97-36d3-a320-4c5b4b9abbe1 | -10.51349 | -57.43391 | 2026-09-01 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2a1ccea-fce4-39f2-9b27-0427a8bcf230 | -6.18355 | -57.7384 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 06b5e6a1-a7d8-32fb-b65d-1f08f2b69ab6 | -6.18853 | -57.73923 | 2026-09-01 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README43.md)
