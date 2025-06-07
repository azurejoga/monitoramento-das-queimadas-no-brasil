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
| 4f0b9f65-a689-361b-a6d1-a80a5b9c4547 | -13.51913 | -56.56543 | 2025-06-07 04:46:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd6a9707-7529-34d6-8ec5-5bcdd22be245 | -12.96674 | -46.77264 | 2025-06-07 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc403092-ccda-3126-8574-20b841e10fef | -11.42457 | -54.29484 | 2025-06-07 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45d8e98e-2482-30af-9d20-07ffef0fd8c4 | -13.88625 | -54.66743 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a958d8b-fefa-3cbe-b87a-04f7cd51c984 | -11.25992 | -60.79826 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d7893bb-05fe-34f4-a8e5-20a380f3d4d7 | -14.72868 | -45.07676 | 2025-06-07 04:46:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b33daea1-10b9-36c2-af75-20fcfbbee4e7 | -10.88134 | -54.31259 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a61f63-3e98-38b4-b2fd-4c173f7aa8c2 | -11.38421 | -56.55799 | 2025-06-07 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d83b349-3c0b-3dba-a09f-daee6112860c | -13.88439 | -54.67875 | 2025-06-07 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bbdb5207-dbf3-3875-bf01-13e42e53cb97 | -12.8842 | -52.2055 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eec9a85e-4712-341a-921a-d8f3a3e15aa8 | -11.54301 | -60.99417 | 2025-06-07 04:46:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a66df228-72d5-339c-bb8a-d8057e2a6001 | -14.21523 | -45.48037 | 2025-06-07 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85ed9c36-48ba-30ac-8e9d-9053377306a6 | -10.33389 | -57.49358 | 2025-06-07 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e658956b-30aa-3d87-881e-a1452307c91a | -14.03085 | -55.13235 | 2025-06-07 04:46:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a24ea25e-0c34-3e9e-801e-97ffd5850f37 | -11.1175 | -54.6643 | 2025-06-07 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37ad869f-f6c6-3e26-bd05-24803191f223 | -12.70145 | -58.02472 | 2025-06-07 04:46:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef1f8295-3456-3e8c-bc49-d01aed9caf39 | -12.32781 | -52.48373 | 2025-06-07 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| daacb667-aa06-3cd4-9bb0-fecb6997e85c | -11.91419 | -54.82573 | 2025-06-07 04:46:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a3c35f-33d8-3dfa-962f-3375f2d31ca9 | -20.85921 | -51.51508 | 2025-06-07 04:49:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9823d5cc-1c66-31c6-817d-1eb7cf7bb36e | -20.92293 | -49.09699 | 2025-06-07 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 08ea52b9-1b8e-34b3-a17f-e225e23a2127 | -19.02036 | -57.62226 | 2025-06-07 04:49:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b8872b79-2cca-316b-8fad-4eb6b672a42e | -20.9234 | -49.09326 | 2025-06-07 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 317a1f36-041c-3c47-a6e2-8670bbeedc66 | -19.07698 | -53.46102 | 2025-06-07 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8efb3f1-f638-3696-820e-776dcc5940ca | -20.99694 | -51.79081 | 2025-06-07 04:49:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7a7e118e-5a18-3e14-98a9-9d3e9878e3f7 | -18.40432 | -54.57591 | 2025-06-07 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e9ba4d6c-3a0b-3096-9055-010253733760 | -23.33676 | -46.773 | 2025-06-07 04:49:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 335649fe-9ab1-3599-99bc-4292f3cdc959 | -19.04987 | -53.46011 | 2025-06-07 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b1bb887-69ca-324a-b10a-d5d14d2847e9 | -19.07641 | -53.46467 | 2025-06-07 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ac4dd3b-170f-3022-bd45-993c50675e10 | -20.73106 | -56.65496 | 2025-06-07 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 185d7c92-dd19-3e74-813b-973c930605f7 | -19.04655 | -53.45954 | 2025-06-07 04:49:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0de803ae-372e-305a-a23d-0c20d2c7c214 | -22.31398 | -53.63214 | 2025-06-07 04:49:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 6730bb0d-a196-3f63-a75d-bf36ae5fd9b2 | -20.9209 | -49.047 | 2025-06-07 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fb80dbbc-7df7-311b-9743-979722cce081 | -20.0868 | -51.23909 | 2025-06-07 04:49:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7addfef6-a68f-3d5e-a38c-c6147878ee4e | -18.40765 | -54.5765 | 2025-06-07 04:49:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c51f72e7-8d83-381b-8a3e-92320f8f5e0f | -20.9408 | -56.59771 | 2025-06-07 04:49:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7609bb1a-9ad3-3ac1-88c8-4eaff097d7d9 | -21.18991 | -55.69644 | 2025-06-07 04:49:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 861c6e83-6eb7-380a-94bb-ef6405ef6e7f | -20.76331 | -46.77073 | 2025-06-07 04:49:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7c9096a8-d548-3dc1-9ac7-8ec14d9c1ec5 | -19.7335 | -54.51061 | 2025-06-07 04:49:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad201c7b-e9e2-3973-8319-fef580455c09 | -22.29634 | -55.1819 | 2025-06-07 04:49:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 949d5a9f-f1dc-3591-93fa-e9ee6006d7e2 | -20.92495 | -49.04763 | 2025-06-07 04:49:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9e1f33ee-31e4-3bcc-8005-8fee2aa433ae | -20.7276 | -56.65434 | 2025-06-07 04:49:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86505987-cba4-33cc-b40e-82b9b4862d9e | -20.55976 | -54.0742 | 2025-06-07 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc826ff0-ab28-3f5f-a898-7915a90c5bb4 | -19.42536 | -54.77676 | 2025-06-07 04:49:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a625d81-e8ba-3f20-b455-ef67e5e0210b | -6.9602 | -42.9052 | 2025-06-07 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| dc2fd93e-e4d6-3098-ade9-284f0559c163 | -7.7361 | -44.1823 | 2025-06-07 04:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| b67ed367-e6dd-3bcf-8850-8b9c020f7a98 | -5.6379 | -43.7175 | 2025-06-07 04:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 288fc01e-1fd6-3e20-8a1a-903136dd32fa | -7.7364 | -44.1592 | 2025-06-07 04:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 25142e8e-1b15-377a-97fb-e20e5a5afb22 | -7.7176 | -44.1611 | 2025-06-07 04:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 8b59e57b-c9ff-3564-b5b6-08d1a0cffaf3 | -7.7176 | -44.1611 | 2025-06-07 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6062968b-cc62-35d9-82a8-21bafbfb0dab | -5.6379 | -43.7175 | 2025-06-07 05:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| e964561f-7afa-3bb3-b0a0-c69f898ee137 | -7.7361 | -44.1823 | 2025-06-07 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2134f8e3-6b70-338f-b889-b877f102e1f1 | -6.9602 | -42.9052 | 2025-06-07 05:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| cf194cd3-ef63-3a8a-a575-ec7332785682 | -7.7364 | -44.1592 | 2025-06-07 05:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 113.8 |
| b563aa40-14d7-3c64-bd37-f8e69ed2a168 | -12.9628 | -46.7626 | 2025-06-07 05:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.8 |
| db30c62a-807b-3abc-b038-6ac50e56f1de | -7.7361 | -44.1823 | 2025-06-07 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 4af6b74a-669d-3ee5-9d70-01861e4e60f4 | -5.6567 | -43.7161 | 2025-06-07 05:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 044b749b-5622-3696-83e0-a39be59c9fc3 | -5.6379 | -43.7175 | 2025-06-07 05:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 08c5a111-a97a-3f80-b34b-5fb6fbe23e51 | -7.7364 | -44.1592 | 2025-06-07 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f30a7e9f-0d16-37e6-9b66-9f576f952864 | -6.9602 | -42.9052 | 2025-06-07 05:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 116.0 |
| 13ca170f-96d0-30ce-a5f7-2891543c604d | -7.7176 | -44.1611 | 2025-06-07 05:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 085e53e3-a864-352f-ba2a-213b3f2ecf20 | -5.6567 | -43.7161 | 2025-06-07 05:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 290f342f-3dd4-3319-a5b3-a005bba40e90 | -6.9602 | -42.9052 | 2025-06-07 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 4043c7d4-c457-3c5c-b927-dfb56de07c02 | -7.7361 | -44.1823 | 2025-06-07 05:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6ab1e18e-7866-380e-8532-b221e39e6570 | -5.6379 | -43.7175 | 2025-06-07 05:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8d463340-6612-35ae-a77d-ef7710a6ce8a | -7.7364 | -44.1592 | 2025-06-07 05:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 143d3216-b7f8-3ee3-a73a-b54c4ffdfbb2 | -7.7176 | -44.1611 | 2025-06-07 05:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| a1ec9292-ac62-3f4c-a492-859aa4085c73 | -5.6379 | -43.7175 | 2025-06-07 05:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| f69604e4-e90d-3dc1-a237-3a1d8d07d579 | -7.7364 | -44.1592 | 2025-06-07 05:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 3bfdb601-811a-3327-91a7-a3eefb388ca0 | -7.7361 | -44.1823 | 2025-06-07 05:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 767637cf-409f-342c-a13b-d8713b9122e0 | -7.7176 | -44.1611 | 2025-06-07 05:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e26f692f-aafb-38a4-b915-48b1bce699f4 | -6.9602 | -42.9052 | 2025-06-07 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| bd307c4a-8831-341c-a9d1-86a8f35d1e21 | -3.05015 | -49.44101 | 2025-06-07 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a44a043f-0ebc-337e-bff5-408b3f6a860a | -3.04788 | -49.4391 | 2025-06-07 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6d1738cf-08c0-3738-9d41-b980960e494c | -3.05113 | -49.43433 | 2025-06-07 05:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f559029c-7dcc-305e-8c5e-394b3212165e | -10.49901 | -53.66554 | 2025-06-07 05:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 329e0dbc-c4a6-392c-8fa6-b40d8d7a0be7 | -10.50012 | -53.65631 | 2025-06-07 05:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 745022a9-4562-3b7b-9ed1-fa5adb77b438 | -7.89383 | -61.47509 | 2025-06-07 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 117e7869-7873-3211-b9e7-6de2409cb776 | -10.49846 | -53.6701 | 2025-06-07 05:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32b7f745-062c-3dc9-b222-d3d2a8ac606f | -9.24143 | -63.29329 | 2025-06-07 05:36:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ae428ca-93b4-3b42-970c-6f65ca1020a9 | -9.24585 | -63.28668 | 2025-06-07 05:36:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01741675-74ac-3647-9642-c2d47b3843e5 | -10.49956 | -53.66096 | 2025-06-07 05:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83e861d9-ce71-3348-8c97-42a1685a7ac7 | -9.36465 | -57.43874 | 2025-06-07 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5769a5c-c307-31fb-af7b-df67bf2c3c1c | -5.12294 | -56.11761 | 2025-06-07 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b44e5216-b52d-333c-a137-b12dc38758f6 | -10.49247 | -53.66906 | 2025-06-07 05:36:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d03b47e6-e2bb-34e3-ab6f-33010cf14776 | -9.36924 | -57.43943 | 2025-06-07 05:36:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a4f3404-5f70-34db-b857-58c7b5720679 | -7.73324 | -44.16761 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| c65db545-cab4-3b11-ae19-a890f718d20b | -7.01151 | -44.6062 | 2025-06-07 05:38:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| bb708c43-8144-3688-aa04-cccc74dd9c43 | -7.01019 | -44.615 | 2025-06-07 05:38:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ead44a3f-df21-3bfe-bcdd-3c81442497be | -5.63894 | -43.71867 | 2025-06-07 05:38:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| cbb64c35-6894-3764-84f1-6b914f07e802 | -6.95065 | -42.89823 | 2025-06-07 05:38:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 824ac564-a6f5-3f78-8955-c5f5accafcc5 | -5.64779 | -43.71997 | 2025-06-07 05:38:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6af71088-db70-38e8-8f2d-cabcbf13241b | -6.95843 | -42.90919 | 2025-06-07 05:38:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| d63c012e-7f8f-3d27-b759-f22ebebdf779 | -7.7421 | -44.16885 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0596e5e6-57c2-31a0-bb4f-cb755d5ab2eb | -6.59985 | -43.89378 | 2025-06-07 05:38:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6f5e4ad5-ff64-3628-bfe4-295216f514a5 | -5.77417 | -43.61673 | 2025-06-07 05:38:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 919cdd9f-e659-39c0-8467-1a9059a192e8 | -10.46334 | -47.95092 | 2025-06-07 05:38:00 | AQUA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0bdb2056-7d1b-381f-b922-e69f589de967 | -5.64727 | -43.60141 | 2025-06-07 05:38:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1b9d542b-a919-306b-9f6d-65670d9a5adb | -7.72572 | -44.15736 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 46677620-614b-3790-96d9-8d70884c2dc4 | -7.72439 | -44.16632 | 2025-06-07 05:38:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3ed59790-fb20-3436-b075-265e576cd1da | -6.94684 | -42.8032 | 2025-06-07 05:38:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |


[Clique aqui para ver as próximas entradas](README24.md)
