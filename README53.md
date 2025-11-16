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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 839b3283-b477-3914-b713-554ee5801c37 | -3.53955 | -49.26233 | 2025-11-16 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 75157a8e-86ef-35d8-aaac-50ecf059d314 | -4.43362 | -43.39358 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0fca205-d05c-3c46-90bf-d828bdd2b201 | -1.99002 | -47.34744 | 2025-11-16 04:55:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 205a2c49-db0c-3282-b8f3-d2a0356c7569 | -3.60473 | -52.04948 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce17323f-fec9-35a3-8e10-26a297e86918 | -4.20622 | -48.56416 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee7c922f-5ad3-3760-8cb1-004cf4f50b3e | -5.77475 | -44.38249 | 2025-11-16 04:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 718ae6b2-afe2-3e5f-9c68-6e6a6b388d65 | -2.85424 | -51.27972 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0123fc53-1f0e-3fbc-ae93-89f5ac9c6933 | -1.19268 | -53.72327 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a3f0025-46ff-3c9a-8aef-602c4df6dff2 | -3.53839 | -53.52076 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3a11748-0802-3d55-b023-4a5210163cd1 | -2.94288 | -48.74178 | 2025-11-16 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de213481-abef-35c7-8cb6-037c477fc50b | -4.80625 | -48.33895 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da51126-162c-320d-9f96-88d887cbe4ea | -2.14423 | -45.34832 | 2025-11-16 04:55:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ed0990b4-23d7-3b66-b673-c72373646bc3 | -3.08442 | -52.92134 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ce5a24a2-26ba-3d4d-a487-4d6edf15e962 | -5.24492 | -43.90703 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05a4b6cb-10ed-33f4-8fe3-ac6a7181ef14 | -3.40592 | -50.26896 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f331eb2-ae13-3960-8314-d813482d96de | -3.33255 | -50.27963 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3476f8b8-91c1-3ff4-a2a7-a3cbcca91307 | -2.82103 | -48.32714 | 2025-11-16 04:55:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b960a9c-60a1-3615-b10b-66866115ddfa | -2.93757 | -51.76377 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23556d63-d208-3893-a2c2-98f78460f6b5 | -2.5162 | -47.81124 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5953b2e8-1930-3e0a-88c4-ba1aa038a97d | -3.13423 | -50.28873 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 850b8634-cba2-3881-89a8-a964f3c897fc | -2.8875 | -51.42866 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0b6ee4c-0f7e-3466-bf7e-47c67315e953 | -5.99285 | -41.90882 | 2025-11-16 04:55:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 501b9351-959f-3138-9f2f-79a8785015e6 | -4.6293 | -47.41126 | 2025-11-16 04:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| af3701a2-eaa6-3dfb-94b0-75e8304e26cd | -3.82231 | -52.05006 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62c792a2-2225-3341-b1fc-d03f3ab7c213 | -2.97251 | -54.65274 | 2025-11-16 04:55:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06adb494-62e3-3b67-b2ac-95bf91a1fe4a | -3.38342 | -47.18714 | 2025-11-16 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f803fd2d-9425-3b09-918e-8d53178ced45 | -3.58399 | -41.65961 | 2025-11-16 04:55:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0ca49765-3f4f-346d-bd3f-6825bfbce0dc | -5.22657 | -44.43491 | 2025-11-16 04:55:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a55f31a2-cf5e-382e-9a22-d66847d8a2ee | -3.46651 | -50.11574 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04c8ff86-d68e-3310-bec8-1ee9083edd11 | -4.73821 | -46.38799 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c3d133b9-f356-3e0c-8721-0aeead9cf315 | -2.96552 | -53.22303 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3de3a094-4eb8-34f3-bcb6-193bace0f2d7 | -3.97803 | -48.93483 | 2025-11-16 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa6c5c6c-174a-3af9-8faa-c0ff07940d20 | -3.27728 | -52.99405 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ac3f76b-7200-34bd-acd1-fc8d93b352f6 | -4.40782 | -43.41 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b07628c8-4de3-3600-94f7-e13391ba7154 | -2.68754 | -49.08031 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59c6b164-24f0-35b9-935f-89adab4b585a | -2.30514 | -53.87647 | 2025-11-16 04:55:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa2ef067-e130-3388-bbc3-0d6f4cf2ff7f | -4.39742 | -49.66245 | 2025-11-16 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c33834e-6b23-3152-ad92-6f755a28357a | -3.06206 | -44.74356 | 2025-11-16 04:55:00 | NOAA-21 | SÃO JOÃO BATISTA | MARANHÃO | Brasil | 2111003 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45ce1964-e5a1-32b2-aedb-93a0d0663d3b | -2.84846 | -48.65088 | 2025-11-16 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6ea18cd-2996-36a5-9cf1-93f60ddb0d38 | -3.58188 | -50.41942 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3b9344d9-6955-3774-bffd-ef2e6dfd8319 | -2.58488 | -51.86742 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a212213-c3fa-3d8a-913f-aef8479e8568 | -3.19794 | -57.04951 | 2025-11-16 04:55:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb8b55af-06ef-37a6-ac79-d34077f69c5e | -1.97448 | -56.42327 | 2025-11-16 04:55:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 566aa9d5-8865-3644-994f-6b0c092f92c0 | -3.22041 | -49.22138 | 2025-11-16 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cbbbac27-ec80-32df-8c36-7f18c5997045 | -3.30947 | -53.85049 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6662b90e-d5f9-3e25-b6e9-cb4e178449fc | -2.40327 | -55.96682 | 2025-11-16 04:55:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed766b48-6037-3b4a-a9c8-af32c5c8f2b7 | -0.878 | -48.08486 | 2025-11-16 04:55:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e92662bb-c9f1-3a3c-a1d1-5a8f970f6cf4 | -4.76143 | -49.38383 | 2025-11-16 04:55:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b44c75e-7784-3b2d-b783-008376c976de | -4.72948 | -46.38173 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 755d0ec0-f41b-3dbf-9d9d-bf4b38b0becf | -0.95699 | -52.33747 | 2025-11-16 04:55:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36ff1374-f725-3a4e-a1fc-854d73721b17 | -3.33842 | -50.16999 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b2a64642-c00d-3dcb-942e-75471bf4ed26 | -1.39934 | -55.82642 | 2025-11-16 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e02a96a-a8d8-394c-9a20-ef040237fc37 | -4.4319 | -43.40554 | 2025-11-16 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7862d00d-e005-3d5d-abef-8aa9e3c8816c | -2.90931 | -49.7934 | 2025-11-16 04:55:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8ded10c-bbc8-3e62-a775-c489a1c01aae | -3.30617 | -53.84998 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67ada17a-2c4c-3197-8882-f635ad03387c | -5.42572 | -47.325 | 2025-11-16 04:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ed30b79-6d8c-31fb-9c92-de2913ec0189 | -4.74292 | -46.38866 | 2025-11-16 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6d344cb9-64a1-399d-a15c-82beaebc5a94 | -3.41263 | -52.36449 | 2025-11-16 04:55:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd1ddbfb-7ba9-3249-8a86-592a7b942b9e | -3.4904 | -54.04205 | 2025-11-16 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 53a0e25c-ca28-33aa-b629-dfdfaa5971f1 | -3.02093 | -51.60625 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3c16c2b-3325-35a2-8cf9-3d11fb0636b8 | -4.64857 | -47.94634 | 2025-11-16 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bc6e61d9-69bb-3d43-8240-94415cdeb2ab | -2.96606 | -53.2196 | 2025-11-16 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dcac24b-44e0-363f-8600-f70d570a67bc | -3.44584 | -56.48297 | 2025-11-16 04:55:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0560128e-3c76-366d-981e-d33531912349 | -3.46222 | -50.1194 | 2025-11-16 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab12f538-e7e2-3686-aef0-5611e357bab1 | -2.52446 | -47.81249 | 2025-11-16 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fb76f527-7690-37b3-b73c-4d62066ec516 | -3.94852 | -47.20596 | 2025-11-16 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10803a05-0448-3888-952d-2d597123b92f | -3.38456 | -47.18516 | 2025-11-16 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f2c4b36-220c-3d1e-8e9a-a1da26306b69 | -4.81432 | -45.50403 | 2025-11-16 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc3db04f-1987-3bdc-b1da-b31bb800d658 | -3.02001 | -51.31979 | 2025-11-16 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0c44aed-de97-3226-a4f5-263b183adae8 | -1.87882 | -51.03034 | 2025-11-16 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b783432f-7bc3-31c7-a8e7-288ed8fc3b7a | -10.04547 | -54.32605 | 2025-11-16 04:57:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7b19564-09b7-356c-904a-0d7bb34359e9 | -8.06015 | -43.10004 | 2025-11-16 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 6a70b049-1f87-313d-be96-c3f798206ac3 | -12.24108 | -54.37048 | 2025-11-16 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51367a10-b96f-3967-bf90-f9453ab949f7 | -11.91758 | -46.1869 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87dbb0ad-2f4f-3967-8d30-cb57759f5ecc | -10.1644 | -44.50795 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc9bfc0b-5245-337f-a739-eee2158f11be | -6.67124 | -42.04261 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 11e6ff1e-8c34-331e-b519-e35a7b1b28ae | -12.05991 | -46.97734 | 2025-11-16 04:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97bc5bf7-103f-3006-8e4e-5592d5b2d489 | -9.82983 | -47.08226 | 2025-11-16 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37232da4-b34f-39d5-992b-05fbfe1018cb | -6.14334 | -48.0456 | 2025-11-16 04:57:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97f9b03d-1a68-3168-8ed8-cb988e730801 | -5.71309 | -48.90309 | 2025-11-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 58851d6c-32e4-3fe3-b50e-a32dfa787db8 | -7.36199 | -46.58323 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cfbf8a74-9034-3d7e-9a4c-a0cc36dabbcf | -10.71191 | -44.52697 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ded34d34-3a8c-3e36-b52d-847b6a305b0c | -8.2073 | -43.56664 | 2025-11-16 04:57:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a36dbd4-94e2-3cd4-993c-8dd945423bb1 | -12.7981 | -46.44903 | 2025-11-16 04:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce47d49c-1e36-3270-be1c-1d1b985267a7 | -5.84592 | -47.67991 | 2025-11-16 04:57:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a39ba10b-eb62-3f22-9fe9-0e120da26313 | -12.21435 | -49.6134 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b71ec2d4-e8c3-3c2a-978b-6c58809b675c | -6.55272 | -43.46833 | 2025-11-16 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1b203b9e-be2f-3e9d-b7a8-e6738e2933a7 | -10.31963 | -48.13109 | 2025-11-16 04:57:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d65affa-3f77-3782-9ff2-7edb90d64fcc | -11.73291 | -49.84652 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7dee5f0-14ce-3125-9abd-00ba21e2d0ff | -10.53198 | -44.83606 | 2025-11-16 04:57:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a361cc9-4be3-3f81-98f8-56dacfff97f9 | -9.06165 | -44.79242 | 2025-11-16 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1845e01a-fa27-33c8-a35d-0e1a43f3484e | -7.92278 | -47.09957 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cc7d834-7f9f-341b-80f2-44876e4579a4 | -9.23877 | -57.26027 | 2025-11-16 04:57:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2daf021a-515b-3a9e-897c-8f2e995d3f0d | -9.73458 | -43.96186 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d2f4b4a-56e9-3c7d-899a-934871ec68bd | -12.65988 | -46.74725 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 89e8b198-8796-3246-9455-2b85b1531142 | -12.69044 | -46.79602 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c55ac2ee-d524-36ad-a921-cd10104e61f5 | -10.05139 | -46.76492 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52499876-0a95-372a-ba81-eebd1436b3ce | -7.26323 | -48.02373 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f371fd92-fc60-3734-8f15-787ff1c75eed | -11.16238 | -49.45086 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1a67a73-0ca4-3062-bc8a-8960b190ff22 | -12.06298 | -48.20921 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README54.md)
