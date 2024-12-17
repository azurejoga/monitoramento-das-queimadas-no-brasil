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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b98e76b6-7e47-35f3-8c46-478ecdc2f9ab | -7.45343 | -37.99332 | 2024-12-17 12:04:00 | TERRA_M-T | SANTANA DOS GARROTES | PARAÍBA | Brasil | 2513604 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f25c79c7-6d62-3edf-8b56-b8862022b458 | -5.3172 | -44.24185 | 2024-12-17 12:04:00 | TERRA_M-T | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 84760b39-b202-38ff-9857-349796d00696 | -6.7791 | -38.38102 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 23620fc1-dbb9-3cf0-9109-cc289c0b954e | -6.36589 | -38.81063 | 2024-12-17 12:04:00 | TERRA_M-T | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| e8918088-72a4-3e9b-a304-8c162080d75a | -6.97532 | -42.81625 | 2024-12-17 12:04:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| ff7a2634-cacc-3855-9c99-37034670b247 | -3.23869 | -41.55744 | 2024-12-17 12:04:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 99adef46-82e2-3dac-b849-368b3e8fd3ca | -3.25817 | -41.22334 | 2024-12-17 12:04:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 38fbac31-882c-3983-9a78-ac54a865bf49 | -5.88741 | -38.16626 | 2024-12-17 12:04:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 04cb953a-2711-3d73-96b4-f384edeae1cb | -6.24097 | -38.84962 | 2024-12-17 12:04:00 | TERRA_M-T | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| dc156b1b-f520-38d2-ae5c-420d8abc9772 | -4.30566 | -43.88566 | 2024-12-17 12:04:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| e305d3f2-869e-38ce-ab79-67c2a07bce1c | -7.45215 | -38.00229 | 2024-12-17 12:04:00 | TERRA_M-T | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3435e7fd-9f51-39f5-9c2b-090e3f2961e8 | -6.77027 | -38.37978 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a04730c7-a696-369e-a268-9e9fe248f470 | -7.46105 | -37.15543 | 2024-12-17 12:04:00 | TERRA_M-T | ITAPETIM | PERNAMBUCO | Brasil | 2607703 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8c100027-55c9-335a-adbf-841ba63e425a | -6.26822 | -39.29583 | 2024-12-17 12:04:00 | TERRA_M-T | QUIXELÔ | CEARÁ | Brasil | 2311355 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 6e16102b-f0f8-3550-ba5f-b9aa7799969d | -6.07976 | -44.15368 | 2024-12-17 12:04:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e2d51926-b8a8-3170-8215-55dcadbaa5a1 | -6.78822 | -41.26521 | 2024-12-17 12:04:00 | TERRA_M-T | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7419ba34-3976-393c-b531-6bad9522552c | -7.04719 | -39.71196 | 2024-12-17 12:04:00 | TERRA_M-T | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 8fc6c861-d5ae-3f0a-ad57-2c73bb82453b | -5.95663 | -38.38869 | 2024-12-17 12:04:00 | TERRA_M-T | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4ad8a04e-a923-39e4-94f0-fd6378a17bbe | -6.26599 | -37.58455 | 2024-12-17 12:04:00 | TERRA_M-T | BREJO DO CRUZ | PARAÍBA | Brasil | 2502805 | 25 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 97602f30-ee78-3f9f-aaee-f6ceac07b566 | -4.9806 | -37.74306 | 2024-12-17 12:04:00 | TERRA_M-T | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0415928d-92a0-3f33-8d0a-71b1188885d6 | -6.9626 | -42.82809 | 2024-12-17 12:04:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 7d44c713-4b83-3554-8181-586a659a492c | -5.22874 | -43.17822 | 2024-12-17 12:04:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 771fbdb0-08b3-394e-9aeb-eca415f82181 | -7.22327 | -38.37547 | 2024-12-17 12:04:00 | TERRA_M-T | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 7582d547-d6fb-325b-bbdd-76a53bf96793 | -4.17796 | -42.44685 | 2024-12-17 12:04:00 | TERRA_M-T | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 599d73a6-b235-3b80-b8e9-30d8491d3d07 | -5.34452 | -39.48969 | 2024-12-17 12:04:00 | TERRA_M-T | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 2c76e688-1971-3469-ad74-04d38b85901a | -6.9519 | -42.82649 | 2024-12-17 12:04:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.1 |
| a6265fb8-7891-3b07-9ff0-2a538320b47f | -7.14782 | -39.28307 | 2024-12-17 12:04:00 | TERRA_M-T | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 54823425-44d6-37f4-b1cd-8012049e96ba | -7.085 | -37.98983 | 2024-12-17 12:04:00 | TERRA_M-T | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 75b0d3d4-6c69-3f9c-acef-d0f2bf3d8a7d | -7.27413 | -37.10757 | 2024-12-17 12:04:00 | TERRA_M-T | DESTERRO | PARAÍBA | Brasil | 2505402 | 25 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 04a0cbad-3e96-3959-a106-0a4d39a1fddf | -3.25667 | -41.22945 | 2024-12-17 12:04:00 | TERRA_M-T | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5eb6a3dd-f4c7-3102-a768-1ed32783215b | -5.86207 | -38.27953 | 2024-12-17 12:04:00 | TERRA_M-T | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 10.4 |
| aa966b37-db84-32c8-82f3-ee28d6167e4c | -5.12126 | -43.20284 | 2024-12-17 12:04:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 9927f6e1-1622-3a3f-90ca-336980c5a88e | -5.9932 | -38.97377 | 2024-12-17 12:04:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8fcb684d-9d5b-398a-9777-cb61aa43ba2a | -7.5257 | -40.91277 | 2024-12-17 12:06:00 | TERRA_M-T | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| b05b364a-4a25-36f0-94fa-aca3fa9c6fbc | -10.22896 | -39.59537 | 2024-12-17 12:06:00 | TERRA_M-T | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 21.8 |
| a10041e8-1c83-32ce-8088-8b627868caf8 | -11.34436 | -37.78086 | 2024-12-17 12:06:00 | TERRA_M-T | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 5604bfd0-e3d6-3506-a6c9-4a295c4b2a51 | -8.81345 | -37.43509 | 2024-12-17 12:06:00 | TERRA_M-T | MANARI | PERNAMBUCO | Brasil | 2609154 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a5c7025c-bfcb-34db-b2e3-3fb27cf6874f | -8.01655 | -37.2693 | 2024-12-17 12:06:00 | TERRA_M-T | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 23f0b6a3-a9a8-31ba-8444-6c5e16686ef4 | -7.80902 | -38.08679 | 2024-12-17 12:06:00 | TERRA_M-T | SÃO JOSÉ DE PRINCESA | PARAÍBA | Brasil | 2514552 | 25 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 79e19c85-9703-3c34-8f57-7e146242aba7 | -9.10144 | -37.55109 | 2024-12-17 12:06:00 | TERRA_M-T | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 1db3f569-4594-3807-acbe-1930903d58ca | -10.88614 | -38.68532 | 2024-12-17 12:06:00 | TERRA_M-T | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 83534205-7c87-3f59-ab86-a9dec5ac8487 | -7.7565 | -37.87111 | 2024-12-17 12:06:00 | TERRA_M-T | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 19334bbb-95a5-3ea7-8478-326a1a845ee3 | -7.80013 | -38.0856 | 2024-12-17 12:06:00 | TERRA_M-T | SÃO JOSÉ DE PRINCESA | PARAÍBA | Brasil | 2514552 | 25 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7fb5c0d2-3474-329c-bc06-a99d9db654a2 | -10.89633 | -38.67752 | 2024-12-17 12:06:00 | TERRA_M-T | RIBEIRA DO POMBAL | BAHIA | Brasil | 2926608 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| bb919a17-2792-3daa-b372-f47916596176 | -7.80931 | -38.72757 | 2024-12-17 12:06:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 2637c532-8624-3b2a-9abc-cf03e1bfc737 | -8.22916 | -37.59403 | 2024-12-17 12:06:00 | TERRA_M-T | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e34602d1-2bda-3b8f-b072-bec52ebcd079 | -10.36186 | -36.64017 | 2024-12-17 12:06:00 | TERRA_M-T | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b8ba4f6e-caa4-3300-afd7-8096342de9ea | -9.31967 | -37.24057 | 2024-12-17 12:06:00 | TERRA_M-T | POÇO DAS TRINCHEIRAS | ALAGOAS | Brasil | 2707206 | 27 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 563a0302-cae0-3d0a-9cd1-dc766856596f | -7.3484 | -41.28833 | 2024-12-17 12:06:00 | TERRA_M-T | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2b013818-b22b-360c-8fa3-c64b5a4f7bd3 | -8.65959 | -37.21645 | 2024-12-17 12:06:00 | TERRA_M-T | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 25.5 |
| 74b89f44-c4ef-3c70-8bfa-4ce77bb98f52 | -8.30075 | -36.54875 | 2024-12-17 12:06:00 | TERRA_M-T | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 2478d019-5728-3e8b-b2a1-74494242d844 | -12.051 | -45.07549 | 2024-12-17 12:06:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 28709d1f-146e-325c-aa64-777b9b297713 | -9.11055 | -37.55231 | 2024-12-17 12:06:00 | TERRA_M-T | CANAPI | ALAGOAS | Brasil | 2701605 | 27 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 027f8cf2-147c-3635-9348-b9fad389b917 | -8.43533 | -38.53699 | 2024-12-17 12:06:00 | TERRA_M-T | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 4d1a1169-bf32-32a1-921f-f34a258ae3ed | -12.77975 | -42.34804 | 2024-12-17 12:06:00 | TERRA_M-T | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| f392c9c6-d2fb-3162-adcc-7a5272e33ddf | -7.69151 | -39.59952 | 2024-12-17 12:06:00 | TERRA_M-T | MOREILÂNDIA | PERNAMBUCO | Brasil | 2614303 | 26 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 58889391-ae35-327f-9885-69f2e973e42d | -7.86422 | -39.61852 | 2024-12-17 12:06:00 | TERRA_M-T | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 4935c2d6-9f71-3ecd-b29c-a405e98492aa | -8.65462 | -37.11638 | 2024-12-17 12:06:00 | TERRA_M-T | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 3d52a7a4-fd97-372d-b495-6cc7715db724 | -8.6504 | -37.21526 | 2024-12-17 12:06:00 | TERRA_M-T | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| d12b4d03-a8e2-38b5-a708-08ea2e036852 | -6.92832 | -43.50935 | 2024-12-17 12:06:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 27.6 |
| e3f00534-e02d-3e68-bb46-87b9125335d8 | -10.65317 | -43.14244 | 2024-12-17 12:06:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a4641e30-4efd-399e-b58a-9d72758b6ec0 | -9.83115 | -38.38771 | 2024-12-17 12:06:00 | TERRA_M-T | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| efaea90b-d340-38ac-9d19-2e2118f489c5 | -16.99968 | -39.30577 | 2024-12-17 12:08:00 | TERRA_M-T | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 366143c6-9507-3996-a84b-e418b07c2b5e | -17.00732 | -39.31292 | 2024-12-17 12:08:00 | TERRA_M-T | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 7b21858f-866b-3496-8dd2-df0ec15827dc | -16.99833 | -39.3155 | 2024-12-17 12:08:00 | TERRA_M-T | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 755faa2a-9a7d-307d-b1a2-319a2f270df8 | -16.93192 | -40.05841 | 2024-12-17 12:08:00 | TERRA_M-T | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| 2972ce0b-0390-3d87-af9a-05bbc8634596 | -17.00864 | -39.30318 | 2024-12-17 12:08:00 | TERRA_M-T | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 8e97052f-4489-3e37-a3d6-cd7d89ab78c8 | -6.961 | -42.8344 | 2024-12-17 12:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 756361f4-5d89-37d3-876d-a5d6a57dcdc2 | -6.9799 | -42.8326 | 2024-12-17 12:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| fbe07f77-0812-39f6-a2bd-a8cf62c08875 | -6.9799 | -42.8326 | 2024-12-17 12:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 694d9556-b132-3382-b8df-bd331a4190da | -6.961 | -42.8344 | 2024-12-17 12:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.4 |
| 93dbd8bd-2889-3095-becf-8474b0097c53 | -6.9801 | -42.809 | 2024-12-17 12:20:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| c97685d6-f9cc-389c-8b09-bbd2e378c16f | -6.9801 | -42.809 | 2024-12-17 12:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 0825cdad-8e0f-3d1b-9fec-07e9a0c5e462 | -6.961 | -42.8344 | 2024-12-17 12:30:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 129.5 |
| 6ab22ffb-bac0-3448-bb53-e5926b7bc5d8 | -6.9799 | -42.8326 | 2024-12-17 12:30:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 09959b86-454f-3517-b715-c2a5f60d8a8c | -6.214 | -46.2202 | 2024-12-17 12:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| d1a6e3d7-7d24-3769-abac-8780b7231330 | -6.961 | -42.8344 | 2024-12-17 12:40:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 2db65a0f-5df4-349e-9d49-3bdc531f345c | -6.9801 | -42.809 | 2024-12-17 12:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| f8461504-e4bd-31bc-b892-1449b1bc1762 | -6.9799 | -42.8326 | 2024-12-17 12:40:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 150.0 |
| 48c16dae-800f-3c26-becb-12b6dc274356 | -4.9024 | -42.08 | 2024-12-17 12:40:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 83.4 |
| 348dd930-d29a-33d1-ba7a-496a96ad9262 | -6.961 | -42.8344 | 2024-12-17 12:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 165.0 |
| be606170-62e8-3940-9d9c-69bfca4814be | -4.9024 | -42.08 | 2024-12-17 12:50:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 132.6 |
| b15027d1-b159-37e5-9868-3d07e2952c97 | -6.9799 | -42.8326 | 2024-12-17 12:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 132.8 |
| 73d011db-ac26-3663-a35a-d988b0b5efca | -6.9801 | -42.809 | 2024-12-17 12:50:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| 4a3e0ed4-09cf-3213-815c-b7d18f25a916 | -6.9801 | -42.809 | 2024-12-17 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 94.5 |
| f90b2b35-2132-3ba7-a31a-a0b5284b58dc | -6.9424 | -42.8126 | 2024-12-17 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 203fc371-456c-3a02-96ac-13b56291ec0e | -6.9422 | -42.8362 | 2024-12-17 13:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 34ed843f-2d01-3fd8-a98e-76000200eaa9 | -6.9799 | -42.8326 | 2024-12-17 13:00:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 8639e65e-c759-3318-a49a-0c46b52dfdb5 | -6.961 | -42.8344 | 2024-12-17 13:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.8 |
| 3e0ab614-0d73-37a6-9950-49c638246fa1 | -4.9024 | -42.08 | 2024-12-17 13:00:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 327.8 |
| 3a0ae3c3-7aa7-3891-9e5e-ca65b711845b | -6.97 | -42.81 | 2024-12-17 13:00:00 | MSG-03 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2123da85-c3d5-3883-8cdc-abd7a133155c | -6.961 | -42.8344 | 2024-12-17 13:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 158.7 |
| 71dcb6e2-fe85-3eba-9454-5488ac260112 | -4.9024 | -42.08 | 2024-12-17 13:10:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 189.9 |
| 386fe6cd-52c6-3ec5-a4b9-bc47e8923295 | -6.9801 | -42.809 | 2024-12-17 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 22327c6b-4660-3ad8-8e69-189f333085ff | -6.9799 | -42.8326 | 2024-12-17 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 117.5 |
| 1f644b6c-b6de-3958-b52d-8fe1c96174f8 | -3.704 | -42.1287 | 2024-12-17 13:10:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 08610c7f-ecf0-3ef3-b1ca-ed27045bf667 | -6.9422 | -42.8362 | 2024-12-17 13:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 73.3 |
| e45e5c10-9839-3815-a045-c8f9eb371bce | -6.9424 | -42.8126 | 2024-12-17 13:10:00 | GOES-16 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| c04719bd-b5ee-3da5-851a-6e3aed369cd3 | -4.9024 | -42.08 | 2024-12-17 13:20:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 181.0 |
| 2165a397-247e-30c1-a2eb-0e5406893540 | -3.704 | -42.1287 | 2024-12-17 13:20:00 | GOES-16 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |


[Clique aqui para ver as próximas entradas](README33.md)
