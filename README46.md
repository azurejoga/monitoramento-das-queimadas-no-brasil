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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1186eb99-3079-366c-83eb-9201b763b587 | -2.03906 | -50.64418 | 2024-11-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a869d2db-0523-30de-bc43-8d8f4653fe1a | 0.98395 | -50.26331 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ee8ccc7-c984-3e31-8855-1f543202fbe7 | -1.28437 | -51.73725 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bf4f1f2-87e6-3191-a4d2-ffcc9b70347d | -6.82808 | -44.39938 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7482401-f852-3956-a29c-6a259acead06 | -2.47955 | -45.87438 | 2024-11-28 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de44a8e6-87e0-3964-836d-d4c196dcc9fc | -2.47733 | -45.86695 | 2024-11-28 04:23:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d136c271-486c-3e6d-b1c8-e99b517eb4ea | -5.49197 | -47.6623 | 2024-11-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcc63c96-ff89-32c5-bf05-e4ff03070300 | -2.70126 | -46.29729 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d0fc27-f9f5-38e4-b645-e4749dbd3260 | -1.34705 | -51.98508 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a14bf21c-b338-3936-bd22-5f878520165d | -1.85657 | -47.97437 | 2024-11-28 04:23:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba5e6fe3-75a2-356e-b9b5-6759693ef110 | 0.98899 | -50.12769 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 05731079-98f6-3940-aa44-7387315c53c1 | -2.55691 | -46.33179 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdd73603-0706-3d96-b888-f89e48858aa0 | -6.26956 | -46.24884 | 2024-11-28 04:23:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6de89b24-a5dc-3bef-8ae1-9def186c625d | 0.99121 | -50.25416 | 2024-11-28 04:23:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 475255d7-a390-34ea-bda2-8a7f48824462 | -1.35087 | -51.99049 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cfc79242-8db3-3aa2-b21d-d0a2db4585fe | -2.22428 | -46.39556 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6b5a858-1acd-3fda-9351-1fbab0fe56b6 | -1.63703 | -52.73102 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cab77402-952e-3dc8-825c-97c423e9d285 | -1.65874 | -52.71846 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ef6440c-7780-3ca0-98c0-f224bfceadba | -2.22958 | -46.12344 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbff8b01-e629-3ca1-8980-f42006d595a9 | -1.68333 | -52.50135 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fe3866b8-7bae-3ce6-b20f-df63643d966b | -1.43513 | -47.96172 | 2024-11-28 04:23:00 | NOAA-20 | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 170a9a56-1768-3bed-b6fd-5f2fc0b6a830 | -0.58768 | -51.71095 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c152b353-112b-3994-9e52-8be0a8ffba80 | -1.44507 | -47.11575 | 2024-11-28 04:23:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78db9ada-eb6d-387b-a2db-fdbc70f99c46 | -6.08696 | -41.93861 | 2024-11-28 04:23:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 31a35d59-b816-30d8-8e0b-255a929e92bf | -2.60129 | -46.54469 | 2024-11-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1de854c-d497-34d5-9ed3-91f1110fcade | -1.62042 | -52.47043 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 869290e2-bed1-3b55-acc9-41fadd81e324 | -1.53862 | -46.06543 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98aca933-64be-3867-ade3-cb748f0c9bd5 | -6.09453 | -48.03976 | 2024-11-28 04:23:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 491f0c46-8af4-3bc9-b155-94e6b02b8b84 | -6.10343 | -43.967 | 2024-11-28 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ef8ad929-9f8d-366d-830c-f488e5a5489e | -1.64101 | -52.73705 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 44f4f0af-2981-3aa6-ad93-47d0f3e7c777 | -1.5827 | -52.27368 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4704c025-d5d9-3f79-b37a-125970741496 | -7.22646 | -39.05657 | 2024-11-28 04:23:00 | NOAA-20 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1af6ddff-ac60-3ae3-be10-1929921da5a6 | -1.31596 | -51.74229 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8fb8e6fb-2bfa-37f3-869e-e223620ffd46 | -6.48295 | -47.49677 | 2024-11-28 04:23:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 958f42b8-92f5-3e43-a9f0-6894f3a35070 | -1.71092 | -52.48005 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5511c542-26d0-37c2-9a7f-6feb2f09440d | -6.5864 | -47.90506 | 2024-11-28 04:23:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bbd0a55d-481e-3e73-a203-0ff007bba472 | -2.04428 | -46.65101 | 2024-11-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be3028df-f269-333a-b5df-56a00240603e | -6.60228 | -39.19608 | 2024-11-28 04:23:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6d15a40-5491-352b-bf2a-1887c7f968c3 | -0.98995 | -51.7235 | 2024-11-28 04:23:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ecef8b41-566d-34d8-ac7f-8392c4cbfaaa | -6.58841 | -44.18112 | 2024-11-28 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 57af6175-4a2e-3574-94f5-1d1023d31d9f | -5.97832 | -45.35532 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a1716ce7-dfbc-338d-b7d3-3b34b0194a88 | -2.54084 | -46.39042 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17dbd0d2-a88f-3a85-97a5-12d5af528cf2 | -5.76087 | -47.91094 | 2024-11-28 04:23:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddb2cff4-3045-3e71-87f7-6a2a30579cb7 | -6.57248 | -46.56945 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2771be5-f77d-3d3f-9ba3-8cf8187cfc37 | -1.64565 | -52.46423 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b2f92d37-d3bb-310b-85df-69b7bccf9e7c | -1.68885 | -52.49709 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 77297119-72b6-309a-9f6c-a331054e4b67 | -3.0853 | -41.14156 | 2024-11-28 04:23:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4d9c02c8-272d-32ae-ae52-b21bee0498aa | -1.6667 | -52.73052 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aeeaee4d-8e9b-3592-8ca2-26e15acafc60 | -2.29754 | -47.84181 | 2024-11-28 04:23:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3dc9fd17-b9ff-30a1-9cce-4b87f8698afe | -2.10744 | -45.34715 | 2024-11-28 04:23:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74153c69-88e1-3098-ba19-2df1fe67002d | -5.90448 | -43.40793 | 2024-11-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3fd3f1f-5cc2-36a1-bbbf-33d378ab7aba | -1.08802 | -53.37552 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41e289e7-053a-319e-99c1-788be597f640 | -8.13336 | -44.47055 | 2024-11-28 04:23:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 582074d7-01b9-337a-9369-a9f1bdae52b5 | -0.26412 | -51.62002 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a835b28-2cf2-3ac3-86f7-503308fa14fe | -2.67056 | -46.14954 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9d37720-adc7-3804-b515-daa4bf8804cf | -5.51644 | -46.26398 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33cfb077-8180-341e-97be-635d8d4c787b | -1.74509 | -52.05255 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6ad9af12-8f8e-334e-888e-0870a4eae17d | -1.22571 | -51.80417 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4cfe8967-5af1-3655-a5d1-45adb93c734c | -8.49834 | -43.28124 | 2024-11-28 04:23:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 027fb642-4d82-3e60-bf4c-5fcb091cfb78 | -1.57678 | -52.01765 | 2024-11-28 04:23:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7482eb25-01cd-33f9-89bd-72638eea7199 | -1.68755 | -52.71943 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 750aa040-391e-3ae9-993d-ef6a1b54ed4a | -0.58385 | -51.7056 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 153255f9-98d5-3298-a758-30f543f37496 | -2.70219 | -46.18661 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5037fda8-f0f7-3c83-badf-25adeb912622 | -1.55194 | -46.04601 | 2024-11-28 04:23:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4734921-8160-3869-b020-d8aa514a7630 | -1.35739 | -54.66068 | 2024-11-28 04:23:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba2a3bb0-af95-35ee-bff8-8bdac0857754 | -6.11683 | -46.59309 | 2024-11-28 04:23:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba70bf8c-418a-3698-bb07-d4cc6237c1c1 | -5.97887 | -45.35182 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 73d78a44-03f1-3fe3-b632-cd358a7a7fce | 0.9842 | -50.12448 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0764c2f-54a2-3d85-8538-8b3c272dac8e | -2.58338 | -46.20692 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abc47339-9655-38a4-8d0f-c6a45a7bd2ad | -2.7011 | -46.19357 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5eda8a6-d1c7-3f69-89e9-2aaa55ed97d6 | -1.6649 | -52.7372 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| e5bc3da2-28e7-3ee6-b0f1-133dd66c5db7 | -6.17034 | -42.61232 | 2024-11-28 04:23:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 079a9198-46a3-3c0f-9291-478aa61654e8 | -1.35132 | -51.98961 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2b6f0f6f-a640-3bd7-a0eb-c982610f05a0 | -1.69995 | -52.76442 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3f69f67e-0f8f-3c44-b450-1e33a4a56825 | -2.72069 | -46.28241 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1173b59a-ddab-3b7e-9240-3109a3721dda | -2.68405 | -46.28028 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b96d0286-c706-35ca-937b-5fb9bbb3df1a | -2.67721 | -46.15059 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ca24049-2790-3fe1-807e-2950779303ab | -1.35883 | -51.97163 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8052972-cd64-368d-9aa9-279a43491e93 | -9.10122 | -43.19357 | 2024-11-28 04:23:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f8df0794-396e-37ee-845f-7fd5f2290914 | -2.7061 | -46.20507 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 796904eb-6874-3417-b032-8a81d2c7fcc1 | 0.97641 | -50.12958 | 2024-11-28 04:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 43fbefbd-ef9e-36a1-a5fd-020bf179249c | -2.71125 | -46.29885 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3c2bdf9-49fb-3b31-b0f3-b9ee5422ea10 | -0.58239 | -51.71483 | 2024-11-28 04:23:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e467a1f4-cb95-3e65-88e2-fb973f4d6252 | -3.96521 | -54.61158 | 2024-11-28 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 416843ec-54cb-3b0e-9606-0197a3ad4edb | -2.55198 | -46.40657 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d30914e9-2a0d-3a37-b126-cc879e87310b | -6.36737 | -45.6905 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dadf29c2-67d9-3a3e-96cd-906588793153 | -1.65819 | -52.47658 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e52075b0-f9c5-3bee-b3fa-139bae069877 | -2.66649 | -46.60199 | 2024-11-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917750c9-f29b-37b3-92e5-369fb0f6009c | -2.17411 | -46.38774 | 2024-11-28 04:23:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bae42b6a-105b-3e48-a049-3047fd5906e0 | -6.38131 | -45.68943 | 2024-11-28 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9c5fd22-ff50-31c2-9344-e6ed71abf5a5 | -1.64499 | -52.43843 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de936dce-8360-38a4-b81d-e58296ff2370 | -1.69255 | -52.6283 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d59f8731-2faf-3e10-acf9-bc4d8b504fe3 | -1.59358 | -52.26545 | 2024-11-28 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 938dff4d-4788-3f11-9798-a1513312941a | -2.1239 | -48.53713 | 2024-11-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69f7214c-5eb9-3f51-889f-e0dccaed3524 | -5.75839 | -46.26007 | 2024-11-28 04:23:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0bc24d5-bd06-34c9-8b58-774d2183b54f | -2.11229 | -47.89038 | 2024-11-28 04:23:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c5ed8a2-9d90-3ea5-b060-4a488860f201 | -5.92775 | -43.78064 | 2024-11-28 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 004917ba-efca-3a36-83d4-7e0ab1bd1a7b | -1.08731 | -53.64558 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e2ef749-40e3-33d4-9a55-d27ae889f0ef | -1.32824 | -51.95703 | 2024-11-28 04:23:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d7d3f41-fb50-3f1f-bc6a-e054b71107d8 | -1.38569 | -53.63179 | 2024-11-28 04:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README47.md)
