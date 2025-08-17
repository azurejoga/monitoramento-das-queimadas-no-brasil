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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84c9c0ff-37f0-302b-83b7-417f97ab2cda | -13.58769 | -47.7618 | 2025-08-17 05:44:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1037fcdb-5af8-399c-9945-63b42985a6e4 | -13.60376 | -46.88827 | 2025-08-17 05:44:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| fa5f1139-ff86-3210-aeb8-c8671affe811 | -13.58609 | -47.77193 | 2025-08-17 05:44:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.7 |
| fe14912e-8846-3d7b-bf9a-db199c79fba7 | -15.13921 | -48.74028 | 2025-08-17 05:44:00 | AQUA_M-M | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9a44435e-9c43-3a97-a53b-31dcb63e1c2d | -12.13757 | -47.90733 | 2025-08-17 05:44:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 3bc4abba-f11a-3a21-8a64-063d73672898 | -13.61274 | -46.8895 | 2025-08-17 05:44:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ddfc1ddf-9036-3a45-9930-9366ae805d80 | -12.55111 | -46.94053 | 2025-08-17 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b4d94412-b7b1-3c33-8536-8c7b1abd5a96 | -12.61269 | -46.90183 | 2025-08-17 05:44:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d7c925d-edaa-342f-bd01-64877cf7fa3a | -13.61131 | -46.89868 | 2025-08-17 05:44:00 | AQUA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 460234bf-1b8c-32d0-af1b-995823bab069 | -8.74229 | -44.03343 | 2025-08-17 05:44:00 | AQUA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 549d07f8-229d-31a3-9415-d76c1f29679c | -10.18225 | -46.82782 | 2025-08-17 05:44:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 07de77db-d215-387a-b34a-fc6f4c41edf7 | -14.59285 | -47.95539 | 2025-08-17 05:44:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b6b3ffa1-53cb-3d5e-9486-a86731f7be4f | -12.13581 | -47.91822 | 2025-08-17 05:44:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 70c94673-223a-3c1d-a3f3-f2afe8a0573d | -12.19102 | -47.23357 | 2025-08-17 05:44:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 79f9d729-d8ca-32f0-b4de-91d659370ec3 | -9.28708 | -40.23275 | 2025-08-17 05:44:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 3b809bcf-54d8-352e-91ad-a5b87a15ca7e | -10.83345 | -45.35727 | 2025-08-17 05:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa547500-327d-3593-ad9e-b1757932da80 | -19.16965 | -46.573 | 2025-08-17 05:46:00 | AQUA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a4eca0b9-7787-3f0e-bd73-9346bac5d357 | -20.28717 | -42.20391 | 2025-08-17 05:46:00 | AQUA_M-M | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| c081b123-e516-3456-b458-2fe050e345a8 | -8.9788 | -60.4964 | 2025-08-17 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e2221f12-549b-3d76-9980-d59cfe3cdd10 | -14.9819 | -54.7536 | 2025-08-17 05:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 140e0924-c0ed-3021-8583-dee0d1ebd60e | -9.16541 | -59.61589 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76349597-526c-3dfb-b1fd-05388e5b406b | -7.21456 | -60.386 | 2025-08-17 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22b214bd-043e-3840-85da-6105f16057a9 | -9.16445 | -59.6231 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa0c469a-108c-3800-9f3b-aa39940978c1 | -9.14478 | -58.29714 | 2025-08-17 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c357c93d-fdda-30b2-af26-d237950d2df0 | -9.19728 | -59.62798 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 692ad0a0-788b-3d92-936e-8408e0d2df46 | -6.13623 | -57.93341 | 2025-08-17 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 23358d4a-51b4-39ff-9b8a-0ba4a87f35cb | -7.74878 | -67.1441 | 2025-08-17 05:53:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f045dc7-121e-36a2-9449-d84b47f6cef0 | -9.19238 | -59.62678 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d083af28-03e2-32e1-93f3-56618e293645 | -9.18343 | -59.64787 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 54a4c359-8fbd-3d7c-ad1d-1b34908a6625 | -6.07694 | -59.94244 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e17fa4f1-5fec-3c20-9533-49d6685cffa5 | -9.19679 | -59.63159 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a25dc73-0919-3f51-a6a9-52d8e4580ae2 | -9.18962 | -59.69168 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ee8764e-d13d-38f4-9ea3-f7e48bccd04e | -8.97159 | -61.67948 | 2025-08-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad8a61ea-af50-3456-b081-97ccb2d3eaf4 | -9.19785 | -59.62764 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 258aaed6-5cb1-3fb2-9110-c2d4248f9087 | -9.38753 | -60.54384 | 2025-08-17 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11520972-e7ec-3f9e-9ec9-8c46f5731120 | -8.89499 | -60.74611 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d841970b-d0bb-3c4c-bb8b-45804e590762 | -5.81099 | -59.21529 | 2025-08-17 05:53:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aad1655d-a9fb-3ff5-9b25-13ebac4be4cf | -6.07355 | -59.96648 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82513b05-7668-38c8-9ba5-ae18bcfe3a6d | -8.9946 | -60.53255 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58334cf9-cb74-3f38-b57c-3d064de8c85e | -9.19692 | -59.63487 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2db2803c-69c3-39f2-a7f2-fd1307bdc33c | 0.96853 | -60.40949 | 2025-08-17 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 61db752d-8c05-3777-8c9d-c81c7c9f4a30 | -8.99892 | -60.53944 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 224b48d9-ed75-30cd-b9f8-7cf81fde85fb | -9.14177 | -58.29454 | 2025-08-17 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5228181-6d8a-384b-8497-d375e014f1b8 | -9.18886 | -59.64894 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17ec485d-9131-36d9-a383-4e2dc090a18f | -9.16397 | -59.62668 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05d652e5-98ac-3d90-bc26-15cf70957357 | -7.97842 | -70.03256 | 2025-08-17 05:53:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a5094f3-e016-3154-abcb-3baf9f7e899e | -6.08124 | -59.94904 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1f5ba16-ed14-321c-ac8f-2897009544f5 | -9.3871 | -60.54697 | 2025-08-17 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77cd3e89-636d-3822-8275-5f5694434a8c | -9.18859 | -59.69185 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 105fd810-8bd4-334b-a15f-3fd727fdd8ea | -9.19192 | -59.63038 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80e2be83-4490-3dad-b213-6c15dc4cfb5e | -8.98987 | -60.52871 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50c47748-aeed-33e1-a7f4-6b21e5c2eaf0 | -7.49577 | -63.8119 | 2025-08-17 05:53:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e7e7e68-1507-359d-b22f-76f656edb7e1 | -9.18265 | -59.6947 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66b2f8cb-1ce6-3d6f-9802-fe4a1bd059d2 | -9.18216 | -59.69828 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a979dff0-fd24-3ad8-82e3-eaca4d939ff5 | -9.17824 | -59.65018 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 188147c2-ac42-39d0-b943-4596607b7721 | -8.99973 | -60.53333 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c4dda9d-3345-314f-9866-12fb629e9cdc | -7.42475 | -60.598 | 2025-08-17 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b56abdb-3f86-3987-916e-615eb4d56f5d | -8.99234 | -60.5101 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bc92dc9-e0f0-3609-8936-d59f7b815e03 | -9.18322 | -59.65481 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cde98b8-fcd6-3c50-82c5-91f852d6cd35 | -9.22344 | -59.64536 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d2b2d0a-05dc-3cc1-93d1-fa48864e9074 | -8.98864 | -60.53797 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07c295a9-ada8-35c9-afe8-5e565c58baa4 | -8.9831 | -60.54028 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afdc8e7b-b87f-317e-bd2e-a4c41cbd84e3 | -8.99215 | -60.55096 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a07d6d7c-b229-380d-bb8c-44dbc1aa473b | -9.20469 | -60.83316 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 317f36e9-1d02-34ca-8fb8-4109aff1f156 | -7.42014 | -60.5945 | 2025-08-17 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6070a404-9cfe-3011-933a-6277423249c1 | -6.07955 | -59.96105 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 33d372e1-9755-385b-9f68-f1d07c1bde57 | -9.21749 | -59.64824 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a69ceb0a-1d65-3f0c-afed-af847b3a4f86 | -9.19738 | -59.63129 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3c986723-e20a-3db3-b30b-d0b3bb767901 | -8.99933 | -60.53638 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7966b029-64b5-3fef-ad02-a0cb90d0d385 | -8.96683 | -61.67883 | 2025-08-17 05:53:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dd1014c-8465-30b5-b817-18aa46546cca | -9.13882 | -58.29624 | 2025-08-17 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 118cd6c5-e1ee-39d4-99e0-26f133599e1f | -7.10469 | -63.00126 | 2025-08-17 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c2313750-dd67-36c4-9875-b54cf68303cf | -9.16252 | -59.63756 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5281635-670d-3d93-9d35-a848c85111b5 | -9.17719 | -59.69401 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a1c385b-64b7-3d53-a44a-3d03c634f9fb | -6.07609 | -59.94846 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c78c841d-4c46-38a1-a198-2bcef590aab7 | -8.23452 | -61.47015 | 2025-08-17 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3c16d5e9-9744-39c8-aa0c-7685965c9c37 | -9.21842 | -59.64111 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c98e04b-74b9-31f7-9c94-b2af1947b529 | -9.2239 | -59.64181 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3edfd8b-d5b5-354e-a469-b5f19d272a86 | -6.08167 | -59.94602 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ff7d99b-9487-3c5e-8b08-835893f1e297 | -6.07397 | -59.96351 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65a40501-d99f-3d90-9c14-70ad06ce212c | -9.15848 | -59.62602 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81a24ae0-5c78-3e01-a7f8-29a6550e37e6 | -9.18294 | -59.65144 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c0785c73-6b8b-34bb-919c-8a39d3709419 | -9.20429 | -60.83609 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 758e2351-90f1-3f67-89e4-b9d8f5ab4524 | -7.41974 | -60.59734 | 2025-08-17 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63b2ce0d-d1fd-302e-81e5-dba30d4efb0f | -9.18957 | -59.6487 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a8f90fe-8405-3f09-acc8-ef48db99398b | -8.9827 | -60.54332 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 962e6d27-cd0c-31c4-8ae1-2b2524a3c739 | -8.99419 | -60.53564 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5b157f2-a998-3860-9e93-c53671fdcdda | -6.07912 | -59.96406 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e32ccf0f-e5fa-39db-9553-e97c7d91fa68 | -6.07313 | -59.96949 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 333bce81-2fbd-3733-807d-87445b1a2aa7 | -9.1767 | -59.69758 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d64560d-3010-3089-9907-b3e7f21acbed | -9.1846 | -59.64399 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b6cb75-8cb0-3ea0-b875-b3eccd7ba204 | -8.98719 | -60.50937 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2364d8d9-d475-3404-86e2-b97f238df009 | -9.18837 | -59.6525 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb732fd9-142d-3a9c-b182-52ab359adb9c | -9.20508 | -60.83023 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84e21cc4-04c9-3754-82a8-d782460be05c | -9.39227 | -60.54761 | 2025-08-17 05:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 590ddab3-6fb7-39bc-8b74-8da98450678e | -9.18414 | -59.64762 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c03969be-519f-36d3-91ec-7bbe9c4dea2f | -9.13825 | -58.30064 | 2025-08-17 05:53:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69aa97e1-c86c-3381-a337-e21f4a42fa89 | -6.0744 | -59.96049 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4abccc51-5464-345d-a8b4-676b131144e8 | -6.08209 | -59.94302 | 2025-08-17 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d6b6fbe-e70b-35c6-a535-0b642021fc80 | -9.18368 | -59.65122 | 2025-08-17 05:53:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README38.md)
