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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 953e75d8-5fe5-3d65-adb7-278ea1207785 | -11.81316 | -46.44419 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e3cbbd06-39d9-3b24-8d94-2c97d8f4a4b0 | -9.44586 | -60.56185 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0adb422d-423a-3921-854d-36c128a7585f | -7.71818 | -50.26909 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a28e5e7-8626-36d4-b013-fd29b59287b6 | -8.73638 | -62.38654 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fe2570c-7f7e-324c-a0ad-0158c2807a19 | -13.51299 | -46.83307 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7c9823e-ce47-32d6-8ddb-dbcd1a39cb66 | -9.45666 | -62.3525 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 80fed973-041b-3562-bd3e-96254d020729 | -8.67243 | -62.41573 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddf6effb-732c-36be-be89-5cb4c76d5321 | -12.55609 | -44.80017 | 2025-08-31 04:51:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e12b3a64-bf1e-39a5-b795-468569956843 | -8.29924 | -44.91814 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9aa1812c-3380-38c8-a6d9-fad0ab20941d | -8.96261 | -50.01033 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3bc7c70-0b17-3084-9b5f-181f8f1d2596 | -8.84468 | -52.01919 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02b1ecb0-b386-3dfd-b919-333bd8ef0414 | -13.50822 | -46.83284 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7009e7d3-0474-3ff8-892a-9ae07886c750 | -9.07201 | -65.43785 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 90c3edda-f646-3606-b49f-c4bccb95e2cd | -11.87618 | -46.72623 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64733498-1f24-39cd-be6d-e3efd67f54c8 | -11.9039 | -46.69455 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 719499be-78ed-3c5e-a26d-e68276043ddd | -12.6379 | -48.18302 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c95bba31-5661-312d-8043-80bd87797c90 | -14.3543 | -51.88793 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2ba8314-1492-3f7e-ac68-f52f9c160764 | -11.89607 | -46.37424 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5a9963e-d3c5-3bfc-bc97-be2e88098f6c | -10.0997 | -49.28299 | 2025-08-31 04:51:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf300c0a-6982-3815-9877-f96df3639e34 | -11.8638 | -46.50949 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 508cd562-6160-3ac8-8c9b-c59c528d35ab | -13.00956 | -56.88214 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 288f7fb1-cb58-3fa5-b3cc-4d6d77be6415 | -12.92138 | -56.97621 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3052b79d-ed9c-3852-9893-4aaaa7ca5163 | -8.54592 | -51.30352 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a29e3021-d8bf-3e75-aae3-bc0279109170 | -9.25342 | -47.07119 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d0db359f-837e-36fc-8a79-11b3b4311bcb | -12.92 | -56.98443 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 779f7fd9-eeef-371e-97ba-76b37d7fcdf9 | -11.8039 | -51.45583 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac527889-067d-3dc8-913d-627f839302cd | -11.32163 | -63.27728 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 17c8a7b5-fe08-3db0-a7c1-b191946a486d | -12.83425 | -48.13033 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6bb3135-31af-306e-8c91-af43ac569299 | -13.52834 | -46.97511 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2485f95f-c9c7-3a66-81a1-1c203357ec4b | -8.78119 | -46.58893 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdbf1009-e323-3b4e-ba82-6cc19288aac8 | -13.67674 | -46.93035 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86721e7f-0050-351c-a96f-95c227a043da | -10.88264 | -55.76522 | 2025-08-31 04:51:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44602b84-0e8b-3916-bd06-9641fce5977c | -9.08534 | -59.48151 | 2025-08-31 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab2e821a-4f76-36de-a36f-0688e054fc0f | -15.07442 | -48.61839 | 2025-08-31 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e495c270-5e46-31ee-a44d-560940bc1c7a | -14.35485 | -51.90866 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 467ab839-1bc5-3d87-b057-12eebabcd286 | -9.44783 | -60.57764 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2be5b586-8e63-351b-be46-7ff1f8afd56d | -9.45902 | -62.33965 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1e02780d-67dc-3fcf-ab06-6e74de2dca21 | -8.5505 | -63.016 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53c2d3fe-560f-3b92-85cf-562faac8c8d3 | -7.70911 | -50.28112 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a20241e-cbf1-350c-8c2b-2aaf74b28a03 | -12.63255 | -48.1904 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2aba5734-7979-345f-bde5-ce78248d3397 | -8.68456 | -62.87458 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d0a87b1-c116-3899-934a-ff73cc4a474a | -12.17231 | -60.74173 | 2025-08-31 04:51:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f52b1913-cde8-30eb-b24e-62ba344fbda9 | -11.08459 | -52.03065 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a8526d12-14be-3bcd-821f-7430f8f9e36a | -9.62315 | -47.79872 | 2025-08-31 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e27eb8ec-dced-30e4-979d-60786d5b0303 | -14.03887 | -44.56992 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 688a0828-a850-3af6-919a-664444e63ac9 | -8.90151 | -62.10558 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd250b8a-289c-303b-a944-217a01f0b28a | -8.73803 | -62.38683 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac4317ff-877b-3c13-be9a-1427dd4f37d7 | -9.44861 | -62.33754 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69e50809-8e32-361c-9353-3c8e9d8baae9 | -7.96355 | -46.41124 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49686e43-36fa-3ca0-ba99-a52b5ca3500b | -8.88833 | -45.091 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa51f82c-3587-3a4a-8769-7dc07695a913 | -8.74515 | -62.39836 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e95d694-3308-32ca-bcad-d404bf14609d | -13.67141 | -46.93483 | 2025-08-31 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b75b9ae-8187-3070-bb00-fe419334f348 | -11.0778 | -52.05243 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d51f2d8d-cdc8-3acf-91fe-0e9daabe8309 | -11.31893 | -63.26232 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4f9f8d5-b43f-34d7-bf19-3e1eaf60f938 | -10.03594 | -46.02558 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e460b3c-dadd-3b92-be69-e3b406c41ac6 | -11.91203 | -46.70501 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ee91969-882b-31a9-928e-e14bea9e9dec | -13.35639 | -46.94075 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4154ddc-0b3a-3993-814e-beb4dc79e204 | -13.01254 | -56.90748 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 257e8abd-db3e-38ca-9904-5fe522d349ce | -14.2325 | -48.05978 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5807c0d1-ccac-3895-8d46-3e8338f7d5e7 | -9.43918 | -60.54568 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f89b3b9e-039e-3aac-bd91-6ddaeb1a331c | -10.67653 | -50.53667 | 2025-08-31 04:51:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b5eab0e9-0691-3ab9-b1b3-7622e784bcfd | -11.07742 | -44.61147 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6706408a-3506-390f-a9aa-a407344b88f8 | -8.63609 | -62.82888 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4b67e94-f362-36b5-82d3-46e68be40544 | -8.74097 | -62.40104 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6056ecc0-b983-3086-a8bd-ed8423bf633d | -10.95025 | -50.85587 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5cdcb92a-81a1-3d0e-b888-52e6be2ab371 | -7.90893 | -63.01777 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0837d4d-7cae-332e-94ec-3bd67a2b0e39 | -13.3452 | -46.98955 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66b02177-ec89-35e6-ad6b-6b9c5d29ec53 | -11.85621 | -46.4573 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b99a39-5eda-398b-bee3-40f0695c7b22 | -10.59827 | -54.9104 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d783e68-ccff-37f3-95c2-c5095fe971dd | -11.21852 | -48.45855 | 2025-08-31 04:51:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05378a9b-a73d-335e-982c-0516fb90a210 | -11.3322 | -43.63688 | 2025-08-31 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2119b58-caca-3c37-b4c1-fd29d3594284 | -12.63299 | -48.21879 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 88b429b1-6e44-304e-9e44-38216a83125d | -13.26098 | -51.9798 | 2025-08-31 04:51:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f847cfe-c8ac-30b1-9dd1-0f57b6ebc591 | -8.64375 | -61.951 | 2025-08-31 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a471ea99-bb34-3fee-86ee-ef8e7b09458e | -14.63101 | -48.057 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| daf74bb6-5884-33df-905a-1cd0fca19afe | -11.55765 | -47.62264 | 2025-08-31 04:51:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7e96868-82b2-3c24-a0f2-0626e4771ddd | -8.74156 | -62.39776 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42fdac72-9030-36fc-a23b-aeadc5230dc8 | -7.95271 | -46.4236 | 2025-08-31 04:51:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 75fe20b4-7005-37aa-8639-c8d896e60aff | -8.65407 | -61.95291 | 2025-08-31 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd029eb9-6f28-3c33-8123-1ee03f894727 | -8.73744 | -62.39015 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14fd2556-642d-375f-b44d-a8e38d9c0665 | -12.4318 | -63.92545 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 89d368e5-27ac-3c73-a4fb-36ff70093c95 | -11.06645 | -52.01258 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46da4896-2e83-3b67-a2eb-bbaba3f01376 | -8.77842 | -46.5901 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00d7ee97-0645-3c24-ad08-c543fde6bc9d | -9.10818 | -65.76942 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0afae57-d370-34d1-a023-39f454c847af | -11.88142 | -46.73436 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4881cc1-eea6-3fc5-8d93-d943029ca9a2 | -8.6586 | -62.8294 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec296390-ac16-38d0-8c50-38348da21030 | -14.03249 | -44.57642 | 2025-08-31 04:51:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d1fd3b0-d988-3230-b29b-5195a22070cd | -13.36261 | -54.38969 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1196911-8ede-345d-b5fb-97db2562b496 | -12.17902 | -50.09397 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f599fbe8-3cd1-335d-add1-0ab1ac67fb51 | -11.89878 | -46.3904 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 422309d6-7039-34f8-aac0-7e838b978cfb | -10.32051 | -59.20137 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d997d763-a665-34a5-991a-281fbe3e6bed | -8.6818 | -62.4246 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f17c4467-96e2-303d-910a-ca793cbf9abc | -11.89893 | -46.42574 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 730e0689-77f0-308e-ab36-cee323be5379 | -14.63446 | -48.06515 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5012699-90a1-3cda-a111-94be74742990 | -10.20321 | -55.4378 | 2025-08-31 04:51:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96f75997-ea2a-3b5b-b5c6-d7c96af6429e | -12.63723 | -48.21937 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f0d2913-f0c8-3635-a0cf-1fa930035a4f | -10.9668 | -50.86669 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f0350854-7e58-3a64-84a3-846775710603 | -13.52354 | -46.97544 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebbccaf9-5c1a-3c52-9c78-c3f6fad91c17 | -8.65297 | -62.83149 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3128b50a-bc0d-3033-a289-9f75db36a39f | -11.23952 | -44.67599 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README60.md)
