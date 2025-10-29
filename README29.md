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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01a5db9c-3a66-3fd0-8ba5-d0438baa89e9 | -4.64548 | -47.95428 | 2025-10-29 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3d0e04b-a383-3a24-b6cd-6fc3cce6b114 | -0.43088 | -52.03939 | 2025-10-29 04:21:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdc670ba-fb34-3153-bead-f4d13e99667b | -2.76791 | -45.3971 | 2025-10-29 04:21:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3fa77fe-987c-3deb-bbd8-c867939cb654 | -10.7684 | -44.73864 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83ef3c98-8d44-3df9-978b-1d123730cf36 | -6.63154 | -47.19609 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 488c9312-492f-32d7-a0af-9da4cb71b980 | -7.34755 | -43.91017 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c7536da5-e1c1-3040-8f65-96eb063e8306 | -8.02818 | -47.39619 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1cc4067-cdba-360b-83ff-ead69ea879ff | -9.53278 | -46.92979 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a73e2d00-b917-3c4f-b7ab-1ddb4c8b7791 | -5.44023 | -46.28846 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5821983f-4918-379c-80e9-039049e1af4f | -9.4999 | -46.93939 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9685efb6-0697-384b-a8a7-dee00c67c357 | -5.34707 | -46.86125 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7c8977f-e28a-380b-8f1d-a9143e4f8baf | -5.5034 | -45.96221 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27726ca5-5bb0-3280-855b-e01cd859c35f | -8.54575 | -45.69538 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a422ad7-b8e7-3daf-a2a6-f220c664ec4a | -9.44425 | -46.89642 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69291a5b-8c91-3ab6-8934-8c4e72aaa547 | -9.94282 | -47.09409 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 19a911aa-910f-39b6-bb18-86f2357fdbe7 | -10.84695 | -47.89032 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5019e6dd-250a-3527-bba8-a18cd59001b2 | -7.8037 | -46.45015 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a5941563-8765-34d7-9b3b-f0f90e7dfdd5 | -6.99039 | -46.23058 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edbc78fe-d9d9-30e0-af9b-509991e223a9 | -5.33277 | -45.43089 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 299316ab-ca27-3f10-be99-ee32d4f202f9 | -6.98701 | -46.23005 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2320c84d-d91e-3bea-a09d-002d51175760 | -9.92816 | -47.67944 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 163f927c-8df5-31aa-9725-220a1efad06a | -6.1302 | -41.70649 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 310d0250-fa44-3c3f-b332-54906ab4a5e5 | -7.32329 | -44.73661 | 2025-10-29 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6ca547d-3fc0-363a-9233-1412c497fc12 | -10.85325 | -47.89524 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2192b360-5809-374e-88de-45d93cd38afe | -9.16624 | -46.27948 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e632684e-0a48-3808-b841-944737c35d07 | -10.75335 | -44.74713 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d79a55b-fb7d-3389-87f8-b2136c2f9241 | -5.40973 | -45.21693 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fadc7fc2-b3b6-3ea3-8b54-8dacebbcf3e1 | -9.22882 | -46.35141 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04b25cdc-2748-3555-ba56-3d0f8014f995 | -6.53892 | -43.56654 | 2025-10-29 04:23:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 599c3653-0999-3590-85ab-dc2aec9906df | -5.57244 | -46.53424 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 886992f1-8535-36be-8c13-f13737a7f88b | -6.93466 | -47.0029 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c66e4fdb-9d43-3234-8eb8-94d8bcf01686 | -5.61051 | -49.11811 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66163d5b-1177-3a2b-b5c5-d4a50dfcb117 | -8.7174 | -50.01228 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b97d70c-0450-3c89-ac56-12066f6a8cb5 | -6.27884 | -42.88089 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 406aa0ac-6b5c-3de6-a977-59114d5296ae | -8.05123 | -45.03053 | 2025-10-29 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84031a39-38c3-3148-867c-8d240db66365 | -7.78957 | -46.45165 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fead0f3-8e7f-34bb-b66c-93e398048234 | -7.70218 | -46.90901 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e046972-20ec-3e91-abbf-8d26fded82b7 | -9.1912 | -48.301 | 2025-10-29 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70af1562-9b0d-3af1-be55-b49bc0242ca0 | -10.52505 | -47.74401 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24c21e98-9898-3b44-ac29-9bfe8e002e45 | -7.27703 | -44.10964 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0c8382d-acdc-3228-8dbf-3265ef7a8135 | -10.88314 | -47.9954 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6796d28b-febe-3582-bbef-73ea902c59b5 | -5.67793 | -47.82487 | 2025-10-29 04:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0867320-ce44-3f7c-9e5f-484809c23849 | -5.86432 | -47.57915 | 2025-10-29 04:23:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d870fa69-0db9-3fb3-a39e-658511022aae | -7.12277 | -47.01312 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb935558-843f-32ac-acc8-2a0be0f935bd | -6.13976 | -41.71595 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8a941e02-6a9f-3ea5-8620-f83d5879a567 | -8.89091 | -47.53244 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eea770d-be6a-3a73-863e-f0b69aebdc9e | -7.75519 | -44.71938 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e358ba13-2657-3a83-bef7-8086bc072266 | -8.40117 | -46.92751 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5505248-91b1-301d-9cbb-33bd59bdf7a4 | -7.79002 | -46.47031 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 633298e4-5857-31d5-ac6d-99cfed3f5bf9 | -9.92507 | -47.1176 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cf2e766-d3f9-3972-8303-28d8021d4e4b | -5.61099 | -49.12157 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f7acd66a-c213-3647-9b0e-f32d21c7773b | -9.567 | -44.71333 | 2025-10-29 04:23:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7763abf-e770-38e3-b5fd-4ccf5b8f2d0c | -8.55095 | -45.69938 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 576eb8d2-9726-39b4-814c-da361053813c | -7.61251 | -43.59534 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8d1e968-75bb-309d-908b-1efe060595dc | -10.56654 | -49.83198 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2b69bd5a-4000-3bb6-9be8-a34bd9567864 | -8.54593 | -50.03678 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94a70cca-7ae2-343f-8e87-cef935a90ba7 | -10.65309 | -48.01283 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7b1396a-6ee4-33b7-ae2a-85ead2d1d187 | -7.79678 | -46.47142 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aaa0c57c-f9da-3e26-bbd8-3788e37c7882 | -9.54822 | -46.92443 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08fd62da-9bd2-3b0a-bb29-f448bd1dff71 | -7.80311 | -46.45378 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d3e6491-df59-3663-accd-05d0fe469442 | -9.62439 | -46.86202 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 74c63b80-ce3c-31d3-9273-b1f2b605b3d9 | -7.98191 | -46.27591 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f487c80-ab12-3844-b454-3c0ceed2ec71 | -6.10233 | -42.46672 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 253cdb5d-0553-3ee4-965a-4880829e0428 | -9.94222 | -47.09776 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6375ac66-4467-33f1-9c40-c393cd344d71 | -6.09953 | -42.43884 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e06ab1ca-12fa-3d93-9c82-f1ea92178355 | -8.54408 | -45.70588 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c52f848b-73a8-3415-84ec-babf0dd48be0 | -7.12215 | -47.01695 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22e30524-e022-304d-b326-563ab5e7f9ed | -6.28467 | -47.88089 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 665724e1-802f-3a3e-bd64-88c28796541c | -6.97254 | -49.40498 | 2025-10-29 04:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76319c21-79c0-3635-9607-63a1be9b292b | -5.64426 | -42.81114 | 2025-10-29 04:23:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b1060385-72dd-3b44-88e3-b1d4fdc59cce | -6.63641 | -44.60981 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2215e99-2d30-3d4a-be44-6cf0a60a33b1 | -6.10987 | -42.46393 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6772b18d-bf45-3523-bce6-9f550798c1be | -7.64366 | -46.92233 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 028d75e6-d816-3d2a-a8ce-f328870dbd0f | -10.42926 | -45.0523 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1df507a4-9a4b-3b2d-abda-5d5368cc8ced | -9.29257 | -47.03345 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 010e28d9-aa14-3204-8dba-0d5f16b01c40 | -5.59693 | -45.35767 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5c9a986-59ac-3f4f-b8f9-2977df2f59bc | -10.52977 | -47.73695 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41b1f02a-eba2-3363-8347-ce23244340f9 | -10.60357 | -49.62 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 560d98ce-dc34-32a3-9c2c-dd2337171a30 | -6.28104 | -47.88035 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de41b14b-302b-38c6-b1ab-d4f8c78bf013 | -9.49442 | -46.99479 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c499669f-c8b3-30cc-a3f8-67a5ab90684e | -11.26621 | -44.67262 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1da29599-429c-3550-8603-8fd7eeb7cc1c | -6.11207 | -41.72878 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32329ddd-7697-33b3-a04e-f1ebc2d958f5 | -8.49023 | -47.49148 | 2025-10-29 04:23:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 898be9b8-3726-34e9-ae6b-b810e3621b58 | -7.79237 | -46.45581 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c92d61d-27a2-3418-8d35-68a2b4cc136c | -11.05417 | -45.36118 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b1bd4e4-aa30-385f-8245-012f04a77847 | -9.96604 | -47.08261 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f80d595-4428-3df7-ad61-b14932242c84 | -10.98546 | -47.72991 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb69ed83-bb97-34dd-81b5-cedc7e14f7ed | -5.87262 | -47.61816 | 2025-10-29 04:23:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4f47260-e101-32d3-9f74-5c6c1f420fc9 | -9.19478 | -48.30161 | 2025-10-29 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3d6a9e8-d82b-3e1d-ae46-8e6f53d50aba | -8.24871 | -46.91855 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a8be2c31-02bf-37e5-96b2-34a1c67900f3 | -7.07596 | -44.93214 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9596e7ff-9210-37f3-add5-b8f7ff347546 | -7.79473 | -46.4413 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 873e3f36-2893-398a-82a0-b4ad3a526931 | -10.98951 | -47.72671 | 2025-10-29 04:23:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ceb8fb9-6b75-3333-8bad-bf2d6a19e574 | -5.67153 | -45.21159 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 597f198e-9ce0-309e-97d2-8a25ba5dde42 | -8.03738 | -47.40565 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f91a03a3-b993-3308-a844-febc90abb357 | -5.62044 | -47.11076 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8b1a3887-6fb5-3d83-9e44-5de0f58e211f | -10.6069 | -49.62293 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a74373cd-eb07-3cbe-b9d0-d10dcf4247de | -9.89873 | -44.89971 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 612fe527-3af4-3d00-a99e-c0623a9f30a4 | -7.45382 | -46.8424 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f168037c-e77c-3144-af51-951518dd3328 | -9.32346 | -46.25387 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
