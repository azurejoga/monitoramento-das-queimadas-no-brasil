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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1342d09f-ef63-3b26-9ac5-763f2e40fa60 | -16.09209 | -49.96888 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 158828d7-ccf8-3b94-af0d-738fb7334ee4 | -16.55647 | -49.21801 | 2025-09-13 04:10:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8bbd137-b7c9-394f-b6c4-65e1fcbd7940 | -19.20366 | -44.62431 | 2025-09-13 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fac383fc-5d97-3f60-9396-9f6fb0bc660e | -17.15299 | -48.48751 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b541435-eee7-3b4c-b701-3a6171e54e81 | -20.55493 | -45.83151 | 2025-09-13 04:10:00 | NOAA-20 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c2903410-3aae-3686-90b2-6171bd6a26ce | -20.02538 | -47.64084 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee27ea73-6d00-3dc3-961c-814076799a9c | -19.99473 | -46.93076 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 934b9e2c-4464-3865-9696-bb34439e5ace | -15.03817 | -50.17634 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a3a6f4f-3e9a-3a52-a1f0-e3de1ceee539 | -20.01966 | -47.65277 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f4ee9826-548e-32ce-a239-e995ab4c70fb | -15.13741 | -52.47269 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d3c9f75-fbb2-3b70-93a4-c276a0a7ed2d | -17.94567 | -46.00151 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3742eba7-7d1e-32bd-9b1d-1c4e69c745f9 | -17.28099 | -46.11161 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| d2c047b8-4c24-3a00-9ce0-fdea2209dc6c | -16.36851 | -41.38057 | 2025-09-13 04:10:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e00de18a-df54-32da-9512-916f14896f5a | -14.62371 | -52.0863 | 2025-09-13 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df2302cc-3a62-302c-bf0e-e9d7c0f57901 | -20.01479 | -47.63858 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c582df7b-b81c-3b76-b2c1-79dc775493af | -15.34906 | -47.25947 | 2025-09-13 04:10:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26ac3d55-be3c-34c7-bb2c-546954ab8269 | -20.02611 | -47.6366 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6cb0d138-b6a7-3da1-ad3a-7e760fb076b2 | -18.47007 | -39.76605 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.7 |
| 2a790334-d5c4-3dc3-98d1-b3ef532531af | -21.92977 | -47.57122 | 2025-09-13 04:10:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62e9be7b-3601-30a7-9663-a9b37ea548ee | -16.29202 | -45.68615 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d06f26c7-c7d8-3ebc-bce1-bef987e00db3 | -17.9486 | -45.26357 | 2025-09-13 04:10:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb67b849-57cf-3b5d-8561-5c22e8322ebe | -19.25884 | -51.42791 | 2025-09-13 04:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6943950b-6c5e-3bc0-98be-42fc34e0cc32 | -18.41044 | -49.40783 | 2025-09-13 04:10:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b3dddb3-6da4-39f2-bf6b-6aac29517c22 | -17.15179 | -48.48528 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2674c459-a8e3-3c17-bdc8-53989e5257f8 | -21.12747 | -45.95013 | 2025-09-13 04:10:00 | NOAA-20 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c03af82-02f8-3898-be92-b9163a547f74 | -15.13684 | -52.47557 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31c1927d-6348-3025-b0cc-334e21f51639 | -18.85203 | -46.83685 | 2025-09-13 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e25a211-01fc-33bd-85eb-e264edc6d138 | -21.06524 | -46.14016 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3959d4f-77e7-3dbf-9236-f9cf6be5f61e | -16.88346 | -45.76044 | 2025-09-13 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3837007a-65cd-35d5-9c8e-b923a343eed7 | -16.88366 | -45.78016 | 2025-09-13 04:10:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8b6c8d5-774d-36a1-9293-99d1d5c6cd54 | -16.05848 | -50.00629 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b9563cb-5bf6-37dc-9038-84f6018f3bf0 | -18.33084 | -50.96857 | 2025-09-13 04:10:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf15c83b-7438-3552-b24a-fa239ddf5544 | -17.99362 | -46.9359 | 2025-09-13 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50af04c6-ba08-3919-a9a8-62ecbca8b81a | -15.10995 | -52.47657 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7b30a97-4b65-365d-9f2c-cf48144740a4 | -15.03902 | -50.17181 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5fa547a-ea87-3488-be5e-61ffd0be02c9 | -20.59797 | -44.91075 | 2025-09-13 04:10:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f44d174f-3f38-3100-8ca9-20c99ab23dc2 | -15.04344 | -50.17267 | 2025-09-13 04:10:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec472830-20c7-3f68-a6d5-b8b5f0a0e507 | -19.98507 | -46.90406 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b7a783f-d401-3b52-a3e6-77436a07dc7c | -16.08789 | -49.96763 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 883e11df-9774-3700-81cd-cc6222518e26 | -16.49601 | -55.15184 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ff860a82-0d53-30c6-988b-555d75539d44 | -17.42643 | -49.2247 | 2025-09-13 04:10:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a55713f4-2af4-3ca7-8988-c6de5215035f | -20.59581 | -44.90282 | 2025-09-13 04:10:00 | NOAA-20 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e30f8f34-97b2-3567-9729-294c471348c3 | -15.77486 | -52.23414 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5f65596-6124-3a25-aafa-2a45d2794a54 | -15.06567 | -52.47598 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 23d0746b-7aed-319a-8388-d5c1301d7f55 | -17.28257 | -47.24332 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff33e78b-d73a-36cf-92e1-a0ba2d42e711 | -16.33418 | -51.54077 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e147fa0b-67a7-3fef-ba0f-99ce3965e300 | -19.03924 | -46.65959 | 2025-09-13 04:10:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d79abd1-b27c-3232-a43c-01bebfc2f4a6 | -19.95353 | -49.27216 | 2025-09-13 04:10:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9713bce6-6913-3def-871b-df09645fc808 | -17.12409 | -48.4847 | 2025-09-13 04:10:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa6e6347-ad4d-37aa-a51a-0d46dea8561b | -21.87278 | -47.4774 | 2025-09-13 04:10:00 | NOAA-20 | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 872c1b7b-d991-3253-b0b9-0158d079a255 | -22.61073 | -47.66246 | 2025-09-13 04:10:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f968713-c4ac-3969-8cb2-5396c139c5b0 | -16.07891 | -49.99208 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72a72ef7-515f-3666-8126-c84f3060b7eb | -17.90888 | -45.90443 | 2025-09-13 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b353896b-d86e-3c72-91c1-8a97f901da5e | -15.70852 | -50.58501 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d6c32d9a-4fd2-36ea-a565-3c3f82f0edcc | -17.44574 | -49.23227 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e11a15a-22a3-3d33-8b2e-bca9b7e43850 | -17.34711 | -42.63369 | 2025-09-13 04:10:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7091fbe3-e206-3bb4-9e03-102909c92571 | -16.4269 | -45.6977 | 2025-09-13 04:10:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18226488-6969-3147-848a-827f8c4f53f0 | -16.49449 | -55.12981 | 2025-09-13 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e3aa52e1-e015-3ec7-9b9e-8049b8e7e503 | -17.33606 | -46.66155 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4998bef8-30db-3ec9-8cbb-41233819a361 | -21.65103 | -50.11731 | 2025-09-13 04:10:00 | NOAA-20 | ALTO ALEGRE | SÃO PAULO | Brasil | 3501103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 09c7d44c-0fce-3135-b796-f4e89096d028 | -16.47991 | -43.68046 | 2025-09-13 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb523239-f62a-3957-be5d-dcecd8ca1f90 | -15.16064 | -50.15173 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d41ca3d-0578-326a-a0ba-14871b8e7c22 | -17.35875 | -42.70422 | 2025-09-13 04:10:00 | NOAA-20 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e10ce6b6-3fea-36b0-a319-7115ef1e23d9 | -20.44827 | -46.45137 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 128a4414-dace-3bc1-9a7f-4a77167a25cb | -18.60872 | -48.20633 | 2025-09-13 04:10:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cbec838-8f57-3486-9378-448cc558ccaa | -20.01539 | -47.65633 | 2025-09-13 04:10:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbc69701-3762-3ebe-8983-427de762a8ba | -17.3044 | -48.73913 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d19c4793-96e7-3cb5-a268-306b71d413b2 | -15.5937 | -54.76797 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0ee6e57-22a6-3b65-b7b3-5515130cf967 | -21.0646 | -46.14401 | 2025-09-13 04:10:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9cf2ea4a-0f80-3e5d-a958-a91ed460ddb7 | -17.71016 | -40.26107 | 2025-09-13 04:10:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0ff773da-a58d-3a80-a620-43693b98c9e3 | -17.30052 | -48.73833 | 2025-09-13 04:10:00 | NOAA-20 | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 78cd9b60-fb08-3f51-a309-d0fde6db1ce3 | -17.91225 | -44.4582 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7b024f19-4dc4-3413-ace4-cf406e1efff9 | -15.11554 | -52.50195 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a2e50bc6-b9a0-346c-bd3f-fdc980f3cb24 | -19.63392 | -43.73451 | 2025-09-13 04:10:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b08e3a0-5e1b-33d5-84ac-20286560858a | -19.65368 | -45.85958 | 2025-09-13 04:10:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f376713-462b-3040-87d6-59dc5bc5beb2 | -15.69961 | -50.58294 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45b9a666-f446-32fd-b8fb-ae38a96e19b7 | -18.70903 | -51.78942 | 2025-09-13 04:10:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 062e6cd2-0c3f-3329-a062-fdfec30666ab | -15.84881 | -49.93959 | 2025-09-13 04:10:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ddc60edc-5d9f-3c4a-a569-e1a6cdd36fa9 | -15.5913 | -54.75924 | 2025-09-13 04:10:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4613cb88-a27f-3223-941c-7e825745715e | -20.10586 | -46.91724 | 2025-09-13 04:10:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6fc52911-376e-3ad9-8365-126df4d7b40a | -17.91945 | -44.45573 | 2025-09-13 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4bee4549-f655-3d88-bc49-69902551090a | -15.14082 | -52.48236 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9603555e-376e-3082-a977-9e40b765613a | -15.60874 | -47.92984 | 2025-09-13 04:10:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b60794d4-a7e4-3d76-8157-3d19a8f06fda | -16.52516 | -51.75222 | 2025-09-13 04:10:00 | NOAA-20 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 414c01ea-cd8f-3a4b-af4b-95cd7b1afd9e | -21.62847 | -46.80409 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 22d60dc3-3e74-315b-9974-7430a82f1afb | -15.75842 | -53.50224 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c7638fa-7f47-38be-96b9-82867ae087ae | -17.4126 | -49.25515 | 2025-09-13 04:10:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3ec2c7e6-a7e2-3ef4-a5e5-b107489bdb84 | -16.87242 | -49.34536 | 2025-09-13 04:10:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11fc2684-d42b-3ae4-82dc-b7bfa9a67b13 | -19.98851 | -46.90467 | 2025-09-13 04:10:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49f5a519-0bab-3200-b75d-6624f97f49f4 | -16.40036 | -49.06502 | 2025-09-13 04:10:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dec454f-8edd-32e2-b9b6-4043d8a1df87 | -17.37381 | -52.91266 | 2025-09-13 04:10:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a1baa08-3e71-3908-9ac2-9cd4d4dc9122 | -16.08244 | -49.99702 | 2025-09-13 04:10:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27f74ed4-13eb-306e-ab8f-956df242090b | -15.7654 | -53.4958 | 2025-09-13 04:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 658f0602-efce-3305-9c78-102278a1d636 | -16.35457 | -51.54087 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3d8984f-de53-3fcd-8d4d-04e9c2307556 | -21.61632 | -46.81389 | 2025-09-13 04:10:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a5ad043f-488a-3d30-b294-ededcc2fd0bf | -17.41189 | -48.22116 | 2025-09-13 04:10:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 20cba0be-4fbb-37f1-809a-8a4279865e2c | -16.34102 | -51.53071 | 2025-09-13 04:10:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1ffae295-3a8b-3c20-8689-fe139613a5d4 | -17.31718 | -46.66644 | 2025-09-13 04:10:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07a997b8-c685-3797-8d9c-2cd18125b072 | -15.67788 | -49.90359 | 2025-09-13 04:10:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 8f01bc9d-2a7b-3549-b50a-ae0e8ad19205 | -15.32218 | -52.904 | 2025-09-13 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README67.md)
