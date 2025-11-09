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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50dec75e-8688-3413-992b-04aee625f305 | -4.12356 | -47.294 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| be3c6f7b-4e81-3651-8dbc-0e16493dbe53 | -5.32422 | -44.83536 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e8aed9d-784f-3b84-8d55-b15f1ec2980f | -4.52286 | -48.83875 | 2025-11-09 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c919fd27-357d-3b6d-9ed9-cbb46638b189 | -6.55485 | -39.49175 | 2025-11-09 03:49:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a816e65-c853-3092-8f02-692bcdf16462 | -4.90982 | -44.64669 | 2025-11-09 03:49:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d78e857-99b5-30fd-95a7-73bfb2ed9528 | -5.48951 | -45.86417 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9a1e5cb-7eaf-31f1-a97e-552011d5dbda | -5.65555 | -45.98702 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 91ced243-364c-39ed-96df-e70945d8ecbe | -5.94767 | -46.65088 | 2025-11-09 03:49:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 931b44d3-b4e6-3e1b-a418-a1fcd8f62410 | -9.47533 | -48.74158 | 2025-11-09 03:49:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b80db64f-ec71-3c7e-8e7a-83c8c8e2e1b3 | -4.6335 | -46.3952 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1960ef37-2d43-342f-8e8a-88047c4cd1cc | -4.32674 | -49.76221 | 2025-11-09 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9bc54463-f031-3ee4-aa97-916638d39026 | -16.70175 | -41.51953 | 2025-11-09 03:49:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8c25d087-913e-3e9d-823b-7b63fccf5d61 | -4.39743 | -45.16235 | 2025-11-09 03:49:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b98683df-1db1-3126-bf31-9e66cfbbe91f | -5.80706 | -41.34336 | 2025-11-09 03:49:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0e590009-2145-3250-8231-a5590b7dc940 | -5.38379 | -44.73217 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd24f9d7-a66c-3bb1-b2de-43f0e8062fc0 | -5.30489 | -47.28618 | 2025-11-09 03:49:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1cfffb5a-d09a-3a28-8c26-e1964c4d3293 | -3.8118 | -45.99045 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 62f51283-6fc1-3c18-a8e4-952a9da1f749 | -5.37181 | -44.62213 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc9cc6e7-0e4c-34f2-aec1-a6a0aaad7a2c | -5.84599 | -46.45124 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1b730ee0-ba4a-3109-bee3-97f6e039df61 | -7.27389 | -38.72474 | 2025-11-09 03:49:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25e1a1b3-e7b3-3a3b-a9f9-9c9baabf5e6b | -4.24198 | -44.67111 | 2025-11-09 03:49:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0569023a-e128-33c2-9244-4f51bba70f90 | -5.1391 | -45.71765 | 2025-11-09 03:49:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e27ff848-e865-3d76-bf53-379419871631 | -10.71948 | -47.73905 | 2025-11-09 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb12b847-4664-3369-b9b5-cb8589f0436f | -4.45656 | -44.64825 | 2025-11-09 03:49:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2302ce58-1a1e-36c8-a6be-855e6f98bce7 | -4.70675 | -44.41441 | 2025-11-09 03:49:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 34b5ee4a-63ff-334c-b53f-65c1f0f86c05 | -6.28745 | -38.87531 | 2025-11-09 03:49:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 763b7b02-5b3d-330d-b0b9-90c1e1fe1ba7 | -5.30614 | -39.79957 | 2025-11-09 03:49:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0013136-8776-3f87-a18b-2469676584c7 | -4.40115 | -49.6707 | 2025-11-09 03:49:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d44d5783-87af-3ca8-887a-3b9be4f0cf97 | -6.71522 | -39.9981 | 2025-11-09 03:49:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3f1fac5f-b5e4-39c1-8ff0-ccf20bd8a105 | -10.33503 | -49.63451 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 1743626d-df7f-3f87-909b-618a5a1edcdf | -5.89569 | -43.96078 | 2025-11-09 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f369147-b512-34b2-84a8-1f9105cec370 | -6.72354 | -38.54337 | 2025-11-09 03:49:00 | NOAA-21 | SANTA HELENA | PARAÍBA | Brasil | 2513307 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 203c3c57-76ce-3b07-b65f-3ebdf2dc1bf6 | -3.80552 | -45.99339 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b895d371-a9d7-373e-940f-0ddb9d815119 | -5.60948 | -39.54855 | 2025-11-09 03:49:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c23172e-b29d-34f2-b400-988baba0b831 | -3.86332 | -49.38055 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51bf2abe-977e-31f9-ab80-37c20d34e9ef | -5.28525 | -44.95281 | 2025-11-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b8de8d52-3f35-31ae-b968-a59e5888d1a9 | -5.65448 | -45.98693 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7b4afda-5e57-35d4-945e-e00c77dfb573 | -4.62908 | -46.39797 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 51680762-f6b1-377e-b863-6c653975c680 | -4.25265 | -48.63173 | 2025-11-09 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 794f48a3-c9f1-3392-a774-e864a7463296 | -4.63414 | -46.40256 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d69d0f46-0867-3f67-9823-92c09ec8e64d | -4.62976 | -46.39409 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 859650a0-8134-3212-8616-d923acae1161 | -5.63537 | -43.2583 | 2025-11-09 03:49:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1788052-3c77-3aab-83e6-61a131c96430 | -4.38927 | -45.95434 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d0d15c0-c1be-3890-89bd-6fd36fd47706 | -4.39246 | -45.96891 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68a315a6-6134-394e-8fba-09dce7e7321a | -6.21223 | -39.67752 | 2025-11-09 03:49:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aef3e87b-9e0c-36f8-9eff-06d69cb26bc2 | -6.70299 | -39.67679 | 2025-11-09 03:49:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd84f4a3-9d30-3fcd-86a7-bc0f9aafd383 | -10.34034 | -49.641 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 0565c6be-a164-3c6a-9a51-ea561220f7b7 | -4.71292 | -46.45682 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da91dced-779e-3c86-a7d8-029d49b805f1 | -4.20828 | -47.78187 | 2025-11-09 03:49:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ceaabf8-8ea1-3f34-9560-7cfb80c6830a | -3.8099 | -46.00183 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b808bd4-0e0d-337b-8e6c-1912dbc52654 | -3.87021 | -49.38189 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b9029e1-311a-3654-b069-c0c3e93fcfb6 | -6.01947 | -43.77571 | 2025-11-09 03:49:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 129ef54e-bdfa-3f75-a79e-3e6868b010e8 | -3.85154 | -47.40332 | 2025-11-09 03:49:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f787ebe-6c19-3f96-af20-68cbd0a0c654 | -5.06338 | -40.47268 | 2025-11-09 03:49:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 68ace545-a7ea-3fc8-a217-7f4fda242643 | -5.37232 | -44.61921 | 2025-11-09 03:49:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0965f319-205f-394d-9fd2-454740d5fe86 | -6.43329 | -39.70239 | 2025-11-09 03:49:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4700ba65-0003-3cdb-9394-12430ce72d05 | -10.34237 | -49.63065 | 2025-11-09 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 37eca63d-b450-3935-9d20-16c6c9aa445d | -3.46387 | -48.82327 | 2025-11-09 03:49:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed74f696-1a6b-3559-8f80-2bcaaf56fef5 | -4.58231 | -45.62445 | 2025-11-09 03:49:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc66728f-9f9b-301f-baa9-3a6b2f48aead | -3.32427 | -49.13074 | 2025-11-09 03:49:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3070ed6b-26ae-3dd5-97b6-951667e5f3ee | -5.39815 | -47.26168 | 2025-11-09 03:49:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d99711f9-f1b4-311f-833f-b8c0586af871 | -5.3104 | -44.20802 | 2025-11-09 03:49:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15889e0f-8d27-33a9-abf3-ee63be81dbf7 | -4.39866 | -45.96621 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e2e6c284-9fd7-3e43-b99c-eb5a76975fa1 | -5.28068 | -44.94867 | 2025-11-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1241b479-d7db-36e1-a0ad-cfc3a5bac925 | -4.24248 | -44.66808 | 2025-11-09 03:49:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cefbf162-3a14-3b75-8784-f6083e7e9b1f | -11.93905 | -40.35645 | 2025-11-09 03:49:00 | NOAA-21 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 19f0bd71-41ae-3906-bd33-f92ddb96942b | -5.32045 | -44.50109 | 2025-11-09 03:49:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f1479588-f265-3bc8-82ef-4ac297326198 | -3.79763 | -48.90393 | 2025-11-09 03:49:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| de6e70d1-cb4e-30fb-bb6d-3a61d2f91071 | -3.81116 | -45.99431 | 2025-11-09 03:49:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1f61fc72-4883-3a98-8003-028d88e1123d | -4.5193 | -45.72413 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e96ff83-9154-3659-b83f-fd7dbeb37043 | -5.09546 | -37.78568 | 2025-11-09 03:49:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| da4cea8e-544f-33ad-b488-8c88b8647beb | -4.40269 | -44.08205 | 2025-11-09 03:49:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6637a0db-7366-38e1-8c41-78bc2352c58c | -12.15412 | -48.00726 | 2025-11-09 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7cf893ec-217c-32fc-a092-1c7dded26902 | -5.1385 | -45.72112 | 2025-11-09 03:49:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 68131db3-97c7-3bf2-9f8e-7362c8a6bdbd | -4.52387 | -48.83314 | 2025-11-09 03:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a54a9398-2312-35ad-80f1-968fa8589bf1 | -5.28473 | -44.95593 | 2025-11-09 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7ebc9c0a-cf55-3d32-922c-06f997f19226 | -4.8343 | -45.44601 | 2025-11-09 03:49:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42bd2076-061a-3660-8121-cd1972ca905b | -4.32534 | -45.70084 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f3c3da1-febf-3149-8a90-abe7134d66b3 | -6.56515 | -38.69674 | 2025-11-09 03:49:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 103bc2fe-15eb-38df-b495-6a6ae4864396 | -4.12222 | -47.29593 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8db469dd-514f-34ff-abd9-8120c7ba8974 | -10.71874 | -47.74294 | 2025-11-09 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5cc7fa1-b7cd-3c87-a44e-81763b28b890 | -4.20604 | -44.7597 | 2025-11-09 03:49:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fd313c9-719c-38ad-8bca-cb511a19c0a0 | -4.3778 | -45.49408 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ab867416-e85d-3597-8156-9a7235383806 | -4.18308 | -45.73675 | 2025-11-09 03:49:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1e52b94-0440-3649-b44b-cf5647702925 | -4.123 | -47.29136 | 2025-11-09 03:49:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5ee34de1-c874-388b-8776-bb82e1ff4e96 | -9.47441 | -48.74648 | 2025-11-09 03:49:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d2ce35d-687a-3a72-8c39-88e61aa21319 | -10.42023 | -48.80689 | 2025-11-09 03:49:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b65e6033-4b60-321a-94fa-27a8b245d0a4 | -4.46931 | -46.451 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6995de5f-648a-31ab-a177-a35b4a1d4bb4 | -4.63552 | -46.39472 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 10d78c55-f11b-3594-8dfc-92d8e940081f | -6.95845 | -40.25295 | 2025-11-09 03:49:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66759147-b104-39e7-b392-005782bd092f | -5.89477 | -43.96599 | 2025-11-09 03:49:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0066c9ba-fc6b-39e2-bdaf-556a99c0bf56 | -4.79899 | -46.01279 | 2025-11-09 03:49:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83ecc51d-3793-3426-be6e-789ddfd8f3fb | -3.86207 | -49.38485 | 2025-11-09 03:49:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 36a53f94-1c02-33a9-85bf-432ce32f96f0 | -6.28684 | -38.87913 | 2025-11-09 03:49:00 | NOAA-21 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46784e25-40ba-36e7-93fc-32c42919be46 | -4.64126 | -46.39547 | 2025-11-09 03:49:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24dc6245-48fe-3511-b6ed-937912c62390 | -12.53833 | -39.55146 | 2025-11-09 03:49:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0a4e353e-b953-3630-a318-cc9ef458be6c | -5.49015 | -45.86057 | 2025-11-09 03:49:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65594e28-5138-3136-b4e1-d42093de95a4 | -11.94183 | -49.1767 | 2025-11-09 03:49:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc0baf64-6ff4-3db0-9e15-d6489791db62 | -4.45198 | -44.6444 | 2025-11-09 03:49:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aca9c53f-0c3c-3678-915e-7fa0fc6add37 | -4.32659 | -45.69365 | 2025-11-09 03:49:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README11.md)
