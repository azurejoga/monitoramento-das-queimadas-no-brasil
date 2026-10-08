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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 263da4aa-880e-3d90-9f94-5b71160ab669 | -10.62451 | -53.85414 | 2026-10-08 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dabb599-1711-369d-8e33-aff7a305ba7b | -3.041 | -54.26903 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 752b6eb3-101a-3a68-b431-0a4b95a58a22 | -3.58958 | -54.68232 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d771aac5-2df9-3454-8cfd-52b737cf6aed | -3.68053 | -55.95054 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2be2cbae-36a0-3714-ade4-647ea8c5b995 | -5.69244 | -53.48351 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3a7b55b-7b79-3ea4-ac78-5761d1f82f4d | -3.1707 | -50.45639 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6402dd8d-c8b5-3153-ab2b-a24ef5691d2f | -2.77867 | -56.50115 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6039e081-430b-3950-b908-f965d583de59 | -3.62824 | -55.27921 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf2cc4ae-e0f1-3d63-8bdc-0cfe4ab57cd0 | -6.62967 | -43.73186 | 2026-10-08 05:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 87d2dda8-b01c-3f36-8b64-f6f3bb1b280c | -2.8614 | -49.54382 | 2026-10-08 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 627af4a1-9cdf-3e9a-89aa-462994b31211 | -1.33175 | -55.42941 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9709e8b8-dcbb-34d1-9ac2-0b8d75f7415d | -2.84828 | -59.11778 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7247892e-7884-3e77-8b5b-aef5564837c5 | -2.76053 | -54.10205 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88c7f9ea-6697-3043-b6e8-9c7d60c6de9d | -3.43322 | -59.62632 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1599437-5d54-3d88-b5c4-18b74b32e60c | -3.07224 | -54.25741 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f431f222-7caa-311a-a50a-2f38d4c0ea0d | -4.14501 | -54.03192 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08fb3dca-6ae8-3109-a09d-1f0156e3ada2 | -6.73444 | -55.1074 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19e72107-f46a-3d87-a803-258605159c59 | -2.93575 | -53.92822 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc61c634-77b8-378e-bee4-8a04feb569f5 | -7.38882 | -55.20747 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cc4ad0b-7ad8-38b4-8acd-837188ca0cab | -1.47446 | -54.63932 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a1d9522c-6142-3c73-85ec-146a08afc0bd | 0.44372 | -60.53528 | 2026-10-08 05:23:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddd69ed3-1491-3a56-a265-4caf4c4f0ac9 | -6.95 | -45.28887 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 65fd0231-5f00-3c78-a8f2-99003ea0488d | -3.93037 | -54.57568 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1b2e19-b884-3be5-88d1-68f035a864e5 | -3.58636 | -54.30659 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ac541ae-f102-3797-ac28-c069bd6b8576 | -4.12227 | -55.02393 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d99942b9-6e5c-3d4d-9606-5e199c1d2ae7 | -3.78321 | -50.75882 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ee0871c-fcab-3f1b-826f-f98cc87179e1 | -2.5052 | -56.13591 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b233c126-aed3-36d2-8739-1197e1d89b2e | -3.01321 | -54.24147 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48f487d0-321f-3ff8-b2d0-15998c25fade | -3.22879 | -57.9501 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca8f628a-8088-36d7-b881-1dd8c63538ce | -3.28506 | -54.02421 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76a6c1a1-ee69-3cfa-9d74-b75c0a71826b | -11.75391 | -61.06199 | 2026-10-08 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ca601898-c453-388a-b81c-37f9d27a6acc | 0.78956 | -59.19745 | 2026-10-08 05:23:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96fca789-3332-3c80-bd0f-c6e56d10e3e7 | -4.34221 | -43.79932 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2583f51d-573e-38ff-84ac-aec8bcc667e7 | -3.20499 | -53.86723 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c90769-951d-3657-ace8-c122a3e99cc6 | -3.60425 | -54.56569 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ddc6231b-140a-3c41-bd9c-bc9230ed441e | -2.50637 | -56.17151 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| cbcd7e1c-e5e4-330c-891d-0b2a294d6b67 | -3.2171 | -57.87102 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73d7e725-9fe7-3c10-ba9a-431e6f288b1e | -3.39854 | -60.83604 | 2026-10-08 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e83d2c9-b2db-3e13-bd11-11fe0fc2b8c7 | -3.67556 | -54.17707 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c76a13ca-ced8-376d-8bdd-3deb3534381b | -3.28551 | -54.04435 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715e3caa-37ff-3b49-af3d-11841563c30f | -2.58458 | -56.14463 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71fd2085-bdc7-328a-b900-648854a17746 | -3.05458 | -53.9304 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41c3c150-70a5-3273-a9d2-d7b25640d0ec | -2.98398 | -54.10705 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 387a0824-bc67-3a86-a8c0-a70f192647ed | -4.89741 | -54.99259 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3c6f112-53cc-3944-92e7-767560906115 | -1.45896 | -54.78045 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9698caf8-8e80-3513-a007-9fd637ac1ce3 | -1.82733 | -55.03454 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61ad021c-bc62-3154-b690-b69d8b2b0a55 | -2.9545 | -54.13024 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7109fb9d-c1f1-3ad3-b3e3-0f64b2bde496 | -3.73685 | -59.47314 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 28312a43-27bd-33f6-ae9c-dbd9ec291b51 | -8.61777 | -67.05798 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 516daef9-ca9f-343a-8081-12efbfe87314 | -4.7528 | -55.65465 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2e7e882-ce2a-338b-a8ee-12a74a7c8234 | -5.11334 | -47.11815 | 2026-10-08 05:23:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b62535ee-f709-3e54-83bf-bc6d4ad1903a | -9.53068 | -59.37992 | 2026-10-08 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0c80b03-27a4-31fb-bbbd-1fc6b0f9636e | -2.90012 | -54.15732 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be93f929-fc07-30c4-bf9a-3c68c8c80905 | -3.04569 | -53.94109 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87aa839c-8416-37ec-9fda-a9305db6f261 | -3.27801 | -54.02313 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e22a8f-1f11-3467-b395-816e825d66a4 | -2.76565 | -54.09805 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdb5cbcf-cd09-342c-a441-d346c2022af0 | -1.51761 | -54.56429 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9f4d5c4-2a60-34a1-a42d-f56ca4a955fd | -6.50905 | -55.39838 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89d08559-3a3a-3e33-9a59-f0ee707a1ef6 | -3.45184 | -58.06635 | 2026-10-08 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca1622d-418b-3bb4-881e-308e2bcbf823 | -3.2375 | -46.95808 | 2026-10-08 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d83d8f25-ff34-3a6d-990c-a55771e49680 | -3.0451 | -54.15211 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1a8cc827-78c9-3efe-a954-3065d89d27ba | -3.5651 | -59.47967 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35aa31ba-1ae7-33ff-a621-8b50ae8a8d90 | -1.10659 | -54.16434 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb50769b-0c13-3f95-aeb7-257f4c7088bf | -1.71521 | -55.43927 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c6db356-8882-3982-b328-d021404a2340 | -3.1201 | -53.79035 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0154ef91-3f3e-3ec3-bc2d-fcea6fbc2476 | -2.93674 | -54.17479 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70ad52ff-2dba-33dc-ae30-f3a5773eb7a3 | -3.02916 | -54.07046 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5a675533-1eab-3221-8823-c15bf816ba49 | -2.85056 | -59.26091 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3732cf5-bca0-37ad-aa5e-9e5324e783ab | -4.58296 | -54.93058 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 46e006d1-1dee-3e40-9d9f-f7e2ae95d706 | -2.78477 | -56.50565 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8b7f5e1-af6c-376a-b158-21fb87c34285 | -2.8259 | -57.60869 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dc990f8-6f78-35d6-821f-f3bc1792e50f | -3.96162 | -56.12641 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c39ed1fd-23c4-3ef6-8fcf-7e423400eadd | -2.22611 | -58.11059 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1744cec-a09d-3065-87ae-3be5b6ec20ec | -3.19886 | -50.56178 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4bc4aa97-ad7e-35f0-ae65-fa8c1849c037 | -3.29093 | -49.51007 | 2026-10-08 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba7fd8e3-1681-3366-8f42-c47fcc147bad | -6.89216 | -43.69029 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d425191-fd96-39fa-80f6-809636c80012 | -8.72336 | -45.15912 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0d767ab2-0f11-3a95-8f4e-f821cc5e4a2d | -3.77621 | -58.5253 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59041377-6ed0-3ae4-9bd1-feb635c695af | -3.28445 | -54.02813 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 296f2752-71cb-342b-99a4-d84f5c1112c5 | -3.08392 | -53.95098 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| ed8d205e-8acc-33a6-b7a1-26bfd777e54d | -3.62699 | -55.50577 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fdf8ca4-a021-3b81-b89e-8f7bba94a2af | -7.22575 | -55.16452 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33fb520c-e1b0-3b4f-99a5-b35e7b03b03c | -4.13516 | -54.25677 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af861140-8f37-33e6-ba5b-3b5f99aa9ebf | -2.05335 | -56.38319 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a57632d8-8522-3bce-b983-a72d19865bf6 | -3.60735 | -55.47724 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9c2c8b0-c5d9-3d24-ae8f-9ffea9fcc03f | -2.88904 | -59.22604 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba318745-5438-3fdc-8b00-2b83ba28a105 | -3.23438 | -53.88819 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b5e7cf5d-6453-32fc-8d87-681c7f40daa8 | -3.06429 | -54.25716 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02c5e6bc-5bc4-3a5a-8db5-50bbc52a4659 | -3.22976 | -53.8905 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0fe2752e-88c8-31d3-bfc2-4985685a2055 | -3.87481 | -55.81926 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5678939-7173-37ad-b0bb-e6b164424c5e | -2.9682 | -54.08894 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16322f83-873e-31e7-80ba-6422d85641d2 | -2.12155 | -54.80832 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73a9b091-9e8a-3ae2-b117-a2e972c9c1b0 | -3.48796 | -59.5847 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b3bdfcd-853b-3df0-bd9d-acd9d5e740d9 | -3.01195 | -57.90898 | 2026-10-08 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12a2ef82-b74d-39d2-8bd0-61a8f27db44d | -3.577 | -54.64976 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9313be9-ac2a-3329-9566-40c0c946c2ba | -5.37572 | -56.06316 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25db8f3f-bc2c-3851-ba50-b8e590542f34 | -2.49408 | -56.12 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ea7416f-c5b0-3253-9943-72abce6a4eba | -1.33162 | -54.22118 | 2026-10-08 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4432401-0ecd-3f81-a1bf-da007fcbcc83 | -6.08667 | -55.7372 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4dc6c5a8-96f5-3f6a-96b1-fce6d8b49d9d | -2.50094 | -58.0704 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README144.md)
