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
| 01716247-6fe2-334b-92a5-c02180c2e6f9 | -11.7988 | -45.3396 | 2026-01-18 03:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 11ad7ffd-34fa-36eb-969e-904f613efdd5 | -13.7477 | -43.66397 | 2026-01-18 03:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6f491d2-548e-3cdd-9533-f1abf0a571f0 | -18.52998 | -39.80231 | 2026-01-18 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ed372ddf-a322-3022-bfd2-ee86c27e1f2a | -14.07442 | -42.4316 | 2026-01-18 03:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6897d7a8-653a-3d18-b260-73aa5f059272 | -14.203 | -43.79759 | 2026-01-18 03:40:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff847b8f-9af3-344c-9d9f-b23149c21fcf | -18.88205 | -40.24155 | 2026-01-18 03:40:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f27d35cf-5fac-34cf-8d6a-5055ab569689 | -17.25804 | -39.28783 | 2026-01-18 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 771c6b8b-812f-3155-a893-b8869dab99c6 | -13.74628 | -43.66198 | 2026-01-18 03:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| be33e156-c6f2-33ff-bbbd-cd39f205ae67 | -13.74279 | -43.66302 | 2026-01-18 03:40:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5bf127df-1f75-3a92-b673-e17399c32e0e | -14.07747 | -42.4297 | 2026-01-18 03:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0c850149-5ef9-3568-9bbb-ce08ae73debe | -14.74682 | -45.90712 | 2026-01-18 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e8c9fa0-1d7c-3423-8901-5bdb983d412b | -14.07301 | -42.42863 | 2026-01-18 03:40:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eda37414-c563-3142-aad2-8fe0cca846bd | -13.99094 | -45.8006 | 2026-01-18 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 664ae3e0-819d-3fca-a9e1-93814fff96fc | -18.8784 | -40.24088 | 2026-01-18 03:40:00 | NOAA-21 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 335a9373-3d61-3361-b462-a5a173c52d18 | -17.25936 | -39.28515 | 2026-01-18 03:40:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 27e721bd-ec5d-3be3-a613-89e87ecb4d13 | -18.17451 | -42.54788 | 2026-01-18 03:40:00 | NOAA-21 | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bc0e2cfe-161e-37cd-b2b3-ef74a3d2bb83 | -14.74128 | -45.90589 | 2026-01-18 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 753a8d89-a97e-3ba1-8b0d-24f9341b27f0 | -19.38722 | -42.69962 | 2026-01-18 03:40:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f45d1bdf-3196-388f-894a-57b380bfac76 | -13.99171 | -45.79683 | 2026-01-18 03:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce87a921-4da1-31a3-8fd0-12f3a605d2ee | -15.82544 | -41.42517 | 2026-01-18 03:40:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8fef2ba2-1990-3d95-9d31-ab96aeab6923 | -21.92915 | -41.21724 | 2026-01-18 03:42:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bf1385a2-c238-3ee6-a15c-81d4b176058e | -22.44673 | -42.08319 | 2026-01-18 03:42:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9e02310-f324-36b1-b270-dd255a089b35 | -22.44765 | -42.07825 | 2026-01-18 03:42:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a98632ec-2032-38f5-b443-22a0bb42baa2 | -5.83589 | -35.64535 | 2026-01-18 04:06:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ae4b1e19-9497-305c-8a64-57490c518b84 | -6.28247 | -35.06056 | 2026-01-18 04:06:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 89cf89e6-193b-3d9e-b60c-47e674452072 | -5.83698 | -35.64236 | 2026-01-18 04:06:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| fe32c669-b6d7-313e-8f62-9ad28641f950 | -6.2809 | -35.07115 | 2026-01-18 04:06:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| fd3e4576-caac-3b2a-b9a3-39c44124ab58 | -6.28195 | -35.06407 | 2026-01-18 04:06:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a03db80c-bf32-3265-9dda-b53387e1887b | -5.88035 | -35.3474 | 2026-01-18 04:06:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1323545f-eb70-329b-a94e-7773ff8e729d | -6.28143 | -35.06761 | 2026-01-18 04:06:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| cf86b22c-8749-3548-8d25-09716554c9d2 | -8.0794 | -35.4188 | 2026-01-18 04:06:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2f36bb5-04b4-31b9-92f8-7b0a0dba66e4 | -6.28546 | -35.06824 | 2026-01-18 04:06:00 | NPP-375D | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e12f3b49-b68c-3586-beb8-3f4c6b0820d0 | -5.83627 | -35.64718 | 2026-01-18 04:06:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ba693abe-7b2d-3a86-b18f-74e7c0129cb2 | -5.87962 | -35.35236 | 2026-01-18 04:06:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 18538b56-0fc3-34e4-a01a-6dfa2acea22b | -5.88125 | -35.35109 | 2026-01-18 04:06:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8c5a8a3-df7b-3378-b9e6-bc79c42857b3 | -5.87731 | -35.35048 | 2026-01-18 04:06:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3435bd8f-cf51-3d89-bbe3-e2fc580a70ce | -5.88854 | -35.61546 | 2026-01-18 04:06:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75e387e4-b80a-3bbd-8bf3-c45975da5c71 | -13.60994 | -43.56096 | 2026-01-18 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c1e0265-887e-3222-a523-f966dc42b5f8 | -12.70898 | -46.79433 | 2026-01-18 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfaa79b8-aa45-3950-99a1-2b3191fd2ac1 | -12.42993 | -43.79099 | 2026-01-18 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 433684ea-c19d-39cc-90c1-938df968ad65 | -13.55021 | -43.70707 | 2026-01-18 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72018c4f-aac2-34ed-a66a-55f0c20f1f2c | -12.71239 | -46.79877 | 2026-01-18 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4515085c-f5d2-3fcd-ab38-02bcb1074769 | -12.70831 | -46.79803 | 2026-01-18 04:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a147b4d4-09b3-334c-b46e-77f2dc6800cc | -11.79217 | -45.35398 | 2026-01-18 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d3d6023-81b8-338c-ad0a-c00243680754 | -14.20326 | -43.79729 | 2026-01-18 04:08:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4248ade6-5756-3951-a093-4540dfcb5279 | -13.40511 | -40.96311 | 2026-01-18 04:08:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 073e9c28-eeb1-32cd-8a5a-2d778ccfdd62 | -11.78676 | -45.36266 | 2026-01-18 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f822ae02-2ffc-3994-b5dd-10bce2de24db | -11.20267 | -42.19697 | 2026-01-18 04:08:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3e54a6dc-7057-367c-9bb7-a1fc2f194b2e | -13.74386 | -43.66134 | 2026-01-18 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d4e9cf1-c60c-3639-9384-95249b38b8d0 | -9.5778 | -44.5946 | 2026-01-18 04:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ebd2e89-d7ee-3bbd-b8c6-89567cd2fcc2 | -12.34899 | -51.2183 | 2026-01-18 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ad2347c-4871-3277-89fa-9dd08d98de46 | -13.5506 | -45.59163 | 2026-01-18 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53f844a7-c769-3676-8db4-56bbcaff8ecb | -14.0045 | -41.94529 | 2026-01-18 04:08:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 682a0844-65cc-3e44-85b9-3e1b92678e78 | -13.55019 | -45.59377 | 2026-01-18 04:08:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 969b35d9-4955-32d3-9140-1a1db66fa340 | -13.74729 | -43.66193 | 2026-01-18 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 763230ec-6570-3401-a83f-bc674959f909 | -13.99046 | -45.79865 | 2026-01-18 04:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9b28a15-b3e6-3e21-85a4-3cc8133bcd4f | -13.64684 | -44.31072 | 2026-01-18 04:08:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1462aaff-9758-3293-9f26-8d3ca6abc986 | -14.07677 | -42.42988 | 2026-01-18 04:08:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2eb3aaf2-3438-3341-b1e3-3c9a12a51e1f | -11.78756 | -45.35801 | 2026-01-18 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ac6e09c-0dcc-3906-9de5-891e5ecf32f5 | -11.79296 | -45.34937 | 2026-01-18 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 44dcf2a4-1813-3a46-8761-f1ec10e9dec8 | -11.14319 | -40.72522 | 2026-01-18 04:08:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 34ccd016-aa3e-38b4-bbed-128c11ee5b70 | -12.3497 | -51.21466 | 2026-01-18 04:08:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 40907eef-4d39-3854-85e7-55c130e38df9 | -14.07344 | -42.42931 | 2026-01-18 04:08:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2223e847-f517-3942-94eb-b86588b6a239 | -9.20977 | -35.78419 | 2026-01-18 04:08:00 | NPP-375D | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0550cba-2fc5-3122-b2d1-d1521ba1c817 | -11.7988 | -45.3396 | 2026-01-18 04:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e1d1fbca-6797-31db-951f-c93f5f5300b6 | -14.77859 | -45.94311 | 2026-01-18 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13651f6a-7c29-3200-bd48-f72624db661e | -18.52877 | -39.80466 | 2026-01-18 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0236278c-c3f5-3fd1-8d41-efa8dddf7b3a | -18.17581 | -42.54799 | 2026-01-18 04:10:00 | NPP-375D | JOSÉ RAYDAN | MINAS GERAIS | Brasil | 3136553 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b57ee28c-d0ec-381a-aa29-506f97333d78 | -16.91608 | -51.28574 | 2026-01-18 04:10:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 35dfc379-0612-3850-b3e7-b5d83c98c794 | -20.84081 | -51.74179 | 2026-01-18 04:10:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6511ff2e-b69a-35c9-b4ad-38ed3a3ab048 | -18.81125 | -51.60846 | 2026-01-18 04:10:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e052b524-ac5a-3cb0-b0ba-46791583a28b | -18.81746 | -51.60349 | 2026-01-18 04:10:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc50e6ea-ff61-3035-a9dd-941722067537 | -22.44581 | -42.08059 | 2026-01-18 04:10:00 | NPP-375D | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dfdde8cc-e5df-3fa8-a3aa-ef3ca57edf71 | -18.81246 | -51.6025 | 2026-01-18 04:10:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c2a9b59-85e2-3605-8706-5e2137184351 | -14.74298 | -45.903 | 2026-01-18 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18c40512-1a9a-3bc4-9e5b-459336982f51 | -19.3866 | -42.69971 | 2026-01-18 04:10:00 | NPP-375D | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2d4b468b-30c9-3d3c-a345-5c1d5017c5b8 | -18.87901 | -40.24316 | 2026-01-18 04:10:00 | NPP-375D | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 28d9eaa5-94a2-3f22-99e7-428b1bd50764 | -15.82365 | -41.42592 | 2026-01-18 04:10:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 815c3bd6-1b0f-3a33-86bd-eb6e95ea2301 | -14.78166 | -45.94584 | 2026-01-18 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3409d0fb-023b-304c-ace9-071ab0a317d5 | -14.74672 | -45.90371 | 2026-01-18 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc5d4b53-8332-315c-8770-a08835c0daeb | -20.84282 | -51.74298 | 2026-01-18 04:10:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 19ebc261-d27b-3e6b-8f83-79b27de68135 | -14.74592 | -45.90833 | 2026-01-18 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 183946b5-abf6-3ecb-bfec-b584584701a1 | -22.44924 | -42.08111 | 2026-01-18 04:10:00 | NPP-375D | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0373712b-f907-3dcc-8df5-582fe96d034a | -15.95017 | -47.68519 | 2026-01-18 04:10:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 632e60e1-85a4-323e-8999-49ac69f21d5b | -16.91107 | -51.28443 | 2026-01-18 04:10:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 37470fb4-afab-3103-b1e8-de230004eac7 | -18.81146 | -51.60503 | 2026-01-18 04:10:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b963c0b7-e959-358d-be04-a298502735a9 | -14.74217 | -45.90761 | 2026-01-18 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46432b06-a84c-33de-ba63-1fa3d2245492 | -14.78234 | -45.94381 | 2026-01-18 04:10:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c587c18-2e5f-305d-94a1-912e6f64f7fc | -20.844 | -51.7374 | 2026-01-18 04:10:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 85e12c9d-f8d0-3d78-b221-46843cc563ff | -21.92856 | -41.21781 | 2026-01-18 04:10:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 65fddb60-dd91-3465-8291-d54f824cf37c | -15.01469 | -43.52055 | 2026-01-18 04:10:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5842792b-2afb-32bf-8d1d-31dc2c08b462 | -18.81646 | -51.60603 | 2026-01-18 04:10:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 215e9c7c-3b46-32a1-b875-53894341000b | -15.827 | -41.42647 | 2026-01-18 04:10:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 40ec1afc-3a91-3653-bc8b-2b04ebf636c7 | -27.51301 | -50.64766 | 2026-01-18 04:12:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8872c333-356c-38c6-a507-31125d4a484f | -27.51817 | -50.64272 | 2026-01-18 04:12:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 6a312eaa-b91b-35d3-9e93-d06dbad39946 | -1.52207 | -46.69611 | 2026-01-18 04:25:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d02977-a6e2-32ec-b9c8-22c95a8ad8db | -4.6913 | -46.4162 | 2026-01-18 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ec88fc-672a-3f2a-860e-4fbcf313f76e | -5.83664 | -35.64447 | 2026-01-18 04:25:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91f0bfe2-9f60-3cac-857c-223215c871d9 | -12.07373 | -45.3041 | 2026-01-18 04:27:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5beca6e6-1f35-3e16-8e63-64a35254815f | -5.25543 | -44.74858 | 2026-01-18 04:27:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
