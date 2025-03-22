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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b0b3ba2-2f0d-3b6e-91a9-e56793f2d586 | -20.47584 | -53.67585 | 2025-03-22 05:08:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc7072a1-9a4a-3724-9599-006d2c4ea8db | -20.35156 | -55.83027 | 2025-03-22 05:08:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e8a4e74a-3e44-3ad5-b604-40115b812713 | -21.23576 | -56.46617 | 2025-03-22 05:08:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbacf6b8-ae62-3dc8-9e66-5bd58cdb7027 | -22.68744 | -54.63378 | 2025-03-22 05:08:00 | NPP-375D | JUTI | MATO GROSSO DO SUL | Brasil | 5005152 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e09e3942-ac18-3514-bea9-28553425a777 | -20.21808 | -46.68462 | 2025-03-22 05:08:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 242efc0d-f105-319f-af81-8e1ad001c64b | -29.51907 | -50.6765 | 2025-03-22 05:10:00 | NPP-375D | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 49cfd412-cc41-37fc-838d-e2b7e224d63e | -25.19297 | -49.32689 | 2025-03-22 05:10:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cbb05bba-ad0f-381c-aea8-a9bbae1d90d7 | -29.51944 | -50.67128 | 2025-03-22 05:10:00 | NPP-375D | TAQUARA | RIO GRANDE DO SUL | Brasil | 4321204 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 81b1d8c0-304c-3f43-8d10-7ed02ddf612f | -28.86632 | -50.87426 | 2025-03-22 05:10:00 | NPP-375D | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e28b89a4-c186-30ed-9213-081a7bf10a89 | -27.7407 | -50.42155 | 2025-03-22 05:10:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 71a938c6-1dbe-359e-9c87-647fd0632e7e | -26.52627 | -52.91092 | 2025-03-22 05:10:00 | NPP-375D | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ebca44c8-d4dc-3144-b9c0-5161dc74a3ad | -25.19902 | -49.32306 | 2025-03-22 05:10:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cecce0ea-99a9-35c9-a55f-60bfa419bca5 | -27.73523 | -50.42116 | 2025-03-22 05:10:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b8838c7e-e75c-3344-8be6-350426212747 | -28.93754 | -51.40122 | 2025-03-22 05:10:00 | NPP-375D | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 12b79af0-f0ec-3261-87d8-353bc9b56e55 | -28.93726 | -51.40465 | 2025-03-22 05:10:00 | NPP-375D | NOVA ROMA DO SUL | RIO GRANDE DO SUL | Brasil | 4313359 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f4a6d9cd-f67d-3e9f-b619-23b03351b250 | -28.62511 | -50.16309 | 2025-03-22 05:10:00 | NPP-375D | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fbea3fc4-8da4-3275-abb3-c8ef731e835c | 2.86079 | -60.17981 | 2025-03-22 05:23:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4648b4d7-b395-3194-9358-fcbeda53b130 | 4.89511 | -60.3023 | 2025-03-22 05:23:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9ce96f4-781f-3231-999e-3659f18960a2 | 3.78675 | -61.73427 | 2025-03-22 05:23:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cd4b495-89a5-3da4-863a-3949afedfcf0 | 3.36256 | -60.64942 | 2025-03-22 05:23:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 84ef0e75-e566-30ed-8b0a-bde85a2a772c | 3.07548 | -61.24474 | 2025-03-22 05:23:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 127f9105-2eba-3f9e-8889-1a2d960a6542 | 3.07883 | -61.24422 | 2025-03-22 05:23:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 836e8bf8-838f-3bbb-b16c-efc814105231 | 2.53044 | -61.63342 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 581f18a2-a7d3-3861-ab31-68e6f93a3acd | 0.8754 | -59.70295 | 2025-03-22 05:25:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ac6105d-54e2-3df4-8d55-4d035749dca3 | 2.64686 | -61.41643 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aeb5d5c-db1d-3f01-9532-47057acf0bfc | 2.31722 | -61.24166 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b645976d-c112-3ca2-9360-1e9364d0511a | 2.5222 | -60.99061 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec8d99ab-4e57-3455-8d28-4f8c3596c8f8 | 2.53382 | -61.6329 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 19949ddd-a8a5-3df7-83ff-dc036f819201 | 2.51887 | -60.99113 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e66e34-d68e-3f1d-96b9-d98ae35055bc | 1.95204 | -60.36811 | 2025-03-22 05:25:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d138a2f-d21a-3886-8d0a-33d5a5157e75 | 2.46027 | -61.31419 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33bdf326-3ffa-3549-8474-12b8e1e241fb | 2.52988 | -61.6298 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e53d45e2-f3ba-3400-aba8-a0e988c3844c | -5.12162 | -56.11506 | 2025-03-22 05:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe944756-6cc1-3e3f-af7b-d559f82d566f | 2.53833 | -61.63961 | 2025-03-22 05:25:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f814cf8-725c-30f7-bb39-4568b17faaa4 | -9.92463 | -59.93779 | 2025-03-22 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a218b473-aa4b-36db-8e90-ce75b978eeec | -9.92523 | -59.93913 | 2025-03-22 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9d0373b0-8509-35ce-99c9-54c2d484c5cf | -11.66432 | -58.26248 | 2025-03-22 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a8b6443-0414-341b-9f71-43320e1c2ae5 | -12.55936 | -57.76178 | 2025-03-22 05:27:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d351ea57-8a2b-3f45-be4d-f7cb4a6b6b47 | -12.26538 | -63.80901 | 2025-03-22 05:27:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a161e946-2aca-32e5-99ef-cb1f4d96f9ce | -15.37136 | -60.08981 | 2025-03-22 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 611ca9f2-0730-36b3-923d-47ca60201d09 | -15.28112 | -60.23497 | 2025-03-22 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa561e73-f6c1-3822-aceb-2642a381fb4c | -19.44079 | -54.78615 | 2025-03-22 05:29:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8dff598-d245-3f3d-b2db-3ee0b1623df7 | -15.59855 | -57.3324 | 2025-03-22 05:29:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d74fdfbe-508b-33b8-96fc-175545bca348 | -19.43556 | -54.78194 | 2025-03-22 05:29:00 | NOAA-20 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65b2adb8-c895-300f-8189-fddfa5054910 | -15.37512 | -60.09034 | 2025-03-22 05:29:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f669378-fa13-329e-a362-92987ccd1bfd | -20.35218 | -55.82813 | 2025-03-22 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b4bec28f-00c4-3371-93a0-659aae417aeb | -22.72951 | -55.57829 | 2025-03-22 05:31:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8e0a3141-14b8-31ce-bb58-5fdb8b20486e | -21.96998 | -57.59198 | 2025-03-22 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97f43f21-b2bb-3286-992a-ed72d1f0de43 | -20.35183 | -55.83157 | 2025-03-22 05:31:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f48c3b50-bf79-3b7e-b53c-0ff7bf4a56c1 | -21.18199 | -53.0811 | 2025-03-22 05:31:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f5ab593-06da-3ef4-bc38-35a16f415305 | -21.23893 | -56.46494 | 2025-03-22 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf1cc283-2723-3676-b8cd-29ee73ce12c9 | -21.96024 | -57.58651 | 2025-03-22 05:31:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67322c07-fcd3-3759-af34-814ebe78f091 | -21.2338 | -56.4643 | 2025-03-22 05:31:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c427cb41-f3b8-3760-b194-f6f763e10a54 | -22.724 | -55.57757 | 2025-03-22 05:31:00 | NOAA-20 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7c1e3481-a971-31ef-a2d7-d2ccc78f97de | -21.18155 | -53.08638 | 2025-03-22 05:31:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f71f25e4-e887-37e0-8281-b0cfb143e332 | 2.51911 | -60.99372 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c6ab772-8843-3e78-84e6-3ba16958c056 | 2.5279 | -61.63596 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 318e0e30-c641-3d7a-b45e-4bd8d7eb265d | 2.52712 | -61.6314 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e490d433-a8d8-3bbc-bb2d-83ceb9faf4c4 | 2.53319 | -61.63027 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0231cc6a-7b27-3e02-a967-f34b51489a8c | 2.53242 | -61.6308 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b06931a9-4105-3371-8e0c-2336c9a8287c | 2.53391 | -61.63998 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32cf1c85-905e-361b-86fe-48bde24ff9e1 | 2.53475 | -61.63944 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2e10a8a1-d2e9-33d7-a552-38ecb5406681 | 2.52635 | -61.63193 | 2025-03-22 06:18:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bce3ce1-4d7a-30dc-be3a-9dfc8ed61288 | -9.92055 | -59.93555 | 2025-03-22 06:22:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f48428cc-9b90-3ceb-aff3-8fca71be4bdb | -21.8881 | -53.4623 | 2025-03-22 13:40:00 | GOES-16 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 113.5 |


