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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8130acc7-71b9-3249-a79a-4f5b69df192a | -9.76645 | -43.45004 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ffa9c3b-070a-3ca4-970f-861c70ae8408 | -4.365 | -47.77607 | 2026-09-08 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| ab8d001d-5d6b-3fb9-b4f1-a18a1ae99b44 | -5.52347 | -44.20697 | 2026-09-08 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdf42146-987e-30f2-b06d-6dea95e90a60 | -2.87146 | -50.438 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a41984d7-efa5-3469-9d3c-f4cc2a6e51a7 | -9.71415 | -43.45615 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cadb376f-ab52-3b31-b166-f2ac56da8223 | -2.63845 | -46.77787 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44755e53-6d11-3135-b8fb-72e43b1c06b1 | -7.3734 | -47.01416 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c56ee05-2c1a-3473-ad39-151015bbb7b7 | -9.71024 | -43.45916 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4f139cb3-d346-37e1-9153-6794fd16d25e | -9.74291 | -43.51191 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3c21d60e-80a4-3efb-b543-d29f290aa6af | -8.09225 | -45.67875 | 2026-09-08 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47f249a7-ac11-3dac-835a-80414c061c72 | -9.76696 | -43.46833 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a9e3040f-4129-3e08-90e2-f402641b62f6 | -6.76074 | -45.4873 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e41bd091-54fe-34a4-b9c5-5e055f6af70e | -2.63278 | -46.77615 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3e93b2d-526d-3065-a117-e4fa1fb57806 | -9.7664 | -43.47188 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6d9cb03b-ab9b-356d-8d15-29c87802c946 | -5.05872 | -44.4393 | 2026-09-08 04:08:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02ef3ac2-d2cf-3b3d-835c-30ead13f199a | -9.71634 | -43.46381 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 414ede65-2fee-337c-876a-18a3c1d8762d | -4.03951 | -50.87275 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa41ff89-1fd7-3c7e-81b3-4cea976960de | -2.98036 | -49.27004 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4d3ea99-fa9e-3721-b349-8332e3b0701e | -9.76583 | -43.47543 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 15f27006-bc80-36ef-9e84-c4b8331fd60a | -6.38637 | -43.74599 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a8a6535-fd58-3f83-a74f-1d5ca3aa8275 | -4.04441 | -50.87737 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da1ee35b-d391-3b78-b249-4533967057ba | -3.26791 | -50.02295 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5974dd85-2586-3b84-b768-27160449d1a4 | -4.57171 | -47.18073 | 2026-09-08 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8e8ed40-4f5c-3133-9cfd-a39086b55df1 | -9.73957 | -43.51138 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b330a2d7-3418-3c42-9bac-f6f3f03699f3 | -9.71138 | -43.45204 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 68f99fa0-161c-325c-b8c1-663cdba1f805 | -9.70967 | -43.46273 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1b9c608d-f4d8-36f5-82d4-18ce5034cb48 | -2.63909 | -46.77379 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67bc9f36-2860-344a-b714-8a943db3e3f1 | -2.87087 | -50.44159 | 2026-09-08 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ba4343c-46d8-3ea6-bc17-a549e8124722 | -2.97426 | -47.33822 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29812d24-0197-33db-8705-d56b3e2d7fa4 | -9.71358 | -43.45971 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3c1e5b09-283c-3c79-a252-639728923dfa | -5.94173 | -51.70263 | 2026-09-08 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb119a46-6122-3419-8f75-afafc3b300fd | -9.72628 | -43.48733 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aaa040a7-379b-3913-b453-9af576fa2baf | -9.74014 | -43.50781 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c3b4d6c-84b5-3ff4-bc54-c2f270e5a8d7 | -3.23242 | -40.86902 | 2026-09-08 04:08:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ddf1a0f-0580-3ace-928a-bdb9ff9ce0ed | -9.09203 | -47.82045 | 2026-09-08 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77dab818-6672-3380-a472-89b4ccb8f77e | -9.72074 | -43.47915 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bf008d4-c5a9-35fb-ab60-a5ac02140b6e | -9.71315 | -43.41958 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| e7a597c3-cbbd-34cc-ba0e-bc2188584352 | -7.37217 | -47.02134 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4e2e01b-0762-32ca-ac68-67eed54afef2 | -4.10901 | -49.05893 | 2026-09-08 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da5f7271-f142-33d7-9dc4-cf799d1d5c6f | -9.72145 | -43.43185 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 111363f3-b4bf-3dba-9452-927b7fb7d7e8 | -5.84985 | -45.16418 | 2026-09-08 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a305ec47-75ad-310b-916a-9e9419a9f7e7 | -9.75989 | -43.40523 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e048852b-bb5b-37fd-9e34-157db222335f | -9.72798 | -43.47666 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a66dc2f-f1c6-3434-a5e6-13d22aace90c | -9.74297 | -43.49002 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d991d367-c630-3008-a1d9-8bb71e212cda | -2.75939 | -49.48085 | 2026-09-08 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8de0f478-ea55-3bd6-8091-f4d498330473 | -2.62988 | -46.77647 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7552c8c1-788b-301f-8671-478efa56fd92 | -9.08789 | -47.81973 | 2026-09-08 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d81c6fc3-462d-354c-99d9-2d92949bf5ec | -6.17308 | -47.08815 | 2026-09-08 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| c561e263-4284-3683-aa01-5e8eda30a6c7 | -9.0589 | -40.26881 | 2026-09-08 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e2492a42-5806-31dc-b892-beedee3d272d | -9.74625 | -43.51244 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b17e09b8-abfa-39b3-8b0f-b0e1dc4cbd9f | -4.98568 | -50.64382 | 2026-09-08 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 958144ef-e306-3f80-a5eb-0c5dd66e9b15 | -9.70748 | -43.45504 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd8c19a3-d228-3523-bd39-6248e50bfb65 | -9.75152 | -43.41483 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 523a6cb4-6a3b-363e-aaed-a2867f0a0e77 | -9.71371 | -43.41603 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| d74c8198-bd93-3a71-ba92-dff876bda974 | -7.29381 | -43.93576 | 2026-09-08 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c119b97f-db46-3320-a960-a1c5444472e1 | -4.9809 | -50.63942 | 2026-09-08 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52e13695-8426-303a-900a-2999ac0e6785 | -7.37621 | -47.02201 | 2026-09-08 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1871225e-6f71-3678-ad7e-a6f579721bce | -2.6285 | -46.77546 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2005b3f-f26a-3bfe-90d4-020b0d578bf7 | -5.59396 | -45.37315 | 2026-09-08 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5df3d5fc-06ba-33ed-9490-41d3591f3a96 | -4.4803 | -48.18929 | 2026-09-08 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cfd279e6-a94e-3298-947b-0327c17a7d29 | -9.72742 | -43.48022 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4cfea16-5b6f-3f46-9c0d-ce52a868598d | -6.38294 | -43.74545 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2b0d4d9-3c99-3a12-bf5d-c5d747346dd2 | -9.77039 | -43.42516 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cafde2c9-e9ee-358f-a8e0-248b798ff02b | -9.7199 | -43.39877 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 266b6b2e-7f9c-3657-bba0-b5cb0b39607c | -3.71706 | -51.14108 | 2026-09-08 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c85223ad-c825-33ba-822e-4166131ce622 | -9.7368 | -43.50728 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09e8aed3-81e9-35db-98ea-480111767ed0 | -9.72465 | -43.47612 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 115a8bc7-3e08-3d25-affa-b118ff256943 | -9.71691 | -43.46025 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b745e2a4-4185-37cf-932d-3bb9bcb97fd0 | -3.88087 | -38.49784 | 2026-09-08 04:08:00 | NOAA-21 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1db11074-8190-3dbf-9c4b-c7741c8495bf | -5.64939 | -44.30344 | 2026-09-08 04:08:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c70ae5b-ad4f-35e0-93c6-3ef25825ba4b | -6.75928 | -45.48424 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 61649051-f4c7-3bd3-813d-da2e06773a58 | -9.71755 | -43.43486 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f20604ce-c0da-3d4f-bc95-a714f582f53d | -9.74739 | -43.50533 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b2f0f94-813f-3133-89f2-b39ab196f209 | -2.63841 | -46.76871 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d4b2126-6868-3029-a347-1f640c69d318 | -9.76527 | -43.47899 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6c1831cb-e74f-3082-87b3-4a096c3b953a | -9.72408 | -43.47968 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8aa078ff-7257-34c1-aa8e-4277d6dfb490 | -9.71485 | -43.40891 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 1cc18ebd-e096-370f-b2b5-f9953a088c71 | -9.31715 | -40.20709 | 2026-09-08 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 5a4e1233-d9d5-3c7b-9922-79dfe1c94aff | -2.96713 | -49.56165 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c3ebc16-67f7-3856-949b-6260efbb076e | -2.30508 | -48.58212 | 2026-09-08 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29265d57-684f-3c22-9058-32a4b0b13f3c | -9.75967 | -43.49269 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32786ce0-7c4a-3580-bd72-c58a15ff6ff9 | -6.38698 | -43.74224 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3a43449-6e9f-3572-8413-086fd33c38c8 | -4.1101 | -49.06767 | 2026-09-08 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fb0f0e65-ec90-3624-8c9a-409c21cf6e06 | -9.70853 | -43.46986 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ea74448-4ea5-3766-a550-98897abf77e2 | -4.57202 | -47.2055 | 2026-09-08 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c5f0f41-5b4d-38f8-b16f-836ab57bf9f5 | -2.64135 | -46.77755 | 2026-09-08 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f161a01-db77-3f95-8abc-89a7b10112a7 | -2.30595 | -48.57671 | 2026-09-08 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab786e8c-5786-3f6f-8c10-7a6d52459c62 | -7.69694 | -44.31465 | 2026-09-08 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 769d5a80-8012-3fb0-818e-b7b4939028b6 | -2.9753 | -49.26923 | 2026-09-08 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47d9f084-56c8-385a-a75c-aa9bb02c13c3 | -6.17371 | -47.08445 | 2026-09-08 04:08:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 6a5d5f74-f47c-377b-ae03-8cfc2d1056a0 | -4.34746 | -47.58122 | 2026-09-08 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 64beab11-8258-3e4b-bef9-609df77b58d8 | -7.6147 | -47.29352 | 2026-09-08 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 951cf6d1-a6be-3103-afc8-d85247dcc14e | -5.75127 | -49.1113 | 2026-09-08 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a565aa4-3010-31f1-b281-daa65d1ef102 | -6.38387 | -43.74223 | 2026-09-08 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73548701-e79b-3d7c-accc-29b90df28fa6 | -4.70179 | -49.15319 | 2026-09-08 04:08:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04ef4026-778e-3c16-bfe2-e5af533780d1 | -9.71819 | -43.40944 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bfd98ce5-0add-34e6-bd15-320ab394cbae | -9.73215 | -43.38622 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65c6ea23-c1cb-3b7f-9e95-c5eda225b298 | -7.29725 | -43.93629 | 2026-09-08 04:08:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50d5ef37-de8b-31ac-840c-bd468e044885 | -6.61205 | -44.72343 | 2026-09-08 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb572fbf-fc65-34cf-bb61-0c87793e1391 | -9.74241 | -43.49358 | 2026-09-08 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
