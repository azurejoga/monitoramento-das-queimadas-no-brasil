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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0338439b-7e17-3128-a26a-0b6880ea2d57 | -6.25986 | -55.42163 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e967db6-5967-390b-8729-ee8429bccae6 | -6.70632 | -56.34478 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b1223c8-c6ed-3f41-8d6c-36cae72aa6d7 | -6.01511 | -57.66177 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b38094c-7827-3cbd-b1c9-0ec65187091a | -6.80405 | -59.59377 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3c69dea-f77b-3065-8a86-7a6d4a4e390e | -7.01491 | -59.25277 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a941bca6-5815-3ab1-918a-1d5326401b57 | -8.59871 | -54.73613 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae134f00-1943-3d12-a7c8-a61bda5059ea | -6.44198 | -54.96445 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd1fc5d-c67d-3442-a14f-3739335878d4 | -5.77127 | -57.55332 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e09d726-bb5f-31f3-a214-9a52eeaf1662 | -6.15295 | -57.93458 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 322dd967-26cf-38eb-a64f-1f66d9813232 | -6.33973 | -54.74474 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e189f5ec-c3be-3884-865c-eb3888132735 | -6.54235 | -55.08678 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3f7f622-870b-383a-b11f-1b8e05f2ff54 | -6.85414 | -59.41687 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33fcf727-3b96-3ef9-9149-808f42a8a0ee | -6.83663 | -52.5016 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c70c4df-8503-381a-a854-63ba3f9db3de | -6.35825 | -54.76777 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85c1fd35-032e-3004-80a6-0bb98fba2803 | -7.00149 | -59.2612 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 689e1153-4d9a-3336-818a-4868aa342a25 | -6.35918 | -54.76118 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d168b351-024c-33f5-9880-c0133cde8dcd | -7.34867 | -55.66183 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56f260dc-8554-3046-b961-a4781b6a67ea | -5.78681 | -57.56845 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0032c995-44d7-3d2f-8e74-af700cac0640 | -9.67637 | -55.09388 | 2026-08-25 05:48:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0268a9d-3c35-3028-a658-d420688358d6 | -6.13381 | -57.85772 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7f547a9-0bd5-3937-966c-cce9102b427e | -5.79446 | -57.61038 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08720b5b-85a0-3eda-9405-d3e8ad80a1e9 | -6.84053 | -52.50823 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 862854c8-c7e1-3649-9e4f-bbff6999d2a3 | -6.8072 | -59.59921 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91dcf6b7-2d13-3f2a-9d5b-23c29a2f21a7 | -6.80069 | -59.45418 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdd42800-1877-302c-94c7-736c8b36356f | -6.79455 | -59.81627 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0146b153-7ddc-33b0-aa6f-ae79d9ad59a2 | -7.49085 | -55.36391 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce17ef62-4b68-38c5-b4f2-190f2ff03680 | -6.1337 | -57.82885 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76ee46a4-4f83-3a95-8ba2-08366064f0c6 | -6.79938 | -59.65206 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 862d4081-5060-3a0f-b45f-cf88b203a476 | -6.80935 | -59.58466 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1908449-643c-3be7-9ffa-c8f9105ac7bf | -10.79633 | -50.92272 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| dfaa4921-7020-30e0-8de6-645d0c2c900c | -6.99829 | -59.25552 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 27b2f77f-a230-37ef-800a-3cde2c9c4cdf | -7.21352 | -60.61985 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e897581-455f-382d-a979-e5620cb98471 | -11.16862 | -54.00441 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce0148b2-2a5a-3a1b-8385-47bc42a54d35 | -6.35635 | -54.78114 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78cc89b6-eecf-3fb6-a562-0a7513fb4915 | -6.34898 | -54.75636 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18d41e06-eae5-3d35-9df4-bc31a3c77a93 | -8.80595 | -62.31818 | 2026-08-25 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b155f93a-36e9-3e6e-8ce1-d209207a12d8 | -6.7871 | -59.65517 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e5e3e49-ff52-377e-ac95-4171ec3ff262 | -7.01018 | -59.25728 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 90245bab-3500-3fce-ae76-017129d29b62 | -10.8043 | -50.91653 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f18d11af-0fce-3685-845b-9637af12330a | -6.81786 | -58.65186 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5396c1b7-1100-321c-8c5c-0c85cae74dd0 | -9.15484 | -59.5678 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8ff7118-0112-3eb5-b439-73226ce98f2c | -6.33597 | -54.77153 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e913bb02-9efe-395f-801d-2f8d29c42f21 | -6.96948 | -59.08085 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5aa217d-30ea-325a-a032-db60e0f375db | -8.57186 | -54.85275 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5736b350-f58d-3d24-8e12-1cb0a8071506 | -6.8098 | -59.68794 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b1b20c31-799e-3ce4-b3af-8ad6e2475266 | -6.34616 | -54.77639 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| caf909ec-9634-332f-bd69-6feaf61ca4df | -8.57994 | -54.87552 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a67ef264-5dfa-3b33-aa99-91f0c7da7ea4 | -6.81036 | -59.60461 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b75c2af-f59d-33f1-95c6-dadaefaf0be3 | -6.68791 | -58.72594 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a995c9b2-005b-3374-9aae-b6faea94e0c4 | -7.38221 | -55.18472 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1917850-0c5b-3ac6-92fb-f2e7df8d3e79 | -6.13001 | -57.82405 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8f53987-0e31-3b65-8b20-342f30f3a8a4 | -6.22644 | -55.61939 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1df416c5-1b9a-3a11-a524-bfec2f8542e0 | -6.84218 | -52.50719 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0570575-934b-3325-8107-57f9ce888e0d | -6.6259 | -58.49144 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1bcf8be8-7756-3711-b26c-24812bc43c2e | -6.13622 | -57.8415 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32c184ce-df5e-35d9-a783-a9e2337c0d34 | -7.22085 | -60.62098 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b6b7f78-f379-3b77-bc67-15c93702f2cb | -6.8125 | -59.59011 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdf7c6ed-d2fc-3291-9a8f-6ca3d81ac259 | -6.99037 | -59.25428 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 67b19711-f802-3587-acd6-f48a61b2b9e2 | -6.35589 | -54.7844 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d03fb8-b68a-3996-afaf-049638fd022b | -6.70152 | -56.34404 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2f605ab-66db-35c5-b92f-b5efc9010a78 | -7.63936 | -63.38671 | 2026-08-25 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053249fc-94e7-3580-bdab-d05d9e3a744c | -9.39198 | -60.58081 | 2026-08-25 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aef6f3f7-7c70-3033-8dd1-a87fbb615507 | -6.74385 | -59.64685 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56a0d459-dc34-376a-a4a3-0d4c8dc04bed | -6.18952 | -53.48671 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 933de5eb-f43d-35bc-bc58-20f37acfb1c6 | -10.80351 | -50.92361 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| d57dc8d3-6797-3088-9f6b-cdc37ace0b00 | -7.00774 | -59.24649 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46b76226-ba25-38c5-9b63-ccf8bba40325 | -6.1369 | -57.86646 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c67d083-227d-3d03-9f9b-18a2b62b342f | -5.78806 | -57.56017 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eabfdf53-3a11-351f-884d-f3d3203495ab | -7.49217 | -55.35406 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a88935b6-6c84-3c23-9b01-1567f6476397 | -6.79703 | -59.58771 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 71091bdb-8ffb-3ecc-a6c0-b7a58f7b39ea | -7.38266 | -55.18151 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69f4051c-5f97-3c88-9736-49ccee076a7c | -6.14316 | -59.92039 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 497975ab-e952-3cb2-847e-843dafa1ac31 | -10.78515 | -50.93039 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| bf423e2e-d03e-3caa-b73d-8680bc441f6d | -10.79554 | -50.9298 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 76f7255e-918b-3170-8ff6-2ae5ff126efb | -5.94621 | -57.73256 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5800999f-fdec-3dd6-b4ef-47032885effd | -6.97189 | -59.07484 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ace23c40-512f-3b77-a9f8-fceae867a653 | -7.54609 | -61.37226 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a2921545-ae08-37d0-ac74-c54d5437a0dd | -6.79876 | -59.60279 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87dd31e5-26e6-36fc-bf21-b143f7501b70 | -6.63581 | -58.4815 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29085721-2883-3ef0-aff0-5da929c6b5b8 | -6.79379 | -59.63653 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 138041ec-ce7d-3b1b-987e-71962a526041 | -6.96547 | -59.08025 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1474c72f-4da9-3839-abdd-57f27d6f9a9e | -10.4301 | -61.22247 | 2026-08-25 05:48:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e111d334-3de1-3990-b23b-f47723c7e9ba | -6.81494 | -59.6004 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ac11428-2d5a-31bb-9845-58503c989270 | -7.54376 | -61.36375 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a7ead99d-206d-3ee0-b148-f8f7907f3c56 | -6.01449 | -57.666 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 04ab6d24-ab1e-3aa7-835d-145d37bb58cc | -8.62129 | -54.73538 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 487fb844-b96d-3c06-a6f1-8ccf9179a3d3 | -6.36359 | -54.76843 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e744fe0a-703b-35e3-8229-9846e3e76dfc | -7.43883 | -59.78007 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 314d60ea-5629-3efe-8dee-afa7b53b4939 | -6.34082 | -54.77571 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21f5f9d6-90a1-3ba4-8617-d357817e31e7 | -9.19252 | -59.45361 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0044e09-e7fa-375f-937f-a197e0416fc7 | -10.79233 | -50.93125 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.3 |
| ff3637fa-c21e-383e-8461-7c82f9a69a28 | -7.53787 | -61.35471 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e1122d8-9c4a-3118-b2da-fc4536c4a211 | -5.78518 | -57.61312 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7699d63-1528-3511-bd16-edafe2b111ea | -6.80805 | -58.66167 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9abe900-a28b-3287-9962-4497881cdcdb | -6.61111 | -58.37829 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9428bf7-c3e1-3b9e-bdb0-9fb0191fb3cc | -6.63472 | -58.489 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c3f9325-61d7-3a2a-92d0-37217ac541e8 | -6.35148 | -54.77713 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3730f3c9-4ef4-3618-9590-d0dec8cd7ef1 | -8.56476 | -63.02488 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95106a0a-b6a5-3cf5-924f-0e84de460f98 | -6.35053 | -54.78386 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd971eb9-d27a-36db-b16a-c404d50f6465 | -6.82143 | -58.65625 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README61.md)
