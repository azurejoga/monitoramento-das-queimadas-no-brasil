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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e61e1bbf-9f35-36aa-b9e5-889c5dfc61c2 | -19.49625 | -42.3393 | 2024-10-01 03:51:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 553d02f6-d757-3b3b-84cd-b4ee3b748e49 | -19.49549 | -42.34367 | 2024-10-01 03:51:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 373bfff9-8060-324c-8b54-e9851a67d6c5 | -19.47726 | -40.602 | 2024-10-01 03:51:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7f3434e2-2d04-32ad-b514-42ceb2b4dc4a | -19.05582 | -42.95005 | 2024-10-01 03:51:00 | NPP-375D | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 53d0423b-da71-3a82-ae00-d0932a1fd88a | -19.04879 | -42.94541 | 2024-10-01 03:51:00 | NPP-375D | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cff7f567-e5a0-3daa-86d7-715235755668 | -19.04804 | -42.94975 | 2024-10-01 03:51:00 | NPP-375D | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 18815fe3-e5aa-38b3-b570-ed9b8e7edc82 | -18.99175 | -41.13034 | 2024-10-01 03:51:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ac1f7142-428d-3d9f-a6f0-cac33736fc30 | -18.98836 | -41.12971 | 2024-10-01 03:51:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aaa453d2-5e4b-33ec-8ee0-947d80eea560 | -18.98773 | -41.13351 | 2024-10-01 03:51:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d24de793-d7cf-306b-b418-93d657e8984b | -18.6751 | -43.6846 | 2024-10-01 03:51:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc3117bb-1061-3218-be1d-32b7ede4e450 | -18.5406 | -43.37123 | 2024-10-01 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eb38de1d-a1b6-3e73-8ad3-1348e87c2ad0 | -18.53769 | -43.36592 | 2024-10-01 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 01b02fa4-4dd4-34d6-a2a7-e24c90a65050 | -18.53691 | -43.3704 | 2024-10-01 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 191e1252-58ab-3eda-af19-60d3dd15890d | -18.53565 | -43.46862 | 2024-10-01 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 7fd8dfe0-3d2d-3128-977d-e4c0dbf0070f | -18.53477 | -43.47348 | 2024-10-01 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e8e1dbee-9042-313c-80ff-2cd74c678478 | -18.53465 | -43.47107 | 2024-10-01 03:51:00 | NPP-375D | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c2c61352-d8b8-323b-890f-a5e367dea4b2 | -20.99904 | -42.6022 | 2024-10-01 03:51:00 | NPP-375D | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c43c8d63-a8a1-3178-8c8e-8e1234e13c1d | -20.81593 | -42.32252 | 2024-10-01 03:51:00 | NPP-375D | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6cfb7abe-8b53-36d8-90ed-0132d3f22dd7 | -20.74476 | -42.20995 | 2024-10-01 03:51:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4cd2d0b8-47d7-3337-bda7-378c0244be9e | -20.7413 | -42.20936 | 2024-10-01 03:51:00 | NPP-375D | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8ef19261-d2dd-3cf7-a451-c4d359d23947 | -20.53884 | -43.37083 | 2024-10-01 03:51:00 | NPP-375D | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8dc17d0c-4638-305c-bacf-2379ae08fa1e | -20.50279 | -41.06295 | 2024-10-01 03:51:00 | NPP-375D | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c2c0841-8ab2-3241-b4c3-cb09dbca56a6 | -20.46576 | -42.95088 | 2024-10-01 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 995ce5ff-7b3d-3a24-8118-98b2cff60e68 | -20.46293 | -42.94597 | 2024-10-01 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2417c8ea-0c90-3cae-85df-a7a4a84a6a7e | -20.4622 | -42.95022 | 2024-10-01 03:51:00 | NPP-375D | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cdcbea21-54ad-3735-8d35-31c5f8b3f833 | -20.45292 | -44.37851 | 2024-10-01 03:51:00 | NPP-375D | CRUCILÂNDIA | MINAS GERAIS | Brasil | 3120607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| adb7e195-f3bb-332c-8774-88ff9096f04f | -20.45086 | -44.54042 | 2024-10-01 03:51:00 | NPP-375D | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 13cc8edb-0d35-3341-8f52-385c4646ae45 | -20.41613 | -43.55457 | 2024-10-01 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 94a8fb4d-a806-3df5-a1df-0e2367d173df | -20.30027 | -43.12932 | 2024-10-01 03:51:00 | NPP-375D | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4c46cea4-8e9b-3562-9edf-b844066df5fc | -20.29082 | -43.52208 | 2024-10-01 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4f9106ca-13c1-3aaa-b30d-1a93853754fd | -20.1901 | -43.51929 | 2024-10-01 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| db3037dd-4d8a-3aa1-89c6-7e08f4af4c99 | -20.18643 | -43.51859 | 2024-10-01 03:51:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1879c5a2-2d85-3791-ad3a-f4b7ed667f0c | -20.09451 | -45.26385 | 2024-10-01 03:51:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6c3d5056-f61f-36c8-808c-736c77efbee7 | -20.0938 | -45.26765 | 2024-10-01 03:51:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8c4ff350-ec86-356d-b357-29a023a6c54c | -20.01404 | -44.53089 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 18201bc8-c05d-369b-a37a-457693db6125 | -20.01214 | -44.54115 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 04294eb5-fe80-3910-b166-3b92c0ef4fb7 | -20.01112 | -44.52493 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6c1e11f0-770a-39e0-b9ec-6ab5fb8da79f | -20.01019 | -44.53001 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 10dad36f-8d22-359a-a8c6-aa0706d3f93e | -20.00924 | -44.53512 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| f491f27b-ec92-3a5f-84b6-a1dc4e664ae0 | -20.00634 | -44.52908 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 965a1936-755b-3a35-9580-a879cf44cf6c | -20.00538 | -44.53424 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| bc1d2e08-c827-380d-abcd-72977ac36e16 | -20.00495 | -43.96642 | 2024-10-01 03:51:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58dc7190-0ec6-308a-933e-f98356b4bba2 | -20.00246 | -44.52831 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| e97a01a6-c9de-3c4e-85be-c037b4459f58 | -20.0015 | -44.53349 | 2024-10-01 03:51:00 | NPP-375D | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 30.3 |
| 7b74587e-69f6-352f-97a7-99799f7eda27 | -20.00118 | -43.96574 | 2024-10-01 03:51:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0d6e2f57-33af-38c4-8019-f9b84f312777 | -19.99186 | -43.54101 | 2024-10-01 03:51:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 958aeb70-a6b6-3db0-b2e8-e7e09743e00d | -19.9882 | -43.54018 | 2024-10-01 03:51:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2acef171-dcb4-369e-904c-9de40cc9fcd0 | -19.89802 | -43.16302 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ad979961-cb6a-34ec-bea6-78a3a5ec985f | -19.89725 | -43.16735 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dfb2013e-8450-339c-b746-b99a1e5359fa | -19.89442 | -43.16224 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 751895ae-e123-3bef-84fd-0e57ae108a57 | -19.89378 | -43.16402 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 605ee3b3-13e3-3753-b821-d1f36deb9c61 | -19.89366 | -43.16653 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 89a732a6-d70b-3672-9a1a-5421c750677f | -19.89017 | -43.16327 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 484e21a5-fbc1-3ec2-ad4e-41a51782e52e | -19.8873 | -43.15829 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f76b410f-337c-3adc-9f31-f4a00c8a0988 | -19.88721 | -43.16079 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c43c474d-53e6-3c60-b364-2ed672bc888e | -19.88656 | -43.16254 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 471efd7a-c793-33d8-aff6-5af66691f82d | -19.88295 | -43.16179 | 2024-10-01 03:51:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee311e2c-c2ef-3c47-ae8b-e2562c45dd1d | -19.87709 | -43.17397 | 2024-10-01 03:51:00 | NPP-375D | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9cab68b3-48be-3508-8c89-48148d7b4613 | -19.87424 | -43.16886 | 2024-10-01 03:51:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c23dc1ce-6067-3bca-9924-681aa6b6b7f8 | -19.87064 | -43.16805 | 2024-10-01 03:51:00 | NPP-375D | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 364f0942-9e6f-3a80-beef-a3dc2b071530 | -19.84189 | -44.61284 | 2024-10-01 03:51:00 | NPP-375D | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f87c3c06-0bdc-3838-a793-bc126b572b56 | -19.8393 | -40.08083 | 2024-10-01 03:51:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ce882fa2-e0a6-35e2-a07a-f7d20fbaf3fd | -19.7923 | -43.16674 | 2024-10-01 03:51:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.4 |
| 98828e7d-14ec-3ab1-9abb-d5341c5cf0a1 | -19.79152 | -43.1711 | 2024-10-01 03:51:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 328e412d-935d-3711-98aa-124bb408b417 | -19.78943 | -43.16183 | 2024-10-01 03:51:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 49e82a19-1bc5-3dc4-930a-a083c4e183c4 | -19.78866 | -43.16618 | 2024-10-01 03:51:00 | NPP-375D | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ce0f2fd-1c12-31c5-9349-42337fb5e3f7 | -19.71676 | -40.35445 | 2024-10-01 03:51:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 012574f3-7f9d-3f8f-b73a-30b0b98f9c32 | -21.6588 | -44.10617 | 2024-10-01 03:51:00 | NPP-375D | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7bac518-5424-3430-be8d-dab8c2451143 | -21.51692 | -42.07045 | 2024-10-01 03:51:00 | NPP-375D | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d6ba772e-d71c-31a0-a618-516f909b63fe | -21.33653 | -46.43069 | 2024-10-01 03:51:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9d1d48ad-710f-3f88-a316-0e30a3c89828 | -21.33571 | -46.43501 | 2024-10-01 03:51:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| af0c85cf-50fa-31dc-8847-d3793d103206 | -21.33222 | -46.43021 | 2024-10-01 03:51:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 9d156fb2-ad16-3db4-a276-dede674e0b98 | -21.33139 | -46.4345 | 2024-10-01 03:51:00 | NPP-375D | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| cbd3099d-1fbf-3c2c-9823-caa41c591004 | -21.31391 | -46.64626 | 2024-10-01 03:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| afaecb6a-2e2c-3aa0-a2e8-aa1059be37a0 | -21.31247 | -46.64819 | 2024-10-01 03:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| be2b1052-a721-3355-b209-b379f11ce48c | -21.31051 | -46.64087 | 2024-10-01 03:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 567017b4-cd82-30a8-afbf-5d80e1c6ccad | -21.30962 | -46.64531 | 2024-10-01 03:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 644e6de8-6128-34e1-b579-de43eaf921b2 | -21.30903 | -46.64281 | 2024-10-01 03:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 63ba39f3-e6d8-312b-ac10-47c56b08eb31 | -21.30817 | -46.6473 | 2024-10-01 03:51:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2de57fc0-8eb8-3709-afae-40769a1ac63b | -21.26909 | -41.77699 | 2024-10-01 03:51:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df0c912e-6f83-39c6-ba48-03a97106c89c | -21.26781 | -41.78468 | 2024-10-01 03:51:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f8c3c91e-82b7-354e-8a1f-d8d2ac9b6623 | -21.2657 | -41.77635 | 2024-10-01 03:51:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ebfecb3d-00ab-3c83-b2b0-f5e78542a242 | -21.26505 | -41.78022 | 2024-10-01 03:51:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0ad3af71-305e-3c2d-86d8-a1a01aa2dcfd | -21.26441 | -41.78404 | 2024-10-01 03:51:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 7938286f-59c3-31b5-9030-750c3669be7d | -21.26102 | -41.78341 | 2024-10-01 03:51:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 05e0f151-c058-38bb-9259-b97260a64b02 | -23.28638 | -45.61428 | 2024-10-01 03:51:00 | NPP-375D | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7193c658-e27c-3638-976f-ceffad4243a1 | -23.08077 | -45.40088 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| f99e39bb-fafd-3f0f-a4c8-7d7d96de28c6 | -23.07977 | -45.40614 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| b74b7dec-26ed-38ac-8136-48549c653e3c | -23.07796 | -45.39453 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 0fcccc7c-3b27-37cb-a88b-c9fb6fec69ee | -23.07735 | -45.39846 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 13dd7c97-0c7f-3557-8d29-cd0ea0df8773 | -23.07697 | -45.39971 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| d86d0cb2-4f80-316d-b178-438e75f34c58 | -23.07637 | -45.40376 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| defd18dd-a165-31af-9d56-a470ce857574 | -23.07595 | -45.40504 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 47d4b4ab-0b36-3360-96c4-35043e818e43 | -23.07416 | -45.39333 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 133ce3ba-7168-34ec-ae95-f6bf624c5f75 | -23.07354 | -45.39728 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 64b64477-8874-39ee-ae66-6280d283aa0e | -23.07316 | -45.39856 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| e703f3ad-6b4e-30af-a116-598f77ea38df | -23.07254 | -45.40268 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 1c6654e2-a781-39b9-8dfd-f6a823a75b4d | -23.07212 | -45.40398 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d2c8efe6-8989-33d9-9aca-511e90a7f561 | -23.07152 | -45.40826 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 0bbb5652-887d-33ae-85dd-6b9b9d2a97dc | -23.07105 | -45.40958 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README59.md)
