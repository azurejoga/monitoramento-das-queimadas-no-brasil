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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92db3624-4e96-3c1e-959c-8cbee1b894f4 | -14.40167 | -48.02195 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d37beecc-2f74-30ce-b99c-a1f99ce32d26 | -18.57745 | -50.58528 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e022c176-462e-38c5-a315-83e0c6361056 | -19.09966 | -46.4092 | 2025-10-12 04:17:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 18b275de-1fae-3438-bc9c-cd5c777e3883 | -17.94183 | -42.89777 | 2025-10-12 04:17:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| c23ab4ca-bd1d-30ad-bb11-005afd392663 | -17.21663 | -47.65403 | 2025-10-12 04:17:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc9ce56a-e72c-3b6a-8fe3-e6aef6895ba4 | -14.96448 | -46.72673 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 106d20d9-6c1d-3710-b478-8c350e30cfe0 | -18.04735 | -44.97313 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741b1715-bbac-3050-bc04-429d78c6d71d | -14.97056 | -46.7319 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 591bddee-838b-39ce-a280-8bdce6732025 | -15.67701 | -46.62392 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d602592-5911-3146-be0c-1737cc7840f2 | -19.52402 | -43.05184 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 741c6b0f-c9ef-352a-bf4e-e8fb5e5e292f | -14.75593 | -46.12884 | 2025-10-12 04:17:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d37a12f6-dc83-309f-a9f4-35baf109f91a | -19.76769 | -42.42251 | 2025-10-12 04:17:00 | NOAA-21 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2b9e6e28-a02e-3ac1-bd55-0ac717377146 | -18.58998 | -50.58223 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 83f3335f-8eac-3298-82cc-126026c2eb5f | -19.53115 | -43.053 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| bf2ba27f-9735-3acf-9f89-18ca3c1cb811 | -22.33135 | -49.86613 | 2025-10-12 04:17:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b4bf087b-e786-3c52-98bf-7db2a36c4a9f | -14.89914 | -48.50796 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94732f30-28b3-395f-b365-501e1a529651 | -13.87118 | -43.33335 | 2025-10-12 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 651ddafa-258c-3401-a775-d4fae2cd542a | -14.90578 | -48.49115 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 262d08e3-5557-3659-9f01-bc1ec6a287c9 | -14.94113 | -46.73406 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ed45102d-8f39-3ed5-bd16-6a710e72b840 | -16.34522 | -42.3875 | 2025-10-12 04:17:00 | NOAA-21 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0acad7b-e356-36a1-b298-b0e8c4d68e28 | -22.38669 | -50.00616 | 2025-10-12 04:17:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 86cfc108-653d-3826-99c1-ecbc6cee5194 | -14.02912 | -43.48575 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6fcd8d43-5dcb-3057-9025-746cc91f2dc2 | -17.89285 | -48.23488 | 2025-10-12 04:17:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b52607e7-0db7-3f4c-8846-c05ff930274c | -15.86299 | -56.75696 | 2025-10-12 04:17:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0dfdbf9b-8aa8-3aaf-ba94-8b6d5c8098a2 | -19.78249 | -42.39666 | 2025-10-12 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| eb8b26c6-3b56-355f-9835-17c5e7cb8cb4 | -17.36403 | -46.65809 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fbecbd9-1432-3569-9afd-a37d0abbecc7 | -14.94328 | -46.74217 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eee31463-8919-3351-8003-a40efe26524c | -22.33559 | -49.86275 | 2025-10-12 04:17:00 | NOAA-21 | VERA CRUZ | SÃO PAULO | Brasil | 3556602 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 07596d91-f7d8-3aaf-a851-519a078ead4c | -16.50727 | -49.0429 | 2025-10-12 04:17:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 304a867c-23b6-3e5a-b053-4d6526f9a860 | -14.90009 | -48.48092 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4010fef9-55c4-30aa-9a05-3894cdec5b72 | -14.86798 | -48.4901 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4ddbae4-4242-38dc-b284-53168902b84e | -14.40454 | -47.98283 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7cd02075-cacd-391e-ad6c-90e49419c997 | -17.40908 | -46.86618 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efe70224-1577-36a2-8074-d103151714cc | -18.36365 | -43.43535 | 2025-10-12 04:17:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66ebe328-0d8e-385e-bf35-745527c19bc0 | -14.0185 | -43.48782 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54827cd1-4a84-3629-9b3e-4872f17fce61 | -18.05011 | -44.97733 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4779b356-ada6-35f4-abee-de0510eb47bb | -15.67406 | -46.64206 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cc92060-f953-3348-b6e1-57b9a7b3c79a | -18.57466 | -50.60057 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 15dfa2d6-82bc-3aa9-8615-09bba35781be | -19.09578 | -46.41226 | 2025-10-12 04:17:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0985dcf0-9af0-3da2-a9c3-65bb96fd1fd5 | -17.1874 | -46.95255 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53197ab6-b9e4-37fe-9889-c146bed8d500 | -14.42026 | -47.95079 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9aa957d-57d3-3190-9534-d421d06a58e8 | -14.4024 | -48.01756 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 6b94bbc0-1bc0-3fd7-8041-c621e735595b | -13.56292 | -43.42058 | 2025-10-12 04:17:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e5d9628-55f3-377c-b2ad-da79bdffe5cb | -15.22439 | -46.3878 | 2025-10-12 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a79474a8-e0d1-320f-b912-a083710471ef | -19.53474 | -43.05346 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 624706c4-e834-36b3-ab1f-637e6e65fdb9 | -15.60764 | -42.33948 | 2025-10-12 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9190d9da-aa4f-3dc6-99f1-01ce2154087a | -14.35965 | -42.24483 | 2025-10-12 04:17:00 | NOAA-21 | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f3634586-e8e9-3186-86ea-da8b19db891f | -18.57562 | -50.59528 | 2025-10-12 04:17:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9db3a3c2-ac27-3879-917d-9380f00a23ed | -17.25059 | -52.27168 | 2025-10-12 04:17:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a7bd8feb-2610-39f7-8ce5-e5686c0ea4df | -15.22813 | -56.86434 | 2025-10-12 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98bfcf33-b7f3-30b5-9187-0bfecdca6450 | -17.87262 | -45.02604 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7b54fec0-f793-3de7-aa0f-e16ae74fee9c | -19.53691 | -43.05652 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b24366a6-54ca-3820-a0cf-30d785e6cc17 | -19.51452 | -43.04153 | 2025-10-12 04:17:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bad83ce4-b29b-30b0-98b2-defd4658b7ea | -14.40031 | -48.00813 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ae14396-7dd5-37a8-ad5d-aab9dd35d76d | -15.2881 | -57.09239 | 2025-10-12 04:17:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e160b8a1-90ca-33dd-8e20-1adadbcb5882 | -15.68038 | -46.62443 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 864b3640-615b-37f3-b8cb-d5c2ad1b1a09 | -14.90655 | -48.48675 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03e853e3-0634-35ec-893b-d40884438f1f | -14.22884 | -45.7439 | 2025-10-12 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d526399-b37e-3cb9-a831-45da1695f7bb | -17.55822 | -46.51154 | 2025-10-12 04:17:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 50913b1e-2bbb-33b4-b5a1-b1c4074fc888 | -14.96474 | -46.74612 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 858ab987-f594-3992-926a-d259cb5a03e0 | -14.3953 | -48.01613 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7f5eb948-7b0b-36d7-bb93-7207a2fd2c4b | -18.07979 | -45.02672 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dca53364-233f-3eaa-b466-16dd4e8c50fa | -14.902 | -48.51303 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e2d3e80-c3dc-31cc-85b9-ae7fb2db3fad | -17.25749 | -46.89606 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68e3b623-7aec-3725-a435-6149f3e49c9d | -15.66085 | -43.90271 | 2025-10-12 04:17:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c43feb2d-7777-3ea2-9ed6-d3fbd55fce3e | -14.90483 | -48.51831 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0eb8bb6-51ab-3ea6-acfa-f916b81f10db | -14.96172 | -46.72241 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 1618ccc2-4491-3e74-8785-1495a323ba19 | -15.23327 | -56.86995 | 2025-10-12 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ecfe18bf-182e-3250-a44d-702e7aafc159 | -14.5636 | -47.31834 | 2025-10-12 04:17:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b62ac4f5-e18c-3af8-a396-9ca59e2f86d7 | -14.86724 | -48.49445 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c703d893-9304-3451-9753-794e43060498 | -14.01905 | -43.48416 | 2025-10-12 04:17:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fa9dc60a-3651-392a-b9b0-1ec41f738b11 | -11.85142 | -56.86859 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6855c4e5-303f-3b13-8ae8-853f857e1a11 | -18.40461 | -46.39294 | 2025-10-12 04:17:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a207d917-6462-3496-b9c9-38e8e3cd8bfa | -11.85901 | -56.86643 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| deac7c17-ab95-3db6-af57-b9eccfb1c4f3 | -15.15583 | -56.81431 | 2025-10-12 04:17:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 22668592-79e4-390a-84fb-8b18d22a59f6 | -14.41365 | -47.95021 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a68f4a9-e577-3684-87b4-c23ca7cb71ff | -14.95094 | -46.72457 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8a4f8e45-2d9a-34e4-bee5-9c82ae85d049 | -15.50279 | -47.99948 | 2025-10-12 04:17:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c92c34b1-af81-3474-afa7-ef98da985b2c | -14.94969 | -46.72405 | 2025-10-12 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3caf8217-89ef-3c87-955f-baa3833853e2 | -17.19349 | -46.95744 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a39d75e6-c980-3e5f-8864-fe4d93a98afe | -11.85146 | -56.8704 | 2025-10-12 04:17:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 347d032c-474c-3f2a-94f8-5881be7b8ad5 | -13.41682 | -43.6899 | 2025-10-12 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84f66822-6042-39ee-8702-3a860441511e | -19.78682 | -42.39256 | 2025-10-12 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5f35d9d-9df4-3701-98f4-2a35504f0ecf | -14.1646 | -42.53461 | 2025-10-12 04:17:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5bf3696f-5b32-3baa-98c0-c77e7c6df0dd | -17.40968 | -46.8625 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4adcc11f-0667-3cf8-be6d-f2bdfee812dd | -14.99911 | -53.88625 | 2025-10-12 04:17:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71bc31f3-8647-304e-9cd6-959a933936e2 | -13.67824 | -43.05331 | 2025-10-12 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 740b1d03-ffe1-35ed-a636-4d1e20762693 | -18.04292 | -44.97987 | 2025-10-12 04:17:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4950725b-02f3-369a-bbd2-a349e26830ec | -15.28916 | -57.08734 | 2025-10-12 04:17:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64941748-c0d6-378d-80ed-97a28693a283 | -19.52919 | -43.05968 | 2025-10-12 04:17:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4622f8ab-14c4-3849-a3c2-3d8c5b8af6bc | -12.24372 | -45.34014 | 2025-10-12 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c30f58f-076a-3ee5-9d24-35222672ee96 | -14.4167 | -47.95016 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55c29fea-5ef8-3ffd-84f2-ea11f6145c61 | -17.4036 | -46.85759 | 2025-10-12 04:17:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9a3996a6-b900-3a82-b4ad-b75b5443c834 | -18.0831 | -45.02728 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19245bee-4e5c-31c5-9940-2c89d6899a86 | -15.46074 | -55.94437 | 2025-10-12 04:17:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1429466d-ea8a-38b0-868e-7ebd1eb66e62 | -14.86807 | -48.49308 | 2025-10-12 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19fbe04a-5f62-3d5e-a9f7-0e125ba9f28f | -15.67188 | -46.63427 | 2025-10-12 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be1f766e-fceb-3b5d-ac31-333518db1899 | -18.07923 | -45.03036 | 2025-10-12 04:17:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 845bc8e9-f146-3096-b4f6-552ced6eb624 | -14.0208 | -47.07408 | 2025-10-12 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b85e7c75-ff50-31fd-b262-1c188dcdda26 | -12.13499 | -45.59328 | 2025-10-12 04:17:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README23.md)
