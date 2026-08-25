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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e44358ed-6b8e-3bac-a428-62b335b2121f | -6.79476 | -59.40927 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3237faf0-6dee-3ce8-8563-92a14107a9e8 | -6.85886 | -59.40947 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| bdca3411-c75f-3bf4-b070-bb9092bca9d4 | -6.6897 | -58.7261 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cbfbe12d-d75e-3e93-bb8a-43b96180e795 | -6.84863 | -59.46708 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e967125b-5394-3f65-ace9-ddc4bf8c6c81 | -6.71678 | -59.44557 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1cad9371-497a-347e-a7d5-8380f6e21a1c | -6.18243 | -53.47865 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 34414602-b607-3e9c-b168-bb61db0e7635 | -6.12859 | -57.8514 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d6ce4869-8e2f-39a3-b703-aa4078f84474 | -6.62981 | -58.50252 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 71e8aade-9e05-38ce-985e-de035daa5ba7 | -6.63633 | -58.48113 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 6c7bade7-a607-3a74-81f7-3905684e744b | -3.10022 | -61.22379 | 2026-08-25 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5be95aec-2053-3bc4-a538-b70282dfef30 | -6.74507 | -59.64616 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 81168635-e8fa-3ea2-b40d-a366c22a3427 | -7.56869 | -61.21195 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 59e9074a-9674-32db-a4c1-df896454adac | -6.12698 | -57.84035 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c5f3e496-e372-3ca9-9f47-f25ebaae6089 | -6.80374 | -59.40801 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4f42f88f-1caf-3e56-9337-bd71cdb6dbc5 | -6.81374 | -59.68248 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e58c2bdd-9318-31d4-bd86-5d16733d732f | -6.12539 | -57.82936 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 317778c9-d968-3432-838b-5fec8cc8e11f | -5.78831 | -57.55634 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 3ae69d59-3ed0-36dc-ae01-13cc9564fe20 | -6.17495 | -53.4743 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 24f2b7d9-c70f-3c0f-b57b-d4a31ef2ae1e | -6.17866 | -53.4976 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 975fcf6a-38c4-361c-812e-2b90a9f8818a | -6.15262 | -57.94854 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 8cb50ffa-2a90-38ba-890b-d06bb4eaf9ec | -3.09659 | -61.19753 | 2026-08-25 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f62e6f99-f96b-3468-a761-506d67dfc8f2 | -6.93402 | -52.80319 | 2026-08-25 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 99d45fdf-9fe1-3073-8fd7-b82396a40b12 | -6.96006 | -59.07885 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 7f903236-2911-3700-b8a0-c1bcd8c4fa13 | -3.13054 | -61.18385 | 2026-08-25 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| afc44cd0-132d-3bb6-8b66-23dc1dfc464f | -6.14722 | -59.92148 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c3e12891-705a-3e50-99db-398c585f79ae | -6.7629 | -59.44831 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3d6d2af9-e4ac-3604-a71f-f329fac05bea | -6.12378 | -57.81828 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| c7f01897-7a04-3ffc-922f-c287f9c7e6d5 | -6.01977 | -57.66776 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a7c35401-c322-300b-9f0a-908136db2caa | -6.00985 | -57.66917 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cad42efd-5ffd-3f08-af3a-6ee5ad81d6ae | -5.96096 | -53.59898 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 6a69f1b2-21f9-3060-803f-442b5d4350dd | -5.79647 | -57.61428 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 45c8642b-8cb4-3f6e-ad66-9121367a1aae | -5.78484 | -57.60411 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 8791d7a2-1fd4-3acb-9d56-c788ad76bb3b | -6.80484 | -59.68375 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 26734782-54e1-3145-bbbf-f0280316bf35 | -6.73871 | -59.66554 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 944483af-07ce-3b36-bf8b-4d9c32a951cc | -6.53957 | -55.09068 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a66aa555-a0d0-31c7-91de-d5ad6ed86d43 | -7.54631 | -61.3796 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1e683f39-a50e-3e3f-b7aa-c97b3eeafbe5 | -7.0135 | -59.26185 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 58b33f86-303f-37b2-8bb3-3a4e9ccbcefe | -6.72575 | -59.4443 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 1989d059-6215-3b0a-b9b2-e99eae497ee0 | -6.36173 | -54.76083 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 81267334-e80f-3cae-9087-83eac3b3ba78 | -7.56747 | -61.20301 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| dd3a7b48-f53f-3e62-be38-c55905c0a89f | -7.21126 | -60.62147 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 40e427d0-4378-3605-991e-130ad1da5054 | -3.22228 | -61.24497 | 2026-08-25 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3115496f-6cd6-3b1e-bb0b-41fddc67d064 | -7.01125 | -59.57091 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 18b5f9c5-e038-3467-ae88-ccbe7abb9782 | -6.63122 | -58.51251 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 47f0a8ac-595f-30c0-a1cf-464c87c761a0 | -7.0045 | -59.26316 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| de0ff674-cf20-344f-841e-49f25065c579 | -6.70469 | -55.59312 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| d003419e-52b8-3dd4-8619-f3d9886ed33f | -5.77829 | -57.55782 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 76a330ae-fe58-3e0f-b3e6-51f8de8a4022 | -6.69919 | -56.34611 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 1dea6789-dd98-336f-98ab-afc16872c740 | -6.69323 | -55.59485 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 605afda4-aa72-31b8-add3-d17abeb97047 | -6.21967 | -57.77481 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c45d7396-22f3-3367-874c-21626a7dcf89 | -6.63774 | -58.49117 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 147.7 |
| bb6080e9-9932-3ed3-83e2-b8d2d21ea352 | -6.22517 | -55.48163 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 75c77baf-4f09-3b0b-9862-38b1d7a604c4 | -6.72704 | -59.45349 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 0eadc3ff-529d-378b-9264-879581d5087e | -6.61263 | -58.38136 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| e9da1630-bf1f-3be5-be40-775d9b7ed9bc | -7.54544 | -61.30647 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b04f7cf-56e9-307e-a754-24fb6a34020d | -6.77186 | -59.44704 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3cebc58-ec72-37ae-b123-337e39a19062 | -6.14859 | -57.7121 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 21f1e455-b82b-381d-b3e6-9aaefe6a3a63 | -6.88975 | -59.03762 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c4d76bde-cb03-331d-a346-3a5d608f4151 | -6.64057 | -58.51118 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ff095d6a-a2c1-3203-9821-f5e83618f167 | -7.54509 | -61.37061 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f3fe278f-54e3-35f7-9fc3-fb3d9dda836d | -5.94681 | -57.73124 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| faeb480b-1119-363e-b467-25e685d890bf | -6.79577 | -59.81379 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| abcfee53-ceee-3c15-91aa-0eec8c0185b9 | -6.78963 | -59.63974 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1f1fe21d-cb29-39d5-bdb2-c5c193d24f2d | -5.78929 | -57.5616 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 2ad818ab-c3f6-364f-88aa-e6f07aa058a6 | -6.70202 | -55.58783 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| d4390d1b-3ddd-3a9c-b0a5-e63fad1a3755 | -6.14597 | -59.91251 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d5a82f3b-3177-3ab7-a7a4-685ad9475507 | -6.74762 | -59.66428 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d5fdd6b8-5cd3-3391-8b8f-95a713dd3140 | -6.62697 | -58.48245 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 30f462a5-9f4b-3df4-8b38-7777d3a407c1 | -6.56089 | -56.55188 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 88e03f7d-7e6f-368d-ba8a-2a9a8edcebe4 | -7.54265 | -61.35258 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 751e628f-89aa-3263-8528-06ea78ee641c | -7.90163 | -63.68562 | 2026-08-25 00:50:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| daea9171-0694-3cbf-a7a9-ee7476709659 | -6.79348 | -59.60212 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 16a5c49f-09c4-34e2-b6c7-0c70aad43d6f | -6.99419 | -59.25519 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fa6acdd-9570-3ef0-889f-ec957822b564 | -6.60321 | -58.38263 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 0d60f86b-206f-3429-a7b3-a9c61b1e2eac | -6.82622 | -58.654 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 15a0a16e-a5c9-3a64-9094-e4fc3cf7dd66 | -6.61408 | -58.39153 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 17b5c282-26b1-3df1-bbcb-5e74295eb6a2 | -7.0109 | -59.24332 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 73838f81-dfcd-3d60-9967-1118c109d9a7 | -7.57113 | -61.22983 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 24ad3266-55cb-396b-a663-ad161eecb702 | -5.77664 | -57.54613 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 3204c15f-da81-38b0-b3b3-f716853e9389 | -6.79702 | -59.82276 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7bdb75ea-9269-3687-89d5-c5d67713063e | -6.40567 | -60.0639 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6f6490b6-feaf-33e8-9f93-26a1b3dc94d9 | -7.34752 | -55.66477 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5075177a-7d0b-389c-8a9c-dabfb44d1fbc | -7.53499 | -61.36283 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59af4644-ca66-358b-a6a5-77d859746133 | -6.13357 | -57.81688 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 5ac2af9a-cc8a-36f7-b730-464a21cddab2 | -6.22467 | -55.61767 | 2026-08-25 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ecc4a50a-6e18-3470-bc2d-87be442a0726 | -6.88842 | -59.02818 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| ac007d65-017b-3a39-8ae0-51bc438d5bb3 | -7.54423 | -61.2975 | 2026-08-25 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 70411bcf-b52c-3e03-a63e-f4dda79ee4e2 | -6.93686 | -52.79614 | 2026-08-25 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a172865e-34a8-33de-8d05-a627de98a9a2 | -6.18449 | -57.75257 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 78131ee9-ec5c-3cbc-8aae-007ad8f68540 | -6.96913 | -59.07754 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 63403913-2943-3686-8116-fc95e0daa231 | -5.95088 | -53.58335 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 450caea4-dd0b-3c19-a9ff-d529c7be87c5 | -6.82762 | -58.66388 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 5c160fd1-3726-3952-a50a-d198da05148f | -6.815 | -59.69155 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7aec33f1-7dc1-31c6-b10e-36edd55640c3 | -5.79611 | -57.60785 | 2026-08-25 00:50:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 3508157d-cef1-31fb-979c-b0354402b6fa | -7.02121 | -59.25127 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 3e45684d-fa41-3edf-a570-d463b802033d | -6.5511 | -58.53016 | 2026-08-25 00:50:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0873a1ad-af46-3a26-85e7-317713df9aee | -6.75652 | -59.66299 | 2026-08-25 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| bd69671d-4327-3a08-81aa-a8a8b389cd8d | -7.38018 | -55.1796 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 690d72ef-10a3-3878-8b66-b5c0fa62e261 | -7.34836 | -55.67099 | 2026-08-25 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 41c68b65-77aa-3577-a47b-6b0e8594597c | -5.95737 | -53.57587 | 2026-08-25 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |


[Clique aqui para ver as próximas entradas](README11.md)
