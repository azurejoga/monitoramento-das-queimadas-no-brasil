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

## Dados Diários - Página 218

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28f9f4d1-448d-38b0-ae30-6bde316d1cbe | -6.58073 | -53.01738 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 338014e6-2484-3164-85d5-7945585072d0 | -5.98846 | -55.36491 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 668a8ea4-1bce-30b2-b6a7-266854914465 | -6.15864 | -51.70807 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6eadc6f8-3000-36c9-ab68-149062ce55bb | -6.13977 | -52.86955 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 560d6392-17cf-3c77-a1c7-902c973a480e | -12.22888 | -57.09669 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2d06d0c3-a868-362d-b1b7-f5ca5030f32e | -13.51254 | -48.6019 | 2026-10-09 05:25:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 968647d9-2459-3ee0-b437-c76dd156e54b | -4.80091 | -56.14164 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51437073-2ea0-3057-9b63-cc0978510e7e | -6.24792 | -52.86623 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c0962727-629f-30a1-bb54-55e50c33c411 | -5.71599 | -53.49794 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7b453206-bf77-39f3-9bdd-4e72dffc5ec6 | -4.7466 | -55.6685 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55d82cc7-8897-3c77-a4bb-dae0f4730204 | -5.96209 | -55.33812 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6884e53-d9b7-3261-a613-a5c607a21e2a | -5.70762 | -53.45758 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4f7e3d0-a0b7-363a-bc6b-a370d9ddfa4c | -4.91668 | -55.85583 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a6b12de-b217-39da-a7fe-e27b39bda5ef | -12.20888 | -57.08035 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 254497a3-7b48-31eb-ae00-db73258e1850 | -4.74363 | -55.66386 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f1980ad-a1bf-32a7-99c6-36a3745b280d | -5.29366 | -60.09428 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ade02c3-6f77-359f-ae41-906062e4926e | -4.92381 | -55.85702 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6de1ccba-e94d-31ef-883a-1876165b1100 | -6.50623 | -55.31775 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2447e2d6-605b-3765-bede-39d63111b54c | -5.99152 | -55.36986 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2b92a31b-1290-3726-8244-e38c26d96e82 | -7.18227 | -52.6156 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 917f434a-221a-3ac9-83fe-12d6b33260db | -6.17595 | -52.86598 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec9b5137-48df-3679-9d8b-2882696abaf5 | -12.17606 | -57.09885 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2b1ff1a-c230-300a-bd31-1e07ae5458ed | -12.22648 | -57.08747 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| b543021b-018d-3f15-ab03-41c6798535b3 | -5.70019 | -49.0882 | 2026-10-09 05:25:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19c65039-fafd-3eed-a7ff-dfb02172a905 | -6.51189 | -55.38297 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38432616-0bde-3d31-b8c8-d94b35542fd7 | -5.8628 | -53.46612 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57caa4b8-7e3b-31ba-9cb9-3b03ad9134f2 | -12.22035 | -57.10421 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b15065f7-d7ee-35ff-b95c-e78b70d39d9f | -5.95838 | -55.33747 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a043c5e-8009-3672-b50a-2ee0c5e57854 | -12.22888 | -57.0967 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 78dfddd2-5376-3ba9-b932-abd547b60c0c | -7.61501 | -46.5335 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fabf2df3-948d-39ec-b98e-bd102fe2dc64 | -12.19704 | -57.13292 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6c5aaa2a-28ba-3c64-baac-70c44448e912 | -4.75142 | -55.66106 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2670322d-6a1e-3277-b8ab-f7921dd9daf1 | -12.19768 | -57.12862 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01c0e55d-c0be-3030-b079-4801bf6c5fd9 | -6.45625 | -55.05449 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20136c31-8858-3e91-81e6-a4045898d77d | -5.70055 | -53.47604 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9b3ed19f-d252-34a7-b6cb-4b31288696c0 | -5.69219 | -53.47513 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 558b966b-3caa-3fdc-aaa6-6aa83f03dc94 | -8.21737 | -46.4283 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca997933-5fd8-3821-9ab3-7180d552699f | -5.70531 | -53.47276 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2af84f1e-a1dd-38b4-9eda-fbef5ea686ff | -7.61203 | -46.53723 | 2026-10-09 05:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d30944c5-a38c-35bb-955a-6aeb76769172 | -6.24477 | -52.85704 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 347eb8e3-b6e1-32f5-ae56-6b0e57d8f6d0 | -5.70413 | -53.48043 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 52fe21f7-3337-3b41-b7f3-71d6e2e0c07d | -7.18293 | -52.61102 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4801e98-7386-3b5c-87dd-3051b1072ced | -4.96057 | -55.12332 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 069d4ac3-11cc-3699-82ce-ea6bef3e8dd8 | -5.71301 | -53.48923 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 59fdecb1-8228-3aae-8068-5a7f222c6d7d | -12.21795 | -57.09501 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dd1c1ba1-2936-3909-929a-d8e36581ea66 | -4.96429 | -55.12386 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46f5f380-0537-3183-abe4-d8d41178201d | -5.88974 | -55.5252 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bfd3543-87f7-3795-b3f0-76d68b313615 | -5.70445 | -53.46036 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 191ada02-ee01-339f-be27-de7b05181afc | -6.87947 | -45.91379 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 26dbb6d3-e661-3cc4-b4ba-08c7a4be2638 | -6.30522 | -59.97303 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ff94fd1-e324-3a94-b59e-b6921a299fd1 | -4.66276 | -56.21686 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1339b5c7-32a9-394b-a73a-51419a78f942 | -6.1069 | -55.79077 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc831d73-0860-3937-bbf5-4588d018923d | -6.49749 | -55.3186 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0bb9fc0-eb4a-3cf4-b20f-3e8ed0038d4b | -8.27808 | -45.74665 | 2026-10-09 05:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80ae729c-6d44-3abb-90bb-642e3242ea36 | -5.70704 | -53.4614 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22392a8f-0066-39d9-8d49-22e9c81f8185 | -6.35996 | -55.15551 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20bf53e6-0ab2-3069-82d5-aae3897bb720 | -3.84899 | -61.19461 | 2026-10-09 05:25:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| db608d64-5c13-370a-a45f-e931c686b7d8 | -7.17774 | -52.61507 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c4ccc43-bd42-3e02-8539-347e0c773ec5 | -6.87947 | -45.9138 | 2026-10-09 05:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8fc3e198-1e02-3aee-b710-3da498b9cc16 | -11.98046 | -57.61345 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c175ca8a-173d-3512-9c85-c4a2fe07b270 | -5.96116 | -55.36994 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 339729f2-cd3c-3799-8929-28eb16d91c2d | -6.5028 | -55.38355 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd9e370-431c-3cdc-8c9b-dfd8b28e87fa | -10.38563 | -68.90188 | 2026-10-09 05:25:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da735bd4-8d99-37c9-a6f9-b0d8158ac2e1 | -11.97631 | -57.61695 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d2575e7-d503-39ee-bc39-135c258a0cdc | -6.35687 | -55.15037 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9b2bbbe-6849-33f9-903a-c0a7e0b46630 | -6.21848 | -60.02396 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6a8126d-fcbf-303d-b47f-cfbb3b3d5f64 | -12.21724 | -57.12573 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c540f4bd-853c-3f78-b7f3-6a39cd6addd7 | -12.24346 | -57.09883 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f849e562-a9e2-340f-a911-e8fd35e1475d | -12.21982 | -57.08201 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| fb2c7a98-f688-3a1c-997a-b5931586ba42 | -13.18883 | -54.37004 | 2026-10-09 05:25:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6ce1f00f-336d-38e6-a47f-4d3017ca1481 | -11.99586 | -57.60741 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a519ffa5-581b-3167-b2e0-24541a56afe6 | -5.15824 | -60.32547 | 2026-10-09 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21ba201f-6670-3ccc-8cfd-2f64761f2861 | -13.50618 | -48.60064 | 2026-10-09 05:25:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb6b1d81-f35c-30f4-afe2-a8cc42a12350 | -14.88037 | -50.29968 | 2026-10-09 05:25:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| deee7c11-42ec-3280-b196-2a62ffeb93d0 | -5.6934 | -53.49511 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4db037-6b7d-3ebd-a172-208940729734 | -4.66565 | -56.22136 | 2026-10-09 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55537aaf-86ef-3af6-b41e-2e3c167ae12d | -4.80383 | -56.14605 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 78408a6d-a622-3ee7-bc1b-6966cb8393c9 | -12.23492 | -57.10641 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1a486779-e8a6-334b-b41f-27aa83295c42 | -12.22045 | -57.07766 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 498a73c8-2ea7-343e-af1e-e1e39146a531 | -5.75272 | -57.57386 | 2026-10-09 05:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33eac0f1-bc47-38b7-89b1-ca59a84e2f88 | -10.36855 | -61.22287 | 2026-10-09 05:25:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c97823ca-b2ba-3bcd-958c-c9c549ca839d | -6.51536 | -55.4109 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac57da9-7110-332b-952e-0da5e2136a4b | -14.88086 | -50.29545 | 2026-10-09 05:25:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14d50fc8-13aa-38e6-8bc3-3956f92f5d97 | -14.73114 | -48.22129 | 2026-10-09 05:25:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b82a5da5-21bb-3768-8198-c405bc668fce | -6.50749 | -55.38687 | 2026-10-09 05:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3480eea9-3dbb-339f-a589-8655387549b1 | -5.96821 | -55.34802 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7ea63939-31d3-32b9-86f9-3e4b229ecf23 | -12.21857 | -57.09069 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6189f2b2-a20b-31a4-93aa-3c658c22c3cb | -12.24044 | -57.09398 | 2026-10-09 05:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7f4e7821-98ae-3ec1-a97b-12b1fb9210ca | -6.03709 | -53.48829 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fea02399-dbe5-3bd1-b63e-060b5123778f | -6.50623 | -55.31774 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cb1e566e-38c3-34c5-b8c9-e43e0341ada0 | -10.67333 | -58.73703 | 2026-10-09 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83cee09e-e6c6-3314-a99e-158387299b49 | -5.95339 | -55.35652 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eca0e6fb-e619-377e-9fed-9c62dfdb2d15 | -11.97277 | -57.61642 | 2026-10-09 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b3f27e8-2f4f-3c06-b865-1b644d912441 | -5.93174 | -51.83623 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0db55d77-c32c-307b-8aad-a0eba52817f8 | -6.85856 | -52.83805 | 2026-10-09 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f7f9904-b872-3d16-8323-94894030deb9 | -6.50249 | -55.31719 | 2026-10-09 05:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d9d353b-60fd-35e4-b2e8-9b492a2ccbe9 | -11.75011 | -61.06942 | 2026-10-09 05:25:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4639ce88-8e60-3315-8985-f33b2a508a9b | -6.30813 | -54.80551 | 2026-10-09 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25b7e358-95f5-33c1-b33b-d669ae920ee2 | -4.30919 | -60.87694 | 2026-10-09 05:25:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76c135eb-dce2-38ef-a34f-2a47440cc1bf | -4.12493 | -59.8797 | 2026-10-09 05:25:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README219.md)
