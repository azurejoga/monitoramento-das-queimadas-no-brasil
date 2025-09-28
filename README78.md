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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e991342b-c2b2-39c4-82a6-63705c910024 | -12.98261 | -49.44843 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 801d0bdb-10dc-3390-b7d0-17b8aac9b6c4 | -13.59557 | -47.29729 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f357cd1-7d42-39d8-a176-db4d41f2c5f8 | -13.59008 | -47.31079 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efe54cca-7700-3322-82af-4f9d0e10c3f9 | -14.43342 | -44.88017 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f770b53-f456-39a5-b0e7-10678b9453c7 | -15.19523 | -48.46001 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c4073cf-9b20-3682-837c-6c4115d4cd4e | -12.23209 | -60.85164 | 2025-09-28 04:27:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bc9b580-d4b1-36c7-b7dd-e8b51a3e14c4 | -15.53841 | -56.29688 | 2025-09-28 04:27:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 074b0176-b0dd-384f-9b13-ec05457aff77 | -19.50168 | -41.10577 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.7 |
| 0160b331-a16c-3e51-a19c-7bb769c0d37a | -13.53899 | -43.50071 | 2025-09-28 04:27:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1dcdcfb5-1260-3600-8697-34c0c6e3bf02 | -19.65865 | -45.97288 | 2025-09-28 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4867c40b-dce7-3b68-a2d3-c9e69eeb6206 | -14.76867 | -45.65581 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f41cf61-70e4-35e2-9192-d01f9bc1b41d | -19.4938 | -44.25236 | 2025-09-28 04:27:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f0044d3-599a-30cb-9008-7fcfb29a9f7a | -13.62015 | -47.31213 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a83238e-938f-3c3a-a90e-3556bfab849d | -15.05981 | -42.33967 | 2025-09-28 04:27:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1029ef86-b479-323c-80fc-a95625bec4c9 | -19.2078 | -46.10986 | 2025-09-28 04:27:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a18aefb4-d5e3-322e-b48c-a78d2ceb510c | -20.20813 | -48.68311 | 2025-09-28 04:27:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3bc9000-98d5-3006-810d-a6358f91eaf3 | -15.01299 | -54.98338 | 2025-09-28 04:27:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d97cdbf1-2443-3886-b6ec-07f8895dfeb6 | -13.75778 | -47.86462 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adfc5563-ecbb-347d-a998-86e2ec01badc | -16.28633 | -52.12387 | 2025-09-28 04:27:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 992a672b-bbb3-33b9-982e-45d7a5d70b81 | -13.77765 | -47.8679 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 937d5913-4c86-3c9f-9c47-df228d86041a | -18.18169 | -53.33066 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4805db0-6824-3804-a360-3f1c66ecc2b8 | -19.49686 | -41.10469 | 2025-09-28 04:27:00 | NOAA-20 | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| db9249e0-0afc-3898-9106-3a50ecad1b0d | -15.61126 | -53.17121 | 2025-09-28 04:27:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 05a9b9ee-7274-3052-b6aa-fd13ab3045e5 | -13.39448 | -48.1646 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5b00966-4c6c-3128-9e25-41bc73328ceb | -14.53263 | -48.41885 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93299ea6-9762-333a-8324-c52fe9d782c4 | -19.50657 | -41.69538 | 2025-09-28 04:27:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fca1b6e4-46b1-3a67-9a88-a972535c620a | -15.54939 | -47.89266 | 2025-09-28 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99b47648-8fed-3eac-b0fb-f65cc1f1fea8 | -12.64203 | -51.69192 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37cd3488-53c3-3558-9151-c479edf839b7 | -15.18112 | -50.09784 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a6fda0f-989f-3540-9f98-be25bad11f84 | -14.32277 | -47.09081 | 2025-09-28 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 083ec159-c63a-347d-b77a-98b43e4d98d9 | -17.18374 | -43.39333 | 2025-09-28 04:27:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8c9e8ad-f73a-3ba6-b9e8-922017d2c408 | -13.40442 | -48.16624 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 287aeb25-3876-31d1-a3d5-1f7d555c1cc2 | -14.42982 | -44.87963 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07486af0-90a7-3348-82a8-dcc8f77959b3 | -13.26351 | -48.45235 | 2025-09-28 04:27:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdd141ce-3a4e-3ed0-bb21-c375938ef1ba | -14.20469 | -44.60063 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efe83a96-2577-30c4-aa14-f6c709d6d744 | -13.60275 | -48.0938 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea0ca11d-ae12-3425-9605-b494d9c6ca5a | -15.4399 | -48.24434 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 493c999f-463d-3598-b8d5-9b5a4dc2ce33 | -15.31592 | -47.88763 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f0cd3ad-00b5-3c1c-8c0b-391b98709ede | -15.84109 | -56.39906 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 012492e1-e1aa-37de-b3d4-6c82124fc4b4 | -12.97983 | -49.4441 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16458706-12f6-3147-a4bd-e84344a92c56 | -18.18267 | -53.32524 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7a5686b-83fd-3177-b3a9-53b87072ad7a | -13.60335 | -47.29114 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2723e779-80b4-324d-a050-7f3b59c33ca0 | -19.32644 | -43.81325 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 522ab28c-7114-384d-aadd-70b12132035d | -12.32234 | -51.51712 | 2025-09-28 04:27:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6a1c9e1-5f9e-3d79-ac32-3d6e07bd911a | -15.15259 | -46.4174 | 2025-09-28 04:27:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f11c2b1-6403-34dc-b748-5e1efce4b349 | -13.7848 | -47.88724 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1146476f-73a0-345d-b6c1-b0a85b742e60 | -15.02928 | -47.043 | 2025-09-28 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc44eb6-5d08-3f26-85bb-653343adfb91 | -12.99409 | -49.4424 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2f59450-c48d-39f4-af9f-372e4d15b371 | -13.5945 | -47.32609 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c137f47-3a56-3eb7-b3e1-93b8276d82c6 | -16.9594 | -53.70364 | 2025-09-28 04:27:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8ba7c066-df8c-372d-bdd3-851b649b93ea | -16.40552 | -47.01866 | 2025-09-28 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a33a6e34-525f-39ff-ae01-96a6fc9e3648 | -19.94358 | -41.65395 | 2025-09-28 04:27:00 | NOAA-20 | CONCEIÇÃO DE IPANEMA | MINAS GERAIS | Brasil | 3117405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f28c10ec-0b81-35e1-96ce-21e4ae472d96 | -15.89908 | -46.21668 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5761599-9a8a-376b-aec1-6c298dbd60cf | -15.81076 | -56.42649 | 2025-09-28 04:27:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3cbcc108-bea5-3d1c-b386-a7fbad14a668 | -13.60167 | -47.32368 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3231950b-d051-321d-abd8-4b1f86165547 | -17.72323 | -46.7131 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f9f0a5a-5894-378a-b2f6-8c216b2b8478 | -15.27781 | -46.4207 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c14f531a-99db-3471-9422-bc416890c378 | -17.72895 | -46.69796 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48269df2-12bc-3ce0-982e-aa4295fdaf44 | -17.72093 | -46.70473 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5cf7e4e2-6934-3be0-b93d-0d2e9e05d84d | -13.70623 | -48.33944 | 2025-09-28 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1283166c-6d49-316d-b71b-c8d1bbbce1dc | -15.33636 | -47.88736 | 2025-09-28 04:27:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0bc0d03-fb6a-3fb5-9ba4-ea12b24f7f62 | -12.99531 | -49.43494 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13855409-dd27-30c6-bfd4-b0ff7822ca05 | -15.44659 | -48.22348 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6de3a78d-0b09-360d-bab0-2dde1506b5a4 | -13.65028 | -48.07258 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20de7205-da92-35c1-a9b5-7b373d54386a | -15.4344 | -48.23609 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a4bef2f0-57c7-3e1d-8006-93dea44fc0ef | -17.72724 | -46.70974 | 2025-09-28 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad3613f8-3f4c-3afd-873c-2f8fa73ee047 | -13.58677 | -47.31023 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d1ca26a7-9774-3f4f-b04a-588e28e96bbf | -15.28295 | -46.45651 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 169f7444-e783-3fae-8ec9-b46f88912171 | -14.59173 | -48.2609 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55a68f62-0a8e-30cd-a990-c33343bfb0d4 | -12.63987 | -51.68184 | 2025-09-28 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de9d914b-a7fd-3953-b130-07e1f3b5ad5f | -19.3128 | -43.82301 | 2025-09-28 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60d654c1-941e-3fdc-95e6-2748f6237cb2 | -18.20255 | -53.3245 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 397ae48b-917c-3b00-9b4c-64caf92b25eb | -14.53651 | -48.41583 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b241ab9b-86c7-3bce-b88a-e1197d812a79 | -13.02282 | -49.45899 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e259667-114d-3d67-b72b-1fde4fd8385c | -15.28688 | -46.43011 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 086fd063-9c49-3402-b87b-7acc47a9d857 | -18.17788 | -53.32987 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2af170e1-72c2-3b6b-a01c-09414e73682f | -14.82268 | -45.67652 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7040bcd3-95eb-3e8a-9012-848f7115c0de | -15.21747 | -48.06178 | 2025-09-28 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb916edb-28a6-3159-adcc-6637654f388c | -18.17507 | -53.32362 | 2025-09-28 04:27:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ed4cb406-9f4f-3460-b608-af639301e5f7 | -15.2417 | -46.45081 | 2025-09-28 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e35e9b4-03e8-3ef9-a66e-27ef46b2a159 | -14.44299 | -46.36652 | 2025-09-28 04:27:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27a7afcb-b293-3e9e-baa6-9368636585d5 | -16.7789 | -49.34734 | 2025-09-28 04:27:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed140544-e3dd-3892-9a34-32fbff374090 | -14.38571 | -54.94559 | 2025-09-28 04:27:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7ff0d63-3805-3277-909d-f0339b6cade0 | -13.60767 | -48.10556 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be3cb7db-bf01-395d-8812-543eb6919f98 | -15.2958 | -49.48391 | 2025-09-28 04:27:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a252d2d6-fb13-3696-ae1f-172ad428b956 | -13.29351 | -50.68983 | 2025-09-28 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7004b8d-7da0-35dc-bccb-bfb8d5fd42ab | -15.63234 | -43.00731 | 2025-09-28 04:27:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b98730c3-95eb-39f8-b8f8-70087e3019b0 | -15.26848 | -51.47321 | 2025-09-28 04:27:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1fb002c-220e-3640-a665-d4a5a8eb56c3 | -13.61992 | -48.07122 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf210b1f-0836-3806-b13b-8bf37e53651c | -14.89403 | -45.56416 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a25b6bf8-1fb9-3cc2-866a-845666b3cd10 | -14.53982 | -48.41638 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3dec2699-730d-3fd7-a3c6-ee26f756f7e8 | -19.66227 | -45.97342 | 2025-09-28 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6611c00e-4d3f-3783-ac73-315145092555 | -14.76984 | -45.67214 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef4e2236-0395-31bf-97a5-bab256b5bc61 | -13.62183 | -47.30128 | 2025-09-28 04:27:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3750e9ee-a86d-3362-bf60-e1a91567b4f6 | -14.53925 | -48.41993 | 2025-09-28 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e72622e5-855d-35d8-8d06-9909dc0c0b52 | -14.81879 | -45.58229 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc86a4d0-4434-3ab9-ab00-97518256b330 | -13.02219 | -49.46288 | 2025-09-28 04:27:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5720b052-73e7-3bc6-aed3-a4735604035a | -15.6756 | -46.26214 | 2025-09-28 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7197d33f-1629-39a5-bdcd-e0fff38c1fcd | -14.88935 | -45.57167 | 2025-09-28 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bee44a26-cbcf-3643-ba15-d7a98d6b17df | -13.71396 | -47.58217 | 2025-09-28 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README79.md)
