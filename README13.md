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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a606a232-2ac5-3edd-ab19-1e841c5ffa44 | -21.67856 | -54.84824 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 572721e8-e57b-3fc7-8aab-78a161a19cc2 | -21.67682 | -54.83719 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 3628cd9e-40d8-3d3e-967a-e546a265ae96 | -21.67077 | -54.861 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 2aab866e-cb19-32e4-bf7c-556c6c49f91a | -21.66903 | -54.84998 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 152.4 |
| ed2a2e1b-cc31-364e-932f-b6ad185ceb4d | -21.66728 | -54.83894 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 114ce3b3-4daa-39d8-a81d-92fc650f2f26 | -21.66599 | -54.85632 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 8c758961-38c6-3110-a43d-dda2c7718dc9 | -21.66429 | -54.84528 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 31.2 |
| ee507388-3453-3655-a4cf-f2149e1354c3 | -21.66259 | -54.83422 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 25.4 |
| e6222229-6e09-3d6a-a57b-e62310107f7b | -21.65646 | -54.85807 | 2024-09-30 01:41:00 | TERRA_M-M | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9fe96da5-223e-3627-97fe-95afa8f0e652 | -21.62952 | -47.80392 | 2024-09-30 01:41:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 272cfdd4-5ff9-39dd-94b2-664517fc6962 | -21.62008 | -47.81301 | 2024-09-30 01:41:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 1376b23c-2188-33d3-92cf-2928c3774117 | -21.614 | -47.8077 | 2024-09-30 01:41:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 40.0 |
| be01594e-68d0-3b8e-8c9f-16b024d8075f | -21.59136 | -47.75067 | 2024-09-30 01:41:00 | TERRA_M-M | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 71ce5c02-2c8e-3da0-aa00-5a17879e29e2 | -21.36908 | -48.49713 | 2024-09-30 01:41:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 286b8ffa-b197-3a93-9ceb-89ce6495f565 | -21.36692 | -48.49118 | 2024-09-30 01:41:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a730cbbb-8847-3f9c-a6b9-10ec3a5bae91 | -20.31889 | -46.65775 | 2024-09-30 01:41:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 57d0747c-fc66-383c-aa39-d2eb419bcab9 | -23.59839 | -54.34926 | 2024-09-30 01:41:00 | TERRA_M-M | ELDORADO | MATO GROSSO DO SUL | Brasil | 5003751 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3362e2f6-3c49-300b-be2c-f051bf882453 | -22.24915 | -49.67324 | 2024-09-30 01:41:00 | TERRA_M-M | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| cf12e904-d8c2-3187-9eed-1cd4748767ff | -16.46572 | -57.40297 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 00b46f0b-3c72-3aa0-9650-88eab632152f | -16.46497 | -57.3344 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 34471cc8-aa29-3951-9c8a-bbf70b89f1e8 | -16.46153 | -57.37424 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 561f0745-77e2-3434-9ccc-6def6843f051 | -16.45733 | -57.34546 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 027e7b4b-6fa3-3ed8-a0c3-9dc951eda4fe | -16.45593 | -57.33586 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 19470f05-8178-3023-be38-ae7ce2580ae1 | -16.14871 | -55.43806 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| cbd2eb2f-598c-39a3-9f7a-4d61ea7b214e | -16.10679 | -57.5339 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 53e23566-9256-3ec2-85ac-f4d5b34e9e0e | -16.10545 | -57.52467 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b5c24b12-ac4d-33c0-837a-be4038211f85 | -15.92805 | -57.19025 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3b313399-c75a-32ba-b669-6d27004baaae | -15.92659 | -57.18018 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| cf3dc255-723c-3cbe-86fe-a43a9f059e7f | -15.91929 | -57.44903 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87633e78-ebd0-3bd9-b12d-994ce97da0d9 | -15.91898 | -57.19218 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 785915af-7279-3316-b816-a86c8f9e0ad7 | -15.91789 | -57.43946 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 79c9839e-3720-35b0-8071-609296c3fea2 | -15.9175 | -57.18196 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 1b37691b-d0cf-3683-8a35-743248983bdc | -15.91266 | -57.21276 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2319c6df-7922-3604-b20b-bfe2cb5c4a3c | -15.91127 | -57.20328 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5ad28355-cb0e-3234-8ba2-4839eee43cfa | -15.90883 | -57.4408 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8569abd5-b848-3faa-8bad-5ccf5ceadf50 | -15.90841 | -57.18375 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 901bf9bc-844c-3966-b134-094fb5ef4029 | -15.90356 | -57.21436 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4cd904d1-10cc-3564-961f-af6efa0667b0 | -15.90212 | -57.20457 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5efcbea7-158c-3345-8a3f-a36446ee21bd | -15.90072 | -57.195 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7f4e1ff6-fbc1-37fb-8293-8b6806f2616c | -15.89717 | -55.40404 | 2024-09-30 01:43:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8665d11c-fccc-329e-836d-cf18a22b5392 | -15.82792 | -57.39179 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 119dbedc-7443-30d9-bcdd-b849be83422b | -15.82654 | -57.3823 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6da37719-52f4-3d63-81b4-24b1bd8ec2d1 | -15.8188 | -57.39282 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 752ed791-2c14-3ea7-a09a-6cd01bf9c388 | -15.81743 | -57.38348 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8f40eddb-4426-3a54-9392-c2924bca9378 | -15.81317 | -57.35439 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7109d112-2d56-33f8-b640-be99a9464d13 | -15.80556 | -57.36586 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ebab568d-6572-37f0-b2dd-1eaf3c067c5e | -15.78487 | -57.79305 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| baea4048-0288-31e3-97ff-5632b1216750 | -15.77726 | -57.80386 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 008cb74d-1064-301c-8bb4-d6d190600508 | -15.7759 | -57.79446 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 33934e2b-5d68-32bd-b78c-7dde998d4050 | -15.77454 | -57.78506 | 2024-09-30 01:43:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e996d300-f16f-30e2-acc1-04222fca5ba1 | -15.62639 | -57.4649 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1020ee83-a2de-3040-bbf2-b66a3f8baa86 | -15.61733 | -57.46635 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| de377237-4e3a-3956-83f1-0b2000eb2b55 | -15.61592 | -57.45674 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a38d2202-eb7d-3fb0-8042-08a336e5f474 | -15.60685 | -57.45818 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| d21d7c4e-a6cb-3ba5-9cc8-20ffa250f38a | -15.60543 | -57.44857 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9ca09468-d01a-3938-ad55-7498e26277ec | -15.59786 | -57.4557 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7063621f-976c-3a0c-a520-e3568a821b6a | -15.59647 | -57.44608 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| da62b5c8-3200-39f0-b912-d40057911d5c | -15.58879 | -57.45716 | 2024-09-30 01:43:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b6829c2f-3be7-3681-8ec8-645a3dbe3261 | -15.56357 | -56.91332 | 2024-09-30 01:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 2e938845-7ae0-327e-a83b-67873cbf199e | -15.55438 | -56.91525 | 2024-09-30 01:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bb9f7922-b9a9-309e-9270-e6e19d5b1710 | -15.55284 | -56.90492 | 2024-09-30 01:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d181b495-9b1d-3894-ae1d-b012859e56b5 | -15.54515 | -56.91686 | 2024-09-30 01:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 074f3a80-d09a-30c2-8340-efe877b70b2f | -15.54364 | -56.90679 | 2024-09-30 01:43:00 | TERRA_M-M | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d8ee8be4-87ac-33c8-b772-6abf5d9f990e | -15.36859 | -58.1661 | 2024-09-30 01:43:00 | TERRA_M-M | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c4cd5f3-47c2-38dd-b0ac-db2171a26aea | -17.0626 | -56.75371 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| f929d15f-3b17-3744-a4c3-201798b7f085 | -21.01533 | -57.51891 | 2024-09-30 01:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 82ff4f81-5535-3064-94ba-b50aa7048415 | -21.00646 | -57.52036 | 2024-09-30 01:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 36f071fe-6c6f-310c-9fa8-fa82b490db68 | -21.00514 | -57.51091 | 2024-09-30 01:43:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 4eb1ec0d-a14c-366f-b92e-2b9869d6a9f3 | -19.14974 | -57.4813 | 2024-09-30 01:43:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| cbb5bf16-ea42-3fc0-8d7e-23c84d5a3509 | -16.10982 | -50.36292 | 2024-09-30 01:43:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 46b76a0c-afeb-3db3-926b-960ab61ec030 | -16.10919 | -50.36856 | 2024-09-30 01:43:00 | TERRA_M-M | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 59f90c67-3f8c-36f6-a26a-482507fad806 | -14.75899 | -48.75543 | 2024-09-30 01:43:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 8b7ed87a-6fd6-3ef8-888c-2a79fb5797cd | -19.98203 | -55.49943 | 2024-09-30 01:43:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 57242a3d-60e5-3020-b60a-904eae2fed73 | -19.98042 | -55.48894 | 2024-09-30 01:43:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8a606632-40b7-3c0b-832b-cbe82cc03a94 | -19.97254 | -55.50067 | 2024-09-30 01:43:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f8c0c662-75eb-30db-947a-d2700cb35216 | -18.65167 | -52.48253 | 2024-09-30 01:43:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 705d8df5-b454-35c9-bdf0-78a20d5d044a | -18.45691 | -50.16108 | 2024-09-30 01:43:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| 504bdcce-534a-3a09-9767-72a3afa5bad3 | -18.4535 | -50.16728 | 2024-09-30 01:43:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 44.1 |
| 6ad1ab6c-35db-3310-868f-a95dea3abc5b | -18.45195 | -50.1349 | 2024-09-30 01:43:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 22.0 |
| 8a497264-5770-3612-b9a3-63d02d13b607 | -18.44874 | -50.14116 | 2024-09-30 01:43:00 | TERRA_M-M | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| 44f73b7a-5e1f-3b71-8298-1e58b2b7185a | -17.25714 | -56.45478 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 782d5a8e-e4e7-3ced-814d-a5f96230ecc8 | -17.15108 | -56.23515 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 25.8 |
| bc389548-0cbd-3bac-b23b-68aaef880c66 | -17.14794 | -56.21418 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 313838f5-fe9a-33b9-b675-3053e1e14129 | -17.13853 | -56.21577 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| e55828ee-14be-35c2-b655-1c2c9ecb0e5e | -17.13379 | -56.18428 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 7b8a5a42-2594-365c-97a0-8f64280b60d1 | -17.12596 | -56.19637 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| c38de011-41e9-30c9-aa1e-ee5d0c565691 | -17.12437 | -56.18587 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 40.1 |
| 63399487-1330-3ac9-882e-21a938c6d4ce | -17.12277 | -56.17532 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.7 |
| 399b3f3d-b633-3362-a5e3-c27c4f512ab0 | -17.11972 | -56.21895 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 0b998be0-4907-3e0a-8963-bbd4465fbf19 | -17.11494 | -56.18744 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6d0bd187-079e-3740-a971-739646e0bda1 | -17.10753 | -56.39146 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 56aa62f8-33cf-3695-a581-555be61e52e8 | -17.1058 | -56.74025 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 169ca819-2d4a-367e-a92a-c9fea3f2fe7e | -17.1024 | -56.3981 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| d3069605-ae12-39ba-aa8f-f1674ccd0ef8 | -17.10088 | -56.3878 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| bda675e8-2605-3d85-9eea-cefb09d64a20 | -17.09661 | -56.74176 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 059032cf-b021-374a-832f-07f4ee4016d4 | -17.09512 | -56.73178 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1fda0d92-4789-3935-a6cf-b681dc7964f1 | -17.09154 | -56.38936 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| ee725de7-3e88-3c8e-a018-b77917333e5e | -17.08067 | -56.38061 | 2024-09-30 01:43:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 5773fc15-b0c9-3a00-bb99-7a62751c1fef | -17.06904 | -56.74631 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.1 |
| e3623345-d359-301f-808b-ae7643acc106 | -17.06754 | -56.73634 | 2024-09-30 01:43:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |


[Clique aqui para ver as próximas entradas](README14.md)
