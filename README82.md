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
| d1fe3e59-06fb-36cb-9a69-17609a5ef857 | -3.07191 | -50.95843 | 2024-11-24 05:37:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a5084a5-8834-3d52-89ac-e3c4e7c637a2 | -2.57449 | -51.88659 | 2024-11-24 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b3c4e01-d7af-306d-b480-012a3fc13f25 | -3.09796 | -53.7365 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80c961ad-9000-38ff-8ab3-0a91ffa2bbaa | -2.85731 | -53.96839 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f372910e-1a88-34bf-8587-ddac12b294fe | -1.48372 | -52.52394 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daedcf11-37e6-3d7f-8af4-870de9e17748 | -1.45314 | -53.39724 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f3a13ad-14c6-3992-bad7-71be26a09a0b | -1.22608 | -53.68488 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e685f887-26b5-3684-95a7-04767e3b317f | -1.52478 | -51.62956 | 2024-11-24 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 132589af-6328-3511-8386-5ff8fe725401 | -1.61091 | -54.41224 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08c71ca9-4dba-360d-9d54-8f2cb47e9356 | -3.12007 | -53.11105 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 539fcd4b-eef3-32cc-834d-7cab64c20823 | -1.75287 | -54.51982 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c71de5ba-9fc0-3d40-9990-922b936434a8 | -1.40471 | -54.47463 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 21d90db7-48af-33f4-88dd-3108e67d0ed2 | -1.51588 | -54.19453 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3766da4-3799-341c-92a6-4b7d61e5b1eb | -2.16196 | -53.77853 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 505f790a-e839-37aa-95aa-7506670a00da | -1.59603 | -52.58683 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0719a333-07d3-3631-9d50-0472e22ec101 | -1.11116 | -53.39404 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94d7e473-7cad-363c-a93d-ffafc90b5ce2 | -1.42768 | -53.38325 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06374b3b-3dc1-3394-b3b0-c0fe7dfff92d | -1.64239 | -53.87657 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8608064-d6e4-3fa2-9f6e-23592b944734 | -1.64299 | -53.87266 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b00c8b1f-b72b-3861-b5d5-a1ebf6df5570 | -1.12263 | -53.58489 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d80c8086-2234-3344-b2fd-894a9aab9751 | -3.10693 | -54.00738 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9a0ccd7-5df2-3b43-88e0-84f738328da8 | -1.51645 | -54.19088 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be84c1ac-5059-3400-a1b6-553a13ed8ffe | -1.11777 | -53.39045 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e97f27a5-46dc-3c03-9e4b-00bccd5dd0c8 | -1.40444 | -54.475 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 277d7721-e3ab-356c-9bc4-7f14db7b74be | -1.74733 | -54.51894 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c149dc7-8d76-3ab8-8ea3-f9b188975b95 | -2.62001 | -54.93541 | 2024-11-24 05:37:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8379052c-ece4-30b4-9dd0-0828a104ae38 | -3.20126 | -52.57833 | 2024-11-24 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dbca788-4930-3e76-a253-56e6fac6c1a5 | -2.17671 | -53.63853 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7f784ad-ed4d-36ba-9e90-6d5f01ef5f38 | -2.94549 | -51.43199 | 2024-11-24 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52a551f6-e7ad-3cd1-9be8-c80adb69e941 | -0.5743 | -51.7256 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e98d9050-c910-3ecb-abcf-755f5d614f85 | -2.62157 | -54.93274 | 2024-11-24 05:37:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 830bae99-c323-311b-946b-6703b4e9a165 | -2.94834 | -53.71686 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c3bfbef-345a-3d8f-9a98-90634537a6ef | -1.61035 | -54.416 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 496fb4ba-a7c5-357c-8dc0-e5c8bd69a39e | -1.61674 | -53.30472 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9660c7a4-d8b3-326f-8eda-e691bf56c8ad | 1.94468 | -60.85735 | 2024-11-24 05:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eaf57175-6f30-3f04-a916-c9849aa72681 | -3.05822 | -53.22803 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a4f15177-3696-3028-a86d-957438b3bc92 | -3.25135 | -53.27773 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fdd5cac9-550f-3a64-822d-6e82d3a84d26 | 0.40338 | -50.86179 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14e1c5a1-7695-34f6-a1ae-4ba87eb37912 | -1.61592 | -55.13484 | 2024-11-24 05:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2ef66b2-6ad1-3917-8a44-98944b8e1820 | -1.44654 | -53.40073 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 995ab66b-0e54-382f-8500-3ddccb13f8d4 | -2.9477 | -53.7212 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f306878-26e8-355e-bf16-b3eb0a616656 | -1.56733 | -52.00973 | 2024-11-24 05:37:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fd8c07d4-64d2-362c-ae10-ee0d4c8e3f70 | -1.60219 | -54.95129 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 410def44-aa54-3096-8a11-5a6ce2e21c9c | -1.61687 | -55.13818 | 2024-11-24 05:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61ff1aa2-a4f4-30d5-83bc-d4653c8ff427 | -1.60152 | -52.59269 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 930acf67-2dbc-3b07-b98c-9bb13c78d847 | -2.62548 | -54.93623 | 2024-11-24 05:37:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c68f76b-7cda-3a34-8b7d-5e928d5ee717 | -1.12269 | -53.58743 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2590464e-159e-36f7-adbe-a302a2660f58 | -1.40506 | -54.47085 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 699294d5-00ea-3cff-bc75-d94981771d58 | -2.20763 | -53.67414 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed8461bd-0672-305f-ad02-c8faa00953d6 | -1.12333 | -53.58341 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 57d7f594-fd94-30f1-9284-cd0a8681f391 | -3.25204 | -53.27311 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 849ef496-efb8-3b7f-8d83-b398866ae978 | -1.73685 | -52.72346 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 429a04e3-69ff-3467-bff9-6bfc73d839aa | -1.05063 | -51.74212 | 2024-11-24 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31e2340f-c0fd-3e34-afa1-9fea301bec09 | -1.11756 | -53.58213 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d1851ef-c31b-335b-a088-0d1b1e7f33d5 | -1.44589 | -53.40507 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39f6572e-01f2-3c0b-bee1-ec9d848b2b38 | -1.11047 | -53.39843 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48d282a0-78a7-39b4-b9b7-adca98c854aa | -1.12323 | -53.58091 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72d77161-d1aa-32d4-a865-e813b51c4059 | -3.12079 | -53.10634 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c044dec2-b619-356e-87be-9e46e3f4191c | 1.38297 | -55.91508 | 2024-11-24 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dd356c4a-2912-39c3-a50d-2ed92281ae33 | -3.20322 | -52.5762 | 2024-11-24 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4749ce4-4afe-33aa-9655-0b673a6ae76c | -2.85704 | -51.82513 | 2024-11-24 05:37:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a38261bc-e4a2-314e-b79a-de66d03047d1 | -0.87628 | -52.76983 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 155e3657-0009-3173-87d7-b13901de9d61 | -3.24521 | -53.27683 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| de4071ee-0eed-3638-9f49-b42d4c3b7313 | -1.44958 | -53.39885 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 69682b17-e1ba-34d7-9ff3-ff316b7ad767 | -2.58658 | -54.23148 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f95059ee-9c66-3952-a1bc-23e7b82fc193 | -1.44719 | -53.39639 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fdf8b8d7-7b14-378a-9b13-a523d73f702f | -2.80839 | -54.02197 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b0e930a-6d09-3498-95cb-8ea3f364734d | -1.21969 | -53.68777 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 67cdf3ac-82a7-3b42-b08b-d5d91b9c44ba | -3.12151 | -53.10165 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54e9f3de-d56b-3b4d-b639-c381f4e49b15 | -0.57343 | -51.73116 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7fb79e5-46ee-352b-b2ac-224687801561 | -3.25067 | -53.28234 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27a6101a-aab8-3388-a9c5-be400462d77e | -1.60584 | -54.41499 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dde88f61-8ada-3ce4-a8f4-a912fd70b697 | 0.41592 | -50.8536 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 196649a9-5e16-33c8-95a3-d0d550ee6079 | -0.27997 | -51.60852 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb218648-07c5-3fe1-8ea3-6bf6f45998f3 | -2.16596 | -53.79185 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7062095a-f3bd-3b35-b1cb-c083e2f86006 | -0.56778 | -51.72461 | 2024-11-24 05:37:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90e6d00a-3022-3f02-b8bd-9c97004b059a | 0.40915 | -50.85465 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16b09a3a-d193-304b-a0e4-8a27980450c1 | -1.60167 | -54.95469 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 141dcb74-03f9-3421-8198-6410e686943a | -0.817 | -52.829 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19e526ac-1d11-37f9-b7fc-62d5c41449ca | -1.7695 | -52.71837 | 2024-11-24 05:37:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 372444c0-81f2-3a7e-92a4-2f6439cfbb60 | 0.41691 | -50.85969 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb19a0e0-b25c-3052-95b3-83f48442ca9b | -2.84708 | -54.00232 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50932fad-d5fa-3622-af29-c8a84d848bca | -1.6114 | -54.41589 | 2024-11-24 05:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3f2fca3-3a64-3eaf-87b4-bfd5d110b7bf | -1.61543 | -55.13815 | 2024-11-24 05:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef103f43-15d7-3d20-8db4-a59e6de692f6 | 1.87112 | -55.92823 | 2024-11-24 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d4e9f9a-52b0-3a57-8645-8634f829f746 | 0.40715 | -50.85707 | 2024-11-24 05:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 980d7155-8c3e-38ff-9584-7b26b858602d | -1.72383 | -53.26069 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6acf097-b1bf-39c9-a0dc-37943e4c31a3 | -2.9523 | -51.43325 | 2024-11-24 05:37:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbb08867-c8ed-361b-bf5f-afc6dae78e75 | -3.09524 | -54.0055 | 2024-11-24 05:37:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c20b634-8e9b-3377-aac3-b4a020805893 | -0.81619 | -52.83428 | 2024-11-24 05:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dbfe9694-dbb4-3b7a-8bf7-028f0d6ad070 | -2.58717 | -54.22759 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c06a27e9-6ae6-3e45-8748-db957198038d | -1.5114 | -54.18613 | 2024-11-24 05:37:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9783e7d-c4a1-3058-91b2-b37b1fbf1121 | 1.87504 | -55.92233 | 2024-11-24 05:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7eedcdc-8218-37ef-9137-ef176f9d4a51 | -3.12004 | -53.10454 | 2024-11-24 05:37:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0daf6a61-3ef1-396a-93b7-9f3ac4eccce5 | -2.91237 | -54.28646 | 2024-11-24 05:37:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cba0d467-8527-3042-b042-56fb65dbb9ef | -3.00034 | -52.51055 | 2024-11-24 05:37:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71961523-b6eb-32ec-aef6-fad6c6642b1d | -2.27851 | -53.6297 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78381aa3-322a-312c-888b-7ae0a621dc40 | -1.04408 | -51.74109 | 2024-11-24 05:37:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d441b6b6-6754-3ea8-b674-2d1c535c4373 | -2.30134 | -53.87918 | 2024-11-24 05:37:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fefffbd7-1a10-3ce5-9b14-5f8af68355b7 | -3.56259 | -51.11437 | 2024-11-24 05:37:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README83.md)
