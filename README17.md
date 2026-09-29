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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3da99de3-b6e5-3292-a73b-3c6ce1fc3243 | -7.9943 | -43.26091 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6835a739-1b4c-311f-9f6f-76a20fb368c2 | -7.51529 | -44.55907 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d79d1cc6-ae49-32c7-b769-bc1a74280aab | -7.07848 | -41.7415 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 503fe60f-5805-3a30-9839-8eb07a39af33 | -3.71397 | -54.21787 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 09d156e3-29cf-3890-aff1-c703bf54a90e | -3.12263 | -40.99054 | 2026-09-29 04:14:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 165539aa-7ce9-3630-aa65-655587d7de9f | -7.46392 | -46.68237 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66c9c019-2714-339e-991a-02c75344bc75 | -8.35827 | -45.39618 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0a5bf24-7d0d-368e-8485-24a7d20de7a6 | -3.80316 | -44.10362 | 2026-09-29 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bf8d64f-f065-3dc8-970b-e9d5d5fb0240 | -7.95742 | -49.57674 | 2026-09-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a68cc84-0a09-3a23-8081-156971bdbe98 | -6.74282 | -44.83793 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e1726d5-59fa-327b-972d-43ec275d3c04 | -2.29649 | -48.54812 | 2026-09-29 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8489a885-c2f0-3c2a-9ffc-06cc07ab176d | -7.40685 | -42.61878 | 2026-09-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a76f84dc-e1b8-3301-8035-697ea3b78fed | -4.502 | -42.55252 | 2026-09-29 04:14:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3f7d11b9-0efb-3687-b607-10331ec661fa | -7.57324 | -47.3659 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a8f0249-563c-3e4b-9d6b-570472824f25 | -3.70695 | -54.22166 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3ed7d575-8bf0-3bc6-9634-3f65054e37ea | -7.38814 | -47.01395 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d37ee94-d0a8-3bae-aa3c-b1ff31f09b64 | -7.3914 | -42.12265 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b22644cc-f6be-3481-9fef-8fd07a62b184 | -8.32502 | -44.17303 | 2026-09-29 04:14:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29ce19f6-8837-30b2-bb6e-36eb95cae807 | -7.53343 | -45.89134 | 2026-09-29 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0dec5c93-77bd-3ce7-b4fd-fa352e430aec | -4.05011 | -54.92685 | 2026-09-29 04:14:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 7268eee6-f02a-3a55-81bc-c16c635ce112 | -8.73271 | -44.92853 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fe1f292-e260-3b79-8846-185801de2614 | -7.42925 | -46.87522 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aed3b1f6-ad7a-33a3-a968-b16404d88656 | -3.88762 | -49.50615 | 2026-09-29 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42f68869-512e-323c-87a0-0a713d446f27 | -3.70777 | -54.21681 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e205528-3185-3bcd-8f36-39581914bb2d | -7.4322 | -46.88007 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f3f7fb0c-ed47-3a54-9bb9-f9aea0a0a3a5 | -5.42312 | -43.4524 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75667c0c-d69a-3daa-82ae-bf15fc4aee2c | -8.22708 | -45.4053 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d278679-5997-370f-be26-041ec46931eb | -6.31611 | -52.62265 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 675457a1-fc1e-3fc4-91f7-f1a4c1a1fc2c | -8.23046 | -45.40587 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1de74ff1-f297-3763-807d-756654a770cb | -8.05757 | -44.8096 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8212321-74bd-3ce1-a237-6c6102add84d | -4.94594 | -48.61586 | 2026-09-29 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d97063b-2b33-3868-a058-5e426cfa0404 | -7.69139 | -48.86363 | 2026-09-29 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bc8893b9-8607-31b1-b2ad-408e64dca145 | -4.32314 | -48.62839 | 2026-09-29 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25a6b92a-d018-3acf-94bd-a2c58606d06a | -6.15323 | -52.90694 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2158b9be-0d45-3ef5-8263-09aa543925ed | -8.96929 | -44.16592 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a09eaedf-80f8-3cf2-90b9-aa98002177d0 | -6.37725 | -45.8099 | 2026-09-29 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2470a4f7-8295-3a77-b590-fefc1f1f4143 | -7.06025 | -42.0647 | 2026-09-29 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6929e694-8099-3b3d-906a-9284c5e32af1 | -5.73643 | -45.0266 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b3810cba-c059-32be-a8b7-fc53743c042b | -7.5713 | -47.36732 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f922f9a-f200-3f78-9d85-90cf3ae83e88 | -7.67681 | -44.89085 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e00f51e9-156e-356a-bc36-516337dd75bb | -6.3203 | -52.63045 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2225ccf7-a37c-3c02-bb3c-ab258c225b2c | -7.42938 | -46.87825 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ea7e8618-b911-3e41-ad24-7c10e37b3ef6 | -5.19082 | -46.07844 | 2026-09-29 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbde8942-fcc1-3c21-9825-91936297b2de | -6.72596 | -45.58343 | 2026-09-29 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b736a21d-d6d1-34a2-93cd-0517a051c5a3 | -8.35504 | -46.8872 | 2026-09-29 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c9c5f6d4-27f0-3d99-bde4-b977b9808887 | -7.60792 | -46.46003 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f8b9619-2d7f-325b-ab60-0abd80125138 | -4.31823 | -48.63173 | 2026-09-29 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04248ae1-0de6-3f95-a09f-c499b4b8d341 | -3.71151 | -54.22443 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 076fed50-d763-3a19-8104-90f61aec9cae | -8.03355 | -43.33815 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b7c3fcaa-c70f-3e0f-b18b-75d7adad19f1 | -5.42751 | -43.44601 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0096ff7d-7d35-3f03-a20b-c37e461c8e8a | -7.63255 | -45.51554 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 193155d1-cbbc-36d6-aa8c-fff72e3f423e | -7.43928 | -43.83236 | 2026-09-29 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f600704c-e442-34ff-8d5e-d44cba90471f | -5.72251 | -53.45455 | 2026-09-29 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8b1fba-ae4f-3d6c-a61b-687e3c12e2d6 | -7.34595 | -47.2505 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64522f48-0337-3db1-8588-6a6965e5c256 | -5.54591 | -44.87666 | 2026-09-29 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c5c17cf-dbca-3498-a6e7-28a1eb936553 | -9.05392 | -45.00591 | 2026-09-29 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ee55f58-75d9-3921-b9d2-6ce8fcdf7e8c | -5.61136 | -44.99604 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 68b287d0-779e-3bc7-b0bb-3d5b5cceadff | -8.24261 | -45.43827 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1aa6e0dc-6fa2-36ae-bcd3-b1ea2a2b6bc6 | -8.00091 | -43.26194 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 86ce00c7-bd67-375e-bd81-7805b276183d | -7.92826 | -45.49038 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37d48030-faeb-35a6-9151-4479a13e8b55 | -5.73857 | -45.05722 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3f816757-26bc-3957-961c-2e70e7bebb14 | -3.71231 | -54.22786 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9e1174d3-7b60-384a-b0a5-74b3ec6d616e | -7.38448 | -47.01333 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c723a9-b71c-37fc-9535-241d596c6630 | -3.16095 | -54.09621 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f94b5e8-4664-34bc-93cd-f40b26b69560 | -7.52245 | -45.08816 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 861d83c4-08bb-33ad-911b-d6d3de432889 | -3.22411 | -54.31844 | 2026-09-29 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4893358f-140a-32ac-aca6-01549b5b362e | -3.27052 | -50.14115 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c0d5cb0b-86d1-3f9b-8cd6-5ca41a3a8be6 | -7.61147 | -46.46061 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 95bb0e21-51e9-316c-a7aa-91e3c1b73693 | -7.47571 | -45.81593 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 34353e94-2ead-3d4d-b2b1-c5b7d00a30ce | -8.23384 | -45.40646 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10fa3d0c-e807-3e65-9bea-4d74a794be95 | -8.97642 | -44.14213 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41b5e6c3-84e6-3171-9f04-544eb49f9c40 | -5.74347 | -43.2772 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec59864e-378b-3723-b7f5-b10916d3206a | -8.98138 | -44.15359 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5d3a15d-e436-378e-8561-7911fd96afd7 | -8.4523 | -44.65892 | 2026-09-29 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 36a4b279-cf5c-3ff1-b293-765d43a7b3fd | -6.887 | -52.47673 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e3fc588-a38f-322e-8d66-a7c2a4b45c43 | -7.53936 | -47.12098 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9c5f014f-bbce-3a93-82e0-9ed6d1e9d8a9 | -8.35489 | -45.39565 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 20ed4e7e-f2ca-3266-87d7-657e3317aa44 | -6.95509 | -41.60329 | 2026-09-29 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 048b3982-33d2-3552-a71e-3bd7eb3fb53e | -7.48262 | -45.81705 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d3311f68-a8ba-3f57-8c9d-549dafb55434 | -8.00145 | -43.25846 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dee4f452-eaaa-3e95-8594-960297516927 | -8.21874 | -45.45684 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 685321c7-44f0-35a7-8636-3c6b9ae65ac4 | -5.73339 | -45.17855 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6817cec-4f43-3499-a229-7b43d0181f6d | -4.81141 | -45.01251 | 2026-09-29 04:14:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 027999c7-1f68-3c69-aee2-c7da2f306a58 | -7.82638 | -45.8158 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d306f7-3795-3ba7-b119-b2c4970c1d73 | -7.37967 | -42.13187 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 14f41800-5a8b-350b-abca-49b91b87d8ab | -2.9856 | -54.54231 | 2026-09-29 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fea466b1-c813-34bd-a7af-443caad5de01 | -4.31896 | -48.62842 | 2026-09-29 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb756683-11e2-3b6c-8516-1c03148c154e | -3.51206 | -50.3157 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 927a2560-49c9-3230-9d23-afab8929a38a | -5.63573 | -43.72297 | 2026-09-29 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31187222-9c9e-3848-af8f-37a347b79a08 | -5.03103 | -43.56746 | 2026-09-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9c01db4c-772e-32f3-bd77-918fa25fd6f5 | -5.73361 | -45.02236 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2362ac50-0054-3dfd-9eb9-408fc23f122d | -2.938 | -41.73898 | 2026-09-29 04:14:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27eeff3b-6d16-32ec-a9c9-cd447c25f7bf | -4.25425 | -51.04525 | 2026-09-29 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15e93edf-1818-36af-96eb-31697f906320 | -5.02994 | -43.57439 | 2026-09-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8cb15b9a-5c3a-3343-9016-e59321f1802e | -7.47225 | -45.81536 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27667fd7-4e63-317a-b155-4f0a74263b6a | -3.15474 | -54.09515 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1a8143a1-f520-3ee8-9aa2-65079c0dbb80 | -3.09555 | -50.27804 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 374de631-2925-3794-bb3d-2949e6a48df2 | -3.02246 | -53.86914 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a4610d98-3a55-3a88-84f6-457eab05393e | -7.08488 | -46.70974 | 2026-09-29 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3547e8a-4a1e-3f63-b5d4-8d7061a17421 | -5.33268 | -46.19392 | 2026-09-29 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
