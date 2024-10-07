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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 318ff76e-8c28-354e-8771-a17f3fd7b4fc | -2.86363 | -52.915 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9821b6c4-5f78-304f-9587-6d31963b1a01 | -2.86173 | -52.90646 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 371535ca-059c-3bde-81d6-2a1a4958339f | -2.86059 | -52.91327 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b7be0da-7345-3af3-9324-a7a545c43a7a | -2.85951 | -52.91968 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 81198e87-0fd5-3ff3-9762-51f72ba9f850 | -2.85766 | -52.90714 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8c12b8a-dfbf-37a2-924d-f6f942ad4b33 | -2.85649 | -52.91377 | 2024-10-07 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c728f1f9-3dda-3e49-8cc1-f1c14d346351 | -4.27842 | -43.74549 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 271b1962-3ae5-321f-9b87-6976ec74eefe | -4.27807 | -43.7384 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97e9a706-5299-3a72-99f1-68a87e2292b3 | -4.27761 | -43.75037 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f236cb05-d0d5-3a6d-97bf-fcb78d354b80 | -4.2773 | -43.74323 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8d17a407-1bd6-38aa-8b65-b382f4cc97ff | -4.27653 | -43.74809 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 08a3364d-ec52-3cc3-87ed-33f47ee5e26b | -4.27574 | -43.75298 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2652e8ed-a52f-32a8-accc-4ef53045d9ce | -4.27421 | -43.7378 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38f15a80-60ef-33bb-b13e-22b1547caecd | -4.27344 | -43.74263 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 437918b0-eadd-303e-a44f-3f7e64fb7006 | -4.27266 | -43.74746 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96d2ea0d-e2e0-3558-bad5-3109790dd242 | -4.27189 | -43.75233 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06111e9e-f296-3c37-9c99-c5545beb080e | -4.27034 | -43.73721 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e807ab69-7024-3275-9391-9750f07e0f30 | -4.26957 | -43.74202 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 908729ac-374f-351b-a9ee-2bfbb6dc6af1 | -4.2688 | -43.74685 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9d27cd2c-3b0e-3390-b3a3-51e4c52538ec | -4.26802 | -43.75169 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77c626ff-5e8c-3c9f-a664-63f6e2d0b0db | -4.26647 | -43.73665 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a94fa642-460d-339d-b970-d36935810cab | -4.2657 | -43.74144 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3783adba-7335-3fe3-b07f-5107c729878d | -4.26494 | -43.74624 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60cb04ff-c692-3049-938e-f94f4b4fb204 | -4.13076 | -43.80654 | 2024-10-07 03:57:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d1342ec-13b6-3e1f-b635-92f833723923 | -4.12997 | -43.81144 | 2024-10-07 03:57:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf14b722-be71-35aa-b3f2-d5677266df7c | -4.04685 | -43.24292 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 663df047-468e-3d09-a89a-4a1bee2ac599 | -4.04405 | -43.24068 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03c8c815-f8dc-330d-b83b-31f0ad6655a6 | -4.0433 | -43.2452 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56a765eb-d061-3ce2-969d-9087c981a000 | -4.04309 | -43.24229 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cac31261-689c-3d15-a2d8-3f62fe7d9123 | -4.04256 | -43.24973 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c97629d2-4dd7-397d-a22b-9eaeb24cc9c0 | -4.04237 | -43.24682 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11196203-55f8-3840-ac7c-044e5404e454 | -4.04165 | -43.25136 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2a70fd3-9301-36e8-a992-cef4b014be27 | -4.01678 | -43.23801 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46779315-04bc-3e22-84b8-f569fb734482 | -4.01606 | -43.24253 | 2024-10-07 03:57:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da1d9e3-fe5d-3cb6-a136-f161930d7f6b | -4.81777 | -44.35506 | 2024-10-07 03:57:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9632e07f-fe6c-3f43-928f-67978bdce2ec | -5.57883 | -44.88171 | 2024-10-07 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73f522a2-37e0-3b72-9a86-03a48590b035 | -5.95474 | -38.6324 | 2024-10-07 03:57:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8133d901-387d-398e-8f05-f16e2aa71615 | -4.67379 | -41.42421 | 2024-10-07 03:57:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8c6ca835-2479-3a01-8399-4649746ebdfc | -4.03278 | -40.40111 | 2024-10-07 03:57:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| afae5095-f9c3-34ab-8951-dae36bd4d585 | -5.18167 | -41.29616 | 2024-10-07 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4099c3b0-6e48-3958-a748-181f606e2554 | -5.17827 | -41.29564 | 2024-10-07 03:57:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de231206-1438-30d3-91d5-bb1580634f4b | -3.95386 | -41.49809 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| df23b9b2-6c7a-31bb-8a35-d093dfaf21fe | -3.95041 | -41.49755 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5c3e25e5-fd3c-34c0-81f5-32213392df29 | -3.94981 | -41.50133 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9eaa0bc2-205f-3d93-a4fd-1afff116f7a6 | -3.94695 | -41.49701 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 747d499b-fc88-318f-a85c-92a40fbb1604 | -3.94635 | -41.50079 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 37438cfe-415b-3da3-bc50-0e5acb871e82 | -3.94411 | -41.49267 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 68dbfd31-b9b9-3f41-85c7-34d7ca45836a | -3.9435 | -41.49646 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1acdd333-cc1f-318f-acc4-cb580865c9df | -3.94065 | -41.49212 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b11f9b3f-8e21-3269-81b9-a6f94704b8cf | -3.94005 | -41.4959 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e9789699-5e99-3b37-9ef0-eca1da1c506c | -3.9372 | -41.49157 | 2024-10-07 03:57:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e98759c6-f4bf-3822-9fb9-393e5208490c | -4.79463 | -42.75586 | 2024-10-07 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36dde6cf-c290-36f6-9aac-b9ac0a1dd65f | -4.791 | -42.7553 | 2024-10-07 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 96731abc-3ba7-3ff5-8b72-420ea089c548 | -4.78737 | -42.75474 | 2024-10-07 03:57:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a6c2395-e588-3e33-a1d1-367ebfe6034c | -4.38191 | -43.03934 | 2024-10-07 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4733b5e1-dc1d-3bc9-af4f-ac00c2accba0 | -4.37751 | -43.0431 | 2024-10-07 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9fdaa20-1bbf-3b0b-9522-48182b4ed7cc | -4.37381 | -43.04248 | 2024-10-07 03:57:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15fbf8e2-27d7-3d47-8b85-48cdae0f5d9b | -5.88077 | -41.98591 | 2024-10-07 03:57:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d3f46567-5a1e-3a60-995e-894c638a0215 | -5.87794 | -41.9815 | 2024-10-07 03:57:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3b558f52-1e0d-35e3-864c-12c839af884f | -5.87731 | -41.98536 | 2024-10-07 03:57:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9c614da3-a504-3ed0-bf70-2426b39fc4d6 | -6.26293 | -42.53017 | 2024-10-07 03:57:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c94f83dd-af95-300a-8a88-9b2bdf35b637 | -6.26006 | -42.52559 | 2024-10-07 03:57:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b74e7d11-add4-3a91-8b24-698b519996f9 | -5.7392 | -43.05223 | 2024-10-07 03:57:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 153b88f5-193f-3075-83fe-65b556c72f5b | -5.68161 | -43.15394 | 2024-10-07 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7bffef56-d0dd-3a2f-b892-fca804be47be | -5.68078 | -43.15651 | 2024-10-07 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 913a3ff0-9ff0-392b-b338-a7047a28ad8d | -5.53033 | -42.79663 | 2024-10-07 03:57:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9fb89e9-eae4-37a1-8393-46e15c801f77 | -6.05532 | -43.09082 | 2024-10-07 03:57:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4d7fbed-6c29-3fe9-9c12-769909a23de0 | -3.38031 | -43.219 | 2024-10-07 03:57:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4be92a2-b271-39a4-a796-510d68583548 | -2.92926 | -44.30079 | 2024-10-07 03:57:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dd46d79-868d-39b9-8b54-211b5a210de9 | -4.28193 | -43.73901 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f462d665-a639-3f39-8922-1049a44caf10 | -4.28002 | -43.73589 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec4d4bb8-0866-32f3-a101-b510ffd834df | -4.27923 | -43.74067 | 2024-10-07 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 241da6e7-621c-36a7-addb-441b34964abc | -20.7174 | -49.6306 | 2024-10-07 03:57:01 | GOES-16 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 57b91f7e-65a8-3d6b-bfba-8963ebebebd9 | -21.3274 | -47.5939 | 2024-10-07 03:57:03 | GOES-16 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 52.1 |
| aa4d64e7-3417-3f27-938a-b86420d4607c | -21.6121 | -47.7121 | 2024-10-07 03:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 43.2 |
| d58c6404-5ce9-304d-8d97-fd6c4f91dbdb | -21.5913 | -47.7172 | 2024-10-07 03:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ee8ca4ac-f931-3a2f-8831-2f13b3e07038 | -21.5906 | -47.7409 | 2024-10-07 03:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 2859ea9c-8a5e-3065-b1de-cdbafa5f393c | -21.5705 | -47.7223 | 2024-10-07 03:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 73.1 |
| eb2cfb18-8e0e-39c8-a4bc-be00fb3191cf | -21.5698 | -47.746 | 2024-10-07 03:57:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 97.6 |
| dbee8865-cc17-3ee9-8bb7-97e8d333431b | -6.34596 | -45.72363 | 2024-10-07 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2e0e7fa-cf51-3981-8f31-4b1d2c5d1db2 | -6.34523 | -45.72241 | 2024-10-07 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 54a8ac23-885c-33fa-9257-33312f90e6e4 | -6.34168 | -45.72308 | 2024-10-07 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c894b08-4c34-3eaa-ae9b-69cbc22a5f8a | -6.34096 | -45.72185 | 2024-10-07 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 518fa7ce-c75e-3876-b68a-89aabd75ef8a | -9.31875 | -46.72382 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c184ff49-f428-3573-bda8-bd88ddc189b5 | -9.3178 | -46.72023 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d6130a4-309f-3a04-bf49-2e54e3c9416c | -9.31708 | -46.72444 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6698f89d-bdee-3392-933e-adc3232ceacb | -9.31636 | -46.72865 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2e8a91e1-ad0b-3072-9c54-fb45120cfbb5 | -9.31517 | -46.71884 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44268e4e-6c02-3679-aba1-534e5d7802b3 | -9.31442 | -46.72304 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0fdb3a8d-84ac-32c5-83ea-01c60b851d37 | -9.31419 | -46.71524 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62404d8a-0fe0-3ff8-83b1-567f4c18bb44 | -9.31367 | -46.72724 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e4ffed87-7699-37f1-989d-647551761822 | -9.31347 | -46.71945 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73e65244-dd13-395c-bcc4-7fa85fc54d61 | -9.31275 | -46.72366 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b7a6031d-e01d-3af1-95ab-daaa68fe0758 | -9.31203 | -46.72786 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 48f7bc24-1869-3a0b-b6f6-4fdd2845199f | -9.30916 | -46.71863 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8c1f870-dbbb-34c4-a6b1-418a4d2d863e | -9.30843 | -46.72284 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5d00e850-f4fb-328e-b027-67497ab5fba8 | -9.30771 | -46.72705 | 2024-10-07 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c8c5b2ca-947d-39ed-8de1-ab2853e430ae | -5.62119 | -47.40208 | 2024-10-07 04:00:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a3f02992-f12a-3e0d-8b96-008a2cae05a7 | -5.61999 | -47.40187 | 2024-10-07 04:00:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea9094d2-1f8d-3583-a6de-ce27f78e0ef3 | -5.61636 | -47.40124 | 2024-10-07 04:00:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README55.md)
