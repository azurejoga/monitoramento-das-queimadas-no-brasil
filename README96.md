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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 966626f3-dc02-309f-9679-d5d8043f4e7d | -2.78457 | -51.36592 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fde2e562-c236-3fa7-9a0a-82ccf4e1f9a8 | -2.78399 | -51.36969 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63d989db-ab19-3a69-a201-be56aa9b4594 | -2.78236 | -51.36575 | 2024-10-13 05:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20df31be-2f97-317a-9849-b06bd921f27d | -3.96575 | -52.17518 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3dde3f9-3a05-3d7f-9ff6-c0c2798fee5d | -3.96031 | -52.17449 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db5732f4-bde4-3f24-8af2-3f4bf23c14e4 | -3.91423 | -52.21065 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f2410de-a72e-3797-bb17-e3f476869c76 | -3.91372 | -52.2141 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b555bcc-267e-31fd-b129-318c66408a09 | -3.9088 | -52.20995 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c974bb83-5960-3e84-92fa-709e79ca1dbb | -3.87618 | -51.975 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a9827b-abba-34bf-b83a-8743b1907468 | -3.87567 | -51.97854 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265afcd1-e8b8-3c7a-8761-539a897bf7a6 | -3.8754 | -51.97885 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ec5ac32-f167-38b7-93d3-53b7e77f22b9 | -3.86149 | -52.19308 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1692aaf0-ea2c-399b-be02-7c4e99cf54c7 | -3.83424 | -51.87703 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33d066b3-7827-3856-9c2d-5c48776f45e7 | -3.82871 | -51.87624 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25e9ca24-72f9-341c-8e63-c4cd1691c56c | -3.71078 | -51.79485 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 592a8973-d1d0-3925-a72b-592224f8220c | -3.71025 | -51.79848 | 2024-10-13 05:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0ecc2f8a-a031-34c8-8830-e00aa5014e3b | -4.12342 | -51.11634 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbd853eb-5116-3bc4-a0dc-fa7f66837212 | -4.11767 | -51.11489 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db971875-32f7-3011-bc32-dfe192d522a8 | -4.03716 | -51.09739 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69bdc691-7506-3dd4-a00a-bbef8945fffc | -4.03657 | -51.10143 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb7142f6-19a2-3783-a3fc-0e53c8b32b84 | -3.92287 | -51.23214 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71cfa142-818b-3be6-b8d6-b67ece0b9a57 | -3.9171 | -51.23125 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b197dfd4-ef09-3936-928f-68d3fe9d38e8 | -3.91652 | -51.23526 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f497558c-7df5-3e52-9c97-9ffa6a9f2755 | -3.83126 | -51.40599 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecd455ce-2efd-39d1-9ffb-7de7bb22f300 | -3.83068 | -51.40984 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7b34f81-b804-3838-ac75-16326508fded | -3.83011 | -51.41372 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 717af800-e990-38c6-97f0-d8065c3005c2 | -3.82766 | -51.40531 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02d6623b-ba39-3ae8-9ff1-231761311339 | -3.82711 | -51.40919 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59ec6678-583c-3502-8886-ac18b80208e6 | -3.82656 | -51.4131 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 985b328e-cd02-3d6a-b050-e4efd78be167 | -3.82555 | -51.40519 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 924f7461-44ea-32ed-a78b-4bd34b0cd47a | -3.77983 | -51.31858 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f95a7e6-6e7a-396b-b38c-90efb624dc83 | -3.77928 | -51.32239 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac51e2fb-a0b1-39ec-971b-eacbb71c4137 | -3.77872 | -51.32626 | 2024-10-13 05:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ba94f49-dfb5-3bc4-b51e-17c6192e757b | -3.68427 | -51.07797 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a82c98b-96a3-36f2-a273-a647fd4e83b2 | -3.68419 | -51.07843 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eee0c1b-aa3c-3a20-b5c5-a235e5398192 | -3.68369 | -51.08205 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1068d9f-2ea9-3e28-be21-c89094ffa507 | -3.68358 | -51.08249 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a99c427c-6c17-3d5a-948d-da0ed18bf3d2 | -3.67845 | -51.07711 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad64a704-fa1f-3b1a-8620-5be51c853cda | -3.67837 | -51.07761 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcc21a75-ddff-3799-95c5-89a73a6b0083 | -3.67786 | -51.08123 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd938eb0-217c-3d37-8b53-17092084cf6e | -3.67775 | -51.0817 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53735605-fb72-3441-b770-5fed4f2bbcff | -4.27645 | -50.95909 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0df501fc-6d3f-359e-9e68-8fe12d5e4a38 | -4.27583 | -50.96342 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 005ce202-8077-3bae-87cf-567ef801f2d7 | -4.27056 | -50.95809 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b5b0c1d-8446-3595-939e-e393491cd732 | -4.26993 | -50.96244 | 2024-10-13 05:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c1f8ca5-541e-3339-a33d-c212c347f769 | -4.26464 | -50.9573 | 2024-10-13 05:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e43e7a4d-1b7e-3785-a9d1-427566bb1f1f | -0.12617 | -51.57669 | 2024-10-13 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0640809d-7df8-3262-91bb-14f6365efa3d | -0.12564 | -51.58002 | 2024-10-13 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d190c76-d589-318d-b4b2-bdc8d19d65ff | -0.42575 | -52.06806 | 2024-10-13 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8478bc0-b7ea-3516-a6a6-ac996b18ec9b | -0.42528 | -52.07114 | 2024-10-13 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8fe3c777-18f9-3bce-9bb8-dbb718da3d74 | -0.42414 | -52.07038 | 2024-10-13 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 307e8a58-56f2-32fe-9f30-7912348530d5 | -0.42056 | -52.06731 | 2024-10-13 05:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cab5f256-7e66-3926-8fb7-e7deaa243cfd | -1.66128 | -52.13802 | 2024-10-13 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49777edf-7f5e-311c-9250-32b245412cd2 | -1.66079 | -52.1412 | 2024-10-13 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc20aa12-a77e-3422-8063-d5bd2db1d501 | -1.65554 | -52.14032 | 2024-10-13 05:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18e52f40-06fb-3e0a-81d8-f433b1138d4c | -1.43574 | -52.86625 | 2024-10-13 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9012514d-d7b0-3888-b096-5b4e1be3dbc9 | -1.4353 | -52.86909 | 2024-10-13 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2cedcc0-6fc5-32fa-a38c-6fbf39409760 | -1.43077 | -52.86539 | 2024-10-13 05:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f72a1270-820f-3688-ad19-2880a2a8a57f | -3.10477 | -53.03752 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d4b8e6e-80cd-3b00-8f22-e73ba8cd4a0a | -3.10432 | -53.04053 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b24586f3-e320-3156-bfd4-50a53828f067 | -3.10388 | -53.04351 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 38a4bc73-b3df-3294-82c2-5d505df3d3ae | -3.10344 | -53.04646 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f0100510-e885-3ffd-811c-45ef3fe4f9bd | -3.10301 | -53.04935 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f27d7b29-24ed-33da-a4cb-6d924c4532c5 | -3.10259 | -53.05223 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00af8124-4f50-3cb6-995a-f16fe1bf02d5 | -3.10017 | -53.0337 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 563b95f5-893d-328a-99be-11bc6af736c4 | -3.09973 | -53.03668 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62f9f1f3-6808-3c54-a9d1-fddba5d95fa5 | -3.09929 | -53.03965 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d98fb4a-545c-35f0-9a41-67a68aab18ae | -3.09885 | -53.0426 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ab2fca98-d89f-3997-a58d-c8c896671bc6 | -3.09842 | -53.04553 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4351f6e7-e4c7-3a90-a427-3c6bb7a07acd | -3.09799 | -53.04843 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fbd15420-d243-352d-99b9-ab8f1d8428b7 | -3.09756 | -53.0513 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1cbbc05c-304a-36a9-83e0-cc419269d95e | -3.09714 | -53.05418 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be9b88c3-6c72-3046-ad33-af4e668e812c | -3.09512 | -53.0329 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e02a8fe1-0aae-3969-a824-93694d499eba | -3.09468 | -53.03585 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b84bfd43-1f07-3a61-ab0c-4eafb5c78a9e | -3.09425 | -53.03879 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7edabf52-cef0-3652-aba1-ff4723d06642 | -3.09382 | -53.04171 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7d2611bf-7dca-3001-a233-ba4ea4221cee | -3.09339 | -53.0446 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5efcb16a-9f5c-390b-aca9-0089657add05 | -3.09296 | -53.0475 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19ddd9d9-cc29-3c1a-b21c-30e3a17b1232 | -3.09254 | -53.05038 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 823d92f9-8217-3343-8f32-81c465609cad | -3.08964 | -53.03499 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b680d74f-c0cb-3b3b-89e0-d09e4f66c6b6 | -3.08921 | -53.03793 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 19e910be-22ca-3beb-b8c1-69f6d7664afd | -3.08878 | -53.04082 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6a05f491-80f7-313a-8e49-6ba2b8190a8a | -3.08836 | -53.04369 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bc089e4c-33c4-3e7e-bf24-9d65e4b060c1 | -2.98576 | -52.90635 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0495a3a3-1c4f-3c15-bfbb-b933e2613527 | -2.98532 | -52.90936 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be95e661-5eee-3082-8da8-8cd0434877c0 | -2.9826 | -52.90417 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3ad4998-0ef2-398c-99bc-95f841896051 | -2.98214 | -52.90722 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00b0918f-e74d-3ab8-9cd5-81c4b9d00a6a | -2.98166 | -52.91027 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ce550db-8c5c-35c2-b3a4-02d934e4dc64 | -2.98068 | -52.90551 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 144faa00-1b9c-30b2-86da-114ce482a89f | -2.96636 | -52.90821 | 2024-10-13 05:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35584d6b-cf15-379d-a064-1ac506678d38 | -2.66878 | -53.34687 | 2024-10-13 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec363a2d-ec2a-38db-823c-5a40f35643e2 | -2.66794 | -53.35238 | 2024-10-13 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d4cf264-093b-354e-bb55-c37a2a5e92eb | -2.66303 | -53.35166 | 2024-10-13 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08de2d44-7bd9-3c47-b220-aa613aedcd03 | -2.65811 | -53.35091 | 2024-10-13 05:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0313a147-43d0-36f1-96c9-e4ea8f75a0a8 | -3.81117 | -52.40354 | 2024-10-13 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65bbf336-b064-34df-ba8d-49d6c16bbb17 | -3.80965 | -52.40027 | 2024-10-13 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b51c7ec-7ee1-3177-b248-44dc179d1051 | -3.80919 | -52.40351 | 2024-10-13 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83590684-6be4-38df-9973-6a892b05737c | -3.77524 | -52.38852 | 2024-10-13 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8b8b53b-cb82-3872-b70f-327fefaa77cc | -3.77473 | -52.39197 | 2024-10-13 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ee92cd7-e80b-3ab9-9a12-c3792604a071 | -1.88374 | -54.43639 | 2024-10-13 05:25:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README97.md)
