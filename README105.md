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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55cdbc10-ad02-3f53-a41b-5dabd562b8a0 | -5.03679 | -56.12008 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bc01688-0825-3a9c-bece-6798f372f777 | -5.03633 | -56.12328 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1d6bee1-562b-3780-a7ee-31de32d1774d | -4.83758 | -56.20456 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8f70738-75da-3157-9968-f47dd6962eba | -4.8324 | -56.20385 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6008fa6-5ca2-3929-a18a-3e32553856db | -4.78713 | -55.89271 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0722e48-1bd4-3931-821a-feb6757cecc7 | -4.7247 | -56.13917 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97dfeb8-5adf-3f0a-8955-093eea792ba0 | -4.72426 | -56.14219 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b592d4e3-9ad5-3864-8352-c7c69753762d | -4.71949 | -56.13853 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff323f9f-1aae-3508-b477-3a49582212fc | -4.65921 | -56.10791 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70f618e7-120e-39f9-ad7b-20787bf61bf7 | -4.64551 | -56.01947 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68354ab2-3ced-3209-b04d-5437ee03e6b1 | -4.53474 | -56.12203 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cadca80-ed03-3dd0-bfe0-175406802d56 | -4.53421 | -56.12564 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| affee1a8-a257-3fc3-acb8-070798d31a30 | -4.52961 | -56.12092 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d6fa7f8-b742-34a7-b3b5-645d2dfb15c5 | -4.52912 | -56.12428 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edce7cf2-95fa-3e3d-b7cc-843f4faec776 | -4.47135 | -55.71043 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c415153b-d446-3b7a-8cdb-4772d75430e0 | -4.47089 | -55.71359 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81dec6e1-aac4-3d51-9a30-44db1ea247fd | -3.99532 | -56.08281 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0e5e8a9-c797-3739-8e65-39086632819f | -3.99017 | -56.082 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdd83715-f93a-375b-83f2-b2557faec109 | -5.01172 | -57.01001 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cf74030-8e6f-3f98-aedc-e3fd62219faf | -5.01096 | -57.01532 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71323879-bc66-3773-b064-cbc6f544d064 | -5.28302 | -55.96497 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e33cade7-3d13-3b73-b322-e985973c55d2 | -5.27519 | -56.01997 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e08cc2e3-1dd2-33d2-8a26-6866c5efb627 | -5.27475 | -56.02312 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6ca7a9f-1a54-3da0-9488-f69777a21422 | -5.25224 | -55.96561 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 103170c1-3b96-3f77-bd3e-608e81b63692 | -5.25176 | -55.96883 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3878c037-69e8-3e99-8991-ab2704147045 | -5.18262 | -55.99903 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 561bd79d-f1e4-38b4-8823-52a5bc67166b | -5.18218 | -56.00215 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30207a00-42d0-3e49-8406-a9c50be5e9d8 | -5.17731 | -55.99852 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d08a608f-91d4-3fb1-9608-a14a11c620e4 | -5.1123 | -56.23058 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d478f3-0dab-34ae-9682-5fe620a19f17 | -5.10712 | -56.22979 | 2024-10-11 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19187f06-e98f-334f-a2cb-3c5249d18582 | -6.56006 | -56.01964 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb16878a-f316-3fd6-94b2-eba9b8b57430 | -6.55959 | -56.02303 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d5c9ab8-d314-37e6-991d-dcae9fcd9159 | -6.55419 | -56.0224 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 341b6906-5c0d-3fbc-9bb1-f9361ed5a39c | -6.55372 | -56.02581 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9311d375-e1b1-3793-93c7-9cce52e9d53e | -6.54928 | -56.01827 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 979ce4a2-5aea-30e4-b3e0-49555ae2f82c | -6.54882 | -56.02164 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6e1f70a-f163-3792-80ab-99870b9042d7 | -6.48333 | -56.0442 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27472d5b-a9a6-3df7-8b91-5b3956590551 | -6.47751 | -56.04674 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e96d2bc4-40ba-351b-bd53-8f89b9afbc39 | -6.47703 | -56.05013 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55d1343d-e691-3ec2-9ef9-411d30018eb8 | -6.47654 | -56.05355 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca143809-6bc2-3bd3-9cc1-e85eceb8b164 | -6.47587 | -56.01951 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8f80036-b446-34c1-926d-d6414601af7b | -6.47538 | -56.023 | 2024-10-11 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4370564c-14e3-30b4-b746-d5d21e5fa001 | -2.68177 | -57.93826 | 2024-10-11 05:40:00 | NPP-375D | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8db7d797-82a2-304c-ac65-dabcbad06d3e | -2.38656 | -57.15913 | 2024-10-11 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aeb80f47-ee68-356a-8794-557aa7b4c817 | -2.38437 | -57.1604 | 2024-10-11 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| baadc2b6-f05e-30b9-b2c2-401996e6e5cd | -2.3819 | -57.15839 | 2024-10-11 05:40:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9911bdb-ff44-3485-aa21-95f169d3d452 | -3.79793 | -58.34926 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b840b71-8541-304f-b438-5f297ca2f565 | -3.79353 | -58.34861 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 583fd703-6609-31d0-b7d6-9ca9fddda707 | -6.34932 | -58.17543 | 2024-10-11 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3df98f74-b912-3039-aa17-3cb4f7ce3170 | -6.34864 | -58.1802 | 2024-10-11 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 355b1bf0-b4d8-3675-b2d5-b035151c12b8 | -5.95953 | -57.69389 | 2024-10-11 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29e82724-a832-3e0a-9d9a-60f25e83d8fd | -5.84058 | -57.71302 | 2024-10-11 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1e65be5-a9cd-360e-a8c6-f3e0bda5f106 | -5.83989 | -57.71519 | 2024-10-11 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b048e71-f4fc-3871-8e1e-0fdcdcafe449 | -5.83988 | -57.71804 | 2024-10-11 05:40:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 416387ec-3d65-309d-8316-40143873322b | -6.89131 | -59.04561 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b84f232c-608a-3def-a1e5-d1622e12b8e9 | -6.88995 | -59.02395 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1797372-7ebf-388e-99a2-8d33e2d2eb76 | -6.88935 | -59.02812 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 722cf4d7-84ef-3a63-9e84-6d7b22ec70b6 | -6.85837 | -59.08827 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1ce1d77-171a-3ca7-bd49-20af2ec971ec | -6.85777 | -59.09246 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d9da054-7507-39c3-9e4b-d570f727b12c | -6.85341 | -59.09179 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2559f489-41df-3bbf-b9c8-8b1e17271965 | -6.83035 | -59.09713 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aeb0e8c-ff13-3228-b3fe-68242db3c51f | -6.81618 | -59.03686 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 002b9eae-4060-36f0-83eb-b6c2c1a5c21e | -6.81557 | -59.04099 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85bc1730-5587-327b-a878-2bae571259dd | -6.75877 | -59.06274 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 969b9319-5418-3837-abcc-81e067ace484 | -6.75788 | -58.91103 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2918f610-752f-3709-ac03-dee175cdcb8c | -6.7544 | -59.06209 | 2024-10-11 05:40:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 224df061-9bdc-3062-a6a8-c84527d71128 | -3.43241 | -59.63117 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5a17c52-9d0b-34e3-9e0a-9a5e8ccb4d52 | -3.41511 | -59.74669 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27f7db7d-6103-39a7-b518-39e23abc35ab | -3.40716 | -59.74548 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89c227ee-71fe-3516-8673-4a3f97f37d60 | -3.63906 | -58.62631 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 485417c3-49ef-35a8-bc02-404a5e54d29f | -3.63845 | -58.63035 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c75c81-9893-394c-bbf5-f23a6833cac0 | -3.63539 | -58.62156 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61a94191-0d1e-3332-920e-b02b21d104b1 | -3.63477 | -58.62564 | 2024-10-11 05:40:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3fe4e8f-f95c-3d34-80fe-fe443a881464 | -3.54441 | -58.68725 | 2024-10-11 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4a3e41e-275f-3b17-9a3f-4ee530ba6f56 | -3.53913 | -59.4719 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f3b8fc3-015f-3835-843a-b0bd1d7bfa04 | -3.53858 | -59.47545 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00a6e526-712d-3ff3-968f-8e6269ceb80e | -3.53453 | -59.47484 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ee51ecd-b900-3650-9f64-4b6cdc847617 | -3.53398 | -59.47839 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98a7325a-89de-3a3a-aab5-b85d37f0695e | -3.48054 | -59.50285 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd90170d-afbc-33b0-bbf1-21525c3c9b0f | -3.47703 | -59.49873 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ccbdf33-45fa-3d45-a4e7-8bf6c54749d2 | -3.47649 | -59.50226 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7511a39-91f8-35a8-bb06-b59cbcafde23 | -3.47596 | -59.50578 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2c5663d3-289c-36d4-a98d-33f735b607a5 | -3.4284 | -59.63058 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c11ed0e1-30e5-32d0-bef9-58f120c8e58b | -3.35266 | -59.50183 | 2024-10-11 05:40:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f86a8d5-c3f7-32c1-9446-d493aa1a265f | -3.08707 | -59.30991 | 2024-10-11 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ecb40924-0ab9-3119-9cdf-37939cc3b70b | -3.01573 | -59.09998 | 2024-10-11 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3310979-e0a6-3b7d-b4f1-050579697d9e | -3.01048 | -59.10672 | 2024-10-11 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56b3fd79-6cc2-3562-b80e-3b2fa1b2ddec | -3.00993 | -59.11035 | 2024-10-11 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a72d387d-420d-3679-a651-37d83ab3250f | -2.62886 | -59.37841 | 2024-10-11 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 842cea86-7afc-3f1e-8fcb-a144d5c45bfd | -2.58794 | -59.40421 | 2024-10-11 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7f79daf-aac3-3225-845c-7ea1c0da6bc7 | -2.58722 | -59.40446 | 2024-10-11 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4010c27-4d85-33eb-9d72-4d6d795af0c0 | -2.50631 | -59.53038 | 2024-10-11 05:40:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f26869a2-3120-3cc1-984d-79060c492558 | -4.41147 | -59.59361 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7932b43-9cfd-3736-8496-21cd76f27351 | -4.34693 | -59.77213 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca4943f3-9f68-3b7b-ad21-8ce63b5dd3f3 | -4.28577 | -60.01245 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b327d66f-d7f6-3606-8d27-994997c6dd38 | -4.25957 | -59.99821 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06f5a76e-00f4-35ee-82a9-03269561ceb4 | -4.25561 | -59.99761 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62aa59f6-9634-332c-9956-3e023eb22746 | -4.25241 | -59.99195 | 2024-10-11 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac08d115-d5bf-3b11-b530-5bd4f45f563d | -4.23551 | -59.85897 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d01b63f1-1cf8-399b-8597-fc9b267e10e2 | -4.23448 | -59.8574 | 2024-10-11 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README106.md)
