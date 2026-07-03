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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b2e1a25-de8e-3df7-815b-42576db19518 | -12.50456 | -43.8071 | 2026-07-03 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25c523ac-5331-3403-98d3-706662802032 | -12.50045 | -43.80635 | 2026-07-03 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66c8d2bb-2ee1-34c9-a514-3bde0407b810 | -12.36286 | -47.43312 | 2026-07-03 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fafc6f00-4812-3d36-b93d-afa303bb6c14 | -7.01602 | -45.43026 | 2026-07-03 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8709d8b2-35f2-3e00-8c26-60ab2d281036 | -12.74638 | -44.53653 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| ceca9469-b270-374d-9309-27eaa2262b9e | -12.7486 | -44.52415 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 212af464-97a3-35be-a3e9-cacb8bbbbf9a | -11.85143 | -48.24455 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cfb6e4a2-3fe5-3c3a-bd82-82e20bfb84c0 | -8.38493 | -48.2282 | 2026-07-03 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 073ccc13-16c5-37cd-9287-885dcb268f7f | -9.20173 | -45.32342 | 2026-07-03 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36638b2f-6b64-3508-b574-5507348c4fca | -12.49978 | -43.81009 | 2026-07-03 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b722164-4c27-3345-b4f0-b27ccc0c6904 | -8.38062 | -48.21851 | 2026-07-03 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6dc4a9e3-1a82-3c45-bf3c-928a61ad56e5 | -11.53256 | -46.6416 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fab55c0b-148e-3dea-9621-547a0a575c24 | -7.91718 | -47.82352 | 2026-07-03 04:00:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a65df109-cf92-33ab-8ba4-55538918521d | -9.19212 | -45.32159 | 2026-07-03 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4807f83a-4aeb-34b0-a339-39c40f43a549 | -10.94673 | -43.05174 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 982e0a98-947e-3519-a47d-0d8c5e3f8d81 | -10.93529 | -43.04598 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| fdd5739a-ffae-37b2-b839-956c432d5381 | -12.86566 | -44.35077 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 591fa717-0091-33df-b83e-0bca3797d8d5 | -12.75423 | -44.5423 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c205388b-48d3-3189-b4c6-9885c9c4b17a | -10.93807 | -43.05383 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| d5ea9f33-086d-3e62-937b-67e45c803a7b | -10.94271 | -43.05101 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 4f500c9f-eb5e-38dc-8e29-0373b44ee57e | -8.38573 | -48.22388 | 2026-07-03 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a56b0109-b7a9-3c10-8b95-163f2b9a7ea1 | -11.4403 | -46.53271 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de7436c6-9760-3f77-bea7-f79e33cf2a4a | -7.27471 | -44.49905 | 2026-07-03 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a2a027b-f096-311d-990e-87ca57bf06ea | -11.4397 | -46.53583 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf7695c2-8d29-3eb9-bf58-7b264693c852 | -12.357 | -47.43528 | 2026-07-03 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e04a936e-b68f-383c-aff6-816dd2528541 | -12.31721 | -46.73922 | 2026-07-03 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51beec42-5b99-3d22-a6c6-90487b3c6535 | -12.75067 | -44.53735 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bc2d7950-fef1-33bb-bbf9-d3f2cf6a214d | -12.50367 | -48.27582 | 2026-07-03 04:00:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7189696-d694-3dcf-b84a-50e2c1fd1d7c | -9.76058 | -47.88229 | 2026-07-03 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db9da44f-e7ef-3192-81eb-843d8222077a | -12.35764 | -47.43201 | 2026-07-03 04:00:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84023173-0bb4-375c-8ccb-f73bd519e6ae | -12.32221 | -46.74026 | 2026-07-03 04:00:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95c1472a-a641-31b0-879a-0c65ed5b4f81 | -8.72973 | -48.33119 | 2026-07-03 04:00:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c4f4b2c7-c3ba-3f7d-bd03-357678bf4fba | -12.74712 | -44.5324 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8dc6b013-0d81-34d6-85f4-1827ce4b7704 | -9.75494 | -47.88114 | 2026-07-03 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6861a60a-a76d-3d56-9a66-6006328bb91a | -11.84806 | -48.24558 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 993f9a95-7f78-3a52-b2b8-c58605c5f36d | -12.75215 | -44.52911 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| e04725bf-4c39-3dc5-a12a-1e4b1b7337d2 | -11.85914 | -48.24813 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c7a9376-2074-3cbd-8149-fd30e27cfba2 | -7.39842 | -44.43561 | 2026-07-03 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe457e68-4461-3343-8e22-11c19f8218ac | -12.74786 | -44.52827 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 7520ee02-c7ee-332a-ab38-7a932b2bd51c | -12.86989 | -44.3516 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e19d178-5a33-3793-a749-7c88f3454f12 | -12.50389 | -43.81084 | 2026-07-03 04:00:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5ce384e-bdab-3656-9990-e247aae9c39b | -11.44088 | -46.52962 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2cf7f5d-406e-34e3-9bc7-41e9dbabb042 | -10.95075 | -43.05248 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b636e60f-6dc0-39dc-bf85-03a5f485a2ec | -11.5376 | -46.64262 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca6bfcd8-267a-3df5-8d16-af0dbb6e8427 | -11.84878 | -48.2418 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d1bc7f8-1cd7-342d-95f5-9abc1504587b | -9.20655 | -45.32432 | 2026-07-03 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55c66a38-4f19-3781-b82e-2bce7f5b7e50 | -12.74993 | -44.54149 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 25ff5efc-6019-300a-be8f-2834fb5ab198 | -10.94734 | -43.04819 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 13a31a43-f95b-3329-a586-786f9e57d9c0 | -9.95496 | -49.28484 | 2026-07-03 04:00:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1daf62b7-f34a-32de-9097-3436705afd2e | -12.7458 | -44.51506 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04ed6e0a-65b3-36e7-a348-21831985d2ca | -11.8536 | -48.24683 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bcbc4192-7e8e-3ea9-ab65-b7083527ec11 | -7.0155 | -45.43319 | 2026-07-03 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8947ec0-320a-3099-af4b-5ede2935726c | -8.37982 | -48.22282 | 2026-07-03 04:00:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc1ff925-48f1-3959-807a-ae284e9ce1bd | -11.53186 | -46.64526 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 37e580b2-f2bd-39d4-a205-fe72ae0e316a | -7.01654 | -45.42735 | 2026-07-03 04:00:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27459ae3-089e-39fe-89db-45824805d085 | -7.92142 | -48.24967 | 2026-07-03 04:00:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f0c4cf2-2047-3b08-8c14-bbcc575cc487 | -11.9203 | -43.38995 | 2026-07-03 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68121939-f528-390e-be02-a168d3a42627 | -12.75791 | -44.52166 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d86ebf60-3cc3-385d-bafe-a7f36b6d8de0 | -13.30038 | -43.55356 | 2026-07-03 04:00:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33969ef2-be82-3388-88e4-3fb36b3b71cf | -12.75496 | -44.53819 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef06056a-4ac9-33f6-b119-c17e57a0e7dc | -12.74431 | -44.52332 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ad3c76c-1bf5-34d9-b57b-6b5fd55decab | -10.93869 | -43.05027 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 663b8339-2be4-3670-97b1-2ddbe677ae1a | -9.19693 | -45.32251 | 2026-07-03 04:00:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68704e83-70ac-3266-85e0-c225897496ba | -7.91794 | -47.81939 | 2026-07-03 04:00:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c7fdd4e-0376-3431-9c13-3f04d02e87c8 | -12.50774 | -48.28421 | 2026-07-03 04:00:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 764cd803-cb5b-3660-aa74-822c8ddad7ff | -7.27383 | -44.50402 | 2026-07-03 04:00:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1aeb622f-4736-34e3-b414-14467cd1a72f | -10.95014 | -43.05603 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 92cea6af-beb0-32b4-8de1-3437e103d28c | -9.95401 | -49.28968 | 2026-07-03 04:00:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28764aaf-b6a0-329f-8498-36dc60f7bd22 | -10.94394 | -43.04391 | 2026-07-03 04:00:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b211a188-61f6-3346-9f70-51839549b67d | -11.8562 | -48.24966 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fba1eda4-bdcb-32e3-a1b5-89d5bebd8f04 | -12.74357 | -44.52745 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eb8e70d-84a3-3bb7-82fe-7095f6c9b1a1 | -9.75716 | -47.87968 | 2026-07-03 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd2c7ef3-4a71-395e-b63a-1b2a7573be56 | -12.74505 | -44.51919 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9a20082-7a19-3866-a94a-584ea9c11794 | -6.7246 | -48.11388 | 2026-07-03 04:00:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58686b1d-1dd1-3010-a5fa-1e5565b975a1 | -11.53706 | -46.64545 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8219601d-41ea-30a5-9513-516a95e8619b | -11.85067 | -48.24838 | 2026-07-03 04:00:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9517515a-2789-3e1a-96b6-30ed212f3af8 | -12.75008 | -44.51587 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 9adab876-f822-32ca-950e-1d1e95c554e4 | -7.23035 | -43.21143 | 2026-07-03 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 102fe91c-5e26-337c-90f1-521db48130de | -11.43471 | -46.53471 | 2026-07-03 04:00:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d28cdb1-382e-3445-ab13-f4b49198cdf0 | -7.23105 | -43.20732 | 2026-07-03 04:00:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02f48c2d-d1a4-334b-a552-adc9030e8295 | -8.73329 | -48.33007 | 2026-07-03 04:00:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3eb51706-c1f0-3653-a70e-d2aa768a2c6c | -11.91222 | -43.3884 | 2026-07-03 04:00:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59e67a51-c6a5-365b-8c85-4aa3626f2136 | -12.85123 | -44.4065 | 2026-07-03 04:00:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f45a1948-3bb5-3df3-8259-2d855ead9890 | -13.30437 | -43.55431 | 2026-07-03 04:00:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1294a650-2c79-3d89-b0c6-d4873c65179a | -17.2564 | -42.66063 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d192f776-421e-38ef-8ef8-ae0eae4c5572 | -13.98752 | -47.44017 | 2026-07-03 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ccb910a-e924-341c-bd58-559dfa9e0175 | -14.41209 | -44.59512 | 2026-07-03 04:02:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6820e763-7b39-330c-9c9c-60c72ed9ea21 | -17.26074 | -42.65707 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91e04805-4326-3244-86a6-c838ad7c1eda | -18.52418 | -47.24165 | 2026-07-03 04:02:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d3199a6-0d99-3928-a895-0a651a8cff7f | -14.41283 | -44.59112 | 2026-07-03 04:02:00 | NPP-375D | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a98b3d2-a30b-3ca4-ad56-67dedbc85055 | -19.84437 | -49.07172 | 2026-07-03 04:02:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ff9b9483-c2b4-32b6-9a08-dc7388c3f397 | -17.25714 | -42.65642 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1076cc7e-42ca-3de8-8e16-ee9f9f7e4c58 | -17.31044 | -42.64861 | 2026-07-03 04:02:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 1953fdad-0528-39c2-a5fa-0cb677e31d42 | -13.98692 | -47.44319 | 2026-07-03 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2bb47d48-cfdd-397a-aea1-c8bbba865536 | -12.66899 | -48.21796 | 2026-07-03 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e06b9319-6099-3dda-8530-99bc80f148c7 | -12.66828 | -48.22156 | 2026-07-03 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bb9f433-4fef-38d1-b679-8f5b56377b7f | -13.98632 | -47.44627 | 2026-07-03 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7e22112c-f08f-304a-8413-342ab0f4dff0 | -21.05983 | -43.19888 | 2026-07-03 04:02:00 | NPP-375D | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 23ce694a-05a3-3688-bfa9-4aec4e276ec9 | -20.43123 | -47.55432 | 2026-07-03 04:02:00 | NPP-375D | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24e23d5e-52a3-325e-a8ee-cf06985ca3cb | -13.98178 | -47.44245 | 2026-07-03 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README9.md)
