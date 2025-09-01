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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbc5ec86-d928-3fbd-b4f0-b73832fdad37 | -6.8528 | -52.81698 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 16b42b90-c0a2-334c-8b2c-4ebcfd03ecc5 | -7.70529 | -50.28027 | 2025-09-01 05:25:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac6dc9a8-8db4-3f92-8af0-7ffc0cc018dd | -15.72017 | -49.00638 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bb951d19-56f7-3f2b-b0be-17d3de7c8d89 | -12.44109 | -63.92477 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6bade0a7-a97d-3d6a-a703-a3a095567c11 | -12.4451 | -63.9216 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83ebf695-7eea-3305-ae1d-d2849c22f165 | -11.52365 | -54.46715 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5871945c-bcf4-3f70-9e39-ba650bbfaa10 | -5.75928 | -53.40322 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 802fdb45-1458-3827-8072-e98b1f1d7a88 | -12.58134 | -48.21961 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 84e70240-aa46-3548-a121-c080c9e81532 | -16.09316 | -57.69436 | 2025-09-01 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 53d3b009-9740-3485-aab7-e2602bf9db35 | -6.83578 | -52.83105 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| acfbcf4b-f1f7-3279-a886-673c0291d3f4 | -12.43366 | -63.92736 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a4b4a8e-6d03-3253-917f-6bb05d2ae156 | -6.84713 | -52.82158 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fc6c9a6b-fc50-3c27-9a6d-03eeafba1b37 | -12.4417 | -63.92102 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2da1b8ea-a36b-3352-a4bf-39afc3e49f87 | -15.29728 | -52.78805 | 2025-09-01 05:25:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52f4ac72-c644-3d64-a536-9bdbab985001 | -18.66383 | -52.5983 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1c59d511-c2a2-37aa-9e98-af819d141060 | -10.50138 | -68.1059 | 2025-09-01 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b36b3d7-630d-3f32-8fba-07fc70ac5945 | -5.76013 | -53.40728 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31a3d4a2-f030-3aa2-aaa6-f66920ffffd4 | -6.34648 | -53.42868 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| acb3e7d4-f2de-31b4-a5e5-b4bf3a8581eb | -15.72521 | -48.89671 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5106e44c-a6eb-3e77-acf4-32cd3c8221f8 | -12.57502 | -48.21149 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2e43c23b-836e-320e-9cf7-1ac407fde346 | -11.88546 | -51.703 | 2025-09-01 05:25:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bd8aea3-5f9e-39d9-895f-79170e83e263 | -12.96094 | -48.11578 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95557cc0-1799-35d9-898d-756342c0af6f | -6.79863 | -52.80883 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 059e92ec-eba5-344c-b0a0-f65fb7fc2242 | -15.30323 | -52.78509 | 2025-09-01 05:25:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2baa356a-0071-3a59-86c0-60f2e66e4994 | -12.44789 | -63.92591 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8e0f51f-1ddd-3eb2-9190-162bd85ebbc7 | -11.59219 | -55.55533 | 2025-09-01 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 713b991a-da43-3407-a804-c29ec3cfe6e1 | -6.305 | -57.92879 | 2025-09-01 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 554782cf-3b9c-3cac-8b29-2472d9b09d2e | -18.66421 | -52.60011 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 31a0ee8e-2e53-3be3-ad2c-4fb5cbf33c5e | -6.3357 | -53.43729 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c6c852e-99b3-337c-ad6d-384cb876dece | -6.81504 | -52.82196 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0b6bdff-fad8-386d-a0d5-ad018b6fbe42 | -10.36451 | -68.59387 | 2025-09-01 05:25:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f4c6c04-f077-3214-8ff1-97d6dd9cf31c | -6.84375 | -52.80969 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d5e712aa-22e4-3e48-baf1-a66bd896bdf8 | -15.71491 | -49.00642 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ee849b0d-4281-3bb7-a126-ef92d2f832f1 | -16.49479 | -54.81776 | 2025-09-01 05:25:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a9ca30e8-c81e-38b2-a3b8-2e5205ede659 | -12.42407 | -63.9219 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8fcf1baf-81a2-3211-9907-fd3ef2e05f23 | -12.60075 | -48.21248 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| baa733a4-c1fd-3682-99cc-5b37870b75e6 | -5.82995 | -51.38137 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd37bf80-907f-3dd9-9ecd-1765454ea153 | -12.86134 | -48.06761 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ef170716-8141-35b1-abff-8df04a7d9b2a | -11.51826 | -54.47159 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5e305f5e-dd08-3fb3-acf3-ad25b6643f2f | -14.5348 | -56.23942 | 2025-09-01 05:25:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a82bbc8b-fab9-3a4e-a700-95934a5670d0 | -18.65797 | -52.59763 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 536a6013-e7cd-3a77-b3e6-01dbc488c23d | -16.29354 | -52.9417 | 2025-09-01 05:25:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db53de4c-df36-3861-af1e-afac10157cac | -12.57096 | -48.22252 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 788d2b66-c691-360b-9bd1-7b3016a2836f | -9.95212 | -66.87443 | 2025-09-01 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdaafc57-dfee-3f85-a87c-5fb1a90efe82 | -14.49912 | -53.16079 | 2025-09-01 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| abc9f771-042d-37b6-bd76-8bcc38888d3d | -12.43768 | -63.92419 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45099a09-a463-3a07-a7dd-dc1e07d23bfb | -6.84146 | -52.82629 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 15dff171-523d-3e44-bf76-4bf6946ddc7d | -14.56183 | -52.99598 | 2025-09-01 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 79c80ccd-19b2-3187-81b5-099c5b3a967d | -15.73077 | -48.98876 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4cdbed39-54c2-3a10-99fa-e24eaefd20ba | -6.34038 | -53.43798 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eedbcafd-868f-3a35-9d1c-bd23c6354a71 | -6.79789 | -52.81431 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1d17d0ba-8300-3a2a-94c0-8f885f8e2e48 | -10.08904 | -68.46808 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15cd8933-e6d9-3d65-895d-eea274d6206e | -10.11765 | -68.27924 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c61b68ea-4780-30a5-9746-804d5db87a28 | -14.48883 | -52.9921 | 2025-09-01 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e2ee66a-bb55-31aa-b64f-3551d2c98a5a | -12.88295 | -48.17053 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3c973fa-0c20-328f-b30d-e0b8b120b36c | -6.86495 | -52.8019 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44901179-be8b-3364-9409-0110f2772935 | -15.73139 | -48.98219 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 28.1 |
| d12123d2-0a17-30fa-85d5-a642fb026a8a | -6.33171 | -53.43166 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8100758e-75b0-3ca4-a402-b844d6de81cc | -12.44387 | -63.92908 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89760ce5-7f72-322f-8dbc-f0ce5bd9b60e | -12.56718 | -48.21758 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b9450827-2e8d-3101-9ea2-6eb03d3d99dd | -15.73606 | -48.98703 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ad73f09-24cf-3a11-8503-985fab140db8 | -12.64488 | -48.20353 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b3e0f2d-2a0b-34a8-aaf5-2e28359d3b5b | -12.98259 | -48.11698 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8a16537a-a065-31c7-9442-3ff0dea52b14 | -15.72954 | -48.98056 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| ec99493c-4bf9-31aa-8fe1-0255210ad2db | -7.70587 | -50.27573 | 2025-09-01 05:25:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6f17caa-bdde-3ff4-8800-6d33d1d48c59 | -15.73666 | -48.98032 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 10c072b7-92f0-321c-aab0-53cfb9ade50b | -12.96153 | -48.11003 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 626f96a5-12c6-33dd-a722-09dd21e79258 | -12.44047 | -63.92851 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be152e91-f0a2-3d7b-966a-f98daf223f32 | -6.43363 | -55.62447 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8598d56-9c54-3fe4-bd87-feded56ba460 | -12.60004 | -48.21943 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 67a22698-40fc-39e3-8d4d-595aa25cca8e | -6.43568 | -55.61024 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4225373d-ebff-357f-83a9-5bb64b700cc4 | -12.87942 | -48.17248 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b10a7327-6c83-3281-96be-be56ac2f530a | -12.8765 | -48.16254 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cb191814-a46b-338f-b15f-649f2b8bcb2a | -12.8544 | -48.06435 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 50494b4b-3c82-36d9-98fb-25ba54dd14c9 | -6.82176 | -52.82342 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2b6824c6-2887-3192-a3b7-11e87eeb573e | -12.83831 | -48.07954 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 445ef87b-1914-3333-b3f8-e18216d68e13 | -12.77618 | -48.08789 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40556424-974b-3328-bea2-296c4be50a25 | -14.02126 | -54.0344 | 2025-09-01 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff440920-94bb-32ab-91cc-b0c546991f50 | -15.69111 | -48.95698 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ede0c538-84ef-3bca-92a2-7d316443c3b0 | -6.80772 | -52.81593 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42f45b29-3223-3d01-8441-677eec66beaa | -15.62943 | -55.92406 | 2025-09-01 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 632df0e6-577b-322f-8e89-cbe4df9fc190 | -6.84221 | -52.82083 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| eba54b23-cd54-3fb5-8680-ae7b3a1b7bf2 | -9.66453 | -68.97277 | 2025-09-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2d63f4e8-cd15-3705-b19a-4d1ce1366b1e | -10.26763 | -68.78852 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65bb3c46-790f-3118-b57a-860448acb9fb | -7.40176 | -47.44015 | 2025-09-01 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e81dd3b-67c7-3b88-93fb-a44dacf2b8d3 | -6.8028 | -52.81516 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bb9e4f2-1531-39af-a38a-37bfa5a41475 | -12.22333 | -64.22361 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 540709ea-c6a5-3f80-a967-2c611af54b88 | -10.08472 | -68.99632 | 2025-09-01 05:25:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7a805ea-311f-321a-a4ea-45fa18333a31 | -13.97684 | -54.06431 | 2025-09-01 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29bd8299-f9bc-375b-9a10-2afd821dab24 | -6.80975 | -59.66714 | 2025-09-01 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28b1d649-d06e-3c3b-a4e0-3b9acd3fec81 | -12.43428 | -63.92363 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03fe59be-b5dc-3613-b103-9821d71eb512 | -6.4387 | -55.61795 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7470274-fa4a-3cbf-9d9c-ecda939fec69 | -12.57878 | -48.21624 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 915f577b-e5ba-303a-8c4c-7a22f9eb1617 | -6.8479 | -52.81606 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 03d73b83-86fb-3d7a-8298-940494d8c654 | -6.83087 | -52.83028 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 43e7503a-ba8d-3e50-a7e4-e99633f8e7b9 | -6.44223 | -55.6221 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3fb9bb5b-017a-36fc-aa1d-ec1e789abc45 | -12.88013 | -48.16568 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6397ca62-1445-3734-8c28-bcb89bf62cee | -6.80599 | -52.81504 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b5dae96-67e6-3a17-b1c3-64672ab483b4 | -15.69683 | -48.89487 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 15e41458-a7be-385f-a9a6-c8983941f51e | -10.26812 | -68.79137 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README83.md)
