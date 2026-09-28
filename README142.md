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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2ff5e0b-48c3-32e8-bfc2-b0658cabacb0 | -24.4121 | -50.87385 | 2026-09-28 17:07:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 911e6557-d304-33ba-8540-499f481dc72e | -15.0796 | -54.59854 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 5e25542d-10dd-3d79-8ab5-4ad88689b4bc | -15.16272 | -43.60395 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 491a5d0a-7333-323c-a6a0-3ee681000510 | -15.19099 | -46.13911 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b832ebd5-82ec-3889-bc7f-e05cb6894096 | -19.02888 | -46.96967 | 2026-09-28 17:07:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| bd94a774-f6a6-3086-860a-2849705e0856 | -15.77967 | -52.45504 | 2026-09-28 17:07:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5da5ad7b-8cd9-39de-bf14-85759d54f1de | -12.651 | -47.24919 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| ad564c51-d276-38b5-800c-8e456a45f0fd | -12.44491 | -48.21852 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7936ddac-5f0a-3062-9990-4cfde9e6984f | -16.68363 | -51.31907 | 2026-09-28 17:07:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 572a92ba-0874-310f-a094-10abc2d2b376 | -15.1502 | -43.57602 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 1b475915-2baa-3c6e-88ce-f1540899aff3 | -16.14971 | -43.63239 | 2026-09-28 17:07:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| bf4d802b-cc5c-3aa3-a228-154c57b7f931 | -11.35123 | -43.42467 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1805a9b2-486d-3df6-afdb-8f0a0a3527ff | -16.54341 | -41.46101 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| a15b8226-37e7-3543-adb0-4cf74e4a7141 | -11.37298 | -43.42062 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7b0cc98e-a7e9-3bb6-8df5-83e05ec7b886 | -15.13026 | -43.61804 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 76675821-8ed6-3db8-83fa-b61098744fb7 | -16.51548 | -42.44872 | 2026-09-28 17:07:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1b720a96-3579-3c43-92b4-e5cf7a8a9451 | -11.6973 | -43.42064 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1ec4cf3a-8c5c-367b-be86-70a8b254ef05 | -12.61937 | -47.27878 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 310f7536-dac8-3279-8bed-bdd2a7cd3029 | -13.48937 | -48.60155 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 19884d3b-6f2d-3a46-b330-a9adc825390b | -13.90516 | -53.67633 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| bfb868af-a150-3fa6-85ec-e3647cdee114 | -17.21625 | -53.33066 | 2026-09-28 17:07:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c55cbd2d-d885-3836-8021-2993a9fb7351 | -12.63925 | -47.26096 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b1b1d0d5-de68-3f45-9457-775599d0db20 | -11.71631 | -44.51843 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 702b8218-c281-381c-91af-ba8c6fe3d389 | -18.10727 | -44.3642 | 2026-09-28 17:07:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7e72e833-84f4-319b-95d1-0c2255e3eef5 | -12.97733 | -51.08743 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 3b2999ec-50c0-3012-9536-8951a106defd | -12.64677 | -47.35339 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| b01a7e40-a9e9-3044-a286-9af37896e447 | -14.6623 | -52.09952 | 2026-09-28 17:07:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93141c19-3b60-3d68-96c1-84e4eab6b0f1 | -12.7389 | -47.78998 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d639fc87-ebd1-3c67-84ef-98f4362699f4 | -16.15311 | -43.63246 | 2026-09-28 17:07:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 536e74f6-5040-3424-8ee3-92435846bf4a | -11.63911 | -43.49062 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2e682ac9-0154-3256-a50f-bd51f83736d3 | -15.14396 | -43.63012 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d52a6279-927a-3297-93ef-168e8277ffb8 | -15.45127 | -41.44987 | 2026-09-28 17:07:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 8bc1369b-c1c3-3a6d-a81d-a8b1d303795d | -13.46145 | -48.58483 | 2026-09-28 17:07:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ce833aba-b4f1-3822-b6ed-a55789236a1c | -15.56098 | -47.9241 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 681257d3-518c-39f9-a2fe-efc6aec4211a | -13.31317 | -43.95734 | 2026-09-28 17:07:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ca218c11-08ab-3150-8caa-58707ff76013 | -11.963 | -44.88008 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9968634-8ed8-3221-b9e2-335421eb9d71 | -16.54771 | -42.36849 | 2026-09-28 17:07:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| af5260b1-f90d-325e-999b-d5238977e2e1 | -17.3043 | -44.52962 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 25fda4bd-e635-3866-b04a-8e836338659e | -18.39386 | -43.43494 | 2026-09-28 17:07:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f2efc034-c259-3eba-b2b9-f551065b46e5 | -13.32202 | -43.94432 | 2026-09-28 17:07:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34a34994-461c-3e3a-8b05-a410124e2b12 | -14.08529 | -46.32823 | 2026-09-28 17:07:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a5d3f53f-a309-364d-b242-81db71e1c616 | -12.75461 | -47.34816 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| e312ee41-b2e5-3b71-b8c1-988b1187c526 | -15.39978 | -47.91122 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 26590304-6c06-3792-9b2e-b423e59fd170 | -12.44069 | -48.21928 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f12c7415-c2e4-37a5-9c39-4a91e9bfc876 | -12.55083 | -42.0408 | 2026-09-28 17:07:00 | NOAA-21 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 58.9 |
| fb075dca-563b-3719-93d6-6279f02fbbf1 | -12.32728 | -42.24522 | 2026-09-28 17:07:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 21b9310f-9874-3d29-a052-be7a890a7280 | -12.7114 | -46.98185 | 2026-09-28 17:07:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b7760b1-d267-3b75-bb33-9f2b6243451a | -13.94991 | -49.07996 | 2026-09-28 17:07:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 2e3f119d-6c69-351f-ab2a-d0e220d39d94 | -16.7098 | -55.33436 | 2026-09-28 17:07:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.7 |
| 527cfdce-fc12-345d-a496-09b24ea99dbf | -15.15581 | -43.59784 | 2026-09-28 17:07:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 31.2 |
| c62253ca-6c7a-3d6d-896e-798f1a589709 | -11.67809 | -43.5049 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 4f6fdd21-76a7-3e05-bef7-e1c3c8f2ef3e | -13.2618 | -47.44519 | 2026-09-28 17:07:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf380aef-9b41-375a-b210-d1624ee1ebb0 | -16.35459 | -42.57812 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 623a01ec-5ff3-3179-98b2-9bd1d4659389 | -13.08868 | -48.56001 | 2026-09-28 17:07:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e734b2c3-8205-3f6c-9926-b15544e35456 | -16.35609 | -42.57453 | 2026-09-28 17:07:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 3d485951-22d9-37a8-8afb-888dd8a9acd4 | -12.90405 | -52.06439 | 2026-09-28 17:07:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a8f015f2-2ddb-3abf-a4ff-a980b39d4be9 | -15.40439 | -47.93718 | 2026-09-28 17:07:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b1fff13a-5245-3bd9-aa7a-19f8f4e5f05e | -11.70152 | -43.47303 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 827eccdb-c1d2-3f4f-989a-2b02ca8b13cf | -13.33276 | -46.8106 | 2026-09-28 17:07:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 3df201a7-c444-3dfb-991f-3e53a130aa1c | -15.72499 | -42.6243 | 2026-09-28 17:07:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 94b874e9-3d54-3433-b2d4-82382df1b852 | -13.68692 | -48.81986 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 72482fb9-eb2f-3df9-9c06-b65a99ee86ff | -15.89788 | -42.9525 | 2026-09-28 17:07:00 | NOAA-21 | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8f225a78-8c1e-3abd-8aa3-19d123974261 | -24.66897 | -49.61554 | 2026-09-28 17:07:00 | NOAA-21 | DOUTOR ULYSSES | PARANÁ | Brasil | 4128633 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 7884beb9-c6bc-3b98-8d6d-ac5a8e330297 | -12.98787 | -44.73717 | 2026-09-28 17:07:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 926b9f89-fb20-3537-98d6-704d65cd00f1 | -11.68703 | -44.51312 | 2026-09-28 17:07:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0eaaa724-8487-390a-9fd1-7ceac5a9f8cb | -15.27268 | -41.21003 | 2026-09-28 17:07:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| d2a92463-c30f-38e1-b85f-ceb9afe903d8 | -12.75671 | -50.6866 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 51a7a936-0adb-34b7-97f2-72067adb9aa5 | -12.64653 | -47.25002 | 2026-09-28 17:07:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| bcf2491d-fb3f-328e-bf29-48f4549f4e09 | -14.11161 | -43.92653 | 2026-09-28 17:07:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| f0c607b1-cf58-3b95-9d40-4a86fbcd4dd0 | -11.9577 | -44.88113 | 2026-09-28 17:07:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c871d3a3-b78b-37bc-9f37-77ce9a9e9b31 | -24.70947 | -51.32882 | 2026-09-28 17:07:00 | NOAA-21 | CÂNDIDO DE ABREU | PARANÁ | Brasil | 4104402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 2c5a6b0a-0022-3464-9e50-3d11d2b9199d | -15.55349 | -47.92926 | 2026-09-28 17:07:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 69c80fb8-4ebb-36e4-b4b8-b5aaaf7e4298 | -15.11644 | -54.70858 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 9fdd870c-4faa-3c25-bf0c-46174991fb46 | -14.48166 | -53.64717 | 2026-09-28 17:07:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b4e6a4c2-bd0a-3f6f-b145-7ab4b632a2b3 | -13.68753 | -48.82335 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3f1c342f-d27b-3707-81d3-b76eca98638b | -16.09136 | -47.86499 | 2026-09-28 17:07:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2ef16f06-f3cf-311b-91bc-40c8949a3708 | -11.38639 | -43.42683 | 2026-09-28 17:07:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 03663115-2001-317f-894c-c4ae0112a305 | -15.08294 | -54.59803 | 2026-09-28 17:07:00 | NOAA-21 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 341eeb2c-9114-3ba5-8135-95f184331160 | -15.1881 | -46.17479 | 2026-09-28 17:07:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bdaf35a1-1bf1-36aa-83e7-7ab4667edb29 | -13.88888 | -48.1097 | 2026-09-28 17:07:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2aa06529-4f72-3d9e-a610-e15970764813 | -14.31943 | -44.82141 | 2026-09-28 17:07:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| afeb8bf6-56cb-325b-88f3-4673425c56d6 | -16.90816 | -42.10448 | 2026-09-28 17:07:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 01824e3e-d7fe-3a15-8f43-e9ed619093dc | -12.43622 | -44.14119 | 2026-09-28 17:07:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| afc9ef88-d431-3bec-a125-cfd6f70108e2 | -14.54045 | -48.31094 | 2026-09-28 17:07:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0122a60a-d142-30dc-9e79-c47a68feb5ac | -12.7263 | -50.68303 | 2026-09-28 17:07:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| eecd7a7c-47fc-3e6a-90d9-52527d44cddc | -17.30569 | -44.52882 | 2026-09-28 17:07:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 27.2 |
| bec0d1ec-bdd4-3d10-8ebb-a915a496102b | -10.70142 | -50.82927 | 2026-09-28 17:09:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 15dac5cf-ac55-3f25-b696-72d125918c70 | -6.01346 | -53.89589 | 2026-09-28 17:09:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fc4e7331-c43b-37b4-b87d-b8f6ef8249a4 | -8.63283 | -49.47961 | 2026-09-28 17:09:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 24afa03e-741f-3c92-8412-753a0d293322 | -8.92974 | -45.05319 | 2026-09-28 17:09:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| ebedc4f8-1ad5-3c78-8216-f8054213990f | -10.20692 | -49.99628 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ff936b08-72cb-3ca4-a912-c150a32418a3 | -6.33787 | -55.98591 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 13967536-f5f7-3dc7-b158-5b56fb73c6ca | -10.08913 | -50.3913 | 2026-09-28 17:09:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a6fef6f1-7623-3a5a-838a-2db79f59fdb1 | -6.16937 | -52.90223 | 2026-09-28 17:09:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6dd58e4d-bd7d-3c14-bc00-32f705ecb334 | -12.06759 | -48.54515 | 2026-09-28 17:09:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 94c4ec21-d160-3c5b-8f99-bd0738d6bf92 | -10.95803 | -45.5622 | 2026-09-28 17:09:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5917580f-0b43-39be-990c-d77bfd9f3fe7 | -6.48544 | -55.97338 | 2026-09-28 17:09:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 02b19e4f-ede5-3c22-8bd2-ca7e60046a03 | -10.20525 | -49.98626 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| be8b0b0b-3886-351b-98b7-2e57cb8f8e7b | -11.5414 | -47.39207 | 2026-09-28 17:09:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 6aaf9329-d7cc-3b52-b93c-a6ea93c7411d | -10.29104 | -49.96842 | 2026-09-28 17:09:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |


[Clique aqui para ver as próximas entradas](README143.md)
