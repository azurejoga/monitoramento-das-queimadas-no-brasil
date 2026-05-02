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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb1686b0-0779-3161-83eb-8c138e5260dd | -20.20163 | -46.45258 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| caa5743a-8e0b-3486-b8d2-18b81c6a9061 | -21.66708 | -56.31368 | 2026-05-02 04:32:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 62d5e517-59e4-3b15-be2f-cce53a44298c | -20.71753 | -55.17865 | 2026-05-02 04:32:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03dd1328-e638-39d6-bb46-35eee01e5fbe | -26.28692 | -52.692 | 2026-05-02 04:32:00 | NOAA-21 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f7eae19f-ca6d-3741-bc49-ba6107faad8a | -20.19931 | -46.44334 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3346596f-391c-394f-9566-50715018a6b3 | -21.23691 | -44.01683 | 2026-05-02 04:32:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e409ccd9-e600-30aa-9ddc-34f78fc6e90e | -21.23088 | -56.93011 | 2026-05-02 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4663d400-d4df-3940-80b1-01a9f55f347c | -20.20103 | -46.45685 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 230ebfe5-2820-3d30-b314-aeec9f18d177 | -20.29424 | -46.48729 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08f9ba63-7ee7-3680-af2c-8d232ff14cd9 | -21.95713 | -57.59425 | 2026-05-02 04:32:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47c70982-c59b-31bf-aee3-c4a5d85fcf78 | -20.70692 | -47.87435 | 2026-05-02 04:32:00 | NOAA-21 | ORLÂNDIA | SÃO PAULO | Brasil | 3534302 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e30ccda8-9d18-3eb5-928b-01a839381cc1 | -27.92448 | -54.82331 | 2026-05-02 04:34:00 | NOAA-21 | CAMPINA DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4303707 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| 6283d185-dd4d-3999-99c4-13ddbcc672bf | -10.9815 | -45.0874 | 2026-05-02 04:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 1d9c5821-792d-3694-aae9-7d45e63e34a0 | -12.3887 | -50.0435 | 2026-05-02 04:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 403e043e-a5bd-337d-bebc-ea3dc65818c3 | -12.37 | -50.0242 | 2026-05-02 04:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| bc68d014-6cd7-3054-8919-267be30016d9 | -12.3696 | -50.0459 | 2026-05-02 04:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 3298083d-0847-332f-b3b7-9857be4a71df | -12.3887 | -50.0435 | 2026-05-02 04:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 01004c70-2c48-30f1-81a7-d7e80f07e221 | -12.37 | -50.0242 | 2026-05-02 04:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 6b5c114e-6197-3648-930f-d33fd1937a79 | -10.9815 | -45.0874 | 2026-05-02 04:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 3a86c816-ed77-3a49-8171-1dbdc769830b | -12.3696 | -50.0459 | 2026-05-02 04:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 6506a8da-7bd7-3808-bc3e-a7ae27998da4 | -10.56251 | -44.3384 | 2026-05-02 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d2d3ee5-6faf-358d-ad67-e7d5c88376eb | -10.55819 | -44.33692 | 2026-05-02 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8fd778c-8444-36d4-be3d-b2108a525632 | -10.55708 | -44.33775 | 2026-05-02 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 691013f3-3bc6-30ca-8e80-87bffd3a7ca9 | -9.6782 | -43.79254 | 2026-05-02 04:59:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 899eb414-9fc5-3183-93bc-e5add343ec62 | -9.67313 | -43.78815 | 2026-05-02 04:59:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e7185b1f-428d-3c84-8deb-b410bca6ffe2 | -9.6775 | -43.79139 | 2026-05-02 04:59:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 559952a3-9f53-3504-8748-53b45e9b165e | -9.67703 | -43.79512 | 2026-05-02 04:59:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0803371e-93dd-3d3a-8ec9-159e78cc76b0 | -9.67263 | -43.79189 | 2026-05-02 04:59:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cbbd4907-d722-3de9-85d5-3b115cbec845 | -12.37 | -50.0242 | 2026-05-02 05:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| eb62e182-fa1d-3a2d-a7e5-a8db8c8a2033 | -12.3696 | -50.0459 | 2026-05-02 05:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 873b2c67-a5de-33cb-9b62-3711d2bb846b | -10.9815 | -45.0874 | 2026-05-02 05:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 52f7acc9-46f9-37ae-84f4-1263a3fd3926 | -12.3887 | -50.0435 | 2026-05-02 05:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| bbf040fc-2f70-3310-9b8a-90065be30f0f | -10.98454 | -45.09191 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ff0e086-bb4a-34ec-b90a-dd37923a17f0 | -12.38273 | -50.03721 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 9f993fb5-9202-3aa5-be63-749d578e3217 | -17.00405 | -48.28625 | 2026-05-02 05:01:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 684e0b35-a329-365d-b223-72c9837bdf07 | -17.6893 | -48.64029 | 2026-05-02 05:01:00 | NPP-375D | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f62c05e4-d7dc-3698-9d5f-d765b32eeb8b | -12.28971 | -57.39125 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3bbc4d1-9b27-3786-a865-b5c44fd3b21a | -12.04344 | -57.91576 | 2026-05-02 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 151bfd44-e6b0-3966-b420-10e6b38697cf | -11.44524 | -55.10826 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd403500-219b-3534-8746-e00b6d5b7003 | -11.43851 | -55.10715 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c9370a6-422f-3d68-9465-a54922c176f3 | -10.99131 | -45.08001 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bca77ba2-637b-31cd-aed8-71a0f0ce43c5 | -15.16121 | -56.10986 | 2026-05-02 05:01:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 46c46eac-c544-338e-b835-fc1c7d311f2a | -12.3713 | -50.03549 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a0e378dd-73d3-30c3-bbd0-1190d8e53877 | -10.99171 | -45.0768 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb978a40-b24c-3113-8387-9c23f0f417ae | -10.98034 | -45.07488 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0bdea91d-0bed-3c17-a082-c29ca879ce37 | -10.97474 | -45.07728 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d6127d6-c3fc-3db3-93fc-8e6f88621f56 | -10.98533 | -45.08559 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 96e46161-1531-3f4b-9fc0-5aafe14fd811 | -10.97741 | -45.09701 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5215db51-84d0-3217-b23c-6d645f04b17e | -8.64104 | -63.99427 | 2026-05-02 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d830c091-5207-3f05-844a-26afb7706743 | -10.98468 | -45.08205 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ffea2df9-b23b-3297-a233-2bb43dcbfd3f | -12.03969 | -57.9151 | 2026-05-02 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87bab9ac-144f-3577-822a-5ef7985e47bd | -12.37892 | -50.03664 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d37bd54a-2455-3f21-8a4a-6bf2ca528fb2 | -10.97308 | -45.08988 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fd4efe83-ca43-3bf9-989d-4c95171fcfb0 | -13.99865 | -56.62992 | 2026-05-02 05:01:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09b13ef4-0d3c-3e11-bc2c-c3e952de38c5 | -12.37444 | -50.0408 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 4d0afa9e-a730-3523-9443-1b51d03fc729 | -13.81125 | -43.65065 | 2026-05-02 05:01:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 113f7c4a-6890-359e-8acd-8f3a38ce80a7 | -12.29334 | -57.39189 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfa0ffb0-8977-3ff3-a282-e91002c7f934 | -10.98933 | -45.09581 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff3b6066-b835-3e63-96b7-20f5eeefa7f7 | -11.43631 | -55.09935 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d087972a-a454-35fa-9b95-ad1a9416b7cc | -10.97824 | -45.09076 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 554002af-9db3-39fd-9895-65d8c5e335c4 | -13.99672 | -56.64155 | 2026-05-02 05:01:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 536332f0-a7d5-39d6-8573-1d480cc95e7c | -10.97782 | -45.0939 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d2dd2ae1-e78d-32c6-8cad-92ce1338f11e | -12.37377 | -50.04553 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1ba0156f-6267-3942-9777-5037dda60abb | -11.4486 | -55.10883 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2da3746-0950-354a-8344-cb7e7da3fa4c | -10.9795 | -45.08126 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6bf442d5-f08a-3fad-b466-1b0c1fa56671 | -10.96708 | -45.09532 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9ef0af15-4546-3107-9d92-7b17e1186fc5 | -10.97391 | -45.0836 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06edcc7d-50ee-3ac3-bbb9-8fd2ecd4fdd6 | -10.99071 | -45.07645 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 760977e7-536d-3600-ab77-69ab58b8e15c | -10.96749 | -45.09219 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b2647a89-de2e-3339-8aa9-1ed2347e5dbe | -10.99545 | -45.08049 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 461ad6d3-0f89-34be-bd40-a1e055dd83e2 | -14.3276 | -57.7393 | 2026-05-02 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64c9c296-aa48-3c41-be34-8a6c1606a4e8 | -10.98341 | -45.09156 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c206663-8ad2-38f3-9d94-809e66b32062 | -11.5582 | -48.26852 | 2026-05-02 05:01:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e96fc362-bd77-3c57-8223-988de7815a43 | -12.28897 | -57.39551 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1389c4a9-99a8-31fc-9a0b-44f221ebaf1f | -10.98415 | -45.09504 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e09cb09-5c87-383a-99ec-a5aaec771a81 | -12.28608 | -57.39061 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0da41f5-cd22-3f0f-995d-f56c0c9d64c8 | -10.98383 | -45.08842 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2f6a55f-0eda-350a-9ae6-fde2dc4dab4f | -12.29838 | -57.40609 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| debab818-6fe1-34c2-8b45-d37b4b706202 | -14.324 | -57.73862 | 2026-05-02 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50e0a6ff-a6f1-306b-8600-fce930068c78 | -15.00184 | -51.93184 | 2026-05-02 05:01:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9d7c695-2491-314f-8e0e-b34fa6f01872 | -14.21928 | -59.00031 | 2026-05-02 05:01:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ce539d4-a08f-31e1-8477-43ace8336a0e | -16.15633 | -58.49548 | 2026-05-02 05:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b7bbdc08-a7ee-3924-a326-e59e0c001926 | -10.98425 | -45.08525 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dda16547-3447-3b7a-b949-3cb069f5d5b3 | -12.37959 | -50.0319 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99c34f74-dda0-31d5-8ed3-c9318efd9c78 | -10.98901 | -45.08921 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4be2a9a-19ca-3f55-bd16-8fc2b71c34ff | -12.04422 | -57.91117 | 2026-05-02 05:01:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee2d1600-d98d-3b60-9241-af235cfb57b8 | -10.96791 | -45.08903 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c28a509f-d53f-30f5-b354-3246e3bd7e17 | -13.37665 | -54.26739 | 2026-05-02 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e646343f-2c38-3439-a9b0-971c54ece331 | -10.98654 | -45.07594 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dfd4aa0-c22e-38dc-8905-6648491c7ec3 | -10.9851 | -45.07885 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd2be149-d702-33c2-a49d-c17378e708c8 | -10.97866 | -45.0876 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68902ec2-f28e-3f1b-af4c-68d3b0d2165b | -10.98985 | -45.08286 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36dd20f9-80b2-3401-81c6-10ef7056f7ca | -10.98613 | -45.07917 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40d2c83c-9f21-3f02-9d01-0186d44ebb11 | -15.58129 | -46.81026 | 2026-05-02 05:01:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d9df1f-2c8e-3fd5-84cc-0b55841d949e | -12.37511 | -50.03607 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 772a9d9f-fbf2-3248-b587-34effba2402a | -10.98817 | -45.09546 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 883cbd99-cba2-30f0-a77a-4ddd26c7f125 | -12.36996 | -50.04496 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4ab1a11d-7d73-3833-ab2f-63485e224874 | -8.63517 | -63.99313 | 2026-05-02 05:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 323941a6-a722-36d6-9838-df1c4da2c17b | -10.98493 | -45.08876 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fbe16b4-e841-3c4d-a256-0a1ee7bd0094 | -14.30528 | -49.24922 | 2026-05-02 05:01:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
