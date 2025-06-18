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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59cac214-eb45-3bd9-86cb-4c1e1262e461 | -18.38241 | -44.50575 | 2025-06-18 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559b38c5-27e5-3a1a-aac1-31fd0c7dbe71 | -18.38145 | -44.51097 | 2025-06-18 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba1bdff0-9d3a-3507-b1cf-291ff5ad9c94 | -14.43912 | -48.90698 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 21067783-de7d-3bea-9b32-892da7815bd1 | -16.78713 | -49.11356 | 2025-06-18 03:51:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ae03351-27ad-398d-a280-2353cd83ece5 | -20.92268 | -49.096 | 2025-06-18 03:51:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 74494935-9f69-356a-9cda-4fcf1469ea7c | -16.09554 | -42.28799 | 2025-06-18 03:51:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78b56490-2e8f-3630-beca-2f913576b3a5 | -17.67847 | -42.73949 | 2025-06-18 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b20d1e52-8d48-3868-afb3-07830f76b451 | -18.99934 | -52.08356 | 2025-06-18 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14159e23-258d-35b7-b09e-2c9a8bdd5d90 | -17.8406 | -45.98068 | 2025-06-18 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d20e3ea-5eb7-3772-b01b-4d42a3aef120 | -20.98932 | -47.39191 | 2025-06-18 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a460c3ce-1081-384b-8ddf-f2bf09d5334c | -14.43208 | -48.91328 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fcd1d58-fa0b-3880-94d4-4bee7c593294 | -22.36264 | -45.17595 | 2025-06-18 03:51:00 | NOAA-21 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 58af61a8-9e7a-3a2c-8b40-9ae6c7e2f089 | -17.7825 | -42.81085 | 2025-06-18 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 306179d7-9b53-3c2c-bf61-7ba888082dba | -14.43837 | -48.91074 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 210d3ea0-035a-3ea1-a9ce-8e6b320eb5f7 | -22.31826 | -43.89286 | 2025-06-18 03:51:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 12ea7bf1-d1f6-311b-bff8-23fb392fe01d | -14.4369 | -48.9118 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c02b357f-ca4a-3c83-a56d-6407dfb75039 | -15.38039 | -47.69415 | 2025-06-18 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fac17906-a025-3440-a1ed-3ff94e8f0771 | -14.43768 | -48.90804 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1ef30f28-343b-3b15-a3d0-d7a2e9201dd5 | -17.67642 | -42.74075 | 2025-06-18 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 765bbac6-0402-39b6-a8c3-0450377e4d57 | -16.65559 | -45.49642 | 2025-06-18 03:51:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b64b0cb9-a2e8-3ed4-b7da-a36f2c353203 | -19.47823 | -49.2939 | 2025-06-18 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe0cc42e-e1d2-32fe-bc8e-768a039c6d97 | -19.47892 | -49.2906 | 2025-06-18 03:51:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 444a3a04-9f01-3d37-be0a-9f15d6b23b7c | -16.58932 | -49.21634 | 2025-06-18 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05ca75f9-9c93-33d9-9f8c-d4b550c1d096 | -14.4336 | -48.90566 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 37ddc698-335b-3779-a9d5-d8b918b1c008 | -19.89858 | -49.35244 | 2025-06-18 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| e63ac9ce-fcc5-3da4-a6d4-432d6519316e | -19.8993 | -49.34911 | 2025-06-18 03:51:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 52eec9f1-16bb-3b14-a2db-66e9033089b3 | -16.58856 | -49.22004 | 2025-06-18 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d4d085f-db64-3c16-9993-4a8020b9cc84 | -15.41077 | -47.83433 | 2025-06-18 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65c4b295-4a9b-3e7b-8677-ec3f4502c955 | -21.99994 | -46.80441 | 2025-06-18 03:51:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 914925bc-6c0b-37ab-adc4-a3482bc9ba14 | -16.68325 | -43.88346 | 2025-06-18 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6499d940-0b2d-3b6a-9e6f-f6a9dd5d165b | -21.07118 | -46.21999 | 2025-06-18 03:51:00 | NOAA-21 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9568eb73-0815-3cfd-9428-32088c277b11 | -17.25433 | -47.08647 | 2025-06-18 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55780001-d04c-3b77-a924-fd1d623f0ceb | -21.64361 | -44.23094 | 2025-06-18 03:51:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1b47565e-d244-327c-82bb-d387728f97d1 | -14.43285 | -48.90946 | 2025-06-18 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1c2d687f-95d5-3b76-b8fb-28e6b9263b60 | -20.31204 | -45.58547 | 2025-06-18 03:51:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c7afa21-974b-3dc7-a9dd-716ff59d9a1f | -20.50529 | -45.58646 | 2025-06-18 03:51:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f4e0684-c2da-3d9d-b3c3-9bb2c44d7cd7 | -22.76632 | -42.96383 | 2025-06-18 03:51:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b2cb826e-8cb7-30ef-9f47-8d48bf758671 | -15.41135 | -47.83141 | 2025-06-18 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a198e704-a30d-3a4b-92f6-4cb5a52fedd7 | -18.37754 | -44.51023 | 2025-06-18 03:51:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 845ff2b6-7349-34f5-98cd-fe8653597ded | -15.40572 | -47.83309 | 2025-06-18 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3816c38b-7e13-331a-bde4-2394f189ecac | -20.99377 | -47.39285 | 2025-06-18 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49bb4051-e65f-3b51-ad2d-8dbdde8e2d74 | -20.98836 | -47.39664 | 2025-06-18 03:51:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a805494d-c37e-3b2d-8742-5f3e7e122705 | -18.53212 | -48.96685 | 2025-06-18 03:51:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8af9a36-96b7-32de-b156-8b59b713eebe | -19.58352 | -53.50426 | 2025-06-18 03:51:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c36b18ec-6681-3da5-a99d-93bb61a5a18a | -15.40063 | -47.83208 | 2025-06-18 03:51:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c843bbc3-7219-3dcf-8bdb-c0de34fd552c | -21.67004 | -41.94645 | 2025-06-18 03:51:00 | NOAA-21 | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0cf8b664-f525-3db2-9319-e2f23063414c | -22.78697 | -43.75559 | 2025-06-18 03:53:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 180b90ed-1a70-36ea-8972-00c183b128ae | -22.77859 | -49.31916 | 2025-06-18 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1b99c963-7333-3652-86dc-669092125fd2 | -21.86334 | -49.74433 | 2025-06-18 03:53:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b787b4f3-8556-3ca6-9f0f-ff7ff7961a16 | -22.76895 | -49.31671 | 2025-06-18 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fc506cc-539e-3d6e-b5f3-cf00b0faa4a0 | -22.22289 | -48.70105 | 2025-06-18 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4af1e746-b940-32a3-8c52-70342e458a03 | -23.40477 | -46.55532 | 2025-06-18 03:53:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c84a182b-d405-3910-ad20-5e6ebb1a9f46 | -23.59555 | -47.43749 | 2025-06-18 03:53:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2dbb1551-7db5-37f3-98ad-2b1969839f50 | -22.90351 | -43.75549 | 2025-06-18 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| dc5b4746-ad2c-362e-a1f4-7c19dccb2f2e | -25.19041 | -49.32861 | 2025-06-18 03:53:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 56cf4da2-64da-3b05-84f5-cfecb8c3b05e | -23.33765 | -46.77086 | 2025-06-18 03:53:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b05454c-5fbe-3237-9466-e3ea77eb726b | -22.8583 | -42.98082 | 2025-06-18 03:53:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c8598898-3fd8-3051-9bf0-65994735f6e4 | -23.9851 | -48.9173 | 2025-06-18 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5989932a-8cf1-37ed-82b1-59f43b4baa24 | -22.76172 | -47.69885 | 2025-06-18 03:53:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68ab83dc-5343-3a69-984c-afe281e34c62 | -22.54148 | -48.81572 | 2025-06-18 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6f492d5-8f8c-3155-b979-516a411a0985 | -22.7834 | -49.32046 | 2025-06-18 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 044ed4d2-5862-3d18-b0d2-3bfa048a134c | -22.22235 | -48.69925 | 2025-06-18 03:53:00 | NOAA-21 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 75359f0c-9ffa-3af0-9a19-e330fca060f9 | -22.77378 | -49.31792 | 2025-06-18 03:53:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 11afb1db-8e3a-39d6-b54e-06bbaabc6b2a | -22.76066 | -47.70132 | 2025-06-18 03:53:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91f21874-8b97-39ae-a471-040a9d5a7691 | -11.1382 | -53.9223 | 2025-06-18 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| d9f1d7a3-437e-3fd8-b5b9-ce4ce175a1d7 | -11.1379 | -53.9429 | 2025-06-18 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 6b964f7c-64c3-3b72-af2f-b2db4911431b | -11.119 | -53.9446 | 2025-06-18 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d17b5c8f-189e-3a4b-910d-4fc84ebdd791 | -11.1382 | -53.9223 | 2025-06-18 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| fcabf3c5-600e-3401-acf8-ef8ea3f0c82a | -11.1193 | -53.9241 | 2025-06-18 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 7f8e6b1a-4624-3ae1-99eb-ef2bfa535762 | -11.1379 | -53.9429 | 2025-06-18 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| a8349959-f8cb-3483-a5ca-d745590c07e4 | -5.07558 | -43.72599 | 2025-06-18 04:14:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d1637c85-0278-36eb-9f00-1df3039b1492 | -5.07501 | -43.7295 | 2025-06-18 04:14:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67da44e2-e887-3b42-ac30-690f0ff998cf | -5.85086 | -43.64076 | 2025-06-18 04:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa81119a-4f9a-3d81-b63d-53cd5b773ced | -4.81421 | -46.82472 | 2025-06-18 04:14:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 76708619-c081-3d08-95cb-f399de9ef1c0 | -4.55341 | -48.00623 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5ae2934-640f-31ea-a929-6cff9e7f3f54 | -2.87409 | -40.02277 | 2025-06-18 04:14:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 08c43b79-d125-39fb-8921-4ebf26c40867 | -4.248 | -47.58612 | 2025-06-18 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26660545-71a0-342a-90a4-783f98ec9aab | -3.22287 | -54.86943 | 2025-06-18 04:14:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdff8742-8bf9-3723-b61e-46ec2f88fde1 | -4.81973 | -47.32633 | 2025-06-18 04:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f69e8afa-722f-3496-adfc-430e9b8a41d2 | -4.8158 | -47.32574 | 2025-06-18 04:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5921822f-a303-36cc-aa53-06f11a1babd9 | -4.38383 | -48.06996 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05469c04-a690-383d-ac61-dd78d2b5b3cc | -5.56874 | -45.20527 | 2025-06-18 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2f816fa-2327-36aa-acc4-bd2cfb21bdfc | -2.87448 | -40.38259 | 2025-06-18 04:14:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b67299f-47ca-3c0c-b729-777323aa9b45 | -4.25201 | -47.58682 | 2025-06-18 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cb1c0a0-e5f9-3262-88ac-43f5ad1d80bd | -2.91742 | -48.23776 | 2025-06-18 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c41362df-1cd7-37ac-b7a3-5e810db40828 | -5.56935 | -45.20144 | 2025-06-18 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb98c8e6-6f2d-3a59-83cf-e3ec7ae022e3 | -4.37906 | -48.073 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef6b80f6-e9a0-3052-aef6-48b4afd2f31a | -4.82061 | -44.35589 | 2025-06-18 04:14:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8e7890ea-8259-3c7b-aca3-a16580110c9b | -4.55281 | -48.00991 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 45d27006-63d9-30ec-b3dd-a9a4bffa4a2b | -4.86897 | -37.58829 | 2025-06-18 04:14:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2cbba76-0898-36fc-8743-5f13c20b9ac5 | -4.54869 | -48.00925 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d15b4feb-5338-37f8-962e-b1821a61fe19 | -5.07223 | -43.72546 | 2025-06-18 04:14:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93edb997-7d59-3082-82b2-8d334be7b324 | -4.38258 | -48.07742 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c0846cbe-a2cd-3086-9d1f-8910c8d14a79 | -5.05795 | -43.24384 | 2025-06-18 04:14:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 450c3a42-edb1-3ca1-b9f5-3f8e55359c2a | -4.71269 | -48.43204 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c6c0a38-47f9-3d42-8676-0bee9ac09434 | -2.9192 | -48.23914 | 2025-06-18 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7314c2f7-25dd-3169-a2ca-64901539578f | -5.07167 | -43.72897 | 2025-06-18 04:14:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 130c059d-a59d-3180-b4eb-b8f090738640 | -4.54809 | -48.01291 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d504ae50-eda1-38b2-bea9-2804d8018357 | -2.91555 | -48.23443 | 2025-06-18 04:14:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 97c8a2f5-f7d8-310d-881d-14f55de4f452 | -4.37968 | -48.06927 | 2025-06-18 04:14:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
