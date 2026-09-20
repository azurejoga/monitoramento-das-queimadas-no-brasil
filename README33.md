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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4adbf681-0abf-31e6-b02c-aeb2c894f603 | -7.43712 | -44.7492 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 116d4b66-1179-3bd8-b7a2-c3c8579f223c | -11.0442 | -48.30102 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be99224c-b660-3122-b01b-b1ce5aca6000 | -8.63783 | -47.61309 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 783c0a6c-3742-3672-bc21-c217f646d486 | -8.26254 | -50.85794 | 2026-09-20 04:19:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c7cdb4c-a667-3ebf-88b6-c7764bbf4cc8 | -6.30057 | -47.634 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e5c37bb0-9618-3527-8ad5-0320aa44e6e1 | -9.72343 | -47.26474 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da6af822-4ce9-3504-9276-15e300c1fe90 | -7.35763 | -44.86903 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f859a47-feaa-3924-830c-73f02fc48c40 | -7.5691 | -45.39781 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 470f02c2-692e-3424-87c2-9c99efa98ba3 | -5.82842 | -44.13077 | 2026-09-20 04:19:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f44d60ce-205a-3f4b-ab12-5ca0d74612e7 | -11.4804 | -47.78806 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 33a830a5-42c1-3bdc-a559-fb7f161ea2de | -7.86061 | -44.85292 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17c2f57f-5d97-3a5b-b368-3391985b0932 | -9.83505 | -46.42992 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 782dc5a8-18fe-3a09-a3c2-7573eaadefd8 | -11.02246 | -48.30123 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e67b3505-12d6-3392-a221-df02c6827b3f | -8.1821 | -54.76249 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fb11b2ba-b08d-3e7f-9f35-d889615178d5 | -6.60802 | -43.75578 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4eddf069-c517-3edc-800e-4cc69a937ec9 | -5.84359 | -53.54446 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c4074524-174e-35f2-95de-32b0d26542bc | -6.41977 | -45.85711 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db667ed3-41c9-34b8-b2d1-3e11dd7936f1 | -8.16535 | -54.75326 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa24bdad-7de8-3e64-8236-205401965870 | -7.08848 | -42.08052 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ecca7dcf-262d-3548-b4ad-9165385d8125 | -8.1568 | -54.83179 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 570af786-6e32-3d29-ac0c-5145c73d67a0 | -5.2442 | -43.66151 | 2026-09-20 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42a3b291-b273-3d3a-8a6c-56a6cc8c217d | -5.49789 | -44.30497 | 2026-09-20 04:19:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d483ae2a-dd26-3ee2-a988-5c5c14365fb5 | -6.44751 | -44.57486 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ec52702-c871-3beb-8e48-0c05b70de06d | -8.62716 | -47.62427 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1787027c-ffac-3f1b-b2da-7f69579cb0a7 | -9.02315 | -48.77488 | 2026-09-20 04:19:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 845fccdb-94b4-3c3c-b3d5-caf19a4d49f4 | -11.10494 | -49.50614 | 2026-09-20 04:19:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97d6da9b-3af5-3eb0-80f9-ad1c7499994a | -5.83998 | -53.52508 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 96a38903-0dfc-36cb-82ea-7b794ef40c09 | -6.94574 | -43.09707 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07026be1-71ae-3398-af75-704f19d3def0 | -5.32871 | -50.09477 | 2026-09-20 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07fe59e9-df31-3245-b8a1-0c4e832169be | -9.23045 | -46.23376 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ba75e9b-ecdc-3a70-984a-8228a26f9c83 | -8.37881 | -47.19246 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd6ef8d5-fd8a-3bb9-a736-251363c6237d | -8.41872 | -54.72549 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11468740-2169-356a-b149-0088e9f83316 | -5.43201 | -47.61115 | 2026-09-20 04:19:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8a19d39-e62f-3185-9379-e5d47392b6ed | -7.2771 | -45.55117 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60422a14-5c88-33b1-8f59-ed2726e376a6 | -11.02177 | -48.30507 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e155e3a-458b-3b40-bab8-2a06ad09e53f | -9.27543 | -48.24037 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 889fc29b-a586-38d0-a541-c261232082ec | -11.03304 | -48.31495 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9378669-2e3d-3e43-8db0-129676df30bd | -4.26326 | -48.63973 | 2026-09-20 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 60c2a3cc-d513-3a2b-bc09-18d5d0ea316e | -4.25616 | -48.54028 | 2026-09-20 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f76732b3-763a-3efb-9e97-8f2769b2a5b2 | -7.06223 | -46.74409 | 2026-09-20 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43fb583c-d638-310f-9c31-d74eb63cf38f | -5.85745 | -53.53881 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b120e5e2-66e5-3196-913b-01d92b71adff | -9.26113 | -46.19116 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58f57c9f-3365-3b78-9448-9fde8a0b90de | -10.09456 | -48.41426 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 305eb794-4c15-3ea3-a78f-659648bce874 | -9.83586 | -46.42519 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 433bcd5c-768d-380c-8285-fdd735619a72 | -6.30546 | -47.60526 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d05343c-c1e1-3221-b3c2-9e381b4e2ad4 | -6.66955 | -50.8926 | 2026-09-20 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0f6362ab-eb36-32b0-a64e-86f41c5e2332 | -8.18099 | -54.74427 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8348313b-79fb-3796-9b00-a51ce1ef7ee2 | -6.19644 | -44.78146 | 2026-09-20 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73f713fd-d84d-33a8-a927-33178baf6bf8 | -6.28092 | -47.59204 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f940eda1-c9bb-3472-9bf7-ba743f7dc070 | -9.94852 | -45.54639 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c226d137-1686-377a-abe2-5d5d10f8c87d | -7.62527 | -46.1244 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4f48a0c-8f9f-36d3-8364-2b67f615fed9 | -5.83133 | -44.13537 | 2026-09-20 04:19:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 948e51d5-83c3-33e0-b4a2-6abe3e77dcc8 | -3.00719 | -54.18005 | 2026-09-20 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 390a09f2-e5c2-31e5-b5e3-b91a55afed15 | -10.48734 | -48.09713 | 2026-09-20 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5730ff9-74b4-35fe-8d21-2f57eedee41a | -11.01004 | -48.32198 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc3a055b-9eef-39b1-897f-56ee04fdd672 | -11.00778 | -48.31038 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b0cdcf4-e8cd-386a-8b3b-89ea8e4bd850 | -8.61536 | -54.60151 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 733cbbc3-d449-3786-8eca-3b9bea479ae4 | -6.60864 | -43.75193 | 2026-09-20 04:19:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0cb3eee-bb04-35aa-9762-c30b6af8856a | -6.91437 | -44.90755 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ade81be5-bab2-3294-89de-848ad75795b4 | -9.55962 | -46.55667 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53d779ee-d73b-39c9-adb1-5b07d925734a | -10.10033 | -48.4322 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dc6d545-85a5-331f-95e2-324a29f7f3ee | -9.12536 | -45.73357 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e600c4d6-3ac6-34f3-a401-db33f85118a8 | -7.4306 | -44.74393 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81d486d5-c89f-341e-90b2-da9f4fc7abe9 | -5.82777 | -44.13477 | 2026-09-20 04:19:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c7fe4f8-39a8-3c46-8084-6bac6c607f9b | -9.82434 | -46.42366 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e7b4530-b153-390d-ae3f-6f19bd6f14ed | -10.31737 | -50.20884 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| ed55a40d-c778-3876-84ab-d0482711eec0 | -6.9197 | -42.91517 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 490580e8-4bbb-3277-9b20-000bb3b44fc0 | -10.84175 | -50.94102 | 2026-09-20 04:19:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db199a17-8ed8-39e6-8eca-ebb76a354a15 | -7.28009 | -45.55634 | 2026-09-20 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50a6a875-8c39-3163-bf4f-2f5b835c7ca8 | -11.48633 | -47.778 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a47568d-a8a7-39a0-9dcf-290568e00e2f | -9.914 | -47.71678 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18dd8999-d379-38b6-b777-22c3bee17b8b | -5.8345 | -53.52079 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e61007d7-97be-3e61-abdf-b6c8d971bf37 | -8.44225 | -43.86088 | 2026-09-20 04:19:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| cb31a0ec-756a-385b-b074-2bf838921901 | -8.17873 | -54.7437 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5385512-3ce4-38ec-9f91-40b38e5ad615 | -8.43358 | -45.82569 | 2026-09-20 04:19:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c750d67f-4cb1-326b-b678-c9bb9559e67a | -10.53862 | -46.72248 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a495450c-a32c-318f-addb-5f4cb2c0ffd5 | -5.8584 | -53.53367 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e9471f93-851d-3c94-a9e8-6d6e86c465ec | -8.08332 | -55.34819 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56dbc91d-7242-3056-bbee-301cff34ab58 | -8.96694 | -44.66559 | 2026-09-20 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c08c9d5-6b14-3b72-a74b-c2642dc7cc4f | -9.73611 | -47.26324 | 2026-09-20 04:19:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 289d8d36-3eb3-3d44-8308-a7331171e28e | -6.54793 | -35.50307 | 2026-09-20 04:19:00 | NPP-375D | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc038940-9bba-3aca-9a22-0e7dc5ece172 | -11.44529 | -45.39573 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1b2b20c7-5dbf-3bfd-b410-54c0774468ab | -5.46825 | -47.66568 | 2026-09-20 04:19:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a028442-bb28-365a-a3a2-917d1c5349eb | -7.59234 | -46.97947 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17b494ab-742b-31e4-80bc-f5d02d0b00bd | -5.75432 | -45.37109 | 2026-09-20 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ba25d96b-da11-3fd9-abf2-64a1e08e672c | -7.37604 | -44.71043 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b762fc9b-6adf-37b4-b186-68903a81f861 | -3.55547 | -50.29187 | 2026-09-20 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3000f35-7569-3fdf-9c72-27b3aeade412 | -11.45112 | -45.72039 | 2026-09-20 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf86fbc0-57d5-3773-b601-889e597f4835 | -9.28 | -48.20465 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2ab16272-2629-31e6-bc03-b2c3d15c66c7 | -11.669 | -43.41845 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79055e55-64c7-3757-8b96-2d74c80bff79 | -8.63715 | -47.61697 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a7677e-690d-35d3-aba4-d261848aa254 | -11.44596 | -45.39171 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a170613-2079-3dcd-8fad-b885e81b5693 | -7.86556 | -44.84537 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 23849f9c-31cb-38f1-a5c7-2a9b6b66aa35 | -7.06023 | -47.53542 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4ea06de-3a9f-351d-84eb-9f5f4647a40d | -9.27769 | -48.20297 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f69e997b-ddc9-370c-b86c-81535d622736 | -5.34526 | -44.82767 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b14e1052-2209-37cc-9471-b6f833ee319e | -5.6396 | -43.37831 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da4ff1a5-7c0d-3f47-b9bd-36f336640a86 | -5.67224 | -43.40661 | 2026-09-20 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c935701e-ed4a-382e-9735-1cba45fa1af6 | -10.27562 | -50.27336 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 2a2ce45d-ac67-3b7e-9d91-dd695f6f0db2 | -5.35195 | -44.83321 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README34.md)
