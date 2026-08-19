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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 41951588-e4f4-300a-9d6a-4ad7c4b69047 | -9.42199 | -60.4409 | 2026-08-19 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 7f9394a7-f87c-36b4-8f00-8a029e186705 | -3.01607 | -51.05719 | 2026-08-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a18a919-733c-3b35-9252-c8ab52144b40 | -8.57207 | -54.73216 | 2026-08-19 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aba1515a-cbc4-3e77-ac52-4d0cf1b4adb2 | -6.78824 | -59.44948 | 2026-08-19 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc04d741-3577-352d-98b5-f400980225c1 | -7.60902 | -60.95253 | 2026-08-19 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91db00d6-4a5f-3f0f-8860-11d6a79ce5d4 | -6.14458 | -57.88443 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ccc478b-4ed6-30cc-a9cd-ff7f6c45c4f3 | -15.28848 | -56.44822 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87788639-b0ac-31e3-bca1-3d801803080d | -12.00049 | -55.52885 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82908ffb-2c10-34d5-9051-d0cad6a6623e | -11.22497 | -55.06321 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5d25ceb-ef55-37c2-a258-a49444d9b6a2 | -7.24896 | -49.89491 | 2026-08-19 05:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 32270060-554d-350f-8927-ea9f32ae4ccc | -6.00714 | -57.86073 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fc861fb0-69db-37e3-b4a7-cb85baedd4e4 | -6.14174 | -57.85559 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 488dfc6f-6874-3a88-ac4f-ad25b9bd3a93 | -12.76849 | -48.45333 | 2026-08-19 05:25:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b502229b-9879-38f0-ba99-16d9c3087777 | -10.94204 | -57.10795 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 125fbcd0-6a7a-303e-b6ef-6bccc2567f67 | -6.00242 | -57.86807 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 822a1334-68cb-3b09-adff-9268cb6c3e77 | -6.35292 | -54.90126 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 723486f6-d00a-3e27-9678-8ebad42b2cf1 | -6.02202 | -57.81002 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f505933a-f1f8-3cb9-82d1-3b6c7a90357f | -4.46562 | -55.46333 | 2026-08-19 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94057f04-30d1-3782-b9c5-22a217ba6358 | -6.03789 | -57.82463 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22365a29-7199-3607-af55-bbe559f8adc4 | -14.15113 | -52.92469 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 70be972e-7b67-3358-99ca-7f07f5b31a77 | -6.3535 | -54.8973 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1750b072-6749-38aa-bca7-65361adebae0 | -5.44203 | -48.41416 | 2026-08-19 05:25:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| dff7ec5a-04c9-3702-b274-8295847b18b0 | -16.26117 | -57.67034 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4f259f86-258d-3ec6-b2e2-1838409c3e5a | -11.22533 | -55.0798 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1b5e6e8-a598-3158-a752-aa03fc08f38f | -16.24546 | -57.66435 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 494fb8fe-857d-3b88-959b-01ada36a4fc0 | -6.338 | -54.91502 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b266186e-dd7e-3c23-880f-d6f0e9e7af31 | -16.25308 | -57.66909 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0820799-b74c-3315-9751-6a01a5ac2c50 | -11.21648 | -54.00622 | 2026-08-19 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6133be75-7414-3473-b34f-bcc966e30f8f | -14.15454 | -52.94325 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| fe4a3bff-9ee3-3b3a-abc7-1992463e8547 | -14.21844 | -52.91138 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1fad7179-8f09-33a1-b426-10af899b659b | -5.13996 | -56.27844 | 2026-08-19 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55dab77e-2677-3d5c-a2b2-7be7002a7288 | -13.4544 | -51.7956 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7371cc81-1455-39de-abb2-06ecfdd4497b | -12.76212 | -48.44636 | 2026-08-19 05:25:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a8be93c-9812-30c5-b387-bae52212cb62 | -6.0999 | -57.86951 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a998c8c-30d9-3089-bfa9-90f83bd0e6fe | -6.39374 | -51.75129 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9cb2205-f84a-3c1c-b0aa-a2417a5acba1 | -14.15416 | -52.94665 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6442019a-582f-315c-86a9-f077e5635f21 | -6.14045 | -57.88787 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c25eca97-51ad-3b76-bb86-216a3004bc05 | -6.35235 | -54.90519 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8aa419c4-67e3-3877-8b89-464864263ccb | -14.15273 | -52.93593 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 473721a7-d5de-36ed-bd7d-acb33d57b0c8 | -11.24443 | -54.82409 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44409267-1587-3691-8a52-25fa1c91f4b7 | -6.00541 | -57.84829 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97f65c9c-fab5-3cd5-9da6-aaebe42695b1 | -14.14942 | -52.91771 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea46a0a8-ca9d-3d0c-a0b4-ac1bf3a01089 | -6.01187 | -57.85329 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7be7ee3e-bdfe-3788-99ab-5037d2d9e29c | -5.4947 | -60.14154 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5b5c81e-9225-3016-9c32-c6642b994572 | -10.9286 | -57.17695 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf544bdd-2ea1-35cd-9be0-4fbec832332a | -11.81178 | -56.60243 | 2026-08-19 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1efb83d-8470-3374-9fe0-d3c6f2ad871c | -13.57957 | -51.67589 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9d6bcb2-7955-304b-8017-d11208f973c5 | -4.12599 | -60.78158 | 2026-08-19 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66872ffb-095f-3f72-ac03-315d1091fc2c | -6.09216 | -57.92109 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e874e9b9-8403-328c-9a80-0c3a3b13cf4d | -5.99895 | -57.84319 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1348d647-8afe-353e-b4fb-10a3afd4a54a | -6.33914 | -54.90712 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73937e35-ef68-3af2-8049-a20bb01a6a87 | -6.00308 | -57.83974 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2b4fea83-df00-362f-a9c7-9c1a80813152 | -5.99949 | -57.86364 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 093a51a3-b86f-305b-9ddb-f297e937dd34 | -6.40446 | -51.71127 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72132e18-31fa-3d16-a2c2-7b082de6903f | -6.10109 | -57.86163 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0901e5ef-c0ce-3d5d-b0ca-401a6621a775 | -4.12545 | -60.78505 | 2026-08-19 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 764d0c29-d8dd-3cbd-ae6c-de6398803c4d | -6.34871 | -54.90058 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ad96746b-8066-33cd-a0c8-c0da8b1e1684 | -6.54698 | -56.5532 | 2026-08-19 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df02c2de-3f7e-3d2d-a6dc-9ddb6b1e17cb | -11.23096 | -55.07156 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69d756ad-d865-38dd-8a70-887ed7ace58b | -6.40401 | -51.71445 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0da3b99b-c122-3745-98ef-e415a8a21138 | -14.16946 | -53.05255 | 2026-08-19 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b940247-f7df-34da-b0e1-e4004e54a164 | -13.45289 | -51.79838 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99049220-6436-3cc6-a34d-90d3bbce63d8 | -11.24172 | -55.05905 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f942c0eb-306e-381a-8c80-7d1b852330d4 | -4.28165 | -60.85195 | 2026-08-19 05:25:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4561d15-c213-3550-94ad-abd9eafabbbd | -15.88422 | -55.56807 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 91e45edf-75ab-3517-a181-de7bb4f25c38 | -5.49524 | -60.13809 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e767534a-c919-324d-8063-fc180592c9fc | -15.77508 | -55.57651 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ca332b23-ca60-3700-b828-14db090b575e | -6.08512 | -57.92006 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 304c7fef-e6c3-30ab-af7f-9583869480cd | -6.13993 | -57.86752 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c41e02f5-f7e7-3e27-b9bf-f376bbc9396e | -16.24903 | -57.66851 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 818e9769-bde8-3224-81fe-1602c610e4be | -14.19794 | -52.89869 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad953311-92f3-3e9f-9357-b4b85c362fb0 | -5.74034 | -51.70458 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd7b20d6-a6af-37a7-ba42-740c58460180 | -15.77754 | -55.56218 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d74c95e-6880-36ee-b721-1f1e2a0769e8 | -6.44467 | -52.72536 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9aa54e00-8ede-35e1-9621-ff9c58308ab6 | -10.93182 | -57.18237 | 2026-08-19 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1c85f84-aba1-3f97-8784-1a9a9a97ddae | -15.27667 | -56.5064 | 2026-08-19 05:25:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d254d4c-161d-3751-b362-464214e37c6e | -11.22435 | -55.06769 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db11cc8c-3d6e-34f9-9126-b2208d2b2eaf | -6.1469 | -57.89291 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6956f8b-4894-3ac7-8a7e-5f8d98a94c0c | -12.06123 | -55.44189 | 2026-08-19 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a237b39-0f10-3393-8d7e-fdbf5a45a04f | -11.22474 | -55.0843 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1050357-1d4e-3ce5-8cdd-591491247c17 | -6.41183 | -54.94397 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1494bdf-4679-32e2-9508-31ef2516e8dc | -5.49577 | -60.13464 | 2026-08-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 96af08b5-1a1e-34fc-92f7-28e2b3750d04 | -11.23723 | -55.05843 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df01e255-8e8f-31da-807d-d64dd0488174 | -14.19831 | -52.89551 | 2026-08-19 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 91e5873a-69d2-3d33-8107-12c3e1f12a7a | -11.1973 | -54.82422 | 2026-08-19 05:25:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07eacf54-cd62-3a5c-86e0-9c143ade066f | -11.24112 | -55.06369 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4bd6791b-c441-3f45-b41f-04d03e51e68f | -11.71772 | -54.62746 | 2026-08-19 05:25:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2ffed65-88d3-3063-ad30-d5c28a937bf4 | -15.23374 | -57.66371 | 2026-08-19 05:25:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 837d9aea-c16e-306c-aff5-563a2f71f6df | -13.57911 | -51.68009 | 2026-08-19 05:25:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 275bb110-0e6f-3271-be8d-155abe106341 | -11.81535 | -56.6067 | 2026-08-19 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18da16fa-fee7-310b-9b3a-779692a48976 | -15.9166 | -55.5637 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a3fc409-693b-3506-8ab5-9a459bf87318 | -6.44645 | -52.74817 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 24c69ecc-2582-3a15-8079-3b3ba679ac54 | -6.42081 | -54.94133 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 286454f3-a483-3088-ad84-9e711e91cdb4 | -6.34506 | -54.89602 | 2026-08-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 544f5f97-f7ae-306e-ad3a-2f89b68cc01a | -16.52449 | -54.68512 | 2026-08-19 05:25:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 10cd3a68-f600-3647-825b-314a248e94bc | -11.22707 | -55.06638 | 2026-08-19 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d17ae17b-e193-361b-a144-8edde9df6f79 | -6.45037 | -52.72052 | 2026-08-19 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2492ba5c-856b-34bc-8739-93755e828bd0 | -6.08571 | -57.91608 | 2026-08-19 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 61587c59-66a0-3099-b9c0-29af3b54ca66 | -16.26572 | -57.67025 | 2026-08-19 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c40a8f3e-57ac-3c30-92b1-f3f7162f1fd1 | -15.77609 | -55.56812 | 2026-08-19 05:25:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README59.md)
