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
| 6333d79c-9b8f-3e3e-9204-a21490da0f81 | -19.04943 | -53.45796 | 2025-06-06 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ee376fd-a883-3331-b91f-730a11ec542c | -19.43485 | -54.77566 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8187354d-443b-3418-8c16-5487e1f1a679 | -19.04608 | -53.45736 | 2025-06-06 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 335934b9-a66d-3087-a96a-365c4f436e12 | -15.01058 | -56.05444 | 2025-06-06 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 039978d6-41a6-386c-8b77-e8e2fce33f96 | -19.07353 | -53.45846 | 2025-06-06 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| edf77578-f13e-3ef3-9f0d-e9068086aada | -20.82215 | -54.95422 | 2025-06-06 04:44:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67093693-7e65-3897-b28f-cd007e27d21e | -19.42793 | -54.77434 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e32a2310-f169-3bcc-9026-dd3ee665ffa5 | -15.0103 | -56.05773 | 2025-06-06 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88fd02be-ba96-33e6-a586-bfee16e9bbf7 | -19.27997 | -55.15509 | 2025-06-06 04:44:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77cc131f-0082-3589-9f61-5acc42b4f79a | -19.42726 | -54.77829 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 77e8a1cd-f975-350f-a9f5-a53da67e15e8 | -15.00883 | -56.06409 | 2025-06-06 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bec95f67-d3e5-3bae-8b1b-586c27669f5b | -17.60045 | -48.41856 | 2025-06-06 04:44:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 499e93cf-6ec3-35e6-856f-beed235313ef | -17.91138 | -54.1138 | 2025-06-06 04:44:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f282bb6-8643-3de3-9ade-3fedddd8f1a7 | -19.43831 | -54.77633 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 12.0 |
| f3488ba9-410d-3db6-89bd-4f7c62f4f305 | -19.39968 | -54.46809 | 2025-06-06 04:44:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0410836e-0139-33e3-9da6-d812f87db569 | -17.93807 | -48.92178 | 2025-06-06 04:44:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f603fd3-3422-30be-bdc0-a0bb3fc79abf | -19.016 | -53.48935 | 2025-06-06 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8806a109-d68d-331a-9136-3d70b7fe2719 | -15.00971 | -56.05925 | 2025-06-06 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 025795c9-bf74-37c1-b4d0-e008d9686e1f | -15.01115 | -56.0529 | 2025-06-06 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7434e9ff-7766-3b0a-ada0-d7faecacabce | -19.07292 | -53.46218 | 2025-06-06 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5e98291-779d-33b1-a2b6-9e34f9e66cc7 | -17.93445 | -48.9212 | 2025-06-06 04:44:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d527812a-e887-3dbd-83dd-efd1e968632d | -17.59982 | -48.42307 | 2025-06-06 04:44:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0285b118-414e-30c4-a8a1-d89101484cb1 | -19.05279 | -53.45856 | 2025-06-06 04:44:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b25207de-821b-3602-9161-0c564d6a8f5c | -20.54671 | -54.11769 | 2025-06-06 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e00cc334-0b04-3c3d-b0e4-5004fb893e70 | -21.47476 | -56.61349 | 2025-06-06 04:44:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5563dd44-77cb-3dbb-b9ea-863b27edffcf | -15.00945 | -56.06256 | 2025-06-06 04:44:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67589e9e-68d1-3a60-ac9b-c7aa86007645 | -18.40846 | -54.57452 | 2025-06-06 04:44:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56e18218-a692-3bc3-b331-5af0f5b08b7d | -20.48025 | -53.67448 | 2025-06-06 04:44:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 114d2b92-d9b8-35aa-8456-aa76382365a0 | -30.15183 | -52.02663 | 2025-06-06 04:46:00 | NPP-375D | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 4b6a3f2f-b983-3cce-a1f3-58d895254eab | -7.71981 | -44.17822 | 2025-06-06 04:59:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e7bdb6e6-8e66-3151-8b9b-ff4679255dc1 | -7.014 | -44.60414 | 2025-06-06 04:59:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 91a383f7-9cdc-3ee8-b020-3d90e04b5013 | -7.00919 | -44.59629 | 2025-06-06 04:59:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 69646f2a-a9d2-3313-ba9b-2b8cf8b92ef5 | -7.71856 | -44.177 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6a06f6e-fea8-3bca-9a90-47b73075d995 | -6.21441 | -55.65091 | 2025-06-06 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8785ef6c-eddd-3051-a14d-3533f30fa706 | -6.19359 | -48.56908 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97ed6df2-bb53-3e00-87fa-a9d1f6b9e244 | -7.20357 | -43.131 | 2025-06-06 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f4399104-68ca-3aad-aad5-b7e49a83aba9 | -5.02781 | -56.19376 | 2025-06-06 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4e177c07-e094-3488-aced-0864a23edda9 | -7.19841 | -43.13677 | 2025-06-06 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 8d7c4f08-c51b-3859-a03d-23a93d25d0d1 | -7.72562 | -44.17273 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f8892156-828c-36e8-b31e-78b5403655a8 | -7.72667 | -44.17977 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a4ffd9e-f629-368d-85e9-e9aee2f37ba7 | -6.22953 | -48.55083 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 58d5054d-f055-3d23-a640-fc8b9a623679 | -7.71592 | -44.16233 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed012cf-8ff1-3dd9-9c68-73d9955f3111 | -6.19826 | -48.56972 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a174294-07c8-34b5-af1f-d046277b1376 | -6.29535 | -48.47428 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60749d58-921f-3915-82bb-398daf1d2111 | -7.72096 | -44.17367 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6acd4bfc-9fd0-3603-82ba-fc17037791d6 | -7.31034 | -50.60673 | 2025-06-06 05:01:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 264e088b-10ab-3338-b8c6-db43b212e986 | -2.92227 | -48.23571 | 2025-06-06 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52f47496-c8d8-3860-974d-b1c6bafde39c | -6.66336 | -51.96047 | 2025-06-06 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7ae907f-769a-3aaf-887f-171e7b26b559 | -7.9014 | -50.36955 | 2025-06-06 05:01:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e10cb797-ede4-3453-8abf-9e70972bdbbd | -6.23748 | -48.56169 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83b6213e-6a54-3a4d-8c83-2b29aaefc130 | -6.19028 | -48.55898 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d470fb26-b924-30e0-a469-9befe25a5e6b | -4.41786 | -47.66583 | 2025-06-06 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b51471c-df53-37da-a23b-e4a5125f1284 | -7.71926 | -44.17183 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 583ce28f-b742-375c-8ca5-3265656b1617 | -6.19094 | -48.55436 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7ca178e-a00e-3c6b-aa57-f02d6b7e4d9f | -7.20279 | -43.13686 | 2025-06-06 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aaad94ab-7dfa-3f33-a543-bd3c8daff0c0 | -5.12162 | -56.11586 | 2025-06-06 05:01:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd0d2fa1-f60e-314d-947f-cac6e822d7b9 | -7.71658 | -44.15713 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f7e3bba-d1e2-3efa-9500-7f0bbf4f70b6 | -6.19695 | -48.54554 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d402875-6a8c-39b7-aacb-ffb23cea8906 | -2.91774 | -48.235 | 2025-06-06 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d153c1e-cfe0-3baf-b4b1-f9d26c17c6e9 | -7.73304 | -44.18062 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5b4bf4e-9b6a-35cb-8dd4-37d3dfe3fdaf | -6.29929 | -48.48033 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f00af28-a69f-33a7-91a4-d3baba16faf1 | -7.72493 | -44.17791 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47f3afd1-160c-31b9-8d94-285284759c79 | -4.97283 | -47.81505 | 2025-06-06 05:01:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 466c9f36-b804-3f67-b0c6-314ef9ad4887 | -7.90675 | -50.36232 | 2025-06-06 05:01:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 94cbcd13-6d70-37de-a278-4befaab6b3a0 | -7.90619 | -50.36623 | 2025-06-06 05:01:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8719bf1c-08e5-3ebe-82ef-1202bec4e9e4 | -6.68256 | -55.19899 | 2025-06-06 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6beb8f9-6f93-3a36-9b49-8e5b66197eaf | -7.72733 | -44.17459 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3fb3d1f6-cd9b-3750-83db-02d29d6d67c0 | -7.7306 | -44.18393 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 83c31a8a-0c7c-321a-baaf-f9d0ec2d6a9f | -7.19606 | -43.13589 | 2025-06-06 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9f19171f-0b99-3090-8bdb-c3c0c1e75a3d | -2.91844 | -48.23042 | 2025-06-06 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2dff9b14-7ec7-3b3f-94e6-7ea050d35e65 | -7.31077 | -55.3079 | 2025-06-06 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2582c372-24bf-376b-8d0c-86110dd674fb | -7.90253 | -50.36169 | 2025-06-06 05:01:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f893bdee-f803-376a-8cc3-5fc600452e01 | -7.7313 | -44.17876 | 2025-06-06 05:01:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 99bff71b-bead-3e30-bc52-ddc76d2d3630 | -6.19627 | -48.55034 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 131fc18e-fe3f-392a-a985-c17c9744eefb | -7.90197 | -50.36562 | 2025-06-06 05:01:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 69318cd3-2b1a-3291-91f2-a47b0dc59ec3 | -6.23418 | -48.55159 | 2025-06-06 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5792759a-b9e6-3238-a725-f378e3c906ab | -3.99759 | -43.24277 | 2025-06-06 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72b769eb-e38f-329a-b382-4414346cf6f7 | -6.12372 | -46.82243 | 2025-06-06 05:01:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2640ad82-31af-3500-a1ab-c4d052674d1d | -9.39381 | -48.42702 | 2025-06-06 05:04:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6733f433-2849-3c76-bc60-9bfa03f115d7 | -14.02533 | -55.13256 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c55ef89-d172-3968-b49b-1bca5ce70b70 | -10.99259 | -49.01863 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 215a43b9-6aa5-3711-b7eb-079c10ade05e | -10.30713 | -57.13573 | 2025-06-06 05:04:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cd40c96-77dc-39dd-a5d7-92ae109a90bb | -11.38746 | -56.55221 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a596ee36-27f2-37fc-844d-1febe6925a97 | -13.52006 | -56.56985 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 068f0a6d-5358-324a-822c-598d36c953de | -13.51395 | -56.56519 | 2025-06-06 05:04:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e143605-dd77-36af-afc1-c146fa8fc313 | -10.53702 | -56.23665 | 2025-06-06 05:04:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd227bab-d2e0-3183-b809-965f63585d5f | -12.8354 | -47.38628 | 2025-06-06 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f21cbaf4-4275-30fb-8a83-69bbe6777cb3 | -11.71143 | -56.45602 | 2025-06-06 05:04:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 840845dc-efc3-3cc9-b3a0-b1b8c0703a8f | -11.38691 | -56.55571 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c348a60-a9c8-3dcd-9a47-5a2493ce33b3 | -11.38305 | -56.5587 | 2025-06-06 05:04:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17f7bd02-5107-37a3-9c9b-7a4829af4dd5 | -14.03866 | -55.13866 | 2025-06-06 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4488ca80-5e18-3a72-8171-2771f2dfc580 | -10.49131 | -53.66477 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 366f7a99-5572-3cdc-a4d6-0b05dc08fb97 | -10.48993 | -53.66249 | 2025-06-06 05:04:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 45b0d58a-386b-3a43-9b2e-e147bd6001ce | -10.66045 | -55.31116 | 2025-06-06 05:04:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1345acd7-dd6e-3303-8510-ae4b351c9157 | -12.95767 | -46.78119 | 2025-06-06 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fd07829-8091-3868-8a66-3edc14804115 | -9.79318 | -63.39223 | 2025-06-06 05:04:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 476e5f02-7334-37bb-9dd6-89a891d8714c | -14.22094 | -45.48938 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91267e62-bf7c-383e-a4b3-4b244707a99f | -14.22675 | -45.49541 | 2025-06-06 05:04:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 671b592d-4463-3f77-ae80-6f70efe2b184 | -10.14592 | -52.13524 | 2025-06-06 05:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d378ab5b-83e3-37f1-88fd-8737b8e142de | -8.47404 | -49.60254 | 2025-06-06 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
