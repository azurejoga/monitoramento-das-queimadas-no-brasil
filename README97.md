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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604d5731-ee3c-396c-8afc-11ee34549480 | -11.34253 | -48.38231 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b7b23e89-114a-3316-aa3e-e8bc2d46e004 | -11.84358 | -47.22375 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| af9262d5-ba54-32b4-8e75-e0a091e3742d | -1.69027 | -47.42096 | 2026-08-28 16:07:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b74f4c79-e87e-39ae-a19b-f0ec9e4f7345 | -12.31719 | -50.58244 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c93098cf-14e4-3027-afbe-e0d27a4b543e | -2.45888 | -48.42111 | 2026-08-28 16:07:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57a0626b-c17f-3552-9dce-2402918d4b85 | -12.31791 | -50.5895 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 016a24d9-ed35-3524-ad3d-4c9194a235fc | -11.2531 | -45.05084 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 36a31d5a-a6d5-3f0e-bf9b-a3e37c47ee4d | -10.06686 | -46.95501 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 21ff0b10-c456-310b-b325-e5cc5de51bac | -11.60604 | -50.19415 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5f9027d6-04ef-3e56-97a8-69888fd1f5f0 | -10.76163 | -50.64325 | 2026-08-28 16:07:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 55249947-b0a2-3716-a99f-3b2af7534514 | -3.926 | -44.89422 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5f6d2a0b-0744-3a02-8289-32a1f7dc2f26 | -11.47955 | -46.95272 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db34a969-75d5-3a60-8eda-19e94fba1ddb | -12.08002 | -47.17239 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| e66ee4d3-fe6d-3366-b731-f5a760c5b8b3 | -12.3228 | -50.60012 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 5e499482-852b-3e68-90b8-526023c12328 | -10.56422 | -46.41492 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 59064915-bff5-3680-9d23-a0a3201249cb | -9.88802 | -46.35009 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8f81b15b-7a2a-3328-a3bf-184073f00bde | -12.33218 | -50.58793 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 02c891ae-8936-3dc9-82a0-8007e987af99 | -9.50096 | -45.65591 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| af438f87-2454-316d-bbe8-59dc786b508b | -11.84256 | -47.21548 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| cead9750-57c8-3141-8a09-a6545639d96a | -2.72835 | -47.04149 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| adab9819-71a6-310e-9cc1-9c7cea7570d7 | -2.81931 | -44.37747 | 2026-08-28 16:07:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cb285f0b-2ee7-31b9-8f14-8448377116f0 | -11.23175 | -45.04974 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f3ecbd8f-385f-3371-8dbc-2304116f7ca0 | -12.08531 | -47.16751 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 82386dcd-4559-38ec-be7d-0a2325903464 | -9.87828 | -45.85801 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 425d1d29-6661-373d-a0b7-446ff45aac86 | -10.9218 | -46.6214 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8c6f467d-3f54-3cd5-822c-0285a8ae5126 | -11.25375 | -45.06374 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 8898b69e-90b0-39a7-af76-732eabab8eff | -3.92617 | -44.89522 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 50c29619-bb66-374d-afbf-e97919ec4433 | -11.0747 | -47.11947 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fb38fced-b3f8-398d-8dec-56e19b4e8bc3 | -12.32213 | -50.56053 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0deaa8eb-2af6-351a-b7ad-99b6b3a1b033 | -6.41001 | -51.67402 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 393c5507-8a36-3ef6-a089-adb45f03f04b | -11.14932 | -45.56204 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 88ff930e-53f5-3203-bf5d-3c7aa004f328 | -11.14455 | -45.5655 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0db1af1f-ab40-3449-a8d5-81b03d9deb98 | -10.02769 | -45.82184 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1709367e-f1c9-32f6-a67c-8e7a325e5675 | -11.15712 | -45.5825 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 44caf03b-2cb6-3a94-94f7-74dd54cee92a | -10.08439 | -46.95993 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be994fcd-465a-3ed5-9f2d-d6c3bd84f4cb | -12.30853 | -50.60163 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 6690519f-cc35-3b42-9dda-48765b3a8537 | -10.07005 | -46.93589 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ead91fd-5f12-3392-8b36-d34bef78c0f1 | -10.90538 | -46.62374 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6bbae222-d774-3545-ad22-3117b47f4ba8 | -2.72781 | -47.03735 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f98f36ff-808c-3764-9d68-95a242a4f7e3 | -4.36708 | -44.35435 | 2026-08-28 16:07:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 44e123fb-6219-31cf-98b2-89c3c5fe22c9 | -11.77901 | -47.62985 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| ade479f2-ebca-3d7f-bcb8-517ecd3afacb | -10.8916 | -50.50325 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e6986e59-f0d4-3861-9560-0ea976a4377c | -3.70553 | -45.25851 | 2026-08-28 16:07:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5196967d-ec9d-34f9-96fa-f265ca6c9baf | -9.86643 | -45.84687 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cf580b5e-2871-3c24-8fcb-1b52571d7eb4 | -1.93167 | -48.70467 | 2026-08-28 16:07:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dad28ab5-18ed-3663-b366-d3d8fe745109 | -4.37266 | -45.00368 | 2026-08-28 16:07:00 | NOAA-20 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd05f459-9c4b-3c10-acb3-a4538f21ff86 | -11.77853 | -47.62563 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 2a2cb1a0-c341-3415-bbf4-7abc349c1ffe | -9.43496 | -37.83626 | 2026-08-28 16:07:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 6.4 |
| eaaa7068-1144-3844-b525-e7fbb21d410b | -9.49431 | -37.00081 | 2026-08-28 16:07:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 57933417-81cf-3ec4-acdb-de5086052d2a | -5.34449 | -45.16036 | 2026-08-28 16:07:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 85db5121-94d7-3a35-8235-e6823ddaba7d | -1.96223 | -48.37414 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| f2767c0f-9e80-3dec-9e53-e3083a769fd5 | -1.84094 | -44.68781 | 2026-08-28 16:07:00 | NOAA-20 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 76ef68af-78ba-3fbe-b2af-da7e243a64b5 | -9.5017 | -45.66173 | 2026-08-28 16:07:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f5f90a4c-0220-3c54-aa2f-c9cee6ea9607 | -10.02688 | -45.81556 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ccc67d16-72d0-3449-bf56-1e5661651134 | -11.08278 | -47.11901 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9648c75a-c4f4-37c1-9ad3-982e5febf30e | -9.87078 | -45.84006 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 258b67e1-4ba7-36c0-a2ea-8f9fcaf70803 | -10.9012 | -46.62868 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 501cad20-6e9a-3413-a302-d5efaf8543ac | -10.33345 | -45.356 | 2026-08-28 16:07:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 783fd2c0-6933-3d86-b7a4-ebb4974443fd | -11.77456 | -47.64349 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c674ead4-7a0e-3635-b53d-d7a6cc5bb9a8 | -10.46934 | -46.18167 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f68be4c4-4721-3f41-9b41-41d048af70a3 | -11.14044 | -45.57432 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7973e831-8398-3aef-84a5-bcc4942394ea | -9.79148 | -43.55094 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 010b78fa-cbc2-3c83-afbb-4735e8eff0a6 | -11.54976 | -48.13232 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 59d3613d-a473-3417-9922-e6515c1541f2 | -10.00043 | -36.38614 | 2026-08-28 16:07:00 | NOAA-20 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 113fab91-b5ec-37bd-894a-e12b7ac3e272 | -10.56466 | -46.41835 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 81b54314-f9ce-3406-b130-05b7b30290d3 | -10.91772 | -46.63309 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| baa1541f-e2c1-3842-801b-24de983bdfc6 | -3.71985 | -38.85463 | 2026-08-28 16:07:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 4ba65a60-3c6a-3179-97dc-6bc9dbb1eacd | -10.7978 | -39.37672 | 2026-08-28 16:07:00 | NOAA-20 | NORDESTINA | BAHIA | Brasil | 2922656 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d6d9c65f-38fc-3dd0-9522-fb7125d008f4 | -11.67049 | -46.73088 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 270f21f3-d40c-3056-b5a5-d311fc72f8ba | -11.7719 | -47.65129 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 397b68fc-ef35-3fd4-b954-234ae34f1945 | -10.92905 | -46.62854 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0cf35d2b-1e70-3d52-ac43-9cae994ff219 | -11.25006 | -45.03572 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 88fad3b6-8aa7-34e2-87f2-e24e1683025b | -11.14566 | -45.57434 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 690235c0-d6b8-3635-bd77-ba3e1b1fa790 | -11.25231 | -45.05275 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d2b294be-c0e6-35ee-a6d9-7e45deec3e21 | -12.3047 | -50.56642 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b30c8ef1-e61a-3f2b-b346-da9e5027703c | -11.24587 | -45.04211 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8b9cf824-cef3-33cd-9524-7e9934cc6017 | -1.78625 | -45.77655 | 2026-08-28 16:07:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 17.5 |
| be1df724-8fa1-31a0-880c-7ddd2d5e9dd2 | -9.88738 | -45.84744 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 96847b43-f28e-3c41-9dae-07ca76914fb0 | -12.06654 | -47.15724 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 6a4a76fc-5745-3b7f-9199-3e9ca931fa83 | -4.14811 | -38.68122 | 2026-08-28 16:07:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb45bddd-53be-305d-99a3-6152749176c3 | -11.24496 | -47.05528 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49d6039d-be7d-3d19-ae18-a9e336365c5d | -9.8771 | -45.84868 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 395470d8-ab90-3967-b47b-fc3ad8b40126 | -11.79671 | -47.65718 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ded64b54-fa95-32b8-bc79-2007cee87290 | -1.65349 | -48.0942 | 2026-08-28 16:07:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 23b6f6aa-43be-3c0f-b2df-c8cc905369a0 | -11.22113 | -45.04554 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 85bbffd2-dad2-3b4b-8167-779e76ddcd28 | -11.41366 | -42.30243 | 2026-08-28 16:07:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 9e5657ef-2f47-3dcf-9122-44d83801183b | -10.0873 | -46.98251 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f7028116-22d7-3b5c-a458-dae0e4598cd4 | -1.22848 | -46.55214 | 2026-08-28 16:07:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9af2ae2d-29c4-3c7b-849a-08d7261f5a31 | -3.02747 | -40.12978 | 2026-08-28 16:07:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 918f8430-1751-3e3e-9db3-d4685d4fc179 | -2.99617 | -48.9498 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e398ed62-3d44-3ed5-bd2b-6935a5101355 | -11.48438 | -45.06906 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 97d7d1af-fa25-377f-b532-0db82827b6e8 | -9.79757 | -43.5631 | 2026-08-28 16:07:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 4c731b0e-6d74-3037-b0dc-baafd47b227c | -10.01831 | -46.40705 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06e03533-4bd0-3448-827d-2ea12e9e4018 | -3.2453 | -41.10632 | 2026-08-28 16:07:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7d744955-3500-3ebe-8f9d-07ba80b66ec5 | -3.21212 | -39.86936 | 2026-08-28 16:07:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 124006a2-087e-3183-8c9a-79b13929cd44 | -4.91706 | -43.46808 | 2026-08-28 16:07:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 393b8ecc-e70d-3e5b-a6f9-c9a2371fcc9e | -0.99692 | -48.08358 | 2026-08-28 16:07:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dcc2117-8cb2-3433-88c3-ca7943f33c0c | -1.58428 | -47.74134 | 2026-08-28 16:07:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 49f53a64-44bc-388c-92e2-7419fec95d65 | -10.90927 | -46.64948 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 964e7379-97a5-393f-9151-aed57ca1bdda | -10.56707 | -46.41756 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |


[Clique aqui para ver as próximas entradas](README98.md)
