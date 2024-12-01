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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dd407a1-5534-35f7-8945-0c571ad37ae2 | -3.34588 | -50.74947 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89826022-933b-3067-be5e-3076f5642f2a | -3.48766 | -53.80836 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 616d1871-381c-37c7-b570-183648021023 | -2.89785 | -51.58085 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d7705330-5db7-373c-ab53-de988ca082a6 | -2.97378 | -53.90014 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8efad14-9e33-3e53-a682-af5602669fd4 | -3.09315 | -54.02092 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebab2218-2124-3d5d-8cba-375f8503fe18 | -3.50108 | -53.8388 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 83d7ae20-9ba8-3f37-bb62-6689db6865d7 | -1.66723 | -52.49923 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d273c2-d3d7-3a07-9f04-216c0bdcfaac | -2.23117 | -53.62768 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c97755f8-9fb5-3fe7-b95c-d2e13072a4a6 | -6.15044 | -52.04618 | 2024-12-01 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84aa0bf2-5c72-3735-9a24-f6f2f572566a | -1.7039 | -52.47143 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d40b111-c2d0-339f-aaca-e43f465035e5 | -1.56066 | -53.51819 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b26fb9da-7b80-3c06-8dff-15ba08e26267 | -2.3815 | -53.68557 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e8ee896-7d83-3c95-ad4f-7bed7c19232c | -6.71445 | -47.27075 | 2024-12-01 05:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9dff3cd0-007c-3db1-a042-3122330f4cff | -2.46112 | -53.70861 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65513c38-d3ee-3e96-9b56-9f7b39c2aab1 | -3.6363 | -51.45316 | 2024-12-01 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f682f3e6-dcd5-3a89-8ebc-047262ea8f69 | -2.84723 | -54.03748 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5eef781-1091-3c7d-9ee9-8c563b8aaec7 | -2.62952 | -46.87978 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61564d3d-d184-3ca8-92d5-c837da12f5a7 | -2.97063 | -53.45249 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f14a0378-b52c-346e-b2bf-a7193092768d | -3.86799 | -51.01062 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2cdad191-c3a4-3924-b35f-de4e22d337d2 | -3.27138 | -50.21043 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0f1f8ebe-79c6-3a4a-9747-1502342735de | -2.9739 | -53.92766 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31c31121-94fc-3fd4-b483-b20afa13053d | -2.61144 | -51.80867 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac3505df-6c80-3ae2-8598-213f7d7f808e | -3.09272 | -53.71943 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 445bbc75-ec5e-324a-9b5b-7d9f2ba01ce8 | -2.77222 | -55.3498 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 73b7d8ba-7cd4-3abe-9486-4368d9fd819d | -1.26899 | -54.55816 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7823c0a-366c-3fc7-af42-c9c141536137 | -3.08215 | -54.57024 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a6f7ba1-432f-3531-a45b-0bee1c79faf2 | -2.0176 | -53.30068 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13acc854-31e2-3a4f-8117-9a0e3f8021ed | -2.60881 | -53.99034 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0497284-33de-3127-bf83-6f1553047617 | -3.86032 | -50.54114 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 290fdfa4-dea9-31ee-8df5-8e2e587b249d | -3.02605 | -54.03141 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 259c8b6a-4259-3c0b-b4cb-ab1cf85878ee | -1.5968 | -52.28658 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3372aee3-10f4-3214-87b6-b65376a1c973 | -2.74702 | -54.10864 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0fe9634-334f-3992-93b8-dd24fe2c2cee | -3.79165 | -58.97371 | 2024-12-01 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f40090d-13e3-3bcc-85f1-23f42743b0e6 | -2.14792 | -54.87237 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 26dce245-14ec-3e67-a4ce-12ab2c0112ee | -3.05132 | -51.06199 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 51d93834-331e-39d1-8602-329b39520ec2 | -2.72438 | -54.14038 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62121bd7-7ae4-3b0e-a4a1-20ea8e6cd51b | -3.09701 | -54.56482 | 2024-12-01 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94e59e7f-3dec-37f1-a92a-a010166b9022 | -3.02135 | -53.40995 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e05b7428-0277-3630-a113-e3d4d05af27e | -0.57529 | -58.13932 | 2024-12-01 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e944faa8-69c3-3b56-874f-a41b2d882433 | -2.80061 | -53.04865 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7a93122-e481-3416-be35-993ba6d6dae6 | -2.88014 | -50.73989 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76885545-05ab-3667-ab0f-343dfa6e8bbb | -2.59222 | -46.93951 | 2024-12-01 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 253f55b3-cddc-3734-80aa-03e79dd21bbe | -2.97027 | -53.89959 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| baf7bbaf-b02b-37ea-8d39-0bf3245f0be9 | -2.62787 | -54.22284 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc153147-9874-307f-845c-9c4c21c46cc1 | -1.36769 | -53.6389 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fe02a62-3290-3c46-be0b-93847aa66d7b | -2.25471 | -55.83658 | 2024-12-01 05:08:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6638368a-d376-35bb-9374-563f67b00444 | -3.28155 | -50.43723 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c23b3cd-7281-3d04-9d4a-a596683a5237 | -1.24589 | -54.55088 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4fd95e4d-0ec1-3ccd-9e2b-11cc662dc9dd | -3.10507 | -53.1119 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d686d647-da08-340d-b6ff-61b74e928bcf | -2.97693 | -53.88414 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f745ddd-46d2-3d53-8ff8-0cae7582295b | -1.26561 | -54.55764 | 2024-12-01 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 085e8604-bcc9-33d8-b4de-0124d1b0a7dc | -2.04417 | -54.66489 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de6dc9f1-1314-3635-be64-d170283d1a21 | -2.57861 | -53.97781 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d420a6fa-e6c5-3140-b84c-74ccb66d7f53 | -2.95086 | -51.79416 | 2024-12-01 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b44bcb8-6d1a-3136-a3dd-2b0d90ed61c6 | -2.83813 | -54.1056 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68ee4eeb-9c54-3888-b74e-c924a012cbcc | -2.38222 | -53.65739 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 326ec9fc-6d91-3a7d-bdb2-bd02c860fcac | -2.86794 | -54.02742 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5827f16-5c04-3956-a0b9-a252dd3cf83e | -2.6227 | -54.21048 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fa67e79-7a3e-3f84-aa8b-798730b9822d | -2.57811 | -53.67719 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4d9a639-5ce3-34b1-9275-48f585d7c0c9 | -2.36076 | -53.65462 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3512731c-4e75-3ed6-bc6f-78ca5a49e5cb | -4.31634 | -46.53908 | 2024-12-01 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29ab52dd-62e9-3a9e-845c-1ab148faf408 | -3.72348 | -51.10503 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dc9e7a13-c109-3799-b752-432131cd33a8 | -3.26786 | -53.6372 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 86c7782d-41a7-3bb6-a241-eb1266faee69 | -1.61826 | -53.86803 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4be8d84-1410-3970-9886-c3f77370e5c3 | -3.49167 | -53.82932 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac16c90-9189-3154-a2a1-6d8c0578c36e | -1.66466 | -53.77653 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0078ceb-24c7-386f-8d5e-27071f25e124 | -2.84513 | -54.08308 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f648329-aa00-3ba5-a557-30fd5160e68a | -2.88907 | -53.9831 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f235fd1e-6a2c-33d7-9eec-7ba6f5c20a55 | -4.08184 | -50.02739 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89fb055a-cdd6-31bc-8e93-c2cf40dfe517 | -3.2668 | -50.57723 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 859289aa-5b03-3645-9c81-afc515cae2f8 | -3.25358 | -53.63504 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32814401-308f-3bb4-b72f-36354cf7057a | -4.54404 | -43.31487 | 2024-12-01 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b6adfe4b-f14a-3a1f-a050-8e24aa9b9fb3 | -4.1756 | -48.61792 | 2024-12-01 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| de045061-183d-363f-801f-2ccf8f73a208 | -3.21549 | -54.23243 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9e08966-c07b-3aad-a797-857c91a7aa95 | -3.47995 | -53.81124 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8475d558-b90e-3148-b88b-873ab494e84b | -3.2127 | -50.27174 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3f60675-9129-3a23-9595-3bd171ba50e9 | -3.06207 | -54.05276 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 354d361f-909a-36ec-b6ce-50d4240d4588 | -3.46187 | -53.88151 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8187767-d46c-3581-af74-7dc3e77307bb | -1.64669 | -53.86822 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2811722b-3437-3c7f-b370-e700234de0ca | -3.12215 | -53.80835 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6e59cb45-16a4-3d59-bdae-e58b5f74a10e | -2.89017 | -53.99916 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a87f4e8-47f3-3494-af8f-e46bd4d91d30 | -3.08834 | -53.29589 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38686d49-6881-3f37-813c-474a370e4341 | -3.14391 | -53.24844 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07c082db-8178-34b4-94db-a4835c4499bb | -2.82918 | -54.03867 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d5ceda-7c66-395e-b553-462a1d9e0674 | -3.01149 | -52.02418 | 2024-12-01 05:08:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e148f3-2a58-3811-85f4-df663bcd57bb | -1.81838 | -54.87303 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ccd23e9-2f8c-3076-8815-c42b82835c88 | -2.81053 | -54.04372 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 869c9f3e-1c76-34c2-a8f0-154fac86f103 | -1.70427 | -52.44412 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db788e5b-2aea-33d4-b1b0-9e4dcbfb91a4 | -1.43161 | -55.19303 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc81be7e-b8c8-306d-843d-fa599e03539a | -1.69432 | -52.63222 | 2024-12-01 05:08:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ca8174b-5286-38fb-b04a-87a100a4a967 | -3.24848 | -53.92785 | 2024-12-01 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0784d828-9c35-3cf4-9748-1991f85934bc | -1.95013 | -53.34175 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 33b9afe2-27ef-3249-9484-1820ae51ab05 | -2.04754 | -54.68765 | 2024-12-01 05:08:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a908741-4ac0-34a8-87c6-533317e89be2 | -2.3674 | -53.68338 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 580c4b6a-13c7-3c1b-ba97-67267ba0dda3 | -2.82147 | -54.0651 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fb246a4-dfe7-35bf-ad8e-cfdbe0055f87 | -3.02233 | -52.35291 | 2024-12-01 05:08:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da66d882-73f5-37e4-ba86-6849ede68d78 | -1.62642 | -53.86137 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2438f2f-f462-3ca7-8f10-bc9733e8a96c | -2.96703 | -53.45197 | 2024-12-01 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60d598ab-1225-37c4-a72b-53a9a2549a59 | -2.6076 | -53.99805 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2035c4b7-ed7e-32c3-821b-cfe45d306fd5 | -2.63015 | -54.23095 | 2024-12-01 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README93.md)
