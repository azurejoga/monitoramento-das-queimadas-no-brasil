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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28fbceb5-dbcc-350f-9a95-89f760ae6896 | -3.09794 | -50.26496 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de2dd21d-0f89-3764-aa45-0be164be5d1d | -2.83014 | -49.43188 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3d46f55-da0f-3e3a-beeb-50831dfdb18b | -3.0373 | -53.26217 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d54893d7-843c-31ce-b498-8d4806b2db30 | -2.18121 | -50.32028 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c08ad09-3089-3a7d-8114-e0264f6ce97f | -3.0143 | -53.23387 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48fb9be5-84ac-32d7-971c-08f7b710f107 | -5.80595 | -44.13412 | 2024-11-05 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd0d670a-0f9d-3723-b4d2-5bf46ca829e4 | -3.41955 | -50.38712 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa77a909-3df1-3dfe-9ec7-2d1ebb0207e9 | -3.30237 | -52.95755 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e63e98c-2f62-36e3-9719-f69c1e83ba00 | -4.37326 | -47.24142 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f29a321-2e67-3b29-8fbb-7c67b3859238 | -2.91798 | -49.33944 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adc95fb7-5fae-37a7-9eba-83c9dbbe9878 | -2.12497 | -50.82885 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0c4fcbe-8bdd-33e0-873b-0b4ea14bbc36 | -4.37574 | -47.25508 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 97c97514-8b87-3491-88f5-6fd6ad80f18e | -4.252 | -45.56348 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42cef2cb-4931-33dd-bdc8-fd15c7227656 | -3.03016 | -53.26458 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 59ee0fb7-f551-389d-89c1-b08a24a0e5c5 | -3.29247 | -50.33908 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e729e1af-1d82-3f3c-8db5-9a92ee84e5d3 | -2.79075 | -51.44158 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 994b7aa6-6d26-342d-9fc5-a019b21f067f | -3.88843 | -48.37074 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f4a4602-f895-38f3-a0b3-81f2fdb21237 | -3.55507 | -47.3859 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| cb79e11e-9cd3-3455-bc49-5beff2bcc6a9 | -3.04337 | -53.26663 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4dd3563-bee4-34fd-833c-c6fb50bad679 | -3.09369 | -50.26855 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10a34c2e-bd93-3a5a-972d-3b71c3620fac | -3.24692 | -53.07259 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1328e39-ef00-3f67-9b5b-47292aa7438c | -5.30929 | -43.07385 | 2024-11-05 04:55:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 420b0b1c-6a16-35c3-b0d7-31f71c430d73 | -7.1332 | -46.00774 | 2024-11-05 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| def13584-a94f-3067-bc28-0365fea61049 | -3.2301 | -53.39757 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34466d09-14a9-3027-961e-36d8afc797e2 | -2.83758 | -53.34315 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ae09e76c-305b-3ed6-9277-5800ac9aa888 | -5.59862 | -46.18571 | 2024-11-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 991f70b8-2158-3f1a-bb1c-5dabbb1519b9 | -2.18602 | -50.82638 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ff0cbe4a-385a-38af-9a6f-50c01eb605c5 | -3.09731 | -50.2691 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17170168-a2a2-3520-9a08-3e0570e969cc | -3.10454 | -50.27021 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0789efc5-f75a-3890-b7a8-f6d51756b2f8 | -4.40552 | -43.11283 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc63cd0c-6527-3c76-91d1-16a3f51ee56d | -3.693 | -51.08165 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecb5e03d-89c2-3067-a99e-a1b27bddb64c | -3.54951 | -47.39325 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a56b1e0c-a063-3480-9b86-85464c288ede | -3.00702 | -45.84893 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 567c6bd9-ba9e-3610-99b2-61c7fce52a5c | -2.87853 | -51.3063 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c663348a-261d-39a9-971d-f0dc3612ab9e | -2.60196 | -51.30285 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 92e5172a-9922-3079-96e1-0d8f36b61377 | -3.5607 | -47.37816 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e7d56f81-e23c-37a0-ab5c-4c1ba839ca56 | -4.90049 | -46.71909 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 297f5238-6ad8-3751-9e5f-589f25e5ca87 | -5.93444 | -43.65392 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6f5cb8d3-0cdc-3d3c-913d-cd628853a098 | -2.92302 | -48.6204 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed1a6500-8a2f-386d-8f35-c10345213c54 | -3.03622 | -53.26905 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b2715b3-eb8d-33c9-b4d1-5aa022b3f70b | -4.24279 | -48.04259 | 2024-11-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 140637ad-7e6e-373d-a27d-aa3fbc09957c | -2.90122 | -49.39854 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0423164d-44b7-35ca-9cf9-da57f744b1c2 | -4.91741 | -44.36284 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f67a085-6f78-3471-9af3-4f9f1a07acac | -5.45369 | -45.5297 | 2024-11-05 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fab457fe-fb33-3081-9552-93d0df984470 | -2.8943 | -48.72958 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c505b969-744d-3896-85fb-5f758374a230 | -4.5647 | -45.80288 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c5e5976-be0b-3be5-a467-bc355d975f8b | -4.37015 | -47.23182 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa2c962b-0f59-35c8-a830-70602fad89d9 | -2.65822 | -48.57427 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef161e39-da5c-314e-868e-e4c1fb6528d8 | -2.75263 | -53.21382 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65de2975-7b7a-3982-84af-df516fab90c9 | -4.60675 | -46.87574 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed3ef3cb-219c-32e2-9e1c-2ebb6dfd364c | -2.27674 | -50.45377 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b37658d0-2020-3bb2-a9df-dcff71648cf3 | -3.99148 | -49.94332 | 2024-11-05 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f40b29f5-82ac-30f4-a65e-53aafdde8639 | -2.64803 | -48.56137 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 855100e6-5d6e-352e-a586-d119a1f829e0 | -2.943 | -54.6768 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7144adc3-2b71-3e0a-885e-822171705315 | -6.1041 | -43.96598 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b5c93cc9-38be-3419-af21-3114f972287a | -3.39526 | -51.67912 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eba7ad94-6c71-3944-98cc-dc2ecda8066f | -3.00128 | -51.75487 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11157a0a-cff9-3882-b9d6-d82fce05423e | -3.64046 | -51.79157 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b35c273a-9e1b-3467-be67-2ee3eb44eb9a | -4.62616 | -45.69993 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfac2586-dd55-3d81-8b9a-188bac02108d | -4.36882 | -47.24062 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c79401b-e2f7-3924-91b9-c0951d24905b | -3.5633 | -52.69988 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8bb9e63-20e1-33f4-bf1e-9d5bf2d00c59 | -3.06135 | -50.50368 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c822791-2e1b-3aba-bddf-e11351c4483b | -7.13276 | -46.01083 | 2024-11-05 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fbdd73c6-80ce-3d3d-88bb-7f3ce166a68d | -4.71468 | -48.85674 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3fe74c82-0767-30a5-8a9f-aef2515d9600 | -3.42084 | -50.30629 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12e971d7-4383-3774-ac1b-826ab40b85eb | -3.4136 | -50.30518 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 260f00cb-1d04-3242-866f-0ec80593341f | -3.07925 | -54.50303 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67b78fae-f993-365c-bf06-a94bdebfdae9 | -6.51859 | -45.94029 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 856f00be-26ab-34e4-a055-2671962bc60a | -4.08346 | -53.76061 | 2024-11-05 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6393b743-bb18-332a-bba9-053463aed79b | -2.8746 | -49.49752 | 2024-11-05 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c7d8d5d-3209-357f-b75b-c41297c71635 | -3.10092 | -50.26965 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a31e488-ad7b-3497-852c-fee8c9ce9a97 | -2.18183 | -50.31622 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40122667-fde7-3577-96be-48792b8d16f2 | -2.78273 | -51.60637 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec33dd4f-3e67-37d3-96bd-a4fecfb27625 | -2.60825 | -51.30763 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa5c24f0-8426-3e50-9b00-d810cc89cb5d | -3.54516 | -47.39255 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9d69c286-25f0-3817-9687-2382b3769bc3 | -3.1005 | -50.24826 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 97088f95-5525-3915-a1f7-0faabd773b19 | -2.15112 | -49.63787 | 2024-11-05 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc3ad7a2-aeb4-3d04-9389-c9ce869f6c4a | -3.27229 | -50.29475 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b5e94d5-e12c-32c8-ac0a-d0ad7e16bb2e | -3.10815 | -50.27076 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a2c344d-f0f6-3bc5-bb65-78e0318c51a0 | -12.35438 | -57.43393 | 2024-11-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39b30ec0-b34e-3b4c-b30c-8ae5acd715e6 | -13.44154 | -61.38814 | 2024-11-05 04:57:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3a1f371f-ff14-3115-bc68-a3fa1d8f34dd | -12.15912 | -44.62359 | 2024-11-05 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64bf5b6d-d3ab-352b-84bd-7dfd51fb0613 | -9.59589 | -65.6964 | 2024-11-05 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 621cddfe-a870-30fa-9660-6ecf030314a3 | -12.36952 | -57.42831 | 2024-11-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aeb5c2c-1a69-32eb-843b-a6197b524f9d | -15.28923 | -60.39904 | 2024-11-05 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51e3bee2-0f43-3deb-8694-f3f05c8eab3f | -12.35097 | -57.43334 | 2024-11-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46cd171f-62f2-3de9-a13e-297b6044a3b9 | -12.34757 | -57.43275 | 2024-11-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 123b2c5e-17b2-37f9-b9c8-f1906a83d95c | -9.59372 | -65.70058 | 2024-11-05 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fd2e919-1285-3abb-8745-5d1af61434b1 | -15.20258 | -60.36049 | 2024-11-05 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb0a9f64-8b9a-3155-a8f2-366fbe12ef6f | -12.35778 | -57.43453 | 2024-11-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6494739c-b717-3525-b08e-6ac5d537a40e | -12.15963 | -44.61927 | 2024-11-05 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69ecf415-4f47-37d5-befc-58297acf39ca | -11.86069 | -43.87464 | 2024-11-05 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70fff34d-7bff-3ba2-836b-83c810bff0bb | -11.86011 | -43.87953 | 2024-11-05 04:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79592650-15a6-3c3e-9f39-d9b20bc8dd3d | -15.18817 | -59.26695 | 2024-11-05 04:57:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb40116-36fa-3648-9b4b-a6b5f63c554c | -12.16508 | -44.62427 | 2024-11-05 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08877e65-72db-3769-8d43-3ca44cd14169 | -9.59511 | -65.70063 | 2024-11-05 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db329529-57a5-3b26-8593-062c77fbd4c6 | -12.16457 | -44.6286 | 2024-11-05 04:57:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7ea36d4-2e95-3611-859f-e3f8c9e5c730 | -9.59453 | -65.69637 | 2024-11-05 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52de1bd8-0a22-3ce5-8caf-c1aa0bdc17d9 | -12.36921 | -57.42882 | 2024-11-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 708357cf-a582-317c-8595-84e3d4894e0e | -19.11304 | -54.91639 | 2024-11-05 04:59:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |


[Clique aqui para ver as próximas entradas](README31.md)
