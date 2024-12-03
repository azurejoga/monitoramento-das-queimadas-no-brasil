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
| c9332013-f556-3ab0-9b63-223be8e1fc02 | -5.8113 | -46.48062 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d611e71d-1c10-3a3c-879e-bd4733ba4a4d | -4.05401 | -46.99202 | 2024-12-03 04:29:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 997d0fa1-8dc2-3e24-ae71-7f1771be0030 | -5.11877 | -43.20545 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 65ba65d8-76ed-3d72-8436-2bb64c00cf6e | -5.56766 | -44.89012 | 2024-12-03 04:29:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15abcbb6-0c42-39ce-a9e3-878cf307ddac | -2.83462 | -46.86029 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e61e853-0f2f-3d11-a350-91bba2c34911 | -1.75363 | -52.78641 | 2024-12-03 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14b33cba-a541-37a1-9ce7-dd9843f6a94f | -2.04922 | -51.19518 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90e63259-c22c-3602-bfb5-a23bc4f15ec6 | -2.68174 | -46.60075 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e599cdfa-45a7-3c90-8d28-10ef4e3842a0 | -3.18788 | -51.16838 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23b6598c-2db4-3e44-a9db-644390dfa165 | -2.55738 | -46.57047 | 2024-12-03 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 528dc854-2088-3cb3-ac22-a7d4777e6ee9 | -3.1169 | -45.98959 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccb14dfb-0a27-3b0e-9498-742e87d7102e | -4.04533 | -48.2745 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5aeec36-2ef5-329d-85e4-29c244b07d6f | -3.08723 | -53.37733 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ddfd58a1-bca2-31a2-839c-3c83583931ee | -1.99883 | -50.65673 | 2024-12-03 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f64acee-7ff3-3428-8f1d-7a62428e9043 | -4.4181 | -45.90298 | 2024-12-03 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0cfcf09d-4084-3465-b540-65a9b1a9f967 | -3.26328 | -53.65348 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf418044-d039-3f4c-9d38-c0e5ec091425 | -2.7288 | -46.23674 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7eb3178e-ba4d-32c6-b114-a122a0f17cb0 | -2.48799 | -46.58085 | 2024-12-03 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec3813d7-b1d9-3383-b7fe-d64e5af9d607 | -3.17275 | -54.32842 | 2024-12-03 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea215e16-5e4d-3898-86c3-874c1c3d4a5c | -2.98732 | -53.90537 | 2024-12-03 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56c41b66-6fca-3eb9-833e-51f905f26f7e | -2.55023 | -53.40984 | 2024-12-03 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07fb57f4-f445-32d6-b6ba-d0a7024ca12b | -2.71748 | -46.13543 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a7faf8-2141-39ea-bbe8-6344abc550b2 | -2.51546 | -47.42037 | 2024-12-03 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7b2b03f-ac6c-395e-85e4-4363e214f579 | -3.82729 | -46.59534 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63465eb4-ef95-3859-939c-e3851192e008 | -6.11891 | -43.95814 | 2024-12-03 04:29:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f773945d-239c-39ea-a055-348359ed4d01 | -4.82092 | -43.43695 | 2024-12-03 04:29:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c69e3dd0-bfeb-32ed-b8b7-194261ed3858 | -2.72934 | -46.23328 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33a26b99-2c22-30e0-bac2-a87a1d6a82a8 | -3.34426 | -46.05675 | 2024-12-03 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d093653-c288-3d12-8f27-c62801672ad1 | -3.02682 | -51.539 | 2024-12-03 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 697a2875-fd6a-3a74-b352-158055aaa9a3 | -4.06943 | -46.6972 | 2024-12-03 04:29:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e030fe5d-271f-372b-afae-9ac23f0eeb6e | -4.32476 | -48.09579 | 2024-12-03 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f9f30cf-f5d4-3c22-b9be-66ac996017d5 | -3.85571 | -50.53944 | 2024-12-03 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea13696a-2752-3a7c-ad86-39c801651f42 | -2.66098 | -46.12669 | 2024-12-03 04:29:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5446daa-1b9a-3592-9c2f-e7588950a0c1 | -3.97971 | -48.19216 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6811790-9fd5-3731-898a-7a522a51738b | -2.81786 | -53.06318 | 2024-12-03 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13ea3b91-a35c-3cbb-87f0-ee38fa026233 | -1.42277 | -55.30392 | 2024-12-03 04:29:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 859143d4-2307-3b5c-9330-a44cc790efee | -5.8074 | -46.48362 | 2024-12-03 04:29:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 8f4c6f2b-9152-30d6-8f74-c342dfa48eb5 | -4.14263 | -48.23897 | 2024-12-03 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 928051f2-b215-3b41-b20a-15ad10d6721b | -1.0735 | -53.4562 | 2024-12-03 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 919daed0-03ca-3dc4-b950-8e20764513e8 | -4.1914 | -51.1914 | 2024-12-03 04:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 8ac30298-6f14-3007-8516-ef2870a2dfe7 | -3.0944 | -53.3804 | 2024-12-03 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| f72e3024-02f2-39b0-a6b9-8e3781287e17 | -5.1181 | -43.1964 | 2024-12-03 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| da47cd15-954b-39b9-8793-fab207eb82a2 | 3.1288 | -60.2901 | 2024-12-03 04:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 32.6 |
| d12961dd-157a-3a18-ab80-76fb22e35b76 | -3.076 | -53.3808 | 2024-12-03 04:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 978c7735-2b0d-33da-9479-053c8d93ea80 | -5.118 | -43.2198 | 2024-12-03 04:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5043cbac-7685-3562-af42-0e779772eb75 | -1.0919 | -53.4561 | 2024-12-03 04:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 122.0 |
| 7eb336a8-0640-30ae-b870-4192882ca3a3 | 2.7267 | -60.3916 | 2024-12-03 04:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d7508569-ae44-3248-936d-55dfe26903cb | -5.8195 | -46.4929 | 2024-12-03 04:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 63eb5c1d-2dc6-32ec-ac61-dd05ca021d88 | -5.7824 | -46.4732 | 2024-12-03 04:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 672cf685-87f0-3041-aa59-52dc226974a0 | -5.801 | -46.4719 | 2024-12-03 04:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 89585dca-9f17-3c25-80e8-ea797c0b0f03 | -5.8197 | -46.4706 | 2024-12-03 04:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 12aac7f2-34cb-3fec-8281-f8a956991993 | -5.8009 | -46.4941 | 2024-12-03 04:30:00 | GOES-16 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| f71a11e3-3a81-3c3a-8b08-32a51efc7c27 | -10.15736 | -47.54068 | 2024-12-03 04:31:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59680aee-74e0-39d0-9221-9d2918fea9f2 | -8.87711 | -47.26615 | 2024-12-03 04:31:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6506ff7-05c7-3e31-832e-750479407666 | -9.81589 | -44.70758 | 2024-12-03 04:31:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f966202b-2aa4-3d72-a60f-81d59ffdf710 | -12.43351 | -46.67099 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d3353bd-81c3-3bb8-90ca-8cda18fe01aa | -10.46061 | -58.67914 | 2024-12-03 04:31:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21bf4269-f2a4-36df-a6b0-bff515c72e08 | -12.63577 | -46.72032 | 2024-12-03 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7427f7b6-f729-321f-922e-3b1221950fd5 | -10.66257 | -44.49209 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b0d118b-0f64-31c9-ba2a-ea340b886f6a | -10.65492 | -44.49096 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b0335df-66ba-356b-bff2-4f172b00467d | -9.647 | -42.16574 | 2024-12-03 04:31:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 525a6d63-9090-3f3c-8114-8f0212ff69ed | -9.57356 | -44.75314 | 2024-12-03 04:31:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee1601b0-b8fe-3b65-aa46-e182072e3ffb | -10.65041 | -44.49519 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1a36fa8a-8d2f-34fa-9a4c-365ce41fce49 | -10.09396 | -47.38062 | 2024-12-03 04:31:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cbcb421-bcb2-3ccf-9f59-3872b0edd490 | -12.49913 | -46.34897 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 127edb1c-8b3f-3704-906d-d6a96dd673c2 | -10.45062 | -45.07974 | 2024-12-03 04:31:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f32de795-7797-3b29-91d0-5aed2c39dfae | -10.65423 | -44.49575 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2d509306-1aaa-3641-8007-c411a78f51c4 | -12.43292 | -46.67492 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41970b76-0b8d-3197-bb0a-d83c6da35844 | -8.73988 | -47.02908 | 2024-12-03 04:31:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53fcf3ac-25d8-3e8f-954d-699c68950e95 | -10.57431 | -44.70341 | 2024-12-03 04:31:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2369dcce-0ce3-312f-b38f-cb53f14570cb | -12.50292 | -46.35079 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62ce7697-4c9f-35ba-96fe-7854e3138ef0 | -9.53642 | -45.35968 | 2024-12-03 04:31:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0dd736e-5193-358c-9766-b23d31c7aa61 | -12.49137 | -48.79913 | 2024-12-03 04:31:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5093e6a0-de84-37e0-a96e-3f641c93f647 | -10.6241 | -49.03343 | 2024-12-03 04:31:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af29d965-e9b6-3f15-8186-2946e1eed29f | -8.88045 | -47.26668 | 2024-12-03 04:31:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6350aa03-e8d5-3a13-a783-99fbc0e3417f | -10.6511 | -44.49039 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bc55fd6b-dac5-3616-981a-5ac0d394ab05 | -10.41745 | -49.24442 | 2024-12-03 04:31:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5cc36856-5e0b-3589-a352-6e0c5910533c | -9.16449 | -43.11768 | 2024-12-03 04:31:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10ea167c-3f1d-3a98-81cf-702fb005347b | -9.1604 | -43.11711 | 2024-12-03 04:31:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0b8a70f2-88ea-30ea-b4a4-f8e4ce2d4992 | -12.43233 | -46.67884 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6777bfef-971a-314a-8e68-54f725d2e9c9 | -10.65806 | -44.49632 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e423ea0a-c77e-3824-ab67-205439547cf7 | -10.89029 | -38.61833 | 2024-12-03 04:31:00 | NOAA-20 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8725cb9-44f9-3d51-b8bb-b7f14e4c39c4 | -12.70141 | -47.63285 | 2024-12-03 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3bc49511-b23b-3d3d-8b2c-c7fa35adc145 | -12.50209 | -46.35358 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb69d407-d919-300b-817a-a7b6514f8977 | -10.66188 | -44.49687 | 2024-12-03 04:31:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6423b846-d6f9-3010-9199-25345d7e8398 | -12.49855 | -46.35302 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db76533c-bf78-3ea5-93a7-b5bb26d2c86d | -10.45433 | -58.68183 | 2024-12-03 04:31:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95ac6234-22fb-3a02-b454-79c3001d594b | -10.45362 | -58.68552 | 2024-12-03 04:31:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2fa69d0d-6499-393c-bc9e-2194e244bd9c | -10.89597 | -38.61905 | 2024-12-03 04:31:00 | NOAA-20 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a8e92b92-eb7f-37a9-9a70-1352c65d110d | -13.92969 | -43.51219 | 2024-12-03 04:31:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb7e641c-ed75-31bd-8f51-f3defd7705a9 | -12.49938 | -46.35024 | 2024-12-03 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a7e123b-7da8-3298-a08f-448a5d2a9138 | -10.20202 | -47.58422 | 2024-12-03 04:31:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0091c30-bf1e-3d63-9608-462f594fe8fe | -9.6466 | -42.16745 | 2024-12-03 04:31:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0efa5cfb-e9cb-3d7d-9e75-2a7a274f0f9f | -10.20147 | -47.58779 | 2024-12-03 04:31:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7d68ec7-bd8d-3900-b6da-7ac8d53b18b3 | -28.71779 | -51.71901 | 2024-12-03 04:36:00 | NOAA-20 | NOVA BASSANO | RIO GRANDE DO SUL | Brasil | 4312906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a652759a-a360-3163-8e0d-4012c6a7f09c | -27.85785 | -54.44863 | 2024-12-03 04:36:00 | NOAA-20 | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3e7e4235-57d0-3ce6-9d61-f780d2cf2845 | -27.85745 | -54.44523 | 2024-12-03 04:36:00 | NOAA-20 | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| de434f99-de5f-3ea8-ad57-20f1f9ec5a19 | -27.85678 | -54.44929 | 2024-12-03 04:36:00 | NOAA-20 | SANTA ROSA | RIO GRANDE DO SUL | Brasil | 4317202 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c84edb1c-fbbd-312a-9865-02c12c63d79b | -3.2958 | -53.658 | 2024-12-03 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a1b18ed9-736a-3b6a-a483-c8d7a81af010 | -3.0944 | -53.3804 | 2024-12-03 04:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |


[Clique aqui para ver as próximas entradas](README54.md)
