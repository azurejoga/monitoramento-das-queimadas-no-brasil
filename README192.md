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

## Dados Diários - Página 192

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5541009-edaa-34ee-ab4b-80604b5dee09 | -20.09734 | -55.95992 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.0 |
| e23b9e56-5e83-38b1-aed3-2b17477341eb | -20.07836 | -55.96566 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af58eb97-711a-3922-aba6-e442788a15c4 | -20.07125 | -55.96455 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 59ec6e68-db9c-37e7-8af7-ef8a6e36ca49 | -20.06948 | -55.95121 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6768e558-24eb-34ff-b26a-6ca95204ef31 | -20.06829 | -55.95972 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 91b1eb6b-ac0b-3145-b06a-647be830a4f5 | -20.06117 | -55.95861 | 2024-10-09 05:06:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 69c39057-d0d7-31e9-8e78-f356d6f52f3c | -20.27322 | -56.9267 | 2024-10-09 05:06:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 183ef8c5-21ed-3337-b2c4-5f20c4291f56 | -20.27264 | -56.93067 | 2024-10-09 05:06:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 943a514a-37d8-3331-9457-501b96448f11 | -20.23557 | -56.96858 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e85d1949-3b7e-32ba-9db5-4321bfa10707 | -20.26921 | -56.93014 | 2024-10-09 05:06:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c30e3ba-07fa-313c-8f61-356b46162b45 | -21.43953 | -57.22028 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e048de7d-28d3-32bd-afc1-3997d4e54e1b | -21.43896 | -57.22422 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2875d4ef-d045-338b-96ac-f85c0117a93b | -21.43668 | -57.2157 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| facc3b84-7d39-3144-93ed-7af5d80b0e48 | -21.43498 | -57.25155 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b0c8575-8ece-30ab-8395-5a0d549e14c8 | -21.43441 | -57.25549 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d7fc34a-051e-364b-89ec-f1b3d43d094d | -21.43438 | -57.23157 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2dc19258-7686-335a-a2cc-7640911ccffd | -21.43384 | -57.25943 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a99e62bb-def8-3ce9-b847-ad2b1d8d9830 | -21.43382 | -57.23544 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5518a628-a90d-318d-b231-9a7ffe2a2583 | -21.43325 | -57.23932 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b356edbe-b6bd-37fc-be33-60ce2b2fd552 | -21.43269 | -57.2432 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd722e9b-f187-3025-8eee-788750dac914 | -21.43212 | -57.2471 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9a557e6-8e51-335a-907b-17203e2f1459 | -21.4304 | -57.25893 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc0e372e-d7f8-337e-b785-db02d9a447db | -21.42925 | -57.24271 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f071f64-8f43-39d9-b06f-0deabe704b7c | -21.42637 | -57.23838 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e64b0dd-eb7b-3b15-9110-fad15e1b71ac | -21.42293 | -57.23791 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afb4fa5f-7018-3fab-95f3-32d763c81367 | -21.41554 | -57.21629 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42627a57-e6bb-3a5b-9fd0-96e388df8760 | -21.4121 | -57.21581 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c76d5d0b-fe55-3115-9987-880db1c99f91 | -21.40809 | -57.21926 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7e8ea1b-94ce-3a5d-bcce-12d1c14ff2dc | -21.40471 | -57.26691 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7518d85-39f9-31b5-9c0e-becd95916db6 | -21.40127 | -57.26644 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc7df23e-19ba-363e-89a9-cb492bd62a09 | -21.40064 | -57.22227 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f94e0be9-223a-37b9-b454-d0616ec86b42 | -21.39839 | -57.26216 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb576b6a-e33f-3501-8bb6-5a5762254e83 | -21.39608 | -57.22962 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96888d3f-0c6a-335e-b6ee-eec29d761ddd | -21.3955 | -57.25788 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d9baeb6-e827-3ced-b8c4-7db95d0cfc24 | -21.39495 | -57.26176 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 50dbe0ab-d9e3-3b9e-92d8-995b9c4a3ea0 | -21.3932 | -57.24958 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6fc71dae-9cbe-3161-8566-7c809a93a666 | -21.39207 | -57.25744 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 995d3abc-dbd1-3651-9f33-61f42ca915d1 | -21.39035 | -57.24506 | 2024-10-09 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ccfd380-420e-3c32-a083-68d0ef88cd0d | -18.87234 | -57.73441 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5a04c8fa-f9dc-3d2c-b3ad-889dbbc3e533 | -18.89455 | -57.7457 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5ac61180-ec4f-3202-ae83-265bba4c409a | -18.86788 | -57.74122 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a0e18cc4-ce41-3cdf-8686-2e96a83744bd | -18.85405 | -57.69728 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5f5e336a-d4d7-39b2-921f-7b0496895782 | -18.869 | -57.73385 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dca00790-caa5-3ef6-9267-edc6bf940036 | -19.12127 | -57.52436 | 2024-10-09 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5d958f57-c12c-32f5-8ad0-0ba60a9a840a | -19.11792 | -57.52381 | 2024-10-09 05:06:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b3620dc-0d98-35c7-a806-18630b108a8b | -18.72861 | -57.22748 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c01d384a-a654-37b8-b8ed-492f43dfc1c2 | -18.71782 | -57.36771 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 552f6679-9a2b-3065-a409-67e9401cef9e | -18.70617 | -57.21609 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2075dfdc-b3d1-3853-9771-5a9777e1c6ad | -18.70224 | -57.2193 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| b7025150-1747-3191-bc3c-e6239b660104 | -18.97313 | -50.19777 | 2024-10-09 05:06:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13d6767b-d2b0-39a3-8e7c-06cf620467af | -18.12567 | -56.3897 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 293d4de7-317a-35fd-a52c-4d85401563b3 | -18.12525 | -56.38908 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2241d7d5-d0a1-3c2b-924b-b7b1ef60f1d5 | -16.53343 | -52.87296 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6136bbec-8d66-3eb5-8479-aaeac201c52d | -16.50425 | -52.87599 | 2024-10-09 05:06:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e9560c0-e681-3355-b579-c2e17789bfcb | -16.50377 | -52.87966 | 2024-10-09 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da296058-4aca-3e87-ac7f-157a00ae3f03 | -16.50021 | -52.87545 | 2024-10-09 05:06:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5f18845-1448-3154-b3c0-b2def6ad0181 | -17.32421 | -54.99881 | 2024-10-09 05:06:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bb0ad5f0-dd06-352e-9990-884c353b8a75 | -17.02539 | -55.03637 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3d9826f4-d6d3-3c1e-a462-e56a03ef0fb4 | -16.76909 | -53.91608 | 2024-10-09 05:06:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff6aac42-6e5f-3c5b-aef6-31ad202d4e97 | -16.76593 | -53.91077 | 2024-10-09 05:06:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2c378d29-f5d9-37ce-a4f6-e73883782a3b | -16.76528 | -53.91557 | 2024-10-09 05:06:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 69d3ec5f-e1e3-3222-acd7-7cec424867f2 | -18.20712 | -54.45505 | 2024-10-09 05:06:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 375dbf42-833a-369e-83ab-23a348b74d96 | -18.12509 | -56.39361 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| aee539b5-a7f2-3a54-938e-2d1097f35e15 | -18.12469 | -56.393 | 2024-10-09 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| d340f693-deb3-3ed6-8a2b-7e92af2ebcf0 | -16.43103 | -55.93195 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5df91086-6139-3612-9fbf-63483d26c376 | -16.42816 | -55.95139 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d058f4f9-1422-3c98-922f-e6fd426fd4ea | -16.42759 | -55.93141 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6207a4f7-6503-37fe-bc0b-e06321988540 | -16.42701 | -55.9353 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d3d5028d-5f2c-39d0-9da9-c89fba397638 | -16.42644 | -55.93919 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 11caa709-3d4e-34df-9308-8b47043a0c39 | -16.42529 | -55.94697 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d22ab5f3-8caf-3424-b369-c58109c831a9 | -16.42472 | -55.95085 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| aae5ecb2-aa9a-3042-b7c5-9067a63a6750 | -16.42414 | -55.95473 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 9e21ecd2-f3b8-3a1a-aac4-9f1081c32c70 | -16.42414 | -55.93087 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 80e72ff6-e425-3b83-a8a2-e5925b4370ed | -16.42357 | -55.93476 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 650c3b69-3913-3deb-8efe-949820af7c0c | -16.423 | -55.93866 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8a57b4c5-6378-3822-b618-b4ab313585db | -16.42242 | -55.94255 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| fb8f6584-765c-339c-a0ad-931ad0afc18e | -16.42185 | -55.94643 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3f58dece-464b-3d04-96f6-2ad6fab6e690 | -16.42128 | -55.95031 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| aad838d0-6046-352e-b997-a18109fcf31b | -16.4207 | -55.95419 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e40a9674-6494-3790-a594-5b10b6b24093 | -16.4207 | -55.93034 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 2aa58a3a-3d2c-3ce2-870f-4532fb0c6e99 | -16.42013 | -55.93423 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 3615ad6b-09ac-3a72-b389-ea390e0d7404 | -16.41955 | -55.93812 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 332fa8b5-d3c7-388f-bd2d-1fb7798f1482 | -16.41898 | -55.94201 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6b89a939-4c38-31f2-bcd4-00af24299769 | -16.41841 | -55.94589 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8d3b64e8-22ad-3640-bb81-43c40dd5808c | -16.41669 | -55.93369 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7997b1a9-f79e-3523-8396-d9e41c18bd7c | -16.41611 | -55.93758 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 7095190c-7278-30fb-87ea-556b308564d5 | -16.41554 | -55.94147 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e9ec0ea9-da95-3c59-9fea-e49a868540a9 | -16.41497 | -55.94535 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 493846b6-e9ed-3b01-8d62-ae1d04745924 | -16.41325 | -55.93315 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 107b9cb7-23da-3060-8a44-dcae2c170b7e | -16.41267 | -55.93703 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b1e9734b-3ec7-391e-a844-c21d30894c58 | -16.4121 | -55.94092 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a9ae2d1d-3493-3f25-b6d9-41bcbb2c1f7b | -16.41153 | -55.9448 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c4db5113-fc16-3553-9e3b-1c563b0b89f4 | -16.41096 | -55.94868 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 57484608-1366-34d2-88b3-928752e8ff5c | -16.35429 | -55.97548 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04b8b16c-da9a-32b6-bc0d-0a21a8873519 | -16.35373 | -55.97935 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fc1d6ba8-ca69-388f-ad32-f0c739dd9eac | -16.16458 | -55.93513 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e249b8c7-3b05-3304-9b78-7a0502c1fab4 | -16.16115 | -55.93459 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3e7c3ec2-e542-365f-abcd-b2d34fc406c0 | -16.16059 | -55.93843 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8e0ad60a-efb7-3606-a070-aae5d0bd9695 | -16.15771 | -55.93403 | 2024-10-09 05:06:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 43a67bc5-7219-3b32-b122-3df2a7761e14 | -16.15716 | -55.93785 | 2024-10-09 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |


[Clique aqui para ver as próximas entradas](README193.md)
