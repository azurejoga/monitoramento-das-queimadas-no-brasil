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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c8a1c49-6e30-340a-9cf9-1efdc7359208 | -14.32705 | -52.97636 | 2025-10-06 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 928447d0-cde2-3ae7-932c-de282248d367 | -14.62497 | -52.5436 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce57d8a7-a76f-3ecb-ba45-77f157f1eec1 | -14.88822 | -51.52139 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e15760a4-0b1f-3c91-88a4-58404fcfef31 | -18.19881 | -53.38155 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6efb7ac4-9d74-3e95-bfc8-3ebe84abd05a | -14.62428 | -52.5089 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3a5b8621-9cdd-38f6-8228-5151743c36e9 | -14.86704 | -51.47047 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3b93d0c6-8eed-3fe0-8907-17eedf74d64b | -15.58798 | -52.44988 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc74d693-53c1-3169-91c5-3b30cf644fff | -14.67206 | -48.38941 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e6d3b5a-9a10-3478-a8a6-7deeea850b97 | -13.26545 | -48.478 | 2025-10-06 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26f4e5cc-2f73-3c3d-8906-78c7d4b34782 | -17.70781 | -56.77593 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 52518ff6-2c7c-3b8f-92cd-283bd811f110 | -15.24496 | -53.78691 | 2025-10-06 05:18:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ffb6631-02df-3e3b-b08b-b735951abf1d | -14.99765 | -56.02909 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e5ea30d-e56e-3456-86e3-a17318882b3c | -14.91859 | -46.86442 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 59a5541b-9327-3d42-9c6f-98831b64d0fe | -15.62263 | -52.54291 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ee84ef3-f082-3513-8041-c0781fdf993b | -14.65507 | -48.36482 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c3f9ae4f-69bb-3429-bb78-83d68fde90b7 | -13.33296 | -48.05175 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7487beb4-1f4d-32a3-b3e3-4817f33764d3 | -14.87636 | -59.64792 | 2025-10-06 05:18:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe74c26d-7fbf-32ca-acb4-da3e229d6abe | -16.00765 | -59.52343 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 229e1ae1-5bb0-3340-9db0-c579c3c169e4 | -14.69504 | -48.29652 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 530c1a4d-3da5-3822-b586-aaed3f9c74c3 | -14.62927 | -52.50917 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9350693c-d2dd-3b24-b298-eb0e7b911acf | -14.69458 | -48.30214 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7717578-8bc5-3f2f-99d1-ab0904d82997 | -15.18815 | -56.82693 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b9bb433-a40e-3300-ac92-f1be68c511b7 | -14.90974 | -46.83529 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdbb4f0a-516e-3a31-a82c-1ddd6923484e | -15.21525 | -56.82558 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c1850ab-d3d4-34ff-acf5-f596a5dd3e94 | -14.63414 | -52.5505 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 11cdeadc-1e52-31c2-8c86-66c56bb0769c | -14.7002 | -48.37116 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3cac3a68-6e97-30d6-9eca-0c74dc8385f3 | -15.60552 | -52.55665 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 34919e3c-7411-3f07-be62-e524d393fb0c | -14.68484 | -48.3971 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6ed0e928-c3dc-32b7-9183-189955965823 | -12.3846 | -63.73203 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| afab7397-bb6d-3b26-a6a4-ff4ed0aa6899 | -15.99716 | -50.84818 | 2025-10-06 05:18:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e114adb9-9c84-30ab-b655-b7ccbc27c198 | -12.94935 | -54.73066 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3cddc14-4bc3-3660-809f-4c73d07d60ed | -15.62325 | -52.53765 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a06999f3-b6b7-34b7-92af-dadb1da5b9cd | -14.67193 | -48.39552 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2101d36d-1c53-3135-9c1e-b0991b953e2b | -12.92906 | -54.724 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f96242-903e-30bb-a4a1-ce39fe32e415 | -14.92958 | -47.13206 | 2025-10-06 05:18:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 940d7fa9-ba61-3100-b6d3-cbb11cd89861 | -13.55437 | -47.2445 | 2025-10-06 05:18:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f0aa0bc-e3d5-3ace-b00e-a581bdf2798d | -14.70608 | -48.37726 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf1ee710-dc1e-365e-b36d-e62e8fc0a793 | -14.71138 | -48.38856 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bc977e98-4c21-3e21-b14b-fc9c3943096a | -17.84444 | -57.63607 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6f2368b5-2a9b-321e-9127-9ea05661a9ca | -18.18693 | -53.37933 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 662c5f56-9feb-302c-bd1d-cd054b77b9ba | -17.84286 | -57.62028 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4acc42aa-c482-3a91-92fd-265e82294d82 | -14.62951 | -52.51619 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe62d9aa-94ea-39c6-a66a-cd158581e3af | -17.84073 | -57.63541 | 2025-10-06 05:18:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 830fcec5-042e-3d8c-9b30-24fb3a7e5039 | -14.70551 | -48.3824 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d531bf01-9b59-31cd-90e9-e6934cc9d8bf | -15.98653 | -56.01068 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5b605b80-ef6b-3c30-9bc0-b188c594b4c8 | -16.02631 | -51.05056 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7c06b7d9-03a2-3622-9fc1-82a4ac5ae325 | -14.62854 | -52.51503 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a0bfc37-d9f2-3605-a4ab-ee80b7f42e10 | -18.12346 | -53.41233 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dbfa0cea-fe4a-3bdc-9e13-dc281f1800a2 | -13.26205 | -47.84953 | 2025-10-06 05:18:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2c30aca5-6b3e-3a5d-8448-2d3ea30178e6 | -11.91405 | -55.91375 | 2025-10-06 05:18:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edce597a-713f-372f-8695-55b867b28fca | -14.71193 | -48.38351 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3600c57b-9dae-3549-964c-e3f444e46770 | -14.64344 | -56.0184 | 2025-10-06 05:18:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 37d874f8-71cc-34e9-9872-0540d5f352ef | -15.87607 | -59.37648 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f8e204e-6623-3b7f-92a1-12e8e53f93d7 | -14.66676 | -48.37786 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8357ef5f-a7b8-3712-83bd-56d87ffbfd39 | -16.03495 | -50.97203 | 2025-10-06 05:18:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 958db6bf-9c85-3a7d-bfeb-61a695c9fe7e | -15.19943 | -56.82876 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68cbfae8-fea6-3f9d-aec6-1b1733afb991 | -11.87424 | -57.81676 | 2025-10-06 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e6da742-dc83-3b5a-a484-0a9656f006e1 | -16.3441 | -51.45563 | 2025-10-06 05:18:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ebbe5d-8d57-3059-b095-8a66db3b463f | -12.38094 | -63.73138 | 2025-10-06 05:18:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b602492a-e5e5-366a-9243-19eb40a76530 | -14.67991 | -48.38124 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f08086ef-4ab7-3b03-8755-d0237fdde394 | -13.34655 | -48.04765 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f87a5e89-70a7-34a5-9314-d252c96c6cd5 | -14.68381 | -48.40718 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0410dc8d-dbe2-35b6-a2ea-215b890f87c5 | -14.56122 | -46.68103 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e56177b-13a3-3ce5-945c-1e25444b6e17 | -18.12407 | -53.40704 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16ef51b8-b4a1-392d-883a-d8ef6d928723 | -12.92959 | -54.72012 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2764d61-9597-3d84-beae-4b4981dc6da6 | -15.20595 | -56.80951 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a592f2d9-87cc-33ce-897a-2cf720d85032 | -18.18033 | -53.36891 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc86efee-64b5-36fd-923b-0e544d4e5a30 | -15.5072 | -46.84295 | 2025-10-06 05:18:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bafcb78-e95a-37c5-a4c0-c7a6a45136f8 | -16.43736 | -52.17395 | 2025-10-06 05:18:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42090452-9d7b-36cc-9e01-cd801d78a7d5 | -14.6714 | -48.40076 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f550d0b0-f402-3ce0-8bab-45ef8b47e57e | -15.59619 | -52.54992 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0e7a1de6-b006-3408-a82f-e2368f42fb5e | -11.91787 | -55.91427 | 2025-10-06 05:18:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11011f3a-9d3c-35bd-852b-d5e14e0706bf | -14.60586 | -52.49501 | 2025-10-06 05:18:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc6fbfbc-e362-3028-bb8d-5dfbd0951db8 | -14.55752 | -46.64457 | 2025-10-06 05:18:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| deb4bb70-9631-322d-a8bc-d321ddbb2fd7 | -15.59258 | -52.53902 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b81a4d4-6f8e-3c2a-9e33-f569be546940 | -11.8655 | -56.88537 | 2025-10-06 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6846ac06-0cb4-34bb-b9e9-747b6486ed9c | -14.32096 | -52.98617 | 2025-10-06 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 085aa2f0-34df-3b2d-b7b8-610ba5a2427c | -14.86243 | -51.47605 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 300aab23-77b5-3ce9-9807-42dc6efa4ec2 | -15.99453 | -56.01181 | 2025-10-06 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d76e49ad-2415-372e-beec-5b67975c4379 | -15.19007 | -56.84082 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df916257-bf1a-3c81-a630-f509f12fcf36 | -15.65894 | -53.83194 | 2025-10-06 05:18:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5942ba0a-f95e-3aa8-853c-7677cc46e134 | -15.60122 | -52.55222 | 2025-10-06 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4f58ed18-cdb6-370b-8f43-537e1db3c70a | -12.94518 | -54.73015 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7163b9b1-264d-3380-80ed-d16beef1a1f4 | -18.18758 | -53.3739 | 2025-10-06 05:18:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6f55730b-74d5-358b-906f-df5c8a6bb505 | -12.90615 | -54.73652 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a296f413-bdfb-30ac-b957-851ebddedd80 | -18.28001 | -53.32561 | 2025-10-06 05:18:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69616cd8-d938-3be5-aa21-db018f5dd2d9 | -13.35979 | -48.04457 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c4ba5239-141e-3e84-914e-95a1216fb073 | -15.22733 | -56.79429 | 2025-10-06 05:18:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8e8ba9d-d1b6-3758-9a22-243932aedc03 | -13.60838 | -48.6987 | 2025-10-06 05:18:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a883f872-3660-3869-b267-770bed2c01f5 | -13.26723 | -47.63406 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1339a2fa-497d-39c6-8118-c283b33e2654 | -15.22672 | -49.28481 | 2025-10-06 05:18:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb7f0503-6fbb-3078-956b-107ae5a646cf | -13.35304 | -48.04846 | 2025-10-06 05:18:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 83b9e6ea-16f9-3233-a60f-c36ebdb3d8fc | -15.99134 | -59.5399 | 2025-10-06 05:18:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb42de0f-0600-317d-a486-0687ca8fea6c | -14.86775 | -51.47672 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ee2b3fcf-c485-3d38-b217-662cf60bd85c | -12.32188 | -55.12742 | 2025-10-06 05:18:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 610f8f28-90fc-31dd-8077-cb8674d7ea1f | -12.90925 | -54.74487 | 2025-10-06 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8208640d-ec82-359a-8ab7-05c940034372 | -14.4891 | -47.55171 | 2025-10-06 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abb3f47b-f5ec-31c3-9db6-000716a1368b | -14.9219 | -46.82891 | 2025-10-06 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f892c512-fa91-3e61-a694-91695bf7563d | -14.70584 | -48.38353 | 2025-10-06 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8bf7f452-0163-3742-82aa-933cbeebba6d | -14.87308 | -51.47738 | 2025-10-06 05:18:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README73.md)
