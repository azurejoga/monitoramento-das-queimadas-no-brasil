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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 941b84bc-d976-3708-b055-2ad17ccd8dc0 | 2.54342 | -60.36113 | 2026-01-05 06:01:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 13632ba1-ee95-37aa-9161-9cedd262d8ee | 2.78558 | -60.30645 | 2026-01-05 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d9e746d-3f77-30ef-ad96-ac8eaecfe6a3 | 2.94811 | -60.2835 | 2026-01-05 06:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64440ff9-e644-310b-b438-969278221330 | -2.44388 | -47.7771 | 2026-01-05 06:12:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 09a97ff3-1b12-3989-bb00-8b27fac056f4 | -2.44253 | -47.78601 | 2026-01-05 06:12:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 59223012-47b4-39f7-9562-9a37e21ea9c5 | -2.45273 | -47.77839 | 2026-01-05 06:12:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 293ff621-39ba-3b38-b66d-b886b270a3f8 | -4.2626 | -48.83432 | 2026-01-05 06:14:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a67e6846-1717-3b39-aeb7-f44e95c2b53e | -1.32428 | -49.41533 | 2026-01-05 12:33:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| f767719e-c775-3f49-9b23-9e7af634111c | -3.40587 | -49.53027 | 2026-01-05 12:33:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 812ec181-3605-36ed-a678-b2dab5492d15 | -1.33572 | -49.40562 | 2026-01-05 12:33:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b09fc205-7658-33ed-965b-b35c2439d5e3 | -3.26507 | -49.14804 | 2026-01-05 12:33:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d7ed3a9b-3db8-3ba0-93c5-b938d897b544 | -1.32587 | -49.40429 | 2026-01-05 12:33:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 1b178d87-9b85-3f9b-9d9e-0f0b8558f2e1 | -16.18821 | -55.44991 | 2026-01-05 12:38:00 | TERRA_M-T | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7934a662-35c2-3fad-b97c-39c3c9fa6bd3 | -18.86595 | -53.6389 | 2026-01-05 12:40:00 | TERRA_M-T | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 304c0902-ed90-31c8-b265-1fb8515dbedf | -18.64624 | -53.28778 | 2026-01-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1a74f858-f547-3802-a54b-5aadeb1ae9d2 | -22.23438 | -50.8891 | 2026-01-05 12:40:00 | TERRA_M-T | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| a9d299c2-e91f-3d24-9ee3-1e8448fa2a17 | -19.52355 | -53.21384 | 2026-01-05 12:40:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 942f77b4-08bd-3a43-9b3e-2ab47c025ccc | -20.24721 | -50.62986 | 2026-01-05 12:40:00 | TERRA_M-T | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| d9e10ffa-045c-3e55-a332-6468d711a978 | -22.44295 | -53.31178 | 2026-01-05 12:40:00 | TERRA_M-T | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c02d5c05-4eef-3668-95de-ad8bb5fecfb0 | -24.28188 | -53.83381 | 2026-01-05 12:40:00 | TERRA_M-T | PALOTINA | PARANÁ | Brasil | 4117909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 2f4ce287-9461-3a13-b28f-9ece5192aa8b | -26.35478 | -52.8417 | 2026-01-05 12:40:00 | TERRA_M-T | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 200ab1e1-5d5b-3c46-8c78-2071345f1369 | -20.4938 | -55.277 | 2026-01-05 12:40:00 | TERRA_M-T | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| aa9e414c-88c6-34e2-a002-3aae5384ec7e | -28.46789 | -50.89382 | 2026-01-05 12:40:00 | TERRA_M-T | VACARIA | RIO GRANDE DO SUL | Brasil | 4322509 | 43 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| a55fadaf-bbf7-30d4-bab8-4683899f0383 | -25.93036 | -53.47157 | 2026-01-05 12:40:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| c344a6e3-f30a-31c6-9129-15ac0aedd724 | -24.80178 | -53.29106 | 2026-01-05 12:40:00 | TERRA_M-T | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 6b727200-1294-3a8d-84e0-1e4bed94700b | -20.97544 | -49.59507 | 2026-01-05 12:40:00 | TERRA_M-T | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| eadaa2d6-199b-38d0-a9ed-b81683805a0f | -19.20564 | -55.00897 | 2026-01-05 12:40:00 | TERRA_M-T | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| da19acd3-69aa-342f-9d18-9f4eaa6504e7 | -27.31412 | -51.46669 | 2026-01-05 12:40:00 | TERRA_M-T | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 70e41b50-2080-3a11-bdc8-12d8bc2d472a | -24.51563 | -53.57656 | 2026-01-05 12:40:00 | TERRA_M-T | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| cc44be50-f2f7-3c66-8674-2c75504bde21 | -27.45104 | -53.93849 | 2026-01-05 12:40:00 | TERRA_M-T | TRÊS PASSOS | RIO GRANDE DO SUL | Brasil | 4321907 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 17b14afd-c32a-3b6c-8055-86b6e210e21e | -27.88729 | -52.22707 | 2026-01-05 12:40:00 | TERRA_M-T | GETÚLIO VARGAS | RIO GRANDE DO SUL | Brasil | 4308904 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| b47f2890-74c1-34ee-8f29-2ef79ab93e94 | -20.38918 | -53.13225 | 2026-01-05 12:40:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cc2d19ab-e526-3b9c-8ad4-e22cde04f4f5 | -28.85353 | -51.88982 | 2026-01-05 12:40:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 2c09927b-cf51-34ca-990d-e48fdec2db73 | -27.35634 | -53.38791 | 2026-01-05 12:40:00 | TERRA_M-T | FREDERICO WESTPHALEN | RIO GRANDE DO SUL | Brasil | 4308508 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3a66489a-f611-3e66-b100-7df4e1c34d54 | -25.57669 | -54.57241 | 2026-01-05 12:40:00 | TERRA_M-T | FOZ DO IGUAÇU | PARANÁ | Brasil | 4108304 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 45a392c9-7e35-3f7b-ba63-c90ff7bc5c5e | -18.34102 | -52.40644 | 2026-01-05 12:40:00 | TERRA_M-T | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 26f6da55-8696-38ac-ade5-0ca91902e2c6 | -25.79353 | -53.30164 | 2026-01-05 12:40:00 | TERRA_M-T | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 0bd0e4f3-da48-3882-90b6-5f145ce63d4e | -18.61807 | -52.79735 | 2026-01-05 12:40:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 331ac23d-830e-3abf-abc4-781392b50110 | -20.96506 | -49.58748 | 2026-01-05 12:40:00 | TERRA_M-T | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.0 |
| 43bf2f3c-1136-3aeb-9b6c-5eaa1830ca47 | -28.9387 | -51.5476 | 2026-01-05 12:40:00 | TERRA_M-T | VERANÓPOLIS | RIO GRANDE DO SUL | Brasil | 4322806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| db5f92b0-8af1-32ef-a812-401bbaf51754 | -28.85632 | -51.89603 | 2026-01-05 12:40:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| f4429cc1-3a11-3ce6-aa46-4dfece2157f6 | -29.44908 | -54.07298 | 2026-01-05 12:42:00 | TERRA_M-T | SÃO MARTINHO DA SERRA | RIO GRANDE DO SUL | Brasil | 4319125 | 43 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e1ae32de-6611-3de2-9f2b-3617579b86dd | -29.19042 | -54.86628 | 2026-01-05 12:42:00 | TERRA_M-T | SANTIAGO | RIO GRANDE DO SUL | Brasil | 4317400 | 43 | 33 | nan | nan | nan | Pampa | 6.6 |
| ee8d0296-1013-3d26-ac89-818c00727171 | -29.03594 | -51.18413 | 2026-01-05 12:42:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 8393ad7b-684d-35eb-9aee-01e49dc37360 | -29.64705 | -53.25009 | 2026-01-05 12:42:00 | TERRA_M-T | AGUDO | RIO GRANDE DO SUL | Brasil | 4300109 | 43 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |


