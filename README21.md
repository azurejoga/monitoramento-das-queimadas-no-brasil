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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bd40a8b-6efb-320e-a028-bbdb6382b31b | -14.85029 | -46.68586 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 82e1dca4-b5d4-35e6-9e40-a9adaa7c7960 | -11.59506 | -47.16649 | 2025-09-07 03:32:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 50947906-b6c5-3bdd-815f-2dbd1f495588 | -13.79241 | -43.16305 | 2025-09-07 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a43ebd35-6a22-3efc-8704-592da32fb939 | -14.84788 | -46.69682 | 2025-09-07 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ba42375-a7b3-3472-a066-be53929d972d | -13.82082 | -46.28217 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cce03c98-9784-3074-90da-d2dba5b4c24c | -11.40146 | -43.56698 | 2025-09-07 03:32:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6c1b5e52-19f3-367f-acb2-c99b3724d738 | -16.28762 | -45.68127 | 2025-09-07 03:32:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8dc3458b-c92d-3d29-940e-4ebc0be95d56 | -13.85663 | -46.24696 | 2025-09-07 03:32:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59aefb7a-f9ea-31b8-910d-4aa53cac6250 | -20.27299 | -43.78414 | 2025-09-07 03:34:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 06524b62-39c0-3a4b-98da-18f0cc0b7b09 | -20.54456 | -46.44352 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| fa4c3b84-6d7e-3cc9-86d8-3b34ca0bc712 | -16.92469 | -45.78033 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90ef0e9a-0d9e-377c-972c-82a1964967f9 | -17.6709 | -43.54155 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1566a275-c96e-3103-bb8f-59dba29b73d1 | -22.42149 | -47.44482 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 01564abe-e3ac-34e4-99a3-d1355bf8fec1 | -18.03639 | -47.09353 | 2025-09-07 03:34:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a55f6d37-f594-37b2-a766-b853b5b0c35b | -16.92273 | -45.7894 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e559ac8d-0e31-3013-bf54-7b2b93d40b91 | -20.09998 | -47.33467 | 2025-09-07 03:34:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aee099a5-a464-38f6-915c-dbc5d4dfabc0 | -20.55018 | -46.4374 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 79600c7e-2f2c-33ba-b480-2a45e767a2a0 | -16.69006 | -46.80341 | 2025-09-07 03:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b20ef420-80cc-302b-a3ca-a2c37ce1b030 | -20.55196 | -46.43722 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 84e85e95-5a20-3cca-bb8c-6c355f143913 | -22.32928 | -49.38073 | 2025-09-07 03:34:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| de9403a7-f049-3af8-ace9-88085cafc4ce | -16.93632 | -45.75478 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e1ea71f-2421-3147-937d-fcff62940545 | -18.98766 | -44.23071 | 2025-09-07 03:34:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7f39ca07-4de9-3c7d-82ac-3b6ca1807209 | -17.22117 | -46.70107 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 060bbb40-c634-3ca2-8a2b-4dc7407be907 | -17.71339 | -44.4874 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb02538e-30f7-3f8e-a9e4-bbac72b36e6f | -19.66828 | -44.88363 | 2025-09-07 03:34:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 3ea96921-da4e-3fef-be71-d75b35c11237 | -17.22399 | -46.71715 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f610a31a-db78-31de-86e7-e15174e02e4a | -21.62675 | -44.01691 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 630a6b8e-f975-3ddb-adf0-85fe4c30b663 | -17.6914 | -43.54353 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c29c4fc7-2c4d-31e6-96de-e10c11243a93 | -17.68135 | -43.5372 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47a1e0a6-0d9d-302b-a9ea-96b7cbf61242 | -22.41624 | -47.44363 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| f2761d61-205f-3057-b4ff-e322a50381fe | -17.95191 | -45.29711 | 2025-09-07 03:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 80822f2a-81c4-3acc-9c4c-78a4911e026d | -19.41652 | -44.31925 | 2025-09-07 03:34:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11f51cd6-4aac-3b0a-b480-5eba18655e2d | -17.68216 | -43.53749 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f57a9c7d-d359-385a-b872-2d2c8c597f23 | -20.54869 | -46.45155 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ed653d34-63d2-35e0-8573-4ad94b623c5b | -17.68989 | -43.5465 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89b000be-8dc4-307b-80d6-b310454237d7 | -17.69697 | -44.48619 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e5793e9-aa1b-32fe-bec7-1631d8960823 | -20.07663 | -41.70921 | 2025-09-07 03:34:00 | NOAA-21 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ab9c857b-9a5d-3144-aa40-7a31f84990a4 | -17.68275 | -43.53453 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5805afb0-6f8d-3212-b62b-40bc9cda8762 | -16.93722 | -45.7506 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3f8dc11-3ca0-33db-a651-927965ab2fc6 | -21.63148 | -44.01821 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 50f6b855-1f92-3bd7-88b3-2a88be6dca23 | -17.68302 | -43.55441 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f0d5882-c0c0-319c-90e1-37da27749104 | -21.70802 | -45.38228 | 2025-09-07 03:34:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f7d27a53-a32f-329e-8043-43cf8992d6b9 | -16.90244 | -45.77013 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 619b322e-ae23-35ec-89d8-454c6dea66c4 | -19.34044 | -42.17145 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 333e0e90-9e0d-306a-89a6-189e8c83ba10 | -17.37762 | -49.2394 | 2025-09-07 03:34:00 | NOAA-21 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2170223b-2c3c-3f41-8364-4a60e6e8d125 | -17.88034 | -44.33313 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 525aaaa2-d29b-3dbb-a46b-3d5ce958808b | -19.88248 | -45.02703 | 2025-09-07 03:34:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2690ed48-8a47-307d-9cab-b14d80b2e602 | -20.54564 | -46.4388 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 72d9d507-270b-3a45-b7b8-d162653149e7 | -21.70728 | -45.38566 | 2025-09-07 03:34:00 | NOAA-21 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8661c3f3-1503-31a6-acfe-0ecb26e7454e | -17.68517 | -43.54857 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75dd41af-2e91-33dd-a7dc-b02f1ee2cff2 | -21.33368 | -49.12915 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 17abecf4-bfa5-3e15-bbd6-9899f140cdbb | -17.69205 | -43.54029 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 875a1734-d028-3613-b249-40b36c169cb6 | -17.70607 | -44.48526 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73bc36ea-b6bb-33a5-b37a-1fce30bc4647 | -17.68196 | -43.5343 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 97c70948-a03b-31e4-89c5-71dfaed3bbe2 | -21.62657 | -44.02119 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9f24db62-276b-39e0-b2fc-75f6c7cfe706 | -20.09862 | -45.32058 | 2025-09-07 03:34:00 | NOAA-21 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a717eb75-4cc0-3a78-aa4f-f79dbd4b1c6a | -18.24552 | -45.20731 | 2025-09-07 03:34:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fb40b88-29e5-3979-8766-727385c61749 | -21.34151 | -49.12519 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 32e61820-57cf-3dd4-b5be-e4293dcb607b | -21.43101 | -44.17006 | 2025-09-07 03:34:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a50ca0ab-df14-3a1e-a5c9-c707e1107193 | -20.7709 | -44.46305 | 2025-09-07 03:34:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4e1b4f1f-adf6-394e-a8dc-591f7fdb3869 | -20.7715 | -44.46014 | 2025-09-07 03:34:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 82d82940-0507-3d80-a317-07d2c8c11352 | -22.41562 | -47.44376 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 74858549-1fc5-36f3-915a-1033d9d28c84 | -17.70359 | -47.65107 | 2025-09-07 03:34:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8eb67e34-25ae-3ace-af4d-fde84d345af3 | -19.344 | -42.17692 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c61d67d7-6fe2-3d05-a580-8d694783adca | -21.34122 | -49.12311 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 45035651-cf82-3663-a667-e3f21f5c671b | -20.54349 | -46.44823 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 542fbdb2-715f-3c4a-874c-a974e3e83e97 | -19.50859 | -42.57238 | 2025-09-07 03:34:00 | NOAA-21 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d0c40608-f76e-315f-a252-0fa101988107 | -17.69522 | -43.5243 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dcdc049a-dcf7-3777-ab2c-b95fe978b491 | -17.67213 | -43.53542 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46a4d016-2396-3ba1-98d1-d236d466249f | -21.34007 | -49.13117 | 2025-09-07 03:34:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 7b09c5f9-b57d-36dd-9c1e-655b768db402 | -21.6277 | -44.01571 | 2025-09-07 03:34:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| f5c9df5b-4594-38f4-b4b5-21f2e54b20a9 | -21.48237 | -45.56534 | 2025-09-07 03:34:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 20d85496-8a28-3a50-a3b5-2b8e724db3c8 | -20.54809 | -46.44687 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| a7c01646-90c8-31f7-b51f-255b8e4b6988 | -17.9522 | -42.77164 | 2025-09-07 03:34:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e49e170f-4495-3a7e-a142-e7e75331f2ca | -17.67324 | -43.52984 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3002e937-94f2-3f5d-a4ae-1adcbd1be737 | -17.69371 | -44.51713 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f57f2dbb-cbb3-3402-a9aa-10441da09e12 | -21.4884 | -45.56314 | 2025-09-07 03:34:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 9e0e0c42-32a8-3d92-9c59-07955f2df6c2 | -22.41818 | -47.4351 | 2025-09-07 03:34:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 62e37445-e444-341c-bbe9-40bcddc9858f | -17.68393 | -43.55483 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5cfcc22-f61b-35c9-83e3-6e29328a17e7 | -20.42884 | -42.21606 | 2025-09-07 03:34:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1ea27945-8979-3cf0-8352-d59e98c462dc | -20.54915 | -46.44205 | 2025-09-07 03:34:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| d8ca473d-8c10-3231-b939-2048263c8fc3 | -19.88365 | -45.02743 | 2025-09-07 03:34:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 872ba6bd-e2bd-3550-bb46-cf743271d901 | -22.69569 | -46.91511 | 2025-09-07 03:34:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| c0835cda-4e82-3714-b9da-f9c7e7785783 | -17.69083 | -44.51608 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 131bb0f6-296f-392a-92d8-bdf198cc34b2 | -17.68155 | -43.54054 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56694cf5-7848-3f19-8953-e61ab81b165b | -17.40598 | -49.30864 | 2025-09-07 03:34:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f6fa38f6-5167-3788-a20e-d82bd12afc76 | -16.93536 | -45.75923 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 502f63ec-8aa4-30b6-b398-abcddc09d260 | -17.22621 | -46.70726 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c96be018-7d49-3fc7-825b-6183f4fbc900 | -18.69062 | -44.44899 | 2025-09-07 03:34:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef95bfcd-4f76-365c-b709-ec2f283e3dff | -18.60474 | -43.64649 | 2025-09-07 03:34:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8fbff331-85b6-35e5-879b-2e66a30d53db | -18.24461 | -45.21151 | 2025-09-07 03:34:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc8653ef-df35-33ed-b54e-d9f47eb7a4df | -18.35757 | -43.91803 | 2025-09-07 03:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9ba0185e-34ac-3210-863e-212acd2cda52 | -16.92371 | -45.78486 | 2025-09-07 03:34:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b12469d-5638-3807-ac5c-551730d211f0 | -17.2214 | -46.70374 | 2025-09-07 03:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| dc034e90-cfd7-35dd-a6ac-bcf12f518305 | -19.06629 | -46.77102 | 2025-09-07 03:34:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 53c53bb8-9302-351e-b1ff-e5b43314c743 | -20.0432 | -41.22414 | 2025-09-07 03:34:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 325eb001-23e9-3de5-9802-acf373432457 | -17.69444 | -44.51369 | 2025-09-07 03:34:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 361c14cf-5f33-30a0-a966-cd8c4d7d219b | -16.68775 | -46.80247 | 2025-09-07 03:34:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c7712458-91cd-3104-8de0-3ae9531e9b59 | -20.04244 | -41.22812 | 2025-09-07 03:34:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ba3736e1-93a7-384b-8a08-0294640d58fb | -18.54842 | -43.81984 | 2025-09-07 03:34:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README22.md)
