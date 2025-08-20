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
| afbf61bc-9cc1-3167-9135-879c3b5b604c | -6.74505 | -39.98763 | 2025-08-20 12:14:00 | TERRA_M-T | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 32.0 |
| b6e8eb66-115a-3f10-9dda-9eaca96f1add | -9.73393 | -45.60673 | 2025-08-20 12:14:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4a6557e0-5b46-3aca-885e-1a96f660d643 | -9.25519 | -44.49543 | 2025-08-20 12:14:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2012ae18-c2f0-3c66-9822-377140ad9a34 | -10.19023 | -46.6071 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1e468946-3d9d-313b-8b87-f409d3001e0c | -6.7873 | -39.1897 | 2025-08-20 12:14:00 | TERRA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 8c2c2748-5ea9-31f5-892a-20eed13e1cbb | -10.99347 | -46.71869 | 2025-08-20 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6a1f014c-b796-3318-a56a-a95163cf4230 | -9.85596 | -44.67946 | 2025-08-20 12:14:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 05979d87-9e16-3519-a220-dc7e3f3c4b25 | -7.21763 | -43.9765 | 2025-08-20 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 472b0c3f-4b52-397c-b5f6-8f1cc8529527 | -12.44336 | -47.66092 | 2025-08-20 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7a98a621-6ce5-300c-a4bc-de38cb7ba2c7 | -5.90002 | -46.15071 | 2025-08-20 12:14:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 92018a86-33e5-3faf-bec0-08988a63ee4c | -6.72508 | -44.32734 | 2025-08-20 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| abf35d25-f12b-381c-9037-c4a9276bc728 | -7.60177 | -44.39016 | 2025-08-20 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 502467c3-a7e3-3776-8cc7-556a5686540f | -6.6023 | -43.89553 | 2025-08-20 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 731a8665-6fb6-3504-95c8-0680ae6b192e | -11.91011 | -44.87666 | 2025-08-20 12:14:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f572155f-d71c-31e7-976c-7b71b2449b9f | -8.7869 | -45.46501 | 2025-08-20 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 9cd124ab-0463-3bf8-a608-dba8ed7e5744 | -7.48698 | -45.00716 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 27b57995-29fd-361a-8744-7998ccec056a | -7.14244 | -44.18347 | 2025-08-20 12:14:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8db8b8d9-0cd2-3f5d-9596-1f0831caccbd | -6.85058 | -44.42176 | 2025-08-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 720c5321-2e5a-3d07-8aea-0afb377da6fc | -6.19662 | -43.56598 | 2025-08-20 12:14:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c2e88fe8-c713-3f06-9560-439b97650c8b | -8.72692 | -49.2924 | 2025-08-20 12:14:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f063b9ea-5304-37ce-a148-6a9211b97747 | -7.58126 | -44.40597 | 2025-08-20 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a9f1e917-3a5d-3ae2-b420-c72e1478af01 | -8.80592 | -45.33159 | 2025-08-20 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7e9a173c-082a-3c4c-8f7d-f7d6a1e8b5eb | -6.56908 | -43.00649 | 2025-08-20 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| db595027-11f2-3815-8c5a-9837f19404db | -5.62951 | -43.14065 | 2025-08-20 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.9 |
| dbbd4fe2-ca15-36b1-ae9a-09744a7ade3b | -5.86355 | -39.04159 | 2025-08-20 12:14:00 | TERRA_M-T | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 13.7 |
| ef9e33f7-42fd-3066-9a15-1418962034cf | -12.98788 | -45.20902 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 220.3 |
| 3f048d54-2643-39c1-8c48-a8a5590fddfa | -5.13276 | -42.87516 | 2025-08-20 12:14:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 87cdba62-7f7c-3333-b53d-0791323c1fd5 | -11.60916 | -46.61416 | 2025-08-20 12:14:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 2ab0588c-dbf8-3dec-84ed-fb747d25976f | -6.96857 | -43.9135 | 2025-08-20 12:14:00 | TERRA_M-T | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 30927f21-1b89-3a8c-979e-3aa0186348d8 | -13.12135 | -42.41761 | 2025-08-20 12:14:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| cf5d87d1-2f63-3432-9d19-a4c5c41d77a6 | -6.73545 | -44.32601 | 2025-08-20 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2d53dab6-54ed-3b9b-8572-76aad8bb76b7 | -6.94666 | -43.87223 | 2025-08-20 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2edf55da-5438-30f2-9920-b29127cb4b49 | -5.78488 | -43.613 | 2025-08-20 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2c4a44b8-68ea-381c-80ef-ef1b387fce5c | -4.8704 | -45.23959 | 2025-08-20 12:14:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| c94fe6f6-047a-36d0-bfe8-4209455e7b25 | -7.30162 | -43.70394 | 2025-08-20 12:14:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9a284dbd-63da-3682-b393-1cc783a6f325 | -6.49018 | -45.19601 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 61db34b7-40e6-3b9d-9745-d35a455d89eb | -10.28518 | -46.77408 | 2025-08-20 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c9ac9e3b-5c1c-3e24-a741-5eb8bae73d20 | -9.81629 | -49.20906 | 2025-08-20 12:14:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d0838623-61e7-3cdd-952a-30b999138d60 | -6.86293 | -43.613 | 2025-08-20 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ff5acc13-1947-3ca6-8b4e-a77f00c7f8fe | -6.84929 | -44.43083 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 50605a8f-17dc-3425-9d67-42c3c6254e91 | -7.99441 | -38.51758 | 2025-08-20 12:14:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 28474505-df07-3193-80e3-f28da30223dc | -10.19155 | -46.59812 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1482d93c-0198-3998-85f9-20f8d61398f2 | -9.73266 | -45.61564 | 2025-08-20 12:14:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d45ef9c-3c6b-3f25-863d-a1370307a098 | -5.13415 | -42.86525 | 2025-08-20 12:14:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a216b80c-1ecf-3404-ae60-5b9c54cc472f | -5.96648 | -44.15381 | 2025-08-20 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1be76829-7404-3076-bf74-1e8d3ab9c260 | -10.69639 | -48.22563 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 807fedc1-2553-399a-878b-cdc2cb37cb14 | -13.17287 | -46.89392 | 2025-08-20 12:14:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b3fca9a2-96fc-3b07-9310-38147ab8aeda | -10.70418 | -48.23697 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| ffc9f857-b053-3cca-93ae-fd6dafabc542 | -6.02524 | -44.38885 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3de91fa5-553a-3fff-a1bf-f02678a5466c | -8.29895 | -46.34973 | 2025-08-20 12:14:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| abc24169-3394-35ee-b8f3-b69ab8d26985 | -6.44584 | -45.44144 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dd34dea0-0db0-35d3-8e2b-2f8ebb453a13 | -6.86847 | -43.11689 | 2025-08-20 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 896d00a0-19df-3049-ba5e-822b1857713d | -10.71503 | -48.22814 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1f108f09-f96c-3791-8602-734ea845c4d5 | -7.31079 | -43.70522 | 2025-08-20 12:14:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fdd2c302-beb1-3375-82e6-221ba9764cf5 | -5.28118 | -43.58873 | 2025-08-20 12:14:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 67c7a932-cdbe-3d58-9cb4-bc89a43be548 | -6.86426 | -43.60343 | 2025-08-20 12:14:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| a8a6327d-b0c1-3caf-88fb-b8506546367e | -7.23594 | -44.69905 | 2025-08-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 42a0ce44-3579-3f4c-a801-c39b42ff8f6f | -10.31735 | -46.67785 | 2025-08-20 12:14:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a1261d18-5afc-3d5b-a45e-43cca5f65362 | -12.67176 | -44.96427 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f0bff86d-1679-343f-a62c-ce96266a0de5 | -8.49069 | -47.60933 | 2025-08-20 12:14:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d2dd0ae0-9b88-364e-b16f-df877288f9b6 | -5.7953 | -44.77024 | 2025-08-20 12:14:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 919a7437-603c-3311-956b-6dc05ab7b779 | -13.03327 | -46.78465 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e7ac0460-62c0-377f-8c32-8f18bd3c9ce8 | -8.78563 | -45.4739 | 2025-08-20 12:14:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| aaf44553-ffa6-3b76-8880-d6deeb7fc840 | -12.98918 | -45.1995 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0b9287d4-b994-394e-b8ab-d5fd760a72a3 | -12.10306 | -47.90036 | 2025-08-20 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 45f5b120-8920-3d5d-970c-ffdf60a0c348 | -3.98683 | -42.50574 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| e6393a0d-4a00-3f23-ac2e-a71909d88a6f | -6.94739 | -42.86268 | 2025-08-20 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 25228a40-17fe-3a66-90ab-74ddfc908357 | -10.70572 | -48.22683 | 2025-08-20 12:14:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 08679c9b-b8bd-34eb-852a-d237d1986d4a | -4.85925 | -43.44283 | 2025-08-20 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cf500d88-ad58-3346-967c-2c9a182277da | -11.12938 | -46.99065 | 2025-08-20 12:14:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 4f92038b-6b50-3337-afa7-a0baff19b0af | -7.5928 | -44.38895 | 2025-08-20 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 2e6c77f6-c2a2-365f-b555-8e1981d8ec49 | -11.88789 | -47.04796 | 2025-08-20 12:14:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| ea48315a-bd12-387c-8097-54b243154085 | -6.27808 | -43.70877 | 2025-08-20 12:14:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ee4d1a61-fe52-393d-a67d-faccf433c225 | -6.86988 | -43.1068 | 2025-08-20 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 181610ca-ca15-3763-b9dc-ae2a8fe15a43 | -10.99332 | -45.89145 | 2025-08-20 12:14:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0442c2f1-6a1b-3550-afc6-b7b78ff0caca | -5.97541 | -44.15507 | 2025-08-20 12:14:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 1a6539e2-70f9-3d19-9436-abb9a866af3a | -3.54837 | -44.22976 | 2025-08-20 12:14:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 092a98be-3773-3ce6-bb3a-de5b7092104c | -4.91595 | -43.23908 | 2025-08-20 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 2e8a43db-6326-31b0-9c69-386e0b80671b | -9.80737 | -46.88607 | 2025-08-20 12:14:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e61c7638-2881-3852-bd81-b5916afc5639 | -6.12247 | -42.7314 | 2025-08-20 12:14:00 | TERRA_M-T | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5750e980-c232-300a-9a58-0ca7552d18eb | -8.29237 | -47.63762 | 2025-08-20 12:14:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 85fd2329-941c-3d2f-b607-0d1d86924b3d | -12.86917 | -46.061 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 5690a05d-a3b8-3616-8aea-01f3b4058f4e | -12.6579 | -45.33032 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e2df6a23-5c99-34d3-a2a3-001d4dc9eacd | -12.64759 | -45.33838 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| db00e542-d6a1-3d44-9ec9-0ab16abb6a5c | -7.41867 | -46.87439 | 2025-08-20 12:14:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f1bd33bb-17fd-3df8-85f8-16eb34ffabdc | -12.44474 | -47.65163 | 2025-08-20 12:14:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a72a7f13-a003-3bd5-8227-2eea9c2d4cba | -12.67308 | -44.95464 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 4333741a-ab34-38d5-8f50-80d5700fdb4c | -8.15376 | -45.5666 | 2025-08-20 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 86a40835-a3bf-38b9-b28b-72937c166d8d | -5.61772 | -43.49128 | 2025-08-20 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 762c225a-270c-3362-b694-64e2ddee59db | -6.78583 | -39.18388 | 2025-08-20 12:14:00 | TERRA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 25.5 |
| b3282ec2-8ff5-33a6-b468-6ec589671503 | -9.52434 | -47.23963 | 2025-08-20 12:14:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e83f4e7b-de4f-334c-96f8-53a81cc62806 | -13.03558 | -46.83098 | 2025-08-20 12:14:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 935cb212-99cb-3a64-a410-db20568c948f | -6.58556 | -44.4673 | 2025-08-20 12:14:00 | TERRA_M-T | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 485b7154-5843-3e32-8562-95af574fda1b | -5.82471 | -46.35369 | 2025-08-20 12:14:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 95286bd4-90a5-319d-ae3b-e1615fe89e53 | -7.11398 | -44.64209 | 2025-08-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 07d540ee-b949-3b29-b39d-2410f02d00b7 | -10.82318 | -43.28405 | 2025-08-20 12:14:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 12.0 |
| b5496151-9dda-354c-9881-707cc69f1b5f | -7.02707 | -44.60532 | 2025-08-20 12:14:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ec2e9bbc-4f87-3414-8a2b-6415cb1a3ba6 | -12.98657 | -45.21852 | 2025-08-20 12:14:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a4214a13-7479-3cb3-8c19-65ab32fbb5aa | -4.95612 | -43.0883 | 2025-08-20 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7e71cbeb-638a-31c8-8ef9-9a65ca0d8429 | -6.43565 | -45.512 | 2025-08-20 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README60.md)
