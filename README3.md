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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efb3d2a8-24f4-3167-b992-b23858c748ed | -6.35118 | -43.65957 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1b52fd6-feb2-3ea6-9dbb-555602e67d2b | -5.64029 | -43.70949 | 2025-04-16 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ffa68bfb-e405-39c4-98a4-9143701772a5 | -6.34397 | -43.66205 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb8d2cb3-5660-3977-9168-809d3f7aa918 | -18.83634 | -43.47058 | 2025-04-16 04:19:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 266a96a6-2768-376e-9431-f8b50e3d4a85 | -5.93887 | -44.4689 | 2025-04-16 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f01e8c7-b5af-3b1c-91dd-7883c6319364 | -10.79031 | -46.52371 | 2025-04-16 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 9962fc5a-3144-3250-b79f-826a53b67ff5 | -4.89735 | -43.61823 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8bb1588-a5e4-3017-9028-28df2b08df8a | -6.35795 | -43.65727 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41844fd8-a95c-3871-8aed-e2d790c1d490 | -12.0353 | -42.77122 | 2025-04-16 04:19:00 | NOAA-20 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 333e0b61-228b-385e-a55c-deb6872bcb2e | -5.94657 | -44.46304 | 2025-04-16 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c482425-31ed-3c1c-84e4-50bca5794c54 | -6.72652 | -40.43081 | 2025-04-16 04:19:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7c6fb517-92cc-3af1-8224-d33ccc546a70 | -14.76774 | -52.07519 | 2025-04-16 04:19:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0689e79-47f8-3e28-9248-a8b765b24eb2 | -6.96 | -43.04002 | 2025-04-16 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67f96f78-077e-3044-a717-81de894d6c5e | -15.28817 | -55.87878 | 2025-04-16 04:19:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 5ce20872-5b9c-3d6e-bbff-8cbaec7016ff | -22.21279 | -45.97654 | 2025-04-16 04:21:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| 23d84c68-8279-3a47-9937-5d8c170cf448 | -22.22533 | -53.55311 | 2025-04-16 04:21:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 27f19aaa-7fe6-3cee-94f7-1b900416ded6 | -17.85423 | -54.27489 | 2025-04-16 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| a73ab3a7-0d5e-3055-8a70-20748d36b664 | -24.89299 | -51.37706 | 2025-04-16 04:21:00 | NOAA-20 | PRUDENTÓPOLIS | PARANÁ | Brasil | 4120606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 54685d2a-d947-3ded-8d7a-e2920f5ae6ba | -18.42447 | -53.37731 | 2025-04-16 04:21:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81460758-4281-34d7-a373-f1c5e79abb83 | -20.50349 | -55.72527 | 2025-04-16 04:21:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| f8370ac3-253b-3569-b599-f846a5ac406c | -17.40286 | -53.62844 | 2025-04-16 04:21:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfa9f15a-0d4d-3034-9bb2-6e03106d9d77 | -19.74348 | -56.0515 | 2025-04-16 04:21:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 26517288-de3e-3954-ab50-589f35e04804 | -21.45185 | -55.77648 | 2025-04-16 04:21:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f4b9afba-edaa-366b-87d8-eb114720c79f | -19.54968 | -51.42952 | 2025-04-16 04:21:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e72846e-29b6-322b-a8b6-658a05e2b5d9 | -25.19183 | -49.32593 | 2025-04-16 04:21:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b458389a-02c1-38c2-8907-800d78177082 | -23.77131 | -53.45016 | 2025-04-16 04:21:00 | NOAA-20 | UMUARAMA | PARANÁ | Brasil | 4128104 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4934fb05-14d9-3f8f-9ea5-735163453de0 | -19.43112 | -43.68902 | 2025-04-16 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31553dc5-eee0-350a-9583-75bcefe0791f | -19.93348 | -54.35368 | 2025-04-16 04:21:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 433f6d7f-3b8d-377f-b1d7-02b0b5747617 | -24.56948 | -49.93834 | 2025-04-16 04:21:00 | NOAA-20 | PIRAÍ DO SUL | PARANÁ | Brasil | 4119400 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 055d0ac5-1a63-3d97-9a3d-d94ebfc49184 | -20.19569 | -42.19941 | 2025-04-16 04:21:00 | NOAA-20 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 6232220f-9e8b-30dc-9dbc-3cda59c0f71c | -24.48762 | -49.30828 | 2025-04-16 04:21:00 | NOAA-20 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9ec3db62-b165-367a-aa27-dac27fcc93f5 | -22.45313 | -42.57723 | 2025-04-16 04:21:00 | NOAA-20 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| d27d1d63-dd53-3edb-8cae-ef55119df738 | -20.267 | -45.52782 | 2025-04-16 04:21:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| c4d2e051-8314-3fe5-b990-492bbece6ad4 | -29.82105 | -54.55438 | 2025-04-16 04:23:00 | NOAA-20 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| f1c63980-58c2-37d9-a2bd-1fc7d1fb72e7 | -29.77746 | -51.17774 | 2025-04-16 04:23:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 502d5b56-6142-303b-831f-d883f0ea6569 | -30.47156 | -54.12892 | 2025-04-16 04:23:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 28c98193-95a4-3f7e-99f3-4ececca34c3b | -26.60366 | -49.42027 | 2025-04-16 04:23:00 | NOAA-20 | RIO DOS CEDROS | SANTA CATARINA | Brasil | 4214706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| eee890cc-5500-3be2-a775-453b7c092528 | -26.97295 | -52.77761 | 2025-04-16 04:23:00 | NOAA-20 | NOVA ITABERABA | SANTA CATARINA | Brasil | 4211454 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 93881c59-f6b8-31e1-85fa-470680e8df29 | -29.21684 | -51.89951 | 2025-04-16 04:23:00 | NOAA-20 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| a01e38d3-7512-3c3f-884e-3fbb5d1bcb86 | -26.56583 | -52.22955 | 2025-04-16 04:23:00 | NOAA-20 | ABELARDO LUZ | SANTA CATARINA | Brasil | 4200101 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 770da2e4-7b98-3c82-bb2c-d0266765ac3e | -29.77813 | -51.17371 | 2025-04-16 04:23:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d6536455-c7d9-3fb9-9a54-89bbf4b8878a | -29.58754 | -51.70429 | 2025-04-16 04:23:00 | NOAA-20 | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| c3a2b918-74c0-33e3-8a30-aa141998ee76 | -2.5855 | -51.93851 | 2025-04-16 05:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae960bd9-2851-3c0b-9818-759f1f211897 | -6.36328 | -43.65878 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87cd5529-3026-3581-95ca-707a140d3150 | -5.94173 | -44.46469 | 2025-04-16 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3565de73-1fe6-3634-b32e-66bcb922d292 | -6.34117 | -43.66288 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b92efa2c-fefd-3b12-8ea0-aaa1f2006306 | -6.34215 | -43.6554 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6cb2d6b9-c009-3a91-abd3-d12312676a7e | -6.34917 | -43.65672 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ce288e08-d4aa-38ae-b6a2-28d68bd37137 | -5.93767 | -44.46905 | 2025-04-16 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb3d1fab-5ec4-39a1-91a8-4ef400f2264c | -6.65889 | -47.59893 | 2025-04-16 05:10:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 34b33bdb-80b3-3594-9894-baf92dd807db | -3.69753 | -53.75565 | 2025-04-16 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05120e10-219d-3ef1-bf0f-6f12ceff04c8 | -6.36148 | -43.65228 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2df94603-11cf-30bd-997c-04739a8537b7 | -6.66545 | -47.59238 | 2025-04-16 05:10:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ef296db-5899-3ad6-add4-122033374b62 | -6.34823 | -43.66387 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9d1a9c86-1aa5-39e5-bb51-5dfaff30bf20 | -6.35621 | -43.65783 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9af0908-85df-3820-a2a7-70c3bb4c8c3e | -6.36056 | -43.65962 | 2025-04-16 05:10:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dd9cc35-2c2b-389c-88f5-6ba07acb7fec | -6.65938 | -47.59535 | 2025-04-16 05:10:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c256ee6-79b2-3a64-9b0d-b19357b97182 | -3.71242 | -53.75374 | 2025-04-16 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c73a25e8-b0dd-31d2-9a68-2ce51c863f00 | -5.94843 | -44.46563 | 2025-04-16 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cd3d3e04-387b-32c2-bb9a-3d428ad9db8c | -5.94438 | -44.46997 | 2025-04-16 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8bce80cc-736e-389e-8a86-1d58d7656513 | -5.94522 | -44.46374 | 2025-04-16 05:10:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 815f0281-b169-30ea-a1b5-8ddeafa72519 | -16.21555 | -58.09595 | 2025-04-16 05:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bd87569a-7ce7-3bbb-b83b-915fdcfb4a77 | -29.7776 | -51.17743 | 2025-04-16 05:16:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 2de5ca36-b5d5-30dd-ba42-08ab2e9cb49d | 3.80406 | -61.83603 | 2025-04-16 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d0d034d-ce00-3e0c-a6fe-227d38c6988a | 3.63696 | -61.01388 | 2025-04-16 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd70439e-5089-3463-970d-50dddf261d51 | 3.80738 | -61.83551 | 2025-04-16 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d37814b7-5013-39f4-b654-2c180161cd36 | 3.64028 | -61.01336 | 2025-04-16 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3210bee-5f7b-3fc9-912d-07dce0caee84 | 3.63642 | -61.01043 | 2025-04-16 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85cb8f2d-e20b-337a-858b-267b3cbde695 | 2.39559 | -61.29005 | 2025-04-16 05:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 597ac7ad-4970-347b-ba58-a314796207a1 | 2.39633 | -61.29457 | 2025-04-16 05:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ae86639-3e54-3bc7-a05c-11401cb4b89e | 2.39709 | -61.29914 | 2025-04-16 05:55:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d7b8799-0cae-3cb1-83e1-2771e48cb233 | -7.1028 | -59.40754 | 2025-04-16 05:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d954859-d34a-3e43-a6ba-66d9a35952c7 | -11.05773 | -68.71958 | 2025-04-16 05:59:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.0 |
| a769e42f-9c41-3297-8680-2a74453a3c19 | -12.30765 | -60.62656 | 2025-04-16 05:59:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9ec06846-ec0e-3f27-9c75-480f55d5fa98 | -10.29241 | -69.06216 | 2025-04-16 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c02be9f7-1344-3247-b221-7a414ce29de9 | -11.98735 | -63.03071 | 2025-04-16 05:59:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bf9cbac-7228-32dd-be86-0c8f6e61be65 | -10.243 | -68.55752 | 2025-04-16 05:59:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| dd61eb1e-bc03-3511-a63b-4513b0bca07c | -10.81508 | -69.53632 | 2025-04-16 05:59:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 0a2ab03e-62aa-3fde-83af-6284c4d29edc | -9.17949 | -57.79865 | 2025-04-16 05:59:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 98639769-fb4e-359f-af67-3b35786e725c | -15.84188 | -59.28642 | 2025-04-16 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 693fcf7f-c5b3-344a-a228-edebf8b5de46 | -5.6382 | -43.6943 | 2025-04-16 14:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |


