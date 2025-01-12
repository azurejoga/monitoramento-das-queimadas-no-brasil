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
| 02d07096-3598-36a9-ad5d-87e1e070f4a2 | 0.91323 | -60.38694 | 2025-01-12 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33cec562-a072-35fc-8a6c-f997f1517c4b | 0.55864 | -59.69411 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 1e24162f-a35e-3d81-af63-691f4ea43351 | 0.5578 | -59.68878 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 639594b2-6d0e-3ce6-96b0-a9cc35b48c5b | 0.91322 | -60.38792 | 2025-01-12 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c778d253-2ca8-303a-ac6b-be4eb946c390 | 0.61527 | -59.75168 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a503df2e-3c44-34bb-bd71-ccc663754e20 | 0.88843 | -59.37855 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e1701e9-7a67-331c-b448-0cb1feca3fb9 | 1.17786 | -60.5048 | 2025-01-12 06:12:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47997348-7576-397a-ba69-4a8979e42ae5 | 0.65933 | -59.65715 | 2025-01-12 06:12:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27614ffe-bf27-3f14-86d4-2a800ec33572 | 0.91399 | -60.39158 | 2025-01-12 06:12:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbdbc7f1-8d99-3a67-9d90-a9863af8dd5e | 0.5563 | -59.6885 | 2025-01-12 06:20:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3d77056d-2cf7-3a56-86ca-1369fbede93c | 0.5563 | -59.6885 | 2025-01-12 06:30:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 191f95c3-b75e-32d7-afbc-22b64a7ae9ab | 0.56757 | -59.69107 | 2025-01-12 06:54:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8e4d3e48-b48a-3a3d-b93a-009016f748e6 | 0.55395 | -59.69308 | 2025-01-12 06:54:00 | AQUA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 82972d9e-6192-322d-9900-c919315ae10b | 0.5563 | -59.6885 | 2025-01-12 07:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0f73ad1d-4f75-30c3-8c9a-074308d2949f | 0.5563 | -59.6885 | 2025-01-12 07:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 28dbae63-39b8-3898-a260-49ce3f12954d | 0.5563 | -59.7076 | 2025-01-12 07:40:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c06a8da2-3586-3e8e-a42b-808d1824d0e6 | 0.5563 | -59.6885 | 2025-01-12 07:50:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 65.9 |
| e3fdea69-123a-3837-8938-5e1cf36c34cb | 0.5563 | -59.6885 | 2025-01-12 08:00:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 17a327a2-dcf0-3df1-a114-c25b776033cc | 0.5563 | -59.6885 | 2025-01-12 08:10:00 | GOES-16 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a103f0ab-7204-359b-af70-c48e0d21520e | -3.1524 | -53.83241 | 2025-01-12 12:57:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 28f139b8-2991-3388-95ff-0d86f230177d | -19.64863 | -57.97046 | 2025-01-12 13:01:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.7 |
| d310b2f1-9feb-3def-ae2b-128451801682 | -19.66989 | -57.9625 | 2025-01-12 13:01:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| c276216f-7d3e-3696-bb35-56a3e67693f0 | -18.67612 | -51.87716 | 2025-01-12 13:01:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 08fe32db-83ab-38b2-956d-52a1144255dd | -19.77491 | -47.93393 | 2025-01-12 13:01:00 | TERRA_M-T | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 414db116-6c04-365a-8980-83ae58adafa0 | -20.35295 | -53.02525 | 2025-01-12 13:01:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3ff71cd6-c64f-32d6-936a-f967b21d17d8 | -17.69467 | -51.81272 | 2025-01-12 13:01:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0ed34a26-59d6-3ab9-98c6-d18ef94dd6bb | -21.47098 | -49.20697 | 2025-01-12 13:01:00 | TERRA_M-T | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| a8545720-3514-3d27-bc69-7194120d8937 | -20.35464 | -53.4218 | 2025-01-12 13:01:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b331cf24-8d0a-3cbc-8df4-b794d5baeece | -17.68353 | -51.82262 | 2025-01-12 13:01:00 | TERRA_M-T | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 707f7164-c5bb-3747-8a7b-212cdf595e9a | -20.4785 | -53.67176 | 2025-01-12 13:01:00 | TERRA_M-T | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fd983c01-6c12-31f8-b5d8-7d5faafa4ee9 | -17.53936 | -53.03747 | 2025-01-12 13:01:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f9ac91ba-8618-3ee0-acaa-686b873c0e29 | -16.39541 | -54.23428 | 2025-01-12 13:01:00 | TERRA_M-T | SÃO JOSÉ DO POVO | MATO GROSSO | Brasil | 5107297 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f8d6b71-c656-38c3-89fd-f1e819db9422 | -17.62683 | -52.17966 | 2025-01-12 13:01:00 | TERRA_M-T | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 12732a67-dfda-385b-8d4e-1a5e9a496d2e | -19.89511 | -53.29663 | 2025-01-12 13:01:00 | TERRA_M-T | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 479d603c-7844-3964-b9ec-d427e408df45 | -21.71768 | -56.10054 | 2025-01-12 13:01:00 | TERRA_M-T | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aac50b8c-325c-38f8-9ebd-90727321634a | -19.66808 | -57.9739 | 2025-01-12 13:01:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.3 |
| 9acf6d3c-2e36-35ee-a103-39a15f7b3c21 | -22.60485 | -48.7961 | 2025-01-12 13:01:00 | TERRA_M-T | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8c12565c-861b-39ad-a4ba-35ab4fdd0f60 | -29.03104 | -51.18087 | 2025-01-12 13:03:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 86bf32ab-e75f-3434-8c0a-db7ed16b5f09 | -28.73195 | -55.85062 | 2025-01-12 13:03:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 8.1 |
| 729967b8-fc47-3ee1-92b7-e0dccbb9ae74 | -24.79332 | -53.29428 | 2025-01-12 13:03:00 | TERRA_M-T | CORBÉLIA | PARANÁ | Brasil | 4106308 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 9e4f0f2e-d7fa-3917-b3b3-a39774338c76 | -28.97075 | -51.05915 | 2025-01-12 13:03:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 5522ff59-fdb6-3595-94ea-7faa3f8844c1 | -29.22816 | -51.3361 | 2025-01-12 13:03:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.7 |
| fbfc7336-3867-399a-8247-2ea0fd9ccfbc | -28.73337 | -55.84011 | 2025-01-12 13:03:00 | TERRA_M-T | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 10.2 |


