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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21a32432-49f8-3ad2-afc0-91f64ab65c00 | -13.37391 | -47.58209 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b6aeb25-da14-3fce-9521-64018c75a717 | -19.66185 | -45.92307 | 2025-10-06 03:38:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f277e55b-0450-3ec1-9449-a938d5fc7f2b | -20.14125 | -40.839 | 2025-10-06 03:38:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| fb69a4cf-cba5-3b81-9de5-4101fe580b7e | -17.25916 | -46.91955 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e268d449-e4fb-3bfd-ab18-fd9f276ad071 | -16.32416 | -41.95245 | 2025-10-06 03:38:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 81541e17-493e-3392-bc77-5676ab63aeac | -13.55503 | -47.24029 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc468d58-4445-3bd9-bd13-ebd71617a2ce | -14.32185 | -47.656 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3b929c3-f47a-340d-aa8d-fc36cd02ae64 | -13.55401 | -47.24508 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1575a4bf-f432-34a5-b3b2-f68e1e3116ba | -20.78387 | -43.31807 | 2025-10-06 03:38:00 | NOAA-20 | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81206d62-1c02-34ab-b246-dbd4e3c9aa19 | -15.34968 | -47.99198 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49708c05-ec1a-339d-85f5-1afd64041c21 | -17.60466 | -44.45128 | 2025-10-06 03:38:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f6d6e63a-c5e9-3ee7-a66b-cc2f576caeb8 | -13.3495 | -48.05302 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ca3d5b10-6956-3ff4-ba88-109f3c47f1b7 | -19.99942 | -45.79465 | 2025-10-06 03:38:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad367912-176b-3811-9c4b-c35b315ea195 | -14.91323 | -46.83861 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 011b76a0-7ec1-3440-8274-e9d9262958fe | -18.27388 | -45.42786 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9c6ba1a-0708-3f47-8641-fe870f11bba9 | -13.3285 | -48.05441 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe65a73e-7dbf-3520-bd04-39dc6e36244c | -14.92086 | -46.8322 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 055a04ed-5885-3cba-a19a-e3ff6867a8c1 | -15.37872 | -47.98757 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abe5d2f9-0e8f-3c24-b69c-a355dddd2d24 | -14.91487 | -46.86013 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d10e47d6-02bc-3f1e-976f-22b7ff10c79c | -14.33695 | -47.71709 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65df66a8-3710-3034-8387-d6bcba86fa40 | -14.91166 | -46.86768 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7829fc9-3080-3211-9dd8-c9c2554c1877 | -17.08552 | -43.38346 | 2025-10-06 03:38:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b70fa708-af8f-3e82-a3d1-9a79313ab883 | -14.68171 | -48.39334 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6769cb90-bad0-3028-94e2-ce7daf345ebe | -15.23933 | -46.67335 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2e23a51f-ead3-38e9-bde0-f129ea2ae051 | -18.50267 | -43.40383 | 2025-10-06 03:38:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e9020a32-42b2-3056-b5e0-018d1b6e96d0 | -14.66805 | -48.27631 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cd06953-d9fa-3b5e-9bec-1f3025aff5f3 | -18.48421 | -43.90158 | 2025-10-06 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1de57722-a18d-325c-bc6d-c0f57c1d5a15 | -18.48778 | -43.90795 | 2025-10-06 03:38:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 20db13d7-6af1-3734-b655-d6ea012096eb | -17.26471 | -46.92183 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d55a43b0-97b1-353c-b342-1f49bfcd7b73 | -15.34854 | -47.99735 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dd8752c1-1cee-3f07-a3da-dbf94805db97 | -14.9138 | -46.86515 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e6aa099-3584-38f8-948e-c947da9f9675 | -15.30668 | -47.31867 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4d764d1-5ea0-3349-b4ce-93ccaa5ccc14 | -15.5041 | -46.84185 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70be0629-f629-33ad-9c0e-c45620ce71e3 | -15.34476 | -47.35026 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 873a9d3c-287f-3a19-9a19-793b33d72977 | -14.92897 | -46.82347 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e351816c-59c8-39d9-b53e-2ac81e31b851 | -14.48653 | -47.55471 | 2025-10-06 03:38:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 077ddc61-27ce-3f42-ade5-9fa8a87e7ed6 | -21.40302 | -45.05581 | 2025-10-06 03:38:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cf1a92cd-3ba4-320b-ad4c-6f13787b13cd | -13.49822 | -47.24734 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63309144-a916-3de9-864e-5ff25017edb5 | -18.392 | -45.21875 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2d600b27-ad0c-3a1f-add8-51df4cec99e6 | -18.50348 | -43.39967 | 2025-10-06 03:38:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| e5534149-dac2-383f-950c-a46cd2c982a9 | -13.36846 | -47.57603 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20d4d03a-3945-3ace-82c3-ab7014281732 | -20.1104 | -46.35213 | 2025-10-06 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f51f9a67-29db-3bff-8cfb-b0c967751f7a | -14.68025 | -48.3999 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2a2b69e7-87e2-3bb9-b7c1-e48fa84387da | -14.34482 | -47.68042 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43ff62ad-a59b-3154-9881-ecbc6118c22f | -21.30312 | -43.84296 | 2025-10-06 03:38:00 | NOAA-20 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 03e00054-f112-33a4-8857-7e67a9046171 | -15.43772 | -45.87539 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0cefb17-a104-3669-a100-36fe748feac6 | -17.07991 | -43.38752 | 2025-10-06 03:38:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 204cbe86-0c04-3c27-9d06-da45e9151a10 | -13.3352 | -48.05536 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d3e69f9-4158-39d3-9156-ebc84aca899b | -17.26574 | -46.917 | 2025-10-06 03:38:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fea58fd4-a689-3bb0-a7f4-51472f6eee1e | -14.69326 | -48.28637 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 145dbff1-61a8-37f8-a832-3d27fcc1536b | -18.27004 | -45.42051 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 399a2181-08a0-399e-ac02-40b5090303d8 | -18.38893 | -45.20783 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56960491-a310-3e76-81bb-4003a366c65b | -21.39289 | -45.08065 | 2025-10-06 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bd7c2f58-fcc2-3b32-9a78-7ac913cba2c8 | -13.25504 | -48.47177 | 2025-10-06 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4e986bc7-7bd0-3ef0-99a7-aad2f0b4d6f9 | -14.67126 | -48.38819 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab1d2eb0-c93d-37e9-906a-3095bbbb7a22 | -13.59982 | -48.69819 | 2025-10-06 03:38:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b5be485-6ebb-3893-9819-3b5448155dbc | -14.68157 | -48.40428 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 430ec396-a5dd-3f1a-8b82-f48123186c26 | -14.33872 | -47.67789 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfcf6230-ead1-32c0-a9b2-a212662de1ef | -15.72897 | -46.29002 | 2025-10-06 03:38:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2a50501-4481-3bd1-a1bb-d6dcd1d3cb40 | -14.32047 | -47.66264 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1fb53902-b6e0-315d-a16e-24287d77e7f8 | -17.07085 | -43.38467 | 2025-10-06 03:38:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 92cd3f08-2bd4-38d2-b3ba-d6ee3dfe295e | -13.49746 | -47.25096 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cdeb042-6371-3f3f-9fb7-437d73b88fbc | -20.10971 | -46.35538 | 2025-10-06 03:38:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2cd5bc7e-bc58-3342-8d41-641fcc914bcf | -17.97013 | -44.9976 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7bad974a-f146-3c03-97ab-129641950e97 | -15.74732 | -47.69492 | 2025-10-06 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 18ac7f7b-605e-3bab-a5ce-79af22e2b997 | -13.25451 | -48.46841 | 2025-10-06 03:38:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3251db79-32ff-3923-9b59-1e8bed6e1106 | -13.36329 | -48.03991 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f0c4315-0d76-39e8-9c25-e87059f77617 | -15.16959 | -45.76745 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf7584c4-d1f5-3963-8432-8b85e8c36202 | -18.38698 | -45.21737 | 2025-10-06 03:38:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4066806-d5c7-3bf3-8ae0-8fa6505bd8e8 | -15.74188 | -46.25681 | 2025-10-06 03:38:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a7cd8d4-b571-3a8b-a82f-1a5f7ba33530 | -15.34039 | -47.3104 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13482be9-76c7-365d-a2f6-7ec0c5d65a9b | -17.9695 | -45.0007 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c3067ce-74d5-3e9d-893e-fabdc2eaf71f | -15.46167 | -44.31048 | 2025-10-06 03:38:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cdc7e1a-6c5a-3c24-8d59-d6a9d724e52d | -18.87311 | -48.61452 | 2025-10-06 03:38:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25bc2548-6f6c-33b1-9f2a-1c7dfcb9e23e | -14.3484 | -47.72579 | 2025-10-06 03:38:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 420aea29-2391-3dc9-a683-1713628ce9a2 | -19.85055 | -43.68776 | 2025-10-06 03:38:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b7da58c-1f74-3220-96aa-a06fc44b1c65 | -14.93276 | -47.13241 | 2025-10-06 03:38:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59dde5e9-a3e1-3fcf-971a-fab7d43548a6 | -15.35607 | -47.99989 | 2025-10-06 03:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc9d182e-f172-3d94-b925-67277ede5d35 | -15.15927 | -45.7611 | 2025-10-06 03:38:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bae8485-3a42-31c0-9e28-dc640c51249e | -19.01739 | -45.02571 | 2025-10-06 03:38:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9458d200-593e-3f60-8c71-18e50f8b74b8 | -14.55135 | -46.65013 | 2025-10-06 03:38:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f02d9e99-69a3-30cf-af8a-606a959a2582 | -21.39175 | -45.08625 | 2025-10-06 03:38:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 18d5d9aa-eb61-305a-ac37-d62edbc4f266 | -14.91083 | -46.84151 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d45eb5ec-88cb-326e-917b-d4a7cd28c410 | -20.11514 | -44.40896 | 2025-10-06 03:38:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 960134ed-e01b-305a-9a4c-d279d09122f0 | -19.62892 | -45.9251 | 2025-10-06 03:38:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2a9b6f40-9050-3ff1-abf0-e1d530dff36c | -17.95371 | -48.55298 | 2025-10-06 03:38:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb039288-9d57-392f-b23e-5b9906c3f833 | -14.53481 | -46.96815 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ec8a004-46cd-35c3-ae24-669d38ad4cc4 | -14.71061 | -48.3873 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2e9b56b-86a0-3027-a7f4-8b6b10ae9cf5 | -14.94001 | -46.83032 | 2025-10-06 03:38:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94cd562e-fd3b-37da-b46b-145c94141783 | -21.10671 | -44.21414 | 2025-10-06 03:38:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fa545110-4252-3124-a9ee-a635491aca38 | -15.74114 | -47.69349 | 2025-10-06 03:38:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 361dc6ca-3663-3cd3-9054-2bcfbf0d607c | -13.36212 | -47.57706 | 2025-10-06 03:38:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5becb8a3-35b0-3fce-ac87-66f6957f5549 | -20.13664 | -40.8429 | 2025-10-06 03:38:00 | NOAA-20 | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.0 |
| b688e926-ebf3-349c-9b1c-5ed789c515e5 | -19.9404 | -44.64062 | 2025-10-06 03:38:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0607910e-69a6-3443-9b93-cb6c38d07886 | -14.6987 | -48.37889 | 2025-10-06 03:38:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb78d2c9-504d-330d-b395-25e01e3805a4 | -18.50357 | -48.35443 | 2025-10-06 03:38:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08ee2bd3-13e1-3af6-b947-c6dc623d4c08 | -14.26671 | -45.85275 | 2025-10-06 03:38:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7aa9cae1-9cdc-3398-b251-238f33eed83e | -13.55096 | -47.24612 | 2025-10-06 03:38:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c513ad90-9f7f-3726-ae6f-ae8c4f688288 | -18.27321 | -45.43104 | 2025-10-06 03:38:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2b5774f-e791-32bb-ba89-fe12ee42e63a | -18.02086 | -44.9995 | 2025-10-06 03:38:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README20.md)
