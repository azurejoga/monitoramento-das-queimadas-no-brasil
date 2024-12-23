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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53d4c054-f503-35fa-ab9b-18b7d169b22c | -3.8409 | -46.679199 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ea500d9-6aac-35fa-b8bb-b19cc20226ca | -4.1704 | -43.640499 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a10df740-b503-335d-9327-f3feac364e07 | -4.0317 | -46.792999 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b3547ece-aa9a-32b1-b53c-bc75f0f23eae | -4.1632 | -43.6534 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 804d8e30-ce81-3aaa-8956-d4517e1921cc | -3.9147 | -46.912399 | 2024-12-23 00:24:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef7a37f7-e1c6-31db-8110-b6081e2e76e9 | -4.1827 | -43.648899 | 2024-12-23 00:24:00 | METOP-B | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f82ccc0-33a5-3629-8a8f-3f7c379913ac | -4.9342 | -41.339901 | 2024-12-23 00:24:00 | METOP-B | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1079b4af-e3e8-3147-b308-ab081e9ad341 | -1.3653 | -53.6987 | 2024-12-23 00:24:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21e47fa7-4fa4-39a5-8668-6b9f000e4384 | -4.7725 | -46.381599 | 2024-12-23 00:24:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4158cf89-73f7-323e-a07e-e7d72029e84a | -4.2386 | -46.931999 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b66ce8c1-426c-3f11-822c-8dba032166be | -4.3771 | -43.997501 | 2024-12-23 00:24:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4283df51-ad8a-3083-b34a-0ad171d85c35 | -0.3621 | -50.063 | 2024-12-23 00:24:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6a4f103-e18f-36fc-9f59-ec51e5d217c7 | -1.7401 | -52.573601 | 2024-12-23 00:24:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaa96465-4aee-3a39-aa72-6e88882e2cba | -4.0841 | -46.7967 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8cffa1b9-440d-3ac2-a140-ff0e3fd039e7 | -3.9888 | -46.7402 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2533e9f1-7d1a-33e3-a1a4-d317aad9bdbb | -4.0473 | -46.409698 | 2024-12-23 00:24:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e1193eaf-e126-39fa-9cc3-6883d038be15 | -3.25328 | -48.06545 | 2024-12-23 00:26:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f851fc4a-047d-3251-b60a-0dc8c4de0ac4 | -2.36893 | -45.91953 | 2024-12-23 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| bc3c6d06-bb81-384f-9205-5a62c359fad2 | -2.26008 | -46.39761 | 2024-12-23 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 581465a2-27be-3f59-8467-3ed765ccc857 | -2.36734 | -45.90764 | 2024-12-23 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 65c5d522-8f20-366d-9e6a-583c9b0b90bd | -2.21147 | -45.58869 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| bf617c29-9779-3551-b5da-9116e325a423 | -2.34527 | -45.59263 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b546428-be8a-370a-be05-6b42b2451840 | -2.2099 | -45.57747 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2b4e6c3-cdbb-321b-8a9b-6ae093a0d7c8 | -2.11785 | -45.50521 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7e5258b8-47ce-3ddc-91f6-f5d3be8610f3 | -2.62567 | -48.64922 | 2024-12-23 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e97d35c6-7a2a-34aa-97ed-56c9cc872040 | -2.26887 | -46.38339 | 2024-12-23 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8c37e4be-5d9b-3d38-a534-73baa18982fd | -2.65099 | -46.10204 | 2024-12-23 00:26:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5456989e-04d7-3656-b313-b0e1db15c528 | -1.63386 | -45.84426 | 2024-12-23 00:26:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6c1a9622-1835-31c0-9a67-2add4d03d5ec | -2.6485 | -45.71877 | 2024-12-23 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a91a7c1a-23b0-37ec-8802-8fab2281581b | -2.56553 | -45.56148 | 2024-12-23 00:26:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| debc6714-d264-3857-aeac-410ac528ff03 | -2.64377 | -45.68403 | 2024-12-23 00:26:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2e9a4572-7808-3cab-a080-9203bcdf5b6d | -1.68352 | -45.90773 | 2024-12-23 00:26:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2d68ba02-90c7-39a8-b61a-6da8cc832061 | -3.00043 | -48.13509 | 2024-12-23 00:26:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| a19ba086-d120-3445-b045-1ae44e1114cc | -2.08354 | -45.33159 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a276f001-b964-3bef-ad06-84b9926f2d11 | -1.72946 | -52.58085 | 2024-12-23 00:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 7a8925f6-33ee-3cb1-bb09-eee279eef840 | -2.36953 | -45.91302 | 2024-12-23 00:26:00 | TERRA_M-M | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b08aae23-c087-3362-ae6d-ea01d50772af | -1.63541 | -45.85571 | 2024-12-23 00:26:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e8863688-9769-3b74-b7a0-d5e8e30ebdc1 | -2.33379 | -45.5827 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| abcfd085-c2f8-3e92-b008-66693d1de149 | -2.63528 | -45.697 | 2024-12-23 00:26:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 80fff722-fa4b-30fc-9124-48b4f39fb03f | -2.06178 | -45.38995 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f0d5482-09aa-38cd-aace-0f5c9362963a | -2.62304 | -48.63018 | 2024-12-23 00:26:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| a6234688-79c7-3607-9525-ad417de810d9 | -2.1163 | -45.49413 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b80719cd-e4e9-312a-bd6b-ca72a055e834 | -2.63371 | -45.68544 | 2024-12-23 00:26:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e2c25b3b-858e-385c-998f-0e663d956486 | -2.9583 | -45.74167 | 2024-12-23 00:26:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 402d78e2-bd6b-31a8-9df0-2d95ac509641 | -2.2706 | -46.39615 | 2024-12-23 00:26:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 892b922b-14ba-3a19-b7c3-a23f0ba8a274 | -2.34374 | -45.58133 | 2024-12-23 00:26:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 294e866f-35be-3e45-8110-b384183c337e | -4.16 | -43.64 | 2024-12-23 01:00:00 | MSG-03 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b2b12e2b-9374-3c3b-8d41-490c06639271 | -3.0998 | -54.597401 | 2024-12-23 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d002a40-955c-3cc5-b1a9-19f38b9179cc | -1.7389 | -52.573101 | 2024-12-23 01:22:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56aa4391-a99a-326c-800b-344fcbc4e758 | -1.6709 | -52.067699 | 2024-12-23 01:22:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0f16a4c-c87a-3605-a7f7-c04b36fcf4a1 | -3.1066 | -54.539299 | 2024-12-23 01:22:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9fbcdc-89f4-3d95-bdf3-6207f2e4df0c | -1.667 | -52.051102 | 2024-12-23 01:22:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4517115-75a6-3683-b971-21a2b1a8f79c | -1.0695 | -53.612099 | 2024-12-23 01:22:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 367bfdfa-5b39-3055-881f-2f57aa50bb72 | -2.4136 | -53.737202 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12b50677-a909-30fb-8cfb-0d76ab8dd360 | -1.3664 | -53.696499 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1075ae8f-d1dd-3525-bbfe-b5fcdf7b2ffb | -1.3695 | -53.7094 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 524a32e6-7316-336c-8f17-b5fd193afc02 | -1.3597 | -53.711601 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa22fe4-82f0-3095-8c22-8818400eadaa | -1.3566 | -53.6987 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63009296-b796-3f89-8ce0-54aefd4e5cbc | -1.3634 | -53.683498 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff1c269d-6c65-3cca-b330-511419dbeadc | 0.6474 | -59.734901 | 2024-12-23 01:22:00 | METOP-C | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d1f44277-e6d5-3390-a2e9-027d3bd9a7f4 | 4.1089 | -60.6511 | 2024-12-23 01:22:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 91afad4f-9e97-374b-a872-787566fcca33 | -1.3761 | -53.694302 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b15d894a-114f-3016-b641-e464b627c0eb | -1.7425 | -52.588402 | 2024-12-23 01:22:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe150f8-bae6-34ab-ade4-3b5344982168 | -2.4039 | -53.739399 | 2024-12-23 01:22:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26d28f17-25a5-3d6c-86da-12276a83d676 | 4.11505 | -60.65965 | 2024-12-23 02:06:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 4245c313-2c6e-3275-b2ce-4844032e00a1 | -9.30951 | -36.02855 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 2dd4b9ed-65be-3ede-a685-51685fed013c | -8.91189 | -35.98281 | 2024-12-23 02:51:00 | NPP-375D | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a4daaba7-17b7-3dc0-8c71-0b4502d09310 | -9.31065 | -36.02274 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4d677715-1ef0-3913-8f64-f262414e630e | -9.31503 | -36.03564 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3a8466b4-8ee2-354c-85fc-1a1a38ff429b | -9.3173 | -36.02405 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9eec87a2-720b-3ec8-87d3-56a2fdc43b07 | -9.31287 | -36.01142 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 6593a95a-aa57-37a0-8853-c0a1b7b2d042 | -9.31177 | -36.01703 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 4e2e04d7-8007-34be-af0c-021ebe7adf5c | -9.30837 | -36.03436 | 2024-12-23 02:51:00 | NPP-375D | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4777954e-afbe-38d8-8229-e9dabcd47ee3 | -9.31842 | -36.01831 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 322d281d-1045-3324-a2be-0af7afabc4d9 | -9.31404 | -36.0055 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6ca56700-3c2e-3a3c-929f-d89e9b1c236b | -8.91301 | -35.97703 | 2024-12-23 02:51:00 | NPP-375D | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d1edc9c1-0966-3fac-91e1-facb7a113077 | -9.31953 | -36.01261 | 2024-12-23 02:51:00 | NPP-375D | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| d2cb7554-2e29-387d-9f88-17b245a0adda | -16.85848 | -39.2439 | 2024-12-23 02:55:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 038f1f3c-192a-390b-ae36-326347b9641b | -16.85147 | -39.24239 | 2024-12-23 02:55:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 752b95c2-ace6-3620-a779-84d86e4c3318 | -7.8833 | -35.24922 | 2024-12-23 03:14:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59c84c49-b533-364c-ad9a-7f9ba7d47150 | -7.02157 | -35.16237 | 2024-12-23 03:14:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b333bca-c920-3f18-b50d-492f410143a2 | -4.87034 | -37.82354 | 2024-12-23 03:14:00 | NOAA-20 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| eb7e210f-29ee-3ce4-b608-2ed16c35c9ce | -7.40452 | -35.2449 | 2024-12-23 03:14:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a01c5401-fa69-390a-ae6e-34e8edbefaa7 | -7.51324 | -35.19052 | 2024-12-23 03:14:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 630dbbf4-c15c-3d9b-a474-07fda01978a3 | -6.96927 | -35.22929 | 2024-12-23 03:14:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 359bd356-d3fe-3df4-9e48-447d59caf97c | -5.82052 | -35.48321 | 2024-12-23 03:14:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 380a4145-b6e7-3d28-b819-2df41cdfafe7 | -5.33991 | -39.76254 | 2024-12-23 03:14:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 42f30f39-8739-3fc3-9d90-cb3dc7297e49 | -5.82507 | -35.48402 | 2024-12-23 03:14:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 557e219d-62fc-3ff0-b1c6-02fd42368c38 | -7.82465 | -35.1925 | 2024-12-23 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4a204610-29e6-3cca-8949-f1ee19818533 | -7.88258 | -35.25334 | 2024-12-23 03:14:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7ba2e4e1-3187-3d04-8efd-81358b5c7d5e | -7.91434 | -35.22449 | 2024-12-23 03:14:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7588afd4-1e8c-3c61-90dd-13d37b2f3acd | -5.33927 | -39.76394 | 2024-12-23 03:14:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df799486-14ea-3de4-a116-b59dc3ae94f2 | -7.23867 | -37.44122 | 2024-12-23 03:14:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71d69103-8e1b-35d5-b848-d9aaccd43532 | -5.34009 | -39.75922 | 2024-12-23 03:14:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4bf4403e-090f-356f-9d42-5ea5c9eb68a5 | -7.8219 | -35.23462 | 2024-12-23 03:14:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3d98341b-94ec-3123-a1cb-d127dc6c0eb4 | -7.52833 | -35.15418 | 2024-12-23 03:14:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7aa985a0-1272-327e-97b2-fce51b794240 | -7.40522 | -35.24072 | 2024-12-23 03:14:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8d5bd850-9d10-37f7-91c9-900394ab576e | -7.87898 | -35.24837 | 2024-12-23 03:14:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| a05dd014-22ae-31e2-ab81-af5b7ce59770 | -5.24377 | -36.18736 | 2024-12-23 03:14:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2147e988-4232-3cfa-9320-c7a7bfa4fe98 | -6.04943 | -39.43775 | 2024-12-23 03:14:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
