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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2df802d6-0dc6-347f-95fb-a35819bab5ed | -8.8269 | -64.24036 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76bd73a6-ecda-3a6f-b762-cd1887fa1227 | -12.31287 | -55.1303 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53088e6c-0587-3426-9d94-b7965d1484b5 | -8.81974 | -64.24279 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 145ccff5-5d80-37b5-ab59-e45722e66ff8 | -12.977 | -51.04338 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 044412ab-8677-3dd6-8c21-dacc2f28f6df | -9.16467 | -62.22787 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1364858d-448c-39ce-8ca5-7af1ae9bc247 | -9.62483 | -64.67191 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e87a884e-91ba-3688-9dbd-8a4f8f9b5910 | -10.83229 | -57.1733 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 19e092da-f3e8-392b-a0d2-c0dbef299eb3 | -9.91208 | -58.5637 | 2025-10-05 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7503978c-b71d-313d-b681-d0edea314d15 | -9.55792 | -63.20969 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 991e48c8-cdcd-3215-b334-8b606fad449c | -9.04245 | -61.64009 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 643bb54f-1d8b-3b80-9b2f-5edc2a933aeb | -9.32363 | -54.51511 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ced14870-ae64-3869-8ab6-12a145fc3b32 | -11.89366 | -63.45012 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7101d46-7ac4-3433-9ffc-2745acbd4816 | -9.8363 | -59.46925 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a30b5538-4462-33ee-b04f-6ba123648fd4 | -8.3217 | -70.19382 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16552ce6-2c66-3796-800e-716d1e24de4b | -12.98108 | -51.04291 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a8d49946-b579-3abc-9c59-8644dcee741a | -10.07495 | -62.50175 | 2025-10-05 05:36:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e175765-a69b-386a-b1ca-f32bf1d43bd0 | -10.80214 | -69.03813 | 2025-10-05 05:36:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 87729609-f65a-364d-a8f9-b266b351c1dc | -9.12325 | -61.76864 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ad287435-cce5-3ddc-b3b1-e045c75b3cf9 | -9.65406 | -63.79675 | 2025-10-05 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a9a297b-29ea-3a69-81ea-8fb78703b937 | -10.65673 | -58.75618 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df5602dc-d7f9-3501-84e3-8b68e31efd34 | -9.15494 | -58.30948 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed5c8d37-6038-3973-a33f-a9b7d2c52a65 | -12.31069 | -55.14854 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1cc35744-e223-343e-8a0f-691eec0d93c1 | -9.65322 | -67.40098 | 2025-10-05 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0e0f60b-4779-389e-8625-752512359fc9 | -12.32308 | -55.139 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64704d5-cfd3-3114-956d-50cf68517b22 | -13.73985 | -51.30432 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c3a0c7c-8bb9-3d05-89af-253dc00a3c4d | -8.42032 | -70.12366 | 2025-10-05 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7388c1f7-466c-37ef-bece-c10485cbb3e9 | -9.73507 | -63.43067 | 2025-10-05 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| deb8ccd9-2089-3681-9771-a483ac00c11f | -12.31666 | -55.14559 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cd1b503-f482-3831-9578-2845fe81c9c4 | -9.04303 | -61.63617 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9531fab9-d419-389b-ac04-23c29d0e6c09 | -9.32117 | -54.53414 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d5a2a405-6cc3-3b9f-9640-f78125c05df6 | -9.84866 | -60.26926 | 2025-10-05 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d810dc4d-b216-3731-b4b5-75fd7758f36f | -14.75414 | -54.6675 | 2025-10-05 05:36:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 899ed706-c41a-3270-9867-12119341a551 | -12.97141 | -50.99807 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1164c30f-a688-3728-b3b4-9ea9db0e7627 | -9.01673 | -58.98574 | 2025-10-05 05:36:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7620e4c-9d3b-3a84-8dbc-106302425f3b | -9.64276 | -54.31522 | 2025-10-05 05:36:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0e2322-86bb-3577-90e1-fc92939701fc | -9.71239 | -67.46674 | 2025-10-05 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58ac6db2-8ceb-37c0-a8e4-4bea95bf8919 | -9.33373 | -54.52413 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c9c9c71-ab2d-3bbb-992e-ef8626cbe221 | -18.25475 | -53.34531 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7e1ce15c-e45c-324e-b278-32c95466bdd1 | -17.88111 | -57.6317 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| df610391-c61d-3292-8502-b377cc70f181 | -16.38232 | -52.15545 | 2025-10-05 05:38:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cf2e44f8-4bef-3a12-b345-9787faaaea1e | -17.95912 | -57.5775 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b748a5c7-2867-3c6d-b1a3-9c5d46dc4f71 | -17.88478 | -57.5986 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 61ddc304-7ddd-3c90-9135-f497f2a0c366 | -17.84205 | -57.62472 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b032efde-5bc0-3a31-8ba8-3db1e897f8b6 | -17.87064 | -57.63377 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 624a6869-d0b5-3cf7-9c26-e4229cbf512f | -17.94591 | -57.603 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 89bef330-3482-33e7-9835-52faa1552230 | -15.21417 | -56.8082 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 500b0caf-0e69-3a0a-9631-a7e3bd7a497b | -18.25531 | -53.33905 | 2025-10-05 05:38:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dfeb17e8-1277-3c23-84d7-1a2a26eca51b | -16.12618 | -53.9789 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8125f58-09a1-3901-afae-b32b72f56504 | -17.90018 | -57.64439 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5a3d79cb-36f7-3587-94b1-33fc193c780c | -17.96255 | -57.54775 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b645e1ff-7ce0-38d6-9fce-018023316d71 | -18.25918 | -53.37009 | 2025-10-05 05:38:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a24b1818-3b72-3c16-a3b4-4253c4d7961b | -14.85431 | -60.06971 | 2025-10-05 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b6b5fed-80a2-39a2-bff6-8ea0e5ef957e | -17.87955 | -57.59948 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 34b2468c-d19a-3630-abf4-c7d76a03f1f5 | -17.85128 | -57.63353 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 5ea809fd-d5fd-3f7c-baa2-00fa01018bad | -14.8502 | -60.0691 | 2025-10-05 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d51bf600-3ee6-35be-b295-2e96dd9be7f2 | -17.85666 | -57.63125 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fc09b5f2-1259-3532-be3d-133396ff2d92 | -15.34589 | -56.94998 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 876ea1eb-9be9-3d68-b300-66ed28d5ee5f | -17.95064 | -57.60657 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| dc871d73-3066-3baf-8fc0-cabdefd22aee | -18.24833 | -53.34222 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a1e8bb3-eeb3-3c1b-b104-162d9b452dcb | -16.15105 | -57.57622 | 2025-10-05 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 34a52146-1a5f-3e56-b3ee-7551456e770b | -17.88535 | -57.63967 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| fd0d9887-d6a8-3d04-9ab0-28b59138bd2e | -17.88027 | -57.63934 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ea9fedb3-7972-3cce-9ce1-782c7c0d97d6 | -15.20938 | -56.84927 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32058040-380d-3f92-a0e4-801115df84d4 | -17.94787 | -57.5859 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 88d30aa6-ccde-3b83-a34c-481d99f3fc1c | -16.15595 | -57.57731 | 2025-10-05 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5e2e8aab-971a-3ac3-80ab-f45f4d4233b8 | -18.25973 | -53.36412 | 2025-10-05 05:38:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e0834f9b-584b-360b-8771-b9d2cd266ebf | -16.01721 | -58.2246 | 2025-10-05 05:38:00 | NOAA-20 | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a3dcfca8-4726-31f1-a1d5-9ea05fbd98c6 | -17.94692 | -57.59416 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| be6d8ce7-a33c-3816-9281-fe067bb73479 | -15.58229 | -52.49487 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 577ccbe7-af40-3ba9-9f69-45d2e368c73a | -16.11945 | -53.98313 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cdd304c8-ac0b-3bdd-be52-5992e64c2465 | -17.89041 | -57.6402 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d8eacdcd-f774-3cfe-b23c-a8c2ea00c3cc | -15.30131 | -59.23713 | 2025-10-05 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c0721b5-8c0a-35b3-a4f9-e4719ea04935 | -17.88137 | -57.58299 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 44ad3032-1883-3eda-ae57-6e375e754174 | -17.87986 | -57.59661 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1f6d1e7e-583a-3052-8ea1-a4c01c245c76 | -17.94625 | -57.6 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 02d06370-a622-3d60-a06c-eea8a9e105d7 | -17.87484 | -57.59558 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| db2a2f8c-79ad-3430-bd8d-4095c2835f46 | -17.86703 | -57.63019 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ce5877a1-dca0-363b-acad-b220b04bb6c1 | -17.96359 | -57.5834 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ab8a8424-b344-3e27-ad14-d8280acc9947 | -15.31023 | -56.94444 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8db4b0ee-49b2-333b-bfc7-8083245df39a | -15.58775 | -52.50917 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d31f0ba3-8d2f-364c-a904-8259b8ec1a76 | -15.5688 | -52.471 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68ca5b85-82f6-3828-ade1-ef390c3b6721 | -15.22046 | -56.79921 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a944d75e-512e-318a-b7ec-77983d6039c7 | -16.12569 | -53.98389 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75acc857-764d-3081-ba3b-335c925f1eb9 | -17.92541 | -57.60261 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| b557f3b4-888e-3ecb-b939-cbdec5778190 | -18.1678 | -53.36691 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8619c3f-5b5d-3949-b333-763e9d6785f8 | -16.122 | -53.97942 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e94b914f-289b-37b0-ac64-be29d68b6d60 | -15.21894 | -56.85664 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25bbf47c-67b2-3e2e-960f-6cd8da2ada92 | -17.92512 | -57.60514 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 4f982d75-96a7-3702-8e61-30a848ac1ce6 | -16.15491 | -57.57752 | 2025-10-05 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d22fd067-d824-32fb-ba36-7a773b4911a1 | -17.9123 | -57.62773 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ea01c0d0-7c09-39fc-8759-0d0e7ee01b23 | -17.95099 | -57.60348 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| fecb46a7-6151-3c8e-99f7-07f24f9ae491 | -17.95585 | -57.56111 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0b58c334-58d0-375d-b85c-a8dc097fafc5 | -15.60176 | -52.50601 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb3e40fa-e360-3164-ac3f-342afe144676 | -17.95846 | -57.58332 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 563b7f68-621a-3b3a-8bdf-8c8220885f94 | -14.85483 | -60.06589 | 2025-10-05 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3233322b-d98d-3edc-a7f0-2296bf2d4dd8 | -17.96222 | -57.55058 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9d0981c1-cd51-3b49-b48b-3b67afb48ea8 | -16.12253 | -53.97437 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4cfb7a53-6c55-37cb-a858-78705751835b | -17.95982 | -57.57149 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 56c0ce89-098c-3e50-a94d-e3e7fbce99be | -18.24234 | -53.33431 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 83d03d72-c6c7-3884-b96e-c8251ecb785f | -18.17263 | -53.3658 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README146.md)
