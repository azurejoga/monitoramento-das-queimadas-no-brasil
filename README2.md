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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e4a28540-860e-366d-bee6-4cb4f0fa4752 | -2.6963 | -46.2719 | 2024-11-24 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4b10ffee-c066-3b8d-8612-d94f718f9ebf | -2.464 | -49.0811 | 2024-11-24 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 9731ee1a-0278-3ef5-8294-ecaff661054b | -3.2212 | -53.922 | 2024-11-24 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| db742efe-1589-3f37-8a38-fa893a99ffdb | -1.8053 | -46.649 | 2024-11-24 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| cd3f2e8c-d2d9-3158-826f-7dfb7bfee858 | -2.8606 | -51.8143 | 2024-11-24 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| c2484d57-f602-34e6-a63b-ed315cff71eb | -2.7411 | -49.1162 | 2024-11-24 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.7 |
| cd6e9338-98bc-3995-b9d0-01644987b850 | -3.5158 | -53.8333 | 2024-11-24 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 4f5b0c6b-429c-3711-8513-97d91981a0f2 | -5.0998 | -43.151 | 2024-11-24 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 3f43c3bc-2f90-31c4-9277-c410a3219704 | -0.8723 | -52.7686 | 2024-11-24 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 79de8dab-02c2-39d2-888a-906efbf7c735 | -0.8724 | -52.7483 | 2024-11-24 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| b4d054e4-e897-30ea-beb4-c1475102a570 | -1.3666 | -53.8362 | 2024-11-24 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 8bfc0344-53e7-3d50-b385-041f7f9d663a | -4.2234 | -48.6986 | 2024-11-24 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 782228dc-860b-3103-9859-3e1060a342c4 | -3.1068 | -45.7903 | 2024-11-24 00:20:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 78.5 |
| ac5b86e6-843f-3a67-8a9c-5368726713fc | -4.242 | -48.6978 | 2024-11-24 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 120f809b-9f67-3d20-93cc-6b6f6fba6622 | -3.0582 | -53.2192 | 2024-11-24 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| ee7335b1-719f-373c-b11e-5fc0eb652f93 | -1.8239 | -46.6265 | 2024-11-24 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 196.7 |
| d4611851-076a-3c4a-b02c-fe2fe0d6e710 | -4.2605 | -48.697 | 2024-11-24 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 5e262e4c-be7a-3892-bb8b-671955ec41c5 | -4.5403 | -42.9066 | 2024-11-24 00:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| feec8680-e5e8-311b-b682-99d8435dfb1b | -3.2386 | -54.223 | 2024-11-24 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| dbce6b0b-7349-39b9-a499-2d7e4b01f53a | -0.8907 | -52.7481 | 2024-11-24 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 6b2b8ce3-be82-3c38-b19c-d1430f366a43 | -3.2604 | -53.2746 | 2024-11-24 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| ebff2885-eb18-3ecc-af2e-63e9850ce548 | -3.242 | -53.2751 | 2024-11-24 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 6fd25376-ca62-3884-8fa9-e3a97a64c1be | -4.2419 | -48.7193 | 2024-11-24 00:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 4b692e10-293d-350b-949b-4844a9e0bc0d | -3.8304 | -46.0057 | 2024-11-24 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 64a32143-56a5-3559-b4b4-649ab027b292 | -0.8907 | -52.7685 | 2024-11-24 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 185.5 |
| c44faa20-eeb6-3657-b0b0-ef3574517ad3 | -2.7596 | -49.1157 | 2024-11-24 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6fdb033d-c3a4-3ec6-af99-e231e3e2ff7c | -2.9229 | -45.3712 | 2024-11-24 00:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 806f1261-61b0-3ab5-849e-40d9a4a4c802 | -4.3559 | -45.2847 | 2024-11-24 00:20:00 | GOES-16 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fb454f0f-d161-32c8-ae0b-b099ebe9a8b8 | -2.5657 | -51.8833 | 2024-11-24 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b24f303e-f2b6-314f-91d0-884aca6aa3a6 | -3.5343 | -53.8126 | 2024-11-24 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 5135571b-598b-3f94-b4cb-eef53c3ae185 | -3.5159 | -53.8132 | 2024-11-24 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 2f878ed6-87e9-36cc-ba8c-8eb956b5e5b5 | -1.4732 | -46.0357 | 2024-11-24 00:20:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 87.3 |
| c724f46e-bd0c-3369-aeda-74ac199b5b93 | -3.2569 | -54.2226 | 2024-11-24 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c185b6af-6749-3c11-9d53-91a2734c5d26 | -2.5842 | -51.8829 | 2024-11-24 00:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 4ffcbfa6-6dd3-3404-80fa-5ded9e9d2c6f | -2.4456 | -49.0816 | 2024-11-24 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f57fae80-5f89-348b-be51-bf08ca8f5369 | -1.6042 | -54.415 | 2024-11-24 00:20:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bfef3994-bd41-36ef-95e4-8352d3b0d5c0 | -2.741 | -49.1375 | 2024-11-24 00:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 29fa9bb1-634e-3f18-894b-1489ddc9df38 | -1.8238 | -46.6486 | 2024-11-24 00:20:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 63d79865-7d88-3d79-97a5-f82e754df8a8 | -1.5129 | -54.1959 | 2024-11-24 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 7acfddb9-ae34-350d-b033-c9f425ab87a4 | -1.9805 | -46.419102 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c590080-6094-3c78-8ee2-2967eec09a61 | -5.5347 | -39.212399 | 2024-11-24 00:21:00 | METOP-B | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 80f13e1f-e6ec-3f8c-afa3-b256b90d918e | -2.392 | -49.054401 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eabb1b3-5b0a-38d6-9924-c8e0ed335c97 | -2.2739 | -48.987598 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ba797c1-53cc-3b60-b692-89d77b090de6 | -3.0831 | -49.194599 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33743ad7-f98b-3dd6-b4c1-e63562429c23 | -2.3822 | -49.056499 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 238cf90c-41d6-3700-8f24-6e6dbea842f3 | -3.1756 | -54.315601 | 2024-11-24 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c27ec90-c7ff-3bad-8b13-deb9d6de26b1 | -2.1864 | -53.647999 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03279334-db93-3368-8248-d860b4b90060 | -2.2049 | -48.91 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7c373d-70ae-39f1-af27-2b3295983945 | -3.2206 | -53.916698 | 2024-11-24 00:21:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63eccee4-161e-3b62-ad70-61d726fac88b | -2.2798 | -47.146702 | 2024-11-24 00:21:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93dd643b-f452-3088-a643-6d575ab45a21 | -3.3839 | -50.719501 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ceffb92b-4add-3248-b842-2461115a2114 | -1.8366 | -46.647202 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d67713-479f-3ee3-b0c1-2955347a97b8 | -2.4027 | -49.102001 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7efbb3e6-cf3b-3a59-91e6-b3b57bb271ea | -6.6435 | -47.3437 | 2024-11-24 00:21:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d6f6287-0bcd-3061-9f7d-bdbc7a2983dd | -4.7671 | -44.7771 | 2024-11-24 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8355460-73f6-3a9b-af0f-e45336ea6561 | -3.2473 | -50.109001 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df8d4c0d-d14b-32a3-ba75-49fb5f43d3be | -7.5645 | -49.389999 | 2024-11-24 00:21:00 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 211ddf81-4496-38e0-ada1-d801586d99fc | -1.8233 | -46.633999 | 2024-11-24 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 883368df-674c-3940-806b-ee406c7bca77 | -2.0831 | -48.8727 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f72348e7-e928-331d-9c45-856b5cf6e1ab | -1.4236 | -46.053699 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2a780f-c41c-39c1-a163-2321c9dddf3f | -2.2893 | -49.055698 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 430ad766-760c-370e-82c4-c5382d8224fd | -2.2154 | -47.771198 | 2024-11-24 00:21:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63b3e3b6-6510-3b66-8dfb-3bf7f3723a70 | -3.2488 | -50.116001 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3b4ab0-c4cc-36e8-9b77-40550577bbb0 | -2.2034 | -49.863998 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6e980bc-8ab6-3280-b1b0-598b416879a5 | -4.2638 | -44.072102 | 2024-11-24 00:21:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9b2385b-471d-3a84-a9b8-c72a1b1e807b | -4.7711 | -44.794601 | 2024-11-24 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6ac2cb7-20bd-3d2c-bbfe-f183083aee86 | -2.2064 | -48.916801 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db8b182a-0742-3f39-bf57-03c72f1c7e98 | -2.7451 | -49.112 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 727bfc90-d591-3c67-a4ac-e300933bd25e | -2.8646 | -51.804001 | 2024-11-24 00:21:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c4967ca-be13-3cf4-98dd-ea6ccf08e5a7 | -3.6694 | -50.2467 | 2024-11-24 00:21:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 614670e7-db70-3f9d-82fe-68dcfae4404b | -2.5921 | -54.042 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1b32fbd-5eb3-35ec-a0f0-2123035afee9 | -1.459 | -46.028301 | 2024-11-24 00:21:00 | METOP-B | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 94a1285b-8d7e-3a81-be65-85728e733ec1 | -2.7056 | -48.662998 | 2024-11-24 00:21:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a6506a-da10-3132-97af-b88df641968b | -1.8296 | -46.616402 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50aadbc3-0fd5-39b5-96d2-df95f32f7273 | -3.3448 | -50.498901 | 2024-11-24 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 259e8a22-0874-37d3-957f-457f2d9d423d | -2.3613 | -48.553101 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4437e72-a033-3bc2-81a6-c0f00c738177 | -3.0733 | -49.196701 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 384cd84f-aeec-3124-86fb-b59f0603d18d | -3.1731 | -54.304298 | 2024-11-24 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3519fa99-b042-309a-a703-65f4b570417a | -2.4576 | -49.894901 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5626945-a3f3-38ed-97f5-a3dd837a17dd | -2.3957 | -46.432598 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b773bf1-0f37-3316-848e-667eab8d2a06 | -2.2371 | -46.460098 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04a8364e-dcab-36f5-a066-2391d9aa088e | -2.7285 | -46.084999 | 2024-11-24 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1292f12f-9fa0-37be-b432-960761dd14af | -3.2525 | -53.272301 | 2024-11-24 00:21:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a7345cd-d7ef-367b-b141-9d0140f1a51b | -1.1636 | -49.319199 | 2024-11-24 00:21:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8a408229-95db-3094-80ac-c0dae8d8aff0 | -1.8599 | -48.1586 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7b223b0-2791-3a53-9f04-8a9f8437b250 | -2.3218 | -46.3344 | 2024-11-24 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51d246ba-5259-3122-8980-7163ad5254ba | -2.1703 | -47.936001 | 2024-11-24 00:21:00 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b5664ca-c893-343a-ab66-dfcaa2ceae29 | -2.2356 | -46.861 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2582fc6-5b68-3e19-a7d1-1798cc5753da | -2.4518 | -48.8624 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 477187e7-f555-363b-b355-2f7052b77573 | -5.9571 | -48.046799 | 2024-11-24 00:21:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9463eeb3-2e89-3fe4-a1ca-61ad6fbc2c20 | -2.2019 | -49.857101 | 2024-11-24 00:21:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09d661a5-2dfb-33fa-afd0-d7d650f6cce5 | -2.7466 | -49.118801 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7bffff-072f-3add-8f0b-1d125bba3591 | -2.5887 | -54.2113 | 2024-11-24 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 222c378b-c8de-3dd1-99d3-dc2d1803202f | -2.1459 | -46.738602 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76730087-ae68-3498-a850-fa1710150a6f | -2.7578 | -48.665699 | 2024-11-24 00:21:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3981d996-a466-3bc8-a133-21eb112e8d62 | -2.4518 | -49.091099 | 2024-11-24 00:21:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54051812-3aff-32a4-b950-bf9094770d1d | -2.4781 | -48.8423 | 2024-11-24 00:21:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7775e5a8-41f3-37d0-9b41-55a8915af707 | -2.2454 | -46.858898 | 2024-11-24 00:21:00 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a10cee5-978a-37f6-b093-0ef216f1feb4 | -2.2212 | -46.3899 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83474ba3-9445-3dde-9c15-0ff0c6452595 | -2.0008 | -46.281799 | 2024-11-24 00:21:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
