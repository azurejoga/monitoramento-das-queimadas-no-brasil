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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e3f417d-6d43-38ba-8805-ee48741e68bd | -11.86439 | -51.48122 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fe5bac8e-81a5-36ef-9504-44cf978eaa84 | -7.69922 | -50.26253 | 2025-09-03 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 344e8454-33f3-3ace-be56-f68e741dd3f4 | -11.61539 | -52.14622 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 39.9 |
| ac705c6e-4457-31aa-b2fb-f10fffb50a9c | -10.54101 | -50.41397 | 2025-09-03 00:50:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b8bde96d-75f1-3de4-8986-9f4aa82e6144 | -8.34336 | -52.53854 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bc532c66-395e-3c1e-8ef4-d256fc611327 | -11.8519 | -51.53492 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5252551d-aa58-30ad-9fba-1e4edda8412f | -12.84764 | -48.0149 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7574091e-02df-3972-87b0-318fe44c159c | -14.98386 | -50.21464 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 946f4b22-6a62-3916-b60c-e7e7d2e43518 | -16.84897 | -52.11663 | 2025-09-03 00:50:00 | TERRA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3da99d0b-dca2-32ed-a905-359882af7a26 | -7.7051 | -48.76267 | 2025-09-03 00:50:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 72.4 |
| c90d3ad9-e34b-3c87-af6f-3c11affd7979 | -14.78674 | -48.15271 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 1d5d50a6-ce27-39fe-8750-c6347ea118f5 | -8.0157 | -50.10386 | 2025-09-03 00:50:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2bb9e025-e2c2-3c43-b5a7-cc9793fa8856 | -10.91888 | -50.86267 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 20d01090-de08-3aa8-8154-a6433a6e3ac7 | -14.97359 | -50.20667 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5f6de678-c3e9-3bba-8f2f-2eee09dd8c81 | -12.48958 | -47.49292 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 9df9dc98-ffdd-301b-92af-0bfefa096469 | -7.71185 | -48.73569 | 2025-09-03 00:50:00 | TERRA_M-M | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4b018314-0727-3d49-871d-5b6b509c7615 | -12.87186 | -48.03615 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| b1913591-7743-31f2-9735-aa2db3f6ab86 | -12.93745 | -56.98293 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 64063f2e-e890-37d3-b4d1-27981a2309db | -13.09313 | -57.12478 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 24b12b6a-7034-3a8b-b576-945313fcdf04 | -16.30737 | -52.97028 | 2025-09-03 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 74847bb7-a45a-3f67-82ac-273e551fd896 | -8.01259 | -50.08242 | 2025-09-03 00:50:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1ae41536-bc38-30ec-b66a-8b89cdbd1b57 | -14.97226 | -50.19732 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 68048757-353d-3b2d-841c-e412aa3b5291 | -10.48558 | -53.65565 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bc9b0f7b-8e25-3db4-a23c-acef14c1bd32 | -7.52976 | -47.45242 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d521ef83-5fef-31c5-a8a4-8bdcd52fc9da | -14.57559 | -48.05213 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| c66971f9-e65a-3ed7-b78d-20154cd60379 | -10.9202 | -50.87198 | 2025-09-03 00:50:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f8787cf8-fc8e-396c-bc35-91e4e6c720e3 | -12.75554 | -47.66886 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b861fec5-7856-31be-a528-96eb8e4c44e1 | -7.47742 | -44.84693 | 2025-09-03 00:50:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 52b01420-3518-375e-b6bb-d7f12b9fb5eb | -7.71229 | -50.2541 | 2025-09-03 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a19a3588-0204-3bc8-8955-0627673822d6 | -12.50027 | -47.49117 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d9307ba0-990b-36e2-bb5e-32b593f4654f | -12.92017 | -56.93572 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d5ae0b2f-7383-312b-b06d-f0e13557743f | -11.61555 | -52.08222 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7d0b66ea-2d8f-3df4-87d0-7aa0529a46df | -8.37202 | -48.29653 | 2025-09-03 00:50:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 43.1 |
| a52feb15-6dfa-32e8-9d63-3238caf90ccb | -12.84488 | -48.06472 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 73377b75-b13f-3f9c-a28c-2c464836adea | -8.86129 | -52.02803 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 28dca46a-d62c-375f-9e1d-171af284c249 | -9.74802 | -49.40778 | 2025-09-03 00:50:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 05d830a3-9a10-301f-b893-c8f1798b4a44 | -11.80013 | -51.5517 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4009bdef-aa1a-3b35-a175-6e3c1d1ab2e2 | -13.30169 | -46.93713 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9988e25e-acf9-3c57-b67f-e24c99c7e5b1 | -11.63072 | -52.06173 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 13ba13e7-5244-3960-945f-02af118be337 | -14.35672 | -52.81243 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8eea017f-9fe8-3120-892f-640251c8521c | -15.5897 | -52.6756 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6909803f-cc08-3467-a3cc-6f50fa117be6 | -11.59279 | -52.11295 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 989.3 |
| 8fd2a52a-c32a-329b-bdc3-77d00eb6ac1c | -14.56211 | -53.04746 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 41f38197-ffcb-3e61-9b9d-2efb9f60472b | -14.78848 | -48.16394 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fa2493c9-0800-30f3-838b-47db6145d7ff | -15.55532 | -48.41064 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 29.0 |
| aeb3aefd-64e8-30f0-829b-295491172244 | -9.69034 | -51.03979 | 2025-09-03 00:50:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 4db3225e-e61f-3f9b-a115-35999b16bb23 | -12.93721 | -56.95543 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 754efd7a-1e2a-3924-8c79-f82c4b315433 | -14.5656 | -48.05338 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 999b4ed2-91d3-31f0-a0c4-c4368be494b5 | -8.01415 | -50.09315 | 2025-09-03 00:50:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 2dfbbb48-4b54-3b50-bc94-f92c78a49369 | -12.89421 | -48.04555 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 088bdec3-6bc1-39d3-9b9b-be47dc6a6c3a | -12.9749 | -54.76834 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 80eef60a-612a-3924-88bd-22fee941aedc | -16.29679 | -52.96149 | 2025-09-03 00:50:00 | TERRA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eeff7c56-92f4-3f57-b9b0-9e0ea5f30700 | -12.76254 | -47.67529 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0203b17f-03b5-38ec-a3a5-037616227dfa | -18.13429 | -51.7543 | 2025-09-03 00:50:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8825f1df-bc94-3834-a800-29d2639dab30 | -11.63955 | -52.06044 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 9c2ff043-dbbb-3742-ab69-34cc4a16fc2d | -13.31404 | -51.77241 | 2025-09-03 00:50:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 13dd82b3-ed5e-36e3-a791-a39bf216453e | -14.98254 | -50.20533 | 2025-09-03 00:50:00 | TERRA_M-M | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| dab76af5-04c3-3252-9036-f28be3e73e2d | -12.60092 | -48.2095 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 14ee8faa-7a56-31ac-ab6d-a0473aa2f527 | -15.5426 | -48.35199 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5687314b-4d4d-3d93-995a-2f08321a1ec9 | -11.02997 | -45.05209 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 8d568f75-9b17-3992-bdb0-687bad1a5ca0 | -15.56327 | -48.39843 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| b45c8eb1-1f06-37e9-b76d-445b067a066b | -17.53684 | -47.57341 | 2025-09-03 00:50:00 | TERRA_M-M | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0550ddd9-8cef-39fa-b8c9-7e81fe1c76f4 | -13.29841 | -46.92936 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e7e60826-70a2-3a2a-a53b-440c6f4d4bb1 | -14.57716 | -48.05762 | 2025-09-03 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 82824c5e-974f-3885-b4ac-3d8b54c618cc | -11.5965 | -52.13983 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a7898521-2bff-30a5-a381-8582d144b742 | -13.28293 | -46.82921 | 2025-09-03 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 2fd3036f-abcc-3981-9db4-e0e51550b865 | -12.85983 | -48.02594 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| eca84a52-fb05-3b19-a2cb-2c7ca5bf355f | -11.58768 | -52.14111 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 067c7dc2-a049-3040-b9eb-69c5b8b76ce9 | -12.60912 | -56.99904 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 62ba9d0a-db56-379f-9375-a80c146d601f | -15.60011 | -52.68405 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f0590d07-de22-3edb-8da6-c89c3783fc47 | -12.99602 | -48.10828 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| aadd6ccf-a314-3430-bf9d-089881fe8e15 | -10.45329 | -53.62174 | 2025-09-03 00:50:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 7877f8d9-8267-31a1-9485-cd76ebee4bde | -15.59099 | -52.68531 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 79d62103-63ef-3103-ad4f-bb60b479074c | -10.08318 | -54.76561 | 2025-09-03 00:50:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e981cfc4-9427-374e-8e05-f2f836575639 | -6.68527 | -44.18192 | 2025-09-03 00:50:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 63426fb5-1549-3eba-aadb-fecbecb954c7 | -15.55694 | -48.4212 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| a4cc0e67-931d-31a7-ac21-7a3c26dce4e1 | -11.14489 | -46.34341 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b621ed54-2c59-3bef-9d30-6fcb4866a418 | -8.21515 | -49.57445 | 2025-09-03 00:50:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 30562572-245e-3f27-85f1-93a4ea4a99c0 | -14.40981 | -51.70396 | 2025-09-03 00:50:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 799646d5-5b88-3ca8-9c83-e750a52d003e | -11.38577 | -43.59206 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 66e65b35-47e2-3858-bf12-259b54da12a3 | -11.11023 | -44.67545 | 2025-09-03 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 20c0c28e-eb49-39d1-8a28-022f252a2ceb | -8.36537 | -48.32542 | 2025-09-03 00:50:00 | TERRA_M-M | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 59990afa-dcfc-39e5-b48a-c748586b8ffa | -16.8598 | -49.60173 | 2025-09-03 00:50:00 | TERRA_M-M | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 69b5a55e-ea3a-3788-9f8e-e67a01c23ac7 | -11.11959 | -45.12128 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 78744ef5-016b-3760-937f-f32a6e7a4c8e | -15.56489 | -48.40904 | 2025-09-03 00:50:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 8c16890c-b1d5-3267-a213-7ce5b0da0b91 | -11.8644 | -51.54555 | 2025-09-03 00:50:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f25a9e7a-570c-3f78-98ad-7b4983f3246c | -11.41701 | -55.1918 | 2025-09-03 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| e16d44e3-0ab2-301d-91a4-09263f2d2959 | -9.62882 | -47.85637 | 2025-09-03 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 11ea09e2-3fe8-38c0-bf16-87ad20a91272 | -10.06037 | -48.09658 | 2025-09-03 00:50:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 4ec889c9-8381-3e3b-8534-5943224e5ef0 | -9.73824 | -49.40923 | 2025-09-03 00:50:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6bf7db12-4b8f-3c0d-923a-cb2e5c32e31a | -12.03575 | -45.57883 | 2025-09-03 00:50:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 5c9967b6-099c-3d7c-8fe8-24d5a652be7c | -12.91343 | -48.10361 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1868bb9c-0f53-3e23-9681-49b0435c0448 | -12.59906 | -48.19738 | 2025-09-03 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9d930bcb-2cef-3322-8318-cac6c2fda24c | -11.64574 | -52.10524 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 63e69d6e-cc85-3d27-840c-a2da2d050d0c | -15.71802 | -53.65408 | 2025-09-03 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a99cac60-80a6-3ee0-8d45-ff1c42581fcd | -11.57402 | -49.91078 | 2025-09-03 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8e48ea59-0178-388f-95e4-c74052afb70f | -11.38084 | -43.56347 | 2025-09-03 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 1b21e1da-6c71-3f2c-8441-52e1d07a0672 | -12.63429 | -57.01222 | 2025-09-03 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 53011c69-7f1f-33f2-a552-5d6cee3da485 | -11.60549 | -52.07455 | 2025-09-03 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 513a5102-6412-310a-b6d1-be7a78aa941a | -17.41707 | -48.06527 | 2025-09-03 00:50:00 | TERRA_M-M | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |


[Clique aqui para ver as próximas entradas](README12.md)
