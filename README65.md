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
| 821d2fed-3c1a-385d-bc3b-385e9d2f3856 | -8.50239 | -54.87079 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae5b3e5c-84e8-3d0e-ab7f-758725497603 | -9.39691 | -60.56771 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2056e5ef-5529-30af-afef-4bb70874ddd3 | -6.03695 | -57.80652 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5de9ef2-7cd5-3aee-97a7-542f61536a68 | -9.40213 | -60.5821 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1460d6b-658d-3e17-8247-9c2299403267 | -9.39229 | -60.55095 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e56933ca-b3f9-3792-b3ff-365308057b44 | -8.58351 | -54.7184 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4015189c-15f5-3cc9-b159-983a986e27d8 | -9.40026 | -60.57816 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40f493da-70bd-30ef-8c0d-9627a5afe1dc | -9.40492 | -60.5788 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df43e5f3-3a7f-32d2-ba46-25a1fe736d75 | -6.78784 | -59.45092 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50e9943e-82c1-3c28-974e-55ee11479ee9 | -9.39816 | -60.5766 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee596dd3-833a-3585-8c85-d5133ff55a21 | -6.08565 | -57.90914 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbc73b4d-7b01-37be-90ab-cebcda94faca | -5.99809 | -57.84877 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f20d04ec-a31f-3ca1-ab2d-b415805bd2cd | -6.84899 | -59.01548 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6294350-7702-3809-8103-cd7054ed3a34 | -9.40747 | -60.5779 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc88d9b4-2be3-35ef-a293-aa2ee4b51ea6 | -8.54281 | -54.76799 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 176cc7da-7aca-35a9-bd3a-cf93f5c3692a | -6.76412 | -59.14658 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3906c4a-7e75-3516-b117-b4cff63cda93 | -7.61552 | -60.96977 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5f15a61-4881-3975-809d-871c21ea0c69 | -6.80309 | -59.44788 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ff9fc18-bafb-3172-ad4a-ec2f9862f17a | -6.6086 | -58.39985 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8d1398-7c15-34ee-a020-900140daaa76 | -6.76907 | -59.14722 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5188ec84-8783-354c-93d4-eb10ca808e28 | -8.58198 | -54.73009 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bec46914-3f55-3a73-912c-aa53a592d0bc | -9.42454 | -60.42449 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 327e8af1-cfd4-33ae-bcb3-9cf562e3ce85 | -6.95606 | -59.04955 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 164f0ed9-ac85-3238-9923-1f79b0bd4d13 | -9.40957 | -60.57948 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af5c8aba-7988-3e90-84cb-4c88b7bc5203 | -8.54067 | -54.73122 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a0863e77-3b45-3067-8ca5-1e22ac5aa38f | -7.04791 | -59.84526 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a78dffd-8847-3c2c-8464-b806dc9fba36 | -8.54955 | -54.7688 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2cbbc67f-e8e4-372c-8ab4-b026fa1ea246 | -6.1433 | -57.84926 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a6f1075-fd71-3557-980a-84a7717636d9 | -8.95035 | -60.54452 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b314835-7b98-356f-8dff-dadd1236bd9a | -9.12074 | -61.60512 | 2026-08-19 05:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba524cf3-50b7-3a7f-89a9-b82ba8beab0a | -8.21956 | -55.0371 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5aac804f-5bd8-3cb8-a13c-6f258385edde | -6.14257 | -57.87244 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d4290b0-51c1-3c92-9835-1cf0cd07188c | -8.55702 | -54.76394 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6d030695-08a4-34a4-93ce-7826ba166f3b | -6.14231 | -57.85605 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f8dbd77-c283-3424-b0be-127868cd0e3b | -4.28043 | -60.85628 | 2026-08-19 05:59:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc000ca8-cdb4-3c4a-8a9e-3b6c98c0ce39 | -6.70217 | -58.93561 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 99e23705-d14a-3435-a8d0-d813190d6c67 | -8.58034 | -54.74268 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4697e332-3c41-32d5-ad3d-0555c31a96ae | -6.95186 | -59.0431 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6c161f94-e987-3369-a6fe-ac7595eb036e | -8.57874 | -54.7549 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86026487-14b0-399b-825a-66e252e0ed86 | -6.14391 | -57.86272 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c0dcef1-4991-3a02-ab2b-51566a4c90c9 | -6.34317 | -54.92055 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c922bff-7960-32a9-a7ec-02f9aed6c745 | -6.76501 | -59.45183 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fad250e-fd8d-3c05-87cc-091b393c7afd | -8.5782 | -54.72675 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b346d64-da8d-3eb1-841b-aff5a787ff0c | -6.02086 | -57.80431 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62abf559-b27e-3741-9eba-bd3947597a0d | -7.05918 | -59.84304 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f8404604-97a9-31df-8142-d2159fdfa44d | -5.49365 | -60.13638 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0bbd846-e9f3-3a5f-877e-450c0d9e9e6f | -9.39822 | -60.55794 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3291742d-9376-32e7-a6c6-070e500e21f6 | -8.9528 | -60.59384 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75c63118-8ae6-3ad8-b207-f2b5c21789eb | -9.40421 | -60.56749 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65b09069-f07a-30bf-be3e-8785ce492a4f | -9.39355 | -60.55731 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e467e66e-6602-3021-8783-bb32aaf6130c | -8.54817 | -54.72625 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed3db886-916b-3ac7-b2c7-df642049ddd3 | -6.88023 | -59.04349 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbd36514-c89b-3984-8d0f-42caa8a40386 | -6.14091 | -57.84491 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f329987-e7ce-3d46-a0bb-dc05ca89c361 | -8.18407 | -55.00038 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a02ad4ab-8e79-3b8e-99f6-e273b69e8fac | -6.89319 | -56.43534 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06782f99-fba8-3f86-9a17-738bf000b6c9 | -8.94818 | -60.59315 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64954a6b-72ea-334c-9981-a7dace851165 | -6.34619 | -54.89897 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9474b4d6-8877-35a3-bd1a-088bfad7614d | -8.55339 | -54.739 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1ab64b27-f36d-359f-b571-f60c4ca0a41f | -6.00103 | -57.86631 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 825f48f1-3e9b-3128-ab2c-d3711a6d0fca | -8.58866 | -54.75299 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dddfe00e-b0cf-3cd1-bf17-26e9b08230ae | -8.55491 | -54.72719 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aaed0100-b184-31cc-ac9f-8600318eb020 | -6.76425 | -59.45709 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34cc54e2-4418-3fcd-8c35-37e24211a1c2 | -6.35202 | -54.89959 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68270784-c324-3c71-a9b3-312d10b50649 | -8.90003 | -60.56661 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9384f412-da09-3a4b-bf4c-c35f97f6f055 | -6.27607 | -55.96888 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e41ef7b-d976-3a4f-9ed8-279b1c7f8376 | -9.42214 | -60.41504 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdaf1160-2a55-384b-8624-15b070e656f9 | -7.60856 | -60.9557 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 442225e8-0f7b-372a-bf4c-340788bccd7a | -8.53606 | -54.76729 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a087062f-a664-3c38-9d25-e358bce023bb | -6.09583 | -57.91395 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 324522f0-2a46-33f6-9f94-57a826709d82 | -6.14027 | -57.88911 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67c9731f-7455-34dc-a5bd-62ed74b6dc72 | -8.22106 | -55.02576 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2aa136-65db-3d25-b902-90113feb436c | -8.5736 | -54.74175 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f874e00-4423-3eb7-b24c-0bca2fd86a5c | -7.88225 | -61.19468 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 969f420a-519f-3f5a-8943-b14a98dce635 | -7.60415 | -60.95499 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f57845a-9029-3408-97ff-4da8a0bf303c | -8.64778 | -62.83216 | 2026-08-19 05:59:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dfcf532-2676-3286-bbb7-3d1fd408f697 | -6.75865 | -59.4616 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8714af08-b769-36a9-acca-172debce78a2 | -8.58394 | -54.76752 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da5e3345-e39f-3f2e-8dba-3f03074090ee | -6.01022 | -57.84027 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1367053e-fb8c-3685-9e94-41cc64e910c7 | -6.75756 | -59.15725 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6bf85e5e-a827-395a-a5bb-aeae518e1b11 | -6.8893 | -56.43741 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33c975f4-3d32-3a1a-a809-6d619fe96894 | -8.57279 | -54.74799 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a72c771-b615-359c-a460-61a67247aa5d | -6.27543 | -55.97338 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e989431-25c6-345d-9155-d09e16a078b7 | -8.55494 | -54.74871 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b2394a0a-aeac-384c-b6fe-fd14eefec547 | -9.40351 | -60.57236 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 210a63fb-bd32-3e24-91e5-84f15d662c8a | -8.58716 | -54.76505 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da9f48e1-8b87-38e9-a77f-515218c45667 | -7.60353 | -60.95929 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7d6ef287-5030-3bcb-99d0-c49f1c844cd6 | -8.53394 | -54.73028 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a21963f-0a33-3906-b485-19a5f37987d2 | -9.42348 | -60.40503 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c09c87a6-f13d-3819-b356-c8d0b75f7176 | -8.55846 | -54.75282 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e052186-aeb8-344e-94e0-daa770c5b4bb | -6.0316 | -57.80568 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 595d62b7-13fb-3126-a70a-99a6381bb033 | -8.57369 | -54.76326 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a83a83ea-8395-3639-bdc8-2906d0a66ccc | -6.88861 | -59.05616 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9217fdb5-ddbf-399f-9d33-b14477817d4f | -9.42484 | -60.43066 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| facf3b43-201e-34c2-ad8d-54ede6a718ab | -8.5301 | -54.76035 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ad46e3b-5c5a-38f9-8d23-45d0b9befbc6 | -6.03647 | -57.80983 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90c92ca6-1f0b-3666-a08c-f260ce688da4 | -8.56163 | -54.75003 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 42922cd7-41e5-384a-8324-147cf31ea260 | -6.60834 | -58.39331 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09d90821-4602-3906-a9ea-e6e4511f6904 | -6.84342 | -59.01548 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bbe62c5a-5f9e-34bc-a07e-57f4cd2bcc82 | -7.60411 | -60.83036 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbff03bd-684d-35bd-a127-792e41e97aa5 | -6.85343 | -59.01681 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README66.md)
