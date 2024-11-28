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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01bdd630-51c4-3b8a-bd76-682ef394d462 | -1.5689 | -52.0177 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06fb9e0b-b7b2-315b-b5d6-61dcfce938c9 | -1.337 | -51.9492 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c09110af-6041-38bc-af01-ae6d98745db8 | -1.3944 | -55.0355 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468ad5c8-e67a-373f-8cfd-1d3158461356 | -1.2111 | -51.757198 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9208dc2e-62ea-378e-9e92-5af3884e842a | -1.5973 | -52.2342 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a020ea6-dba0-3dea-b1ae-6496aa32d0c0 | -5.2189 | -44.901299 | 2024-11-28 00:41:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc2a7741-c717-309c-8783-356ef9ba0572 | -0.9967 | -51.720501 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1bef153b-2ba4-3c06-8301-86454df83d68 | -1.5817 | -55.7766 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae3555bb-fc8d-31da-979b-1c775d971683 | -7.8332 | -48.187698 | 2024-11-28 00:41:00 | METOP-B | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c580319d-5551-3ccf-b91c-2c87cbda4e09 | -1.384 | -53.616501 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0692861e-ca08-39b1-beac-d589818096d1 | -1.5117 | -54.4576 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a041002-57fe-3f53-bfa1-556c235394d1 | -0.9819 | -51.700699 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 36b160c6-7871-3143-8609-85d2eca4d149 | -1.6368 | -55.701401 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf52e6b3-4ac3-3518-9159-58a6d7b76c55 | -1.648 | -52.457901 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6db1251a-1b8a-3e07-8731-efd09a49f7a1 | -1.5644 | -52.271099 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38afa80b-1dcd-3ba7-9b4c-44530a9adc93 | -1.3931 | -54.983601 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42247ea3-3d79-371d-b88e-d003696a57f5 | -1.1119 | -53.598301 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b977a3de-daaf-3ae1-a900-61e1fd6638dc | -1.096 | -54.030499 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 240aec52-16a2-3255-9a72-52bad056c725 | -1.1944 | -53.872799 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59959897-bd92-31ab-ba16-333a2276402f | -1.2043 | -53.870701 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b8f81e-c4bf-3392-9de3-6ed08f4d23cf | -1.0524 | -51.738899 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 2e38171b-d0fd-3371-a12c-5443f5b0cf84 | -1.3713 | -51.9641 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7aa8854-fe53-3f15-aa39-a1a07f4887d9 | -1.0999 | -53.6366 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32e9bbaa-f661-331a-b320-bd9103be790c | -1.3946 | -54.990601 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23d2cf8e-7ddd-346e-bf75-c20a0b597ef9 | -1.6665 | -52.722599 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0dd7311-a9ab-3051-b121-540098cca14a | -1.5907 | -52.250401 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1080fdd-d607-3096-a70b-73543da1fda2 | -1.5841 | -52.266701 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54ccba8-4ea1-35b9-9a67-12fd758e9fc2 | -1.0735 | -52.424301 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b40dbb2f-daad-3a23-b9c1-3cfd2704bc8c | 1.3005 | -60.395901 | 2024-11-28 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 59a8c49c-fb46-30e1-9c72-7828e34719e3 | -0.9686 | -51.641899 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2f3279-c81c-395a-8706-335c9702feb5 | -1.6593 | -52.4627 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a7d775d-eafd-3f31-a84c-41ba29deae19 | -2.1437 | -54.8405 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46c69956-7fa8-3592-b434-4ac92cd32e1f | -0.892 | -51.713001 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6045ef95-c5af-3322-a50d-a891c8ed6124 | -6.1588 | -42.6133 | 2024-11-28 00:41:00 | METOP-B | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ea9c960f-0f67-33a3-82d1-013a42439f3a | -1.4995 | -52.439701 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbbe0ce8-faa4-3bee-87df-b49c7af6faf2 | -1.1503 | -51.670898 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467fea19-1628-3e92-9fcc-2341147312c9 | -1.6376 | -52.002399 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d998f311-13e3-3114-9751-aeeab6047f8d | -5.6452 | -46.385601 | 2024-11-28 00:41:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4e09d7-390d-3abb-8ec0-42c35a8b6f5a | -0.2728 | -51.617199 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 804999d5-044a-3b63-bd81-f58155f97dd5 | -1.1646 | -53.558102 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4caa8bc1-567e-3e9b-98d6-82d9b5c178ee | -1.3697 | -51.957001 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e2411fc-830c-3650-bc37-d534114d8a57 | -0.5892 | -51.695202 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 491a7d54-09cc-32ea-a30c-6ae2fbc83cd0 | -1.5923 | -52.2575 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 556b32ca-40b9-3883-8250-75128d9c9149 | -1.7388 | -52.0396 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a4b2272-3142-3e50-8238-38f2e34ccf42 | -1.722 | -53.241699 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b35a45-afd1-3158-843b-a0d7645a5895 | -1.2307 | -51.798599 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30cec27c-fb83-3f4a-ad3a-dffdbb58a7f6 | -1.3599 | -51.959099 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ad15edd-6868-3a0a-838a-763f4f47d861 | -1.3422 | -51.4263 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf9cba6-aa34-3b4a-962d-fa3b3c063729 | -1.6265 | -52.271999 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8127bb5b-b1fe-3922-9dc2-1328b1266822 | -1.2058 | -53.877499 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fda27a5-722a-34eb-a715-5f6b1aa12558 | -0.4656 | -52.014301 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 329b45af-ac58-3163-b761-f3ada48622e6 | -1.6691 | -52.460499 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fdd5ab1-3c57-3bda-a155-99401428959a | -1.8183 | -53.577499 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02a18f29-2366-3782-863d-de39dee5865f | -1.5665 | -53.511902 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39db2454-a8b0-3ead-b0ff-e90b14047706 | -1.6821 | -52.472198 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 464d666c-91ed-3a27-98c4-dd39f1e2940c | -0.8838 | -51.7225 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 913b8987-966a-3baf-9267-7d0eaafcb421 | 1.9026 | -55.720402 | 2024-11-28 00:41:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4dc6c36-08a0-34de-9277-c1a7e021e365 | -0.9081 | -51.647598 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 988fa105-c0b5-3d21-b116-8fb6cc078acf | -1.1661 | -53.564899 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26f956b0-0605-38f8-8f83-6befc70adbde | -1.0771 | -53.169998 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20862fe6-ee60-3b24-940b-cac3359f2980 | -0.6023 | -51.707802 | 2024-11-28 00:41:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 97179c3f-985e-384c-b32c-aa4b1b204417 | -1.6144 | -55.372601 | 2024-11-28 00:41:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2b80852-fc34-37a7-8066-0d634b6546ac | -1.5963 | -53.826801 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b123af9-1e20-3de1-87f7-3bc4f562d402 | -0.9588 | -51.6441 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5d9c9bc-57c0-3db4-b9bf-3603eeb80f90 | -1.296 | -51.7229 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07c94270-11ea-31e5-9972-a253f624d8bd | -1.1959 | -53.879601 | 2024-11-28 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6e43922-4eb8-348c-89b7-cf97974ab9a0 | -1.6748 | -52.713501 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84ffe770-8908-3eb8-b158-f9f0a9dfa7a8 | -1.6824 | -52.428299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4fb09aa-e0fe-3db4-862e-9651a24d5cd1 | -1.2094 | -51.749901 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e3031a9-dfd8-3e37-b60b-0f95193490e2 | -1.3821 | -52.421902 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89515567-684f-3501-89b2-edc6ae8d3171 | -1.3719 | -54.9809 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2019e81e-b5c2-3575-ad6f-cf6a6e8a14db | -0.9507 | -51.653599 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ad6b75-29c4-3118-a2e4-0617714de882 | -1.3091 | -51.735298 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d18a6e74-34ea-3b83-aeb5-4291c759dfd1 | -1.3694 | -54.649502 | 2024-11-28 00:41:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39b9b9e4-0c85-3ba3-8fc1-f8865da97b6d | -1.0048 | -51.710999 | 2024-11-28 00:41:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6f591159-bd44-375a-a42b-f9630d991c16 | -1.7245 | -52.477402 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01b65d9d-ccee-39f8-aedf-82c99c7f9a67 | 1.2474 | -55.974602 | 2024-11-28 00:41:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7901c90-cfd3-391e-9ec5-d727851928fa | -5.5147 | -46.2691 | 2024-11-28 00:41:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1e44db26-71e3-360b-88eb-e6ef40891831 | -1.695 | -52.483898 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c80d316-3133-37fa-b60d-5216c796bac4 | -1.6795 | -52.7342 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901a4247-def4-3569-bb5d-13885c0b0613 | -1.6552 | -52.7178 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eadc789c-bebc-3623-bfa2-1eee8d07f64d | -1.1092 | -54.135101 | 2024-11-28 00:41:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e474fbe1-c052-3de3-bb87-10c7c9746521 | -2.2146 | -54.514198 | 2024-11-28 00:41:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7216ad-fd68-3ab0-8565-170f5e8a9aab | -8.1355 | -47.981201 | 2024-11-28 00:41:00 | METOP-B | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee7154b-5f3e-37d3-a4b9-159310ff0743 | -1.2892 | -52.1022 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c002bfc-c6e8-3f78-bccf-36498132b519 | -1.6934 | -52.477001 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4722ad3b-ccae-3a3f-842e-188a4592c912 | -1.6982 | -52.497799 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c3771a6-83c2-3d1e-b848-bc308d3fef8f | -1.4525 | -52.5961 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e9403d3-0b8d-3b12-97a8-8b8bf5204253 | -2.0121 | -55.905701 | 2024-11-28 00:41:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74653523-9bd3-37a5-b5a7-ea781157bdd9 | -1.3206 | -51.740501 | 2024-11-28 00:41:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11773067-7669-36c9-ace8-33f1a1ce9a22 | -1.3354 | -51.942001 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5422421-ed6b-3509-982f-710f30786598 | -1.3092 | -51.917702 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62480075-fb93-31a8-92a7-fe95a0837269 | -6.1061 | -43.984798 | 2024-11-28 00:41:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b4175288-9ca2-3ba9-8726-4c5fbf7009da | -7.8091 | -49.995201 | 2024-11-28 00:41:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99d002ae-a955-3202-b7e8-bab676d0d7bf | -1.6703 | -52.511299 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e044677b-397c-34da-a5e9-99c9a8aab4f1 | -1.6495 | -52.464802 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b74d61d-b1e2-32f0-8b71-5616c3e7dac7 | 0.981 | -50.1194 | 2024-11-28 00:41:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b2e37781-6efb-3bc1-8bf1-d0101cfe6856 | -1.665 | -52.715698 | 2024-11-28 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0274365-7459-3582-a1da-b8de5f0d59a3 | -1.1067 | -53.3923 | 2024-11-28 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cddf9093-f0dc-3505-b2af-c9d7e3f4986d | -6.3615 | -47.061298 | 2024-11-28 00:41:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
