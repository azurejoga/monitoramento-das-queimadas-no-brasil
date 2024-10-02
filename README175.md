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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51285dd5-68f3-374b-a640-92175eee1a1a | -12.5364 | -53.13095 | 2024-10-02 05:36:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9707f258-e875-3116-8aed-a5e063e7c48f | -12.3313 | -54.10408 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c4e7ecf-8cd3-30f1-af99-4f8aa24b6aaa | -12.33078 | -54.10844 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4fba466-8486-38b7-bf84-fbe5558572b1 | -12.32587 | -54.099 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d44bb84f-2998-3f5b-add5-c369ec66e25e | -12.32536 | -54.10337 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35727b84-32df-36b0-b745-2f03e03d5879 | -12.32485 | -54.10773 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c2f5f9-047f-3dd4-9a45-4fed57c4cbe0 | -12.31994 | -54.09826 | 2024-10-02 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0684e376-c48f-36f6-956f-a574525120b7 | -12.26767 | -53.99957 | 2024-10-02 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1433598-8ad4-353a-8909-e7217b2cf53d | -12.26714 | -54.00397 | 2024-10-02 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ba3cea2-35d4-3684-9879-458262f301c7 | -12.26173 | -53.99862 | 2024-10-02 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ffb2fc3-1a4e-3ce0-bb60-8c9b94efb72e | -12.2612 | -54.00302 | 2024-10-02 05:36:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63358a9a-5b4f-3837-b4c5-083e0385e7d7 | -11.42083 | -55.06534 | 2024-10-02 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdedc554-6136-37b7-ab29-221348e5e2db | -11.42073 | -55.06597 | 2024-10-02 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56b11028-4430-32c2-ba10-73b0de75020c | -11.41533 | -55.06453 | 2024-10-02 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a237fbf-25bd-35a4-ace7-2a943c1b5a2c | -11.41524 | -55.06517 | 2024-10-02 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22976c77-0ec9-3501-8a03-56d85aad0cc9 | -16.13962 | -55.42374 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e7380d4-ed88-3e74-81fc-084d04f5fbbd | -16.13448 | -55.41785 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be155cd6-7cd2-332f-8f42-5243be9db752 | -16.13404 | -55.42189 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 504b3aa2-55fe-3b77-863c-4d37031a1938 | -16.13355 | -55.42629 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dba3596b-d518-3e77-b489-46e6d34f3648 | -16.12841 | -55.42044 | 2024-10-02 05:36:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a672a11e-5e25-3ac3-a600-7b7eff04b8f7 | -15.38259 | -55.84428 | 2024-10-02 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b49495aa-f389-328f-addf-22e3ab72dd5d | -15.3767 | -55.84703 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07f86768-936d-31d1-91b2-626afe8c00de | -15.37663 | -55.84769 | 2024-10-02 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ab5f7dd-bf21-3871-939b-208b4395ba28 | -15.37634 | -55.85036 | 2024-10-02 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7dc658cc-521f-3e41-b6cd-85ec2f4e9e3b | -15.37625 | -55.85099 | 2024-10-02 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f3953d48-2a16-3ff1-b71b-64d83749acab | -15.3731 | -55.83007 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e3e27762-57a5-318e-9ccc-5a4555a25fb8 | -15.37305 | -55.82933 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eba589f7-cadd-386d-9c37-eaa48405ad75 | -15.37269 | -55.83354 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bc5f582c-c898-33eb-bd2c-0f1f98e6b71b | -15.37267 | -55.83281 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b511ff32-f115-3003-8bb1-b557787e3a03 | -15.3723 | -55.83696 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 28141949-98f3-3e88-aed7-2ae5c7cda165 | -15.3723 | -55.83624 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| eca1e6c5-5f5a-3754-8234-b61a8a741119 | -15.3712 | -55.84629 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 402c8298-c123-3d7f-954b-a6ebde49473a | -15.37114 | -55.84687 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 796e434a-da85-33be-a164-9ff1be976575 | -15.36691 | -55.83525 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c2f4611a-0a2e-335f-8484-3fea88de6e43 | -15.3669 | -55.83451 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 5d6f193b-c863-3c10-ad85-243239d337bb | -15.36653 | -55.83787 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b6f78c9c-5f67-3f49-ab92-bec98752d489 | -15.36652 | -55.83859 | 2024-10-02 05:36:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a8d3c943-8b7e-34f9-8d30-ef5ff98f45b6 | -15.3658 | -55.84458 | 2024-10-02 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9bd0b21-264a-32e7-acd5-8f5407fa058f | -15.36575 | -55.84526 | 2024-10-02 05:36:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eae66e4a-e99b-3117-b750-18f157b4a2ce | -17.09618 | -56.69756 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6fa12147-5824-3462-9beb-30f1c85e5a3b | -17.09581 | -56.70101 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ec2ffb01-dc3d-3db3-a63d-574aab936741 | -17.09198 | -56.69989 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b0272d0c-48a5-338c-afc8-e753e67b4467 | -17.09079 | -56.71024 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 94f012e1-8c18-3ea4-a8c3-e87e56464ce2 | -17.08974 | -56.70729 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 78261c9f-5461-35c7-8359-ef84452bbdfb | -17.08936 | -56.71074 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0bf6590c-d03b-3209-9bf8-cbc2f1d78bd2 | -17.08586 | -56.70618 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1415f212-3f17-3c50-aa0f-9d27d0af2a9a | -17.08546 | -56.70963 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8e233099-934f-311f-b0e8-d552a4163e1c | -17.08478 | -56.70321 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a975ec1c-e4eb-369d-bff3-45213715b149 | -17.08441 | -56.70667 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7e24e8d0-79b4-3809-90d4-3f613f3cf0d8 | -17.08053 | -56.70557 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7646ddf2-2280-3cc8-8580-25289b8a2229 | -17.07945 | -56.70258 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 231bf8f1-479e-3d1d-ae4c-5558b8dc51f6 | -17.0756 | -56.70148 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 30de413f-4698-382f-8a58-dca1a5a1623f | -17.0752 | -56.70494 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 87ce240d-ac10-3807-a7e8-528ce80bff15 | -17.07449 | -56.69846 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a79bcf29-a643-3263-93be-ad7eb6aa7f3e | -17.07412 | -56.70193 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c87c4fe9-8f1b-3df4-97b8-aea3a39a3ea8 | -17.07376 | -56.70539 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 76b214be-08fa-3dd9-869d-3a9d63f39ec3 | -17.07067 | -56.69739 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 584d2d93-b699-36ec-abe2-4b1d9db35f27 | -17.07027 | -56.70085 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| bbc6746e-2e9a-36a2-86f9-b89569ebb9d6 | -17.06988 | -56.70431 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9961c72f-e810-3ce5-8c7e-1d52e0995f1d | -17.06495 | -56.70022 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8839b739-c540-32dc-9bed-41f5de5c3bcc | -17.06456 | -56.70368 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f27425a7-fac4-3994-a0d6-676a39ef4003 | -17.06417 | -56.70712 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8b453050-395a-31c9-a520-b1243be4d605 | -17.05923 | -56.70303 | 2024-10-02 05:36:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f0fb6ddc-ba6d-357a-956b-2b058a3bc089 | -17.15973 | -56.2052 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5c4ecfe3-89dc-39fc-b104-849399941b1d | -17.15934 | -56.20889 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9db4040c-5272-30d3-bf57-a802b28729d7 | -17.15895 | -56.21258 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ec5d21ba-2d0f-3630-8c24-df541d949bb6 | -17.15895 | -56.15968 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b6d8e9ad-6dcd-37ee-a7fa-03cf69b9d3dc | -17.15856 | -56.16344 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8c9d142b-5b28-3788-9583-87f0863ea8e0 | -17.15816 | -56.16719 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 22a30d05-6571-3fa6-9bd5-ebbae74cb8ac | -17.15777 | -56.17095 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d6a6d444-13c7-3c57-8aea-ada9d8fa13f4 | -17.15659 | -56.18217 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e3ab6fb2-7284-381c-a4d4-2a297a407f76 | -17.15619 | -56.1859 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| dc2b533a-462a-3359-8761-a22f0a9b7833 | -17.1558 | -56.18964 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cb2eb526-c234-3e12-a179-f733916ad5fa | -17.15462 | -56.20083 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 55619030-f030-3c68-9b4d-16e5abb8c0d8 | -17.15423 | -56.20455 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d412be0d-cd49-326d-9ee7-9e5898186e66 | -17.15384 | -56.20823 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7fd34408-41c8-3e5c-ae29-d26027d9be88 | -17.15303 | -56.16281 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d9454323-2389-3260-9c84-058c9b13dd67 | -17.15296 | -56.16277 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| ca8f5878-e5f7-3286-a93a-49fc9ae080e0 | -17.15264 | -56.16655 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ac34ae11-1812-3d7c-99e8-2cc5d80f4cab | -17.15254 | -56.16651 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 35d8a8c6-70f4-3279-a3cc-7514a81d797f | -17.15225 | -56.1703 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9db53b85-8898-3cb8-96fe-3e2114a0151f | -17.15212 | -56.17024 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 1e939144-8078-31b5-b71a-65d3973b1a3b | -17.15186 | -56.17404 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9f159cd9-ba46-3ecc-bcd0-1f3c32daaef9 | -17.1517 | -56.17397 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 5a7ec75b-7b21-39ae-a6b8-a336ef2b61da | -17.15146 | -56.17778 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 069109b8-eab9-3c89-af30-07414d2117b3 | -17.15129 | -56.1777 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff24faf2-2bef-3528-961e-722aa9407836 | -17.15086 | -56.18144 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 5ebda4f9-f08d-3c5f-b908-09117c98eea3 | -17.14872 | -56.20385 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 37a3e332-b448-3d54-b4d5-a12ca185c566 | -17.14837 | -56.2037 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bc8bf5e6-48fd-3ad3-b344-565f2eb6d91f | -17.14833 | -56.20756 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d605f13a-46d6-37d5-9259-984fd2b765c7 | -17.14795 | -56.2074 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0c2f92b3-bf80-32cb-b79d-2a8ee48fad67 | -17.11714 | -56.23391 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f170e184-1b79-36ba-b5d0-0b9229b01312 | -17.11673 | -56.23761 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1d7804af-4bab-3b45-8864-44c3dae5bcce | -17.10941 | -56.10059 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 89f37c6c-a57e-3c67-ba33-daca01eae147 | -17.109 | -56.10437 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 6898a6ea-ab29-3da5-a1c8-ec14b1cbf264 | -17.10818 | -56.11189 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a305be37-2434-3c92-be23-66f680817ce0 | -17.10777 | -56.11566 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c4f2f731-a1f6-3c2f-890a-67219740bd9f | -17.10346 | -56.10373 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0639d41d-b46f-3d59-b53c-eccf51fa034c | -17.10305 | -56.10748 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bd0924dd-fce7-3e22-9530-6923cff62238 | -17.09792 | -56.10307 | 2024-10-02 05:36:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |


[Clique aqui para ver as próximas entradas](README176.md)
