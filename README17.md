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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b051cbc2-2518-30bd-a5ec-f89a349825ca | -9.97513 | -39.17768 | 2024-12-12 04:16:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 59368020-a900-3c81-b3cc-987a1516f690 | -8.36538 | -43.35901 | 2024-12-12 04:16:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a1b68843-0020-3d19-b422-039cf24a5978 | -11.20393 | -53.82635 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 009cb732-4d09-3058-aad9-d52dcd218aac | -6.92254 | -43.51779 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8e8aa580-c014-398a-99aa-2ae4c77e6cfe | -10.0193 | -47.5624 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2db5bf12-9a65-36a8-9d9d-a37eed01ba73 | -6.94183 | -43.52434 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3874ab8a-0ecc-3f17-8560-4052f6197d8d | -6.93306 | -43.53714 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b39a785-4e50-3a01-bb2c-094ce800b4c6 | -13.83737 | -40.98928 | 2024-12-12 04:16:00 | NOAA-21 | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7ce39ca7-e764-3aa8-af2a-0b3a242ab378 | -6.91647 | -43.5133 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ab4b84-fa0d-3b28-b9cb-768392e0c99c | -10.00909 | -47.5562 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a72197a8-6eef-32b4-b18c-d2c149713f1c | -10.29515 | -53.69919 | 2024-12-12 04:16:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b73efa2e-0fae-3f69-9d64-b583df043e76 | -5.92275 | -48.05705 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 03c8c893-a9e4-3443-b6a0-25f347ade1bb | -6.92638 | -43.51485 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| e9a5a008-6985-3be3-a119-52f564ba6569 | -5.92757 | -48.05267 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 47c29657-1dbb-3c82-9898-c0c4418c5cfd | -11.87487 | -43.72167 | 2024-12-12 04:16:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea6b6e7a-74a3-319a-8968-37c1bcb5975a | -11.47987 | -48.2134 | 2024-12-12 04:16:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64fb1204-1b60-3f5d-9cd8-125c33bc436e | -11.19857 | -53.82547 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c4d2af9f-ab0a-3970-9608-bdb723370dc1 | -6.92969 | -43.51537 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| f61b617f-ad38-3c54-82a3-dad0d0a19daa | -6.96967 | -42.99723 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f9faeb2a-8c77-3531-9563-504ae8f56b1d | -6.93191 | -43.5228 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 55d205f3-ac8a-33e5-b828-707dfe515a4b | -12.65537 | -46.58002 | 2024-12-12 04:16:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 555f7487-d28c-3799-8231-38d4972a0345 | -8.36999 | -44.48186 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6cb31561-9c5e-3837-9989-00baa64842c5 | -8.86278 | -35.72649 | 2024-12-12 04:16:00 | NOAA-21 | MARAIAL | PERNAMBUCO | Brasil | 2609204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ee6fc1ef-87fc-35b1-b9d8-eb5f6b2e1bab | -7.00462 | -40.95117 | 2024-12-12 04:16:00 | NOAA-21 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| fbf802b6-55a9-31cd-9c83-e08983da7e59 | -12.90593 | -48.59462 | 2024-12-12 04:16:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a09962d-cc21-30d3-9e08-aadba8c7818a | -11.20819 | -53.82066 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c0ce168-f548-3b73-88a4-16642d6adc7e | -12.92552 | -48.63608 | 2024-12-12 04:16:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b4eeaac-1d4b-320f-932e-f0ac1f4e44ad | -7.57208 | -49.40392 | 2024-12-12 04:16:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7448e98-2a9c-325b-9ae5-c016f1a4eb53 | -14.08143 | -41.76709 | 2024-12-12 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fa4f487a-67cc-3a20-b35b-8ab46fb82203 | -13.26141 | -43.66988 | 2024-12-12 04:16:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f82fc011-cc23-3bdd-a764-a3f6f27c8fb1 | -5.93153 | -48.05335 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 599a4fcc-c8ee-3147-99ae-ee6d9c446c1f | -8.36943 | -44.48537 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c5de630-d8df-3498-be37-267970e7e2b9 | -6.91316 | -43.51279 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef13712f-e278-3d19-b82d-512c9a8639b6 | -6.73945 | -42.52895 | 2024-12-12 04:16:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6a66ef29-0b57-3700-940d-509e74c6594f | -11.74514 | -43.77044 | 2024-12-12 04:16:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6263160-fc92-37f0-a959-365480b16ca2 | -11.19748 | -53.81887 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f551b84-705e-3f27-b795-046848f2df50 | -6.93859 | -43.54508 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab73dfbf-4276-3ca9-a7be-0c15d7b7536d | -11.19959 | -53.83662 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 370a9ecd-37af-3ccc-974e-3686606f7390 | -8.56254 | -40.79636 | 2024-12-12 04:16:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 32466f59-adb9-30eb-83ee-f9d7d5b0545d | -10.53628 | -44.68002 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85b8039d-2703-3b2f-9ffe-43b9f16592d3 | -6.97576 | -43.00174 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c619ef63-abda-31de-9424-b754f395a0d8 | -6.92476 | -43.52522 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| c2ab8011-470f-3458-956f-3f35257a6131 | -7.80511 | -46.20573 | 2024-12-12 04:16:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c08675aa-f025-3540-a99e-58a914c7d05b | -6.97245 | -43.00121 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6f75c6d2-0113-348a-809a-f6cf70b01e61 | -6.92861 | -43.52228 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 47.6 |
| bc1b7195-4a34-3918-9416-f38ea3118b16 | -5.92455 | -48.05516 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f0a06f77-f3fd-33c1-975f-5535c2e8ca35 | -11.11141 | -54.6517 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d591e8dc-2e3f-347d-98a6-f72139ede09f | -10.55501 | -44.58255 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f98c600-bd18-331c-9fa5-936cda3663f7 | -6.93522 | -43.52331 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| baeb4958-5e65-3dae-9782-1eadc0ddd080 | -11.20625 | -53.83077 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34d3b546-fd10-3adc-a8c6-26ea3d71f4ce | -8.15196 | -43.79112 | 2024-12-12 04:16:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| a1474bd9-00d9-3efb-be3c-1d0e98a1bbce | -6.8613 | -41.06224 | 2024-12-12 04:16:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 732abbb4-d508-3565-8d04-a12c8f169621 | -6.94297 | -43.53868 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cf3fab0-9637-3884-9815-45d87d7c9335 | -10.59458 | -44.97815 | 2024-12-12 04:16:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61657cde-f483-3773-a53b-a8437785c07c | -7.47507 | -44.7398 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61512102-c104-3cd5-84bb-77f3bc1df864 | -11.68315 | -48.07707 | 2024-12-12 04:16:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49183c09-5bb2-36f0-8903-bb0edde08cb2 | -10.49512 | -44.63763 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0079ec7-abed-3ebf-b3c5-66c427da5f61 | -9.7933 | -36.23085 | 2024-12-12 04:16:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c771e2b0-5df5-3bf7-b246-4ff7a4548990 | -11.11065 | -54.65568 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 030eda12-4653-34c0-adf7-d735a2bab8e6 | -11.2116 | -53.83171 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 814fca10-1540-3547-b1d9-2a72204467ba | -7.43318 | -44.74423 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 267e458a-a3b3-3995-a938-65a05a0b17dc | -11.42477 | -55.91925 | 2024-12-12 04:16:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ceb93096-c114-313d-80e4-b21323f9e89b | -6.93798 | -43.52728 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60fb6eb4-5f30-31a7-82d2-71d4829b85e0 | -12.41625 | -43.80347 | 2024-12-12 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e662fcc3-cdf0-3a2f-bb2b-7b3ce4414076 | -9.34217 | -47.83677 | 2024-12-12 04:16:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd6e4a4b-d3e7-3c93-8e05-aeaefbb75cf3 | -11.47911 | -48.21786 | 2024-12-12 04:16:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a42cfbf-59a2-3cf4-b0f8-b62b05b19e90 | -6.92975 | -43.53662 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 817c1e6d-64ca-3896-a4b5-90bedfec2e47 | -6.93468 | -43.52677 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 7ac3201e-b493-3c8f-ade4-620f9c401059 | -10.0098 | -47.55188 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4c9cbd9-b522-328d-9c9c-7515dff3b7c7 | -10.08764 | -47.37978 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3945e85a-1a88-391e-b0e9-030ffbbd3c5e | -6.96359 | -42.99273 | 2024-12-12 04:16:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a753fd79-41ec-3971-8433-9e100bfae165 | -11.20518 | -53.81961 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb5b0adb-e9a0-3cf5-8827-041b13583ca9 | -12.90367 | -48.59557 | 2024-12-12 04:16:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77792282-3276-3531-9dd3-f17196a2552c | -9.58138 | -42.12807 | 2024-12-12 04:16:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f609f06f-0a22-3f83-9cc3-44055ec687cd | -6.93022 | -43.51191 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d552841b-ebf1-320d-bd73-6c9561807f61 | -11.43173 | -55.91584 | 2024-12-12 04:16:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 037a27fe-d7d5-31cb-b358-af00390357d9 | -11.20205 | -53.83652 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| de075bce-fd71-33f2-add4-f869509cbb6e | -10.02002 | -47.55806 | 2024-12-12 04:16:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d26c6296-6bd3-38f2-9e5f-78f0bda13bed | -12.90509 | -48.59943 | 2024-12-12 04:16:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 116f815c-6f45-3576-b932-60c0982f8680 | -12.69551 | -46.76455 | 2024-12-12 04:16:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09d7b710-daf9-38b7-b1f3-4ba19937199e | -11.19919 | -53.82209 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45b6a173-8b0c-339a-8948-246b4c115111 | -11.20456 | -53.82297 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 857bdfac-a16b-3b0c-bda2-d2a4888e0420 | -11.53676 | -51.28 | 2024-12-12 04:16:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 319c6298-64d7-31b8-a8b5-43fd21113ce9 | -12.48545 | -46.3487 | 2024-12-12 04:16:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fd2f419-b3ab-321a-9bee-439929569dc0 | -9.97913 | -39.17823 | 2024-12-12 04:16:00 | NOAA-21 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6354008d-61d6-3506-9681-cef81c010630 | -6.91923 | -43.51727 | 2024-12-12 04:16:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 1b48f969-a7af-3140-895d-e9d12146bf06 | -7.429 | -44.73273 | 2024-12-12 04:16:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8886ac41-7aff-3b80-b969-ae4be7563778 | -9.67028 | -36.35009 | 2024-12-12 04:16:00 | NOAA-21 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c9941b50-07b2-3388-b7c0-ad1d628f26ed | -7.79324 | -35.13325 | 2024-12-12 04:16:00 | NOAA-21 | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 7c2041ff-b168-3e28-8c94-a1d291b18459 | -8.73246 | -49.73484 | 2024-12-12 04:16:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3a37d44-612e-3dc5-8638-91217680b498 | -12.4168 | -43.7999 | 2024-12-12 04:16:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| daff16a6-705c-31eb-9f6e-7e307052bef0 | -10.53573 | -44.68353 | 2024-12-12 04:16:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 493b92d3-b4e1-3ccc-970d-0c97555aa63f | -5.93237 | -48.04832 | 2024-12-12 04:16:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70564358-a216-3e25-979d-20d0aa33f92a | -9.79472 | -36.22 | 2024-12-12 04:16:00 | NOAA-21 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 93e6079b-aa3c-3c9f-b708-7921245f43f6 | -12.40411 | -49.68075 | 2024-12-12 04:16:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bffd594-f7c6-3243-94ec-0327d062f372 | -11.79772 | -47.8872 | 2024-12-12 04:16:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85c10eac-cbea-3ad7-9af5-5da09dba8b7c | -11.19795 | -53.82883 | 2024-12-12 04:16:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6396cd22-8c61-3d05-a166-790822a15e9b | -9.19506 | -49.4742 | 2024-12-12 04:16:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 289d7d01-6e34-3bc6-84a6-6cb4cf50bae4 | -14.12066 | -41.67797 | 2024-12-12 04:16:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f3a1b0cd-643b-33ab-9242-a9a3dff5eb0f | -11.74847 | -43.77096 | 2024-12-12 04:16:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README18.md)
