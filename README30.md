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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 710fa9d8-daaf-3159-83ad-7ee12ebd029f | -14.1217 | -44.8699 | 2025-08-11 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 8deccc21-5fcf-35f1-b00b-cc9979872310 | -14.1212 | -44.8933 | 2025-08-11 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e2cda44b-123c-3000-9166-f36c474c9952 | -14.1297 | -45.4043 | 2025-08-11 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 10d58421-1852-3134-b511-0ed162b40571 | -14.1217 | -44.8699 | 2025-08-11 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f83f9cfe-2edc-3ce9-bf28-db30820eae07 | -14.1103 | -45.4077 | 2025-08-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 0ac70618-e025-3443-b242-dbf325307079 | -14.1108 | -45.3844 | 2025-08-11 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 47791d14-0b46-3293-aa2d-86653749e7b8 | -9.00054 | -47.46604 | 2025-08-11 12:51:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| e71f6304-42ae-3b02-ae38-d3cb13d33a83 | -9.00701 | -47.4462 | 2025-08-11 12:51:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f4259ae4-1834-3d69-b7a6-bffb67bee0d1 | -7.40326 | -59.99234 | 2025-08-11 12:51:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| b523de2b-7aeb-3a80-81c2-9b3706b406d2 | -3.17952 | -48.8019 | 2025-08-11 12:51:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| a0f7033c-2f24-3b91-9780-e85de3ef8eb7 | -2.44945 | -47.32676 | 2025-08-11 12:51:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3b2942e2-7983-3c8c-875a-bab6bef2ca28 | -9.00376 | -47.4403 | 2025-08-11 12:51:00 | TERRA_M-T | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7dbc8bc7-536f-3ccb-b912-d5f46bb639f6 | -8.79664 | -52.05623 | 2025-08-11 12:51:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| eec7d086-85c4-3755-a1d5-f2b44ca6020c | -11.54518 | -50.56861 | 2025-08-11 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5284a0eb-d209-3ccd-8b3c-7faac67911cd | -8.56135 | -54.69857 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 07b40ee5-c3d9-350c-8902-fe4dfc5efab7 | -10.62341 | -54.59195 | 2025-08-11 12:53:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75772503-1803-3a58-9c3e-460a4bb6d707 | -11.76605 | -49.12183 | 2025-08-11 12:53:00 | TERRA_M-T | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 23a9034a-3f5d-38fc-ac3b-cf076cc46875 | -8.57019 | -54.69982 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0f989fac-bbb2-3333-991c-9931c39860d1 | -8.57274 | -54.68201 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 45775011-aed3-3e94-a972-6a277073efa4 | -8.93229 | -60.74313 | 2025-08-11 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 979c5000-3288-3be4-a948-031566b8931c | -11.544 | -50.55791 | 2025-08-11 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 08748d6e-4d9e-3a2b-9b90-83f69770eca9 | -12.31741 | -50.05842 | 2025-08-11 12:53:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7b3b4151-b1c7-356f-8fbf-fab1ed83808c | -9.92042 | -52.42864 | 2025-08-11 12:53:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 06a9a711-f889-39d3-bcc5-02a3c1a68c01 | -11.00828 | -55.06602 | 2025-08-11 12:53:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 54b365c2-5cee-3f77-915a-731f1b23e4f3 | -11.71351 | -50.10964 | 2025-08-11 12:53:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 0c059441-0d52-3b68-abdf-94748eec29b1 | -8.57146 | -54.69092 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 23e6bad7-384d-3c26-b890-d4b198f92681 | -12.61125 | -47.15921 | 2025-08-11 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 10192e3f-a7e2-3a42-b065-57e5b72b00c5 | -11.5336 | -50.56716 | 2025-08-11 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e962d0dc-abd8-30cc-884e-be065bd0a6d2 | -8.56517 | -54.67186 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ea7b56e7-a633-33da-a393-adb45384ff37 | -12.63748 | -45.35189 | 2025-08-11 12:53:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 6d4211d4-1537-3193-90f7-2885d71e8e33 | -8.93495 | -60.72637 | 2025-08-11 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ea48f5a0-f5d8-36e6-8f2f-e7a6e95fdb32 | -11.12771 | -50.50774 | 2025-08-11 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8f4c5c0b-a8b3-3fd4-a395-0922117ac225 | -12.61459 | -47.12841 | 2025-08-11 12:53:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 5a81fdb9-210e-3000-b70a-6d65ff98f364 | -9.37217 | -61.52725 | 2025-08-11 12:53:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| c572104f-fe32-3d3a-8d6a-f256f16dc13c | -8.56262 | -54.68967 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f8ec075c-a962-3de6-a58f-c7982c646a0b | -11.75366 | -51.61808 | 2025-08-11 12:53:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0e4325b6-b108-3962-bc06-6781a992b2c4 | -15.33866 | -46.06711 | 2025-08-11 12:53:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 300ca475-52e9-316f-af0d-adcf1f99a808 | -11.12207 | -50.45833 | 2025-08-11 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 0812a004-a16d-37d5-86f8-7cf7f4c647f3 | -8.5639 | -54.68077 | 2025-08-11 12:53:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0a77f428-9424-335a-a817-e344094ccd59 | -11.11192 | -50.46695 | 2025-08-11 12:53:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e70b1f5b-7030-3275-9ef4-c2633d263beb | -15.34061 | -46.07218 | 2025-08-11 12:53:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 5c1a2a59-f7b3-3b75-9ca5-abb9d0d9112b | -10.93462 | -49.41373 | 2025-08-11 12:53:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 60e343c4-755d-3a3d-b41e-ad7f6f958a5c | -15.41428 | -53.89896 | 2025-08-11 12:55:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4668ad9b-8d68-317f-b5f9-2a0fd3f19021 | -16.29678 | -52.92188 | 2025-08-11 12:55:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 7b2b4f22-1cb0-3ef1-95a4-372237281d7e | -15.43486 | -53.9194 | 2025-08-11 12:55:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a6ce6e1a-2b2d-3d3a-bc04-609733df18de | -15.44448 | -53.92074 | 2025-08-11 12:55:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 804dd8a6-c01b-3e4a-a2bf-626d017cbdf9 | -15.43208 | -53.91255 | 2025-08-11 12:55:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c789e64d-3122-34dd-880a-2778b2396688 | -18.91214 | -47.56187 | 2025-08-11 12:55:00 | TERRA_M-T | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 01df78b2-6e46-336d-8dd4-8e3685396371 | -16.29836 | -52.9095 | 2025-08-11 12:55:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| cd78deaa-a90c-3092-9b63-1e8565957f2a | -16.29414 | -52.91518 | 2025-08-11 12:55:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 40283b48-eefa-38b4-ae00-e4c18f4ea728 | -16.88166 | -52.00816 | 2025-08-11 12:55:00 | TERRA_M-T | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 06f16544-1932-3aac-9acb-63660b064cb5 | -15.42245 | -53.91122 | 2025-08-11 12:55:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 1e018929-d5d0-3274-8fc1-0e22c6162540 | -21.11456 | -48.80652 | 2025-08-11 12:57:00 | TERRA_M-T | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| 3d3f0335-8f5b-37d1-b2f8-2a074ad87150 | -21.3061 | -48.67609 | 2025-08-11 12:57:00 | TERRA_M-T | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 81eace1b-3d87-3e81-8ee3-fab7de9c1686 | -21.30334 | -48.70859 | 2025-08-11 12:57:00 | TERRA_M-T | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.4 |
| 4952334b-dbc5-320f-ada4-566e0aea740e | -21.11772 | -48.80031 | 2025-08-11 12:57:00 | TERRA_M-T | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.3 |
| 68922792-d4e6-3818-bc01-0d7f02f0268c | -21.12071 | -48.76826 | 2025-08-11 12:57:00 | TERRA_M-T | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| e23cd61e-5ba3-31c9-87f3-f94156a041a7 | -21.11731 | -48.77462 | 2025-08-11 12:57:00 | TERRA_M-T | ARIRANHA | SÃO PAULO | Brasil | 3503703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 81.7 |
| 4f02526d-1d67-3f56-a90e-4e6212f93259 | -21.30746 | -48.70235 | 2025-08-11 12:57:00 | TERRA_M-T | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.6 |
| a273e369-ce4d-314d-bcc8-6f73c1a95a42 | -14.1212 | -44.8933 | 2025-08-11 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| c265165b-54bb-3a79-9925-54f90e0cadae | -14.1217 | -44.8699 | 2025-08-11 13:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 390cbaba-a3bd-37e7-96f5-92a69a61c6bb | -14.1297 | -45.4043 | 2025-08-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| b5f04363-cd1e-34e0-b305-2792a8def9e6 | -14.1108 | -45.3844 | 2025-08-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 6f0c1f6e-fb5c-3080-9d49-7c8addac6eb1 | -14.1103 | -45.4077 | 2025-08-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 22174a25-2bdf-3709-a3fc-b047077dc29c | -14.1297 | -45.4043 | 2025-08-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| dcef6382-ef42-359a-9c25-bc0c2f3971fc | -7.0614 | -59.1972 | 2025-08-11 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 215cca98-9322-33e2-8da8-216fe2f443f2 | -14.1108 | -45.3844 | 2025-08-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| d2b41ade-c863-3fea-a217-1034a5b6414f | -14.1212 | -44.8933 | 2025-08-11 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 96e07a0f-b905-322a-b8c8-aaa7428f4864 | -14.1103 | -45.4077 | 2025-08-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 36052bd2-bd44-302d-a751-22d19eafc570 | -11.7278 | -45.0274 | 2025-08-11 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bfab3d08-e07f-3c81-9423-1655000ffe28 | -14.1108 | -45.3844 | 2025-08-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 262140dd-dda7-3abb-a66a-0565d7885cfc | -7.0614 | -59.1972 | 2025-08-11 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| bcd246a2-f11e-37ef-8fe6-a91806f7648c | -7.0799 | -59.1964 | 2025-08-11 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1cd92086-f462-30b5-a8c4-e88143c26fd2 | -14.1103 | -45.4077 | 2025-08-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6b00efd7-bb4d-3588-98a0-db5e9a4a19f3 | -14.1297 | -45.4043 | 2025-08-11 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5c6ada38-d630-34f2-8fc3-5c40486eb22a | -7.0614 | -59.1972 | 2025-08-11 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7a7c0df3-2e02-3fa4-b179-9ad39b3962bc | -11.9224 | -44.8597 | 2025-08-11 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 84024bc0-90e9-39c2-99b5-06db50ce63dc | -14.1217 | -44.8699 | 2025-08-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 18a453a7-0b3a-33de-acc2-f312ec446695 | -14.1212 | -44.8933 | 2025-08-11 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 024904fc-0c90-3ffd-b3a1-3ac790208a72 | -14.1297 | -45.4043 | 2025-08-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 820885a0-9133-3ca3-88e1-a7d1c6c336a6 | -18.9111 | -47.5671 | 2025-08-11 13:30:00 | GOES-19 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8fddd191-cbb7-3f35-ab87-2925bf8f020d | -14.1108 | -45.3844 | 2025-08-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 8a634c50-6e1a-3d17-984d-00a2e55fdf52 | -7.0799 | -59.1964 | 2025-08-11 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3fafc2ae-51ee-3951-a60a-1e36073ae7e9 | -14.1108 | -45.3844 | 2025-08-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2e8b3e80-ae61-3739-a824-e2df3f23c4bc | -7.0614 | -59.1972 | 2025-08-11 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 885e66b7-97f2-3b5a-83d0-907d32cf5afc | -11.9224 | -44.8597 | 2025-08-11 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| cf67090f-78e2-33bc-b8e9-3131eeb8c158 | -11.9032 | -44.8626 | 2025-08-11 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5d45df7f-86d9-3bb7-94f7-724e69274da0 | -7.0799 | -59.1964 | 2025-08-11 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 86c9c756-2ee8-3f35-b558-ba22d1bacbdf | -14.1297 | -45.4043 | 2025-08-11 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| cdf5481b-6b82-3448-b705-107c96233589 | -14.1212 | -44.8933 | 2025-08-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| fb2c3d98-d142-38af-8cb9-cb566cce798b | -14.1217 | -44.8699 | 2025-08-11 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| e7ad6bbc-043d-34a5-a5d6-908ea698664b | -8.579 | -54.696 | 2025-08-11 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| bbd1ec11-88bd-3606-aa63-ab78f0015191 | -19.5627 | -46.5815 | 2025-08-11 13:40:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 109.7 |
| e5d7a01f-425c-3bb9-aca8-ac07fb4bedc8 | -7.0615 | -59.1779 | 2025-08-11 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a82ac6bf-8c79-351b-a5db-33740f5a3057 | -9.864 | -43.5407 | 2025-08-11 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| c22de5c9-e5b9-3608-91af-87f83351a83d | -7.0614 | -59.1972 | 2025-08-11 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 89b27648-d128-355f-bf7b-d9a484912670 | -7.08 | -59.1771 | 2025-08-11 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ced8e195-a521-3303-abc3-99a650070467 | -7.6113 | -45.2026 | 2025-08-11 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 58efa9fe-9f0c-3b52-8bd7-c9b5d305f37b | -15.4407 | -53.9258 | 2025-08-11 13:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 31538d06-6450-397b-8dc1-53d03d31e6cf | -11.9224 | -44.8597 | 2025-08-11 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |


[Clique aqui para ver as próximas entradas](README31.md)
