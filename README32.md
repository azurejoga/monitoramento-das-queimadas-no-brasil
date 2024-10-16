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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48f35018-65ab-3122-95f5-714a5e2e3364 | -5.05605 | -45.58183 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 631591cc-f1fb-3f7d-808a-61e84d13420f | -5.05525 | -45.58678 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1de7339-9be0-3cc5-ba59-1ee89f4849b9 | -5.04977 | -45.35111 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b349b59-04ec-3169-bd33-d6901933519b | -4.90388 | -45.96196 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a24cbac-222f-3666-91e6-7094ec3899b6 | -4.9033 | -45.96542 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98dc8ada-5a30-3647-82a6-61bbe5aad19d | -4.90244 | -45.96436 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc7a29ac-affa-3779-9e88-acc96c09369e | -4.90188 | -45.96783 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f853279b-fabf-37ef-ada3-38e55f59413f | -4.89929 | -45.96468 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1389c059-4b96-3d02-ba97-1918670e96ec | -4.84508 | -45.98703 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e6ad209-2259-3560-8f6c-370a0d92ae83 | -4.81756 | -45.9785 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2f57410-2b90-3690-9369-c9756b915193 | -4.73451 | -45.66485 | 2024-10-16 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1cdfe51-7ee9-31f1-ac52-532dde67d033 | -4.73056 | -45.66417 | 2024-10-16 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d332ac4-dcb9-349e-a3cf-bd6345f6cbf3 | -4.68702 | -45.7826 | 2024-10-16 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9a19650c-89ee-30e9-9f63-c5fce3f858e8 | -4.68304 | -45.78197 | 2024-10-16 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 851c73eb-eb5c-3321-af12-24944b3fd8ac | -4.51727 | -45.42208 | 2024-10-16 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54c1de7a-3c03-3cba-b83a-8e3198c2971c | -4.51337 | -45.42139 | 2024-10-16 04:06:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 467bf547-66aa-355a-bbd2-89304c9aea88 | -4.41943 | -46.02326 | 2024-10-16 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dcf8d84-365a-3f45-a3f1-6958841bd618 | -4.41886 | -46.02672 | 2024-10-16 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 622e847d-c05f-3c21-9738-e3b01990b5e1 | -4.4148 | -46.02605 | 2024-10-16 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3187eb0-c72d-344a-8f40-bfe79a6e6a88 | -4.38384 | -45.78797 | 2024-10-16 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c37f3d60-ded8-3a65-8f4b-e5d05fe40248 | -4.38296 | -45.79321 | 2024-10-16 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2bb76008-a13f-3be7-bc73-3aa7119cc3e3 | -4.38255 | -45.78986 | 2024-10-16 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 485da16a-da11-3ae7-8329-27744515de59 | -4.37985 | -45.78728 | 2024-10-16 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1e606311-ab98-3159-8cb2-ee3f1f24d30f | -4.37896 | -45.79256 | 2024-10-16 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 461f5d8e-a9d6-3290-aa8e-2939da5567af | -4.37855 | -45.78918 | 2024-10-16 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8c093e9a-0c5d-3bea-961b-e98b737f34ac | -4.32853 | -45.32702 | 2024-10-16 04:06:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60955992-8550-3f32-bbba-dafab183dde6 | -4.14205 | -45.36809 | 2024-10-16 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 364d59ee-f2e4-32d8-bdaf-4f7d43a8266e | -4.14153 | -45.37007 | 2024-10-16 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5bee566-82b1-3a38-b942-bd249b1f20d8 | -4.14127 | -45.373 | 2024-10-16 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c073f795-3555-3e47-95bd-e0d1fae3df12 | -4.13736 | -45.37234 | 2024-10-16 04:06:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b22e82c3-1cdc-3d1e-88cb-b9eefa2899d0 | -5.64125 | -44.97151 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca552cca-330c-3243-b0f5-21a0adc91792 | -5.36712 | -44.94637 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6b69e4c-3b66-30c7-8b5d-5ced7d4b1ef4 | -6.52326 | -45.64551 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a9aee7ce-115e-3c96-88aa-054bccd8ee1d | -6.51942 | -45.64483 | 2024-10-16 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71619223-7c7d-3c0b-9a6d-c10d75871013 | -6.46102 | -45.99647 | 2024-10-16 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a69cdbc6-6774-34b9-a9ae-76ca806a7036 | -6.44832 | -45.85609 | 2024-10-16 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 26800e79-fecf-3b3a-a7c1-bb22488a88c6 | -6.44441 | -45.85551 | 2024-10-16 04:06:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08c88930-130a-30cb-ab26-b394d02b25fd | -6.25362 | -45.87009 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18f0e880-87db-3e78-888b-036222b2f3d3 | -6.25054 | -45.86448 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51ae7ae-733c-3151-b9d4-74f8f94f5574 | -6.24971 | -45.86944 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fd87a2a9-8a43-36a6-b97b-10636ccd1e95 | -6.22517 | -45.89579 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0db6db1f-9e67-32c0-aac0-540dd71e3c3e | -6.20442 | -45.586 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0226302-0298-3533-92e8-a3370a9affa7 | -6.20209 | -45.60007 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 09321a42-2009-3e48-9399-55008a62544a | -6.20057 | -45.58535 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 702e2543-349b-3a01-b37d-39931b00e678 | -6.19979 | -45.59005 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f4bee5a-2318-340c-8034-3d233f7c6b96 | -6.19902 | -45.5947 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a4d0e6b7-f242-354e-a48c-74787b645603 | -6.19825 | -45.59939 | 2024-10-16 04:06:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0473fc2b-6d0c-337d-9810-930884223a04 | -6.09141 | -46.09493 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ae55f28-64eb-341f-8da6-4a27fb4122c7 | -6.08744 | -46.09426 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e99cd678-b591-3d42-8d82-2a04ab6a9741 | -6.01684 | -46.41839 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eddd67cd-4ec7-3091-99e2-4413ddd7e321 | -6.01627 | -46.42193 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04ec6d55-6026-3630-86fd-192ee2a8b367 | -6.01613 | -46.41774 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 941bec37-a7e4-3c9e-94a0-bbd7bc13e52c | -6.01552 | -46.42128 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa197dc5-f107-31ae-9699-1923aba7f498 | -5.99077 | -45.73995 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d76f516-2567-3b65-aad0-3e1911e517a3 | -5.98688 | -45.73931 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be1840d4-9bf3-3f58-a6df-08f5ab521e41 | -5.70131 | -45.67548 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2449a9ac-7a6e-32a1-b8f9-0c96fc6e0cf1 | -5.60757 | -45.19934 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 12e5fad4-6fe7-337b-bb0f-24bbf8ad7344 | -5.60681 | -45.20397 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ce540a00-6d22-379a-8fc9-32f4f9fe0d87 | -5.60501 | -46.24445 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a0893b7-de8b-3211-b7be-c1bb4139776b | -5.60378 | -45.1987 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e5e43540-8444-3511-afba-31c3b1d5bb69 | -5.60301 | -45.20334 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bd7d98a-7146-3dbc-a8f6-3407d5c0f2e8 | -5.58066 | -46.31709 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91cd121f-1c3a-369d-859a-9e32f5c92abe | -5.55992 | -46.29088 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d924c674-870f-38f7-a516-c4620da8276f | -5.51809 | -45.39853 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b8f1969-475a-33e5-aba7-1f530047b757 | -5.51425 | -45.3979 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a077e56-6e56-3eb6-b5da-33a1b1c27a3e | -5.49378 | -46.43605 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d88059d9-5602-36e7-9344-d6fb527adfc1 | -5.49316 | -46.4397 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49811a3a-eda7-311e-9835-d1af42545232 | -5.47989 | -46.37425 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2daea031-61f9-335d-8234-bd2a296681c6 | -5.47905 | -46.37375 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37888977-77b9-3edb-827b-c0ca1354e70c | -5.44974 | -45.88261 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43b707d7-2915-3c27-943e-5cf53b0a6d41 | -5.42226 | -45.47583 | 2024-10-16 04:06:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6702cfaa-3e9e-3c21-9e53-6dabcb54236a | -5.41021 | -46.41418 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eed5915-0ce6-32d1-b3bd-a9cfc0677c1c | -5.40725 | -46.00583 | 2024-10-16 04:06:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a7e604fc-b08d-3162-beaa-6a395bfc41d9 | -5.30443 | -45.40676 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457f2023-bc6e-34b7-a957-9241c731030d | -5.30364 | -45.41167 | 2024-10-16 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c2b0c0d-0bbc-3b75-8c26-074fbdc6a1e7 | -5.28378 | -46.3494 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9445afc-e43b-3965-afa2-87dbdd452061 | -5.2797 | -46.34867 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4bd6a03b-b461-3788-9495-3c304c726a76 | -5.27911 | -46.35217 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9088f74e-9d9e-3227-8f19-0236e9767325 | -5.27321 | -46.3622 | 2024-10-16 04:06:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93d3ade4-56c4-30d8-af05-b5c3bd453a89 | -5.22894 | -46.15459 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4c645eba-3f25-38db-bcc8-7ba45b5a5ecd | -5.19604 | -45.5578 | 2024-10-16 04:06:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76b5e0cb-9798-3d52-99aa-054bceb1af80 | -5.17267 | -45.72183 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76184e4-8616-3bfb-bf92-5f49d9478210 | -5.16873 | -45.72119 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e772684-5075-3c6c-bb9c-1de7e8d94df0 | -5.14128 | -45.77194 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45089206-c524-3908-8e37-6a308ef9c2d8 | -5.13963 | -45.77376 | 2024-10-16 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a72f37d-d220-3f2e-9074-382369c06af2 | -5.095 | -45.83136 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d4f3af33-3c90-3152-b599-5fd8b5652be4 | -5.09103 | -45.8307 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e222398-c2e8-3955-8e21-1ed9e7642de7 | -5.05026 | -46.0788 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0aff18d3-5a34-3988-b2e6-0679379b06cb | -5.04967 | -46.08239 | 2024-10-16 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 35de6a4e-624a-3f8a-8ec9-f183a738f16c | -7.84784 | -46.90366 | 2024-10-16 04:06:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91a611c5-f468-3c80-9258-d06e4b0a089c | -7.60725 | -46.80016 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b83e73a8-73d8-3cb7-861d-59be7c0df9f7 | -7.60517 | -46.83699 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8946600-1b1a-3ee3-a378-ad059e404215 | -7.60455 | -46.84061 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5435634-6690-31dd-9087-8443f29f3568 | -7.6038 | -46.79588 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c92b8f7-748e-352b-99af-0cc72841de41 | -7.60319 | -46.79948 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79c9107e-9f66-3265-827c-e03d23ec0d56 | -7.59912 | -46.79879 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45dca0a2-b0f9-3f0c-8337-b3eca65c528e | -7.50548 | -46.85995 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 579507f5-9ec5-3171-aa09-5432a3f423fe | -7.50486 | -46.86363 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00872fc5-a839-3765-9cbb-0d319944f391 | -7.44461 | -46.77964 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76474e3f-ed12-3c32-ab40-3634d9972fda | -7.38322 | -46.74671 | 2024-10-16 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
