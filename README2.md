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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e938bb12-8d24-3208-9625-5bbac095b9eb | -7.2713 | -45.37 | 2026-08-25 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 2f4cfd08-c318-39c1-b447-d542512747b3 | -8.0883 | -44.6533 | 2026-08-25 00:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5758b284-e057-3025-a924-c1d75191dd06 | -16.3946 | -49.9191 | 2026-08-25 00:10:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 1bd5ac7a-0df6-3c04-b06b-cefdf41f0a24 | -7.5475 | -61.3627 | 2026-08-25 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| f16652cd-a958-3ad7-92e5-4ee452190ebb | -11.4498 | -44.512 | 2026-08-25 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 568b2256-54a6-382e-b047-0b82388fc900 | -7.3103 | -64.7044 | 2026-08-25 00:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 53ba9eb4-1157-3ddb-ad41-11a509a2c4fb | -7.2856 | -44.0875 | 2026-08-25 00:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f7d02a14-aa60-36c9-9055-53ccc7dd7acd | -11.4306 | -44.5148 | 2026-08-25 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 7003e91e-28d0-3d9b-8286-73ac23e58b9f | -7.0057 | -59.2575 | 2026-08-25 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 6941bdde-aec9-36bf-b4f1-65defa10fc01 | -11.1447 | -44.4632 | 2026-08-25 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| dbeef6a7-0933-3f57-b9d0-1b9bcdec929f | -6.6411 | -58.4793 | 2026-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 2f276bcc-8fb7-3c1d-82a2-23eb6dcd11c9 | -6.6226 | -58.4995 | 2026-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 9d1cbc70-dcfc-37f8-a9ff-1d3c3c19a482 | -6.8246 | -58.6655 | 2026-08-25 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| d747462a-28ac-336f-9610-629bdb6be752 | -10.3536 | -45.0561 | 2026-08-25 00:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 57d687be-1ad4-36c6-b286-86a4f0c2b7a3 | -6.1464 | -57.9359 | 2026-08-25 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4dbdb9cc-f3f1-3a2c-a49a-9114599f9341 | -7.2903 | -45.3456 | 2026-08-25 00:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a179214a-4d05-364a-a2ce-05acda058ea3 | -3.5407 | -48.1673 | 2026-08-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| df0a4f81-aeee-3a29-b238-1a13d4753309 | -11.1443 | -44.4865 | 2026-08-25 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 8a88308a-a028-36cc-9b6d-07311ab67496 | -7.529 | -61.3635 | 2026-08-25 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 012b8a6b-ffe0-36c1-9e9e-fdde77c3ee0c | -7.25 | -45.83 | 2026-08-25 00:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4f330c7-39c9-3966-bb31-b8137619a536 | -11.41 | -44.53 | 2026-08-25 00:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 577ad176-9f04-3514-9548-21068f75122e | -7.25 | -45.88 | 2026-08-25 00:15:00 | MSG-03 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3926b1d7-4cc4-38d1-8019-55992fa6b63e | -10.37 | -45.03 | 2026-08-25 00:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9c03ee83-faf1-3944-9abd-23ac1eee5498 | -10.37 | -45.08 | 2026-08-25 00:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 880e85a4-4cbe-39a7-889c-42aa289eeafd | -6.1477 | -57.702 | 2026-08-25 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6e0215b1-ba00-37e3-aa9d-4a4122fbf9df | -7.2471 | -45.8685 | 2026-08-25 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 9688f6e4-1dea-3160-b5be-3399081f1e65 | -10.3723 | -45.0767 | 2026-08-25 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 233.7 |
| eb51a8ab-7045-35ac-bc7a-5d5073210d50 | -10.3918 | -45.0512 | 2026-08-25 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3d7cb1cc-05f4-3a79-bbf0-4e81b0870863 | -6.8007 | -59.6127 | 2026-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 25e6a31c-9239-3ae8-a836-c731fad39b1b | -8.616 | -54.7339 | 2026-08-25 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 28338d58-8336-3d09-801e-592debd5d102 | -7.2903 | -45.3456 | 2026-08-25 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 6d14251b-203e-342b-a883-93baaff26529 | -12.7792 | -44.2812 | 2026-08-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6caa5a2e-3eb6-3ae3-90b8-16a6479e967a | -7.0058 | -59.2382 | 2026-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 2b92f9eb-b09f-3d30-a885-ab5c8e1e90b0 | -11.4302 | -44.5382 | 2026-08-25 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 138a2add-ab0d-39a1-9dcf-468d4e11739f | -6.641 | -58.4987 | 2026-08-25 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 232.9 |
| 375b91f7-ff53-3e6e-a3cc-4cb91cc390bd | -10.3536 | -45.0561 | 2026-08-25 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f6068129-671e-32cc-b7b9-2a80572cd96f | -6.6227 | -58.4801 | 2026-08-25 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 9ede3392-432c-3ddf-9272-79ce2ac1f024 | 2.5983 | -60.697 | 2026-08-25 00:20:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.2 |
| d9106ede-ec76-3b6f-ba55-1bd46f857d7a | -16.3946 | -49.9191 | 2026-08-25 00:20:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 4ae4fd9c-6f2c-3112-98aa-2a2882867366 | -8.5973 | -54.7352 | 2026-08-25 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1c8c1a86-a211-3c22-9e76-1c534c44dde4 | -6.6226 | -58.4995 | 2026-08-25 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 183.3 |
| c2a0f662-d824-35d7-99f6-a2b0f600d190 | -7.2713 | -45.37 | 2026-08-25 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| b8e213a2-4da5-3fec-b651-086f62d0c715 | -7.3103 | -64.7044 | 2026-08-25 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 76829327-4bcd-31f0-8a4e-e95442105136 | -3.5407 | -48.1673 | 2026-08-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 5b196c7f-944c-3d3a-9186-4555d5171693 | -7.3288 | -64.6852 | 2026-08-25 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.3 |
| d3246331-9292-36af-84d3-5e2f8f48ef03 | -11.1443 | -44.4865 | 2026-08-25 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3b758478-987c-3017-9513-5d5b372b3e8e | -7.2858 | -44.0644 | 2026-08-25 00:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 5a516bd0-062e-3fe7-a54a-6ef528c9a7ef | -11.1447 | -44.4632 | 2026-08-25 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| d18c2ad1-c46c-3fb6-b1da-acd50bc1e110 | -7.2525 | -45.3717 | 2026-08-25 00:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| e8d91e4d-34f6-3787-8289-04d227c766a3 | -7.0057 | -59.2575 | 2026-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| f9eba0dd-00fc-3cb7-8473-fe5ee777ff54 | -7.5475 | -61.3627 | 2026-08-25 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| fafaa322-8110-380b-ba79-718a85537f13 | -6.1464 | -57.9359 | 2026-08-25 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 3a014700-98cd-32a7-b00a-5f692024aa52 | -7.2661 | -45.8443 | 2026-08-25 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 252.1 |
| a5e7327a-23bc-3e9f-b2d7-c9b2407b02b3 | -11.4498 | -44.512 | 2026-08-25 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 20790b10-877d-310e-87c7-f743849f3f86 | -3.5221 | -48.1896 | 2026-08-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 9a16cdeb-6999-3fe0-aad9-2a3cd8e00fff | -6.8008 | -59.5934 | 2026-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 3bb23798-6ffd-3d30-ad35-1605211f8a2c | -6.8192 | -59.5927 | 2026-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.6 |
| c110c02e-4994-3b71-8ea1-778b227ab603 | -7.267 | -44.0662 | 2026-08-25 00:20:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| e9ed3638-d159-3a2f-990e-2902640d5efa | -7.4286 | -43.1182 | 2026-08-25 00:20:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 932910a1-525c-3582-99d1-73a1b83a0250 | -7.3104 | -64.6858 | 2026-08-25 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 23293c56-e54d-3683-8923-0cbf7a82a6e7 | -7.2474 | -45.846 | 2026-08-25 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 2350f95d-aec3-31fc-9b59-338222ba26f9 | -7.3287 | -64.7039 | 2026-08-25 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| d7de2ce6-a71a-38ef-b51a-ec7a2bb74f0a | -7.2901 | -45.3683 | 2026-08-25 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| e9a95224-f498-3689-8952-28ebc5a047cf | -3.5222 | -48.168 | 2026-08-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 21b82d23-4595-3884-977f-16a0afb7dc66 | -10.3727 | -45.0537 | 2026-08-25 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 623.2 |
| b3119d73-a35c-3e4a-afdd-bff61a215155 | -10.3731 | -45.0306 | 2026-08-25 00:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 8a194ed6-05d0-335f-b30d-91565ad7740a | -6.6411 | -58.4793 | 2026-08-25 00:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 10a06c01-824c-303d-800d-461f60f1a0e1 | -11.4494 | -44.5353 | 2026-08-25 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 85a01be6-68a2-3b53-93e0-f3a4a3da6e53 | -7.529 | -61.3635 | 2026-08-25 00:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| fd3700e1-519d-3fa2-bdd8-6a4513f8f2ad | -8.0695 | -44.6552 | 2026-08-25 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8606e54e-5298-3bb7-a82b-2b852ebcb71f | -6.8191 | -59.6119 | 2026-08-25 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| dd91a4b7-3ec0-343c-8269-7d38a74ba9a6 | -12.799 | -44.2544 | 2026-08-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 09692ba5-7101-3002-989c-bbb781cfa9a9 | -8.0883 | -44.6533 | 2026-08-25 00:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 1f9b30b6-e986-3998-9028-deb54de6395f | -12.7797 | -44.2576 | 2026-08-25 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 15032e57-5f82-336f-b3de-ddb8aa056be4 | -3.5406 | -48.1889 | 2026-08-25 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 04a1eb37-b4df-31ab-9817-50dd45fcfb48 | -11.4306 | -44.5148 | 2026-08-25 00:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| d0e6ba1f-8d84-32dc-a3d6-76a8ae5bea81 | -7.2659 | -45.8668 | 2026-08-25 00:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 3ee1772f-7f88-3442-a407-6797eeb7bcd4 | -6.8872 | -34.9289 | 2026-08-25 00:20:00 | GOES-19 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 61.7 |
| f5525d82-630d-3a6b-86cc-f47732e9dd64 | -7.2856 | -44.0875 | 2026-08-25 00:20:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e49fb5be-bd9d-3a49-84e4-fc6d56c1c2ca | -7.0058 | -59.2382 | 2026-08-25 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 1976695b-fd5f-35be-b9bc-4c1adee30c64 | -6.6226 | -58.4995 | 2026-08-25 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 179.1 |
| 5246193b-7c21-3805-a8de-97521e654529 | -12.7792 | -44.2812 | 2026-08-25 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 02bdafb1-7cbc-387d-bc2a-7ecfa7f65275 | -6.8192 | -59.5927 | 2026-08-25 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 65d4ef1f-f88f-3923-8b4e-93fbeae0cdc7 | -7.3104 | -64.6858 | 2026-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 86560373-babd-31c9-9b02-793843b2591e | -7.5475 | -61.3627 | 2026-08-25 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f91c01b8-3e39-34ac-baef-b3cfe36b197e | -16.3749 | -49.9223 | 2026-08-25 00:30:00 | GOES-19 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ad993bf4-4f9e-3c40-b312-b2fe2a575009 | -7.4289 | -43.0947 | 2026-08-25 00:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 69.5 |
| df30fa04-c9b1-34de-8120-8f2a96397025 | -6.1477 | -57.702 | 2026-08-25 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| db6a35bb-0eb4-3ad9-826e-bba079713262 | -6.1464 | -57.9359 | 2026-08-25 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e4cebb92-4da2-3c93-bc78-7ea1a6481405 | -6.6227 | -58.4801 | 2026-08-25 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 999ae7f7-fdd8-34bd-8d74-1c4e9047580e | -17.2321 | -40.2701 | 2026-08-25 00:30:00 | GOES-19 | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 109.0 |
| 24622597-f745-3f25-a9cb-0816c248af00 | -7.2901 | -45.3683 | 2026-08-25 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 89d5c62e-981e-361f-b2c2-378a326e2940 | -3.5406 | -48.1889 | 2026-08-25 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 182.0 |
| b00efacd-eadc-3dac-ab4c-2f11af4fb94c | -10.3727 | -45.0537 | 2026-08-25 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 602.3 |
| 3c791498-5d3d-37b8-bc8b-26db72e6c2ed | -6.641 | -58.4987 | 2026-08-25 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 270.3 |
| 3370136d-b58a-383e-9822-debf4d660384 | 2.5983 | -60.697 | 2026-08-25 00:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.5 |
| eb6dba6b-6809-3da1-8231-acac3ee1fd50 | -7.2471 | -45.8685 | 2026-08-25 00:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f66cc689-ea13-3b89-8e90-f3d8b23c401d | -17.2523 | -40.2648 | 2026-08-25 00:30:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 73.8 |
| a7095d4d-8115-32cc-a108-d596a1d91f79 | -10.3918 | -45.0512 | 2026-08-25 00:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 35c78ff1-b0e9-3cd6-8fa3-a66c4ccc7b12 | -7.3288 | -64.6852 | 2026-08-25 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |


[Clique aqui para ver as próximas entradas](README3.md)
