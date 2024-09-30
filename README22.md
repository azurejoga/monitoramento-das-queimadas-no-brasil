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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43a4686b-8d05-3cc0-8bee-3f8755f8b7b5 | -13.45756 | -48.61181 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1008af5-3f8e-3a61-9687-cac7a2313580 | -13.45705 | -48.61966 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ad1ae8a-35e2-3789-ae36-99a37139b05d | -13.45648 | -48.61696 | 2024-09-30 03:45:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aca7a7b7-7827-3a45-ba1d-bc2c4757ab80 | -13.44171 | -44.025 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbf372d3-9fcf-35f9-b78c-ab1e4e93491c | -13.4371 | -44.02417 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 670c21d5-75fc-379a-b348-1f106142d5e6 | -13.43159 | -44.02819 | 2024-09-30 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 597e3fc7-d123-362f-9636-6553d0fda51b | -13.36661 | -42.05853 | 2024-09-30 03:45:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dde4b989-e69a-3ceb-9614-af22acfe8876 | -13.35687 | -46.30242 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dc6aaa5-e825-31c5-a886-82763cae6fd0 | -13.35441 | -46.30218 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e2777e-9f8b-3024-9d89-8494c258f247 | -13.3215 | -42.07681 | 2024-09-30 03:45:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7dceb987-6b74-3b4b-9746-d3c34cb12651 | -13.31672 | -42.08007 | 2024-09-30 03:45:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4185cb95-a07c-39ad-b31b-cc00d7f877fc | -13.25298 | -46.36602 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19475626-7d1c-339e-8099-3604e3ab609e | -13.25258 | -46.35091 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6656edbe-7e0d-3b2f-80c3-5182cd26de95 | -13.25188 | -46.3544 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 693641aa-8aef-353b-93b8-020de487819b | -13.25115 | -46.35806 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c0a56798-869b-321e-b5df-dccd3c4815fe | -13.25041 | -46.36177 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 088d11f1-4e8e-3344-b4b0-b5ae4e7c848f | -13.24972 | -46.3539 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9dedb405-4592-3396-ab76-31b30d7c974e | -13.24967 | -46.36546 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99ffc1e4-906f-3b8f-8bb5-7a6cd117b5b1 | -13.24902 | -46.35754 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aae4e28-a16e-3afa-9f26-043fe0e68490 | -13.24831 | -46.36125 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c3ee77d-b8f4-3f25-be9d-20a300721234 | -13.20016 | -46.32165 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82c143ba-c35f-3ac1-951f-872d778fcfb8 | -13.19993 | -46.35132 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c12c9cd-6e59-3660-9343-92e3c735b88e | -13.19944 | -46.32536 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec396b1a-9d41-3052-a72e-a7793198b1fd | -13.19925 | -46.35479 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c916e26c-2c49-3190-b367-91308b337a53 | -13.19872 | -46.32899 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 93a0416f-2ab3-3ce4-a145-5d14bddf338d | -13.19856 | -46.3583 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ddbc140-c8f2-3a32-a13f-760d2ecf7bc1 | -13.19801 | -46.3326 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c71de07-aaea-35fa-9007-c9c3ab2298e3 | -13.19662 | -46.33968 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 729d88f5-e937-32f7-8294-2ebc7980ca38 | -13.19594 | -46.34317 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 10b69958-6c65-3988-869c-5916716fbac3 | -13.19525 | -46.34664 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7ec968be-ef6b-394b-b047-c3049875a448 | -13.19457 | -46.35012 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45c90496-2dfd-3e65-82f1-1e6d9cbc1834 | -13.19388 | -46.35363 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4d67080-2234-376a-b497-90d82f133f37 | -13.1934 | -46.32767 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| aed56e36-0047-33df-94a9-19bb25e4c8f0 | -13.19318 | -46.3572 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b6012ddf-f502-33ac-a25e-57b509587bd4 | -13.19269 | -46.33124 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 28867880-48c6-3bc2-980c-1ab3644bde93 | -13.192 | -46.33479 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4119d9b9-5fbe-3146-81c5-438c7a126ab5 | -13.1913 | -46.33832 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| bb51540d-025e-3fad-9ed8-647ccbc6cba1 | -13.19061 | -46.34184 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ccf788f-ae64-35cd-8b84-b36afcd92c38 | -13.18991 | -46.34538 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 20902507-a9ec-3565-b1ac-ee3d6e29f6d3 | -13.18921 | -46.34895 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2635c9a9-13d3-3e4a-8e41-04d339446e51 | -13.18849 | -46.35256 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0684f098-496c-3db1-8d1c-6864a1b01e9d | -13.18779 | -46.35616 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3bb4cfcc-3309-345f-a79d-7af1b6a5ad51 | -13.18708 | -46.35973 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 28f51ad4-7901-387f-bc20-990a132260e5 | -13.186 | -46.30861 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f79bc2-1006-3ef2-8d3c-54dd98733fe1 | -13.18527 | -46.34056 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d0e91fd0-a88c-3a96-84fd-18948b0ea5d5 | -13.18523 | -46.31251 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98bb38b6-19ae-335d-ad5d-2216bbe54021 | -13.18455 | -46.34419 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| febb4268-0e43-34a8-80bf-926e09fd8947 | -13.18452 | -46.3161 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f46aae51-427f-3c81-a30c-06f90a6eb425 | -13.18384 | -46.34783 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 35167d5e-33db-3155-8d6d-95d414432a8d | -13.18382 | -46.31963 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ecb056a-44ea-3f7a-8c9e-e646a81e568f | -13.18312 | -46.35145 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e17d3ab0-f758-3fcf-87df-fd78f3870481 | -13.18241 | -46.35503 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 5e3b9c87-5705-376e-87f2-9ca21fd33d22 | -13.18172 | -46.35856 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b86b3c03-6072-397f-9303-ca4a7aa518c5 | -13.18005 | -48.50964 | 2024-09-30 03:45:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be0a7a8a-a3c8-3356-a744-13132464c0cb | -12.83689 | -44.27383 | 2024-09-30 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b889aec-b490-386e-99b2-8040791ba5de | -12.797 | -44.81117 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 642ff17c-4957-3bc1-85c8-8ca0fa2f8c9b | -12.78299 | -44.83195 | 2024-09-30 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1581e06-3660-3382-b15f-48f88613430c | -12.73412 | -43.4771 | 2024-09-30 03:45:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03f9f414-bfe2-3e01-b948-f9617fa9c95e | -12.72877 | -43.4809 | 2024-09-30 03:45:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42ce32ff-6431-3f33-b1fa-b7ac4f6f0222 | -12.72704 | -43.49015 | 2024-09-30 03:45:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eefa24be-c49c-31b9-9b33-2fe513cd246f | -12.72169 | -43.49392 | 2024-09-30 03:45:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9541106-1260-3b45-811e-1933f9153401 | -12.45953 | -38.48036 | 2024-09-30 03:45:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 14b94660-7c57-3128-ad7f-df9696a662b5 | -12.10142 | -44.99548 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1dfd885-6278-383b-b2b2-8d4758eb98d9 | -12.10057 | -44.9964 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dee258b8-9f39-3ae1-8b03-257e3ff1594c | -12.10003 | -44.99922 | 2024-09-30 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc3d5f9e-09b5-35ca-a542-1216a09ce25c | -22.72725 | -44.82017 | 2024-09-30 03:47:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| b924dc7c-7dea-35ab-ba12-38fc54507c49 | -22.7264 | -44.82447 | 2024-09-30 03:47:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 952007d7-55d6-343a-99a8-a6eb6bae7909 | -15.2838 | -47.50276 | 2024-09-30 03:47:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95f5d750-b230-33a9-864f-c432ce57a7ef | -22.90551 | -43.65801 | 2024-09-30 03:47:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 73193239-9387-36f4-8ff4-5604cba42644 | -22.78546 | -43.75834 | 2024-09-30 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1574f763-e176-317f-aaea-b3a7a7f3d961 | -22.74047 | -43.76373 | 2024-09-30 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c7f40dfb-5c97-35bd-9917-9cd737a00e06 | -22.73954 | -43.7687 | 2024-09-30 03:47:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6b39a5ad-0685-3a72-93a5-130e5cfc4de4 | -22.70186 | -42.1602 | 2024-09-30 03:47:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 69a6640c-31c7-35c9-9fb5-ab939f9f1798 | -22.69909 | -42.15509 | 2024-09-30 03:47:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 285332c9-1e70-3582-8bb8-2da161249e3d | -22.69831 | -42.15945 | 2024-09-30 03:47:00 | NOAA-21 | SÃO PEDRO DA ALDEIA | RIO DE JANEIRO | Brasil | 3305208 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d0d3b1f7-e75f-3d80-bc3f-8a9c2fa6d28f | -22.60219 | -42.20967 | 2024-09-30 03:47:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b22f6df4-d8b9-33d7-8482-48742900a736 | -22.6014 | -42.21409 | 2024-09-30 03:47:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f6cb6d9b-96cc-3955-8286-c379da25c530 | -22.49771 | -42.05814 | 2024-09-30 03:47:00 | NOAA-21 | CASIMIRO DE ABREU | RIO DE JANEIRO | Brasil | 3301306 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e585f25-c188-3630-a46a-81d8d2415de9 | -22.46414 | -41.91902 | 2024-09-30 03:47:00 | NOAA-21 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e4f9b5ad-dd87-3c58-811f-fbd830511c66 | -22.4634 | -41.9233 | 2024-09-30 03:47:00 | NOAA-21 | RIO DAS OSTRAS | RIO DE JANEIRO | Brasil | 3304524 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7e7d9af2-5edf-3d22-8554-7c5bfe2b8751 | -22.3885 | -43.38972 | 2024-09-30 03:47:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e6d87bfc-a057-34b2-b68a-e584696f7a43 | -22.38752 | -43.39499 | 2024-09-30 03:47:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e01ef04f-c543-319a-8b9b-b13d8cd8ab7e | -22.38374 | -43.39414 | 2024-09-30 03:47:00 | NOAA-21 | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| eca42ef2-b73f-35ce-95b5-d41444865f59 | -22.30704 | -41.87983 | 2024-09-30 03:47:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d74b6eb3-03ae-32f4-887d-30081190bc95 | -22.30628 | -41.88413 | 2024-09-30 03:47:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b61243dd-ecef-3a6b-a03b-5d9cdc5e5944 | -22.23041 | -41.77694 | 2024-09-30 03:47:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4892cb17-318c-3eb2-b7b6-bbb47cb645f3 | -22.22966 | -41.78117 | 2024-09-30 03:47:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7e40c6ad-0ea2-3e71-b879-7a71ba42ca3e | -21.98498 | -46.81568 | 2024-09-30 03:47:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd8370dd-6613-3247-9c4e-71b74e57e596 | -21.98112 | -46.81804 | 2024-09-30 03:47:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 4a325c11-ae5f-3e1f-b129-24586e55ca63 | -21.98029 | -46.81459 | 2024-09-30 03:47:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67c53b44-6250-335b-8f2d-d7736e7cf993 | -21.9792 | -46.81996 | 2024-09-30 03:47:00 | NOAA-21 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 931596ca-362f-3e11-aec5-c1e398d34bb1 | -21.9343 | -41.5554 | 2024-09-30 03:47:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c533dfa2-c2c5-3e48-8a8c-b78c27cfae18 | -21.9308 | -41.55471 | 2024-09-30 03:47:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c4372b3-d37b-344b-a183-a61020f1f4ee | -21.92925 | -46.03986 | 2024-09-30 03:47:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 68639cfa-d38d-3515-ae00-6cc9b7edf625 | -21.92673 | -46.04195 | 2024-09-30 03:47:00 | NOAA-21 | ESPÍRITO SANTO DO DOURADO | MINAS GERAIS | Brasil | 3124401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9498bc8-b46a-3acd-8c64-700020cf64ad | -21.86331 | -48.37153 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 071f2606-ce74-35f1-a800-215c297835bc | -21.86266 | -48.37095 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 906b0bce-b9ea-341b-83e5-e80087371b6e | -21.86256 | -48.3749 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4135a5c0-c8c1-3dab-a016-2870f93e6585 | -21.86194 | -48.37431 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3899bfc6-2a6a-372e-bf92-ebf00b8d0eb7 | -21.86181 | -48.37828 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README23.md)
