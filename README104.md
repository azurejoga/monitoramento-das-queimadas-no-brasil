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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87cf4d7b-28c4-39da-a2c0-09abeaed66ac | -16.90354 | -55.7817 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 51ea125b-b1f1-3006-b411-e8704f256775 | -16.90275 | -55.78549 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| b74dbb77-78a7-3820-b306-12817335b274 | -16.90196 | -55.78929 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| d532a4e1-4571-36c6-9b09-2acf2bf8a308 | -16.90117 | -55.79307 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.2 |
| 58401909-18aa-3545-a41b-89223e1c472e | -16.90038 | -55.79686 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| d9065d44-fc3d-3f7d-b77c-42e1ddd2e948 | -16.89804 | -55.78046 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a4b1f4ea-1362-3201-8879-059f651c806a | -16.89725 | -55.78426 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 3fc2036b-d708-34e3-8c35-71d717696c66 | -16.89646 | -55.78804 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| db5a78dc-9f1d-3d36-a027-aa43d66032b4 | -16.89566 | -55.79184 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| d9cd6ff8-0e3a-34d6-91ee-28442b122b2c | -16.89486 | -55.79564 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 77d3eb76-0560-36ba-8a72-d16a8591c627 | -16.89174 | -55.78303 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 9220872f-22e3-3d15-b7e4-82336985b7ca | -16.89094 | -55.78682 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 36de36f8-3421-3e2c-8afd-ce02e38d90e6 | -16.89014 | -55.79064 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 81fd91da-facd-30ef-a127-0a4e909ab330 | -16.88934 | -55.79446 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 54b4a826-1e58-36f1-9773-5937901c2cb0 | -16.88622 | -55.78182 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 60341d6f-64e5-3a33-b9d6-9ac7e81ccd18 | -16.88543 | -55.78562 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 71eabdec-f835-3114-a3d5-6cecb46a7ddc | -16.88463 | -55.78943 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 42351197-03af-3554-9eeb-4e769acd6cb7 | -16.88383 | -55.79325 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b0b72305-5a03-3d90-a8a7-d0822edc0796 | -16.87751 | -55.79583 | 2024-10-09 04:19:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e29238c5-482a-3656-90b9-700a2630a90e | -16.16542 | -57.42058 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a77cc298-1a61-335a-8210-cf036e9c8afa | -16.16451 | -57.41809 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 507e98bd-da48-316f-9a06-50fdcf45744b | -16.15933 | -57.41887 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f9520a2c-22e7-3a82-8139-3bed38f5f018 | -16.15838 | -57.41657 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0179c2cf-1f3e-371c-ac74-6c4790e8faa6 | -16.15583 | -57.60487 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| db91a92d-edee-31ae-8fe4-8b31f1d2d1b7 | -16.14087 | -57.40811 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5f86f6d-ecde-3c68-99cf-8c4f69b4c26d | -16.14005 | -57.41177 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4927a3c2-5e49-3f60-839f-06fec481e7e2 | -16.13339 | -57.55866 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| f2f33d40-e56a-30d3-850b-42041b3f1d19 | -16.12999 | -57.55559 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 8ea16f0a-4a25-3f54-a723-30a0e7c261e1 | -16.12908 | -57.55981 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 09a0640a-91f7-31b5-b971-2658b9feafe2 | -16.12729 | -57.55676 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| cdae5645-d902-35d8-9e23-34757878fc2f | -15.95403 | -57.21571 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f8ff188-2932-35fe-98d0-fcaa056e4449 | -15.95302 | -57.2204 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9104a4a7-ac14-3894-9636-3e99b6040165 | -15.94805 | -57.21373 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d4e835a-3402-3cd9-9a96-ccc8c6a0c1a1 | -15.94698 | -57.21872 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4b9290a8-92ca-39bb-ba7a-fe20b13b83a1 | -15.94193 | -57.21242 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5ae5b73-01f5-3575-9ed8-911e079db0c4 | -15.94083 | -57.21752 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 44cfaaef-64b5-3bdc-b107-bbd3a7083c34 | -15.93575 | -57.21135 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b9af842-b6cf-3496-acf0-73c2c32078ab | -15.66119 | -57.38796 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0a34978-1daf-3a03-9012-0ceb88216b91 | -15.65516 | -57.38574 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d99a912-d3f2-3983-84b8-e4c8eff6e5b5 | -15.64896 | -57.38437 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd29ef2b-663a-33e2-b6f2-3ac3846430ec | -15.646 | -57.37776 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce0d553a-b4c0-3a5a-9b04-00121a4d7b0f | -15.64515 | -57.38181 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b7d5ebc3-7ab3-3b07-8f85-b869dcba8f92 | -15.62845 | -57.36861 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6490178-a519-35e0-a4da-3fbe2fa876b5 | -15.6262 | -57.36945 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6214ed60-c086-38f2-bb12-c5dc32913722 | -15.62236 | -57.36674 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79a2d53a-6ba9-3d27-ac3c-140f462bad9e | -15.62086 | -57.36414 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a001139d-a7a3-3a26-83ba-5bb48f7337e4 | -15.62009 | -57.36765 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a2d92fa-ead7-3cb6-9fbf-89b1345a8bbb | -15.61618 | -57.36524 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9de640c8-ceb5-3b35-a58e-8e1e50c7f999 | -15.61388 | -57.36634 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f02e8171-e4a1-31e5-a069-ef4514a51911 | -15.60899 | -57.36843 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4e9a3dd-beec-3ff3-82e1-c48dc7ce7e64 | -15.60766 | -57.36501 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7e526661-a04c-374d-80b1-76620145bf44 | -15.60263 | -57.36779 | 2024-10-09 04:19:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70d059f9-dff1-3824-ba21-c8680e0009b3 | -16.62126 | -57.1104 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 8d4dd753-83bc-3088-83fe-72de126d45e1 | -16.62024 | -57.1151 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 08d19abc-9a96-3d46-96a2-937d9ee34e67 | -16.42679 | -57.32973 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a4c122ce-5022-386d-88a9-058c6e9c64d4 | -16.4207 | -57.32833 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 0207a2ff-ca96-3414-b6b5-73c47afdfef8 | -16.4146 | -57.32694 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 35656f33-ed84-3cf6-81f6-b8a8f349a8ce | -16.39225 | -57.69451 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| af19ab63-db4b-320a-ba81-50a98ec9f7c4 | -16.39105 | -57.70001 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e420db52-dae3-34b9-93f7-7dde84ff86c1 | -16.38988 | -57.70536 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9c6978da-08a9-3e3b-bb14-c38fad92b5f3 | -16.38252 | -57.70908 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bf010be7-48bb-36a8-b718-f6247f31f2d7 | -17.17619 | -57.31667 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 349e274f-9191-316b-9115-bcde1b507d30 | -17.17517 | -57.32141 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d8a0070b-2e65-3d3e-9894-2782e03b5bd5 | -16.98206 | -57.47802 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 1454a019-f35b-37ba-870f-da277731b5e6 | -16.98099 | -57.48289 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 33.1 |
| 17456195-e940-300e-8a73-0b38323db1b5 | -16.97704 | -57.47172 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| ef244bee-b217-3add-829a-eaa604af6a6e | -16.97597 | -57.4766 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| 63037d1f-adb5-3d05-97a7-033e2168aa60 | -16.97095 | -57.47032 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| f8721f10-7f37-3ee8-b3fe-10f4ab7db921 | -16.96989 | -57.47519 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| d392675b-9d8b-3a2f-b68f-0c442c21e2a8 | -16.96882 | -57.48007 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.3 |
| 93021132-abed-3fdc-83f5-1b82a14b3834 | -16.96488 | -57.4689 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 260c32eb-cfca-330c-bfb3-75b941b24f79 | -16.96381 | -57.47375 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 196e6349-b12a-31ea-8352-a0c99d70243e | -16.96307 | -57.44802 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| b41f2d5b-b74e-36a2-b082-3098a4045a21 | -16.96093 | -57.45776 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 3989d6ab-3f78-3a13-8f18-986b8e24793e | -16.95987 | -57.46261 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 0d3ab609-087b-381e-bdac-f66c92e5773c | -16.9588 | -57.46746 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 65b12bd9-ea2b-37ac-82bc-c05dd32af213 | -16.95844 | -57.49821 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 452f61b8-9d56-302f-9584-3a9fb35d93b1 | -16.95773 | -57.47234 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 4e728908-f4fa-3290-a875-6a8f8340c7cd | -16.957 | -57.4466 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 6af709e3-6594-3250-8b2b-d85b2c6e5cd9 | -16.95665 | -57.47724 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7442f50b-b8fe-38aa-877c-70c35c5586a9 | -16.95592 | -57.45147 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| e768a3fa-4589-33e8-8df5-dd68dbe9d01f | -16.95486 | -57.45634 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2944590a-4685-3ebd-aa68-edf6a9f653ff | -16.71115 | -57.46231 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 6048450a-b438-3ff9-bed9-29fc012028d1 | -16.70504 | -57.46087 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a9c348be-a941-3873-bcf6-820d0d4f7e0f | -16.70463 | -57.46058 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 019a4947-e91a-3735-ac09-b39185fc5c97 | -16.7 | -57.45451 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1b254ce9-6104-372a-b656-107ef53aa729 | -16.69961 | -57.45425 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5d9790eb-0cd4-3d02-af26-cfcb8e898bc2 | -16.69894 | -57.45945 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1ac6391f-3662-3987-9399-b913da1f279b | -16.69852 | -57.45917 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 7a90861a-de29-3f0a-a234-a9fd86a2b8d1 | -16.69601 | -57.44324 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5d24056a-7e47-32d2-99a7-e8ae17d1294a | -16.69569 | -57.44302 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5a52dbf2-42dc-3cb8-ae87-a3c5f8317b26 | -16.69495 | -57.44816 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 17a7675f-956e-3504-8f25-755f06b51e78 | -16.6946 | -57.44794 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 5b5f232a-fbfd-3d05-944f-fefbdad95254 | -16.69389 | -57.45309 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 1214a613-b761-3bf0-b954-3207449fe67e | -16.69351 | -57.45285 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| d5f25df8-2d10-3594-ba6f-ca5c81d8fcc7 | -16.69283 | -57.45802 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 23b0a149-af22-3100-a99a-c206097d56a3 | -16.69241 | -57.45776 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 83970400-fcc3-3dc5-b2a0-45065dfe8080 | -16.68779 | -57.45164 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 26a1acdf-e080-348e-b459-67057a024d0b | -16.6874 | -57.45143 | 2024-10-09 04:19:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| fe0fc52c-ce04-3c51-b35e-7706fc634c9d | -16.66418 | -57.14503 | 2024-10-09 04:19:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |


[Clique aqui para ver as próximas entradas](README105.md)
