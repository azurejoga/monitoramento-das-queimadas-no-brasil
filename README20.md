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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72c2b4e1-5f81-3e4b-bc9b-d3c48383df62 | -6.96778 | -42.88696 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 3c54f725-9f4b-3553-a2e0-870528c26242 | -6.95949 | -42.88895 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 866d519e-69ba-3d27-a5f9-4138c6963faf | -6.72601 | -43.1482 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6316a36f-0ae2-33c3-9fd1-20382102adcb | -6.20921 | -43.35914 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9dc4dc-a492-38c6-a40d-9291ead9315c | -6.02425 | -49.22568 | 2025-07-03 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa38385-9e22-304c-a76f-6832fd204238 | -7.25428 | -44.33567 | 2025-07-03 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0a611263-62a2-3c20-8255-e7d971ff9bdc | -5.91373 | -43.45034 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5354786c-daf4-3120-bacd-03131e610af8 | -6.28373 | -43.68113 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5367458f-9982-3fe2-ac25-fc1e52ab0400 | -6.92479 | -43.88499 | 2025-07-03 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4b1ad7d-cc0e-3916-97e0-f5199e451390 | -3.46024 | -49.3847 | 2025-07-03 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e2127d34-0b98-3019-9db0-14b3fb0639ee | -4.53777 | -48.02654 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8918ebfd-319b-34ac-95a0-93c3647f40b9 | -7.20203 | -43.09155 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2e4309bb-5e0f-364b-9399-50796566331b | -4.48821 | -50.50175 | 2025-07-03 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aadbe4a3-ecfb-33b4-aaf0-811dd6ce4ec9 | -7.06016 | -44.36496 | 2025-07-03 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 630ffe9b-21df-31db-b5c2-5f2ce558dfad | -6.69958 | -43.15554 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 58d1bc7a-7406-3d1d-8a51-83c416644fd0 | -6.72539 | -43.15289 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 922564b1-fb12-3e22-b347-23bf13a7bdf3 | -6.29018 | -43.67778 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 42623dad-0214-33df-add2-fda827a1f1e7 | -6.72169 | -43.18098 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 01e65fef-14e2-35be-811e-f4bd673015f5 | -2.92404 | -47.80957 | 2025-07-03 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91fbaf08-a3fa-37ec-b5cb-dbb783093d4f | -6.69149 | -43.16913 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 5ab8bf1c-ea73-3fb3-bd43-4f7176b2e023 | -5.92079 | -43.48601 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2601df6d-05c2-3d9a-a712-1058fa89d9de | -5.41337 | -49.08129 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dfca082-c5b2-3c1d-9583-feaa6d1a5ae2 | -7.22933 | -43.07563 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| b8d3dbf4-e91b-3259-8927-45072717c509 | -5.92139 | -43.48179 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c75d26e2-900e-3111-ada7-5623e11db35c | -6.96153 | -42.88625 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 6dec4568-86e7-3097-ab9d-763d41b9b30a | -6.01972 | -49.22859 | 2025-07-03 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52cce242-c7a3-3bfb-af35-670e22f205dd | -6.33287 | -43.75006 | 2025-07-03 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff1f86ec-1252-3ce2-8a98-096d8442b24c | -6.72466 | -43.15432 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82c360f1-ca25-3575-a2bb-b261e08a2911 | -7.19523 | -43.09539 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 006be530-dbfc-3c8f-b82c-f2ae6f063aa5 | -6.94838 | -42.88951 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 13e794a1-40b9-3ca7-b6b4-5985a10ca372 | -6.69345 | -43.15481 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5c39da75-8f60-35bb-b626-5d1d81c7a076 | -2.91172 | -48.23518 | 2025-07-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6dedefe-45be-330d-af7e-519e88d9e50c | -7.06069 | -44.36117 | 2025-07-03 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a175f0a5-4ae6-39e9-ba26-527764dc080c | -5.92198 | -43.47759 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f623d911-a327-31e6-96b1-6382ddda1152 | -5.3972 | -43.24819 | 2025-07-03 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a4ed513-0267-3e39-84c2-55d3b4b15e40 | -5.90838 | -43.44534 | 2025-07-03 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a12a9783-d3df-3e4d-9bee-4df4e91213ae | -13.43526 | -47.81973 | 2025-07-03 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd653673-d7c6-356b-9c64-e77b87bdab23 | -13.22827 | -57.13771 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b42a0198-8707-30d0-aee6-30a8e639e2d4 | -11.33105 | -55.21123 | 2025-07-03 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bec0a8d6-4aa1-3cc4-b4dc-28cf0b7e71ec | -12.42807 | -50.02795 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63b32acf-5b60-323a-a83d-541349424c77 | -7.85992 | -47.8816 | 2025-07-03 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb26a5d6-f6cd-3947-b650-7a60247784ec | -11.65709 | -44.59597 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 036397d1-3cd6-3212-a137-e7ac4de42dfa | -9.5305 | -63.57838 | 2025-07-03 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b778836-3805-3ced-bb9f-bc6a8be9abef | -10.29647 | -57.13962 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 020bf933-5b6d-3ff2-a04c-5578536ff4ea | -13.94837 | -46.37125 | 2025-07-03 04:57:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d98855d-c6ab-3986-ba59-1ada06a8067d | -10.82244 | -54.02448 | 2025-07-03 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e144923b-3540-3c1e-ba88-b54b5067cc6c | -13.94751 | -46.3784 | 2025-07-03 04:57:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7933e1e-3def-3a12-8dbc-ad9667b9046a | -11.31407 | -46.21169 | 2025-07-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0d91491f-ad9d-3535-8b33-0c323b4497c8 | -10.94769 | -51.37359 | 2025-07-03 04:57:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29894013-bbb5-3391-9a5c-e538b5893734 | -11.50317 | -48.96089 | 2025-07-03 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c3a424e5-157c-3f6f-805a-d75eabe0a836 | -9.17467 | -48.77538 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 11cd0fbe-574e-37f4-ab8e-d5d75be27afd | -8.86307 | -49.03684 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bf7bf44-d55b-3a92-a5d6-a7feb0ea0267 | -11.40506 | -55.36672 | 2025-07-03 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7be61fe-683d-343a-8874-8fdca1f3deb6 | -11.49934 | -48.95593 | 2025-07-03 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 419e531c-67bb-3453-b885-e95c21d584f2 | -10.1275 | -58.21516 | 2025-07-03 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 791e8b75-fdc6-39d3-8f04-38b846275eda | -11.87572 | -54.68063 | 2025-07-03 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 198e0c29-f2c8-3465-8809-c432a10f6e2b | -10.70574 | -49.67408 | 2025-07-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c9113ae-f50c-3bbe-a2ed-e13d8474cd75 | -8.52633 | -54.77298 | 2025-07-03 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5eb3d8-9101-32f1-b0e6-bea0accb0e62 | -13.94794 | -46.37484 | 2025-07-03 04:57:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27c13140-33a1-375c-ab62-618e4437e8af | -9.63377 | -61.463 | 2025-07-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a621f65-2836-3201-849a-834163d2fd2a | -9.514 | -65.58434 | 2025-07-03 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8042da72-d6fa-3867-9096-adfe8d59ce5d | -10.70991 | -49.67467 | 2025-07-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5542a51b-81ae-39e5-9016-4e5767c3501b | -10.68354 | -49.49185 | 2025-07-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62eee8fa-e44b-324f-8827-c6ee44b55d1a | -7.09647 | -49.16893 | 2025-07-03 04:57:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cda3b936-0e58-3607-acbe-5e8556272fb6 | -8.58374 | -49.87949 | 2025-07-03 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed91ae9b-e437-3c81-97bd-cfd4ea2296af | -9.17405 | -48.76782 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8155b25e-d755-3e3d-accf-5239e66eeb5e | -11.64059 | -48.0726 | 2025-07-03 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 885b3b3b-2e3d-3f87-be6d-e81a40e5fbd3 | -10.88856 | -56.45485 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adbf0be3-35ce-3d14-8546-f1810eb2e78a | -10.5366 | -56.23626 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7642b559-ef90-3cd1-8805-576af6e906fd | -11.54832 | -47.31203 | 2025-07-03 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8ffbad3c-ec93-3003-868f-2d3a4ada2b64 | -9.08827 | -59.48465 | 2025-07-03 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fdddab9-75ba-34b1-af52-6e9085fff4ab | -10.88579 | -56.45072 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16b268e4-1dd7-32c0-8e0d-be4a4101657c | -9.17779 | -48.77258 | 2025-07-03 04:57:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ca6bf31-adb8-317b-a9a3-6ac4a35d4531 | -11.65321 | -44.59893 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9ed6a898-bacf-34ea-8ccf-6fb4144bb5b5 | -12.42282 | -50.03509 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7968dd70-9771-3ce9-923d-708061e94edc | -8.58572 | -49.88018 | 2025-07-03 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0fe411a-c9a5-316e-932f-6e02d46cd788 | -10.89248 | -56.45183 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a38dbc89-d059-343a-b4c8-48a964676666 | -9.70465 | -56.18449 | 2025-07-03 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03885e11-913c-3503-ab2e-40385c6d9479 | -10.30392 | -57.13703 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| befe3f44-7699-3e4b-81a9-d68aa6700252 | -10.70521 | -49.67792 | 2025-07-03 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 026c45a9-6d8e-30af-8286-87885a8e37b9 | -11.64726 | -44.59821 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d282d934-2c09-3b7d-af52-0c329cd9c8c2 | -10.6631 | -49.45371 | 2025-07-03 04:57:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41def5ca-2293-3ab1-b6c1-b3acc3910de0 | -10.88521 | -56.4543 | 2025-07-03 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8862cf5-803a-32c1-abd4-fd719bf62fff | -7.8554 | -47.88091 | 2025-07-03 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fb1e7d4-1d05-32a0-8db5-5ae581a201f0 | -7.61173 | -45.75119 | 2025-07-03 04:57:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12d994f9-a5c2-34e4-acaa-3fedf1a5913d | -9.09082 | -62.67232 | 2025-07-03 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 741c2e98-5383-374a-a9c1-203eb9fe2ad9 | -6.97401 | -55.28394 | 2025-07-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2efe89d-ba8d-352d-9da8-82deeae2d19e | -12.42389 | -50.02737 | 2025-07-03 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b40604a8-2230-3811-b86c-206cb0507dc4 | -10.99373 | -45.19991 | 2025-07-03 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e7e699a-4979-3bdb-9739-f6b77d0ec620 | -10.29833 | -57.12838 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 59e88939-241c-3725-8778-a45a59f4eee8 | -9.39886 | -63.25647 | 2025-07-03 04:57:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f46b3ac6-e80a-3564-b264-80f2b03a8b41 | -11.78781 | -57.24618 | 2025-07-03 04:57:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d87a07d9-51d5-3cf3-a068-43e9cee543fb | -11.65916 | -44.59966 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4fc907a3-3238-3c7a-bd59-33ba2897f037 | -13.22694 | -57.13411 | 2025-07-03 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6bd41651-1e8d-30fe-b3b7-67d888a5f40e | -11.1435 | -43.33209 | 2025-07-03 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 61887550-3cd2-3551-9a36-f81bb2ad7f53 | -11.66305 | -44.59673 | 2025-07-03 04:57:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8713d76a-90cd-3949-99a0-7a4fe7d0ef8f | -10.08874 | -47.99345 | 2025-07-03 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9e6b4c0-5366-305f-bc5f-4b0e009de75d | -11.87294 | -54.67654 | 2025-07-03 04:57:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b729fccb-032c-37af-98fd-6961aef097b9 | -7.73448 | -55.41658 | 2025-07-03 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4e531fd-5e65-3bc7-9b94-6ae08a5d3e9e | -8.71884 | -64.17412 | 2025-07-03 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README21.md)
