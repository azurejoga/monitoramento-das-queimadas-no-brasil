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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87e675d2-ab36-33f4-baf0-c4df531ccae0 | -6.38214 | -44.42816 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5dbd78f-ddaf-3113-93d6-7263d276714c | -8.20462 | -50.10363 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 37318d12-2c1d-3957-8b2f-f0071601a672 | -9.06135 | -47.05566 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49fb83d6-f814-3bc0-8a29-cbcd8c702416 | -6.85212 | -47.87908 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32625d73-41fa-3dfd-9cbb-091f02e407a6 | -4.33265 | -48.39223 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c584fa49-12f2-33f5-b9cf-92f6fc90c7f0 | -9.06281 | -47.04569 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8527e7ed-09f6-3f69-80c3-562f5456bb4d | -8.07268 | -50.1759 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4d0b201b-6145-3f4a-9b3d-ee5a315e80f0 | -5.81422 | -45.68225 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d1d2e0f-cea1-3074-a1b3-e627c2b5bef0 | -8.42216 | -47.27231 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 984538da-bd8e-327e-980a-5af5fd5dc91d | -8.74912 | -47.10779 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4914968-f7c9-3e5e-bc2b-d20d2f0c307e | -5.55724 | -45.70456 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 465eca96-0a3c-30fe-8088-ead6864a6ad7 | -8.0162 | -49.02211 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6fc5210-7d02-34a5-88e8-4adac33b9f8a | -7.97147 | -53.25481 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1df75f11-539a-3946-982b-baeeefadac7e | -6.40343 | -42.61574 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8e3b6e9-2861-3f22-adef-bfe14da27713 | -6.16966 | -53.50526 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c93ac74e-15c1-37b3-ad46-8a7714654d1f | -7.62274 | -46.5476 | 2025-09-11 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fd9d071-4cf1-3670-9ba0-b02c0b6afe4d | -8.20736 | -47.14093 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a989620a-58ac-3ca5-943e-dfd150ee609e | -7.73046 | -50.75821 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e623b4-3659-33fa-8a38-fe37e6eddc88 | -6.857 | -47.87132 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9c3ba71b-4b5c-33a3-8752-f97ef5453de9 | -6.38661 | -44.42893 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ccb0b70-bdb7-3722-8f0b-c2537d0690c9 | -9.05674 | -47.05986 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4bc440f-7088-3478-a982-9064dc21c0f1 | -6.31938 | -47.74576 | 2025-09-11 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba8fcfb3-bda6-3d1c-b8c8-38094a5c64ac | -6.2018 | -43.53288 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 06476b6e-323e-3537-a66e-f9ab71d7dc8d | -5.3608 | -45.22557 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44033859-9b90-3cab-b3bc-06111174f6ba | -6.7481 | -45.94086 | 2025-09-11 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 552ea743-ba03-338f-86a9-9483ae7c3566 | -4.92823 | -55.7794 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3219aedc-7f27-3365-bbf0-573d1d108bb8 | -7.86109 | -44.88255 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1617d910-4b9c-3a56-9a7f-06cab86d1f98 | -7.18099 | -44.96073 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2942ab67-1393-3c2b-a8ea-84e5dea833fb | -3.14151 | -49.90033 | 2025-09-11 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc552c53-eb53-3aae-bd81-1caf8e1b0d8d | -6.24236 | -44.80416 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fc50bbb-7c82-3a3f-b3e2-18a57d740cd8 | -5.36534 | -45.96607 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0380e32-9996-307c-9441-1bfa85d7f86d | -7.67617 | -50.27842 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d0d238e-9aa7-3f57-a332-a83391543c4c | -5.93423 | -45.68558 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 808bf89b-fde4-3384-9237-8babeebb470a | -8.01516 | -48.64887 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13b281e9-3077-35d1-b023-75cabba70b4e | -8.73189 | -47.09005 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8a56bab4-0956-3524-b3e2-05ca12428666 | -5.8781 | -45.66945 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86089575-6c30-3326-bd74-c0b0629e7dc3 | -7.48139 | -46.09727 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdf29016-c6a2-3810-9d1b-887a03047f12 | -6.32365 | -47.74204 | 2025-09-11 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f2bb2e5f-8aac-3690-86e5-06259b98c831 | -7.11873 | -50.76171 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7fba622-a5a4-305b-9e01-d6fe5ded98aa | -2.7411 | -49.44388 | 2025-09-11 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5f378e1-171e-35af-b683-e119815d577b | -5.90708 | -45.75508 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b64c9d8-e63c-3ab5-80fe-6b6f68044322 | -5.82014 | -45.27088 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 971e7c2a-0508-36b7-8840-784839b41195 | -7.10214 | -50.75919 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d73b162-1a7e-3793-9936-cb07516c461f | -6.61619 | -43.99785 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d29dfa8e-d0a4-325f-b0ed-2c08575c68ee | -7.47485 | -45.28709 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40f01fa6-90be-3544-b6e8-d322a4474a04 | -6.74922 | -51.98171 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e76cb15-54a9-3ee7-bef0-9f4d4be50798 | -6.74606 | -46.01007 | 2025-09-11 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4621802-ad84-3471-9bb5-83d88ec1dbb0 | -8.03933 | -48.65664 | 2025-09-11 04:44:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ad8478a-2e57-34f7-a163-9338ec8d6ce4 | -7.58707 | -47.75777 | 2025-09-11 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86124768-a5d0-35c7-8fe4-633b5cef3a09 | -6.44371 | -44.77934 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfaeeadc-82be-3e62-9e7d-5bc6cfd67aa6 | -6.7487 | -51.96354 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8022740f-3969-3523-876d-65cc4d6c6075 | -6.63851 | -44.07428 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea0c55ee-9496-3d57-9d30-cd606d52c58c | -6.53955 | -43.10744 | 2025-09-11 04:44:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb25cf6c-2410-3766-9cfe-411f3975c268 | -6.74984 | -51.95645 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d95e6c3e-68a7-38ee-a971-57625db29f57 | -8.03998 | -48.67638 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 796c166b-65ee-361b-9d15-a6a6eb684e7c | -6.82808 | -52.80069 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46e94241-344a-3ea5-8d8d-f47f431e60be | -8.19558 | -50.10677 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac9113b9-8cff-330c-9b4b-529a78a68662 | -7.73432 | -50.75527 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f689e765-f096-3af6-a54c-345fc23f7e91 | -6.31626 | -43.81785 | 2025-09-11 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1b931779-c64a-31b9-a5b9-5bc1fcbabd3e | -7.47055 | -45.28649 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f2a9bcc-8fba-36f3-a9aa-39d994f5038e | -5.41236 | -45.92372 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddffff0c-db54-3ac7-ac47-d3b88379f2b2 | -5.82817 | -44.83743 | 2025-09-11 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4edbe660-dbdb-3c3b-8719-70234075b03b | -6.40013 | -43.51268 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd1b1312-462e-37d9-8489-416df7e79203 | -7.56094 | -48.21043 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 084b3d2f-a12e-37f7-a9e7-e4df70332d85 | -3.81137 | -52.34628 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2caa87d-0e9f-3308-8aee-980721317b2a | -7.70293 | -44.75606 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89cea0ef-0384-3f89-a51d-56a1ca27b78f | -8.96881 | -46.08811 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73d3f47a-3f9b-390c-8f5d-054fc66dd477 | -6.72929 | -51.95679 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 504f1cd3-cfd9-39a8-8909-58e38c1ba84c | -5.19703 | -45.72354 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef013251-ea6f-33c2-9e9c-43c9da735fa4 | -6.31032 | -43.42375 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c2745fe9-ef55-339d-8459-4df4af1d1064 | -8.20352 | -50.11084 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a90d118-7eba-3b95-8b78-a2c07c64be7b | -6.35781 | -44.50246 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 88ce6022-3586-3a27-8fd4-f9de7a47b7fe | -6.66852 | -44.12755 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c9deb54f-4f45-3ab0-94e4-e8db108b7a1c | -7.10546 | -50.7597 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 16cada8c-b1ff-3fe8-9935-7a3c6300c737 | -5.20107 | -45.72412 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 503dcdd6-0d60-302f-b43c-fe66c8db83ef | -6.07908 | -44.81986 | 2025-09-11 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21864e27-436a-350b-b469-4ac94a67d6b1 | -6.85149 | -47.88331 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863fcff7-faed-3a2d-ba96-d1fd235e9fe3 | -9.11003 | -46.96561 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11fca4b8-1658-3f06-a526-7a01dd9e5062 | -5.78508 | -44.86033 | 2025-09-11 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a055327a-4d76-3d3f-921f-5c741592d2f4 | -8.79228 | -48.09237 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16e553e3-afc0-34dc-96ac-be1b817a92ac | -5.45127 | -44.00063 | 2025-09-11 04:44:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f41d4643-ad51-31ab-8fc1-fe87d48254f8 | -8.42667 | -47.26822 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0a48139-ceb9-33f6-b183-7a4de338426a | -8.01869 | -48.64946 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11c80625-bf82-31b1-a523-a28e431e9295 | -6.17592 | -41.07676 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28a33a8c-4017-3c21-a329-7e9f8e6b5941 | -5.11259 | -46.23969 | 2025-09-11 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 602f8b3c-1631-35ba-b729-5706082ba027 | -9.18922 | -45.58821 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f44b2087-fec1-3137-a066-f21436931df7 | -6.25097 | -43.42888 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f682ee32-0210-33c9-9151-8405add8d63e | -8.10046 | -49.25024 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a31e6da-7157-3ccc-8506-86709d4da26c | -7.50218 | -48.26999 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3de6df0a-faf4-3802-b6e1-c038d1ddb194 | -7.86139 | -45.50662 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4aeb067e-bfd5-3a9d-92b1-32671680105a | -6.74757 | -51.97061 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b375363-eaf8-3a1b-bdde-149badddf641 | -9.09591 | -46.95689 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de3b0eb6-0855-331f-ade3-a62bcb7d7f26 | -6.18569 | -41.06262 | 2025-09-11 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cdcf9fa-e086-31e5-9221-72d0b3c0d2cd | -6.61432 | -53.33688 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11b9daec-53f7-3998-8844-fb19e83a5c09 | -5.6034 | -45.7868 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21871297-763e-370b-bb50-5dfcda53e1b4 | -6.83807 | -47.89863 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 49561aab-4912-3c40-b1d9-b93f6d65da06 | -9.13167 | -46.19187 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c3febe6-4ecb-3d92-8ed2-137d547b8cf0 | -4.3286 | -48.3955 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2290bd2a-7ffa-3d57-9d34-ad297a455fde | -8.02257 | -49.02704 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9b41ae6-2dd1-3b64-8f06-0890ba3ba461 | -3.07779 | -48.81699 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README89.md)
