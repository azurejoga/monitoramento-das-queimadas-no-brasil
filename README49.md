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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea0880a0-f8ca-38b9-9fd8-8b5656790140 | -11.92509 | -46.76923 | 2026-10-10 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f5b10c4-2bd0-3f7d-ad0b-051dd712a5b8 | -11.33159 | -47.80158 | 2026-10-10 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3421fd0d-73e1-3723-9cca-1de811efd222 | -11.60381 | -43.7187 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f3e9921b-da59-3fdb-8825-da62fbdc663c | -13.91406 | -48.91454 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9966f22d-fe8a-3866-8667-adbdcd1945c0 | -14.46012 | -43.95116 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| edd09787-b8b4-382a-aa5d-137afcb90997 | -11.17664 | -45.31919 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| da2b4b16-238a-3b93-a57a-4228f716ecb7 | -11.03034 | -44.02412 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 613750b4-c47b-33c7-989c-78a5f0ada991 | -14.45407 | -43.94652 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3d8dfa0a-f799-334d-bddb-2b2193b03dca | -11.60207 | -43.7512 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bc976278-5cfd-3d1a-8113-41f9eb4632b7 | -16.76289 | -47.07486 | 2026-10-10 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65054e76-26ea-3a5b-acb6-3c44ceb7b0a5 | -11.83197 | -43.52477 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 32b44786-7c9f-3cd0-addd-ed08186f97fe | -13.10816 | -46.35312 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb6c4f26-f4b4-34c1-9170-9bf6d681df4e | -11.98293 | -49.10458 | 2026-10-10 04:10:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5026a980-889c-36ff-ac0e-602dbd3ce046 | -15.85121 | -42.03018 | 2026-10-10 04:10:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 816cd2b0-99b9-3c99-93a9-7c565c779e12 | -12.37957 | -46.5731 | 2026-10-10 04:10:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8eadb3c-9805-3c13-a0c4-e7a5e781c68d | -11.82744 | -43.59632 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 834b0082-a875-39d9-9964-3cb3795d688b | -13.25946 | -44.01056 | 2026-10-10 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52936347-eb45-36da-8618-ff95d21db981 | -11.28483 | -45.19568 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66e21363-e0da-3343-92e9-6bb9cec4bdb3 | -10.89324 | -44.79878 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 646dbc47-ce71-3ad7-ab03-6f680ff4caf3 | -13.36759 | -43.90823 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ced2927-2e95-3c46-ab89-c7c1050c828c | -11.05553 | -44.10221 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 918b2b79-c4c7-3791-bdda-b3bd194d1bd8 | -11.58572 | -43.63975 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01fa3b0a-2d7c-3841-9990-a99b29ecc624 | -11.57176 | -43.70626 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79cc4064-8052-358a-a0ed-1a15ea8ee66b | -16.11561 | -42.85175 | 2026-10-10 04:10:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cc07f46-a019-3ee3-a55e-b02be995c209 | -11.78724 | -46.72393 | 2026-10-10 04:10:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8be7d049-02c7-3fec-820f-503226fed6dd | -18.0935 | -42.26148 | 2026-10-10 04:10:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 73b51982-635f-3cfa-8497-7e0c8f61bd58 | -11.68901 | -43.65344 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a4cd381-d6a6-39b9-857a-55e5e5eefcf1 | -11.33555 | -47.80233 | 2026-10-10 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71091bb1-32e1-31c9-956f-cdd0b92e9a36 | -11.83845 | -43.61258 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c040167-281d-3d13-a160-d6022fe1ca95 | -14.33576 | -55.00977 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4627016d-8557-36ac-a53c-f3d1fd2888b9 | -11.24348 | -44.87119 | 2026-10-10 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e0f76f8a-f99f-32ca-a8eb-c418b4b75ceb | -11.56017 | -43.69358 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 791c4d74-4efd-32fc-acd6-ff2a5585c33a | -13.36653 | -43.89352 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f30f1dad-22cf-3dc8-abdf-22a9337ddfab | -11.45696 | -43.37707 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f2a74fa-da3a-3621-b097-6bbfc1c74ba3 | -13.33361 | -46.33068 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b18819d0-5dbb-38fb-98dd-a8064ae98f4e | -11.59662 | -43.72113 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4cd0a0a-d03b-3907-a9f2-2aa5dfacf3f7 | -11.17947 | -45.32371 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92ef082c-7bdc-3086-8179-538289fd6c0c | -17.36194 | -48.17192 | 2026-10-10 04:10:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b869caa-cf31-3d5b-95b4-fb7aaeb91cde | -14.44487 | -40.73086 | 2026-10-10 04:10:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 799c9af5-30c6-3527-908c-b1a45bf9f81d | -11.66788 | -43.7008 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c4fa6bf-4bf4-381d-9136-bb421cdc868c | -11.96131 | -43.48079 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bbe603f-b3fc-34b3-89ed-140a62c74e36 | -10.93473 | -45.37671 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 190efa26-a57f-31eb-a10c-aa73dca87a87 | -11.96903 | -43.47483 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50f5e620-bab7-3ef8-8678-18746a0929b2 | -12.49574 | -51.29136 | 2026-10-10 04:10:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 29208bc9-e981-3e9c-b574-19b2588d99aa | -10.5412 | -47.30718 | 2026-10-10 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c92961e-666d-3d4b-8d1a-5fab5ae23524 | -14.87305 | -50.30831 | 2026-10-10 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0765efe5-6e37-3ba9-b97b-c7d6fcdc6b8f | -15.98668 | -52.4857 | 2026-10-10 04:10:00 | NOAA-21 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e367ceb-dc21-3836-935f-8dbaba1ca89c | -11.20149 | -45.29875 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 764faf4b-bc9d-3f3d-9ec7-db52739b053e | -14.44696 | -43.92714 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f25fb47a-fba8-381d-bf73-153f33b39048 | -13.36984 | -43.89407 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a56f8af5-a8be-3b12-998f-7019c3753bd4 | -14.45962 | -43.93287 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a5c7c859-742d-3a7a-b23f-ba6a5894080f | -11.23481 | -46.29576 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9068ac35-3204-3bd2-b882-356d513d496b | -11.60763 | -43.73755 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f44785a-536b-370f-9f50-a3b69d970799 | -11.95966 | -43.49128 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c54ccbf0-ecc9-3800-a449-d901cbd44945 | -12.04498 | -43.42638 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91cd0c08-8896-3714-97da-8f9cb633d38a | -11.01754 | -44.06667 | 2026-10-10 04:10:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79464907-d727-3568-969f-586aebda46c7 | -13.89846 | -43.93098 | 2026-10-10 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f7b6b75-8db6-3633-bdc0-cd2a6b3a50eb | -10.24571 | -49.67446 | 2026-10-10 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2abfb80-877e-3f1b-90b3-577f33923a1b | -11.98887 | -43.45642 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 451e6318-8b8e-38f1-916a-64bde9394f04 | -11.57129 | -43.66639 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 923571a2-8f19-36c5-8e34-ddcb76cc4a1d | -13.3709 | -43.90877 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d1466eb-bb4e-3dac-8cc9-2e3c8a3cc9be | -11.85842 | -43.55055 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a20eed3a-021b-34c0-83e6-86569775b203 | -14.32536 | -44.66687 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d07fb52-be08-3515-bd2c-75015390fce4 | -13.20216 | -48.13534 | 2026-10-10 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5bcb4a45-797d-3f74-90ae-be995c6c5e15 | -11.65526 | -43.67326 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5fe63934-e694-3718-880d-f1b1b31c5c44 | -12.86891 | -39.92001 | 2026-10-10 04:10:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 24ddc4f6-e01d-3db9-83f3-3ff7b5656c68 | -15.37226 | -41.927 | 2026-10-10 04:10:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| e9960c95-ee43-36ab-82f4-f73430779712 | -14.34278 | -55.01461 | 2026-10-10 04:10:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 75df8105-925f-3a28-8d5c-104b7d228256 | -11.24283 | -46.29265 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a2494c1-527d-36f2-8f21-b8130282e67b | -9.95942 | -55.33757 | 2026-10-10 04:10:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 800bd6b1-8e47-3160-8154-8af7071ef2f9 | -12.25359 | -44.42565 | 2026-10-10 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a15f8da2-0511-3cf1-91e6-ca4dc8466586 | -11.4705 | -47.46481 | 2026-10-10 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c763a8e5-fb1d-39ea-8bff-8aa576a973fb | -12.90875 | -45.1146 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f328a0c7-eaa0-3707-8f8a-f097aac937fe | -11.76304 | -45.45916 | 2026-10-10 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 200e5d19-b75c-3370-9a7f-686a216db0f4 | -11.94206 | -43.47396 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65b82d66-1289-3bae-b909-93becea19416 | -14.52766 | -49.3255 | 2026-10-10 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25bbd2f6-ab01-3b1f-90ec-a2e264c34fad | -17.10027 | -41.57471 | 2026-10-10 04:10:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3496ebbd-12c7-3733-b943-b92b7c8cf542 | -12.91276 | -45.11142 | 2026-10-10 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 757480e9-edb0-301d-89cb-a9a84afd1f91 | -14.74301 | -48.21645 | 2026-10-10 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8993cc01-9314-3bb8-869c-b21d49d694d1 | -15.0232 | -46.25257 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a511db9e-ffc7-3aea-8f47-2b7814e81ba7 | -11.59558 | -43.6848 | 2026-10-10 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60841029-d6b2-3b10-9a26-3027e17a4fbe | -10.73693 | -52.03494 | 2026-10-10 04:10:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff71ee2e-63e6-3d7a-9ee2-c91306b92645 | -16.57002 | -46.80035 | 2026-10-10 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 657041a1-ef25-3341-a234-b4b095cb965a | -11.73707 | -44.94843 | 2026-10-10 04:10:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ce90ff5f-33d3-362e-9c40-dd70c5fad3c8 | -15.77167 | -40.9294 | 2026-10-10 04:10:00 | NOAA-21 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0b38c845-d150-3976-9021-7ce1091983f6 | -12.11988 | -43.31614 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f3e461e-5875-3617-b969-0cb447765b68 | -12.07317 | -47.38293 | 2026-10-10 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1dad651-8c7c-3d55-965e-1937523f681b | -8.4971 | -54.61324 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d38164f5-2456-34fd-9c39-5697b8cf54e1 | -16.71301 | -41.88231 | 2026-10-10 04:10:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7e78de78-8ce8-30df-9c84-28724d4278b6 | -13.37315 | -43.89461 | 2026-10-10 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1889728d-fed1-3235-a2bc-d03d4b16cd23 | -16.2263 | -39.14584 | 2026-10-10 04:10:00 | NOAA-21 | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 39a01c3a-5bb7-3725-b532-6b48452b6d37 | -14.459 | -43.95825 | 2026-10-10 04:10:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5160de2a-481b-32e9-b724-a7eda9a9da6c | -10.93889 | -45.37332 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf34c3a-d026-37ce-a8af-f68a74e04fb0 | -11.99762 | -43.44744 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c0f3428c-2f17-3fbf-990f-d820f00a01b0 | -11.18297 | -45.32425 | 2026-10-10 04:10:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0982c941-16c3-3df0-8312-a63bfcc4e9dd | -17.46188 | -45.08953 | 2026-10-10 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6aa635c4-0481-360f-9b7f-969d94fa0f45 | -14.33203 | -44.66799 | 2026-10-10 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85dcc8db-48be-3cfb-810d-2be0e6748291 | -8.65157 | -54.54013 | 2026-10-10 04:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5553141-b306-30ec-865b-2a75ce2ad540 | -11.95746 | -43.48374 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4cffb53-e111-3fcc-aa42-1f942abfc34a | -11.95912 | -43.4732 | 2026-10-10 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README50.md)
