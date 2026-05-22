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
| c54ac731-9ff7-3a91-a485-e0e802b016a6 | -9.3045 | -45.49381 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 79da597a-5634-391a-8fd4-79f85d960afe | -8.55301 | -45.98785 | 2026-05-22 04:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d5f4a32f-bf5c-39a6-8c7c-2eba2b0c417c | -4.66002 | -42.42131 | 2026-05-22 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25aed110-1ff4-36c8-bb05-cb8c618fe75b | -11.05041 | -46.71431 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b090d2f-7774-3e6e-9166-b75b3648b15a | -9.30274 | -45.49031 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d9ae9090-ac05-300f-80c3-a21b2f7aaee5 | -5.02767 | -37.56814 | 2026-05-22 04:04:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6bcf873e-a108-3ac6-b8c0-7ccfc11bde54 | -10.66306 | -48.24814 | 2026-05-22 04:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b14698-e086-3ea3-a316-801211053a17 | -9.29711 | -45.48885 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8d5b6c9f-658d-3d20-8714-6a94b1a3f844 | -8.5722 | -46.43432 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59ebdb7d-e48b-3b21-b821-b7c113c7bcc3 | -11.06024 | -46.7079 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f764b930-d425-39f7-b498-42206df35dfc | -10.66687 | -48.25396 | 2026-05-22 04:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 806ae545-2d71-3ff7-a44f-0725938e9e3e | -8.2212 | -36.1133 | 2026-05-22 04:04:00 | NOAA-20 | SÃO CAITANO | PERNAMBUCO | Brasil | 2613107 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f0c0cd3e-e76c-3d1b-bfe2-7f6731669eb3 | -8.9187 | -46.91322 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a0aa871-871f-34e8-b02b-d902a58c2099 | -11.06913 | -46.53019 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5ac4e03-43be-3966-aa2d-957fdda7b9b6 | -11.06585 | -46.70083 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac5472d2-7a0f-3ab3-aaed-11037a494504 | -7.63767 | -45.30453 | 2026-05-22 04:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b27fb008-a802-39e4-91ac-b614e1bacfff | -5.95345 | -43.4885 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ba4d33ba-0b6e-3887-be1c-3486b2df4a19 | -9.40009 | -47.36668 | 2026-05-22 04:04:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 036eced0-b135-3d6f-bb2b-2d6b3408b034 | -8.57648 | -46.43517 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eef9464-62fb-3ffa-ab3d-0df5fb472fc6 | -6.5181 | -43.68196 | 2026-05-22 04:04:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2261cdb0-9e67-3ba2-a22e-b7234583c69f | -11.06515 | -46.70472 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 611ee1cc-5e59-3be9-9fee-3ba0fb8de1cf | -8.73668 | -47.98012 | 2026-05-22 04:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51df8691-b6e6-377c-b10c-6f335a5f2edc | -5.94898 | -43.49238 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 00bc680c-d665-3768-a6d4-99602e7e48bb | -7.0528 | -45.05914 | 2026-05-22 04:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7695ebcc-d167-3bd9-98b0-945db2ccb7f2 | -10.66443 | -48.25018 | 2026-05-22 04:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dce8f23-ad31-30df-bf87-56e442d4be04 | -9.72234 | -47.04634 | 2026-05-22 04:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b1347b4-997f-3084-81af-de41682f3acc | -7.64173 | -45.30519 | 2026-05-22 04:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a19f5f8-4f38-322f-a97a-ed7978f77cfe | -7.72007 | -44.5548 | 2026-05-22 04:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b62a384d-a511-34d1-b489-c765725628e4 | -5.94973 | -43.48792 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 38638899-a726-34cd-b3c8-585d340745db | -10.73802 | -44.0958 | 2026-05-22 04:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ccc62ff-df0c-300a-81eb-b2aa8b424f5f | -10.66913 | -48.25101 | 2026-05-22 04:04:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5922ce4c-06e1-3d31-b128-b24ce573ecbf | -5.94777 | -43.48921 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 58569ac9-c5b7-33ad-bb0b-1fe52eef24db | -9.2977 | -45.48536 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35b63b99-c109-3e98-b2ab-60fbcb8e3c10 | -9.94122 | -52.46407 | 2026-05-22 04:04:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f54d5ffe-3320-3125-a8de-50ab80ba0445 | -5.76841 | -45.13194 | 2026-05-22 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 457e9d95-a919-3b70-b8ae-8b7592c36130 | -11.05533 | -46.7111 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bee75c86-3d38-3fa7-8b64-a7e487e87a84 | -5.77254 | -45.13261 | 2026-05-22 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0f2de47-a9c8-39f6-99b4-dd140b3a8e23 | -5.92321 | -43.47582 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6006ab95-c0d1-31e8-9f50-a5244043bb3f | -8.71356 | -48.32431 | 2026-05-22 04:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 55679287-1dac-3366-960a-56d029aa3016 | -10.65339 | -42.29574 | 2026-05-22 04:04:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0332666a-023e-3309-a312-46315aec0562 | -11.09451 | -46.68585 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 589d0e81-817f-328e-a58d-a38f5ce7b8f4 | -7.72087 | -44.54995 | 2026-05-22 04:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a880120a-3f1b-380d-bd69-6e4ac3ac6c1a | -4.66068 | -42.41724 | 2026-05-22 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c78996f7-5b3e-337a-95af-f3a1cdf5a882 | -11.04029 | -46.79426 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 08128018-8b8d-3bec-a53b-1352b4f11f35 | -9.29312 | -45.48811 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae5dbdbb-2479-3ed9-b1d4-c64cff0e4f6c | -8.56198 | -45.98568 | 2026-05-22 04:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c0cd372-2c7e-36f3-ab29-21f8121e9ab4 | -11.08962 | -46.68903 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a36c276e-6a61-3be3-aa7f-6055f3a18c16 | -7.05221 | -45.06266 | 2026-05-22 04:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 443b1c8c-857e-34a1-9d95-733654a61e6e | -8.93117 | -46.92008 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eff708ff-422f-30b2-8144-6574ab2054a4 | -5.9515 | -43.4898 | 2026-05-22 04:04:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 24b9dcc8-737d-3daf-98f8-fac8413dc7ed | -7.64111 | -45.3088 | 2026-05-22 04:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dbce9ff-8289-3728-a316-91ce97e8b359 | -7.64578 | -45.30586 | 2026-05-22 04:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b626aebb-36d2-36a8-b67b-d792502bd50f | -10.49242 | -49.36102 | 2026-05-22 04:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e7847d5-b99a-3fb1-9a07-263f9238bce4 | -11.04099 | -46.79039 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c544d58-0d59-3d00-b8f0-1e3cf863de93 | -6.56635 | -47.90592 | 2026-05-22 04:04:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| a1fd4a07-238a-3539-9b42-9a6d6f454213 | -9.30151 | -45.49727 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7588e1d6-e957-3e1f-ae9e-35238beba2ef | -7.30445 | -46.98639 | 2026-05-22 04:04:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45493127-cc6d-3d22-97d0-eb3c279294b8 | -10.73729 | -44.10007 | 2026-05-22 04:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e72bb844-7cd2-3150-aaf0-53d3330e1638 | -11.05603 | -46.7072 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31c5dd65-0847-3497-980c-525df9368f1a | -8.55013 | -45.97947 | 2026-05-22 04:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3fe7781-a50c-3931-9549-58340666814b | -9.29652 | -45.49234 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 01c2ba89-f002-3cc4-82bb-55d8263664cd | -7.64234 | -45.3016 | 2026-05-22 04:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 152be60c-29ea-3a7c-9c50-d8db43fc3bc3 | -11.03829 | -46.75738 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad1bf2cd-72e2-3edc-b43f-2595b582daec | -9.30611 | -45.49452 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ed8a1a02-8ec1-3b7d-b787-df1e2a600a84 | -8.7243 | -48.32062 | 2026-05-22 04:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5dca2bf4-7323-3be2-8446-d6289e66e5c6 | -9.29371 | -45.48462 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33e7ea2b-b23e-3b51-88ac-2177df29c3d6 | -8.55782 | -45.98485 | 2026-05-22 04:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7af88896-1b37-3d11-98ae-c505d6d987c4 | -9.30391 | -45.4973 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 875df93a-641a-3b45-95e0-72e8badd3597 | -8.93268 | -46.91137 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a31d8cef-012f-3bbe-9c5b-c3f80d03232b | -5.77606 | -45.13705 | 2026-05-22 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32f52264-aae1-3f9e-b72a-c1e651305964 | -9.2943 | -45.48113 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 269c39b7-e9c1-3f4d-ac00-70aa64606c7e | -10.48681 | -49.36297 | 2026-05-22 04:04:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef4cef0f-e92b-36a1-8bdf-09f8802886d8 | -10.65002 | -42.29518 | 2026-05-22 04:04:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d9ccde72-8f2f-3245-b9c2-8375c5833428 | -11.05111 | -46.71041 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dcc0c20-e42c-3257-bad6-eb481aeab0e5 | -9.30051 | -45.49307 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f26dae40-81fd-381b-b58d-85a4449ba485 | -5.91105 | -45.58065 | 2026-05-22 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f2c88b2-1964-3fe9-a6d7-dfac0ffaeb3b | -8.73574 | -47.98544 | 2026-05-22 04:04:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da853d67-b8d7-3dea-bd62-bd95688b1cad | -11.00749 | -43.02676 | 2026-05-22 04:04:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d7f86c0-8758-3b97-b477-e8c5d9cb310b | -9.28972 | -45.48389 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9bb9150e-65d0-3ce3-bf56-760014b105fe | -9.72597 | -47.05143 | 2026-05-22 04:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a5876b1-98a1-3e6e-b9a7-a7ef459ef0ab | -6.56141 | -47.90517 | 2026-05-22 04:04:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1468a576-bb0d-3fec-8836-62c50f2db8ba | -5.02826 | -37.56441 | 2026-05-22 04:04:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b2f52b8c-d2da-36cc-b951-6277f9838aac | -11.06094 | -46.70403 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcfdc569-89ce-39ef-aa59-4b568365f010 | -7.04878 | -45.05838 | 2026-05-22 04:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6b27832-01ec-398a-90fa-22e74301e007 | -8.92676 | -46.91924 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 749ee3e2-9d9c-3f4b-b5fd-4ca63f1e072e | -11.05004 | -46.71471 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9eb3210-7455-3ece-9394-92344ae2d3ca | -9.29992 | -45.49656 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 74dbbe67-5ce8-3d54-8202-a4f3f6cf63f0 | -10.73682 | -44.09794 | 2026-05-22 04:04:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 169804c0-75f6-3e25-ab10-e648b7f3850a | -5.77317 | -45.1288 | 2026-05-22 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76095661-8c9d-3a33-be78-e3f5cac583b2 | -9.29031 | -45.4804 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be70df36-00c2-3e5c-9975-c46a22d85ab6 | -8.92311 | -46.91404 | 2026-05-22 04:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f426a63b-11aa-354a-8921-d419003fb9b5 | -11.08542 | -46.68828 | 2026-05-22 04:04:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d12c9af-ddf1-317c-a456-ee2452381f9a | -9.30212 | -45.49378 | 2026-05-22 04:04:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 521a8e29-4e65-39f4-87b7-ec4bf125940c | -8.71942 | -48.31977 | 2026-05-22 04:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20963e4e-e783-319c-80cd-92d1d4fde930 | -11.90866 | -43.74208 | 2026-05-22 04:06:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e37f62c-d526-33e4-97fe-8a14a01e1c71 | -11.61587 | -47.90694 | 2026-05-22 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65556921-9c28-349e-a1a3-3504c824c423 | -16.35275 | -43.87625 | 2026-05-22 04:06:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 442c9c1c-1631-3a48-99d7-2e25d9576697 | -12.88649 | -47.24091 | 2026-05-22 04:06:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 839e00b3-bdb6-3bfd-8151-ab4f858f26c9 | -12.22988 | -44.25118 | 2026-05-22 04:06:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0948e5a-ed0a-3b9f-baa2-a3d56629c525 | -12.81239 | -44.86689 | 2026-05-22 04:06:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README4.md)
