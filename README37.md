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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c957869-9559-3653-9d18-fd21615be4e9 | -14.1707 | -45.3042 | 2025-08-18 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| bce3a781-f1af-3ba7-8c55-0193f65e6eac | -14.1902 | -45.3008 | 2025-08-18 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| d779805f-9932-3802-913f-8893c06e067c | -6.5203 | -45.4787 | 2025-08-18 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 47427d36-5c0f-3c64-ad07-af63fd07a66c | -6.5205 | -45.4561 | 2025-08-18 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f06a8234-cc8d-33f4-949c-708c166b08d4 | -13.8748 | -45.5411 | 2025-08-18 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 80ce16e8-505b-3509-848b-85081816df35 | -14.1702 | -45.3276 | 2025-08-18 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 473dad20-86e1-3362-8bb7-154e08f348ac | -14.1902 | -45.3008 | 2025-08-18 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 2d35ac1b-c59d-3e32-93cb-2fca103d083a | -13.1746 | -54.9337 | 2025-08-18 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 233.8 |
| 8fe621ed-4399-3ae0-a7f3-f2692fbc14c3 | -14.1897 | -45.3241 | 2025-08-18 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| bebe1166-23ff-3724-8af9-15ec356773c5 | -12.8418 | -46.0309 | 2025-08-18 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 608b21ed-92f3-3569-8dda-0ba3d8914b5b | -12.6435 | -45.3269 | 2025-08-18 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| a121e318-d51d-351d-bac0-7a810642b1df | -14.1707 | -45.3042 | 2025-08-18 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 105.5 |
| b77a8f77-eaff-321f-9d8e-5f4526def7c5 | -6.5203 | -45.4787 | 2025-08-18 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 5aee8c8b-6834-3672-81e2-b71a383344c3 | -13.1555 | -54.9357 | 2025-08-18 13:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 6226eb32-6ce5-32e6-ba39-1b950f008930 | -8.7414 | -46.6674 | 2025-08-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 9645a864-6914-3089-bae3-59c43729dd35 | -8.7602 | -46.6655 | 2025-08-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 50bf0c08-90cc-39fb-bfea-67a00061d32e | -12.3129 | -50.0097 | 2025-08-18 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ab8819d1-3edc-391e-8708-1fe92595340d | -12.8422 | -46.0079 | 2025-08-18 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6902a266-1b0d-352d-a322-52aec6289d7c | -13.8748 | -45.5411 | 2025-08-18 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 512859e4-f037-3614-b9ad-61ba46d89a5e | -8.76 | -46.6878 | 2025-08-18 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 340.4 |
| 1141111d-f63b-34c2-9c30-803dbe4de9f7 | -13.8752 | -45.5179 | 2025-08-18 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 31e2edce-5731-3ebc-83cf-9c3c69bb2fa0 | -12.2938 | -50.0121 | 2025-08-18 13:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 2bc3db02-46ca-36f8-a635-f54a89446b1f | -12.2938 | -50.0121 | 2025-08-18 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3338ca24-1f72-3f3b-b8af-2451faf1a34b | -13.1558 | -54.9151 | 2025-08-18 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 0829912f-9df6-3f70-a8fc-25cdb44693b6 | -13.2567 | -50.7947 | 2025-08-18 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b0d4087f-6824-34bd-82d8-210ffde07a33 | -6.5203 | -45.4787 | 2025-08-18 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 419.5 |
| c42a32b2-5360-3a73-8782-f25112e1c5c2 | -13.1994 | -50.7806 | 2025-08-18 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 92d92932-105e-3c07-81ac-0713fa23da68 | -14.1707 | -45.3042 | 2025-08-18 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 8006bef8-8d7e-37a3-b4ef-88aa0b70332c | -14.1702 | -45.3276 | 2025-08-18 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| a1571676-7a84-3802-8569-353064808231 | -8.7414 | -46.6674 | 2025-08-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 007c80ca-9eab-3aa2-9853-3203e6f41f26 | -13.1746 | -54.9337 | 2025-08-18 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 386.9 |
| 98714089-7a51-3e13-bcee-bbeb988f831f | -14.1902 | -45.3008 | 2025-08-18 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7dde6021-1c51-3152-b477-bad3908d40e1 | -14.632 | -54.9187 | 2025-08-18 13:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ebe7b5eb-007c-364c-a754-0539f041e571 | -12.6435 | -45.3269 | 2025-08-18 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 1c01303f-a3cd-3c82-a7d7-52302c388f26 | -5.7949 | -45.0132 | 2025-08-18 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 9c0891c3-905d-3e88-a6b3-3ddfef12dac8 | -14.1897 | -45.3241 | 2025-08-18 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 792aa349-7c32-3f8e-9ac1-8aca43da1576 | -13.8752 | -45.5179 | 2025-08-18 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a2c86542-9a28-31d2-9588-cfca268b2c8b | -13.1555 | -54.9357 | 2025-08-18 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 185.6 |
| e55b7513-f996-3c13-8be0-4cb20ac893e4 | -8.7602 | -46.6655 | 2025-08-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 70673894-17b4-3553-a926-8ccbf4dc9915 | -13.2375 | -50.7972 | 2025-08-18 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 8cb9991b-f42e-3d47-97c4-0b0bd6b5e0d7 | -13.1743 | -54.9542 | 2025-08-18 13:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| a42bf2b4-980a-3e0b-be92-c560b87750e6 | -13.8748 | -45.5411 | 2025-08-18 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| ad4eb125-f911-39d4-ac27-ce4ca73ae626 | -8.76 | -46.6878 | 2025-08-18 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 7695ce9f-fa62-3d8e-a3c2-c6051efed6df | -13.1555 | -54.9357 | 2025-08-18 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 190.0 |
| f8072073-927c-3320-be85-0b593ad6ac70 | -10.5418 | -50.3615 | 2025-08-18 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.3 |
| b6bf459b-4fd2-383f-8ccf-1e9c5fd356f9 | -6.5203 | -45.4787 | 2025-08-18 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| abc7c749-2d55-35f7-928e-df7e40c14776 | -14.1902 | -45.3008 | 2025-08-18 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a464d8ae-3615-3ee4-8c37-91f5471456bc | -13.8748 | -45.5411 | 2025-08-18 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 011677f3-7803-3bd0-abed-7d7a5888be31 | -12.6435 | -45.3269 | 2025-08-18 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b80730db-12b5-3171-9f2a-c1942f560fab | -9.3989 | -48.2994 | 2025-08-18 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| e872b109-d8f5-3f6f-91f6-ac6d528f368c | -10.5415 | -50.3828 | 2025-08-18 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 931ce989-6bdf-316e-a373-ab2fb3c235f3 | -8.2257 | -47.3165 | 2025-08-18 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 965bf8b8-9b0a-366b-b8b8-9ef615004ab2 | -14.1707 | -45.3042 | 2025-08-18 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| d71820d2-96ad-31ea-95d7-5a0efb164bbf | -13.1746 | -54.9337 | 2025-08-18 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 210.4 |
| 73ac3ca8-fbee-3a56-8320-9300a0412820 | -13.2375 | -50.7972 | 2025-08-18 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 43761ef2-0109-301a-a80a-bd814121fb99 | -13.1558 | -54.9151 | 2025-08-18 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| d6710d40-323f-36cb-86f8-7abf86c03d2f | -13.1994 | -50.7806 | 2025-08-18 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 190.3 |
| 3c67b0aa-85c3-311b-a284-e04f0c072fd2 | -14.1897 | -45.3241 | 2025-08-18 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| c7646278-a01f-3710-9c00-0dacb99c0b07 | -12.9366 | -46.1076 | 2025-08-18 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e02a12ef-82b9-3af7-bdd8-987660c8080f | -13.1749 | -54.9132 | 2025-08-18 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 70823deb-f37b-3f63-96f8-f6bbe01316b5 | -12.2938 | -50.0121 | 2025-08-18 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| c6b6e80d-7b83-3331-86ca-3d07fe5bf521 | -8.76 | -46.6878 | 2025-08-18 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 47b211b9-8244-3e82-aec0-24d4ea7af363 | -13.2567 | -50.7947 | 2025-08-18 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3674dd9e-f808-33f8-9010-54f9a75620e8 | -8.2257 | -47.3165 | 2025-08-18 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 42d268e0-97b6-3e8d-ae68-c5a488f3852f | -9.3989 | -48.2994 | 2025-08-18 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 63dedc8b-7c12-39cf-80f9-026182c665c1 | -13.1749 | -54.9132 | 2025-08-18 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 666212a1-60a5-39f9-b5ca-3820a5e78ccc | -12.2938 | -50.0121 | 2025-08-18 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 8c05c67b-9872-3778-ad02-065d2cc0d42b | -13.2375 | -50.7972 | 2025-08-18 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 08808a67-2516-3b25-9524-039af123fad0 | -12.6435 | -45.3269 | 2025-08-18 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 9afcaec9-5873-3d75-b0df-f1b43db1890d | -6.5016 | -45.4802 | 2025-08-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 0cd68957-72d1-34c2-8640-5611364b598e | -11.1609 | -46.9471 | 2025-08-18 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 4b86d7c0-c6ef-3b4a-9b1f-76c243c8bdbd | -11.9108 | -43.4081 | 2025-08-18 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0c232c40-3cff-38ae-ad1f-649a089a0968 | -7.2224 | -44.6914 | 2025-08-18 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| af81479e-8a9a-31ef-a158-acd60cd8b2b8 | -14.1902 | -45.3008 | 2025-08-18 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 0c7f0f18-9257-3951-8586-0da987cf8a33 | -6.9712 | -43.6066 | 2025-08-18 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 842.8 |
| 80c4bf34-1205-31bc-ab7a-fd8178f27d48 | -3.982 | -42.516 | 2025-08-18 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| eed6a540-d994-33e0-a899-1f6a5abb8efb | -6.9715 | -43.5833 | 2025-08-18 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 763.6 |
| be9ea4a8-24a3-3125-8845-784a668465e4 | -13.8748 | -45.5411 | 2025-08-18 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 87800fb5-2ed7-3c2f-b9a1-13219adecb23 | -13.1994 | -50.7806 | 2025-08-18 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| d1c9ff2f-5acc-3e95-84c1-c1465fad082b | -7.2036 | -44.6931 | 2025-08-18 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0ede7a29-362e-3b3c-8c29-ddc85a2d46bd | -8.76 | -46.6878 | 2025-08-18 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| d51c982d-4439-3157-b1b8-db2ad72a892e | -3.9819 | -42.5396 | 2025-08-18 13:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 1ab32f28-3630-32bc-955a-2981e4192c13 | -14.1897 | -45.3241 | 2025-08-18 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2e6820c9-3b77-34ba-b9ec-c50562e49610 | -13.199 | -50.8021 | 2025-08-18 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 7d31d051-480c-36d4-8a37-665dd3bd2962 | -12.8611 | -46.0279 | 2025-08-18 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 0e3b9ce1-616d-3ef0-9903-9048dfabca8e | -13.1555 | -54.9357 | 2025-08-18 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 225.5 |
| fe9825a5-9b08-383f-ba8b-14b6237e0d2f | -12.8418 | -46.0309 | 2025-08-18 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| ebdfe6b0-a371-3793-b9f4-125099475724 | -10.5415 | -50.3828 | 2025-08-18 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 43e2002f-fe86-3b0f-8ad9-2fd9ae23e115 | -7.2039 | -44.6702 | 2025-08-18 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 74d9d2ee-aa66-35ef-bbff-e2043529198d | -10.5418 | -50.3615 | 2025-08-18 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 015b3f03-c19a-365b-af98-41c2373eb65c | -6.5203 | -45.4787 | 2025-08-18 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 203.8 |
| f4eca891-0667-3e30-8279-8130b9a05e39 | -13.1558 | -54.9151 | 2025-08-18 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.7 |
| f32757ea-f61a-31ee-b0ba-41b1b16875f4 | -11.1425 | -46.9047 | 2025-08-18 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 639b3b6b-3da2-3126-97d5-e932caee6002 | -12.9366 | -46.1076 | 2025-08-18 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8d0d4b04-981b-3c98-8e88-812824e5c14f | -13.1746 | -54.9337 | 2025-08-18 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 235.7 |
| cc57aeb2-7232-3426-b727-5c291482e7ee | -11.9104 | -43.4319 | 2025-08-18 13:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| f7bc5452-7797-33c5-92ea-da194544fad8 | -13.199 | -50.8021 | 2025-08-18 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 1e459176-d580-319b-9642-bf088b8e42e0 | -6.9712 | -43.6066 | 2025-08-18 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 567.2 |
| 7f034778-5f1f-3d94-a56b-12dc4eb4d554 | -8.76 | -46.6878 | 2025-08-18 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 71f5b3e3-1a76-3aa6-bc0f-333531ff247d | -6.5205 | -45.4561 | 2025-08-18 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |


[Clique aqui para ver as próximas entradas](README38.md)
