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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fde451e-4002-3bf7-8bd7-3ac81bf33f99 | -12.31993 | -47.46 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e646bfce-7284-3156-a1d0-c0e7e15073c6 | -12.32581 | -47.46129 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 549e97e5-eca6-3d06-bff3-e9e392e14935 | -12.52626 | -47.56836 | 2025-10-27 03:45:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9fab8ade-d207-320e-8f08-cc2683fc80ee | -14.43887 | -46.49194 | 2025-10-27 03:45:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31e1bda8-0bb3-3046-a92b-e97cfdd50ab9 | -12.50571 | -44.33919 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0523201-e22d-3939-9e13-484e928072f5 | -17.31638 | -43.60539 | 2025-10-27 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af0eead7-2a41-3b0e-8f23-12e8218a66b6 | -14.6302 | -48.42582 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3e28b1d0-8485-3d51-b75b-d999d7608b02 | -13.19097 | -48.44463 | 2025-10-27 03:45:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f616f49-48b0-3c66-b805-7442041a4726 | -15.10926 | -43.26395 | 2025-10-27 03:45:00 | NOAA-20 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10769a90-e387-3446-92ef-dfc1d8621fe3 | -14.56541 | -48.00569 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 007a3577-9fa9-3713-9a0c-e44d7e864c22 | -12.3233 | -47.48764 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d0e73fd-28ac-3ea0-8129-415836c28a67 | -14.67382 | -46.3461 | 2025-10-27 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 375a8a93-7a07-31b2-aa3f-b1b7d0802e7b | -14.43954 | -46.48856 | 2025-10-27 03:45:00 | NOAA-20 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 238aed4f-2d4f-3049-b41e-359d66ae7092 | -14.14846 | -43.57624 | 2025-10-27 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f223a39c-ffd6-382c-8bbf-ec7a5e5935b9 | -14.62648 | -48.42166 | 2025-10-27 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f18cb84-965c-3ace-95c7-ed84526f3349 | -12.28146 | -43.83129 | 2025-10-27 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42fcd10c-23a0-34a8-97a2-fc8bb94a6c03 | -12.86551 | -48.66071 | 2025-10-27 03:45:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b4a45f4e-3d57-3dec-b6f6-e614b18bfedd | -12.28412 | -43.83078 | 2025-10-27 03:45:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 643d8a6e-1570-3cf5-83bb-79b655756a5a | -12.5082 | -44.33261 | 2025-10-27 03:45:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d1f66da-4497-3d53-82c5-7296e164a1b9 | -16.37605 | -47.41677 | 2025-10-27 03:45:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 041fbcf4-3b30-36dc-a471-071b7f1706a8 | -14.44206 | -47.78823 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d30538-b792-320a-a897-502a4a3e9384 | -13.43557 | -47.38588 | 2025-10-27 03:45:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2634186f-5edc-37a5-91c0-8f74630b2af6 | -12.33267 | -47.47128 | 2025-10-27 03:45:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d61014db-385b-3281-a27c-d8ff05a3bdf2 | -17.22347 | -44.43763 | 2025-10-27 03:45:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1062295a-fa03-36c2-9d52-52630206089e | -15.13769 | -47.94321 | 2025-10-27 03:45:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6daa6de3-535b-30fa-91dd-1de4e26186b9 | -14.44461 | -47.7756 | 2025-10-27 03:45:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b0ca089-136e-3cf6-8055-9b5b77e8d463 | -21.66788 | -44.51945 | 2025-10-27 03:47:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1de73e3b-78b7-33bf-984e-96714c6b204d | -19.87266 | -44.18048 | 2025-10-27 03:47:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 823ea950-dff6-38e7-9cf0-26547fa2ffbb | -21.65707 | -44.50884 | 2025-10-27 03:47:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c58ac47b-b624-3b44-8908-a9df2bb27f9e | -19.9926 | -43.75229 | 2025-10-27 03:47:00 | NOAA-20 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 03c5d96a-3c4c-3511-969e-5d08555b5940 | -20.65997 | -42.73236 | 2025-10-27 03:47:00 | NOAA-20 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4ec9e81a-25a4-3775-916d-664d1a049c22 | -20.97517 | -44.32601 | 2025-10-27 03:47:00 | NOAA-20 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7c4fbbb7-66f1-30c9-a803-0ec7dabfe42f | -20.40691 | -44.06349 | 2025-10-27 03:47:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 27c2b623-cfa6-36aa-af9a-38ba32e27e0b | -20.72176 | -42.78053 | 2025-10-27 03:47:00 | NOAA-20 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0459a8ab-bf2d-3f41-b9a4-3bb7902e6894 | -20.65725 | -42.72988 | 2025-10-27 03:47:00 | NOAA-20 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 12eca7ae-417b-3047-bcef-12b82ce11f4d | -22.07174 | -43.86879 | 2025-10-27 03:47:00 | NOAA-20 | RIO PRETO | MINAS GERAIS | Brasil | 3155900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cdf8b8b2-4598-3134-9666-7798468684c2 | -23.52725 | -46.07049 | 2025-10-27 03:47:00 | NOAA-20 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea575b26-ad87-322e-9583-3bb121d5acef | -20.901 | -43.43195 | 2025-10-27 03:47:00 | NOAA-20 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f0ee2226-3eb4-3e02-a7c5-b27d6ec30901 | -21.66864 | -44.51552 | 2025-10-27 03:47:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec61e002-e9b7-3dfe-8b55-023a61decf0f | -20.21942 | -42.73972 | 2025-10-27 03:47:00 | NOAA-20 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 3dd777e9-524e-3502-898a-2e4afd3fbd00 | -20.24057 | -44.10395 | 2025-10-27 03:47:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 903c95e0-7fc2-32bc-ac0a-c0d0fa798a54 | -20.60789 | -45.26003 | 2025-10-27 03:47:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73abac6b-3d65-3035-941a-bd52f1ae380a | -21.58952 | -43.49076 | 2025-10-27 03:47:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| ad26e7d2-5df0-323f-bef4-80e6c3977fdd | -21.66376 | -44.51853 | 2025-10-27 03:47:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9226499d-9b08-3757-a7b4-38947898bb2a | -19.87344 | -44.1764 | 2025-10-27 03:47:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98100648-a5c0-3173-a5c1-cc1af60c4259 | -22.36069 | -45.17957 | 2025-10-27 03:47:00 | NOAA-20 | VIRGÍNIA | MINAS GERAIS | Brasil | 3171709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe5f52f6-1c7a-3446-b2fd-65f7c9455496 | -20.85715 | -43.55625 | 2025-10-27 03:47:00 | NOAA-20 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b74802f5-d21b-3c62-b448-90551b6169e1 | -20.24131 | -44.10005 | 2025-10-27 03:47:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27f6e34f-ed9e-39f8-903e-5631d253bfab | -21.94745 | -46.51289 | 2025-10-27 03:47:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b29212cd-0796-3555-a3cb-fc0f38bee2c0 | -19.64003 | -45.38847 | 2025-10-27 03:47:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a24d0e74-da17-312c-a5c0-167db595f377 | -21.71451 | -44.45533 | 2025-10-27 03:47:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| be9dde61-7aa7-3eed-a854-ee492647456c | -21.58856 | -43.49592 | 2025-10-27 03:47:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| abef971c-c12e-3f14-b86a-c5404a8366c7 | -19.98916 | -43.74821 | 2025-10-27 03:47:00 | NOAA-20 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d23c252b-7369-3fcd-b874-2e2482638e39 | -20.75231 | -43.23172 | 2025-10-27 03:47:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 09fb56b2-d6a4-3420-928f-47bac75a6d9d | -20.71798 | -42.77975 | 2025-10-27 03:47:00 | NOAA-20 | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 973d6886-056c-36b9-89b1-859462253c37 | -21.9407 | -46.52207 | 2025-10-27 03:47:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d86b2729-32bc-3ed9-acf2-db1f3a592e34 | -20.79861 | -43.30872 | 2025-10-27 03:47:00 | NOAA-20 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b06c7156-8c82-35fb-956c-f8c5ec67075d | -22.12271 | -42.98397 | 2025-10-27 03:47:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 262a07b2-d820-3867-a73f-c408e86c3452 | -19.92034 | -44.82031 | 2025-10-27 03:47:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa7218c1-af63-3947-8228-e73dc2591983 | -21.37811 | -43.60251 | 2025-10-27 03:47:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c033e932-98b0-36f8-a81b-d363b378422a | -21.0677 | -43.64119 | 2025-10-27 03:47:00 | NOAA-20 | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 29cb065e-f0c3-3723-907a-44f3aa6692f8 | -19.92119 | -44.8159 | 2025-10-27 03:47:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e8e48ef-1f07-38d2-80bd-b134df832005 | -19.99191 | -43.75593 | 2025-10-27 03:47:00 | NOAA-20 | RAPOSOS | MINAS GERAIS | Brasil | 3153905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af7cc8da-aeed-3f50-b3d8-f1ac67d155f7 | -20.24391 | -44.10891 | 2025-10-27 03:47:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 921da8c5-cdd9-3ca9-9639-525d2538f436 | -21.58368 | -43.50047 | 2025-10-27 03:47:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 3ab49b47-ea82-3ce6-bdaf-70bdf12363f1 | -21.47901 | -43.86287 | 2025-10-27 03:47:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0f3a5756-4dc7-33f5-866b-751b5b493a10 | -19.92548 | -44.81706 | 2025-10-27 03:47:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ab65e1f-cfc2-3548-91aa-31e741402ec1 | -20.65618 | -42.73168 | 2025-10-27 03:47:00 | NOAA-20 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 62bfa2e6-ca70-30fe-a41f-dbc5589d10a7 | -20.65636 | -42.73486 | 2025-10-27 03:47:00 | NOAA-20 | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 522adc92-b16a-3a51-823b-c37f83050ddf | -21.48864 | -44.96757 | 2025-10-27 03:47:00 | NOAA-20 | LUMINÁRIAS | MINAS GERAIS | Brasil | 3138708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5962c303-e67e-34f2-914e-a86708473405 | -19.64102 | -45.3835 | 2025-10-27 03:47:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 153c3b23-73b4-3e83-83a2-80e5f237ede2 | -22.0734 | -43.86692 | 2025-10-27 03:47:00 | NOAA-20 | RIO PRETO | MINAS GERAIS | Brasil | 3155900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f1663328-a466-3681-9f2c-4106478e0cd8 | -20.22138 | -42.74202 | 2025-10-27 03:47:00 | NOAA-20 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e01fa012-c135-357f-bbd6-4deca3953f3c | -20.75322 | -43.22677 | 2025-10-27 03:47:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 517b1c7a-7ebe-3d87-aba1-7cf6cee7d123 | -19.92234 | -44.81481 | 2025-10-27 03:47:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 891628be-92d2-3bc1-91a0-77c71e35051b | -22.088 | -42.98227 | 2025-10-27 03:47:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cacd3cfa-70aa-305d-8502-eeb748f04720 | -21.47503 | -43.86206 | 2025-10-27 03:47:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d1b4853b-f923-32d4-b65c-4401d601d480 | -20.79961 | -43.30341 | 2025-10-27 03:47:00 | NOAA-20 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e5637103-945a-375e-bd0f-50dfaa119f45 | -20.21853 | -42.74462 | 2025-10-27 03:47:00 | NOAA-20 | PIEDADE DE PONTE NOVA | MINAS GERAIS | Brasil | 3150208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8c05e182-a0fa-3adc-9f3e-b59be45db2cd | -21.94289 | -46.51144 | 2025-10-27 03:47:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dc4a4b47-dc5a-310f-9fb2-5dbfa69b415e | -19.61765 | -46.18596 | 2025-10-27 03:47:00 | NOAA-20 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ba556b8-95f1-3760-9cf5-2747238038d9 | -22.11896 | -42.98318 | 2025-10-27 03:47:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5cf61f09-cc6a-3441-ad99-86e5c585c57d | -21.11339 | -43.95247 | 2025-10-27 03:47:00 | NOAA-20 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74dcb5b1-7f64-39b9-acb1-18618f8ba9e4 | -20.75712 | -43.22743 | 2025-10-27 03:47:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f2b5d75-1c5e-3222-a6d0-94c5c1fe73de | -21.66119 | -44.50971 | 2025-10-27 03:47:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 28607386-dfcc-35a9-84e7-44f2947be7cf | -21.11268 | -43.9562 | 2025-10-27 03:47:00 | NOAA-20 | DORES DE CAMPOS | MINAS GERAIS | Brasil | 3123007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a3a8863b-ec01-3ef1-ab66-bd15deb223df | -19.92662 | -44.81599 | 2025-10-27 03:47:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5007ce15-1ec4-3c31-8d71-2f03925fdf2a | -19.88382 | -44.37245 | 2025-10-27 03:47:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5934dc6-db3e-37f5-9f91-c7d3bd3b9737 | -19.88303 | -44.37656 | 2025-10-27 03:47:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6b65704-f23a-30dd-8dd4-df81030f3c4e | -19.92146 | -44.81919 | 2025-10-27 03:47:00 | NOAA-20 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b006c62e-dcb4-30fb-8120-15d4938b2517 | -21.94181 | -46.5167 | 2025-10-27 03:47:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 9e8da1b6-53d9-3f65-a2a5-4a249b23c65e | -19.63902 | -45.3935 | 2025-10-27 03:47:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccc823e0-294a-3441-bf55-89fd018b0957 | -21.26282 | -45.18858 | 2025-10-27 03:47:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e21c816a-845d-39c2-bb13-8f34d7f801cb | -21.47174 | -43.8576 | 2025-10-27 03:47:00 | NOAA-20 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 314f0ecb-9c52-32b9-a11b-246bc1b264ed | -20.6076 | -45.25646 | 2025-10-27 03:47:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1ac1d8ec-10c8-370d-b6d6-1e133454f10d | -21.5827 | -43.50583 | 2025-10-27 03:47:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a95469b0-b0e9-392f-8acc-d7a3020ad59c | -23.11392 | -46.39073 | 2025-10-27 03:47:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a3fe334b-43b8-30ba-9ae9-6dbd02eef4e8 | -20.76102 | -43.22816 | 2025-10-27 03:47:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d4536fa6-74d9-3e44-ba4d-93c7d9b73b99 | -21.37424 | -43.60137 | 2025-10-27 03:47:00 | NOAA-20 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a8583ca7-2744-3e4c-b31d-af87d7ff1edc | -7.8408 | -46.487 | 2025-10-27 03:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |


[Clique aqui para ver as próximas entradas](README26.md)
