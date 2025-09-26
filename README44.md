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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 342fe07d-b84c-3e34-89e1-148c606dfaad | -8.61426 | -54.99261 | 2025-09-26 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ef485f6-11c6-311e-a653-b48a9dbc92cc | -11.6677 | -44.46446 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f79c16e-dade-3377-a24d-2070e56b8ad1 | -12.56624 | -45.85152 | 2025-09-26 05:04:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5756c88-ba71-342b-80ce-eb4d18d6b9ff | -12.0637 | -47.98446 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 789a68f9-4d61-34b1-970c-6fcdf8457044 | -9.47326 | -48.23737 | 2025-09-26 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1bc0ea9-0b39-3b0b-a8a3-4fb1374b0ba2 | -13.63364 | -48.09845 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb513935-d3c5-3d96-b43e-65f020c892da | -7.80949 | -55.21941 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9fcf083-cff3-3e35-b358-ec0bd75c3c00 | -10.29191 | -45.22943 | 2025-09-26 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90ca5687-c178-3702-86f1-73f3caa37771 | -9.67541 | -46.03035 | 2025-09-26 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| df12ff78-ded3-38ef-bc72-87804faa887a | -12.72967 | -43.45833 | 2025-09-26 05:04:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87755664-5b4c-3a06-95ef-3747a21944fa | -12.02422 | -46.51119 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 51b9f289-5fad-3624-904d-ccba9585936a | -10.0077 | -44.17625 | 2025-09-26 05:04:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76af5d85-2daa-3ef3-8cae-b51b354d6745 | -7.31546 | -45.75871 | 2025-09-26 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 779231b1-4454-35ec-852a-ec257d2f700f | -12.06829 | -47.98954 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06c2403c-e2df-3040-a5e0-27b9fd4acd66 | -10.39908 | -46.14462 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f403c935-2700-3de4-bb34-406f326ca3ad | -13.84966 | -45.61669 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a70bce5-c245-300e-9f1a-fad8ae61fe61 | -10.12004 | -45.30993 | 2025-09-26 05:04:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 939cea3f-014f-34c6-86be-e93b62eb81f7 | -10.40891 | -46.16202 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f037f1e-dcc0-3ba4-a70b-aeb8a23562b6 | -10.39327 | -46.14391 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2d58010-3994-3e8a-a25f-95ae4453fdd8 | -8.08375 | -55.22309 | 2025-09-26 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d63b3db8-e21d-3217-a2d4-4e3defd2c9cb | -11.23841 | -45.54257 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| df97bad0-4697-3bdf-a6d9-51d97f4dafb6 | -7.79642 | -46.01363 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb7bde50-8a71-3f38-aa80-9fa51caad275 | -10.39856 | -46.14867 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cec21b9f-bd87-397d-934d-4f5c0a497227 | -11.66707 | -44.4701 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 572215a5-74ea-3586-8d30-f2b53cac7b82 | -13.27911 | -50.70192 | 2025-09-26 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3c9bbc71-1d72-3d40-91ec-f98fc1408fad | -11.97766 | -46.6045 | 2025-09-26 05:04:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 413aa3d4-6c04-35f2-8934-da65f84097ec | -10.39834 | -46.15207 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3cbaac53-7810-3974-889b-4b6738392213 | -9.69662 | -48.94587 | 2025-09-26 05:04:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9c93e305-7035-3735-8057-5c7bab97a892 | -13.64616 | -48.08472 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8cc29e7-bad5-34cc-82c6-efd5148c384b | -11.65368 | -45.35567 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e12cc034-6c2b-3e34-9c36-c42e08b48d4b | -11.25062 | -45.5441 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 96233431-750a-3dde-a54c-af0f3befacd4 | -11.76995 | -47.5648 | 2025-09-26 05:04:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17807e57-f811-3b95-b4e1-09811dc991b9 | -10.79087 | -45.37889 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 638b8af0-5e58-3308-827f-2b4cd785f295 | -12.06852 | -47.98852 | 2025-09-26 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1b09d6e-8ec9-382c-a5e9-e44bac292658 | -10.40788 | -46.17038 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 94204183-567a-3f87-8ec5-7bd8c3bceb8e | -13.85453 | -45.60965 | 2025-09-26 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6965f2e6-950a-3870-9c77-b695343651be | -13.69578 | -47.9675 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d01a0b5d-60d4-349e-8851-fbbabf873eae | -11.65982 | -45.35695 | 2025-09-26 05:04:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da27bade-9f6a-30cb-9edb-f6aace0f7fe3 | -10.61565 | -49.55498 | 2025-09-26 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6a514e12-85a5-30a9-a323-b548d55d83bd | -10.40112 | -46.17743 | 2025-09-26 05:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c068eaef-abd9-341b-8855-dd126d4ada11 | -11.96491 | -47.88136 | 2025-09-26 05:04:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6e210834-8f2a-37b5-968e-f35f90c8d319 | -8.32578 | -49.52929 | 2025-09-26 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da827d17-4ed3-3076-8c35-ac53bf1c6233 | -8.61707 | -54.99671 | 2025-09-26 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e57a7213-0b72-3954-adab-d7399c6314c2 | -11.24508 | -45.53863 | 2025-09-26 05:04:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 125c6054-ffb1-3f84-a24f-d4fdb2a85e01 | -7.68148 | -45.99107 | 2025-09-26 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d968676-c181-3462-98ce-485f47fde60a | -8.61762 | -54.99314 | 2025-09-26 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6fba9f91-dcd5-3873-884e-62338e6981a9 | -13.69781 | -51.15549 | 2025-09-26 05:04:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db176614-0055-3de6-adf7-e75d5763ea21 | -11.67631 | -44.45445 | 2025-09-26 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e15eeea7-b7d6-3c94-b1a1-597446b75e8a | -13.63865 | -48.10176 | 2025-09-26 05:04:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ee7bf9-ef4b-397b-85a3-ba3f807ff60a | -15.93774 | -59.47131 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 183b5caa-4b0e-338c-a979-15639fd9df93 | -15.36733 | -59.16709 | 2025-09-26 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 977bbe3a-499d-36c1-a0dd-ce597b6d7f34 | -16.84859 | -50.52087 | 2025-09-26 05:06:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 13e1642e-4975-3582-8b40-87f166c23861 | -15.89726 | -59.33733 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9022eb64-9f0a-3743-82cf-195e67350a92 | -18.54915 | -46.96861 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 006c45ba-86e1-3df5-a7ac-81ee543137b8 | -15.92012 | -57.49782 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e9ebd32-e770-324e-9169-85bccb0a5320 | -14.9519 | -47.50506 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3209752-7016-31ea-8309-00930c6d810c | -15.88684 | -59.40059 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dd6db24-2465-3c72-9b85-c8052323abdc | -15.36612 | -59.17448 | 2025-09-26 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b737ce6-c7e5-349d-bfc6-011ce8e3e510 | -18.18318 | -53.33794 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01eccdec-27ac-39c8-8449-66cf0ac28c82 | -15.02662 | -46.94241 | 2025-09-26 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f93b59a5-e3f1-3181-93d3-576873f12c04 | -15.92675 | -57.49892 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dfc36e1b-1cc5-300d-96e5-f0f74fe602b6 | -15.92399 | -57.4948 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c81f975a-686e-3a5a-a66f-7afc28987857 | -15.06546 | -44.98489 | 2025-09-26 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ddc3a9b-ce23-3aec-9c94-75ea51061293 | -15.38487 | -46.1128 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a41a99c0-e7b9-3bec-8c03-dd29f29f92a8 | -15.73068 | -59.49684 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f417a4c4-c5ec-3487-a74e-7c9a1980e877 | -15.99707 | -59.49677 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3517db08-0e09-3d3e-b8ae-7b72c21e9e8e | -14.75853 | -48.35359 | 2025-09-26 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4400bd7-77b7-3e71-9385-bd957c1d5be5 | -15.91127 | -57.48904 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98ff48c8-9edd-338c-8de6-4df81e52f440 | -15.5151 | -50.43655 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fc9eea46-32b4-3523-a024-af8f95191115 | -15.02067 | -46.94266 | 2025-09-26 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9c170a1-4a48-3b82-ae01-f9e593c30a95 | -15.93618 | -59.50222 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b58c2d07-4baf-33ed-9455-6f4021643641 | -15.72453 | -59.49192 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1594e950-32fb-320d-84d6-9c63e5e32e63 | -14.59862 | -48.25559 | 2025-09-26 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 67674b79-11d0-3e6e-b00e-5c377c02299c | -15.90796 | -57.48848 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 69bec9cd-7e00-3771-81bc-aca7476be48c | -17.93048 | -55.85374 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 13ad0305-ccf2-3517-9a0a-ae667cbc80bc | -15.26224 | -46.4441 | 2025-09-26 05:06:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f259450e-ff03-3a29-9029-0e5bc814e41e | -15.97402 | -59.48894 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b470023b-744a-3392-b84f-38cb766abe75 | -20.01244 | -44.24099 | 2025-09-26 05:06:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 24cb42e2-3fea-301c-8626-73abd970f890 | -16.21851 | -48.80253 | 2025-09-26 05:06:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d93caee7-d949-395c-a0c7-285bce65a553 | -15.5126 | -50.43789 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a806a341-c6a4-3b77-8fe7-3a4bdb6bbfb9 | -16.21771 | -48.80938 | 2025-09-26 05:06:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 31b77d9b-ddbc-3677-afb2-c1559c0c82b9 | -15.26378 | -59.45259 | 2025-09-26 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43b082a7-b653-3ce0-ad6a-04f5b41845b0 | -18.18407 | -53.33107 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14fc8e02-2bf4-38c1-ac8b-683cf95c4f25 | -19.75068 | -48.15495 | 2025-09-26 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21675787-9dd2-3cc5-88f6-129c76f5e2f2 | -15.72792 | -59.49249 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4566c92-1807-3124-a12d-ef60c7af347e | -15.51842 | -50.42896 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 046680f2-2469-3d03-8682-599acb99e7d7 | -15.5157 | -50.4319 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 30dbe32d-24b4-3407-b36b-bb061fa9e29b | -15.38355 | -46.11417 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5c5d159-1c06-34e3-945e-e7b798d208f6 | -18.30092 | -57.09561 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 51bf9b9c-7a72-399a-b255-f5a0b9e2ad84 | -17.58681 | -51.81829 | 2025-09-26 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21ad93c9-6d8f-3149-87c6-b5d9de26e325 | -15.92067 | -57.49426 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba7fc348-1ea3-3678-badc-4c76ead8abec | -17.17579 | -56.36084 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 03ddcb8a-301b-36c1-993b-f6ebda03b743 | -14.94622 | -47.50465 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 457a1155-b227-3282-b5af-0088c25a7892 | -15.51786 | -50.43365 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2f7a79ff-1ab6-3814-aaab-321862664400 | -14.10609 | -51.15298 | 2025-09-26 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0453bcb-8637-36e1-9735-569bc722d677 | -15.83158 | -59.60785 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61253eef-9bd7-31fb-bcb4-176827a2d95b | -15.0326 | -46.94205 | 2025-09-26 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8c79272-8476-3933-9b9a-03b8133fc446 | -15.90796 | -59.33545 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b35c951-ec67-3299-9848-fee5b62d3317 | -18.1845 | -53.32774 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f120f1fd-e92c-39e2-8160-3089faf35b03 | -18.55458 | -46.96637 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README45.md)
