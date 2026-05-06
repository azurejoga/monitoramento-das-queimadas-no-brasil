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
| 30916baa-4a9e-3743-b6d9-00ffb6e1d2fa | -12.49661 | -58.4681 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8770d01c-8a28-3c92-8b1b-903ca7294c78 | -12.4943 | -58.48347 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7382dd82-9b0d-37aa-8c5e-f41118ae7e7f | -12.60066 | -58.65918 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9b16d57-ed68-3fa3-be9e-385912e11695 | -18.77908 | -51.94582 | 2026-05-06 05:27:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32486c6f-2cf1-30fb-85af-422a58f98207 | -12.50466 | -58.48509 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 60d33308-7c88-37e2-9aad-6bee8888098d | -15.9842 | -56.21345 | 2026-05-06 05:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9b39dae7-5c65-3940-8b51-c244bfee096a | -12.50063 | -58.48838 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0f5c672d-afa8-3be3-9d5e-adb7391832b3 | -16.49387 | -52.71979 | 2026-05-06 05:27:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52fa62f9-c365-3141-b03d-ce1a8644c290 | -12.50697 | -58.4697 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e74b8b78-c929-3ec8-9b0b-d1672de8bfcd | -12.50639 | -58.47356 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39c039e9-26e2-3fcb-beb4-aecb7e4d7993 | -20.2154 | -50.65294 | 2026-05-06 05:27:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b0873493-3e05-3336-9bde-ecbb93609b0c | -18.43784 | -54.7125 | 2026-05-06 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| abae599c-0d21-3ec1-9b83-7756a82a0d60 | -12.49948 | -58.47248 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 582bcb11-9d09-3dd6-83f5-addf0fb3c779 | -14.08536 | -47.62656 | 2026-05-06 05:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acdfd3b9-8479-34fe-ab2f-2c67ed4823ef | -12.51043 | -58.47024 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 35d4463a-c5d1-3dfe-a92d-a088d7034db2 | -13.11275 | -51.72503 | 2026-05-06 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 875f3e16-e918-3e6d-8628-b1e998075f8f | -18.43384 | -54.70688 | 2026-05-06 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4734a874-38f2-3d35-a03a-2ce336ed11cb | -16.17193 | -58.49104 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4fcb6682-f1c5-324d-b914-fe0af268708d | -12.50582 | -58.4774 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a7358db-db96-33d7-bded-c3f193565097 | -13.69753 | -55.69295 | 2026-05-06 05:27:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05e7dd0d-1f4f-3793-9fb6-82e687a75e46 | -12.50927 | -58.47794 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d6c36f17-d744-36ce-8da0-67d392e3f26d | -12.5012 | -58.48456 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 987252e8-30b8-3526-9bd6-7a46f5d2623d | -16.59778 | -58.23761 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 92a32cc2-c295-3340-9713-078dbf0ed071 | -19.94458 | -54.38361 | 2026-05-06 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37c2e424-2c9b-3440-afb5-abc5029a5b29 | -20.21585 | -50.6481 | 2026-05-06 05:27:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3afe1820-b420-3d56-b987-c217bd8f5ff2 | -14.06782 | -47.79456 | 2026-05-06 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fec4f545-5f91-3061-ae01-fb27f7d0d62d | -14.8542 | -48.53896 | 2026-05-06 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 477d8730-ce94-3075-ab8c-3982d43a0f31 | -13.69498 | -55.68158 | 2026-05-06 05:27:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8da0c089-06d4-3ff4-95c9-3d2bfb592590 | -18.49834 | -55.51197 | 2026-05-06 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5ee53e82-4b12-39b8-9d62-673e473f0ab5 | -12.50524 | -58.48125 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ef81910-f130-3c7c-b00d-9cd5276d0afe | -18.43846 | -54.70747 | 2026-05-06 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78839b63-966c-38cf-9e63-6e0f862d68a9 | -16.15704 | -58.49299 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5e16ab28-c2e6-34ae-b56f-d48f3abf9c12 | -12.50236 | -58.47686 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcc95546-93ce-337f-827b-571899d61a5f | -13.11315 | -51.72182 | 2026-05-06 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d55d214-552a-3a01-a7cf-b45505ac40df | -18.29004 | -54.13343 | 2026-05-06 05:27:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55b44c6f-7c78-3726-b320-4bf6a834ff88 | -20.20973 | -50.64731 | 2026-05-06 05:27:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 127b19ec-feba-3630-b394-1c0763bec181 | -14.32565 | -57.73757 | 2026-05-06 05:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a983fdae-2292-30fe-b99c-43646aa4e0d6 | -13.69803 | -55.68936 | 2026-05-06 05:27:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76f7d022-5892-31e5-ae72-b5a2ebb26f62 | -12.29626 | -57.56355 | 2026-05-06 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 795146d2-7d5e-3ce2-8e14-609a5597d75d | -12.50294 | -58.47301 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f65a0ab4-1cc4-3173-a189-8109107fd206 | -19.26725 | -55.14456 | 2026-05-06 05:27:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 004120ce-402b-3a68-9622-37104b03cbc5 | -15.98725 | -56.22135 | 2026-05-06 05:27:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| a0aae49f-9602-3b89-99e9-81a0be7ac7e8 | -12.50006 | -58.46863 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e5fa4562-7f60-3378-9417-410b8d70caa8 | -16.42885 | -57.26778 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b4f8dbac-37cc-3411-92cc-37f0927f1185 | -13.69853 | -55.68576 | 2026-05-06 05:27:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1abca6d0-739a-30e5-97ac-c8ccad28f8f3 | -12.49085 | -58.48292 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6791418a-1ed6-3ff5-a033-1be39d3f2755 | -13.10791 | -51.72106 | 2026-05-06 05:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0dd7bec0-660a-3803-9120-b9d301855083 | -18.43694 | -54.71341 | 2026-05-06 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da69d149-610b-3690-a53b-0f35db991254 | -12.49718 | -58.48785 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 30c673d8-a5bc-35dd-bde5-bbdccbd193c5 | -12.29566 | -57.56765 | 2026-05-06 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0535df6a-c7b6-3244-9d47-a36c5a6d59bc | -12.49775 | -58.48402 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 343c7d98-5f2f-3f3e-bc35-a71e967f5129 | -14.079 | -47.6189 | 2026-05-06 05:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c516a5b-a49c-3efb-889a-e40cdf590ebf | -12.15623 | -57.75616 | 2026-05-06 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aeb280d-bd05-3542-bfc1-f5f97dfe0791 | -18.50272 | -55.51257 | 2026-05-06 05:27:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cf9f61af-22db-38d8-91fc-c4f134d2c7de | -18.43752 | -54.70837 | 2026-05-06 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cc5ee563-87cd-3fc3-9f8b-121500e3cfd0 | -14.08528 | -47.62544 | 2026-05-06 05:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42293a21-8ef1-3031-aa81-77afca90cf22 | -14.07912 | -47.62005 | 2026-05-06 05:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a21ad62a-56ea-3f19-b57e-802098e5eed8 | -16.24772 | -60.02323 | 2026-05-06 05:27:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acfb213b-c357-314f-a203-f43e7fc3159f | -13.99372 | -56.64187 | 2026-05-06 05:27:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 914b5d97-ca49-3669-92f6-5885bd3e78fb | -11.85673 | -63.72062 | 2026-05-06 05:27:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 161ad96c-5443-3d48-8bc8-3614807e015b | -14.07495 | -47.79216 | 2026-05-06 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b27d3640-6a28-346d-b62b-9065706d9459 | -14.0683 | -47.78996 | 2026-05-06 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8462eb7d-6bfd-3cdf-af54-54467868e3d2 | -14.86087 | -48.53867 | 2026-05-06 05:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 617d73a4-0766-3cec-8454-c3f01d08dbe8 | -13.69903 | -55.68216 | 2026-05-06 05:27:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67fd0e8e-d38e-3c93-a11a-567999cf118e | -18.43322 | -54.71191 | 2026-05-06 05:27:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 75b15704-2a5b-32c7-949b-acf6fca05bf8 | -14.02552 | -56.79009 | 2026-05-06 05:27:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 209311a6-463c-37dc-9965-a1a6dabf3271 | -14.02485 | -56.79484 | 2026-05-06 05:27:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a104b865-ae45-35d9-8261-0a6eb811f902 | -12.49372 | -58.4873 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a56048ca-574c-3730-9811-51c3ac6590be | -12.50352 | -58.46917 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e22729ee-a110-3756-8983-7a128677b3f2 | -12.6041 | -58.65969 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7321d16d-9df7-3a66-82fe-a35066087481 | -12.49603 | -58.47195 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a1d20b1-3681-338c-927c-ad918204ecf5 | -12.50985 | -58.4741 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 131c2bff-1a7f-30bd-bcb1-e1b7a9aaa669 | -14.07449 | -47.79654 | 2026-05-06 05:27:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6dd024b-1c25-3ec0-a862-98a38ee6bcc0 | -16.75729 | -51.87303 | 2026-05-06 05:27:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d5c7b57-b586-3add-9568-cfe50de1b7a1 | -12.50869 | -58.48179 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25529e07-117d-36ac-b543-caa24e1e61a4 | -19.94939 | -54.38429 | 2026-05-06 05:27:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e275f1aa-93f4-30f6-963b-ecf145f27c15 | -16.16061 | -58.49356 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 797cf503-74f2-3919-a980-089a6f564cc6 | -16.43266 | -57.26836 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 14d7d7fa-17ed-3e27-b5ac-c6cd96528936 | -16.59718 | -58.24192 | 2026-05-06 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1d124ca5-b474-348a-8608-c162e2b08021 | -14.08463 | -47.63176 | 2026-05-06 05:27:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 250afe7f-374b-36d6-be96-cf0f75be2d72 | -20.20929 | -50.65214 | 2026-05-06 05:27:00 | NPP-375D | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.6 |
| 25be3304-3c2a-3481-b7c1-df77f411a409 | -12.50178 | -58.48072 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6e9673d-58de-3196-84ac-7c026a717d85 | -12.50811 | -58.48563 | 2026-05-06 05:27:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 541c8dc9-2da9-3168-8efe-f1b21e49d255 | -16.75767 | -51.86946 | 2026-05-06 05:27:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0f055cf-d671-316b-ac23-edd808e6a72c | -21.70229 | -48.42447 | 2026-05-06 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1d44fb7-5408-3d74-aa8a-9228e9eeeadf | -20.7972 | -51.65729 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 06aedd3e-50ca-3afc-9a77-2ae16940c254 | -20.79099 | -51.66108 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9ca99031-ffa9-355d-9870-5d024dac2c50 | -20.7968 | -51.66172 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 3d987a04-aad5-3ed2-ad6c-30d65c6889b3 | -20.79736 | -51.66296 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.6 |
| 86ba5657-f4dd-3530-9be0-2f129b19c6c8 | -20.79156 | -51.66235 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 7d3dce6e-a2d2-305e-8c26-fa6b374704c0 | -20.7978 | -51.65854 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 06ac8e22-cee9-3daa-8334-89c6cb8f666e | -21.29651 | -56.10447 | 2026-05-06 05:29:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9664e1e4-8db9-3fef-a902-01dcb23885ef | -21.70555 | -48.42945 | 2026-05-06 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c1d81207-39fc-3ee1-a6d7-9b68e4350d57 | -21.97532 | -57.59533 | 2026-05-06 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 12b68388-d415-3b4d-a01b-4282f5ae4005 | -21.70608 | -48.42199 | 2026-05-06 05:29:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 274389cd-ef84-3baa-9a81-d988bc7da4c6 | -21.95527 | -57.59174 | 2026-05-06 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59ac2ff4-a18c-3db9-ab9a-77a949dc13e0 | -21.29599 | -56.10891 | 2026-05-06 05:29:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 774dd5a3-d10f-35dc-8de2-3f4bd2b3be05 | -20.7914 | -51.65664 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b06c2099-3b07-334b-80cb-62267b7720b4 | -20.79199 | -51.65793 | 2026-05-06 05:29:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| b9e4c12b-ed23-3d35-9d07-70d8ff5122e7 | -21.97934 | -57.59599 | 2026-05-06 05:29:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README11.md)
