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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 12578765-59d7-3156-a69e-3523468e1344 | -11.8243 | -47.1954 | 2026-08-28 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 155.5 |
| 3e15eebf-73c0-3ec8-b4cb-64037b282fc6 | -6.857 | -59.4371 | 2026-08-28 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 416b0d79-deed-32d8-9313-8a5ae64213d1 | -10.4693 | -46.1802 | 2026-08-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 87447523-de0b-3708-8134-269cc6b0f4c8 | -10.7839 | -50.6346 | 2026-08-28 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5df0d469-65a3-3906-8710-5e6cb384ea0c | -14.9985 | -52.5925 | 2026-08-28 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 8e613cfd-0d56-3f4d-97b4-d836a379b020 | -7.5846 | -61.3232 | 2026-08-28 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 08a33e18-e3d0-3370-ad14-c107110ebf04 | -8.0739 | -45.8372 | 2026-08-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 287ca687-d20a-3a01-aa53-0a45ccf8080e | -14.4842 | -52.1512 | 2026-08-28 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 94dbdc2c-1082-3d8b-b400-667fc7981125 | -13.3258 | -46.9107 | 2026-08-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 5f232851-9972-3cce-8e84-e91ff6c49ea6 | -11.6773 | -50.4724 | 2026-08-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| d27c06c8-ac6d-30ae-a073-ab4daec9c010 | -10.7598 | -54.0179 | 2026-08-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 36184c96-f6c0-3f7c-b14a-43a3b3284b39 | -10.7596 | -54.0384 | 2026-08-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 8b203117-7c44-358a-8b46-374b72992465 | -10.8028 | -50.6326 | 2026-08-28 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| de55f708-d40b-386d-9d44-fd0a363cf210 | -7.3663 | -55.1734 | 2026-08-28 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| c94bb576-4aa6-3476-90b3-f5dd47fc588d | -13.3254 | -46.9333 | 2026-08-28 14:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f7cb7183-f4ea-35d2-a86e-562a685fb30e | -10.8996 | -46.6216 | 2026-08-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| f581f17f-7d3f-35e4-bc42-3f586bf32d8d | -14.8627 | -52.6106 | 2026-08-28 14:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| cc7d987b-c91d-3912-9d20-4b9aa39fa865 | -2.7303 | -47.0644 | 2026-08-28 14:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b9103c17-2450-3312-8120-ad05965c9b28 | -7.6214 | -61.3408 | 2026-08-28 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 184.1 |
| ba20b9d8-3402-3a10-b161-1b63dcfd6eee | -12.0541 | -47.164 | 2026-08-28 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 9c4ea93d-f7fa-3b03-a2a0-22507a4b024a | -10.3202 | -49.9782 | 2026-08-28 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4171b061-4757-3240-9564-42afcd1e9062 | -8.0742 | -45.8147 | 2026-08-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| c379edd8-1184-391b-b049-3d34733183be | -7.603 | -61.3415 | 2026-08-28 14:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 6c07b47d-cb20-35ea-a193-d9c684b05ad6 | -11.2493 | -45.0501 | 2026-08-28 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 9fd6876c-03dc-3797-a9d8-ba920de2542a | -11.2109 | -51.2476 | 2026-08-28 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 0bfaaf5a-7d0c-354c-bfa0-56ebf0ae1c96 | -9.2284 | -51.5219 | 2026-08-28 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| 3c5b2b05-97e4-3ede-9dce-681f640bade7 | -15.4594 | -53.9653 | 2026-08-28 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 3a67cd0f-72bd-3077-a0e8-968299793093 | -13.5797 | -45.7753 | 2026-08-28 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f2447f5a-2c08-3c63-8d0e-c648a0c539f1 | -6.2692 | -53.1526 | 2026-08-28 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 27533ba0-9523-33fa-8ec9-40a0935ea87d | -9.9708 | -53.9419 | 2026-08-28 14:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 194.7 |
| 59aba83c-1844-3019-ac48-210c8f82cfaf | -10.9187 | -46.6192 | 2026-08-28 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 245.9 |
| ebd75d73-f595-3a31-ac73-f39b26805b74 | -8.948 | -62.3894 | 2026-08-28 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 495c4e6b-c4b7-321c-945c-9a62dd6780bd | -15.4788 | -53.9628 | 2026-08-28 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3ca855d3-6fe8-305e-ae1d-11b389bb0e2d | -13.3358 | -54.3407 | 2026-08-28 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 91c4c246-e104-353a-8894-c17cae564e54 | -10.9556 | -50.5311 | 2026-08-28 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 18e32bb2-e531-39ad-b3e9-03f3a497669b | -8.093 | -45.8128 | 2026-08-28 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| f3f9671e-40d7-3594-bf0e-1120bc1f2925 | -10.7975 | -54.0146 | 2026-08-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9ec7fd41-b30f-3de6-8dd8-48e08fd1400b | -11.8246 | -47.1729 | 2026-08-28 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b2777ef6-7759-39a2-9a6b-bb79cd267007 | -12.3041 | -50.5701 | 2026-08-28 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 267.3 |
| f077d644-2912-32ee-9b53-fef53d5bd83d | -12.0733 | -47.1614 | 2026-08-28 14:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 0e45d301-ad89-326f-a3e1-d3f519bb6416 | -14.4444 | -53.3806 | 2026-08-28 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4d3d9feb-e4c2-3126-b957-b38625538244 | -8.5968 | -54.7957 | 2026-08-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 4c27ad02-39c5-3c1e-b038-9f5bf760137b | -10.8996 | -46.6216 | 2026-08-28 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 16017c99-c159-3355-abbd-b84825010a63 | -13.3447 | -46.9304 | 2026-08-28 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 3a144c02-6ed2-372e-87b5-5a42a9cabd3f | -10.3202 | -49.9782 | 2026-08-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 39f6eaee-b3fe-3600-8874-e27fc20d27d7 | -10.4981 | -64.5005 | 2026-08-28 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 79.2 |
| fcc9188a-1bda-3a42-83f3-64f7e0bb4739 | -9.4758 | -48.1822 | 2026-08-28 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 115.4 |
| c8258860-3317-3e21-ad2c-5306f397c82a | -14.2402 | -51.7576 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| adb124e8-fb67-3839-93a2-f5a7de34183f | -11.7782 | -47.6697 | 2026-08-28 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e2c44658-2606-319c-9ef4-6e222de4de97 | -2.7303 | -47.0644 | 2026-08-28 14:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b85e0dad-be6d-30ef-afb3-00f67483e0f9 | -10.9187 | -46.6192 | 2026-08-28 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 6b02eec2-2efa-399d-b116-20d8ae229eab | -12.209 | -50.5601 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.1 |
| b1a7a637-4de6-3766-a24e-2448f4099a63 | -11.8239 | -47.2178 | 2026-08-28 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 162.0 |
| d4b8341a-2e51-31e7-bd9f-765219f1d089 | -10.9589 | -50.2958 | 2026-08-28 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 4ab8ea98-70ea-35d5-8fa1-4bd8fad0e05e | -8.164 | -46.1657 | 2026-08-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 618387bd-e8a7-3c22-971f-e46d38405ceb | -11.843 | -47.2152 | 2026-08-28 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 4f129649-09f3-387b-8fd4-a2fc163131f8 | -11.6773 | -50.4724 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6a6e9f0e-ddd4-305d-9f3d-2e5254b9ed9e | -6.857 | -59.4371 | 2026-08-28 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| c7f77508-1bab-351a-a896-9c7b7f48d143 | -7.4953 | -55.2862 | 2026-08-28 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| b2fc35ba-6bb8-369b-8cfb-c82fa123f6d8 | -10.7598 | -54.0179 | 2026-08-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 44c39a58-8063-37c3-89c6-20c355f30bb7 | -6.2693 | -53.1322 | 2026-08-28 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| a58bd26d-bc3c-3ccf-9e0a-71257fe29f73 | -8.5779 | -54.8172 | 2026-08-28 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 83763d62-049b-3933-9166-ea2a390b9bf1 | -13.4194 | -51.3945 | 2026-08-28 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 68cf9328-9c05-34bb-a1e1-f051181fc77f | -10.559 | -50.4876 | 2026-08-28 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 3287bbef-10dc-3766-a98d-e1203bb22067 | -12.0733 | -47.1614 | 2026-08-28 14:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| feeb5da6-3e12-37b8-ad1e-a921f3bed6da | -6.8755 | -59.4364 | 2026-08-28 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 32186177-f4d3-316f-b6d0-38d76f20810e | -11.2493 | -45.0501 | 2026-08-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.6 |
| 749d8b78-e32b-37be-8927-de8571ef34fb | -13.8752 | -54.1153 | 2026-08-28 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| ee79bc7a-f5b5-3a23-830b-967cdab2d6c5 | -14.6024 | -53.1508 | 2026-08-28 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b3a2575d-8115-37b0-a47f-7e27e44d100a | -12.1507 | -50.6313 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 98f94c8e-f15b-3bf8-9a18-addb407df924 | -7.5846 | -61.3232 | 2026-08-28 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 46983f5b-8853-3ecc-b14a-7d10dd5c8e5a | -10.8992 | -46.6442 | 2026-08-28 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d2f45819-c3b3-3396-a477-013a094d57a3 | -8.9478 | -62.4084 | 2026-08-28 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 864d281b-6329-302b-8bb2-2b44bfc7cdfc | -11.7786 | -47.6474 | 2026-08-28 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 5b641549-b591-3f17-b365-c7b414216237 | -13.5797 | -45.7753 | 2026-08-28 14:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| d98efc9a-0808-3129-9080-d0201b11194b | -11.8246 | -47.1729 | 2026-08-28 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 151.6 |
| ce59d0dc-27e8-3adf-a261-959d7cba420f | -11.2497 | -45.027 | 2026-08-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| cd79490d-a2f8-3d04-84d5-f8abdffe8a81 | -14.3182 | -51.7046 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 170.1 |
| c20b7780-b459-3172-8392-025df7a1573f | -10.498 | -64.5193 | 2026-08-28 14:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| b620a5a3-782a-305d-8b17-a16464ebe753 | -21.0372 | -57.8494 | 2026-08-28 14:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 6895064e-9c3c-3d56-bde6-d02372be28d5 | -9.9708 | -53.9419 | 2026-08-28 14:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 177.9 |
| 2ddbdeff-2e53-3910-8c23-d0950c6d0ae1 | -10.7791 | -53.9752 | 2026-08-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 763645fe-7cf9-3dfb-b5b2-9b32366d85d8 | -9.1525 | -49.9639 | 2026-08-28 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| ff84999d-5ba5-3c44-b012-93d97178af05 | -13.4191 | -51.4159 | 2026-08-28 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 7b95a5a0-6b25-3072-bf2c-42fa268bbf27 | -14.4842 | -52.1512 | 2026-08-28 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 257.2 |
| 03509539-056c-3c43-b9df-d6ad97a1202c | -7.603 | -61.3415 | 2026-08-28 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| a1012bbe-6df2-31ae-87cf-0e90468bc74e | -9.2284 | -51.5219 | 2026-08-28 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| ef8db936-748b-39e1-a37d-d52c4f07700a | -9.2282 | -51.5428 | 2026-08-28 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 4d9f998b-27bf-3678-9bf0-f6c836abcffa | -8.948 | -62.3894 | 2026-08-28 14:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 71292ce5-f73b-37ec-9039-87cf7e3489e7 | -14.9985 | -52.5925 | 2026-08-28 14:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 5089297b-c5be-333d-8c3a-803da19e6b85 | -15.4788 | -53.9628 | 2026-08-28 14:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 4eab8ac2-795e-3830-b4a2-b5ca99979cdd | -6.5865 | -55.4346 | 2026-08-28 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| c3cc66a9-c14d-3ebb-9716-00dc324a6aab | -8.0739 | -45.8372 | 2026-08-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| b5587cf0-111d-3e0a-85c1-90d2ddb8159e | -12.3038 | -50.5915 | 2026-08-28 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 7f021047-adb3-38bb-bc04-d5a5c2cd9d4d | -11.2489 | -45.0732 | 2026-08-28 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 2cb10169-a662-3a4e-ab7b-c635946b8cca | -10.7596 | -54.0384 | 2026-08-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 52df10dd-fe82-3892-b879-c2cb5db703b7 | -10.7407 | -54.0401 | 2026-08-28 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9fe381dc-320c-3e14-9221-068c692ddd46 | -8.0928 | -45.8354 | 2026-08-28 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 1f316d2f-2b8a-370e-9c8d-fe29d4ae5bb1 | -6.2692 | -53.1526 | 2026-08-28 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| d7ca3704-d932-3d05-a071-8681963f2967 | -7.1452 | -43.193 | 2026-08-28 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.3 |


[Clique aqui para ver as próximas entradas](README79.md)
