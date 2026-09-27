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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba6ff391-8245-39e5-abd6-15ffbd84b77d | -11.9777 | -50.7371 | 2026-09-27 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7e0d1199-34eb-39ca-b42d-3273d480be46 | -12.7225 | -47.2937 | 2026-09-27 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 250.4 |
| 5d79212d-8913-3605-9a0c-96d98b05e9ed | -11.3048 | -51.3011 | 2026-09-27 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3200d7a3-3e43-36e3-91b6-be477f176cc0 | -11.9389 | -50.7843 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 1eec340c-04b0-3678-84e3-e687c95f5955 | -8.5982 | -54.6341 | 2026-09-27 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 22e72257-5817-3ac0-94a5-a80820a609c9 | -11.9405 | -50.6773 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 855e4963-bb91-30b6-baa7-ee46997605c2 | 1.5834 | -55.8645 | 2026-09-27 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| e494c46a-e141-3636-849e-0c605e8a19b9 | -12.7035 | -50.6714 | 2026-09-27 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ef92cc90-375a-3e91-bd2e-5a0a1c409613 | -17.0529 | -56.59 | 2026-09-27 14:50:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| dc329271-6bce-3fe0-ad37-1dac127dbd5c | -17.0533 | -56.5693 | 2026-09-27 14:50:00 | GOES-19 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| 09eee8b1-ee72-36d0-ae3f-7c80e1a49403 | -8.4838 | -54.9242 | 2026-09-27 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 29a06b7c-0b9c-3134-95e8-30d8e906ed26 | -11.958 | -50.7821 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 24a5ac1d-008b-3b06-9210-fa21c389d0f1 | -7.3653 | -42.1058 | 2026-09-27 14:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 177.2 |
| 2e99df5f-af12-3e83-b628-70803f5c0677 | -11.3046 | -51.3222 | 2026-09-27 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 7c43f56d-d404-32e3-8a01-fab71b3d22b8 | -11.0679 | -50.6257 | 2026-09-27 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 85991c0a-3fb6-3c58-a312-29e359029dbc | -11.2091 | -51.3746 | 2026-09-27 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 4b78c17f-8594-31f5-99f6-331b62026b1b | -12.7038 | -50.6499 | 2026-09-27 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| e9e68399-126b-3143-b5e4-77bbede8bc30 | -9.1525 | -49.9639 | 2026-09-27 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 25805e7a-07b8-3949-8bc0-cb0d566c3640 | -12.2911 | -50.1849 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 4cf6c0f1-ea46-3d48-93cc-18601a44de99 | -8.6171 | -54.6126 | 2026-09-27 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 5dfc0ebd-619d-37ee-b087-585b00f3b43a | -11.73 | -50.7656 | 2026-09-27 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| dc359911-ede2-396f-9dec-30d089281601 | -10.2257 | -49.9879 | 2026-09-27 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 209.2 |
| c66b9173-8ae3-3c4e-bc9c-a0ca4106e7ac | -12.9457 | -51.0695 | 2026-09-27 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 206.4 |
| 57ef0801-b2cb-3589-9a8b-ea74528f9337 | -12.7421 | -50.6451 | 2026-09-27 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| e918ad50-a7a9-3a12-996a-5fc53a66a8ac | -11.6989 | -44.4984 | 2026-09-27 14:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 49833bf9-423b-3630-a446-436aadef11a8 | -9.8494 | -48.4709 | 2026-09-27 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2b74eab8-cc1b-34fd-b295-d2c0d976a0c4 | -13.2186 | -54.5182 | 2026-09-27 14:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c886004f-523e-3336-a3ab-c313ff27a3d1 | -8.5984 | -54.6139 | 2026-09-27 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 8f3cc552-576c-3dc4-9992-7b771f3e7503 | -20.2029 | -46.1918 | 2026-09-27 14:50:00 | GOES-19 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 33f27350-5f88-33d5-9c57-a52f2ec29f94 | -11.1924 | -54.1225 | 2026-09-27 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0c79a270-9a2e-368c-8071-e3a52a8df21a | -15.9869 | -54.9419 | 2026-09-27 14:50:00 | GOES-19 | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 85a89939-1237-3d1a-bf9f-6028cad29b68 | -10.8187 | -57.2192 | 2026-09-27 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| eccd9724-7f99-320f-9b70-e71c7523a879 | -7.055 | -42.849 | 2026-09-27 14:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 92e8e454-3699-3ecc-99d7-d8252ffcd54f | -11.2859 | -51.3031 | 2026-09-27 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| bb9fddae-fade-3849-a7f1-70982a6ffd1c | -12.0352 | -50.709 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| bacd6a6e-d89b-3b86-a2c1-b02cb6277742 | -11.79 | -50.5664 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a7baf244-b792-314d-93f7-006c8120c588 | -11.9402 | -50.6987 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 972ad174-6f5d-3be2-88f3-9e1a0193b282 | -11.2113 | -54.1208 | 2026-09-27 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 1502b2fd-c1d6-3ecf-a40f-80fa66093835 | -12.9461 | -51.0481 | 2026-09-27 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 868305b0-7352-3183-a989-74a8e0a8681a | -11.9777 | -50.7371 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f4eacdf4-82db-3962-bbf3-73db2ee9b42e | -12.9269 | -51.0505 | 2026-09-27 14:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 01db20a8-a643-3031-9aa7-32df1883610a | -11.8024 | -51.013 | 2026-09-27 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 9126ad99-b207-3a62-abd9-503161cfaa93 | -11.2118 | -54.0797 | 2026-09-27 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| aa39ff1b-4f87-3e85-a2e1-4434ce961db2 | -9.8491 | -48.4927 | 2026-09-27 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 7274614f-73a3-3af8-8243-8b3a162f29aa | -10.0348 | -50.1569 | 2026-09-27 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| b5695b2e-0770-3f46-abeb-bd5b7b6b3555 | -9.7874 | -44.8289 | 2026-09-27 14:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 365.6 |
| eb693166-9893-3dbd-b3cf-1532e528585f | -11.7329 | -50.573 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0407f4ec-5b01-31c1-a575-9bc4c5ca7629 | -11.3739 | -43.3972 | 2026-09-27 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 70e7236b-39b3-3c53-8c92-21b25b62db65 | -11.81 | -50.4999 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| aa19e392-b9bc-3eb2-b2da-fc9d06cef456 | -17.5697 | -46.9019 | 2026-09-27 14:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 103.1 |
| f1a157e8-ad52-3258-be15-c563bca522fb | -12.1553 | -50.3305 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 796b0ad9-1205-344c-9dec-4c82065eac2d | -8.4296 | -54.7262 | 2026-09-27 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| e9933d13-0a77-3be6-a658-83120c5c5446 | -10.7114 | -60.7505 | 2026-09-27 14:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| ba90e49f-cd22-38e5-9408-8f923e3c3212 | -11.9132 | -49.9721 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| c054fc84-52b4-3c2a-a4fd-9f2f994f473a | -12.6647 | -47.302 | 2026-09-27 14:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.5 |
| f560f8c2-10ca-3d8d-94dd-ad6a9b0cb56b | -11.9018 | -50.7245 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8283e2f3-85f6-3578-877c-b30d84df91ea | -10.4046 | -53.803 | 2026-09-27 14:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 92b17705-d828-3792-93ca-a6a2481e24b2 | -12.6655 | -47.257 | 2026-09-27 14:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 177.6 |
| bc7056ae-aebc-360a-93e0-926a2fb9d6c8 | -12.0645 | -50.0401 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f304b7d5-61ff-3531-bc2e-2320721c4587 | -12.4351 | -44.1497 | 2026-09-27 14:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 0eaaaa69-80cf-3306-b15d-3827bbbf445a | -11.9586 | -50.7393 | 2026-09-27 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| de930eb8-5976-3263-85db-0e68e69063d5 | -11.657 | -50.5603 | 2026-09-27 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c048dd9c-780d-3296-984f-dc106c125b9c | -6.8408 | -43.5021 | 2026-09-27 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 910a1ae7-0fbc-3250-b0db-e4ffaf9dea4d | 1.2794 | -50.851 | 2026-09-27 14:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.0 |
| ef4f6dee-b5cb-3e30-a8b4-0950d943eb03 | -7.3467 | -42.0839 | 2026-09-27 14:50:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 107.2 |
| 5216873f-f35d-3d82-a8a4-bf3aa12576a9 | 1.6201 | -55.8641 | 2026-09-27 14:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 623a3a2d-0836-3701-94eb-b351bb5956af | -9.1528 | -49.9425 | 2026-09-27 14:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 8bad393e-fdd4-3932-b80c-4f8f2f407e1f | -10.2827 | -49.9606 | 2026-09-27 14:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 683e31e2-7d92-31b0-90c9-f2d2d04bfec6 | -11.8014 | -49.8129 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 80f14fac-115b-3428-a137-258f1719188c | -12.1366 | -50.3112 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 6d43edab-1ac8-354c-a18f-601f7995983a | -12.3286 | -50.2234 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c7a89b37-1718-309a-b642-537b30cb54db | -11.1183 | -54.0062 | 2026-09-27 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 707bdfa6-7cae-3f2e-ac33-c0588ef089bf | -12.288 | -50.3789 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b27361d0-eadc-37a5-9b38-9cee99aa6165 | -8.5982 | -54.6341 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 99578451-16a2-3775-9279-0b0a33f46e6c | -8.411 | -54.7274 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| bdd6c766-cee1-3e9d-86d6-d4fb86426228 | -11.2118 | -54.0797 | 2026-09-27 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e0f9307a-628a-3348-810d-1fe7d353765d | -11.2859 | -51.3031 | 2026-09-27 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| eb72a472-47f7-3f89-85d1-dbed83806e61 | -13.2186 | -54.5182 | 2026-09-27 15:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6723621c-6a63-325c-ac60-daf18edb54e2 | 1.8692 | -50.6753 | 2026-09-27 15:00:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3fc75172-1904-3c55-8de9-10c5db2aae55 | -11.9783 | -50.6943 | 2026-09-27 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 244f592e-bc6d-399a-8ef4-37ae1acc4c1a | -8.4298 | -54.706 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| b1fe57d8-7edf-3867-9205-3b102edeb3ed | -11.2654 | -51.411 | 2026-09-27 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| a0a710cd-5cb5-3201-ad4f-411c988e766a | -11.3048 | -51.3011 | 2026-09-27 15:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| e4049608-232b-3d4b-b647-e5ee14baf3e6 | -11.9352 | -49.7752 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| e34d8595-3570-36b4-9e45-7ef1f6b3d98a | -11.6561 | -50.6245 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6bbf3472-660e-3df2-b6a3-8920752d0ad2 | -11.1924 | -54.1225 | 2026-09-27 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2973a947-1cb5-3bcc-b400-76fbf3754d89 | -12.3082 | -50.3119 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 9ac2b338-9756-3570-b0eb-efcd687c558c | -12.1369 | -50.2897 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 22cfaaef-49e5-3120-ba09-0344b00f4e50 | -10.4046 | -53.803 | 2026-09-27 15:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| d7e9e105-afad-3e4c-b472-2de066866a27 | -11.8084 | -50.6071 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f62b4d57-4a49-324f-b895-90323b870269 | -12.0793 | -50.3181 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0f5812ce-95e4-32d8-adf7-77c89737db1d | -8.4838 | -54.9242 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ea5f5b16-e5b2-3d2c-9ae9-e0be45c94c1c | -12.8059 | -54.0255 | 2026-09-27 15:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 013b7da0-a5a4-37b6-949d-7940112d0ce7 | -11.8941 | -49.9744 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| dbf496ac-2c7c-3806-8bd5-5c2f8ce8fdb0 | -11.6199 | -50.5004 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 03be0390-ee8b-32e3-abb3-3d7fb95d400e | -11.958 | -50.7821 | 2026-09-27 15:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 89447704-aa27-34a3-927c-2b4947b79163 | -8.5984 | -54.6139 | 2026-09-27 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 957cb73e-c0a8-382f-af48-10021bb76d60 | -11.0991 | -54.0285 | 2026-09-27 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 61954b1b-9128-33ee-b444-be7426358aa3 | -11.9615 | -50.5465 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 0fe39fba-6b74-3677-98ff-fcb927eabb92 | -11.8097 | -50.5214 | 2026-09-27 15:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |


[Clique aqui para ver as próximas entradas](README62.md)
