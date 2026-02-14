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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd2e5a6d-25ae-3196-b50b-e5ac96dc62da | 3.87539 | -61.02894 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 834b44b7-cc9b-3be9-98de-7d53c5b7ed69 | 1.83477 | -60.83239 | 2026-02-14 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4738397e-62f3-3e90-92fc-2d2d7327c4ff | 1.80606 | -60.46069 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dab157c5-2c30-3f4c-bf8b-4ea20ac81a7f | 3.73344 | -60.92057 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1acb69c0-096c-3885-8f4f-3cb2d8d728ff | 1.90848 | -60.57881 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54a60446-0266-3e40-b83a-84c7b628ba83 | 4.53914 | -60.71764 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f78246c-5ca1-3c04-beb1-0874d1e9c602 | 3.73159 | -60.93668 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8e8e2d77-b2c3-3698-ab07-e076153bf001 | 3.80758 | -60.89418 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fc10bb1-20d1-337a-9481-2e3aa5cde3db | 3.87001 | -61.02182 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b550ae7-618b-3996-9566-5cbbc05ec042 | 3.74816 | -60.89904 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a423c2e7-9c90-3fcf-974b-7a2bdbec605a | 2.23662 | -60.70519 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b8a62ae1-b4f5-3829-b4a4-9e67b038ffcb | 3.84103 | -61.00126 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e836f127-56f0-362f-997b-3dc375e6ce39 | 3.83919 | -61.01773 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f32c58e-4c7e-3cfa-b18c-3feb027d5c93 | 3.8332 | -60.97817 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 707f5fe9-fba1-3570-9b90-2f030453d035 | 3.87059 | -61.02575 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9ae7a41-8c86-30ec-8991-c0d3f098bd75 | 3.74727 | -60.89869 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab6190fc-d550-3182-b056-e9f27dd1ef2c | 3.11729 | -60.30697 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27965c49-ab92-36c9-bc34-5b3011c616c2 | 3.10983 | -60.31163 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 229ee6ed-5bdd-352c-bfa5-da0fbe0de349 | 2.23716 | -60.70876 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8658f366-6eb2-3078-864a-cbe37801f9a2 | 3.40866 | -60.65512 | 2026-02-14 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26700120-7945-33b6-894b-b1874a45132b | 4.34435 | -61.00881 | 2026-02-14 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4155105f-7142-33fb-a67c-f365b7bce91e | 3.87488 | -61.02419 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0c741e8-7efc-31c5-bc7b-6b2cbc2277c5 | 3.88025 | -61.03248 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c987bbb-1ece-397e-bb57-1c3ff9477109 | 3.74125 | -60.91544 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c897239-e4eb-3e8b-b2a2-cdd90244d3ba | 3.73764 | -60.91996 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d373d9e5-38c5-3907-96b2-a1c82a01ea75 | 3.74426 | -60.90704 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd447c76-76a2-3284-8c6a-43d7fd6a9eed | 1.90741 | -60.57186 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22a546d7-74a2-3b93-81dd-dbf199a06e3f | 3.83333 | -60.92215 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8efbf460-d119-3503-af10-16a288068cc0 | 3.87482 | -61.02507 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3912050-9d69-39fd-9531-06d4983ed8eb | 3.756 | -60.89393 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57653d7a-4226-3993-823f-48dd42d3fe9c | 3.86582 | -61.02173 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 102ba638-bac1-3866-9383-e88524eebebc | 4.38999 | -60.55818 | 2026-02-14 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b587db8-8a89-3ac1-95e1-7927cfa40721 | 3.43502 | -60.21559 | 2026-02-14 05:10:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e638356-818c-314d-ae39-7e4a4688e941 | 3.11091 | -60.3186 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 87fc9f19-b0dd-373a-8fa8-02f79f23b99e | 1.83532 | -60.83598 | 2026-02-14 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 811720f3-f168-3c26-8783-79faa2e9bcab | 1.80937 | -60.45584 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 32f468d1-023a-30d3-b56b-257ce892bfd5 | 2.23607 | -60.7016 | 2026-02-14 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0598dff2-6c64-3031-adec-eccfa244bd91 | 3.87601 | -61.03316 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acf4ced5-b1cc-36b5-b85a-ff460ee1d86e | 3.7451 | -60.90743 | 2026-02-14 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 888014c4-7319-3c81-8212-a167fcf1b5bd | 3.2467 | -61.05097 | 2026-02-14 05:10:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce30d593-bba3-3623-a333-3964ec56738a | 3.30108 | -59.98932 | 2026-02-14 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3eaaab13-b01f-3d84-87e0-7a4534577c45 | -5.14004 | -60.38643 | 2026-02-14 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d76caf4a-8b8b-32d1-9b73-8a8a94193ad5 | -5.69473 | -57.79118 | 2026-02-14 05:12:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 58c2c7d8-d507-3bc6-83bd-abc24a62d4d5 | -5.14928 | -60.37512 | 2026-02-14 05:12:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56e55001-6cdc-3398-a0ed-56eeba50ec24 | -10.6128 | -44.3284 | 2026-02-14 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| fad3fd8f-eba9-3751-8a02-2355dd18be80 | -10.6128 | -44.3284 | 2026-02-14 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d194785b-c8d3-353d-9b50-c1f1a85a168a | -10.60234 | -44.32843 | 2026-02-14 05:37:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.6 |
| c5bc4f70-ecd0-3aa1-b5da-c1dedcc022a7 | -10.60263 | -44.32338 | 2026-02-14 05:37:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| fee28556-3a76-3235-a238-8e271984c421 | -10.59913 | -44.34404 | 2026-02-14 05:37:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 3d10dfa7-396c-344a-986f-7aa5d1b12f64 | 4.54484 | -60.71789 | 2026-02-14 05:37:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e59a0d00-8104-354d-9017-220573713e46 | 4.38226 | -60.35545 | 2026-02-14 05:37:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24688637-26a8-389b-87d0-f7c59567f1cc | 3.80814 | -60.89714 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e4c4749-430f-3833-8232-92600b5bd218 | 3.83198 | -60.91835 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d093d51-b2b3-3dc2-95c0-efebb4048e97 | 3.67608 | -60.93977 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fce0e2dc-805c-3a3a-8b2e-74f7009c0c13 | 2.83099 | -60.77148 | 2026-02-14 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2887756d-55c1-3221-83e1-bc0659937110 | 3.74208 | -60.91109 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a43e301d-f578-3272-8a3e-faff61a9d1cb | 3.74763 | -60.90309 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e17fbdc0-ecbf-331f-9220-951e133cfdd8 | 3.73153 | -60.93056 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab9e50d9-8bb6-37c9-b299-86bff350d789 | 3.19222 | -61.2612 | 2026-02-14 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 279877ed-e56a-3616-811e-774cfa461bb0 | 3.12567 | -60.31211 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 772ae414-7b47-380d-acd3-a73041f75a25 | 3.73209 | -60.93404 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78ca8280-3d1d-34f8-ad6b-bebcc3f3c6f7 | 3.83308 | -60.92527 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce60be1e-9a61-3ce3-a2fe-1f3ed558d399 | 3.86513 | -60.98075 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1a65b7e-d30f-337f-9406-c20ff917f6c9 | 3.11216 | -60.31424 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5535545-cd8a-388f-a2e6-00279d9677e7 | 3.72931 | -60.93805 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a966b7fa-99f9-3b69-9d5e-73bca6274fcf | 3.83516 | -61.02452 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ef1591e-590a-3a14-a9b8-218cfeb60213 | 3.83738 | -61.01706 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 282a77ca-aa86-3556-b514-17035564a9cd | 3.73098 | -60.92709 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| afe1d380-915a-32d6-a8e1-ad171a81fbda | 1.80699 | -60.45751 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89592436-f5de-3deb-a507-6d7f4d573ad1 | 3.74986 | -60.89561 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59fc65ce-0453-3a1e-aa3e-645170c55e2a | 3.84519 | -60.91984 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 555be838-644a-3ce4-86ca-d0848b5261f6 | 3.10879 | -60.31478 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 112e4ab2-108c-3f8c-ab82-156851ba5254 | 3.83628 | -61.01012 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e29b1396-f1ae-3dee-b08c-a34c3373c332 | 2.49124 | -61.30395 | 2026-02-14 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97250059-b0e3-314b-8477-c380663d81d5 | 3.87509 | -61.02185 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74fb0c41-321f-3dcc-ba64-2d2ca9284110 | 3.30095 | -59.98885 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68920116-e62d-34cc-9176-b5aaf5254f93 | 1.91071 | -60.58135 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83884eed-69e7-3de9-a73a-1858ec91e69a | 3.80925 | -60.90416 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72dee5e1-40af-3d29-87a5-2f0a0886473b | 1.90901 | -60.57062 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d305cd5-6000-3976-8714-ddda16bf86a7 | 4.20423 | -60.89939 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ca86a08-445f-37c6-b18b-310f35864f78 | 3.25404 | -61.05266 | 2026-02-14 05:40:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 664e7ead-e0c7-3fbf-a560-70b92d973d58 | 3.80759 | -60.89365 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19374954-8460-3b64-a513-e3fe4d3cd035 | 3.80426 | -60.89418 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83220c17-d014-39d8-bbd3-287d96a2f074 | 3.83253 | -60.9218 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ad26d878-e28c-340d-9ac8-25c5c457f1f6 | 4.20037 | -60.89653 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d4ee483-b8f6-3eb2-a253-57ad6ae840b3 | 1.8353 | -60.83341 | 2026-02-14 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d09cc0a2-ac9d-3e67-8d32-4193d012426e | 3.81091 | -60.91463 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92dfc93d-c5f8-3a36-943a-6cf83a2e3f66 | 3.74708 | -60.89961 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0edf7a35-ec0b-38fb-86b0-330f6320b665 | 3.11777 | -60.30603 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 303433b8-0204-3d83-960b-2e8872558f22 | 3.73431 | -60.92656 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb1f60d7-ddfc-330e-9cd6-2f2db30d9680 | 1.90958 | -60.5742 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b7cfca2-0610-3792-9707-60432bd40cc2 | 1.91015 | -60.57778 | 2026-02-14 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 189a674d-21ff-39ea-83c8-32e2d40b51a0 | 3.86788 | -61.01943 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5062b5df-d708-37a3-a9c7-ae90190a64fe | 3.87176 | -61.02238 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c05443b2-fdaf-31dc-b004-417f909f539e | 3.05091 | -60.45882 | 2026-02-14 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4fae658-9d37-33b1-948a-fcb4b3d1fbd4 | 3.74264 | -60.91456 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b62aea57-5678-3bb6-9b1c-86376833df57 | 3.74486 | -60.90709 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e8d43e5-a343-3275-86eb-08642719d0f0 | 4.26685 | -60.69667 | 2026-02-14 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 591b8783-fbb6-3606-adb5-06b1a7ab5a66 | 3.12344 | -60.3198 | 2026-02-14 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b2c693e-59a1-33ed-acae-387667013a91 | 3.84464 | -60.91637 | 2026-02-14 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README4.md)
