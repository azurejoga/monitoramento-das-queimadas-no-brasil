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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67779257-eb91-30e0-ab3d-ce41b6a6edb3 | -2.97768 | -45.83471 | 2024-11-11 03:55:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a4395e9-7b1f-3368-a641-2743e1e36d7e | -2.83732 | -46.64866 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 978ae20b-5f69-317e-a246-a4a16100cfc9 | -2.69569 | -46.81956 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0a27d67-c0e8-3c53-819d-41aa378295d9 | -4.68368 | -46.37395 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d363ecf-a6cf-3797-88ba-6f8ae83a1f21 | -3.52272 | -40.90536 | 2024-11-11 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 841fcd1f-572c-368e-8021-0c797e20e801 | -2.05768 | -46.14497 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37bcaa4f-9424-3c1f-9ba5-6d8adc03700d | -3.53777 | -43.56309 | 2024-11-11 03:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42e15709-910c-354d-b987-bc111ae75fb7 | -4.68463 | -46.36845 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 463fbf8b-6506-3c51-8a80-d43791ec172c | -9.10614 | -35.56203 | 2024-11-11 03:55:00 | NOAA-21 | MATRIZ DE CAMARAGIBE | ALAGOAS | Brasil | 2705101 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b850b63a-bdce-34a0-9ed8-a6edd1cdc670 | -2.19176 | -46.57508 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9de9a1b-74fa-30c1-9c96-3f754aa35bc9 | -9.22629 | -35.35175 | 2024-11-11 03:55:00 | NOAA-21 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7c7f178b-3ac6-3481-aac4-d9d5e0a69579 | -2.22972 | -48.39314 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 625d59f7-d247-30be-8f58-2776c4c14833 | -2.25517 | -46.51838 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| df9c0cef-513a-3e50-a6c7-9fb7efaf100d | -3.76367 | -40.82964 | 2024-11-11 03:55:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50f8bde5-0a3a-3cd1-ae80-85f4178a3c15 | -3.52933 | -45.70755 | 2024-11-11 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| eb4de679-7c60-3c96-8460-bbeb3fb799ae | -2.47698 | -46.3483 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3a60edd-f89f-3f6f-a27d-242eac819e37 | -4.46355 | -38.74707 | 2024-11-11 03:55:00 | NOAA-21 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e460afdd-fe3b-313c-9492-e717a23d1632 | -6.85079 | -38.88321 | 2024-11-11 03:55:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 10613c87-aa44-3f78-b78f-c3fec44e8f36 | -2.19069 | -46.58157 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b2e154d-63e2-337e-93cf-0c533fa76307 | -2.15774 | -48.90018 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fbc9fe8-3a7e-3071-87f1-662f535da9b8 | -9.51566 | -36.08731 | 2024-11-11 03:55:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 86e17877-f5d7-399e-a7aa-d7a20fdfbfe9 | -2.10346 | -46.52326 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 90934371-4a2e-3b21-a2d9-714fd8aa87e4 | -3.60673 | -44.26503 | 2024-11-11 03:55:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 33cd55f0-fce0-3d64-a5cf-427efccea8d2 | -3.68672 | -45.23875 | 2024-11-11 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38729d06-c511-3a22-a0e6-195ddd07c3f0 | -2.8326 | -46.64462 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38ae903b-1eed-343c-b573-4b433566ffcf | -7.63037 | -40.04498 | 2024-11-11 03:55:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 12d3bd71-c73a-3b81-9f19-2c1fb261b52b | -10.25594 | -36.51727 | 2024-11-11 03:55:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 167459e7-a69b-3e8b-bdf6-1b25432ebdf6 | -2.99348 | -46.93939 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 855de765-4671-30c6-ae5a-32e22809007c | -6.84417 | -38.88221 | 2024-11-11 03:55:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17b99817-5674-3402-b9cc-7859d0022f36 | -3.32453 | -46.10302 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3c0947e-fdfe-3956-8880-af2d06706e7e | -4.69421 | -46.43257 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44381e41-03bb-3599-8231-61d6cd81b96e | -4.12805 | -43.58839 | 2024-11-11 03:55:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8af366cc-c166-34cb-a0ff-944a5f82b033 | -3.24395 | -45.38454 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62aa626e-4511-3c40-a90b-7d3171389d43 | -5.55309 | -41.66468 | 2024-11-11 03:55:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6adbec18-5930-3af5-ba67-5022f400884f | -3.24411 | -45.38275 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f4b4d489-4bac-3c7d-bb13-e843a0832332 | -3.53422 | -43.1827 | 2024-11-11 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efb17085-ccc2-3c09-b056-298b77194003 | -2.08884 | -46.48087 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3a65b32-6b0d-363e-b6f6-e51c38b29487 | -5.58789 | -41.49321 | 2024-11-11 03:55:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5a1fd05-386f-3e16-8e3c-d28f458216eb | -3.24644 | -46.48736 | 2024-11-11 03:55:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c051a7b4-0314-3fcf-b216-570857faecb6 | -4.13372 | -38.70231 | 2024-11-11 03:55:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 76b463ed-7a2b-320e-83cc-630b7527a121 | -6.85355 | -38.88716 | 2024-11-11 03:55:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9c140514-a137-3af4-ad50-c08ba0d9a79f | -2.9769 | -46.9877 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c1bfdc4-93fb-38c1-ae01-f21bf3962eab | -4.69525 | -46.42655 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30562617-709e-311d-9e1f-bd085f1a12e9 | -4.0876 | -43.94439 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c98635a-af6a-34d4-a6be-d402e81d5723 | -2.26264 | -48.75834 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0290c12-2814-30ac-96b1-c9a8706243cd | -2.16228 | -46.42713 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32a49e9c-e876-38e0-834c-9a9dbf3720e7 | -6.01166 | -38.65871 | 2024-11-11 03:55:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 34638580-e6d9-3417-81aa-3b4fbf71f2cc | -2.97881 | -46.99377 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ea60f3a-bb7b-3d59-86db-90973fcf5978 | -2.87569 | -46.6451 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 916650f5-5e8e-349c-8b76-72077c50e97e | -1.84509 | -46.58438 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 2223717d-c3c5-3dd1-a398-e9ee966ce924 | -2.87341 | -45.36618 | 2024-11-11 03:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8803c5b2-6411-347b-ae24-3da25f9bd187 | -5.82036 | -44.1242 | 2024-11-11 03:55:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6aa75816-1894-341e-8eb7-8c4100f520a8 | -2.66184 | -49.39475 | 2024-11-11 03:55:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21d2c7d3-4a9e-39b5-b132-7bae9b480d80 | -4.70732 | -46.38622 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee2de23f-7150-3433-9f8b-8847e08711cf | -2.69672 | -46.81338 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca3d1a38-fcf4-3558-83c7-eb7cfe2cabff | -4.80495 | -40.69409 | 2024-11-11 03:55:00 | NOAA-21 | ARARENDÁ | CEARÁ | Brasil | 2301257 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a90727ff-d481-3a8d-8b4d-d35ec4a4d8cf | -1.98609 | -46.44968 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95c802df-6f0e-35ea-8f11-72ccd92eb236 | -2.99882 | -46.94029 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b19bb3f0-427e-3a67-a490-5026a4cfa1a7 | -4.69473 | -46.42956 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b44dfe7-3f38-3067-85fe-6b5a7b0788b6 | -9.59951 | -36.0183 | 2024-11-11 03:55:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 66c8dafb-2d3c-32ac-98a6-1236211d4ba3 | -7.48797 | -34.9267 | 2024-11-11 03:55:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 50d22793-c5b8-3737-87e5-0161120f1da5 | -2.30844 | -48.9028 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39df96a-0919-3fc6-ae73-68761605ba55 | -4.07279 | -43.95443 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb6133e4-e6f2-3114-8183-81638e515145 | -3.24498 | -45.37756 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b27f6c10-33cb-3d17-81ca-65bf469b8964 | -5.54945 | -41.66413 | 2024-11-11 03:55:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 40e50160-0705-3ce2-a871-d98ee0552df1 | -2.23514 | -46.44294 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f3a7d2e9-162c-3353-b860-b5b8f8a6c25b | -3.53952 | -43.17595 | 2024-11-11 03:55:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cce000d8-ec3e-35e7-a04a-77b953737a8d | -3.52041 | -40.90608 | 2024-11-11 03:55:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 986b5e92-770d-3441-b90d-eae173bc685b | -6.52994 | -39.58292 | 2024-11-11 03:55:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 40175780-2a76-382d-b99f-7e859a848ddb | -2.69939 | -46.67031 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90183899-0aa1-37bb-b485-fed326d18590 | -2.15159 | -48.89919 | 2024-11-11 03:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9d4b8ab-bfd2-3b5b-8ef6-5d929a894c94 | -3.3017 | -42.38112 | 2024-11-11 03:55:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c911ad2-aa6c-3c5e-8980-65134e3fef8d | -3.68461 | -45.24108 | 2024-11-11 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ffa2a508-cb08-3778-a2e1-660805870678 | -2.08249 | -46.48654 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e522e9-cada-3f50-a5ec-b6cebcfe54d0 | -2.97635 | -46.99107 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5a15f9c-1d98-3a68-bca3-47cd324514b7 | -1.98555 | -46.45294 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6790bd9-ab18-3ac0-b649-5078189f759a | -3.12381 | -45.97738 | 2024-11-11 03:55:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e31536ea-8a7c-36ab-83b2-02a78c597296 | -5.53964 | -39.10918 | 2024-11-11 03:55:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c0baf5c7-66bf-3d82-af0b-b70f4dd026cc | -7.73 | -35.18005 | 2024-11-11 03:55:00 | NOAA-21 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a746130-4600-3821-bba3-94170b7ae065 | -2.73616 | -45.21401 | 2024-11-11 03:55:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 95e44e6a-cef6-3028-8fea-48e958391a41 | -7.22806 | -39.96571 | 2024-11-11 03:55:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 238b180e-5bc8-37d6-b690-653eaeb7a500 | -4.71232 | -46.38709 | 2024-11-11 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4dcfda15-642c-312e-a6bf-b7d454c0edf0 | -2.19545 | -48.37879 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce6c137a-cc55-3903-a13c-1f44e2bb7223 | -3.59344 | -44.54772 | 2024-11-11 03:55:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7aa02871-8401-345e-b7a6-14f9755feca2 | -3.55509 | -44.96016 | 2024-11-11 03:55:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31a48953-ecce-3c95-bf39-57b4b13c9ff1 | -2.08883 | -46.4818 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fb8c971-2aa9-39b9-8b5b-d6fa33321d77 | -3.24019 | -45.37678 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8eadccba-383f-398e-97ab-c8bdbed080d6 | -2.06829 | -46.34128 | 2024-11-11 03:55:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7c138c6-3426-3bdc-bf02-c59020da77a7 | -2.55091 | -47.45261 | 2024-11-11 03:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8c5cabc-2236-3237-a29f-6fe3ce098ecc | -2.19473 | -48.38309 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f486cf5a-d398-3f54-9ad7-3dca90427172 | -3.23453 | -45.38121 | 2024-11-11 03:55:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c93ef98-4578-3ba4-b884-56c0eefa2c73 | -3.02603 | -45.81924 | 2024-11-11 03:55:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| dc323579-6c23-33b1-be64-9ca25b76db64 | -5.84858 | -42.48487 | 2024-11-11 03:55:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 17e0dbad-a3f5-3bde-bf3e-ce701ebbfdf6 | -3.69143 | -45.23952 | 2024-11-11 03:55:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f0fa07a-01bf-3676-8acf-9d13ccc5cbcc | -2.18877 | -48.38216 | 2024-11-11 03:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| df37c776-f301-3329-b1ac-be636011c70a | -7.43626 | -39.76668 | 2024-11-11 03:55:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0095bc67-2323-3785-b0ad-cf09b896364b | -4.07344 | -43.9504 | 2024-11-11 03:55:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bcac9ecc-776b-338c-9149-9281710050fe | -7.48953 | -34.9253 | 2024-11-11 03:55:00 | NOAA-21 | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad45ebcf-1ef2-3050-b04c-7f830f78c795 | -2.98419 | -46.9946 | 2024-11-11 03:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4d052d4-793e-3ab9-874f-02308285b6db | -3.59271 | -44.55227 | 2024-11-11 03:55:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README26.md)
