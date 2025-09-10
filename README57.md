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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b724286b-92ba-3a57-9db3-06573822ee50 | -11.46669 | -49.27301 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20413520-90a9-3587-886a-656ace2ea2bd | -8.85293 | -47.27511 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55e8c369-6668-3d3d-aa0b-355d9a7a81da | -9.06846 | -46.98172 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ea18d5c-0562-3cee-ae02-221652fb69a0 | -7.74774 | -50.72773 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed51d61e-349c-31a7-a733-09011ea82d2c | -9.31587 | -46.71313 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0c1fd71-2d67-3ea5-80ed-ce8d65c21a34 | -10.96434 | -46.80322 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1b73676-7be9-3663-9d1c-d64ea71c17b0 | -6.17022 | -45.81598 | 2025-09-10 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 432f7f2f-e667-3736-9d89-1063c3c1565a | -10.30426 | -48.80361 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4de4c0b-c8bd-3495-bad3-40a903e07df0 | -7.87194 | -46.02735 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4cee553d-bb10-34fa-a827-1b569a8e5324 | -9.02808 | -49.78547 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ece04dc1-6d9e-3556-ba79-85756332f592 | -9.05473 | -49.81123 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3d941f7-8d28-3d2d-8de4-de07bf73aab6 | -10.0199 | -51.68938 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| faa527b2-9a81-38e4-95ac-0a4f9ea3344e | -8.04696 | -48.70051 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8e9ae7f2-eb20-31ab-9c15-e2ca74c4cd4e | -9.01883 | -49.53996 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 779215da-97f7-3cd5-b63b-37f8e0d68335 | -10.00877 | -48.08613 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3000b8b4-b6a0-388d-bafb-428f0dbd26da | -6.85055 | -47.92726 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2ee1e014-66c5-3fd0-b5f0-8c3890a35048 | -5.7291 | -51.68576 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 601d9e54-6f10-39b9-98ca-2411262789c9 | -8.4811 | -47.3077 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a360e8d4-c4c7-3c36-ac1f-962c5c7d1782 | -9.21769 | -50.52991 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61528e7a-29b9-319b-bd02-b9be80f717fe | -7.8706 | -46.03634 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e55d5f2d-1379-3020-b953-f97d70394aba | -9.51626 | -46.54568 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 823aaf1e-ff7e-3e68-9952-58ab9f8b7ac0 | -6.4442 | -44.06859 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a550355-b9d3-3824-a552-ab9c5839bbb8 | -6.88469 | -47.88802 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 967ccf86-af8b-3ff7-81c2-6e53d4e9a388 | -9.21268 | -50.5399 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8dbada3a-279c-3961-bf2e-1c4aa385edf6 | -6.81642 | -51.87899 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e6674d1-5dcf-3ed6-8721-19c5d7c44e45 | -7.79071 | -52.12391 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b669792d-fe6d-3953-851f-0b2a94940620 | -7.74432 | -50.74897 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a8a18f1-7b87-3774-b368-535b2101afc9 | -5.66507 | -51.63651 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eff0c9ad-18da-3c40-88cf-eeb109af8443 | -6.93083 | -43.9197 | 2025-09-10 04:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c99d924f-4d2b-3df0-af05-df6aedaec588 | -9.10104 | -46.98563 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39e6afdc-82f0-37ac-a300-83ba6a8ac069 | -10.38556 | -50.54568 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2550bbe4-87cd-3bb2-81c2-c8133a097261 | -7.99708 | -46.33028 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec488711-6292-3092-be11-2eab778e3b46 | -9.83092 | -46.05731 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0e7bf50-04f6-3551-9d34-dcacb6cc75e0 | -9.04651 | -50.50257 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b961c64-ab60-378d-9555-af5954596152 | -11.4391 | -49.27236 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5aa8f2fe-402f-3832-9812-529d9d00a1e6 | -9.60877 | -48.03853 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a05b9b22-4a48-3ea7-84b1-14a3177af6b4 | -8.43121 | -49.12342 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17a32391-07d0-3755-9aa4-e07df70a0693 | -8.95154 | -44.93937 | 2025-09-10 04:42:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f60ad0c-887a-3a9d-a41e-7f620b67a3d2 | -6.34122 | -47.09834 | 2025-09-10 04:42:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d8f94de-fd77-35e6-9f30-f132d1f29b7d | -6.95597 | -44.807 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc569bcf-5edf-3195-a8ee-6b236100b71a | -6.87848 | -47.90578 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f1be14-91d1-36fb-a910-87b7e3b77c00 | -10.38612 | -50.54216 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5276727-7506-3222-ac3e-5d74c663c832 | -9.07187 | -45.71446 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 582164ce-bdf4-3a3c-adca-c493ccc65d84 | -9.51691 | -46.54128 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd362807-dd47-317f-9f0e-925dfe84a93d | -5.42447 | -51.53633 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99c2ff7c-49d8-3d98-b726-38356aff3677 | -8.07116 | -50.18793 | 2025-09-10 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79c64fce-27a8-38fa-bf09-387eab2c88d1 | -10.75011 | -48.18284 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4669d156-5adc-30aa-ba6c-33825631103f | -10.65988 | -48.61924 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f9ff951-81ff-3f94-a0f2-69730177fcfd | -7.69875 | -47.29152 | 2025-09-10 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 615c9e1a-de7d-3b64-aedc-63f5ce091a85 | -11.65848 | -46.89362 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7816bacc-aa43-35c2-94cf-e1d4f85fccf6 | -9.03474 | -49.78653 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c5ba3c3d-e90f-3a58-838f-c6c9621da8ff | -7.07387 | -43.91183 | 2025-09-10 04:42:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52a26f37-cb5d-372e-963d-0eda5fcc2b13 | -9.43968 | -46.70789 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c173e91-0241-3bd0-9ed6-2a3b866b2b4c | -8.01855 | -44.50323 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c771ec78-6a46-35a0-ad85-fa86d7329984 | -11.12126 | -45.11509 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa7de767-bb8b-3c05-92e0-b22862d221fe | -6.8277 | -44.88985 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5d885cf-c9c0-376c-8bf5-e8617d16273d | -8.42818 | -47.27581 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f1b77c85-2476-3686-bc34-b6baa0dcfe15 | -6.68021 | -44.56813 | 2025-09-10 04:42:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee8bd5d4-10c1-34a7-906b-e47ca701258c | -11.12109 | -48.36372 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0ce7663-1446-3a2f-815b-b2b935d3518c | -6.67862 | -44.10946 | 2025-09-10 04:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adc87bbf-3870-39dd-af61-52edc4d8f9bc | -11.11409 | -48.40958 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba0430f3-8e57-3bbe-92bd-7e5e45e4bba8 | -6.86745 | -43.94179 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebba8134-3ffd-30de-ad28-c2a7f5e4baa2 | -9.82918 | -46.04259 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6bab879-78d8-3f54-9423-06184b7f77a2 | -9.10288 | -46.97321 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4fb7d23e-be6a-3672-bda1-ce51077a06e4 | -11.44887 | -43.61701 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b3fc0af-c530-3d07-b2e2-8f9815175350 | -9.9812 | -50.30065 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 174fdc6f-38d6-3c2c-b986-2299d95eeea6 | -11.37705 | -45.58904 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 865fe01b-1bc2-3fc0-9998-d7b2bf9101bd | -8.0508 | -48.67562 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08d07b51-dcab-35f4-9370-d7fcdeccf77e | -9.3146 | -46.72815 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 475810b3-4cd9-3778-b021-055362d2273b | -5.7289 | -51.68666 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5ddfbf8-baea-382d-b80a-8b3abffc3a18 | -10.30709 | -48.80791 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf1e3a16-c406-35b5-a68d-a6417d55c3c7 | -9.06298 | -49.83798 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0ba38f6-ddcb-3124-92a9-f8b262aee5d2 | -7.76331 | -50.75937 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7db03f7c-df5b-3493-9ab5-f9e6c01de2a2 | -6.87904 | -47.90211 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8c397e8-e604-3db6-b35b-62ddc47b2928 | -11.12074 | -48.42596 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 703a593b-e478-3d1e-b7f3-fa3fecf2f274 | -11.34905 | -46.56139 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f028aaa9-3532-320d-bdc2-93154dbf27c2 | -7.27665 | -44.56515 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3330f7a6-0ff7-31f2-8642-97c20d6e3f63 | -8.57634 | -48.9501 | 2025-09-10 04:42:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de678842-2c46-3577-9f3b-e0e39f150173 | -11.42577 | -43.57992 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce828cc9-6124-30d8-956f-e71cfc51849e | -7.25179 | -44.45598 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bb83321-da5d-3d0e-afb7-c14c06487147 | -7.75109 | -50.7283 | 2025-09-10 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bca33e1-6917-3d19-8585-67798b10f03f | -8.41226 | -49.09888 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04bd9414-227e-363b-b6f4-9a1b4edaba42 | -8.43006 | -49.1088 | 2025-09-10 04:42:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef06465b-c57c-37bb-8a27-d9cd35acb2cf | -12.14637 | -44.84628 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1adf2386-edc8-3bcd-9d33-8e8f28cfd4f0 | -7.84716 | -46.01416 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d83eb57-939d-3fb7-896e-a2adf3fed2c4 | -7.98242 | -46.32758 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b8c0181-069b-3ee9-9ec5-75a24a539ab7 | -9.07689 | -46.97449 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61bc6dbf-cb02-3965-8e54-c89d555c8cc9 | -7.8662 | -46.04019 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc13c531-731a-34fb-9c52-01bba3566f3e | -8.85896 | -47.23494 | 2025-09-10 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c09831b8-43c6-32f3-a51b-069557b01b69 | -10.00676 | -51.70599 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d2090d1-6317-3659-964e-253017886eae | -9.70051 | -46.8581 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75d6a09d-b684-35e0-b975-3d07e60e329a | -9.31463 | -46.72171 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 09d982ce-9dfe-3d66-9584-5a9e047049a6 | -5.66157 | -51.63594 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1821abc-f4ec-3013-b052-3c9cbeff152f | -9.07645 | -45.71015 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3a3be40-aeb9-3634-bdea-d65136f5ebde | -9.8271 | -46.05674 | 2025-09-10 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0f514b5-87b7-3065-b43b-6780665845e2 | -10.01652 | -51.68876 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 12ca1f89-888d-325c-a7a5-15bcb7e9d6ed | -10.52006 | -49.79962 | 2025-09-10 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 387de366-a311-30e4-a647-a53472d1f362 | -10.31387 | -48.80899 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35ba1080-7de5-3081-9bf8-49b5241965da | -11.11292 | -48.41723 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b0f82ca-d5c8-3d03-8e64-4f18d077bf08 | -9.75455 | -45.39968 | 2025-09-10 04:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |


[Clique aqui para ver as próximas entradas](README58.md)
