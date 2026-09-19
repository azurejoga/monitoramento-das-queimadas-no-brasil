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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7badcc16-4f1c-3804-a906-74f49f8a0407 | -5.2304 | -47.566101 | 2026-09-19 00:41:00 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d39c3de1-052a-3c5e-ac2c-64e180cb0201 | -10.0245 | -51.907902 | 2026-09-19 00:41:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e06fbc88-510e-3f75-a0fa-3723df3cd2ee | -4.21538 | -56.33373 | 2026-09-19 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 1cc7403a-fe56-3582-8f3d-5b02bdf39130 | -3.76065 | -55.9619 | 2026-09-19 00:41:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f2438076-2b7e-307c-b11a-53a0fd7d1448 | -3.33277 | -59.82309 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 45c5ba63-2d3d-3d00-9a51-740683986b8b | -6.36346 | -58.27852 | 2026-09-19 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ffc4e7d8-d534-3a89-ad45-d14a7de35413 | -3.51456 | -50.81266 | 2026-09-19 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 13b36a9a-4918-3103-9544-38a9d7272bea | -3.11745 | -61.41186 | 2026-09-19 00:41:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 70cb6ef8-0f6f-347c-8c50-197d861f031d | -3.36401 | -50.43734 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| b615242b-87ff-3a86-98ef-a20515a09ab1 | -6.44325 | -59.97665 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 63602038-f95d-3907-aa2a-e2df9608bb96 | -6.94084 | -55.04378 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 85b24e0b-8302-381a-bfa5-516ed014c33d | -6.76391 | -59.43112 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6d37e129-951c-3ee8-910c-4e98828d7072 | -1.59627 | -55.5588 | 2026-09-19 00:41:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d1058fe0-befa-39e5-b60d-d5a3d2967440 | -6.81421 | -59.1927 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63fbab22-71b6-3299-8680-a39eda314c96 | -3.34645 | -59.8571 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 68270f48-1e22-383c-98f8-50c71bd58c45 | -7.55517 | -61.33103 | 2026-09-19 00:41:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| d2201f82-4768-332f-986c-e1007a273a93 | -5.99281 | -51.81277 | 2026-09-19 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 272cf4b5-7fc0-3d7a-9f1f-380d3d5d731f | -8.47629 | -57.63335 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a8fd91d2-9844-30a1-a2a2-34b77527b5cb | -3.33916 | -59.80421 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1e5fbc88-91aa-301c-b89b-95a5e47a8e2a | -4.49021 | -54.97508 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 46399906-07c0-3cf5-aae6-d72189623c2f | -6.09617 | -57.68629 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 37e8df99-1b1c-3a30-adb7-2b501dd33103 | -6.13195 | -59.93682 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d0eb363e-9f8c-3b50-9621-966de33f9ac8 | -4.06228 | -56.25277 | 2026-09-19 00:41:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b3bfc819-738a-3ed4-b834-9f3e224bb391 | -6.14204 | -57.69377 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 94824978-d6c0-3dd8-b8ff-6e0672701f30 | -4.49243 | -54.99034 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7f2f982e-08e5-3b19-a81d-a45a36aa995c | -6.00317 | -51.78448 | 2026-09-19 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ec73bb13-1d7a-3310-86e4-3749a1a658f5 | -3.14456 | -61.40218 | 2026-09-19 00:41:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b646ef36-19d0-3806-a216-d6f7672df725 | -6.7451 | -59.4248 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 25de4148-0134-398a-aecd-76e6e76e647f | -2.81358 | -50.44653 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 063d9b1f-62e7-33b9-b938-c9e2702f6ecb | -4.80361 | -56.08989 | 2026-09-19 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 387e28f5-ed19-3e7f-84c8-1ab0798f591c | -4.80118 | -56.21805 | 2026-09-19 00:41:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 35874313-50e4-3997-a0e9-a3aad27de5fe | -7.30065 | -59.91829 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1a8e2a3f-7bc5-3c23-bdb1-589b03959310 | -6.93711 | -55.03644 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 14bca9f6-fd97-3afa-b116-b0db0c86b7fd | -5.75858 | -57.45729 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bfd0fe68-e1f3-3d3a-8126-94fea5d35cdb | -3.11869 | -61.42088 | 2026-09-19 00:41:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 29168ab9-4f9c-3839-a98e-03aed7a60b46 | -7.59321 | -55.70158 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5ea9d315-0332-3c66-bd12-d0eff140111f | -3.10976 | -61.42211 | 2026-09-19 00:41:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 26328d69-1079-3501-9e92-3753b8a0406d | -3.33155 | -59.81427 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 34086f18-78d9-3f6c-be95-9abcf9d02b25 | -3.69355 | -60.63044 | 2026-09-19 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 680148c1-2964-3077-9c62-2a829fd869d7 | -2.83618 | -50.48218 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| f62b6ec9-201c-3a91-8dda-e02621d8f32b | -5.74128 | -57.60415 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f312cbfe-0828-3592-acbb-2dd866e7217a | -3.69235 | -60.62164 | 2026-09-19 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b3d11e1a-a7a1-3e60-ae0f-d802dc7ce1d1 | -6.13316 | -59.94563 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 0b41a8f0-5e0d-337b-a702-cf21a0d6e1c7 | -1.19422 | -54.22478 | 2026-09-19 00:41:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 88e549a3-8e1c-36c0-9d34-d9b072c370ea | -3.05318 | -61.27408 | 2026-09-19 00:41:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bead7102-da2a-3ef7-809a-2e9f5c6b53bc | -7.58221 | -57.69885 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2112712c-5183-3446-aabd-536ee97a75f8 | -5.88143 | -53.54947 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9748c6cc-0bb1-3afe-b962-5ea96b1112f9 | -3.75531 | -55.95526 | 2026-09-19 00:41:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 93a800d4-b6a1-3095-bd41-57a3bf52b6fb | -1.64126 | -55.1487 | 2026-09-19 00:41:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| aef79836-6a2c-3d58-a247-321fb70eb175 | -6.20214 | -57.78495 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 099f99cc-a1ca-3a4a-990b-db7baa4da000 | -4.36131 | -55.4332 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8a0942d7-96c6-3985-9d25-c80859c2c5d8 | -2.8229 | -50.47935 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 208.9 |
| 682546aa-15f9-37ad-8f59-173f2786837d | -5.89403 | -53.54762 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 35b98500-f3c1-3a41-8087-59b58ac28986 | -3.60609 | -59.06736 | 2026-09-19 00:41:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9a34e4fb-ccc3-3b36-9fb5-6913f51c4cf1 | -1.31309 | -55.82654 | 2026-09-19 00:41:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f0b6c14d-acb4-3a2a-9d9d-d6fab856733d | -6.71076 | -59.45351 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ddadcf8b-d8c3-3d9e-8d7d-0bf7ff0955de | -4.53171 | -54.93696 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f9c27c3f-5a2d-3cdb-8bc2-ac7350413889 | -4.38208 | -55.25914 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 5610a476-e92d-36e7-97b6-4f06e13c52ed | -2.8193 | -50.4848 | 2026-09-19 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 23fde359-fb90-3e7f-b7c0-2debcd1431c4 | -7.57172 | -57.69061 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| dd873c28-fe82-3863-acc3-cf5d4a8591d3 | -3.03941 | -61.23949 | 2026-09-19 00:41:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bea8ec70-0ccf-3417-a026-17d9a8ba9fe0 | -3.34037 | -59.81303 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 470944bd-7e8e-3770-af85-a4b23ed63196 | -6.71197 | -59.46232 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7b70f65d-6aec-3d04-b8cf-6485219db072 | -1.59126 | -54.44246 | 2026-09-19 00:41:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 441af083-6183-3572-a13e-562960fb4a3f | -7.55388 | -61.32129 | 2026-09-19 00:41:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c65782c6-bcf1-32e0-82b5-a63ded1843ee | -6.36735 | -58.30637 | 2026-09-19 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 129cab64-7382-38f3-90f5-70c1f01fdadd | -3.71238 | -60.63678 | 2026-09-19 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6cf0f50f-3972-3159-b470-22eadb9d01d3 | -3.52399 | -50.81812 | 2026-09-19 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 7ed108a5-c181-39e7-8ea3-2535560f8beb | -6.621 | -55.69754 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 883a3799-df38-3c9a-bc6a-013ed9352e1e | -6.92775 | -55.0313 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ecd9fb0d-7d2d-3b41-985d-0368a6cc1ea5 | -6.15412 | -57.71217 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1bf0859-891d-320c-9821-30c3f767f747 | -6.32873 | -55.28521 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4b1842d1-9b8e-33d6-adf3-dee8f083d92d | -6.00728 | -51.8107 | 2026-09-19 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| f086bce9-22e5-35ab-a52c-fe46bea09c09 | -1.19241 | -54.21907 | 2026-09-19 00:41:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| f14abbbd-83ba-3d7a-928c-e08230b83293 | -4.48518 | -55.49703 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b461a535-5b6c-30e3-970c-9a7640ba30c2 | -3.5188 | -50.78334 | 2026-09-19 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e20206f4-148d-379e-93fc-2a48dcec138a | -6.76702 | -55.84926 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4e29b5f8-255c-3193-bdb2-da677cc6ed54 | -3.49319 | -59.3107 | 2026-09-19 00:41:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 25319998-65aa-3a19-a0e7-ef4a7c89c399 | -6.33846 | -59.96752 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 954a8994-e58e-3f90-9dce-44c002723318 | -4.31755 | -60.88589 | 2026-09-19 00:41:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 001a6d4b-a050-37b3-a22c-35ddb8a50728 | -6.37765 | -58.31433 | 2026-09-19 00:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 3b754442-193a-390a-9171-e382eca20373 | -3.45095 | -58.22327 | 2026-09-19 00:41:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 03accb2a-0d06-3648-9f94-95b7cf95d1bf | -4.54028 | -54.92949 | 2026-09-19 00:41:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b379adb6-e9ec-3e24-9d90-cc06aab86e38 | -6.33112 | -55.27905 | 2026-09-19 00:41:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2b2c88ea-738f-3d7e-b503-0ea6a240396c | -4.06049 | -56.24008 | 2026-09-19 00:41:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| d8e43802-58d9-3b27-b067-9849c7cbc775 | -1.22967 | -55.72995 | 2026-09-19 00:41:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dd229a0c-6368-3e85-943c-3f1cd5b47f32 | -6.13437 | -59.95443 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 029b183a-dd38-3a5f-a2ba-c87c884265c9 | -6.76269 | -59.42231 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a3a23a87-1852-39f0-a843-51b4c9fe5ada | -7.58087 | -57.68927 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 6f22f436-fa91-326f-a073-06727f4abc31 | -5.91391 | -59.95275 | 2026-09-19 00:41:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7fa1989f-68af-3d74-bf98-f4279c6b2bad | -3.69114 | -60.61284 | 2026-09-19 00:41:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 82fcfcb7-54f1-3c0e-a0b1-05dd2727da22 | -4.0679 | -56.24609 | 2026-09-19 00:41:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 8c1d40c9-c706-32ed-ac18-46de2ee85ea3 | -3.48512 | -59.5911 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d3828d82-ce00-32f8-8fe1-7089a25f956f | -6.20077 | -57.7752 | 2026-09-19 00:41:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| e86db984-0fa7-34a7-af45-973cab76419a | -4.70835 | -55.6925 | 2026-09-19 00:41:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3f486d1c-08a2-3ce5-85cf-cb0956c5f23f | -6.00537 | -51.81647 | 2026-09-19 00:41:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| d3bd1b48-135e-32a8-be37-bd1b547cb74b | -6.0854 | -55.55606 | 2026-09-19 00:41:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6f80fc69-2603-3e48-87ba-6833d5a57eef | -3.34766 | -59.8659 | 2026-09-19 00:41:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b5ae6185-f72d-34d3-9324-3f29e2281069 | -6.75389 | -59.42355 | 2026-09-19 00:41:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fcbb1d46-1bd5-3b40-9661-da8bbfd36647 | -3.82124 | -50.75301 | 2026-09-19 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |


[Clique aqui para ver as próximas entradas](README22.md)
