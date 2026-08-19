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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89b24a79-030a-3e8a-bc46-097406494ed1 | -8.93353 | -47.60211 | 2026-08-19 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bf3152d-4ed3-3294-bdab-8dac700f4f6e | -6.88325 | -59.03794 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2be6664-a877-3e2f-a39b-7eb55bc00c3e | -6.09107 | -57.92011 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 682cab92-b53d-3f66-b82e-de278a718891 | -6.7034 | -58.94526 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63f1f66e-801e-31be-99b1-8465b1a36fdd | -6.89204 | -56.4361 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a17e1ef-48af-353b-9f4e-d88c2e4e2b05 | -6.08059 | -57.9141 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c4e5f4b-e667-30ae-9920-326586520702 | -6.99222 | -48.04844 | 2026-08-19 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fac2c114-6f62-3835-8c8d-1e8a1c3faf08 | -3.93357 | -50.99501 | 2026-08-19 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d7413987-878d-31ab-a9fa-9a817e1968a8 | -6.88173 | -59.06294 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d25db120-200a-3d7f-ac2d-26c746200f24 | -8.35703 | -45.97701 | 2026-08-19 04:38:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eba54a4a-3d79-3d5a-b115-2f787c9bbcfe | -6.53478 | -43.12109 | 2026-08-19 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bbbffbe0-f3dd-346a-b011-df3f06c521da | -5.91168 | -43.62183 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1a7de50a-b503-351a-b1d5-11854d379fb8 | -6.85369 | -59.03192 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d975d39c-e416-396e-bdb8-328179540ab0 | -7.21801 | -43.28555 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 73f81d33-9a94-3c48-8389-752a2a2cad1d | -7.10909 | -59.77196 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2a677cd5-d165-314a-a75b-b5cd0e922000 | -6.34078 | -54.91913 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fa5a7a8-00ce-33f1-82a7-0b9e26050db8 | -5.9271 | -43.62411 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0761f432-e401-3312-98db-cb41280eee9b | -7.81456 | -44.60216 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccedaebf-6f13-3dd4-99eb-fa25788b0226 | -4.45805 | -55.45364 | 2026-08-19 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91c20cff-1509-3507-b3c8-8d2f9bf0e3ba | -6.69619 | -58.93696 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55e63ff5-bddb-3335-bbd3-5767bdd01cf3 | -6.75787 | -59.15043 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af2ed6f6-301c-34cb-b32a-b8e87a19fdea | -6.68341 | -59.07178 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88a4a642-5061-3b21-b897-e54eb6a56728 | -6.87458 | -56.41808 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3db48c7-e231-3236-b53a-93a294e5eb7c | -3.30238 | -48.79769 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90c2c9ac-6148-3fec-8a33-4f8f4baa84f6 | -3.27095 | -49.52372 | 2026-08-19 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c76c1cba-31ae-322b-86a4-3a2a73506f23 | -6.29248 | -43.64219 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1465cbb7-8a05-30bf-89d3-698bed05e2f1 | -6.88584 | -59.04096 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85ff8c0b-ae8d-3db5-bdec-cb68f9dd0334 | -6.69162 | -58.94278 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b44ab98d-4224-3421-a983-c41a091a7396 | -6.88253 | -56.43148 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27b720fd-9721-37c0-9f33-584d0169455e | -8.55558 | -47.40886 | 2026-08-19 04:38:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec080b85-6b56-3f2c-b7a6-91657e9d4d6f | -1.80931 | -47.19956 | 2026-08-19 04:38:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 13ff7de9-493c-3b7d-8bb6-4807a98d0606 | -7.44607 | -45.14312 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 880799c6-1e4c-3eeb-abc9-fcd327cec574 | -4.70827 | -47.15207 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e44c6eeb-37bc-33e2-8c08-8b8c83b65d90 | -6.99553 | -48.04897 | 2026-08-19 04:38:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd579e3d-c3f6-3ac1-8ae8-442421630083 | -8.0998 | -51.6638 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c01ef4a9-c982-33f9-9324-019af9850a0d | -4.00692 | -48.06229 | 2026-08-19 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a0cfaed-bd1b-3c5f-b136-960ecd9720a4 | -5.999 | -57.86529 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a9d563be-d3b3-3a94-9646-dc59fbb20349 | -6.29174 | -43.64704 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65f98a0c-f2b3-30d5-a32b-7ee41e7b0945 | -6.44057 | -52.73853 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f6a32a2-9613-3797-afe7-bad653e89ee7 | -6.02059 | -50.19889 | 2026-08-19 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9e4f9b4-acdd-3410-97ac-d212b0a40275 | -6.84857 | -59.02638 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e96eab6-9551-3b54-88be-72e26ecfbe3d | -5.92325 | -43.62355 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f5bc6d3-1c93-3733-a8f1-d8c057033869 | -9.0277 | -45.86548 | 2026-08-19 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2729c69f-abe1-3350-827a-95468c26b694 | -7.04555 | -59.8466 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c6eaa7d-63cc-3ec9-9b34-2d1079f9a981 | -6.57054 | -51.20637 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a8db82d-440d-3e52-aad2-2253e99fcba4 | -8.1084 | -51.65685 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dbcecfde-a7a4-36ac-9b2d-3d0da9b7f300 | -7.30603 | -44.53574 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e8b639f-2116-3377-bee6-2e8e8201c521 | -6.44391 | -52.71847 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd3c223c-fcf9-3d0e-9241-14a3660595f7 | -6.9949 | -59.04782 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d08bf364-aa58-3d4a-862e-1ff1d106523c | -6.76691 | -59.15569 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f499c41-7fd7-3a5a-9543-bd8d750b163e | -5.4294 | -48.4126 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 53f8ad88-06b9-3648-9945-ccdccabf0182 | -6.4414 | -52.73351 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 693b392c-3689-37cc-a4cc-46e838e6fc89 | -6.83914 | -59.01092 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba0e7964-32bb-3972-84f3-6bf7b8093d2d | -5.42829 | -48.41954 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55be1121-51c5-3bf9-a8f5-3d98c0fc3f2e | -7.01545 | -45.9 | 2026-08-19 04:38:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 915621e5-e599-3ea7-9c8d-24cdf22c197b | -6.0072 | -57.8514 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bba6d4a2-4004-3a2e-a046-ffd02f347caa | -6.01344 | -57.84862 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| daf6b514-cca6-3f6c-bed9-3c0c1329fa26 | -6.74657 | -59.16556 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94c0cec4-9c84-3684-9a72-32d297f5ab38 | -4.47983 | -43.90641 | 2026-08-19 04:38:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32d8b5d7-c56f-375f-b175-ca8917ec1a8e | -7.56631 | -55.56376 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd65b378-7a5d-3240-85a8-377996a799bb | -6.87608 | -56.4096 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8536dd03-17c0-3151-a11f-825312554425 | -6.66856 | -56.1584 | 2026-08-19 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a75f5c05-2091-3671-81f5-a27bf0ed1396 | -6.01962 | -57.84618 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17cb06d3-ae5f-39fd-a10d-899c9660afc0 | -3.14616 | -48.1542 | 2026-08-19 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf2f3b6d-0d7f-3ae2-8904-9b9053a2da7e | -6.83695 | -44.94437 | 2026-08-19 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68022690-5076-3557-b73a-1a4e9c185513 | -5.9218 | -43.63317 | 2026-08-19 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f42cbb50-6f38-3f25-adbf-7745b3f4ff46 | -6.138 | -57.8826 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 719cb26c-39bb-3ac0-8c9c-c80b4842090d | -5.43326 | -48.40965 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 720b9a21-1adc-3093-849d-00384ee918ff | -6.84073 | -59.00223 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d04b3e3-e77c-3e5a-b5d0-05c856ebf494 | -7.53867 | -55.58406 | 2026-08-19 04:38:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 058929fa-b04e-360d-bbd6-038626f4a74f | -5.42553 | -48.41555 | 2026-08-19 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 206212a4-9a05-3375-8c4e-e6e227adf122 | -6.33776 | -44.08185 | 2026-08-19 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4da56b0a-d532-34da-9824-0320688354e1 | -7.7539 | -48.27926 | 2026-08-19 04:38:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7f91ef3-654e-33f7-89a0-fc4ae603bee1 | -4.46295 | -55.45436 | 2026-08-19 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8ff54f30-8cdc-341e-9cb3-1077fa1b3875 | -7.45393 | -45.13995 | 2026-08-19 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f83a051-8bcf-3d59-8ea8-a0c560bd7ae4 | -6.28861 | -43.64161 | 2026-08-19 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f305a911-3d2e-3052-bf1e-bcc8e643c0ee | -6.01575 | -57.80278 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 819e2e2c-1570-3e16-98f2-8996645dbe40 | -3.45767 | -56.80606 | 2026-08-19 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e96a64cd-06f3-3b59-8b53-9f1c41ed7b3e | -6.03168 | -57.81008 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| def48d58-7dfd-342c-b715-c50ef7a31940 | -6.89913 | -43.24924 | 2026-08-19 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 991ace47-d0d4-3026-9731-19fc2998e283 | -6.16361 | -45.35033 | 2026-08-19 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea68fbe-7f81-3d1f-9fd7-caf646a3c727 | -6.88836 | -59.04358 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a451ba25-ff93-381b-8506-8222ab0ae33e | -6.88007 | -59.05557 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0231aa3-b3d8-3eb6-912d-6f4ec8f76f57 | -7.61625 | -46.54631 | 2026-08-19 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60940ce6-1a62-3f3f-8917-9693f9e1cd48 | -2.76735 | -48.57103 | 2026-08-19 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8696047c-d21a-3405-ad6b-ab310c359de7 | -8.36036 | -46.35223 | 2026-08-19 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28162026-8eb1-38f3-b50b-468446201790 | -6.7028 | -58.93429 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c88023ea-8855-3911-bdf7-f70bd9f8a280 | -8.18003 | -44.43092 | 2026-08-19 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 485e5cc3-bbcd-3390-9be4-1f8e9662c444 | -4.71049 | -47.15951 | 2026-08-19 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e02e2f07-952c-381d-837b-51984b686e32 | -6.00031 | -57.85786 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 875091a9-ac75-3c77-b167-792d55f87664 | -8.04589 | -50.10285 | 2026-08-19 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfe32db0-07ce-3542-b77d-287673b3bbf4 | -6.41732 | -54.93975 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04954644-be93-3dd0-82a3-c0d8ba587f79 | -6.84511 | -59.01176 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e6b93414-31e5-3d35-a61b-245792d5439c | -5.35352 | -45.18465 | 2026-08-19 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51f2828c-50b9-3c42-a3e2-95ff6e97d466 | -6.33856 | -54.90446 | 2026-08-19 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7121a924-7468-3be3-9a13-9d521e8a2f34 | -8.10342 | -51.66441 | 2026-08-19 04:38:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 351f8bd8-8744-358f-9c60-b4f8e2d70bc6 | -6.88166 | -59.04676 | 2026-08-19 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d01d1e67-5bb8-31e7-855c-13c60101f786 | -7.19071 | -43.45558 | 2026-08-19 04:38:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 414bb084-8ff8-3db9-b51a-21b4dc8cc845 | -6.0875 | -57.90769 | 2026-08-19 04:38:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 70c4108e-6e7b-33db-8755-5efe0e87d3c9 | -3.42709 | -51.51361 | 2026-08-19 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README35.md)
