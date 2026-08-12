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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5be26f9d-29b7-3ddb-836a-97c0fc2a8c09 | -8.95393 | -60.55444 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 396bc964-068b-32c3-87ea-1a5dc1d1816d | -11.49296 | -54.60476 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24cbfb30-adbe-3219-badb-eeea4efdd336 | -8.95265 | -60.56082 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 188dc2ce-8735-35bb-a4f0-59d7dbc30104 | -9.37713 | -47.44353 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7793178-a2b7-30b5-9e30-84decece8595 | -11.47684 | -44.57217 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9fe17210-efea-3366-a4b0-50d7a1e3fac7 | -11.98331 | -46.39977 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| baf634b6-bb13-339e-af8e-893ba32cd555 | -10.82236 | -50.33729 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75163afa-04fa-3706-8df1-873c5ff91fb7 | -11.82993 | -51.84155 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9caa296-430b-3b6d-a35f-6ea6a11ec818 | -11.82361 | -51.83405 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1199dff4-d126-375a-ad35-d2440c75e2a7 | -7.01186 | -44.62403 | 2026-08-12 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a4d54cb-ff27-3821-84b0-51887941b16f | -11.94934 | -46.33168 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a553b18f-827e-31a3-81e7-ef3a0100b8d3 | -10.21267 | -45.93207 | 2026-08-12 05:10:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f184bda9-ccd3-3d7f-88c5-8a227c418dab | -12.10133 | -47.18757 | 2026-08-12 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd4e4af-d2a4-34b5-af0f-3818505b518d | -11.80599 | -51.56723 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 31a5f702-eda9-3db5-858d-5f380a85094e | -9.76015 | -60.76868 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d13d6fc1-9a6f-3d18-9e9d-ef0744c89ff9 | -9.15667 | -48.96017 | 2026-08-12 05:10:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d2b396f-c19b-3e01-9c04-d8748dd9e6a5 | -8.98048 | -60.53526 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d1a40d10-8757-3cf0-ab00-1958a6df0270 | -6.04325 | -43.87084 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 472bbf30-5098-3c9c-a7a8-cfbce39b36d1 | -11.46909 | -46.6939 | 2026-08-12 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20444849-2a0e-3ec0-afd5-54e610f2f15f | -11.61055 | -54.66219 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 572fd7a2-df0e-3d4e-9f5b-622bb81db89d | -11.98233 | -46.3867 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 86883643-ba9f-3bca-8922-3ccea051771a | -6.5957 | -59.0057 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97e5f1f4-290c-3c77-b0cc-a7edf1e9633b | -11.60533 | -54.64928 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67782f5a-7b37-3bbf-91aa-58525559fa90 | -6.0484 | -43.87169 | 2026-08-12 05:10:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2669121a-92f8-3313-96f2-5159431809fd | -9.76471 | -60.7647 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81e18d4a-6304-34d5-94d3-e3c6a3412319 | -11.82454 | -51.85696 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec670713-98e9-3427-9a33-32020df72829 | -7.38219 | -59.9705 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a8f9d0-692d-31ba-bc55-ae9baa9a3a83 | -11.98536 | -46.38304 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc11a6f2-2b19-3bce-afe1-8d72d326a169 | -11.81236 | -51.82468 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2f2f366-647d-39e1-a790-82474267f457 | -9.13596 | -46.39474 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1a068e2c-652c-3509-9fa0-05ae8ee49325 | -7.4083 | -59.99793 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 885a7d52-4016-398a-95c6-0639ce887b5b | -11.98717 | -46.36831 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bb5a989-5647-3d67-b9dd-6582c5fe1d56 | -7.91393 | -45.11574 | 2026-08-12 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd5f0aae-1eec-3a94-9d98-109bead4c28f | -6.54095 | -43.12257 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2ce541f-99ea-390e-ad2c-4751f4d188a1 | -11.78246 | -51.85859 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 02b45df6-5815-32d7-a382-016ffa2d804f | -8.66056 | -54.95296 | 2026-08-12 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 509ba77e-2d51-3663-9863-0a42fa48afc4 | -6.85703 | -46.00557 | 2026-08-12 05:10:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bae53b25-6aa2-3c83-9db5-b4726461890d | -11.95347 | -46.34761 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 270cd7fd-3c5d-3d0d-8535-82ec00f572f9 | -11.82201 | -51.84528 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9e5ff32-3005-3c14-a209-3980d53e232c | -8.89437 | -60.58424 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e328b7c-62ae-34d0-9d92-0c784ec42ef8 | -11.94357 | -46.32938 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 290a741a-ed9e-3600-a70a-10bd6f4237f3 | -11.47092 | -44.56564 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1984b3e0-f12a-3c17-8c5d-5d19ba5bbfe1 | -6.99445 | -42.63097 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 72c3a610-e925-3c0e-9fc2-06bd585a5f28 | -7.6862 | -55.16623 | 2026-08-12 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61f7cacd-0225-3740-9456-70aaaad8b0bb | -11.465 | -44.5591 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75b54cd9-257e-3209-ab5a-1443d05ee199 | -8.8945 | -60.56051 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1d23aec7-dd6a-3fac-a8e5-b7dd0cdee74a | -9.6256 | -48.32944 | 2026-08-12 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9db81438-3e48-3ee0-845e-869652e50ee2 | -11.97998 | -46.37777 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 48af7d96-4a61-3d31-a797-4d796e8bce29 | -11.98385 | -46.39539 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6b92a33-1ba2-3b53-ba25-2c8f0e34b3bb | -8.07381 | -46.51744 | 2026-08-12 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 70b493b3-1fe2-304e-86a2-71a39f737a48 | -11.78657 | -51.85914 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29c888a2-976e-3b2a-b74a-d44a09789940 | -8.94376 | -60.49785 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b9cdee3-8e82-34e8-984d-94e559929b51 | -9.13026 | -46.39389 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faeaae5f-92e2-398b-be22-31bf1855bd8c | -9.48037 | -47.8293 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9c9c41a-d5b1-3873-9fe6-c8787533fca9 | -8.95569 | -60.54246 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a0825ea5-ee10-3f5f-82f4-9ade8db09a79 | -11.78404 | -51.84732 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4d6624bf-de75-3589-adb6-29b6cadedb50 | -6.59179 | -56.05818 | 2026-08-12 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67a40d16-842f-31d2-acca-562cf756f3ba | -7.40457 | -59.99732 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6f07be0-da4b-38b6-97f7-4ea6dfdeaf84 | -8.94893 | -60.53653 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1d02598-603f-3add-9384-9a018484dc70 | -7.42249 | -60.00492 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce126052-eed4-3da8-bd91-840a2cd15a7c | -8.95193 | -60.54182 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb8ffb74-4476-347e-a051-f6ae318a5379 | -11.82308 | -51.83778 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff118512-1d16-3730-8d71-18584dd1feac | -8.77899 | -45.79343 | 2026-08-12 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5bc90f5-a92e-366f-93f2-388507dadf74 | -8.94294 | -60.52602 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b60f499-2eeb-3829-9427-ef30a2266ec9 | -8.94816 | -60.54116 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44341b50-baee-3160-86ea-744484bf5f68 | -7.4567 | -46.15321 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2e17e45-8755-32ee-9e91-9dee57890b53 | -11.4584 | -44.55831 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a764adc2-a9ae-37d8-a59e-ef2d932d2c66 | -10.09303 | -46.21793 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc959f6-3570-36c4-8a7b-2f96e57a1871 | -11.98185 | -46.39086 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b596bb09-b6c4-3c07-86ab-961feef95ac2 | -10.0999 | -46.21048 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b7cfde1-eab5-3b5d-b8f7-c6ad824c1747 | -8.95718 | -60.55689 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bfff11e-fe30-3b8f-b414-c821a6d77d28 | -11.60183 | -54.64875 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b197e060-3b81-3cbb-9973-20543844c309 | -8.95642 | -60.56147 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7161dad-db7c-363b-a1ed-bdf389a0e2f5 | -11.4632 | -44.56105 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 277bbd0c-2234-382f-8fc0-c6b0bf6a2ede | -11.15804 | -50.53048 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7dc9155-4d09-3429-b173-6b60472e4b64 | -7.92063 | -45.11195 | 2026-08-12 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c12a43c8-af29-34fc-835b-158fab1c7151 | -9.76392 | -60.76935 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9da497cd-d225-30fd-9f7a-a781601bcd29 | -7.00061 | -42.63813 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9264670-9e19-37dc-998e-4f6f2a2e9cfc | -11.97253 | -46.38943 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbce7025-f0aa-34e8-a341-6c357debcc21 | -9.34333 | -47.49353 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41cd9b1a-c764-3d0e-8616-a13694bd197f | -10.3681 | -46.38215 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2d0dd528-ef7c-3742-83bd-4c0a47b9ac7a | -9.47399 | -60.50858 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d7a3758-3496-31b3-9aa0-8666bc319f2c | -7.41576 | -59.99918 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f14bea4-d873-362c-8293-eba22ec11835 | -12.13742 | -48.26923 | 2026-08-12 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b99e31d5-9f58-3b74-828f-27c0f9a251f7 | -11.47045 | -44.55612 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef35d5b7-ce15-3d05-be9f-1ef2c7c049ba | -8.07432 | -46.51361 | 2026-08-12 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e04f679d-b682-3e29-b6e2-9d109b506902 | -8.95334 | -60.53541 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb45d99d-2a67-372f-af7d-1f74a2838935 | -8.95692 | -60.55965 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b6e1b04-f11b-3e3a-b451-2b440dbc13d4 | -6.99264 | -42.63058 | 2026-08-12 05:10:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e9157ef9-0717-31f7-b323-94ac78483bfb | -12.10087 | -47.19149 | 2026-08-12 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 993fb5a1-ebbc-3f62-ad3e-7cb69ffbace4 | -10.83841 | -50.35322 | 2026-08-12 05:10:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 180d067f-8cc8-3e29-b647-632ce56dd888 | -11.24541 | -54.83241 | 2026-08-12 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d5f1d2c-250b-3bf0-9239-caf344732787 | -11.60474 | -54.65323 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa22a92f-ad2b-3557-8170-9aae03f7bb4d | -10.46944 | -46.61605 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f827a217-1f87-381e-b816-56880d40f3f7 | -11.94656 | -46.35487 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 492f68aa-e237-3e40-ba16-50d21b86faff | -8.94858 | -60.56297 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5fe04f67-88ef-35b9-8076-bb3a522851a7 | -11.78605 | -51.86287 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8d29779-efb5-3b23-b6e3-113e99361f51 | -11.81594 | -51.82902 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31c6188f-797a-3790-b85a-dd593cde5e49 | -11.98489 | -46.36453 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 05007b51-fc50-3330-8fe4-31f69022f18a | -11.98436 | -46.39121 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README30.md)
