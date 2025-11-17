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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b66d9d7-3a98-3bc8-844e-c090c4e101b3 | -10.62104 | -48.07688 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fbc2d75e-fc2b-331e-b1d9-b939413e8600 | -12.86163 | -46.02653 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f1b58d6-1f4d-3d0a-99a8-d17cc58ce5ee | -10.315 | -44.2834 | 2025-11-17 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b17c26ec-1802-38da-b1dd-e4fe2bc24848 | -11.73359 | -49.84262 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04ee6fcc-480b-3452-9316-3365add98efb | -12.8714 | -46.47216 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec2f7380-6fde-3848-88b6-7ee43795b22a | -14.31272 | -47.1046 | 2025-11-17 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a73718b1-073f-3f25-9331-beb0314546b7 | -10.71338 | -44.5276 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e86214a0-6502-38c5-895b-b6ea5077f553 | -11.15768 | -47.46381 | 2025-11-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a445c4e-b9a7-334a-a04e-88dc1743b842 | -12.6437 | -48.50695 | 2025-11-17 04:40:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c60b973-fd34-3ee8-af48-3b94d1f48541 | -15.13147 | -43.74656 | 2025-11-17 04:40:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 08a88804-d4ea-3f2e-a2c7-8de0d3eac98c | -10.83369 | -48.03714 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b26015c9-0ce8-35a6-a546-d490c814c1e3 | -13.46829 | -44.03109 | 2025-11-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8641a47-8d46-3137-bdca-de7aeb9eb308 | -12.53053 | -48.7528 | 2025-11-17 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1c4ca75-fde6-37b0-af50-b36a4a65b74d | -10.63483 | -51.75914 | 2025-11-17 04:40:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d99a2223-36ac-36be-809e-c7fc247751ba | -10.85657 | -44.08826 | 2025-11-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fb91db3-2d05-37c8-ae68-53ac30758b52 | -12.8599 | -46.4702 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf76d7e8-44a9-3d75-b0f6-6568a3d7266d | -10.70809 | -44.50289 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e284140-5de1-373d-9c1c-04cc477068ce | -9.43697 | -46.36332 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6198d6bf-61b0-3d04-b819-ed5d097ec652 | -10.51483 | -48.01441 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e14a4136-6d4d-3501-aa92-847f91967a96 | -9.51957 | -47.26801 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1cec89b-1c4a-347c-9e1d-341a7e6b98d9 | -11.97739 | -43.99445 | 2025-11-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcafaa3a-9fb8-3385-b28f-62c951d9214b | -10.32295 | -44.28902 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88b51b00-9818-34ea-bb2d-a8282eaa5c7f | -10.16898 | -44.53297 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d612bf76-39ec-35d2-9a5a-99d1c644a934 | -13.52185 | -48.75175 | 2025-11-17 04:40:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d757a06-3786-3e59-ad0d-55aa62aa3784 | -12.21166 | -49.6296 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c26786e-ff67-3c6e-b668-0f545497f7f2 | -11.81985 | -47.58517 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 097006e0-5ebc-3906-92a8-7148d8264228 | -10.85728 | -44.09027 | 2025-11-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aabcf3b5-f19c-3461-8882-ec52ac5c795b | -12.20773 | -49.6106 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22c4db7e-d6d2-38b4-af86-50ca3ea37c05 | -10.13336 | -49.15099 | 2025-11-17 04:40:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bda059b5-7dee-3f6f-b2a9-ab9d0f642aa7 | -12.29451 | -61.95854 | 2025-11-17 04:40:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a646cef-8cdd-3088-9c39-0bfd469bc776 | -11.15584 | -49.44574 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f6edd97-ae2e-3def-ac2d-bd306ab74e74 | -12.15782 | -54.28473 | 2025-11-17 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea37d902-63ec-3ef9-a8b0-8f71861d075e | -10.86861 | -47.88658 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14a36227-025b-3c01-9e2f-9f785341fbf7 | -10.65991 | -49.37547 | 2025-11-17 04:40:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 356aca57-d2fc-3398-8be2-ff2c9bf8d8b9 | -11.43966 | -54.33665 | 2025-11-17 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02b84c92-7b14-399e-95a6-631c58737070 | -9.57793 | -49.09702 | 2025-11-17 04:40:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 854f28b7-7ae3-399c-b53a-b6d9c03090a5 | -9.32361 | -46.57447 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82f3f0df-effa-338b-a6bb-47a36a010626 | -10.27056 | -48.05296 | 2025-11-17 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b305ac19-9eb8-38da-b6a6-c30ef9b25215 | -11.27521 | -49.79529 | 2025-11-17 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 753cc63f-bfda-3265-a115-acb2df846d3f | -14.91118 | -47.38452 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64df2709-f562-3509-a2af-5f6ad26c9651 | -9.98333 | -44.77268 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b9ef445-aa1b-3821-97c4-db8b53bb46c8 | -9.71215 | -43.95853 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2a70ce7d-2285-3439-a46d-be584d58482c | -10.85783 | -44.08611 | 2025-11-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f712fae2-5def-3a0e-b29f-3f109b560bdc | -11.56951 | -42.42075 | 2025-11-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7201a184-1a0a-307a-8b49-582e58045ac7 | -11.84764 | -49.21096 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9eaaefd-a78e-39ae-b6db-9eeeaaaefc06 | -12.44235 | -44.75372 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 259562e8-3f33-3f21-b5b7-a7e0209af5d2 | -12.22389 | -49.61683 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a7d7483-bc6e-3665-a7bf-fde08e687595 | -10.96417 | -44.52272 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 192a2eef-6daf-33c4-8668-d78887e69ecf | -9.74797 | -43.95474 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59634396-dfff-31b1-b613-2295432291a7 | -11.82283 | -47.58982 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4fbc1f13-0e42-3009-9f30-2bf0c282f4e6 | -10.09517 | -44.77633 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac438e89-3c9c-315e-abce-1ee261c28b19 | -9.72139 | -43.95544 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 877974b7-5583-3351-a9bb-b4bd27ca0d5a | -10.84064 | -48.03803 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c36dbc29-2516-37bb-8fd3-535524785b10 | -11.81925 | -47.58932 | 2025-11-17 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f89679a4-28ea-397b-9807-59eb6a445d17 | -10.39119 | -44.91579 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65446e3f-2ff2-307c-a7fd-7b18161fcebb | -13.41748 | -53.47864 | 2025-11-17 04:40:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46a3d1f4-1fc1-3cc2-8c80-94792f1e01b6 | -12.42884 | -43.17428 | 2025-11-17 04:40:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 91dde1b0-53aa-35d1-8c19-01832ee52428 | -9.72721 | -43.97748 | 2025-11-17 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87a92abe-2693-35c4-a431-8bda90abb9bf | -12.63619 | -45.07542 | 2025-11-17 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4e38823e-834b-3b2e-9fcb-e997d0ae4945 | -9.79821 | -48.56107 | 2025-11-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e146f11c-fcc7-3035-9133-ad0e84dcabe1 | -12.22723 | -49.61736 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6ca6e86-da18-36ae-a8cf-30973f43be3e | -11.71134 | -48.86707 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0dc195fa-f975-3a8f-a204-7ed850345795 | -14.78251 | -52.44596 | 2025-11-17 04:40:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0646908c-e402-3ff7-8da4-0b1164287dbe | -11.7096 | -48.85544 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c9a868b2-a3a7-3b7a-8def-ff30e13d7f11 | -12.70503 | -46.7753 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ada6bc39-39a9-35c3-a52a-c95dbcdd289c | -11.80852 | -45.2979 | 2025-11-17 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87150ff1-44be-3763-b898-6c354f2dbf0e | -12.74368 | -48.92042 | 2025-11-17 04:40:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1d9e0be-f16c-360d-b37a-8066e8145d3f | -14.65586 | -46.5379 | 2025-11-17 04:40:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5f839e34-bb5b-3757-824e-5e4d91731845 | -15.52742 | -43.36858 | 2025-11-17 04:40:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a99fc7c-e976-3046-b988-7fd0ee6c08f3 | -12.80365 | -46.43567 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a083ea4-4824-3174-84ba-a9011e829a4d | -11.84261 | -49.22132 | 2025-11-17 04:40:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d68a0a03-c5fd-3edc-8f17-2143d65c379e | -10.53213 | -45.39104 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2bccfd9-3540-38b3-a5d4-098bed6e23a4 | -10.55398 | -47.93298 | 2025-11-17 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b743b47-6fe1-3676-9f65-3ede778d1100 | -12.87975 | -46.46856 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 434468fb-e0c7-3c9c-9ca5-ece57a53272d | -10.96362 | -44.52675 | 2025-11-17 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42e5af56-64e2-3b02-bb80-ddb242551e8d | -12.87226 | -46.43795 | 2025-11-17 04:40:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ac2f99b5-3340-3ba7-bbd6-5b76077d65de | -11.65961 | -49.61646 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 713948e6-0ea3-3b90-9b63-b8195dd7bd7f | -9.73954 | -47.22469 | 2025-11-17 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8997b1b-5b0e-38d3-8179-b969d8cde04d | -11.44979 | -49.09351 | 2025-11-17 04:40:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba020bda-2131-34d2-b7e6-4c69ca52ab90 | -10.92928 | -48.68053 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62b9fbd5-744c-3b59-9370-5c842fff5c16 | -12.66143 | -47.16286 | 2025-11-17 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76263a1e-98a2-3001-8eb2-294a9a21467b | -8.50894 | -49.41375 | 2025-11-17 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a3cac55-6950-3745-9c72-8262a71b0b82 | -10.38657 | -44.91888 | 2025-11-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be33d23a-bb3d-3a58-917b-cf0596a100d7 | -8.73256 | -48.32029 | 2025-11-17 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18c04592-0fdf-3cf1-b9a1-4b8f433f0730 | -11.66888 | -44.73312 | 2025-11-17 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f52f1a8c-b949-3a9b-8eed-2d975da93717 | -10.92473 | -48.68769 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a52e4f6e-5cc1-3ad2-b0a0-1673125420c7 | -15.26168 | -46.55602 | 2025-11-17 04:40:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2da2f59-64b0-3455-b87d-f9928a25d1ab | -13.40549 | -43.75069 | 2025-11-17 04:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1316650-9778-3951-9918-8a3aa9e06331 | -9.05599 | -46.00558 | 2025-11-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91899ac8-3756-3e38-b19c-f0a0196065f0 | -11.05368 | -47.60788 | 2025-11-17 04:40:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0fe0525f-e24e-389f-99c9-777815030a5a | -10.1591 | -44.50501 | 2025-11-17 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e87356d-caf4-3a66-ba4d-3cd786435538 | -10.92079 | -48.69077 | 2025-11-17 04:40:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dbdfbcc-bdd9-3252-8c77-961753af7f47 | -11.70621 | -48.85492 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 89082da9-1f51-30b1-944a-e2aed40226a3 | -9.85372 | -44.18999 | 2025-11-17 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c25af12a-6d1f-3262-a926-5a0853cbe07e | -10.94591 | -45.0797 | 2025-11-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2703d258-63b4-36fa-bcd7-3d4d082894c5 | -9.52265 | -42.93289 | 2025-11-17 04:40:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6ee23c22-7eaf-37b8-acd7-2a6ab024aa79 | -11.71868 | -48.86442 | 2025-11-17 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b34005d0-f2c0-371f-8396-2eeb31c39cdb | -15.77794 | -45.43298 | 2025-11-17 04:40:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f95fceb-95d0-3d85-ba03-982fc2f586c0 | -12.801 | -46.44212 | 2025-11-17 04:40:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08c8cb4d-beff-3dc8-98a9-e1c8d0815d51 | -9.98744 | -44.77328 | 2025-11-17 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README36.md)
