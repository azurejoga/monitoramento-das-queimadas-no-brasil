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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5761026b-d63a-36d1-ba7c-3b01f6d58266 | -11.79438 | -45.94006 | 2026-07-18 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c4a078b-0d2b-3711-8fb2-dfc9663cb81a | -10.53326 | -48.15967 | 2026-07-18 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9d28af1-a695-35ec-8aa8-1efd78cda6fb | -11.54894 | -48.26383 | 2026-07-18 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 38f69af7-48cc-3e48-a10d-4237d195839f | -9.07856 | -50.59038 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7da773d4-a131-3d89-868e-33c4a7139c9a | -10.83705 | -46.47396 | 2026-07-18 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 458a0f92-a24a-3642-9e23-a699d2b58b96 | -11.79508 | -45.93591 | 2026-07-18 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a526015-a1a8-3bd2-807c-2c2f81fa1b55 | -10.52979 | -48.15515 | 2026-07-18 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd5d9311-e5e5-33ee-8297-69661ba171c5 | -10.52912 | -48.15891 | 2026-07-18 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6054eb1-492e-3f31-9f01-1f1b845799ff | -2.88708 | -42.95539 | 2026-07-18 04:19:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2efb5211-9579-390c-a2ae-a07a53148ee9 | -11.07839 | -40.21527 | 2026-07-18 04:19:00 | NPP-375D | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d82ce89d-eadb-344f-8f89-3de19f9b8365 | -9.69703 | -47.69936 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 423233a3-b6a5-39b5-8762-00707c03ca48 | -11.65688 | -49.76667 | 2026-07-18 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a9a5c98-db51-3e73-8b24-71791c9d9d38 | -11.547 | -48.2634 | 2026-07-18 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ae9a161-a4dd-316b-9b05-d123ee169634 | -8.71381 | -49.60246 | 2026-07-18 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58c5427d-4933-371a-b4e7-fc0bb4fc7438 | -8.94827 | -47.60709 | 2026-07-18 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d498f822-0c0d-3742-8262-3ca3289afc89 | -12.95065 | -44.72982 | 2026-07-18 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 987ca8ba-6b0e-33ba-9701-1b2490fe93e0 | -8.94291 | -47.61377 | 2026-07-18 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e56284d9-f146-3a7b-ba3a-a3af36e1d8d5 | -10.65124 | -47.23075 | 2026-07-18 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5674c7e9-d161-38bf-869a-1fec4d8354da | -11.79796 | -45.94069 | 2026-07-18 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7916d624-7e85-3420-a303-46bbd7cbb5d8 | -9.53043 | -47.12442 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a18f3e4-4206-3713-9168-0e9f5e1b2b0e | -11.40693 | -47.52485 | 2026-07-18 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc4050b1-fe3c-3dc2-aa9d-05397204ae0f | -13.73684 | -51.88147 | 2026-07-18 04:19:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acfd7a76-5341-3f8b-bb2d-9e499a1d4e2f | -10.4758 | -42.47963 | 2026-07-18 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c5cd2669-bbf4-34d1-9268-603b0f7fbe85 | -13.57843 | -47.79878 | 2026-07-18 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9331f6eb-bc5c-3e3a-9c01-af405c1b042e | -9.52649 | -47.12373 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f4669aa-d692-3bee-88d9-69348fb9dbc9 | -2.76797 | -49.46673 | 2026-07-18 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e10254b-22c5-30e1-97e3-a1a8bf8f0075 | -9.16723 | -50.89061 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 347d9aac-2635-3e01-8d8e-80ea44a255fd | -2.79553 | -49.52509 | 2026-07-18 04:19:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28861164-61a8-36bf-a764-939ec18de54d | -2.79036 | -49.52421 | 2026-07-18 04:19:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae9f867a-0cf3-3a88-9599-716d38c3843d | -9.16274 | -50.88638 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48f813e2-6885-32a9-912c-d5ca5432a8a0 | -9.95752 | -50.55563 | 2026-07-18 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6feb43bf-66f7-3c1e-b6f3-a86af613b086 | -11.47384 | -47.3472 | 2026-07-18 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f801c972-9782-3e5f-b310-8bb965991a6f | -10.64711 | -47.23351 | 2026-07-18 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4591b995-00df-3e02-ae07-88fd632e88b0 | -10.65036 | -47.23577 | 2026-07-18 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83ad2b7a-1970-3409-ae43-0d2d23629b2d | -4.10052 | -49.36043 | 2026-07-18 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3e15436-30ed-3973-aaa1-9475cf431820 | -11.22107 | -42.04294 | 2026-07-18 04:19:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9176af6e-42f1-3d44-8ce5-87942448df99 | -13.31791 | -45.15185 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b671e6aa-f3c6-3d72-a8ca-733cf9a9d2c6 | -11.40999 | -47.53057 | 2026-07-18 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6a06b5d-b291-3576-b4d5-a34f184c58cd | -9.69828 | -47.69945 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 434e8593-4410-3cca-9c82-c370714dc061 | -4.82818 | -44.06229 | 2026-07-18 04:19:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b99c2dcb-3047-37b5-8fc8-3c833260cbce | -2.76746 | -49.46979 | 2026-07-18 04:19:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8803dee7-eba7-35de-b8e9-018999dfa88b | -15.65706 | -43.32377 | 2026-07-18 04:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a6e35e4e-ca6f-3773-8f9b-1f61003998eb | -13.31728 | -45.15561 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c4815ed5-ddac-3876-b1fd-f2e825dfdddd | -10.47635 | -42.47613 | 2026-07-18 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 63c13b69-ac8c-3ee5-8da8-31505271564a | -13.31108 | -45.15065 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 5f19e796-01d8-30a2-b1fc-8ff54389634e | -10.36093 | -46.38509 | 2026-07-18 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c409f3a5-db53-3f5d-896a-35a259894792 | -5.12327 | -43.23392 | 2026-07-18 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb6bc5f7-5bfd-3148-948f-c587344705c9 | -12.50763 | -48.25607 | 2026-07-18 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04d7e468-11d7-3e2e-b3f3-9ccd3528dc51 | -9.70047 | -47.70364 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 467c0252-a41d-3243-8b0a-f1c733ff3d38 | -11.59835 | -48.52676 | 2026-07-18 04:19:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec090aa7-ede7-3ff5-a95b-035818595dc8 | -12.45518 | -49.59263 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 685876a6-2d5c-3646-94fa-8b96a9aa6644 | -13.73184 | -51.88038 | 2026-07-18 04:19:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 955e9263-1f6d-3a62-86a7-c42485b4746f | -12.66382 | -48.2221 | 2026-07-18 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f94b2d11-14c9-3319-b325-0c7aa1af6f93 | -9.09536 | -50.61139 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64fcc474-7c65-3aa7-8f33-814b6648f8e1 | -11.54767 | -48.25969 | 2026-07-18 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 38639173-3a40-37b4-a01c-4d27ad54fce3 | -9.53129 | -47.1194 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 316c63d6-0b46-31d6-95f5-40f0fc923dd0 | -14.00258 | -54.00719 | 2026-07-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fc8e0f9c-2a61-3a16-945a-0e2e146c4ab4 | -9.48886 | -46.66311 | 2026-07-18 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3b469404-16d6-3249-8fde-9ba466cfccca | -10.8052 | -46.54801 | 2026-07-18 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afef1cbc-fb06-3142-8b51-e1566a17d333 | -12.30245 | -50.09181 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0462977d-56ef-3c78-ba03-c5bf445f12f1 | -12.45308 | -46.50992 | 2026-07-18 04:19:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c95b6530-a4fc-3627-90d5-918192f39030 | -4.83173 | -44.06287 | 2026-07-18 04:19:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbcf975c-182a-328b-85a6-4ae9f15386ac | -9.60796 | -47.75903 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db145b3-8387-348a-9b11-1d198036c3bf | -8.94354 | -47.61007 | 2026-07-18 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da6f9101-ec48-3c48-be13-8b7c1f034072 | -9.07249 | -50.59519 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 117b8f5b-4dbe-3ebd-b6bc-b584e431d870 | -3.14568 | -48.15248 | 2026-07-18 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74853fc0-7ec9-3194-825b-073872cce81f | -12.38624 | -43.89516 | 2026-07-18 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bae76dc-d26f-39db-9e9e-1d91779ddd6e | -12.11018 | -49.93737 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32687523-5a96-3264-a767-35449a239030 | -10.95313 | -49.81131 | 2026-07-18 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2719d45b-d05c-3d93-bbdb-46a1dad66b68 | -9.16216 | -50.88951 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d8adc40-bd98-342c-9843-1754ff035f7a | -11.4777 | -47.34803 | 2026-07-18 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac86e176-7280-3a63-9ca3-335e554db190 | -9.08931 | -50.61614 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2cd7380-f7b3-3305-9a3d-3a44d1c7d49c | -9.52735 | -47.11871 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41eb89b3-9774-34ea-90ef-dbf0f227bf9f | -2.77313 | -49.46756 | 2026-07-18 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89e88493-2889-3f62-8cdf-a8653c2aad55 | -13.31512 | -45.14749 | 2026-07-18 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 39621a30-a915-3776-8412-dfea6ce6c454 | -13.57582 | -47.79493 | 2026-07-18 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0537b3f-740a-3ee9-9040-0343fbd3d179 | -2.04524 | -48.03711 | 2026-07-18 04:19:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9ca07a79-6b7d-3767-b76d-1c6885729b86 | -13.57457 | -47.79807 | 2026-07-18 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abe98ca9-e788-37ca-a3a5-33963252ffa9 | -15.55541 | -47.3216 | 2026-07-18 04:19:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 63e45009-887e-32be-92a0-c8360dbfd340 | -9.69766 | -47.7031 | 2026-07-18 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df314b0f-624d-31bd-ae62-84f78616be83 | -8.94764 | -47.6108 | 2026-07-18 04:19:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 978e5b57-cb2d-3966-ac3d-df3ef6f704ae | -2.88363 | -42.95485 | 2026-07-18 04:19:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 226a2e53-3b3a-3583-a79d-905b0e4ab150 | -10.84823 | -44.98681 | 2026-07-18 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76059223-b490-392e-b9c5-216e52bd0c27 | -8.71439 | -49.604 | 2026-07-18 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| add1d2b9-0782-39c0-b113-181dfcd91014 | -9.48803 | -46.66792 | 2026-07-18 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9610556c-bc90-38e7-a84b-7795ee880513 | -10.47912 | -42.48017 | 2026-07-18 04:19:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dfa69669-8ea5-3dbb-874b-61fd3da86edb | -14.70751 | -43.21284 | 2026-07-18 04:19:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a49239fc-a938-3cdd-9367-08579ce1d810 | -3.14699 | -48.15421 | 2026-07-18 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 927cb389-3917-3cbd-884c-faa189d3d874 | -13.55325 | -47.78329 | 2026-07-18 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f88e45ad-6049-3af4-95ff-a7c33de987aa | -9.0775 | -50.59608 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0c92c6a-5b0b-36c6-b414-7ade825e327d | -12.11046 | -49.93544 | 2026-07-18 04:19:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8cc4c23-680c-3634-bbaa-d25775bb8b2c | -3.98654 | -47.93053 | 2026-07-18 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaca2fe6-c489-3e34-a7b0-381128dd8192 | -15.24024 | -48.57557 | 2026-07-18 04:19:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e01eb90-1bb4-3895-bca9-5ca359604868 | -10.84476 | -44.98624 | 2026-07-18 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4c597a7-45c5-3513-bf29-3d5c970825ee | -12.6598 | -48.22139 | 2026-07-18 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3af04bd4-4104-3d12-bfa9-91b6642155d7 | -9.49268 | -46.66383 | 2026-07-18 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a4f1541-1892-3722-81a0-cdd1ff7e5b22 | -11.55177 | -48.26039 | 2026-07-18 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f356b74c-9ab5-3a7f-b92c-e4babd6bde9b | -9.0781 | -50.59505 | 2026-07-18 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a05141fa-4b6c-313e-981b-40e596d21169 | -10.95286 | -49.80861 | 2026-07-18 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a1b603e-c855-30fc-b130-a23ce6fad583 | -10.95398 | -49.80652 | 2026-07-18 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README8.md)
