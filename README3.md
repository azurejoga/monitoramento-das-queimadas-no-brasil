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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6bdb597-260f-3acf-91d3-d6b6a5dd7bb8 | 1.11331 | -59.19545 | 2026-02-10 04:44:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d16365db-9004-3e59-bdc4-eae88e44dffe | 0.78489 | -60.67255 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 10eab420-4d93-333a-8d71-91cb53483510 | 0.77881 | -60.67348 | 2026-02-10 04:44:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82eade6a-ff55-338f-ae48-35d43a5dcf75 | 4.40162 | -60.68898 | 2026-02-10 04:44:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 70bcdc79-f5b1-3b9a-8886-972ae969571c | 1.11685 | -60.50518 | 2026-02-10 04:44:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ad355faa-6e80-31d9-8024-8b3194ac0aab | -3.207 | -51.2636 | 2026-02-10 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| db65977f-4d05-31fb-a802-e6f809a98223 | -6.91048 | -46.67633 | 2026-02-10 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d6ab16a-ea11-35c8-aaf0-b7b5c2af9069 | -1.82725 | -54.49672 | 2026-02-10 04:46:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8136a336-bb45-3de8-b701-9c4200240c4a | -2.99714 | -48.94989 | 2026-02-10 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d25cb2c2-6c40-3823-b105-988d8501bbbd | -3.035 | -51.642 | 2026-02-10 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ff569b3-ba8d-3a50-bbe5-260f13c66433 | -4.12043 | -47.36453 | 2026-02-10 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0d880f2-5ad6-3388-b7ff-cc7800548876 | -3.45974 | -51.21476 | 2026-02-10 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9882d463-d805-3b9f-a7f6-f7243a55cec4 | -2.15601 | -47.89261 | 2026-02-10 04:46:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85d76b66-c13e-3564-90e1-92f97338aaa5 | -5.45167 | -38.38937 | 2026-02-10 04:46:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 044eee51-c140-3faa-8172-dad692af84ca | -11.0192 | -45.07683 | 2026-02-10 04:48:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07bb0a22-71f3-3a2d-8004-2110ccd3edb8 | -10.1842 | -47.77753 | 2026-02-10 04:48:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69cd93c2-4eb7-3ce6-b153-8916012d9341 | -12.47182 | -43.73527 | 2026-02-10 04:48:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c5449195-38e0-3dbd-90e5-8c4e6d6bac4b | -15.883 | -43.68739 | 2026-02-10 04:48:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97bd5e62-fede-33e7-ae64-e27f4bd08103 | -11.16152 | -49.2484 | 2026-02-10 04:48:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4606b99-4936-3700-88b9-76414738506b | -15.88487 | -43.68623 | 2026-02-10 04:48:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f523fdc2-bba6-3623-8f21-fa09ca09ae5b | -12.03211 | -45.33679 | 2026-02-10 04:48:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac3b49b6-5c39-3ac5-ae69-8fc435ed1232 | -11.16091 | -49.25251 | 2026-02-10 04:48:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624c0934-1565-3a6d-8396-78edee06671a | -19.39166 | -55.11265 | 2026-02-10 04:50:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dcab3cc-955b-31fb-b110-d6702587d3b9 | -16.44364 | -58.16767 | 2026-02-10 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 61a34c39-ab7e-3186-8850-9f0a9f59f8ab | -18.97431 | -52.92825 | 2026-02-10 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 43bfe356-2916-3243-bd53-77827a7137be | -16.45048 | -58.1742 | 2026-02-10 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| dc73a535-a02b-3643-9f89-55be24f922c2 | -16.44751 | -58.16842 | 2026-02-10 04:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 56d93218-ec7e-3cfe-b787-37d23f4a8d91 | -18.97765 | -52.9288 | 2026-02-10 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29c91fda-ebf6-3f41-b835-7fb0412c5bec | -19.39225 | -55.10897 | 2026-02-10 04:50:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e0ccb117-9401-3f65-9b27-bb4a9673596c | -21.19311 | -57.39201 | 2026-02-10 04:50:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c10fc7d2-e7b2-309c-9abc-e0cec77a992a | -18.97041 | -52.93143 | 2026-02-10 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2bd6471-bd26-3629-8f46-4840583113b8 | -18.97375 | -52.93198 | 2026-02-10 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 978e361c-18b4-3f70-9231-5f24ddaf9047 | -18.97709 | -52.93253 | 2026-02-10 04:50:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 249686e6-65d9-3049-9bec-5d8292e7d343 | -26.63321 | -53.69048 | 2026-02-10 04:53:00 | NOAA-21 | PARAÍSO | SANTA CATARINA | Brasil | 4212239 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7f5cf11f-a7fc-330f-bcdd-ca50463326d7 | -32.92521 | -52.58222 | 2026-02-10 04:53:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 19ec4d55-897f-342f-b87a-628a0c7fc9b5 | -21.92394 | -56.92699 | 2026-02-10 04:53:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff5d1c2a-8373-3c22-a72a-26a5cb62bab3 | -23.73219 | -51.63493 | 2026-02-10 04:53:00 | NOAA-21 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbdd6095-286f-399c-b56a-03d67af2f966 | -27.03573 | -52.63834 | 2026-02-10 04:53:00 | NOAA-21 | CHAPECÓ | SANTA CATARINA | Brasil | 4204202 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e6048643-04bc-35fe-bf20-1d8bf593bd44 | -32.92586 | -52.57647 | 2026-02-10 04:53:00 | NOAA-21 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |
| 6e299c54-5460-312a-9d67-3ac15ddc7f3b | -30.47513 | -56.38811 | 2026-02-10 04:55:00 | NOAA-21 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| a3440feb-c55d-3f74-b6e8-702caebae3d4 | 3.22995 | -60.81094 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff2b5503-92de-3c0c-aaa9-c96b830047bb | 3.3747 | -60.65563 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64759ddd-40e3-32c0-84fa-27b8d289f7c4 | 1.11356 | -60.50562 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4798d380-0cce-35a6-8115-97974b6be3f5 | 3.25226 | -60.41882 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea3c156f-16d6-303a-9191-d5db58c5ea5a | 0.95272 | -60.51877 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9a903f3-6159-3e1e-901d-94b06e914969 | 4.86248 | -60.6468 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0036c05f-9ba2-369d-9a4c-1e8906ff1628 | 3.30042 | -59.89872 | 2026-02-10 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cca9c546-0353-37d0-9118-12e813015729 | 0.95435 | -60.5289 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 70666c70-b3e7-38b4-b089-9c884e5cd5b7 | 0.95432 | -60.5169 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 318a91f6-b48d-3f48-b22c-48b6972e9fba | 1.11288 | -59.19775 | 2026-02-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bbe2918-a6ca-3313-96fe-9a9f47db4295 | 0.78232 | -60.66763 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8755ea9e-759f-39ce-a4cc-8d1dfc1cb0ab | 1.88009 | -60.90924 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7258e46-1e01-3747-aef9-69fd03da47a7 | 2.18189 | -61.92193 | 2026-02-10 05:14:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad5b0ace-fcea-38b3-a614-14a0d9df946e | 1.11833 | -60.51007 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a9178e1a-4426-3566-bc3c-5313a58329e2 | 0.78713 | -60.67215 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7899cf7-5b9c-3fbc-a55e-88fe14551e25 | 1.11913 | -60.51516 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| eb72a5d5-cf89-3160-af39-9d017089b071 | 3.99852 | -60.93481 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f762c647-f33f-3b87-aeda-f21df3c26967 | 1.82264 | -60.50414 | 2026-02-10 05:14:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d15eab96-389f-38d7-a891-04a474c54369 | 3.30987 | -59.90754 | 2026-02-10 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 42aec423-4846-3472-919e-a10c3fc8abd3 | 3.31382 | -59.90695 | 2026-02-10 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983b3c2f-3b2b-3867-a590-53d9a7749ed3 | 0.95598 | -60.53906 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31f9a3d5-6b40-3905-976b-8b94b293639d | 0.77512 | -60.67405 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e69f0c6-aafe-3b12-9867-26b4ee1cd6c6 | 0.95907 | -60.52134 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0b37f7a5-ddc6-39c8-b6c1-e9f3f92cbea6 | 0.95985 | -60.52642 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bbb647ca-3875-33a6-86e6-c92f77000bf7 | 0.78632 | -60.66699 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5574583-5c2f-3117-ad7d-779ba684bba2 | 3.60402 | -60.30679 | 2026-02-10 05:14:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1704d54c-daca-326b-9846-be6bf3e85312 | 0.79113 | -60.67152 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 577fbb2d-9051-3eee-9fc6-28f8eee466e5 | 1.11656 | -59.19717 | 2026-02-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02a649d2-af04-3232-9ea1-528774d41868 | 1.2782 | -60.43935 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ea40f75-0d85-3a2f-b24e-e46c6bea3ed2 | 1.28139 | -60.43366 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bebadb15-36cd-3ec1-9daa-b19c47a05a39 | 0.96304 | -60.52071 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d071c52-3928-36f0-86f4-e305d825dcd2 | 0.95832 | -60.52827 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3c7a6f7-6547-338b-bd4f-02a4ed906e7b | 0.78312 | -60.67278 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a91ed2-e648-30fb-a743-d67f736ddccd | 3.23054 | -60.81474 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e4d5c31-0b85-3d4c-a54b-9b2923dbd548 | 1.11436 | -60.51069 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a4ab07de-3fe6-3148-a1eb-3283528a9134 | 0.95354 | -60.52383 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a1f0c111-0438-3d66-8892-b476e6d52168 | 3.78592 | -60.58351 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf2a944-406e-3bc2-bff5-556dd1418672 | 3.37639 | -60.66682 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6c27a444-6e08-34a2-a560-01facfaac539 | 0.95112 | -60.52261 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 00a0da9f-7169-3d74-ba21-56b51b5e8110 | 3.78952 | -60.57915 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6487f9e5-ff23-342f-a733-839537f90d9c | 2.17744 | -61.92258 | 2026-02-10 05:14:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8a662c0-089e-357a-a091-81e9168f7299 | 1.87595 | -60.90983 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccf9891c-7723-373c-b86b-6898f52302e9 | 0.95751 | -60.52321 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e561485c-a1e3-38f1-a2a1-6f98cf126778 | 4.30481 | -61.15144 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3538391-9147-3583-a802-d1372ca6046b | 4.3918 | -60.69117 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27d93f52-d677-3c32-bc8f-85a3f07bb26a | 4.86672 | -60.64616 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81fa7c69-27f0-38dd-9bfd-28c7eacfd5f5 | 0.96382 | -60.5258 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a84425ff-a067-3d95-9b8b-865354071bde | 1.27742 | -60.43428 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5217055a-f720-33f3-b707-80fefb10b74e | 3.57831 | -60.74903 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2031f07c-28d3-3666-8a14-0f5cc3306d45 | 3.30909 | -59.90253 | 2026-02-10 05:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3fbf4b13-6c71-39a1-b030-3d66d6b9948e | 0.79033 | -60.66637 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af9ef00f-a6d4-3794-880e-f46fcbcdd1f2 | 1.28217 | -60.43871 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36fa9232-2001-35ea-91e8-a67d6d80f6e8 | 1.87524 | -60.91666 | 2026-02-10 05:14:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 168f8bb3-dc9c-3c4d-90f8-b11128f948fb | 0.95509 | -60.52197 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f081553-75fa-33c1-9734-1a13c39db09e | 1.11355 | -59.20205 | 2026-02-10 05:14:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f9c23b9-0ca8-3dc3-b5ae-8ac72beb91ac | 0.95587 | -60.52705 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff881bb9-d250-3f6d-8a11-72d068f63d48 | 3.25171 | -60.41525 | 2026-02-10 05:14:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8841995f-32f6-39af-af4d-dc61f1868af3 | 3.64066 | -60.56979 | 2026-02-10 05:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfa34781-c6b4-338c-8a8a-07a446024aa6 | 0.77912 | -60.67342 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf57bcc2-f54b-3f86-beee-cee2cc2424df | 0.77433 | -60.6689 | 2026-02-10 05:14:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
