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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e095a15a-4379-3297-951d-c9da0d9e3806 | -4.51792 | -55.76499 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f13f7b18-19ff-3afc-9eac-398ff0f3e8bb | -6.62323 | -59.93215 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3971358d-b042-3a45-85d5-718d62d0e049 | -4.38133 | -55.03039 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af5509c4-8a21-3c0f-92d8-6a8abe6f9162 | -6.61295 | -59.10329 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7276b059-75f8-3309-a958-3c3f48cba595 | -7.45325 | -61.37687 | 2026-09-22 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4032cdde-5f35-3cee-b3b9-2bd62a58b5df | -5.88597 | -51.5728 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fbe61166-f33b-34e3-978e-89782975ed4d | -4.08598 | -62.08927 | 2026-09-22 05:42:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9a00d59-bbbc-3af0-a303-9dfefd0d4244 | -3.06159 | -54.41362 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3e82f29-755a-37b8-bca9-28957ce1c6c1 | -4.20816 | -59.91046 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a6307e1-8084-30d8-ad78-cb8bd90696a0 | -4.41665 | -55.24382 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a179e76-a57d-3af5-9b75-cc13a71a9b43 | -3.07201 | -61.27079 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e91959b-524a-3c9d-965b-2987880d4254 | -6.86653 | -59.90718 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58f333f0-fc60-3889-94d1-3bfe687ed5f9 | -3.34138 | -59.85714 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f119cd1f-5751-34fd-844c-06765c577532 | -6.71235 | -59.45689 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3d150c9-8cca-350d-a859-0f5831e6451c | -4.41992 | -55.49968 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6e4f762c-d0a9-3bd7-958a-4eb2ff05062e | -3.38687 | -61.29511 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60dc2b1e-fe7d-3973-9a2d-095d7b9cbd69 | -3.30221 | -57.86508 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc2e899e-c746-3944-9dab-ef0d0a7c3308 | -5.80853 | -57.74448 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 738881f6-2811-3db6-bf3f-b28b930839fb | -3.41503 | -60.19933 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20d5f12a-f17c-388f-8649-18b2a0e36f0c | -5.45651 | -60.15439 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1976841-36da-3dde-86e7-8e11a3f8b9fd | -3.10653 | -61.40782 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c678ac96-20cb-32ff-8661-d568a75b8d98 | -7.39693 | -55.22797 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f8b82e-881e-3d23-b796-86dd93571283 | -5.87743 | -53.63588 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bea94f1e-a7b1-3e0e-9164-7593b8d5fe79 | -3.3924 | -59.52769 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05f7e03a-d3b1-3e09-b2dc-5f06b9328577 | -4.22302 | -63.07355 | 2026-09-22 05:42:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c87451-704e-3d00-9ff1-294606de2751 | -2.78974 | -59.89192 | 2026-09-22 05:42:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e76263cf-e5dd-3075-af7c-e56a2c86201b | -6.30281 | -57.73965 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7553de0-91c2-359a-837f-31db0d7186d7 | -6.76271 | -59.11102 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aea6a3b-807f-31bd-8f12-50e5ffcbeb5f | -3.45287 | -58.40486 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1416f228-7155-370d-aad0-4b9049e77f57 | -7.23737 | -55.59908 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0acc4b6e-282e-3ecc-8c96-f6ac5dbceb30 | -3.68586 | -60.59685 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b31b260e-16b0-3b8a-a2c0-3d9714a9108b | -6.31117 | -60.00477 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07275573-e9ff-30b6-94ec-3b8781714f81 | -8.61578 | -54.63162 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f905595e-bec8-35b9-9a54-465a556f24b2 | -3.06663 | -59.28194 | 2026-09-22 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09e1f877-a0a1-3ad0-837a-610b9c6bf701 | -3.16041 | -60.57695 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45ed65c0-3dc8-37d1-b5b9-37856a356ea1 | -8.62184 | -54.62868 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f32a08b1-edb0-3898-a75d-68d783ff6a42 | -3.14686 | -61.39534 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62152d04-df88-3f51-bc85-4b7198a77992 | -2.65784 | -57.78054 | 2026-09-22 05:42:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c15eec7-6aff-307b-84bc-bc0d33cd6340 | -3.29864 | -57.86077 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c72ae673-c73b-3a6b-8222-737a2521bd04 | -3.06232 | -61.28817 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c071687-653e-3917-88df-cd730f214c28 | -6.83128 | -55.53237 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eaaa8861-d539-3b53-9d74-c2d96affa198 | -3.72075 | -60.58083 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c272c26e-fc80-3247-b3cd-afd935b766d2 | -6.04067 | -53.27666 | 2026-09-22 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2bcff69b-3ac6-3777-a659-10f72c8b42ac | -5.37638 | -55.89943 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 301b2cd5-6ff1-31e0-bc34-c2f62ba961e3 | -3.68153 | -60.62451 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6036bd0-5f08-3c7e-8a8a-a6aa23f2b8da | -3.4285 | -61.32048 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b5b0bdd-9fb1-3019-9e11-efea751d2b94 | -8.59861 | -54.63288 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d5ec726-7194-34e4-b202-4b37a427d3c6 | -7.60466 | -55.35368 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f12e3f29-caba-3975-83ab-07a670d21903 | -2.9196 | -57.78625 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 761f3491-42b0-311a-8b7d-2d091b2003f7 | -3.58727 | -59.06813 | 2026-09-22 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a5f9efe-9716-30cf-9a77-c3ae6cd742b4 | -3.0875 | -61.17071 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7154afcf-ce32-3fe8-8947-5fe8187f13a2 | -3.30633 | -57.8657 | 2026-09-22 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d9153ec-77db-3743-bd18-e2e753109649 | -3.05216 | -54.40546 | 2026-09-22 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d78bfef7-9f7b-34cc-b883-4303ac249674 | -3.00253 | -60.79932 | 2026-09-22 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f422ee7c-8acf-336b-abf7-d2ce044804a3 | -3.68443 | -60.62901 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be66694a-ef4f-3104-8d22-68210b3c0e87 | -3.12689 | -61.43345 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc47b5df-5a40-3d39-bbd8-0255bd5aa696 | -7.72484 | -61.23373 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 401a9db7-0bbf-3363-8bb0-ece93c1dacd6 | -7.87137 | -54.73532 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1ee600e-c928-3910-99f1-ccdfe923c74e | -3.42281 | -61.31203 | 2026-09-22 05:42:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1390c0e-1eb8-3a32-98e2-69fdcbdf8ea8 | -3.2364 | -53.95697 | 2026-09-22 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| db771813-8f5d-33ec-991f-689444a1c02b | -6.78712 | -59.13936 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da3583d7-303c-35ee-b55a-9d08d3815d54 | -3.24341 | -60.8077 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ef43be2-15c4-3d76-87f9-fb2a3c0ce5c2 | -5.37978 | -55.91054 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5c03787-12e0-3107-a6a1-69799c34fd9c | -3.47559 | -59.5919 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f53c6f4f-9c24-3d10-815c-5dce10149769 | -3.69188 | -60.58155 | 2026-09-22 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9ec72378-e112-3d4f-bd98-66f0381fb687 | -4.94433 | -55.82379 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da03a8a3-499a-3533-a96f-e3c71dd84006 | -3.41862 | -60.19989 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ded92193-9d2d-3503-8773-9a03e2db6a23 | -4.34917 | -55.65493 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11c0b536-1f90-3703-9668-4685212dc416 | -2.93731 | -57.80776 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 351f06db-c192-3b1c-a9a1-8c01db8e217e | -4.95702 | -55.82761 | 2026-09-22 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8ccf1bc-ea38-31a5-ba80-8a19fec58305 | -7.29358 | -59.50774 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd092ffa-5cd8-36d3-bf49-d7928190d321 | -8.25799 | -55.30354 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6907de8-0532-30c5-b80a-35a1426faee7 | -3.19408 | -60.43252 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71ef5214-d379-33c7-9df5-d29ead5ec89e | -6.1412 | -59.95068 | 2026-09-22 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5635b6c2-4771-3cbd-8253-efe7c3496e55 | -6.74165 | -59.42065 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81847443-eb6e-38ae-9ff0-5ab2ca84e6bc | -3.1899 | -60.43528 | 2026-09-22 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30f124c9-b6f4-32a7-a37a-d3b3f1a5f647 | -6.72914 | -55.06541 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ef48ab0-492c-3219-933c-a5ba11b07ca9 | -6.35386 | -55.84386 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58d44442-35b0-38c3-bffa-28d7327d693e | -6.09301 | -57.69927 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 599fe68f-1e54-3185-a224-b487d16c6cfd | -5.81407 | -57.7367 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b571f44f-d189-3244-ba96-f53e334f6a41 | -2.95948 | -57.72021 | 2026-09-22 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2494a619-db80-3972-81e5-eb62c0e74a44 | -3.48641 | -59.57103 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 840be836-e320-36a7-9351-c7321c2aa16d | -3.48573 | -59.57544 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7134779b-ee34-36ca-9e53-ed53643707d8 | -6.25821 | -55.44146 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edbc33a6-2cf7-3fd5-ad25-be2b7bf9f8a6 | -4.27906 | -56.25907 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64afea26-d735-3eed-90f8-a5d3a07c49dd | -6.83597 | -55.53615 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1dd1cd0-2ce6-3dad-b38a-6f0e4fb8f2a8 | -7.33309 | -55.6054 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 427e68ce-51b1-3dcc-87b8-a7071dff6b31 | -6.05167 | -57.82771 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ac37760-2d41-3816-911b-e2d4b2d1dce1 | -4.68159 | -55.62494 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fd628e0c-b390-3e70-8516-4015582a36fb | -3.9236 | -60.55767 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e347384f-d01e-3990-8313-6c48ab6be608 | -6.86342 | -59.90187 | 2026-09-22 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5f8b992-2faf-3840-9c7f-ef1ae451a56a | -6.2578 | -55.44434 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 623ddb93-b144-38ce-8934-beee07aef3eb | -4.51626 | -54.98566 | 2026-09-22 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d76c4ef-ed08-3f5f-943f-25b3cafb4895 | -4.76946 | -62.8183 | 2026-09-22 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 010ec011-3ca6-3474-acc6-aba325e22602 | -6.72166 | -55.08059 | 2026-09-22 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c47b3d1-7146-30a5-8580-e043ac7b72d4 | -6.09946 | -57.62672 | 2026-09-22 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cf139265-96ab-397d-bf4b-3297ec2de7f5 | -4.68077 | -55.63032 | 2026-09-22 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0d407852-aa2e-3ac8-9ae6-4b75967b4fd3 | -3.3975 | -59.5194 | 2026-09-22 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 02dea047-91f0-3c38-94da-03ca92b1a3c7 | -6.63081 | -59.9333 | 2026-09-22 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 19.9 |
| ec15b261-eece-3f3c-888b-aab69ccdbf7c | -7.4022 | -55.22859 | 2026-09-22 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README114.md)
