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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b47bf60-0149-3347-88b6-73f547630712 | -8.83035 | -44.78294 | 2024-12-01 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ec922485-b6f8-3f26-abdb-47c690fdfba1 | -10.65683 | -44.4894 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bed3c00f-9ed2-3fc9-94d5-ff03df01d56c | -8.94019 | -44.2494 | 2024-12-01 04:46:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e3dbf7b-10ec-3478-8d75-24c0e3def6e2 | -12.92963 | -48.62788 | 2024-12-01 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b200c27-6db0-3b64-ac2b-458d691505c2 | -10.6609 | -44.49524 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5187b39a-5a6f-30d9-9b61-f37395c4ea29 | -11.77948 | -54.6948 | 2024-12-01 04:46:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89dd7c6d-f7d5-364d-b489-09b4e92d7a62 | -10.65546 | -44.49974 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 75fa8d61-deff-329a-ba2f-a9db9ad10eeb | -10.45279 | -44.94178 | 2024-12-01 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d012da89-da8f-3f3b-a4a0-dbc44d08356f | -12.03654 | -54.6474 | 2024-12-01 04:46:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8815b9b-ae7d-39bf-938d-1f0cd37d1256 | -10.66566 | -44.49589 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a5d1f85a-8649-3ea5-8c41-3f139dc26fca | -8.7388 | -47.02713 | 2024-12-01 04:46:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13791750-019a-355e-8781-f29818cac46f | -10.45148 | -44.94316 | 2024-12-01 04:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e9a5bf0-3bac-3e41-a801-4bb91b6ce0b2 | -8.93425 | -44.24697 | 2024-12-01 04:46:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 944a3c29-e0ea-352e-b81e-66d0b013d3f1 | -12.93339 | -48.6284 | 2024-12-01 04:46:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7d2f48c-f1e6-3580-a142-073c0231bd2f | -8.93076 | -44.248 | 2024-12-01 04:46:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 396e7037-dc34-3b46-afe4-4c2e3d85708d | -10.66159 | -44.49006 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e95cac65-fd9d-3e39-88fe-194f101bcec7 | -10.65752 | -44.48421 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c320a446-4bfd-3907-8d8d-00865483a4b7 | -8.93547 | -44.2487 | 2024-12-01 04:46:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70816682-921d-326f-afd8-2823b8315998 | -10.93954 | -45.12222 | 2024-12-01 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e824a60d-06bd-3bb4-baba-f82e86b40435 | -10.66022 | -44.5004 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3f067005-a212-3414-b0b2-24782f43dc19 | -10.93889 | -45.12694 | 2024-12-01 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e892da55-7926-37dc-9243-ae6a82675034 | -8.83553 | -44.77908 | 2024-12-01 04:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65cfd309-2c70-34a7-82d5-995cf30812e5 | -10.60633 | -52.81664 | 2024-12-01 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0742530-88b5-3278-a6a0-a86b3a381f67 | -10.65615 | -44.49458 | 2024-12-01 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 0fbc25ce-6cfb-3358-8428-0f0fc65c78c2 | -8.74271 | -47.02769 | 2024-12-01 04:46:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6188ac9-e53a-33d9-be4c-b52def8773cc | -10.60576 | -52.82019 | 2024-12-01 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 848c9881-3e7f-3ff2-bdf1-908d27c6bf15 | -21.09142 | -51.58532 | 2024-12-01 04:48:00 | NPP-375D | NOVA INDEPENDÊNCIA | SÃO PAULO | Brasil | 3533205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d834ce29-ef10-3f30-9328-88dbccf09cde | -17.65058 | -57.57707 | 2024-12-01 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 618cb069-7d72-3c4b-8b2f-5486dffdc03c | -18.73027 | -48.2349 | 2024-12-01 04:48:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5ae99b1-e8e0-335f-b4b7-713dd88de207 | -2.9963 | -45.5706 | 2024-12-01 04:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1c78a5ab-7183-375d-b814-5ef290cf5f3b | -4.5562 | -43.3028 | 2024-12-01 04:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 8025a271-c882-3a1b-92ee-a8208574b850 | -3.259 | -53.6388 | 2024-12-01 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| eed6a155-fe80-3d8f-a622-97bb883b950f | -4.0052 | -44.7596 | 2024-12-01 04:50:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 9c301161-105a-3729-8381-110f5d720208 | -3.2774 | -53.6383 | 2024-12-01 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 87c948d9-b075-3e56-a18b-067cd7309f21 | 1.1439 | -55.9871 | 2024-12-01 04:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f550aae6-ddfe-3b60-a11d-af2ba51d41b4 | -3.4974 | -53.8339 | 2024-12-01 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 14c7f6a3-fa8d-3ee5-8b26-c1278bb6d964 | -4.5578 | -45.7232 | 2024-12-01 04:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ebb4502e-67cd-30d0-85f0-2b73fd4718ad | 1.1622 | -55.9869 | 2024-12-01 04:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 4d6c6119-9b22-38f4-b374-f964053f66f4 | -3.1273 | -54.5264 | 2024-12-01 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| de7fdc7c-b71f-3ecc-9b0f-86d0039950bd | -3.2591 | -53.6186 | 2024-12-01 04:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| dc8a8696-5f2c-340c-96c1-0a635b237c00 | -3.1456 | -54.5259 | 2024-12-01 04:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 73784ad3-1cf6-3385-8194-2668f011ecf2 | -4.0052 | -44.7596 | 2024-12-01 05:00:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 1a8b8e64-5730-34a5-9a85-d0fb9e2e48fb | -3.1459 | -45.3854 | 2024-12-01 05:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6a8a8b54-d9ad-3cc0-97e0-405ac983c137 | -3.259 | -53.6388 | 2024-12-01 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| bb19f9cc-d7d0-33dc-82f0-753a028c4dbb | -4.5562 | -43.3028 | 2024-12-01 05:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 157.8 |
| ef1cea9d-139a-3d74-8fe1-d9a6879cb3c4 | -3.146 | -45.3629 | 2024-12-01 05:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 9184f7c5-130e-3a49-9b9b-eadb3fcecb13 | -2.8197 | -53.0425 | 2024-12-01 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e0471a6c-ecf1-3920-89d7-8096dc26aa10 | -2.9778 | -45.5713 | 2024-12-01 05:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 77fcfb08-5119-3cd0-94d7-abf0764e9da0 | -3.2591 | -53.6186 | 2024-12-01 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| fa915854-5108-327a-b33e-72359690f7a1 | 1.1439 | -55.9871 | 2024-12-01 05:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| abdd1247-ec5d-30d4-8c6c-04c2de831881 | -2.8013 | -53.043 | 2024-12-01 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| c9544572-dab4-3ed9-a4aa-f792764e3342 | -3.2774 | -53.6383 | 2024-12-01 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 538fd110-2540-34a6-8b5b-da3c17b39fcd | -10.6674 | -44.4835 | 2024-12-01 05:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a2b5cb9a-b20c-3a31-a7de-c17a44c37460 | -2.8196 | -53.0629 | 2024-12-01 05:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 91ee85b0-1b91-33b0-9403-3f7449515ac9 | -4.5578 | -45.7232 | 2024-12-01 05:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3aa9e365-bcf8-3d3e-9ba2-360c7cbb38d7 | -3.4974 | -53.8339 | 2024-12-01 05:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 6b3a33fb-0056-38a6-a6c1-e12f44901622 | -1.31641 | -51.96759 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0ba6b64-f8bf-39f8-9d96-dccb9587bbf8 | 0.0548 | -51.22614 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a8d656-1f46-36df-8bbd-de5ed2bc6a97 | -1.31138 | -51.73013 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b7db371-5643-31b8-8fa0-4ddf1d39e56e | -0.57965 | -51.12609 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a8a0c59e-c607-35ce-bc80-602fadc769c3 | -0.74159 | -51.78318 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaae3268-8117-307c-a4ac-fd8220bdcf99 | 1.18671 | -55.94207 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55981300-9643-3129-8c27-e13d8cd4ed0d | 1.45899 | -55.88171 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3f4f6a6-26cf-38d0-abd6-9248504d09e9 | -1.3197 | -51.67671 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 879152c6-84ec-3cfd-a63b-4ccaa4f88824 | -1.09882 | -53.60295 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27233f69-42d9-35a9-80da-1dd95d4c2540 | -1.18152 | -51.76727 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba9d1344-4123-3a6e-a8d1-f2824b725c4f | -1.16845 | -53.57007 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fac79c5b-3378-3e3f-a97a-da4b790168a0 | 1.21127 | -56.01222 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8eb6abd7-d92b-3960-9625-5735a59501ba | -1.44901 | -47.11546 | 2024-12-01 05:05:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4acd616-2a71-36a8-9135-562ec8efdcbe | 0.07961 | -60.4688 | 2024-12-01 05:05:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a79ab53-b35f-3ae3-ac43-9e7ffd68566f | 3.26989 | -60.08741 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57c63cda-7ad6-3922-bdf8-49770afa515d | -1.0727 | -53.21187 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a8444c6-2386-3a0e-a544-e5a306a4abbd | -1.06491 | -53.63733 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b098ad5f-fa50-3932-8011-2bb7e9d782bb | -1.29588 | -51.72776 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c21897d-37ea-3560-8c68-7a6829f5b925 | -1.23769 | -51.79765 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 079bd13a-c94b-30a2-b0aa-0be9d9ec3ed6 | 1.68008 | -50.66196 | 2024-12-01 05:05:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbec2405-8cf4-3fd4-bcc5-b4889c315387 | 3.26883 | -60.08043 | 2024-12-01 05:05:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed99214-19af-385d-a4f9-511d24e2c5d0 | -0.95763 | -51.65994 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a3dfa50-efce-3a07-993a-a8727957b806 | -1.07708 | -53.39185 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 908413ed-cbed-39d9-963b-5721a40b3289 | -1.06712 | -53.38628 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fd1fa5a-be99-320f-858c-24fab5726d56 | -0.58233 | -51.69144 | 2024-12-01 05:05:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f641eae0-f19a-3d8f-bcea-dabd2ebbabc8 | 1.15203 | -56.0033 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55b7f683-d411-3fc4-8a1c-2bb882cf856c | -1.24645 | -51.73994 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c586215a-b58e-36a2-8e07-06a35ad9635f | -1.16797 | -53.41334 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ed6d791-15c6-32e3-84f6-5b9ddbdb173b | -1.09599 | -53.38655 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 359996bb-0838-3eb3-b3a8-cf1329df5035 | -1.31704 | -51.96979 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8c53d00-047a-3810-8fed-2e156eae5842 | -1.44369 | -47.11467 | 2024-12-01 05:05:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b39d0ebe-b15b-3f2a-bb5e-b8298b2886f4 | 0.97461 | -50.25999 | 2024-12-01 05:05:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edeb2171-6994-313d-8c54-b322a832316b | 1.1471 | -55.9935 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7ad31aab-1eac-37f1-8850-1a9b272672d0 | 1.26926 | -55.90421 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d4f6f32-5b69-3331-9d60-c484157af084 | -2.28693 | -45.60847 | 2024-12-01 05:05:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 20.8 |
| aa64021c-8252-3eac-ad17-9e85c80ccad1 | -1.27491 | -52.70803 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6029e08d-e887-3e84-bda6-0b7bb2c2fdc0 | -1.07945 | -53.63567 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c795eb1-26a5-3e55-b851-39bf5ab01dc1 | -1.0934 | -53.63783 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acf1403e-92f7-3c8f-bf16-5b7edb4db6bb | -1.0919 | -53.13572 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13214a8b-2718-3658-9a73-c06f67f49838 | -1.12064 | -53.2312 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfbdd14a-7d23-390b-b971-e3c71e6905fc | -1.27689 | -52.69537 | 2024-12-01 05:05:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c606b1f3-3635-3e41-ba8f-c1a91e79546b | 2.1211 | -55.87638 | 2024-12-01 05:05:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf0d3e4d-4dff-3068-bc21-9a3e40698927 | -1.19609 | -51.7498 | 2024-12-01 05:05:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d71b12e2-4673-3ccb-8e05-997f75359f95 | 1.19278 | -55.93761 | 2024-12-01 05:05:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README71.md)
