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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 376f89d4-2afe-30bf-aa93-9e5c0a69d47b | -12.78347 | -47.4823 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ef783e67-c51c-3163-9ea3-5ee44c847c93 | -12.35724 | -44.10633 | 2025-09-23 04:00:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 19a1bed6-d0e7-314b-8f22-af0d17b86b5d | -12.77091 | -47.49624 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9996a33d-c21a-33c4-8a74-b08fecc07c54 | -13.424 | -47.55381 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c679d9e-1361-3cce-ae21-bf713b5d865c | -14.99834 | -40.79538 | 2025-09-23 04:00:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 169cac8b-2279-3960-926e-164c0729266a | -12.35895 | -44.09652 | 2025-09-23 04:00:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23aac337-f3d5-3136-9509-5700a4b9de97 | -14.62862 | -42.52832 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a7245ad-d161-3b6b-a80a-f10ac3da7b9f | -13.51763 | -42.34977 | 2025-09-23 04:00:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 04a561c8-7de5-389e-ae71-31be424d5862 | -12.00052 | -47.74893 | 2025-09-23 04:00:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c0c7053-8d2f-3b52-b425-1e0420c1aaff | -12.76031 | -47.50294 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 426d33fd-b0f1-3186-a7a7-9291d6d32830 | -13.8566 | -42.45787 | 2025-09-23 04:00:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 59e69086-49b5-3f32-8e8b-eda25f76e4e6 | -13.56144 | -42.55993 | 2025-09-23 04:00:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c22e72a8-68b0-38be-926d-1ca826966126 | -12.76606 | -47.49862 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 4d4c5554-4136-35fc-8d23-0782dae53295 | -14.6245 | -42.53159 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3bae25eb-0163-3a3d-99b8-50512f788622 | -12.13334 | -44.28637 | 2025-09-23 04:00:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0ec6b36-c9d7-37e7-bfce-27236c39a4ca | -13.71984 | -42.43541 | 2025-09-23 04:00:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 548a432f-9b71-3e43-84ec-43d2792e3393 | -13.56005 | -42.22459 | 2025-09-23 04:00:00 | NPP-375D | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac2dc8a2-7e2f-3ec0-b314-ffbaec81a123 | -12.77755 | -47.48992 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 51669769-1069-3a63-b056-1100a84b510c | -15.59007 | -42.39585 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6018ef10-f9f3-3b4e-b160-cf02eaaeaacc | -14.64602 | -42.49391 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04ad9235-3a83-3f17-b885-ba9d10efb7e0 | -14.69049 | -42.50568 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 56acf8d6-d145-3873-8f1a-068ef5e54cca | -12.12855 | -44.29068 | 2025-09-23 04:00:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90b661c9-6ae7-386f-b382-3e131d088aaa | -15.58065 | -42.40997 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 51f6d7b3-e970-3ceb-b0f2-314e1bc801e6 | -15.48628 | -42.26432 | 2025-09-23 04:00:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6338b11-0cb7-380a-9dd2-8959f8196914 | -13.41446 | -47.55236 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a17adfca-d3e2-3514-864b-ecfd8e819861 | -12.13247 | -44.29138 | 2025-09-23 04:00:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e14c0281-86bd-3017-9da7-caa33c705bcb | -13.41544 | -47.54449 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a36c739-6f96-3b5f-9009-6800ab061eb6 | -13.42412 | -47.5505 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89389302-ef3d-3e3f-a8b4-d531cb01f7ca | -13.423 | -47.55897 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c98a6e3-c842-33a5-ae48-cf3d3efef01e | -13.41348 | -47.55742 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ad5c74e-73c1-3f3f-95d5-835d1e9df572 | -15.58536 | -42.40291 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 30b858ae-d643-368f-8db1-d3324407d472 | -14.38727 | -41.20838 | 2025-09-23 04:00:00 | NPP-375D | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 37410f1d-7c97-3cbc-b290-68f01502d2fb | -12.78328 | -47.48559 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dc7403b7-a311-370a-89ec-61e9471383d9 | -13.41454 | -47.54932 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27112b55-895c-3dd2-a5b9-4796c26af157 | -15.5935 | -42.39645 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8a7c45ff-ae97-397f-812f-95568197bd9b | -12.75934 | -47.50822 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b5d0009-01d1-3183-bb41-206289837934 | -12.77669 | -47.4919 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bc7352bd-d15f-3e06-890b-d26f3b5d4b18 | -15.59414 | -42.39261 | 2025-09-23 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8362d1cb-59c8-3cd1-a285-17e3355051a1 | -14.62515 | -42.52767 | 2025-09-23 04:00:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fdfb63d3-a3fc-345f-ac3c-15a1e3e0fa98 | -13.4203 | -47.54464 | 2025-09-23 04:00:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7544355-6da9-388f-b642-e7f9b7c785d5 | -12.42883 | -45.14404 | 2025-09-23 04:00:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6148d058-d0dc-379c-83ac-cde7fb722421 | -15.67339 | -41.31319 | 2025-09-23 04:00:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 12ead0bf-37c9-3383-96d3-ec23756297ef | -12.35339 | -44.10557 | 2025-09-23 04:00:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a90db1e-aa73-394f-9320-47153ef09712 | -12.7718 | -47.49426 | 2025-09-23 04:00:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 465a6764-e8d3-3707-9fa6-a9e991f33b9e | -19.87893 | -52.96526 | 2025-09-23 04:02:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 88914414-a4b7-3827-9024-51f9506c8061 | -18.92447 | -44.73811 | 2025-09-23 04:02:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f3f345c9-fbc4-328f-b280-59b0c986f349 | -19.87531 | -52.96655 | 2025-09-23 04:02:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96bab343-e4ef-3b0f-935d-00eeb3a30fd8 | -20.9999 | -50.00555 | 2025-09-23 04:02:00 | NPP-375D | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c18bf1d7-a2c7-3aee-9b43-5b53309ccb79 | -19.88211 | -52.96383 | 2025-09-23 04:02:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bd761083-bfc2-37f3-8b43-8bb71d2a0d5c | -24.20805 | -50.42043 | 2025-09-23 04:02:00 | NPP-375D | TELÊMACO BORBA | PARANÁ | Brasil | 4127106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| e287ff91-7b73-3ec8-9a67-bb8597974e6c | -19.88112 | -52.9683 | 2025-09-23 04:02:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 741e9385-5c9f-3cd4-8bdd-6730766ee4de | -6.3412 | -56.2009 | 2025-09-23 04:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 5815930a-bcee-3f4a-b32b-aa77fb1fda2c | -5.48301 | -42.25172 | 2025-09-23 04:17:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f39a282e-8434-313b-b8d6-f8295a60191d | -5.14283 | -42.88248 | 2025-09-23 04:17:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8f61f2e4-0db9-32eb-aa6a-1ee6af6ba726 | -4.4 | -50.6948 | 2025-09-23 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31764363-a3c1-309c-af0d-ccf33cd7f5eb | -6.66993 | -42.04183 | 2025-09-23 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eb80f6e4-1780-3c61-acdd-a15db1f820b9 | -3.81041 | -41.56358 | 2025-09-23 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a01909a0-caa1-31e3-857c-8dd94049afeb | -5.73917 | -42.60732 | 2025-09-23 04:17:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd8ef23e-a0ef-3ca9-914e-0a9917a5ba1f | -4.37964 | -43.28809 | 2025-09-23 04:17:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6fe66cb-74f8-3a83-91cc-75ad2443cd41 | -5.67993 | -46.36302 | 2025-09-23 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb2ae839-afda-3efd-ba38-abca0700d4eb | -4.6753 | -43.63348 | 2025-09-23 04:17:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 11a6de4a-0817-3385-ae74-11ad178936d8 | -5.7918 | -42.76593 | 2025-09-23 04:17:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b75c32f6-b336-3478-bb70-545da88d73c0 | -5.87362 | -47.21008 | 2025-09-23 04:17:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b87d842-3980-3341-9381-0cf8c24275ff | -3.646 | -48.32268 | 2025-09-23 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cb4a2321-5e58-3ecc-b4c4-4aa2055e1ef5 | -2.67827 | -52.18215 | 2025-09-23 04:17:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a2ff1a-61ee-3778-a30b-2bad7efda6b5 | -4.76602 | -43.22896 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b924bf8-fce5-3c88-a393-852b65755318 | -3.21643 | -49.17515 | 2025-09-23 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c985f219-a452-3cad-b3b7-0c62872f8a02 | -3.33319 | -46.54364 | 2025-09-23 04:17:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7b5c3acc-f1bc-3417-bdfa-fe36fdaab710 | -3.81102 | -41.5597 | 2025-09-23 04:17:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 663a4e48-e690-3575-9a84-5c78d4da9966 | -4.39962 | -44.37176 | 2025-09-23 04:17:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50c5427d-e36a-377a-ac65-4451db2a6e50 | -5.12554 | -40.74657 | 2025-09-23 04:17:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52e6d2ad-6329-36f6-afa7-0a1452f23740 | -6.35773 | -43.36222 | 2025-09-23 04:17:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c12a2367-08a3-3d43-a5c9-987c52cd1351 | -4.96841 | -48.01683 | 2025-09-23 04:17:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cb155f32-5070-35c3-a589-19a67f262178 | -5.56953 | -43.60503 | 2025-09-23 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3521648f-546c-3260-8059-feb09b6158a6 | -4.78034 | -47.25346 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fe308d07-efe7-35a6-834e-11e762447b8f | -5.94608 | -45.39547 | 2025-09-23 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c21bdc5-6f0b-33be-8c92-4a5746eb0026 | -2.78645 | -49.57775 | 2025-09-23 04:17:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 967c55e6-d5a5-3822-bffa-a5c090227f2d | -3.79135 | -48.63501 | 2025-09-23 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fe90acf-3517-3e63-9e77-ac54fc09c520 | -4.47876 | -43.82623 | 2025-09-23 04:17:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f51b239a-6110-3a7d-9ed6-84bc0fdbc695 | -4.10711 | -48.74389 | 2025-09-23 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42443197-6dd4-3cf5-a691-0fff4a6a67dd | -4.79856 | -47.2774 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c3f2bd3b-4642-3b50-8d8d-4a2361f75bcc | -5.97979 | -44.12926 | 2025-09-23 04:17:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 47532ed4-e78e-35fc-8d61-16db9170b961 | -7.01389 | -39.25626 | 2025-09-23 04:17:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 77d1506d-7683-3582-a22c-08f768e90e21 | -4.77715 | -43.22348 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3d1a41e-b392-39d9-8f1e-95049a86a2fa | -4.15475 | -48.60101 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5244dd89-b85f-3cd1-96d6-bb79eb915fbb | -3.63229 | -51.91008 | 2025-09-23 04:17:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e82d9a2-d62f-387c-acd9-46940d803937 | -6.55689 | -39.89509 | 2025-09-23 04:17:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f96c679b-bcf4-3678-8b63-9c13b93e934d | -2.24967 | -47.88091 | 2025-09-23 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3211203f-8712-3899-b589-8c78f87c6944 | -5.69346 | -44.43859 | 2025-09-23 04:17:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ebb5578-e69c-306e-8e01-d66546442e6e | -3.05896 | -46.31057 | 2025-09-23 04:17:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ea6a8a7-7e7b-34bd-b7f5-224ebe10ae9e | -4.49079 | -48.11766 | 2025-09-23 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f67ab094-94da-3050-876f-fddf53fd2f4c | -5.23609 | -43.69632 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 915d8ec1-3131-3b70-94cb-c83ff27b1039 | -2.49126 | -47.99739 | 2025-09-23 04:17:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd8759cc-d2d7-3788-b30a-93e7780b9a02 | -4.6637 | -47.49388 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5d55ecb-3a94-3f12-a0e6-6e51eeec0f95 | -4.96585 | -43.23121 | 2025-09-23 04:17:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f695c0e8-07fa-3776-962f-252ace10588e | -5.56135 | -45.3349 | 2025-09-23 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c1c47ce-f3e9-3f36-9b97-c9948bfbf331 | -4.0102 | -50.48898 | 2025-09-23 04:17:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 44618fe5-a40e-3665-92c9-cb6d02d812f5 | -4.96285 | -47.81797 | 2025-09-23 04:17:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0625d06e-eda8-3efd-b541-7b5b1620b177 | -4.78391 | -47.25411 | 2025-09-23 04:17:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d4acce09-26f1-3f3c-a17f-cf6ef44b7bce | -3.1982 | -54.9795 | 2025-09-23 04:17:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README12.md)
