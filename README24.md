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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64afa529-23dd-321c-84f5-a65235e76fbd | -20.28216 | -46.10797 | 2024-09-30 03:47:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 09cd01c2-8158-37d6-8112-d564b1048f53 | -20.26898 | -41.2088 | 2024-09-30 03:47:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99ae164e-b319-3d9f-a669-0ee2cccfcd77 | -20.26822 | -41.21315 | 2024-09-30 03:47:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30708e11-b20b-3c3e-979b-4b381b91007c | -20.26542 | -41.20838 | 2024-09-30 03:47:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1f8f0ef4-84d7-3af1-84f3-6364fab06075 | -20.26468 | -41.21269 | 2024-09-30 03:47:00 | NOAA-21 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1fc1e439-967e-35e9-ae3a-7e6947944b68 | -20.20399 | -41.96695 | 2024-09-30 03:47:00 | NOAA-21 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1924ec58-7bf6-3996-9560-87b4f7162dd5 | -20.16663 | -41.31623 | 2024-09-30 03:47:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f298ff49-f988-36c7-b7e8-85a17aa7236d | -20.12546 | -44.26135 | 2024-09-30 03:47:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 469b1437-6f23-3f02-9f0c-630648c6fd88 | -20.11701 | -42.01124 | 2024-09-30 03:47:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 63fdda00-fc35-3f06-bcbd-c1af2859fed8 | -20.11339 | -42.01042 | 2024-09-30 03:47:00 | NOAA-21 | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cbb6baf4-3a4f-38c9-b467-a1b1a1c730c1 | -20.0981 | -42.24514 | 2024-09-30 03:47:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3417da5c-de3f-3610-9556-a2185d681091 | -20.09442 | -42.24438 | 2024-09-30 03:47:00 | NOAA-21 | CAPUTIRA | MINAS GERAIS | Brasil | 3112901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2f0a3e6a-61d0-3e8b-829d-d5298a9e5d20 | -20.08177 | -44.66973 | 2024-09-30 03:47:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a6714771-d498-3b25-8068-d24f06d1c976 | -20.07098 | -42.33249 | 2024-09-30 03:47:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b21079ac-ff8e-3eb9-9286-438b82e18f31 | -20.07011 | -42.33733 | 2024-09-30 03:47:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fad1fa6c-675b-36e4-a1fb-66c1bed80c9d | -19.98071 | -47.69351 | 2024-09-30 03:47:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ff8c63cf-37d2-3372-8d5c-d5961fc89592 | -19.98 | -47.69681 | 2024-09-30 03:47:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 86105957-3a46-38c9-8a76-ae6bc70c5b56 | -19.97425 | -43.95287 | 2024-09-30 03:47:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f25c4f8d-0148-3daf-894e-a02644bc018a | -19.97347 | -43.95695 | 2024-09-30 03:47:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 783e9400-136d-3c98-8dac-abfc2d591dce | -19.96936 | -43.9563 | 2024-09-30 03:47:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 02588fa4-75e3-308a-9371-8875345a5038 | -19.96346 | -43.94287 | 2024-09-30 03:47:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f94953c-4710-3d5a-b35c-6b0014854684 | -19.89666 | -43.17967 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 94680ef6-3fba-33c6-86b8-e44f7225f8f9 | -19.89378 | -43.17343 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 48c9bd94-5997-3416-a3c4-4c0dbcf271fe | -19.89279 | -43.17873 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d6a2a0c6-e793-342c-8485-7d04599c680e | -19.89185 | -43.18382 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 9b8ab7af-4e8c-310e-830e-5f9d676e2135 | -19.88994 | -43.17235 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 471eebff-3e0e-3433-947c-ef569a59db62 | -19.887 | -43.16644 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 88cd00d7-0a5e-3528-84af-3b731f9ae43c | -19.88608 | -43.17141 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d5a217fd-56e9-3f42-a85c-b793ee2e3bc1 | -19.88216 | -43.17072 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| f69a5e76-8957-3f74-bdf0-6950aa3c025a | -19.87826 | -43.16997 | 2024-09-30 03:47:00 | NOAA-21 | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 402927fa-90a5-32a9-86cc-3c5a797faed2 | -19.85024 | -42.75245 | 2024-09-30 03:47:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| d6fc45c4-7b42-3e97-9397-aa726260716a | -19.84938 | -42.75716 | 2024-09-30 03:47:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| aebf9a79-ffcb-3c4b-9929-8bddba327984 | -19.84847 | -42.76211 | 2024-09-30 03:47:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 99cb9d9b-2435-3206-aa76-f87cc5dccdd6 | -19.84552 | -42.75666 | 2024-09-30 03:47:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 517d18a8-9778-380e-a03b-0bce4597d8ba | -19.78268 | -43.1607 | 2024-09-30 03:47:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 964c7df9-faf7-3364-91f0-53a462c141c4 | -19.74792 | -47.88902 | 2024-09-30 03:47:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b7ea0e70-7465-3370-9b94-d013834d1353 | -19.74273 | -47.88762 | 2024-09-30 03:47:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77de60e9-ae50-3aa6-a9b0-edb61ca0b765 | -19.72659 | -42.42465 | 2024-09-30 03:47:00 | NOAA-21 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2daaa932-1b28-33e0-94d1-ef638653ec65 | -19.69645 | -44.195 | 2024-09-30 03:47:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdbb5d27-60f7-386e-a69e-38f179702ae2 | -19.52283 | -42.87996 | 2024-09-30 03:47:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7d6a5674-7a28-3cb7-afaa-5ba229a90444 | -19.519 | -42.87904 | 2024-09-30 03:47:00 | NOAA-21 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f705555e-51bf-3f60-84d7-0530f9120cea | -19.5122 | -43.8598 | 2024-09-30 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7be01cf-53ef-351a-8c46-7d0c3b572cb1 | -19.49181 | -42.3429 | 2024-09-30 03:47:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e73550bd-61f7-300f-9989-8811610e54b8 | -19.44236 | -45.87514 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 99459f98-26b2-300d-9d30-d06f00e765c9 | -19.44139 | -45.88008 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 59fdcbcb-2758-3f9c-b3bf-8561b2aa4ebf | -19.44066 | -45.87296 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| bf5ca05d-06d1-359c-986c-52908f5139bf | -19.43966 | -45.87785 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e82b1aa8-0011-34a9-aff8-66c4a2d1cd2a | -19.43876 | -45.86888 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4a19d54e-6a0a-3d0c-a9d4-9bc2a21e2080 | -19.4386 | -45.88307 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7a5f8b7c-e28d-34e6-b590-83ea8c720106 | -19.43777 | -45.87391 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5164481f-de79-3d4d-9f24-10046dabf8c7 | -19.43749 | -45.88847 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4270d91a-4082-3d37-89d3-1c4e63252f57 | -19.43611 | -45.85782 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95d4c979-8e89-37aa-8040-68086497e9ba | -19.43571 | -45.88436 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5936b6b1-5ff5-3055-89db-4a8d5cf13839 | -19.43517 | -45.86258 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21bfd5c3-bfe2-369c-bbf7-99295023cba0 | -19.43464 | -45.88975 | 2024-09-30 03:47:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b00bcd97-7a6a-3537-a249-6b7f857d813b | -19.43395 | -45.88209 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e87ecfb5-e0ee-3e9d-843c-c5c6512d6220 | -19.43353 | -45.86051 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9d256d2b-c075-3317-8c9a-15928a6cb660 | -19.43284 | -45.8875 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53b4e06a-1c75-3d5c-94f5-0e6086f2c2ce | -19.4315 | -45.85669 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0713a4d1-286a-368d-85d3-ffc7c6b6e3f8 | -19.43106 | -45.88338 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a2ac8c39-05d9-31bb-8c71-84930f069ff2 | -19.43055 | -45.86147 | 2024-09-30 03:47:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ee6a248-936f-334c-8673-4e095bb6dad6 | -19.4293 | -45.8811 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c92eaa4-4417-36a0-99e5-295706140329 | -19.42819 | -45.88653 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2127fd1a-a782-337b-aabd-3308adab5d0b | -19.42642 | -45.88234 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1caaa4a-25c2-3486-a0d2-f6128b92129a | -19.42594 | -45.86034 | 2024-09-30 03:47:00 | NOAA-21 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d68e5d5e-3dd2-3cbb-881e-4f519713a06c | -19.09733 | -43.45181 | 2024-09-30 03:47:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7ee2ad7-4149-3b15-b774-69e68e79d7ae | -19.04428 | -42.95156 | 2024-09-30 03:47:00 | NOAA-21 | DORES DE GUANHÃES | MINAS GERAIS | Brasil | 3123106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f06b87a3-d55f-31e6-9023-326f66abe616 | -19.00416 | -47.14559 | 2024-09-30 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7511064d-8fc9-3160-961d-eb8bbf3c1d40 | -19.00349 | -47.14879 | 2024-09-30 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7603e770-3280-36c1-8769-e25af44ac595 | -18.97369 | -45.45682 | 2024-09-30 03:47:00 | NOAA-21 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 87198220-39e7-381d-bf34-9f6beccfb531 | -18.97329 | -45.45902 | 2024-09-30 03:47:00 | NOAA-21 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 1f922b6d-9a04-36e6-9b54-a499375e1b92 | -18.97272 | -45.4618 | 2024-09-30 03:47:00 | NOAA-21 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b1c5a9f1-c4ab-3b4f-91f4-fc9b286267db | -18.95508 | -43.5168 | 2024-09-30 03:47:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6dca4853-2476-381f-9f93-2fd541186f27 | -18.57908 | -43.8625 | 2024-09-30 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a611520d-3ee8-342c-b6c3-7505db76cfee | -18.57835 | -43.86635 | 2024-09-30 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cbaaf1e3-0a27-3940-961f-fa51e9345c93 | -18.57494 | -43.8616 | 2024-09-30 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a8a85a72-29f4-31f1-a08d-07428de0b2dc | -18.53306 | -43.36974 | 2024-09-30 03:47:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 99f549f3-caab-381c-9b97-f81c9fe020dc | -18.52876 | -43.02713 | 2024-09-30 03:47:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fd3c43a6-1aef-362c-a3da-cfeb64d5477f | -18.52705 | -43.35727 | 2024-09-30 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 32a91e02-dbbd-3572-8fb4-4dc45e3c8b92 | -18.52637 | -43.36088 | 2024-09-30 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37a74627-730a-3090-8279-9a4c0ef93aff | -18.52228 | -43.36039 | 2024-09-30 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO ITAMBÉ | MINAS GERAIS | Brasil | 3160207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0a668d9-3342-3edb-9f4b-751deff68f1c | -18.46736 | -50.16578 | 2024-09-30 03:47:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 8dafb4a0-4bb2-34ae-9f28-9c440e320c27 | -18.4612 | -50.16443 | 2024-09-30 03:47:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 3dfa6a93-5505-3300-b3af-993c11600107 | -18.46006 | -50.16945 | 2024-09-30 03:47:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 547117fe-6cc1-312e-bf95-2d6319f8ec1b | -18.45619 | -50.15799 | 2024-09-30 03:47:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b935fe22-065b-37a9-a662-f76155e9d7b9 | -18.45504 | -50.16304 | 2024-09-30 03:47:00 | NOAA-21 | GOUVELÂNDIA | GOIÁS | Brasil | 5209150 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| b65ddf33-6c56-3cfa-a6c6-35f6addcbd4f | -18.00756 | -44.31184 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3eb28f0-2a4a-3f06-afdd-46405e6d73e1 | -18.00668 | -44.31635 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc92d351-82a7-35df-a4f0-cca59aad7d66 | -18.00581 | -44.32085 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a098d00a-c4c8-3fe0-8118-4ddfe9d8bf2b | -18.00578 | -44.3129 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5cd26e4-37e4-3e70-828f-299c194c492e | -18.00494 | -44.31741 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9cff54bf-227a-3a96-84a5-68f3b45cc90a | -18.00239 | -44.31537 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76343208-2966-30e7-88b7-b020e0e44f82 | -17.98673 | -44.34951 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf3c347a-5246-364b-aa79-9b7f33f67577 | -17.98525 | -44.35061 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b02c231c-8c2a-3e65-acbd-9d2f6f5b6dd4 | -17.94225 | -44.24688 | 2024-09-30 03:47:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 318fe71d-cf92-3864-820e-8e7527f7020c | -17.86501 | -49.91433 | 2024-09-30 03:47:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63c2d93a-5862-358d-94b8-f426dd70b7e9 | -17.78229 | -44.27682 | 2024-09-30 03:47:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1d6ebe9-2002-36fb-95d6-5f192d72a5bb | -17.78086 | -44.2769 | 2024-09-30 03:47:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e202850f-659e-342f-9140-2dad1de58823 | -17.7764 | -44.44602 | 2024-09-30 03:47:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb4c8228-b0d7-3d81-89c8-a955b719f456 | -17.70336 | -44.30615 | 2024-09-30 03:47:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README25.md)
