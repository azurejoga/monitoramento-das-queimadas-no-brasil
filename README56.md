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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 032ef6d2-789f-3dc7-8f88-20010b764592 | -12.85652 | -46.98381 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 65b56228-f6da-3117-aa42-7f24f1e872bf | -14.04379 | -44.95849 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5f5813e-1f93-3cdd-85bd-92db4019c1fd | -8.53884 | -44.63952 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed111536-0748-3789-b885-95afc6a78d88 | -8.2411 | -45.52052 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 430c37ab-9b1f-3bbe-b242-7af3c3b349cd | -11.45369 | -51.50431 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b7c4792-f2ca-3850-93a2-5249800e141c | -9.42254 | -54.71438 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71539235-75df-3cc4-9b79-5eb885a73be9 | -11.63972 | -46.8402 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad23e620-ae2e-3143-99f2-284f50458e7c | -11.88734 | -49.9065 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96d318e5-e4a6-3543-aa88-7140434ab9f9 | -13.59888 | -48.04062 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 048eb125-d556-3f0b-b7ea-76bd3c0132d9 | -14.38467 | -47.14004 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f57b9dc-506f-34ea-b386-71a438f352ae | -7.79268 | -55.0289 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c98ec152-1911-3b73-bd3f-be418068af91 | -11.06211 | -47.82792 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 89ddae38-c54c-3b0c-8461-737d74f8b26d | -13.6073 | -48.03307 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a26ddd4-8a40-33d3-a500-d5d9d2c90672 | -13.37009 | -47.31573 | 2025-09-30 04:40:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1cea7776-7aa3-3e02-9248-6aedd3696f27 | -8.25141 | -45.54514 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| da6a2979-0040-37fa-a01f-11db33067d39 | -11.46176 | -45.00256 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5123b2a3-c235-37cd-bcad-4bcd5222bb98 | -13.62696 | -42.53574 | 2025-09-30 04:40:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 20b8d537-7b37-31b0-9e05-e7742d854460 | -7.4793 | -47.26243 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd20526d-ca80-3559-b8f8-7b4a480196a9 | -13.81007 | -47.48112 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 075bbb8f-38f1-392e-a3dc-db955a8cc024 | -11.21458 | -47.20498 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a40e408-47ff-3b35-bd01-e545e74bfecc | -7.82076 | -46.98744 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbafb96f-d666-38fe-9093-ba365763858d | -10.53461 | -43.63935 | 2025-09-30 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9635ead8-e4fc-33c8-b71f-c66b9ebe0e59 | -13.64478 | -48.04143 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c321fb8a-e16a-35b2-9ea3-b8e94a4135af | -11.65293 | -47.48923 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e43801c-e999-3474-a9dd-22cbec8cc75a | -8.24987 | -45.54222 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 43cfaa31-535c-30c6-88ca-c0f808d1d756 | -11.91102 | -48.0587 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e000b98b-c319-3de8-9407-c0ab4c908419 | -13.79891 | -47.87494 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 75bfac29-6949-39e7-aa9a-ca74e498cb7f | -11.15645 | -54.1198 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0af320cb-0c45-3d17-b0cb-451a0e48ace7 | -11.21822 | -47.20555 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bfed3764-b19a-3745-b1d4-99aea8242d59 | -13.81386 | -47.95162 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 84e2f83a-17f2-3bc6-a48a-76e63963aa63 | -8.67027 | -47.7167 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4883e1a-1b74-3407-bd58-f32f2db83a70 | -13.65132 | -47.32922 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a356959c-63ca-3e9d-b049-a42d755b71e4 | -10.14198 | -45.30441 | 2025-09-30 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 923a429f-8e5c-3ea9-8fd9-48f9960d28af | -11.30381 | -53.96091 | 2025-09-30 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 610004a1-51e3-3900-a9b9-0fd55574c907 | -11.39534 | -55.08717 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73dd70eb-a72c-31eb-a0ae-6bb49d82a7da | -9.51831 | -47.69247 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca0ee766-47b8-33ce-b955-e6145aede98f | -7.83141 | -46.98896 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd73e941-46f7-37e6-9cfc-acf6cb2efd70 | -10.63078 | -53.6894 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 90f25e89-941a-3d11-8cc9-9fbf5b6b1a8d | -13.20501 | -50.93177 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 816dd4c1-3d28-3a0a-b519-7fdcf0bbe441 | -7.20236 | -48.59843 | 2025-09-30 04:40:00 | NOAA-21 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba7f9c2a-a767-3bf6-b812-025028f115f4 | -12.1702 | -47.73975 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 040fcd2b-ceb2-332a-9a25-63a6a3a05e3e | -14.00594 | -49.62797 | 2025-09-30 04:40:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e8af4d4a-aecf-37c5-a798-9881ba97c411 | -7.21209 | -45.47261 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11634d4a-557b-3cad-8eab-dd27adbc6516 | -8.33016 | -46.21611 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3eaa98ef-6637-31ef-b8ca-e1550936dda1 | -11.45968 | -45.00772 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3ddacda8-2b71-3eaa-b089-01636b359f26 | -9.42083 | -54.72428 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc5e2ef8-a7ad-392b-89d0-d014190c0418 | -13.20831 | -50.93231 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a7eac64-fa4d-3f98-9540-1ca7ec92c278 | -8.77001 | -50.58858 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50e20173-83bc-3fe7-95b0-ab72a25016fe | -12.84948 | -47.00668 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| d36b71ef-c030-3ca2-a722-0ce524fc8946 | -12.58841 | -41.2898 | 2025-09-30 04:40:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 563d671d-3736-3bc9-9b57-308f13d74e8e | -10.38206 | -49.54584 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56928769-3937-3549-862a-89cb11981c6c | -11.65781 | -47.48079 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8e64a46-b9dd-358a-90f4-d6a5823bd79f | -7.56148 | -42.41433 | 2025-09-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7b203e66-7c35-3d39-b378-9032e4feb04e | -9.74252 | -47.78909 | 2025-09-30 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d947875-8a52-39bc-a049-8b436345d7d6 | -9.95878 | -48.79824 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a81a013c-5cee-3773-b223-abb481b48510 | -13.21555 | -47.3218 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b77f02c7-9424-3bd5-b3ab-188794042b96 | -10.07019 | -50.22069 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 80e3d3f7-79ed-308d-9ed9-b169cb4e2018 | -7.21518 | -44.75972 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb3601c9-9071-34df-8fa4-1811c25b7801 | -11.71461 | -44.47274 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d541421-3afe-3fa7-b1c1-d21b3d0d353b | -8.85548 | -46.58487 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8677ad6c-f069-3f0b-a517-0bbf9287506d | -10.88495 | -53.7385 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcf92455-1f57-33d7-b9ad-8bf0cf0780cb | -13.40424 | -47.54818 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72044406-5b91-36a0-9ed7-52fb13568483 | -11.88695 | -48.02343 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91fd89b8-4e4f-3f6d-bdc8-2652b7e8b3f6 | -10.65306 | -48.5404 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 74d91bf5-3795-38a2-82bd-dd52d149d045 | -7.11206 | -45.5478 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 91c67af9-b9df-35c1-acc6-f667929f2e21 | -13.57859 | -48.05428 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff5dfd52-811b-3870-913d-843d4969e8a5 | -9.1289 | -47.63976 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bef6bfd3-ca52-365e-a42a-fd69779350da | -10.85188 | -47.95384 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 47b25eef-3b88-3fea-8296-ef5937ddef10 | -8.1388 | -46.39635 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7189ab4f-9b0d-3202-bd86-05dd2f098462 | -13.22262 | -50.9274 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e11c500-23c6-37ae-a34e-b3d659b8e884 | -9.08307 | -47.6258 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a1d3d51-73fb-3760-8ef2-56113a246b58 | -13.02878 | -42.80808 | 2025-09-30 04:40:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 1fad6b32-cf8e-3e85-a369-8677fc6c4479 | -13.35277 | -47.80856 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc72d2b5-dc30-33b8-b806-21c943c95e28 | -13.20171 | -50.93124 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 992fb850-98c3-36d8-ab83-dfe3726487c3 | -10.40059 | -49.04813 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c41508dd-0db3-3e1b-beb7-e7ae63f88e5c | -12.02895 | -47.89333 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 022bdf9a-05a6-3f90-9d5f-f8a55a959288 | -13.80941 | -47.4857 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f958e13b-9004-3d2c-854f-7e9de4aa0f0a | -13.22867 | -50.932 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| cfc7b2be-53ef-3661-bbd5-6f1aeaee699d | -13.61086 | -48.03376 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 57bc4946-ac2c-3ed8-aab1-ea7466112f61 | -9.42858 | -54.7256 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e655dbb8-52a0-3fde-9dfb-ebcfb16c4e22 | -8.83271 | -50.66702 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c346f62a-67f9-33be-8a79-19777d61006f | -11.25078 | -47.23711 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f1928d58-6d9b-3bf1-89e8-3ea3c6b77e9c | -7.91545 | -44.60686 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| caa99e3e-c1ea-3c65-a4e0-d14414812c5d | -13.36359 | -47.91401 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2dae8609-6d62-346c-9804-c872560e8ba2 | -6.75347 | -50.92165 | 2025-09-30 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4407073-deba-3665-8a8d-5a56a97ee386 | -11.20239 | -47.2121 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8fb92c03-a07e-3401-9c23-337b816e602b | -10.29984 | -54.1379 | 2025-09-30 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c13396f1-d7cf-3186-8d6b-d0fd79acf2b2 | -13.72475 | -48.64162 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dc09ada-20a4-3519-9851-fa038afc1ba0 | -12.75679 | -46.86748 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5a020790-c098-39e6-9000-df52cab0edae | -7.82962 | -47.00109 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9b6e6a1b-2479-33ea-be19-61471ee10847 | -10.40435 | -48.16283 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36c51c6e-6a28-3cb0-81b8-a43669b2c832 | -13.79653 | -47.86562 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 558f02a7-6dba-3d77-9cdd-138cdda05986 | -7.7509 | -46.99454 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5fae9dd7-c3c7-363a-a319-ed7c8900c2eb | -8.25656 | -45.51054 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54968d08-f5ae-34c7-a897-a8b273fd211b | -9.4255 | -54.71191 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e0cb87c-d663-3bd7-b199-4d0657301fa4 | -9.30715 | -49.81044 | 2025-09-30 04:40:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f49ebc5f-fec7-3e34-86a0-c1ab5fde0e97 | -9.95535 | -51.37898 | 2025-09-30 04:40:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee04d9d5-406b-3448-a64c-1744c4e4a4b3 | -7.83376 | -46.99757 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b8d60d6f-cd06-3f5c-b872-51def09d7a49 | -10.63438 | -53.68999 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 386d7af8-5230-35c3-8f72-fe7201af3db2 | -11.89047 | -48.02397 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README57.md)
