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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a20645d-1dda-38a0-84ce-5ed914c19ac9 | 3.6166 | -51.3102 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 89ae16a1-9a99-3746-aafa-463169c22792 | -3.1096 | -51.107899 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8308c0d6-3c93-3820-bf6c-91b617deed41 | -2.8356 | -52.9217 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075079de-15d5-38e7-b949-be0bea4d7a36 | -6.1242 | -43.976299 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4623b15a-15d4-3c04-8e1c-34964f280fb7 | -2.7559 | -53.2043 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4b7447-ec4f-3db7-8d00-70c9b997c875 | -5.6531 | -45.926201 | 2024-11-06 00:54:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f4293b6-dd9a-3aa2-81dd-1d6e9fc07686 | -2.9973 | -54.125 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea634725-bf2d-3268-9335-ae352862b081 | -2.6756 | -51.820999 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d2c4fb9-04a4-38aa-a368-807803ebf718 | -3.0101 | -53.413502 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec5ac629-0e93-3484-818e-4a7e8de048ca | -5.6561 | -45.938801 | 2024-11-06 00:54:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 765ffc96-4382-30f0-a3b7-8a3f2d0cdde3 | -10.0235 | -55.059502 | 2024-11-06 00:54:00 | METOP-C | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15484ff7-dda4-3c86-813c-1cf2e981c5fa | -3.1392 | -51.191601 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68274a01-5dd0-3b21-a92e-8825d3636440 | -3.2437 | -53.397598 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b68254c5-4661-3fa8-b742-f1ae15589ea1 | -4.647 | -43.818298 | 2024-11-06 00:54:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ebb641ae-1b86-3771-a08d-4f7dfeac5dfa | -4.1243 | -43.567799 | 2024-11-06 00:54:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ecca318-3c93-35e6-a13e-9dddc7040cf8 | -5.027 | -43.609501 | 2024-11-06 00:54:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa912acd-50a6-3075-83c5-22e857b9ece9 | -2.6788 | -51.8349 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd6ec44-f9fd-33cb-ac65-f70091d70155 | -4.1919 | -51.013802 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795baf42-3626-32fa-8f0b-3f8831b46954 | -2.1575 | -53.6539 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e41faae-1457-3f6b-abe6-52806b1e8258 | -2.9277 | -51.035198 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c08c9b2-22b0-3e00-9140-25e4678cca0f | -2.9327 | -52.535301 | 2024-11-06 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59b625c6-d2c0-3ab0-b83c-f08f06c5e90a | -3.2551 | -53.402302 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 331b8fac-8a11-3af1-b63e-25bfaa7b1d9e | -3.1816 | -53.848 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2845a0ec-b593-33a6-86e5-a8dd6e6ed950 | -2.9098 | -51.046902 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f3d636f-02f3-3a60-98b2-b7c30fdd1b81 | -2.8155 | -51.488098 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8d2b1a-79d3-38e7-a667-1ce1a551d45b | -0.8572 | -52.841801 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1138721-8014-3a19-93b8-674c777d61e1 | -2.7227 | -54.141499 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6853e59e-0a20-340b-a588-971a64ababc8 | 3.5178 | -51.246201 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 508c8172-9073-3a32-9357-636f5728fa88 | -2.9675 | -53.858898 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd344bba-0970-3698-92a2-24cb0f2c946c | -2.8078 | -52.935101 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8beef51d-c5b1-3857-8c02-958ac3f1d9cb | -2.7234 | -51.715199 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43f00b58-0e54-3712-a0ae-fc22a901992c | -2.9991 | -54.087502 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eadf91c7-f08a-3702-810b-fdc500454bfd | -2.7145 | -54.1507 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff2a795-7e43-373c-a782-56d2a36036fa | -2.7591 | -53.217899 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23a1c821-9e25-3b8c-acdf-a56c0f99646e | -5.1389 | -47.6973 | 2024-11-06 00:54:00 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5c82096-cfb6-31b5-86d4-6c844d9929f3 | 3.5276 | -51.248402 | 2024-11-06 00:54:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 29b7b420-cca3-3e47-b9e8-74497ece5cd6 | -6.1145 | -43.9786 | 2024-11-06 00:54:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21cef120-9f82-398a-a8e8-b27932660083 | -3.1425 | -51.205799 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c9845c-3de1-3bcd-8dc7-2606218ef468 | -12.1655 | -44.615398 | 2024-11-06 00:54:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2396eaf4-5c96-345b-afbb-1d559686b79f | -23.932699 | -54.075802 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 091c07a9-bb47-3638-8ae2-a635ae4113e4 | -2.9969 | -53.852299 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e372c68-d696-35c1-bd82-c01721e6c13d | -2.8778 | -51.310398 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce77ba0a-86fb-32f9-90a0-9df22ca39f53 | -5.9391 | -43.767799 | 2024-11-06 00:54:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f876b8c9-95da-39af-8ea5-adba49b389fe | -2.8227 | -52.910198 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a63d1347-a442-3c8c-b90f-1805f1815574 | -6.5006 | -44.6689 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bafa46a4-b0ff-309a-b606-2b89f3fbdf42 | -3.3397 | -51.6133 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e4ac11d-f329-3a1d-b459-739b454a9a76 | -3.1606 | -50.2145 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29910457-b186-354b-a8ee-aca079a42928 | -3.3252 | -50.079399 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a44576cd-84ea-378a-ab5e-2b75c5314d98 | -3.0285 | -54.081001 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ffdbd8-6324-3177-8414-5f50ba91d370 | -3.1308 | -51.110699 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 132886c2-dc6a-32f3-9247-8f4cb72843a4 | -2.9392 | -51.040298 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 548648da-ba3f-343c-83ba-01147b141c57 | -4.4701 | -50.655701 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92e4a2ae-eca2-3e6c-85f0-2332b3b1cdbe | -2.8129 | -52.912399 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723cc74b-7915-3142-b08a-380c162bf3a0 | -3.9659 | -48.144199 | 2024-11-06 00:54:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd1e6382-b75d-3145-ae47-91eca598df1a | -1.0655 | -53.66 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 714441a3-b0cd-39dd-8308-15d7931a21bf | -3.3315 | -51.622398 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54f06cda-39dc-3b22-ab22-daf6c82bd244 | -2.9179 | -51.037498 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c497a765-fa06-3833-ad32-0b8f1ebe4f9b | -3.0294 | -53.272499 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56515d13-cd6a-3175-8301-fefca0cf2395 | -3.2307 | -53.386101 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfcfa6f0-a963-3fb7-8093-408e0fce4111 | -23.9499 | -54.058998 | 2024-11-06 00:54:00 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2975accd-a5c0-3407-ac31-9747827a4c78 | -4.0923 | -50.494801 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2eafc7c-ea09-381f-9984-39533f7de13b | -1.3634 | -51.946899 | 2024-11-06 00:54:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9804500-3c67-38f3-b8b1-181fea132dc1 | -2.8342 | -51.792702 | 2024-11-06 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4d7631a-c857-322d-be2e-27566d328183 | -4.0621 | -50.009499 | 2024-11-06 00:54:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b95f5160-4e1d-350d-9163-bb30f3432de6 | -0.3572 | -51.429199 | 2024-11-06 00:54:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3017bbc9-c5d7-38e2-9723-274288df0dc4 | -3.0247 | -53.251999 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8c93159-f346-3681-a9fd-bdc984de5f8b | -3.5154 | -53.142601 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc9aa04b-8ec0-3ebb-a283-83f192e0c149 | -2.6718 | -52.522202 | 2024-11-06 00:54:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70d4a66b-c787-3ddb-b6f2-a3b6910c0905 | -1.5129 | -52.1036 | 2024-11-06 00:54:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebcf48dd-f31b-3077-ae85-0541b26d737b | -3.178 | -50.6007 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 184e3bd2-2398-3e77-be56-518ab917ab05 | -3.1752 | -51.258301 | 2024-11-06 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 581d2e72-e5e2-3ff2-803c-8f6c890eb5d0 | -3.02 | -53.231499 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55af61fa-48e4-3983-a72d-40018313aeac | -3.1089 | -53.710499 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 243c416a-7957-3d97-ad5e-9342c85f8f6b | -3.186 | -50.591099 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96ee0053-6364-3e2d-a935-8616a5c6896b | -3.6808 | -50.233299 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3969983f-4194-37db-8c65-d33cb6368fd4 | -3.7432 | -50.0578 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31744096-03ae-39f2-9517-491c776966ea | -2.8423 | -52.9058 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78e31c69-6342-3f0d-ba42-a1050865524c | -2.8211 | -52.9034 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2962018-8ac4-3dac-94de-9e3d940e2d90 | -3.0164 | -53.441002 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f522343-0351-3d29-9737-1b0b81155f7a | -5.5413 | -43.696499 | 2024-11-06 00:54:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3dcc0bbc-2fe8-32ba-bfdb-bb2066f1e63a | -6.5007 | -47.480701 | 2024-11-06 00:54:00 | METOP-C | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea7b0baa-51d9-3e2e-8b7f-a45eb466b203 | -1.8604 | -54.699501 | 2024-11-06 00:54:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 853c7cf7-b0e8-3dfd-8855-bfb21e7e3584 | -3.0392 | -53.270302 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 800b6066-7845-34f7-aa43-d1823115fb85 | -5.6629 | -45.923901 | 2024-11-06 00:54:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e1225d8-b07a-3a02-8490-b19d625a6c85 | -4.2428 | -48.532299 | 2024-11-06 00:54:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aed8b257-96ff-30e8-9dc0-63f4dfe04bf8 | -3.0975 | -53.705799 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0e81816-3894-35ac-adf8-fe45a8d88330 | -6.5139 | -44.6814 | 2024-11-06 00:54:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24c01f39-8674-3204-b984-fde6dd5929ae | -2.8191 | -52.939701 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a86a3c7-86f6-345b-93f3-3d2f853473c3 | -3.6693 | -50.227901 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 007a4ff2-176e-30f3-900a-17f2a169ba76 | -3.2045 | -53.2262 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95a40958-3ad4-3347-b910-f555dcb531e8 | -2.6159 | -54.531898 | 2024-11-06 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7458a9fa-a08d-3313-813c-034355056260 | -3.0861 | -50.961498 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dab939bd-6a79-3884-bdb8-a1d79aec44a3 | -2.8207 | -52.946499 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07004bdd-2b05-3e09-a766-99acfdb422d6 | -4.217 | -53.551701 | 2024-11-06 00:54:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9689e23-d526-371d-91e6-4990027e8053 | -3.1588 | -50.206799 | 2024-11-06 00:54:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bec6cc8-ff2e-3bab-bfe5-a5991ab30196 | -2.816 | -52.926102 | 2024-11-06 00:54:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad7a36f6-a264-3795-a936-f8540295c75d | -4.0764 | -53.930199 | 2024-11-06 00:54:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd9cd32-bf33-3aa8-b3e7-80397085e2d7 | -5.5466 | -43.676201 | 2024-11-06 00:54:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6de2460d-fd3c-3b89-b582-ae58b6f5e0f1 | -3.671 | -50.2355 | 2024-11-06 00:54:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ccbaf23-74c8-30c6-b223-ee2afad005cf | -1.5014 | -53.491199 | 2024-11-06 00:54:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
