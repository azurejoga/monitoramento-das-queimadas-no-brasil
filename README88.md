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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c1d587c-4f29-368a-9fe3-042a1eb60ec5 | -9.53566 | -45.43051 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ff64c274-b669-3e52-b262-2a29b6fec2d5 | -3.66926 | -40.57244 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 85feddb9-ca6e-3302-9c8e-350d95500458 | -4.28962 | -39.23581 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 048f4c1c-ab1f-3420-af39-7d28f08e9fa0 | -7.11157 | -42.09903 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f629fcce-d91f-33ff-b6ca-8fa7ff3c810a | -4.0883 | -38.25537 | 2026-09-14 15:48:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 868f1314-a652-360e-a6c6-86b5ad1df3d7 | -7.55885 | -41.84464 | 2026-09-14 15:48:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b7e086c6-c3b2-39e6-9f43-505defdba78b | -6.92785 | -43.22586 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1bdcb5c3-f4e8-355e-a394-f4cf54f1a52f | -8.21191 | -43.78757 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0451291a-63cc-3a80-8b88-ab9895fda200 | -6.67267 | -41.66732 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7e5b35f2-1a89-3da7-bb9f-a7b8200de90c | -9.86301 | -45.96023 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 873f724f-7827-3b25-a7b4-992a673df28a | -6.29645 | -41.68432 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 19826e5b-ffb5-3ac6-bcbb-d10316a645a3 | -7.09894 | -41.80512 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f2b77510-2ccf-3b18-af60-ed13bb035d48 | -7.09542 | -41.81808 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 2c3dfaa4-c6c5-32d2-ab63-07ceb4bd3b88 | -5.41666 | -42.2249 | 2026-09-14 15:48:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dae06f2b-b9ce-3ff6-804e-449591953f75 | -9.5049 | -45.47992 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ee60a7a4-850d-368e-a78a-f4561eac8f1f | -9.49896 | -45.48762 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d1428acb-1190-3961-a9bf-4e6499b2b8e3 | -8.63146 | -44.443 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c88552be-2c83-3a8b-82c8-79c25bc269a8 | -6.31743 | -45.04698 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2d2e84d0-3f3d-3b01-a2ac-ec906035fb34 | -8.56429 | -44.49545 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b6c17901-c358-35e3-8837-74ab8f32f395 | -6.16432 | -45.19429 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e6fe48bb-b8b0-3d5a-9ab5-32409bcb4220 | -8.122 | -44.06813 | 2026-09-14 15:48:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecbc0d78-4ae2-3d4a-b23b-566bd42d99bf | -7.19096 | -46.13266 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 5b1094a2-42da-30e7-bd79-4c2558431045 | -9.33175 | -44.37135 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dbab19c2-fb1d-3a65-a6f5-3f9469eaddfe | -3.49445 | -40.68049 | 2026-09-14 15:48:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 75742f8a-337b-3672-815c-7e6858fe0a52 | -6.64675 | -41.78299 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c97ea08b-57ae-32ef-aeaf-815713c9222d | -6.24054 | -45.96281 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6181bfbc-a1cd-3236-8bd6-1e27bbdebedc | -3.88392 | -38.82254 | 2026-09-14 15:48:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| feb891ba-fe5c-33f6-be16-f476bf4afb46 | -7.08546 | -41.82249 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| b244eff1-b687-3b7e-a8bb-8180d00b2683 | -3.96734 | -43.11336 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| f4545951-22c4-3170-855d-7c65049b66c8 | -7.10674 | -42.09982 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| cb10cc33-f534-3732-947d-b497148f456d | -8.80443 | -45.89995 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 873746a6-2386-3e8d-82fa-5d39c4a7935b | -4.72151 | -42.27927 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| dc585174-0c54-3802-8050-d0b703caf3ee | -7.26445 | -39.28691 | 2026-09-14 15:48:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 178febe1-ca89-3c21-bad7-4f2e29f1cd78 | -5.93426 | -38.11233 | 2026-09-14 15:48:00 | NOAA-20 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 7fbd9a2d-3643-3aaf-8b2b-f93203b9922c | -5.11311 | -40.60861 | 2026-09-14 15:48:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 1fa69033-c12d-3937-849b-fc23247719a9 | -8.48994 | -44.56715 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bb550e10-604a-3dd9-af07-2c4a7605e843 | -7.09556 | -41.78004 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 45.7 |
| 6c1be1c6-652c-39d7-bc0b-22ff5324d3e9 | -6.5371 | -42.23862 | 2026-09-14 15:48:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| e4e2e3ed-82a5-344a-8be4-98f244f8d5f9 | -7.47192 | -42.11423 | 2026-09-14 15:48:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 5c0aef09-a9a4-3b9a-8bd3-e5923e53377b | -8.48712 | -44.87608 | 2026-09-14 15:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ddf62e6e-85e7-37c4-b633-89d583ae3e23 | -9.48055 | -45.47112 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c3adc99d-a8d0-3bb5-80f1-84debf8a5888 | -4.45834 | -39.35183 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 4c3a22e7-1e4a-3dc8-a14e-9cfd2f2c9127 | -7.97913 | -44.0261 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1a899048-4dab-32d1-8b8d-2868dc85d8bf | -6.65308 | -43.65878 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 70e7cdeb-f59c-3fd3-bc78-ef49e80e401d | -6.23535 | -45.97528 | 2026-09-14 15:48:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 67926c5b-116a-3e4d-9071-4ca14b6a02b3 | -6.52211 | -42.24715 | 2026-09-14 15:48:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b85b3a29-229e-33cd-afc2-d464cac5fe1c | -7.15254 | -42.12359 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| dbc4517f-6153-3296-960c-66210d1852e5 | -8.58464 | -44.45492 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 29f524dc-d1c2-3ce3-ac8d-9748712d5e48 | -8.92321 | -45.4491 | 2026-09-14 15:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8c6de7a9-0dbc-3d08-ab31-c8fba4dfda2d | -3.70883 | -41.71557 | 2026-09-14 15:48:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 7490f83b-5698-3b0e-a51b-850b01164dd8 | -7.43505 | -38.98193 | 2026-09-14 15:48:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 7dac892a-4e30-3d4b-ad6e-bd3db3741655 | -7.11407 | -41.80004 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 7cc7ea15-daca-35d3-87e9-3f0f934e9fea | -4.37695 | -39.23879 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ec0c2d24-06cb-32a3-bfc1-a4b0095c0fbe | -6.29815 | -41.68565 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 3b6c4307-c004-3d43-ae92-1acd8ced1f53 | -8.61895 | -44.44508 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| b811c1a7-4335-320c-8f39-c10d30d4a0c6 | -6.16359 | -45.18905 | 2026-09-14 15:48:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5634fc0a-fa85-3dcf-b038-8e4d38b713d9 | -7.02439 | -44.64243 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9323416c-d987-3a47-b7f5-27a88fdd2406 | -6.78941 | -42.89148 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 853351be-e651-34af-b13e-20b14cdf46d1 | -6.44188 | -39.34566 | 2026-09-14 15:48:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 19a4131e-745e-3497-83ca-0fb1898b9c88 | -7.1468 | -42.121 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 779f8b13-60cc-39b2-86d2-926241c13b47 | -3.96783 | -43.11679 | 2026-09-14 15:48:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 0b701def-2a63-3942-af9b-a423b723fa6c | -7.19019 | -46.12639 | 2026-09-14 15:48:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7823d1f2-4320-344c-89b2-082587c9fa33 | -9.88079 | -45.99118 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 830c013d-b2e7-3c03-88a5-2d7bd98a654d | -3.66699 | -40.57499 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 3fde150d-00d1-3654-a2df-bbf7e7bd45cd | -8.58819 | -44.45437 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cdd62980-6656-3388-8b31-51698808e548 | -6.26742 | -41.95044 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9e87d745-fa75-38e5-8d79-f3e574bb6ac0 | -8.49058 | -44.57238 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ca660575-b188-3488-b3eb-48d82a982133 | -6.7194 | -41.77863 | 2026-09-14 15:48:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 53f142da-203f-3c3e-8fae-ccc37ddeadfd | -3.49267 | -39.36073 | 2026-09-14 15:48:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 9aea9981-d019-3d19-ab56-f24333af9876 | -8.49311 | -44.56791 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 148c862b-2c2f-3a6e-8674-bc2131a8b180 | -9.74067 | -45.26475 | 2026-09-14 15:48:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ee2c61d7-dc4f-329d-92c7-b3e205e4ba17 | -6.29308 | -41.68641 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 339156cf-2ee4-33f3-b607-72e11e2e4ef0 | -5.84851 | -40.58393 | 2026-09-14 15:48:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 29493fd2-4946-3ddc-a238-527fa13b8d8f | -9.94054 | -45.78211 | 2026-09-14 15:48:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7d0464eb-5940-3f38-9f2e-c6258efa1acb | -6.53519 | -44.08744 | 2026-09-14 15:48:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 904fd2d8-fe7f-3db2-9a46-094f68374c3f | -6.34583 | -44.10186 | 2026-09-14 15:48:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d8eccd3a-16a8-36c6-9bf4-640cb2018766 | -7.16576 | -42.10184 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9893b49a-4f51-3ba6-ab1f-81ba7fe1ecbe | -3.78498 | -40.77917 | 2026-09-14 15:48:00 | NOAA-20 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 2b55e5c8-2a8a-30ab-b300-7bb2c1bace62 | -6.78868 | -42.88861 | 2026-09-14 15:48:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 5b546bae-f3c3-3e66-a26b-2764a89f3dcf | -8.17754 | -43.10933 | 2026-09-14 15:48:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 4e9754ae-f1ad-353a-aa6b-75ced3381bb1 | -3.51383 | -39.41904 | 2026-09-14 15:48:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c8bd6e6e-bb39-327f-9e27-c3d48dbec7dd | -9.873 | -45.98516 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 4172ed12-a733-392e-abd8-f85ce01e8848 | -6.9359 | -43.8758 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| be92bd33-6087-3da8-adae-90ba8ccd4d13 | -7.09977 | -41.81127 | 2026-09-14 15:48:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| b8b64b98-d115-3ab4-9992-4cb34194f242 | -7.01685 | -44.63354 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 655e1e71-8907-3817-9d8f-f880d3848ec3 | -7.06349 | -41.54263 | 2026-09-14 15:48:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 98a250e7-1981-3734-9465-3759b8fd6ea4 | -4.72195 | -42.28236 | 2026-09-14 15:48:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bd1e3bee-9f40-3f47-a691-8fdefce8fdb7 | -6.1175 | -44.68531 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 72d8994e-2714-3c89-9ab2-8669dceff23c | -3.72628 | -38.80363 | 2026-09-14 15:48:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b15e9d0a-7388-3cb0-86d2-abc617f320c5 | -7.16002 | -42.0992 | 2026-09-14 15:48:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 59dbfd56-2b8f-344b-ba39-4cb89c7ec075 | -9.6207 | -40.98362 | 2026-09-14 15:48:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d31be32-2827-347e-b949-35bf9cfa1635 | -3.42557 | -39.61477 | 2026-09-14 15:48:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 3be442c6-5b5d-39f3-8578-9f72d29811a7 | -8.41996 | -44.7554 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7cafc7e1-563f-35e9-b1c5-d8defd2ce854 | -7.34063 | -45.31912 | 2026-09-14 15:48:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9432bd07-e5a7-3dde-b7e1-4d1d9c9232f9 | -3.97341 | -42.48042 | 2026-09-14 15:48:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bd422761-53fd-3364-8705-74186f103ca7 | -4.45458 | -39.35985 | 2026-09-14 15:48:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 5bd51dd5-15e6-33e9-8a51-d4a6243228f9 | -9.73794 | -45.26931 | 2026-09-14 15:48:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 090f5afb-ecba-308f-9024-c7b6cbd67338 | -6.70122 | -43.14725 | 2026-09-14 15:48:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5fea546f-55b9-39b3-bc23-98112b9c64cc | -7.48387 | -42.12261 | 2026-09-14 15:48:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 5411df9b-c298-3c1a-bd6a-61a26d87c1aa | -8.796 | -45.88794 | 2026-09-14 15:48:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README89.md)
