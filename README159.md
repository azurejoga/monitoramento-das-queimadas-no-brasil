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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 440bdf4d-fe32-3ee9-a1a9-b6f13dc20421 | -12.1476 | -54.26583 | 2024-10-04 04:57:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60d73a67-28fe-35ab-803f-9609f7995e7f | -11.58765 | -54.48226 | 2024-10-04 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d95e66a0-2ff1-3a5e-acde-3c86f7ae9726 | -11.5871 | -54.48581 | 2024-10-04 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b71419e5-5c7a-3fe5-8ac7-82e09a35cc2f | -11.58432 | -54.48174 | 2024-10-04 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c11277b-39d0-38f9-b7ae-153568eba4a5 | -11.58378 | -54.48529 | 2024-10-04 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 25dab6e4-b093-3122-8e74-99f288a7bde8 | -11.37631 | -55.23133 | 2024-10-04 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 736157ec-2a02-33f9-8212-6d3de6d0a7a3 | -11.35129 | -55.19472 | 2024-10-04 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6734deee-00af-32e6-9489-ec583741fd07 | -11.35074 | -55.19822 | 2024-10-04 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1da3765e-f95d-36bb-be8d-658b1747619d | -11.31877 | -55.20744 | 2024-10-04 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5dd9dccd-fc7b-3ac7-b26f-f611cbfa9e13 | -11.21066 | -54.74813 | 2024-10-04 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 51353554-548a-3bb7-8c67-fbf99f9ae7c2 | -11.20735 | -54.7476 | 2024-10-04 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3835b6da-e0d9-3e4b-a343-1960219d0e6d | -11.18909 | -54.75523 | 2024-10-04 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5651c3bf-a039-311f-88af-97f364cabcf9 | -11.18855 | -54.75875 | 2024-10-04 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 86bc4940-f74d-36e8-a6a2-2c24c619bbe5 | -11.18578 | -54.7547 | 2024-10-04 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6dc26928-0064-3a1f-b4cc-c3ed37131e07 | -11.18523 | -54.75822 | 2024-10-04 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 85f6cd56-5b0a-37c2-a8c3-ca4f9b54b00e | -10.99884 | -54.25139 | 2024-10-04 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 212cb014-d43f-3c27-bade-c2fc8c0187f4 | -10.99551 | -54.25088 | 2024-10-04 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 3ee626b5-b173-36d5-b14b-71c682517dba | -10.93177 | -54.24825 | 2024-10-04 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecedd7c5-7d09-3acc-bef0-cf78e5b45781 | -10.93122 | -54.25181 | 2024-10-04 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab23e6d1-bf98-3368-9ba8-a51a2dc9a9c3 | -16.58521 | -56.05348 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7c3347ea-b22c-39c6-be1a-576ee5ef34dd | -16.58245 | -56.04933 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c69200bb-c53b-35ae-8a8f-4928e7779f59 | -16.58091 | -55.92718 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 20cee0f1-b8cf-3174-a6ee-c4104749fb26 | -16.5798 | -55.93439 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b002025e-4ec8-3a6b-b60a-a059f8843a7f | -16.57648 | -55.93384 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ba5b4ad9-6240-3c2c-9592-e560d1ba90dc | -16.57151 | -55.92192 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 869621eb-8ed9-3228-9a22-a59579da0d15 | -16.57094 | -55.94772 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aa6e8a5e-73ce-3a87-8ca5-169cc575cd08 | -16.56819 | -55.92137 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 725851a6-77b7-31a7-9f1c-aa43c4d51759 | -15.39419 | -55.85462 | 2024-10-04 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 618d67d3-9dc8-3640-a8aa-0c46f019640f | -15.39088 | -55.85409 | 2024-10-04 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d7e4c86-e93c-3736-8e1a-160ee8540390 | -15.38757 | -55.85355 | 2024-10-04 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de9150d9-da4a-399f-9f2e-f39f83185439 | -15.36274 | -55.83828 | 2024-10-04 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85c038b3-0ad7-332c-991a-36c7e67d8f26 | -16.71986 | -55.46598 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0c0c659a-86ec-3104-8ea7-02d921973827 | -16.7193 | -55.46966 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b6fbe04a-4c84-30ca-885d-7eadbad29f8b | -16.71652 | -55.46545 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 892a949e-da4d-3854-836e-10a4012741d8 | -16.71374 | -55.46122 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e7c148c9-3120-3c0b-900a-4399661739a8 | -16.71317 | -55.4649 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 50b4172f-0cd1-3685-9db8-680429f8d0e6 | -16.71039 | -55.46069 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b201fd63-7427-34c6-b18a-10c436772b65 | -16.70927 | -55.46805 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 700857d0-9288-30f9-88ca-c961f19c6dfa | -16.70649 | -55.46383 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 60908c60-ac58-356c-b001-1dc27bceaeb3 | -16.70592 | -55.46751 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2e364312-c271-3fa1-8ece-3004a2bd94e3 | -16.70314 | -55.4633 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fc8ce0b7-6cd4-3532-b072-6fea7c894454 | -16.70036 | -55.45908 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f90adbd7-a559-3320-a84c-4e6d1c6df9d3 | -16.69702 | -55.45854 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fe00fc00-5994-3487-ac84-7ede70942de4 | -16.69645 | -55.48474 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f3930ee7-7371-38d1-9c77-a04f1af3c359 | -16.69589 | -55.48841 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8237b0fa-b3fe-366e-ab61-95d3f03a66a7 | -16.69367 | -55.4805 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 63b49451-91f1-38fe-88c0-799ca2768fcd | -16.69312 | -55.46166 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| aa4a6896-9009-3b70-863a-b07725e1b077 | -17.04419 | -56.70188 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 47334e17-c53d-3d82-ad32-dcdaa2f411f9 | -16.69311 | -55.48417 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bf44dcff-8d57-3b5e-93df-80fd5861ad77 | -16.69256 | -55.48785 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d5e43a72-2147-314a-8962-5e0af9ed1eb3 | -16.69256 | -55.46532 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7ca82275-a915-326a-9a2b-b1ae9e379bb3 | -16.692 | -55.46897 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| aa4b4cdd-0caa-3e04-a0a8-ac462b1d3ac3 | -16.69034 | -55.47994 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7606821a-0a2b-3243-895d-8b140b8915da | -16.68978 | -55.48361 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c0149d35-af14-30dd-944c-d6aabaef0b51 | -16.68922 | -55.46474 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 785c8939-d63a-3d4a-a32c-bc58fb252bd8 | -16.68867 | -55.4684 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6334f809-12d2-3469-be4e-358f3ad212a7 | -16.6881 | -55.49463 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4c193c8f-8aa6-3edf-a557-2775fb7aa320 | -16.687 | -55.47938 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a53e68ac-6fa5-339c-8009-160af4e9575f | -16.68533 | -55.46784 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 2cc620c7-4227-39d7-966e-9f2fc473432d | -16.68476 | -55.49408 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 70f7504c-5e95-3f29-8b05-0b93692ae425 | -16.68421 | -55.47516 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| a4bc0987-e813-3699-89ea-8b57383387c8 | -16.67419 | -55.54099 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7e9cd6ba-231b-3f92-8251-78be508f8ad2 | -16.67307 | -55.50341 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1a89a7ca-8302-3130-a90b-9932ba765b63 | -16.67251 | -55.50709 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 34077fa5-2224-35b0-b9d6-cc25a00a5c39 | -16.67141 | -55.53681 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e77363c8-fbeb-3aca-982d-b6006430c5e6 | -16.66918 | -55.5065 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6ab1b0d9-a654-38be-97cc-a324153d2292 | -16.66862 | -55.53264 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a0ba6113-8674-311d-902b-561ad10ab9c9 | -16.66751 | -55.51747 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 25e3ca2c-f2eb-3b8e-9399-b3d0e6f37bc0 | -16.66696 | -55.52111 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9bab32a7-2d15-3e7f-a92c-62dea8d9fb8e | -16.6664 | -55.52477 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ae6a04ae-2a7d-36f4-8a20-56752db387db | -16.66584 | -55.52844 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 16ddaab5-923b-31b8-aa73-497f265cda74 | -16.66584 | -55.50592 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 17a08591-21a5-3f52-a25b-2af3bce9f287 | -16.66529 | -55.5321 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 87fa67ce-d04d-3743-9910-7d7d4c378188 | -16.66529 | -55.50958 | 2024-10-04 04:57:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 8cfce396-5874-3d59-a15f-dcf00e853b41 | -17.15407 | -56.15116 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6001315e-71ff-336a-8d3e-7603f7f2f71c | -17.15351 | -56.15477 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f7fa7da7-06ed-3fe7-a3b0-4b4e7ec3cb7b | -17.15183 | -56.16561 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6f8b25fa-84bb-3f32-ba3e-cfb55d46af33 | -17.15127 | -56.16922 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5ad57fc7-e79e-3435-81f2-fc82261139a4 | -17.15075 | -56.1506 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d98ee4b7-4d6e-3a24-8a24-93e8401e4c44 | -17.14964 | -56.15783 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 0a275c84-a2ef-38ed-9706-12fca30fd4a2 | -17.14907 | -56.16144 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 21f159d6-80c4-38e8-baa9-208be7628de8 | -17.14852 | -56.16505 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c5ebc4d7-4a0a-36b9-80b6-65af2ef37c0b | -17.09773 | -56.09733 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| eb293aad-8ffa-32dc-a646-df656923af9e | -17.07861 | -56.0904 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9787519a-4160-3fe9-a05f-6daab1a72721 | -17.07033 | -56.07789 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 84fef843-0dcc-3d92-a4b8-a3168bfa023e | -17.06977 | -56.08151 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 7b570867-84bd-3723-8eb3-5baead2188c8 | -17.06701 | -56.07734 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 45cd9320-8a56-3042-9682-c23d8a7757b2 | -17.06646 | -56.08095 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 217e1b14-3dfc-3cf0-88e6-64908026ad61 | -17.06426 | -56.07317 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6aedb8b1-07c8-3359-b5cd-0073f92e7d5a | -17.0637 | -56.07679 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| e771520c-cf5a-36e3-bdea-9ffdbccedc86 | -17.06094 | -56.07262 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e94b912a-31cb-30fa-8d37-2d89b85d1213 | -17.06038 | -56.07624 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 7aa36a0d-e859-3edc-ba86-dd67da6c851c | -17.0565 | -56.0793 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9bfd75ef-1dc8-3df3-a94e-6fff47655303 | -17.05594 | -56.08291 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8e3ac716-a624-31aa-a5ee-5661963fab1d | -17.05582 | -56.69279 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b886c921-ec03-37d6-ab41-a054aa6387e0 | -17.05525 | -56.69638 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bb6ebf1d-073b-3a9d-9a96-0ec2995de305 | -17.05374 | -56.07513 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 630ddfd6-341a-3d5b-9120-bc243425825b | -17.05318 | -56.07874 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1d6df45a-3fd4-3d2e-a98d-1e7ccc8397d5 | -17.05042 | -56.07457 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7dbe5b4a-0402-3691-8998-a7a0d9f6ab8d | -17.04986 | -56.07819 | 2024-10-04 04:57:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |


[Clique aqui para ver as próximas entradas](README160.md)
