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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0ca9418-86d2-3556-9e4b-f80e63631d47 | -11.48481 | -59.08957 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fda82a0-28a7-30f1-b24c-227fe16a908e | -13.27157 | -47.63017 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ce10e2e2-d44a-3123-ac7f-b0ad0ab6d02b | -12.29591 | -64.0247 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8761e658-a0ed-3afe-93ac-dc81a99abed7 | -12.44772 | -54.40189 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d20db62b-4a08-3c4a-b495-e29d367804a4 | -16.00359 | -50.84139 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 180ef384-d901-32dd-9cc6-7b6f63cd6c68 | -18.11018 | -53.39839 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5b9db0f4-489c-35b2-9b74-c3da62177d20 | -14.63777 | -48.34258 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0be21e5d-4399-3f16-8c3b-8bb867055244 | -14.90612 | -51.50643 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2ca37c26-2bbb-33c5-94bd-23cac4e6620b | -14.64737 | -56.01894 | 2025-10-06 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1560a62-4f5a-3247-954a-d25d2f532de9 | -16.95675 | -52.69528 | 2025-10-06 05:18:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcfa2617-56fc-3798-9a44-36b2cc40efaf | -14.6302 | -52.5103 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| faf82149-c549-3ece-8f44-f7155baa1b27 | -13.33885 | -48.05827 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1ccca966-d703-3060-844b-9b709a2cf5cf | -14.3664 | -47.72379 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d7c0c65-076d-388e-a8c2-a3f6623c62cb | -18.12104 | -53.39032 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ff765c01-002e-332c-aa37-3292f134e897 | -18.25632 | -53.35756 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 257128a8-a75e-3235-b82d-1909a7f51e05 | -15.99527 | -59.53675 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd2c40c1-5a67-3850-94cc-77342f645bbf | -15.22648 | -49.28216 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 782c37f7-a19c-307c-b748-45c8d7980f9f | -14.66658 | -48.38373 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d16c4e2c-ab6c-388e-be16-7156a5a9d022 | -13.34599 | -48.05294 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 8cb84ab2-c852-32de-a37e-fe330e662cfa | -11.8721 | -56.89066 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17450089-eb27-3375-baba-7ed07415ea50 | -16.00477 | -50.84997 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20d84093-5a04-373d-a1c8-bbd1b7ec9e39 | -17.6747 | -52.24609 | 2025-10-06 05:18:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dd61959b-f5cf-3a02-a2b0-13f770c64b5f | -11.71625 | -59.12998 | 2025-10-06 05:18:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a510d96-b99d-30c9-9255-fa69671714ec | -13.60012 | -48.69393 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10f8c03a-05eb-386b-b022-751cc9ce8f75 | -10.38402 | -67.89816 | 2025-10-06 05:18:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6a62fdd-b2d9-3d23-907d-f8b9f4163126 | -14.67743 | -48.40017 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6f9b2a70-8c1a-3408-8202-46c61792a3cb | -13.26088 | -47.18586 | 2025-10-06 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21f886b1-e379-31b3-a5d2-9b6e9aec3891 | -16.34454 | -51.45184 | 2025-10-06 05:18:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df12af6b-77f2-399f-946e-0185b10e69e5 | -18.27186 | -53.32646 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8aad4466-7e7c-35a2-b457-04d437d47c74 | -15.60684 | -52.54592 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6d974db2-2825-334d-83fb-06399286f161 | -13.60163 | -48.70222 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5dc53e6-5964-3ad3-8972-79730b5070e1 | -14.86449 | -51.50384 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a717b02d-91b8-3532-ae2c-0a5918062a81 | -15.18444 | -56.82598 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d8afb1d-cdc2-3093-b28d-04a1724bfcc7 | -16.09791 | -57.70238 | 2025-10-06 05:18:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 83d9f772-2beb-37ff-a6df-20a8134adb4c | -14.8784 | -51.47804 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d4347a-aaf1-30ee-a921-942980fcec81 | -16.02829 | -51.03254 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c39a8894-7fe0-35e2-b5c8-2b7192f104bd | -18.26531 | -53.32316 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ebb810a-0cae-3c9b-8600-edb7d6c974e8 | -15.34361 | -47.31791 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 9ba987bb-5446-3103-b96d-6a8bbb2a2108 | -14.87349 | -51.47398 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9b08defe-420e-34dc-9d3a-da155d6ab5c9 | -12.90509 | -54.74426 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7ed3612-1bc9-3350-809d-fb6ac77ba026 | -18.17766 | -53.37362 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ad3f0158-c7f0-3d6b-993a-11064bf49f9c | -11.86973 | -56.88169 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4e35f36-5b72-35f8-ac57-9851327d26ee | -15.59686 | -52.54596 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0c7766c2-71fb-398a-b496-60d1e04716b6 | -18.13379 | -53.40873 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 8f369e44-cc70-34d6-93a6-7b87083d2d7a | -12.91086 | -47.29958 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e46a514b-69aa-338c-8e39-4a31e70a3545 | -12.91604 | -54.72615 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a001447a-0c1b-33e4-80b5-a6655b750bd9 | -14.84441 | -54.79305 | 2025-10-06 05:18:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c0a217d-2d28-3df0-9ec2-ec2b5195e23b | -15.61124 | -52.55149 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 57213f52-d76d-3109-b366-e98c4ae773ce | -13.2411 | -48.46661 | 2025-10-06 05:18:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5957bf8e-8a6e-332c-9db4-19adeb728774 | -11.91856 | -55.90952 | 2025-10-06 05:18:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5b5b056-7be0-381c-bc2b-135ed0c0b557 | -15.21213 | -56.82036 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80190978-d23d-3650-a5cd-37380800e70f | -14.68386 | -48.40116 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 15fcc2be-fa4a-3fce-94ea-e33f40d06f08 | -13.08149 | -47.82959 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98d70e48-6e4f-3121-a344-5995956d923c | -15.22361 | -56.79333 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14180a4f-280b-3018-90a8-efda66ef7d12 | -14.68441 | -48.39603 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1fc2ba66-a879-3449-86ca-4aedf682165a | -14.86816 | -51.47332 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1af69e84-5c35-3629-826f-dc69793590b5 | -18.27249 | -53.32078 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3a880b7-26de-3ee2-b1af-2d878f0a7b2d | -15.56675 | -52.45636 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 79ce87d5-439e-305b-8af7-228a96fd77ca | -15.30181 | -59.23727 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f50b446b-d9cc-3bba-82fe-1976350f263b | -13.03545 | -58.77067 | 2025-10-06 05:18:00 | NOAA-20 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1fcf454-2d25-3b81-9fbd-179243d06813 | -15.99744 | -55.99035 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e8a44b35-1c34-3e54-ab19-5e2f992a7aca | -15.19442 | -56.83716 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1b721e6d-37a3-3315-b085-f0dea53336c6 | -15.5778 | -47.27674 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 73691031-b163-3ebe-92a0-bfc8e113ff16 | -14.87198 | -51.47455 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3132049c-f1cd-3c02-bc8c-195342cb41c2 | -13.36033 | -48.03978 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf779d31-92a3-3201-b621-a87c7ba6c620 | -15.20322 | -56.82917 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f5737ba3-98a3-3e45-870c-86e9f430d14a | -15.30722 | -56.94105 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca8f9355-e3f7-35c8-a6a8-714c70b8f393 | -15.99401 | -50.93143 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 84bc7725-1aa6-33c3-b799-9561f75c4624 | -14.68704 | -48.37547 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51126ea9-8e5c-32d8-95d6-bdecb4e54050 | -14.32162 | -52.98095 | 2025-10-06 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 25e480be-1537-3475-adc4-00812b421389 | -14.61361 | -52.51378 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 78ecfb29-1871-339a-8a73-08dee6060d2e | -18.11563 | -53.39415 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 84bc4109-5eae-3921-8dcc-45466f1f2d71 | -14.34303 | -47.72164 | 2025-10-06 05:18:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5651c86-8b22-35cf-9d1c-5683849ada8e | -15.57275 | -52.44894 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cbc04c2-996c-32e0-8388-633ac5868c68 | -12.2952 | -64.02219 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 783c2fb2-7268-3a82-a29c-a3137df8bcdc | -15.22031 | -49.28158 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 99ddd9c6-3e5d-37ef-af61-71f4e0862bf3 | -14.67738 | -48.40621 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4e7323e3-6f0e-36f9-b052-07776ab3f816 | -14.63108 | -52.54555 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19e49e44-0600-3079-995d-3863f0d186eb | -14.6785 | -48.3903 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70323023-ec1a-332d-bacb-945d534c3f8b | -15.34402 | -47.31282 | 2025-10-06 05:18:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 935522fc-b20b-32bf-b434-8b69e51e0b5c | -18.24113 | -53.35962 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b7d4c1fa-f38f-3f50-9b23-be4c9bbe7622 | -18.19453 | -53.37542 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71ff1473-acd3-37a7-8eef-1f7853b29064 | -14.56053 | -46.68811 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4724b6cb-f79e-301d-81ae-020398caa6b8 | -15.18378 | -56.83074 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7c9aa311-e558-34a0-9cf0-bdebf4a3cba7 | -11.83818 | -60.43147 | 2025-10-06 05:18:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b417ea0f-d622-3d9e-95e2-4d27847d6da2 | -15.87946 | -59.37701 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609b8164-0828-340f-9bd4-55d66ea1a5da | -12.38686 | -63.71886 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 165d2993-94a4-377d-9a33-a478f8877e89 | -13.68311 | -47.3594 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 473b6913-69b2-3aa0-9351-065af320facd | -13.26824 | -47.18159 | 2025-10-06 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c00354ff-059b-3e85-a2fa-984676872831 | -14.93873 | -46.83197 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80ef1782-6c38-3b86-8853-492ed0fed765 | -15.65856 | -53.83448 | 2025-10-06 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27eab13e-36ec-3bac-9bf2-2e5b0ea56958 | -18.13873 | -53.40892 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a93da110-3a65-3276-9473-c990663c3241 | -14.63311 | -52.52834 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4884c1e9-2fe6-36d7-974b-27fc8139bc9b | -11.95958 | -55.25788 | 2025-10-06 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 937d90dc-91aa-38d7-af61-36755ccdb139 | -12.9066 | -47.29662 | 2025-10-06 05:18:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da4205ba-b038-34b6-828b-072f4d83ff8e | -13.71752 | -48.08451 | 2025-10-06 05:18:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f3d9981-8e87-32e2-b221-515d2c8ffdb3 | -13.27386 | -47.63502 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f083312f-12c0-3f7c-a388-3a3bb69823a7 | -15.17826 | -52.77314 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8633cb9d-783c-362b-aad6-22fcfdc0f96a | -15.98811 | -50.93354 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21739789-7f08-328a-98eb-a72318794b4f | -15.59687 | -52.54435 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README70.md)
