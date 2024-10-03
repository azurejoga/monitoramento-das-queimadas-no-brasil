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

## Dados Diários - Página 200

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 222b7322-8f39-36ef-8027-573362d88cc5 | -7.63612 | -67.20794 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1324a762-e7c0-39d5-9ab1-fc105753a2b9 | -7.63674 | -67.20345 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e783854-19d4-33f4-9b9e-1f1e243990ae | -7.63735 | -67.19895 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d111281f-6d06-3594-a8f6-f042cc00846f | -7.63796 | -67.2052 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0ec81f54-6971-3c9b-9551-a844476641f8 | -7.63855 | -67.2007 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 501df925-fda9-3a6c-9495-97970beb1d24 | -7.63913 | -67.1962 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab876e63-eb2f-3e7d-9868-662f7a783feb | -7.64279 | -67.20425 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dac6caa2-7ca8-3bd1-9659-19bec2aa2ca5 | -7.64341 | -67.19975 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2aba8138-6dc6-3d07-9f54-385ccd8e11d9 | -7.6446 | -67.20152 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 640602f6-d5bb-388a-ba3e-7e6a351d5543 | -7.64519 | -67.19699 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 753c53f8-f8ef-3be1-bcd1-feb72000fb3c | -7.68718 | -72.36256 | 2024-10-03 06:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bfb1b39-21df-34d3-a2b4-c1a8bac9ff1e | -7.71065 | -67.12234 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac24ec7-c639-37cb-ba17-19e12b02f6f9 | -7.71125 | -67.11784 | 2024-10-03 06:31:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80193833-9cdb-3718-8aff-bbee3d96193e | -7.77797 | -72.98396 | 2024-10-03 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd69984b-e1a4-3224-aeb2-1ddc587cf4af | -7.78208 | -72.98454 | 2024-10-03 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81cd36a-0d44-3cda-af92-00552099a274 | -7.79076 | -72.99983 | 2024-10-03 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45f77c98-8373-3413-a04f-bc0bfa5c635a | -7.84915 | -71.81279 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16caf6b2-0801-3ebc-b2c5-74b0a933832f | -7.88246 | -72.80079 | 2024-10-03 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d44372d6-3ff3-31e3-a3bf-3bdadba029f0 | -7.94968 | -72.51531 | 2024-10-03 06:31:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8ab97f8-8869-391d-b64e-0dcc2375d952 | -8.04645 | -71.18456 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04915608-511f-3ff2-a4ea-374545bbb9db | -8.04657 | -71.26693 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 294c5614-7b30-3daa-acd4-3781bb9ebbdc | -8.07232 | -71.27211 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29ac634f-504f-3212-bbba-4c6ca65c7c87 | -8.07971 | -71.21886 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75612c57-6be7-39bc-8804-358607191fd3 | -8.09011 | -70.93165 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b56ab32-cea2-34a2-a6d3-e55d94d0195a | -8.12223 | -70.49787 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8791d60-42eb-38cb-8777-9c5752474833 | -8.12712 | -70.49862 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4b5a01e-9a5c-3cf7-8e5f-e2ea39eedb53 | -8.18318 | -70.08904 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fbacac0-99bf-3f0a-95ff-92ab65983816 | -8.18456 | -70.08902 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 885cceb2-8a34-39e0-b87d-abb0560da654 | -8.1882 | -70.08981 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca57e9b6-0f41-359b-a9cd-3e18749fd106 | -8.18959 | -70.08975 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad814d48-b397-3c54-82b4-375e05ea1d97 | -8.19636 | -71.0122 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69a44e9d-e7a8-3d76-9572-45a384a7c96a | -8.22417 | -70.80778 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1648ce98-fdd5-36cf-b137-7eb8f6336893 | -8.25434 | -71.14703 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5289f4d3-06d9-31af-ba53-de0efed2d9de | -8.2558 | -71.14853 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6247e813-8807-38d2-936a-4bd205f1be24 | -8.25646 | -71.14362 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfafb1cb-d0e7-35f1-bb85-d02edc58dba7 | -8.28229 | -70.56225 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 333994de-0838-3490-afb8-af8f64d2431d | -8.30781 | -70.52162 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91436238-3d76-32e3-af76-c49fc4ca2a9c | -8.33958 | -70.25405 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b06df110-f9da-3db2-8dca-d00569fa1e66 | -8.37131 | -71.20988 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd1a0d7f-9c76-37dd-8f46-3f723db2827a | -8.37362 | -71.2118 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a456ee8a-6dad-31d6-9623-6c2dbb39998c | -8.46639 | -70.36423 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bd18018-2998-3a36-9e0a-3824edffdd9b | -8.46709 | -70.88134 | 2024-10-03 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35613c8c-b971-3032-b09e-93bd673d0e6d | -10.27305 | -68.76878 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5347d72b-5f1d-3478-8432-6fa49ccfa897 | -8.46725 | -70.36505 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b784bfd-099a-3f96-9a6f-86f3e48dd514 | -8.47134 | -70.36494 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc44ffe3-4538-35f1-a04d-87eddce93c6e | -8.47221 | -70.36577 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f41fc5b-220a-3d30-9d48-3117f988bfd9 | -8.49095 | -70.52634 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe4c3b67-c917-3c2e-8ba3-0a6c66b0fa9d | -8.50448 | -70.23717 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a79182f7-f191-3138-91ad-d83cd4980b63 | -8.50458 | -70.2366 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a882a5be-63f0-3fb0-81ae-cbc851c67f35 | -8.51295 | -70.2501 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8443714c-3ee8-3a60-8e2b-80a826e74f6f | -8.51297 | -70.24947 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aec539b1-e7b5-3df3-a855-c41b43d9725f | -8.52985 | -70.35096 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68b5f0b4-7dd9-3dfa-84db-604f3d74b412 | -8.55186 | -69.95779 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59dbe2d6-12c6-3f25-9845-d9721a4d2fce | -8.61044 | -70.02402 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2545d89-bbcb-3d08-b6f1-e1e646273014 | -8.61085 | -70.02103 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2125cf2-0973-3445-a0aa-225b6531ff17 | -8.61552 | -70.02476 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de0948cd-117b-3f80-b856-3874418776a1 | -8.61593 | -70.02177 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41fce8ea-665a-3703-a074-625f1ce4c513 | -8.61718 | -70.5283 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67f21dd1-c17e-386a-b06e-a5afbe4267e8 | -8.62612 | -70.02313 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db41250-1faf-3d1a-9090-808e47556a1a | -8.62654 | -70.02012 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0929467c-d8f7-31d6-9f01-15f048d6ec5f | -8.64069 | -66.7189 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b36b917c-e32c-3b1d-9aa9-fcc702a8305d | -8.64135 | -66.71391 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3811235c-3838-36ec-9c28-ff56951c1dd7 | -8.64279 | -66.71951 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9d475bd-6697-381e-b698-92ee101c6be8 | -8.64341 | -66.71451 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe4b7194-7398-31e8-9242-eddc97027921 | -8.64767 | -66.71474 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a53e9f6f-f67b-3fe6-ab95-34ee17211a64 | -8.64896 | -66.60611 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6498fe66-b67b-3544-97b3-bcd1887244c0 | -8.65032 | -66.60645 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2952a6da-8c0d-3031-9c5b-c565f528211d | -8.65232 | -66.6793 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 697c89c9-f653-3d67-b5ac-81cc2fbbe835 | -8.65415 | -66.67991 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e0f6d669-bb8b-3ce3-b1fa-5d9477864c0b | -8.65478 | -66.6748 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 04ac206d-575b-3027-86b7-8ffae82dd147 | -8.65533 | -66.60696 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88a3c5b2-0c8b-3d0c-9ec4-eeff64faaf83 | -8.65599 | -66.60188 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c9454ec-7ea3-370f-a209-988182c62fe5 | -8.65668 | -66.60734 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f667899-8479-3ec0-94fb-12025fec1b82 | -8.65731 | -66.60222 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd11c02e-737a-3483-aad2-dac5e192c962 | -10.26789 | -68.76411 | 2024-10-03 06:31:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07eae3a0-2784-3e5c-8b61-6b9f7cefaafb | -8.65866 | -66.68014 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fea4b889-2e2c-36ec-856b-34045344dab5 | -8.66049 | -66.68074 | 2024-10-03 06:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24193e70-955a-3958-8409-4d753318f1cf | -8.74549 | -71.01016 | 2024-10-03 06:31:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1bdf7ae1-5c81-32b5-b64b-dbbf1a5776a9 | -8.75514 | -67.70542 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44b51775-e86e-3462-92e1-6abb4421c478 | -8.75569 | -67.70107 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f759470f-33a0-3706-8fa6-df31d9b6ec56 | -8.76108 | -67.70627 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cecd429-fcad-3370-bb73-5b67194d5a0a | -8.76163 | -67.70193 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 39afb3f0-47a8-3b2f-89be-eefd6bc3cd5d | -8.76219 | -67.69756 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8af9dc2-9075-34e9-88b0-a8393e07930e | -8.76703 | -67.70708 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7b07c2a-950d-3460-9943-a85fcaecb9b2 | -8.76758 | -67.70275 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b0788a8-a1c6-3348-a014-91c15d59fafd | -8.76814 | -67.69843 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d1b8e99-2a0c-3126-8228-7fdb58661117 | -8.7687 | -67.69408 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20407f6a-b09e-3d8e-9848-3e9ab8cfd2f0 | -8.77409 | -67.69923 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c18c6af1-a0c8-33a0-a4f8-1687f4c992ff | -8.77465 | -67.69488 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cf38bab-4719-39f2-904a-f284da6a00c6 | -8.78061 | -68.84803 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b048916d-b9bb-3e03-85d3-75fc32f7f518 | -8.78107 | -68.84442 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a3dafbf-3f4b-31f8-9dc3-1d5c8e4e4f89 | -8.7814 | -68.84939 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 338ad271-2a42-3dda-a99b-0096f2cc9b56 | -8.78188 | -68.84579 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be91f87-638b-3517-a40b-79d20e72a09d | -8.78237 | -68.84219 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9d879bf-3e66-39dd-9282-a73a2a45a70d | -8.78271 | -68.79788 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e00edaa3-d12a-30e5-a48a-12a91e6670ce | -8.78613 | -68.84885 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79141015-a419-30b4-be1b-e8c569d48146 | -8.78659 | -68.84525 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d566ca-a10d-31bb-b12a-b8c84bc1e12e | -8.78663 | -68.80081 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 02d5a0b9-f973-3c5d-b4e4-a46b834d5bca | -8.78709 | -68.79717 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 2e009582-4277-39f7-a53f-76316193d4a0 | -8.78776 | -68.80225 | 2024-10-03 06:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README201.md)
