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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2db59b72-819a-3ef0-b057-41567eed7497 | -18.9431 | -54.53909 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6e8b819e-3cba-3fac-9a03-4e3af1a59c6a | -18.94254 | -54.54214 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de12acdd-2e4d-3e19-9ea2-ee9a85d7ec5a | -18.93994 | -54.53384 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be741d7f-29e7-3c37-88b5-e173405123de | -18.93931 | -54.53859 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d7b5a98-f794-30c1-9675-473f35d275d4 | -18.93615 | -54.53332 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0f31d44-e06b-37ef-8a14-b53bc05c6758 | -18.93562 | -54.53637 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70f73a73-2ab5-3d6d-9342-65184dc622c2 | -18.93553 | -54.5381 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23421677-d2c7-304b-bb5b-79809fd5bd5d | -18.93184 | -54.53588 | 2024-10-17 05:08:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da4d2e1a-1945-31ae-bf39-a40b775fc223 | -20.58947 | -55.52934 | 2024-10-17 05:08:00 | NOAA-21 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc00f19-41d9-3e55-85f6-9f6bf238e6a8 | -17.63515 | -56.23207 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 380a2779-e950-3560-84b9-1130c989bc0f | -14.98784 | -55.30503 | 2024-10-17 05:08:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3165edf9-c608-3b87-8a7c-8a17c6efc975 | -17.71363 | -56.32066 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 687cfcc1-9938-3130-89d8-387bed1d13d2 | -17.65235 | -56.23483 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 81463e80-ade3-3df6-abc4-e85498d6fdb7 | -17.65178 | -56.23875 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| da0e1d1a-b9d8-3a75-bb4d-6ddcdd25a714 | -17.65122 | -56.24267 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8e921c20-92d9-3aee-b760-6c48fda89020 | -17.64891 | -56.23428 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f3def3dd-1ff0-3c08-b991-6f1e318cdc14 | -17.64604 | -56.2298 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 33568db7-1645-3635-b65a-26bbafb2f19f | -17.64547 | -56.23373 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 182aace3-eb24-3234-8d94-cc5ec3672155 | -17.64434 | -56.24157 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5c98dc69-476e-3e87-a76c-76eaf8dfdadb | -17.64377 | -56.24549 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a937ebd6-a128-309a-97d9-c4cb1da72305 | -17.64146 | -56.2371 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 45f9886b-4299-360e-acc3-4515182632ed | -17.6409 | -56.24102 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| de6e16ed-25bd-3bdd-b407-8f9be3520b12 | -17.6392 | -56.25278 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3784b41e-17b7-3fb5-a7b7-33535c85be7c | -17.63633 | -56.24831 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5a56dee7-2cae-3f2c-aba3-84a6bf6021e7 | -17.63345 | -56.24385 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 381245a6-1b8b-3b73-be2c-a64b79137a88 | -17.62827 | -56.23097 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e0093f9f-bf8b-39fe-b84b-cdfd45e8e0dd | -17.15079 | -56.12314 | 2024-10-17 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4d35c012-c45c-32ed-9156-a6e4876ad4d7 | -17.15019 | -56.4589 | 2024-10-17 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 709845a3-764c-388b-b9cf-c86960b22f44 | -17.14963 | -56.46272 | 2024-10-17 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a6eea02b-a877-3fc2-b37e-5fcdac6df8cb | -17.06163 | -55.98981 | 2024-10-17 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 972c7088-3c76-3dd4-a68b-c8fe1f1fd80a | -17.06106 | -55.99376 | 2024-10-17 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e39cdced-5ff6-3ec3-8166-7f4888307f4b | -17.05818 | -55.98927 | 2024-10-17 05:08:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| c146aade-dba6-3758-954f-7645e3f33364 | -17.21494 | -56.68214 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 388cdd04-bc89-3450-820b-350ed5f2efe5 | -17.20818 | -56.68105 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6c012d20-f67a-30ab-9852-aa4576195dec | -17.20479 | -56.6805 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2a5bd394-7e2f-399d-8883-8a29a06ad3ce | -17.20197 | -56.67618 | 2024-10-17 05:08:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c3642866-6c26-3369-8db2-7ad0d3f05236 | -17.88017 | -56.85606 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1d5102c1-4d09-3f3a-be14-b36553926f40 | -17.87961 | -56.85984 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 48d59815-76c8-3c3f-bb8b-254e950718d9 | -17.87905 | -56.86362 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c0e459c7-2295-3296-8f35-a0f8248150e7 | -17.87849 | -56.86739 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6e578c3d-4bc0-3421-a841-07b3bfc29698 | -17.87679 | -56.8555 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 6f449c56-9994-3ff7-bfe2-b9fc4fd8879d | -17.87511 | -56.86684 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1cdc7748-4027-3dfb-91ab-106d08fd372e | -17.87393 | -56.82792 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dd9eb37c-3ae9-385c-9a6e-3985becad86a | -17.87337 | -56.8317 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ff0eafd8-8600-333b-8be8-631119cb078c | -17.87282 | -56.83549 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e1d137f5-b5a1-33f0-b26d-e6f8d8008701 | -17.87118 | -56.87007 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cb6ece4b-7d0f-3830-ba1c-698df41ce99d | -17.87062 | -56.87384 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 68776037-c51d-33bb-add0-62f170b95369 | -17.87055 | -56.82737 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8603870c-331e-3ed5-8aac-e3f829d16fb1 | -17.86999 | -56.83115 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c65c3736-022c-3559-a717-d127d3c702f0 | -17.86944 | -56.83494 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c85f7cd7-48e8-39aa-9c88-5b5a5ba38afa | -17.86832 | -56.84251 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| bd2bf41a-4d82-32c1-9865-df8e1fb30469 | -17.86724 | -56.87329 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6f9ac7b8-91df-3c78-803f-8123aa2c4a47 | -17.86661 | -56.8306 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0bc67ba4-c3c0-39e7-9326-609a5c3bcdf5 | -17.86605 | -56.83439 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0ebd31be-4582-34b8-bc2e-64b6b7e06c3e | -17.8655 | -56.83817 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 85dc1282-822b-396d-9741-68ec94de1158 | -17.86438 | -56.84574 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dc441b3e-8618-3a84-8c9a-919fe2979a81 | -17.86386 | -56.87275 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 20017ca4-c0a8-32da-b475-96ff0b9a597f | -17.86383 | -56.84952 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| dd973cc8-5e0c-3c7e-a445-f4ccd1f16939 | -17.86212 | -56.83762 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f065ae66-f623-3ad6-a42f-2ec33d1e8614 | -17.85873 | -56.83707 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 966ded1f-7eb9-3479-a3d3-ff361ca84f1b | -17.85818 | -56.84086 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7377d6aa-977b-3121-9dc9-42e63bb82b12 | -17.85741 | -56.83707 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b97067b4-b4fb-35f4-9c6d-485c53c37f30 | -17.85684 | -56.84084 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 37ce29d3-be0a-31b1-8e5c-8c88a7497d47 | -17.85403 | -56.83651 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 70187863-7c19-3bea-9a61-f73df2f860d2 | -17.84838 | -56.85108 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ee42ea39-f0c5-3821-9a71-f0c6874d50e5 | -17.84781 | -56.85486 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5279bbda-f508-3918-8c85-bd3c38b90fe0 | -18.22659 | -56.85626 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7fdc56ea-ff6b-3ac3-af3d-0c7bfc779442 | -18.22321 | -56.85571 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| e3a0e69e-8b5d-3731-adcf-15aad4cd7e60 | -18.21926 | -56.85896 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 2bdf2e2f-9840-3f7d-ac77-cac3fc6a78a6 | -18.2187 | -56.86276 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 99cd50de-527c-307d-a9d2-4c7e65301eba | -18.16183 | -56.84197 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 90c21d47-fef1-3e2c-9741-ce5d91ba29df | -18.26667 | -56.60738 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 76fa5922-898b-3f8c-aecd-59156f13383f | -18.26611 | -56.61125 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 03d21a7c-f844-3761-ae97-733389e80eea | -18.2627 | -56.6107 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 0a4beaa9-1b0f-359b-86ff-9672ac5dfcc9 | -18.26098 | -56.59854 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9fbe949e-032c-36e5-8428-74c8921c04ba | -18.26041 | -56.60241 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ff2ac2c4-f2e4-370d-a8f7-0ca284209c22 | -18.25926 | -56.58636 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5f858795-f3cb-309e-80a0-344f700be895 | -18.25756 | -56.59799 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 99576b2e-d9db-3801-bbbf-96476ccfd6fa | -18.257 | -56.60186 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| e9596885-8954-3ee0-9a85-95b3dbb5b474 | -18.25643 | -56.60572 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| bb363292-4847-398b-b113-9bc364d9e8f3 | -18.25587 | -56.6096 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8b3e8627-ceaf-3e66-9c3a-2b10031ea9f8 | -18.25415 | -56.59743 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 363af451-d4b9-365d-bfa0-2b7b3fb46c01 | -18.25302 | -56.60518 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| f439df2f-cbff-3177-817f-7930d428acf6 | -18.25245 | -56.60904 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1f635fb8-689e-3828-91a6-93142eb147ac | -18.25073 | -56.59688 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d81b01ce-3d4a-3296-a250-75820e9f60a4 | -18.25017 | -56.60075 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| beab99aa-4131-3489-bec3-2c6cf43c98b8 | -18.24961 | -56.60462 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9aaaa94b-d356-33e8-af2d-cd13f76e49d8 | -18.24904 | -56.60849 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3fa9b322-845b-31ee-a49d-955da680557f | -18.24848 | -56.61236 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 636fd427-07a5-336d-ac27-166d2ef09220 | -18.24791 | -56.61623 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 52228d65-3083-396f-829f-3f07b6d281aa | -18.24676 | -56.6002 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bf9bce14-6aba-3666-b7a7-08f9af1dd4ef | -18.24619 | -56.60407 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3849f53d-6ce0-361a-a6f6-e02a825d8c36 | -18.24468 | -56.37672 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3cd10a07-a4b6-3639-b7fd-c1a048aca1ac | -18.2445 | -56.61567 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| ad5da851-2592-3ad7-b314-2bfbc761b577 | -18.24334 | -56.59965 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 87aee447-872f-3e5b-a3f9-0132e629e086 | -18.24124 | -56.37616 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| df958b0c-4c68-3d7a-b21c-75bd0a545722 | -18.24013 | -56.3357 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9ab0e8d8-bced-35f2-99de-0ff42d3a5e2b | -18.23726 | -56.3312 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 1d0a42d9-d73c-39ad-901e-6fb5dd34bcd8 | -18.22693 | -56.32956 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 785e0c5e-c06e-32f0-9ce3-fcd98aca1f0f | -18.22635 | -56.3335 | 2024-10-17 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README47.md)
