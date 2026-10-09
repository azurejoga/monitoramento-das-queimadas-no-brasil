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

## Dados Diários - Página 224

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d37fe03-56b9-3b7c-bce5-d08073ef9c66 | -4.3098 | -60.87314 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23f56ec9-ad82-38b5-9d7a-49cda4f0fdf0 | -4.74239 | -55.67197 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3a6cefa-3dc5-3626-aa9d-8d502c54c890 | -4.11486 | -59.87809 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08e07ca8-fded-324c-9acd-013eacef6893 | -4.29974 | -60.01712 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 813fe0a9-148b-3912-86f5-ed9c5f969d92 | -5.29087 | -60.09019 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2e3b208-6f19-3aaa-8558-e9cbc259a243 | -6.07091 | -53.60539 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4895294c-70b5-307a-89a0-018105de9ea2 | -5.9349 | -51.8301 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0dcfa91a-b067-3f0b-9f04-96d97407b6f6 | -6.49582 | -55.30447 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42f21c15-42af-3c10-bc32-3887c9bff61d | -4.0736 | -59.83512 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c600b58a-7bb9-3ecf-9af6-4ef39c821705 | -4.96057 | -55.12333 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 369869b6-5a0b-38a1-80d9-a117a38efe5d | -5.88485 | -57.75518 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b33e0590-7bdd-3366-ae69-eea9c2358ae0 | -12.21431 | -57.09444 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ae69ed2a-488b-30c8-a89c-66baf8977633 | -6.88132 | -45.90021 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 25ae4db5-073f-377f-b9e5-c69c4ae10a95 | -6.01056 | -53.48492 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9327b67-745d-3540-a85b-200d6307c08e | -4.12772 | -59.88379 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e0ef7e1-adcf-3892-8778-127dec2915bd | -11.75182 | -61.0588 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c96649e5-0fb1-31cf-a004-4716e7624d0c | -6.50124 | -55.31912 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 59f96b44-811c-3602-9272-8eb5dda17961 | -12.21005 | -57.09818 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cdd69687-682f-37c0-aabb-d1aa15e693ea | -6.24347 | -52.67729 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a781fbb2-e5ea-3944-8e87-0f7bd55ba387 | -8.21962 | -46.41054 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 934b7e89-411f-3b05-9b66-876e753ccf9c | -7.08664 | -52.69127 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1be3d4a0-591f-327c-b8b4-8907ba6c8a3e | -6.07442 | -59.88557 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7f02c8e-b9ec-3e44-968d-f5153ba8a3ea | -12.2295 | -57.09236 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 209ffc4e-0b12-3160-8d33-88cfeff84b4e | -6.41553 | -55.19948 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5102379-c8fd-3985-b7df-d039a2778b5c | -6.11052 | -55.79138 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6903c5f2-1688-3cfc-91e0-30629e3b87e1 | -12.22035 | -57.1042 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2eee68a9-5448-3269-bc9a-43fa8b0e50c5 | -4.93486 | -55.80828 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9f3d9c5-2744-3892-a0f4-9ea4d2b996b4 | -6.49277 | -55.2994 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9914f30d-a1f8-3166-8e37-e065ac909bc1 | -4.07638 | -59.8392 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeed22ad-3718-3cd5-b1bf-581b65785005 | -5.70335 | -53.46799 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dde6a73e-d417-3d2c-ac49-02f95db45dea | -12.21555 | -57.08581 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| ed3cde53-4cc9-3e13-83d9-f730c9c4f16e | -11.96222 | -57.58979 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 692b564f-b6c4-3ca9-8940-d8acbc959e91 | -5.2374 | -60.18747 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e8ca17b-631f-3b7b-86e7-3b241714f130 | -11.76752 | -58.28422 | 2026-10-09 05:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91156590-eb19-3fc8-90c6-db285b5b89dd | -7.08347 | -52.68167 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8f0abab-d27c-3be5-9fde-4f9d36a6d614 | -5.88541 | -57.75162 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d5788b1-1df1-35a5-93f3-91d64c8e54f7 | -5.70862 | -53.46094 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5f4e7818-3240-3e5b-aa13-3cb3ace6ded4 | -21.9738 | -55.9324 | 2026-10-09 05:27:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7271e836-7555-33b9-9d5b-c1ddd6693d50 | -21.97327 | -55.93704 | 2026-10-09 05:27:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29327a09-6a9c-39d1-b68f-b12efbe3e073 | -21.96882 | -55.93642 | 2026-10-09 05:27:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e100a7de-6050-337d-86b1-4915c8e9ec7a | 4.87551 | -60.31456 | 2026-10-09 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c6a2111-7ae6-3a57-b8cf-0a60e63f24b7 | 4.87648 | -60.32014 | 2026-10-09 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7be2324e-6ec8-3216-a44d-c49a4a35e660 | 4.22427 | -60.83665 | 2026-10-09 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce63249d-d790-3b79-9f15-039a45576413 | 4.87599 | -60.31734 | 2026-10-09 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34892e71-4fe8-3c1f-aa41-054916ec0434 | 4.22993 | -60.83891 | 2026-10-09 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4dd40365-a674-3162-bbf4-9c0a6257cb54 | 4.22941 | -60.83584 | 2026-10-09 06:03:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0683c27-95b9-3210-9748-dd3de4812d7e | 4.87551 | -60.31455 | 2026-10-09 06:03:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dc839ef-1edf-380e-ab06-23e752055059 | -2.86112 | -59.11114 | 2026-10-09 06:05:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa5b4c38-7b0e-35c2-8f79-1ec2aa45c5f7 | 0.4488 | -60.54265 | 2026-10-09 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25471e80-e6fb-39d2-b3eb-1b9d4b2adc58 | 1.21943 | -59.98071 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9390c01c-5cb2-3a15-8676-d25b4069cff1 | 2.76657 | -60.00087 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3620ba4-2c27-30ff-9d55-2736f581d031 | -2.39209 | -57.89561 | 2026-10-09 06:05:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1af4de7-7e89-3fb1-b66a-ca2c2667a072 | 1.21875 | -59.97639 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4ae20ed-c5d2-389f-abae-c5b72e0cd252 | 2.76863 | -60.0098 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67080fa3-46fc-304f-b93d-db4c98a580aa | -2.68839 | -59.78526 | 2026-10-09 06:05:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9eea2dd5-1f38-3a52-835c-f216914da4a1 | -2.55482 | -58.03907 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb028b26-ea89-3821-b183-6025fb07c4c4 | 1.31927 | -60.71505 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2c750ee-912b-3968-91f1-268ec8a230e0 | 0.44765 | -60.53527 | 2026-10-09 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fab73458-3c23-3f25-94f7-5afaa98ee94a | 0.44152 | -60.53254 | 2026-10-09 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d669e3f8-3cd5-365c-aa21-dd3e9195c7a3 | -2.54803 | -58.03806 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 398020a2-ae07-3cc5-93ee-8a2220e51656 | 1.31871 | -60.71156 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cc51955-cfab-3d96-8126-7f8b1bf9111e | -2.54769 | -57.99356 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 34002e18-a90d-3659-8ba5-c74e81c21285 | -2.81495 | -58.29115 | 2026-10-09 06:05:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d6562feb-f687-31ce-8ef6-4461b071be4e | -2.85945 | -59.11078 | 2026-10-09 06:05:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bde30d9-c883-37c1-94a6-cda93e19a145 | -2.50102 | -58.07455 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d33a8dcb-e27a-34dc-af55-f9ebe01dbdce | 2.76802 | -60.00605 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04910c66-1635-3171-b106-1ac079083c75 | -2.85867 | -59.11596 | 2026-10-09 06:05:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ae9f58b-a713-3072-8725-df8ed2273da6 | 0.44822 | -60.53895 | 2026-10-09 06:05:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 393fde1a-548b-3a9e-9b1c-ef62b39b413d | -2.86037 | -59.11636 | 2026-10-09 06:05:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9c8024b-5dbb-30d5-aad3-41f67ac2875b | -2.55574 | -58.03297 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 36119d3e-b722-3760-aa57-a0f80c727c87 | -2.54877 | -57.99512 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce3b32db-0c23-3a12-bf9b-c9c85129905a | 2.76719 | -60.00458 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9096f744-e612-314f-870d-e7dbc60bddea | 2.76782 | -60.00832 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b158601-0537-3802-980e-c60d02e7809a | 2.76743 | -60.00231 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e64a512-c0e5-3507-b791-219f63d7e2c7 | 1.21308 | -59.97749 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af2f5819-704f-3266-8e2d-db7eb97a8512 | -2.81585 | -58.28499 | 2026-10-09 06:05:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 7784ee75-68f9-33ee-8025-02cd32dacbfc | -2.50012 | -58.08069 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0523237f-f21b-37be-827e-31fcab233ab3 | -2.50012 | -58.08068 | 2026-10-09 06:05:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 462e687a-6cb8-3fc5-8bc3-f2b368aad8c7 | -2.85945 | -59.11077 | 2026-10-09 06:05:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c418b48a-cf21-3aca-b643-47e9a7858930 | 1.31927 | -60.71504 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d05835fa-b05a-3ad9-99a8-b166c7a236f3 | 1.21943 | -59.9807 | 2026-10-09 06:05:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 39d0efa6-a619-3444-9e58-1897f7d5b751 | 2.76657 | -60.00086 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67c179eb-8607-3703-881b-c96e24fca389 | -2.81495 | -58.29114 | 2026-10-09 06:05:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 061a1077-d1e1-3d28-b0ad-b1484bca997e | -2.39209 | -57.8956 | 2026-10-09 06:05:00 | NOAA-21 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5442f6c9-cef0-3a45-b876-5298fd10de5a | -2.86037 | -59.11635 | 2026-10-09 06:05:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fe6621f0-91e1-3b92-b82a-858752aea532 | 2.76802 | -60.00604 | 2026-10-09 06:05:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78e5dc99-cc7a-324f-9bff-db7408eb2f9c | -3.86168 | -64.94952 | 2026-10-09 06:08:00 | NOAA-21 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f34187b-2df3-3bcc-8e0e-dd5d4b3afaed | -3.90006 | -58.95565 | 2026-10-09 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7347ddd2-c074-38b6-a200-a79c0ff57f41 | -3.67115 | -60.60589 | 2026-10-09 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf3184db-8577-349f-a206-8631f4da7bf9 | -3.18816 | -58.64304 | 2026-10-09 06:08:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a329c865-aff0-3b70-bb0a-24737d452ad7 | -3.76934 | -58.84479 | 2026-10-09 06:08:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09709b1e-01a4-3f26-8862-20984f0126c8 | -9.11304 | -67.82422 | 2026-10-09 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3402d010-f3fb-3d2b-8bfb-234d8128b1e3 | -8.5503 | -67.02579 | 2026-10-09 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6bb2aa9-b22b-3028-ab63-19977562c161 | -3.59713 | -61.61534 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90973b56-ffc6-3a36-956c-ec592e28aae2 | -6.93269 | -59.26237 | 2026-10-09 06:08:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 388c9563-4ae5-3b86-b25a-731ec42385cc | -3.3892 | -61.07684 | 2026-10-09 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a1f7db1-dd2a-3966-922c-ce38820711cb | -8.75247 | -62.62336 | 2026-10-09 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0534599-d494-3602-ba76-6a6cb7f9c6fd | -3.4674 | -60.2569 | 2026-10-09 06:08:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66cceca8-96b2-365f-b091-5976eff8d478 | -3.60547 | -61.63522 | 2026-10-09 06:08:00 | NOAA-21 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7b96122-6f45-3999-acd3-64c14e12a2a9 | -3.74234 | -59.37199 | 2026-10-09 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README225.md)
