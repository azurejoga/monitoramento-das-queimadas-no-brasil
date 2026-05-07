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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c34c2dd8-0bbe-3dd6-8df8-bc041c365f82 | -11.60936 | -48.05295 | 2026-05-07 05:08:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3d8e50b-3fc2-3227-993f-5c5f7dfdf8ff | -13.6289 | -47.82251 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 662a6207-8ab1-3fe9-90bd-ef455e8ea4bf | -8.81083 | -49.94504 | 2026-05-07 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3dd90073-b54b-31f0-a0fe-22fa26f26515 | -11.739 | -54.80624 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c515a49d-c505-3569-a4b9-c55791feb7df | -13.89361 | -47.52449 | 2026-05-07 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 687dba8e-c7e2-3ff7-a28a-4eda3a33dd93 | -12.49065 | -58.48274 | 2026-05-07 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 995a4a60-706f-3014-b6ed-e11b91fa266e | -11.73565 | -54.80571 | 2026-05-07 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddce661-44ef-36c7-81f9-3a0a873d3b19 | -12.85765 | -43.75564 | 2026-05-07 05:08:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6b4962b-4410-3e0d-803e-40963510cb95 | -12.76527 | -58.99628 | 2026-05-07 05:08:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07b2ae8b-08da-3b69-a179-7254673fcdc0 | -12.34291 | -50.01531 | 2026-05-07 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb61bed5-5f89-3a90-9925-f3f289f75e4a | -11.84282 | -57.84805 | 2026-05-07 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68ac67fe-b0c8-3704-8a3f-cbb938889ad3 | -10.55185 | -42.43629 | 2026-05-07 05:08:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dda8c424-4693-393f-a4f2-07329c906033 | -21.33184 | -47.08123 | 2026-05-07 05:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca9eca26-f559-371e-9a0c-76a97a8edce7 | -16.16548 | -58.49051 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8b8e0f37-e2dd-31b1-be2c-3b99908aa3c6 | -21.70609 | -48.41816 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e88e6940-272c-3175-b93e-f2ef4127840f | -20.71544 | -52.07884 | 2026-05-07 05:10:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1758d5d7-dc2e-3f51-9ec9-cf933d6942ca | -19.94813 | -54.38052 | 2026-05-07 05:10:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b57eaa9-b41e-31ef-80da-e07ffd0b3ec8 | -20.22658 | -46.84494 | 2026-05-07 05:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec44ff24-cc9d-30d9-ad05-648466a0f2c4 | -20.71135 | -55.18144 | 2026-05-07 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e113581b-cb36-3418-84ef-0e0c0d1e4c4d | -21.95776 | -57.59269 | 2026-05-07 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a6a2c96-ffbe-3dd4-9e47-22bcd41a9651 | -21.70574 | -48.42179 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 939d14f3-2206-3874-aee9-3618f4173918 | -22.97183 | -52.69295 | 2026-05-07 05:10:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a6e746f5-5a82-3632-8bba-2edeeadf5eb3 | -18.48707 | -51.69063 | 2026-05-07 05:10:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26e4f808-9027-3ddc-9e05-8274cdd765e9 | -16.60322 | -58.23837 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3908e495-5fe8-39bd-bb1a-37fecf0dfbb9 | -21.70644 | -48.41451 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c3993632-3d27-3281-a106-e6c35c8eff29 | -18.78576 | -51.93644 | 2026-05-07 05:10:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362180b3-6e41-3e38-bf86-225aba6b70cf | -21.90209 | -50.7302 | 2026-05-07 05:10:00 | NPP-375D | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91e85452-2070-36c2-92a6-3fa0f41ac77b | -18.78072 | -51.94341 | 2026-05-07 05:10:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7e5f87f-4314-35b4-910e-b2c6f9698229 | -18.78528 | -51.9402 | 2026-05-07 05:10:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13a1a869-7c97-3ba7-81c8-75dd02ad5774 | -22.74547 | -48.21611 | 2026-05-07 05:10:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d566ac9-583d-3185-b32b-e6a862ea27cd | -22.74582 | -48.21247 | 2026-05-07 05:10:00 | NPP-375D | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4eb93b36-748f-3cc8-b644-547cd5288581 | -21.70217 | -48.42051 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 40bedda4-37dc-31cc-b7de-20b6ea4c3681 | -21.97503 | -57.59198 | 2026-05-07 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac818842-eb6d-3f5f-b3d3-254ec6d9f096 | -22.00842 | -48.42661 | 2026-05-07 05:10:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f3307cc-288d-37e1-bdab-3f63302c218f | -21.70789 | -48.41736 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1f844546-1cf2-34e4-ba1b-6e4396a83515 | -18.43715 | -54.70754 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7ff0e072-9f31-3ae3-a045-e06caa2e492a | -20.71194 | -55.17733 | 2026-05-07 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b781e0ed-77da-3606-88cd-220b8164094a | -21.33224 | -47.07681 | 2026-05-07 05:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89608d5f-9296-353e-b962-a4d6cab99b0e | -20.79332 | -51.65903 | 2026-05-07 05:10:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bdaa5524-df3c-3180-884d-4fd5cc677127 | -18.44065 | -54.70808 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6b381f66-a938-3b7e-8cf9-7935096f897c | -18.44476 | -54.70452 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3598faad-b0cc-3c62-be3b-6f13bbdf0117 | -16.16205 | -58.48989 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 40edcadb-282e-3eba-9d44-1ccd523ae16b | -20.22695 | -46.84114 | 2026-05-07 05:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d34855ab-ead1-3c09-96cd-05108c9942ff | -16.59983 | -58.23776 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 62dcd4a4-9c10-3b89-9d3d-3d52e74fdbdb | -21.90641 | -50.72859 | 2026-05-07 05:10:00 | NPP-375D | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 907ab444-44ae-3a02-b3be-997689152cf6 | -21.97836 | -57.59258 | 2026-05-07 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50e03eaa-129d-3075-82e6-e375fa51c8a4 | -18.22665 | -54.59793 | 2026-05-07 05:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb219c53-af38-3dbc-9463-e60553245a9d | -21.95442 | -57.5921 | 2026-05-07 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d164eba0-1e77-3093-a078-e8b06d74f8fe | -21.9817 | -57.59318 | 2026-05-07 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a75d14a7-cd87-3892-aede-25ddf745e07f | -18.7812 | -51.93966 | 2026-05-07 05:10:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1a28b9e-1cec-330c-964d-093435ad50e3 | -21.70752 | -48.42097 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8cada2e1-8aac-3278-8dba-1bdbaf83b229 | -18.43423 | -54.7029 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ea99ef0-63cf-303e-8715-5c5e100a03ee | -16.6026 | -58.24214 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d3232608-718a-3a16-be4a-7a52002cc14d | -18.48804 | -51.68295 | 2026-05-07 05:10:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01cae1cf-b7cf-31d7-97d6-e2c5e72571d6 | -19.77665 | -54.09177 | 2026-05-07 05:10:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15fa2d8b-2307-3a2b-8619-757358a7da2e | -18.43774 | -54.70346 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 54bf49e6-19bf-3c76-ba5b-86e817c0907c | -20.23247 | -46.84453 | 2026-05-07 05:10:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4d43bf1-c646-3ac3-96cc-4b7cd99076c1 | -18.48343 | -51.68622 | 2026-05-07 05:10:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 982f92a5-a085-32fb-a94d-1bea6d0e687a | -18.44125 | -54.70399 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 865d4333-fad4-385a-9cd0-8a666571e77a | -21.33199 | -47.08159 | 2026-05-07 05:10:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0fd7d826-dfe1-3b53-b570-6f5a0c454d1c | -16.16955 | -58.48729 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 86ab0079-80db-3530-8a8e-9d8effa4feaf | -21.955 | -57.58836 | 2026-05-07 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f2742bb-672b-31cb-b798-9c0c7853d07d | -22.97595 | -52.69351 | 2026-05-07 05:10:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b22c67a2-52fe-3c10-a139-d683aebea626 | -16.16141 | -58.49372 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| d3ffd40a-99a2-392d-9abb-7ed3a4da916d | -19.94752 | -54.3849 | 2026-05-07 05:10:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee1185f3-ef35-3b04-9ad3-9596a8d250b4 | -18.28641 | -54.13068 | 2026-05-07 05:10:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25b07a50-4871-3ad4-a356-2cbc87a72aae | -21.70255 | -48.41684 | 2026-05-07 05:10:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 11770038-8651-3ffd-b416-fcee1788b959 | -21.90586 | -50.73348 | 2026-05-07 05:10:00 | NPP-375D | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 03d56ee3-c9b4-3bff-93d7-ecbf04f7e793 | -16.16891 | -58.49112 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e6406b4e-c375-3d8c-92dc-ae481e928783 | -16.16483 | -58.49434 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6e3c8c99-0c2a-3174-aa87-8fb5f57542f1 | -18.44416 | -54.70861 | 2026-05-07 05:10:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 071e2ef9-131c-37f9-a767-1d29988e77fc | -16.59921 | -58.24154 | 2026-05-07 05:10:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cc80ea87-6828-3f8e-a9a2-715cc68a1cf0 | -2.62464 | -51.94955 | 2026-05-07 05:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 84bd05d9-57d5-37d4-b063-a1b6977dcd09 | -11.73481 | -54.80558 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7993259-b623-32f1-af92-ceea68c0bbce | -11.60519 | -48.05521 | 2026-05-07 05:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd0f9cff-0a4f-3109-83e8-aab701ae651b | -8.72594 | -47.97708 | 2026-05-07 05:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9fc0359-3407-3f12-bfc2-9cfd4f726b45 | -11.7309 | -54.8003 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3329551a-826c-31d2-bb4a-32e9663425fc | -11.79663 | -56.96432 | 2026-05-07 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77b13ea7-f91a-3da3-8ce3-3782d050f312 | -11.74001 | -54.80154 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2688d723-dbec-3c88-bf9f-01b9957ab990 | -11.73545 | -54.80095 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e92172ae-579a-3bf2-b7a2-29e0de47d7a7 | -11.80057 | -56.96492 | 2026-05-07 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9151bfba-a6ca-3e85-b594-9a2d7108c6b1 | -11.72572 | -54.80426 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4f744e-1d75-3a42-8765-c30d7d7d3b79 | -10.24195 | -52.23144 | 2026-05-07 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbfaf4fe-4abc-3d5b-a524-908b2e90b376 | -11.73026 | -54.80493 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda74287-e54e-37cf-87f3-3674d6385615 | -9.24879 | -60.333 | 2026-05-07 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cbe3410-dc33-3ef6-b53f-1b7f48bd729e | -11.79735 | -56.95918 | 2026-05-07 05:25:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccfdc0e7-349d-3620-9428-a18e5a18c348 | -11.72642 | -54.80593 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 817d8b10-29f4-3f3a-a4f8-c467c71676d4 | -8.72518 | -47.9831 | 2026-05-07 05:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f45d019-2b89-317c-8559-abcb7f781aa5 | -11.61917 | -48.05729 | 2026-05-07 05:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6210c9ea-75df-3aee-935a-a6bcc987a30d | -11.47727 | -52.91888 | 2026-05-07 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5b03273-d7c6-3ae1-a728-b093b199a47f | -11.72702 | -54.80131 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59498f8c-611d-3cd9-bed6-66a4aa07f8e9 | -11.73936 | -54.80619 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e7ea00c-df03-31af-82a3-8c38a20a9e5a | -9.24824 | -60.33653 | 2026-05-07 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab999258-a931-3b4b-96b5-f8c68918f0c1 | -11.73217 | -54.79734 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8166e008-e496-3726-b4ae-ec956b76329b | -10.23619 | -52.2341 | 2026-05-07 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70cbdbc5-c92d-3d84-9ea2-71900d3ad47e | -12.34242 | -50.01475 | 2026-05-07 05:25:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1734be02-49d6-3506-85e9-2eff46796076 | -11.73097 | -54.80661 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb8dc17e-dc94-3b76-98de-afc784e0c392 | -11.73612 | -54.80264 | 2026-05-07 05:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3386c8e9-861f-3788-9bac-a58584051b02 | -8.81037 | -49.94682 | 2026-05-07 05:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e40c5d88-f107-3ebd-b8c4-60f58c5b3fe2 | -10.23664 | -52.23075 | 2026-05-07 05:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README8.md)
