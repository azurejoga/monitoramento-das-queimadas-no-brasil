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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca81b47c-fd00-3537-8d99-0277d72c55c0 | -15.58057 | -54.75192 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af7f8202-c80d-3cd8-ace3-4ac1ed32bb87 | -17.54467 | -44.54818 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6410dcb3-98c0-3439-b6dd-e7209b54d431 | -17.28333 | -47.23899 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b320985b-24e6-3dd3-94e7-a58002f41ca1 | -15.10403 | -52.506 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68b5a40e-99ec-350c-bf74-57f0ecdc757a | -15.15747 | -52.39854 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d8e303fb-afe0-3526-afb1-3122c4dd4177 | -17.28709 | -46.09639 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7004513f-1722-3968-846f-119b10e7b126 | -20.64502 | -48.69033 | 2025-09-13 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5266ef07-87da-3e67-ad6b-1a20d4fcc13d | -20.6487 | -48.6911 | 2025-09-13 04:10:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e049807-1158-3284-98ba-4f8a0817cd34 | -16.4092 | -49.03984 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf2c506f-d40f-371c-a330-ebe21a711f75 | -17.27386 | -47.25069 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a773e50c-c6aa-315d-aabe-3ebb4d0beeb9 | -15.21332 | -56.68998 | 2025-09-13 04:10:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 64479616-ae55-3233-b6cd-b3e6f8760aec | -16.55781 | -49.23373 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e3187f3-0c5d-3f5a-acf3-58ab54cc2ef2 | -16.41067 | -49.23557 | 2025-09-13 04:10:00 | NOAA-20 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48d7070f-c0b0-3f85-a530-aba8b1c63e61 | -22.79462 | -47.7981 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9adb71b-d94e-347a-b01b-7706acc6b0b1 | -15.06001 | -50.15751 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6f63768-60ce-32a8-8f30-18dbbd69427e | -18.76969 | -48.55049 | 2025-09-13 04:10:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2465834a-1c24-34b8-a3ae-cc5cadaddade | -18.00207 | -46.92897 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38d20fbe-e05a-333e-b474-ac52db1aad1b | -16.56923 | -49.31014 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 198868a8-14e2-32c0-9b86-5c8f0dbe7005 | -20.55159 | -45.8309 | 2025-09-13 04:10:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9ca4099-3792-3aca-8d1e-0c7ceecf0fea | -16.35989 | -51.51424 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 386484f5-56ef-35a3-b3ac-63b6b4fc9212 | -20.28823 | -46.58644 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf41f4f1-d7b9-3a89-98bb-5d08c4d4fa87 | -15.59622 | -54.76501 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67c1304c-f245-359f-b9a0-f30a8c82c751 | -18.60276 | -47.19271 | 2025-09-13 04:10:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a40b6e5d-88ec-3c1a-b488-250df1683a42 | -17.41167 | -48.22382 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a22869b6-1eb9-33a1-9b5a-4284748e15ea | -15.15801 | -52.47641 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb0dc4a9-9afb-3353-bd24-47068f2db662 | -17.28167 | -46.10761 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5d8c5a2a-9796-3feb-a07b-44e0fb19bfd1 | -20.60363 | -50.40401 | 2025-09-13 04:10:00 | NOAA-20 | GENERAL SALGADO | SÃO PAULO | Brasil | 3516903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0bd06fa5-f687-34ee-98b2-821c5c37af0f | -17.91613 | -44.45515 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b244f803-1200-3ee4-be6e-bfcbc0f1bad3 | -15.10468 | -52.5028 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba0b70a6-2515-3b85-9042-a4f8e4b51b41 | -18.85482 | -46.84147 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eed9bf19-1f24-3479-8943-c83786783455 | -15.17437 | -52.31322 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2540bf54-ac97-3222-b420-81817921294f | -16.53167 | -51.74635 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c5f36d6-3f8d-313e-88ce-f83786a53801 | -17.54409 | -44.5518 | 2025-09-13 04:10:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1b832df-02f4-372f-bc5a-463728ab6383 | -17.79112 | -51.73294 | 2025-09-13 04:10:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6b1e84a-b03d-3784-9881-aa4fbeb8c902 | -18.47074 | -39.76099 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 30d5443c-3738-3165-930b-2465702cc1ab | -22.22947 | -48.59983 | 2025-09-13 04:10:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c2cbfaf2-05ad-3740-b28c-64f9c556bbd0 | -16.06783 | -50.00387 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 073a1779-f367-3567-aad4-5e56f77454af | -18.18194 | -45.20924 | 2025-09-13 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d63fd3ea-63c8-351d-8ea7-5a55f36a1da1 | -17.41994 | -49.26033 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f2b1bb0-6d2e-311b-8913-d9860bc65282 | -15.5884 | -54.77318 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab181574-2f71-36ec-a343-43fccb74908f | -18.15836 | -49.19078 | 2025-09-13 04:10:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 21.6 |
| 2a09275a-d4eb-3eab-8e70-1cd0247c9353 | -16.92965 | -51.88557 | 2025-09-13 04:10:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 804a2bf3-8f9e-34f8-b927-0a01e349f33b | -18.47515 | -42.05408 | 2025-09-13 04:10:00 | NOAA-20 | MARILAC | MINAS GERAIS | Brasil | 3140100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a3954146-bf6f-363e-852c-ee18adc111ee | -15.11493 | -52.50501 | 2025-09-13 04:10:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afd33647-cff2-31e8-bfe8-dd15c6f591f6 | -20.37458 | -50.12785 | 2025-09-13 04:10:00 | NOAA-20 | MERIDIANO | SÃO PAULO | Brasil | 3529609 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2ada860-59c2-332b-8469-e4397a6d56c4 | -19.63059 | -43.73392 | 2025-09-13 04:10:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 268f924a-4ef6-33f9-b7f8-08e8573d013d | -16.25536 | -50.07011 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a14e6a8b-9cab-3d31-ab78-9d1d08db5db8 | -22.79809 | -47.79876 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3764d2d8-a2cd-3d77-9e76-2efcac42032b | -20.29439 | -46.59155 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c5ae756-08b4-3c19-86e9-a919b578b41f | -19.98163 | -46.92419 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55f1d324-bb79-3b25-8ebb-070030c6220b | -15.12133 | -52.49973 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7eb8b269-bf41-3331-a021-8b0a30e8406a | -16.43921 | -45.68761 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7a81ef3-d150-3f47-95e5-70c8faf99a28 | -18.89185 | -47.05335 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90ae6ca3-b3af-3e09-93d5-c854d92fea40 | -16.25624 | -50.06545 | 2025-09-13 04:10:00 | NOAA-20 | AMERICANO DO BRASIL | GOIÁS | Brasil | 5200852 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 632a2969-9e89-3d51-8439-05aa539db3a1 | -17.2851 | -46.10823 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 85f492ff-0f80-3057-a581-6e4517e73e13 | -20.38888 | -45.53725 | 2025-09-13 04:10:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c4d8f3e-92f3-3ba8-b451-d57fcd83fec7 | -16.50101 | -55.15741 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 38a7ae49-f43a-32fc-873a-44ef892b593f | -20.54539 | -45.83382 | 2025-09-13 04:10:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 714d302b-1ef3-304b-b068-513c02e2536d | -15.07899 | -52.49755 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85097d68-13ca-331e-aa5a-398c15d728a9 | -15.5386 | -47.94814 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d419f763-7bdc-3171-bb6d-87b85fde98b1 | -15.68718 | -49.90138 | 2025-09-13 04:10:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 716c952f-285e-31c1-9295-b922284471a1 | -15.59064 | -54.7537 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7a5876d2-1e99-3e28-b4af-0cf974dcd6ef | -22.18266 | -49.6128 | 2025-09-13 04:10:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5d67f088-d192-3a6f-97db-25fea40fcd75 | -14.62491 | -52.08788 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cf45c74-0866-3608-8756-df1ea35b8375 | -14.6376 | -52.09565 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43be4f1a-ce4a-37a4-ba6c-f3dd7ec463c1 | -20.59855 | -44.90708 | 2025-09-13 04:10:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7cac613b-6a68-303f-9908-5bf50dc3bdaf | -17.83389 | -50.41099 | 2025-09-13 04:10:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27b2cf85-fdba-342b-8ff0-5ea35a7a60aa | -21.61487 | -46.80175 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| ff5cf9ee-cd6f-3b65-b6fc-1b8e3ff64a5d | -17.40789 | -48.22314 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ae77142-e832-35af-84d5-a23c2a4f3bb9 | -16.52738 | -51.74119 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a601c37-5f51-3d15-9e69-0fbff7737f72 | -15.16329 | -52.47664 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf9c8573-81ba-3936-9c82-4f487f3c51b7 | -20.00198 | -47.64919 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98f14c7b-3349-326f-9b66-a241836f9c21 | -20.55554 | -45.82779 | 2025-09-13 04:10:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 790e703f-78cc-388c-848f-852f28b5c6f3 | -17.29958 | -48.74362 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 913ccb6a-1862-3454-a52e-f23dba8e39ed | -17.31215 | -48.74082 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b396a7b7-e852-3f78-b1d3-d999a0d1b44c | -15.11451 | -52.48047 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b0ea81c1-3b48-3cb4-8df7-c0cb93ae0227 | -22.22789 | -48.60872 | 2025-09-13 04:10:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3ce90ca2-6445-374e-b110-541e34e61251 | -17.35104 | -42.63051 | 2025-09-13 04:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1d7836e3-b085-30d4-a864-bccdb9fc4187 | -16.87716 | -49.34241 | 2025-09-13 04:10:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f214a8b-78b9-3aab-ab79-a69f0703e66f | -18.06514 | -45.44822 | 2025-09-13 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e753c6a-4694-342c-8952-e07838bc9c0d | -15.12252 | -52.46714 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f2b079e-59a9-3739-82ae-32d8de41bdfd | -19.62027 | -46.6953 | 2025-09-13 04:10:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af559943-7a47-3d3b-b07d-7fd39009324c | -16.43252 | -49.04865 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bd92293-b9e1-3d05-9b2d-f5e0236c7166 | -20.09344 | -46.90681 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11349f28-a92a-3bbc-a230-123a3e907e3d | -16.60784 | -49.46283 | 2025-09-13 04:10:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2b09cbc7-340d-3569-a2e9-9d942c910f46 | -15.15248 | -50.12226 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf099af2-3915-3887-be32-f3a0c37c60b7 | -17.43109 | -49.22185 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee9f3136-2b37-33f1-a234-a3704fbe72fa | -21.58064 | -48.4225 | 2025-09-13 04:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 354546ac-90d9-30d4-bf3c-3e8677d523a9 | -18.59353 | -46.55186 | 2025-09-13 04:10:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e2a55de-39d0-392e-b6d0-1601513b5926 | -16.36446 | -51.53625 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57964b42-2854-3551-8b62-0ce77c3d6c83 | -20.61617 | -50.22522 | 2025-09-13 04:10:00 | NOAA-20 | MAGDA | SÃO PAULO | Brasil | 3528304 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7cbb6eb9-8efb-3bb0-a68a-0efc25846773 | -15.76329 | -53.50008 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fad6f4a2-dc48-351a-a629-146774de0ad0 | -17.12497 | -48.47975 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b3bc759-321d-3ac7-ad8c-7eee248e26f1 | -15.07025 | -52.47983 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1689695-ddae-3061-9c5b-38c81a6a4891 | -15.16147 | -50.14727 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9792f8bc-eee3-33ce-86e2-a09fc6064e09 | -18.412 | -49.41022 | 2025-09-13 04:10:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cddc394c-e440-3355-a712-cbdddb241abf | -17.83546 | -50.40268 | 2025-09-13 04:10:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9e58018b-f85d-3f40-969b-10b9aef7c28a | -17.24773 | -43.87198 | 2025-09-13 04:10:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 462f360b-8615-3fa5-9f06-77f2cd0a428e | -17.42319 | -49.2425 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af1402df-4c4a-3056-a4e6-ce3142a45bd1 | -17.76978 | -42.16968 | 2025-09-13 04:10:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README68.md)
