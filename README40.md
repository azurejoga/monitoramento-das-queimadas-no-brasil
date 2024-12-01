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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9afd0142-1eac-3d94-a129-94dfcf091d89 | 1.2514 | -50.69516 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0129df65-2c01-303c-bcc8-f179f475754b | 0.97586 | -50.12198 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 733cca9e-5831-3a56-a661-57e755342168 | 1.1727 | -56.01336 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83d1def2-a32a-39d9-81bf-f657f192980b | 1.20944 | -56.00939 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35f80231-301a-3a91-9b25-0cf8d040dfab | 1.14951 | -55.98445 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c5a2ebc-02c5-3539-891e-4ce05605f399 | 2.7352 | -60.39226 | 2024-12-01 04:42:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1718fb96-dbeb-39b5-8972-d28e30e3782e | 1.16161 | -55.97015 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29c2f792-47df-31ce-988d-8d5d02509529 | 1.15548 | -55.99278 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 9f1fddc2-d2e4-35e6-8094-0165e8fa801c | 1.1655 | -55.96794 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f7ef5dd9-a9a1-300e-a635-6c1d150ba1a3 | 1.17617 | -56.00507 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2ea5f35-7d15-36c2-8b78-b77f6ee8e9be | 1.17837 | -55.95816 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30e6ba18-2e19-3d77-9811-b91163686198 | 1.15334 | -55.97921 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cff715de-fb07-3236-b01b-8fd6309634f5 | 0.9401 | -50.73495 | 2024-12-01 04:42:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9ec5e7d-d19c-35d5-9b24-935b8f35f6f9 | -2.43828 | -53.88648 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be9bdd2a-3686-3994-a4fe-adc3704780c8 | -3.20635 | -53.12351 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9d394894-3718-3972-9389-31e77a1b783f | -1.43891 | -53.39801 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc1db58e-2bf7-3431-a8bd-2103eb059ff7 | -3.25981 | -54.22876 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20273dbc-43e8-33b6-9c0f-7ead60d5124a | -1.28201 | -52.69046 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3113fb58-6fa2-3201-9b5e-9f462100a3de | -3.26113 | -50.78728 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19abe4fb-57b9-3578-aa38-01e5269f4cc6 | -3.25141 | -53.87064 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b9946fd-88a1-3341-8a3d-e52697062fab | -2.76239 | -49.22593 | 2024-12-01 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef870ac7-b131-3808-b134-4e1362c6f060 | -1.6997 | -52.646 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9389f82-e6a2-3a31-82fd-40a4adbf7c6c | -4.28664 | -53.69137 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5191126-b901-3c2e-a73c-b3ea8e1aab4a | -1.06888 | -51.79436 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79a123ff-ab91-35df-aca4-55e2c1162850 | -2.84768 | -54.05434 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c175094c-256c-3365-b6d1-985f5acf5ab8 | -1.56912 | -51.16995 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10a5eae4-00a6-36e9-8735-98fb3f6764d6 | -3.65099 | -51.96069 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 417e12d0-47c9-3372-92c9-58e6a0c5b2e6 | -2.86697 | -54.00636 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0f68554-160c-31bc-8a6d-e5b4030ca98c | -3.19602 | -51.30703 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 462224e5-3089-3b0d-bede-f2536c1af140 | -4.9024 | -41.3183 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dba05ee1-88d6-32bc-8ccd-4407b8d957bd | -1.26723 | -54.55237 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62a6485b-be7d-37d1-ad78-bf0b63a4447b | -4.05645 | -46.81825 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35c9433e-d5bb-3ade-928c-3e1302e443f9 | -3.4716 | -50.26781 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 106465a9-c0a1-393b-bf5d-71ce2146b278 | -3.69197 | -51.81136 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a360b85-cc74-33b1-b143-c9b42de5f5e0 | -2.98399 | -53.90455 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f3c86f3-cd49-3e91-8d49-a005a3dbbc35 | -2.9817 | -53.895 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7641b3e-2d3a-3e4e-882d-3d9eb42d2616 | -4.20161 | -50.68333 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90193884-1066-3be6-bdaa-354aa6e83255 | -3.02658 | -54.02351 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39bd984a-aca1-30fb-a1bd-6f31a5e597ea | -2.47121 | -46.56727 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cbba87d-c3d9-3f44-a609-ff428b17c68c | -2.1903 | -53.77344 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 22062faf-99c8-3d12-a48c-02d01fe51503 | -2.82975 | -54.09343 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4206fd24-a528-379c-b317-3d5d4fb30ed1 | -4.01709 | -49.93874 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf788594-14d0-3087-bcfd-30b4db2c1444 | -2.61704 | -51.80822 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8862961-f9bc-3002-869a-2fd656d7fb92 | 0.85623 | -59.45137 | 2024-12-01 04:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7255698c-4873-3cd2-ab9f-e9559d1a2f9c | -2.78315 | -52.99442 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 520f2b88-c516-32cc-bb7f-c1a821a4733d | -1.44641 | -55.19656 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| caed702e-7795-344d-b6cf-37cedd850f52 | -3.45224 | -54.6215 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 494c39bd-5b04-3a24-8c01-faa283ef90d2 | -1.65834 | -53.42522 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31513a41-6116-3ad6-9217-b54b6e24389a | -2.8506 | -54.03621 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 70d622d3-da3b-31e8-8974-dd341aa074f6 | -4.01431 | -49.93475 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1340d5a-5e86-36c7-a0ca-69de83fbcb1e | -2.19039 | -50.58045 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 751ff7b4-a9f8-3ce2-a9b2-54f27afd5ab4 | -3.59092 | -50.37186 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad4d51f4-9213-3bf6-bb84-bb454dd2499d | -3.8056 | -51.00419 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6ca74abb-339d-361c-99ea-952d322e6b52 | -1.65532 | -53.42037 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f45ab635-a1da-380e-93dc-93ec81f68f17 | -3.02612 | -54.02583 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f052b9b-d29a-3d00-8f18-7e130d507f1a | -3.95402 | -49.7581 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5af6765c-2622-3f16-81e5-527237cd5e2e | -4.18887 | -50.6778 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b596a62-c4df-3c31-b754-9d6e279340fb | -1.6389 | -53.86508 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 299d758c-5a30-3091-817e-f4e2258f4fc6 | -3.02357 | -54.01842 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bdeef57c-98cb-34a5-8d79-9e1d87128e38 | -1.62401 | -53.88577 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38ff131d-4903-3972-9dc5-789b2e0cb46a | -3.25041 | -53.92524 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d30495a6-e523-3726-b856-78faf2d6cf7a | -2.83782 | -48.47643 | 2024-12-01 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d48e906b-b567-3774-96f6-1232dd9f8c2d | -1.31561 | -51.73649 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21dd922a-8cf4-3b77-aea3-edd20ec893bd | -1.28128 | -51.73111 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a265ce1-568d-38e1-b392-bf817b2e7a53 | -3.19884 | -51.41981 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89ef4f15-407d-3707-951b-913256b2a1a1 | -2.19105 | -53.57226 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| edd41a02-9e45-3b16-9aa2-b3ffef2534f3 | -3.92973 | -51.17757 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 075cbdbd-3134-38ee-a02f-0fdec3af6b57 | -1.48588 | -52.67615 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 916ba068-34a6-3133-a1d1-23c77c6a37af | -2.96304 | -53.89215 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e9c4b8b-4183-3ec6-bc2c-e05dd283ebfe | -4.20786 | -48.12132 | 2024-12-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c68ef8f4-186d-3c97-99f0-52a266d51b59 | -4.16893 | -48.62439 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21fe0d02-e94f-3b24-8425-b40ec2057bed | -3.48882 | -54.03033 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a196fabd-4041-3d00-b395-23ead17eae29 | -3.26507 | -53.64191 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a6e9242c-fa53-3eff-a0d2-509a392c05f1 | -1.20719 | -51.73918 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6be81bb-3468-3eda-95d2-455603ab523e | -3.13138 | -54.52851 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f65bb807-290c-36de-9e3b-4c8d19031214 | -3.00871 | -53.23612 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa8cfc81-e082-3340-ad44-6c5884429ab1 | -2.33482 | -52.18251 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 584b098c-c4d8-3d9b-8806-53b5b065005a | -1.07454 | -53.62684 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a84b44ad-75ce-36fc-bdd3-fe6f18a10c72 | -2.95137 | -51.79272 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab9e2188-2fb5-3c4b-9418-f9eef4e09e23 | -1.49028 | -52.6481 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0c5d9d5-efe6-31a5-925e-c44c2f0e63ba | -3.63688 | -51.0207 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc316513-1c97-3bb1-9fec-d8c60a026656 | -3.21302 | -54.08884 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65708181-26e9-3572-9893-8891fcea2e0a | -3.18849 | -54.33149 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc831cf7-51f4-39a0-b1f6-38bd3cf9a7ad | -3.00577 | -53.23136 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2280d3fb-de19-3f15-bea1-2a7ee01a4b37 | -3.01087 | -51.79097 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 34cb6e50-97f4-3951-98b7-92ec5d56e1ae | -3.72518 | -51.10226 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11f0b71e-74cd-3dc8-b97b-357f85fb9b79 | -2.97781 | -53.87169 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cc34767-2721-3ae7-913f-70cec5a56d4a | -2.75202 | -51.75031 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 31e650e0-f521-3e89-9778-68ace2089952 | -2.32383 | -50.6793 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f85ba62a-2e4a-3811-988e-741b2751b8b2 | -2.61363 | -51.80768 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 828d12b3-8d06-35c2-9fa5-fea26d268185 | -5.65408 | -51.46705 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8aee73ef-5d22-39a0-852c-637bb5ef6f20 | -2.26739 | -53.46269 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07797320-4eee-3e4b-a421-be3a57772faa | -3.29215 | -52.58901 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38743bb2-0c26-3aa6-9490-bb9598d69db0 | -3.11907 | -53.80666 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| f1a8267a-1d0f-387b-b8f5-93b8bd422a30 | -3.24742 | -53.63475 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba3e6236-5f27-336b-bf0e-1bc7efea3c66 | -1.66038 | -53.75217 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d42b9219-a969-3cf8-9e93-7250d7ef17c2 | -3.24878 | -53.62628 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74cff452-96d8-3410-b85a-7b129ca46d33 | -1.08514 | -53.63304 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d0ff79d-35d6-3c15-a2ac-a9f93ce10bc8 | -1.82475 | -50.90169 | 2024-12-01 04:44:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c5235911-1eb9-3cb6-b909-85da5e5a98c3 | -2.57845 | -53.97649 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
