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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a8ddb86-0cb7-375e-a2c4-1c1a8f52aa3d | -2.99974 | -40.30054 | 2026-02-05 03:46:00 | NOAA-20 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d5d5162-0f68-3abe-8228-646dad649792 | -8.06787 | -47.12121 | 2026-02-05 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 422fd681-5211-38bd-958c-b40d1077d449 | -8.81426 | -38.92763 | 2026-02-05 03:49:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a2843312-e2bb-3914-accd-40023ff1d218 | -5.97549 | -43.56153 | 2026-02-05 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d453da56-c164-3af5-83f4-e856aaea648d | -7.16483 | -39.27614 | 2026-02-05 03:49:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 459add55-1e79-38f1-a516-afd0a1bf0560 | -8.4044 | -40.61675 | 2026-02-05 03:49:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04989959-10b7-337a-b94a-dee57eab045e | -8.08078 | -35.41725 | 2026-02-05 03:49:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d1b68ad1-b2b2-3b10-9359-751a88933d71 | -9.17949 | -40.86945 | 2026-02-05 03:49:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0579fb14-10d0-382e-a192-5ff130162d6e | -7.48819 | -35.17241 | 2026-02-05 03:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2e3a6677-f9b8-303f-9a50-bb16d7b9bf7a | -9.33432 | -36.8341 | 2026-02-05 03:49:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b46c94fa-1c71-3fe7-bbca-f5be0cace5ed | -3.91519 | -43.5273 | 2026-02-05 03:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2c34b06-7a62-3930-83a3-33edfc535e06 | -9.4999 | -37.05742 | 2026-02-05 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17558271-807f-306f-8366-81d20c6ef3f2 | -10.51667 | -40.33017 | 2026-02-05 03:49:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 958ed3d9-6a24-3470-a3cd-0a1bd006efde | -5.18161 | -35.77065 | 2026-02-05 03:49:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c4499ed6-adca-3c44-8aea-efd0cc54c06d | -8.08021 | -35.42096 | 2026-02-05 03:49:00 | NOAA-20 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2d369c7f-b686-3c9b-b07d-416af92dab24 | -8.67149 | -36.27015 | 2026-02-05 03:49:00 | NOAA-20 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 90b2acb0-8884-3543-bf85-bd8ad0359a9a | -5.34401 | -40.56881 | 2026-02-05 03:49:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c67945d2-c739-3df3-b3da-702ef6069ce5 | -8.67484 | -36.27068 | 2026-02-05 03:49:00 | NOAA-20 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b8f1f979-25d6-32e0-a169-5378fb1eb45d | -5.90338 | -43.8426 | 2026-02-05 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6aa483b8-3a17-308b-a9ec-1e3638196859 | -8.71043 | -35.2802 | 2026-02-05 03:49:00 | NOAA-20 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 48f84f3c-3659-36c2-a7bc-5a89c7deecff | -5.90391 | -43.84558 | 2026-02-05 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c5e3938-1026-31f7-8c2a-402782dd73c2 | -5.69616 | -43.16235 | 2026-02-05 03:49:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bbf66802-7a9b-36c9-a75d-11739cb68bd9 | -7.48534 | -35.16814 | 2026-02-05 03:49:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 01ac8156-d5d9-3ee9-b046-8f9347734e35 | -5.30169 | -39.48351 | 2026-02-05 03:49:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 56b793be-752b-3424-bb3d-aa65a0c0ec3e | -10.446 | -36.8675 | 2026-02-05 03:49:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| db14c05d-7680-3880-b8f4-e4c849b7a13f | -3.89293 | -40.8193 | 2026-02-05 03:49:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a790390b-277b-310f-a95f-0c1859729e6f | -5.90256 | -43.84728 | 2026-02-05 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d237c5e-c56a-374e-a3e3-6fba7707f9c7 | -5.96137 | -43.53566 | 2026-02-05 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e5df8d8-a68c-342a-9470-7952b908938b | -8.06299 | -47.11661 | 2026-02-05 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc8637e3-21b1-346f-8b30-6f9a9c5503ca | -10.59573 | -37.10492 | 2026-02-05 03:49:00 | NOAA-20 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f3d6c179-7fe5-395b-94cd-cca808c25579 | -9.33765 | -36.83462 | 2026-02-05 03:49:00 | NOAA-20 | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 82c3e834-c019-310b-97cd-8ff4e2651114 | -3.89215 | -40.82417 | 2026-02-05 03:49:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d977251d-a8ff-30af-84a8-6433b138b300 | -8.06234 | -47.12019 | 2026-02-05 03:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac0271d-ea98-33cb-91ec-c28fc54a21a4 | -9.49659 | -37.0569 | 2026-02-05 03:49:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e11d59cd-ab84-3726-ab68-c1bdbafbb156 | -8.5004 | -35.76052 | 2026-02-05 03:49:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0e147902-ffef-3d2d-b54f-e9dca4fd49c1 | -11.06147 | -38.43896 | 2026-02-05 03:49:00 | NOAA-20 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 610071bf-8a1d-3316-b82e-aa138f7ca845 | -9.38946 | -38.24953 | 2026-02-05 03:49:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07299cc9-6554-321c-bb03-a35e2a3d1f14 | -7.38681 | -34.98781 | 2026-02-05 03:49:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f847db79-e810-35bd-9cd9-84fef9fa1427 | -9.49137 | -36.85094 | 2026-02-05 03:49:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f6a2e828-12b9-3ccb-b3e6-3b305b8d3462 | -8.81485 | -38.924 | 2026-02-05 03:49:00 | NOAA-20 | RODELAS | BAHIA | Brasil | 2927101 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d80dc69e-0659-3973-8bb9-711bc8b26b55 | -10.69989 | -38.53156 | 2026-02-05 03:49:00 | NOAA-20 | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fde35e09-4f09-336e-b134-f9c4b9a3c2d0 | -9.97978 | -36.34675 | 2026-02-05 03:49:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9f2f849c-6619-3ef6-bb77-f2e89803e070 | -15.41833 | -41.42547 | 2026-02-05 03:51:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1eebd73e-21bd-3fd1-ab0e-fbb9b4b86b39 | -15.80039 | -41.46618 | 2026-02-05 03:51:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3473b913-997e-336a-a23c-593b3391728b | -15.28669 | -40.97316 | 2026-02-05 03:51:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| df0a88fd-db92-302b-89f9-c3e98562ae2c | -12.39161 | -43.67299 | 2026-02-05 03:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d7e8198-7101-352a-856c-9770e90e7cac | -15.48502 | -39.14113 | 2026-02-05 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c06c7493-e351-37bf-83ca-a1b9763157be | -11.79805 | -40.0788 | 2026-02-05 03:51:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 944999bd-4686-3308-8a03-accbd80a828e | -15.56591 | -43.79401 | 2026-02-05 03:51:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 59af264c-6a9f-3982-9a49-bd883a7fac57 | -13.38576 | -39.96033 | 2026-02-05 03:51:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 743937a7-292b-3dba-b0d9-73845d2994e6 | -15.48559 | -39.13756 | 2026-02-05 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3149ac19-d42d-37a4-9e71-682e37b4680d | -13.36049 | -39.90307 | 2026-02-05 03:51:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bb8e09a6-a218-3f0a-90ff-a08fb2a2c7a0 | -13.36108 | -39.89943 | 2026-02-05 03:51:00 | NOAA-20 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4c1c89c-a5ad-371c-8cc5-c24d07e34521 | -12.3852 | -43.49693 | 2026-02-05 03:51:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2a86fa2-d802-39df-947f-63f0dd70cd65 | -15.47913 | -41.64629 | 2026-02-05 03:51:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 02e96097-7c2d-3553-8649-dee886942421 | -10.65995 | -46.86296 | 2026-02-05 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a14ed00-147b-3804-95db-4d0ae0819a20 | -15.42461 | -41.43071 | 2026-02-05 03:51:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 0fcaa040-78fa-3c4d-9929-4967d40b2bea | -10.89349 | -39.86099 | 2026-02-05 03:51:00 | NOAA-20 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5a3e275-8f63-341b-9203-2e645a0439a9 | -11.00047 | -45.23769 | 2026-02-05 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d1f4839-b6e7-3fca-81f7-b1f4863196c3 | -11.71505 | -40.20109 | 2026-02-05 03:51:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7c5fb202-60f4-31dc-bd33-adc077b46cfe | -13.38913 | -39.96091 | 2026-02-05 03:51:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 09e34585-88ba-35af-a6a2-a464dac4ebe1 | -10.92901 | -45.16526 | 2026-02-05 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 043e2bd7-36b0-3d09-85ce-b4dbc995ed28 | -11.7116 | -40.20058 | 2026-02-05 03:51:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d84a435-ae21-3bcf-9ba8-4fe3455cea6a | -15.42113 | -41.4301 | 2026-02-05 03:51:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f45ab277-7c9f-3ac4-ad13-82e9669bc672 | -12.44532 | -39.51181 | 2026-02-05 03:51:00 | NOAA-20 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1732ddff-bc56-3415-b250-05447d3bc62d | -12.12783 | -40.45807 | 2026-02-05 03:51:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2b53fbd0-5e6a-3446-8a71-fda94e5f2c67 | -15.48228 | -39.137 | 2026-02-05 03:51:00 | NOAA-20 | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac28aa54-36b7-37c9-9a3c-dd3d13ded36b | -10.94348 | -45.13806 | 2026-02-05 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fa1ba29-b7de-3e20-84a8-5b58f34efdb7 | -12.82151 | -39.4366 | 2026-02-05 03:51:00 | NOAA-20 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 36db81d4-d585-3a24-a361-47227f484e2a | -16.43032 | -40.87343 | 2026-02-05 03:51:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c5f612ad-3623-3baf-96af-618e503fbf77 | -13.60343 | -41.08612 | 2026-02-05 03:51:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3196c111-030f-325c-9692-37eaa23e28bf | -18.13381 | -40.21328 | 2026-02-05 03:51:00 | NOAA-20 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82f90a2c-04a7-3453-8533-5c43cfdb6dfe | -14.06206 | -39.49644 | 2026-02-05 03:51:00 | NOAA-20 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0619b4a2-abce-3bb9-95dd-736c495b5a2e | -10.65935 | -46.86622 | 2026-02-05 03:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a0eb1bc-93cd-324f-a5cc-06a5c0046c3e | -16.46914 | -39.10384 | 2026-02-05 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 35328f73-297c-3420-aacf-69dc00dbee23 | -14.05873 | -39.49588 | 2026-02-05 03:51:00 | NOAA-20 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d094209e-62c0-37d6-98e4-fd66abe8f892 | -11.71657 | -40.17028 | 2026-02-05 03:51:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c90f885-06da-3cbd-809a-5e3e9b229f53 | -16.46858 | -39.10742 | 2026-02-05 03:51:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9e9dfdb8-f0ea-37d4-b974-7bd210a021fc | -15.42181 | -41.42608 | 2026-02-05 03:51:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2b5baffe-428d-375e-a9cf-962566b4a80d | -10.92989 | -45.16036 | 2026-02-05 03:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bea19263-4de5-398d-a53a-c36278446458 | -14.05931 | -39.4923 | 2026-02-05 03:51:00 | NOAA-20 | UBATÃ | BAHIA | Brasil | 2932309 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d669778b-e86d-3178-81b5-fc5b4afac8fe | -27.68621 | -48.75235 | 2026-02-05 03:55:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2404c2c7-743b-39f0-934f-a5932f2ee49a | -9.3861 | -35.5406 | 2026-02-05 04:10:00 | GOES-19 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| 577f7468-34ff-38f8-95ae-4877fd7193fe | 4.38755 | -60.59727 | 2026-02-05 04:38:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca8e0392-819a-3b94-bc25-2861e81b4046 | 4.3984 | -60.63299 | 2026-02-05 04:38:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fca1b469-7e34-38ba-b4e9-6fef46a3eba1 | 3.30859 | -60.89891 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 984fc3aa-c2b9-3655-9147-b549c5fb66fc | 2.92099 | -60.75621 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04f043d8-9883-3e9b-821e-90430eb21ae8 | 3.30762 | -60.89216 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2796929-2213-3a30-bf35-e3ba9a513d67 | 3.42627 | -60.73392 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f472f7c2-6735-3d0e-99d8-514aeae3914a | 4.3923 | -60.64058 | 2026-02-05 04:38:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb41db7e-4dd0-3dc1-aae6-d98c494e6e1a | 2.92104 | -60.75588 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 733407b2-1246-32bb-97a4-dd1cf46984ac | 2.92798 | -60.75565 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90b9f6f6-34c1-3bc5-96e1-0c26f328c5e9 | 3.42723 | -60.74054 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dbd08f78-eeaf-3db9-a155-31f38e37b2ab | 2.92212 | -60.76312 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dfa2350f-224c-3200-abce-3f201a6cb0d3 | 4.38638 | -60.58909 | 2026-02-05 04:38:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c23e96b8-bf7a-3f4e-9e8d-d404c813370e | 2.92201 | -60.76338 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec34d406-f3e2-3aa4-b389-3b46fa223a9f | 3.43228 | -60.72641 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8fbc01f7-18f8-37c7-833c-0c98831a3979 | 3.30941 | -60.89224 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cc1c1653-7815-329c-b62a-54826aef253c | 3.31042 | -60.89897 | 2026-02-05 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 962791db-0a33-3b98-9165-20f45d704a4d | 4.38595 | -60.59417 | 2026-02-05 04:38:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README3.md)
