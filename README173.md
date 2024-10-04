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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 392c1db1-aaae-3fe3-baea-d1a6e886994b | -21.40182 | -57.23358 | 2024-10-04 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c36c95ea-8238-34b5-b458-3b310c436ad0 | -21.4024 | -57.22985 | 2024-10-04 04:59:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bab15366-1ea2-3bcb-9879-55c33231586c | -22.11587 | -56.70817 | 2024-10-04 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6eda21d0-d93c-30b8-9210-d0fc01ab9752 | -22.11922 | -56.70874 | 2024-10-04 04:59:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00cc8c9b-86fb-385d-9bc4-9eac0910425c | -21.29186 | -48.90584 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e77220a3-74f4-34d6-8aec-59002cc456f7 | -21.29125 | -48.91173 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 81416e41-1df5-30ed-99b1-1662fbc6c04b | -21.29062 | -48.91777 | 2024-10-04 04:59:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 5a8d3463-d44f-3acf-9a00-5d5c8c2ca3a7 | -21.28792 | -48.89476 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4fa15686-d0ce-356d-a321-dbbc1e674da9 | -21.28761 | -48.89777 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| b5a3a2db-5c77-3406-b3f4-ead9897faa55 | -21.2873 | -48.90075 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 39.6 |
| a9aa73d1-3b00-3d12-9454-55e2f84ade3e | -21.28684 | -48.90518 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 04bb4312-3666-3b70-9227-78bee25fced5 | -21.28623 | -48.91108 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7ac63396-ed3f-304d-89df-42fab38339ad | -21.28559 | -48.91723 | 2024-10-04 04:59:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 3c2d3d76-4eb7-3b74-a64f-17f0bbff437a | -21.28291 | -48.894 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f4369d3-04ad-36a9-bc97-9da2b104a2e7 | -21.2826 | -48.89701 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 49d5aafb-8877-35c3-972d-5ea28a5e0254 | -21.28229 | -48.89999 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 4a4ef2ef-594a-3ac3-95e6-153e895732d4 | -21.28183 | -48.90448 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 0f67b0be-5626-35ef-8a9d-5cd53971db2b | -21.28121 | -48.9105 | 2024-10-04 04:59:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Cerrado | 55.2 |
| db93e066-3b9a-3013-a512-d461866e3a4a | -21.27728 | -48.89931 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 13416a09-b32a-3b2e-9812-1f47ab49f19e | -21.27681 | -48.90381 | 2024-10-04 04:59:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 8eadc504-575e-332d-820b-097a9be24c2c | -23.23151 | -49.98826 | 2024-10-04 04:59:00 | NOAA-20 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ee13742b-b5d7-3a13-8688-7e167af692e3 | -22.46575 | -50.12251 | 2024-10-04 04:59:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 254bfec2-3e57-343b-9451-fa0f4664b756 | -22.46104 | -50.12189 | 2024-10-04 04:59:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8442a0d5-39a3-3517-9508-5e8766d1d4af | -22.46045 | -50.12731 | 2024-10-04 04:59:00 | NOAA-20 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bea4ac3c-67ed-3661-a7c4-13e7222adf71 | -22.26744 | -51.48498 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 4e07b914-a68e-3e74-8846-ba8baeb63c69 | -22.26694 | -51.48932 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 613803f1-3717-3526-8a94-46da3ad5ca90 | -22.26644 | -51.49367 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 534a30e2-3c23-39b2-bd0c-a0ae120e68f9 | -22.26364 | -51.48003 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 28e0c770-92b3-3222-927f-49447d62906b | -22.26314 | -51.48433 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f29b7325-b05d-3e4b-a56f-db57016196b7 | -22.26265 | -51.48863 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ba9cc7a-4ebf-30e3-9c8b-5411f695927d | -22.25885 | -51.48367 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 673645f4-3978-3793-b68d-79441396ded3 | -22.25836 | -51.48797 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b93e00ec-1e55-36b1-a80a-a012f0b768c8 | -19.63819 | -56.56697 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 074dd2dd-35d9-3447-9132-f134232f7d98 | -22.25786 | -51.49233 | 2024-10-04 04:59:00 | NOAA-20 | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| c3225157-f6f5-3cd3-bfa8-bb7e0a53e7d7 | -20.87667 | -51.49675 | 2024-10-04 04:59:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 08b51164-0247-3fec-a6aa-23a6b299e7a0 | -20.87618 | -51.50085 | 2024-10-04 04:59:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 970d2f07-66ba-3f6f-9bd9-b106c184abc1 | -22.6068 | -52.55762 | 2024-10-04 04:59:00 | NOAA-20 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e1c1fe13-f024-34a0-933f-fd9fbf6831ff | -22.60277 | -52.55698 | 2024-10-04 04:59:00 | NOAA-20 | TERRA RICA | PARANÁ | Brasil | 4127304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b9697fcc-ac82-3962-b547-b0308dbfae26 | -22.46716 | -51.97556 | 2024-10-04 04:59:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e360a91d-f76a-35a7-b59e-33a5ac48fec0 | -21.41769 | -54.18931 | 2024-10-04 04:59:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 311fdaa0-5128-3969-8ae7-c1258877dfff | -23.25246 | -54.93714 | 2024-10-04 04:59:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3504d3b-2f5b-32e6-a75e-417c1083e62b | -20.00055 | -55.45295 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ead46259-13c4-3d96-9f3d-f760d0d1d174 | -19.95727 | -54.88804 | 2024-10-04 04:59:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5f26d3a-7400-3e18-92ff-1bf89be6a6a8 | -19.95702 | -55.48605 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 472ce6d7-5f3e-3c9b-a2ae-89f989e53674 | -21.35351 | -55.6887 | 2024-10-04 04:59:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e582db5-f463-3a03-8cf6-0a9b36331867 | -19.65616 | -56.47172 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d8823503-8f1c-377e-9142-bc9026326fd3 | -23.05384 | -55.56618 | 2024-10-04 04:59:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ce8fe1af-b7e1-3900-9093-4afa574dd33e | -20.0486 | -55.95793 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4bdceeb4-f94f-3d80-9bdd-758d68d1eaea | -20.04578 | -55.97684 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 155cb31a-257b-3c96-a7dd-1efbe975a2dc | -19.83028 | -56.46675 | 2024-10-04 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 653f3c4e-ac82-3e31-98b3-02925fc67490 | -19.32761 | -42.56749 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e89be342-2883-3857-b6fe-cb00407a6b4d | -19.32659 | -42.58075 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 472a374a-707a-3d05-b73c-db3ac100c028 | -19.32581 | -42.59104 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 911e26a8-567d-32a8-afcd-a31f4bbf17cf | -19.32531 | -42.56514 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ea59ebe4-3ce7-3740-97b7-428281e1ee4b | -19.32517 | -42.59937 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| a95fdbf9-e829-308e-a9af-f1909ac0424e | -19.32431 | -42.57713 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 8490080e-5413-383b-9b55-662d87025bb2 | -19.32326 | -42.58976 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 8bd6db38-85d6-3ecc-ba3d-56812b346690 | -19.32253 | -42.59852 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| e9053360-f920-3df6-9a3b-cb5fa5da902e | -19.32196 | -42.60551 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| ee4fa80f-7c74-39ce-853e-12a417f1daab | -19.32133 | -42.55439 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 02f49431-05c3-304d-93ba-a012a31025c5 | -19.32058 | -42.56432 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f7b3f1d9-1ff6-3078-82df-f64c738287a0 | -19.31961 | -42.57705 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 305329b5-e118-3510-87f0-c20b8b869aeb | -19.31898 | -42.5537 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 41699f1e-02ec-3ec5-ac2c-19dd6d50bb13 | -19.31856 | -42.59092 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 3f05db2b-d552-3cc6-8ab3-26a33476302c | -19.31821 | -42.563 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f1b57e7b-3bf1-3284-96c8-cdba25be3b8d | -19.31794 | -42.59906 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 84cf9520-4319-3e91-897d-04b1921b189e | -19.317 | -42.57772 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c955ea46-2f72-3bd0-aa8d-fa2b7e7c9e92 | -19.31599 | -42.58995 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f7ff94a8-ee73-3eec-9d48-7a2f55adb4cd | -19.31532 | -42.59802 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f181b380-e246-3f5d-b12d-9b7e6a9ba02f | -19.3133 | -42.56444 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0aa5fdc3-a583-3c0e-b8d9-fb766539e59a | -19.31199 | -42.58183 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 516007d3-4757-36e6-a134-462241d66f0a | -19.31131 | -42.59081 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 984e5ffd-5e6d-3fea-ab3f-bcca614c3042 | -19.31099 | -42.56245 | 2024-10-04 04:59:00 | NOAA-20 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c4f5e6e8-3d92-3dc6-999d-7c215001414a | -19.30878 | -42.58926 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 336dc2a1-d6c2-3409-9f02-0f553882ea95 | -19.3042 | -42.58881 | 2024-10-04 04:59:00 | NOAA-20 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2dfe40a8-1b79-3a60-bffe-2d082f57beb3 | -19.02886 | -43.18798 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c8faa35d-2529-3f92-a00a-ab7cf12b8b84 | -19.02823 | -43.18896 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 43ecd03d-a17f-38fe-9cf2-7dd5cfedd9e5 | -19.02192 | -43.1873 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a90a1709-f9bd-344c-b82b-2f28caabafcd | -19.02128 | -43.18826 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 5c5f395b-b8ac-3df4-a36f-7d395016e495 | -19.01594 | -43.17503 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 42a28de7-9098-3e13-ad24-982d3bb85daf | -19.0154 | -43.18143 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 7425e19a-dc02-3348-85f4-35b773e05e4f | -19.01523 | -43.176 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.3 |
| d8fee797-66b8-3dea-8af5-cbc353f5f9a5 | -19.01473 | -43.18234 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 66edefca-08eb-34e9-8fb7-145ab0b59830 | -19.00845 | -43.18076 | 2024-10-04 04:59:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 588e6d90-19e8-3f99-8c9b-f32e2b3ca342 | -18.97192 | -43.19888 | 2024-10-04 04:59:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6f1f0edb-a658-38cf-aaca-290014e59a68 | -18.9714 | -43.20523 | 2024-10-04 04:59:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 44ccde45-6bfe-39df-b049-ae6d5fbdfc03 | -18.85777 | -42.91167 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bf6f5bce-407f-3fbe-a38a-d88a233810ec | -18.85726 | -42.91762 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2024598e-d76c-3295-a541-dad01aca6d14 | -18.85584 | -42.90956 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f11d1538-62db-3c70-94ec-9e8161b5ee65 | -18.85537 | -42.91549 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 46ce91dc-962c-32dc-98b6-a09180615ab4 | -18.85125 | -42.90469 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 801c21c9-b6e3-388b-8031-b89246dbeb4f | -18.85067 | -42.91158 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ffbbc9c8-dfb3-3936-a277-5f18674dcbe7 | -18.84937 | -42.90144 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b4209c9e-82de-3c73-8cb7-6b4557b5a8ce | -18.84878 | -42.90895 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| afe16799-2a48-34b9-b6e2-96035b911a11 | -18.84361 | -42.91099 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 4697594b-87fe-3ec6-90de-e2a796187b29 | -18.84187 | -42.90648 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 448ad345-926f-389c-b828-72757881191b | -18.8412 | -42.91502 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3c2b25c4-baf6-393d-b0c4-db85559d0923 | -18.83428 | -42.9127 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 34b9b601-b321-3eb5-9273-851e8b8d7093 | -18.83372 | -42.91982 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 23f08892-af26-3c39-a313-3d16a5f774b0 | -18.82883 | -42.98262 | 2024-10-04 04:59:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README174.md)
