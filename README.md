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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 768d31e0-4d17-3c09-85c5-6ca037490cee | 4.4435 | -60.9846 | 2024-12-17 00:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| d9a700af-9da2-399f-b96d-192bbbeb5478 | -4.9047 | -44.1831 | 2024-12-17 00:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 340.9 |
| 1768d33a-84c3-3c77-9922-71a430b3b60e | -5.1123 | -43.9164 | 2024-12-17 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 9c3bfaef-9857-3a77-8058-d9eeb23c0fe4 | -5.0751 | -43.8958 | 2024-12-17 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 3e64c136-1146-330e-bfa5-1519a57231ea | -2.8124 | -45.1274 | 2024-12-17 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 047961a8-0b30-387a-9f33-5d231494f09a | 4.4435 | -60.9657 | 2024-12-17 00:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 1f2aa225-ce74-31a2-95bd-7f4f5aa39d7d | -6.1953 | -46.2215 | 2024-12-17 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| adb8b9d5-e828-3c3a-9b2c-524be5159a49 | -3.1503 | -53.1965 | 2024-12-17 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3041f428-ff54-3616-b37d-eaacf357824b | 4.4618 | -60.9653 | 2024-12-17 00:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 1f77a306-c5bf-3861-871a-3c34757f6a3d | -5.0936 | -43.9176 | 2024-12-17 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 243.9 |
| fd18ee7f-78d0-3c28-bd43-678d1e288e3b | -6.214 | -46.2202 | 2024-12-17 00:00:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 05d7c531-812b-35f4-a481-8dfedbed6d10 | -4.8858 | -44.2073 | 2024-12-17 00:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 4558dc98-85e5-36d3-b262-564f681bcffa | -4.9024 | -42.08 | 2024-12-17 00:00:00 | GOES-16 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| afa3bb95-cd1d-3bc4-9d33-405f0903dbe6 | -3.2969 | -53.3547 | 2024-12-17 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 91d28470-b298-3f0c-9934-05e77caf99e2 | -4.886 | -44.1843 | 2024-12-17 00:00:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 431.2 |
| b68a4e0f-cdc4-33a7-8208-af9a0d303862 | -4.8861 | -44.1613 | 2024-12-17 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 214.0 |
| fc88cf4d-ba75-308c-b1a7-5eb596855fd1 | -19.1043 | -52.8493 | 2024-12-17 00:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 126.2 |
| a24887b1-1ec7-382a-8ab2-e19e7253328c | -4.7952 | -46.4012 | 2024-12-17 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 65a66b59-285b-3c35-b35c-2c6b943b303a | -4.9048 | -44.1601 | 2024-12-17 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 171.9 |
| 987f4922-7efd-36fc-be16-b827ebea4d99 | -3.2968 | -53.3749 | 2024-12-17 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| b558a044-0832-36f6-aafb-adc0115fa6e7 | -4.8673 | -44.1855 | 2024-12-17 00:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 80f90664-855b-331f-9481-96fb84e3df3c | -5.0749 | -43.9189 | 2024-12-17 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 88587453-ae4c-33a5-8304-5a2216a14f81 | -19.0842 | -52.8527 | 2024-12-17 00:00:00 | GOES-16 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 115.2 |
| d84c8a04-8c09-3d4d-b85c-e1ee1aa76f26 | -5.0938 | -43.8945 | 2024-12-17 00:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 9eaba374-7643-3cf3-ba7f-b485a82f6733 | -18.8994 | -56.056 | 2024-12-17 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.4 |
| ac2bbdf2-24c7-346c-b773-80a9525634d0 | -3.1503 | -53.1762 | 2024-12-17 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9cc98155-f2ad-37f4-895c-db7dfab772a6 | -3.3152 | -53.3744 | 2024-12-17 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6166691d-bb47-3298-adbe-c37839ee676e | -15.0865 | -59.6487 | 2024-12-17 00:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 72360b23-332e-3df8-bdad-23f189442248 | 2.3245 | -60.7385 | 2024-12-17 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 40728e77-0b31-387a-823b-507f34572214 | 4.4436 | -60.9467 | 2024-12-17 00:00:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 567d53a1-1b5c-37e3-a66d-6186310120a2 | -5.08 | -43.91 | 2024-12-17 00:00:00 | MSG-03 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 187f4611-e213-3b91-99c1-1b69cea8297f | -4.88 | -44.21 | 2024-12-17 00:00:00 | MSG-03 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3c9fc7f-d2da-3639-abca-6beed220d308 | -4.91 | -44.17 | 2024-12-17 00:00:00 | MSG-03 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a5e3d88-ba2d-3c70-986a-9cd6110fa8d7 | -4.88 | -44.16 | 2024-12-17 00:00:00 | MSG-03 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f24b094b-a9fa-3746-8004-62ecc8cd2857 | -6.1831 | -35.2188 | 2024-12-17 00:04:00 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1557d437-409e-37d7-9807-5148c3ac70d9 | -8.5243 | -35.080601 | 2024-12-17 00:04:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0815195d-5a31-3668-bcaf-2664a980b7cb | -5.0786 | -43.911598 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 557b03c8-fdb4-38ab-a700-1cb83775b393 | -6.1994 | -46.208599 | 2024-12-17 00:09:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f695b54-2533-375c-b6cd-4564e490e8f9 | -8.6561 | -36.900101 | 2024-12-17 00:09:00 | METOP-C | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 498a1499-a8c7-3061-a28a-03be223499bc | -9.9505 | -36.2995 | 2024-12-17 00:09:00 | METOP-C | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84b38bda-f445-3a58-8a44-b82de0e6c008 | -6.0295 | -42.141602 | 2024-12-17 00:09:00 | METOP-C | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 776a3af9-3b60-349e-a6aa-41e50951ca81 | -5.1116 | -43.185902 | 2024-12-17 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a476228-24ef-3caf-a7e7-7bfefc40b1c3 | -5.2004 | -44.5513 | 2024-12-17 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23e3b323-2020-3ae1-a629-98d3161e44e6 | -2.8132 | -45.122898 | 2024-12-17 00:09:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cfdc6b6-74be-3b9f-b9c7-57bf0d256244 | -3.1292 | -45.477699 | 2024-12-17 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b12a549e-2c1a-34ed-953c-48504f61ee58 | -3.9933 | -44.158001 | 2024-12-17 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 776b1fdd-a477-39dc-8945-157c9c7fdf62 | -5.0864 | -43.9006 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a16bcb0f-198a-3740-9331-2a97bf67889c | -4.3954 | -41.427299 | 2024-12-17 00:09:00 | METOP-C | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5602497e-3c36-3f90-a1be-ad55b0b42fea | -7.2133 | -44.8983 | 2024-12-17 00:09:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d0db348d-d2ba-3ae2-bdff-697c389ad467 | -5.8363 | -39.160099 | 2024-12-17 00:09:00 | METOP-C | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 33601705-ac70-3070-948a-8e069a0c5948 | -6.6729 | -38.581699 | 2024-12-17 00:09:00 | METOP-C | TRIUNFO | PARAÍBA | Brasil | 2516805 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 107ed03f-067e-37e9-a925-06f0de45e0cd | -5.5536 | -37.981701 | 2024-12-17 00:09:00 | METOP-C | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 1c411c7f-074d-3fa7-9567-8cca588dc956 | -1.6201 | -45.841999 | 2024-12-17 00:09:00 | METOP-C | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 559bd56b-0f22-3d84-8301-92a06d223d26 | -2.9689 | -39.834702 | 2024-12-17 00:09:00 | METOP-C | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ecf8b76-8ad1-3088-8c2e-8aa3fdf8258b | -4.5202 | -44.033401 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbdfa1df-16ea-3a69-a570-97bbc87ae4d2 | -4.6633 | -44.030399 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1cb527f8-d4a8-37f3-9a04-3afdcc4a4ae8 | -4.1258 | -43.5583 | 2024-12-17 00:09:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad6cdad-bc3b-3b76-ba5f-9f2936e1e9a0 | -7.4099 | -44.719898 | 2024-12-17 00:09:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 80cefea7-05dc-3a68-bacc-d60241bf510d | -2.0496 | -46.649502 | 2024-12-17 00:09:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c988db3d-8023-37bb-a95a-9b9767e94be8 | -1.2325 | -46.7547 | 2024-12-17 00:09:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ce62a5-10be-390c-8897-57d224015a4f | -9.0118 | -35.955898 | 2024-12-17 00:09:00 | METOP-C | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 00af2844-d01f-35e7-888d-5c2b40769ac9 | -5.1404 | -43.222801 | 2024-12-17 00:09:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a93ff1f2-b36d-3ef9-96a0-4d48ae13c315 | -3.9377 | -42.6343 | 2024-12-17 00:09:00 | METOP-C | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f73a921-be1c-3aad-af6f-83a75261a2c2 | -5.3638 | -44.039501 | 2024-12-17 00:09:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0e6b306b-41cb-35c0-ad4b-f89bfcefea05 | -4.0422 | -46.903999 | 2024-12-17 00:09:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d8cd36c0-fe9a-341f-b7a6-102f354187f4 | -5.1809 | -37.534 | 2024-12-17 00:09:00 | METOP-C | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| b1aaa8c3-6607-3325-ac94-c3433cccf90b | -5.354 | -44.041698 | 2024-12-17 00:09:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2ec44c5c-0f10-307f-84cb-d4e96b9a0a40 | -5.6184 | -44.818001 | 2024-12-17 00:09:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 96893178-d9c7-3235-a626-4c91557af793 | -1.8887 | -46.798801 | 2024-12-17 00:09:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e79b02-430a-3f9b-a10b-192cbf08941a | -5.3952 | -40.657398 | 2024-12-17 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 37c6adf0-b1d8-3c81-b189-9f3e7c938791 | -5.9857 | -43.4645 | 2024-12-17 00:09:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae0c2304-0d5e-3a62-84b0-a9e3ff9b955a | -3.6588 | -47.1567 | 2024-12-17 00:09:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6eaa93a-2cdc-3001-942a-a69c54128c41 | -5.4872 | -39.122601 | 2024-12-17 00:09:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bb9f45fc-0db8-3bd0-bf35-54e855a68aee | -4.888 | -44.1623 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1778ee3d-cd8f-35f6-a0a6-7dabbc488bbd | -4.8661 | -41.367199 | 2024-12-17 00:09:00 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8c105aa0-7c45-3acf-9628-b3fad37a18d5 | -5.0746 | -43.893799 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 413a466c-95b7-3d94-a613-93307b24a566 | -12.6824 | -38.383202 | 2024-12-17 00:09:00 | METOP-C | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 20ff8ce3-2212-3629-9d8f-58b4870672d7 | -8.9863 | -35.935398 | 2024-12-17 00:09:00 | METOP-C | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| efa360f2-e5bf-37f9-8010-33cd1b48e2b6 | -1.3918 | -47.454201 | 2024-12-17 00:09:00 | METOP-C | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f71a0b39-38fb-3d76-8ca3-7c226dc8fa25 | -3.8399 | -45.8568 | 2024-12-17 00:09:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d633469e-73b3-3ac0-9200-9cda34cffaad | -6.1928 | -35.216499 | 2024-12-17 00:09:00 | METOP-C | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 67465beb-be55-3d65-925c-cc26903ebd77 | -4.2008 | -44.3507 | 2024-12-17 00:09:00 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdb7efab-79bd-3d40-90ec-3c73dd5613fc | -5.5294 | -39.171299 | 2024-12-17 00:09:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0a711a07-6b55-38a1-a83a-6a5d4392c1a4 | -7.2157 | -44.909302 | 2024-12-17 00:09:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d6232ae-37a1-327a-b608-ef5ea19cdd0b | -4.2029 | -44.360001 | 2024-12-17 00:09:00 | METOP-C | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d712397a-82f8-336c-87d3-c314145e7241 | -4.397 | -41.434399 | 2024-12-17 00:09:00 | METOP-C | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 58e6c471-fe0c-363e-bd50-63a84480cfa2 | -4.9627 | -43.714901 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 26f0a1e6-1a86-3790-a91e-9b7692999cdd | -4.8921 | -44.180698 | 2024-12-17 00:09:00 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdeb6904-bb07-3fbe-89bf-6024813d75f0 | -5.2178 | -43.2929 | 2024-12-17 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93100c90-392e-3a29-bb16-c4b994cee96b | -6.0312 | -42.1492 | 2024-12-17 00:09:00 | METOP-C | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e1256dc3-6534-3d6e-b7be-7a98e76338e8 | -4.8807 | -41.386101 | 2024-12-17 00:09:00 | METOP-C | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a1e87243-6d97-3300-8497-bc2bfbb8bd14 | -9.9611 | -36.5201 | 2024-12-17 00:09:00 | METOP-C | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c793d02c-166f-3801-bf86-eb6a4f1e142a | -12.684 | -38.390202 | 2024-12-17 00:09:00 | METOP-C | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4fa25aa1-d536-3893-8929-1f665517122b | -12.08 | -38.001099 | 2024-12-17 00:09:00 | METOP-C | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f9a42043-130e-323e-8125-94839f75af9f | -4.228 | -44.013401 | 2024-12-17 00:09:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 93202902-998d-345b-9780-61b97ec15140 | -4.8803 | -44.173698 | 2024-12-17 00:09:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7e7017c-c939-3342-921a-4fc7757d0bba | -4.9605 | -44.949402 | 2024-12-17 00:09:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fe17fd07-e981-3a9c-8941-0add92775c0b | -5.3839 | -40.652699 | 2024-12-17 00:09:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f178d098-7179-318b-8b66-bb91f6347cbb | -5.0904 | -43.918499 | 2024-12-17 00:09:00 | METOP-C | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a2a6bd4-c425-3484-8942-5f691463c46b | -5.9876 | -43.473202 | 2024-12-17 00:09:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
