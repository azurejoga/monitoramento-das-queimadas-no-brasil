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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2bc36eb-6dfa-3c1c-8c9b-3746c2d5a4b4 | -8.53753 | -35.74792 | 2025-01-07 03:34:00 | NOAA-20 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ec8e2e8f-60bb-32d8-b6a3-b62a08a25d40 | -8.07187 | -35.12506 | 2025-01-07 03:34:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6b8f6ccd-f633-36bc-a5c1-086d05f97947 | -8.06851 | -35.12451 | 2025-01-07 03:34:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a37939a5-e62e-3d7f-8761-4de7fb558ac0 | -9.78453 | -41.76944 | 2025-01-07 03:34:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| baa80782-dc77-345f-a50e-d3c742420a4a | -8.0713 | -35.12863 | 2025-01-07 03:34:00 | NOAA-20 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b2bab4f0-009a-3a92-8c9b-4656e79b355d | -3.72791 | -39.95648 | 2025-01-07 03:34:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 47712524-fac8-3779-81a8-6157b5e66c18 | -5.88149 | -35.3848 | 2025-01-07 03:34:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d5f49fc4-895b-3578-bf7b-42266d5a9c1f | -8.34274 | -40.41693 | 2025-01-07 03:34:00 | NOAA-20 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e95e7f9-e995-38dc-93ab-8c0a9f8949fe | -9.55897 | -38.28699 | 2025-01-07 03:34:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e60705b4-2724-30ac-a522-78af3f7bf552 | -7.56007 | -35.30475 | 2025-01-07 03:34:00 | NOAA-20 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 83fe1cc0-767b-3cdd-8a45-95232475b5a8 | -9.86634 | -37.10077 | 2025-01-07 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b7afad7-9706-360d-8fc0-e4ceafd09921 | -8.38956 | -35.02625 | 2025-01-07 03:34:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5a72726f-cce2-311a-8d55-0653d1dc84c9 | -7.82426 | -35.22834 | 2025-01-07 03:34:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 86f9acf5-29ef-362e-9c71-ea871bad6308 | -7.57346 | -35.19974 | 2025-01-07 03:34:00 | NOAA-20 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30d924fd-964f-3589-a180-db682c969054 | -9.43657 | -35.65422 | 2025-01-07 03:34:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c012dd11-cf56-3803-87f9-7e2cfce7d22f | -10.2191 | -36.38573 | 2025-01-07 03:34:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cdca3543-d675-3140-8a04-c9e0c7aba692 | -6.00866 | -39.2502 | 2025-01-07 03:34:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 341ed935-cd0e-33b2-971f-f507da4d269e | -10.18314 | -36.28359 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f714dae3-0ac7-37f7-9b16-33aa0738ca1b | -9.56275 | -38.28756 | 2025-01-07 03:34:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1dbbfacf-ccc4-3d29-bbb5-791663410349 | -10.05915 | -36.33282 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 171fbfa0-c891-34b4-9e18-a5b21c32f4a2 | -10.08392 | -36.16097 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8f7e8460-5c6d-30d5-9c48-cd48c3093875 | -7.68199 | -35.26495 | 2025-01-07 03:34:00 | NOAA-20 | BUENOS AIRES | PERNAMBUCO | Brasil | 2602704 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cd926855-8f51-3b01-8201-37a5fcc422cf | -10.5368 | -36.88435 | 2025-01-07 03:34:00 | NOAA-20 | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 7d37edc8-da16-3b6c-9e16-038b95ebdfe6 | -10.08793 | -36.15784 | 2025-01-07 03:34:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a57da96d-f694-327b-85ef-0e3958588237 | -9.86281 | -37.10014 | 2025-01-07 03:34:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 32e15eb5-ac05-37e2-b82f-20a0ab7f140d | -5.87807 | -35.38426 | 2025-01-07 03:34:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 428f1fc7-5489-3264-8cbc-4286b1355582 | -9.49983 | -35.58313 | 2025-01-07 03:34:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 92be5d73-2c4a-3e2a-82b9-876712ff7d9c | -9.78123 | -41.76928 | 2025-01-07 03:34:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8b4ca61e-8d57-39f7-b1d7-c03d71590166 | -8.00382 | -35.22781 | 2025-01-07 03:34:00 | NOAA-20 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 95267f1f-0fb6-3ad1-99f3-7871e6685b99 | -9.56353 | -38.28291 | 2025-01-07 03:34:00 | NOAA-20 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 977412f4-4e11-386d-a1e7-ea1003f36d5b | -6.61241 | -35.22117 | 2025-01-07 03:34:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a657d3e5-513b-3bff-8066-cb9081f11f45 | -14.34632 | -42.95621 | 2025-01-07 03:36:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 83ef6a32-557e-3a5b-9a10-2773f2468c57 | -11.95836 | -41.34624 | 2025-01-07 03:36:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0da7c16-8bfd-3fb2-bc93-32551493d088 | -11.8087 | -38.46478 | 2025-01-07 03:36:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dfd0d81d-d5d9-30eb-b148-502a0157c56f | -11.94506 | -38.39125 | 2025-01-07 03:36:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ce220aac-d7b3-3d4f-96e1-5d4254841211 | -13.6077 | -39.16209 | 2025-01-07 03:36:00 | NOAA-20 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fa7a98f5-25b7-355e-9edd-a187a326d2b5 | -11.80502 | -38.46408 | 2025-01-07 03:36:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc644a15-f797-382a-a6ed-70d361a0c381 | -13.60512 | -39.15971 | 2025-01-07 03:36:00 | NOAA-20 | TAPEROÁ | BAHIA | Brasil | 2931202 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 295fe29a-75ac-33e0-bd58-63773024e7b1 | -12.46759 | -38.34107 | 2025-01-07 03:36:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2f420425-83e4-3f17-93d3-7b53631adc01 | -23.40505 | -46.55667 | 2025-01-07 03:38:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 111023b8-9ec2-3a37-9f88-317bfd616c2a | -22.54818 | -47.31334 | 2025-01-07 03:38:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4c5b145-6888-3178-8693-bb088fe7e411 | -22.78665 | -43.75887 | 2025-01-07 03:38:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c1bcf244-d4dc-3f85-bf88-852044d86540 | -23.33755 | -46.77406 | 2025-01-07 03:38:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad7519d1-e84a-3cbb-bf02-8d340769629c | -22.5474 | -47.31687 | 2025-01-07 03:38:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c511028-75b8-385e-8fae-d7c3e8432385 | -22.53664 | -48.81691 | 2025-01-07 03:38:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 267c9358-4dfd-3d60-ad8f-ab210993c0a6 | -10.087 | -36.1511 | 2025-01-07 03:40:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| bac604d3-f902-3a6c-8f8a-c39d3fb2374d | -24.07715 | -51.02257 | 2025-01-07 03:40:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0dccf738-0bb3-34f3-bee8-ee7fb78c53aa | -3.12756 | -40.99504 | 2025-01-07 04:25:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ff0457f-e1c5-34a2-9494-cdf8b71debd4 | -6.40354 | -35.14385 | 2025-01-07 04:25:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 37309aa9-b924-3d81-9414-f1cba68c9629 | -6.86016 | -35.14497 | 2025-01-07 04:25:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2b5faa06-6756-3a37-a5e4-0cec46feae73 | -6.40291 | -35.14857 | 2025-01-07 04:25:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 4396c968-84ba-3fbc-ad60-5febb302d21b | -6.86626 | -35.14619 | 2025-01-07 04:25:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| fcc3826c-6577-30c5-ad13-221a512e58ee | -7.95111 | -35.25988 | 2025-01-07 04:25:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1a4c7eb4-1f12-3e8f-a7f2-081961e0b477 | -3.13149 | -40.99564 | 2025-01-07 04:25:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 890101d3-bd13-3f0b-b139-dab5a9c74243 | -6.3968 | -35.14768 | 2025-01-07 04:25:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 11bce50c-9f5c-32f6-9e3a-e9a8d9a7d17f | -3.73103 | -39.9591 | 2025-01-07 04:25:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb2f20a8-d4bc-30de-a5e7-903a48db2151 | -6.39743 | -35.14295 | 2025-01-07 04:25:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 63314dfa-9446-3814-ad70-f98c6c814fa7 | -10.20044 | -36.41523 | 2025-01-07 04:27:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a67d82ae-c5f7-3e3f-93a2-db47d6d94cb7 | -9.56198 | -38.28788 | 2025-01-07 04:27:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e25f6221-369e-3145-ade7-19afaf4cc80f | -9.56754 | -38.28579 | 2025-01-07 04:27:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b506a93c-f519-374f-944c-56cdc4a0f3f7 | -13.75895 | -39.96842 | 2025-01-07 04:27:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 1f86aec7-ad50-3e89-8ab4-efaabb72a4d4 | -12.36122 | -52.48967 | 2025-01-07 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b7b026-9d68-3565-9a61-bdf2afcb46af | -12.3573 | -52.48897 | 2025-01-07 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2acb3ecf-f432-3bd5-991f-0476e1a365ad | -13.76102 | -39.96916 | 2025-01-07 04:27:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| eee7ea2d-f69f-3677-a7c1-a97dde27e230 | -8.34731 | -40.41521 | 2025-01-07 04:27:00 | NOAA-21 | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e8c9defa-bb2d-3ac2-8e16-9ed693ee2c14 | -8.53318 | -35.73974 | 2025-01-07 04:27:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9157c822-e720-377c-9a13-9b4b0359dca5 | -12.35338 | -52.48827 | 2025-01-07 04:27:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dd04e37-ca67-3928-9728-d57fe57d9904 | -8.53455 | -35.74105 | 2025-01-07 04:27:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 77015a83-9dce-33f6-8395-82da3a7b17fe | -10.19451 | -36.41448 | 2025-01-07 04:27:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| afde1092-05ab-34b7-b4ed-55340d75d3a7 | -9.56239 | -38.28479 | 2025-01-07 04:27:00 | NOAA-21 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 54232064-b857-3383-917d-4fd21f0d56ab | -8.5391 | -35.74156 | 2025-01-07 04:27:00 | NOAA-21 | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0ecd7915-21a1-36da-afd0-5ebb060a1a33 | -12.46733 | -38.34374 | 2025-01-07 04:27:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 40757d9a-6f62-3b74-b112-641434bfebde | -12.46776 | -38.3401 | 2025-01-07 04:27:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57477920-71dd-3f8e-b226-68cbe76137bd | -13.76387 | -39.96899 | 2025-01-07 04:27:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a3dea5a1-7a70-36f4-8f7c-a87b23644358 | -9.28229 | -56.89243 | 2025-01-07 04:27:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a447046-1908-3959-bbbc-3a6aa3db6d37 | -17.42167 | -45.96523 | 2025-01-07 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da856547-4505-3e6e-b8e4-2174afeac600 | -20.41724 | -43.5523 | 2025-01-07 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a030f5b8-19b7-3e26-9559-4451c5291fdf | -19.5825 | -49.37522 | 2025-01-07 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6cedb028-f8e4-3ddd-b5d9-11d7225773ab | -20.19046 | -47.37954 | 2025-01-07 04:29:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b8a96a1-ee9c-3a6c-9f8b-2827bda6e4be | -19.3378 | -54.16886 | 2025-01-07 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fd1f5b1c-62f9-3271-b4d3-ecc686568800 | -17.46139 | -47.8676 | 2025-01-07 04:29:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1968e958-6a80-3283-9ccc-20c2686188c4 | -19.33417 | -54.17021 | 2025-01-07 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 519397c2-349e-3e05-9fb9-bbfc01b3780d | -19.33389 | -54.16819 | 2025-01-07 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c42f1a5-a525-338c-9c91-4e6c5d2b0f5f | -19.93933 | -50.55783 | 2025-01-07 04:29:00 | NOAA-21 | POPULINA | SÃO PAULO | Brasil | 3540408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d9e9cf3e-eed5-3b5a-b82c-3b298c60499b | -19.33807 | -54.17087 | 2025-01-07 04:29:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f2ca855-c112-30d8-8ad2-a0601bb5c36e | -19.58638 | -49.37215 | 2025-01-07 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6fd0abc5-0f51-3fa0-877a-c16f9b24f452 | -19.58307 | -49.37157 | 2025-01-07 04:29:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 480b654c-01ed-38ae-8584-59769502a77f | -20.11919 | -47.50908 | 2025-01-07 04:29:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5f9f499-0eca-315a-8d4b-b1442895492e | -20.91395 | -47.15152 | 2025-01-07 04:31:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bf47e72-a1f1-3881-b85a-ba71e11ecd1c | -23.58167 | -51.44885 | 2025-01-07 04:31:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4311aba9-908d-3479-9f9e-3ce3921c7635 | -23.29758 | -53.24026 | 2025-01-07 04:31:00 | NOAA-21 | DOURADINA | PARANÁ | Brasil | 4107256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e666c2ea-fd67-3915-b547-cfef6636ec5d | -24.24328 | -50.73846 | 2025-01-07 04:31:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 606ea8fc-7c71-3eb9-bf46-c3746d45f632 | -21.55986 | -54.19487 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f63c182d-2fa5-3a38-a378-76eaf5e7ae85 | -23.30109 | -53.24099 | 2025-01-07 04:31:00 | NOAA-21 | DOURADINA | PARANÁ | Brasil | 4107256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95a191aa-27ba-3ffc-9a09-56feb442acb4 | -21.55807 | -54.20466 | 2025-01-07 04:31:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 78d1fdd3-6b02-3a3d-b0d6-8290b2545086 | -24.58808 | -52.82306 | 2025-01-07 04:31:00 | NOAA-21 | CAMPINA DA LAGOA | PARANÁ | Brasil | 4103909 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9aff0c9e-de29-3c1f-9fca-7537f0ab908b | -21.10328 | -51.20869 | 2025-01-07 04:31:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1d05f81b-0eec-3cba-b7df-246a37232a30 | -23.52172 | -46.97403 | 2025-01-07 04:31:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6f283496-bb9f-3b2c-aede-8a19af494ad6 | -21.87945 | -56.11303 | 2025-01-07 04:31:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2278b49a-d0b7-306f-9fa5-0ec24c7c10b5 | -21.10391 | -51.20488 | 2025-01-07 04:31:00 | NOAA-21 | MIRANDÓPOLIS | SÃO PAULO | Brasil | 3530102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README3.md)
