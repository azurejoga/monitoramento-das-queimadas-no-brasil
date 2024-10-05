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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8624a233-5b13-3f6a-82b2-cc1679135d10 | -10.13037 | -56.76405 | 2024-10-05 05:31:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5ad1f026-07ea-3046-8278-372ad5a78536 | -10.10953 | -58.21897 | 2024-10-05 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5c54bf5-cbe4-3ce6-8e33-584626c0dd0a | -10.10947 | -58.22206 | 2024-10-05 05:31:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a232fd0-0f2d-388a-a76d-fd6fc6699361 | -14.9366 | -59.18532 | 2024-10-05 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6db1a3e0-0c12-3cc2-b6dc-315328e63066 | -15.38363 | -58.1398 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a540da4a-e992-32b9-83f4-5c4e85745f0b | -15.37989 | -58.13523 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16c9d182-fb3e-37ce-838e-5f330e69e42e | -15.34746 | -58.15095 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfbc1a89-6b49-3543-b008-27197476f03c | -15.34322 | -58.15017 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 027c4a02-c8a6-31fd-a0c4-844b5e42573e | -15.12895 | -59.02963 | 2024-10-05 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a23483f-afa5-3bf1-a3d4-a46a0aa92aec | -15.12847 | -59.03324 | 2024-10-05 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9d75de7-cf5b-334c-9293-2ccdfc1e3a0e | -16.54473 | -58.21674 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1c5f698b-6704-38da-b12d-705e711e10b3 | -16.54095 | -58.21191 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 777d47fc-a52a-3aa3-a541-1b981a876dd7 | -16.54041 | -58.21616 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b68e0f0-e76f-3e12-9abe-5bd8c4ae0bf4 | -16.53988 | -58.22039 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 87b0d12c-60e4-381e-b0ed-44498a5950ff | -16.5388 | -58.22889 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 99b47136-0be6-3ee3-a283-1f904b633683 | -16.53663 | -58.21132 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 713bb530-1763-32fc-b7a4-5fedb5fed0d0 | -16.53609 | -58.21557 | 2024-10-05 05:31:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e798d739-35d6-34ff-a7d8-1be987504117 | -15.38795 | -58.14002 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e4c52c2f-2d20-3508-aa77-5c89044726b9 | -15.37028 | -58.1423 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e3c6f47-117d-31d0-af17-d8e5157cd09f | -15.36604 | -58.14149 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 117ea337-0e92-3f20-874e-3233af071b9a | -15.27332 | -58.19204 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9064bfa2-63a3-320a-8e01-7a939b61951a | -15.26911 | -58.19118 | 2024-10-05 05:31:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d67f83dc-c73d-3520-924c-c4c554393683 | -9.89232 | -59.4961 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00fe0468-4464-3b4e-844a-75e07546a784 | -9.89169 | -59.50038 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a43903f6-c09c-35ec-bf7b-cdc7bfe092e3 | -9.88805 | -59.49983 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 99d477b0-9a3b-38f7-9080-36b3e5b58cfb | -9.88742 | -59.5041 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 751a6fe4-acd3-3bc1-a7f1-b6b225580f6c | -9.8844 | -59.49926 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b475d40b-b18e-3c59-a256-900871573929 | -9.88377 | -59.50354 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 929e527a-b374-3357-b9e3-0a42672e8f9a | -9.88076 | -59.49869 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9e5dcb2-d2dc-3ad1-b9ba-d0807170743e | -9.88013 | -59.50298 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23690925-bb29-355f-ad69-e23c6f0f0ef6 | -9.80617 | -58.97809 | 2024-10-05 05:31:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eef8893-8956-3ce1-9f03-4d23d32eabe6 | -9.80552 | -58.98268 | 2024-10-05 05:31:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 889ec114-942a-3d4e-980e-2386b4525445 | -9.80242 | -58.97754 | 2024-10-05 05:31:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f10e3449-d77d-395e-973f-5de33223e69a | -9.80176 | -58.98213 | 2024-10-05 05:31:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac47089-380f-3319-93e8-254285c11b43 | -9.80111 | -58.98672 | 2024-10-05 05:31:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 380850f5-bfbf-3776-bbdf-76b6941ab8b6 | -9.79736 | -58.98617 | 2024-10-05 05:31:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 157fff82-fa83-3c34-b9b5-3aaf54ddbeff | -10.11266 | -59.02613 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94e48de-f6f9-3d91-84d8-e308c8c64327 | -10.11215 | -59.02381 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a66fe3f2-28f8-3576-b226-eb27459592bc | -10.05248 | -59.34964 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c4dac9d-486a-3bb6-824b-72b9b1b96ff9 | -12.32518 | -59.21226 | 2024-10-05 05:31:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aea7eb8e-09b0-39cb-8db1-a7bcf2ba5536 | -11.77086 | -58.88839 | 2024-10-05 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94a6b694-522c-3112-a1d7-fe7c93c4084a | -11.76699 | -58.88781 | 2024-10-05 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f47b79ba-0783-39c0-83b9-23fc1e8ec063 | -11.67792 | -58.89173 | 2024-10-05 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea09bf4-56cb-3fb9-ab57-fe0f97c5c2bd | -11.67406 | -58.89113 | 2024-10-05 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a294ae11-c42e-3192-92fc-953ea6a696ac | -11.37659 | -59.19243 | 2024-10-05 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78c37169-41a7-33d6-a4f5-7e0c7db51934 | -11.37644 | -59.19514 | 2024-10-05 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c60a138a-4731-39d0-9a96-ba3f629263c2 | -15.17732 | -59.44501 | 2024-10-05 05:31:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6c0dbdf-7be2-358e-b268-264a78ec6e52 | -15.15467 | -59.52461 | 2024-10-05 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60729aa0-adcb-3da7-bb50-ae304ad15e27 | -14.78331 | -59.42757 | 2024-10-05 05:31:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0972ebe1-c0d5-3536-b7cc-bf9af5650335 | -14.78261 | -59.43261 | 2024-10-05 05:31:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f213909-9406-37f8-a8b1-f7d5152f684d | -15.49144 | -59.80861 | 2024-10-05 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 8b303a35-d21f-3751-b8c4-58dedd45324e | -15.48624 | -59.81787 | 2024-10-05 05:31:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92149971-a9c2-3d85-969d-4472332b7412 | -9.27585 | -60.83013 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e01c01f2-4a40-3dd9-a9b1-484501e6b8e3 | -9.27528 | -60.83387 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 800f5bf7-76c2-3227-8ef1-7c965efa8fa6 | -9.26885 | -60.48012 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bd4fa73-0eb1-3114-bdc7-cb4933514efd | -9.26828 | -60.48397 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98904c9e-1617-35dc-bc8a-baec2d46ad89 | -9.26788 | -60.79055 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61afadb5-db53-3ff2-9d0d-fd4da8b4f2a7 | -9.26731 | -60.79429 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5996a0c3-3d27-3f85-98c2-30586d67717b | -9.26598 | -60.49937 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a358c376-a7be-3097-b94a-93366a03f313 | -9.26541 | -60.5032 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6cf62d1-235d-3a92-a8a3-ebb9dee89d6a | -9.26539 | -60.4796 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8837f6c2-e263-33c9-a074-1ecc7ea2b56a | -9.26482 | -60.48346 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a16fd601-b934-3441-ad40-7e81dc357f57 | -9.26424 | -60.48732 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d19b6942-8d16-3c04-8a6f-7f8ac7dfe6fd | -9.26367 | -60.49117 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d870335-9648-3298-add9-004d5d117f77 | -9.25101 | -60.50493 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3edb1637-ae80-35d1-9846-87b5b71309e4 | -9.24755 | -60.50441 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc5072c9-3fe4-3692-b40b-b300b4cb34a6 | -9.24746 | -60.44228 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23c1e700-3dfe-3f9d-a285-6b46fd89f7f8 | -9.24688 | -60.44612 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32ee5c69-b5b2-37b5-ba79-fc89c4a187d1 | -9.24629 | -60.44125 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 183afe13-e443-3f57-bc49-d7540e528903 | -9.24572 | -60.44509 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6b164d2-70d0-33d4-af6c-0aecb352088a | -9.244 | -60.44175 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 876e3152-a2b2-3294-bbaa-c37fe7e03459 | -9.24341 | -60.44559 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91818a8e-22d8-39d8-b234-6b086e48189a | -9.17013 | -60.50894 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c5d6c3d-11e7-397f-be7d-ce9ba2825bf6 | -9.16956 | -60.51278 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7955b370-5b6f-3c80-82f6-d751858efce0 | -9.16668 | -60.50842 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e846b622-b877-35d3-b255-c5b78c1b635b | -9.16265 | -60.51172 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a8124a-7ce0-3602-b178-04b238db89f4 | -9.1592 | -60.5112 | 2024-10-05 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43290b75-a043-3600-a533-5608a8b84e84 | -10.38098 | -61.17477 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 808caaff-291b-3864-a6f7-3eb61e894463 | -10.37701 | -61.17797 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf6a79c7-1ba2-3185-8537-8df803c87ad8 | -10.37361 | -61.17744 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26aee3bc-6182-37fa-88b3-dac291d6b5b5 | -10.07515 | -61.10975 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d51e856-0dfa-3793-90c7-ef9ae529a49b | -10.07458 | -61.1135 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41f8b535-a148-38b7-9a11-913d322ce530 | -10.07175 | -61.10923 | 2024-10-05 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b608f3b-e926-3b87-9258-e5cb1ef291bc | -9.94947 | -60.11149 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9e9c90a-10fa-3622-a339-8fd25863ca66 | -9.94942 | -60.11269 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b0743d-1952-3666-a8b9-dbf8556b7053 | -9.94888 | -60.11554 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67d44d99-b088-3ba6-bd26-c21d5b8190f5 | -9.94832 | -60.09597 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| caa1679e-856d-3212-b9df-6fe7021b3b4b | -9.94828 | -60.09474 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3f25d8a5-5f0b-3a11-af04-d679e7d8e83c | -9.94771 | -60.10002 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd437e2a-e5ca-30cd-8ba3-c408c5a9b6b7 | -9.94769 | -60.0988 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c3fca8-109b-35db-a689-4538458384e9 | -9.94588 | -60.11215 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83d4b604-ed9e-314c-88fa-92d8b0c47bbd | -9.94478 | -60.09542 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dac0c660-86d0-3105-9c92-b13a9e601a7d | -9.92877 | -59.93477 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14b17d26-c3b0-3de2-b1c5-8935c5721487 | -9.92588 | -59.90491 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 038dae17-4b4b-304b-aee3-6b7a950f9fa8 | -9.79798 | -60.47849 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34dfd6f4-99cd-3254-a832-8fc527b668ec | -9.7974 | -60.48236 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ef1c20a-0148-3188-a8ee-6a79413e0424 | -9.7791 | -59.81606 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1adf920a-cfe7-3de3-8f46-219216248686 | -9.49223 | -60.36663 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd361c4f-8b95-3802-8f3b-b7d9c60dec18 | -9.48932 | -60.3622 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02647f35-2b10-3f40-b543-0859185a6f2e | -9.48528 | -60.38949 | 2024-10-05 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README145.md)
