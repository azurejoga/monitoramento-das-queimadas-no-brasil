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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b35a881-ee00-32f9-84bd-b8fbec59b9d0 | -10.82957 | -57.19675 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a11c44c5-3548-3d80-85d3-eeab47c3fcb7 | -10.32817 | -50.33932 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35ab60be-fd05-39f1-ae06-036cfb79f224 | -10.20695 | -58.25621 | 2025-10-04 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f9e34da-909d-3fae-8198-fe1ed48d57d6 | -13.17304 | -50.92438 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0ead643b-e193-35fa-b781-c0593591b936 | -9.25193 | -56.88177 | 2025-10-04 05:33:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9533cd7-b7c5-32cb-9e43-e12c81df7187 | -14.57188 | -52.48222 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7e9993f-a1de-3871-9225-78027a79a9e1 | -9.34633 | -54.52378 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cba2e920-25d9-317f-9a49-a6787ffc772d | -10.36016 | -57.82255 | 2025-10-04 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3190f174-a152-339d-8418-0e6f3b356dd2 | -9.94046 | -50.24538 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 922e2792-ce45-36a9-bee4-8ad55077f7b5 | -11.96642 | -51.48269 | 2025-10-04 05:33:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75285e09-0eb6-3038-984b-137385b1a7b6 | -15.58274 | -52.46548 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 038158cf-e804-3f85-9c24-c42bd621099a | -12.38392 | -54.46744 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fbb6184-c73d-3f47-820c-17e109782f1b | -12.98532 | -53.4333 | 2025-10-04 05:33:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ba272c4-819b-3c98-a5e1-a8443fa74ab0 | -9.90502 | -63.59439 | 2025-10-04 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff8f5ad9-e646-32a8-9510-2ad611e60274 | -8.61997 | -54.9911 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c0dcf96-ea7b-38cb-96a9-b86a137f0f8a | -13.17496 | -50.93697 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 5b53c2d1-3f8d-3f12-9a27-3be9b4ba73cb | -9.63446 | -55.13232 | 2025-10-04 05:33:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76825dcf-a8e2-3914-88d4-2abb117bc6ff | -15.58225 | -52.47015 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 198d30a9-70fc-34e5-a360-54761b4d0c93 | -9.92528 | -50.20096 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c61c6812-8c9f-3fe2-9d86-3e831a75a240 | -10.63829 | -49.14465 | 2025-10-04 05:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16e27e71-7b1c-3df1-98f4-8021b61a1ef5 | -8.61882 | -54.96384 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 351a36a6-147d-34d2-a1c9-de55c5430fbd | -9.86079 | -60.27266 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9863dc8-d2c6-3ac0-bd78-96fd8a09d973 | -12.39128 | -54.4516 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36c8b2e2-c5a5-3657-b7c3-babf0eb46106 | -12.28461 | -55.13692 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cf0db6c-eac5-3af0-acd9-3af99ffbd850 | -10.33629 | -50.3283 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6c234be3-56ba-39dd-b4c5-92f11f69af4e | -10.44206 | -57.5848 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08acb3c9-bdc6-3de6-80a8-a0f79bb54ff3 | -10.63907 | -49.13759 | 2025-10-04 05:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| af0f06b1-61dc-39cc-af30-6ec1c647b18c | -9.34415 | -54.53011 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6aa19050-d378-34c1-a77f-7579d84d29bf | -11.12959 | -55.46154 | 2025-10-04 05:33:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dbb83799-7750-3c17-b9d1-565bd16f18d2 | -15.20518 | -56.83614 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a76e1639-9e54-39cf-b66f-bb974284f8d7 | -9.63633 | -63.20105 | 2025-10-04 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a969b406-1f53-3bce-b35a-642f365534eb | -9.93373 | -50.24453 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffc7e9d2-307c-3979-b2fd-592c2c2deb42 | -8.61957 | -54.95848 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cedb9a38-b35a-3b42-b53f-c4cc650e07ab | -9.93994 | -50.8979 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90fa090d-a790-3dff-9280-b04689f1cf4e | -9.98818 | -57.82095 | 2025-10-04 05:33:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eba8a609-5c2f-338a-94a8-9a0c55905144 | -12.30014 | -55.13628 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c778ec85-d6c4-361a-b04e-248e6c94e0db | -13.17266 | -50.89442 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 431b799d-0dba-3ef0-beb3-5160f388d9d3 | -9.37303 | -63.451 | 2025-10-04 05:33:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b5b8b891-b873-33e2-a47f-f2b7d17d1383 | -9.31896 | -54.53546 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 058dbecd-c6b5-304d-9850-ffdd3dc19058 | -9.62872 | -62.40936 | 2025-10-04 05:33:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 98b4362e-1b85-396c-94a8-c79958a285c9 | -9.6258 | -63.15985 | 2025-10-04 05:33:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a74b576c-b9cf-332d-a32c-e7523d78df13 | -9.9991 | -60.01706 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69303b8d-e814-32d2-a9d0-403cff324e29 | -13.1784 | -50.93702 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 24f270c0-7a61-3c99-ae39-bae5584764a0 | -9.94117 | -50.23945 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6332fce4-10d7-362c-9e57-e0b0c713e355 | -15.23208 | -56.84996 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e3c40aa-9d70-326e-90c1-3a78a59e0a50 | -8.61808 | -54.96913 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b3c3c15-3716-3eaa-baad-a0e03c7bd89d | -15.20579 | -56.83128 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b6f2354-9fab-33fb-b19f-84b81ad02440 | -10.60008 | -54.35658 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b24925b-ab15-3ef3-8575-8b61e9b37224 | -9.93315 | -50.89786 | 2025-10-04 05:33:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95afecca-7024-3379-a6eb-aee4a3deb1be | -15.03472 | -56.05189 | 2025-10-04 05:33:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8cc5bfb1-3b30-3b10-b622-3568489dff8b | -8.61924 | -54.99632 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87b304dd-caaf-3ae7-b40a-4a03546a6222 | -12.36572 | -54.16922 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9edd06f1-6b87-325e-ba22-7340e7e0798e | -9.91604 | -50.50301 | 2025-10-04 05:33:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8891951e-7b30-332e-8bf4-aa4a61f17f8b | -9.32992 | -54.53067 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1f95ab9-2b69-3e58-83bf-6d9391d360de | -15.58943 | -52.4623 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 465e6172-3ff5-32da-bc34-8d0344a82097 | -8.54428 | -55.01751 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0572146-a7b9-39b4-99a2-1234b0e3536b | -9.63724 | -54.31631 | 2025-10-04 05:33:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b886e9ec-4bbb-3670-ae2f-e9aa1af91df0 | -15.59257 | -52.49276 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a079b5c6-cf3f-3f5c-a146-6b85d87dad56 | -14.57429 | -52.47956 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 921281a5-cae7-3a34-9e38-4588ada4bce6 | -9.33702 | -54.51648 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1eb63c13-944b-356f-9044-7ec2212f99a9 | -12.28498 | -55.13402 | 2025-10-04 05:33:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f8f9040-2a62-32b9-be15-0da7c5c49c12 | -9.34086 | -54.52605 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9b27e01e-9088-3ef2-8bfe-0f342c8d6c34 | -9.71418 | -67.46502 | 2025-10-04 05:33:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 301d69cc-ad9a-3731-8f61-9942bc08b8a2 | -9.97365 | -62.19168 | 2025-10-04 05:33:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bc6674f-58f4-3558-8090-3a84ff7837e4 | -8.61321 | -54.96853 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 587a79ee-36fe-3b78-abac-a6505f6d7f38 | -15.59934 | -52.48883 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72c223dd-877d-3066-9070-651846a8bc12 | -15.22251 | -56.81259 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2af66005-a0b7-3870-9290-3aabb7c48d26 | -9.99551 | -60.01651 | 2025-10-04 05:33:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a80829d-63bb-3d32-8bc3-d2e8a88aedd2 | -13.17171 | -50.93625 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 7699346b-ca2b-360a-b3b8-120ac9e5f322 | -11.71205 | -51.47007 | 2025-10-04 05:33:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac0c7960-8162-3b3e-a217-1eb3c223b649 | -9.34492 | -54.52421 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| da15b762-efb5-3367-bc4e-cabbe49aab94 | -15.60937 | -52.48165 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bb2e7f9d-5c2f-3709-bce1-6cfbb7767966 | -11.71267 | -51.46485 | 2025-10-04 05:33:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f2d5246-0aa7-3cc3-98c2-715a73d8bbd9 | -15.60713 | -52.47529 | 2025-10-04 05:33:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ec55e09-f426-34fe-bbdb-478a35573cfa | -11.16801 | -61.31458 | 2025-10-04 05:33:00 | NPP-375D | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3deed8a8-5502-355f-9426-d1917de00223 | -10.83292 | -57.17214 | 2025-10-04 05:33:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f63afdb1-32a0-3ae0-922e-7d4354598b26 | -14.57376 | -52.48429 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6925a1ce-4084-3b12-b306-18b36917fc37 | -9.34593 | -54.5267 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 120577cd-82af-3abc-88a6-94d4946729d5 | -9.71097 | -62.40799 | 2025-10-04 05:33:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6a7c922-ca3a-39b1-b225-2c406923b618 | -14.98305 | -49.97742 | 2025-10-04 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4aa456f8-f62e-33df-918d-4d0144c9eec5 | -14.58319 | -52.49406 | 2025-10-04 05:33:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 197a6c7f-45e7-33b9-9a2e-6111d130c572 | -10.12131 | -52.34782 | 2025-10-04 05:33:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8afa73a-5adf-3613-bac9-6befe7bce69b | -10.89085 | -53.75093 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85d9be75-c779-3adc-b511-ffd377ad26e3 | -9.45285 | -56.65232 | 2025-10-04 05:33:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2617cc99-9e3e-37de-9dd6-005171ceca2c | -9.44786 | -56.65596 | 2025-10-04 05:33:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 313eb396-8268-37a5-94ad-01984ac63743 | -9.52677 | -59.38426 | 2025-10-04 05:33:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc8f3e40-6e20-3b11-888a-dcbe6a03d606 | -15.00294 | -56.02312 | 2025-10-04 05:33:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee1c4b95-2a85-3fb7-9bae-cfdec3ded0e6 | -11.12886 | -55.46701 | 2025-10-04 05:33:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9d62efe-89fa-336a-87e0-c94c1dcb89f6 | -9.26917 | -62.37747 | 2025-10-04 05:33:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcdd8f9d-938b-3012-ab60-ceadab0c514c | -7.8772 | -61.68314 | 2025-10-04 05:33:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84b06c4d-ab2e-3d1f-b1f6-06bf8108d1b6 | -10.59527 | -54.35279 | 2025-10-04 05:33:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51f5bd92-90ce-30f8-ac9e-b132a9d876f2 | -8.64515 | -54.59106 | 2025-10-04 05:33:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46ab6721-a834-3adf-b150-e1d4f483bef7 | -10.63662 | -49.13962 | 2025-10-04 05:33:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab52dbd9-25a0-3d61-9ea5-7adde6884ab4 | -9.90225 | -63.59031 | 2025-10-04 05:33:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53d6dd95-a215-3cb1-acdb-2e0e15801813 | -10.33257 | -50.33376 | 2025-10-04 05:33:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 943cb310-eca6-3f0a-8c9b-af8f5d1f4b80 | -13.17907 | -50.93108 | 2025-10-04 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f3c274c5-5231-38f0-9305-ccbd4d4117b2 | -11.12473 | -55.46087 | 2025-10-04 05:33:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a2f85e9-9373-3e8a-a539-3eb980b9d448 | -11.76184 | -64.92483 | 2025-10-04 05:33:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 523562f1-54c6-3c22-83a7-24d5e9f825f7 | -14.75277 | -54.63248 | 2025-10-04 05:33:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb41f14b-b587-3325-86fe-9ab1dfaa6b40 | -12.9063 | -54.74921 | 2025-10-04 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README129.md)
