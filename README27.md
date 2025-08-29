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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 100e80b3-e5b7-342b-ae18-b7aac8e503d8 | -8.46078 | -43.64765 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c377539d-8058-3f13-b102-8e230fc6e984 | -9.84181 | -44.68161 | 2025-08-29 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c23bf9e0-80a2-35df-9328-76e3b7a61c4f | -6.72606 | -43.57933 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 71dfb02b-3114-308e-ba0a-7e9f6aae0b97 | -9.82202 | -44.89943 | 2025-08-29 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54d39d83-700e-31ff-b36f-2b226e9d9d7b | -9.4928 | -45.38908 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3bd97bb-3edd-33dd-a611-bc65cecd3eef | -9.51941 | -46.545 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5527893-7447-3433-9954-16877f251cc2 | -8.44612 | -43.65378 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89dabb36-bbe2-3a26-9400-c68b0919f956 | -7.21564 | -45.44739 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee810e68-2866-3e11-bdf7-7029b6063047 | -6.72681 | -43.57486 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bc7afb42-0f5a-398b-b5fd-edefa4233460 | -9.49379 | -45.38358 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c0f71ed-f22d-3b9d-bd2c-1c955b213972 | -8.44481 | -43.71202 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3e4e3ca-babd-364b-9cec-b6196932b60e | -9.43489 | -47.64911 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a8f92667-fc3a-3ef9-b4b4-a496e6064785 | -3.97381 | -43.24382 | 2025-08-29 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c97b4042-3444-31be-b25d-95e4d277dfed | -6.45098 | -44.56257 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c6805470-efe9-3f76-b868-7c9ae97003ef | -9.6898 | -47.06594 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81c2f4b4-664a-3a4f-be42-bb2bf5f395dc | -7.16146 | -44.1485 | 2025-08-29 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc651062-cec4-3375-87b1-9004d7b98545 | -8.08251 | -45.02363 | 2025-08-29 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6162d36a-6310-336d-880e-0ee9a6f0e1f6 | -8.45111 | -43.65213 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 714fecc2-801d-3f5b-b462-931ae8de0fef | -9.55387 | -45.84801 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a60bd927-d11a-3231-8f3f-bee50ea51040 | -7.22082 | -45.44761 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5acd45e-6dec-3fce-92c7-7472b9c08d15 | -5.47417 | -41.41444 | 2025-08-29 03:49:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c70904ce-27a4-3c7e-a4a5-7d799af1854e | -10.95021 | -46.87727 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28dc17c9-d318-3b5c-bfd9-23d424102358 | -11.28019 | -43.30789 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1d60b20e-3298-32d4-a9ef-b8baba77ca35 | -13.33071 | -40.34497 | 2025-08-29 03:49:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cbf3fafb-61ae-3459-a812-a1bff32cd9f4 | -17.54165 | -46.61144 | 2025-08-29 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccd1d642-4f23-3516-aaf8-330f462172d7 | -3.41892 | -49.05512 | 2025-08-29 03:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| e3d5ed4d-370f-3f82-a64f-984dc038e994 | -6.16821 | -44.18016 | 2025-08-29 03:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c34ccb87-2034-37bc-b0fe-74f5a9c01d2d | -11.50262 | -41.52286 | 2025-08-29 03:49:00 | NOAA-20 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| fd199b48-6bc8-3f35-8956-d563966d19f3 | -6.22698 | -42.75459 | 2025-08-29 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b64b398-8101-3750-a9f5-68e5a3ee391c | -12.8326 | -48.10596 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1273ee9-8cac-30df-b811-ee80af2f1663 | -11.34754 | -43.566 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 30db72b1-f773-383c-8922-dc49d75a82d2 | -17.04575 | -45.8846 | 2025-08-29 03:49:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b177e0a-6141-323f-8b4d-974206d3784a | -6.37412 | -44.32904 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca07658b-c2b8-3da3-8a9b-e68a298f948f | -11.3226 | -43.5615 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5ead359-05b1-3cc9-b0df-58a167299013 | -12.84892 | -48.13977 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f72f04cb-7ab4-322e-9db1-bcfd31f343e2 | -11.64202 | -46.38181 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2336930a-b41b-3493-9cc2-165d0b235546 | -13.33133 | -40.34119 | 2025-08-29 03:49:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 71efc4e8-8456-3bc3-bc03-59693606dff7 | -13.19174 | -45.28441 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d1c0fd10-b960-3897-8160-bedaeb850874 | -11.29071 | -43.54794 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef0e57f8-ef03-3cdc-8e9c-bc376b892dad | -6.44474 | -44.57708 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50b713e1-5db2-3686-bec7-33ab8b97880f | -13.40423 | -46.9976 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bf9f70f2-f1c4-378b-88d1-82ea7954373c | -12.91003 | -48.11779 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2cfe7bb5-b080-3463-ac1d-36ec79fd573e | -11.3192 | -43.58056 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 083e4133-1966-3c76-bd10-a7f4f86de989 | -11.56558 | -46.37622 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14ff1624-690d-392a-a6b7-7cc0db1533df | -13.44383 | -46.95444 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 796c9aae-c847-3a8e-917f-8297e5ed3fb5 | -12.70289 | -48.15783 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 844ed02f-2b91-3c33-b17b-271f24cae58e | -13.55987 | -46.91459 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24103660-3273-3c0a-b191-8938f81cb466 | -10.82665 | -47.49874 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fdcec77-06ae-35d9-b186-ffa983323ef6 | -6.54591 | -43.92225 | 2025-08-29 03:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 037261d4-2409-3f86-a441-b9c498da8503 | -13.18811 | -45.27888 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e9ec7bb9-3a37-3d20-91ea-6a1a6c739b1b | -13.54447 | -46.94078 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e56aff8b-6de8-351f-ada8-f64a5261a26a | -17.04092 | -46.50876 | 2025-08-29 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77275cb5-303d-3f7d-83c9-e3716ffbafdd | -17.85625 | -41.54089 | 2025-08-29 03:49:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1f074595-6989-3515-bc69-00d40e5f5210 | -13.54579 | -46.88022 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5bc564fc-68ba-350c-86d8-71c1faf84ed0 | -12.06442 | -46.63101 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfd464be-3dd6-3e9c-b1de-18b81dde53cb | -11.07465 | -44.75444 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b310bee-08f7-3f46-9953-813d1ea3cb69 | -11.03639 | -45.14165 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ddb05f1-d597-3c15-84e8-781a50751b69 | -12.80795 | -48.1737 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f921de7-dd78-3163-ac1e-bca515e3db60 | -12.69649 | -48.16183 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89cedf2c-2888-3c10-ba90-e53c80fae997 | -5.62088 | -45.00377 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ed88784f-778f-3bdb-bd77-af2a5e6032eb | -11.53879 | -47.3134 | 2025-08-29 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2e8f225-a647-39e1-8394-b38afd3a9f5f | -5.5943 | -45.52 | 2025-08-29 03:49:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb40e460-f698-3d2b-ac6f-38a8ed99bf86 | -12.85132 | -48.09911 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8f3fe4b4-9e17-380d-8450-6b3033df1383 | -11.6365 | -46.38379 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1456fef0-8ace-3fc5-b209-69dd371ee203 | -12.70422 | -48.15122 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c5238dc6-9088-3660-9d8f-cad65e313fde | -13.90141 | -43.87911 | 2025-08-29 03:49:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54209cda-85d8-33a9-9199-8d89a3ea5637 | -5.90277 | -37.82041 | 2025-08-29 03:49:00 | NOAA-20 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 44dcc263-563d-3979-8947-ffb7c990ca42 | -5.98533 | -43.33979 | 2025-08-29 03:49:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a98d147-7359-3e49-81e9-3bb32ccbf00d | -13.41321 | -46.84423 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88cd70c5-e44d-3b85-8734-532758ad44ca | -11.33433 | -43.28756 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3c975c1e-39b4-33e5-966d-3c3f49c03003 | -13.6659 | -46.87422 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07c579c2-3c15-3349-8b16-ad7cd1bdfb18 | -12.83847 | -48.10661 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00749a1c-dd0a-3ccc-bd52-831e1160422d | -11.06249 | -44.76435 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7f6101c-0799-3b9d-bb95-cf3e895d8030 | -12.6866 | -48.18339 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d5aa2ed4-2842-30f6-8cef-18485357c309 | -11.55876 | -46.35767 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97e8e62b-46ed-345d-b800-2b9da160b94c | -11.92733 | -46.69925 | 2025-08-29 03:49:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fddd4ea4-84c6-3be0-aa97-bc3ec7efea65 | -5.6137 | -45.01496 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4e7b665-7085-35e8-8e9e-6d99e90e0383 | -11.08369 | -44.75611 | 2025-08-29 03:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 786a902e-378a-3ae7-a2b5-8edd1bf4e7d8 | -13.67297 | -46.91805 | 2025-08-29 03:49:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f43c603-9ab1-3fe2-a4b6-72c4f30f27fe | -13.55032 | -46.93734 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5d915c24-d623-30f5-b3c5-e12f0402dc76 | -13.43275 | -46.9579 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5f1b5376-c544-3566-9f45-98852d4f8dc0 | -4.49176 | -47.68489 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e09273b-fe08-3205-9287-5895779c3f81 | -13.58393 | -46.86987 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1356cc07-e48d-3605-861e-9480a28e434e | -13.37107 | -46.87564 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb701bab-d62c-347b-b08d-c142abda23f9 | -11.30317 | -43.55018 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9c533d4-98e8-33c4-820e-ec46c373104c | -17.75328 | -44.50323 | 2025-08-29 03:49:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 83c171ad-f695-31ae-907e-e5c29c79d758 | -12.89428 | -48.14029 | 2025-08-29 03:49:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efe2d6d2-caff-3ad5-9422-51e48540f19a | -11.03134 | -45.06523 | 2025-08-29 03:49:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e3a02927-41fb-3ccd-b078-08491a19f2c9 | -14.24236 | -48.06327 | 2025-08-29 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85f25114-a07c-38b8-9c53-0a0d06706f3e | -13.19088 | -45.28906 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8ef01001-7924-345f-b1fd-450c38e3dd04 | -13.53251 | -46.94889 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cb9022b-9d11-34d5-b717-f5dc287ffd4a | -13.59979 | -46.86937 | 2025-08-29 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cd20ad6-9c14-3a1f-9e91-4362d652a69d | -11.3462 | -43.57361 | 2025-08-29 03:49:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6fafbc7-0c8b-342c-a68a-d7693ca6b703 | -5.89662 | -38.38604 | 2025-08-29 03:49:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b6dd1e7-1d59-3a91-b55b-551656219d7b | -13.19001 | -45.2937 | 2025-08-29 03:49:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d5e7f9a3-4433-3a58-9a14-54a693f0c905 | -5.61817 | -44.99652 | 2025-08-29 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4a62ccdf-6dd5-375c-897e-623a8d2bbb79 | -4.10159 | -48.20336 | 2025-08-29 03:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11a281e2-b3ff-3439-a0cc-4c484b70cca2 | -6.13736 | -44.42002 | 2025-08-29 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52f1c8cc-706f-3b6d-a8e8-94193f144ba2 | -11.59568 | -46.38108 | 2025-08-29 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ef411f7-a015-33ef-8b2e-b42d58325151 | -10.84841 | -47.50298 | 2025-08-29 03:49:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
