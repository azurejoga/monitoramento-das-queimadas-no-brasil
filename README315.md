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

## Dados Diários - Página 315

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abd723dc-0917-344b-bba9-e383684ab2f4 | -9.97959 | -45.9679 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 85dd19d1-e3a9-3872-928e-49644288d60f | -7.16747 | -47.78378 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c657abbf-a699-3e0c-8421-d41c3052084b | -6.52684 | -43.5355 | 2026-10-08 16:37:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9690e516-55f2-3e77-a416-1df22c5cdebf | -6.31385 | -35.12954 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 33628c7a-fd81-3c96-b678-3a692b04c37e | -6.89883 | -38.52205 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 01b721e1-59e3-3e8a-a123-189381521966 | -8.2594 | -54.72776 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d3ce0b91-8f73-302b-a421-2949d3673e69 | -10.51354 | -47.31115 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0febb17d-baef-356d-8747-5d296e8f14e2 | -7.26184 | -45.3409 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 310c4edd-2134-32c2-855d-e332ed0b3ba5 | -8.28918 | -45.71274 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 4fb95af6-8141-3046-97c9-913b7f050ea2 | -11.34189 | -46.66292 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 84707bc3-44ed-3b4b-a566-c33dc42da428 | -6.8223 | -39.54337 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9757fc3e-dd16-3611-96c9-9f0400787744 | -10.49855 | -47.30556 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 92e25e42-d3d7-352d-8108-40753c2a4d83 | -10.46478 | -47.24342 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 12303a0f-bcc1-3398-817c-74a2b98d91a3 | -7.79196 | -44.5771 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 21e29828-458c-3061-9cbe-d555e1a99552 | -7.53604 | -42.08509 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 9cda3688-abe7-346c-b66a-f960e4782de7 | -5.72972 | -41.77913 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 402382bd-4ed1-324a-a43b-d9d9f26604c5 | -11.01464 | -45.43155 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8b34f714-12bd-3061-a1f0-27da8af2646b | -7.64072 | -44.3711 | 2026-10-08 16:37:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d1892097-53a3-3a31-b5a7-a263175daca9 | -13.29999 | -41.51037 | 2026-10-08 16:37:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 34dbb601-779b-3a40-861a-c0721063b74e | -11.77637 | -45.58209 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5e64d0f3-09f5-312c-8426-6e0cdc0abcfc | -11.09138 | -44.02872 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| ef98717b-e9e7-3c2f-83e1-cb9db35d4eff | -18.04031 | -40.53333 | 2026-10-08 16:37:00 | NOAA-20 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1178c981-e040-3339-8388-48602ace8636 | -8.39354 | -46.92421 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 04578dfd-2c6e-38a5-9a9a-1b5c1701e048 | -11.63832 | -43.7013 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 712b122e-4fd2-31f6-a3fd-670030a2e70d | -7.20935 | -45.08869 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0e4e046c-d168-3de3-bf7c-d601393c5375 | -9.88108 | -44.87188 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| a1913ea0-89ab-35f9-a8d6-ebb2d0c70add | -6.72354 | -45.17411 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 4bac26c2-f59a-387c-946a-770c9d281d77 | -6.72848 | -45.18406 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 13890420-1fd5-3229-9b83-7c234e58ba27 | -11.62941 | -43.71009 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 033d3807-8898-3c03-a071-0ec9881ffcdf | -11.83952 | -48.09901 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d4b01da6-52a8-3699-932b-b58c2e5c497a | -6.9679 | -43.44152 | 2026-10-08 16:37:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8cbf2e99-3550-38cf-bf1e-e5972a96cdb1 | -19.99676 | -49.08764 | 2026-10-08 16:37:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ca1c963f-914f-3a69-aaae-261f6575f248 | -6.69931 | -45.28131 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 590a0925-c1e5-31f3-96c1-e50b809b7a01 | -8.95556 | -45.16482 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 9cadb7a0-7d0c-31ac-8897-d7b999b0e660 | -7.28783 | -46.15665 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 226f4041-2ece-3d3c-8bda-55ceea822fd2 | -10.7467 | -48.54176 | 2026-10-08 16:37:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4b2852d6-fa44-33e6-8d0a-21a2009d7ab8 | -7.57985 | -46.69911 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 623e7e55-728a-3ce8-8457-523a61947ebc | -14.00834 | -48.7588 | 2026-10-08 16:37:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| f9b724c4-de8b-3f11-9db7-363667af5045 | -12.18266 | -44.65619 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d4dcfc0c-59fa-34bf-9d2e-4cbaeed2a035 | -7.05523 | -44.33245 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c606eea7-3f92-35ce-a6a5-b26bd4227ebd | -6.05885 | -42.91543 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 67870ae3-07c3-334e-9032-07e51a2e1114 | -6.59282 | -44.85329 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ed9dbb90-e667-3f92-aafe-e002528e9b76 | -18.13096 | -42.06137 | 2026-10-08 16:37:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| adee226b-533f-334e-8cd6-3f940bd44df7 | -10.51815 | -47.31842 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7e1ffda4-1f85-3f09-bd3a-096604c08682 | -5.98867 | -42.70789 | 2026-10-08 16:37:00 | NOAA-20 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 3e524649-a5a2-3f91-9294-c78e78275678 | -5.77619 | -42.06511 | 2026-10-08 16:37:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ca3f0c11-fa44-3ce8-8c6c-3923fe3ef997 | -8.97384 | -47.55766 | 2026-10-08 16:37:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 06ff95d6-2c93-3db6-9e82-1944c1a1ab30 | -5.09409 | -37.50101 | 2026-10-08 16:37:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 02854c1c-f040-3b40-9a30-e2d82c191820 | -7.04165 | -45.45398 | 2026-10-08 16:37:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 3c6bbe4c-fea0-3798-b1a8-db62b19cf2f2 | -12.84269 | -44.6238 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 0dcf3e71-963f-390e-b89e-30813cffe54d | -6.5382 | -45.40337 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 853e024b-37ca-334f-a4c9-c3290097c989 | -11.86987 | -47.40534 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8140430e-befa-3cc6-b7a3-4d257be26631 | -8.96729 | -45.13092 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c6d4c5ce-2551-3935-a557-f0f6713872d3 | -7.70253 | -45.44779 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| bf5ab9bb-b73d-3cac-86f5-e84aec2ec7df | -10.50745 | -50.83538 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ce1987e5-d2e3-3599-9cc4-f5b4cd0e7294 | -11.22315 | -41.57962 | 2026-10-08 16:37:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e3e73b70-5ce5-3e61-bbd6-abe3a6202982 | -9.03366 | -44.37236 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| e8b1c88d-1a92-335e-9533-89e5401021d5 | -8.07765 | -55.2938 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0c650ae2-068d-3267-a396-3c2208f2cb74 | -7.31776 | -43.99174 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 48a1770f-d8e2-387e-93ce-1098b3450cb3 | -19.10006 | -46.75238 | 2026-10-08 16:37:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 414e5db1-83f2-3ed2-98ae-4b179f2baf4e | -7.6013 | -48.11736 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 101b9c10-fca1-370f-b4bc-dd52131433f9 | -11.77071 | -47.74542 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 3af94c35-2986-3afd-9974-ddc93c210242 | -6.40981 | -37.79121 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 5cb96360-8b61-39b8-be7e-29dbc2bdd0f6 | -9.88278 | -44.86089 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| cbd085f6-9734-3b64-b0a3-cf9a19cc3ebb | -8.89178 | -45.39217 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 59021910-23a8-3530-9b5c-b9f8a9bc9775 | -6.96259 | -45.24967 | 2026-10-08 16:37:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 380d5825-3a79-3dcd-b90b-c8a660404ffa | -12.20675 | -57.1301 | 2026-10-08 16:37:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| c0bfb6f3-dd6e-3f8e-8dab-13337e590262 | -10.41479 | -47.27908 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 495cf1b7-ab22-3012-ba10-d8bba16b75ce | -6.97186 | -47.66819 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f77afe48-383a-34ea-be5f-2b96efadf49b | -6.12384 | -44.13259 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8d336cee-b2df-370d-b19f-0bb863d825da | -5.89072 | -43.34094 | 2026-10-08 16:37:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 656602ef-dbfb-3446-812c-303024f24e3b | -10.47274 | -47.85196 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 105ed444-4d26-310c-b299-30097265f20b | -11.24572 | -46.25068 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 2dbcdd63-cec5-3024-8f76-9d3a3746be8a | -6.34718 | -44.41534 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed72668f-c4c1-3172-9a5f-cea7c4c9ba2e | -6.68569 | -45.08318 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2b1b3940-c910-38bb-a158-8fe3534b3f0e | -6.85325 | -41.74831 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 96248f2c-0859-360a-a7b0-cdc8fd91ccb7 | -11.48539 | -47.59289 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c1d2507c-3822-3b9a-86b0-8e07813abb3c | -7.88022 | -54.98795 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| af7e88c4-6b11-3673-a341-264cb76cbfb3 | -7.8852 | -54.98381 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bb4cd764-1e4a-33c0-b304-5361bb250da9 | -8.60631 | -45.63352 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| dd5526d1-8e0e-331a-b37c-c2feccde80e6 | -9.35766 | -46.27601 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6404ac0-7a7d-37a4-bca9-00236c1f8084 | -11.23356 | -45.24198 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 438e9714-5564-330e-9459-750e2399902e | -8.20335 | -46.3339 | 2026-10-08 16:37:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3b4e4966-f8fd-3774-9578-113790731edc | -8.93887 | -45.1464 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 780019e7-eab7-31ec-a496-716fd8415e26 | -11.31074 | -46.69054 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| e01929f2-3050-3253-949b-e75306838bf5 | -8.31955 | -50.37526 | 2026-10-08 16:37:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 89d2820c-fbd0-3344-865f-5c0d38c9dec0 | -10.4706 | -47.23476 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| a9786562-c398-30dc-ace4-2b5671d1aec4 | -11.87694 | -47.40429 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c76380b1-7cd9-3c98-b494-d391a65c7f30 | -8.92936 | -45.1728 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 8afdf20b-8b0e-31ae-911b-46db51506f98 | -10.99049 | -45.40647 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.2 |
| ca9111ff-c728-3776-9f60-99fbde5ae688 | -10.87085 | -45.55875 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 36c2df21-0712-329d-abbf-360d00506bda | -8.30347 | -45.71766 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e32e3eb-4c1f-38b4-84dc-b903892ba9b6 | -11.6375 | -43.59394 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.8 |
| dc6b36b5-960f-33ea-b1f1-da1b5f41ea43 | -7.55518 | -40.04273 | 2026-10-08 16:37:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bc72e01f-f716-30e3-997b-eb97505049ff | -9.94003 | -43.57186 | 2026-10-08 16:37:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 857f41a7-9bb3-399a-a6aa-8a7f4b1df6db | -19.02341 | -44.34642 | 2026-10-08 16:37:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| adc72dde-cf7e-3f89-9c03-35392de00cce | -9.81691 | -45.67623 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a0700d73-ce27-3b9e-8992-26f15d11b12b | -9.07583 | -45.10915 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4f427f0e-5bf6-3b19-851f-29dd67261154 | -7.80353 | -45.5103 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce2313ce-91da-3f95-9943-7787c6be347d | -10.98943 | -45.39942 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |


[Clique aqui para ver as próximas entradas](README316.md)
