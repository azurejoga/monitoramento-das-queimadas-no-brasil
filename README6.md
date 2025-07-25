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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb57aad9-bcb4-316b-a688-13142227fee5 | -5.48524 | -42.14921 | 2025-07-25 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 917cca8e-8983-3d1f-8d38-c566ba3952b4 | -5.48898 | -42.14983 | 2025-07-25 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f03ca35a-e3f5-3371-98c6-e0ad6b4d490d | -2.91705 | -48.2364 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4f91c45-e8d9-34bc-83a0-257b64646dcd | -4.10488 | -47.9358 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62eaeaa2-526a-3433-8681-fda34f27bc98 | -5.86449 | -35.69256 | 2025-07-25 03:53:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 10a23c8c-3879-3129-b4c4-ca3fc879a706 | -4.28901 | -48.06433 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 086c1ee1-0700-356b-8dda-d3b435606d48 | -3.32864 | -48.72057 | 2025-07-25 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 496c105c-a560-307f-9ff7-c28d9436455e | -4.83833 | -45.30463 | 2025-07-25 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ae66a4e9-5918-3502-99c2-67a03d024cda | -3.58067 | -47.52452 | 2025-07-25 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 77b43a56-1035-3b1c-9982-9bfa2f395a7b | -4.10551 | -47.9322 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6934f0d3-4f82-3f3d-bcae-47b218ad6396 | -4.83753 | -45.30941 | 2025-07-25 03:53:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d6685758-656a-38fc-8ddf-bba97df42990 | -2.90697 | -48.26064 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f1b8f4c-19ed-3025-ad67-bfda0b51b37f | -3.35232 | -42.86885 | 2025-07-25 03:53:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6d5673b-01e2-3768-97d4-750894267a5d | -4.04109 | -42.5225 | 2025-07-25 03:53:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 81f66342-6dec-3fac-90d3-4e5cba6cf881 | -4.29264 | -48.06111 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcbeccc5-4b95-3c63-80f2-d382f0607186 | -4.35218 | -47.68889 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8d7bca2a-ab4d-352a-8847-6d0b24f91ab2 | -3.04959 | -47.38112 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 34912dab-e8dc-3b62-9bc4-4a43434f533c | -5.0039 | -37.1449 | 2025-07-25 03:53:00 | NOAA-21 | GROSSOS | RIO GRANDE DO NORTE | Brasil | 2404408 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 926d6c9b-a5cc-3b6a-a7cf-5eda9a2c75be | -5.48451 | -42.15372 | 2025-07-25 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7cfc75f1-a6c4-39d2-a44f-af725a36e616 | -4.77983 | -45.33984 | 2025-07-25 03:53:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 63096068-126f-39bd-a9b3-259b0580cac5 | -4.10697 | -47.93605 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 560b0f1d-42bf-3510-8945-107c5b37e0ff | -2.91565 | -48.24472 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1fe32f9a-ee3c-3a02-90c9-817d855727c4 | -3.12273 | -47.01218 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 37e54a35-6a2d-3c32-a943-52eedff11309 | -4.04086 | -42.52007 | 2025-07-25 03:53:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8c4fd531-e1ec-35fe-a50c-22c52f1ed45e | -5.53101 | -38.26211 | 2025-07-25 03:53:00 | NOAA-21 | ALTO SANTO | CEARÁ | Brasil | 2300705 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 06de0725-1969-3b44-886a-bd065b3510f2 | -2.90981 | -48.2438 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8dc160a-98c3-3a6f-9c79-0fabc521c565 | -3.82609 | -41.57683 | 2025-07-25 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1f6fd73c-c576-3023-890a-f14049133b94 | -2.9084 | -48.25217 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf441200-bb9f-3594-a30b-59e85062e6b8 | -3.04346 | -47.38391 | 2025-07-25 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 490b3484-5211-32f8-8293-c7c08597dbf1 | -4.35158 | -47.69246 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| c194a788-52c3-36e5-81ef-a4c41783d8e0 | -4.83289 | -45.30864 | 2025-07-25 03:53:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cd06a69-b69a-39e3-bd6f-e48b7ea62956 | -2.91425 | -48.25304 | 2025-07-25 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc407ec7-8bea-3adc-a5e9-7b33d59992a5 | -3.32574 | -48.72128 | 2025-07-25 03:53:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21341b8c-a757-389a-a11a-add8ce365844 | -4.57091 | -40.77261 | 2025-07-25 03:53:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 757f25c2-d21e-3230-bfc4-296fbdeb534d | -4.90205 | -37.36567 | 2025-07-25 03:53:00 | NOAA-21 | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9b5e7199-a676-376c-8179-aaeb52709d61 | -4.31422 | -47.98318 | 2025-07-25 03:53:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94eaba5f-8405-3e48-ab10-1573f1704691 | -3.8252 | -41.55866 | 2025-07-25 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4574fe91-eabe-3910-a8ae-85fbe350ed5e | -4.04008 | -42.52504 | 2025-07-25 03:53:00 | NOAA-21 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 956b0d27-44a4-3e3a-b45b-6687275c8b5d | -3.8259 | -41.55428 | 2025-07-25 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a68fc96-cb57-3094-bf19-d15dd16e6cea | -3.82679 | -41.57242 | 2025-07-25 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 118105d7-224e-363f-bda5-4502478a6351 | -4.4507 | -38.44769 | 2025-07-25 03:53:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f0df1e6f-0c5f-3cc2-a17f-d31412d0eff2 | -11.45915 | -45.12219 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b6cd8bb1-08aa-38c2-8f9c-1d5a4c6b0f2f | -7.26503 | -43.06823 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| a4a9938d-1a1e-3220-b1dc-9fdd6cdd0cab | -7.30258 | -44.0187 | 2025-07-25 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ec22135-5027-3ec7-bcc3-a2f575ddf468 | -7.25654 | -43.07171 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 7e755390-037c-3a66-a22b-1c6b349bf0ff | -11.44962 | -45.12815 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 65ae7be7-5b7d-3bb4-95fc-5d9150f3face | -12.42349 | -45.37773 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 310e32b6-7196-3428-9bf9-a64fcd958905 | -7.86642 | -48.21655 | 2025-07-25 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0f0d002-6ab7-33f7-94ce-cdd546201e68 | -7.55367 | -44.48377 | 2025-07-25 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 971948c1-b987-3724-b4c3-51f01eb7b909 | -6.9496 | -44.56302 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3b153bc0-b728-3994-b099-2f701f932096 | -10.61097 | -45.23851 | 2025-07-25 03:55:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ef81aae7-5b15-39d8-88ea-db683dbd2a58 | -7.16793 | -43.48045 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a70aa6e0-fe0b-3cce-9adb-72155dac4196 | -7.91453 | -44.08482 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 770e6e4c-22f6-3356-af21-91f4de0ab4ca | -7.90985 | -44.08771 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7d84561-e337-3121-bc05-953d096aaa16 | -7.91798 | -44.08908 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7c8a1643-0cbb-3c6f-aaed-b6c81e5455d2 | -7.16483 | -43.47473 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6f2394e2-c455-3fe2-88d1-531f53a17c73 | -11.45373 | -45.1289 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 77496b1d-5963-366c-a203-4008ed9466b0 | -7.89926 | -42.63897 | 2025-07-25 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4106947b-25ad-3bfd-8e91-65b3d3416ae5 | -8.1277 | -50.46577 | 2025-07-25 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ac6d4983-e74e-358a-874f-d496dbecdb61 | -8.12156 | -50.46453 | 2025-07-25 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa507b6c-0b77-39b6-8bc2-68996044c863 | -7.92549 | -44.09409 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c9b755e8-d182-3569-98ac-609b4e0abcae | -12.43104 | -45.38298 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7cda74b-7799-330e-8680-238705fa7565 | -7.26424 | -43.073 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 843b518f-273f-35cc-8815-e2a0685efd5c | -7.11249 | -47.84509 | 2025-07-25 03:55:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 56811dea-471c-3ee6-806b-2c145a425309 | -8.51035 | -43.31084 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| b78d9b91-2b17-306e-acfa-abc6179e7c8e | -6.82805 | -43.05592 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f4e3728-2f79-307b-9934-89cdbe2e0e3b | -6.98846 | -43.32643 | 2025-07-25 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ceb370aa-5fc0-3a46-9602-9695ccfa48a7 | -6.93914 | -42.80569 | 2025-07-25 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 69ab1f20-04b2-30d1-ac94-95c76b82785f | -11.46391 | -45.11922 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 4f1c989f-58d4-324c-91dc-065d8947bc39 | -11.45029 | -45.1244 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8ab635e8-61c1-3821-bcbf-d0b3a01ff425 | -10.42783 | -47.19308 | 2025-07-25 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea83c58e-e0b6-3177-bf12-30058d9d241f | -7.90586 | -44.08618 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d9114e70-1caa-3fbd-b342-790c7df94334 | -7.46331 | -49.40199 | 2025-07-25 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bf7c4c7e-235f-30b1-8a04-c5ad4d06222f | -8.3676 | -51.07771 | 2025-07-25 03:55:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 392dfcd3-2346-34aa-b665-0761577357d8 | -6.89959 | -44.08162 | 2025-07-25 03:55:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6dc09e6b-465a-32e9-99f1-9da56b639167 | -11.45572 | -45.11765 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1edee91-fb6f-3e8c-992b-538d2884e0ac | -9.00954 | -45.33788 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7688297-d51a-347c-a186-6be5dde01ebc | -7.92204 | -44.08978 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 38ce861e-3d88-381c-bab7-d1600440483b | -6.95387 | -44.55867 | 2025-07-25 03:55:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 7fd3a6a4-6177-3971-ba04-2028b7013148 | -8.13573 | -49.59026 | 2025-07-25 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9ccde19-1cda-36b3-9e52-26497348873d | -7.88092 | -45.53433 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80916d8d-7960-35d6-811c-16fabc3cec07 | -7.90932 | -44.09051 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 16490c9d-2be2-3502-bc72-466b3012c3ff | -8.09384 | -43.15242 | 2025-07-25 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 23e9bb9b-6e25-3a60-b5c9-a0bcb438de77 | -11.44552 | -45.1274 | 2025-07-25 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dea9bcb8-56d1-38da-9199-5c5b027c9217 | -7.92327 | -44.08267 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90ca1adf-af70-33cb-9ee4-af2da0b61448 | -8.32961 | -44.95088 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44c5c0c2-51c8-3f70-9879-506b5070ae6f | -7.91109 | -44.08054 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0292be37-ac6e-3cba-aead-6fc6d8dcba60 | -12.25712 | -44.78201 | 2025-07-25 03:55:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02449645-3af5-3c4e-897f-c7ff3e57acf3 | -8.2026 | -44.93809 | 2025-07-25 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6724d5d-73e6-3cdb-add9-60fde9efef4e | -10.74533 | -48.18834 | 2025-07-25 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5b3fea15-3f0d-3bfb-aac5-5b888480a8d7 | -7.8858 | -45.54693 | 2025-07-25 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c76a0932-ba85-3d21-9d2d-6fd07adbbb7f | -8.79077 | -36.97989 | 2025-07-25 03:55:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cde29a47-1641-3d0b-94a4-8692ae04fd35 | -9.43101 | -44.73727 | 2025-07-25 03:55:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16e536b1-13f9-30ab-99b7-115e605cd8a3 | -9.0507 | -46.62207 | 2025-07-25 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f233179-6329-35bf-9459-f50ac2c81180 | -7.53608 | -42.42377 | 2025-07-25 03:55:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 041116a1-6086-3f37-a5b9-8b737b855f10 | -7.92081 | -44.09698 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ea3856b-9ef2-3e2a-80c0-b253721eb1ea | -7.25348 | -43.06632 | 2025-07-25 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 2ac12d26-02b5-3154-9ebe-884d3df76996 | -7.30195 | -44.02237 | 2025-07-25 03:55:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9deedf1e-a76b-3e7d-a9f0-20b2b124bc7a | -5.99246 | -45.72782 | 2025-07-25 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53046626-4b6c-3f2d-9e3a-c4c06f41ed02 | -7.91674 | -44.09629 | 2025-07-25 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README7.md)
