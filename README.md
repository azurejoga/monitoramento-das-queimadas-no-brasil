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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c0dbfba-85f5-30e1-ac55-e140ea0da527 | 2.3071 | -60.2264 | 2025-03-31 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 4b3730ff-ca55-3949-a014-7ce5d720d16a | 2.3071 | -60.2264 | 2025-03-31 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c9270c42-230a-3e76-9e07-7bc0157aa4f3 | 2.17864 | -61.25648 | 2025-03-31 01:26:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 3b1e4ca9-a957-3115-ba94-e511cf90fc14 | 2.36018 | -60.14772 | 2025-03-31 01:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee1a9e1a-f89d-3c16-907a-2d87e317f7bd | 2.31387 | -60.22181 | 2025-03-31 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 485975bb-7504-324d-a03e-a5be923ce29d | 2.41259 | -60.70652 | 2025-03-31 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 0ffdb2d8-b51d-32ff-8b3f-c8d053b8dc82 | 2.8962 | -60.26876 | 2025-03-31 01:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da287123-1ff3-3067-9890-aaf336ab10c7 | 2.27449 | -61.22944 | 2025-03-31 01:26:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 24.9 |
| fe58de5c-53b9-3236-9e43-1d43aa437ec6 | 2.40371 | -60.70527 | 2025-03-31 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a3a4384e-01ad-3d36-afc9-842017799767 | 2.14088 | -61.86052 | 2025-03-31 01:26:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b4ec7b2b-7723-344f-ac4a-8c3b210defcc | 2.31265 | -60.23058 | 2025-03-31 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.8 |
| c14cbcf7-8705-3400-a96c-f7c38b6d2dfe | 2.06306 | -60.96033 | 2025-03-31 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d450fe1c-846e-39f6-a590-b5dd79c633c2 | 2.17736 | -61.26561 | 2025-03-31 01:26:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16948d6f-2aa6-3163-96f4-0e8ae64f53e2 | -19.6792 | -48.2307 | 2025-03-31 03:00:00 | GOES-16 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 146.1 |
| ecd00798-3730-3020-9911-f6c39d6420da | -19.6799 | -48.2076 | 2025-03-31 03:00:00 | GOES-16 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 93104910-b54a-38ee-b32f-64830ad4b1de | -8.87711 | -36.5284 | 2025-03-31 03:30:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b404b571-11e7-37cc-b0ce-f92f2a3c4b5d | -8.53867 | -37.72078 | 2025-03-31 03:30:00 | NOAA-21 | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 501254ad-c80c-3248-b2ff-fc743b66980b | -11.05829 | -37.10348 | 2025-03-31 03:30:00 | NOAA-21 | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8cecd1cf-7aae-3548-ad77-b0f47f0f2d72 | -8.39079 | -35.02671 | 2025-03-31 03:30:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 69197cc8-de7a-3377-9bab-13ce4da3b5b7 | -8.07227 | -34.97652 | 2025-03-31 03:30:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 918f52c4-d9b5-38ab-abf3-886468eb5cad | -8.07578 | -34.9771 | 2025-03-31 03:30:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4e9a3553-e376-3b0b-956b-b5edd7a00b44 | -9.58596 | -37.7608 | 2025-03-31 03:30:00 | NOAA-21 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f736e15b-0de0-33be-88c1-39dce1aa3905 | -16.68119 | -43.88557 | 2025-03-31 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b2057fd-e439-36aa-80fe-cf5efbabde74 | -18.03951 | -39.92665 | 2025-03-31 03:32:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d9b5f0b-05a1-34c5-8e96-318c1328c909 | -17.41575 | -40.03183 | 2025-03-31 03:32:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3ba939e1-ef5b-3dcb-9f26-25436cda7edf | -19.6731 | -48.22687 | 2025-03-31 03:34:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5e16602b-e6cf-36db-bcf3-43159e85da78 | -19.67958 | -48.22822 | 2025-03-31 03:34:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1d33e662-4506-33ec-b7b3-aca6719628b4 | -19.67459 | -48.22054 | 2025-03-31 03:34:00 | NOAA-21 | VERÍSSIMO | MINAS GERAIS | Brasil | 3171105 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 866a5e5e-7370-317b-b922-26aab1142527 | -25.56956 | -49.35879 | 2025-03-31 03:36:00 | NOAA-21 | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e3720256-706f-30e5-ada0-7ebd88cf7eea | -8.07417 | -34.9777 | 2025-03-31 03:53:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 67f553cf-9ad5-3c66-a914-4e23b9c689b8 | -8.39211 | -35.02629 | 2025-03-31 03:55:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c936cee-af0e-3030-b1ee-ae5db49da6dd | -10.43546 | -38.34355 | 2025-03-31 03:55:00 | NPP-375D | ANTAS | BAHIA | Brasil | 2901601 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85c56685-a1f8-3e3f-9e2a-861a57baa54b | -8.39275 | -35.02185 | 2025-03-31 03:55:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2b533eb1-aa0c-38f7-bfd6-6a402240f055 | -9.64307 | -37.89487 | 2025-03-31 03:55:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0cc9557a-443f-3862-ab15-931821860329 | -10.69532 | -37.04993 | 2025-03-31 03:55:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dc6c9c10-e5d0-395e-a3a1-134c26d70fb0 | -8.87555 | -36.52749 | 2025-03-31 03:55:00 | NPP-375D | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9e2d1af3-55d8-3a2a-b3e5-14db30f8252d | -9.64363 | -37.8913 | 2025-03-31 03:55:00 | NPP-375D | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 370ec9b5-52e7-378f-b4d3-f53924e31d53 | -8.39133 | -35.02386 | 2025-03-31 03:55:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dbf47713-b566-3b13-8995-1499d3054448 | -11.05773 | -37.10357 | 2025-03-31 03:55:00 | NPP-375D | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e8c9269c-63bd-3234-bc10-f3e47a900534 | -8.5367 | -37.72002 | 2025-03-31 03:55:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 302c10f4-5460-356e-bb9a-51b28fe1406f | -16.68252 | -43.88213 | 2025-03-31 03:57:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e12d891-e237-3bde-b558-c75b1f352db5 | -16.08754 | -41.98142 | 2025-03-31 03:57:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e06f1d21-e3ce-303d-97fc-4056f76980ae | -18.37817 | -47.36285 | 2025-03-31 03:57:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9ab0e52-519f-3b7a-85a6-e96841cfd700 | -18.37734 | -47.3598 | 2025-03-31 03:57:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 308d0875-4cf2-3823-8264-95a4fecb3d65 | -16.63437 | -49.35355 | 2025-03-31 03:57:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03c5dd90-b994-3b88-a2f4-1279b7f5e4ff | -18.48169 | -48.36975 | 2025-03-31 03:57:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b6040aa-b929-3754-b05e-79071b317e7e | -16.63497 | -49.35057 | 2025-03-31 03:57:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ab78aa1-6f6b-3ac5-8c6d-d3fcebd58c38 | -16.34823 | -43.69565 | 2025-03-31 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a4f95b7-b7c6-3e18-b567-dee1607ec2c6 | -17.09394 | -44.97417 | 2025-03-31 03:57:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d11276a5-4d9b-3650-84ba-58370c7fcd94 | -16.63999 | -49.35183 | 2025-03-31 03:57:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dfecb81-0f33-300f-9451-b87afe355a05 | -18.03875 | -39.92426 | 2025-03-31 03:57:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c23b3e9-7d68-3b36-be21-c42958523c32 | -17.75082 | -42.89573 | 2025-03-31 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 328b4e4b-9882-3835-9dd9-124309e4f724 | -21.36112 | -42.65336 | 2025-03-31 03:57:00 | NPP-375D | CATAGUASES | MINAS GERAIS | Brasil | 3115300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2a75bd15-adf3-3f00-aa4a-9c45019e3a16 | -16.04548 | -43.80131 | 2025-03-31 03:57:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ecbf2d0-8c28-31df-89a1-8581b0d3d76d | -17.70442 | -42.83483 | 2025-03-31 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8263ee0a-3c46-3dcd-90bc-708125fdd71f | -17.77605 | -42.80792 | 2025-03-31 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b23c724-2fb3-3fb0-8691-f2794da65bb9 | -17.37843 | -42.48522 | 2025-03-31 03:57:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c294b37c-42cb-3043-a883-27594d5eccf4 | -17.77948 | -42.80854 | 2025-03-31 03:57:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09504158-8005-3041-9109-15cd11d0ce95 | -23.72844 | -51.77552 | 2025-03-31 04:00:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fe8bbe58-a1c6-3f8e-8475-24b83f994081 | -23.59377 | -47.44013 | 2025-03-31 04:00:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ef46aa5-f66e-3e0d-ab93-15606085b1c2 | -23.72915 | -51.7723 | 2025-03-31 04:00:00 | NPP-375D | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eac71e93-a36e-3871-8856-49b0007bc66e | -28.58586 | -49.44291 | 2025-03-31 04:02:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f4022200-06ad-3a3a-81c8-2d44c96bc317 | -9.64404 | -37.89553 | 2025-03-31 04:17:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ade66882-86c5-32dc-9017-b0083641ae18 | -10.82613 | -37.16648 | 2025-03-31 04:17:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df9f69c9-3c87-3a8c-b45d-b6cce9de410b | -17.5948 | -43.19734 | 2025-03-31 04:19:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edb8c086-a8fa-326d-98c7-a3c48b4d7cfa | -19.51312 | -44.27635 | 2025-03-31 04:19:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e9e443f-c3da-3514-a124-fdbaae090afb | -14.4456 | -45.62204 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3cd8c492-de82-3544-b152-f64fa1570a3c | -17.70614 | -42.835 | 2025-03-31 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be640857-dbd1-3b89-9cf9-9b4b364d8ee7 | -17.70544 | -42.83196 | 2025-03-31 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29f0dd33-a79e-3189-99a8-8460c9dd66a8 | -8.39248 | -35.02267 | 2025-03-31 04:19:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 44ff36ed-c124-308c-b0cd-ad69800ffe7d | -5.7939 | -43.62031 | 2025-03-31 04:19:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3631d336-ba00-3cc3-b702-8f307962746a | -16.63855 | -49.35143 | 2025-03-31 04:19:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8da8191-a041-3550-ade3-48e1cb8cfc4a | -15.56822 | -47.85587 | 2025-03-31 04:19:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 56935f40-d4bc-3ea0-9bb8-216e68bee509 | -17.6645 | -46.68586 | 2025-03-31 04:19:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20b07def-adc6-3c13-9599-d62296108080 | -14.44173 | -45.62508 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f616188e-2347-320d-b416-0c1fb134de90 | -17.77872 | -42.80789 | 2025-03-31 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 011d03fa-7fbc-3c44-a0d2-b961a4177e44 | -18.48073 | -48.36737 | 2025-03-31 04:19:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 361314cc-539c-3f1a-8a34-ba885e01cc91 | -18.37721 | -47.35952 | 2025-03-31 04:19:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd579fc2-7191-34d1-8610-37f433a86a1f | -17.00783 | -49.78112 | 2025-03-31 04:19:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3553e4a6-bbb1-3b84-9a50-0f68f34b4f8b | -14.44228 | -45.6215 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19bd96d3-c55d-36c4-8002-542090a1f536 | -14.43896 | -45.62095 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39ca9092-404c-3f8c-93d5-2e16902ab8de | -14.43564 | -45.62041 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eb4cac4-87fc-3f2f-bdd8-85dedaa3dac3 | -18.48407 | -48.36797 | 2025-03-31 04:19:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab9d8560-0e82-3b61-823b-bcff4daa5f68 | -14.43841 | -45.62454 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53e79b80-2075-34a4-8adc-7c4f91a65039 | -17.09473 | -44.97497 | 2025-03-31 04:19:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 502970c2-3320-3055-a3fa-a25dd0536832 | -17.75167 | -42.89288 | 2025-03-31 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23ff3d0c-a3bd-370d-b86b-f0488fa62b5e | -16.68167 | -43.88486 | 2025-03-31 04:19:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58f0d318-3658-39b6-a01d-afbd018361df | -14.44837 | -45.62616 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e70e66d0-dede-3e03-96ef-6f32fdf311ca | -14.44505 | -45.62562 | 2025-03-31 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccd9770e-9a79-3bbc-9b1b-92d91a546f46 | -17.86806 | -44.56358 | 2025-03-31 04:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d50b8cba-0273-3e52-88e0-79b3d6c2d8e3 | -16.04759 | -43.80403 | 2025-03-31 04:19:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0330705f-01f4-3f59-ac39-fcbf3906749a | -23.98608 | -48.91735 | 2025-03-31 04:21:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac0f1570-c28f-303f-a6ad-90e14c9b22f1 | -20.41705 | -43.55355 | 2025-03-31 04:21:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b38cb447-357e-37a3-82cc-ac73a1ef9e31 | -20.41768 | -43.55168 | 2025-03-31 04:21:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0e174775-73d3-3651-9661-d0fad062ee84 | -25.91221 | -49.41078 | 2025-03-31 04:21:00 | NOAA-20 | MANDIRITUBA | PARANÁ | Brasil | 4114302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| af0a0f04-23be-3c4a-9c14-914b1dd3df36 | -20.74531 | -42.52029 | 2025-03-31 04:21:00 | NOAA-20 | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bd4b82fb-5bd2-3075-a33c-ca407ab2c18e | -24.24296 | -50.73833 | 2025-03-31 04:21:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d96b5bdd-385c-3c06-b404-5a47c5711635 | -25.19173 | -49.3278 | 2025-03-31 04:21:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bad0d6a0-9d08-3f0d-bb01-02716c8cbf66 | -23.98277 | -48.91672 | 2025-03-31 04:21:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 97a18398-c764-3060-8426-751bcfb7b751 | -23.72992 | -51.77492 | 2025-03-31 04:21:00 | NOAA-20 | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README2.md)
