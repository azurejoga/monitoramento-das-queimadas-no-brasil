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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80a9a84b-87c0-36a2-bf56-fb4820524b7d | -4.35848 | -45.28134 | 2024-11-19 05:08:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83475ef6-8e5a-3eb8-b08a-92f684303586 | -1.76314 | -55.22351 | 2024-11-19 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fe199ea-42f1-3777-92cb-7a54a3804ce1 | -3.38175 | -54.75896 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21fc93de-7588-3508-b358-6e4749c1a964 | -2.58745 | -53.99199 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e232e4f6-fde2-3ff1-8b07-d3cf9b21b090 | -2.59975 | -51.79843 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ce47361-44d2-3fd9-b8fb-92abac40b069 | -3.08589 | -54.66219 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b199344c-3102-3654-b416-b6c68c325268 | -1.20163 | -51.7763 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34f3540a-2ae9-34be-b093-c7a7ad7c2757 | -2.16288 | -51.96808 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4517e502-1564-3884-a7ed-e144d95cc95d | -2.59225 | -51.72398 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c99ce53a-9548-3029-a732-4689565655d2 | -1.62081 | -55.14423 | 2024-11-19 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee8b9a4b-3a6d-3bc8-a2dc-7d571d32f615 | -2.34481 | -53.909 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de319c46-3eb5-3649-9341-af10fc7ce99f | -1.13582 | -51.68045 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba89df5f-1907-3e97-80fb-7fe51d43cb65 | -4.38905 | -47.77737 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 720d7272-eebf-3507-ad9d-ba0df6f2ab77 | -3.34219 | -45.36369 | 2024-11-19 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| cda66690-895f-3990-b799-734c5ba80d29 | -1.64987 | -52.77124 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d4398bd-75cb-3f15-8863-4856ac51b6a6 | -2.28652 | -53.63737 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcc919c1-8ec7-3b67-ab80-33162c103cfe | -1.48485 | -51.16011 | 2024-11-19 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de184cce-4e17-3b5d-a8ac-5eb1e8dfd572 | -1.61798 | -52.47954 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462ec4a1-6c56-316b-8421-d5cb5c7afa97 | -0.85542 | -48.74669 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 997d605d-7e23-3ccf-aa90-6cd5f556f8e3 | -2.8997 | -53.04866 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcb7eee1-a79d-352d-97f1-6e46ba8ada67 | -0.85072 | -48.74595 | 2024-11-19 05:08:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 117e0259-4413-38b4-8e53-8d40a0eea119 | -1.36329 | -51.98687 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5697010e-ee7b-389f-8c36-8f2252d225bb | -2.55542 | -53.99099 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 859c6dd8-c09f-305f-b420-42b86bc5312b | -3.9744 | -49.91876 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2280eb5a-1fc3-381e-9d51-1824658dc077 | -3.10971 | -53.74354 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb8baaf5-4504-398b-afcb-55a4b6de841b | 0.07752 | -51.40725 | 2024-11-19 05:08:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5161befe-e36a-3138-b1e9-aeee2804ee22 | 0.63963 | -50.5771 | 2024-11-19 05:08:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10d77ab-c869-310d-861d-0b9226e87be7 | -2.82629 | -54.03865 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00afecb8-b53d-37df-a639-de2ddf7a4da7 | -2.9912 | -52.60436 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b245d230-a5f1-3e9e-8aa8-2ae8d0edf737 | -1.57793 | -55.17714 | 2024-11-19 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a2115b-80f9-3a75-be33-69ef23d93b7b | -3.84745 | -50.69658 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b182d90-6f41-3484-ab46-907c41a5cac1 | -2.95723 | -51.45491 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c4c11ef-4cc0-31b3-af2b-c2cc88b58563 | -0.14776 | -60.8694 | 2024-11-19 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea3745c-b4d9-3410-8602-e2c44d2b83fa | -2.81118 | -54.02057 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab7eaec6-4be3-3a15-bad9-66242e52874f | -2.95609 | -53.71404 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 807ab654-8612-344b-86b5-8f7f09ba29b9 | -4.19049 | -48.56362 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728b37ad-86c9-325d-841b-1251dcc5d9fc | -0.96026 | -51.72699 | 2024-11-19 05:08:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6e906eb-753b-3ee0-b192-f95c5d29d5f4 | -3.08931 | -54.66272 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3b3a2fb-02fa-3149-bf80-154df8a9918b | -1.9941 | -45.35019 | 2024-11-19 05:08:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13bbb51f-e9eb-3824-a0db-fa4bd32dbd96 | -2.96112 | -54.16436 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f2166c0-7b82-3c46-aaae-b410cf45d25a | -2.55193 | -53.99043 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a052c2b-2179-348b-9a81-5aeee5f39f56 | -3.54835 | -50.41249 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cca61702-a433-3c16-9a9e-cb4a1e4de6fc | -3.58506 | -53.72598 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 324f8123-e40f-393c-8c75-1afea904294d | -5.97306 | -45.35632 | 2024-11-19 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d2105d0-b5e9-3003-b672-1a7b11b2c13a | -2.28472 | -54.72004 | 2024-11-19 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| cf9e73c8-3ee9-3fe3-b838-0c79116240f4 | -1.43606 | -53.38054 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f88fc9c-0601-30ab-94b1-efa59cb90101 | -1.92372 | -54.06159 | 2024-11-19 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7ac66cf1-5e56-3c90-b09f-d77ad72c7a5b | -3.06 | -54.40734 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e827678a-9b49-3946-9aca-f701a39d380a | -1.62033 | -53.28892 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c249cca-886f-328c-a449-0a10f3256e35 | -3.04334 | -54.40088 | 2024-11-19 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efbedbb9-fac1-3743-8b8b-79d171971846 | -1.62394 | -52.62175 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57296306-4ea6-3279-be6c-ba67d546e672 | -1.22127 | -51.74294 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2029719-4673-316b-9a2d-0f5054588ccf | -1.62161 | -53.29589 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d831334a-2855-3551-9770-dad1eba304b7 | -3.97896 | -49.9194 | 2024-11-19 05:08:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b4fddbc-e390-3c90-b2a9-b22a26185511 | -4.3866 | -47.76739 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 630f57b5-fdc6-3bc2-83d2-70f66fa23fc4 | -1.72873 | -52.69357 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd341f32-dab2-3271-a769-097f8693de3c | -1.42379 | -51.10036 | 2024-11-19 05:08:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4ad6f5f-d79d-3bcb-ad6b-7aad74215527 | -2.89536 | -53.05245 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f6c39de-d529-3b4f-9456-2df5b08b4e21 | -1.39489 | -52.42628 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b24a80c-43da-30ac-9555-931ae7b6e02c | -1.24907 | -52.05259 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ad2f5ac2-14d0-33c3-97bf-ef43116c4f17 | -3.76295 | -52.13932 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8d6dcc4-bd20-3948-9d62-61343e1f94da | -3.23261 | -59.33462 | 2024-11-19 05:08:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d72e45d-4853-3cc5-b5c7-40d9790085c1 | -1.32788 | -51.86111 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eebadd86-e4b4-3981-b8ad-ec94dabbf568 | 1.71268 | -56.10857 | 2024-11-19 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce0c482c-18f4-3f4b-bb92-eeea43b5b686 | -1.06462 | -52.39037 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44d57e5d-b2f5-3447-94a5-aacb1f7ed827 | -1.20124 | -51.76928 | 2024-11-19 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2116c349-cea0-3931-ade9-e251c0924dba | -4.57424 | -48.0145 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ab4b4129-2096-34e1-94c6-368461b1d907 | -2.77095 | -52.60657 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bbd69bd3-081f-3f55-bacb-58327025d371 | -4.55374 | -48.00822 | 2024-11-19 05:08:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 79dbdd8b-f774-38c3-96e0-4470f12e043c | -4.06007 | -50.00565 | 2024-11-19 05:08:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe655106-e7b0-3bb3-b703-a2c5e1cd7df9 | -3.10814 | -53.70652 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30433c06-d965-39e4-9c82-014b01de1c70 | -3.47159 | -48.25286 | 2024-11-19 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba87516d-63f7-39d5-ad6e-dbe0186a102c | -1.64245 | -52.67338 | 2024-11-19 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3a318b89-7377-3a3b-bdec-2cf08361c4b3 | -3.89781 | -50.08799 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c811790-0ddd-39c0-ad30-cda0427fca17 | -1.58909 | -53.80956 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 05b861f7-6afd-3673-9423-334c3446ed78 | -3.50511 | -50.80904 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fac260e4-8214-3d18-9a57-2e08c913e233 | -3.04323 | -54.84657 | 2024-11-19 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bb6e068-d0f7-3b3c-a677-c78f47d7f61d | -3.77746 | -51.98839 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 46b03984-8812-378e-bf7a-9f5ad1a2ccea | -3.62374 | -52.2636 | 2024-11-19 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3847ad90-8c86-3b36-92c4-64c9ac2774c9 | -4.04922 | -54.37587 | 2024-11-19 05:08:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 070dca8e-3f3a-3631-88a1-047778b824e9 | -2.95192 | -53.71748 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f32f5101-de7d-3155-b7a7-13eec9b719e2 | -4.10673 | -51.04376 | 2024-11-19 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4f458ac-6587-3bad-9f04-4794df5be3d6 | -2.95129 | -53.72145 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72067e62-56d4-3ee6-bcb2-e165a2517648 | -4.39436 | -47.77818 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88101534-79c3-378a-abc1-ebf2c17646a1 | -1.90225 | -53.32879 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 390c6d14-032e-3b82-971a-0f8073866535 | -3.60029 | -53.99651 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ddad44f-71ed-3d20-b26f-feae84507187 | -1.78811 | -53.59647 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eb00fc0-ba8e-339b-b518-14c0ee3ef347 | -2.76412 | -52.60105 | 2024-11-19 05:08:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a5a9a69c-05c9-3afe-ba03-013c2cc8b4c5 | -2.53936 | -47.3324 | 2024-11-19 05:08:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2491157d-5f2f-31c6-bbfa-a3dfe6d557c3 | -2.85416 | -51.58495 | 2024-11-19 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c90d449e-8d49-32e0-838b-4d99bf20a19b | -2.86875 | -51.79158 | 2024-11-19 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 389e3f61-a754-36be-a3d2-2f21278e4818 | -3.10736 | -53.10326 | 2024-11-19 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c5e5f8cb-042b-3893-8d91-6935e8b3d777 | -0.82758 | -52.8368 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e166ba06-5df7-3f22-a924-2d7a69e4e2b9 | -4.39194 | -47.76803 | 2024-11-19 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebe37779-56d8-30e5-ba28-99a015e0d86b | -3.39509 | -54.27161 | 2024-11-19 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce5d8f67-bfe7-3bf0-82cb-f8adbaab1f98 | -1.62328 | -53.2934 | 2024-11-19 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5cf767d-d1a4-3668-beed-0d5d75d5d920 | -1.76431 | -53.51733 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a650232-21f1-30a4-bc59-4de523a4441c | -2.79789 | -54.00751 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1cd796d-e17f-3e3e-8b0b-1f1c5f041bc1 | -2.83804 | -54.00887 | 2024-11-19 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e20023a-4a33-3c74-af69-616be0e72048 | -2.65739 | -51.68398 | 2024-11-19 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README44.md)
