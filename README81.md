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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb9cf71-1b3f-3c3a-a750-fcecd3d01651 | -8.3718 | -62.697 | 2026-08-22 06:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f150611e-3726-3472-be97-1cbe3e0847be | -12.0921 | -56.3368 | 2026-08-22 06:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| f49c702a-605a-3918-a15f-b5e394946308 | -8.5406 | -54.8197 | 2026-08-22 06:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4f1d0ffb-4ffc-36d1-b781-720e4166aafc | -6.8019 | -59.4008 | 2026-08-22 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 46f27b74-e6bd-357e-80e0-71ca4300c077 | -12.1113 | -56.3149 | 2026-08-22 06:20:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f9eae55f-63ad-3164-93ee-5099cd8346c2 | -12.0923 | -56.3166 | 2026-08-22 06:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 2f3f70f5-1432-3cd8-856e-fae384d3216b | -6.7691 | -58.6873 | 2026-08-22 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f2754538-fe79-358d-9a9d-d1af44194af9 | -8.3904 | -62.6774 | 2026-08-22 06:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 173.8 |
| 8b9f51d6-de68-3c63-8433-74f903682084 | -6.7833 | -59.4208 | 2026-08-22 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 49314b24-52b2-38d3-95bf-b266853cfeb6 | -6.7507 | -58.6687 | 2026-08-22 06:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 861fb9c6-f35e-3bad-bf52-3baba31e63a1 | -14.3744 | -51.8038 | 2026-08-22 06:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 12ad0bfc-a452-362e-99a2-25e1ceb2e8e6 | -6.8017 | -59.4394 | 2026-08-22 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c52700e7-1936-3034-9ced-895f1b90b4b6 | -6.7832 | -59.4401 | 2026-08-22 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| cb440f82-e502-3a75-99a0-386ec8a0eb9c | -8.5406 | -54.8197 | 2026-08-22 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| c16a9fe4-14ec-37cf-b363-52c6f0877d72 | -6.8019 | -59.4008 | 2026-08-22 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b6da252c-6f22-359d-970d-d4d1d371ea78 | -6.7507 | -58.6687 | 2026-08-22 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 42704fa1-f296-3526-b2ae-d7577757ef13 | -6.7691 | -58.6873 | 2026-08-22 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 22811942-18d7-3ec0-a527-fda8babed5d5 | -8.3903 | -62.6963 | 2026-08-22 06:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 306.8 |
| d8fcfcbf-f785-39be-9a85-910248988fea | -14.3744 | -51.8038 | 2026-08-22 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bd0b1145-8c5f-3bed-abb1-c8935b565e2e | -8.3718 | -62.697 | 2026-08-22 06:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| eddd27ee-615b-398d-97fa-a3deb3b24503 | -18.0867 | -46.933 | 2026-08-22 06:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 78.0 |
| df0dfed9-ebdc-3cff-9109-5e4bf3aad574 | -14.3748 | -51.7824 | 2026-08-22 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 218274b7-343e-34b1-8a5c-f6657f8a7782 | -14.3937 | -51.8012 | 2026-08-22 06:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 8c772a86-24af-3725-ac27-aa217c702c6f | -8.3719 | -62.6781 | 2026-08-22 06:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 96aa2e69-b72f-3862-994e-83fff56fbf44 | -9.1722 | -59.4629 | 2026-08-22 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 48b64580-f750-3ca9-9feb-ea47f1785f9b | -8.522 | -54.8209 | 2026-08-22 06:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f8af49c5-c223-3ba6-aebc-961418ba7f73 | -8.3904 | -62.6774 | 2026-08-22 06:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 315.3 |
| c149d12b-2297-3872-8981-edd75596eded | -6.7833 | -59.4208 | 2026-08-22 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.8 |
| 4b930254-470b-3963-bafd-92f1871023cc | -6.8018 | -59.4201 | 2026-08-22 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.2 |
| 42e11443-9a3e-31b8-89d8-bdd63b277270 | -6.8017 | -59.4394 | 2026-08-22 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| c9f63c64-49ee-32ec-9b5e-fc48183bda88 | -6.7692 | -58.6679 | 2026-08-22 06:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 7c192a08-04c1-38f0-98ed-7468a72d38aa | -8.3903 | -62.6963 | 2026-08-22 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 242.4 |
| 48563ed1-7a3e-3fed-9ece-5e471c7c78b9 | -8.5406 | -54.8197 | 2026-08-22 06:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a64adc3c-cc4f-3a51-beec-cc81bd2d87c0 | -6.8202 | -59.4194 | 2026-08-22 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| a2c48650-74e2-340a-91bb-0639bfaa9d6b | -6.7692 | -58.6679 | 2026-08-22 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 28cc5da1-22dc-34d9-b1e2-429b51818443 | -14.3937 | -51.8012 | 2026-08-22 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5bcf1990-4cba-39e9-aec0-8d4fe3460244 | -6.8018 | -59.4201 | 2026-08-22 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 0af8f2f6-a1ba-38e9-9f5c-e5544b3e20f5 | -6.7507 | -58.6687 | 2026-08-22 06:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f5054347-9e3d-3100-a0c0-b57133403ea6 | -8.3718 | -62.697 | 2026-08-22 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 32d93235-fa82-32d5-ab49-938e40abddea | -6.7833 | -59.4208 | 2026-08-22 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 17a8e3bd-fe0f-3ac3-9a7e-a8ca686f96cd | -8.3904 | -62.6774 | 2026-08-22 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 284.1 |
| 9591f202-8909-3bc8-8fe8-26f73f19824c | -8.3719 | -62.6781 | 2026-08-22 06:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 974eb89d-9ce0-379f-ac79-115e303a791a | -9.1722 | -59.4629 | 2026-08-22 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 1f50ad81-ea0d-3f69-8108-0ef35972964e | -14.3744 | -51.8038 | 2026-08-22 06:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 62039614-c333-3c44-b039-4466ee9a7670 | -6.8017 | -59.4394 | 2026-08-22 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 9fbb5e4d-0a66-3a17-8d30-7a79c57b0918 | -6.7832 | -59.4401 | 2026-08-22 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| e4469fa8-cb96-3ac5-bb73-ac86028358e8 | -6.8019 | -59.4008 | 2026-08-22 06:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 8b9e8b01-bb0e-3c4e-922b-59ba135a33ff | -7.01944 | -71.77244 | 2026-08-22 06:44:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14c7f838-4f7a-35fa-aeaf-b0e3aad61b2b | -6.7692 | -58.6679 | 2026-08-22 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| b9df0039-93c6-3724-9bc7-d59801358d53 | -14.3744 | -51.8038 | 2026-08-22 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 10532ae4-d3d6-3a19-a4e1-7a1fdd9c57e5 | -8.522 | -54.8209 | 2026-08-22 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c2f3f733-e2de-3f5f-ba53-110e714bad8b | -14.3937 | -51.8012 | 2026-08-22 06:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c1a03ae7-e461-3d67-83ab-57a8a2da8014 | -8.3719 | -62.6781 | 2026-08-22 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 25ea289e-023e-3d80-8b92-053040727cb7 | -6.7833 | -59.4208 | 2026-08-22 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 7a6bed36-40db-34d1-bb59-08c8e03e2a68 | -6.8017 | -59.4394 | 2026-08-22 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f76395a2-6226-39b2-8174-86bde4a199c1 | -8.3718 | -62.697 | 2026-08-22 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| bd4c3d35-b946-329f-adcf-a29421218139 | -6.8018 | -59.4201 | 2026-08-22 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.5 |
| d557070f-648e-378f-825b-b6e731cb68f5 | -8.3903 | -62.6963 | 2026-08-22 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 170.9 |
| 4260359a-78e1-31ee-a904-78bcc4694e43 | -6.7691 | -58.6873 | 2026-08-22 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 837fae77-be5c-385c-9416-7da2e3cfe4d6 | -8.3904 | -62.6774 | 2026-08-22 06:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 169.7 |
| a85fdde6-2e1a-31d5-9daa-1e9fcc92ec25 | -6.8019 | -59.4008 | 2026-08-22 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| db7050d0-ac04-3771-b030-fa62f258e87e | -9.1722 | -59.4629 | 2026-08-22 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 73d3a8f3-8357-39d3-899f-9d65bfd4e3cf | -6.7507 | -58.6687 | 2026-08-22 06:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 065bf2b2-a32b-3c48-b2bb-bd4137424c8b | -6.8202 | -59.4194 | 2026-08-22 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 76fca012-7874-3c0c-aae1-54f8679d83f7 | -8.3719 | -62.6781 | 2026-08-22 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 0dd549f9-221a-388d-99e8-7b274604b153 | -8.3904 | -62.6774 | 2026-08-22 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 25048054-1099-34ca-9e4d-3f5b90612fe3 | -6.8018 | -59.4201 | 2026-08-22 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.2 |
| 3c5f7916-8ff9-3c0d-b903-91907618dc41 | -6.7833 | -59.4208 | 2026-08-22 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| f5d4a449-c02c-3cc1-bafc-a34b2ccb4ffc | -8.9042 | -60.5385 | 2026-08-22 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 612cb7ae-f1d6-30c7-98f2-6a0730b17f30 | -8.3903 | -62.6963 | 2026-08-22 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 6ca4b9f7-2297-3be9-9ed9-c4dfde87e6e4 | -9.1722 | -59.4629 | 2026-08-22 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 3d9144f3-24d8-39f4-995a-7ab67bb5965d | -14.3744 | -51.8038 | 2026-08-22 07:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 276ecbd9-e32b-3acc-b283-a6654500d9a5 | -8.5406 | -54.8197 | 2026-08-22 07:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 31a118ca-f258-311c-96cd-2c4a80dc09ef | -6.8019 | -59.4008 | 2026-08-22 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7aaf878b-a2f9-327d-9313-e214312b21e3 | -8.3718 | -62.697 | 2026-08-22 07:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1ceeb296-36ea-3ec5-96da-50c887e2879b | -6.8017 | -59.4394 | 2026-08-22 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1761c998-74c3-3ca2-af5d-ddfc0f89a48a | -6.7692 | -58.6679 | 2026-08-22 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b61a67d0-8b37-31c6-9c7a-bdcf52e44eac | -6.8019 | -59.4008 | 2026-08-22 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 891423c4-405a-3a1a-940f-be0a831dde22 | -6.8017 | -59.4394 | 2026-08-22 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d94cf133-21fa-39db-aede-d9219ea4aa07 | -8.9042 | -60.5385 | 2026-08-22 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a7d3c4ef-af22-354b-aa2b-3f9785198ee3 | -8.3903 | -62.6963 | 2026-08-22 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| be610c34-5253-3fba-9d0c-cf5e94ff0bb5 | -6.7507 | -58.6687 | 2026-08-22 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 92c98d11-a2e9-323b-924a-fc489a5b6fb7 | -6.8018 | -59.4201 | 2026-08-22 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 148.8 |
| 23e990d4-da6c-34cc-b9f6-caebdadde655 | -8.3718 | -62.697 | 2026-08-22 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b34be61c-49f5-3d12-b7be-3a0cd86df503 | -6.7692 | -58.6679 | 2026-08-22 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| befbcc1f-625d-376e-96cb-32057efca5eb | -9.1722 | -59.4629 | 2026-08-22 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| ee02caf5-eea8-3e65-be81-1f46cc09f165 | -8.3904 | -62.6774 | 2026-08-22 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 865160ae-6e82-30ef-901e-3f01b2a62e9f | -8.522 | -54.8209 | 2026-08-22 07:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| edf83d55-c436-3611-abd6-dfd72bcc482c | -6.7833 | -59.4208 | 2026-08-22 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| bc404009-1a82-3239-9363-1be8b8b1b52f | -8.3719 | -62.6781 | 2026-08-22 07:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 147.7 |
| 1a598d90-e66e-35cf-9ec2-5e55913cb1c4 | -14.3744 | -51.8038 | 2026-08-22 07:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 04aeae3f-0ef7-3379-bb57-e444528bee5e | -8.5406 | -54.8197 | 2026-08-22 07:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 52539225-66f2-3536-8849-34cd7286c55e | -9.1722 | -59.4629 | 2026-08-22 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| ac8cef1e-aeb5-3ee3-89f0-a2be46b20db8 | -8.3719 | -62.6781 | 2026-08-22 07:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 2c2b09aa-e5aa-31bb-a76e-4140203e57e2 | -18.2855 | -43.3119 | 2026-08-22 07:20:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 7d66386b-4999-3e46-abeb-a970ba02005e | -8.3903 | -62.6963 | 2026-08-22 07:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5ffd9c94-0009-3cb2-abdb-32c9e3d606fc | -9.1724 | -59.4436 | 2026-08-22 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 9ca3f612-50ca-379e-a921-62bfc799af99 | -6.8018 | -59.4201 | 2026-08-22 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 8e1af7da-7490-3f91-ac70-a1f17096999e | -6.7692 | -58.6679 | 2026-08-22 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 14192ae3-09eb-321b-bc2e-29902e5e0d81 | -6.8202 | -59.4194 | 2026-08-22 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |


[Clique aqui para ver as próximas entradas](README82.md)
