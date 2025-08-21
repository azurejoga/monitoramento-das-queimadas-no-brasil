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
| 8f36eef1-68f0-396b-9ca1-2d7157a89de2 | -6.49192 | -43.10246 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 971eeeec-b279-3147-bd4b-d2815361eaa6 | -5.75519 | -45.30033 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de380293-777c-39aa-af2e-6c21b97b3b7e | -5.9904 | -42.81322 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8ac48ece-517e-3ec3-8317-a839cf629b3d | -6.21228 | -43.32977 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ecd031b-b7c6-3a01-8f02-dd5ee6720937 | -7.95183 | -42.63968 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5712dc71-9f6f-364c-b14d-746688dfb014 | -6.49129 | -43.10682 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6474cf51-c259-31e0-b503-d513249872d4 | -5.87596 | -42.40839 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 14de8053-1d32-30d2-914a-735df14008f0 | -6.36616 | -43.25661 | 2025-08-21 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc8cb4d-e294-37ec-9d41-4652eb394905 | -5.10488 | -46.17866 | 2025-08-21 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7593815-c8d4-320f-bb3b-3c955e455d5a | -7.569 | -44.39964 | 2025-08-21 04:38:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51891f0c-6ebd-3ca5-8a50-284df8e09434 | -6.29201 | -43.88112 | 2025-08-21 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44ce6717-3c47-3d83-b7df-f2f9506f4da3 | -7.53419 | -50.52647 | 2025-08-21 04:38:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b39d6dfe-c038-3cea-a834-4c3b5720a9f8 | -4.8157 | -47.31752 | 2025-08-21 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78f0b271-ed43-3798-a2e2-2bbe12dc2453 | -6.54636 | -45.51562 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f483e7a5-a5e8-3e00-9092-0dddcae4c1c1 | -6.25879 | -43.72542 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ac98b2e-cbb4-3395-bed5-3798e4201227 | -5.21966 | -47.46836 | 2025-08-21 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a896aaa-5f19-3e01-882e-b84a69538a11 | -4.65033 | -43.12741 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f6328dd-fadc-3322-ade3-01f54cb2eccd | -7.14955 | -44.18307 | 2025-08-21 04:38:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72296cd2-c1cf-3294-b654-9d523f8c2abf | -5.82164 | -51.68945 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86fd1ef1-25b2-35f1-938f-ab0153c40d3c | -6.73015 | -43.98375 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1551a1f3-9bd2-3319-9d20-68648bf54474 | -3.94394 | -48.09166 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9b200ec-e01d-3345-8f03-3d23dc16c3bd | -4.64232 | -43.12206 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1994a1c1-f850-3401-a8c8-c5482e3d2523 | -7.95654 | -42.64014 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3c852e8d-4e04-36a6-8342-57f7d74f1f7b | -2.38775 | -47.66414 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 574c78d6-ead0-302e-966e-4fb3ddf8d9df | -2.62241 | -46.84399 | 2025-08-21 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ce78d43-ea51-3cb3-81cd-89e2f62fa917 | -7.12442 | -44.66073 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4efb508e-dfcc-31c2-b15d-e21825194efa | -6.50083 | -43.44836 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49a99b6b-ffb3-3136-8d3b-0c4ac89faa8b | -7.2567 | -43.68679 | 2025-08-21 04:38:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cae648e-72f1-3e0c-8a5f-7d9a9142261f | -5.11788 | -43.21228 | 2025-08-21 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c29cd5e9-9c61-3518-95b7-4a097a4e73ca | -6.12634 | -44.72234 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44730e82-d85c-3020-993e-abde6e35abff | -7.01345 | -44.62357 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58bf437d-792e-3fba-b8b4-aaa93f7eae62 | -2.53886 | -47.71651 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff508a5f-b01e-3afd-b546-bbea93b8b834 | -3.96684 | -48.09552 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6b2129-52c9-3ef9-9cb9-87a0b240cafe | -7.02823 | -44.60707 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0d7f359-6d67-357a-8c3f-57877d78b9f7 | -3.88611 | -52.1638 | 2025-08-21 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c209373a-b23e-3a85-9d06-1c670d1852bd | -7.64283 | -45.24936 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5d243680-f732-3585-8ae7-0501ed8e9a51 | -5.67996 | -43.86728 | 2025-08-21 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4b41557-a8eb-343c-aac6-58c91ea327ae | -5.25694 | -44.4775 | 2025-08-21 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a9fdf0-e9d3-3d4c-a956-f2d7682a1ae1 | -7.01449 | -44.61647 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 1fa2c8cb-d68b-338a-a1f9-5bff578da311 | -6.53356 | -45.47086 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4084ee7-6db9-3d26-bdac-51fe79693b2d | -4.65002 | -41.40779 | 2025-08-21 04:38:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e285ac7-6737-3d35-8d11-ad6a7ab6b391 | -7.63962 | -45.24385 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f7a53f-442f-307e-bf91-d7de0b0e1af8 | -6.11015 | -44.37858 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ebeb0b2-2b9d-3268-97fc-c12e7f783608 | -2.58133 | -51.91343 | 2025-08-21 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f33d1ed-6e83-3cb2-b40f-0ef088111c9f | -6.2684 | -43.7188 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b1b89f5-104d-3187-af9a-df473c7bda76 | -5.44131 | -45.09765 | 2025-08-21 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c72f1b40-4af9-3950-b6eb-d0e568cb9039 | -6.66095 | -51.57331 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cf3541c-68fd-3451-bcc7-59fc490918a1 | -6.4288 | -44.66183 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86d51856-c24c-3296-83a1-63b68c8950a5 | -6.20002 | -43.5671 | 2025-08-21 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c4bd7ef5-06ae-396a-ab18-e0d6efdf1a81 | -8.34397 | -47.50439 | 2025-08-21 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a18377a-65af-34f5-813e-9c9c2106d49d | -5.96779 | -44.15841 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb0cbbd6-d445-3f58-83b9-14613b930e8b | -4.31544 | -48.08112 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f55f3212-bf6c-3307-9d4c-c19aa46a5a69 | -7.01748 | -44.62418 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca820577-a877-3fe3-a2bf-6b161ae21243 | -5.0856 | -47.71957 | 2025-08-21 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e1fc10d-cab8-366f-953d-cbe37916f558 | -6.86352 | -44.42703 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d056e8bf-563c-322c-a529-d5e243daefcb | -9.35855 | -48.28855 | 2025-08-21 04:38:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4795a9de-ef84-33f4-b718-62efe6f1ada1 | -3.97004 | -56.11312 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ecdb151-c3ff-30a7-b0cd-7a7d1bb5533a | -5.40848 | -42.37045 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 46fc3c21-347a-36d1-97f6-078ea914833b | -7.27723 | -49.57425 | 2025-08-21 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e891d898-793b-3644-9704-ba7ad01ba0a7 | -6.02398 | -44.36922 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac456816-4e8f-3305-aa83-facd3ddd537e | -6.0186 | -44.34999 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ecc31fc-c4ee-3bf5-a2e2-cb5623bd5ba4 | -7.70161 | -44.01498 | 2025-08-21 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5abaceda-efd9-343f-a51b-40a19288ce0e | -8.28953 | -46.32481 | 2025-08-21 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47112365-0305-3f35-95a2-4d4c4ca5b8eb | -8.82204 | -47.4732 | 2025-08-21 04:38:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c62aa515-7811-3792-a4c6-c16c8828a22a | -5.98595 | -42.81234 | 2025-08-21 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 326b585b-f92c-3b19-833b-defafd65a080 | -6.06718 | -44.1102 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bde047c-335f-33d0-989d-aaab3985644a | -6.4187 | -44.67474 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1cc5f88b-eafd-3d86-806c-9051ebdf0eb4 | -4.85935 | -42.53722 | 2025-08-21 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fe32fec4-6a0a-32a5-9840-26c6a6ceca78 | -6.01296 | -44.36003 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0df89ba8-f0bd-3193-a970-57c7a489eb82 | -6.02908 | -44.36278 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5cd5917e-6587-3579-9d06-c050c748dee1 | -6.25983 | -52.81936 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23577462-cf4a-3574-835f-9560b1cf0690 | -6.27149 | -42.81842 | 2025-08-21 04:38:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0dc78217-0f75-3041-ba07-3bf8965589fb | -7.73929 | -45.73305 | 2025-08-21 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b494b90b-4b91-35cd-bf8d-4cfd40a5aae6 | -5.40915 | -42.36585 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c1ed4345-2adc-3051-b73a-541fde627873 | -7.23745 | -44.71008 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40c9a4ef-d734-319f-a522-80dbe47391a7 | -2.89311 | -48.07797 | 2025-08-21 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75f18d8a-acd7-3cff-ab76-634b275f8854 | -7.63498 | -45.24574 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a67910fc-22f4-310f-8c41-ca977fa1cde2 | -6.46018 | -53.38409 | 2025-08-21 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 085a801a-9952-3ff9-b31b-28df369f7e1f | -6.41976 | -44.66772 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4faf24c1-c9c5-3f43-9349-9aa8de64fa20 | -6.34127 | -43.42747 | 2025-08-21 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3d86241d-25a2-34da-81c7-16966ffe9be1 | -4.91191 | -45.32332 | 2025-08-21 04:38:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 763dd60d-4664-332d-b682-72df97150874 | -4.60194 | -48.50832 | 2025-08-21 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7a59841-495b-3e0a-b742-88ec9a171176 | -3.98721 | -42.50883 | 2025-08-21 04:38:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e98e1946-4495-3a55-801f-300fc11927de | -2.91578 | -48.30104 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0ac1f9c5-6714-3699-b1f5-b0c1441852b1 | -6.01404 | -44.35286 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1073dba-25f4-32f3-93ce-7aa3ef599e5d | -6.54123 | -45.52412 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdde4a66-a1e2-3c34-b540-7b30e234cf94 | -8.83771 | -52.03831 | 2025-08-21 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07923aad-4f46-3a86-b85b-b93325d5de98 | -6.0826 | -44.42516 | 2025-08-21 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f8f5ea7-b7c1-3327-b7ad-7c14145b6889 | -5.48565 | -42.16687 | 2025-08-21 04:38:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 984fdb2f-559e-3ba6-a43c-2dce95d93863 | -7.12089 | -44.65669 | 2025-08-21 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af96493e-479f-3327-889d-ba8aeceebd6c | -2.91524 | -48.30449 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| efb3a576-40ad-3d36-beb1-db628729dbbf | -6.07322 | -44.11856 | 2025-08-21 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1e3b3e8-215e-3923-9615-5032fb6be922 | -4.4057 | -47.63398 | 2025-08-21 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85ecfb89-3f9f-313f-a468-84adc7e41966 | -2.92556 | -48.23893 | 2025-08-21 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b8ee06d-f163-3ac5-8734-32b85d93741f | -6.34426 | -55.55938 | 2025-08-21 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f757c474-215d-372a-ae61-171b53ba50f7 | -6.74908 | -43.9431 | 2025-08-21 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ac0fb61-cd3e-3f32-9cd5-c64406062f29 | -5.25464 | -44.4762 | 2025-08-21 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15da61e6-9624-3ab8-8016-7b63d5dce0fc | -7.63502 | -45.24811 | 2025-08-21 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c8f1f26-5f11-39cf-befb-307a473998e1 | -6.10569 | -45.41113 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dcaf8cf-6f76-3b15-ac59-107521e52948 | -6.10626 | -45.40843 | 2025-08-21 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README38.md)
