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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e6fa584-1dda-36ee-be03-5c8682ffbadd | -13.12737 | -46.84878 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ba7a9f6-4dcb-36ab-b87b-4912664496f6 | -18.69519 | -48.18212 | 2025-08-15 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d8ae5cd6-33c1-3d10-80a3-f4d25a34eba9 | -13.63827 | -46.9172 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 342499e9-058d-35ce-a86a-ddd673286ad3 | -13.57958 | -46.96712 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dbb432a-9916-3705-aac2-8c11a6ffbe31 | -15.58296 | -47.32351 | 2025-08-15 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0154c94-f582-3f60-a920-a7fc9b76e45b | -14.07012 | -46.31533 | 2025-08-15 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0c076b46-32c5-3933-9f43-25c65f264b25 | -11.53393 | -47.25045 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 952f7931-647b-3972-ac4d-512f51f36fa5 | -12.5834 | -46.95922 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 78cec2b7-1987-3533-aa02-746c94962109 | -19.3714 | -41.75296 | 2025-08-15 04:04:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6bd87228-a721-3e15-8a64-693bece196ee | -12.68229 | -44.95842 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12e02049-33bb-32d3-8aec-b800b83c7ad8 | -18.94615 | -48.18463 | 2025-08-15 04:04:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 267bdc43-16a6-3d63-a2ee-4b80d7e161bc | -12.58753 | -46.95977 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f41d351b-eec1-347c-b4b9-d98e0375a2a8 | -13.15311 | -46.86768 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12cd936c-9bed-3e52-9146-772021a9c345 | -16.39296 | -50.91018 | 2025-08-15 04:04:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b2a76669-9e75-360f-b595-43c70afa5331 | -14.06112 | -46.29866 | 2025-08-15 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eecd16d0-c7a5-3f96-9b87-dc83ef55f8f9 | -13.88855 | -45.55791 | 2025-08-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14916bb6-191f-3ed8-a76c-35e912c17063 | -11.34342 | -55.41969 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ce482620-79e3-3481-99e1-c01ed45f3e3c | -14.04872 | -46.30161 | 2025-08-15 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e088d9a8-7213-30fa-9e82-559e9e8e8fee | -13.38229 | -44.3104 | 2025-08-15 04:04:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c785a7e2-4df6-3164-8391-60b99421db25 | -15.3231 | -51.5132 | 2025-08-15 04:04:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd5edd6d-8eae-34ee-a15a-9076ece16f74 | -13.88486 | -45.55722 | 2025-08-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57e6e6ab-a88d-32b7-937b-155454d338f0 | -18.69917 | -48.18296 | 2025-08-15 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 1316269d-85d6-3d9b-937a-c8b6387fa32a | -11.35609 | -55.4297 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 35b6846b-b52e-3e07-b8de-6d8d6bf4fb54 | -14.35381 | -43.19286 | 2025-08-15 04:04:00 | NOAA-21 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d6f4937b-6f5d-35e9-bc9d-ba47e172ab3c | -17.59571 | -43.19945 | 2025-08-15 04:04:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63d3dc8c-fa9f-3f77-808b-dbc052356c8b | -16.3781 | -50.9072 | 2025-08-15 04:04:00 | NOAA-21 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bc67711-b806-3f1a-964c-cff5ec109412 | -11.53749 | -47.25024 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a89d8b1c-18fe-32a9-b50c-96489cb6e1d2 | -13.32145 | -45.22274 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 974c43c8-71ab-3169-acbe-a89f53037aa2 | -19.11568 | -44.46909 | 2025-08-15 04:04:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad43521d-70e1-36c7-8b1c-bef4e268f002 | -19.45388 | -45.30717 | 2025-08-15 04:04:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5de6a21-784b-37f0-ab6d-7af4ee155af8 | -17.05647 | -51.79286 | 2025-08-15 04:04:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75f74e73-8f2c-3f19-ac79-f362e27c6a75 | -12.68593 | -44.95907 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 087a1edb-f5ee-34d8-ac84-3df8344fc378 | -12.49216 | -47.02594 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba24063f-4004-37f2-8dd8-9e3a675ebb01 | -12.76182 | -44.41441 | 2025-08-15 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 40f93668-4614-3731-81f0-89d0cd0fe2c4 | -11.35885 | -55.43464 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c856d85f-d937-3819-a1d8-f0ea1f4ee0fc | -12.582 | -46.94353 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dbefe287-488e-3193-a2a1-b8f3f1401b76 | -13.3309 | -45.23346 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ca0995c-aa25-39aa-97e5-263ff7f30ffc | -12.75406 | -44.41728 | 2025-08-15 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0beb07dd-75a0-3d77-8449-1114135de0ff | -18.44498 | -41.83944 | 2025-08-15 04:04:00 | NOAA-21 | FREI INOCÊNCIO | MINAS GERAIS | Brasil | 3126901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3095f562-e29f-39c6-9078-e0a6a3a96c21 | -16.30639 | -52.92577 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fa094047-7461-3fbc-b2da-d18abf9f7117 | -12.59092 | -46.96449 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 89b5a4e1-6cea-358d-9806-a71896429dfb | -13.89148 | -45.56308 | 2025-08-15 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b752eda-d759-3424-b007-6ad47093669c | -19.53081 | -41.95559 | 2025-08-15 04:04:00 | NOAA-21 | SÃO SEBASTIÃO DO ANTA | MINAS GERAIS | Brasil | 3164472 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b86cb990-a131-312c-910a-fe9ca07dddb2 | -13.328 | -45.22842 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1e676fcb-738a-3d4d-a431-3b1af0eda41b | -15.9353 | -48.15707 | 2025-08-15 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8f93ca0b-c9a3-316d-aebd-18ee6ce35c5a | -12.79416 | -45.9734 | 2025-08-15 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c03a3af6-37a0-312a-a9d4-f30f6f883507 | -17.64705 | -44.50218 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83dafa86-46e9-38d5-825c-4f79a3a8cbb3 | -17.64561 | -44.48972 | 2025-08-15 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78b6531c-7c82-3cdf-8267-d64ede1375b3 | -17.50099 | -48.00719 | 2025-08-15 04:04:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7faa7764-37ea-3540-86f5-c53d04d76202 | -11.3545 | -55.43715 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5425b75-e47c-35f9-8669-710cb673e825 | -13.32586 | -45.219 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c44fa433-42d3-32aa-b7c3-e38e746fe1d1 | -13.12663 | -46.84862 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bc78aa2-5cfa-3f4d-b2fc-e7af1bf4b1bf | -19.78321 | -43.73252 | 2025-08-15 04:04:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f50c89f8-fe71-3227-bceb-707079a55af6 | -19.78753 | -43.68415 | 2025-08-15 04:04:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d9b0d0d7-64ec-30cc-a370-4d855140d983 | -14.24123 | -44.58193 | 2025-08-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 09683920-0958-3934-9b74-16535111afd2 | -13.56791 | -46.96253 | 2025-08-15 04:04:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7770b707-4a79-3ffa-b7da-38d1b77124af | -16.4737 | -51.98346 | 2025-08-15 04:04:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd8935c8-e0c2-38b4-8ac4-290c8926a712 | -16.52563 | -44.93787 | 2025-08-15 04:04:00 | NOAA-21 | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76e36e0f-3e07-3989-a68b-f8039450362d | -20.00942 | -42.20218 | 2025-08-15 04:04:00 | NOAA-21 | VERMELHO NOVO | MINAS GERAIS | Brasil | 3171154 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2322b76e-6e3c-3a65-bc75-495974d007d3 | -15.13473 | -43.96308 | 2025-08-15 04:04:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6fb7e6e-8fab-30b6-8e91-64aa93db10cd | -12.41809 | -43.49111 | 2025-08-15 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66853a10-86bb-3dc2-ade2-62c5ff0c3406 | -11.35175 | -55.43314 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 41242aa8-691a-3f4b-9f1b-2178c03d995f | -19.475 | -43.61796 | 2025-08-15 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61861b77-6b82-3180-b428-5b71d7f1efcc | -11.36185 | -55.4201 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5d098e6e-b355-3f11-b177-d7ff3e0d8b03 | -12.49486 | -47.01075 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10711eea-13c9-3ef0-90c2-16fd9a9d3bd3 | -15.89268 | -50.17146 | 2025-08-15 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| da81dc76-9404-3157-acc6-2793c59586ec | -16.60968 | -40.99204 | 2025-08-15 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 754fb38f-38e9-34a5-ba1e-0b73a60f2ff1 | -16.30277 | -52.92987 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f0b64183-7ff7-3a71-a6f8-3d34b2556f0e | -16.37248 | -41.37826 | 2025-08-15 04:04:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0bb5e57f-fff5-3c23-8680-fc58acab54b7 | -15.66883 | -56.3808 | 2025-08-15 04:04:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a0bd321-0195-36ba-b083-c5b6676826c7 | -11.34619 | -55.42427 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ef8e3b7f-d303-3ae2-805f-7024f8ec6a2f | -18.29794 | -49.54973 | 2025-08-15 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 63840b1e-af54-32dc-b4f3-87b6f686a3f9 | -12.50788 | -47.00917 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98aaf247-9e81-3d43-b832-8ba5a95b0e15 | -12.59559 | -46.96196 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 240dca1b-bf0f-3ae1-b203-5216fb3c5114 | -13.15026 | -46.86036 | 2025-08-15 04:04:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf1a1419-a217-3e72-924e-935a1cf445d7 | -11.54881 | -47.26046 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca91783c-13d7-3c05-b3fc-dbaaa4fa9b57 | -18.51253 | -42.08906 | 2025-08-15 04:04:00 | NOAA-21 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 46453552-9f19-371b-aabd-b7826e0535e3 | -17.36259 | -44.13769 | 2025-08-15 04:04:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 107b197e-6cf1-3613-930d-54d07efed347 | -12.57723 | -46.94654 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8be73be0-703d-3692-83be-af7c69c334b7 | -14.90935 | -45.18909 | 2025-08-15 04:04:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52b87e49-652c-3e8c-afac-c553383913b6 | -11.45351 | -47.33258 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b6972d6-5a5b-3e1c-a501-53c2392e15f0 | -15.89155 | -50.17716 | 2025-08-15 04:04:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| c0b1790c-97e8-38f2-ba83-ad143c3a2842 | -12.50855 | -47.00537 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26ab98bc-aa1f-3f2a-87c3-fe9819b91064 | -16.69629 | -41.01361 | 2025-08-15 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 118eabd5-c8f1-3d98-91f8-b82d24ed0e51 | -18.29882 | -49.54527 | 2025-08-15 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c9d973e6-5bc9-3eca-9a08-c66148b04249 | -12.58544 | -46.9479 | 2025-08-15 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d31f99ef-6f6a-37f0-b517-4c3fad84a571 | -18.5092 | -42.08849 | 2025-08-15 04:04:00 | NOAA-21 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 19572397-f777-3d9c-a084-47fdb5441518 | -17.74973 | -42.25847 | 2025-08-15 04:04:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a30655c7-1410-30f7-9919-def4332f3acf | -17.49813 | -47.83942 | 2025-08-15 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53f4b108-d8fa-3aa5-bf58-736d5e5e91a8 | -12.43418 | -47.88029 | 2025-08-15 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a37db4-8e2c-384e-b1ca-05dcd53dce40 | -11.3521 | -55.4137 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a7af4cfb-53e8-31ce-84da-9636e1d79382 | -13.32725 | -45.23281 | 2025-08-15 04:04:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0d0738e8-eee1-3489-81fe-3867081f1736 | -17.49879 | -47.83583 | 2025-08-15 04:04:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45cc5466-0488-33c6-8e52-ee6b4d704ed3 | -15.95586 | -48.09099 | 2025-08-15 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9718d52e-25c7-3133-b2c6-eef918d1c210 | -14.23705 | -44.58534 | 2025-08-15 04:04:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 39e9aadb-d5c3-3bb7-99c8-7ddb932a6764 | -11.54734 | -47.26858 | 2025-08-15 04:04:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c5717ee-cfe3-30c8-b7e9-ccc725c57d5a | -16.30737 | -52.92116 | 2025-08-15 04:04:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5bd63691-777c-399c-bc5e-13061dab6140 | -19.4756 | -43.61427 | 2025-08-15 04:04:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd341053-27e7-3aab-b5e0-727155de3b72 | -11.35915 | -55.41534 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 34831ad3-fe11-3ca1-bcf7-df9eb48cc2a8 | -11.34918 | -55.40985 | 2025-08-15 04:04:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README25.md)
