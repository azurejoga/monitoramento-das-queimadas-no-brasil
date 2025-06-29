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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e183f828-58b8-3e6c-b4a1-11648d99eb56 | -9.43194 | -47.95025 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e59cddb6-fb2e-3ad7-8137-aa7d433c498e | -11.03774 | -55.37538 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e810b600-c911-304e-a59a-896423ab7915 | -11.54704 | -52.76967 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c08a5d89-1fbb-31eb-bb69-a47cbf52fb95 | -10.86049 | -53.7557 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f55e4f7e-4718-3fa3-b058-d5f7e4416336 | -11.03574 | -56.26628 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 836fe4de-a2ef-3987-8ce3-5a435117344f | -10.5533 | -52.04332 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| bd990df2-8b17-3788-a140-56d607161bb1 | -8.12379 | -55.09 | 2025-06-29 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74ed9323-3693-3259-8e8b-688764c86db7 | -9.43277 | -47.9465 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 34cc3a83-b70f-3e33-afeb-82ed811bdfd9 | -11.55912 | -52.80149 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17d6980c-b947-30a8-9ddd-71ab2d90d7ed | -11.26038 | -52.75264 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b437d60d-1926-355b-9d23-e04b51feb869 | -11.11772 | -55.44399 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c72ed43e-3f14-3697-8dc3-76608d27ab80 | -11.01828 | -56.22208 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b814604-8b9d-3511-b0c4-12f777ff90f4 | -11.04268 | -55.37175 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4fac2e50-0646-3357-8a26-5e472b3ae43b | -11.54982 | -52.79023 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 08b4ffbd-28db-3e5b-ac61-cb756edbae4b | -10.35214 | -57.50156 | 2025-06-29 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d39e75e3-bec8-38c5-8933-9c881c1d2a0c | -12.0643 | -48.478 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7fc3fd87-1c72-36db-85b3-1ab91b44d552 | -10.56332 | -52.05194 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 58a9b76e-8adc-3eb4-ab35-fed058682676 | -9.08959 | -59.49586 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4052f7bf-011a-37b2-9d29-f1db94e0fdc6 | -11.01668 | -56.23349 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d87d7968-2771-3d90-a36a-1c70038955d1 | -9.42425 | -47.95564 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 65d99136-bb72-3c65-96f9-6bcfee7e1d8f | -9.08391 | -59.4874 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 197ce978-af53-3346-8ba7-e10a62084d20 | -12.06537 | -48.47156 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9a2bc4a-fd26-36c9-a6ec-84ed0270d128 | -11.54456 | -52.78947 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bec3de62-1e59-327d-8b4c-54a5c4a17794 | -11.26077 | -52.74937 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| aaca14e7-d5e8-3048-bf20-8fad890da0bc | -9.0833 | -59.46837 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4747ad74-e206-34e4-b63a-18af2b307ab2 | -11.02496 | -56.28391 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6c96525-deb1-3d2c-919d-05265ec6b695 | -10.57014 | -52.04199 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4b64b18a-5842-3f6a-bd17-0869980e89b2 | -11.54013 | -52.78209 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 96a54c3e-dbe8-3385-898b-5343aaa6349b | -11.0248 | -56.26556 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ebb4987c-74b9-3529-ba6a-91f0ad73ff09 | -10.10128 | -52.19565 | 2025-06-29 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb113c26-d099-3288-97b4-c250d702f09d | -9.39905 | -63.26056 | 2025-06-29 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b130139c-be3a-32b6-88c3-9770f2ddb2f8 | -10.55876 | -52.04408 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8993965d-5c75-379f-90ed-cbde6f8771a9 | -11.02586 | -56.25804 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6ac969ec-39a5-380f-96c9-55298627e59b | -10.05294 | -59.35923 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cc11c9b-9335-3468-a23f-f5b36e100b5b | -11.26728 | -52.74249 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47980b16-d99f-3fe0-8686-b5dfa46bf7f6 | -9.09295 | -59.47365 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9cf03f2-43cf-3a53-a21a-7f4ab0d2447d | -3.6267 | -47.54979 | 2025-06-29 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93242e6e-84eb-3baf-b6a4-04dac1fad278 | -11.05527 | -55.37794 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10c6269b-ecca-3f28-a60f-1075f77afc1a | -4.32112 | -48.0742 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d3ee973-28e3-3218-81d6-e81879b977a6 | -9.71406 | -56.18481 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b228b83b-6895-3a03-ad3d-b9adcefb2edd | -10.83173 | -53.76249 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3ef65c-6226-38f3-9483-e3f450faf145 | -11.27778 | -52.7415 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2cbface-806f-3dec-b426-881ab71b76df | -10.84024 | -53.75852 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7b16eff-df10-3408-9d2e-ed4977cb18cb | -11.56522 | -52.79555 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2daa6a13-2545-3b3f-a6c7-490ab7d9399a | -9.43891 | -47.95095 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9423d98-f3ee-356e-885b-0e0bbe4a917c | -11.05088 | -55.37735 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 156e473a-e441-35b8-8ffa-d1abc70e2d0d | -11.55231 | -52.77043 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 8b77bf6e-34ff-3616-a2cd-a0f11638f3ec | -11.5519 | -52.77375 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 6df46807-0329-3c43-b4f5-e787f3527fc7 | -2.75017 | -54.59343 | 2025-06-29 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f9c7be50-ad53-350b-8aae-4c749a7fd3d7 | -11.04105 | -55.37885 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52a6698d-775b-30b8-be17-72e1226a159a | -11.04706 | -55.37243 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f11bd7db-dd17-36a4-91d1-764ca785e9a2 | -12.05844 | -48.47053 | 2025-06-29 05:23:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 28854c67-b93e-31a2-88cb-9490cbf0ed07 | -11.00431 | -56.23146 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73252f26-4527-3c01-9981-5a8e54d74b8a | -11.26117 | -52.74838 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 71559176-262a-3de5-adb0-41d7ad26ccdc | -10.56968 | -52.04557 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20889d67-a7ae-3384-bf9b-2acb830ca0d8 | -9.70592 | -56.18357 | 2025-06-29 05:23:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f97e0d55-5de2-34cd-885a-ed95dbcb47c7 | -11.04649 | -55.37678 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 948e4466-cf89-312c-909c-cc6df070c45b | -11.55302 | -52.80735 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 99c54822-d6f0-3035-9eb3-1168e88b9a7a | -4.54145 | -48.02099 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4871c8e6-bd59-3d97-932c-21bd04139d65 | -11.03728 | -55.37381 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f78ee3c-9d2c-3c7c-8483-fc3534444f21 | -10.55241 | -52.05043 | 2025-06-29 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2dd54a81-d262-31a8-ad64-ffc79a09e4b1 | -11.03668 | -55.37813 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 674912d4-f4b8-33ca-87ff-8e50f1e4e47a | -9.47135 | -57.33236 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 541db191-5830-31ef-b2fa-7f5692dc930f | -9.0901 | -59.46943 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9feba907-c34a-3b26-96c9-a2bd64642b6f | -4.32026 | -48.08014 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 074cba9f-ed55-3c4f-8014-1e06104aba4b | -9.24642 | -63.29284 | 2025-06-29 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd2bc5e7-6f68-34f5-bf7d-d65d91352dac | -11.56354 | -52.80878 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97a21d77-d672-3986-b58b-6a203a8ea647 | -9.11142 | -59.04535 | 2025-06-29 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50c5d360-5832-3e52-931f-4e2b7344b334 | -11.55509 | -52.79095 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4916828b-6834-3d7c-943a-57f85d786455 | -11.55261 | -52.81059 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5cd752c-2c99-310f-ac2d-5250fb36257e | -2.75425 | -54.5941 | 2025-06-29 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2ac72e47-575d-396c-8e61-f2299781e44d | -11.02597 | -56.27639 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9599ced8-47ce-32bd-a365-605aceab1446 | -11.55551 | -52.78766 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8172618a-3287-330b-a34a-ac91750fb078 | -11.55106 | -52.78038 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1a28bb9a-cdd6-352b-bbc7-368f1678cb88 | -11.05145 | -55.373 | 2025-06-29 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e8101d1-d844-3e0d-9009-e798318dd180 | -4.54788 | -48.02242 | 2025-06-29 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e86c1e27-5481-32f1-b364-ed04fb5979df | -11.03523 | -56.27008 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9a8661c-e6ca-328b-a386-c4457af6ec56 | -11.54538 | -52.78293 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 8b51e59a-9b05-36b8-885c-cfa5a00650a6 | -4.66283 | -55.97029 | 2025-06-29 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0f970be-fbd5-375d-9877-06f5d4b9f276 | -11.02285 | -56.26823 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 362b1b0a-bd8f-3eb2-82a5-8d7feed0a994 | -11.26033 | -52.75489 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c3f66ec9-1a33-3630-99aa-5e6b63bb9bf8 | -11.56397 | -52.80546 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f3786b4-0a7e-314a-85ee-9bb08aff15f3 | -11.56481 | -52.79884 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c44b1ce0-4029-332b-a614-382e51e93a2e | -11.54497 | -52.78621 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 23e894ff-fa09-3ba8-8123-057df77fdefe | -11.02533 | -56.2618 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7657cbe7-bec2-3fa9-ac88-b4042a0afeb0 | -10.83247 | -53.75702 | 2025-06-29 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c48b618-89d8-341d-836b-dcd042ae49c7 | -11.02386 | -56.26069 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1977363d-35a3-35a3-8c61-ea63f037e67b | -11.02068 | -56.26493 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cd7e1f02-c922-313f-b97e-db93b7dca2fd | -10.67168 | -58.76514 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae833c6b-8954-328e-95d6-23366a1340f3 | -11.54053 | -52.77883 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f7a6569d-b7f3-3707-9a74-b0abb4951884 | -9.25325 | -63.29399 | 2025-06-29 05:23:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe4dd458-3653-3048-bdf5-686ea373fa51 | -3.63208 | -47.54399 | 2025-06-29 05:23:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce3d6a9f-e8c6-3ba5-b75c-8275d45e6047 | -11.01908 | -56.27622 | 2025-06-29 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bcbbff6a-8cb5-305c-9a06-0b4f36e75c51 | -2.95574 | -60.01694 | 2025-06-29 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8411592c-16ce-39c0-83e0-7e88b4099aa0 | -10.03917 | -59.35707 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 580f834e-6cf5-3410-a13d-e47db9288ba3 | -10.29503 | -57.02837 | 2025-06-29 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51e7341d-c541-3509-8786-d274c633347f | -9.47512 | -57.33294 | 2025-06-29 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84deaf7e-9c95-33bc-9bfb-0b5deba47cb7 | -9.86493 | -60.32006 | 2025-06-29 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86dc6e4d-7482-3e76-9ce3-da43f9afc699 | -11.26525 | -52.75658 | 2025-06-29 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62a3016b-45bb-3244-a5f0-af312d75d531 | -9.42502 | -47.94904 | 2025-06-29 05:23:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |


[Clique aqui para ver as próximas entradas](README25.md)
