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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 750c0c0a-9ee2-3d9c-a86a-f1928e8f423f | -11.6104 | -44.0913 | 2025-10-18 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 21a49cc4-4420-3430-81a7-6ab8c88b3532 | -5.0029 | -46.0108 | 2025-10-18 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3721059c-91fb-3ebc-ab02-8ede93114536 | -4.4632 | -43.2386 | 2025-10-18 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 723b9d43-2760-3e88-8b1e-3e4c74164e1d | -10.5128 | -43.4525 | 2025-10-18 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| d2048ee7-403e-3498-a29b-073da263758c | -13.4468 | -43.7652 | 2025-10-18 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 809d071a-c472-33d1-918f-4e1d47757db0 | -4.4446 | -43.2164 | 2025-10-18 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| fd5d3f85-5be2-3b46-8538-7aac9cee6021 | -5.0215 | -46.0097 | 2025-10-18 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 90ecb417-2d53-3fe0-9042-26fccd816d6e | -10.9752 | -44.3244 | 2025-10-18 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 97de5976-a779-3a1f-a6aa-f37044cf589c | -12.6135 | -52.8202 | 2025-10-18 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6c29eefe-bc81-35bf-953e-fa2de974238d | -4.4633 | -43.2152 | 2025-10-18 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 55ec6de9-0a61-34ad-b28a-721552a08ded | -14.277 | -51.8593 | 2025-10-18 01:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 54.4 |
| aba535ed-e184-3e7e-8f61-9bc93e24d462 | -3.1431 | -50.2464 | 2025-10-18 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| f0b9d3a6-30f0-38f7-8554-5fbc0916d9f0 | -10.4937 | -43.4552 | 2025-10-18 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 04fb7401-71db-3706-813f-1349f2c543f7 | -18.3938 | -55.4559 | 2025-10-18 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 149.3 |
| a0eb87a6-6eeb-353b-97d6-d60d60fb63ac | -8.6029 | -40.2083 | 2025-10-18 01:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 90.0 |
| 7f910c3a-10dc-34ce-bd9c-55ad2b714fc1 | -8.389 | -46.2333 | 2025-10-18 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 560c860c-2753-3658-9747-4296d01bcb45 | -12.398 | -47.2056 | 2025-10-18 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 2677f5dd-00be-3f72-b470-9ddf0e4a32e6 | -18.3934 | -55.477 | 2025-10-18 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 242.0 |
| eeb9c38e-ea34-378e-b942-e484a8c1f1b9 | -10.4945 | -43.4079 | 2025-10-18 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1a3aee80-d8fb-37ae-aa45-18ddf5d0eef5 | -11.204 | -47.8318 | 2025-10-18 01:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 42356395-3cc4-3c06-b2ee-9cbbbbb38769 | -10.5132 | -43.4289 | 2025-10-18 01:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 7a0c5dcc-33f5-3e5b-b260-eb92f734a18e | -11.5917 | -44.0707 | 2025-10-18 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ead053c6-befc-3c0d-8fa9-603ac15e2104 | -4.5269 | -44.7998 | 2025-10-18 01:20:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8e809823-e827-3bcb-b9b6-9571ec451832 | -4.0007 | -45.5054 | 2025-10-18 01:20:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| cf2c52c7-5117-3013-ba3f-9a9f2942e909 | -11.6109 | -44.0678 | 2025-10-18 01:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 6be49d95-0ee3-3615-a8b1-1efee9020d38 | -18.3735 | -55.4798 | 2025-10-18 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 203.3 |
| e61f9953-a506-3ed3-97be-d320e8709ca1 | -8.6032 | -40.1834 | 2025-10-18 01:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 103.9 |
| 50b3eea7-50de-3965-83a2-ee779af40f6d | -13.2296 | -43.9692 | 2025-10-18 01:20:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 8a0e32e4-ef6b-35dd-b475-0aab0c7b9bb4 | -18.3739 | -55.4587 | 2025-10-18 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 138.4 |
| 5899c87d-bc28-38ad-a88b-b08c39292867 | -10.1718 | -44.5264 | 2025-10-18 01:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a8039302-816d-3330-b889-5b40b076df6e | -4.4445 | -43.2397 | 2025-10-18 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 7560b884-0053-30cd-a6a3-cbcbf976436f | -13.4663 | -43.7617 | 2025-10-18 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 766e08f9-adc4-3ba2-a87b-3d23626a9d76 | -5.3105 | -44.8423 | 2025-10-18 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 504aa48c-e963-3200-9c49-a090d6b3e83f | -13.4663 | -43.7617 | 2025-10-18 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 5a1769e9-1b37-3905-9f10-e02674e5af9d | -18.3739 | -55.4587 | 2025-10-18 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.9 |
| c434c77a-1376-36b5-8bf9-1364995c65c5 | -10.1718 | -44.5264 | 2025-10-18 01:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| b01ee93b-6f2f-3e7a-8d3a-d7507bf9fc32 | -8.389 | -46.2333 | 2025-10-18 01:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fe31bc9f-e492-3e93-95de-e2f0fd43a192 | -8.6029 | -40.2083 | 2025-10-18 01:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 77e967b9-d221-3eed-afbf-78df3e9e0c8a | -10.9752 | -44.3244 | 2025-10-18 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2adf00f8-9fb5-313b-bd40-93bd91590151 | -10.475 | -43.4342 | 2025-10-18 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4746fb10-88e0-3e28-874f-8c5b63bd6d48 | -11.6109 | -44.0678 | 2025-10-18 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 679e07ed-0ea2-3136-ad2d-e6e39141d8ed | -12.5947 | -52.8014 | 2025-10-18 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ae6c651e-0484-304a-bc92-81f4b6ef34f0 | -18.393 | -55.498 | 2025-10-18 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 1672b0b1-dd34-3e3f-bcf7-0b3de34ff5c5 | -10.5132 | -43.4289 | 2025-10-18 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 998d85d0-4b0c-3bd9-88f0-760719266cb7 | -5.0029 | -46.0108 | 2025-10-18 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4c235a1d-b678-3fc5-af7e-74a7a18f758b | -3.1431 | -50.2464 | 2025-10-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8c563130-f6cd-38a8-a1c9-6ab3c585504b | -10.9758 | -45.4324 | 2025-10-18 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 8b24c30c-7e8c-3cd2-a43a-c4d84b900151 | -10.4945 | -43.4079 | 2025-10-18 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 75bffbde-0c49-39f7-8843-fa8316e417d0 | -3.8572 | -41.5719 | 2025-10-18 01:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 70.4 |
| d1a3e286-2780-38ca-a0e2-326d5b39622c | -5.0215 | -46.0097 | 2025-10-18 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 70418c24-b871-32e3-9fde-0850ecd48cbb | -10.4941 | -43.4315 | 2025-10-18 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 226.6 |
| 35c5de16-6f4f-3fc5-a66b-d7b46bb877ca | -13.2296 | -43.9692 | 2025-10-18 01:30:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 17541a0c-1a75-3351-912f-12dca194fe09 | -4.4446 | -43.2164 | 2025-10-18 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 924dea5b-da83-3f2c-b55b-0e16242483ad | -19.1114 | -57.5486 | 2025-10-18 01:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 75.7 |
| 1d0655ac-1998-3ae8-a3f0-b15b89d7bcb0 | -10.9944 | -44.3217 | 2025-10-18 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8f32e562-5cd2-33f2-ba49-ce80c72ca8f9 | -4.5269 | -44.7998 | 2025-10-18 01:30:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| efa2916d-9a93-310d-b467-6e8cc77bbb2d | -10.4937 | -43.4552 | 2025-10-18 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 2969a10d-9e3d-347a-8a3b-1018fea64872 | -18.3735 | -55.4798 | 2025-10-18 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.9 |
| 4266795c-f23a-3a6e-a08f-ef985e85eccc | -2.9257 | -49.1747 | 2025-10-18 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| c4f799f8-0d7c-3fa3-be1e-fa2adf850b19 | -8.6032 | -40.1834 | 2025-10-18 01:30:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 9715c53c-f6ce-3d14-be88-abd60e457b18 | -10.5128 | -43.4525 | 2025-10-18 01:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2eb4dbfc-fe7f-3ab0-af41-9f2d728bb514 | -11.204 | -47.8318 | 2025-10-18 01:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| b093d7cb-d565-347c-afa9-d036aaf08be3 | -18.3938 | -55.4559 | 2025-10-18 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 178.4 |
| bbb87c65-17c1-3d8e-a581-040b19acf982 | -4.4633 | -43.2152 | 2025-10-18 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 134.8 |
| e3db42b1-e304-323f-8ff5-4d9080655fe1 | -18.3934 | -55.477 | 2025-10-18 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 326.2 |
| 897c7a5b-e736-35dd-8826-1d3e47c856a9 | -10.9567 | -45.4349 | 2025-10-18 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 0e173f78-4571-33d9-8cae-ec89f8774f3b | -3.1616 | -50.2458 | 2025-10-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 44131504-e62b-34c7-bf3c-6f4c9c31e35d | -11.5917 | -44.0707 | 2025-10-18 01:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| bd68228e-40a2-3c1b-b2ec-a747fa553d00 | -3.1432 | -50.2254 | 2025-10-18 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 33e004dd-96c9-380c-96bf-7226fc4d49d2 | -10.9755 | -45.4553 | 2025-10-18 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 9b50b688-6be0-31dd-b063-cb4714de6872 | -12.5944 | -52.8223 | 2025-10-18 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 2d993028-8097-3a73-804f-60a826d476f1 | -12.6135 | -52.8202 | 2025-10-18 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 129.8 |
| ed1c7ce1-7df7-3ebf-a77a-6487fa179957 | -12.6138 | -52.7993 | 2025-10-18 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ae63086b-e317-3768-a52d-1cb65e4db20e | -4.4445 | -43.2397 | 2025-10-18 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 7f57df3a-1d8b-3a53-8587-1b91f0e6dcf5 | -13.783 | -48.2311 | 2025-10-18 01:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| e2b0b939-5a66-38d5-baa4-d2d766e78707 | -4.4632 | -43.2386 | 2025-10-18 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 6e9818b4-fd5f-30e6-b6df-891018910e33 | -11.6104 | -44.0913 | 2025-10-18 01:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 9b9227b5-ce97-3e03-92b4-92cf0120271d | -10.9564 | -45.4579 | 2025-10-18 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 301.3 |
| 7c25f926-f234-3a29-864e-8c2257312b7e | -10.1528 | -44.5289 | 2025-10-18 01:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 44cbdd67-f366-3491-ba52-a0405ba09c5e | -10.5132 | -43.4289 | 2025-10-18 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8bcca0a6-0f6f-3889-bb4d-240ba016fec4 | -18.3938 | -55.4559 | 2025-10-18 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 154.4 |
| f487df73-80aa-38b2-8c4e-56b668d13930 | -11.5917 | -44.0707 | 2025-10-18 01:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 314e5999-f053-3011-a1e0-1315de1f7973 | -5.0215 | -46.0097 | 2025-10-18 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 8c69867a-7485-38a1-85ee-e4372602b8c6 | -11.6104 | -44.0913 | 2025-10-18 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ae49bfa4-91b7-3685-aff2-d3f01cddcdd6 | -4.5455 | -44.7987 | 2025-10-18 01:40:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a0dfb8a4-4376-3ce5-a563-7e6e17fe9841 | -4.0007 | -45.5054 | 2025-10-18 01:40:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| eb272a33-7eea-3988-a739-11406ac5804d | -4.5269 | -44.7998 | 2025-10-18 01:40:00 | GOES-19 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 355.8 |
| 52384318-f6b6-3707-bcfd-86431351e5d3 | -8.6223 | -40.1809 | 2025-10-18 01:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 570a4bcf-f761-3287-9681-57f0cf777d2f | -8.6032 | -40.1834 | 2025-10-18 01:40:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 4e5ac9cd-4006-38d0-b09d-076bc8b0f3e1 | -4.4632 | -43.2386 | 2025-10-18 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 190.3 |
| d9719e47-b2af-3340-b0bb-7564d76cf61d | -8.389 | -46.2333 | 2025-10-18 01:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b741672b-1099-3bf2-8bda-95b1c7ec346f | -18.3735 | -55.4798 | 2025-10-18 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.5 |
| 128e1243-8d1b-38a4-9ef3-5415a0763312 | 2.0231 | -55.8389 | 2025-10-18 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e64c957c-9594-3bce-9a96-b234af00aa9a | -12.6135 | -52.8202 | 2025-10-18 01:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 26f19e5c-9b38-36c3-b28c-f7c5f375e295 | -10.5128 | -43.4525 | 2025-10-18 01:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b5818163-33cc-3637-bd63-6c67d5713339 | -13.4663 | -43.7617 | 2025-10-18 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 0cc98494-3f4f-32a2-bb3a-f7b8b7d6c587 | -18.3739 | -55.4587 | 2025-10-18 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 509a2743-55cf-3745-9fd3-a33712fbef88 | -10.1718 | -44.5264 | 2025-10-18 01:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 612c6b91-c45a-3e31-bd98-ad24b3a75693 | -13.2296 | -43.9692 | 2025-10-18 01:40:00 | GOES-19 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 38.4 |
| d100cfc5-e076-395c-8c00-44d4ba5a6124 | -18.3934 | -55.477 | 2025-10-18 01:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 358.9 |


[Clique aqui para ver as próximas entradas](README8.md)
