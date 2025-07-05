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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87e2550e-2683-3d71-8d85-9753ab35edfb | -5.72161 | -49.1111 | 2025-07-05 03:55:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 980623b9-7e66-3af8-99d7-ad92a4c4ff2b | -6.99792 | -44.29057 | 2025-07-05 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64fd66a3-f81f-3454-807b-6ea613aa1efa | -4.11368 | -47.92855 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a4c3251-0d5d-382f-9ebe-0a07ed1fec39 | -5.60626 | -45.174 | 2025-07-05 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bef874f3-ac08-3b11-aff6-e62f157cef47 | -8.07324 | -34.97904 | 2025-07-05 03:55:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4b157c36-2362-384d-8d65-d495867b9c0d | -4.11271 | -47.92646 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7e1a915-e36f-37d6-af06-d15ed082e17c | -7.15317 | -44.32028 | 2025-07-05 03:55:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f437a54-da25-3bb0-b4a0-3b6482bb6c3d | -4.11146 | -47.93396 | 2025-07-05 03:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0daaa0d-960d-3233-b31e-d8281c40df54 | -4.90304 | -37.36492 | 2025-07-05 03:55:00 | NPP-375D | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6a353df4-579c-38a6-aedc-2d8f8f68f63b | -7.94953 | -44.85015 | 2025-07-05 03:55:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 59dcdfc5-9ffe-3db2-8e9b-06628d96b4df | -3.52776 | -48.43385 | 2025-07-05 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbc843ef-9cef-327a-9f71-a44efd282381 | -3.81248 | -42.5463 | 2025-07-05 03:55:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fde3814-a3f5-3a3b-8eef-ae8e121f2e1e | -6.68325 | -43.15882 | 2025-07-05 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9ce48413-de4c-31db-9c0d-b5157d61d515 | -8.25054 | -35.71046 | 2025-07-05 03:55:00 | NPP-375D | SAIRÉ | PERNAMBUCO | Brasil | 2612000 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 43ec82d5-b5ba-3d4c-87d0-18c64c1a09a0 | -4.23733 | -41.90468 | 2025-07-05 03:55:00 | NPP-375D | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 735d2245-d233-3529-8740-7ffbe08596ec | -5.06671 | -43.72566 | 2025-07-05 03:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f8917e0-cb5f-3e78-8495-e25313dae9ff | -7.24904 | -43.08336 | 2025-07-05 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 10f8dba8-8a3c-3a40-85e9-67aeaa1fb1a3 | -4.81741 | -44.35328 | 2025-07-05 03:55:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a51569cc-2ee7-3cef-baf4-d00dcdbf6f76 | -5.07094 | -43.72631 | 2025-07-05 03:55:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c947f1c6-7ef2-3b00-a719-5e7463076cb7 | -7.34505 | -49.63638 | 2025-07-05 03:55:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39df4f74-d9e2-3ca9-9945-3f61238ba43f | -11.44967 | -45.11664 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0bd814c-10be-386d-8840-029e0b5b4223 | -12.01555 | -47.76677 | 2025-07-05 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd99d018-9765-3658-a5ef-427eb87796a1 | -8.9975 | -47.44434 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| afe8b99b-d770-3b81-8219-7e805a7183f1 | -11.44134 | -45.1151 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96fc2353-f4ca-358f-8e5e-3eb9d9aad346 | -12.75545 | -44.41711 | 2025-07-05 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96505155-fe9c-322b-91b7-c012268c0787 | -13.12083 | -46.9173 | 2025-07-05 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3dd4ed41-79d7-35e4-bb7a-a7f90b58aea4 | -10.56794 | -49.13418 | 2025-07-05 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afb7610e-df5f-3ef8-b6ab-eca103cd8973 | -10.61374 | -46.42662 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 46080372-c831-329f-a1b8-2b2f9886ef36 | -14.66681 | -45.37265 | 2025-07-05 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc45189a-4635-34c1-8e9a-3acda59eabd0 | -9.58674 | -44.6054 | 2025-07-05 03:57:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b1fdb9f-b0c2-3dfa-b67d-734431b227ab | -11.87521 | -44.87276 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36280738-5285-3618-8d7f-65e873ee1476 | -15.92582 | -43.51542 | 2025-07-05 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 696e5443-7694-343c-9b7e-54fd1a4732d6 | -8.99644 | -47.45028 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b94b7453-f3e1-3688-9040-4c8be82cf407 | -11.45451 | -45.11355 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a731696-1435-3e1c-9012-4832b1316a47 | -12.75154 | -44.4164 | 2025-07-05 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1e84c00-d157-3068-afc4-39d7f4bae5c8 | -8.01142 | -49.7179 | 2025-07-05 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e222c34-0981-349c-92fa-0bf76ec00b90 | -10.36311 | -48.72118 | 2025-07-05 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b720332-6207-35d2-b65e-1530d5afff65 | -13.12169 | -46.91252 | 2025-07-05 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37120b8d-6a00-30df-90ae-bc9a1ad3110b | -11.43717 | -45.11433 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b040138-90ce-3f5f-84cc-cb1c0b0e9f1d | -8.99591 | -47.45324 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4f25c3a-e8ca-3e0e-a700-2c53704477d7 | -9.79441 | -47.74591 | 2025-07-05 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f605edd-69af-3eec-98d1-4f67cf52f98f | -10.60451 | -46.42496 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9d4014b8-5930-3fa0-a01e-31f8fabec66a | -15.92509 | -43.51961 | 2025-07-05 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4889af49-8de2-30a3-bbc8-35eb1ddd2194 | -11.31043 | -42.13116 | 2025-07-05 03:57:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ebba160-9fe2-38be-a67a-4ddd0c43087a | -11.43786 | -45.11047 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b489d7e6-c582-32b4-8e1a-40c87e18f143 | -12.68985 | -44.60518 | 2025-07-05 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25758e49-a574-3de0-9454-f4e16d5373ea | -9.58125 | -44.61239 | 2025-07-05 03:57:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33cf9b95-9fc9-354d-8616-ce6a38acab7d | -14.48044 | -46.35761 | 2025-07-05 03:57:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6689ed6-c263-377a-b314-6d279ae3727f | -10.60657 | -46.42374 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| adb924f4-e2c2-3222-88eb-f3d396e2c79f | -9.78709 | -48.2561 | 2025-07-05 03:57:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52bd8a11-31cb-34e5-9a4c-0146a989d626 | -9.00205 | -47.44827 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 451e094e-4b88-3a35-928f-b95e4b54b9dc | -10.66139 | -46.40031 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84dfc52d-5bc1-310d-a3ae-e01798a0a2f4 | -10.56244 | -49.13299 | 2025-07-05 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4ea5277d-0e8c-30a8-afd4-32a19623fcec | -10.55766 | -49.12807 | 2025-07-05 03:57:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 61254fca-1231-3884-8ace-05ad47e96e2e | -10.61119 | -46.42455 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f50377a-ac37-3369-adf2-ed7f86bb903b | -7.95346 | -47.23191 | 2025-07-05 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6d719f8a-b996-3911-889b-8f78bab42892 | -15.07919 | -48.94637 | 2025-07-05 03:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d90c8c21-65b1-364c-b548-5e4dd7fb79c6 | -15.03978 | -45.6175 | 2025-07-05 03:57:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f406243b-15b1-3306-8afc-a37625ff14a0 | -9.79498 | -47.74281 | 2025-07-05 03:57:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05a1c6e1-c5b8-3cb8-bb2e-efdf4f939d99 | -9.78764 | -48.25309 | 2025-07-05 03:57:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b23fb607-7579-36dc-b1ae-30144b9f1bfa | -10.6158 | -46.42543 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ad9cca6-d6db-3b8e-8ff6-4608d7218a17 | -12.0145 | -47.77233 | 2025-07-05 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db22eeff-0e75-3121-a265-35cc643c0fda | -10.37284 | -46.99115 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4cb5c0e8-3ed3-385e-a27a-7baed458167e | -10.61533 | -46.39213 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85c3ab70-ca5d-36f4-85bb-e9c5e25ad746 | -10.63434 | -46.47056 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 83afe985-1d15-3a17-8544-f6eff6b3c743 | -10.61092 | -46.41605 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 042b6b4e-d13f-3057-aa5c-f96554c498f9 | -10.35775 | -48.71999 | 2025-07-05 03:57:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b3ee6c-4925-3b7e-ac2f-c9bb51d8fa18 | -11.87584 | -44.86923 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b5a5370-716a-3624-8938-8a83cc7a5c09 | -9.58607 | -44.60926 | 2025-07-05 03:57:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 06fa71bd-2603-3f7d-8ee7-1715a6632c83 | -8.01743 | -49.71893 | 2025-07-05 03:57:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5629ada-7a89-3bfe-8ab0-aad2ee7e9955 | -10.61291 | -46.41483 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbf1c57-9df3-3a65-873b-08022ba2d789 | -11.87499 | -44.85047 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f357c2d6-a56b-316a-b79a-ad153f53fc87 | -11.88052 | -44.86658 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13c4d3a9-6829-3cb3-8e84-d2ced64c7a2c | -9.00152 | -47.45126 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95b629ea-a7fd-347d-b0d4-5f8cf7ffeb4b | -10.6513 | -46.40349 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fe32ca2-914e-3162-8bf2-f63eac448040 | -13.23612 | -48.02853 | 2025-07-05 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da49e8af-3b38-3126-acc0-a2c659b354fc | -14.66214 | -45.37549 | 2025-07-05 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8ff2e83-57eb-3174-a4ad-19766a161bf4 | -11.87393 | -44.87992 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d6ddbc9c-b9ee-35cb-8575-9fa07b5b7c3f | -8.37785 | -51.07126 | 2025-07-05 03:57:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f07f773-5389-36a0-ba16-65a2f9142121 | -10.60823 | -46.43068 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cdee1b5f-33da-3dd6-854e-0b1ce6e4e3f4 | -8.99697 | -47.44731 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bbf8374-a015-35ba-b3c5-0994b58030fe | -14.67018 | -45.37703 | 2025-07-05 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2303d72c-ec84-3973-abaa-d65d6140a081 | -11.00216 | -42.79107 | 2025-07-05 03:57:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e02826c-a377-3fc8-9c27-9eb91bc85ac3 | -9.00258 | -47.44529 | 2025-07-05 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70225da-ff13-3e48-8b88-b56c857f62f6 | -10.65679 | -46.39947 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c097dacd-031b-3d11-93e5-d6578379e6ef | -11.87988 | -44.87014 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7089731-5de1-33c5-83fb-accdc09a79cb | -10.61032 | -46.4295 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dc37ad13-90f0-3e2f-9eef-3b2cd5594a14 | -10.63897 | -46.47137 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e5e6898-c9a3-3dec-8619-f7e8462487e1 | -10.61465 | -46.42169 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f308353d-6f58-3b0a-b82f-a55b75c2197e | -11.87801 | -44.88061 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 527bb544-dec3-3a8b-b088-ec195f161214 | -11.87436 | -44.85403 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64715939-01b7-31cb-be56-f262a87eb043 | -12.75242 | -44.41137 | 2025-07-05 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95bfb173-bd4a-3fc6-a9a3-3e6674a2c22c | -14.67949 | -45.37136 | 2025-07-05 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57b19d8a-be53-3120-9230-ea907f466ad4 | -11.45035 | -45.11278 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 397aadaa-0b4d-3140-a6a5-45223f481db5 | -11.87051 | -44.87552 | 2025-07-05 03:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7a5d9481-c6fb-3430-bdea-3bfacf52da4a | -12.76199 | -44.40273 | 2025-07-05 03:57:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c799699-08b4-300f-9dd4-6eedfe8a1ba2 | -13.12085 | -46.91404 | 2025-07-05 03:57:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94c71454-632a-3acb-a7a2-dedf95927445 | -9.84473 | -46.46754 | 2025-07-05 03:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43037ea0-e621-3cb0-bb19-3ca6faaa7f60 | -10.61666 | -46.42051 | 2025-07-05 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ba0f9b9-7a9f-31c3-9e16-63a278dbd9d2 | -14.67885 | -45.37496 | 2025-07-05 03:57:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
