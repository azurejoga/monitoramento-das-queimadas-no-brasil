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
| 279666e2-7663-352d-9ffb-4049656e6e8e | -12.59298 | -43.97972 | 2025-12-30 03:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b7d5aa6b-6b6f-3261-a2d8-131161ae73d1 | -7.15141 | -38.6678 | 2025-12-30 03:44:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5423e345-c58d-39f1-9dd1-6e01a970e924 | -11.74949 | -43.32878 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c69208e3-92a1-3bb8-bdd1-52636c852e16 | -12.59225 | -43.97738 | 2025-12-30 03:44:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fafad149-2cb0-303d-8ab2-c867d201ca9b | -6.37824 | -39.51627 | 2025-12-30 03:44:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0f7b81ee-9302-3df5-ae8d-bd62993b1f22 | -7.09779 | -38.78885 | 2025-12-30 03:44:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 702801d5-bf6a-3069-a68a-74c77367cc5c | -8.81311 | -38.93745 | 2025-12-30 03:44:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e4827a80-7b33-34b1-b092-3b4d816ad784 | -7.80115 | -42.69886 | 2025-12-30 03:44:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6cd344f-2bc2-3c3b-8dc1-5fdc632a28e5 | -6.98414 | -43.83916 | 2025-12-30 03:44:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5d07d3c-364b-3605-ad58-09ca52887b27 | -7.1521 | -38.66364 | 2025-12-30 03:44:00 | NOAA-20 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e1269280-9c56-31d7-b571-ef4af70faf9a | -6.99017 | -38.94018 | 2025-12-30 03:44:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ae6f4e7a-2f23-3529-8cd4-0e309d615447 | -6.97518 | -35.12553 | 2025-12-30 03:44:00 | NOAA-20 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a9dcffd1-3fe6-396a-a20b-6a9e6784e149 | -6.92826 | -44.57125 | 2025-12-30 03:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45074422-e4c1-32f2-9a24-b5f80972aec7 | -10.04515 | -36.26785 | 2025-12-30 03:44:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e8b3924-3d66-3323-ab3b-a4cbef5d141a | -6.95816 | -37.25504 | 2025-12-30 03:44:00 | NOAA-20 | PATOS | PARAÍBA | Brasil | 2510808 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5623ee12-128d-365e-8931-014d23266a39 | -11.75117 | -43.31968 | 2025-12-30 03:44:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b93005b1-d93c-3941-b244-45a20cd1c535 | -10.08179 | -38.43243 | 2025-12-30 03:44:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28f2d593-fa5f-3a10-87a6-5375c4561a1b | -18.60286 | -41.70681 | 2025-12-30 03:46:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fd683672-e5ba-3f51-b234-a21b29c9d5aa | -17.24274 | -41.34468 | 2025-12-30 03:46:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e6ea7e93-da98-3518-a8c7-5989b9b551ab | -18.82483 | -51.61547 | 2025-12-30 03:46:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cedbb8a1-7694-3d48-8647-b24d093222b4 | -15.25451 | -41.81083 | 2025-12-30 03:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 673f7f4f-0c81-3e7a-862f-f64a4620b50d | -15.04848 | -42.10921 | 2025-12-30 03:46:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09fdc86a-8858-3558-999a-2fd12723a06b | -13.47248 | -44.02221 | 2025-12-30 03:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 61bbdd5c-213a-38f0-9845-7f00dfd6bd66 | -18.91314 | -40.61372 | 2025-12-30 03:46:00 | NOAA-20 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b05ee13a-466a-3c15-8f81-308072b1489e | -15.1377 | -45.28444 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 981b3b37-cd31-3d45-a3ba-1182de4c4837 | -15.13874 | -45.27906 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5912619-b0f4-393e-a098-cdaae9a16a97 | -20.50306 | -42.47179 | 2025-12-30 03:46:00 | NOAA-20 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c4588e00-e7fb-35ea-995c-79ea9f2ce964 | -20.53064 | -40.93759 | 2025-12-30 03:46:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2d0b5aad-e498-33e0-9fd1-514fdad847d0 | -19.45361 | -45.45498 | 2025-12-30 03:46:00 | NOAA-20 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb262b71-3f38-34e7-9243-42f8f955d678 | -15.1329 | -45.28346 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2184187d-2c65-394d-9411-f4030002f7a4 | -18.65047 | -42.67515 | 2025-12-30 03:46:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e8e0f6cb-39ed-3321-9083-68008cb57a2d | -15.25746 | -41.81663 | 2025-12-30 03:46:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d903a22-5af5-39c9-8124-eb527f25fb6d | -13.42244 | -43.85925 | 2025-12-30 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b46e325-96d0-394f-a62c-f16ebd76e9cb | -13.47794 | -44.01828 | 2025-12-30 03:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| db64bcd6-e533-3314-a9a5-5a0736d53b19 | -16.37274 | -43.76923 | 2025-12-30 03:46:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffa9c735-7f71-3f2b-9b1f-1dfd73ab25a7 | -18.37074 | -39.9584 | 2025-12-30 03:46:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6d00a418-c14e-39f2-8dda-9cdca1342bf9 | -13.5026 | -46.70697 | 2025-12-30 03:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5866e58-499c-3b93-b031-1f5b7d7fbd45 | -20.24265 | -41.30591 | 2025-12-30 03:46:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 11fe39f2-6be1-3db2-8a9e-a488eae36261 | -18.73582 | -39.74792 | 2025-12-30 03:46:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dd398a72-4903-31cb-a912-bc862833319c | -13.5231 | -43.51339 | 2025-12-30 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47ada18b-a016-3d7a-aa6a-1f04bc0efa46 | -13.508 | -46.70819 | 2025-12-30 03:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da998ee3-b803-34c3-ac2b-0ebce85a5d20 | -20.52719 | -40.93691 | 2025-12-30 03:46:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 16dc9373-5d12-3795-aa14-c6dfae2c7b71 | -16.00809 | -41.67992 | 2025-12-30 03:46:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 66fc42a0-aa20-3b60-a78e-11e18f45fece | -18.82336 | -51.61121 | 2025-12-30 03:46:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 691bd644-0894-3cef-b3a4-5297f49650d2 | -13.42782 | -43.85545 | 2025-12-30 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f5d444f-f37d-3322-8644-1d689cf3df50 | -18.82199 | -51.61699 | 2025-12-30 03:46:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b8a1537f-c99d-3ee0-b247-95152fe83cc2 | -16.86869 | -40.61774 | 2025-12-30 03:46:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3cfbe1c0-e610-366f-bc84-67927e155cbd | -14.95283 | -42.77789 | 2025-12-30 03:46:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54938477-23b1-3ee3-b957-306154895575 | -13.47427 | -44.01276 | 2025-12-30 03:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b0ad656e-fda8-3bc2-bbc2-5488d10e6065 | -18.81828 | -51.61385 | 2025-12-30 03:46:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 430c3eeb-2c08-3b31-977e-38bc84581555 | -15.25834 | -41.81162 | 2025-12-30 03:46:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a22ab8b1-8433-3df4-ab7c-845e56af32fe | -13.47338 | -44.01747 | 2025-12-30 03:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fbb0e22e-445c-3d86-bad9-aacad61ed15d | -13.4697 | -44.01194 | 2025-12-30 03:46:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c37f2441-6c8a-3439-afb5-988a4798fba2 | -19.14085 | -44.20733 | 2025-12-30 03:46:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| de54a156-4721-37e5-aeb3-f9d06a24005a | -18.12577 | -39.74171 | 2025-12-30 03:46:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab5c0b10-2e0e-3c54-8fba-01c9637d0736 | -18.81966 | -51.60786 | 2025-12-30 03:46:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c8bac89c-dd15-348b-a360-1880bf902b6f | -13.21084 | -44.56549 | 2025-12-30 03:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6b61b2c-189a-33ca-b79c-db78d6da7cf5 | -15.12706 | -45.28787 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29e3dc0c-3f19-3536-b13e-2cf15f737f23 | -19.77709 | -41.91033 | 2025-12-30 03:46:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d5d7ec0b-3254-354a-aff9-1bc1e76ee7ed | -18.8168 | -51.60961 | 2025-12-30 03:46:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f03b4948-8ddc-3449-b4f9-ac74903bde65 | -15.13395 | -45.27805 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7898bd3f-1c1a-3b43-9e2f-a3d98b85d80b | -14.2483 | -41.75806 | 2025-12-30 03:46:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe2748dd-f815-30c5-b35f-edf94b9ad836 | -18.04696 | -41.55668 | 2025-12-30 03:46:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 737e77be-96e1-38a3-b5d4-11873aae9911 | -17.24119 | -41.35347 | 2025-12-30 03:46:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3b30db1a-6b82-3023-a723-306d3803f722 | -15.13186 | -45.28888 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c328f511-0fd4-3eb9-9f10-fc4d15b43da9 | -19.93844 | -42.18595 | 2025-12-30 03:46:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 32887601-3275-3bab-a076-2d4f9e15db86 | -13.42695 | -43.86012 | 2025-12-30 03:46:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4e6b786-66ed-3550-93cc-cc8db11a9023 | -15.1281 | -45.28248 | 2025-12-30 03:46:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c7829d8-1aaf-3c0c-ae43-a137c89b834f | -21.15382 | -43.08553 | 2025-12-30 03:49:00 | NOAA-20 | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1d5706b1-99c3-338d-9811-d3a7a7223ce1 | -21.25612 | -48.65477 | 2025-12-30 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 26ba6f6d-4467-3cc6-b7d9-b4145c769119 | -21.26071 | -48.63391 | 2025-12-30 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2d51e090-fbd6-359c-b398-a4e0366ed02c | -21.15471 | -43.08077 | 2025-12-30 03:49:00 | NOAA-20 | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 8214ca8c-787b-343c-bd88-22975fbb82eb | -21.26598 | -48.63517 | 2025-12-30 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 21918c81-53b6-3d4d-ba9b-dc3bf4fe97fe | -22.02858 | -42.31314 | 2025-12-30 03:49:00 | NOAA-20 | CORDEIRO | RIO DE JANEIRO | Brasil | 3301504 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dd681009-0ab6-3af8-935b-8cb7b18c2448 | -21.15759 | -43.08635 | 2025-12-30 03:49:00 | NOAA-20 | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 10d99d15-093e-3b1c-816d-c369c1b56a6e | -21.25534 | -48.65828 | 2025-12-30 03:49:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| ac8e1788-d290-38ea-91d3-0fc6c13b5912 | -21.15849 | -43.08152 | 2025-12-30 03:49:00 | NOAA-20 | TOCANTINS | MINAS GERAIS | Brasil | 3169000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 37c08a31-ba5b-3271-ba76-b13b68dcf929 | -10.0463 | -36.2664 | 2025-12-30 03:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.7 |
| 0bdf5601-2d41-368f-97ce-7675e3a0a08d | -10.027 | -36.2699 | 2025-12-30 04:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 2742a1b7-4159-3c58-9b73-8848ea11499f | -10.0463 | -36.2664 | 2025-12-30 04:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 230.6 |
| 9e483816-d3e9-34ba-8f28-d02a2abb4ee0 | -10.0656 | -36.263 | 2025-12-30 04:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.8 |
| ce6aca84-a25c-3dc7-a0bc-4c459b80e0ba | -10.0458 | -36.2935 | 2025-12-30 04:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 65.0 |
| d0101194-6386-367b-9d8b-b3cd1e98bc31 | -10.0463 | -36.2664 | 2025-12-30 04:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| 99c02f24-d1b4-31ed-8ba8-a1207c2f3891 | -10.0463 | -36.2664 | 2025-12-30 04:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| c9bb92ac-9f57-39da-9880-c25c55c19aba | -4.34775 | -44.11671 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6776a0cc-dea6-340e-a6a5-fd8e068990d0 | -2.46725 | -48.11416 | 2025-12-30 04:31:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f66c326-aeca-340f-a670-b5248570cfca | -5.26234 | -44.72961 | 2025-12-30 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1cde6875-9057-3ce7-a9df-7e301e31abeb | -4.73878 | -38.72799 | 2025-12-30 04:31:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17a221f6-16f4-322e-994e-4ad0890e2c7d | -3.18865 | -48.02702 | 2025-12-30 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2bf24cc8-14e6-3aeb-899c-75365cb0a98b | -3.55917 | -43.1985 | 2025-12-30 04:31:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03f125c6-9cd1-3077-a009-c1f769de7c83 | -4.33919 | -44.12407 | 2025-12-30 04:31:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8c71a89-faf1-3070-96ea-044a1b8ff716 | -5.62581 | -44.88972 | 2025-12-30 04:31:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d4db3ca-2845-3f83-8d26-4cc907c780a9 | -5.14484 | -39.46977 | 2025-12-30 04:31:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85ccc045-811e-3439-a50f-f6d7ede26d37 | -3.02211 | -49.44567 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 788981b3-2dfe-3098-8d22-5199f46d9bcc | -3.55762 | -43.59618 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 427e107a-7cbb-3c0c-b661-7cee1833475b | -3.02331 | -49.43808 | 2025-12-30 04:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| db1e450e-c836-3590-aba0-9fde9f33adc6 | -3.39445 | -42.11038 | 2025-12-30 04:31:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 71b67c58-2a37-319b-ae52-3481edd53c11 | -3.54952 | -43.59949 | 2025-12-30 04:31:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dadfc155-4283-3a01-96c7-1e99f090723d | -5.30985 | -45.18069 | 2025-12-30 04:31:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45c17be5-dbdd-3e74-964e-19e97a13a7ca | -4.50711 | -43.48717 | 2025-12-30 04:31:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README5.md)
