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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 036f5f58-f1af-31a5-8bc0-159af541e2b8 | -15.59512 | -47.82538 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fed3671a-84b7-35e9-95c4-a51de5177490 | -14.56468 | -48.23733 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 814f0cdf-520d-3eca-99ca-f9571cf89fce | -14.51939 | -48.01147 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f015e79b-167f-3844-a76f-2612a675b4e2 | -15.19916 | -50.18386 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8501e993-ff8e-33d9-b829-56355829325b | -18.03187 | -44.00699 | 2025-09-30 04:42:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c17cb36-0e02-3835-a0cf-705aa73f853b | -14.59337 | -48.2829 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d293b10b-f51b-30c4-9c1d-139b95531a13 | -15.39176 | -47.06816 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 799c34d5-71f6-3ab5-af52-175763ca81ec | -15.32872 | -46.25916 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db51b871-4471-3950-9a60-481f4f112520 | -15.15907 | -52.83652 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b3dc8a3-3090-3413-886b-980e37dc9b10 | -15.16681 | -46.41989 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eef89d98-c102-3b7c-a20b-b18f26d63bed | -14.54303 | -48.48514 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d10018ed-dff2-3158-98e6-c17c88abefe2 | -15.82706 | -48.1661 | 2025-09-30 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90579655-98e7-3f53-b400-1851c45858c2 | -19.69476 | -43.68517 | 2025-09-30 04:42:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d6e4339-40d4-33da-8d03-f9b613e31b0a | -14.70904 | -48.15191 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3fe7dc3d-0a4d-3763-ba7a-da9326af16fb | -20.39658 | -43.68481 | 2025-09-30 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 40889255-5853-34ad-a4f2-b1bec844668e | -14.56528 | -48.23315 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 685519c1-e3c3-3a72-a589-d0dfefc98e8a | -15.03453 | -46.99271 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07d0bab1-e527-3874-8833-3ba2516de676 | -15.25226 | -56.83633 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 592ae6ee-76de-3e48-8b9d-696615b4cc43 | -15.87821 | -46.21111 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eefc27b2-714a-3c59-9c79-7c591c6a0cb9 | -14.71613 | -45.67093 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 654c2694-dbcd-3ce1-9bf0-79e38fcd91ef | -18.70773 | -43.18839 | 2025-09-30 04:42:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9121d7f6-2b1a-3004-897c-0658e7fd251a | -19.30536 | -43.81859 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af898611-2c6e-367e-a866-1cfb9a95ac4e | -14.78792 | -48.31077 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f055ec4-28bc-3457-b0d4-492b2cfbafdc | -15.27753 | -49.25179 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba2b2c5d-6e98-398d-8ca4-df977e010c4d | -18.46988 | -44.02254 | 2025-09-30 04:42:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2a46f07d-b899-361c-998a-5af062bab888 | -15.11103 | -46.48855 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d82db7eb-f18f-3fc5-b4a5-2e6cd2c3da41 | -15.81371 | -46.04128 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61bbfafa-0ca1-3fbf-b6fc-b781a1c14e25 | -14.52195 | -48.3814 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dca15e5a-a818-31e3-a50a-bf9e15cca279 | -14.5359 | -48.48552 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21283294-78f2-39ae-ace7-979d8bd48b9c | -14.53943 | -48.48616 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2cae8b5c-68da-3dc0-842c-e1020cded03e | -15.3249 | -47.38049 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f84e808a-9863-31d4-b20e-4c8e85912904 | -15.79947 | -59.5231 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ae8ddc2-a2e8-39cc-b9c9-f7b857d40ea4 | -16.61625 | -49.2057 | 2025-09-30 04:42:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f5e9190-55ee-3ec7-89b7-69487c6daee5 | -14.70846 | -48.15606 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 05822888-7295-330b-b7dc-4dbec0f65933 | -14.70787 | -48.16028 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6e61e2c7-e219-3e79-846b-c859ebcd259b | -15.1193 | -46.4575 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deb10d61-6004-3280-b6ac-2833c8a4575a | -19.71576 | -45.8813 | 2025-09-30 04:42:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 23d98f56-2256-3ce5-b182-84a78173e67e | -15.27449 | -47.89639 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ab26856e-5c58-3d5c-9229-fef797a49a32 | -17.08923 | -48.56651 | 2025-09-30 04:42:00 | NOAA-21 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df79c209-5c3a-3042-b8dd-b505544cca92 | -15.23027 | -50.09112 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 001af615-b88a-3f5a-894d-c9a4422c1295 | -16.41308 | -43.11931 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d75520d-3b54-32e0-88bc-98d10fdc0d6c | -19.85451 | -43.81576 | 2025-09-30 04:42:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 724eec75-fdd5-3c5b-93a8-1b6071c5f6bc | -16.22611 | -41.72885 | 2025-09-30 04:42:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a7c40623-f996-35df-bf2a-ad2b9c265354 | -14.64699 | -46.96511 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a77bb38e-f378-3f3f-8223-53a58c9a1527 | -15.04292 | -46.98904 | 2025-09-30 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e2b4c950-a8b0-3033-a61a-0d6125258337 | -19.30608 | -43.81197 | 2025-09-30 04:42:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9c8e074-8f46-368e-9225-0e6bb5a8ceec | -19.86138 | -42.58433 | 2025-09-30 04:42:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| a00c0c0e-8a32-352d-8fd0-fac6ffa8f6ef | -14.57856 | -48.21754 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6b66dc75-b269-301a-9e4f-2e8d4abb3378 | -15.91979 | -46.24458 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51a1b6dd-2002-3ad9-a5b8-dbc0f641412d | -14.52363 | -48.44523 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 787218fc-1c5d-36f6-aaf0-4ba97a6ed1f7 | -17.88334 | -57.62444 | 2025-09-30 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| c703a261-415b-3548-ba8f-54f848189070 | -16.00432 | -59.51406 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b566e9f0-831f-39f7-9537-c301adb2b71a | -14.58202 | -48.28557 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4469fdb9-0d8c-3dba-a068-11c395a0a9f2 | -15.12478 | -47.98185 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64a8b4c1-3082-3f1b-916c-baa879920ff8 | -15.25684 | -56.83397 | 2025-09-30 04:42:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9d66bde-c0c7-3ddd-9357-672b4a21d020 | -14.72972 | -45.66464 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 689af3e7-50ed-3f59-95e5-aee6e83687ec | -16.28346 | -52.53542 | 2025-09-30 04:42:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ac481e3-8b7d-3826-a16f-567634c14509 | -14.70301 | -48.14236 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 36541a03-46c0-3872-8050-b3cb9d78e865 | -15.80423 | -59.52396 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2c49fc4b-db2e-3429-87a0-479ad3bed5a4 | -14.53891 | -48.48864 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 705e8f5d-325c-393e-986a-de6961915e23 | -15.22862 | -50.10213 | 2025-09-30 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c668f563-2111-38d3-8623-4a4738d68679 | -14.53325 | -48.37877 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8562bbcd-970d-315f-8d59-c4f339c29e27 | -16.51632 | -46.95114 | 2025-09-30 04:42:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbf284ba-c02e-3a70-a62d-377ca93ecffa | -15.27235 | -49.26303 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6fab88ed-05e2-3208-b1df-04eeefa52dff | -15.15847 | -52.84021 | 2025-09-30 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 536364b1-a5a7-300e-b068-2644b828248c | -14.70963 | -48.25265 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d99ade79-3764-3fe4-99ed-fb0881443041 | -15.78719 | -50.32119 | 2025-09-30 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5aa72368-d1e3-3a68-8258-2020eb2d9b49 | -15.49484 | -48.55486 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 498be043-f767-3e23-b7c3-bfe26e15ae21 | -20.29111 | -46.23481 | 2025-09-30 04:42:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e1d06f-20ca-302e-b128-e7d72b50fe53 | -16.28206 | -47.83995 | 2025-09-30 04:42:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4308ee91-fd9f-37c8-b65b-e246f6fccd80 | -15.73151 | -48.89367 | 2025-09-30 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fa80dea-d137-3aea-92f8-e72f2e791f29 | -17.04139 | -43.41658 | 2025-09-30 04:42:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a68ab3f-c9fe-3a69-bdc8-3887362f4038 | -14.5189 | -48.4277 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71990abd-757d-3072-a344-c0902a444d3b | -15.16191 | -46.42607 | 2025-09-30 04:42:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2116e40-f530-3e8b-bdf8-d5001f1fa9b4 | -20.61807 | -46.19201 | 2025-09-30 04:42:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5805da2c-c145-386c-8d54-ae3c33b49717 | -17.72007 | -46.65004 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f3549603-a21f-343b-834b-a62d52d4bfc9 | -16.41273 | -43.12249 | 2025-09-30 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af91d1f-9ae8-3143-9120-1363212de72e | -14.73861 | -45.66182 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9ef57aa3-c4f2-318b-a774-50c3d6ba3889 | -14.52551 | -48.38196 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37d081e4-bb0b-3bb4-bad1-d9a637922a17 | -17.0274 | -44.99181 | 2025-09-30 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db3e84f0-5534-3b60-87ea-b588f5773013 | -15.27232 | -47.88966 | 2025-09-30 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 152892d3-d5ee-3911-a171-ff999784d4ec | -18.31894 | -41.75406 | 2025-09-30 04:42:00 | NOAA-21 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a671c1b1-e334-3c5e-9e7a-80b4311b84dd | -20.42835 | -46.16934 | 2025-09-30 04:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d98c440-bc05-3637-9750-daf9d8c2f120 | -14.7292 | -45.66867 | 2025-09-30 04:42:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ceec7f3-d72c-3f3c-b55c-900aeb0bd162 | -20.04723 | -41.32668 | 2025-09-30 04:42:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 0221287b-2d45-3b6a-9b7d-be8b58449868 | -19.45833 | -48.92577 | 2025-09-30 04:42:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 942c621c-a009-3a00-b155-26ac436991fd | -14.56019 | -48.46621 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f810957-87a9-3c4f-bd79-56da91602b55 | -15.71184 | -59.51441 | 2025-09-30 04:42:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8682a3-2f1f-336e-a5c0-0f63e4a552f0 | -17.71355 | -46.66892 | 2025-09-30 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2263997-0f7b-35b9-8812-db609b6ef11f | -14.65856 | -46.96681 | 2025-09-30 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c136ccda-04e9-352d-9ddc-b00c603f6cba | -15.38939 | -47.06926 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe34ccc0-d95c-30a3-8010-9799445e14e9 | -15.9255 | -46.20166 | 2025-09-30 04:42:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8252d66a-7b3b-3e10-b2a9-56d120712168 | -14.51651 | -48.44422 | 2025-09-30 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 4f28a158-26ce-33c3-b81f-eeb059beefc9 | -13.73824 | -54.72278 | 2025-09-30 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc4711d6-afa5-301a-b8b5-19e21f13be75 | -15.49007 | -48.56269 | 2025-09-30 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| de9ad804-083a-3613-9e58-df94da9e988b | -15.39465 | -44.97651 | 2025-09-30 04:42:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf15650-add0-3476-8dee-5b5d13766814 | -15.37885 | -47.07596 | 2025-09-30 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5da8f9a8-9d93-374f-aae8-64fe49a5f573 | -19.98156 | -41.9111 | 2025-09-30 04:42:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 36026b52-245a-3bbc-b6f2-3963b07984b5 | -15.28566 | -49.26859 | 2025-09-30 04:42:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e0f64199-b1a0-3811-8038-2ed9956b274f | -19.69443 | -43.68833 | 2025-09-30 04:42:00 | NOAA-21 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README77.md)
