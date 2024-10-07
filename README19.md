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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bff03987-8317-35d8-82b4-e40dd86248d6 | -16.3102 | -51.2798 | 2024-10-07 01:20:43 | METOP-C | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1154035e-aa71-380d-bff4-8937f3fd495d | -16.062201 | -50.4352 | 2024-10-07 01:20:43 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4870ad43-41e6-3743-8e22-d4e1a37101c9 | -16.054899 | -50.447601 | 2024-10-07 01:20:43 | METOP-C | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec910c35-f290-3b7d-b187-1704d1bafe04 | -16.1728 | -50.928101 | 2024-10-07 01:20:43 | METOP-C | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 93d1ea88-f1c7-3f1e-8be9-31563aacf9c5 | -17.2679 | -56.181801 | 2024-10-07 01:20:45 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 93a031a0-7886-368e-b9a8-1cfaf95a9e33 | -16.908001 | -54.547901 | 2024-10-07 01:20:45 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 947d6002-4228-3217-912b-5f4bdaf1433f | -16.909599 | -54.555099 | 2024-10-07 01:20:45 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8eda9c-f9f6-3192-b472-a71b305c96ee | -17.0198 | -55.047901 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9aaf8610-efa9-3135-b9de-5560d0050126 | -17.021299 | -55.055 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 277e500b-e1bd-329f-b422-b96bb8759103 | -17.0229 | -55.062199 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff5a461b-9ad9-3453-9d98-925fc68b6f17 | -17.0245 | -55.069302 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 137bedfc-3983-36c1-8fa2-c789040cc588 | -17.0261 | -55.0765 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eedd9604-c061-301f-9c3c-9a5fee7a5840 | -16.8983 | -54.550301 | 2024-10-07 01:20:45 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7a1da3d5-7711-3cf1-9c88-1933936bd8d5 | -16.8999 | -54.5574 | 2024-10-07 01:20:45 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 432ca86d-147f-3ba9-8a33-2047eb92c571 | -17.003599 | -55.0215 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 25f455ab-3db3-39da-bdf4-5dc9d2c3910b | -17.005199 | -55.028702 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b720fb72-a6a0-3609-858f-09400786615c | -17.0084 | -55.042999 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2050285b-c9f2-3008-8fd5-09bb8684948c | -17.01 | -55.050201 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4daf7830-d8b9-3a84-80d7-f56592d2a0de | -17.011499 | -55.057301 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50c1044a-bc66-3f0d-b6a1-0099b58976f6 | -17.0147 | -55.071602 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eaf82327-431b-3ccb-811e-6c44b5c7177a | -17.0163 | -55.0788 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aae535b5-7b76-385b-b720-7f61ececdd8a | -17.0179 | -55.085899 | 2024-10-07 01:20:45 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a41366ff-b080-3037-99ce-93ffc3f555f1 | -16.880501 | -54.516899 | 2024-10-07 01:20:46 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2efd83b1-df1f-3a2f-a8e7-5c87ab6d13b3 | -16.882099 | -54.523998 | 2024-10-07 01:20:46 | METOP-C | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7866b799-7b0b-3b99-ab10-50366d240529 | -17.0065 | -55.0811 | 2024-10-07 01:20:46 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97aab96e-f6fe-3015-9f13-7ecdfcb8ddb7 | -17.008101 | -55.0882 | 2024-10-07 01:20:46 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84c813ec-b4e4-3dc3-b92d-05e3b7d7eea5 | -17.009701 | -55.095402 | 2024-10-07 01:20:46 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c56037b2-cbfc-3f7c-a88e-3075e0836d51 | -17.155701 | -56.137402 | 2024-10-07 01:20:47 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3a17ef15-2ec0-3d90-9177-34eaff0da55c | -17.1894 | -56.2939 | 2024-10-07 01:20:47 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8d374e43-5895-3f62-b79d-be23a86b0c1f | -17.145901 | -56.139702 | 2024-10-07 01:20:47 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 621dc7c5-aa15-3b01-a64b-3d63f2662724 | -17.147499 | -56.147099 | 2024-10-07 01:20:47 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 161293ad-ee36-37ab-b610-023125123709 | -17.149099 | -56.154499 | 2024-10-07 01:20:47 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c822757-8799-306d-bcb3-31c6ff6c7fdc | -17.053301 | -56.044498 | 2024-10-07 01:20:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 984f32bb-0d9d-37cf-bf7c-318affd89741 | -17.054899 | -56.051899 | 2024-10-07 01:20:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f701110d-c788-3657-9f01-3aefaff876ca | -17.1451 | -56.469898 | 2024-10-07 01:20:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa8645a0-5db4-3910-ab7a-de2048f6963a | -17.043501 | -56.0467 | 2024-10-07 01:20:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d6a44ca-c972-32fa-8363-5378fb302df7 | -17.045099 | -56.0541 | 2024-10-07 01:20:48 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f8afaf48-85e4-328f-a88d-8268584529f4 | -17.151699 | -56.740501 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1345aea-d024-3f9f-9467-afafb175365c | -17.153299 | -56.748199 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f782425f-35e8-341e-8089-667a96a27811 | -17.155001 | -56.755901 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ca7c85d-4266-317f-85c8-ffe2d542755e | -17.141899 | -56.742699 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7290ab71-3938-3a43-9286-9363c7ab67ff | -17.143499 | -56.750401 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fa826159-e7d2-387f-abba-4464580ed5da | -17.145201 | -56.758099 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44a8a25f-3308-3775-8492-121d371015a7 | -17.135401 | -56.7603 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0d36cc13-66c2-3597-8d4d-d7070a910d59 | -17.136999 | -56.768002 | 2024-10-07 01:20:49 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e32dafd7-e628-3adb-92d1-36f9ec735cdd | -17.123899 | -56.754799 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 44358973-65d3-3c86-b7d1-ded7951c744f | -17.125601 | -56.7626 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4da2eda1-031c-37e8-aac2-933ebca74f94 | -17.127199 | -56.770302 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 07e9c1a1-525b-30d0-880c-6105e92faa89 | -17.128901 | -56.778 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 503f6281-d328-3b51-ba6a-beb1a5bd260c | -17.130501 | -56.785702 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 69c1bc81-699a-32cb-a471-3dbb4ffa5652 | -16.4928 | -53.944 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46734d54-577a-3d0b-be00-2875c2101247 | -16.4944 | -53.951199 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 532b8f84-3c62-3990-93d9-477052c4d912 | -17.110901 | -56.7416 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0a2249b2-59d2-3d9a-a110-1080e0d4ad74 | -17.112499 | -56.749298 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0fb9fd35-433e-364c-8a5e-8464afc5e01b | -17.114201 | -56.757 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d175ef8-d9b9-3bca-a999-3fe23292b135 | -17.115801 | -56.764801 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7dd757e3-800b-3ff9-9abb-7636f7b9901f | -17.1175 | -56.772499 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 09c2df01-ba1c-33de-9fdc-755bfc279485 | -17.119101 | -56.780201 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 45cae91e-4d1c-39e6-bc6c-1dbbb139856e | -17.1208 | -56.787899 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b54e28d-bf7b-3358-9070-7939fc4af697 | -17.1224 | -56.795601 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 28fe7251-411a-34e9-94b6-0559a2746efe | -17.1241 | -56.803398 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 76b27798-447b-3eaa-a690-733297bcc55d | -17.1257 | -56.8111 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 23103a84-969e-38f0-a414-4a51a0671a94 | -17.1273 | -56.818802 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b32fc6d0-b40e-3fed-bec5-04655dc6bcaf | -17.129 | -56.826599 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b310a05-9a6e-3e25-bc09-7145c4aeb74a | -17.1306 | -56.834301 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8441365c-e42d-3193-b153-2bb0b9b18749 | -17.1588 | -56.966801 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae656a51-9d63-315b-abdc-1ab227fcb2fb | -16.483 | -53.9464 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 219bab54-9909-33d0-85c7-436fd8dd3b89 | -16.4846 | -53.953602 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dcdfe768-9bb8-33cf-ab3a-ed355114976d | -16.4863 | -53.9608 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e4867f5b-a86a-382c-988e-1500979b8094 | -17.111 | -56.7901 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e1790d7-a484-3c9e-ac7a-bca6e1ebd5c2 | -17.1126 | -56.797798 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 00d94f2a-9690-3031-a15b-14a1c2145d73 | -17.1143 | -56.805599 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5483f5c8-1a9b-30a5-840e-c6c47327a520 | -17.1159 | -56.813301 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a8d461f0-af0a-3eb7-ae14-4b607a2286bc | -17.1175 | -56.820999 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d2ae420c-c6ac-311b-8c33-08d7c3ad75ca | -17.1192 | -56.8288 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4e41502b-d500-37d8-b73e-d8b1902c4835 | -17.1208 | -56.836498 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2dfd373b-b941-3b8a-9c4b-9ed2ba0b5e28 | -17.147301 | -56.961201 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 746a5891-a9c9-39a0-ac35-f101307fb77d | -17.1012 | -56.792301 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b8ae8cf-4711-36e4-b621-f70283c8bd77 | -17.1028 | -56.800098 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 289c2c93-fbdd-3b6a-8a46-94c97dd1c99f | -17.1045 | -56.8078 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cbc4ba2a-503e-339e-a78e-dda966b4b6f1 | -17.1061 | -56.815498 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b1a76a70-10d7-30a1-aaf5-ac205428a054 | -17.1077 | -56.823299 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5be723ff-cf69-357a-8a17-ac5be4c4af93 | -17.1094 | -56.831001 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 661b77c8-4517-3a8b-a997-680fa8d96d00 | -17.111 | -56.838799 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4ae78d0c-6fd5-3099-b640-cd71302e5692 | -16.455099 | -53.914902 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7cce4e49-15ba-3654-a10b-15034c4b2b8f | -16.4568 | -53.9221 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b1004b0-3746-3e74-93fa-570bcb1beced | -16.458401 | -53.929401 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3bbdb476-ef79-3bf7-833c-d1f6511d6188 | -16.4634 | -53.951099 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 500a92e4-dfeb-3198-b0d7-bf0305b271bc | -16.465 | -53.958302 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ca0c53f-9c7d-30f8-b9e0-640dd300789c | -16.4667 | -53.9655 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6fdc8c97-6a5d-3834-8ef3-f29361f849c5 | -16.891199 | -55.866299 | 2024-10-07 01:20:50 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0604103d-4243-30c8-902c-e8c89d300c1e | -17.0651 | -56.6716 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e128887f-929f-3b3d-83e0-194a614dd6ee | -17.0914 | -56.794498 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 737a108a-a989-31eb-8c21-505ec8fa0425 | -17.093 | -56.802299 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4d8202f5-1183-3f82-9b12-1bbcc4babc00 | -17.0947 | -56.810001 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ffe47225-72a5-3779-a8c2-2261327bd7d6 | -17.0963 | -56.817699 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0924a2d5-413a-3930-ac1d-3c2dc30e3f7f | -17.0979 | -56.8255 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8eded493-bbc2-301e-b6a5-86e415c2d796 | -17.0996 | -56.833199 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d99a8751-a03b-37e1-bb28-5032f775304d | -17.1012 | -56.841 | 2024-10-07 01:20:50 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a4f35a8-05e2-3f67-b77a-23a0f19dd73c | -16.453699 | -53.953499 | 2024-10-07 01:20:50 | METOP-C | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README20.md)
