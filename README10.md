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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83bd36d8-74b0-37cf-8606-8a4f485db7ca | -3.84966 | -40.35286 | 2025-09-17 03:42:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e487082f-f188-3ec4-a4a0-1947e307be3b | -7.57528 | -44.56599 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71a92a08-dd3e-3c29-b213-d26de7e0f764 | -7.06702 | -44.35194 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c65f63dc-9de3-319b-b365-90933a1c41d4 | -6.86734 | -38.43794 | 2025-09-17 03:42:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 9b906b57-68a5-3b18-a20b-a7b9f464e708 | -3.48994 | -39.59095 | 2025-09-17 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 16e815b8-fceb-3902-ab1e-2aa4c7ed99ad | -6.6846 | -46.30985 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 211301ce-9d06-3235-bb35-dd50952a5314 | -5.67435 | -43.50769 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7fdb84cd-43b7-3912-9a60-b7952e2cbc6d | -6.30036 | -42.40053 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f73a878b-c417-3ce7-b140-81791b17bdd3 | -6.97863 | -44.45477 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1edcac8b-d47b-3954-8209-91fba0626f3b | -7.58289 | -44.58397 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c8defd12-a3a7-396b-a084-9b77c8eaeba4 | -6.2274 | -42.02235 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b424a83d-d802-3df5-9340-508e645cd75d | -6.28582 | -42.37991 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c5801bd6-62f2-3de4-816b-5a7d6bd92078 | -5.79032 | -43.4939 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ea0bf0d-f037-34fd-b0f3-916802484957 | -3.03253 | -43.2461 | 2025-09-17 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 82061016-d5bb-3ae3-8a7a-0802cb48b00b | -5.79585 | -43.49186 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 698c5bad-4885-3bbc-a4a3-3b5d639ecf27 | -6.22432 | -39.24773 | 2025-09-17 03:42:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1623dbf0-976c-3d6c-a9dd-87489a6664b2 | -6.87289 | -45.18693 | 2025-09-17 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8129c4d5-d9fe-38bc-a3f6-b17abc81b42d | -6.87798 | -43.97203 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b58c5fa0-ef67-3e95-a3fb-5e206495c765 | -5.81348 | -46.3597 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a0d2983-1dd5-3a47-8716-1b4783e0050c | -5.77251 | -45.9066 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 37c81ac7-d8cd-38b4-b845-baae8a6433aa | -7.2686 | -46.58001 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 390be3b9-9709-3e9f-96a4-b35f1d6d482f | -6.21532 | -43.90148 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8cfaad81-4d07-30dd-87b0-80ce823bddc1 | -6.97549 | -44.44177 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7b05edb-eafe-3cda-bc75-15dbf8bbf459 | -3.23663 | -46.79421 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 370db7e1-b6d6-3222-bddd-e2e72d5184fe | -5.194 | -35.86653 | 2025-09-17 03:42:00 | NOAA-21 | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1709b294-e96d-3b18-b5a7-84fb4d67eb29 | -6.41383 | -42.6509 | 2025-09-17 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d7ddb2f5-b093-3150-86cb-f57c51aa2cb4 | -7.11978 | -35.15152 | 2025-09-17 03:42:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f5f46b43-52fe-3194-b4df-72a40a26ad1f | -6.74096 | -46.99591 | 2025-09-17 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b18755a-b778-3e19-a2b0-e1828faaaf07 | -5.82015 | -46.36368 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c84cce70-cedd-3561-bfc1-9b93aec5ab7c | -7.31024 | -43.96578 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9df08cd3-ae11-3373-99ad-475605969b93 | -7.58174 | -44.59044 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| ca0e8390-9da6-3e8b-bb89-56190ad213aa | -6.8807 | -43.97386 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59cda724-09b9-3d20-b5c2-aeefb6d52210 | -7.52804 | -44.73828 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea9625f6-8ffa-367d-a764-aecae08d2855 | -7.65543 | -44.47787 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29595510-d924-3b13-81c2-0795b3163b6a | -6.21374 | -43.9107 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55381711-ccf7-3cf7-ac67-7aed5990a389 | -2.92442 | -48.30413 | 2025-09-17 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8854f9d1-5544-3a03-98d6-d3d44674bc02 | -6.21834 | -43.9147 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd08ea7f-9c7d-3945-98d1-91819d247a87 | -6.41296 | -42.65598 | 2025-09-17 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 69e0e42e-79cf-3b23-ad03-7459591ff8d9 | -3.603 | -38.95318 | 2025-09-17 03:42:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 5334bd8a-32e5-30d9-a05d-2920a8aaa7c8 | -2.91731 | -48.30297 | 2025-09-17 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7b4eb886-42fd-3561-9385-19272cfb16a2 | -6.87212 | -43.96311 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 36d60f77-3ecc-3056-a0c6-5a7948e560b5 | -6.87849 | -43.96905 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a529381-6c1c-35c0-85ca-c8809fab4643 | -6.67537 | -46.31009 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 19d4c524-b279-3ada-aaec-1b8878890912 | -6.87774 | -43.96107 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 510549fc-00d2-3929-b5ea-c3c080b2028a | -7.3172 | -43.98512 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e31c3945-357f-31c3-9665-1e5fb3b63b06 | -5.6415 | -37.48615 | 2025-09-17 03:42:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 72c0ce8f-9bd5-38d8-a9c9-3162dfe9bd1d | -7.13818 | -46.09005 | 2025-09-17 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ab5489de-9edc-31dc-b3c8-65cb845f9274 | -5.77119 | -45.90466 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0aa9d9b9-f99c-3d97-b68c-e901f25af6b5 | -4.39103 | -38.69129 | 2025-09-17 03:42:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a231bc5d-ff79-323e-8a52-742eabf7b926 | -6.40027 | -43.33349 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 618c0ba0-00eb-3115-8f7d-aa4cf955e574 | -6.21267 | -43.91695 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d9f8aa-2a59-32ac-ad4b-fc4474dc6919 | -6.22056 | -39.24709 | 2025-09-17 03:42:00 | NOAA-21 | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d7ee2123-dc49-37be-a478-36fb41571369 | -6.86273 | -43.96914 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92b98066-8e55-364a-8a94-88ec38bf97b9 | -7.06357 | -44.34111 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63c8aab5-7d73-3101-860c-5662bf9941e7 | -6.04385 | -43.13768 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 431e67ba-6d81-34c7-8697-e78ba0506410 | -7.83064 | -43.8544 | 2025-09-17 03:42:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba97f385-a67f-37af-b9d9-240755500936 | -7.25919 | -46.59714 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4024e180-2260-3681-aa1f-effc8d570295 | -6.62014 | -45.57908 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c01e282-b423-3fd7-8d66-4a2886b835a8 | -7.58231 | -44.5872 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| c5f7e72e-4232-308e-ab39-12acfafc3b1f | -6.64268 | -38.91619 | 2025-09-17 03:42:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 295a6c07-8d37-3fdf-9f33-6b4097339bdc | -5.76737 | -45.9013 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7457aed4-9388-398b-b859-c28337ebf33c | -7.96576 | -35.24638 | 2025-09-17 03:42:00 | NOAA-21 | GLÓRIA DO GOITÁ | PERNAMBUCO | Brasil | 2606101 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 602ec1b8-6c1d-34dd-92c3-46083fb3f388 | -7.57586 | -44.56272 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6989fafd-a381-3ed7-bafc-f3f32cfe0eaf | -7.26538 | -46.58539 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a55afaa4-3ed8-3bb2-aa23-144408b0f95e | -6.87747 | -43.97501 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 58d6ae72-4a12-3d04-93c0-67b3e895ceee | -6.87721 | -43.96405 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4b9d651e-3de9-31a4-9da1-fc880bc4b378 | -7.58404 | -44.57749 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| feea7f2f-428b-3d22-89ad-48c546e6b1de | -6.87225 | -45.19061 | 2025-09-17 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7e9c07bb-7efe-3241-b4f2-c19c3464dc0c | -6.30113 | -42.39609 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b8f7aa5a-0174-3f11-90f7-8d48a551ca20 | -5.77327 | -45.90226 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 926110d7-eaf6-3174-af36-a31baf12322a | -7.13862 | -46.0912 | 2025-09-17 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7fa3045-5946-3f7b-9c12-3cb9833713c7 | -7.26453 | -46.59014 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| df6b7c33-4efa-3a8d-94c4-5cb8d6a98258 | -7.58929 | -44.57838 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e25634b-3b6d-32a9-a7ae-f4398a0bc179 | -3.41836 | -47.60498 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7af65d15-e00c-3c91-b2c6-cac4c951d32b | -6.59645 | -44.32249 | 2025-09-17 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59a1003f-7b33-344d-8ca6-05ec5199c8d5 | -7.07941 | -44.55811 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 89143d76-52f4-330d-86b3-88edb8f890cf | -7.58987 | -44.57512 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15942bbe-0d99-3497-86f3-e2d6b8e6810a | -7.27452 | -46.58154 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b254c02-c241-30d6-a6d9-408f10328c72 | -6.87392 | -43.96513 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2de299ba-db6a-35b4-87fe-c113c6a5126b | -6.8734 | -43.96813 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b3b0b6e-1de8-356e-b4c8-ae2476afba85 | -6.10039 | -45.94584 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15d0d9f5-c912-371e-b471-edca91d5c545 | -6.40031 | -41.7943 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 96152c10-757b-3ef0-bc9e-9c4257db74c4 | -6.57327 | -44.08602 | 2025-09-17 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e61dcc8-4667-3b59-b3c5-10b2904bc0d7 | -7.59281 | -44.58904 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f29857ec-5aa9-372d-8294-9ca7f8741e49 | -6.67863 | -46.30886 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 8af71db5-4592-3f52-80df-be0afd918590 | -6.88177 | -43.9679 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5e99c591-d8db-3d59-a3e6-03769948eda7 | -5.08595 | -41.16964 | 2025-09-17 03:42:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fa4475b6-94e4-3ca1-80da-0d14ba7a2b8c | -5.84379 | -37.49395 | 2025-09-17 03:42:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 74fe52a8-8e79-35d4-803c-ea7e4b1a0613 | -7.67924 | -44.46935 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a4cb686-7ba8-35cd-a905-f2c12a09c9f3 | -6.29815 | -42.38586 | 2025-09-17 03:42:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6da32c8a-fcfa-3a1b-9b42-0711905f2b05 | -6.04283 | -43.14347 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0ee26572-32b1-344d-9778-a00adbeddde5 | -6.87186 | -45.19037 | 2025-09-17 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5addde4-e441-3d77-b610-abe2340efaba | -7.65079 | -44.47374 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8eae1a9c-39fe-3e4e-a3f1-3be531455ee9 | -6.09913 | -45.94428 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e9659c48-43fe-3f6c-868c-e9911bd50aef | -7.5747 | -44.56924 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 088b22e4-ae3e-367a-b32e-5f633be65910 | -4.6386 | -46.07122 | 2025-09-17 03:42:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 623ba3ad-862e-303c-928c-ef9fe554f626 | -6.18047 | -41.2263 | 2025-09-17 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0c76331a-b1ff-3f70-962f-a98fda234fa9 | -2.37707 | -47.63235 | 2025-09-17 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 837fcf1e-d9f5-3780-b475-e4597121a084 | -3.50744 | -48.45124 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cc4d2774-fd91-30ee-bef1-a1890790fa24 | -7.52861 | -44.73512 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
