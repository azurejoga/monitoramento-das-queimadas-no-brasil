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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7898c520-6fe0-3eff-aa9d-65990200b68c | -15.81747 | -59.50478 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7e95fe39-3ef6-311b-a98b-bbbb5acd40fc | -15.96726 | -59.41249 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ecb2ed3-7f67-311c-9cdd-f0f9cf538c04 | -15.90566 | -59.45601 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9698d998-f3cf-306f-bd50-dea548c41ed0 | -15.92505 | -59.444 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 83ded472-b3c8-34da-813a-ee7903340fbe | -20.54148 | -56.15352 | 2025-09-21 05:53:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afb8c161-7511-3f8d-b501-65802379260e | -15.97044 | -59.43397 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d05e7c7e-ef46-370f-9b82-7b489476195b | -20.60823 | -56.71957 | 2025-09-21 05:53:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17f69a2a-30ae-393d-88c7-6c8b28b5b21f | -15.95373 | -59.43474 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1eca6c00-a315-3cdf-b913-9635965f7904 | -15.81559 | -59.50562 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ac94fc6a-87d4-39f0-88a7-5275f1edc72f | -15.90685 | -59.45901 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f8e7d0a-da85-382e-9cfc-47ecfaa731a7 | -20.60768 | -56.72639 | 2025-09-21 05:53:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 06af7489-b865-36c9-8fc7-1f05ca0bc0b0 | -15.97771 | -59.41832 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 361ad703-a350-38f1-9e9f-54aefcb473d5 | -15.81445 | -59.51547 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 36c973c3-d303-3d3f-b2ec-d96684b8bb1c | -15.92407 | -59.44018 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 098b8f50-43a3-36f6-80e5-7ec1f530ac44 | -15.95161 | -59.45417 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a5a109a3-7772-305b-88ee-92acbd3419fb | -15.89555 | -59.39829 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1857513-31fd-3831-b370-52afe81884f1 | -15.96654 | -59.41903 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 22f5fcb3-64ae-3ca2-a079-423f2466b2de | -15.81825 | -59.49751 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b4e388e-fbb8-3a33-87db-14b1c38f5b9c | -15.81405 | -59.51892 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dd7a6c57-20b5-3e57-98f5-c942aa9abe51 | -15.82249 | -59.50925 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 680b233d-1fd0-34d0-b487-7ff265cd2b1c | -15.93089 | -59.429 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5665dd7d-07b3-32bb-865e-146de0baf047 | -15.92362 | -59.44411 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ca43879c-ef89-30d2-8b69-5141aadd9d16 | -15.82146 | -59.51862 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ff974db0-a50c-3e44-8707-d24335913c20 | -20.53504 | -56.14558 | 2025-09-21 05:53:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24b871a3-7996-3166-b173-22f37b9fcf68 | -15.96579 | -59.42577 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e1df8433-07b8-38a3-b5c4-1c723bad170d | -15.42111 | -58.78087 | 2025-09-21 05:53:00 | NOAA-21 | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98095e2f-d0bb-35b8-883a-1d6d51aaaf24 | -15.82182 | -59.51535 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 3df6826e-bdf8-3860-b266-5149af0828db | -15.95331 | -59.43855 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d40552a-60b6-3196-b4a8-27a02e1a8a78 | -15.91106 | -59.45717 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 567f76ea-0cac-35fe-8398-3308bd353186 | -15.95492 | -59.42379 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cdd77bef-85d2-300b-ae51-1cfc62a96a33 | -15.9654 | -59.42931 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d6af20b7-18a4-3a3b-a18c-23d30c214a7c | -15.82216 | -59.51222 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| fe350754-8d30-3a91-b5c9-3a8c909cdb1d | -15.95121 | -59.45794 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 20e2ab1b-c7ec-3b53-a8ee-b613d9b04b6e | -15.83332 | -59.51091 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 556c7511-e057-3744-a101-6c6af3b64269 | -15.41545 | -58.78012 | 2025-09-21 05:53:00 | NOAA-21 | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20133c92-8775-3094-8817-2b211a873096 | -15.81713 | -59.50792 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f55a9f7f-1961-36f2-a505-c3c97decf441 | -15.94541 | -59.46033 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fc8280b-9b0e-305b-88e5-ba15a0360d5d | -15.81598 | -59.50228 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82982cb6-7706-3ef9-93a0-edac38938787 | -15.9381 | -59.4256 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3d1ffa02-5590-3e0f-bf3c-3dbdca7e4122 | -15.8168 | -59.49514 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 918f49b7-296f-3da1-b6f4-0f3885945698 | -15.82785 | -59.51062 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6333e501-6e27-355d-b81e-f354ef777d0f | -15.90717 | -59.45609 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b46e963-c84e-36a9-be1e-a05d2b454d47 | -15.93135 | -59.43683 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45d82ad5-e855-3234-97e2-a36a9d4680f1 | -15.97859 | -59.41032 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7df8c32e-baeb-3304-a4bb-b644b614f031 | -15.97085 | -59.43023 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c16e6497-c2f9-3415-8328-9d2bb81ddb4a | -15.97814 | -59.41444 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0d1b5ad7-b9f4-389d-9b30-8e90caa16ef7 | -15.95531 | -59.42018 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b712d284-e383-3833-ba3f-8b0ec157cd5e | -15.97157 | -59.42372 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2fdd6f88-92a0-3c8f-8423-d8899bae71bd | -15.824 | -59.49531 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 218ad37c-0b87-34f8-b521-b21249bfdbd4 | -15.94611 | -59.45393 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3118155c-5a2c-35fe-b564-4c7cf954591f | -15.965 | -59.43301 | 2025-09-21 05:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a7bbda15-32a9-3792-ba6e-a6750dce9d12 | -15.978 | -59.4269 | 2025-09-21 06:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 34b0db8f-c492-3128-a38e-b26a7a8a8149 | -15.9586 | -59.4288 | 2025-09-21 06:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b4547e05-cc49-3b6b-8c86-b2ec2599ab90 | -22.4866 | -48.2229 | 2025-09-21 06:10:00 | GOES-19 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 839be4a4-e0de-37d6-8570-ef684bb18f41 | -15.978 | -59.4269 | 2025-09-21 06:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f5b50b47-10d7-3a1c-af75-109b1cb09733 | -15.9586 | -59.4288 | 2025-09-21 06:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 21a75d12-7ebf-3f1c-87cd-ef473e677b9a | -15.9783 | -59.4069 | 2025-09-21 06:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 86c95dc4-ceeb-3a97-b101-257daa5f2d36 | 4.323 | -60.74033 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fc3e2f31-e002-37bc-93e5-30258a2c432d | 3.21857 | -60.30039 | 2025-09-21 06:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2cc7a15-ef36-36a8-ac4c-e79a623428a2 | 4.32372 | -60.74457 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b7544c75-f1c1-36fb-a809-076eb2da6279 | 3.21932 | -60.3047 | 2025-09-21 06:14:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97f4f9c3-606a-3ce4-bdbf-9d248c5719c2 | 4.32751 | -60.73252 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc24f55c-8b80-3117-93e2-51c40186185d | 4.33017 | -60.74801 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1aafd21-4b05-3543-a9e6-900f1dca752c | 4.32953 | -60.7443 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6a44748-50d0-3caf-a42c-1b4f1fa2a2ae | 4.32439 | -60.74844 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 306ef1d1-69cf-3e04-89be-e859a340e5c6 | 4.33392 | -60.73576 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bdc6605-8f6c-3202-934e-2fb5a7682e4d | 4.32887 | -60.74044 | 2025-09-21 06:14:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e98c37ce-10aa-341e-a9b5-707b90c105e2 | -7.20189 | -72.68323 | 2025-09-21 06:16:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c6d39ac-b4a6-3173-83e3-ca8f07da3f94 | -9.17798 | -67.76267 | 2025-09-21 06:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9750ab45-5961-32f6-82a6-a61e004d7944 | -8.22659 | -71.02791 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f95ca48c-1b5f-39e1-a498-0a0299e2cdc5 | -9.73949 | -68.43623 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a91d9f16-08a9-34f9-921d-43ad652a303d | -8.49508 | -70.61737 | 2025-09-21 06:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 484d5475-41ca-3e90-a72a-d92a63a4c452 | -9.3985 | -68.29554 | 2025-09-21 06:18:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3b57bd9-6e90-386e-b70f-e44280b9135a | -10.66502 | -69.10419 | 2025-09-21 06:18:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ea9136-e4c2-3210-9276-fb220c1f9f13 | -10.25024 | -68.82578 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f992ad19-78e8-33bc-a92d-57a13b994517 | -8.49249 | -70.61546 | 2025-09-21 06:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db02e485-133d-3bfc-b722-e48177024864 | -9.96752 | -68.80145 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 577f9a17-8df6-3173-844f-7a72262d7755 | -8.66604 | -66.58897 | 2025-09-21 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a6e7566-2aa8-3a45-89dc-4186cda0e8ed | -8.53238 | -67.0807 | 2025-09-21 06:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48470bbc-1fad-33a9-8a32-b204eab37965 | -8.27021 | -70.83317 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 172fb3b2-2d77-3557-ab97-cb9feff03042 | -8.8649 | -67.10295 | 2025-09-21 06:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab7b73b0-cd7b-3736-a76e-8758390c9824 | -8.53753 | -67.07684 | 2025-09-21 06:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54db9db3-0e9d-3f93-8fff-8fdbc6e7249b | -10.28224 | -68.82698 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03b2f165-335c-3095-94e0-a092d0acdf2e | -9.41211 | -63.7036 | 2025-09-21 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7c03620-2343-3929-bf04-cb1cdca4ab8a | -8.03791 | -71.36916 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c3f5f6d-09d0-3bb0-bd76-cea40f52a703 | -10.25077 | -68.82211 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c15f8851-ba6f-3dce-85d0-64ed4e6c0427 | -10.19473 | -68.80257 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35b3bc78-0be3-3d6b-89cb-0dfe2d21edca | -8.03443 | -71.36861 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9dd341e-3703-334f-a22a-6ceb5d77a37e | -9.74314 | -68.44065 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 150a34f2-ee73-343e-a9d7-1f1b061f34cd | -9.40689 | -63.69875 | 2025-09-21 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26ef0a95-a2af-369b-b49d-1b2c5c06e486 | -9.41263 | -63.69959 | 2025-09-21 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b583c32-7a7b-3d6b-a0b4-49d3d31da1b1 | -10.09573 | -68.8341 | 2025-09-21 06:18:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7c927c4-83ff-3d4b-8ce6-3d9ddafb5c66 | -9.39429 | -68.29492 | 2025-09-21 06:18:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b311673d-bfda-3222-abf5-043c5993ca53 | -9.11914 | -66.01287 | 2025-09-21 06:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82ebe862-4ce2-3005-8e75-a355768b8dfc | -9.4189 | -63.69643 | 2025-09-21 06:18:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b2e9712-df1e-3205-aca5-3c3ed16d868c | -8.85041 | -71.35533 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dccde0f-6ec8-30b3-a9ae-6b978fd1f558 | -9.39375 | -68.29879 | 2025-09-21 06:18:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bf8a191-a00d-396e-ba51-199724d0a7ae | -7.97815 | -71.34028 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92b04c4a-b397-335e-9677-5ea095c70efa | -8.26664 | -70.83261 | 2025-09-21 06:18:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 88212d43-4ac0-35af-b3d1-ff645f8c96c7 | -8.71028 | -69.11349 | 2025-09-21 06:18:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README46.md)
