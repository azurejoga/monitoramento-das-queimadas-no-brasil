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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75eab107-aa5d-3c96-90e5-583687030cf0 | -14.1828 | -52.8878 | 2026-08-18 06:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 54c0e2c4-7077-347e-99f7-712bb1307e05 | -6.7478 | -59.1716 | 2026-08-18 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| afc9942b-f509-39c1-9772-8d06563d64f8 | -14.8233 | -46.619 | 2026-08-18 06:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 731a823a-9f46-3d0f-a712-1bc71a784690 | -14.1821 | -52.93 | 2026-08-18 06:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| bdffdb73-c0ec-306a-9cf9-c1341f961277 | -14.2017 | -52.9065 | 2026-08-18 06:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| c39eee85-af19-3bc7-9f33-4b806bd7760d | -14.1824 | -52.9089 | 2026-08-18 06:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 234.0 |
| 6c6c7eed-6cee-3b24-ba22-86e6c5716f5e | -14.8228 | -46.6419 | 2026-08-18 06:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 2db18c31-05ed-3bf6-8d88-405c61d62c13 | -14.2014 | -52.9276 | 2026-08-18 06:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1fbfbf57-6b67-388c-92ce-c5f5a36c332b | -14.8233 | -46.619 | 2026-08-18 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 70.7 |
| c50cd180-b859-3c5b-84d4-d3ca2dedc917 | -14.8033 | -46.6453 | 2026-08-18 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ec905bcf-9fac-357d-bae6-921f76f21b21 | -14.1631 | -52.9113 | 2026-08-18 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| bd1b2470-7c69-37a0-b3aa-c415e1bdcfec | -14.8228 | -46.6419 | 2026-08-18 06:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 522c7d47-8f5c-368d-bddc-4b5212ba480f | -6.7478 | -59.1716 | 2026-08-18 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 6b220c9b-7f7c-36db-8bdd-420333285a07 | -14.1821 | -52.93 | 2026-08-18 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 7c21921e-ffcf-3bca-ab51-dd40cdabb3ce | -14.2014 | -52.9276 | 2026-08-18 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 6897b5d6-5200-3edc-b4cd-ccc5da7ad2a4 | -14.2017 | -52.9065 | 2026-08-18 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 05e07adc-33de-3b09-a618-7aaa30612d21 | -14.1824 | -52.9089 | 2026-08-18 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 290.8 |
| a23814a9-6979-3390-af64-5314a86583ca | -14.1828 | -52.8878 | 2026-08-18 06:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 71b7caba-d4db-3c9e-972e-cb4b7136f3f9 | -8.56042 | -54.73056 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 45be0e05-69f3-3ed5-bebb-73fe4613ed51 | -8.36244 | -46.36872 | 2026-08-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 316124f4-f4cc-3dce-822d-0e70a2020860 | -8.59007 | -50.3496 | 2026-08-18 06:46:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2412884d-bb62-34a4-9f19-dbeaae72bccf | -7.24496 | -49.89209 | 2026-08-18 06:46:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dc1afdaf-1901-3aa0-b1b1-fdb6b910e768 | -8.60935 | -50.34315 | 2026-08-18 06:46:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2aac16a9-287b-30b1-8ebb-7589fe7f8991 | -8.31708 | -46.48069 | 2026-08-18 06:46:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b25abfb2-c710-367f-b2fb-0edc421650dc | -7.82089 | -44.59208 | 2026-08-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6c6e6c0e-71e6-33b2-8292-cb8eebb95ed6 | -8.4911 | -48.80776 | 2026-08-18 06:46:00 | AQUA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9cc427b-3f18-39af-9f6f-57682545deb6 | -8.48977 | -48.81657 | 2026-08-18 06:46:00 | AQUA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f81b354d-2e49-37dc-bd37-9decc57f4926 | -6.26164 | -43.27637 | 2026-08-18 06:46:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e512d0ae-3211-3ec9-abee-4c21986f9c54 | -8.20973 | -55.03376 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6a5c4f41-6d0b-36ba-b829-e56d33166d05 | -6.40638 | -54.93877 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 06409dbe-7af1-3284-a5c3-16205fc54132 | -8.2128 | -55.01522 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| ed374a7a-b6a2-358e-829f-70a6b8e43b2e | -8.48844 | -48.82537 | 2026-08-18 06:46:00 | AQUA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 774665ee-3159-3fbb-b167-8c2ccd195ebb | -8.20058 | -55.01294 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| a5a28248-e829-38dc-ac5c-19ac2d43214a | -9.05976 | -50.84083 | 2026-08-18 06:46:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c9624887-bd77-3771-8447-678752c13b45 | -7.81889 | -44.60591 | 2026-08-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| e7b5a15d-c5ab-3aaa-9cbe-59106fc411e6 | -6.84172 | -58.97934 | 2026-08-18 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 465e02fa-8aeb-3f9a-aa1c-c54296715423 | -8.57507 | -54.71563 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 192.0 |
| 1e681970-f5ba-3f21-b0f6-7a5d718f2fc1 | -8.59149 | -50.3404 | 2026-08-18 06:46:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 41fdc321-865a-3e01-9270-fc1fcf199c41 | -3.68315 | -47.65171 | 2026-08-18 06:46:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 15c90790-3ab1-36ae-bfe6-e943adabc48a | -7.23603 | -49.89099 | 2026-08-18 06:46:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| af589b32-86a8-3717-a935-8b218c7e9d72 | -8.36398 | -46.35811 | 2026-08-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 8e895d8e-bae8-3a66-9776-0b69b2b6218f | -4.01057 | -48.90182 | 2026-08-18 06:46:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 2cdb247c-f8e9-3fba-9261-23664387c24b | -6.75192 | -59.15881 | 2026-08-18 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 2c2f41be-6351-35eb-ac07-8f5b40e1373a | -8.176 | -55.00928 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9c14f31c-8cc0-3987-808b-d02cfc144002 | -8.58052 | -54.68203 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 30cb74d3-f2fd-337b-8322-74722f377327 | -6.7372 | -59.16092 | 2026-08-18 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| eedcf829-46b1-3874-bd75-73c5fa3bb3e9 | -7.81277 | -44.59775 | 2026-08-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 51660052-0512-33c0-b211-77e17adf477a | -8.56319 | -54.71363 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| d12b40ea-1262-3bac-b44f-088e903642ad | -8.56596 | -54.69672 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 74c18169-8132-3a2d-b136-13658f5f407d | -4.00922 | -48.91067 | 2026-08-18 06:46:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 3ee17ce8-ca13-3095-b5ed-84a8b75998ac | -7.23746 | -49.88177 | 2026-08-18 06:46:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b792675e-2c70-3b24-8fa9-e89f7b741f7d | -7.45129 | -46.15458 | 2026-08-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a6b412d5-35bb-3246-979a-24afa4861961 | -9.07028 | -50.83283 | 2026-08-18 06:46:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0f4a2dc2-968c-3eb8-938c-c8b6ed499bfc | -6.409 | -54.92657 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| fc95f961-e2e2-342c-9d9c-425991e27ca4 | -9.0627 | -50.822 | 2026-08-18 06:46:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| a9daa07e-95a5-3bf0-8a92-336b0c4373e1 | -7.80816 | -44.60422 | 2026-08-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 93da806b-31bc-388d-afb6-eae3c262bba1 | -8.60042 | -50.34178 | 2026-08-18 06:46:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6d5ff462-0926-399b-9b30-3c8827d75462 | -9.76129 | -46.69976 | 2026-08-18 06:46:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ce879941-db0a-3b09-82f0-0ac0bd47a13c | -8.5723 | -54.73269 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 241.8 |
| cd56eab3-8450-38b1-a461-b38f7f88a0f1 | -8.56332 | -47.39392 | 2026-08-18 06:46:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b97d5914-be59-3843-91d6-ba11c93a6d31 | -7.46089 | -46.1559 | 2026-08-18 06:46:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c25f0d0d-4713-3a60-995b-5881b2dda645 | -8.5778 | -54.69882 | 2026-08-18 06:46:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| a5afee01-b204-3607-953a-17312f8d348a | -7.81089 | -44.61155 | 2026-08-18 06:46:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ff0da142-394d-3a4a-8cf3-811a3711773a | -3.68446 | -47.64297 | 2026-08-18 06:46:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1538a9cf-c222-3e33-8358-7976a9c68c75 | -6.75466 | -59.16333 | 2026-08-18 06:46:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 896756ad-ba26-39a8-b6be-08800ae096bb | -9.06881 | -50.8423 | 2026-08-18 06:46:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| b9efe566-21d2-3005-bc9c-65e8a88052d7 | -8.3266 | -46.48199 | 2026-08-18 06:46:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 75e50bea-df52-3083-9d52-5bc2a248b9d5 | -12.46034 | -54.19403 | 2026-08-18 06:48:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a27fd9ce-51a8-3092-a7c1-0b119f19f188 | -14.17833 | -53.04806 | 2026-08-18 06:48:00 | AQUA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2ff3944f-17fe-3279-af5d-1a6227944cc4 | -15.3853 | -52.79568 | 2026-08-18 06:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 06bd7072-a1c1-32a5-855d-067ebe069a67 | -14.82377 | -46.62938 | 2026-08-18 06:48:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b059ff3e-7c79-3039-905d-20ed9204a5b0 | -12.53842 | -47.85438 | 2026-08-18 06:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0a74bcc5-7642-3f57-8551-f424deea8681 | -14.03579 | -53.66922 | 2026-08-18 06:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6677fd7f-3160-3db6-abd4-1f7575172bad | -14.83228 | -46.64463 | 2026-08-18 06:48:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8bdf26d6-acf9-37d0-8d21-3f83381acdfa | -14.17073 | -52.91499 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 887c33ca-db00-3ef9-ba69-b1c6afd887ed | -14.16304 | -52.90254 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f4dac48e-54b4-3e49-8519-13dbd81cc2f2 | -12.77076 | -48.42779 | 2026-08-18 06:48:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e97cacf9-0c19-33d1-9627-e07dc7489f92 | -8.58179 | -54.7224 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 190.8 |
| fdcd5fc9-2844-3346-bda6-76bdef16acc7 | -13.41497 | -54.37278 | 2026-08-18 06:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 880ca8a4-84c5-385c-957c-2b17d15d1918 | -12.77213 | -48.41833 | 2026-08-18 06:48:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c030e47a-d694-355f-b98e-92ed8b1ad3f1 | -14.18965 | -52.91823 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 22c85ed5-5d3f-3f99-a675-b488ef4ba15e | -14.17247 | -52.90431 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b5cafb69-847c-3469-bf3f-594d9f632e6e | -12.70288 | -48.51403 | 2026-08-18 06:48:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8205dac7-73b1-3ad1-8508-1a16931ad8aa | -12.71599 | -48.48703 | 2026-08-18 06:48:00 | AQUA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3e407a03-7d57-3a61-9153-1afbaad1be58 | -15.38695 | -52.78552 | 2026-08-18 06:48:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 85702a6c-df76-3bf5-b4f3-2b195586cfb3 | -11.09817 | -49.91237 | 2026-08-18 06:48:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 73d09173-88fd-3b2a-89ca-227ab13c1d17 | -14.81181 | -46.64039 | 2026-08-18 06:48:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 538dde7a-33d4-3aa9-9c72-7ee49203fe13 | -14.03379 | -53.68113 | 2026-08-18 06:48:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 23f1e9b1-9931-315e-88c5-553f0659f05d | -9.46488 | -51.61326 | 2026-08-18 06:48:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d7cc908e-219a-316c-a838-024163492f8f | -11.12225 | -47.26471 | 2026-08-18 06:48:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dde9802d-12a2-3e87-8d99-6df172800328 | -8.57566 | -54.68671 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c008ea7a-036a-3acd-a71b-1b53c7f7cd5d | -14.16479 | -52.89186 | 2026-08-18 06:48:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8596ab96-8de9-3665-b28a-13e30075d919 | -8.56703 | -54.73729 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6820b920-aea2-372d-a454-240776f6bc62 | -8.58419 | -54.73472 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 27b85ec6-483a-3a9a-9878-9104b02164dd | -12.54126 | -47.83435 | 2026-08-18 06:48:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5cc3ca1a-bb9d-3b72-a2d7-ee3b20c6e163 | -11.12081 | -47.27468 | 2026-08-18 06:48:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 86c0025c-0bf4-3033-8cea-997ff7b89c72 | -14.81348 | -46.62759 | 2026-08-18 06:48:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 18dc5d84-5656-39f7-a1c1-d3a8d2077917 | -8.56993 | -54.72032 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 193.5 |
| cb7c5a7f-f122-37fe-9235-8fc4238600d8 | -14.24651 | -51.93228 | 2026-08-18 06:48:00 | AQUA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fe381f77-2c2e-3747-b175-4553328203ee | -8.58964 | -54.70092 | 2026-08-18 06:48:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |


[Clique aqui para ver as próximas entradas](README62.md)
