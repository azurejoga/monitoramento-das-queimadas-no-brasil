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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c0ed579-0d1d-30de-9802-b0002aa9969d | -15.9232 | -59.34859 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8b3fcd9-a247-3ffa-96ae-3d8c361c063c | -20.98722 | -50.03364 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5fd851f1-b105-3f3e-8f82-97e056589bd5 | -15.76936 | -59.49773 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9307e62-6ae1-3f8b-8127-a7094995244f | -20.70642 | -57.85889 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 18f92a6c-dbc5-37d8-b542-ab66707eed50 | -15.75287 | -59.48565 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6520a520-6a5f-38ae-b766-03768089a023 | -20.76426 | -56.92042 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 805c4c92-f0c6-354c-ae4e-d821aa2fccbc | -15.8956 | -59.34803 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ea3c72d1-9406-3ba9-8952-6636ccea4cff | -21.83111 | -50.58301 | 2025-09-25 05:04:00 | NPP-375D | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 803d9920-d683-30b6-bc40-22bb14835b90 | -15.91052 | -59.34685 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dd8a206-f1c0-32af-9c39-33a2c991282c | -15.26856 | -59.43353 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb959e77-b17e-3f94-b9bb-5d2e3891b35c | -15.27293 | -59.42979 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef793b8c-8e97-3433-94b8-053380c568bb | -17.95696 | -55.85096 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e0c32d26-1f6b-32b6-9065-6c251cd7aa03 | -20.7358 | -57.85986 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 17a1e41a-9e02-3d0b-b44d-b8f138f98314 | -15.96914 | -59.51012 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 59e5b070-72b3-33dc-a8f8-41bc5c41c657 | -20.77821 | -56.91905 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3607c3cc-5b33-3e47-95c9-00413af976dd | -15.88273 | -59.42357 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2db1a39a-ad95-35ed-911b-cb1288a4a4fd | -17.93788 | -55.863 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 515b58e6-0019-3564-b847-6cb29cb3e445 | -15.81349 | -59.48195 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d8f3c67-7fa4-37e8-8f7d-a8bf3a356b86 | -16.85437 | -50.50915 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8920ef9e-a776-3691-a68a-5fbbdc0c21db | -17.93284 | -55.85075 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| d1ce812d-c6e9-364c-b5cd-0ed75c9c0aaa | -15.7608 | -59.48268 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ca6f7bcc-d9c6-3701-ac13-a6ef8ce20855 | -20.61387 | -56.715 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a1453a9-5a78-37f9-b918-58fef9b71bdb | -15.91762 | -59.34837 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d2c8eb8-19d8-3fac-8d68-b1bd6616b096 | -15.76591 | -59.47443 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 93721393-6b45-3795-808d-a68487b7e12c | -17.9418 | -55.85985 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| aab9a74d-718e-3ad7-b4d0-11a2af5271b3 | -20.46912 | -56.65293 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5352d894-dc69-31b4-8fc0-db4d7f5bed5e | -21.97099 | -49.50583 | 2025-09-25 05:04:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 89dd8824-cdef-3ef9-87b7-e016c2c2bcc9 | -20.98898 | -50.01814 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 32430530-d8d8-3e49-937c-bbbc11260235 | -17.94237 | -55.85614 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3e611752-45d2-3aae-9399-2fdd88345e44 | -15.25155 | -59.44158 | 2025-09-25 05:04:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00d4842b-cd7e-359a-bb7e-1ce3c9261a9c | -20.98746 | -50.4727 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 08b5e804-01d4-32cb-810d-b32f619edb77 | -20.98857 | -50.46284 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1045cc3a-636d-31d4-ba43-d9e61c1426d4 | -20.24237 | -56.0608 | 2025-09-25 05:04:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 699c41a1-9617-3281-8166-756e42d46803 | -20.97841 | -50.02705 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| d01e1fc2-c4ea-3c58-9deb-241517917608 | -20.99609 | -50.47863 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9fb4afd7-7e25-3ae7-b611-5a20e6df5d76 | -16.00596 | -59.48946 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc68c045-8bc5-3943-a965-e7fc8184e48f | -17.93395 | -55.86615 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| 97bdd828-5986-3f39-a20e-8f1b1ac23b36 | -17.95023 | -55.84984 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 83933713-79f6-3a6d-894f-b076a93b5800 | -18.8787 | -51.52143 | 2025-09-25 05:04:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5ed5ec6-d3fc-34d2-91b9-22ace6fdef6d | -15.75363 | -59.48122 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47cf1460-9914-35a3-98be-f5f53a5d7bd7 | -17.93731 | -55.86671 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 5ff16700-9b47-31d7-ad1b-7e3f2cfaabb5 | -15.802 | -59.48409 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98682b50-09b1-3a56-8591-9c2dd77c981f | -20.6925 | -57.86018 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 26da3fbc-3ff8-3e74-b459-f76ebc6cc86b | -20.76369 | -56.92414 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b051898-ddd2-340f-bae0-40a8f48eda90 | -16.84954 | -50.51265 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34396860-4f90-39dd-b2c8-a3ead9f63e9f | -15.36224 | -59.16898 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a360bc6-6d50-35fd-9611-770450e0c89f | -21.97591 | -49.5066 | 2025-09-25 05:04:00 | NPP-375D | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 0f3efaed-d7fe-3012-bba4-ff062a85c3bc | -20.97958 | -50.01667 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 8b7bcff1-5983-33ce-8bdf-8c73f8e973d6 | -15.88344 | -59.4194 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 342a6e1c-b4f1-381d-87c1-5b43aa664ecd | -15.76863 | -59.50201 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 31bbc872-57a5-3112-9bd5-2398097d4d51 | -20.70232 | -57.82005 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d3843b53-f549-35b4-ac40-7e6018bed91d | -20.77487 | -56.91846 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f6452ba-dde4-3f81-9f45-e4daa621fb11 | -17.93451 | -55.86244 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.6 |
| cac60e11-041f-35f0-922c-45651fc11f16 | -20.9878 | -50.02852 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 604f4ff5-fd2a-3b10-9cce-8e32fa6939ac | -15.89204 | -59.34737 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 26e3c175-13e9-3431-8c97-b22ae12461e4 | -15.76669 | -59.46982 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2733b962-3acd-3c67-812b-b771dd01dec1 | -17.92891 | -55.8539 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6dc765a6-9846-3565-8a85-bef4220a1f9f | -20.77764 | -56.92277 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 667d867b-5430-30ff-8556-5c518442ca47 | -17.93002 | -55.8693 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| eb6a537e-7074-3949-aebe-90aa1dc98280 | -17.92947 | -55.85019 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.4 |
| eb7e5cad-9347-354b-a064-4c74e96d746c | -20.99663 | -50.47378 | 2025-09-25 05:04:00 | NPP-375D | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| cfc60a68-999e-3e5c-be77-7271e728fbd1 | -20.78099 | -56.92334 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4a8fc70-5ee1-34c5-b81e-6fc3af0bac4a | -17.9564 | -55.85467 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 891e9d55-41fe-350c-9841-3eeb9d1da886 | -17.93228 | -55.85447 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 3e62026a-5c2d-3961-b509-ea6e955c3e5d | -20.7025 | -57.86199 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7f636e37-1cce-328a-8369-e54d89a9c612 | -20.4719 | -56.65724 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42197d1d-9f56-36f2-99c2-272c6a50c6e5 | -17.94068 | -55.86727 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 92599251-f9e2-34ba-804d-084740a96b79 | -15.87346 | -59.34846 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b75e9c9-1936-37c6-9e05-a1e4bea5cbf0 | -15.3658 | -59.16964 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f0429db8-8044-3d93-a958-97efdeade7c2 | -17.93844 | -55.85929 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| eea2522f-a9c6-3603-9ed1-63475e64c586 | -18.87455 | -51.52081 | 2025-09-25 05:04:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc05056b-e4f0-3a76-b808-592d32d84aa8 | -15.35297 | -59.18026 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 362a10fb-1bfb-3bac-8bc5-31ee507f9701 | -21.00724 | -50.02572 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2eddefe6-4315-3fd7-a9ef-ab8f047703ad | -15.82659 | -59.59952 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3792c00-37a3-3aa2-ade8-f64aec0565ac | -20.98427 | -50.01742 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 695b0649-d582-3deb-8d7f-e59b2dc2060b | -20.2428 | -56.05787 | 2025-09-25 05:04:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 58b74518-d5c0-3e23-a85c-1878fca79b0a | -15.80559 | -59.48477 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 964c93e0-5f02-344b-bb77-5c52f90e21c8 | -20.69976 | -57.85769 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 878f3f43-4daa-3892-9f72-799f697fc582 | -21.16268 | -49.71942 | 2025-09-25 05:04:00 | NPP-375D | UBARANA | SÃO PAULO | Brasil | 3555356 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6446b661-bfa8-3084-87e4-a18607584f18 | -17.93564 | -55.85502 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5486399f-3018-3231-8a49-bb97b345015f | -15.35367 | -59.17612 | 2025-09-25 05:04:00 | NPP-375D | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ad91ed5-9bd7-302a-91ed-cd105b150b4c | -21.00665 | -50.03093 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58c84f00-97f7-3479-9f2b-6df74d394581 | -20.79925 | -56.96097 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965d2928-6b3d-3edf-bb45-d099b280a9b6 | -20.76838 | -57.82764 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| d6d99764-a2a6-36e5-9dfe-7c76b7419b82 | -20.99898 | -50.01431 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 3bae530b-dde0-3010-95ab-76fe79fe1771 | -15.75646 | -59.48638 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| afdf04ac-9a60-3828-a273-51cc174c43af | -18.18556 | -53.33651 | 2025-09-25 05:04:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0dddbf0b-999b-3c0a-a190-9e4ab919f6af | -20.73914 | -57.86047 | 2025-09-25 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 7ef0f395-fc26-3d30-95a8-ba3551a87b1f | -15.88197 | -59.38485 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d59c6361-d6cb-3e98-a685-674ab7ec1782 | -20.76034 | -56.92355 | 2025-09-25 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8660edf-5aa3-3ea5-b52d-e7260b3b2ad6 | -21.00014 | -50.00407 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0afb4a0b-75be-3ce3-8027-1fe970d48555 | -20.979 | -50.02182 | 2025-09-25 05:04:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| ae2a0990-50ec-3d93-9e27-8baf71e6cb46 | -15.77082 | -59.48917 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 927df88b-2dc9-3f43-a3ac-2f14518f1a6e | -18.95503 | -49.58064 | 2025-09-25 05:04:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaa75d97-1401-3b3d-aa36-c8a535ed18a4 | -16.85868 | -50.50977 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| afd56678-36e3-3fed-848e-44a34bd36b21 | -16.85814 | -50.51397 | 2025-09-25 05:04:00 | NPP-375D | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 968c761b-96ad-325a-bf7d-0db69de937e5 | -20.70431 | -56.74186 | 2025-09-25 05:04:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfa0d661-be09-38cb-b31c-e263fe1312c1 | -15.89344 | -59.40403 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b4ac6c0-33eb-3698-8750-4ee55b33489c | -15.90343 | -59.34526 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ba4818a0-ece4-3f64-9550-c19e9265c252 | -15.88986 | -59.40343 | 2025-09-25 05:04:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README32.md)
