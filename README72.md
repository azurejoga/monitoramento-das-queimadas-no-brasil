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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa8136c2-bbec-3db1-bbca-ef1996c3ff86 | -17.95602 | -57.36651 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 5512c2a6-d7e5-395e-9fa8-2a90781c421e | -17.95535 | -57.37017 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| a4095315-529e-3756-8f71-d42f6d79c111 | -17.95469 | -57.37382 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 8995d92a-6f86-31c6-b151-f9d9e53e2db6 | -17.95402 | -57.37748 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.2 |
| 3db95b6f-fcf4-314e-8048-56d1de062fca | -17.89289 | -57.30488 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| f326edb5-56f9-3a24-b2f1-3132a532a9ed | -17.89221 | -57.30851 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 102df481-471e-344f-8bff-2f8fa373fc9a | -17.89153 | -57.31213 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 15d09659-e814-3b44-aa41-c000ea2f0d26 | -17.89086 | -57.31577 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ebd3ad12-d1f3-37ec-8ca7-53de89a9b3d4 | -17.88891 | -57.30408 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 75acced8-3a1e-384f-86ad-558c7d4f6f1c | -17.88822 | -57.30771 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| ae8c3512-652d-3a01-ba9b-f586ee7e07c7 | -17.88754 | -57.31134 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 602571b5-8cc0-368f-a3fb-096697c881cc | -17.88687 | -57.31497 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4952ccd0-d10d-3669-acce-82d536e18102 | -17.8856 | -57.29967 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 5cf5e82c-2f85-3183-a7bc-4aba46ac7edd | -17.88492 | -57.30329 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 4a57bb57-ec3c-3ade-985f-fe7b58a22c95 | -17.88424 | -57.30693 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d6bc8019-e9c8-3959-b6b5-d1ace3b3cdb4 | -17.88355 | -57.31055 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bb4ce571-933f-3a35-8394-14d7d64ba552 | -17.88339 | -57.30292 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 71277152-332c-37a5-8c9a-9f26296c03f3 | -17.88273 | -57.30656 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 1e7020d2-a146-3de3-a36d-9bda2feb8618 | -17.88208 | -57.31019 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 8bfe6b61-dcac-3410-8d5f-1ef1568e274c | -17.88093 | -57.30251 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 6f27cb0a-a3be-34d9-904a-65d38523a520 | -17.88025 | -57.30614 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0ccf529b-a450-316b-a9c4-25f72dcf1ea5 | -17.87956 | -57.30977 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 30ce000e-dd7e-3514-84da-ca1076329e97 | -17.8794 | -57.30212 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 8ab8859c-26a2-35a7-8bd8-05559c2e667c | -17.87875 | -57.30577 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 211faa2c-ff61-33d6-8b13-a1faa27964f3 | -17.87809 | -57.30941 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 302cc9a3-886e-37e0-9101-885749ff251a | -17.87476 | -57.30497 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a5ec8bc7-6f34-3e60-a89b-7d90bb6ac8b3 | -17.8741 | -57.3086 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 215ad5b8-8599-345c-bbb5-f88ca288071b | -17.87077 | -57.30417 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ef26b41b-97dc-32ed-b698-3b145f6d31a4 | -17.87011 | -57.30779 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 37f169eb-0444-3484-8ac7-68dbe851f401 | -17.86945 | -57.31144 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 05a4d46b-b8b8-307f-8d68-ffb2663d0ebb | -17.86678 | -57.30337 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5d4241f1-f484-3c8b-85b4-57e3c3954a63 | -17.86612 | -57.307 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e126880d-e784-320b-980e-409744aa496b | -17.86546 | -57.31063 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e8a5b83d-affd-3171-828b-ba383b13fb26 | -17.86279 | -57.30256 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9198d63d-97f0-3e57-8e94-48a976e88aa9 | -17.86213 | -57.30619 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e8cfe16b-14a8-3f10-b280-cf120e882c56 | -17.86147 | -57.30983 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| a489180a-5385-3c4e-a0c4-c8d0fea4aa31 | -17.86081 | -57.31347 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6bbed34b-6e1c-3d11-8a2b-367582d40fd8 | -17.85814 | -57.30541 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 1877d31a-eec4-3f8f-acea-1907769855ee | -17.85748 | -57.30904 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| afcb948d-162e-35d5-95e0-d5d208de84d6 | -17.85681 | -57.31268 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e80265f7-d134-3955-b7fd-60b25bec501f | -17.85615 | -57.31631 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 468606eb-9388-3117-a846-8639f19f5486 | -17.85349 | -57.30824 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 288a6975-c820-3639-9afd-c19c96f1a908 | -17.85282 | -57.31189 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6bda7796-b3e0-3ed1-81f0-f032f64dedf2 | -17.85216 | -57.31552 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5550a1c4-53c7-3af1-8390-abadc29548c8 | -17.85016 | -57.32644 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0e3a4ee2-548f-36fe-959c-07d306321456 | -17.84883 | -57.31108 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.3 |
| 0059d136-6865-390b-8038-5da4a048338b | -17.84817 | -57.31472 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 5921d206-b650-3bc4-9b13-b5f575f66221 | -17.8475 | -57.31835 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 536cd40d-e571-342f-bc9a-7e8fd1c74990 | -17.84684 | -57.32199 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 6d661538-85f1-3338-a582-bea9cb331339 | -17.84351 | -57.31755 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| f90695e0-7533-3d90-ab01-969435d60884 | -17.84284 | -57.3212 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9592fdbb-6521-391a-bbfb-af1520982838 | -17.84217 | -57.32485 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 532092a7-41ea-31ff-9462-f9975c3669e6 | -17.84018 | -57.31311 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 79400e6d-31cb-3f23-866e-c580fdfae785 | -17.83951 | -57.31676 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a0788d57-cbd0-3417-b268-500a6d43834a | -17.83884 | -57.32041 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ef850898-547d-37eb-a4ed-ed93c0a6cccf | -17.83817 | -57.32405 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 48b8ef31-b923-377d-9b22-b022f8ac0960 | -17.83552 | -57.31596 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8d8bc253-3a9b-362a-ab09-501e875b3011 | -17.83485 | -57.31961 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 37d08da1-4414-369b-890b-8803b3af26b2 | -17.83418 | -57.32325 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d25a54bd-809b-3cd2-8ead-d69b5a1dccbd | -17.83152 | -57.31517 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 349fb54e-3a17-3c70-bf07-534ed242a04a | -17.83085 | -57.31881 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a0ad9bcf-64a8-3ce0-81eb-24470cb7544c | -17.83018 | -57.32245 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 8efc62cc-9e8a-3834-8588-8c6b9ad67042 | -17.19108 | -57.46474 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| f6f8c17c-7a87-3f87-99cd-b74f11c8e64a | -17.19039 | -57.46854 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 625c3107-32d9-3413-98ae-e9046c4ea979 | -17.1897 | -57.47233 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| a0277ee6-03a6-36e7-9307-ced951f7c0c3 | -17.18638 | -57.44418 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| cd641c51-07f4-3841-843b-d1498309bf3c | -17.18632 | -57.46772 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 6ab715f9-6efe-3239-867d-340e29fad2ca | -17.18493 | -57.47533 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| c471254a-2b9b-31d3-b7d2-fca2e189932f | -17.18424 | -57.47912 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 78114ab9-5a46-3431-ab10-bb12f44c8865 | -17.18301 | -57.43959 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5427198b-1949-3de1-9ec3-20d55c343a39 | -17.18293 | -57.46312 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c901abda-e6ca-3abd-8b3c-dd9899ce6c33 | -17.18093 | -57.45094 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d20fe79a-5bd7-392d-8457-269f5671c06e | -17.18024 | -57.45473 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6bea765b-483e-3811-acab-e43ff9facb66 | -17.18016 | -57.47831 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 7090cc20-a1be-3f69-b8c1-41236a178178 | -17.17886 | -57.46231 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 351f4402-2efb-3c03-9159-661321c4a966 | -17.17817 | -57.4661 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b30c68fb-b8ed-3825-bc3f-de8f7efb5eed | -17.17747 | -57.4699 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 4081ce1b-9ccb-303b-94b6-e0e6d0405696 | -17.17678 | -57.4737 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 0018b7d2-c3c1-3424-bd88-7f677830e45b | -17.17469 | -57.4851 | 2024-10-13 04:44:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| b5c5b1eb-1ec9-33f3-8b89-7a0551742a22 | -19.02348 | -57.62129 | 2024-10-13 04:44:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cdb11647-88e0-31e1-bca8-bc1a6f150744 | -19.02177 | -57.62128 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1548c43b-eb3e-3a80-b424-393e4b405824 | -18.67231 | -57.33794 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 4da97cdb-f557-38ed-a4da-acf96c6ff158 | -18.23192 | -56.50778 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 920b2329-35a3-3aa7-8c55-8c538f4ac39e | -18.23159 | -56.48758 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 432cd200-9450-3145-b9a3-bdb5bfc77ced | -18.23106 | -56.51265 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 11e696ca-ef41-3084-9102-4271fd2f045c | -18.23073 | -56.49244 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 07e856e9-6594-36c4-a901-7c0f08660c11 | -18.22695 | -56.4917 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 5f885682-d1cb-3972-b396-3677c579c3d9 | -18.22608 | -56.49656 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f354c56f-da3a-3f69-b963-3c508b26fe5f | -18.22543 | -56.45628 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f7bae3d-de73-33b7-b7ed-fc8a1680135f | -18.22456 | -56.46112 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8938185e-10b6-3c62-bc99-5b4d8a2c1343 | -18.22391 | -56.42102 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 921c6dac-37a6-378e-8857-c8c65806d0f4 | -18.2237 | -56.46597 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1422d4e5-2b5d-3419-94bc-1da5defc5353 | -17.64896 | -56.25607 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f29e0a46-d5c9-3772-81c9-c84d45e4d993 | -17.64868 | -56.30075 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eb12e3e0-336f-3059-ae25-1a4598658be8 | -17.64839 | -56.28077 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 52865f70-0a01-3b38-83d0-0d6f295750c2 | -17.6481 | -56.26085 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 07be63a0-9968-3768-8f22-83904da96dd5 | -17.64752 | -56.28557 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 11d64d2f-f8c6-3b22-830b-ab67207c1fe1 | -17.64665 | -56.29038 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 4a1b10c6-6eba-313f-84de-1029d2afff7d | -17.64636 | -56.27044 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f4995d1b-94da-3ae5-aafe-a7c51047de81 | -17.64578 | -56.29519 | 2024-10-13 04:44:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README73.md)
