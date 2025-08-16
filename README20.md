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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2093c297-a859-3840-b162-0006acf22201 | -8.17437 | -45.01996 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b3b4f28-3353-3dce-8794-19db68962429 | -9.17913 | -45.32071 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56699bde-fb88-37f1-9809-819a8f4212e4 | -13.10565 | -46.84822 | 2025-08-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d05b3ac-a101-33d3-a136-8bf5cb1e1349 | -13.5762 | -46.97987 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cd82e5e-dbfa-3a32-8359-26e84520b319 | -12.82508 | -46.01086 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 562b55dd-b42c-3385-b0cb-533ba30a26c8 | -8.2921 | -44.96714 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7f3db53c-f007-356f-bf30-c801f2cc6fbd | -13.67181 | -45.89503 | 2025-08-16 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54016d19-6e7e-37d7-a8a9-2f789c2af638 | -9.7039 | -46.26672 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 463af21b-70fc-3610-bb53-c8ee5da54d54 | -9.80593 | -48.53985 | 2025-08-16 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed7da11c-8876-3d6e-b4b9-f72a8bddf8c2 | -12.60251 | -46.96411 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7c8115eb-adf4-3846-a22f-e409c9281733 | -12.83091 | -46.00884 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08e133d4-aa72-3cd8-a4e4-c594d177442a | -9.70319 | -46.27054 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b512e23c-0500-3d81-a0ca-55a5b79974cf | -13.87096 | -45.5554 | 2025-08-16 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84beed70-fbb4-32c7-8051-d78335a4be1b | -12.56445 | -46.96067 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ee827c4d-1bec-3e3f-b845-ec8ce48035fa | -13.57596 | -46.97984 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a68281ea-8908-3c08-a689-4a2bffbf1a9a | -12.62017 | -45.22354 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9665c66c-a000-3999-9917-79319ad26198 | -12.45307 | -47.00671 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2c8f6eb3-695b-36c2-82a6-9e184a231150 | -12.55008 | -46.97464 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b256fff9-bd41-3e59-bd7f-cfc5eea7f45a | -13.46762 | -43.75461 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbe9f7be-02cc-3dd2-94b4-d315a0280187 | -12.56528 | -46.95645 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1c791162-df6b-30d7-8895-2aa8d4534e92 | -12.68411 | -44.96152 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7987743c-3461-31e6-9b4e-63fe03939ccb | -12.60206 | -46.97639 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bde451b6-e36f-3bd5-a2a0-07fe12eb7f3c | -10.53976 | -42.55055 | 2025-08-16 03:45:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13428a8b-f2c8-34ba-a563-23df32c0de25 | -12.60078 | -46.92315 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1db9f1e7-2e65-3df5-a442-665806236530 | -12.54041 | -46.96471 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 0d1a3b02-aa94-3d10-a06d-7762d71055b1 | -10.95339 | -45.18597 | 2025-08-16 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fae08872-1a2a-37c0-ac11-2dec607878a4 | -13.58155 | -46.98048 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3f494db-db12-3db3-b1af-d6c61a428653 | -7.40349 | -44.88599 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8523696-2cfa-3bc8-b64a-98d7b0f6b18c | -12.61284 | -46.94159 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 70760482-f64e-3c0c-8a28-e9d8a6b431a2 | -8.94503 | -45.81615 | 2025-08-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bb3fe06-830d-39cb-82bb-2c75b195daa4 | -7.40886 | -44.8868 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aed1edf7-3830-3300-9803-ae2804e9d606 | -12.8006 | -45.96877 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa6227ee-334a-3bda-b2e4-ef48cb49e7bd | -12.61442 | -46.94247 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| af4694d2-72f3-3047-9214-e3f636a1977b | -9.70578 | -46.27412 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0256d518-aadb-332c-b3f4-f7460584edcf | -12.56611 | -46.95222 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 80f70e5e-d3fd-397e-8bbb-e8f48ddc52d9 | -10.35439 | -49.92702 | 2025-08-16 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d4f08b6-8cf0-397d-a992-cedccb2aaeea | -12.60578 | -46.95718 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3d642caf-ebd5-3246-90e8-2b80b5019d7f | -12.77881 | -45.94092 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ef666fe-02a5-3008-b791-58ac14d49ced | -9.17789 | -45.32743 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| dfe00153-f98b-36f7-be61-53b0c92a775c | -9.70086 | -46.26938 | 2025-08-16 03:45:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa58a67e-3b5c-39e6-9eaa-4e9d5ca13705 | -13.57165 | -46.97391 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2d2522f9-b715-396e-97eb-15153f48f08b | -12.40731 | -47.78563 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b76b5a54-cfed-3ebb-9516-82cc9b789264 | -13.11201 | -46.84496 | 2025-08-16 03:45:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2cbf7d21-3203-30c8-bfbe-f8a2ec987da4 | -8.94566 | -45.81675 | 2025-08-16 03:45:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02809fa3-5aa6-36ee-aba8-14b198b3547f | -12.82633 | -46.00444 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d7399f0-625d-3ad5-89f2-df898476d7d5 | -12.47519 | -46.98304 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 630199d4-2232-391a-b4c8-251a548d0d7a | -12.59434 | -46.92651 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ce37ae40-d39b-3910-8b03-330e9f5f3816 | -12.80669 | -45.99374 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9452743c-cdac-3c82-8e3c-e7d6fe346586 | -9.17254 | -45.32646 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d75792c2-9a90-33bb-ba83-272e9e5fc9a1 | -12.59003 | -46.94864 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53f90a48-0e3c-39db-bbd6-c3df531e97a1 | -12.5893 | -46.95241 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a7e96b3-23b9-315a-9f66-264e66d2ede4 | -12.5371 | -46.95205 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| dfacc630-ad25-30a4-ae82-14653febf4cd | -12.59773 | -46.95898 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fb3511fb-22b1-3aed-b476-76ea14e7aa84 | -13.5721 | -46.97065 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 79984b7f-2c30-3cfd-9c59-a868a11494b7 | -12.60429 | -46.96487 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0606d072-2c94-3e13-a1f4-dd352fed1b35 | -7.07564 | -44.93705 | 2025-08-16 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c31c012a-c13c-31f8-a9ce-32002bb07287 | -12.46247 | -46.98848 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2bda927-0075-371a-a22b-731a60141dde | -12.61461 | -45.22552 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10265f85-7f29-3e72-bf8f-b3b84ac5ce7b | -12.59078 | -46.9448 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83ee6bda-9b3d-30df-8aa5-0bc2d173e89d | -11.26306 | -50.47346 | 2025-08-16 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0c30cbc9-af02-3cd0-93ac-23dfe86951e6 | -12.60283 | -46.9126 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d702de10-ba3f-33b4-ac3f-ecf128b4c1a4 | -14.21537 | -44.77731 | 2025-08-16 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ab6a144-52b1-3a65-8988-3f846489c4d0 | -8.17971 | -45.02087 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c531553-ae6b-3a76-a3a1-9730cbcc54d6 | -12.77365 | -45.93959 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f84d2f3-f1ab-3459-b92d-af2520ae04d4 | -12.59793 | -46.93785 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4645ffe4-7575-3b07-aecc-70e865f342b3 | -7.15243 | -44.38816 | 2025-08-16 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 829b0a1d-2d6c-3ad5-9772-6ea10e1c9fda | -12.60729 | -46.94935 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 903796c4-c934-3942-ae4e-6e2f2d2d6472 | -8.19571 | -45.02366 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd563f98-3647-3b6c-8d14-02c17f6210d7 | -8.18915 | -45.0296 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b6b5611-61bf-31b9-bd5d-8ddbee065f14 | -13.8721 | -45.54959 | 2025-08-16 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca23d22c-9df9-31ae-86be-79eaa02a4e85 | -9.17851 | -45.32407 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 37fca39f-9c60-33f7-8785-592df97e7ee0 | -12.59544 | -46.95066 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 82f96f2a-e705-3a28-a36b-971665ba6e39 | -13.42806 | -43.67799 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| d1035459-b3e1-3820-b4c2-e599924fabb4 | -12.80001 | -45.97189 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c54b3377-227e-3b5c-8b83-3435283289b3 | -12.60808 | -46.94529 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 9e70abe6-ed86-3129-b157-2fdd037d3d5b | -12.4523 | -47.01061 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2e1d9a5f-a75f-33f0-bce4-a14903420d9a | -11.50591 | -47.24016 | 2025-08-16 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2afef70d-ebc7-38dd-82ea-c6e238bc5cdd | -12.53964 | -46.96859 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 5d0b9591-0af3-3f27-90b5-3fe17697294f | -13.57515 | -46.98526 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59dd43e7-cd7c-3200-8b06-9700e30a611b | -12.59156 | -46.94079 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6d9ed5e7-cb2a-351e-8a15-123ce5134090 | -12.55646 | -46.97179 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 054d0aab-8a85-35c4-b86b-17a0630f0673 | -8.18381 | -45.02867 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1932efdb-febb-339a-8705-5f1329694762 | -12.4925 | -47.50839 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4907f9a6-5244-3f8c-8667-7da17b177aad | -12.48765 | -47.50189 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1254d20f-02ed-3d75-8d88-ce3f6e2ef2e1 | -12.6064 | -46.91598 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1b2132a6-4fe3-30a5-8938-cc18c6a938c6 | -12.83569 | -46.04026 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f0379cd-ff0f-308b-bd82-245844d1696e | -7.97646 | -43.96187 | 2025-08-16 03:45:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fcfbe5e-209b-3817-a645-a5994f5ccc0c | -13.58442 | -46.96629 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8978e876-c90b-31f4-895e-1722a1a3cfe2 | -11.50507 | -47.2444 | 2025-08-16 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 14ba7877-f1e4-3341-a392-21f1cc1b4beb | -11.99192 | -44.5371 | 2025-08-16 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 185b5041-249f-3fe7-9308-a82562670be3 | -12.61614 | -46.93355 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3792ad22-ba33-3169-9387-b302e0f92fa1 | -13.57081 | -46.977 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2db8d836-1528-33cb-9879-07c4e7e18e02 | -7.3861 | -44.92095 | 2025-08-16 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea41fc19-9f29-3541-b5fa-2dab870ac2a6 | -13.58311 | -46.97375 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99c0df52-3677-3e1b-9916-0bf58ba98e72 | -12.04814 | -45.76399 | 2025-08-16 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 79acd9ba-6170-3a54-b799-5a93072a009a | -12.80794 | -45.98738 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da4d6a06-7023-3554-aaa1-d2e8cef74690 | -12.82317 | -46.02065 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c35d9c95-020a-3b2f-a545-5b2b9ed6124f | -12.56285 | -46.96885 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b42257bc-9196-31e7-a123-fe89e13cabb2 | -7.58645 | -45.16191 | 2025-08-16 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 11d8dff6-1007-3a45-8671-3ef304da0762 | -12.05336 | -45.76501 | 2025-08-16 03:45:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
