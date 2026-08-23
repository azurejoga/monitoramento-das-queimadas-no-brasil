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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0df6be7-aa50-37b6-87b6-367381496c98 | -2.49957 | -48.13482 | 2026-08-23 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b67cc1e7-25a3-32cc-b22f-28b51baf84be | -7.15104 | -42.79279 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 97c84280-3939-3771-986a-7d396314355d | -5.53172 | -46.61073 | 2026-08-23 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46267c7b-1d7a-3a84-9f29-b1e1f4aa3491 | -7.48827 | -45.14973 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d7b7cd4-23fc-36b7-b3ad-ca127615ee9f | -7.51967 | -47.63849 | 2026-08-23 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f100095-077c-395f-b18d-9406ae878205 | -6.18881 | -55.43416 | 2026-08-23 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85dc8be5-d154-3c44-a84d-4d1b714086d3 | -6.78406 | -42.68038 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 10db5372-6372-39a4-966a-60a4a032ff22 | -7.18824 | -42.76978 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 629af23e-80ec-3216-af58-0f66bcac29ef | -8.23769 | -38.85472 | 2026-08-23 04:08:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 375fbd12-02c0-38b8-ae6a-3893257577db | -10.4564 | -37.14184 | 2026-08-23 04:08:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2490bad-5105-3d9c-9dc3-bfc2409be70e | -3.65608 | -49.44463 | 2026-08-23 04:08:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d3f8faa-38da-396a-bd58-5aa0c1e3c52e | -7.30584 | -42.99558 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0d729cd-926e-3c56-a2d2-0746c0c4334c | -7.26746 | -49.90922 | 2026-08-23 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3fcfc736-43f8-3939-a86e-6289e6a94613 | -8.37991 | -46.47596 | 2026-08-23 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b635d44-6c97-3389-94c3-1f68d361339e | -7.28462 | -42.99953 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8592e92c-af07-3db5-b5d2-280adb5b8c82 | -6.18636 | -53.529 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7b714796-6701-3f2c-b9e4-3e57333e2b3b | -5.33798 | -41.56004 | 2026-08-23 04:08:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 96def4ed-ddc8-3669-b86f-e702d58c1102 | -2.96073 | -49.26922 | 2026-08-23 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72c5cb82-dbeb-3aff-9a49-18530b5764d6 | -6.38078 | -54.96777 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24cb3084-a4df-3ef3-8635-9603c0d888e7 | -9.02371 | -50.73375 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e227534a-14df-3ce5-97fb-911fc8479ad9 | -5.29077 | -44.70387 | 2026-08-23 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69a45910-cf79-3eeb-b1f1-7d9be222e752 | -6.38055 | -54.96898 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c5c8e75-aaf2-38fe-9263-a4488376d890 | -8.1538 | -44.06233 | 2026-08-23 04:08:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 78492f75-43c1-3b30-818e-9bbb76da3964 | -7.47283 | -45.13048 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bebf2c4d-cf0b-3446-b0b7-89cf8fd7f23c | -9.64104 | -48.31841 | 2026-08-23 04:08:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a395f53c-92a2-3118-8370-2d86d86ed66b | -7.7273 | -46.14526 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4001dc9-7d64-3dab-b903-4eea2b5e6b1d | -6.43753 | -39.21497 | 2026-08-23 04:08:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dddc8667-ac5e-3c71-ab95-014f6aaf033e | -4.31454 | -46.41682 | 2026-08-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3f288ab-24e8-3abb-b040-39d500a9b397 | -6.86562 | -45.98353 | 2026-08-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c51879bb-7e25-3bfc-b3d2-abf83ec70971 | -7.69613 | -44.81348 | 2026-08-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20e42a74-4b9f-32b7-b1fb-d4b19f1f3270 | -3.01196 | -51.05195 | 2026-08-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9134fda6-392c-30b8-98d4-cab092f74f32 | -6.17148 | -55.5691 | 2026-08-23 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b58a3132-c495-3b35-a2b9-c7603332c108 | -7.69678 | -44.80944 | 2026-08-23 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26d0256b-6b32-3e71-850e-7e0184009f5d | -6.37509 | -54.96001 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e5b46f9-a0ab-36f0-8012-750040d75181 | -6.09701 | -44.89218 | 2026-08-23 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e0ff423-f4d9-3962-8279-8f4a63c3abbc | -7.9882 | -45.23876 | 2026-08-23 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ac6ee5d-1530-3f2f-9ebd-1f181570d5b5 | -5.61893 | -45.69287 | 2026-08-23 04:08:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 175b8b70-a8e3-354e-bcef-dbe99fbd9a77 | -7.18494 | -42.74759 | 2026-08-23 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b894d568-fc72-399b-98f5-8261c155e895 | -7.76856 | -46.1567 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 495906e1-2a12-39da-a27d-01f7986100ff | -9.02201 | -50.74309 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 214e9844-e8f2-310d-8cb9-5ec54b54814a | -8.92978 | -48.54585 | 2026-08-23 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d07fc881-1b78-3565-ba99-fea4dcf409e9 | -2.56709 | -47.24926 | 2026-08-23 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f7e754aa-29c3-3da6-bb84-52ad528ef081 | -7.08164 | -45.01968 | 2026-08-23 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea383467-d018-30e0-bc6d-0248a98f7d60 | -7.30197 | -42.97675 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b24dc70f-3dac-3504-a2b8-e3b2ffbb5cca | -5.17033 | -45.05876 | 2026-08-23 04:08:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dc7edc64-2a7f-3803-be2f-56df540c0c6b | -7.03375 | -48.02144 | 2026-08-23 04:08:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f55d5f62-407f-3d6f-917a-4cdcfbf5c621 | -9.45553 | -40.3274 | 2026-08-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 96630e1c-e1b3-3840-9df4-09badb6134c0 | -9.74696 | -43.30357 | 2026-08-23 04:08:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6741dd26-46e0-305d-823d-f91df20478c6 | -7.72886 | -46.13602 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a01ee6-2d9c-3a8e-9029-acb6d51e9630 | -6.78739 | -42.6809 | 2026-08-23 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7fa0b0ba-cf84-34c0-b234-f9a4168d30ee | -7.76777 | -46.16148 | 2026-08-23 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69b6b0d5-613a-3b26-90e7-59a941d40d83 | -3.37983 | -39.20353 | 2026-08-23 04:08:00 | NOAA-21 | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc81a8ef-fe51-3041-8237-5f62b6f55574 | -6.89565 | -55.7039 | 2026-08-23 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| acbee5bb-e71d-349a-a019-c0e5cf238b79 | -6.47011 | -42.47193 | 2026-08-23 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 33d48726-06ff-31cc-8d45-daf3902bf046 | -6.55633 | -55.09684 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9010ec2e-a380-30a2-ad48-a787412dc819 | -6.19997 | -53.52608 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7764fa7-a4e8-32c0-96c6-59eefa449a45 | -6.94447 | -41.74673 | 2026-08-23 04:08:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2303543-dd27-3ce0-b4ea-a5b7c44b5e6a | -7.29858 | -42.99808 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cd81bb99-e06b-3655-bb9c-8595b3fb9acf | -7.30475 | -42.98082 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bb3ccf7-5849-3fd1-807a-f3af5eb47f00 | -7.30641 | -42.99202 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 876527d5-7654-3839-83fb-69bea0d4e3c3 | -5.67651 | -47.49211 | 2026-08-23 04:08:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8db2dd9b-67bd-3a83-9568-903aea03afe6 | -2.91218 | -48.86962 | 2026-08-23 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| ef39f4ed-f00e-31df-b559-aef8eba293e3 | -7.30249 | -42.99505 | 2026-08-23 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 90dc59b0-e0f8-3df0-99ac-aa61d8f7955d | -5.96291 | -53.62379 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 95bc5a58-2c37-3270-aa74-6405b6e428b2 | -6.52257 | -51.44589 | 2026-08-23 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a4f489c-fb0f-38ce-8daf-aa712ddaa65f | -10.46 | -37.1462 | 2026-08-23 04:08:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 838a0820-8388-3e8f-ba22-9b7d31f8975e | -6.19739 | -53.51735 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5fe8cfda-557d-3a45-9302-f75dc32b6e63 | -6.20277 | -53.52365 | 2026-08-23 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e63f346-59f2-3343-ab5d-5a0bca63597d | -4.30983 | -46.41989 | 2026-08-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3db980de-d126-39e8-8cf0-ced6adce2ed8 | -4.16986 | -42.43815 | 2026-08-23 04:08:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 65d464b8-65d2-3823-9f5c-88ebed6bc486 | -9.01765 | -50.76711 | 2026-08-23 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c1aff1e-670e-3423-adc7-72e47b1f76ba | -2.49878 | -48.13984 | 2026-08-23 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34044624-9a30-3ca3-a3bc-376fd6e09782 | -10.4559 | -37.14552 | 2026-08-23 04:08:00 | NOAA-21 | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b948910d-8db3-3655-8d58-0ec69445cd60 | -9.45266 | -40.32312 | 2026-08-23 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.8 |
| ad8f4321-7bd6-3720-aec2-6f025e43e9d0 | -6.658 | -58.75 | 2026-08-23 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c59cbc60-3d30-3fbe-a9d8-a711c5d7480c | -6.8062 | -58.6469 | 2026-08-23 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fa21de2d-0862-370e-97d0-9b70e8d3f941 | -13.1505 | -51.4281 | 2026-08-23 04:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f457450e-ae0f-3292-9ec8-e690fcc22183 | -6.6949 | -58.7485 | 2026-08-23 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| eeaa0325-5350-3978-bc93-6eedfd432a36 | -6.6766 | -58.7299 | 2026-08-23 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 4d88787f-079d-3948-9a7d-5fc79bdbe68d | -6.9513 | -59.0859 | 2026-08-23 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d94923f6-3407-37b6-a295-827c5917e78b | -6.6765 | -58.7492 | 2026-08-23 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 1cbe4255-06f5-3a17-af37-38c01a958c1e | -6.782 | -59.6519 | 2026-08-23 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e90e74ee-1022-327a-bc48-0bf9fd2d5b9e | -6.9699 | -59.0658 | 2026-08-23 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 0ba9d185-2266-32d4-af0a-623cf7b43c45 | -6.9514 | -59.0666 | 2026-08-23 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e1eccd66-c720-3f6f-bcdc-a7b1381b62f5 | -6.8188 | -59.6696 | 2026-08-23 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 8c7cb6d9-76df-335d-a5fd-7e8de5e5068b | -6.1285 | -57.8393 | 2026-08-23 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 53b27ffb-616c-3ece-9e8e-39e5ac8e6e2e | -13.1697 | -51.4258 | 2026-08-23 04:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| c9f66ef6-a0b4-3b04-a810-c275f93ddd0b | -6.695 | -58.7291 | 2026-08-23 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 05f735df-6f2d-3706-ae93-c603b98abde2 | -10.68744 | -47.72248 | 2026-08-23 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa5d8a78-c728-3e13-87dc-a2d67456c55d | -8.52496 | -54.81718 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45514c87-1621-3cc8-b18f-d7aea2cdd6f9 | -8.53703 | -54.82535 | 2026-08-23 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8029be1a-12dd-3903-ba1d-2c394d0bdbd0 | -12.36956 | -46.4562 | 2026-08-23 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f29507a2-32d2-34b5-aa6a-32b1d27d61ce | -10.85269 | -44.74702 | 2026-08-23 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d6ea47f-6ddd-3293-a025-8f811d01720b | -12.7402 | -46.46316 | 2026-08-23 04:10:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fc2fc4f3-8578-30b5-999d-9fac8b6741cc | -14.31443 | -51.84249 | 2026-08-23 04:10:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ef68edb-c9e0-3aa7-9076-76d7b2ecaf7f | -11.44262 | -44.53126 | 2026-08-23 04:10:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cf334860-073a-3fef-8111-6ecb55849b14 | -13.53712 | -48.18908 | 2026-08-23 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d7b7900-20a4-30ae-8e95-36e4d62ee8ee | -15.25268 | -52.84098 | 2026-08-23 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ccb82fd-cd70-3641-bc7e-4105c6d7018f | -10.32817 | -45.40423 | 2026-08-23 04:10:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 58859c99-23d0-37de-aabc-ae9a6ee0928e | -13.19952 | -51.44598 | 2026-08-23 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
