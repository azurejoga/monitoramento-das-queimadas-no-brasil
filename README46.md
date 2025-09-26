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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72ac17b7-63b0-377c-939e-1ca32369003c | -15.26873 | -51.46886 | 2025-09-26 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7cd7cb4c-28cf-308e-919a-47c441734ac1 | -14.60018 | -48.25855 | 2025-09-26 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7743f71-88df-3870-8502-5e43fe7d1dc3 | -15.99601 | -49.03178 | 2025-09-26 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 75e491b8-7dbc-3cad-83d2-68351046b477 | -14.10495 | -51.16158 | 2025-09-26 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ce8403e-8005-37be-94ca-4bda1a5df95d | -15.73006 | -59.5006 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4756fc38-3d3f-3624-837f-2c0a67a98dc8 | -14.57438 | -51.40842 | 2025-09-26 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b880b9f2-7272-32b9-8291-463992bc1004 | -15.0211 | -46.93872 | 2025-09-26 05:06:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a471fb4-b6c6-3d21-91e2-a06dc97efc6a | -15.27415 | -49.47962 | 2025-09-26 05:06:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d164315-a637-3487-aa9b-eaa8c2eb66b1 | -15.83221 | -59.60407 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f9b4c87-46bd-35cc-9c58-168a3f9ac192 | -15.7273 | -59.49625 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0f8a7cf8-6e5b-3e4a-9926-1c54920c5a2d | -15.88744 | -59.39691 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4cf0b2a9-88d3-369c-81d7-777dbcfd3f3b | -17.18204 | -56.36577 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e8bb59eb-3137-3a6f-bb5e-cbe3fa855186 | -17.58627 | -51.81961 | 2025-09-26 05:06:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f08b681a-9978-3194-917b-f7ad32b66e55 | -15.97803 | -59.48569 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11e33dec-e34e-340f-b21f-a3307acae36d | -15.5163 | -50.42717 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8a6c4ae0-2970-36ff-b769-2b915e274bbb | -15.92344 | -57.49837 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db91c180-0834-3848-8f1b-bad92725d349 | -16.40444 | -54.8268 | 2025-09-26 05:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e05405b-266d-365f-b0ad-b0c984d0f963 | -15.91349 | -57.49671 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1130998b-73cf-3038-bdcc-c0b6b5fb3a6b | -17.94157 | -55.87621 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d0b987de-d10d-3ab0-90f7-ebd6ff35ee74 | -14.94665 | -47.50087 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26cde74f-9e5b-3b91-99b1-ce2517d0fb02 | -15.88651 | -59.38149 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 180ab769-fe04-3ca0-9c7b-071e0b97fc98 | -16.85583 | -50.5008 | 2025-09-26 05:06:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 944bf8fb-65b4-3a4e-97ff-49d6bceb6536 | -14.59825 | -48.25884 | 2025-09-26 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba4f403c-7af3-3ec7-a851-b706371e4809 | -15.26967 | -51.47213 | 2025-09-26 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2520389a-4e23-33e8-9113-2f34c8d872e8 | -18.55567 | -46.96467 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85fd5ab7-a08d-3c60-b754-0a6ba8ab2d14 | -15.23762 | -48.0857 | 2025-09-26 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 509fdd80-1081-35cd-a7be-73a258cb6518 | -15.06481 | -44.99104 | 2025-09-26 05:06:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d4f9511-7f89-37c9-85e0-0e83419aeabc | -17.02882 | -52.24118 | 2025-09-26 05:06:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41a66b96-5d56-311c-b40c-12fbc72c110d | -17.1792 | -56.36139 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f01fd5ae-ed8a-3910-adac-c423235638c1 | -15.99636 | -49.02863 | 2025-09-26 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d729a384-c0a5-34eb-819a-2709e7ccc6cb | -15.90063 | -59.3379 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7202e5d-d108-356c-be98-bebbd1c43509 | -15.5731 | -51.68985 | 2025-09-26 05:06:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83384bd8-b23d-30ae-af41-cc81f7aee154 | -15.38442 | -46.11681 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c26aa68d-b639-3eba-9920-7728dfbe34cf | -15.87644 | -59.33751 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71131194-6fed-33d6-abc6-6b21f63c8a77 | -15.91404 | -57.49315 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e7acad7-3755-37b9-982e-48aafe4e39ef | -15.99497 | -59.48837 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3eb5e3ab-4a65-30dd-a873-9bb237ed8709 | -15.94344 | -59.46374 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53a5f4fe-b6ab-3106-b347-b25f50ab2266 | -15.99441 | -49.03055 | 2025-09-26 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 913257eb-32b5-3a87-a946-688cb4338d0c | -18.54849 | -46.96572 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 041b21cb-9405-382f-8e53-879a634552fa | -15.88777 | -59.41597 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d68f0aa1-ff8d-3f00-a349-bf1133e3aa19 | -15.93989 | -59.47942 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 723ebe34-940e-30b4-9967-34e9b47b7e8d | -15.51373 | -50.4285 | 2025-09-26 05:06:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 591da34c-7e7c-349c-9c2d-20ab189e65aa | -17.18319 | -56.35809 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d82f7929-ffd8-35da-bba3-0714793007ee | -15.2702 | -51.46784 | 2025-09-26 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3194467-9c9a-3382-9061-221d739598d6 | -15.93741 | -59.49466 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d8f2266a-e884-343c-9ea7-ca5ae7611447 | -15.63205 | -53.62337 | 2025-09-26 05:06:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fff7901-d689-3992-8057-aebf3f5809c7 | -15.26438 | -51.46824 | 2025-09-26 05:06:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c26cc1f8-04c1-3401-9bac-87b1c9ac1a9d | -14.10552 | -51.15728 | 2025-09-26 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3516ccd-7498-31ef-871d-dd80b3a6776a | -15.93961 | -59.48669 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42df5522-d565-3cbf-8b51-1b58bad7bca5 | -15.93772 | -59.49803 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f223f68c-1eeb-34e6-bd99-8ac4a2ade169 | -15.38972 | -46.11512 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a027d27d-ab3b-33fc-be45-c92c79b65a90 | -15.98544 | -59.48296 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6c8463d7-9c4b-3d79-83f9-38cb09d7a20e | -20.01965 | -44.24201 | 2025-09-26 05:06:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c5a6db77-a5d8-3df6-8e15-2fb694d7d1b9 | -17.18261 | -56.36193 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| edf7d4d3-6379-357d-b714-4511e8d2062d | -15.94089 | -59.47905 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1d12126-456b-3937-b9b4-bccfe7bd1c51 | -14.59485 | -48.25779 | 2025-09-26 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 581a0d72-a2d8-3375-bc06-0b2c3353cdf0 | -15.238 | -48.08241 | 2025-09-26 05:06:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e614bf34-a6b0-38e5-b133-20a540f23219 | -15.88408 | -59.39627 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f19376b0-dd5d-348f-a07e-017aafdee61b | -18.31328 | -57.10534 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3f288368-8bd5-36da-b34b-e7912c17b608 | -15.88379 | -59.33495 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efdb4c6a-669a-326b-ba63-6b98ccd990bd | -15.82756 | -59.61102 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b35e973-740d-31b5-9496-a02b0a91ab13 | -15.26567 | -59.44107 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da70be5e-19d7-371c-b9f9-2c16288683dd | -15.904 | -59.33848 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eec5b002-18c3-383c-91bd-90a203ef0f9a | -18.30036 | -57.09937 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 9c59efec-5d2f-30e0-bf34-c938fd7bf4c0 | -14.11046 | -51.15358 | 2025-09-26 05:06:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7886b220-192e-39ed-8b75-475e8824d1d3 | -15.36948 | -59.17508 | 2025-09-26 05:06:00 | NOAA-20 | VALE DE SÃO DOMINGOS | MATO GROSSO | Brasil | 5108352 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19b39134-25d7-3217-8451-6e2e086772f1 | -15.98479 | -59.4869 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93644100-0b07-3298-b22e-b6c16c6a84fc | -14.82213 | -45.41331 | 2025-09-26 05:06:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 330401be-e4d5-39fd-a4df-9d805fd7c15f | -15.88717 | -59.33551 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb28636b-78a5-3a8c-8450-07f2e4249a65 | -15.98416 | -59.49073 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49c1d598-930a-3d3b-b79c-a26a894711f0 | -18.29924 | -57.10687 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 81fddec4-bb48-3d4b-b009-5bf3bc2c32ef | -15.94619 | -59.46812 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7454d75b-8230-307b-88c7-af054c1e2bd9 | -15.91459 | -57.48959 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb79e0c2-8209-3a5a-a658-d00e3a65e65d | -17.94332 | -55.86406 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 15d2002d-5a60-3b52-bce2-9131c958fb8c | -18.18764 | -53.33503 | 2025-09-26 05:06:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1dc41061-543a-342c-88ae-300a33badc9a | -15.53853 | -44.33378 | 2025-09-26 05:06:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc33a296-00f8-3eda-bb4b-cc4c2b64e141 | -18.54957 | -46.96404 | 2025-09-26 05:06:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e6f57cd-97ad-3b2a-8fd0-15ec29cdb462 | -15.9368 | -59.49844 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1251b724-6541-3765-bdc2-feb306dadc6c | -16.40383 | -54.83105 | 2025-09-26 05:06:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 498b8dd9-c219-3048-b9ac-89de8e326143 | -15.93652 | -59.47878 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 277f8b3a-8a54-3024-b217-3a164613ed12 | -17.1953 | -56.37141 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d51f808f-f3f4-361a-9810-bacb09b149ac | -15.03218 | -46.94577 | 2025-09-26 05:06:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d01b7b6-7fd3-38ff-b380-544e8b3faf31 | -15.57794 | -51.68623 | 2025-09-26 05:06:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4458fec-2125-3f68-8a38-e3a13e19f2e4 | -15.99093 | -59.49179 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c0cf626a-511c-35cf-9a0b-b994bba3829f | -15.53164 | -44.33304 | 2025-09-26 05:06:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7c1cf488-f374-3719-8616-731330c8e4e6 | -15.93835 | -59.49426 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dfbe9cd3-dff8-34f1-9a55-1cd6c89a6983 | -15.92731 | -57.49534 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd3b7550-4e3d-346c-a3bf-4edd933be891 | -15.99959 | -49.0312 | 2025-09-26 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ded30c4d-1f5f-3f50-a703-b771240dc704 | -15.38227 | -46.12659 | 2025-09-26 05:06:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4aad661-8d8d-3d92-b0f8-70c14144ed5d | -18.3043 | -57.09616 | 2025-09-26 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 08591cb7-25c4-3b1b-9225-025e6ba42025 | -15.9168 | -57.49726 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e577b4f-defc-329f-8309-a99292cd1109 | -15.9046 | -59.33484 | 2025-09-26 05:06:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54ae980f-8a7e-3edb-b520-00204fd00b4a | -17.17805 | -56.36906 | 2025-09-26 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 87e52ed1-8ebe-3bab-9dd9-a1be37889897 | -15.99479 | -49.02739 | 2025-09-26 05:06:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7c1ffe3-e8e4-3aa3-a64c-6a1df6b78425 | -15.92454 | -57.49124 | 2025-09-26 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c27c803-4d61-3a32-8ae7-207cee027131 | -20.60724 | -56.73592 | 2025-09-26 05:08:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2fa03248-77b0-3982-8599-7747d65205d6 | -20.98959 | -50.01181 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ae61a778-e58b-35ff-898f-124906fdc73d | -20.75122 | -57.89309 | 2025-09-26 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 72d1db48-ce5c-382b-bd9d-757b295a8130 | -21.00234 | -50.00624 | 2025-09-26 05:08:00 | NOAA-20 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c3395e4-9444-3125-ba4a-81f8652e5a25 | -20.55592 | -57.14182 | 2025-09-26 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README47.md)
