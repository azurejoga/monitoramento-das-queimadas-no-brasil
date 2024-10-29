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
| 4c469cdf-e054-3d8a-a4e0-9799507d6d53 | -13.36445 | -45.10798 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 77ff8be5-8fe8-3d43-acfb-405b16397505 | -13.36353 | -45.10051 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7625005d-47ef-39d8-ad12-65b6554a6352 | -13.36226 | -45.10658 | 2024-10-29 03:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 482760ce-9d7a-311e-8cae-9df807cf852a | -17.17103 | -39.42847 | 2024-10-29 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6a448e3a-7a43-350e-b3ab-efed4e538579 | -17.16663 | -39.42758 | 2024-10-29 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ea224694-3e36-3800-be2e-91ce9bab75bc | -17.16581 | -39.43188 | 2024-10-29 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c0345f62-9b26-3a93-b660-9b7e4c908145 | -15.93047 | -41.97676 | 2024-10-29 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b485c290-9fbc-3d47-a458-d115ddaf1de4 | -15.92443 | -41.97933 | 2024-10-29 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9e5fe8c-0d7b-382d-a764-baec3b6031d1 | -15.92374 | -41.9828 | 2024-10-29 03:25:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 811d6967-174a-3e7c-b097-6f1c9d84b9fd | -15.2103 | -42.36425 | 2024-10-29 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 47bb521f-9f59-35df-bc8c-aa67a66a7039 | -15.21003 | -42.36173 | 2024-10-29 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5d919259-2746-31f2-8a62-b04f362e4081 | -15.20956 | -42.36793 | 2024-10-29 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 206a5a40-a5f2-3d30-8482-1337ebe4eb2a | -15.20927 | -42.36541 | 2024-10-29 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| fb761ac5-be5b-3e7c-9e35-71d4d9186ff6 | -15.20477 | -42.3632 | 2024-10-29 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| eb0b8ee6-44c4-342a-b4a8-1584c50c9c42 | -15.20404 | -42.36684 | 2024-10-29 03:25:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 02177344-6fe3-33c3-a255-37d12b18601b | -14.94892 | -43.34938 | 2024-10-29 03:25:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8ea70b9d-9d87-34c0-afef-604093b1309f | -14.94802 | -43.35371 | 2024-10-29 03:25:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f5264ab6-46a3-3125-a9bb-eb684fad7bd4 | -15.44863 | -43.62729 | 2024-10-29 03:25:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc742043-f795-3c49-aa05-29e2102fa057 | -15.4477 | -43.63176 | 2024-10-29 03:25:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f84813cf-b5d6-3338-9ad4-318394d14437 | -3.0501 | -50.4171 | 2024-10-29 03:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a1a430af-c87b-3ed2-a05e-1ce139d60b1d | -3.0913 | -54.287 | 2024-10-29 03:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8f65fda1-bd75-30ac-918e-7f8cb4015563 | -3.1097 | -54.2865 | 2024-10-29 03:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| 5bf8262a-571e-34fc-8f78-b5d784166bb9 | -3.1098 | -54.2665 | 2024-10-29 03:25:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b3e07b59-9a75-3dec-af59-af7a9a6bccc2 | -3.1794 | -50.3922 | 2024-10-29 03:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 37f777da-b4de-3bb7-8026-356681e74d45 | -3.2503 | -46.8709 | 2024-10-29 03:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| ee4855f2-309e-3b84-b992-1efbac870866 | -3.2688 | -46.8703 | 2024-10-29 03:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| a608088f-b413-345f-bd64-5c02829c69c7 | -4.2575 | -46.1188 | 2024-10-29 03:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ca0a86f1-dbbb-36f3-bbe0-fe0c63ffcf34 | -4.2576 | -46.0965 | 2024-10-29 03:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1e8a3011-91d0-3741-8209-7c8eddee8e93 | -4.2761 | -46.1178 | 2024-10-29 03:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 112.8 |
| a369e88a-b2cd-3d02-ab10-518ca79fe89f | -4.2762 | -46.0956 | 2024-10-29 03:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 42675d73-2ce2-3516-b2d7-f6edb5b8c714 | -12.3334 | -49.9208 | 2024-10-29 03:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| aebf0b93-05bc-32ef-b019-a370a0c73edc | -12.3522 | -49.94 | 2024-10-29 03:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 940ee575-9d06-3f8d-b8e0-34302f765af8 | -12.3526 | -49.9184 | 2024-10-29 03:26:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 17d347c4-a447-3ea9-90e3-c20853eb5a59 | -3.0501 | -50.4171 | 2024-10-29 03:35:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b73fa9a2-1f90-3f50-9600-78942910ba14 | -3.0913 | -54.287 | 2024-10-29 03:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 27f3b1e0-9a9b-3a73-b04c-172816bfd189 | -3.1097 | -54.2865 | 2024-10-29 03:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 90f666f6-4a53-32dc-aaa2-12f4d69ce5e7 | -3.1098 | -54.2665 | 2024-10-29 03:35:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 89aeb8e7-d56b-38f9-836b-2b1beb9f68ea | -3.1794 | -50.3922 | 2024-10-29 03:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d3350316-e262-3868-a722-7def2677252f | -3.2503 | -46.8709 | 2024-10-29 03:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| 5bf7dbd4-2d91-38de-8b61-2790573772ff | -4.2761 | -46.1178 | 2024-10-29 03:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 31053de5-9f56-340d-af23-0fe555bcb96b | -4.2762 | -46.0956 | 2024-10-29 03:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 142.9 |
| 73816286-3cfc-33c1-af37-b2048e0b69af | -11.138 | -55.5313 | 2024-10-29 03:36:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b5e498e7-2abb-36bd-a441-430ebe9c7975 | -12.3522 | -49.94 | 2024-10-29 03:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b6fba7ef-e7fc-3e00-ae50-7f39944c17e4 | -12.3526 | -49.9184 | 2024-10-29 03:36:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 116a6545-5425-3dd1-b47e-2aacd2ffc52c | -13.6028 | -45.587 | 2024-10-29 03:36:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| bcd3f4fe-531e-3524-b379-05031a794f6f | -2.5066 | -47.4425 | 2024-10-29 03:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 6b929410-d659-3b94-8fd8-8086567645de | -3.0501 | -50.4171 | 2024-10-29 03:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 43450983-246f-3dbd-b9dc-ac7d35751a4a | -3.0913 | -54.287 | 2024-10-29 03:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 076c880d-51d1-36c5-a11e-591b06562100 | -3.1097 | -54.2865 | 2024-10-29 03:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| e5ad78be-a387-33e6-a978-14b29e7215e5 | -3.1098 | -54.2665 | 2024-10-29 03:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 6c9a8de2-1f39-3bc6-9cd8-8e4f8098e12d | -3.1794 | -50.3922 | 2024-10-29 03:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| cf22ebb3-d0c3-37b5-87ae-2b6cd1eaa6ab | -3.2503 | -46.8709 | 2024-10-29 03:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| 54ea597f-42d3-309c-86e3-bd0cbc9ea89d | -3.2688 | -46.8703 | 2024-10-29 03:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 12c54a32-5d4e-3398-b093-be3c706ae82c | -4.3473 | -43.779 | 2024-10-29 03:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5065dabb-ecc3-3035-9907-9cfefd62dec1 | -4.2576 | -46.0965 | 2024-10-29 03:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 564156eb-f152-37e8-b331-da0afbf14827 | -4.2761 | -46.1178 | 2024-10-29 03:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f8dda7f2-9d8b-3df2-977a-a8bf0275a8a9 | -4.2762 | -46.0956 | 2024-10-29 03:45:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 316cd414-bd5c-37db-8c84-26388bbc23bd | -6.5631 | -51.1126 | 2024-10-29 03:45:43 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 509fca32-4198-3fce-8a4f-8bba91f024ed | -12.3331 | -49.9424 | 2024-10-29 03:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 931c549c-bd75-3352-84ef-6874ea4041de | -12.3334 | -49.9208 | 2024-10-29 03:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a084f286-adef-35d4-930f-6553552c4275 | -12.3522 | -49.94 | 2024-10-29 03:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| d7f459de-a428-3183-a6b2-8ce6136a9e8a | -12.3526 | -49.9184 | 2024-10-29 03:46:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 137bb988-5862-3853-ba27-aeff1270f6f8 | -7.10427 | -39.59169 | 2024-10-29 03:47:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e36ef7be-dbfc-3c05-9ad7-603cb8cb183a | -7.10362 | -39.59565 | 2024-10-29 03:47:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72b2d368-9af3-363c-9b1c-9203ead0c238 | -7.10075 | -39.59116 | 2024-10-29 03:47:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 07d23ef4-547c-3f54-b026-bbb6244cd048 | -4.40486 | -40.69464 | 2024-10-29 03:47:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2c9e53b8-5b90-3828-b8fc-2b01f3dd4ef9 | -5.42737 | -35.56183 | 2024-10-29 03:47:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f72b4fea-46c4-3bca-9857-b8f8b2d5f6f6 | -7.69928 | -34.92764 | 2024-10-29 03:47:00 | NOAA-20 | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 69e2f9cb-5e6a-3572-89b1-debce012460f | -7.64011 | -35.36453 | 2024-10-29 03:47:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f4fdde0a-2ae2-3f24-a5ba-cb3bc6c128a9 | -7.63672 | -35.36401 | 2024-10-29 03:47:00 | NOAA-20 | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| da1ffa6a-18ae-3f84-afd9-e36a13a136bb | -7.47711 | -34.8449 | 2024-10-29 03:47:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a143586e-9c60-3d84-9754-bc2d7d99c3ce | -7.47442 | -34.84479 | 2024-10-29 03:47:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 36e40af8-3454-335c-8514-8e936d59175f | -7.20869 | -35.23199 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a85bc4c8-b250-3df2-9391-b8dbc64fcc31 | -7.20529 | -35.23145 | 2024-10-29 03:47:00 | NOAA-20 | SÃO MIGUEL DE TAIPU | PARAÍBA | Brasil | 2515005 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e0d12313-fd6a-36c1-bf2d-8b863d0981fb | -7.20474 | -35.23512 | 2024-10-29 03:47:00 | NOAA-20 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 916e6a94-5c05-35f7-a241-3a1759380cc7 | -6.82956 | -35.32432 | 2024-10-29 03:47:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0514c92d-6021-3cfa-a511-ecd33a2a1f5b | -6.81505 | -35.44039 | 2024-10-29 03:47:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 498ddd6e-dcc4-3755-bd3a-c1946581662e | -8.15915 | -35.38226 | 2024-10-29 03:47:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 20503353-a9c4-3802-a4f1-d78a103a8180 | -8.15859 | -35.38597 | 2024-10-29 03:47:00 | NOAA-20 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d74bddab-b72f-3e3d-8ac7-03b51329cf64 | -10.927 | -37.66767 | 2024-10-29 03:47:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a467fcd6-1c56-391e-9fbb-82dc6466151f | -6.1196 | -37.83726 | 2024-10-29 03:47:00 | NOAA-20 | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9569b1e8-6745-3867-81e0-817bf38764c0 | -5.04982 | -37.99854 | 2024-10-29 03:47:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8b5c93c-55fe-3043-98c9-1158b22b2283 | -7.87539 | -38.14198 | 2024-10-29 03:47:00 | NOAA-20 | SANTA CRUZ DA BAIXA VERDE | PERNAMBUCO | Brasil | 2612471 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 754dc50f-a809-385e-af09-bd82633378e7 | -7.56549 | -38.76014 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 45db262d-3952-3c41-8981-2b4688c4d7fe | -7.56328 | -38.75225 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d3e9d475-6217-3d5b-9d06-1ed011200628 | -7.56269 | -38.75593 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f71a734b-d94d-3871-8b16-8237159c52fc | -7.5553 | -38.75858 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e23ac228-ade5-38df-a18a-f60a8426204e | -7.5547 | -38.76225 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5cec133a-e8df-37bf-8a16-71e3d396aef9 | -7.55131 | -38.76171 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be8555b1-2b0d-3ae2-9899-edf13776de6c | -7.54851 | -38.75747 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3499ad90-b7ac-38ea-a3d3-d01c3160f4fc | -7.54572 | -38.75323 | 2024-10-29 03:47:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 777b9bb2-000c-3225-b3fd-488cc9ff8049 | -7.23946 | -38.84472 | 2024-10-29 03:47:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8d1753f2-beaa-30fd-8e32-d41be136bd05 | -7.23886 | -38.8484 | 2024-10-29 03:47:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e66601d-8594-3fb8-a345-1292a084504b | -6.67687 | -37.47298 | 2024-10-29 03:47:00 | NOAA-20 | PAULISTA | PARAÍBA | Brasil | 2510907 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ebad1d92-fc70-3ffc-b65e-d79315070a93 | -6.67466 | -37.4655 | 2024-10-29 03:47:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c538a5c9-4f2e-3db3-bd19-528ee2d42b48 | -6.67355 | -37.47248 | 2024-10-29 03:47:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 22b4a406-fad5-3ad5-8e11-dc10be07cae0 | -6.67134 | -37.465 | 2024-10-29 03:47:00 | NOAA-20 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59c666c7-abe3-306c-bd1b-3d3b31d04c04 | -13.05475 | -40.34915 | 2024-10-29 03:47:00 | NOAA-20 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a11bc64e-1b10-3e36-9fcc-2a0f41481c48 | -12.76748 | -39.55336 | 2024-10-29 03:47:00 | NOAA-20 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3efbbd4-67db-3f16-beeb-447ca3aa2bfa | -12.7653 | -39.54554 | 2024-10-29 03:47:00 | NOAA-20 | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |


[Clique aqui para ver as próximas entradas](README25.md)
