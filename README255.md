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

## Dados Diários - Página 255

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cd19183-78c3-3822-8de7-0fa547829925 | -14.36838 | -39.84272 | 2026-10-08 16:16:00 | NPP-375 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 897d4596-2d8a-34f2-ba12-31c9e1adf24a | -14.35157 | -39.35844 | 2026-10-08 16:16:00 | NPP-375 | AURELINO LEAL | BAHIA | Brasil | 2902401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1594f64e-27d6-3b45-a773-0c2b795d9d20 | -18.12961 | -42.38692 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 644efc2d-2f4e-3884-8038-e53361225c99 | -15.47968 | -41.00437 | 2026-10-08 16:16:00 | NPP-375 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 60556c7c-a31e-3563-a0f9-99edc87f868b | -15.05947 | -41.25253 | 2026-10-08 16:16:00 | NPP-375 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d66c75ac-3e2c-34dc-a160-ee528ed9418d | -15.53305 | -40.62484 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7d3b45ed-4462-3217-852a-b8f73adbe9ad | -15.06567 | -41.35327 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 16300dae-7bd1-3712-bfc8-891cbd8d76fb | -16.37215 | -39.80824 | 2026-10-08 16:16:00 | NPP-375 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 46.5 |
| c597da86-47cb-3a5b-b7d0-eee8d9842269 | -17.13949 | -41.50074 | 2026-10-08 16:16:00 | NPP-375 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 057fac12-314a-35ff-8a21-520fd52b80e9 | -15.88122 | -40.77918 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d4c9d335-af42-3638-a3d0-f344c12ee262 | -20.4468 | -42.5283 | 2026-10-08 16:16:00 | NPP-375 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 2bfec02b-1f6b-3a70-8b50-6793a697802a | -14.97322 | -48.19792 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 3c2c3c2e-ce5a-3cc9-b09d-31660aededc3 | -14.75527 | -39.80985 | 2026-10-08 16:16:00 | NPP-375 | SANTA CRUZ DA VITÓRIA | BAHIA | Brasil | 2927804 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 91af9be3-48ba-350c-af01-19a5da5ee695 | -15.63075 | -40.12927 | 2026-10-08 16:16:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 2c94d68e-159c-37d5-9620-89ec8da6f155 | -14.45921 | -41.32629 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| ff0e6015-b8ef-3bc5-a884-796d8fb5d54d | -14.96733 | -48.19896 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d9abe0f9-c1d0-3bd7-8824-c2f59eed46f4 | -15.26259 | -42.34572 | 2026-10-08 16:16:00 | NPP-375 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b5db908a-f501-39b8-9afa-c4c3bafafb71 | -15.11008 | -43.63566 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 75636152-fe7d-328e-8b31-27738d3fbc63 | -14.96646 | -48.19058 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0c7f9917-2f0c-3dd4-bafd-df587fb1f5c1 | -19.64102 | -42.04829 | 2026-10-08 16:16:00 | NPP-375 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d1815c33-ec40-3424-a06d-db3fcec0eae5 | -16.04827 | -40.64952 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c5a1c725-d3a0-378e-bf91-561478e2b924 | -16.0296 | -39.82423 | 2026-10-08 16:16:00 | NPP-375 | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| be6f07a4-a309-3034-a34c-269c34b90e01 | -14.44307 | -43.92326 | 2026-10-08 16:16:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 009f4e90-9701-3789-ba0b-97a8efcc8783 | -15.60516 | -40.50607 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 8524afed-52cb-39d8-ae89-6909d79d6c7c | -14.42967 | -41.13625 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 59bd00bb-f008-3ded-9411-a39224c60ae5 | -14.99935 | -44.05829 | 2026-10-08 16:16:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 24.5 |
| fa965bd7-77cb-3641-afbb-a7f9b3444cde | -15.04542 | -40.24026 | 2026-10-08 16:16:00 | NPP-375 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 57fb80e0-79f5-3804-9e45-01a1b8b035a9 | -18.33838 | -42.3819 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 34c311f2-d189-3675-9cbc-3f0cadbcdb78 | -17.36984 | -45.44617 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 314c3648-de47-36df-aa14-4a69370d0a3b | -15.10516 | -43.63192 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 40.8 |
| f7a08b6d-67de-3adc-b87b-39f708d4cfb4 | -14.44692 | -43.91833 | 2026-10-08 16:16:00 | NPP-375 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 49026dcc-f82d-353c-88b1-422bade870aa | -15.09267 | -41.35524 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| a2bc6ba3-d49f-3171-b299-9ad95e1b5bbc | -17.02591 | -41.06055 | 2026-10-08 16:16:00 | NPP-375 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b5f86ca9-dfec-3c71-8bd3-bd8466cddd56 | -16.15014 | -43.12025 | 2026-10-08 16:16:00 | NPP-375 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2efc4158-4e93-395c-8387-b346da33f345 | -14.42263 | -41.51054 | 2026-10-08 16:16:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 3d9ba351-b91e-3bbf-bb42-aab4389db933 | -17.42673 | -40.41786 | 2026-10-08 16:16:00 | NPP-375 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d8b4b04f-fcb6-3d4d-99db-52c4b894c9e2 | -14.73389 | -40.28703 | 2026-10-08 16:16:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 908935cf-0d38-3332-a804-c4340d65b951 | -15.63019 | -40.12526 | 2026-10-08 16:16:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 7975aad2-00fc-38fa-b4c4-aa71ff2f5989 | -14.68411 | -41.06401 | 2026-10-08 16:16:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fcc7136c-e5c4-3a9f-a28e-f5d43eb7edfc | -15.54834 | -42.35512 | 2026-10-08 16:16:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb81a5b1-dca2-3480-96c8-899508539ac2 | -18.22776 | -42.3136 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1d9cc119-73a7-3903-a83c-268ce22c70c5 | -17.22066 | -39.38115 | 2026-10-08 16:16:00 | NPP-375 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 61899e5f-9e79-3452-89d7-22c39dddfb41 | -14.73279 | -40.28791 | 2026-10-08 16:16:00 | NPP-375 | NOVA CANAÃ | BAHIA | Brasil | 2922706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fcd6971e-8c42-3a32-9f22-6416d4e7988c | -16.70788 | -41.88197 | 2026-10-08 16:16:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| dec891fc-03eb-3838-a993-50cc54d64063 | -16.00298 | -50.04591 | 2026-10-08 16:16:00 | NPP-375 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fae56d0c-b7fa-3697-875b-bd372e00a06d | -16.29601 | -49.14312 | 2026-10-08 16:16:00 | NPP-375 | CAMPO LIMPO DE GOIÁS | GOIÁS | Brasil | 5204854 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9bcac176-6782-30b7-acdd-65e28c497ff9 | -14.17787 | -43.43281 | 2026-10-08 16:16:00 | NPP-375 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 56d7fa4c-92a5-344f-918a-04973fa108ac | -20.58539 | -48.45613 | 2026-10-08 16:16:00 | NPP-375 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bd5b5d85-5286-3f93-995e-d95840a1566a | -14.73684 | -41.7958 | 2026-10-08 16:16:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 7169eb98-8cee-3b09-9cc3-e1d992097079 | -19.07076 | -48.64517 | 2026-10-08 16:16:00 | NPP-375 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7d95645f-51ca-3f2e-8757-49f9adfa7573 | -15.39176 | -44.33669 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0807c042-6a3e-398f-871b-8bd3bf93e069 | -20.95199 | -44.77561 | 2026-10-08 16:16:00 | NPP-375 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 1b20811e-11a8-3b45-9f9c-9d68bcdbfae7 | -18.07845 | -41.48267 | 2026-10-08 16:16:00 | NPP-375 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5dafe834-9af5-3a7c-ae2f-8310d9759f24 | -16.1495 | -43.74442 | 2026-10-08 16:16:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8598db42-a280-32e9-be3d-0824a498b776 | -14.536 | -41.27318 | 2026-10-08 16:16:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 7285b068-a36c-3159-84da-409d44194ca8 | -15.38077 | -40.76337 | 2026-10-08 16:16:00 | NPP-375 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d419dd26-3b66-3f3a-97ca-4f107127f999 | -14.94224 | -48.10954 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d20fe9c7-8e56-33e9-aaca-c1abf279fdfd | -18.04227 | -44.59978 | 2026-10-08 16:16:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d9fa2247-34e7-32a9-bb7a-5105b7ad257d | -14.99876 | -44.05371 | 2026-10-08 16:16:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 43.0 |
| 25f6199a-a454-3a5d-a201-2110b569c2df | -15.10899 | -43.62703 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c80d1427-4748-3c44-9fbd-76698cafc874 | -20.11828 | -42.03131 | 2026-10-08 16:16:00 | NPP-375 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0d1f5ee6-4209-32ed-8142-94431c195607 | -17.18646 | -44.43622 | 2026-10-08 16:16:00 | NPP-375 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 37f00ef5-4b89-3603-8b03-9cfac4005f76 | -16.51114 | -45.10896 | 2026-10-08 16:16:00 | NPP-375 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cc5e53a8-e295-36ca-be02-9a1dd0610c6e | -14.77897 | -42.65656 | 2026-10-08 16:16:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| fe23a519-ed98-3618-9330-bbe01889312d | -15.38773 | -44.3421 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 05ee8245-be23-3938-89f3-3f753e343e22 | -14.87885 | -41.53142 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1203a15a-18be-3137-b860-aecc474b77ba | -16.31434 | -44.55966 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 818bb0ab-6963-34d8-83f3-44769a4e8f1a | -17.69664 | -39.16644 | 2026-10-08 16:16:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 389990b1-9655-3635-82ed-9002adfa52bc | -19.7004 | -42.18199 | 2026-10-08 16:16:00 | NPP-375 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| adb779a9-1f7b-31cb-a0bb-38b010043551 | -15.63135 | -40.13353 | 2026-10-08 16:16:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| d1a2107a-4581-3ded-a4bb-3a0936a6d3ca | -17.26247 | -41.19637 | 2026-10-08 16:16:00 | NPP-375 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 350d208c-d101-34bc-9168-72fa3f9150be | -14.85669 | -42.0664 | 2026-10-08 16:16:00 | NPP-375 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| e3bb27d1-8751-3f9d-b888-b78d14abe4c5 | -18.12946 | -42.38719 | 2026-10-08 16:16:00 | NPP-375 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| edb7f611-6a00-3119-ac3d-e01549eedcb8 | -14.9352 | -48.09982 | 2026-10-08 16:16:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9180a84b-26c0-3e8b-8fcf-0295810b5190 | -14.95221 | -41.47824 | 2026-10-08 16:16:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7201a06b-1df7-35db-bae4-57a5ab8ef73c | -15.00326 | -44.05312 | 2026-10-08 16:16:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 844ff237-b764-37b0-a63e-891c4dea1eb4 | -15.62778 | -40.13414 | 2026-10-08 16:16:00 | NPP-375 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| fcd364dc-cc17-30a2-bc08-bd222d35390e | -20.11836 | -42.03297 | 2026-10-08 16:16:00 | NPP-375 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 85f737ad-1c97-30a9-a327-9c69190d9482 | -17.69681 | -39.16679 | 2026-10-08 16:16:00 | NPP-375 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 5bad4aa5-f496-331c-9c9b-0d44097ef691 | -16.7187 | -44.898 | 2026-10-08 16:16:00 | NPP-375 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be2ce3e1-41df-3cfe-8d45-c4fe65af77af | -16.31906 | -44.55892 | 2026-10-08 16:16:00 | NPP-375 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| af5aa08b-d41c-3934-8372-3af66ed0d411 | -16.05135 | -40.64461 | 2026-10-08 16:16:00 | NPP-375 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 962098bc-985b-3147-af71-8af7a24b586d | -15.82278 | -45.41217 | 2026-10-08 16:16:00 | NPP-375 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 70755c75-aecf-3602-8fc0-8641218dbd26 | -15.56309 | -44.51685 | 2026-10-08 16:16:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 16b64b37-a6ec-3cd1-a1e8-a283f85a797d | -14.5553 | -44.07255 | 2026-10-08 16:16:00 | NPP-375 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 6c8efd32-3a12-368e-8887-e01e613d87eb | -17.94957 | -42.31753 | 2026-10-08 16:16:00 | NPP-375 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 496885a5-e34d-3de9-9728-e55eba523da0 | -15.51681 | -42.65342 | 2026-10-08 16:16:00 | NPP-375 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| f8670468-fff3-3f55-afb5-75e1389e5250 | -16.93092 | -42.11011 | 2026-10-08 16:16:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 65d9ddf9-9153-3635-8673-7a79bd737f92 | -16.20952 | -40.36771 | 2026-10-08 16:16:00 | NPP-375 | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 61ff8053-e742-3770-ad82-5e91ba86a6bf | -16.19572 | -44.57675 | 2026-10-08 16:16:00 | NPP-375 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 27f285eb-e6f2-3ec2-bba6-46b2c85bb8e0 | -14.15716 | -42.10242 | 2026-10-08 16:16:00 | NPP-375 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| da2af208-33b0-3ec6-9971-677f76861429 | -20.95006 | -44.77753 | 2026-10-08 16:16:00 | NPP-375 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 119ce9ab-58ed-3f72-809f-de34acc28e6f | -13.83474 | -39.58483 | 2026-10-08 16:16:00 | NPP-375 | NOVA IBIÁ | BAHIA | Brasil | 2922755 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3b56e304-aad4-3863-8c5a-f6d50c456cf3 | -14.55589 | -44.07713 | 2026-10-08 16:16:00 | NPP-375 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 7cd86504-5707-364a-a8eb-d741e973f221 | -15.54077 | -43.17413 | 2026-10-08 16:16:00 | NPP-375 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 7ae1f0c6-3143-398f-bbd5-cb65c36213fe | -19.22675 | -40.68255 | 2026-10-08 16:16:00 | NPP-375 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 907f6e1c-b77c-3940-883f-18d8b3f9d423 | -17.36544 | -45.45306 | 2026-10-08 16:16:00 | NPP-375 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd5b8de6-5e14-387f-adb1-42f47471d90f | -15.63542 | -39.73163 | 2026-10-08 16:16:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| fd4672c9-f92d-38be-8851-9a141680cfa5 | -21.54748 | -48.33422 | 2026-10-08 16:16:00 | NPP-375 | DOBRADA | SÃO PAULO | Brasil | 3514007 | 35 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 4e33dc6a-e0a9-3690-9f3f-f0b1e0b931a2 | -15.11282 | -43.62212 | 2026-10-08 16:16:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 9.9 |


[Clique aqui para ver as próximas entradas](README256.md)
