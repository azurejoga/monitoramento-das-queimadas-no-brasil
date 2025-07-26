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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475d135f-c512-34cf-8b17-124a862fc2fb | -3.38712 | -47.49305 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fff55794-9af4-32df-b94c-a7619533cdbe | -3.9895 | -43.23041 | 2025-07-26 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 23828a24-ddad-3637-9056-ba6b1507af59 | -3.39392 | -47.49413 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 070ea664-bed5-366d-9158-1043a22efcf4 | -4.06478 | -42.54166 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 4966a8c5-23ff-3825-9134-78ba44b9beb6 | -3.31414 | -48.71307 | 2025-07-26 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9343d42-6969-3b71-be84-4ae890a49c5b | -4.06906 | -42.53798 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9f0c7877-6598-3a71-877f-100fefd84107 | -2.91543 | -48.23438 | 2025-07-26 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbd09fee-fd3f-304a-9f89-ae230d576e3b | -2.86159 | -46.77112 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7d2dc73-fe09-3b0c-afdd-352897fdcaaa | -4.75932 | -38.48489 | 2025-07-26 04:23:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 87b7827a-34f5-3c08-a80c-51aea65bd665 | -3.05439 | -47.38136 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81fc0265-fa14-3de5-9418-c6bc9c8eaff2 | -3.39744 | -47.49843 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8979a11-24c2-366e-a99f-29b486e68857 | -3.43596 | -43.13821 | 2025-07-26 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 368b960d-66b9-3104-a5f7-4cb46ddd8353 | -3.04702 | -47.38395 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84a1771e-59a9-3934-9cf1-db54d1545221 | -3.65928 | -43.04917 | 2025-07-26 04:23:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 877a2f1d-d04b-3218-8db3-e0bbe23043db | -3.05396 | -40.02694 | 2025-07-26 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c7f91eca-fa61-3e6f-aee1-6f22c9906f11 | -3.63052 | -43.07037 | 2025-07-26 04:23:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c5fbc4b-0bdb-3274-b22f-8511f39804d9 | -3.58727 | -41.65021 | 2025-07-26 04:23:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 684ca136-a2a1-3c2e-bf17-76fee4b59ea0 | -3.56027 | -47.3777 | 2025-07-26 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482e9a18-967c-3659-afa4-c9f8beac621f | -3.39803 | -47.49477 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 8c27e881-a109-36e1-9a63-75ceaffd9daa | -3.39674 | -47.49834 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3d81b3e6-837e-3a32-b38b-31f63c7ae547 | -3.65895 | -43.05041 | 2025-07-26 04:23:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1515bc3d-7db6-3034-b6fe-39633cf0a0fc | -4.06425 | -42.54313 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f5eae4a3-958e-3d81-8ece-e133916bf29b | -3.05873 | -40.02372 | 2025-07-26 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 05b63958-d32f-3bcd-ab2e-81108a82616d | -3.05498 | -47.37769 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dea0793-b04c-3142-bf4f-bf0fc1fa9741 | -3.82312 | -41.57534 | 2025-07-26 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7927f123-dcd2-36c9-9252-b07a49adce0d | -3.99011 | -43.22645 | 2025-07-26 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 7a88e241-deeb-3bb8-b90b-04f27e16b1af | -2.91004 | -48.24561 | 2025-07-26 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4f3389fc-b57d-3789-bae0-e74326e8077f | -3.0476 | -47.38028 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34402833-dadf-32b1-a94f-bc92359fbf1e | -4.06855 | -42.53945 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4b5e7270-dadd-341f-99e5-89b27045a069 | -3.38828 | -47.48572 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 575ba43d-8dfc-3dbc-9223-12a10198a5e1 | -3.05454 | -40.02309 | 2025-07-26 04:23:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d2143f9d-7fec-3bc3-b804-ce6b62c5bd66 | -3.13003 | -47.01258 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ce47bd-10d6-34cf-b1f0-99807a59e49f | -3.11324 | -47.00993 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a68692b-fa9d-31fe-93e7-054aa3b86053 | -3.94555 | -41.48294 | 2025-07-26 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84d26f74-3840-3830-bc25-6f9e416ab58e | -3.27571 | -48.81653 | 2025-07-26 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d73e1b8a-2009-3c31-8037-2f2046bff663 | -3.58631 | -47.51985 | 2025-07-26 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 609938ac-1b99-38fa-87ab-075da60c7a6c | -3.46305 | -47.67872 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02fbe68f-4a65-349c-a40f-1bfdb7932009 | -3.3911 | -47.48993 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 892882d4-c201-3600-b21e-399afa98cf31 | -3.39167 | -47.48627 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a81a47b-16d7-396d-a8e2-d301c43a86f9 | -3.39052 | -47.4936 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ffa23942-a00f-3ed7-9453-93286f16989b | -3.4947 | -43.31422 | 2025-07-26 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82f97229-d23e-3415-a15c-afa95fb04758 | -3.39732 | -47.49468 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 7d660cae-8b73-3987-a9ec-8811b4478adb | -3.3843 | -47.48885 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65371691-7a72-3cdb-aa4f-844990ff4e0d | -3.99302 | -43.23096 | 2025-07-26 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7c932b3c-963a-30a4-8fd3-60c5b045f4af | -3.33112 | -49.03343 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0657a05-2d33-3cbe-95d2-15514ea6b9c1 | -3.826 | -41.55639 | 2025-07-26 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ef360912-8700-3452-b078-62c7924abfcf | -3.12331 | -47.01153 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a16607d4-f51b-3649-b301-e5c69bafe6b2 | -3.3979 | -47.49102 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 170584d5-474e-30ba-a882-1cf294a62a5d | -3.31292 | -48.71091 | 2025-07-26 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ea8278-28d8-36eb-815f-d8e9ada085f6 | -3.58175 | -47.52662 | 2025-07-26 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5cdcfe62-0957-35ab-8de1-aa2d1acbe4d3 | -3.42921 | -39.04569 | 2025-07-26 04:23:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76e927f1-dae6-38cb-96e2-1512adf0e515 | -3.43245 | -43.13767 | 2025-07-26 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a183230f-d592-322e-9e49-3995c5cb3b95 | -3.051 | -47.38082 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 360c1e69-6c83-309c-b0b9-5e6ea816865f | -3.82527 | -41.56115 | 2025-07-26 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 2a7d5559-1b37-3e5c-9e93-e053f7ee51c4 | -3.82455 | -41.56589 | 2025-07-26 04:23:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0b61ad6c-63ad-39a9-bc15-5ad6c4b98764 | -2.99581 | -49.32029 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 897700ce-8044-3407-8fcb-48a63fb59f6a | -2.99735 | -49.32254 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cdc141f-66d3-31b9-b1ab-4684c4078d1e | -3.43084 | -43.28863 | 2025-07-26 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e099818d-2f27-3a90-a599-1135775249b2 | -3.42735 | -43.28809 | 2025-07-26 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d82976b-34dd-32e8-afa1-33222824268b | -3.65541 | -43.04987 | 2025-07-26 04:23:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ac0e256-b133-316e-8904-dab12be0ddb4 | -3.81257 | -42.55059 | 2025-07-26 04:23:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b2e8fb0-4f2e-3b66-8f8c-da3099d568cd | -3.32657 | -48.71728 | 2025-07-26 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8dde6ece-84c4-3c0e-9daf-a76c026c21f8 | -3.3877 | -47.48939 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| c7c5863b-6c19-3fed-93b4-794d362519b3 | -3.31226 | -48.71499 | 2025-07-26 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5244c10b-c1c8-31a6-907e-d980bb2bb411 | -2.90942 | -48.24954 | 2025-07-26 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 4e9baf96-a895-3238-99e2-ca3326ebbeb2 | -3.99362 | -43.22701 | 2025-07-26 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 515f85f8-7ef3-33b2-8d85-202aff6c5a42 | -4.03477 | -42.51695 | 2025-07-26 04:23:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4f9d147d-691e-3e37-9760-545fba953965 | -3.38488 | -47.48518 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdf6815-4e0a-3213-87f3-c874b73ef3dc | -2.85914 | -46.77053 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60de4b5e-c24c-3e88-bf2f-bac9b0e25018 | -4.06491 | -42.53889 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 7bcdaa43-d623-3685-8e31-526453d6f55a | -2.90653 | -48.24505 | 2025-07-26 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 08e4dc8c-4258-3964-b4a8-548174149f9a | -4.06843 | -42.54221 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 95af3a41-5114-3480-bd06-abc8481fb07f | -3.38372 | -47.49252 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6bd6f12-68b9-34d4-b5c1-9749335dac4c | -2.82502 | -47.52324 | 2025-07-26 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c122b988-ba28-3921-ab93-bf715f84e55c | -4.04205 | -42.51806 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| eb033aac-6c23-3b96-ad5b-183168c9c3d5 | -2.9059 | -48.24899 | 2025-07-26 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7e3209e5-b2e8-3132-8a31-fdd520316511 | -4.06788 | -42.54367 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 0e0103e4-95e3-33fa-8ef5-6ce97c20a202 | -2.99364 | -49.32194 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 172d5843-208a-37ba-91ea-2a805a8870fb | -2.99434 | -49.31749 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fce617d4-7ad7-308a-83d3-fbc8a919653a | -4.03841 | -42.5175 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 18b5c18d-2e9d-3c4b-bf93-748f547f33af | -3.59108 | -41.65079 | 2025-07-26 04:23:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3e5beff-3623-31ce-9e76-094aa8029363 | -4.07207 | -42.54277 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| e45de85b-2f34-38ed-b089-26fae1d8ddfe | -2.99211 | -49.31968 | 2025-07-26 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb14e2e5-2f38-3dcf-bb2d-e7b4cd62495a | -4.06542 | -42.53741 | 2025-07-26 04:23:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da176976-3903-3195-a9f7-a17383a5fdd5 | -3.11995 | -47.011 | 2025-07-26 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31d7d06e-b156-3bdd-8b4a-65858a094b76 | -6.65699 | -58.84216 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a2e3c90f-c44e-37a3-a2aa-db5ab11a237a | -6.62796 | -58.85372 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 151e9132-1485-3c8e-a133-b9d9b0a2e6ea | -6.62354 | -58.84114 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 8a308c4a-8516-3451-bc36-be1eeb7c0c63 | -8.1711 | -43.21696 | 2025-07-26 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7207556c-68f5-3351-be9a-ad9c849d724f | -10.67425 | -51.89486 | 2025-07-26 04:25:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| db09440d-1a7e-3080-8a5d-0c650646ce4d | -7.17756 | -43.49264 | 2025-07-26 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8f3c8dc5-cac0-3bef-a4a0-2a74d2e0b915 | -6.87614 | -43.67569 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a7ab2791-afe2-3ebd-bec4-040ee830953f | -6.56039 | -41.4981 | 2025-07-26 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2bcb0865-69e0-3770-8261-b15330628376 | -6.659 | -58.83112 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| e846316e-fdfa-3b0c-a952-c4bdd7dd6062 | -6.54443 | -43.4762 | 2025-07-26 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 959518ee-afca-3bb0-a35d-53f9bc28e3ad | -6.64743 | -58.85772 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 377d0406-bdd2-3b8f-a9da-f912de2c7db9 | -7.23702 | -43.06384 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| edbb2e3a-f1d1-3a37-8050-c570975a82dc | -6.66627 | -58.93377 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a99423a-297b-3087-9285-7f142e75d8f5 | -10.50039 | -44.88225 | 2025-07-26 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a1a5fea-e359-3277-bb80-e39e24c7c64f | -6.65799 | -58.83668 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |


[Clique aqui para ver as próximas entradas](README15.md)
