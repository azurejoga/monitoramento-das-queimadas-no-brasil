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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ce926a9-1979-3322-8ed4-635c8e14bfdf | -11.69919 | -50.59782 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2f7959e9-b774-330e-9ba4-fe7ae9d171bf | -11.10713 | -51.33675 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ff8da9ca-0cf2-3765-9d5e-893bc5e58e6f | -11.27653 | -54.43913 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 397963fd-62f8-3986-b76f-867304d73175 | -11.28043 | -54.4361 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e388912f-9ea1-37b0-abe8-3bdbed8c5eaf | -11.61044 | -62.39028 | 2026-09-28 05:12:00 | NPP-375D | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad9531b6-808f-3f00-81ad-cfcc44b123fe | -12.29 | -50.2629 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb7864d1-5f99-3e65-bdd0-a18bf19e51dc | -13.45098 | -48.6021 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d86ea197-541d-36ef-8394-0ba545b8ed23 | -11.78706 | -51.04846 | 2026-09-28 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efcde134-fe15-3b30-be89-785c293f4af4 | -11.37833 | -47.44151 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 807212bc-b149-3291-a1ca-14d2c1edc0fc | -12.80021 | -54.01291 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2ea7344-18c4-32b5-9dd9-c322aa97522b | -10.8258 | -61.41141 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a004b22-44a6-3c00-af44-3d32e914935d | -11.07518 | -51.39761 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b13e9a1b-7fb2-39a2-8952-ac2efc0f2c34 | -14.80047 | -45.95502 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99a0a4e8-21b9-3451-9f10-326223f10cb2 | -10.42483 | -53.83512 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 793e98da-f290-359f-9b5a-ea6f1b0c4f72 | -10.82085 | -57.2314 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11c64045-5a1c-37ac-bf2f-7823c4032e2e | -15.11392 | -53.88025 | 2026-09-28 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59b158ef-2803-3aab-bcbf-14eed129c7f0 | -12.11707 | -57.17005 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f190a8b4-2a35-35c3-a9bc-07ea1cee15ee | -10.92498 | -50.67191 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a104092f-3fd4-303e-8401-f543668aa0e1 | -14.49041 | -53.64342 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4eb75eba-b95e-38fb-b9e5-44136b41b863 | -15.17079 | -46.16225 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cd1a520-0847-394e-b61c-f79ba71ace84 | -12.31456 | -46.40667 | 2026-09-28 05:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f57aba96-998d-3f78-9bea-8a53aff5692f | -10.82306 | -57.19659 | 2026-09-28 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1278e2e4-4910-3170-8da7-0d5caa372535 | -11.69408 | -44.52732 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f9854c0-a630-3b62-82ec-80976f2b2373 | -8.6067 | -63.93134 | 2026-09-28 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09c2ade1-2925-3d2f-bdc3-97d6e766df33 | -13.68757 | -48.81313 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b7f5a1a-3c0b-3df3-b7f1-e51816494169 | -10.40626 | -53.82103 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ebee6f2-1712-35bf-9161-87b1634fbd27 | -13.07519 | -47.43809 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5adbb8fb-21bb-3220-bf80-a5f00047cd22 | -11.70655 | -44.52443 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f331006-598b-3b9f-90e2-3ab2818106e3 | -9.16557 | -61.40414 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 72753977-9f5e-3189-ba1f-68ceb9d5a605 | -15.16608 | -46.15348 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5645d6c1-98d5-3da4-ba35-6658e0bdafba | -14.73419 | -45.56681 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 252b271d-a0d1-324e-adb0-796aded00b89 | -12.18918 | -48.33877 | 2026-09-28 05:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89a8d7f2-ed2d-3a86-a9c4-ebc782cc25e9 | -14.5266 | -48.30809 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd0b1fe0-41cc-3fa4-b7f2-3f29a482673a | -13.70996 | -48.82119 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 32f63903-2b6a-37ee-99a5-ef21d9b40fd1 | -14.51633 | -48.31178 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 054e2e92-7c61-3709-81a8-a4666bae9072 | -10.82426 | -61.41988 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 327ba1a7-bad8-3fb7-8e20-291cc072dd99 | -11.78537 | -48.3345 | 2026-09-28 05:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e984a42-033b-3852-8b4a-25b961d83a0d | -12.13903 | -60.76828 | 2026-09-28 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62e83641-3064-3a1c-b296-1b8544cc93a8 | -10.82657 | -61.40721 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40eeadcb-c39b-382b-8945-e8f2160076fa | -12.76383 | -54.04525 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bdc0609-a74e-3cc7-93fa-4bcc2e41fbfd | -12.14333 | -50.34349 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9834f4dc-750e-3237-87de-11319d2f647d | -12.55449 | -50.08212 | 2026-09-28 05:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71988a16-83e5-350f-9b37-426346aaff4a | -10.41526 | -53.82989 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22e7ad1d-4807-3051-bb6b-061fbebbc3e3 | -10.41864 | -53.83043 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fbd537b-f4f2-3715-8b55-735635d811c0 | -11.10264 | -50.68188 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09665342-a559-3d54-97d1-7d6f758d2053 | -10.89147 | -50.68224 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c8ed378-5caa-331f-b147-7824e6cca11c | -13.46464 | -48.59153 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0b3d1a77-0836-3150-bace-a67eeaa7b3ea | -11.3562 | -47.43316 | 2026-09-28 05:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f29e093c-fa56-3199-89c8-cad0e513eb50 | -13.15722 | -48.54585 | 2026-09-28 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cf7649b-7284-3763-9fcb-0aa5272a030b | -12.70759 | -46.99171 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4bdb4c95-1488-3a07-a0e7-c93e6555a4e1 | -12.18452 | -48.33811 | 2026-09-28 05:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 777d4f29-5822-31af-9129-94f36b4f96df | -12.1339 | -57.23824 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 846d8be8-3ab3-3cfa-8c83-c32e785dd8f9 | -15.1712 | -46.15862 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3b0db01-5731-31fa-b843-3c5deffbd548 | -12.6891 | -46.97282 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a65fba8-7730-3c16-b594-87ec0cb84a39 | -11.78373 | -48.3374 | 2026-09-28 05:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd219714-9c36-3fa2-851c-d6f48d08086d | -9.92931 | -60.71827 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 565275cf-1e05-34f3-bab4-8f8ff9e60d5f | -12.901 | -52.04778 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89acd94d-bf56-3c0a-8a15-a78e80cedb06 | -10.41695 | -53.81901 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f03744d2-7aff-37ae-801f-022097bacca5 | -10.82146 | -61.41058 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a0eb4d9-9384-34bd-aaff-fee4760230ad | -13.15312 | -48.54111 | 2026-09-28 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3522b75d-31d6-3aa8-b975-4fd93a811a5c | -11.10781 | -51.33214 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3d6c4359-bdbc-31bf-be10-496fc8cba5a0 | -10.89466 | -50.68779 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78b286c4-20e7-3e25-9ff1-f0d79f9da938 | -11.4232 | -47.41643 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 23323cc4-7eab-3896-b534-ab881285e7e2 | -12.64005 | -47.31319 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cda52b2c-cc17-363a-93af-7f94ffd3aeff | -15.1894 | -48.43432 | 2026-09-28 05:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99717f74-8c48-354a-b0f8-b6c90a2c79b3 | -11.37683 | -47.42775 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9d7afe5e-b6e2-31be-b3c0-29c4119b9956 | -13.47087 | -48.5952 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76dd855d-6189-34fa-9541-f58a1572cf53 | -14.72841 | -45.56596 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 50a1d5a2-5e29-35fc-8764-8ec9cca11252 | -15.40864 | -47.90357 | 2026-09-28 05:12:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a2bce99f-06f1-3071-bb15-dbf9c50d449f | -14.72174 | -45.57292 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1811437d-ea9d-3a40-8945-f8a6e69cc756 | -15.05823 | -47.23074 | 2026-09-28 05:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 751b6394-a0ac-3ccb-bf03-b3dadc6b0bd0 | -10.81971 | -60.74861 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 170e8cfc-e516-356a-b4e8-3670104a35e6 | -12.15729 | -50.35996 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e4ae11bc-4cb4-3c24-a001-112e2c704fc1 | -11.44506 | -44.92782 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df1b5dff-5803-3d0b-aaa1-dde0f45ca6b9 | -11.14351 | -50.04683 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c16ac0d-8751-3a44-a4bf-dc9ec250493a | -15.17606 | -46.16601 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2da82aa-4f12-3358-89f1-b42b8ec2cc1d | -11.38019 | -47.4278 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cad50af2-2ab7-36c9-92b1-1bffc0be2b5d | -12.65512 | -47.31524 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ea29c472-395d-3229-a870-da5102ae1f7c | -10.4192 | -53.8268 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1ea78f3-4d9d-3eca-9012-34b01cfaf5be | -11.6995 | -44.53248 | 2026-09-28 05:12:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0032b7a6-a8ef-3554-8fb1-a9d1622bce74 | -11.44989 | -44.93629 | 2026-09-28 05:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8b140856-148f-373c-b387-53c11eaa0216 | -11.54395 | -50.51938 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c6f2325a-3270-3fff-817a-f8dff578dae3 | -11.70715 | -50.599 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b89397b-4f72-3e0b-918e-fe9e3933cfc8 | -11.63402 | -46.77732 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfd7d73d-8674-3f27-811f-dc5056dd5fca | -12.62448 | -47.27507 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c665fe92-d174-3aa8-80f4-c3a056e20129 | -10.40963 | -53.82157 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7ae01a5f-d017-32b0-b278-4c8c5b4253da | -12.1482 | -57.23678 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bd13c5a-cf1f-3670-81a6-76c4f59c6002 | -13.71578 | -48.81257 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4e2afb84-4935-311c-869d-28effef7e791 | -14.90366 | -49.49335 | 2026-09-28 05:12:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a5a16cbb-6421-3142-b011-1553d957ab4b | -12.17469 | -50.41406 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0955fbe-8263-34f3-ac7f-34c496026fc0 | -11.78899 | -48.33322 | 2026-09-28 05:12:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11b23e81-313e-3cbf-804b-124003d22f7e | -12.06554 | -46.48161 | 2026-09-28 05:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| db860a4a-ca7d-3297-a115-15da6505ff5c | -11.41255 | -47.42154 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ad812bd-325f-351d-80f4-add7014e0018 | -13.15478 | -48.54414 | 2026-09-28 05:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d0bbca93-54c5-31aa-8e48-13ad94c7d471 | -11.04194 | -54.03864 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bdc74f4-ea41-3140-9684-bba9a82d2528 | -10.41807 | -53.83406 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9880a440-6cc7-3609-bf05-f1810e7928ba | -12.11366 | -57.16947 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23320ceb-fab3-3ba1-a653-9122a0f4e613 | -10.8204 | -60.74478 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 54ca921d-9024-3780-8851-344abc9471b6 | -11.3653 | -47.43991 | 2026-09-28 05:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65f56dde-81c2-3ed6-9ecf-85e4ffb9da13 | -11.13432 | -50.05296 | 2026-09-28 05:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README57.md)
