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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f90472da-78e9-312a-a812-e0eae400f95d | -13.24422 | -47.83305 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26ba652f-eef3-3040-ad26-31fb93da6b44 | -12.70103 | -48.55393 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ee1a97cb-2c0e-3207-a8b1-9c77db5ebe2f | -15.23735 | -56.84904 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ca8652e-7d6e-3ef0-b852-ae37be839771 | -12.81238 | -46.86276 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0711c65b-32ba-3111-812d-2c02e29d35ae | -12.08043 | -47.99508 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be689d4a-80bf-3e24-b42c-64a4c7a4a93b | -9.83161 | -56.37994 | 2025-10-04 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba7baf50-734c-338c-87cf-108f164b7327 | -11.45194 | -45.14263 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2b35c17d-4597-3d9c-83fc-c19ef4bb6105 | -14.93427 | -46.86394 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 3083571e-b952-3ac9-a8a1-16e8da37ca9c | -16.08615 | -51.06968 | 2025-10-04 05:06:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| feba9e67-ef2a-3794-806d-8d988f24bebd | -15.33264 | -56.93794 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09a175fa-4fe6-3749-a463-7352b3785217 | -13.31472 | -48.13057 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6f6d079-e0e2-3d35-9aef-d5b8b0b5a94f | -13.35023 | -47.21921 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdb8447f-9324-3e3a-b112-1dcb82e6727d | -13.74587 | -48.09781 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcd5bcea-d2b2-3ea3-b8e3-054b83126741 | -11.92248 | -46.38103 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 64e01178-acca-3088-8645-44ce5fe804d2 | -13.14625 | -47.80698 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36127c68-200d-3491-bf2b-9b67d769bae0 | -14.67912 | -48.27876 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a58a2f3f-76cf-3f6c-9efb-caa1ef252d89 | -13.32615 | -48.11064 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ef924cd-3dad-3f7d-bd2f-3320a3e0c996 | -11.8742 | -44.97511 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d8ac657b-5d3b-36b0-a57d-b810a0208f6e | -15.20848 | -56.83692 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cade121-bd21-33fc-957d-e99302b80b22 | -15.37327 | -47.95235 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00139749-3bec-37d2-a463-3f92c1b2fac4 | -13.74801 | -48.05614 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 80dc365a-4798-3a46-8a62-e91f1a75a5ca | -11.91756 | -46.37958 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f612b3f-183f-3155-a8d3-db81076beca5 | -11.10616 | -47.75317 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43dc96b9-110d-324d-b17c-a77653fc562a | -13.45283 | -47.25049 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 707e285a-3f1d-35b4-861f-19352c1802e6 | -15.3563 | -47.95342 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0924072d-aa72-3ebc-96db-81ff05335f52 | -12.91984 | -46.79383 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea43b381-7ba3-32d5-b8bd-2263979df201 | -13.18982 | -50.88589 | 2025-10-04 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22ee7e04-5272-3199-8186-afcfa1900095 | -13.12996 | -47.8201 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d73439e5-6d53-3f6a-b5cf-bb80797aeaac | -11.10166 | -49.8093 | 2025-10-04 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3c40d99c-edc0-3911-8c84-d8e3ccd0c86d | -13.60675 | -48.18419 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 283f980f-da9d-3cbc-94fe-28e25d00461b | -10.32012 | -58.49594 | 2025-10-04 05:06:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b421f0-127e-384f-a975-e201c8dcd2b3 | -13.10814 | -47.8941 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a8175d60-2ecb-343f-98de-83ed25f014cc | -11.91522 | -46.24984 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2288954-38cf-3f39-9c80-15060494c414 | -15.2251 | -56.81733 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36d53275-cc09-3b08-bce4-d76208ae1272 | -8.76305 | -64.19942 | 2025-10-04 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1df540b-ee9d-3714-a725-ce287b2338b7 | -11.85529 | -44.95276 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae494b39-7bdd-349d-aff9-fcd80dc753e6 | -14.92651 | -46.8968 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b25cdf1-df63-320c-99e2-4d7426f4fc16 | -11.42505 | -43.4868 | 2025-10-04 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19adf047-e443-3d9b-9e9d-c7108b012db6 | -10.06156 | -59.35435 | 2025-10-04 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea23bea2-b9ef-3524-911a-b5cf5572e3f6 | -14.91523 | -46.89065 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 728bd4ad-c050-31c1-9394-962614f11e50 | -14.8903 | -48.27484 | 2025-10-04 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4ac83a8-95fc-37be-9c12-33d10c51ac5e | -12.30525 | -45.36471 | 2025-10-04 05:06:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4464fe9a-e057-3067-9b0e-cabbfefa1946 | -13.20843 | -47.80945 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 854c787a-23c6-3ea7-8460-ad8948b69666 | -13.22633 | -47.84414 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 154aeef5-1924-3bf0-be5a-66c97b13129d | -14.31039 | -45.86597 | 2025-10-04 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eefa80b1-9746-34b5-8c65-185b62edf10b | -13.77999 | -47.82183 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9b0779b-8302-3050-91af-ff73f1ad96a1 | -15.60895 | -52.47831 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| dd00e993-b4d0-39f0-acf5-3adaf2b9b260 | -11.07958 | -47.87676 | 2025-10-04 05:06:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb072b32-e3b1-3adb-95ae-eac83f17af4e | -14.89307 | -48.34849 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a9de07b8-e5ee-3910-bbd4-99d87c5d759e | -11.54527 | -47.66341 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 097bf30d-0ab8-332e-8cd4-1930b33f5fc2 | -11.79357 | -46.82749 | 2025-10-04 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1c474158-9255-322d-9b07-881a58fef0e8 | -15.5998 | -52.48437 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cede0f8a-8de7-3bd6-9456-1d1f41a947d6 | -13.12187 | -47.82607 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a0bb6a19-858f-318e-94aa-9063e1413441 | -14.35207 | -46.11079 | 2025-10-04 05:06:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f3a1c778-d4ea-36c9-b197-7d8dd75fd379 | -13.13302 | -47.82499 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98fbbffd-6b2a-37bb-ba0a-53c5bf62aac3 | -10.64698 | -55.08998 | 2025-10-04 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e268aae-8dd5-3578-869f-90d5bdd02187 | -13.31631 | -47.26546 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0cd1ca93-d288-3267-a596-5e7e6212e721 | -14.92205 | -46.88308 | 2025-10-04 05:06:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e073a754-71ea-3297-a097-f0e4fa315d5a | -11.05981 | -54.81167 | 2025-10-04 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3133b512-cb76-3c2d-8ec7-2e254464366a | -12.28063 | -55.1324 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92c9cbe-9578-3310-a467-53acee123488 | -14.80783 | -59.71613 | 2025-10-04 05:06:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f76814f-9459-36f4-a442-723e9ebea186 | -12.39087 | -54.44881 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dec3a6f4-8294-3dc1-8af9-6ea218403c63 | -15.31466 | -46.30566 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8e41e5d-0772-3e64-bab4-4e54915da734 | -14.81187 | -59.71288 | 2025-10-04 05:06:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c475965-7b97-38b9-b7ea-ae816b885ab1 | -14.66575 | -48.29978 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4171586a-09d9-3a0a-bd14-30bcd86355a9 | -11.11146 | -47.75387 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 286ff3fb-b9a3-3a5a-9e53-ec8956d25f7b | -14.22402 | -46.08431 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d323ae11-23c7-38bc-8e83-c4ed009641f0 | -15.19034 | -52.78439 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96a2d724-c56d-33ad-b933-0e92e8de09f9 | -11.92151 | -46.38958 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 96b1ee4a-c514-39ec-a0c7-eb48f82f04cd | -11.9219 | -46.39299 | 2025-10-04 05:06:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 550519f7-4d20-3e03-b1c4-20dd15514f74 | -10.98547 | -46.51125 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6858fc0b-dce0-383e-98ea-2b97dc576d98 | -15.59194 | -46.94038 | 2025-10-04 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41533e13-27ea-33b8-9171-0eb81c3c8854 | -11.24427 | -47.79843 | 2025-10-04 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8cc83509-f5ba-330b-adb4-06452a7dfe60 | -12.65398 | -46.99674 | 2025-10-04 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5811f12c-1049-3f6a-bf67-bf729565a55d | -12.30231 | -55.12804 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 204bec7a-bccf-39f9-b7e5-b5eee2c75111 | -12.27434 | -55.12753 | 2025-10-04 05:06:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bfb464a-741d-353a-9100-083881f98ea9 | -11.00532 | -46.68174 | 2025-10-04 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 18254be1-1cc9-3764-9675-4b076cb0c113 | -12.36676 | -54.16626 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4890ef6c-5828-30cb-8e91-dd37039af3f5 | -13.35155 | -47.20761 | 2025-10-04 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 886c34a4-9fb7-3c75-92c7-b97534a1b148 | -14.89898 | -48.39291 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a484f54a-59e4-36c3-8ca2-22d236e5ab13 | -12.9253 | -54.72646 | 2025-10-04 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b60d2f61-2b8e-30f1-af88-ba1f97d8ae2a | -14.20012 | -46.07756 | 2025-10-04 05:06:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d5e62d8d-5391-3849-a43e-29be99a94b9b | -13.70675 | -47.34163 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74c41528-01c9-3fcf-9c3b-8c88d35fe943 | -13.32851 | -48.09033 | 2025-10-04 05:06:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d740294f-52b9-3a29-a9f9-6d053b9b6a26 | -15.7922 | -46.25533 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c1e7e8e-fc69-36f8-aee6-6627f9d30125 | -11.88581 | -44.98757 | 2025-10-04 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d4087c22-6941-3ebf-bf0d-1b3707a20829 | -13.12768 | -47.82356 | 2025-10-04 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8569a68e-37a9-3146-89aa-d243871620f1 | -15.49646 | -52.85637 | 2025-10-04 05:06:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 262e5457-6ba9-3319-b3ea-189de97bd4cb | -13.75912 | -48.05464 | 2025-10-04 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a85a3a6-137e-3a4b-8564-f69f6fccd713 | -11.12172 | -47.88287 | 2025-10-04 05:06:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4399fe04-e739-3747-ae7e-5cc08b8474ee | -12.52946 | -45.97282 | 2025-10-04 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ddb4bf99-071d-347e-b9a5-0d435d7ea3ab | -15.3679 | -47.95197 | 2025-10-04 05:06:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba2ff48b-1215-35d0-be7a-dade1e9b81f5 | -14.6718 | -48.29458 | 2025-10-04 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63afe6cc-0083-32a7-9964-c1eff09a1a03 | -11.70096 | -47.51025 | 2025-10-04 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d77355fa-9e60-3199-9b3f-5985ffd6f467 | -10.97053 | -49.5682 | 2025-10-04 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1391325-5b72-3f2d-8102-59fe2089122c | -13.57419 | -48.18483 | 2025-10-04 05:06:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 783bd327-54fc-3a6e-9b30-4b2067d122d9 | -15.79764 | -46.2635 | 2025-10-04 05:06:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eab5019-d61d-39d4-baa5-02b7101907f8 | -15.23121 | -56.82211 | 2025-10-04 05:06:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4b40cd1-8c17-30de-bef0-c36486fcb52d | -12.72211 | -48.57404 | 2025-10-04 05:06:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06833bd6-7db2-3df1-ae67-b8ca2f043387 | -15.60844 | -52.4822 | 2025-10-04 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README119.md)
