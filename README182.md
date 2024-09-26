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

## Dados Diários - Página 182

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70e4a9ab-7a28-3f55-9e1e-a39e2d6d5359 | -10.90168 | -57.41169 | 2024-09-26 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| a40eaf50-e04f-3b5c-9a89-faa98968dfdc | -10.89143 | -57.4101 | 2024-09-26 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| c42064c9-1f70-3495-af28-b085b0a9c36f | -10.88959 | -57.4219 | 2024-09-26 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 337897ef-88d5-3e97-8718-c8c9bd95ff20 | -6.85172 | -59.00875 | 2024-09-26 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 27072f28-1229-3cc0-95e3-db334b626f3d | -6.77173 | -58.69485 | 2024-09-26 13:08:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c3beaebe-3fd2-3653-b9cf-e1bb4a9c8b69 | -6.70764 | -58.91708 | 2024-09-26 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 23a9cd52-7c95-360a-ba0c-5aa502aedb90 | -6.68029 | -58.57888 | 2024-09-26 13:08:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 8eb47500-d4db-3286-a8b7-2071dee04aa2 | -8.78042 | -58.16198 | 2024-09-26 13:08:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 36ddd335-433d-303c-b641-05dc3bb8ea5c | -8.77963 | -58.16779 | 2024-09-26 13:08:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| ab6dc24f-d00a-3c07-8217-92e26930dcaf | -8.77819 | -58.17645 | 2024-09-26 13:08:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d7590cd1-b2c1-3140-b008-35d2a1a11e5d | -8.7332 | -58.16939 | 2024-09-26 13:08:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 305a6195-1fda-39d1-a90a-fb4773f231a4 | -6.80364 | -59.31295 | 2024-09-26 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 1a431fec-72e7-32c6-b654-8a1b87aea947 | -6.79087 | -59.31094 | 2024-09-26 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| af1bea14-41c9-3806-8046-650881683121 | -6.59461 | -59.90644 | 2024-09-26 13:08:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 472e99d2-bf88-3b89-8f12-6689a7c2edba | -6.58883 | -59.91254 | 2024-09-26 13:08:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 9aa89c18-ee42-3e52-9586-5b3e86f352c6 | -6.58435 | -60.02629 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2fd79cba-6c73-308f-b070-aab433f32486 | -6.58069 | -60.04902 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 16db3e8f-a011-3fe4-aafc-a7bfa452a98d | -6.57394 | -60.04108 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| c20c71a0-64a1-3b43-8f2d-b4c5453eb5c3 | -7.27295 | -59.50042 | 2024-09-26 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 9fd04adb-fc8c-3d95-af79-1fbf59d21ab8 | -7.19825 | -60.65199 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 16c3f6ac-f201-3762-a6b8-7af3bf22eac5 | -7.19783 | -60.68389 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.3 |
| e6b4b262-31ea-3f54-afb4-795d5bd1a337 | -7.19443 | -60.67629 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 0afcbbbe-818b-30d7-801d-531c9cf6162e | -7.0912 | -59.23856 | 2024-09-26 13:08:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 63f4ea97-d1db-3078-b636-16307a03e0e1 | -9.24052 | -60.50311 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| ededa8c9-39bf-3e10-a5ea-9ba262985c21 | -9.05375 | -60.43656 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| ff1435c9-d0c5-3937-9b13-42449d91c759 | -9.0519 | -60.42087 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| db192ce6-fca1-3fb0-a6a7-758822be30ec | -9.04822 | -60.4426 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 336fec96-163b-320a-be0c-c2e9c0877352 | -10.71228 | -60.72351 | 2024-09-26 13:08:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 85585e5d-eca5-3d8a-a063-bc18d35ad3fb | -9.58349 | -59.75814 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 39e08600-d0e5-3bfc-9578-2dd5af285272 | -9.58038 | -59.77714 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 9815099c-37d0-3251-a8ab-cbcb08177685 | -7.99603 | -61.21236 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 875114e5-b448-3aa1-a6d1-ec0b18bff675 | -7.29625 | -61.10861 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ff66a226-b8e5-3cb3-8fd1-2cb7acd38532 | -7.29558 | -61.10125 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 5b5fa2b1-8c2d-389b-87b3-1552bcccfacf | -9.12616 | -61.32341 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| de0062b5-1c35-3a3b-ab33-80e30dcdb0bc | -9.12181 | -61.34922 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 8406d2f5-9c08-3b90-be68-84ee42f43b29 | -9.11992 | -61.34189 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| dbfd9e62-506d-3a00-9e7d-a5871cb6d4ea | -9.11181 | -61.32101 | 2024-09-26 13:08:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3a0c89a3-1364-3ae1-80bd-b345814a82ae | -8.22541 | -61.49168 | 2024-09-26 13:08:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 8c1dfc82-9e15-322c-a8e1-e59f00051ef7 | -8.22507 | -61.49786 | 2024-09-26 13:08:00 | TERRA_M-T | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 3046b138-383c-3187-9883-211715d4b5a2 | -6.93759 | -63.12 | 2024-09-26 13:08:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f2e6116c-e8a2-3b11-9a71-0b5e9d8064b0 | -6.93529 | -63.112 | 2024-09-26 13:08:00 | TERRA_M-T | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| d1106138-8d67-3b59-9b31-bfb00abb5d94 | -12.9666 | -44.71614 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 8352992c-a35a-3205-9839-05eb71bd5212 | -7.85044 | -44.91491 | 2024-09-26 13:08:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 81fd4a27-f7fd-3255-9abe-aa76eccceeb3 | -7.48352 | -43.8801 | 2024-09-26 13:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 9220dc01-b6b3-369b-b76d-c9aaad96405c | -7.47615 | -43.88471 | 2024-09-26 13:08:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| d5c61529-8b21-306d-a0f6-5f89671aa4bf | -7.36569 | -44.09108 | 2024-09-26 13:08:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 56f4a2ac-cdb0-3b28-a3a3-21b1f5c4daaa | -7.35968 | -44.09724 | 2024-09-26 13:08:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 436d6dd0-c495-3855-bb6e-d77cfa7488fa | -10.65604 | -45.91722 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| d27d852d-4315-3829-9733-a674bf6d3e18 | -10.65314 | -45.91156 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 40a183b0-ec1d-3fdb-9fba-d08a50c6c1b6 | -10.64502 | -45.8576 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| d4d776f0-4f91-3e3c-828c-8f30997a3703 | -10.64185 | -45.88412 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f0738f2b-49bc-3e1d-8aa2-e4c5dfbd4f05 | -10.63875 | -45.90998 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e560aedd-3360-300d-ad42-f87a8c5b7082 | -12.24882 | -45.47163 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| ecdaf09e-50c3-3149-9c30-a315648ec922 | -12.24618 | -45.47776 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 144.2 |
| e28f60c9-4d40-32d6-8bee-61f65ccb2301 | -12.24543 | -45.50118 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 616.6 |
| 7de71023-d568-3c46-b9c5-da5e2b2b47c1 | -12.24301 | -45.5074 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 552.6 |
| 4d16a91a-09ce-32f9-bd0f-837aea45df3a | -12.23361 | -45.46965 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 161f4357-f578-3085-b2c5-c2c9563f70b4 | -12.23025 | -45.49928 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 454.1 |
| 37329395-b4ab-3660-ac1f-ad5f51241f56 | -12.21843 | -45.46747 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 102.5 |
| ab1eb60e-86ba-3271-b353-a23957037a69 | -12.21507 | -45.49742 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 910.6 |
| 1f7d411a-f84d-3fff-8ef7-463571a283ec | -11.96795 | -45.17036 | 2024-09-26 13:08:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 767bd28e-b060-3bea-a228-65ec2db5e3f2 | -11.2523 | -46.10289 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 849ce78b-6ff3-3668-88b5-4cad9025f5d4 | -11.20389 | -46.0193 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| d232d6f2-27c1-3fa0-a81f-8b75f871e066 | -11.20108 | -46.01337 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 200.2 |
| 31465cc8-6e88-3808-87d4-dd905a89ca1f | -11.18956 | -46.01714 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| 4a210c30-ac72-3c41-845d-bdfa50fc0b22 | -11.18674 | -46.01134 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 5135f51b-5e08-3709-a94a-2176c3336592 | -10.84262 | -45.87185 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 61b14c77-8ccc-3cb6-be77-c9bd8c695689 | -10.84056 | -45.86588 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a2b32fc1-ac7d-3d47-a57a-a40326142963 | -10.83737 | -45.89241 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 39b13903-d325-356f-b7c9-b534d2f2e27b | -10.83424 | -45.91842 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.4 |
| 0ec4c074-4433-3029-a174-57a2826ed096 | -10.81993 | -45.91589 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.5 |
| cd61782d-195b-389d-a341-749e42645c4a | -12.72331 | -45.55584 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 538.9 |
| ef262fe7-84d8-3f1c-b4ea-23eae1541a56 | -12.72091 | -45.56109 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 650.0 |
| f2d7558a-9beb-356b-b4f6-b89031fa6a71 | -12.71988 | -45.58545 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 460.2 |
| 50d60749-a80c-389a-a922-ffde522bdb8f | -12.71771 | -45.59067 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 229.1 |
| 7e1cb25b-14fd-3a10-9090-55a80f89761b | -6.5318 | -45.52894 | 2024-09-26 13:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| e0f5cf76-bba7-3fa3-892d-67a4e230acd3 | -6.52604 | -45.52277 | 2024-09-26 13:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 4fabe82e-f97d-327b-bd47-77eed95aa94b | -6.52288 | -45.54659 | 2024-09-26 13:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 6b8fbef7-6955-36f5-9335-7d2339740e95 | -6.7666 | -45.19229 | 2024-09-26 13:08:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| ab8c08ad-5cb4-3195-90aa-f952d6d3293c | -8.4264 | -45.67035 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| cda313c3-5e7d-3610-97ae-d345917bf75d | -8.41943 | -45.68782 | 2024-09-26 13:08:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.1 |
| d2bc4964-8e7f-3dc0-a8a1-bcdcebd1afa5 | -10.72109 | -47.37088 | 2024-09-26 13:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| bc8c272d-2165-3f85-9a25-aa2412bb235a | -10.71867 | -47.39061 | 2024-09-26 13:08:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 807d880e-7511-3b2a-8aa8-348b4919ae35 | -10.2129 | -46.18869 | 2024-09-26 13:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 44481930-7691-3b3e-97fc-63ae55acfc4c | -10.20778 | -46.18127 | 2024-09-26 13:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 158edcc9-d280-3ec6-9577-59fe23c6497b | -10.20482 | -46.20468 | 2024-09-26 13:08:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.6 |
| ed91b706-849f-34dd-bf10-c0587336970d | -10.20464 | -46.13872 | 2024-09-26 13:08:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 4d2b6216-f654-3394-86a7-e2f65c559cc8 | -10.19988 | -46.13118 | 2024-09-26 13:08:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c61f0ffb-91e1-39da-8ec1-5c45ba27ffe8 | -10.19068 | -46.13649 | 2024-09-26 13:08:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| c608d9b0-b204-300f-8a97-7cc9c1a3d382 | -11.14002 | -46.16087 | 2024-09-26 13:08:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| a0a7d54d-2f23-3b83-8f59-211b8cb4ab38 | -11.67943 | -46.33561 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 6b716e6d-0ab9-3abd-913c-11f3fc06d530 | -11.93798 | -47.3309 | 2024-09-26 13:08:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b46873a4-fa02-35f0-9fe2-310e9429dc15 | -11.93544 | -47.35176 | 2024-09-26 13:08:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 36784d7a-9c60-3673-a75c-465824404421 | -11.89352 | -47.05908 | 2024-09-26 13:08:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| e86ea7ce-8e55-35eb-a696-cbbf1b5eb01f | -11.85077 | -47.72783 | 2024-09-26 13:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 188d3af8-b4e0-3db9-9a17-75ffaa4401bc | -11.47437 | -47.28622 | 2024-09-26 13:08:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 879f5513-8710-3b55-9178-81210c3d8d41 | -11.47186 | -47.30682 | 2024-09-26 13:08:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f6e4e2a2-bf9f-3af3-aaee-5fcf0255c22e | -11.25821 | -47.45584 | 2024-09-26 13:08:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8fc0060a-2a31-39ea-8ce9-bb02b776d93e | -6.34117 | -46.90328 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2bb9337f-6618-331b-99fd-822d6afc413f | -8.59601 | -48.35704 | 2024-09-26 13:08:00 | TERRA_M-T | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |


[Clique aqui para ver as próximas entradas](README183.md)
