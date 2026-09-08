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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81bf5cd4-00bf-3934-929b-2c2891e9f823 | -13.43894 | -43.81618 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fac10d00-f33c-34d4-8f53-6b6e313126c5 | -13.22735 | -61.71375 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2265379d-2aa0-3d3d-aaed-917221018333 | -13.21829 | -61.71605 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8aa83341-d476-3203-b216-ef6d5f6d50c7 | -11.48466 | -51.12083 | 2026-09-08 05:06:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3951c4c3-d7de-3a86-ac63-6daa044ad138 | -13.26286 | -61.7084 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0d8751a3-9b52-3352-9067-9ab7216497cc | -13.2745 | -61.76332 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5526fd18-537c-3203-af93-f41bcb37ae16 | -13.43974 | -43.81765 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba1992b5-d5a7-3953-906d-851c672775bb | -13.27023 | -61.78697 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d81a11a9-0fa1-3adb-8921-7089273ceb3e | -15.22763 | -59.62576 | 2026-09-08 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bbf3295-6974-35d8-bc42-833c3cf3881b | -14.68749 | -55.16956 | 2026-09-08 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cf76ed2-ef43-353e-a943-be632c09d7ef | -16.00876 | -55.77551 | 2026-09-08 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92a720f4-a463-3ede-8095-5f8188820d7d | -13.22697 | -61.71168 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02ff1783-d36f-3b4e-9791-b5d5c7b1962a | -10.76854 | -60.78743 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffcaa0bc-c7ad-32d0-a674-5de5928e031a | -13.27726 | -61.77201 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 099ef3c2-52d9-35d2-a662-3b8bf21522b6 | -11.40731 | -62.12637 | 2026-09-08 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a303106-ad32-3960-a70e-5a2e228e6075 | -14.52698 | -59.79666 | 2026-09-08 05:06:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 706b645c-2b58-3f6f-8c59-73d365062c4c | -13.41516 | -54.6248 | 2026-09-08 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb110c7d-fa72-3e61-945e-a32beba7efc2 | -11.93456 | -49.74115 | 2026-09-08 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e19a678-688b-3e8b-b813-d53e3bc44b46 | -13.23152 | -61.71454 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 132668bd-2803-3eec-abba-7cc741f485ab | -13.25869 | -61.70762 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cbc0f8e6-836b-3da2-9891-e8333f0cfdfd | -10.76918 | -60.78372 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a79b4ade-a2f5-387a-be46-b74d81c79f07 | -14.69084 | -55.17009 | 2026-09-08 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be06e433-aac6-33f1-9052-5e087904c559 | -13.2221 | -61.71479 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5356f89-1155-3fdd-b74c-4b8a7b3a9e49 | -10.74868 | -60.70763 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f04cab0a-a201-3d3f-897b-843d5070d487 | -16.00486 | -55.77858 | 2026-09-08 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3abb7121-567b-38c7-9673-afb3f879abba | -13.27513 | -61.78383 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f32f2931-30b4-3863-818d-06430c13af31 | -13.2719 | -61.7061 | 2026-09-08 05:06:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2ce98336-34b5-373c-9b85-fafef63530c3 | -13.27584 | -61.77988 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9333d572-e1a2-355f-bf8b-c456c22a53ff | -13.41853 | -54.62532 | 2026-09-08 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a637f57-d8e2-394e-88ad-cfa15bddc01f | -10.78083 | -60.78968 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aff81fbc-76f6-347f-9393-35b39a90bc49 | -13.43334 | -43.81657 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c1040de-ba6e-308d-a0d0-c6395feaae52 | -15.83755 | -56.61011 | 2026-09-08 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5acf44cf-075c-3c00-b551-b23f70e7383a | -11.934 | -49.7452 | 2026-09-08 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa9f1167-6923-3e7f-939b-633700f7b3d8 | -13.27119 | -61.15295 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9545eca-8c6b-3c1d-8038-944fbe9e8e05 | -13.42749 | -43.81031 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31020b25-7d01-3796-8b03-352fd07f9d00 | -11.94309 | -49.74236 | 2026-09-08 05:06:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24437c1f-755e-398a-a960-12d3e5d9a47e | -13.43391 | -43.8112 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 12838723-d800-38f7-b1be-8f3dea7e16dd | -13.43254 | -43.81519 | 2026-09-08 05:06:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a0bde90b-a25f-3156-85bf-82da0c5a83a1 | -13.27055 | -61.15656 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 088aa162-9ec1-3a07-91b0-a5f3e7d3ea6f | -13.22246 | -61.71686 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d54f1467-db3a-3349-b945-eb1865bfe8bd | -10.77392 | -60.78075 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 045a9ae8-fbab-3fe9-97a7-f8e930123308 | -15.83424 | -56.60955 | 2026-09-08 05:06:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b601975d-17fd-3d46-9e30-3baa9c4e4163 | -14.69028 | -55.17374 | 2026-09-08 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00aae1c5-3191-3ad5-bb08-fdf9a93d5c7c | -11.40648 | -62.12405 | 2026-09-08 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19985252-44cc-39c8-9ec4-071aea8e6bc5 | -13.24547 | -61.70913 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1fb17a4e-e501-3964-b1f0-2854c77bf4a4 | -13.2228 | -61.71088 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 294d713f-2111-34c5-88f5-3c92c582f12b | -13.25452 | -61.70682 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a1dac995-43ac-3735-85c2-d8de3346cf02 | -13.22318 | -61.71295 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3deb9fd0-0a6f-3a14-bf75-893842a0a27b | -13.24892 | -61.71383 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905c557f-3dc1-3611-ad67-8bac4ad386ca | -13.4146 | -54.62845 | 2026-09-08 05:06:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf86213-d583-3954-8f81-74893417fdd5 | -16.0082 | -55.77913 | 2026-09-08 05:06:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1a55b3a8-059c-36be-b0aa-8628128bd61d | -10.76789 | -60.79119 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b37772f8-76e2-3783-893b-214fc8dc471d | -13.27797 | -61.76807 | 2026-09-08 05:06:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 41cbfde3-2734-332d-bcd4-da4889f44c1f | -11.40565 | -62.12856 | 2026-09-08 05:06:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69bc0f21-3435-31ce-b67b-660714ddda25 | -10.77673 | -60.78892 | 2026-09-08 05:06:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40655111-d7d2-349f-b0e6-c221f6a217cd | -20.49929 | -57.42727 | 2026-09-08 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 9024185c-7f98-3a7c-8063-58104c18190a | -17.09343 | -56.87325 | 2026-09-08 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 74d2aac1-a886-37e8-b7a5-f3b56a1cd198 | -22.58871 | -54.96051 | 2026-09-08 05:08:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| db9bbcd1-5826-36da-9436-1ec54ce8fc30 | -17.097 | -56.86992 | 2026-09-08 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 04a49cf4-2d4a-3211-bdcd-e3f2b4df6908 | -17.09643 | -56.87352 | 2026-09-08 05:08:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e83d1e77-a736-3a96-984f-0ea4930af7bd | -20.43387 | -57.4351 | 2026-09-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cf882afc-9b87-31c6-b024-295272d10c2e | -21.9833 | -56.05353 | 2026-09-08 05:08:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4b58b30-75a6-390d-80ee-7020ad709ae4 | -20.49207 | -57.42979 | 2026-09-08 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3750ff41-7699-349d-a400-89fd40e0a79a | -20.50217 | -57.40887 | 2026-09-08 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f8dac011-a4b1-3168-8279-7a2ba9333534 | -20.49597 | -57.42669 | 2026-09-08 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2d962548-507d-39b6-ab3d-aec3d52bb2de | -20.50044 | -57.4199 | 2026-09-08 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e09394bd-0c2d-38da-ae2c-67a4fdb917e4 | -21.97298 | -56.05196 | 2026-09-08 05:08:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b30e4cc9-7263-36a7-9e81-76adf6b45726 | -20.49986 | -57.42359 | 2026-09-08 05:08:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a87d2d02-78d1-35b9-b2ac-500d05e031b9 | -20.45825 | -57.43183 | 2026-09-08 05:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ad5a3165-4b0f-3f86-aebf-d4c9f3f9a9fd | 1.10255 | -60.51115 | 2026-09-08 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e569b30c-9af5-346b-adc8-c7ff1be5abf6 | 2.45935 | -60.77719 | 2026-09-08 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 61dbf313-eb93-3db9-a200-89ffe1d55f50 | 3.6044 | -60.46173 | 2026-09-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2087a705-f50e-3473-bde6-eed9efe9d4ab | 3.61285 | -60.46527 | 2026-09-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f84cc00-56f6-3292-8d4e-c7f0b99c20b4 | 3.61209 | -60.46048 | 2026-09-08 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4780b62-c0d8-35d5-9f6c-dd21eb9acdb2 | 3.11018 | -60.77076 | 2026-09-08 05:46:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b9082ef-7f47-3ac7-b4e7-f25b620520ed | -5.19099 | -59.76365 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cf7615f6-e1ad-3ca3-a08a-dcf43bed3f72 | -5.55249 | -60.2459 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 188448c8-e22e-3634-a7ae-ee44939dc9d9 | -5.18639 | -59.76294 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0c67981-49fb-3e84-8879-1d4187b8db32 | -3.06312 | -59.27469 | 2026-09-08 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 890b59d1-6627-3bbf-adff-b049c20e1552 | -1.19669 | -55.73067 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c128ee3-4280-31fe-a83c-6989cb7c3cc2 | -2.18402 | -60.22403 | 2026-09-08 05:48:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3236d262-919a-3c72-b89f-9294cd591481 | -3.70526 | -58.93515 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa80e264-cba2-3352-a2a5-147da6386e89 | -4.19212 | -59.95422 | 2026-09-08 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de7df159-8c5d-3788-8e9c-3fdf5b9141a4 | -5.28613 | -60.11868 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1a66155e-53d5-3836-8283-162906d841a9 | -3.37813 | -59.4299 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f910eb28-fda0-34a9-96b0-da432c819803 | -3.69973 | -58.93956 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 54fc88c6-0e5c-3806-9e0b-7bd9b23455e7 | -3.14834 | -60.65816 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| accd0de6-afb9-3c46-a02a-5f35a0b3873f | -3.45476 | -59.51507 | 2026-09-08 05:48:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d10f6c27-7a84-373f-af34-8c1d20aafe93 | -3.15313 | -60.65497 | 2026-09-08 05:48:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b2353254-530e-352b-8756-e33f521d0807 | -5.48342 | -60.20044 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ce4c816c-5bff-3a45-863f-63696d6be413 | -5.59586 | -60.24929 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7368dd95-d189-3a0a-89ad-d110013d8b17 | -4.19277 | -59.94976 | 2026-09-08 05:48:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd184d8d-4b0a-3579-a963-4153e0c93a09 | -1.20595 | -55.72002 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeb9a327-e0c7-3ed9-a6d8-a80d492c0c4a | -3.77699 | -58.84609 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a7fe09de-8c69-39ca-b42d-3287d801e376 | -1.195 | -55.71502 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 98022686-b688-3dd1-b82d-763c6cb8561f | -5.54801 | -60.24523 | 2026-09-08 05:48:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bd6f160-8939-3c8b-9c0c-8b5916cdbf4b | -1.1985 | -55.73087 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dba4bff-ba08-38bd-ab3f-02b893459cf0 | -3.70373 | -58.94544 | 2026-09-08 05:48:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48df1ca1-00b3-3830-94b4-a9cd923bc651 | -1.20247 | -55.74344 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 546860ac-c22c-39f8-a543-213dacecf5ea | -1.20059 | -55.7432 | 2026-09-08 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README24.md)
