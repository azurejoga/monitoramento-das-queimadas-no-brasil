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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e751990-0aee-34eb-86a3-32cb3106470a | -21.2561 | -48.6372 | 2025-05-19 00:10:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| d2c11e73-a912-3e3e-926c-6a833530d106 | -21.2561 | -48.6372 | 2025-05-19 00:30:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.0 |
| d4d9aa0d-145d-393d-9512-b005e97e112f | -21.2561 | -48.6372 | 2025-05-19 00:40:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 64.2 |
| 454d7008-39aa-34a3-95f5-beda08d80ac6 | -21.26587 | -46.58685 | 2025-05-19 00:52:00 | TERRA_M-M | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 912f7fe5-e7aa-31fc-bd2c-e2b4eaddd707 | -21.25451 | -48.63959 | 2025-05-19 00:52:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| f645102e-9e34-3678-a08a-84b6bcdab5a2 | -21.25584 | -48.64904 | 2025-05-19 00:52:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 0210a6b9-f4a3-30c7-b2b4-7cf57bee9d60 | -10.45452 | -54.37778 | 2025-05-19 00:54:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 6b1bfdbf-a265-3d12-b63f-ec481872f79f | -12.10392 | -44.77004 | 2025-05-19 00:54:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d1efa3e1-83bd-3d3b-ad1b-971b32e5e8be | -12.13425 | -54.66692 | 2025-05-19 00:54:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 74ab56d7-446c-3990-92b4-c9c99ea16ac8 | -12.03876 | -54.97155 | 2025-05-19 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 64e2122d-9144-35a3-a46f-689a69f786fc | -12.10079 | -44.75126 | 2025-05-19 00:54:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 20702976-8249-3cb7-b88d-784745b4edb2 | -10.45391 | -54.38349 | 2025-05-19 00:54:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 9a0dc1fc-80a7-315c-8496-13d048f2efbc | -17.0621 | -45.02147 | 2025-05-19 00:54:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 25.5 |
| b4ff5b20-be28-3793-b4ad-16ab7ff86682 | -13.04454 | -53.72672 | 2025-05-19 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 64fde9f5-2d03-3c6c-80b3-48e644dc765e | -12.29588 | -52.47681 | 2025-05-19 00:54:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c8469db0-296c-381a-bfa5-09a8e1158288 | -12.099 | -44.75792 | 2025-05-19 00:54:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b6dfaeef-109c-34fb-923c-510379a9375f | -13.16408 | -56.8169 | 2025-05-19 00:54:00 | TERRA_M-M | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 31a7b9ab-683c-3f5c-ac50-3bc4453ca520 | -13.04313 | -53.71549 | 2025-05-19 00:54:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 75d2c36f-5fd4-3203-9221-fa685d1fd82d | -10.45242 | -54.37231 | 2025-05-19 00:54:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 3202d042-c339-3ca3-be14-4b213624b510 | -22.3627 | -47.5227 | 2025-05-19 01:10:00 | GOES-19 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 214.6 |
| 9ce5bc3b-18b9-31de-8492-1e51fadb1b0e | -22.3418 | -47.5281 | 2025-05-19 01:10:00 | GOES-19 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 318.2 |
| 9a81c869-c633-3204-993e-d489d6d7834e | -22.3208 | -47.5335 | 2025-05-19 01:10:00 | GOES-19 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.7 |
| 8a368d81-c56b-3323-b7f9-f62b4c0fb66b | -22.362 | -47.5466 | 2025-05-19 01:10:00 | GOES-19 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.6 |
| 51eeff67-f2c5-3284-b609-5b46ddca13b9 | -22.341 | -47.552 | 2025-05-19 01:10:00 | GOES-19 | RIO CLARO | SÃO PAULO | Brasil | 3543907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| 211d1990-e57e-3753-ad9d-aad37249fd21 | -21.2561 | -48.6372 | 2025-05-19 02:00:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 47.4 |
| 9c3a5f73-2d7d-3b22-a079-e837ae6cc9ce | -21.2561 | -48.6372 | 2025-05-19 02:10:00 | GOES-19 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.9 |
| 3b33a2ab-23b5-3d13-b2cc-e78e3bb704e0 | -9.6222 | -40.34887 | 2025-05-19 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b6c6d1c8-095b-3e54-893c-bfd318b1b2db | -9.42785 | -40.37817 | 2025-05-19 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8a2d8680-8060-3085-a414-a32ed8517562 | -9.42679 | -40.38373 | 2025-05-19 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1bb2a538-3ac3-3da9-9754-86c825d52dea | -9.42737 | -40.38173 | 2025-05-19 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9e427a5c-2709-377e-9f5d-41a75ff501f7 | -22.6784 | -42.85973 | 2025-05-19 03:17:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 80e1bcaa-d79c-3581-ace0-b8cc9fd203cf | -22.902 | -43.75505 | 2025-05-19 03:17:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1586e416-f084-3366-8492-173d02d6b4cf | -4.8174 | -43.21934 | 2025-05-19 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfcceb4d-2fd3-39d5-b4ab-f8ebff19261d | -4.81176 | -43.21832 | 2025-05-19 03:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f84e1b5c-70d8-38d6-879b-3a6a976cc4aa | -9.59095 | -40.33736 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0004372-f96a-3591-9397-ba19993858bf | -9.62381 | -40.35163 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7e8e977-8689-3e87-8106-03e4fece97f4 | -12.10788 | -44.76118 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2613c1c7-a08b-39f3-9339-6dfa22edfeb5 | -9.62024 | -40.34678 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2790c8e4-94cb-3d07-aef1-b109c2ec8f9b | -12.10383 | -44.75282 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 19fd2989-fdcd-3323-8b09-8d0e8cf49396 | -9.42854 | -40.3833 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| fdc3165a-3156-3a36-9c07-8bc96e2b799c | -9.42926 | -40.37918 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| c29fa204-656a-3ef9-92c8-988d75a649ac | -12.10428 | -44.75312 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02c2ee8a-a261-39ad-8968-e101a7efb969 | -12.10288 | -44.76049 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38566395-4a74-3eb6-b46d-a8b193b97724 | -12.10768 | -44.76524 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbc58c01-66b2-3a38-963d-e1e778aafb80 | -12.10358 | -44.75681 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96c3a29a-7a0f-368b-ace1-4aca9d4b7b15 | -12.10839 | -44.76153 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45ca1e38-5597-3ccb-b1a8-df1ce3234b7c | -12.10908 | -44.75785 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca2f4f54-831a-34b8-b08d-d39ce0253d6e | -12.10715 | -44.76487 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 15f6e061-bb11-3f3f-9c60-08aa14a3db61 | -12.10861 | -44.75752 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 991a4c86-500a-3ea4-b7af-e56460d5f86a | -9.62452 | -40.34756 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 620ee3ab-dda0-3e53-a828-c99ce74562de | -12.1031 | -44.7565 | 2025-05-19 03:38:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 225a7ac3-16f7-3c27-b989-17c54d4841a1 | -9.43357 | -40.37994 | 2025-05-19 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c77f489c-61da-3220-b333-82d36939fa7c | -18.80951 | -40.5079 | 2025-05-19 03:40:00 | NPP-375D | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0f644654-5b02-3775-8d47-872d5258e5a9 | -17.06406 | -45.02642 | 2025-05-19 03:40:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0d8a4452-a9f0-3354-a229-2ebe34c703fb | -17.05765 | -45.03173 | 2025-05-19 03:40:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8e027a39-5b41-3c63-aa52-69d5488ccf74 | -17.91957 | -45.52831 | 2025-05-19 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91752407-9e7a-3db2-80bb-910c9f08a842 | -17.9189 | -45.53152 | 2025-05-19 03:40:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46133acc-080a-34e0-9f4f-3a98076c7920 | -19.83903 | -40.08141 | 2025-05-19 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0ac10049-aebd-3fbf-9b55-5e6d5c46f156 | -19.72012 | -40.35562 | 2025-05-19 03:40:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cad6f427-bbf5-356c-9148-f9adf9e5a1de | -17.05895 | -45.02536 | 2025-05-19 03:40:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 155a1658-0a71-34e2-8a90-3bc79c6399dd | -17.0583 | -45.02854 | 2025-05-19 03:40:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba2c869e-71dc-3a27-ac3a-753f7bb2780a | -17.0596 | -45.02218 | 2025-05-19 03:40:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 88d272b4-7711-396c-a184-6b88b9088b2a | -14.13515 | -41.69152 | 2025-05-19 03:40:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56af76af-a995-3787-a8ed-8c885b77dfb4 | -22.6997 | -43.34874 | 2025-05-19 03:42:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2dc27697-507e-317b-a88b-837f8946b90b | -21.04362 | -50.67099 | 2025-05-19 03:42:00 | NPP-375D | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| eb4b1173-fe3b-30a5-be30-319f8ebc6e9c | -21.25614 | -48.6459 | 2025-05-19 03:42:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| eb16ffd4-71b6-317e-b3a0-51cc8096652e | -22.45724 | -51.72397 | 2025-05-19 03:42:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c63947e0-8abd-36b0-a5ec-1ae1d61d1642 | -22.53934 | -48.81525 | 2025-05-19 03:42:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7501be73-1363-3f3e-9ec6-a97752ec9c88 | -21.2582 | -48.63699 | 2025-05-19 03:42:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d39b26f8-a97c-3792-ba4c-7bfd82e3d3bd | -21.26567 | -46.59198 | 2025-05-19 03:42:00 | NPP-375D | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ed1605aa-e5ce-3bee-a5b4-8f46a0e76f3b | -22.45553 | -51.73066 | 2025-05-19 03:42:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| c0d68b02-403f-3be2-b47e-30c03f6ef2dd | -20.76377 | -46.76936 | 2025-05-19 03:42:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3aa1d362-78e1-3373-827b-4e1f436e93fe | -22.78979 | -43.75875 | 2025-05-19 03:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8fa0d99-8b65-385c-9765-5e1b4cb09461 | -22.45485 | -51.73126 | 2025-05-19 03:42:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| d97f108c-1325-3dae-879a-278673a43d32 | -22.46388 | -51.72624 | 2025-05-19 03:42:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 2389eaa1-739b-3b0f-b2fe-7262c87c5fde | -23.34097 | -46.77509 | 2025-05-19 03:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eb85a303-876f-340e-906d-c0ce33148eac | -23.34163 | -46.77206 | 2025-05-19 03:42:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 413dab70-fcd3-378d-8865-9324ec5aec43 | -21.26642 | -46.58858 | 2025-05-19 03:42:00 | NPP-375D | JURUAIA | MINAS GERAIS | Brasil | 3136900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ed921f95-64a3-3bbb-98a4-d1a077231a14 | -21.04083 | -50.6703 | 2025-05-19 03:42:00 | NPP-375D | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1a289011-fbaa-3cbc-bd5a-00dd0543686d | -21.25717 | -48.64144 | 2025-05-19 03:42:00 | NPP-375D | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6b74458a-0f60-3640-8825-228db1481385 | -22.67909 | -42.85526 | 2025-05-19 03:42:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e90f8646-2732-3da6-947f-3c44dddd29a4 | -20.76603 | -46.76949 | 2025-05-19 03:42:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f879b486-dee4-3825-9ce9-43cf7f66ff13 | -22.78558 | -43.75772 | 2025-05-19 03:42:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85090e91-8c63-3d5b-a1a0-d43548edf2ca | -22.45652 | -51.72456 | 2025-05-19 03:42:00 | NPP-375D | ESTRELA DO NORTE | SÃO PAULO | Brasil | 3515301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 06e53beb-6d88-3f31-8fc3-2c0771b90d02 | -21.04744 | -50.67185 | 2025-05-19 03:42:00 | NPP-375D | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f15efd66-5c1c-3597-bd1d-89099bd2cc87 | -4.80998 | -43.21959 | 2025-05-19 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 621344a5-2bee-3863-ade8-39ce07df17fb | -5.07018 | -37.71755 | 2025-05-19 03:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d1ec52f-10a4-30e8-b1a5-cbee858b10ff | -5.02698 | -47.96845 | 2025-05-19 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7176f444-4e19-33e2-be5d-452e1f126f84 | -4.81441 | -43.21575 | 2025-05-19 03:57:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a6a632d-a0a3-37d2-a1d8-ae8122d88c4a | -5.02647 | -47.97149 | 2025-05-19 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 070ef9fd-1d02-312c-a034-ed7ca2ddc190 | -9.62272 | -40.3432 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1aeb47f-dafa-3d10-98e2-ab8ee02c9d87 | -9.63252 | -48.20707 | 2025-05-19 04:00:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f592520d-4ea5-30ef-8b4f-16d823444e4d | -7.23224 | -43.5465 | 2025-05-19 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| efd352fc-cde3-30b7-85df-0eb9f2419799 | -9.42629 | -40.38316 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f882cf82-0dc4-3d9c-88d2-2634f35f6c8e | -9.43015 | -40.3802 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| c04d4d94-b242-3d8a-ab51-04c808edeb4b | -7.31069 | -43.29723 | 2025-05-19 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db83cfb5-c513-3feb-8517-e3b290d5cf45 | -6.23266 | -43.36171 | 2025-05-19 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd59615f-1c77-38de-b59c-ca281130ed5b | -9.61886 | -40.34617 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 06f439ee-2933-348b-b42c-6e9812405998 | -9.62217 | -40.34669 | 2025-05-19 04:00:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 069af374-65eb-3929-bba5-af42cda77f91 | -8.3191 | -40.59901 | 2025-05-19 04:00:00 | NOAA-20 | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README2.md)
