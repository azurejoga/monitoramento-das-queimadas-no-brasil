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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a724f3c6-6c94-3701-9962-3b2412862f8d | -3.0 | -54.1287 | 2026-10-06 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| db850c0a-3fe2-323c-aba3-c1eec7b7b70f | -3.0932 | -53.7239 | 2026-10-06 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2780f72d-963b-38a5-9ade-76eec4b96358 | -3.4943 | -54.6367 | 2026-10-06 04:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 0bdf9853-0358-3b96-9078-44a7776e7c82 | -3.0375 | -53.8865 | 2026-10-06 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 571f41af-e811-3484-90dc-0e46f504b264 | -9.0231 | -65.7169 | 2026-10-06 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| eecb082b-e9ae-3b47-abb3-76ea63bbf4cd | -2.8713 | -54.1518 | 2026-10-06 04:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b1aecd0b-1986-3ea1-a40b-409bd2ed7a8d | -3.6731 | -55.9622 | 2026-10-06 04:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 69a7a3a1-9c98-39e8-b171-35809f9577ea | -3.0732 | -54.2273 | 2026-10-06 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 83b0e14f-56a3-3588-b785-2e0b5ef1c52d | -3.6732 | -55.9425 | 2026-10-06 04:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7caaa755-5cce-3cd8-909e-f7810b57574f | -3.0915 | -54.2469 | 2026-10-06 04:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| a8aa2987-0e2e-3ebc-ae76-cb11cfe94af9 | -3.0191 | -53.9071 | 2026-10-06 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f1a04777-0a6a-344d-af43-9e7266e3b3da | -2.9448 | -54.1501 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 25d0c610-a86a-3168-8f8f-b77db2959759 | -3.1115 | -53.7637 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 3d5d4a20-c270-31bd-9d46-9bcd4ad18cc9 | -2.8713 | -54.1518 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 26de4be6-47d3-35c8-9481-32a8f73a436f | -3.6731 | -55.9622 | 2026-10-06 04:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 6829104b-d033-3c6e-9ae5-066ea90bfcac | -3.0932 | -53.7441 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| ae8a12ac-7ce8-35b9-9f6e-435cb8f77c5b | -3.0548 | -54.2277 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| cc0e503d-150c-378f-b485-39711e687688 | -3.0917 | -54.1666 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 79e86954-1283-3191-b8e4-e0b400d24eaa | -3.6732 | -55.9425 | 2026-10-06 04:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a506286d-e56f-3220-90eb-d54a64e35aa2 | -2.9449 | -54.13 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ed6fbd94-50bc-3a06-94a7-717b59f90404 | -3.0191 | -53.9071 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4ed651f0-001d-3567-8361-7fa405984b43 | -5.8323 | -45.0105 | 2026-10-06 04:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9c762c46-74d2-39d3-9ada-7efee72aa884 | -3.0932 | -53.7239 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c4e07d08-410e-39a3-9ffe-ab95ed5d4bb4 | -5.8511 | -45.0091 | 2026-10-06 04:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| b9bcc163-1911-37c9-b7f7-ec9aed53e4d5 | -2.8714 | -54.1318 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 52a4b0f0-fdf2-34be-9229-3a8dda401c80 | -3.0375 | -53.9066 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| dced3e32-02ad-34e3-a78c-089f0c503709 | -3.0375 | -53.8865 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| be948842-f326-3a93-94f5-2cfad7804046 | -3.0192 | -53.887 | 2026-10-06 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| e9395024-a6b0-3d13-80cb-d1d048161c8b | -3.0734 | -54.167 | 2026-10-06 04:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| da5459d7-5056-31a8-8985-27f4c5451698 | 2.4585 | -50.8299 | 2026-10-06 04:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a6bd2efd-fd20-3ef3-af0b-ddff89397071 | -11.29 | -45.49 | 2026-10-06 04:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52df27a6-2224-35c3-bf55-45e6548bb942 | -11.29 | -45.54 | 2026-10-06 04:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 127f361b-099a-3d21-bbf5-bf045a6a099a | -11.26 | -45.48 | 2026-10-06 04:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e38de87b-e489-3aea-8975-2cb5762f18dc | -11.26 | -45.53 | 2026-10-06 04:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0debb3eb-78bd-3c81-aae1-7acdaf695a2d | -3.93867 | -42.99342 | 2026-10-06 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 197ba6c4-cee6-3ad4-936e-20a6bd842a2c | -3.07157 | -44.45533 | 2026-10-06 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf227c8d-1a2d-3fc7-a2d9-613a35422362 | -3.28165 | -42.26212 | 2026-10-06 04:17:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6c24083-5af6-3aba-b01c-fb9836326101 | 0.29353 | -51.08708 | 2026-10-06 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 487741ff-529a-3f4d-a874-680f3ed77381 | -2.70102 | -49.03489 | 2026-10-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9822fce5-4c4b-3662-96ad-e2b2439c8cdc | -2.70562 | -49.03874 | 2026-10-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6373885-a389-3402-8e0b-d29e201aa430 | -0.99599 | -47.65831 | 2026-10-06 04:17:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a79e92a2-58df-33ef-b399-c403aaba2321 | -1.08499 | -54.11798 | 2026-10-06 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9b473c6-7fff-3237-b1f7-988f333af263 | -3.93521 | -42.99287 | 2026-10-06 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7313af06-31c3-33d0-84ba-fc9d45b046a9 | -2.1798 | -48.13845 | 2026-10-06 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddfde77f-952c-3636-ab60-1da4022481a3 | -3.33649 | -44.584 | 2026-10-06 04:17:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe00c5f5-e5e7-3b06-b40b-e491ebb9bf13 | -2.68516 | -49.03534 | 2026-10-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96408234-710e-3b51-9a41-3a8e3e370610 | -3.33272 | -44.5834 | 2026-10-06 04:17:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 978f94d4-c653-3c91-994d-b4c43c343e09 | -3.28223 | -42.2585 | 2026-10-06 04:17:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f35d41bb-b947-3cb1-845a-c217242bca3f | -3.97073 | -41.55282 | 2026-10-06 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5d50fd8-18cb-393e-bb85-95f0c665e94e | -3.71228 | -40.34668 | 2026-10-06 04:17:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 858ab44f-a924-3013-a5a2-1da527afbc07 | -0.94498 | -47.55317 | 2026-10-06 04:17:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36a8e3b3-dda8-33a7-894c-d295b731626b | -3.39166 | -44.48215 | 2026-10-06 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3c7c524-0218-3df2-8723-623e4f600b26 | -1.09218 | -54.11928 | 2026-10-06 04:17:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37cc850f-f348-328e-9260-14ed57c57d34 | -3.29185 | -42.26372 | 2026-10-06 04:17:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cee18d20-ed42-37b7-93d8-bb920abfec1d | -3.96795 | -41.5488 | 2026-10-06 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5455d53e-cc62-3002-9266-e9350e4b2202 | -0.94023 | -47.55242 | 2026-10-06 04:17:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58db149b-0307-3e2e-a346-db9853174432 | -1.69847 | -45.79012 | 2026-10-06 04:17:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7617aa75-af97-3305-a264-516a63c7897d | -3.3744 | -42.50895 | 2026-10-06 04:17:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24677c70-30fd-3529-8981-89f42ba3bced | -3.39915 | -44.48336 | 2026-10-06 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 23059105-8cf9-3b4d-88f6-3957ee6ca86a | -3.93929 | -42.98965 | 2026-10-06 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56afd53e-5857-3e8b-89bd-8f834212a5bc | -1.69787 | -45.79385 | 2026-10-06 04:17:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95383591-1ad6-3368-ac2c-5752cf428c0e | 0.29965 | -51.08604 | 2026-10-06 04:17:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46db46a5-28f9-3d38-b9ba-de1352bf9b58 | -3.96127 | -41.54774 | 2026-10-06 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 07f6aa8c-47be-35f3-9434-e40e98263da7 | -2.98534 | -48.59117 | 2026-10-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 38910582-36cd-3b21-898e-edaf80faf9fe | -3.07532 | -44.45594 | 2026-10-06 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3da0a73-ff6c-3c15-8f00-76e767721e99 | -3.39238 | -44.4777 | 2026-10-06 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 297101fb-2619-34e3-8c5b-f517b4ae9d8e | -3.3954 | -44.48274 | 2026-10-06 04:17:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22f91cce-9c43-30cf-bc4e-f2db566a7673 | -3.96163 | -43.16117 | 2026-10-06 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb2aef75-bc1a-3e41-9f37-92386ef6c424 | -2.98583 | -48.59209 | 2026-10-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82b933bc-59a6-30a4-b3a5-7e9d74ac056d | -3.77472 | -41.59653 | 2026-10-06 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a63947c2-e6a6-3473-8528-54e81dfbe6ae | -2.83967 | -48.8518 | 2026-10-06 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24c3f743-dcd3-3906-bfea-1059f889698f | -3.93582 | -42.98909 | 2026-10-06 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ac489c7-c1c7-364f-8b58-a9f918cdbc4d | -1.6943 | -45.78946 | 2026-10-06 04:17:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6053e359-922e-37f1-9f50-65077f07e4e2 | -3.24111 | -43.22487 | 2026-10-06 04:17:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b3071fa-f1dc-34ef-b48f-b87ebdcf70c9 | -3.07908 | -44.45655 | 2026-10-06 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c6126c6-763a-39d4-8ac1-d418d8d0d478 | -2.70051 | -49.03788 | 2026-10-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bb2b038e-c222-3267-b01f-7ea8b31ce061 | -2.59605 | -47.35104 | 2026-10-06 04:17:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12ef046c-d95d-30d4-b8ab-0fb94d6097cb | -3.77806 | -41.59706 | 2026-10-06 04:17:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 6d044e48-69ce-3013-8cdc-6f802705f387 | -3.0746 | -44.46042 | 2026-10-06 04:17:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57339c32-f1e6-3ec8-a2e1-19622d2f709d | -3.07711 | -54.1855 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00c30004-e7d6-377b-94c7-247bca323346 | -2.9218 | -54.11077 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a83184bb-ecb5-35d6-9398-bb39429452fb | -6.1774 | -44.28837 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c298075d-50e0-3f8a-9454-cd204840a297 | -2.92392 | -54.12331 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f572ffc3-e50c-39ed-85f5-6cff81e5401d | -6.71391 | -45.97754 | 2026-10-06 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f816df1-e17a-3201-a86c-9e1ed713befd | -3.22665 | -53.88517 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16e6c3f4-5f05-3c58-812b-24bbad13dda3 | -4.10978 | -49.39754 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2df8f141-62f1-3ded-bfe9-6f98f8bbbf70 | -3.0858 | -54.15932 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68d611ed-b22f-3aad-b3af-ea947c70723d | -2.87575 | -54.15006 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4d2c8cf6-d182-3ca0-baa4-a9530623aecd | -9.88364 | -44.80118 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5840b7b-fc30-3673-9613-feafc9d5d992 | -6.49165 | -46.08474 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fe24ade-60b6-3fc0-9f5d-5e3d197b09e2 | -6.61702 | -41.56973 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1d11820a-9a10-3b9b-aa4d-0ef677803ad4 | -6.18485 | -44.85483 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cca73a36-2f43-306d-8b86-9ed85f01a58c | -6.32026 | -43.34643 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f9339e0-a282-3dd6-86a2-66deced6e418 | -5.07784 | -45.17332 | 2026-10-06 04:19:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94aba1eb-edd3-3668-8289-e9bd66014523 | -11.27236 | -45.52687 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 0207ede6-c886-3524-9c70-eb617b780f7a | -2.99865 | -54.13744 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44d138cd-25b3-325a-a981-ed3be2df81ff | -7.41263 | -46.7898 | 2026-10-06 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d83134a1-b49e-338d-8870-63604e25f5f0 | -3.27772 | -54.18909 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6e3e5122-8889-34ac-a31f-4e7edd632cf9 | -9.87176 | -44.80732 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e92549e-b953-30a9-8425-535453a4590b | -3.06951 | -54.16943 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README25.md)
