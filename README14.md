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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c7ebfc9-6280-3419-9f96-d45b71a84464 | -21.24666 | -50.01129 | 2026-09-05 04:04:00 | NPP-375D | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 5d6580e2-0d19-35b5-a9d4-768c6375dd4b | -20.34358 | -47.59314 | 2026-09-05 04:04:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80dff2cd-19bc-3db5-8038-f5b5a7ab6309 | -18.17005 | -42.93917 | 2026-09-05 04:04:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f9962f3a-7910-36d4-a840-ad5a6069f2d9 | -21.2967 | -51.6735 | 2026-09-05 04:04:00 | NPP-375D | SÃO JOÃO DO PAU D'ALHO | SÃO PAULO | Brasil | 3549300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 58d7f1ac-6eb1-3657-b118-f96237faa3b9 | -21.55151 | -44.05635 | 2026-09-05 04:04:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8bc702d0-1ebb-3488-b58d-4e257689f888 | -20.82673 | -46.31059 | 2026-09-05 04:04:00 | NPP-375D | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f93cbab8-9003-3242-afcf-79efa464c43f | -21.46122 | -48.67675 | 2026-09-05 04:04:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cabb12ab-f6d1-34ce-b89b-3e80589ca1d9 | -20.14337 | -46.32965 | 2026-09-05 04:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48269566-6346-3ec9-8ec0-4915ccb656f8 | -30.61361 | -52.50083 | 2026-09-05 04:08:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 44f4acee-ffe1-36a4-a5d7-609fdfd96f88 | -30.61533 | -52.50191 | 2026-09-05 04:08:00 | NPP-375D | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6edae40f-de87-3298-9c4e-9e2c9604befd | -6.6698 | -59.9443 | 2026-09-05 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| bf3f3714-53c8-30c0-a4b2-68c098c99214 | -5.3277 | -56.0263 | 2026-09-05 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 8af861f8-98fe-3754-81b6-5cbdb8601058 | -6.6514 | -59.945 | 2026-09-05 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 139.8 |
| e53e2d67-2286-3361-9666-6cc5b2363ace | -6.6697 | -59.9635 | 2026-09-05 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 87c1f763-7b96-3798-a497-0415ee372d39 | -6.6513 | -59.9642 | 2026-09-05 04:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| ec021957-0a3e-3e09-adab-c2df3c3bb839 | -3.7645 | -61.7737 | 2026-09-05 04:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 9c3f7980-309e-35d7-8c93-a58813505076 | -5.3462 | -56.0256 | 2026-09-05 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 7b41ea21-8e8e-3392-9658-8de506b0deba | -5.346 | -56.0454 | 2026-09-05 04:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 08aa6eef-ba28-36f7-be85-076823876a45 | -1.18634 | -53.83059 | 2026-09-05 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 482e89b4-1ba7-3df6-9fc2-5857e35e3279 | -3.71648 | -39.62554 | 2026-09-05 04:17:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5bbe5452-f599-387d-ab7e-48368d7aa61e | -1.18295 | -53.83163 | 2026-09-05 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e4c17617-a6f9-3707-8ae8-863130f9d799 | -3.44107 | -43.27415 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1208606d-1a44-3e66-9277-309251db3236 | -3.47041 | -43.34638 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26e72d64-b0e3-3cd8-88a5-a59e15b816d2 | -2.87065 | -40.4108 | 2026-09-05 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5f4a3519-844e-3f65-9973-bfc3c5ed884a | -2.88678 | -40.39794 | 2026-09-05 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9473b1c2-35a7-3e5d-9b72-993f813e5d8e | -3.611 | -40.87497 | 2026-09-05 04:17:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 269ae2aa-4387-3eca-a81f-a692a6b32442 | -3.0507 | -39.93217 | 2026-09-05 04:17:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b957ee6d-a940-318b-b10f-1fc05cc6331d | -1.1811 | -53.82325 | 2026-09-05 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 431630e8-b7d0-373a-8c0b-b3eb39c30ba5 | -1.18021 | -53.82855 | 2026-09-05 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45a0e5e3-6b03-378f-b6de-0bd9d9cacb0d | -2.7717 | -47.77588 | 2026-09-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ade29743-f35c-3d88-9ed8-64f03ca8103c | -2.45692 | -47.58368 | 2026-09-05 04:17:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 332ef044-1167-3217-9468-87a6029d7f5f | -1.83713 | -47.9292 | 2026-09-05 04:17:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76f8933e-6a84-33ec-b0a6-4ad2bba3cdea | -1.17759 | -53.82471 | 2026-09-05 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aa69ae4e-21a5-370b-a63b-a0092245b58a | -3.44439 | -43.27468 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7fef500-a6ea-386c-8cd6-40b7bb418b16 | -3.96709 | -40.43476 | 2026-09-05 04:17:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f04c1990-a38b-369b-819d-2f254c310be8 | 0.21304 | -51.5122 | 2026-09-05 04:17:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e7eb03b-ddeb-320c-b0f9-c8b141a90684 | 0.21362 | -51.51586 | 2026-09-05 04:17:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0007be3-12e3-34e8-822a-0c561ba28244 | -3.44217 | -43.26722 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8801d6bf-2d8d-39b7-ae1d-3c07826d3147 | -2.10959 | -49.52776 | 2026-09-05 04:17:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f9eb616-1574-3825-a1b1-5062673ae158 | -1.95378 | -48.22713 | 2026-09-05 04:17:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c29aae7d-26c6-32c8-a3b3-7721cb4c3a20 | -3.4391 | -43.26671 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05af998c-eea2-38d6-a2a1-7c9745806acb | -2.03179 | -47.90141 | 2026-09-05 04:17:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9248c032-da50-39e1-89fc-823b177275e6 | -3.44162 | -43.27069 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a11e78cb-0587-339e-8d6c-f040efa4ca1b | -4.26705 | -38.0153 | 2026-09-05 04:17:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 16.2 |
| ae5f5044-8728-3c57-a2ff-fa88021e246e | -3.47096 | -43.34291 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af4f56e7-3ef8-3f04-b820-000b882f94b2 | -1.80964 | -47.88309 | 2026-09-05 04:17:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fcc66e8-09e6-359c-bcef-5140121c8c38 | -2.8244 | -46.70863 | 2026-09-05 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 512c3794-289d-31ac-bf52-9dbbd57e09ac | -4.29525 | -38.52744 | 2026-09-05 04:17:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4a7b07bc-c8e5-3a84-9dc8-f61c3c0dcf36 | -2.85498 | -40.46581 | 2026-09-05 04:17:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d7794462-88df-300b-b1a6-6ce189f78f8a | -4.29681 | -38.53032 | 2026-09-05 04:17:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c12eff85-3c39-3fe7-b7fd-f9bdf07b3b64 | -3.43965 | -43.26324 | 2026-09-05 04:17:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8400cbab-a16c-3841-b193-c8a8f1340370 | -4.26509 | -38.01685 | 2026-09-05 04:17:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 17108bea-f737-332d-9627-04d0f5eda661 | -1.1838 | -53.82635 | 2026-09-05 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e596513d-358c-3152-b833-281e4fb1efeb | -2.55189 | -45.80098 | 2026-09-05 04:17:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53fd27ba-4909-339e-a8c6-b172b0c689bb | -3.44273 | -43.26376 | 2026-09-05 04:17:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 971311b0-28c7-3ce0-9785-b781466f21a8 | -5.16948 | -56.05782 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63d7bbb7-f33a-3180-ad70-1e7404d2bcae | -9.78576 | -41.99899 | 2026-09-05 04:19:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 165e6911-9bd8-340b-bab0-93af8e40b57f | -7.66892 | -46.05768 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d410263f-fc52-3393-9ad5-565db6d5a8ef | -5.2963 | -56.02183 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aaf437da-8369-30f5-b641-10949d5daa4e | -8.96854 | -44.42817 | 2026-09-05 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9929ad8-e1b9-3c3f-9e06-2e98f3006179 | -5.41383 | -43.2609 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3046251-5684-36c3-bf7e-7a3676139a3b | -5.21577 | -44.31469 | 2026-09-05 04:19:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50f2dc9d-da87-3eec-bf35-9fa09fa5e525 | -9.61036 | -48.5643 | 2026-09-05 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e6c199-6f0c-3974-bb1c-5cbc462eea6e | -6.42014 | -46.20113 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30d36736-81c7-3617-a970-902799db8b15 | -6.12759 | -43.75088 | 2026-09-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f71410a-9993-3221-9e57-3a0bcf6b6e77 | -5.30304 | -56.02315 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9fb6511-ecac-39df-b550-310eba7c25f5 | -7.69923 | -44.33496 | 2026-09-05 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4f833ac-c822-316d-840a-0dd911ea26da | -5.17734 | -56.05301 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b929b8b-e7e6-3065-9233-e26c0ea0d916 | -3.22343 | -48.61122 | 2026-09-05 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17a3aad4-0182-3d76-bd4c-d97592cbfa90 | -5.41941 | -36.76809 | 2026-09-05 04:19:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f45959a5-2724-3aab-a54d-0311067feeed | -5.84646 | -52.04163 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cdc27505-1978-3425-91fa-cb65f438773d | -5.97905 | -43.61669 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3604165-62d4-3aa1-b8b0-34c6ae3cc245 | -5.20731 | -39.41145 | 2026-09-05 04:19:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb12cf08-f0ae-349e-89cf-d06c628c36bc | -7.46067 | -46.15346 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 049d3a8e-493b-30ec-8b1d-aac998624b44 | -5.21913 | -44.31524 | 2026-09-05 04:19:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 164a0a40-4346-3d98-860a-ba43f961dc0b | -6.35456 | -46.11158 | 2026-09-05 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8bbecee-2c67-3ecf-bab0-9bf3540723c6 | -4.73862 | -48.13871 | 2026-09-05 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32c6a30d-8f78-3b33-ba33-eb4f69dc7b8c | -9.61509 | -48.56 | 2026-09-05 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb81e368-1bdd-3300-a15b-5823338da14a | -5.29907 | -56.01826 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 693c017a-2b4d-36c0-b63d-fffff5bae025 | -4.90825 | -43.4711 | 2026-09-05 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f1b1e7ab-50f6-3735-8d37-8c67067aafbb | -9.29945 | -47.62523 | 2026-09-05 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fb8b4cd0-73a0-3d40-9413-7118cc11d3ab | -5.28953 | -56.0207 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bc4cf25-0d95-3279-bfd4-fe9bcea74d94 | -5.33733 | -56.03805 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f938ed3d-bdd1-3f79-9e4b-badb31eda7db | -5.97574 | -43.61617 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9e93411-2bab-326f-9980-3f17e111523a | -10.16849 | -36.22403 | 2026-09-05 04:19:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e05730aa-49d8-31da-9637-303a74893981 | -6.12372 | -43.75384 | 2026-09-05 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cac0755f-4a4d-3f0d-8053-dbba7266783a | -5.34407 | -56.03935 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 04cb00a7-32f4-3f85-a538-86fd2a5d01d8 | -5.61482 | -44.93438 | 2026-09-05 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6f9bcc4-97d9-3e1a-98e7-ff1c0c00545b | -5.17516 | -56.06524 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f4fdf7c-938a-3225-b857-a7467d4881f1 | -5.84589 | -52.04494 | 2026-09-05 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bdd3b229-3814-35db-8eee-0a69b8a7d8f7 | -4.36493 | -47.77771 | 2026-09-05 04:19:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 56e100ab-3d73-3b84-94de-0baa388e77a0 | -5.34518 | -56.03326 | 2026-09-05 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f1435a0a-5e62-327b-bb6e-aad6f292e616 | -6.12099 | -44.68579 | 2026-09-05 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdc8aee6-9c8b-326e-bdfa-38679a28df17 | -7.07641 | -44.32125 | 2026-09-05 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66c62b24-750b-38aa-a244-999fab7f63cc | -4.17756 | -42.44353 | 2026-09-05 04:19:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 205c20ac-cb6c-3c76-bae4-7660406353a9 | -5.41438 | -43.25745 | 2026-09-05 04:19:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e24e7c9-d667-364f-b7ca-04aaf5edbb42 | -5.98237 | -43.61721 | 2026-09-05 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95cd99ad-f283-34b4-bc9c-8716b901f878 | -6.71487 | -43.47521 | 2026-09-05 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f420386-efcd-3522-87a5-e69592d07c80 | -2.80554 | -48.6786 | 2026-09-05 04:19:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c244171-4a97-31d5-839b-2dd649533143 | -7.46262 | -46.14168 | 2026-09-05 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
