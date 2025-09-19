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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8006cacf-12e1-3ad0-be1a-d8d1edb18e97 | -12.1564 | -44.94948 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 67eea31d-8f7e-36fd-8eae-a16e45415565 | -10.04548 | -49.19861 | 2025-09-19 04:46:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03fc9ed3-20d5-3c49-87b5-a277099817fa | -10.92096 | -45.6454 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 859c905e-b8d0-30e4-829a-e81f625c69fa | -10.37171 | -42.46059 | 2025-09-19 04:46:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 198c72bb-a138-33f7-87c9-c24ec3519b3b | -5.47574 | -46.69184 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3f51f2c-973a-317e-b757-314af5a24720 | -5.4726 | -46.68646 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe28d5e9-8984-3b23-bee5-73ccdd8c2f8f | -6.51693 | -51.20673 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a37abd0d-e7e9-3544-8759-e42562482110 | -12.09608 | -44.84886 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 46f565bb-7618-3f6b-8f43-1c279e8fb289 | -7.57298 | -44.49413 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 086f2e8a-3ad1-37ea-af2b-0f2d52a1d875 | -5.76056 | -43.3866 | 2025-09-19 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ca6f7ba-3d09-32de-ac94-4b667bcf5b8e | -5.99544 | -46.64066 | 2025-09-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c48c8671-518e-3efc-8886-546fbba56e0c | -5.46945 | -47.45175 | 2025-09-19 04:46:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 602d4797-1cde-3af7-9187-93992ea152d9 | -6.37923 | -43.33942 | 2025-09-19 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 47aab758-0561-3e2d-9bf1-abaee0eb290a | -5.63566 | -50.02901 | 2025-09-19 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61903e14-7918-34df-9fba-e26fc4d997d0 | -8.14168 | -46.78154 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f50f7408-e5cb-353a-883d-1afac8fee34f | -8.01974 | -45.73965 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf9a8bf6-cc20-3fab-ba27-cce558a1047a | -8.0515 | -45.72844 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12539a5d-fcff-3248-bcff-155f502f1479 | -10.96357 | -49.57357 | 2025-09-19 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d27a2690-b154-3f42-9f44-ae63f4ada9c9 | -12.14712 | -44.94674 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a4f48ecd-9e47-3a9d-a56d-f98c509bbd48 | -9.32681 | -48.94518 | 2025-09-19 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b197d608-a8d4-3049-88ff-0312fee268df | -6.12695 | -43.94821 | 2025-09-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc249faa-93e2-3033-8e4a-7ed9db75f571 | -7.45894 | -46.37816 | 2025-09-19 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5293d927-9802-3d60-96a9-6b66ed5a09fc | -11.21775 | -49.63826 | 2025-09-19 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47e60a85-ac15-3878-aa98-d20b42f83148 | -11.18555 | -45.36108 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4188688f-5a06-3527-bf0c-ef22a4c5fc1d | -10.29017 | -50.23743 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| d314884e-38cd-3221-a728-1ec3e2c1730e | -8.0247 | -45.70405 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd0282e8-0732-39c0-864a-3af54c2850ce | -7.57084 | -45.49306 | 2025-09-19 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a3b1a20-f5b6-3bbe-a8df-500342504318 | -5.63124 | -51.08386 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78651bd6-f4c6-3ae6-8ca3-5b28f35ff860 | -5.77756 | -45.9753 | 2025-09-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ed213693-1b1c-3e9d-be0f-5708a18d8ed3 | -12.10093 | -44.8144 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3a87f96-45ba-3877-b30a-8a8b41881c1a | -8.04362 | -45.7231 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 893b626f-cdac-3e52-9d28-b2b09ef5002f | -9.17393 | -45.32154 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c58a580b-3e50-3926-a200-e94c21cca7c4 | -10.28621 | -50.24062 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4b03557-b919-3c46-90a0-bfcb0eeac774 | -8.15034 | -46.77743 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fc4c257-36c5-37a2-9bcb-5721086993d9 | -5.79567 | -43.90364 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36e4f512-2ade-3351-b511-b7197657e804 | -6.2623 | -43.91999 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| a2b3ed73-54fc-3317-bf6a-2e88eaafb463 | -7.62017 | -44.45741 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d31d2d45-a168-3557-806a-75dea56d8da9 | -5.12786 | -47.83189 | 2025-09-19 04:46:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e047a411-ec1a-3b43-adf4-e4f94589f9d1 | -5.7924 | -45.35593 | 2025-09-19 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c9c5146-74ad-3481-b8d7-6ea808770d98 | -12.10216 | -44.80455 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 122ae0c4-d8aa-3966-b644-7720fa5c88ff | -7.45186 | -46.14283 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 570d14ef-fde9-31a2-809e-9b788af5597f | -6.82069 | -47.84964 | 2025-09-19 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3051ddb1-83f6-32a3-a166-2ffcf69c6258 | -8.15356 | -46.78302 | 2025-09-19 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5989ae0-46a2-32fc-844c-53c0302c1059 | -6.95361 | -42.44078 | 2025-09-19 04:46:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3bfba471-888e-3d44-ad6b-13368b0be0a2 | -8.97896 | -46.22528 | 2025-09-19 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 109ae554-3f26-39b8-809e-26b11c439d3a | -8.21845 | -45.80179 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b7c53bd8-bc6f-3e2a-a936-64a475cbcf10 | -7.52728 | -47.67551 | 2025-09-19 04:46:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 04b61ba2-0651-30c8-89c2-d3a5f1acd26f | -6.73017 | -47.27366 | 2025-09-19 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1ef2b47-f0a8-346e-a2dc-c81cff87dd9d | -11.18491 | -45.36572 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ae54abd-d20f-3e62-9218-2e75f8b1f100 | -8.63697 | -45.71373 | 2025-09-19 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b9ace69-720e-3903-92cc-442dd8ae8ce3 | -8.02417 | -45.70792 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2efbf1d2-fca0-3b51-bae8-063097589310 | -9.17012 | -45.31649 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e0e6692-eb75-3cbf-9603-5df74df3001b | -5.30024 | -54.45857 | 2025-09-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09f918e4-6eee-3d8e-9580-833e1448e442 | -12.73693 | -47.7439 | 2025-09-19 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b5ddd7a4-cd75-335a-a5c4-595bae87f20b | -12.24975 | -49.16464 | 2025-09-19 04:46:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b085b0b3-6afb-35e8-a263-09337c3171b3 | -7.83997 | -45.63555 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd2b8be8-ccbd-32bf-b46e-84839c4ecfa0 | -7.00041 | -44.63504 | 2025-09-19 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34411c2d-e026-3a34-bc2b-26f6f8f85b64 | -6.51249 | -51.19192 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05045120-4471-321c-a334-9f709eddead4 | -11.54754 | -50.54864 | 2025-09-19 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fc52252-827c-3231-bc7f-78883140d458 | -7.3623 | -44.59146 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f93757c6-234c-341b-ae39-0a8374d66921 | -12.09533 | -44.81758 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d10b3ee-e585-3769-84c8-f5025c8f4085 | -12.09266 | -44.83792 | 2025-09-19 04:46:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52a8b5bd-5c8c-398b-b756-12864e0be2a2 | -6.90121 | -44.76775 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1bd8e8a8-5b9b-31ca-aba9-c34b601f5e75 | -6.5896 | -45.58038 | 2025-09-19 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a91ce7-7798-3328-8319-7f033d98dbbe | -12.0067 | -46.72943 | 2025-09-19 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a43c6ea-e937-38d5-80fe-04f7b1e79dc8 | -10.37218 | -42.457 | 2025-09-19 04:46:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c468bf5e-d04d-3054-9f3c-70f50e643838 | -7.70232 | -44.47264 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0603290-7a00-3853-83c1-ebe97802bc80 | -8.37665 | -44.67897 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 69f76de9-b246-3e8f-a65f-fa69dbdf0866 | -10.92021 | -45.65695 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c654893c-e0db-312a-ada6-60e186af7640 | -5.97589 | -43.79647 | 2025-09-19 04:46:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ad95077-fbca-3f10-9cde-68afc967fdb5 | -11.09465 | -41.06947 | 2025-09-19 04:46:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ca61dd07-d4c3-3244-8db7-02c998e04b52 | -8.03351 | -45.73365 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| add7b012-7785-350a-babc-347e4482dd93 | -8.62021 | -45.32981 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27ff34d9-daae-35dd-9a0b-4b24c561ecef | -12.15051 | -44.95781 | 2025-09-19 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b43462b9-1279-304e-9925-471ce32f8664 | -5.63277 | -51.94012 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da5d5e6e-27b1-3812-87a9-88719b8ee3ce | -6.83393 | -41.03858 | 2025-09-19 04:46:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b0c2dbbb-73ed-3859-af0b-e099d366c8a2 | -6.20155 | -43.92455 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 45c931a2-5e7d-330c-b13f-c2f96b22588e | -6.20928 | -45.10393 | 2025-09-19 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e1efda4-a5ad-36de-b631-888e4fa379ae | -5.47008 | -46.6844 | 2025-09-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cdf23c94-c518-31dd-90b4-0bb4c2bf9829 | -7.84103 | -46.21297 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 07a021c1-2315-3b2d-8be0-4c7cd6455302 | -8.02837 | -45.70875 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59daddc7-51cf-34f2-b1c3-d7a22dddb7f0 | -7.61181 | -45.26934 | 2025-09-19 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34e066f-ef3e-3916-b865-a09f96adc241 | -8.33343 | -44.71588 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 156d7d60-378d-3f1b-946e-3171dcd72b8a | -8.48641 | -44.73131 | 2025-09-19 04:46:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 076ec271-df99-3617-8001-f6ef134f422b | -6.9311 | -44.90415 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b605dadd-f2d6-358a-83ad-8745cfbd9ad4 | -11.17279 | -45.36193 | 2025-09-19 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5030d627-c157-3098-8a6b-cfd6a2f97315 | -7.63947 | -44.45355 | 2025-09-19 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d4aa0ce-2b0f-3e61-8551-b49f05d86e68 | -10.29523 | -50.22683 | 2025-09-19 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e47ae99e-6304-3998-b0b4-55edbea574db | -6.91407 | -44.80426 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7b1023f5-40d0-3a77-9c81-e04fe73ebb4a | -9.18719 | -45.32347 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0b4cc42-997f-3f22-afb5-86179138f00d | -8.68861 | -46.45351 | 2025-09-19 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15cbd141-f557-32ff-9ba2-39726612150a | -8.03572 | -45.71794 | 2025-09-19 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8d247ba0-7f0e-304b-8f58-3d25e2239c84 | -6.11686 | -47.40489 | 2025-09-19 04:46:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e4f74d5-84da-3f2a-a3d9-93f5ce31969a | -6.25901 | -43.90961 | 2025-09-19 04:46:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9020440d-6ef2-33b7-9fc9-eb09b84542c5 | -6.75952 | -46.01046 | 2025-09-19 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7ef0ec9b-355b-3bc0-8eee-bd13ce04a3ca | -5.54567 | -51.37048 | 2025-09-19 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5604e40c-6d69-3595-a179-4a9b7922e1b4 | -7.28859 | -43.92756 | 2025-09-19 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1e43fe24-3110-348b-860a-e57f7993b740 | -6.81768 | -47.8449 | 2025-09-19 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8a0a2cc-2aba-350f-aafd-fbef30b36347 | -9.17513 | -45.31275 | 2025-09-19 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c5423a2-a761-3199-9e1b-c4df1dbea0c0 | -7.04692 | -46.41805 | 2025-09-19 04:46:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README26.md)
