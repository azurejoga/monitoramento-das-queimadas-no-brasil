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

## Dados Diários - Página 139

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10b2eb8f-2f5f-3912-b98d-bea8b77439c9 | -17.84381 | -50.50538 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 091d2ed6-d7c3-3517-8dc1-6659626d98f3 | -15.60476 | -56.41193 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 67a11a48-e0ba-3cce-8715-be28f3f8d389 | -15.63726 | -56.38312 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e1a9536-ee42-3f81-97ef-dee7d554e128 | -14.95873 | -54.56923 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 0f060332-69c0-3381-9c23-d4cf74b1e0ab | -17.86889 | -50.52103 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5b72b6ac-e708-3f36-b5ae-f7f09b39aa98 | -19.19596 | -57.35922 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 41ac28e4-2fe3-3659-a15d-b95de4b36404 | -14.08919 | -41.34621 | 2026-08-31 16:48:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c724c3ac-f2a2-370d-843c-95ea165cf168 | -14.44882 | -49.00663 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 0901e36c-ded0-3859-9b69-44116896712a | -15.65353 | -40.95683 | 2026-08-31 16:48:00 | NOAA-20 | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 72d39421-4acb-3980-8994-99c097000404 | -20.26967 | -58.14149 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| af2a189e-9570-3409-a974-3a53a8a76bcf | -15.09277 | -48.3676 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d2bc98ae-f877-35f3-9d81-8a60586c068d | -15.73996 | -56.10542 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 7a5de9db-03c1-3de5-93cb-d797fbe00ae6 | -17.37149 | -44.87803 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a297714a-9074-3c01-a7e0-c39ad5407902 | -14.80658 | -40.67271 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 6b759bb0-07c3-3d14-844b-58cda4252876 | -13.61112 | -40.64568 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 91189741-a4b7-3df5-9a1f-3b3fb9eb7640 | -15.33001 | -56.19903 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 43475086-3079-3dfc-9445-2d2ff01f5f3f | -19.10086 | -57.40374 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 8170fa7d-b8ca-3c77-8ff0-66e22c65fa3e | -18.26462 | -52.72079 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 01fc63ec-095e-38cd-a6c5-e2da0520d308 | -19.21975 | -57.35682 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.7 |
| d1f4b1cc-3aef-371e-a0a6-fe64c7bcdeaf | -17.35664 | -45.81186 | 2026-08-31 16:48:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fd38e5d9-0bd8-3396-b75d-2adb12910c6e | -18.1228 | -51.61605 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c82e1c01-9ea7-3734-9e99-7c3d33b24524 | -15.67478 | -45.93287 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f7c37907-bc99-377e-96eb-454c4b6f92ca | -19.20235 | -57.36315 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 0d6b0fbe-5650-3be3-9b8e-2e2bd9bcbff7 | -16.19803 | -49.31546 | 2026-08-31 16:48:00 | NOAA-20 | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3fd01c49-b8c8-3050-af15-8d5502f143e8 | -19.23625 | -57.34145 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 44ce4335-2104-39dd-b07c-06abc4cc0753 | -15.88677 | -56.47204 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 974735d1-cc39-3e6c-8dc5-74f55cd53685 | -18.48197 | -43.96975 | 2026-08-31 16:48:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 284fc3eb-8c12-31f4-bafd-d5dfe8143687 | -18.47852 | -43.97041 | 2026-08-31 16:48:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2b56cfe9-aef6-3346-bedb-556e970f67c9 | -19.17646 | -57.40704 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.3 |
| 297f9cdb-2121-336f-9e09-d07326069dcc | -14.58009 | -54.11313 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 191c9e69-3255-3a2f-8ebf-b6e855784b3b | -19.18546 | -44.51336 | 2026-08-31 16:48:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dff9ab86-23c1-3695-9e47-3b6e3d719ff2 | -15.22572 | -56.36236 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 9e82fc5d-3c9a-3324-a137-e9847b75c65d | -17.87276 | -44.25356 | 2026-08-31 16:48:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2ba301e9-8987-3d4d-860b-1c9d5e2734a5 | -14.3988 | -53.27323 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 58a14dcb-6a90-392f-aeb0-9e3283a1a92f | -18.51328 | -48.33905 | 2026-08-31 16:48:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f137ee7b-9560-3516-875a-089b4a45302c | -15.46059 | -52.79769 | 2026-08-31 16:48:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 767b9ae0-5f2e-33af-9f8a-756ccd27fda6 | -16.02816 | -54.40327 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 67db07f7-1115-32a0-99d6-2edb1bdfe4ba | -15.96788 | -55.95606 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 5df42d8a-889f-3d12-8a82-7e2d5ec9408b | -13.61641 | -40.64931 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| 15a61a8a-125c-3d67-b193-7bc861b2f013 | -16.70964 | -47.64016 | 2026-08-31 16:48:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 423f441d-e279-31e7-854d-787b6e742893 | -14.57361 | -53.60176 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| bbead146-772a-3ee6-b22c-911882774a0f | -14.8587 | -42.06565 | 2026-08-31 16:48:00 | NOAA-20 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 37.0 |
| 362f64bc-77e8-3338-9479-d71c6c866b05 | -15.58088 | -56.29718 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08003557-486d-3cdf-9dc3-f0549e36d33d | -16.55929 | -52.50577 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa1d21bb-73f5-384b-9a2d-d91b844c97c3 | -14.77746 | -41.33074 | 2026-08-31 16:48:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0e13a701-596b-37d4-90e7-2e8dc2f88524 | -19.21205 | -57.33937 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| d7407f5e-77a6-3eac-a666-8ec01d470f2d | -19.12291 | -57.38316 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 88d64587-982b-3fe1-ae1e-adfb11bb4621 | -14.56711 | -53.58522 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 8af7bbff-574e-3d4b-a879-b007fd56f297 | -18.05392 | -42.23238 | 2026-08-31 16:48:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 4c96434d-f069-3091-9dbb-f20e71d3e4d5 | -19.22481 | -57.34718 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.0 |
| 684762ca-c1da-36ac-959b-2390c6afcbd9 | -15.88213 | -56.47962 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8081d30e-f066-3a7b-b03b-9d22ac7a7e68 | -17.86627 | -52.10418 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a6c15a19-56f8-36f9-aabc-ad99ab3f7b23 | -17.81628 | -50.64723 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1f1783c4-8a9a-3993-964d-298997067f21 | -14.59474 | -53.08785 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 2ec32da7-ed10-36dd-a93e-022db4338a79 | -14.96532 | -54.58394 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2b3e414e-de64-349e-8dce-c9870dcdeaaa | -17.86259 | -50.50252 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 255.2 |
| 83839993-c5f7-3e1e-8ea6-be2f4c23bfea | -16.00203 | -43.5549 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b6872191-fabe-3d08-b7d1-f8c9befe291c | -15.87174 | -56.48462 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 24a68683-9a56-3a14-9a4b-1dc6620ce4f7 | -16.55606 | -52.51409 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 6147b554-fdb6-37e4-bca9-165ff2fab7fb | -15.83005 | -42.00105 | 2026-08-31 16:48:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 5952178b-929c-39a7-935f-f7ec417db477 | -19.17813 | -57.36104 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |
| b0398a1e-f46d-3498-8d67-ea86a7615ae6 | -19.11478 | -57.39044 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 1e515b19-c082-3554-8521-3ddd2aad6e7b | -17.5334 | -41.31334 | 2026-08-31 16:48:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 100dee32-25bc-3e4b-9a1b-100263ac9ea7 | -19.16496 | -57.41283 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 13399c30-ea6b-3448-b4f5-bbcf2d629c5b | -19.1964 | -57.36375 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| e62f7447-7f04-3966-9b41-b52c86ed8f0f | -14.39419 | -52.96575 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ded72d29-1295-305d-8d90-f7e7b47951fd | -14.46294 | -53.16621 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 1487f38f-47ab-3e54-904b-7d358a5bd3ba | -16.75296 | -47.63322 | 2026-08-31 16:48:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| a22394e7-95a1-3ea1-a6ce-e97f37b14a58 | -18.20689 | -43.97761 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 764231e5-51f4-3211-b3a3-d294ac00434e | -19.09534 | -57.40891 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.8 |
| ce22e961-5bdc-31d5-8143-d36163ee0d19 | -14.59061 | -53.08909 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 87bb63bb-9e75-3161-9a29-f878f06fb93e | -15.74389 | -40.42354 | 2026-08-31 16:48:00 | NOAA-20 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| d6395def-aa69-343f-9108-1fe44af78da5 | -16.85995 | -48.27828 | 2026-08-31 16:48:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0efeb58c-f9b8-3ceb-ab7c-e73868250a58 | -13.95785 | -42.79504 | 2026-08-31 16:48:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 6d37e6dd-972e-3e06-b4a9-532edb6e65a6 | -19.21843 | -57.34327 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 824ff9df-dea2-3b5a-aa12-f935d816ac3f | -14.42276 | -43.14768 | 2026-08-31 16:48:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d656da65-3ef0-3cc7-aa4c-22d86d26d48d | -14.02862 | -47.80112 | 2026-08-31 16:48:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d7afde5-7d9c-3614-af56-183881b73c48 | -15.23102 | -56.36163 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| aa4f431e-3096-356e-a1c9-22b71b83c417 | -17.72372 | -46.85163 | 2026-08-31 16:48:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78c02c8b-2d44-3b47-b3e0-f4cea42e1095 | -15.37329 | -41.18427 | 2026-08-31 16:48:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 8eb8c5c3-bf9f-3c27-b94e-cb204ff84528 | -16.27944 | -42.58205 | 2026-08-31 16:48:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b561d34d-9964-3527-8107-aefb25fc9f95 | -14.82281 | -55.71912 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 106cd492-2ef6-3fcd-b50a-f61f431dd89b | -19.12139 | -57.42923 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 26a12ad8-8a1c-3032-99b1-2b2ba9747621 | -19.1293 | -57.38709 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| fc552b74-f96b-362a-af3b-ffe0ecff094f | -16.8943 | -40.22239 | 2026-08-31 16:48:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 92bed1ee-bc52-388a-bd72-f9e266b740f2 | -15.01271 | -52.75771 | 2026-08-31 16:48:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8dbd00c1-ea05-34b6-bb4b-6c228e26e2bc | -18.39982 | -49.30796 | 2026-08-31 16:48:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 91753e19-3fe0-3e11-b745-a97e59f265fa | -15.99442 | -48.05074 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8da4ea7b-38c8-3064-83f5-1d1069d574ab | -15.56187 | -56.27182 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb8b234c-6e78-3070-a78c-9462c4793a66 | -17.8739 | -50.50106 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 1423527f-3010-3087-9ea2-2e5006253eb7 | -15.9787 | -55.95807 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 2e5ad30d-07be-3520-b6ef-ee704a0eafb3 | -14.23248 | -43.82954 | 2026-08-31 16:48:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 5ab5dc77-b979-382f-8be7-77ecc0014e9d | -15.67192 | -45.91469 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 939c69ae-7fd9-3352-b72c-f3216609563b | -17.89215 | -52.10886 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fcda764b-5407-30af-83e0-11d9f332e9ab | -15.19819 | -46.22697 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9fd21d0c-1fd7-3295-a27b-6946a9aeb5f0 | -16.55049 | -52.51412 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 38.3 |
| e82ddd61-96cd-3cc8-99ac-ad8b99825369 | -19.21799 | -57.33876 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 147eefcf-fc7c-3e43-a7d0-1dbd5f0e435e | -16.02344 | -54.4037 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0ded7048-0530-363b-a2bb-a5d501949c54 | -19.16241 | -57.38556 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| ef3e85d8-2a7a-3968-b9de-032466b49b0a | -15.99979 | -43.54187 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 42.1 |


[Clique aqui para ver as próximas entradas](README140.md)
