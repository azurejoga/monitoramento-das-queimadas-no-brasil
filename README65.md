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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ed96c8d-fa60-3151-9cb4-5f8dc26f7737 | -6.76038 | -59.32287 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c70ea34-4299-3352-baf2-41e76a4d77a2 | -6.75816 | -59.0906 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 462b210d-ab2b-3028-855e-adba4bec6199 | -6.75637 | -59.32219 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f1aaff4-a01e-38e7-973a-1a3ed15cc667 | -6.75401 | -59.3364 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e189725-66d8-3ee4-acc8-311052ab21c9 | -6.75235 | -59.32152 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d683ac4-e0c2-31d2-8eaf-c7f428b250bb | -6.75176 | -59.32508 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43536642-4aa2-304b-8278-1ab446353a12 | -6.75117 | -59.32864 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de19ac4e-36c4-3480-b7ad-bb032c1829ae | -6.75058 | -59.33216 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c4c10cc-a4cc-3533-a4bd-9a53048ba832 | -6.74999 | -59.3357 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 543ca223-4fd6-3f96-88c5-ab0ab4d52fd4 | -6.74833 | -59.32086 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0b6246b5-e5f7-3bf3-967d-c84ef8c449db | -6.74774 | -59.32439 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b9614327-fe99-3bd7-a024-36f0569736c6 | -6.74715 | -59.32793 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6c2ed589-7f3c-384c-89f9-51f8844f2d93 | -6.74656 | -59.33146 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 57235cac-d56a-3114-8789-3920f93868b7 | -6.74598 | -59.335 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6629687d-2e33-3cc0-b540-8b58b1ae510d | -6.74372 | -59.32377 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 923aaa8b-0fa6-3afe-9e9b-8d7b55a846c8 | -6.74313 | -59.32731 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3582c699-c37f-30a3-9d4d-eefc9cf5aa52 | -6.74254 | -59.33085 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ebdaca31-d712-3960-a5e5-7af600cc5865 | -6.74195 | -59.33438 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 18c31c5d-5ee8-3c32-a65b-495a3446fa2d | -6.7398 | -59.29779 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea961409-bf81-3751-844a-23d252bfc266 | -6.73639 | -59.29355 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b022ce01-65ad-3319-bb30-00240c2a200c | -6.7358 | -59.29708 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f79fc04-0aba-3bcc-9ffd-992b9e8edcde | -6.67986 | -59.45654 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae7a6eed-94a8-3d86-b1d8-401f495ad33b | -6.67581 | -59.45588 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b59b39a9-a577-338c-85a7-ba8a33985725 | -6.67521 | -59.4594 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3d37ceb-0291-3dd4-97dc-294b9c831832 | -7.40194 | -59.71248 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9722e96-f25e-38c6-a1e6-3eac46bf1b37 | -7.40132 | -59.71611 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51a647e2-b7a1-3775-aeb5-e03dc376563f | -7.4007 | -59.71974 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a85a1ba-e1c8-3732-9817-0c3eaadaac25 | -7.39786 | -59.7118 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f878dd37-f6aa-3db0-89a5-8e8b1a6dc40f | -7.39724 | -59.71542 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 421ab1f2-4e21-3567-b3c8-513ae97ded77 | -7.39662 | -59.71904 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d774269b-9ace-32da-a830-a9630b068923 | -7.396 | -59.72267 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73b8732c-f69b-33e0-b4f3-a74823960888 | -7.39254 | -59.71836 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37ce1963-a542-3e8c-b592-a0da9c88afc0 | -7.39191 | -59.72201 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7a4fa09-1012-3cab-89bd-9ce72cd0a8d3 | -7.35014 | -59.74871 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0643d764-4143-317b-9675-4d1d37c7253a | -7.34953 | -59.7524 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84b5711a-db54-3d9a-a842-9af047b2669e | -7.18477 | -59.75946 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e0c16b5-ada1-35a6-9393-ee4e62a4b3fc | -7.18415 | -59.76311 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78e0bfa0-f61e-34f8-b33d-ecaf5b773500 | -7.11178 | -59.7734 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0b451fb4-c173-3255-a23f-acccffd0e9ff | -7.10829 | -59.769 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 258f8b2a-a89b-3f53-aaef-37a28989d1ab | -7.10417 | -59.76833 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65fde050-0c0e-39a0-bb5e-b08e42d3cd8b | -6.92474 | -59.78447 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71d2a0a6-ce39-34d5-b424-c53e95537f10 | -6.92411 | -59.78814 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c667642-d59b-3caa-baf6-d358aceb333c | -6.9223 | -59.78414 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4ad9a73d-490e-3c56-b48b-457a14e06aaf | -6.92169 | -59.78782 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cb8557dd-5b7b-350e-9061-c7ebfafe8bb6 | -6.8974 | -59.85733 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e7311b9-7948-3e36-b472-23ab2670a71a | -6.89444 | -59.79845 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42230b2a-f688-35c4-9758-49b4b09a10c0 | -6.89381 | -59.80219 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db5c7277-9084-30b4-bac4-a23cfec3480d | -6.88904 | -59.80527 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba2b9c11-dda7-3afe-bc65-ce5a5a153d55 | -6.82252 | -60.12416 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18bea407-4b46-3688-85d3-41cfcb891faa | -6.82186 | -60.12807 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d8e130d-c2d1-3367-9c8f-fe2639538be5 | -6.81338 | -60.12674 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c881f40d-ee65-3bb6-bdc6-d2fc34a34ed6 | -6.81271 | -60.13068 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 72a28770-8962-30ef-93fe-625c9941de9e | -6.80915 | -60.12605 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa82b004-12a6-3ba2-b5bb-272d796cab1d | -6.80848 | -60.12998 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5efd05bd-03d7-377b-b307-c4ab2b2b1e03 | -6.80334 | -60.10906 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 900acd60-9a85-3acb-bf2d-af3823e7de3c | -6.80267 | -60.11295 | 2024-10-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 264838bd-67fb-3ef2-8208-7223f8b97eeb | -6.73872 | -59.63115 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 254d4e76-be7d-30eb-ad25-aa0642676611 | -6.73785 | -59.63082 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62cbb602-d5eb-37c7-a4bb-4522e03d5f89 | -6.73498 | -59.67212 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc612776-6532-3458-86b9-822e56107643 | -6.73463 | -59.63041 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8880e9-4ef5-314f-8522-d6391ed2f101 | -6.73203 | -59.67187 | 2024-10-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12eb2ef9-ad0e-37fc-89e0-7c25f4a6b289 | -6.71262 | -59.75277 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41914f6-8a2a-3d32-9b66-0e2b187348eb | -6.69209 | -59.86274 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9edb2dfa-65b6-335c-84f2-b080e806e501 | -6.69146 | -59.86657 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a4f085e-57a9-36b9-badf-9e6db0e8a8cc | -2.9136 | -60.08536 | 2024-10-12 04:57:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3788a71b-fd93-36f5-9d88-5a444444a71f | -4.73068 | -60.77948 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d289012b-ac00-373a-a54d-03781ebe3083 | -4.72989 | -60.78418 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 05ea4c20-8690-36f8-84bc-5745573dd17e | -4.7261 | -60.77873 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1b5ef5e2-b52f-35c1-b84c-dca0ff4bf031 | -4.72599 | -60.5204 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df7d292b-652c-305f-a314-2ffd3d3769d5 | -4.7253 | -60.78344 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 99a3dad0-ad67-3c9a-8195-b64392b02a27 | -4.72451 | -60.78815 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 920f4629-5930-3fbe-a445-501bf0867eff | -4.72152 | -60.77798 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 656f1031-49e3-3e61-86a4-2494dc981fd4 | -4.72073 | -60.78268 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff9b2d48-2a8b-3607-bd20-42979ebf4d48 | -4.71993 | -60.78739 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f9b2965e-e7da-31a2-979d-a3751db82186 | -4.71913 | -60.79209 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c54dafb-8f9a-3ec5-ab0c-8e5a05784d71 | -4.71833 | -60.79681 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bb8dd25f-b158-3dee-bada-6806995690cc | -4.70893 | -60.82436 | 2024-10-12 04:57:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d18bde0-a24b-3d48-81be-8d9dca34e2d3 | -4.47291 | -61.07895 | 2024-10-12 04:57:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6495754-d145-348a-9105-4a06334bb8c9 | -4.00569 | -60.38414 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 292d097f-1529-392f-acd7-85c81969d0b1 | -4.00456 | -60.38003 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0df8134c-7b5a-3d3d-be2b-755456bb5938 | -4.00382 | -60.38457 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 546f98a2-aa77-3c95-8d9d-235980186c11 | -4.00309 | -60.3891 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 93b54075-f19a-3cca-8168-fd69674e13bf | -4.00195 | -60.37887 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4264c491-2bd4-344c-b715-18077beb1dea | -4.00118 | -60.3834 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d5f1873b-470f-3301-8fb6-8dd3f09187e8 | -4.00041 | -60.38792 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2d4a5a35-2c83-3ac4-a09d-6583503fc99b | -4.00005 | -60.37927 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c29101b-b23f-3a23-a027-b2e51987af3d | -3.99964 | -60.39246 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9d1a2936-29f6-3c3a-aac6-bd6ac8c7a4e1 | -3.99932 | -60.3838 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 69d588cc-dad8-37c1-8de9-dd2d4ec253e8 | -3.99858 | -60.38835 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4172bae3-d2eb-3211-8d48-cc0879fa1ded | -3.99784 | -60.3929 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 182bd501-6526-39e3-bd4b-29caef9848fc | -3.78885 | -60.11945 | 2024-10-12 04:57:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e91a6dfb-b318-3c5d-a77c-4897ffb94792 | -1.92866 | -61.73814 | 2024-10-12 04:57:00 | NOAA-21 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2602ca28-28ed-3491-aaf0-37b2bb751217 | -1.52099 | -61.58889 | 2024-10-12 04:57:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49a64dc2-ac2a-3435-86af-61b3f07fb1e9 | -1.5205 | -61.59196 | 2024-10-12 04:57:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a0070ac-1f7d-3639-8e08-283a0324bf53 | -1.5154 | -61.59111 | 2024-10-12 04:57:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 916d6ddf-10e7-3a64-b383-e9a6ce7a1830 | -1.5103 | -61.59028 | 2024-10-12 04:57:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 687d84bd-f624-34eb-bd6a-b779b2f28082 | -1.48939 | -61.5901 | 2024-10-12 04:57:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 542d5fc8-3e2e-3505-aeaa-0ad9778379b6 | -1.48891 | -61.59307 | 2024-10-12 04:57:00 | NOAA-21 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 011f8883-c791-3fdf-bfc0-ce193f104748 | -3.04787 | -61.68085 | 2024-10-12 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2eba360c-e8db-3167-8ed0-9f9ac3602f35 | -3.04739 | -61.68371 | 2024-10-12 04:57:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README66.md)
