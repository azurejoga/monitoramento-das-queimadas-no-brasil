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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbbbb4a7-754f-3cbd-8fdb-15b6d36c00f6 | -11.2231 | -53.973598 | 2026-09-04 00:25:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 520c206f-ff1b-30ae-bd92-90eec8dc761e | -13.4065 | -43.8689 | 2026-09-04 00:25:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 347c5b65-feb3-3df4-9997-17ce4559e84c | -8.4624 | -54.747898 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556217ce-c4b7-3678-a44f-0f4dabf32f08 | -17.1035 | -56.852798 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 852edaee-dddf-346f-9bf6-80de89b4777b | -18.8043 | -47.553398 | 2026-09-04 00:25:00 | METOP-B | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fd3303ab-98f7-32e0-967e-d90ac1812bea | -4.4808 | -55.402802 | 2026-09-04 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5bb64ea-ae42-32ea-8c69-a9f9b7bee5fc | -8.5057 | -54.6651 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e69d65b-3e26-301f-bd8a-4fe893aa9b52 | -10.212 | -50.273201 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c7e110c-40d5-3892-816c-d786e2fb1c68 | -3.6313 | -54.607201 | 2026-09-04 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ed6462-fbe3-3de9-8b14-e75d3bc8c57a | -4.3545 | -47.776501 | 2026-09-04 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01068d8a-fb38-33ff-b471-abca31b229f5 | -8.4485 | -54.685299 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8c5e0a-6eff-3b91-a032-0c34c6e67dd9 | -10.4452 | -61.186501 | 2026-09-04 00:25:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74eec7e7-9542-3e1a-ae9c-0073bac62cc6 | -10.8641 | -50.8983 | 2026-09-04 00:25:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 04979f85-143e-340b-bfe2-fa4cb0082385 | -17.0916 | -56.844398 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76814f5b-40fd-3054-8524-f5f699465b9d | -5.5863 | -43.993099 | 2026-09-04 00:25:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08bfe7bc-1bf5-3fe2-b7c7-35152ea1ab0f | -10.3396 | -49.938702 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ca176136-ed8b-3d60-bcf0-667a4d0e6924 | -11.942 | -55.9053 | 2026-09-04 00:25:00 | METOP-B | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce3b815-70a8-3c6b-9307-c7211e9ca616 | -8.4237 | -54.7127 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16b85166-69b2-3432-8011-1f0da1c32790 | -8.1229 | -54.794601 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcfc1558-cd4a-31df-aae1-72877b8731b5 | -8.2928 | -54.910198 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3ef918-c56c-3107-aae8-ff7b3e801538 | -8.5026 | -54.651199 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cef94932-799b-303d-a80f-18d3b21cf87d | -8.4387 | -54.6875 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9681dd-e13b-36a0-9d44-0c671a8f5f85 | -18.154301 | -51.8088 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| de13221f-9868-3fb8-9144-92fbd4757b57 | -21.723801 | -47.1591 | 2026-09-04 00:25:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bbe67805-ab36-3498-8218-2ef1ae1a2d65 | -8.4996 | -54.637402 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 601214b8-4675-3a5b-a04c-eb523b4b3d33 | -19.622999 | -46.959 | 2026-09-04 00:25:00 | METOP-B | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8430c3eb-5213-3ec3-8558-e3a2a62a7159 | -10.5739 | -50.0126 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 36711dbe-98aa-3053-8311-af476ed99d76 | -21.4604 | -48.674 | 2026-09-04 00:25:00 | METOP-B | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6faf38ea-282d-3d1d-942d-1fcc67295277 | -10.6571 | -61.739201 | 2026-09-04 00:25:00 | METOP-B | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e197817-fc82-3561-b08d-0085a84cd307 | -4.3642 | -47.7742 | 2026-09-04 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adfb19eb-a4f7-3008-a1d6-180fd6f5dbe2 | -3.6731 | -53.748001 | 2026-09-04 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71493c79-1baa-34a3-9e50-707d4de5240b | -3.1176 | -51.726799 | 2026-09-04 00:25:00 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8f21e81-bd91-38ee-9487-1f38b6e74ef4 | -3.6298 | -54.6003 | 2026-09-04 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89188a1d-b1e2-346b-a89d-42432b87a4e1 | -7.5515 | -61.341999 | 2026-09-04 00:25:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 906a14e4-a5f3-34d1-90aa-5a358e1aba4b | -18.724701 | -48.912498 | 2026-09-04 00:25:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bb73a8f8-8789-3252-bfb9-72544339200e | -8.4593 | -54.734001 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75eba310-8d31-3036-ab51-4187d780ab90 | -20.980801 | -49.1035 | 2026-09-04 00:25:00 | METOP-B | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 26db514f-eb69-37fa-97b9-7ee07fb1c980 | -15.3217 | -47.033401 | 2026-09-04 00:25:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 180afd3b-77b3-3680-8ff7-6deeecebc6f6 | -14.7858 | -47.126301 | 2026-09-04 00:25:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e5acd779-b624-36a9-a4a3-14bd5d1cd80c | -18.7363 | -48.918201 | 2026-09-04 00:25:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a375904a-b5b9-3379-981b-197562c78228 | -6.9865 | -62.961601 | 2026-09-04 00:25:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6063e4b4-218e-3498-a163-747737b2d0e4 | -4.4658 | -55.427799 | 2026-09-04 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6dc716d-a730-3416-b2f0-a060a7c1b259 | -17.095699 | -56.865101 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fbf969d1-ef7c-306b-aa9a-aa234762da58 | -18.7325 | -48.901798 | 2026-09-04 00:25:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1fca0c31-8b26-37a2-b6d7-6105104cf0c6 | -7.5583 | -61.3256 | 2026-09-04 00:25:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7300957e-e602-336e-9268-3f0314989aac | -5.3889 | -54.452 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 213b4803-e419-37ec-8c81-a9250e4e37c0 | -21.7246 | -47.1194 | 2026-09-04 00:25:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 72583803-7550-3f49-b156-8204e598516f | -8.1878 | -62.793098 | 2026-09-04 00:25:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e41c4ed1-ec7f-3e67-8e89-f3f2620734c2 | -10.578 | -50.030102 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2da18bb1-30d4-3506-a0ce-66521258bd94 | -10.4981 | -51.3218 | 2026-09-04 00:25:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 50d47a0a-9ecb-3385-8da1-bf311818b101 | -4.1256 | -56.3424 | 2026-09-04 00:25:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28663b84-1ece-31b2-adc5-6dc8a63f368c | -7.3393 | -55.203201 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80234916-db23-3f51-a726-6e71fba2fd27 | -10.9121 | -49.610298 | 2026-09-04 00:25:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7778e997-cb42-3112-a607-4afac6b6568b | -8.4371 | -54.6805 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2c2a1f0-d233-3fa6-9487-e525057c3468 | -18.1413 | -51.7967 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c52a366-fee7-3caa-8e8f-29248fba33b1 | -3.6715 | -53.740898 | 2026-09-04 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc5f4736-5b37-37b5-87fd-22caae02c816 | -10.5682 | -50.032398 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb89078f-11a8-3e85-adb5-60406d5faef0 | -8.4691 | -54.7318 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be529cab-0760-3ab1-bdf6-b29f4795267a | -14.7886 | -47.1376 | 2026-09-04 00:25:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5b9585-2189-3409-ba14-71d91c7c1c9b | -10.21 | -50.264599 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23609b96-ebdc-3a94-93ba-adedc7960b9e | -10.3375 | -49.929901 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5b72a4c-f653-3806-acf8-df51d7b455e6 | -14.8971 | -44.665699 | 2026-09-04 00:25:00 | METOP-B | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| faa500cb-4268-34b2-9633-27701f57029f | -18.133101 | -51.806198 | 2026-09-04 00:25:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac710c74-5270-3081-8266-d4464f23f722 | -17.0994 | -56.8321 | 2026-09-04 00:25:00 | METOP-B | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8d00249-60a9-33cb-9273-a4fc6687bf8f | -21.714899 | -47.122101 | 2026-09-04 00:25:00 | METOP-B | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2dd268c6-ca69-3fcc-a507-bbd7344181e8 | -10.32 | -50.337299 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5e020b12-c18b-3d96-9aa2-9ef545138943 | -10.6213 | -50.389599 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2957a264-2584-39f1-a7b2-87e0dd8c3618 | -8.4609 | -54.740898 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86f92804-08b4-3483-b902-07da1b00e4cf | -4.9716 | -55.845699 | 2026-09-04 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f81d324b-446f-36ae-8e6c-f34f8f3839c1 | -6.3136 | -46.109299 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 193b85be-4a60-3fbd-881b-ad6a76e5fc38 | -9.9978 | -48.550598 | 2026-09-04 00:25:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3b536a4-d745-38ac-8c77-4bd2f08858b5 | -7.5613 | -61.34 | 2026-09-04 00:25:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 147a1854-8de4-33a2-bfe7-2e186430b344 | -6.3049 | -46.073601 | 2026-09-04 00:25:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 829a37f5-a928-330a-a5a2-4339c5502aea | -21.5793 | -48.651199 | 2026-09-04 00:25:00 | METOP-B | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 07c920e1-5149-3505-936f-4840e9424572 | -3.6748 | -53.7551 | 2026-09-04 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46337232-f8ec-35c4-be02-a3df9ae7c74b | -10.3102 | -50.3396 | 2026-09-04 00:25:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40a09736-6075-39c7-bd5d-74c8dc2c4a43 | -8.1213 | -54.787601 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec9bd2c-84ae-3ef0-9a5f-10e953b03fe2 | -4.143 | -60.679699 | 2026-09-04 00:25:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74ad0b51-15b9-3fef-a7a4-4ed1406141f0 | -5.5767 | -43.995499 | 2026-09-04 00:25:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| edade26a-55b1-3095-b29a-4bc3a421be54 | -8.4944 | -54.6604 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f22193c-8b36-3536-87f8-b3783aec1878 | -8.5011 | -54.644299 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc86971e-fdd0-37d6-8107-fc502c5ce9d9 | -8.4402 | -54.694401 | 2026-09-04 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8f43b78-f1e5-3097-b43c-071d40a4871d | -6.1308 | -57.685101 | 2026-09-04 00:25:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d286320-06a5-386d-a3f6-e28dc8daaf23 | -8.2048 | -62.7979 | 2026-09-04 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1e028142-2594-386e-8a02-fa110c6b9f69 | -10.92 | -45.3483 | 2026-09-04 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| a6486eea-b4b7-32a1-82df-a9d970bf3f57 | -18.7358 | -48.9307 | 2026-09-04 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 409ecef2-e947-390c-81ef-c2f6141888a3 | -8.4861 | -54.6619 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| ace87a07-151c-3ced-bc3d-d280b6b0894a | -8.5234 | -54.6594 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| ec4cddf1-e044-33be-a100-7687f8d3356a | -8.4668 | -54.7439 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| f6c38f68-86ea-3fb7-bb66-955ebeb0af5e | -10.9009 | -45.3509 | 2026-09-04 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a12efd3f-5ab7-3f3f-8b08-6d1e934266ea | -8.1128 | -54.767 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 2fe00130-8453-3ac1-9a8e-4c3f0bcb50a1 | -8.505 | -54.6404 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| b9a7d4e7-f24d-3d14-9ab1-642435ad9237 | -7.5476 | -61.3437 | 2026-09-04 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 140.6 |
| 1853c2b1-658e-392c-ad34-2c36b37d4097 | -6.3088 | -46.0791 | 2026-09-04 00:30:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| d1a0b4bc-035a-3171-a743-86170102eb67 | -18.7363 | -48.908 | 2026-09-04 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 04da2715-f665-3704-a635-0f7067652dd4 | -7.0047 | -62.9902 | 2026-09-04 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| cc576d2c-ea22-3b12-a59d-870389bbd723 | -7.5477 | -61.3247 | 2026-09-04 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2e1e7431-0908-345b-8c13-0e3e304b6272 | -8.4863 | -54.6417 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 146.5 |
| 9cab8134-70d4-3b23-9d85-0859f56a616c | -8.1126 | -54.7871 | 2026-09-04 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 76a06260-42c4-3c4a-a6e9-6a4de5a5b2f8 | -7.566 | -61.343 | 2026-09-04 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.2 |


[Clique aqui para ver as próximas entradas](README4.md)
