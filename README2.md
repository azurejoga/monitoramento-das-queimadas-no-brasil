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
| 85827042-0672-3045-b4ec-53ea41f530c1 | -15.06513 | -45.3212 | 2026-09-03 00:05:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0da27d5e-c3c1-365b-9a33-336695a0c932 | -10.201 | -50.29834 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 5c2780ee-828b-3ba8-963c-a6327246639c | -14.21215 | -42.03266 | 2026-09-03 00:05:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 44.8 |
| eaf90982-c171-35b2-b855-82e67f18787d | -9.6198 | -45.71349 | 2026-09-03 00:05:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| f8eeb8af-338d-368f-aa31-e2ba12ece047 | -18.83437 | -47.60607 | 2026-09-03 00:05:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 8badda21-9b4c-39a2-9145-ccac9c168d9f | -10.48688 | -51.32726 | 2026-09-03 00:05:00 | TERRA_M-M | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 06d6b98d-5d9d-3132-acb5-235d03d20e09 | -18.84441 | -46.44489 | 2026-09-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 6d2ee72f-0dc5-3478-8233-f9b905bbb103 | -17.85172 | -42.61919 | 2026-09-03 00:05:00 | TERRA_M-M | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| db0eade9-6bc5-3e46-bd0f-32430d26e0e6 | -10.55793 | -49.99793 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5b0795d2-c5d1-3d5c-9a2d-d3aa9a3db776 | -11.29128 | -45.18248 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5aad1d71-74e6-3593-beb5-20555eb5f180 | -13.78136 | -49.72774 | 2026-09-03 00:05:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| cbda9da4-9a05-3677-a01d-5d144d6a5231 | -11.00085 | -45.09161 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 1b096a0a-b304-3638-b7a2-677044345edd | -11.76604 | -50.49233 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 0d8b37a6-85fc-34e4-bbe7-7f6e30d54c96 | -19.18747 | -46.84067 | 2026-09-03 00:05:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f675d377-bcc7-3255-9089-2f09a0a918e1 | -10.19978 | -50.28938 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 28466f57-552e-3364-a0ad-b3b3317c5a92 | -10.338 | -51.24387 | 2026-09-03 00:05:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c103a6ef-af40-3988-b86d-beb51bf9f1b2 | -13.40568 | -42.48732 | 2026-09-03 00:05:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 756fa0ab-67d3-32d8-8d8e-5ac902569f7d | -10.53002 | -50.00827 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| bb89c7e5-5fde-301d-80cf-a1e5f07cc637 | -9.15251 | -49.97913 | 2026-09-03 00:05:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a7155480-be6d-3946-90f0-f58cb8571153 | -10.24219 | -47.75862 | 2026-09-03 00:05:00 | TERRA_M-M | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6487ebe7-0a32-35b0-9969-7fa139245d22 | -18.5884 | -48.23549 | 2026-09-03 00:05:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 66450adc-2605-315a-ae67-523639696a38 | -13.39148 | -51.36845 | 2026-09-03 00:05:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 9e14e4b7-3de3-3c78-9058-b2487a96d3df | -10.53517 | -49.98024 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| faf7b8bf-6284-3698-affc-3a3cc79c411f | -13.5358 | -43.30793 | 2026-09-03 00:05:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| dc6a549c-9440-33c9-bd99-4b4d57c3a483 | -11.7648 | -50.48308 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 8dc110bc-05fa-3295-af98-6362d661a594 | -10.22997 | -50.29704 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f11db7cb-a4bb-3579-b154-24e0b78155ba | -10.53395 | -49.97132 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 401da714-5d9a-3b09-8a47-fc7592d3fe03 | -13.40934 | -42.51347 | 2026-09-03 00:05:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 18.1 |
| c36cc692-1b5f-3e18-b552-032cb238c32f | -15.06695 | -45.33296 | 2026-09-03 00:05:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5b15cd46-2420-3ecd-aee7-82a9a6104d29 | -13.40909 | -42.50755 | 2026-09-03 00:05:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 62.6 |
| 8ebf0310-abfb-3cf2-ad42-054c7fbf94e5 | -18.14111 | -51.81706 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4e96d179-fedc-33bf-8274-315387c3df9b | -18.13955 | -51.8043 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4d2d0fd2-e63b-3507-9353-ac53ebd33804 | -18.16722 | -51.79411 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0c2f8e15-4adb-3d99-aee5-3073cb2f253f | -12.39972 | -44.80874 | 2026-09-03 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 7a89bf3a-3e33-3f6a-9232-b57cb9b04446 | -18.76488 | -48.92997 | 2026-09-03 00:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 3b700212-c55c-3fbe-9a53-735a5f6f6e11 | -12.34573 | -48.14185 | 2026-09-03 00:05:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1d211922-926d-3de3-88be-53fe3faed548 | -10.20222 | -50.30731 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f42e331d-56ed-3d59-a575-2bfe884ae2b1 | -8.78127 | -46.48352 | 2026-09-03 00:05:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 67c2c906-ca55-38fa-a09b-8761621d4cc1 | -18.83309 | -47.59681 | 2026-09-03 00:05:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d877c65b-eb4a-31c3-b1ca-4dec2952d645 | -10.87129 | -45.30843 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 2c7c0c90-ce7f-3e22-a825-3a4b1d525661 | -18.76361 | -48.92042 | 2026-09-03 00:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 178.3 |
| dd167d78-566a-3ca1-ae8f-04c1c905bfd6 | -10.16655 | -50.37645 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.0 |
| e3cf1a4f-aef5-3f97-9d3e-c292c1af79ad | -10.56994 | -47.72135 | 2026-09-03 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 64fb7912-fe46-38c5-a5ec-3139320f9a49 | -12.35597 | -48.14971 | 2026-09-03 00:05:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 30a1ed8e-bbf1-319d-ab3e-3afb15d88f9f | -19.09137 | -57.35737 | 2026-09-03 00:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| 04b255e8-1ffb-323e-a569-a0f7365c239c | -10.23118 | -50.30602 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1496253a-05b9-332c-818a-4d3c1019f137 | -12.41269 | -44.82091 | 2026-09-03 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 0e9f450a-16a3-3777-8da7-83077c6995ab | -12.13088 | -44.20381 | 2026-09-03 00:05:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 09984225-e954-3dba-984c-e623ce3a66d2 | -18.53052 | -46.82534 | 2026-09-03 00:05:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 1c8ae3da-7c67-3858-bbe9-64a13a046e0d | -13.41848 | -42.48561 | 2026-09-03 00:05:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 3f5bbd28-fcc1-36ad-8230-ba89f59b90bb | -11.28917 | -45.16867 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7f7c8af5-efa7-3b35-ab82-ca2cbb591f04 | -13.4218 | -42.50548 | 2026-09-03 00:05:00 | TERRA_M-M | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| c226d751-75ef-3a5e-ba50-921af24a7e2c | -12.40189 | -44.82253 | 2026-09-03 00:05:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 53688e8e-e065-3ec3-964a-10c4b89ec6a4 | -11.7725 | -50.47258 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| cec1f185-2de5-3425-bb2b-f0093d54bfc3 | -10.98786 | -45.07926 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| f0e094b3-9df5-3710-99e9-7e933cecc4f8 | -16.75914 | -49.62685 | 2026-09-03 00:05:00 | TERRA_M-M | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f5c4c603-80fd-395f-b168-81a7fbd9dff0 | -18.82428 | -47.5982 | 2026-09-03 00:05:00 | TERRA_M-M | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 18a64d92-cbb6-3e96-a62c-13315e62bb75 | -11.2073 | -45.0177 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 104ba99d-f367-3ed2-9242-0823a2ad6e90 | -18.13783 | -51.8111 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b3fce7bf-b98d-3afb-8ec2-e9b7173fd713 | -10.31984 | -49.95053 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bb266662-ffd8-30fc-b647-ea94f4bd8033 | -11.66103 | -50.53236 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 72d18d91-ebce-3aaf-9680-6c57e1a6b714 | -10.99002 | -45.09332 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 381.0 |
| 1b4b0cac-f50d-3681-bb1e-3f78b86b3a26 | -9.12672 | -40.64719 | 2026-09-03 00:05:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 31.6 |
| ac0ce2c6-543a-39d2-976f-8432c63bc4dd | -18.84342 | -47.14198 | 2026-09-03 00:05:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4557155c-c403-3d92-954d-339b6dfed124 | -8.39217 | -44.98424 | 2026-09-03 00:05:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3beffcab-d254-3f84-a472-94abd1101cbb | -18.15692 | -51.79539 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7203bac0-fa08-30d2-bb98-da46785247b0 | -18.65048 | -47.28665 | 2026-09-03 00:05:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 236e48d4-5081-3884-a0bc-beff40732f9c | -9.15605 | -47.57539 | 2026-09-03 00:05:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| a7ba893b-ff2f-334e-b91f-7543cfd18147 | -18.14961 | -51.82243 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4f705090-2637-3184-bbb5-2636afa7a943 | -10.90536 | -47.28867 | 2026-09-03 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 23d64e4f-0d85-3ea5-97b8-c39c241ff558 | -8.41283 | -44.96586 | 2026-09-03 00:05:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| dd7bc4b0-5f9d-34e5-bd0a-095050153d82 | -9.60981 | -48.55927 | 2026-09-03 00:05:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| a20d27f0-36ef-3d1a-88b7-207be3cffb7e | -11.76233 | -50.46461 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| a71d855d-5d0b-3009-a798-90bb03bf4623 | -18.13081 | -51.81848 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5a8b0c3d-06e5-38d3-a6d2-aae63da568dc | -10.17539 | -50.37519 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 621305b9-094d-31b2-bdf1-89ef260df8df | -17.57461 | -44.96922 | 2026-09-03 00:05:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 53366400-1305-3451-863d-42cfab62cfc2 | -13.2837 | -48.84744 | 2026-09-03 00:05:00 | TERRA_M-M | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a30eda1-1a2d-39b7-be4e-d3beb4a219ae | -13.1004 | -44.49887 | 2026-09-03 00:05:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7601aa0e-1df0-3955-8b62-2aaec928c6c6 | -14.61831 | -41.04638 | 2026-09-03 00:05:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 16.0 |
| c94a6428-a189-3550-a9ff-91535084b000 | -14.60898 | -41.02731 | 2026-09-03 00:05:00 | TERRA_M-M | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.1 |
| c5df4eb3-9b71-316c-9a08-f6a084fa7f10 | -10.20862 | -50.28812 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 26ac0f38-604a-3155-98d8-57f322ae08ae | -19.0946 | -57.39208 | 2026-09-03 00:05:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 5a0067bf-1f9d-369f-901e-f720beb3188e | -18.15841 | -51.80814 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 3aa8cb6b-23a2-3f7a-882e-ba854359c674 | -18.85227 | -47.1406 | 2026-09-03 00:05:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c0476025-38b5-3e2b-850e-d4a53acf5f9f | -10.18424 | -50.37394 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 357ea5ea-ffec-3b67-815c-703d6832c348 | -10.20984 | -50.29709 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 5c56006d-d273-3dad-9631-94f480f56579 | -10.56074 | -47.72273 | 2026-09-03 00:05:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 8609967e-dc3d-3f14-b859-9ec50faafd3d | -18.1393 | -51.82384 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 739a42ca-8eb8-361b-81db-999f622165d0 | -10.5288 | -49.99935 | 2026-09-03 00:05:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e47c38be-ff6a-3fe8-a598-bdaedb9ae293 | -14.08844 | -41.17878 | 2026-09-03 00:05:00 | TERRA_M-M | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 664362ce-ab3f-3805-a095-4d0b9c3bdc12 | -18.16871 | -51.80671 | 2026-09-03 00:05:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 26d6efa3-11d7-324b-b642-1d0b6c3871f6 | -18.83542 | -46.4464 | 2026-09-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 6ddad67f-f8ca-31f1-9f9b-655e4bd1f0a6 | -17.48619 | -47.85107 | 2026-09-03 00:05:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b844a349-5533-37a8-9392-4316f3b0ab7d | -9.60473 | -48.58836 | 2026-09-03 00:05:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48ea8342-3c7e-3879-9f49-d60cf1c6334d | -11.27848 | -45.17048 | 2026-09-03 00:05:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 8ae907b1-bc3a-3dd1-98cd-549abcd3fb53 | -18.51661 | -48.23703 | 2026-09-03 00:05:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 172af6e2-138f-3617-9c46-04c5f3e865ea | -18.83683 | -46.45607 | 2026-09-03 00:05:00 | TERRA_M-M | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bd990edf-eb16-3337-869e-ddeb25322063 | -10.7742 | -44.74265 | 2026-09-03 00:05:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cbca45d2-e35a-30a7-aeb9-58709bd24d0e | -18.75468 | -48.92178 | 2026-09-03 00:05:00 | TERRA_M-M | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| f463893c-cc90-336a-8663-3c08e53cbeb4 | -11.68591 | -46.94464 | 2026-09-03 00:05:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |


[Clique aqui para ver as próximas entradas](README3.md)
