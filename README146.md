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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26472d9f-14c2-347a-88bf-4f9f7a61f044 | -17.08498 | -56.72169 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 240788f6-f634-3904-bec9-5a9341b39469 | -17.08453 | -56.20452 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 28e15061-2755-3bf2-b179-bf097621b2c9 | -17.08437 | -56.1165 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 21383bd6-8a22-3274-a1ee-785600302b2b | -17.08434 | -56.7271 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 167fbd3b-4a35-343a-99fc-15128b34cfa4 | -17.08433 | -56.12058 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e6ea7054-2757-37ec-a997-774f69ad6e5b | -17.08383 | -56.21039 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 252209ce-5795-3ae7-9ca2-093e13ada44d | -17.08371 | -56.12247 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| db2a2465-fa0b-3bf1-9860-f7bf37c80356 | -17.0837 | -56.73252 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7ab0fe21-f768-3aaa-a5b6-3a88d3da1432 | -17.08305 | -56.73795 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 2bbb6215-7ce2-3e79-8d6a-18e711881cd7 | -17.08241 | -56.74335 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 3abe011b-cc10-3ca3-806e-7d34895d557d | -17.08208 | -56.7048 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3d1b7fd0-b973-37bc-9db5-9648a1e21e16 | -17.08177 | -56.74874 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 127c193c-e08c-3203-be65-0c8b5e4b0ca6 | -17.08144 | -56.71022 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5c699f95-0590-3026-8f3e-14709290aa8d | -17.08113 | -56.75414 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 9738b0e1-1502-3315-98da-f39f6f9b6a5a | -17.0808 | -56.71565 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 884f7f8f-b738-3800-b231-8a2191d44476 | -17.08016 | -56.72107 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a7b043ef-2f4b-3229-8323-c9f790aa2dba | -17.07954 | -56.2039 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 61f22535-982a-33e1-b18d-0880131fa761 | -17.07888 | -56.73189 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b2a245ac-3c05-3014-a5d8-d548b6292fc5 | -17.07824 | -56.73732 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 248bd3da-da28-350d-9fbb-1a51a62c3bc0 | -17.07759 | -56.74273 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0302f320-001b-3aea-a7a3-13a589d76f8b | -17.07696 | -56.74813 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 3c825812-a762-3ddf-b623-a7901cfd48a3 | -17.07661 | -56.70961 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 0f099e23-08c2-3f5c-a6b4-4770c57e8661 | -17.07597 | -56.71502 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 799909d3-c655-3a8f-876d-8cb0ea161864 | -17.07533 | -56.72044 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 5d3f2a60-fc31-37f4-9178-0ffec9553612 | -17.07469 | -56.72586 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 16b7e128-0b1b-36d2-9b12-9ff4dbd9fed8 | -17.07405 | -56.73128 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e924cd17-acd3-3c8e-8fdb-d8f5cfadd38e | -17.07342 | -56.73669 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 54d228c3-42a8-3937-9b98-850431f4bb42 | -17.07278 | -56.7421 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 0ec3a90a-c604-3147-81a2-930a3df23dcc | -17.07115 | -56.7144 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5abf2f03-b497-3b99-83b6-0d1e9333dfdf | -17.07051 | -56.71982 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5f393c81-658a-313b-923c-d9cea1ec217b | -17.06923 | -56.73066 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| fd93325a-652e-39cf-9da9-1c652ddce108 | -17.06696 | -56.70835 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| eb9c92de-2108-3715-9b60-e1b8a70e236c | -17.06632 | -56.71378 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d43a69ee-86a4-3cae-aaf4-9c32cade6f3b | -17.06569 | -56.71919 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9ca38c67-cc37-3a6b-a66c-2e57e07d75f7 | -17.06213 | -56.70773 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7d3896af-932f-3b35-bd14-166e06c44192 | -17.06149 | -56.71316 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 24a516a5-86e0-32a3-a22c-1cc5731dbbc7 | -17.0606 | -56.10553 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| bc61103d-08d9-3e6e-b8f7-fb4e166cb50d | -17.0573 | -56.7071 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2adf501a-d15f-3605-8839-400e56db5733 | -17.05667 | -56.71253 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 37bce779-23ce-392d-b08d-5d74e62c102b | -17.05604 | -56.71794 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3ca5c35d-8a0e-3c3b-8769-cb14d768a865 | -17.05541 | -56.72335 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 17a6cc35-c0eb-38a5-8320-840f1d45e755 | -17.05184 | -56.7119 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3a988269-ad47-305e-94b1-6036278e9367 | -17.05121 | -56.71732 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cb8e75b9-abdd-3a53-acb1-6dee03f6ba6c | -17.05058 | -56.72273 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c7ad0120-3fcd-359d-858d-2bc2f229f189 | -17.04898 | -58.39861 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6725f71e-699b-3467-9e6f-1ac2229f1899 | -17.04807 | -56.74435 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b89ec228-6d0a-3d60-b49a-8f51a379a9a0 | -17.04745 | -56.74974 | 2024-10-01 05:31:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd707b9f-0474-38c3-8a03-9b18305a4ce1 | -17.04468 | -58.398 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 51fff1f1-01bf-381e-969e-f2c67cd43cab | -17.02243 | -56.08254 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7cef53c6-3add-30b5-8508-1fb08ac03a50 | -17.01807 | -56.07592 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7a3228cd-9e0b-3f97-8ad5-a1412a7cf4a7 | -17.0174 | -56.08191 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2aff5567-c48d-316c-882e-7339e11734cc | -17.0143 | -56.07516 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4b7cc8e4-2936-364c-88cc-70dc93005549 | -17.01358 | -56.08113 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e8612d71-0930-3653-a856-a438474ac6c4 | -17.01236 | -56.08127 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c7c63517-6925-36ec-874e-d354e7910321 | -16.96259 | -57.94956 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a6e7dc11-2aeb-36e1-94ea-377cba46ccb4 | -16.95816 | -57.94896 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9eca4e27-ac28-391a-ab0b-4e4bdc86aaf4 | -16.94016 | -56.18576 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| caaba827-c550-3a4c-8848-4bb0302030e0 | -16.93947 | -56.19165 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2d1772c4-9cf0-30e3-b9e0-54f57127e271 | -16.93878 | -56.19752 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8f92339e-4a74-3c75-9e1f-e5eb79a0baa9 | -16.9381 | -56.20335 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e53545ce-4c57-3375-a07f-f438b8de2726 | -16.89148 | -57.70033 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 451c5e4b-2784-34dc-9fe5-bb9c19c7c8d0 | -16.8909 | -57.70496 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e7d5e8bb-7463-333b-9b86-e795fe3a130c | -16.88973 | -57.71423 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7b0b7e0f-b19b-313a-9c40-756a792d5c23 | -16.88914 | -57.71886 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b8db5f3a-6e5a-335b-a8b1-0397fc5a2f13 | -16.88639 | -57.70435 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2c770743-c93b-3e14-b934-4ffdb688cfea | -16.88581 | -57.70899 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 87e30c4b-2129-3f13-8db4-551859f40e10 | -16.88464 | -57.71826 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1dd37da3-c262-32d2-a30c-79529f3f1cc9 | -16.87346 | -57.69791 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ad4f6466-8463-31ed-94a0-24bd4230ab6b | -16.86954 | -57.69267 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6f732e26-8561-3618-937a-c5d92c680beb | -16.8651 | -55.9139 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 64ca9acf-3457-3b32-9764-a63438fc5924 | -16.86503 | -57.69206 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 5dfebdda-65ac-3e28-914e-b58525afe725 | -16.86475 | -55.91693 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a84be90b-d772-3c39-a92d-0e1d60914147 | -16.86445 | -57.6967 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 80470b90-79f9-361c-904c-5b6373467144 | -16.86179 | -55.89798 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb5de703-f2f2-3558-ae97-6bb37bf0bc62 | -16.86143 | -55.90103 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 65681dd2-ea93-38fc-b356-c5b42bdb581b | -16.86108 | -55.90409 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b16a6c7c-7fac-317e-a3b2-13583a384b46 | -16.86073 | -55.90714 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 01828f9e-9b04-30e2-98e2-cd3057508039 | -16.86037 | -55.9102 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 59f47be7-7702-3d3e-ae4f-4e24d910103e | -16.86003 | -55.91325 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ab14a7e8-fe31-37aa-97fc-1166e7fcd9c6 | -16.85976 | -57.77108 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3706b49a-cc00-3197-907e-8343bbd93a6b | -16.85967 | -55.91628 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 841458f4-3b0e-38b3-b287-54c9b3950d70 | -16.85933 | -55.91932 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 60854088-0cae-314b-a3b0-d78f21d0e18b | -16.85897 | -55.92235 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0f40bb3e-90e2-383f-b7db-d1129bee7cd3 | -16.85775 | -55.93297 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 87476761-d79e-3aed-992d-bbedae572145 | -16.85705 | -55.93904 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6279e2b0-a8c2-38d7-a362-b04220c50aa8 | -16.85705 | -55.89429 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| cd63f5bf-1c48-3119-96bb-5779aa43d877 | -16.8567 | -55.89734 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| bab6df38-7c72-39d0-9217-94a2e17657a2 | -16.85635 | -55.9451 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1e78133a-db96-3229-9f36-9a2caed8faea | -16.85635 | -55.90039 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f5271311-d7ad-360e-a90e-952839b6c36b | -16.856 | -55.90345 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1e33d007-0968-31be-b484-972bb6b3833f | -16.85565 | -55.9065 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 3a3efebb-36a3-30b2-8998-7c3244002510 | -16.85545 | -57.69547 | 2024-10-01 05:31:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f1b591d0-3ecd-35a6-9fae-abd195d1b711 | -16.8553 | -55.90954 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 33a2f824-ac63-30eb-a253-a561d76512c8 | -16.85495 | -55.91258 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2b76d49c-0c8c-3b05-80a2-1d059bc83d56 | -16.8546 | -55.91563 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 901be751-5144-3999-80a3-8f7f25f269d2 | -16.85425 | -55.91867 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 37d68cd5-7df9-3055-82a3-6a680825a5e9 | -16.8539 | -55.92171 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c22451eb-9a30-3661-9c06-65203ad2e9ef | -16.85355 | -55.92474 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 64839a43-abc2-3daf-a28f-c4d27e6444de | -16.8532 | -55.92778 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4588e368-ffad-3923-882d-3b273c7056a4 | -16.85162 | -55.8967 | 2024-10-01 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |


[Clique aqui para ver as próximas entradas](README147.md)
