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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f360314-a01e-3e24-bc7d-34f8f39c1fd5 | -4.07174 | -48.32109 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 391342f7-9f3c-3827-a584-fed50f994a40 | -3.96237 | -48.12893 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ec73592f-f679-34c0-99f1-2babceb31398 | -4.02967 | -48.28541 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1422fddc-4ff0-329d-842d-252472084bd4 | -5.44675 | -43.25953 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2997ace-31b1-3548-af01-134f7a5bdbc8 | -4.20976 | -46.69476 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6ccda47c-9719-3d5c-82ec-bb611f424e44 | -2.97491 | -53.91064 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9cdee95-0d3e-3b29-89ef-a2eb470a6e23 | -3.59055 | -50.27018 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6a35408e-157b-3a8c-b1e6-8e1cf2b4d6a1 | -4.25367 | -47.57101 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e1fb9a4-cd98-3938-9da5-9e3f434c5b04 | -4.0186 | -49.92231 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6c422d7-05d1-3fb3-b7a2-26f6b0d6d1f7 | -3.53685 | -45.74739 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d156abe4-dc42-3b43-ac1d-e949808159a7 | -3.05585 | -51.06693 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2ef75cf-6989-3d87-af48-bfa21967ff7a | -3.19814 | -48.66441 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d44cc896-50f0-30e0-b982-584e433db057 | -5.1698 | -45.28141 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 038a5088-3247-3fab-b289-49ac6de30981 | -3.74924 | -51.94987 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c7af27a-c420-3e18-aacc-8a384fbc5e1f | -4.2813 | -46.08147 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4c3abdc-5033-3a5c-bdbe-32ea9736ac1c | -4.28621 | -48.6454 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4366de9b-844d-3c7b-bcfb-c71c4f931099 | -3.15979 | -54.48283 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9ee554b2-52ec-38a3-87b6-fc059f870aec | -3.47698 | -52.62478 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 356e95f4-9242-3332-abe7-4cfec7ebf91e | -4.61622 | -45.98133 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 109b0b6e-9d15-34a3-9b10-c961af5ad329 | -2.84188 | -49.43284 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd17a311-b720-343e-bed0-fca341949a8b | -2.8484 | -51.77317 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68c9d2e7-d686-3462-acc0-79e46932ba2f | -3.34436 | -50.35814 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cf07b5cb-6149-374b-8cb8-7270d23fae91 | -3.54875 | -50.3259 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e8461913-81d9-3dac-a5ad-0d7d5b22073f | -4.1303 | -43.59558 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 817ab56e-fb78-3b71-8f43-856dffc20973 | -3.16194 | -54.4856 | 2024-11-09 04:33:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f370d09e-0947-33be-a77b-880d2caa94d8 | -5.04441 | -46.79583 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c8c5e30f-6cb6-3d1c-9b71-2401c96cbc27 | -5.17808 | -43.99859 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c5d0c503-0f33-36f1-b97f-35c83a8318bd | -3.17733 | -51.30576 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad96d049-8d51-3ed8-a036-f9c602f06256 | -3.24644 | -51.55038 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70aa48d9-30fb-3d5b-99c7-cebcfb7a35de | -3.24897 | -46.44257 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca6366e3-c9d6-321f-90fd-0c9908473ec9 | -2.82217 | -52.93334 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d845d410-3605-304b-9117-a2fc809b313e | -3.80583 | -52.02304 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 856ee65c-6183-38b5-98e4-e4008edf22e7 | -5.50605 | -47.17385 | 2024-11-09 04:33:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd160492-2ca1-36d4-9cd2-a420b5242a49 | -4.73673 | -49.00039 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c377dee-47ca-36e6-ac6b-51254651e0d5 | -3.31617 | -46.33843 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d077868c-f0e2-3977-a8a8-a5d0d43120bb | -2.87795 | -49.2267 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfe8401a-0583-396d-9511-58d2f6b43ff2 | -2.399 | -53.86484 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0f2bd444-37bd-37a9-a1b2-d9f84980dfeb | -5.85568 | -46.45326 | 2024-11-09 04:33:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29dc5b55-d165-32d1-8a8c-46ceac54c122 | -3.12424 | -50.21339 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 797ba954-5ade-3f83-8ec3-a7f8e2b604db | -3.03091 | -53.25623 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c34ee771-2138-38d2-b649-a7e7597ae95a | -3.2402 | -50.44464 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d417bdb7-d7a1-3502-b658-0122cf142ff2 | -3.17008 | -46.62223 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce5800c8-7677-3223-b271-fa0a525d5841 | -3.97358 | -48.16631 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe85379e-8108-36cf-bb4d-a2f0329014ce | -2.66299 | -49.89828 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8eef3feb-e370-39ea-80f8-ea8368cb4e03 | -5.21947 | -47.90284 | 2024-11-09 04:33:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c29b17c-640d-3876-bd1c-1c713c6af6d7 | -2.86572 | -49.14875 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b45a5d01-0ab9-3f7d-98bd-1e633d4c1aaf | -3.17658 | -51.31039 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f7e63dc0-83a5-3a35-a978-fdc49b284e7b | -4.02038 | -46.18348 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 87e20fad-6bbf-3cb8-824c-09ad059e7fee | -2.88203 | -50.41303 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f79dd2b-59be-34a0-99a5-4ce089f0bee6 | -3.33196 | -46.41238 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a3f1cee-44fa-32d2-8a98-5faf8b8a88ee | -3.80975 | -52.02366 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef4ca8f0-de07-3606-ba0e-f03d4683d3d4 | -6.17775 | -45.44732 | 2024-11-09 04:33:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 24d087a7-b46e-3139-94e5-710d1ee57ea6 | -6.23434 | -47.28059 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1daaeded-7b51-3439-a6db-a956887c96bd | -9.77173 | -43.57998 | 2024-11-09 04:33:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90f7bef3-2d2e-364a-a95b-eb04acd30f5d | -4.10806 | -49.4199 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b06fa24-d9bb-3d58-8c4c-23258d820af9 | -3.88635 | -46.43405 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 311ba466-97b4-370d-9d49-b35b6579d63a | -4.12886 | -43.59717 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 19af7f3d-2bd6-3cd8-935c-51d624004d9a | -4.60822 | -48.69607 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4a7c0ef-8845-3448-991d-2b014943fa6d | -2.87571 | -51.47094 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f8138284-cc19-3c6c-aa6b-8cc58f17f342 | -2.96079 | -48.02872 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd863b88-a3e1-3885-85d9-10a2fd68394a | -3.49912 | -51.30844 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c89af3ff-20af-3b62-bddb-494828bafc5b | -3.76999 | -51.38499 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c872b28-1977-3488-9c98-111795c755f2 | -4.38838 | -48.57893 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1ee5165-5816-3dc6-bbdd-22f29dec32f3 | -7.59569 | -40.05082 | 2024-11-09 04:33:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8dbcc40b-cf59-313c-bcb2-567380296e4a | -3.06851 | -47.5782 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5b42bfc-ca50-35e2-b899-a52ad0fb9bb0 | -4.41017 | -43.3784 | 2024-11-09 04:33:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aff4719-77a9-3c8d-ae7a-a11225c5b85a | -2.88031 | -51.46677 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a1e305-7899-3164-a333-6996c19438fa | -4.31816 | -45.61818 | 2024-11-09 04:33:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ab0e001-cbf7-3ee2-9dc1-86181f07fe73 | -3.59372 | -47.35481 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a6be1970-3f1b-3c21-ab89-b02ed3d622ac | -2.85335 | -49.22672 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52ebfe6c-1bf1-33a8-93a3-fbb4042a0c3f | -2.99904 | -49.23813 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 08850afe-7022-36a4-be50-ba0f851eef9d | -2.60293 | -51.30257 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c304dd47-5567-3740-b6be-d66d69e572d2 | -6.10496 | -44.75565 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3db74c77-7c2d-3299-beb4-b9f1099d0acb | -3.07367 | -50.57451 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2b031a97-fd8f-348d-ba83-f4035a67cd0e | -2.7991 | -52.94194 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e00e7b79-dfb8-3533-82bf-0238bf7be278 | -3.1025 | -53.70987 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b91a4f95-1b95-391c-8cb5-05631af31475 | -3.89057 | -52.3945 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ab4f47e-8e52-3b20-8223-f7ed4c64deb4 | -4.4941 | -48.49114 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1b75141-d3c7-3da2-b8eb-5bbe79fd02a8 | -3.2346 | -50.45662 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9cbd759-635b-391d-992b-4cfba6180962 | -4.21277 | -48.68116 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a299e40f-01dd-343d-93f0-0ccec6b1ccde | -2.61513 | -51.29967 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34cf460e-ec5f-3945-a4f8-73ac2700d692 | -3.09401 | -50.2419 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 24a18dd2-815c-3794-9c51-7147224be4b4 | -2.72894 | -51.73886 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da2037f8-27c3-31a5-8e43-e9445367f87b | -3.88532 | -50.24005 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 55b5ec4a-7c88-398a-b938-a6314a26b12a | -6.23488 | -47.27711 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 973f7aea-d1ed-3d90-bd71-a516db644e83 | -3.97765 | -46.41546 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96d44c47-157d-382f-8338-60fc6e51aef4 | -5.17742 | -44.00302 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1a925d0c-cbe8-3954-b7ad-fb17252ecdb0 | -10.21218 | -36.25169 | 2024-11-09 04:33:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| 96de63e9-859f-3d01-8548-b5bb7bcd8eea | -6.23658 | -47.28807 | 2024-11-09 04:33:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 96ffe16e-0e46-321a-bc60-922f45338be7 | -11.08999 | -43.3425 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| cb9fd0e0-c486-3775-aee1-5b2d7f91965a | -4.38767 | -47.76082 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4ef8a4a-5624-30e1-977d-66e95076d17b | -2.62275 | -51.30087 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4a621dd7-5bdb-3a07-ab16-a3370434d4b0 | -5.28725 | -50.57057 | 2024-11-09 04:33:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7b8e7a2-5da4-355c-9bc8-e404b9347ae8 | -3.78628 | -52.21661 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fdc3e47-737e-308a-8747-3c97ed613cac | -2.24356 | -53.77416 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 21f747da-5c81-31a8-80d3-ab4cdba46c4d | -4.70806 | -46.3731 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78164afa-fbe8-31f1-9f58-7c88b887510a | -3.44067 | -51.11602 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ecb225a-bff5-3a5d-a3ac-2291c238d2cf | -3.03982 | -50.35984 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4446ff9-f42b-3104-913d-120fd35ee2b7 | -4.70471 | -46.37255 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb94d6b6-2ebd-3f71-8d55-1c41d2db91cd | -3.68308 | -51.3013 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README51.md)
