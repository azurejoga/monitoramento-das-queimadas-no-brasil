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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96f48aa4-a580-3c07-bec1-143e33a61ac9 | -11.7107 | -50.7891 | 2026-09-23 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 077df1e3-998f-3f01-ad96-6f9e955d651b | -12.4216 | -46.9551 | 2026-09-23 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 66a90397-f246-380b-8102-702e8bcd8740 | -6.7211 | -44.1618 | 2026-09-23 01:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 24850031-73cb-37e9-a4d3-5d076d568d6f | -11.1204 | -48.327 | 2026-09-23 01:10:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 36481d2d-1dd4-3bca-9461-22deec24428f | -5.7752 | -45.128 | 2026-09-23 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| fd7171b8-c7e7-3cc7-b091-9510b54d63d9 | -11.5307 | -45.3553 | 2026-09-23 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| e57dae2f-62b8-3f04-868f-9d0d2d58f5dd | -4.3358 | -55.6461 | 2026-09-23 01:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1c3eb97a-a4c5-3edd-8549-d134a11741df | -6.6815 | -55.0703 | 2026-09-23 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2a0e4441-a6e7-3eee-aeb3-54e96d036971 | -8.8105 | -44.2757 | 2026-09-23 01:10:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 321.9 |
| eb0f9481-2d56-3c2b-b662-e3f423873548 | -6.6776 | -58.5554 | 2026-09-23 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| f4de5ef9-82c5-3290-a2cc-24eec10a1752 | -3.6947 | -60.5645 | 2026-09-23 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 06b368f0-b784-306c-a44c-53c0be2875f5 | -12.3867 | -50.1731 | 2026-09-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 80098b9e-2fd5-391f-9278-a3e31a8b95da | -6.0925 | -57.6847 | 2026-09-23 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 4abc969d-289f-3d20-ab67-c5924e7b5e83 | -3.6764 | -60.5649 | 2026-09-23 01:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d3b6a29a-3c7b-3ed2-a15f-09e7be5dca37 | -12.387 | -50.1515 | 2026-09-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 153.4 |
| bb775e76-55e3-3772-9899-18e6882f3858 | -12.1672 | -50.8004 | 2026-09-23 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| c7993a16-ed3e-379f-a592-7a8ac1bdd854 | -12.3679 | -50.1539 | 2026-09-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 93767588-4f2b-3ff3-a73b-737b801b9459 | -12.1481 | -50.8026 | 2026-09-23 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| b28054a9-dbc0-3b3c-a602-1b5586c90d92 | -8.4985 | -57.6075 | 2026-09-23 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 13746a86-98cd-3d31-90bd-3ac0448b4394 | -6.6775 | -58.5748 | 2026-09-23 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 0c5e1a40-aabf-3bc3-8fb5-b8f92407a879 | -3.6947 | -60.5645 | 2026-09-23 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 66fee6bc-df90-32a2-afc4-18ea652ffc45 | -5.7565 | -45.1293 | 2026-09-23 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 70a54eba-e7d5-3026-b5ce-d952785b7c0c | -6.6315 | -43.7533 | 2026-09-23 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 6674f01e-4d32-3ef2-b1c4-3dd095e3494b | -5.7752 | -45.128 | 2026-09-23 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 71ef48d2-4979-325c-a78c-53a4343e4456 | -8.8108 | -44.2525 | 2026-09-23 01:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 899ab1ff-7bb9-31de-a237-e770fccb5e75 | -11.6891 | -50.9619 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| d16ef257-a27f-3232-9d7d-45f7946cc5cc | -3.6763 | -60.5839 | 2026-09-23 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 44845bc3-5ffc-3061-9a4e-7e5642c9f488 | -11.7104 | -50.8105 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 30c2284b-66e4-3cf6-bd54-ff8ee249fe19 | -12.1287 | -50.8263 | 2026-09-23 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| cb6303ba-68af-32b8-b952-58fe9de6b6e2 | -6.7211 | -44.1618 | 2026-09-23 01:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 3c8c9feb-5aa1-30db-aa0d-6d410742d571 | -12.1478 | -50.824 | 2026-09-23 01:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.3 |
| f68a1217-afd2-3979-9d08-15a71800d5a0 | -6.1109 | -57.684 | 2026-09-23 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 63de6fd5-2b2c-39a8-91e5-f0f687c0dde7 | -11.7297 | -50.7869 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 865305b7-5e13-3b75-9fc3-4261edf7954c | -3.2314 | -46.9376 | 2026-09-23 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| 2af61e04-3ea5-3ed3-a8bc-20a9b3c793a0 | -12.3867 | -50.1731 | 2026-09-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| a268c055-de1e-3d31-98ba-f9454ccae9f2 | -8.4538 | -48.6944 | 2026-09-23 01:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 89.3 |
| aa97e53e-2028-3071-8ff3-85c6ce3a967d | -12.4216 | -46.9551 | 2026-09-23 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 6e382367-43eb-3f22-998e-ca4fbb92fbe1 | -4.3358 | -55.6461 | 2026-09-23 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 7ab76314-ceca-30cf-b5b1-680586fb35d6 | -8.8105 | -44.2757 | 2026-09-23 01:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| f2db4df1-dd05-38b1-93da-b05e8d633da1 | -6.5939 | -43.7565 | 2026-09-23 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 4178282c-e448-3b79-bb79-b4f9be04800a | -6.0925 | -57.6847 | 2026-09-23 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 9717b621-209d-36fb-a586-452592c5e8b1 | -6.2949 | -57.7545 | 2026-09-23 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 11afe9c4-2bdf-37a5-855c-2805dda1f278 | -6.6816 | -55.0502 | 2026-09-23 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 9065fde5-5c95-38e4-9b1a-8c83c3021619 | -11.6704 | -50.9428 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| dfb88185-9e68-3583-9779-3c43a7674734 | -12.4212 | -46.9777 | 2026-09-23 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 930f5d76-5d9e-38d3-b1dc-c3723f245880 | -3.2128 | -46.9602 | 2026-09-23 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 611471e5-f867-3d6b-8b2d-aa33838b18ee | -6.6815 | -55.0703 | 2026-09-23 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 339e4a33-7739-3a5e-83a4-6fea98444c17 | -8.2062 | -54.7207 | 2026-09-23 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9ff6043d-b493-389f-8709-99d67945b53f | -9.1025 | -61.4299 | 2026-09-23 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 028e55f5-49c3-30f6-9cad-74971a0bd9bf | -12.1192 | -45.6368 | 2026-09-23 01:20:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 36823ca1-bcb3-38f3-980e-fec2a7f291e1 | -6.6127 | -43.7549 | 2026-09-23 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 338.1 |
| abc91841-ce5d-36d0-a494-ce8c7f270ca7 | -6.6317 | -43.73 | 2026-09-23 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7788751d-1ae0-3e03-bda2-90e0af277ff4 | -12.387 | -50.1515 | 2026-09-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| c113df61-6379-3f80-b392-fd8012508a59 | -11.73 | -50.7656 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| fdf47dc6-0b88-3d86-8f40-e2961e963df0 | -3.2313 | -46.9596 | 2026-09-23 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| b5776508-f391-3cdd-891e-26fab18c70e3 | -6.6129 | -43.7317 | 2026-09-23 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 277.0 |
| 901c13b2-9e42-38f2-a39b-2f0e9ba75746 | -8.4726 | -48.6927 | 2026-09-23 01:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f6961a76-e2f5-3fa6-9e9f-02386eb06789 | -3.2129 | -46.9383 | 2026-09-23 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| c6325d90-5df4-3798-88d6-79e7f41e64e5 | -3.6946 | -60.5835 | 2026-09-23 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 234e03b2-de35-3faf-991e-bee43b8b0e6e | -4.0925 | -62.0874 | 2026-09-23 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 15faeed6-2940-380e-b173-06778db6c394 | -5.7567 | -45.1067 | 2026-09-23 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| cc624462-63df-3dbd-851d-f4743d00d7a0 | -11.7107 | -50.7891 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 02f4538a-0934-33eb-ab4e-14ee71ca7ef9 | -6.3293 | -43.9411 | 2026-09-23 01:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4da7e1fc-27ce-32d4-aacc-e63d9e5270fc | -12.3676 | -50.1755 | 2026-09-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| e4321459-66e0-34b6-ab2e-c96fa9f8192f | -12.402 | -46.9804 | 2026-09-23 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2ab1db2b-285d-3a03-98f5-cb11678a50fd | -4.2951 | -49.1234 | 2026-09-23 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ac23b524-e212-3b27-8485-9c3f66280894 | -11.6895 | -50.9406 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| da3204ee-095c-323b-a5a0-be7313d3e572 | -5.6246 | -45.2518 | 2026-09-23 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 2256cd92-2bda-3558-8789-48c80f2362fb | -3.6764 | -60.5649 | 2026-09-23 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 82ee1968-39b1-39a1-9fdf-8578cb5f0f1f | -11.711 | -50.7677 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| af4177a4-052f-3333-a260-aa95d1b7ba66 | -6.6776 | -58.5554 | 2026-09-23 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 7599e5fc-2a1f-3f9e-859c-94c43a496473 | -11.7085 | -50.9385 | 2026-09-23 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 2c2cfafe-1209-3158-90b2-149690a8925b | -7.8811 | -61.1779 | 2026-09-23 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 48dd37f7-cae9-35b7-af43-da8574cb93a5 | 1.4085 | -50.7451 | 2026-09-23 01:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0101a61d-bdfc-3faa-8a75-fb1075f1730e | -5.7754 | -45.1053 | 2026-09-23 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d5230028-24de-3d30-aa5b-d4a2db60bfd9 | -6.5941 | -43.7333 | 2026-09-23 01:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| ada315fb-4a70-32a6-8f44-85586ee0c5fa | -6.3134 | -57.7537 | 2026-09-23 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 28db97a2-6c89-3c6c-a5d1-49f29bf488f7 | -4.3357 | -55.6659 | 2026-09-23 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 694205a8-f608-38f0-80b9-6bb0f3ff9422 | -8.9351 | -61.4759 | 2026-09-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 9f928003-c77b-33f3-830a-13c281c7a0bc | -3.2128 | -46.9602 | 2026-09-23 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 3f3030ea-eac7-36fa-8e2d-0454c1ef0556 | -6.6315 | -43.7533 | 2026-09-23 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 122.3 |
| e423b1b3-fe10-31ed-9958-00f61cbd40ec | -8.9165 | -61.4767 | 2026-09-23 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 1d5e092a-30fc-32bd-a2b4-3bc1a4da1bb2 | -12.1099 | -50.8071 | 2026-09-23 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 51381418-536e-3b44-afec-415b73baa43d | -3.2129 | -46.9383 | 2026-09-23 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 4e3c179d-b314-38a3-a5d5-f55c0cf5e1b7 | -12.402 | -46.9804 | 2026-09-23 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| a58fded8-b6c9-3be8-9140-eafe6b1f4387 | -9.8404 | -46.3911 | 2026-09-23 01:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 496c9196-02a2-3664-b953-ae3607ede83e | -5.6246 | -45.2518 | 2026-09-23 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 09951663-f9b2-3091-b843-9451f20db5bd | -6.6127 | -43.7549 | 2026-09-23 01:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 165.5 |
| c67f0ff9-ce13-35b5-abe1-d5c38850b959 | -11.5311 | -45.3323 | 2026-09-23 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ef16ddf1-5278-3f0d-908d-84e6a8b915c1 | -12.4216 | -46.9551 | 2026-09-23 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| ec17a386-2d8b-3ec0-863e-04a977572ae6 | -12.129 | -50.8049 | 2026-09-23 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.6 |
| f2191a64-ff54-3b1e-9886-6a3025449c1e | -6.6776 | -58.5554 | 2026-09-23 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| cbae587c-f48e-3556-a895-a061350c238b | -6.6146 | -59.9272 | 2026-09-23 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 232.3 |
| 9b391d6f-8c46-3b7e-bb4a-fb5664a3585f | -6.6148 | -59.908 | 2026-09-23 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 214e8d03-f488-3e01-9a0b-78fcfe753a12 | -6.6331 | -59.9265 | 2026-09-23 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 83e22595-8c22-32da-b4a2-79aeb7b56001 | -12.4212 | -46.9777 | 2026-09-23 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 8ac59881-7dec-3921-80d0-a203701f7864 | -3.6947 | -60.5645 | 2026-09-23 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 61c9d8cc-8437-3923-815a-43e1628e41cf | -6.633 | -59.9457 | 2026-09-23 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| fc7597b2-a099-3ae3-8c22-2f7a76b2ba32 | -8.4538 | -48.6944 | 2026-09-23 01:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 86.5 |
| ccd354f2-eeb7-3ba5-8758-b2c9cd34003f | -3.6946 | -60.5835 | 2026-09-23 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |


[Clique aqui para ver as próximas entradas](README33.md)
