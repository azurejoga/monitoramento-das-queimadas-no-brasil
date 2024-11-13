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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0797d120-1c5f-3860-8e35-ea7806eec8e9 | -2.71615 | -44.86021 | 2024-11-13 03:40:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6faafb07-b7f4-3e9d-852f-1500ee13130f | -1.28376 | -47.90627 | 2024-11-13 03:40:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c87b95d6-0600-31e2-8f19-ba03892474ef | -6.55579 | -35.27754 | 2024-11-13 03:40:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 069c8ef0-687c-34af-87ad-3b9e9328abb6 | -4.66036 | -47.42866 | 2024-11-13 03:40:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ebd320b5-36f0-3b96-a050-348428eb5e34 | -11.3406 | -37.62888 | 2024-11-13 03:42:00 | NPP-375D | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 867ed44b-7d77-3124-96b7-7e78d8badcc4 | -5.15119 | -48.18666 | 2024-11-13 03:42:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6125780a-03b7-3a67-a579-66766ee3e1b0 | -7.39959 | -37.55828 | 2024-11-13 03:42:00 | NPP-375D | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17eac659-3884-3374-b4fb-c71a076bc924 | -7.46 | -35.1434 | 2024-11-13 03:42:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 679c0d3c-76a4-3be8-a19b-2cf547f07fc6 | -8.11944 | -38.617 | 2024-11-13 03:42:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 784c8faa-00c6-3ab0-b3e0-bde3f96d8d14 | -8.12305 | -38.61763 | 2024-11-13 03:42:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| af63ba20-b70d-32bb-a54f-a0782db8d25d | -6.82299 | -46.7784 | 2024-11-13 03:42:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8fa0752b-2265-342b-a3e3-36a26a2806f0 | -6.95134 | -47.85523 | 2024-11-13 03:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b6e8ddb-d1dc-3086-ae74-bc73dd374a0d | -10.36719 | -49.18622 | 2024-11-13 03:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41258422-ee37-388b-b22b-fe2b462830d5 | -10.73396 | -49.52015 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 945335de-c571-3dec-993d-b61eced44aec | -10.73856 | -49.52703 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 39f8051f-5a14-3733-b7a3-690b66a08541 | -8.11875 | -38.62119 | 2024-11-13 03:42:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b0b562a0-a012-33a5-abdc-0db471c883c5 | -8.00352 | -34.93264 | 2024-11-13 03:42:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2b144d2d-ba54-36b9-af15-17381a75a6d4 | -7.65596 | -35.18831 | 2024-11-13 03:42:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 60c12aac-d620-3e65-a1b6-3f2774339448 | -7.07535 | -38.88437 | 2024-11-13 03:42:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5ee42363-f9fe-3f22-8cce-e204193c268d | -10.72577 | -49.52521 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 64e994f3-ecd2-3f35-9160-476427fb7c69 | -5.15242 | -48.18003 | 2024-11-13 03:42:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e57224bd-5a13-36e7-9a3d-d1aa87e244f2 | -7.80159 | -35.07911 | 2024-11-13 03:42:00 | NPP-375D | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 871ea3ad-9bf1-31c1-bfbd-851b84434306 | -10.74082 | -49.52169 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 16c5a28e-50eb-3607-86f2-e83db6f8722e | -7.65928 | -35.18884 | 2024-11-13 03:42:00 | NPP-375D | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f2d4e88c-6e98-3dea-9378-67124589ff06 | -10.73266 | -49.52655 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e49938b7-0ab6-3e29-b20c-896f73d266e7 | -10.73952 | -49.52806 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f9767e37-5a5e-3ab3-b054-e4613af84816 | -9.52952 | -35.71057 | 2024-11-13 03:42:00 | NPP-375D | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7006978-2357-3d8c-a134-8b3d5ef8bf47 | -7.06863 | -38.87875 | 2024-11-13 03:42:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| c07a8546-e099-365e-969f-fb7848ce1307 | -7.45945 | -35.14688 | 2024-11-13 03:42:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 60eb33e2-6083-3543-a099-0ad99878a39f | -10.73989 | -49.52069 | 2024-11-13 03:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4250f88b-fba7-39ac-bbed-95b466974dbf | -7.46768 | -37.52217 | 2024-11-13 03:42:00 | NPP-375D | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e79f1148-4696-34a9-9cdf-4ca52fae38d1 | -10.36962 | -49.17416 | 2024-11-13 03:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90dd2eb6-9a1b-3578-9a13-ff2504252b02 | -10.36841 | -49.18016 | 2024-11-13 03:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1155f12e-469e-3dc7-bbfb-2dd348083b4a | -6.82922 | -46.77965 | 2024-11-13 03:42:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f40e794a-39e5-3db4-9247-9d6527be9969 | -18.06547 | -42.6219 | 2024-11-13 03:44:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95ca4cd7-96be-39fc-af85-06cb05bea4ec | -19.83729 | -40.08318 | 2024-11-13 03:44:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cc4bc9fd-50ba-32ee-addb-7897ed0e7108 | -15.8658 | -43.79098 | 2024-11-13 03:44:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7ccdb1d-0709-396e-9531-45330b826d53 | -14.954 | -42.3014 | 2024-11-13 03:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 85c3ce29-e2f6-3ec9-99f6-844d4f6516ab | -19.71814 | -40.3547 | 2024-11-13 03:44:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d49e48ea-d47c-357d-b960-f82194b9b7a0 | -16.13878 | -43.56078 | 2024-11-13 03:44:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| de671969-d949-3cdc-a2a8-e6427cd8a8ab | -17.75377 | -42.89481 | 2024-11-13 03:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8be136d-ae2c-356b-bce0-4607190c98c0 | -16.65347 | -40.94559 | 2024-11-13 03:44:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21162b50-0ffb-316d-9943-f6cecb4341ad | -16.13958 | -43.55647 | 2024-11-13 03:44:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b92660f-e514-35c9-9cff-fe99e376dff9 | -14.62006 | -43.66094 | 2024-11-13 03:44:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b15de5b8-245b-3b80-abd7-358dd2404043 | -14.61757 | -43.66142 | 2024-11-13 03:44:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5095286d-736f-3514-8ef2-695fe676b1b9 | -18.77122 | -40.79479 | 2024-11-13 03:44:00 | NPP-375D | BARRA DE SÃO FRANCISCO | ESPÍRITO SANTO | Brasil | 3200904 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0fc944b5-ee4b-321d-84a3-8e1057eb0179 | -20.02744 | -41.64063 | 2024-11-13 03:44:00 | NPP-375D | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 489d163f-6033-3b2e-af38-ea782930de9d | -17.25191 | -46.29183 | 2024-11-13 03:44:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74eeca71-7088-39d5-97e9-56816623cb4e | -14.95807 | -42.30212 | 2024-11-13 03:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6f500ee-f895-3080-8c6a-609f29000f73 | -19.27467 | -39.89474 | 2024-11-13 03:44:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e0de8890-ceb4-3daa-8526-905a026a0e00 | -20.99755 | -47.41996 | 2024-11-13 03:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f49edaf8-cd08-3485-8f5c-078f881fcf2a | -20.99253 | -47.41882 | 2024-11-13 03:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96cdaffe-b922-3363-a0d2-ee669171866e | -20.9932 | -47.41563 | 2024-11-13 03:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d19e4716-8362-3e0f-8dc2-2ccefcff36b2 | -21.04931 | -47.24756 | 2024-11-13 03:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fcbbe457-b7fc-3c77-8c61-8b5a1da1fa2e | -20.99822 | -47.41677 | 2024-11-13 03:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ecfa5b-bf69-37c9-8d75-9a69ad801c9d | -21.0484 | -47.2503 | 2024-11-13 03:46:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f35e727-71d9-30c7-ba75-3ab7f87cbead | -29.52863 | -49.88974 | 2024-11-13 03:49:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 11.9 |
| 57720a3d-303f-3354-a587-7ed7f7bb4fcc | -28.58678 | -49.44156 | 2024-11-13 03:49:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 46f41eef-b709-3edd-bbff-482f138032b5 | -27.46879 | -48.68061 | 2024-11-13 03:49:00 | NPP-375D | BIGUAÇU | SANTA CATARINA | Brasil | 4202305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 563a8307-30f5-3aa9-aa38-f4a51e1bcc35 | -29.52915 | -49.88996 | 2024-11-13 03:49:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 8.9 |
| 7f349227-058c-3890-9f14-741bc50045c8 | -29.5306 | -49.88378 | 2024-11-13 03:49:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 8.9 |
| 16ac725d-aa6d-39a7-b470-49f4d3130358 | -29.53003 | -49.88356 | 2024-11-13 03:49:00 | NPP-375D | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.2 |
| e3ede26a-e43f-3466-b2a8-36fce991386b | -3.0689 | -50.3326 | 2024-11-13 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 56250209-5ade-3021-9600-d3578e17400a | 1.048 | -60.5986 | 2024-11-13 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 98c7edcf-3a4d-3d51-bac1-6056be834c34 | -4.6776 | -44.5861 | 2024-11-13 03:50:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| fd5c478e-a2a1-319a-8df2-51b2350fef54 | -3.0504 | -50.3332 | 2024-11-13 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5999a3dd-57fb-3c32-b302-60814051ad4a | -10.7425 | -49.5244 | 2024-11-13 03:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f08b660f-c501-3d0e-b0e6-dfe323902b59 | -3.9483 | -48.1724 | 2024-11-13 03:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 9b133034-7a1d-39ab-8f10-c39361f7ad2d | -2.9925 | -51.0242 | 2024-11-13 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| e6310d66-0ac3-38f9-8112-fc7c6077675c | 1.0663 | -60.5985 | 2024-11-13 03:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 61.4 |
| be9fe291-6d96-31a4-a77d-031324c8aa60 | -10.7235 | -49.5265 | 2024-11-13 03:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 72fc2689-828d-33cb-a843-0dc707c8002f | -3.0504 | -50.3332 | 2024-11-13 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9c44476d-f749-33a5-9610-b1d2f3604076 | -3.9483 | -48.1724 | 2024-11-13 04:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 96888f4e-87e9-3aad-8d21-c200b1f981e6 | -3.3518 | -48.9689 | 2024-11-13 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f1bdaff2-4af4-3dcb-9024-de59c11e3e9f | -4.6581 | -47.4216 | 2024-11-13 04:00:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b2566fb7-c13e-3552-808e-c58264178cb4 | -10.7425 | -49.5244 | 2024-11-13 04:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| ff1d774d-4cad-36c1-94a8-9d430f8bfe1a | -3.3519 | -48.9475 | 2024-11-13 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 99615956-bcc0-3f19-9747-e1e67c010f5a | 1.048 | -60.5986 | 2024-11-13 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| e8f8f173-9855-3164-8766-7c206fc2eab1 | -10.7235 | -49.5265 | 2024-11-13 04:00:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| d8b8059b-3f98-3abb-8694-fe6a47328d73 | -3.0689 | -50.3326 | 2024-11-13 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 8103f7a7-79ba-34c8-9af0-07360bf16778 | -2.9925 | -51.0242 | 2024-11-13 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 011401d2-7d6a-3e80-acac-4350bd0702c7 | -2.9924 | -51.045 | 2024-11-13 04:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 8dec6a46-fee6-33de-bd3d-3d6d35c4d1da | 1.0663 | -60.5985 | 2024-11-13 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5dc17301-5162-35ee-ba41-fcaa17867c12 | -3.3334 | -48.9482 | 2024-11-13 04:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| dd7469f3-eaa5-3669-8089-5c1ea69cf1b2 | -4.03963 | -48.09969 | 2024-11-13 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37594cd9-08b1-3ad0-89d6-8d8d365ee5e8 | -3.04289 | -50.33449 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 560fd10a-9cf2-322e-a318-8ac7014c9aab | -2.99478 | -51.04283 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f739132b-2a6f-3559-9fff-4cc70a9e5b98 | -4.36977 | -44.10344 | 2024-11-13 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bdb63956-7aee-3777-a78f-9012f79a08bd | -3.49916 | -50.84686 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ca0930b-fcef-30d1-8bef-bd57c6ae4e4c | -2.62322 | -46.81852 | 2024-11-13 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0d9f7d3-b51b-3f0f-b4bf-6399198980a7 | -3.54255 | -51.59911 | 2024-11-13 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ec49385-3eb0-34c7-9119-54d592a9c7ad | -3.24993 | -50.3107 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8df212e-f204-38e7-8f2d-45e6f70c2c6d | -2.93551 | -48.31187 | 2024-11-13 04:04:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 077587c6-0b77-3adb-bfe3-d421b0a9427c | -3.51729 | -49.95521 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b56bd4e-b055-3264-80f3-9ec0d3658129 | -3.34264 | -48.98059 | 2024-11-13 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7650e3a-efb7-3262-b07b-08bb8b1527e5 | -3.17513 | -50.45666 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5287f3a8-c5a7-3aca-a699-d6e04f64bfd3 | -3.52004 | -49.9383 | 2024-11-13 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27dc42b8-e831-3175-ba38-3a4ea9aa1af2 | -3.97434 | -46.60178 | 2024-11-13 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d55731b0-b660-3ff5-a0d7-b9163e60fd71 | -3.06054 | -50.3302 | 2024-11-13 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3ca7faf-4c1a-3bd6-8030-c2281f337134 | -3.95042 | -45.78313 | 2024-11-13 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README15.md)
