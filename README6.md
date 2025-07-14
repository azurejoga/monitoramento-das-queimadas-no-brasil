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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aeb66e0-248b-3551-8d44-ec518ca5dc48 | -13.65116 | -46.81085 | 2025-07-14 04:04:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 247f7196-0f68-306b-b004-9cc19aac67de | -13.03407 | -47.81375 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 30c8216d-b905-3656-8934-b4d9ab427185 | -13.03475 | -47.8099 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20b7d371-58bf-3545-8f7a-f1669682c7b3 | -17.32236 | -43.47155 | 2025-07-14 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 60a0fbf4-1aae-3ec8-9887-9308f6b755b3 | -13.03585 | -47.81684 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41d24b14-83fe-33c3-a90f-0d26012424b4 | -13.03297 | -47.80833 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2470fd7-aac7-3b3a-810a-042dc29fc482 | -13.03228 | -47.81207 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c4f958a-f3e3-3e05-8690-2dc17914e5ff | -13.03933 | -47.82209 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62bdfc10-0e86-359a-bc59-2d5f58da7f19 | -11.71752 | -47.03708 | 2025-07-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02de0b8d-bd68-3d25-b23e-9cd7a30cedb7 | -19.88902 | -42.61021 | 2025-07-14 04:04:00 | NOAA-21 | SÃO JOSÉ DO GOIABAL | MINAS GERAIS | Brasil | 3163409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 92fc0922-c1ea-3e36-94ac-8bda367f6b4d | -16.30631 | -44.20785 | 2025-07-14 04:04:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ff618e40-1ece-35ac-974d-1444cc628f6d | -13.10297 | -47.30021 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7a1eb99-db08-3ff9-83c6-f26a22de7c1b | -13.02354 | -47.81121 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1a2e5bd-3347-320c-b804-721223518875 | -16.68329 | -43.88308 | 2025-07-14 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c4d96b6-3f26-3330-b6cb-0e2ba2408dea | -13.12782 | -47.26814 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b239388d-e1d0-3253-aa3c-7377e5fee4ec | -17.22707 | -49.56221 | 2025-07-14 04:04:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 757805cc-cee8-315c-ba5a-e17567493ad0 | -13.28975 | -39.87278 | 2025-07-14 04:04:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c3a0d922-d220-3745-b12e-f8abffa0b717 | -13.12494 | -47.27268 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9758d78-0ab4-31fc-b45b-6e2559097f6d | -13.04013 | -47.81773 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e4c600b-2649-36f9-bbb7-9b401f83a474 | -16.73279 | -51.76015 | 2025-07-14 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54bccefa-8075-365d-b8e0-b5ced82c511a | -13.02793 | -47.81155 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1495b9f-a52a-337c-a15a-850bfae3ae1c | -12.41405 | -47.50428 | 2025-07-14 04:04:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00739571-54ef-39da-81e8-095fc1da3102 | -18.03953 | -39.92425 | 2025-07-14 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 38ed8d3f-a4f5-39e0-a31d-faf5c51485ea | -17.228 | -49.55737 | 2025-07-14 04:04:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6a7daf1-7773-34ca-8419-562f4a389a7d | -17.59755 | -43.19762 | 2025-07-14 04:04:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e02f767-37e5-3218-b02e-9442267f7c66 | -13.00569 | -46.31015 | 2025-07-14 04:04:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47e8aa24-d59d-365b-b342-b2c59801d1ae | -17.32178 | -43.4752 | 2025-07-14 04:04:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 867faea4-c7e9-38cc-a9b6-30e1ea0951bf | -13.02537 | -47.81275 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47e19bc9-a533-3630-9d3a-05505898c407 | -13.03042 | -47.8093 | 2025-07-14 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9ea4b56-d5e2-3a38-a1df-90e73aa6a19e | -16.73233 | -51.76069 | 2025-07-14 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 28ef83e9-4e31-3864-ab5a-eed3389b3a38 | -11.71476 | -47.05279 | 2025-07-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cff7c62a-2707-3965-bbbc-c365f3902f90 | -13.14808 | -47.32171 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d4fbfdf9-1b3c-3b89-acd2-8a8debb92d50 | -13.14144 | -47.26379 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b653d444-d491-3a08-a6fc-8e9f08e5193c | -12.13301 | -45.89858 | 2025-07-14 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 747ef150-4b73-3ab6-8641-2fd6eaa87995 | -12.12914 | -45.8979 | 2025-07-14 04:04:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44e9cd62-11ce-348a-93f5-c0b17ab908af | -16.30695 | -44.20404 | 2025-07-14 04:04:00 | NOAA-21 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d230ddb-3ca7-3d2d-a313-12252662e6f5 | -13.12717 | -47.27169 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe9dbb21-7ce9-32eb-a58a-da97fc695c3c | -16.73212 | -51.76339 | 2025-07-14 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f7a3b09b-3514-394a-aabf-9564776271c0 | -13.12559 | -47.26892 | 2025-07-14 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f034ea46-caee-30db-b83a-dd83d26966e4 | -17.09526 | -43.80581 | 2025-07-14 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e5e98d3-4e6f-3a2e-8aec-f5129f290cb7 | -11.71894 | -47.05355 | 2025-07-14 04:04:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e856ef8b-0aac-3d08-959d-d826472bff20 | -20.99533 | -51.79459 | 2025-07-14 04:06:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5679e3d7-0d13-3000-852d-b7ee2a696497 | -22.46942 | -52.40625 | 2025-07-14 04:06:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.5 |
| a62757e8-a8e4-38a7-b786-c97906399bfa | -22.14321 | -47.51295 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7ca3b9e-0ac0-35fc-9a91-06df4f583a66 | -22.07665 | -43.21046 | 2025-07-14 04:06:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9cc0326-5699-3987-b0da-b49d8ddc2eb6 | -22.14602 | -47.51828 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3503c88-29c7-394f-81d9-2f8ea113db47 | -21.17199 | -41.86255 | 2025-07-14 04:06:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3cd1f4f9-319c-3e0d-a3af-33d039933887 | -23.9846 | -48.91477 | 2025-07-14 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae01a957-50d2-3408-9ddb-14b4e949b311 | -21.94203 | -42.27187 | 2025-07-14 04:06:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f469e5e2-a89a-3d75-a81c-868baf101431 | -22.20049 | -41.64827 | 2025-07-14 04:06:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 947760c7-14f1-3b04-90af-80660dbaaa70 | -22.62449 | -43.25017 | 2025-07-14 04:06:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5aeb1da1-95cd-30a7-b40d-e305693bdc4e | -22.13893 | -47.51912 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb45423b-f76c-3bb3-9dbd-674d8e90f344 | -23.08271 | -54.19104 | 2025-07-14 04:06:00 | NOAA-21 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e2c089b7-7dd2-377f-89af-9deaf7aa7461 | -21.49076 | -54.27381 | 2025-07-14 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f823a5f1-705e-335c-88cf-e4b7f51b2244 | -22.41998 | -43.00831 | 2025-07-14 04:06:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f1831f2-7b88-3f8d-9108-00613c1c8e6f | -21.48695 | -54.26482 | 2025-07-14 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 946e9fcb-240a-34e0-bad1-690ba4d81d8b | -22.48504 | -44.06158 | 2025-07-14 04:06:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6a4e666-f669-3966-8fe1-677d356774d7 | -22.14178 | -47.52443 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1e7b5c8-4308-35a5-b626-4850d09b1918 | -22.13811 | -47.52375 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9bad6ad-8b76-3744-ba5e-4893b267d708 | -22.67682 | -42.85966 | 2025-07-14 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9de18417-16e9-3f27-a2b1-1b9082571011 | -23.0853 | -54.19196 | 2025-07-14 04:06:00 | NOAA-21 | NAVIRAÍ | MATO GROSSO DO SUL | Brasil | 5005707 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| bb4bfe1f-b375-3036-ba6f-aceae77396c3 | -22.4755 | -52.40143 | 2025-07-14 04:06:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 1828087b-ea9c-38e3-bfc9-dd812c9da291 | -22.13418 | -47.52086 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fa2c6d9-fb40-3bdb-8806-3de6f438b6cb | -22.14342 | -47.51516 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ba77e2e-0b48-3f10-9119-5d378638761c | -21.49163 | -54.26992 | 2025-07-14 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 04e74140-ca80-3066-813f-d6cbcd14c890 | -22.13785 | -47.52153 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13d5873c-39c5-366e-af8b-f4ce3f3733df | -22.13445 | -47.52307 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 67d12a31-1dca-317f-b6cf-d692351f8a2f | -20.41924 | -43.55177 | 2025-07-14 04:06:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e28835ac-b900-35ab-b2c5-706dc4c6ab4f | -20.14205 | -50.72153 | 2025-07-14 04:06:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 7f591f4c-4a8c-32c0-847d-33bf74817820 | -25.19271 | -49.32467 | 2025-07-14 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32e0c288-8afc-3ccf-a914-5179249f686d | -25.19174 | -49.32971 | 2025-07-14 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 66cd1b4c-735c-30dc-bafd-4694dfb6b1f9 | -22.1426 | -47.51979 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7dc5dbc-f197-3ec3-a7ea-c578ab3c48a7 | -23.63106 | -46.42555 | 2025-07-14 04:06:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76b1393a-a791-32ad-b5a5-5de68a5a5d31 | -25.1903 | -49.32769 | 2025-07-14 04:06:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b4f6e9d1-d74c-32a4-a170-de24153ff829 | -22.42054 | -43.00455 | 2025-07-14 04:06:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a9230079-4f52-357d-b272-200d835d1b6e | -22.1387 | -47.51688 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 442ed851-adad-377a-8457-ca8b772d490b | -22.48034 | -52.40257 | 2025-07-14 04:06:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| 75af58e1-ddb6-30c9-9aee-fc3f566c1da8 | -22.14152 | -47.5222 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ee01340-ea4e-3c44-bebb-f16e704dc699 | -21.04601 | -55.98641 | 2025-07-14 04:06:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f41c95d4-56c8-35a9-82d7-4f7d07027e33 | -22.14519 | -47.52288 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0657195-91ca-3d6a-9498-2843b2ca85a8 | -22.20107 | -41.64425 | 2025-07-14 04:06:00 | NOAA-21 | CARAPEBUS | RIO DE JANEIRO | Brasil | 3300936 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e009ccdd-2c5e-3f69-9382-a4affcd8d704 | -22.14686 | -47.5137 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c37ad747-350d-3112-aa35-671c64c95b6b | -21.91226 | -42.26266 | 2025-07-14 04:06:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a968865-5e93-3f49-8f97-281660a9dee9 | -22.90316 | -43.75668 | 2025-07-14 04:06:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 06acb170-08b6-3fdb-ba78-6fe31ae85adc | -22.47425 | -52.40741 | 2025-07-14 04:06:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| 3d81f9e1-20d5-3b9b-9b07-5c1653b1f2c6 | -22.07608 | -43.2142 | 2025-07-14 04:06:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ea3ec6bf-3d64-3e18-a799-845a72be5987 | -21.62131 | -43.64945 | 2025-07-14 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b1dce6b6-425f-34ab-a8bf-61b557afc24a | -22.14434 | -47.52751 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cbd9f4e-72dd-3b57-82ff-ece6ce680044 | -21.1817 | -44.27522 | 2025-07-14 04:06:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25b7a703-f2fb-3604-b650-1fbb55ec5507 | -22.67739 | -42.85585 | 2025-07-14 04:06:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5dfd6856-d79e-304f-80ab-59af89f02a02 | -21.48608 | -54.26871 | 2025-07-14 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| e392cd30-ebd3-3625-b398-cf0ab1b382cc | -22.13976 | -47.51446 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 097fa924-fae2-3511-ab4d-172f785d1dad | -20.14107 | -50.72643 | 2025-07-14 04:06:00 | NOAA-21 | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 96bc127d-dd53-353f-aaa1-ebe34fed82de | -23.98364 | -48.91986 | 2025-07-14 04:06:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc085774-68c8-37a6-9ece-67a605656b5f | -22.62724 | -43.25449 | 2025-07-14 04:06:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dbd43e5b-ec7d-3f23-b328-1b7a85a8dad2 | -21.4925 | -54.26602 | 2025-07-14 04:06:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a02b70a-e481-3594-b01a-c915662773f2 | -22.47067 | -52.40029 | 2025-07-14 04:06:00 | NOAA-21 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 124.2 |
| d3487460-3e8c-3d43-9996-0e707aa52ce0 | -22.62391 | -43.25395 | 2025-07-14 04:06:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1b0af0d2-ea59-347a-9394-59884d97a968 | -22.14236 | -47.51757 | 2025-07-14 04:06:00 | NOAA-21 | SANTA CRUZ DA CONCEIÇÃO | SÃO PAULO | Brasil | 3546207 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a9f2098-b43a-3d4b-bd5c-835466d23103 | -21.62577 | -43.46782 | 2025-07-14 04:06:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |


[Clique aqui para ver as próximas entradas](README7.md)
