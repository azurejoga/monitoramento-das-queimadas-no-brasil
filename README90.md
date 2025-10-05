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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2eecd737-f3a2-3a9f-8c3c-a283ba344c9f | -12.59129 | -48.12587 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee6ee869-1fd6-374b-aa27-dedfe7ada6c2 | -13.49399 | -47.27679 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d8e0f18c-80c3-3032-831b-c7075eecf15e | -13.09646 | -47.92446 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 85265444-1d79-3c25-9d13-4bdb81e6bb67 | -9.31239 | -45.66473 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 525cc185-d978-3165-9400-7e4a71b52ad6 | -10.39783 | -45.40555 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b73bd5bc-2a1d-36e3-a372-fe78004698a3 | -10.62236 | -48.67242 | 2025-10-05 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86eed0b4-d1b3-37e9-a52b-d7a1b3c00bf5 | -7.69778 | -42.59155 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4c973d4c-8f0d-3b63-ac92-d24204a7e3e1 | -12.81538 | -46.8549 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a7c0c29-64c0-32d7-b5c7-791d84608c8d | -12.08574 | -45.15114 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb8d03ea-3a5d-36de-8e8e-1370961e2c83 | -8.59308 | -46.30236 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6c2a08ce-bca4-3011-ab88-37190c44144e | -11.83379 | -45.08086 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fb135827-ed81-3ff6-95c4-311a14e75ffe | -7.72621 | -46.31441 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 01eea088-2f77-3e75-aa4e-fe5036f02a93 | -12.31129 | -45.35975 | 2025-10-05 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a5c8df1-f57e-375a-b03d-c6104ac2d227 | -11.88015 | -44.96667 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40b2e0bb-5029-3453-9821-fa739e397492 | -13.25531 | -47.23371 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6909f4da-4dbf-39cc-894a-eeef1cf2aafb | -12.60802 | -48.1185 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3fe78555-bc04-3a0b-94d7-c445930bbd53 | -11.8354 | -44.92472 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4a0355a-c2c5-3402-9e47-824592c9481b | -6.59599 | -44.3188 | 2025-10-05 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3cd4997d-9caf-3b12-9aa0-93d9cb8807ab | -12.31308 | -55.15852 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6eb0d160-6a33-3104-bef3-5b6f9f5a9b38 | -13.525 | -47.29509 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 597f7e49-f648-3061-9be1-a641a865919f | -13.30204 | -47.79914 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ef9cfb4-2a65-30e5-8fce-a2284f4e43d3 | -13.3186 | -48.08521 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 284f42b3-0752-3ffa-9994-4b93393d4604 | -11.90337 | -55.88425 | 2025-10-05 04:46:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 845bb418-7e09-329e-850b-dff570f187ee | -9.94176 | -48.77793 | 2025-10-05 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93336c43-f1bf-3708-9f12-94d43a4ac545 | -11.78752 | -47.9235 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2a0799c-57a0-3ce5-9f1c-ecd316470eaa | -10.7178 | -44.1744 | 2025-10-05 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855c9090-d5eb-3d9c-9e14-97156164b421 | -11.5298 | -47.66925 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15cb20c1-6c52-3073-a121-1b12fa24414e | -8.14576 | -44.08398 | 2025-10-05 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 207196c8-cc33-36fb-bbb3-f0a48e5659b3 | -11.78367 | -47.92291 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef29ccce-dd3a-3001-9055-dd2daf3ca647 | -10.94712 | -47.07356 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 20f16366-aaa2-38eb-911e-66bf01b62e5a | -6.55159 | -45.80288 | 2025-10-05 04:46:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c52a1113-d74a-399a-8304-efd10ec29165 | -12.94037 | -51.01021 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9a2c9306-86fa-32ba-8c39-4a5348858777 | -9.17426 | -46.19312 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83127b9a-1044-31ec-af46-94f0d5aac4c9 | -13.1069 | -47.93578 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 10e66b14-b0a2-38f9-8f85-d8d52bfb811c | -10.18418 | -58.17955 | 2025-10-05 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb1e6b05-8c19-390d-93f1-9f37a15ba8a9 | -13.52637 | -47.28484 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb711ef1-0186-3866-b5a6-c0e7bda2c10f | -13.43268 | -47.27143 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b07916f-2a27-3f8b-9d5e-229557dcdded | -12.57144 | -54.77666 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f51ac5fe-cdec-34f7-b34a-2df97effc7db | -10.65726 | -58.75622 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ffacb54-0047-33e5-b038-7c25f3ad03cb | -8.94305 | -48.63694 | 2025-10-05 04:46:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d11c249c-6f84-35cc-88b2-2de3ca14af0e | -10.75753 | -45.33428 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2467e934-f841-30db-8173-8b6d4655ba9e | -12.61187 | -48.11908 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bb3e03b-e4ca-3af7-82e5-ed3e79d99fdb | -11.80525 | -46.8447 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 272d07ba-aae1-31e8-a2aa-034f739d602b | -9.16725 | -62.22696 | 2025-10-05 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a939864-f215-340c-a84d-6ecf4a913880 | -9.17476 | -46.18955 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa621b7a-af3b-349c-8f4d-a8f8827b8f7e | -10.85064 | -47.19556 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9cf9eb76-f6c5-36b8-8a2d-70a48be6b205 | -7.05593 | -42.7704 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d4d34aa3-c951-3187-86e1-397315785401 | -11.83116 | -45.065 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e2d8d1bd-905a-337d-8c9f-a9dc5dd30bd4 | -10.83795 | -57.17706 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c57cc869-51ae-38e1-86be-8511b66d403e | -12.31796 | -55.15103 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 125af4e5-47d3-3d19-a8f6-11da3d83a899 | -11.71319 | -45.3524 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5a426add-6c96-3c8d-b5a4-7594d6a21665 | -13.31998 | -48.07513 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| def35898-92e2-3312-8dc9-9782a193b575 | -13.71737 | -47.34571 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a98198c5-982a-348a-b864-467c82980822 | -9.61556 | -50.54683 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed423047-e3a0-3e99-abfb-70efd10522b1 | -13.34884 | -47.59163 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d121ba61-fa1a-3b56-a10b-f7b304079d1d | -7.24888 | -44.88593 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfec5701-1d7f-36aa-b9a8-2f32b30bf5fc | -11.30012 | -48.61192 | 2025-10-05 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 10f992a5-689d-3eed-bae0-87eb0859c9e0 | -9.25825 | -46.78062 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e01c78b2-1977-37a9-a48b-72a5aaeadd0c | -7.73075 | -46.3114 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4278ce26-8df0-319a-afaa-09aaef36421f | -7.758 | -46.32204 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f120d130-7076-3f03-876b-6dff8d328bf9 | -12.46702 | -45.5301 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a09f3b16-2d02-3911-83d2-e93bad25aec9 | -9.56946 | -46.12187 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a42904af-5f2e-3fa0-b234-ac515e4a9047 | -5.60067 | -51.14315 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b25a5960-e87a-378d-ada6-4a7afcad7845 | -7.87543 | -45.22813 | 2025-10-05 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e941938-c2df-3788-8c91-bdffcd38d5c2 | -8.479 | -45.91102 | 2025-10-05 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ace2e408-c48d-3eb7-8b3d-02d8548d25c4 | -13.09525 | -47.84631 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 797c2252-3fe7-3434-a953-95c894445ff7 | -7.78859 | -44.12452 | 2025-10-05 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f1228f0-4529-3525-8516-248c0fa7266d | -8.6038 | -46.28548 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f51019ee-c344-3707-b936-7cab3549e49d | -13.68002 | -47.72097 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c43c9bde-a3a3-3299-a4f3-74b6b900df9f | -11.81905 | -48.87664 | 2025-10-05 04:46:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f819df21-ec45-3b77-9ccb-8bd2e2f30106 | -9.33798 | -45.76466 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6090670-5157-3215-972b-dcde7defc449 | -11.81444 | -45.08411 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b15d2bc-5172-37a3-a442-0cc855d51fe3 | -10.39724 | -45.41007 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3b3b58d-7be4-360a-a459-ccfe859af59f | -11.54279 | -49.80537 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc0713e7-79d1-3dd4-be64-efc078333bd8 | -8.62888 | -54.99434 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 566ae6a2-802a-3cc2-83f3-236b3dda95e0 | -7.77351 | -42.6182 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c55c1541-f3bb-3fce-805e-7754c40fef87 | -13.31758 | -47.62841 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a53daa7d-75b4-3fee-8e94-1667ad3da0a3 | -8.57777 | -46.32243 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1dfbc1b1-0b4e-3d7e-b56e-135b5cb0480a | -13.08291 | -47.90542 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f2b6a50-8d29-3c36-9a16-f6ebadb9de40 | -6.70952 | -42.8338 | 2025-10-05 04:46:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2af6a51f-f34a-37f1-af5c-3172be7714f7 | -9.31326 | -54.53485 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9466e15a-65a6-3c79-a93f-0c457ea6f87a | -7.51073 | -41.27582 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| eb0349cb-0c73-36e2-b0c4-c1dc55d8700a | -11.53232 | -54.50969 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d95ba3-8fdd-3238-90c1-48f80a52ec1f | -12.24202 | -47.84946 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5a76814-2dc6-3501-a3dc-194e23cf8630 | -8.55084 | -46.30784 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 25545c04-1505-3816-bcf4-b4a5e99c2a06 | -13.14699 | -50.92083 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84284a2c-6eb3-3c9b-a80d-35c55e157311 | -11.01658 | -46.68599 | 2025-10-05 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb5a4576-bb77-3b5d-a79d-16135c85a3ef | -7.19179 | -42.9355 | 2025-10-05 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3a0692e0-30c9-3019-9b47-f8a71cf1aec4 | -7.43205 | -46.49702 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 785979cd-2081-3f02-8f6b-d84377d5470a | -13.54425 | -47.24474 | 2025-10-05 04:46:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d8913bfb-92da-345c-991c-d086cab3a7d6 | -12.5969 | -48.14168 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd1ab41d-fa0f-3fee-b748-039b6c9ea568 | -10.68702 | -49.27405 | 2025-10-05 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e8979e7-3a17-379f-80bf-229f403da3ca | -9.26781 | -46.29508 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ea0e36b-bc7f-38d9-af15-b51258b35cc3 | -11.9552 | -51.47444 | 2025-10-05 04:46:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 729989da-b051-3079-8b9b-6cca7af85964 | -9.89494 | -43.70557 | 2025-10-05 04:46:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3763635-1dac-340a-9adc-37bb260583fa | -12.39093 | -51.09374 | 2025-10-05 04:46:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdc1327e-e3bd-3332-9c8c-a088fbf2d99c | -10.99966 | -57.06062 | 2025-10-05 04:46:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b424774-9735-35bc-bf27-accca65a238a | -7.25268 | -44.8909 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0d12ed7-37c3-38b5-8d58-7e44e6630a00 | -7.7749 | -42.61811 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c18785b-bde3-3cc5-b562-ed351e2ad126 | -9.78652 | -46.77026 | 2025-10-05 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README91.md)
