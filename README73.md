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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e89a9589-d0a4-3414-884d-97f590d4b1d9 | -3.4003 | -61.3087 | 2026-09-03 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3be99fca-c45f-3004-a681-ba530a093eba | -3.4002 | -61.3465 | 2026-09-03 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d643a6fe-7bd0-3b15-bb22-01a73be65a09 | -8.9144 | -70.5816 | 2026-09-03 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 41.7 |
| f23fff9e-1dfa-3601-a39d-32185a8ac222 | -10.5254 | -50.1709 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 4084515b-7f59-3829-9704-e62f09db899a | -10.2212 | -50.3303 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 85f2715f-046c-307a-ae1f-451af6331e4f | -10.9592 | -50.2744 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 9cd3e2a3-d623-3122-9fef-b055c94bb2f8 | -5.1791 | -60.2809 | 2026-09-03 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 770eeb5c-7857-32ce-b321-5bdc1bfc1e26 | -19.1144 | -57.3823 | 2026-09-03 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| c6ccdc2c-960c-375f-ac13-bdcd644fa94f | -6.6765 | -58.7492 | 2026-09-03 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6f450772-82ee-36f6-9a11-340d5a8863bf | -14.2369 | -51.9498 | 2026-09-03 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 1c8fb561-2a24-315b-b251-b0db265ed466 | -3.0164 | -61.4848 | 2026-09-03 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 224.3 |
| 087330c9-f44a-3fd4-9af9-546d05b45ddf | -10.8206 | -50.7159 | 2026-09-03 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 76b8f8b1-b19e-3c5b-b690-e7084e09cfd1 | -7.0243 | -59.2181 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2c70fe90-ea25-3900-90ec-80ac14f6814d | -19.1147 | -57.3615 | 2026-09-03 17:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.5 |
| 8b0e1978-64ce-3f53-8fc5-0605e4919844 | -3.2181 | -61.1418 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 7372fd24-3086-3560-948b-b0eafdc95fe4 | -17.0878 | -56.8534 | 2026-09-03 17:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 239.7 |
| 63451281-89a5-3dc4-b8ba-abc4feabc338 | -5.5649 | -60.193 | 2026-09-03 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 7d0ce993-9983-3d3a-bbdc-20c46b7a9e12 | -11.6199 | -50.5004 | 2026-09-03 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 67f08a36-6782-34ac-8311-8533af2fdc5d | -6.6015 | -58.9651 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| c16254dc-2fa8-3fbf-9427-b5bf19c92f01 | -6.8062 | -58.6469 | 2026-09-03 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9bfe9bc7-4a5e-36b5-b82b-83eec25f421a | -8.8026 | -71.06 | 2026-09-03 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 80.1 |
| cb5e1b3b-bba7-340f-85b2-400db81f6a79 | -8.5542 | -63.1814 | 2026-09-03 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a181e874-0db7-339f-9912-231a3bff1fc2 | -8.615 | -54.8348 | 2026-09-03 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 07faec36-ef3e-34f0-94a5-62744da48f1a | -5.565 | -60.1739 | 2026-09-03 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 134.6 |
| d205b739-11ac-3098-9de4-d505d3bd8390 | -10.746 | -50.6386 | 2026-09-03 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f35d7f19-6181-391c-a4b4-f3f58c2dc371 | -6.1361 | -59.9063 | 2026-09-03 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 026b7ef6-df65-3fed-b703-0f8cf7c2de16 | -6.7279 | -59.4423 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 6b60ed31-4703-378b-a40c-96e9ca95c757 | -10.5793 | -50.3789 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| cb8aa285-9af9-3fb2-898a-ab9e400f61d6 | -8.7804 | -62.4913 | 2026-09-03 17:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d07f90f6-2b34-36b1-9e25-c69196861c7d | -6.9872 | -59.2582 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ac39c945-1326-395b-b5cb-d5a06201bc87 | -10.8614 | -50.4985 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 633b62c9-3854-3bcc-8d01-4fb65df48a99 | -6.6357 | -59.4459 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 197.4 |
| 5e01f40d-dc47-3d99-a169-e7200398ffe9 | -6.7463 | -59.4416 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 4e94376f-afec-3034-bc20-f5d5eb1b6846 | -8.7656 | -71.0971 | 2026-09-03 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 45065644-5293-356b-99d4-f46cff7f2d92 | -3.1633 | -61.1238 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 184.7 |
| 537fcf6d-a503-34cb-a44c-cfefdc4e1380 | -3.7645 | -61.7548 | 2026-09-03 17:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5822d601-279d-3d1f-a2ca-188e82f3f094 | -10.127 | -50.3184 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 7d61d843-871f-3c3a-9b71-fecf965ebdbc | -10.9565 | -50.467 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 018316b5-8e64-3f9e-8ed3-a14381dda8c3 | -10.9755 | -50.465 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 769648a4-5227-3ac1-bdf3-cabad449c0af | -3.1449 | -61.1808 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 8275850d-c668-3162-80de-f8616cc40ca9 | -11.6389 | -50.4982 | 2026-09-03 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| dc378631-40d1-3e25-ad8a-26f7692006f1 | -3.0904 | -61.0871 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 27ddada3-44c0-3a5a-b5e5-c772f0bb32aa | -14.2562 | -51.9472 | 2026-09-03 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| f960567e-0427-3092-af62-c26132aed98b | -10.9562 | -50.4884 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 875006a7-197e-3992-978a-1e6daaed4755 | -10.3583 | -49.9528 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0a39bb5d-25e7-30c5-ba59-6fd2b986e7ec | -3.7828 | -61.7545 | 2026-09-03 17:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| be6a5a84-e1fb-3987-81d0-4a9202372a0d | -10.6472 | -61.7741 | 2026-09-03 17:40:00 | GOES-19 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 347.0 |
| 445c92d4-340e-3f97-8c52-cffc78476823 | -10.3959 | -49.9703 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6901d358-4f29-3ade-9f65-2531d5e818a7 | -3.1998 | -61.161 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 64c9cc4d-cf7b-3b71-80b6-768d97b446c5 | -3.7462 | -61.7552 | 2026-09-03 17:40:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| b3a08440-d635-338c-a417-578668ed80cf | -9.12 | -61.6011 | 2026-09-03 17:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 50bc9043-a905-3795-b631-847cde750ff6 | -6.6766 | -58.7299 | 2026-09-03 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9a535404-06f6-39c3-9deb-1d31d5f99027 | -8.6667 | -62.9314 | 2026-09-03 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e243b29d-814d-3088-8ae8-f2a9f528f156 | -11.6573 | -50.5389 | 2026-09-03 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3e54a22a-e514-3c79-b887-b0b6d719f3e7 | -10.5983 | -50.3769 | 2026-09-03 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| aacc8100-8185-3c48-97c9-fed8bf7f89a1 | -15.2275 | -56.3716 | 2026-09-03 17:40:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8f722cf0-0312-31bb-bb59-09509a43002e | -20.8633 | -57.3916 | 2026-09-03 17:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 30723429-d8a5-30c0-bab5-b9aaeb4a8a01 | -3.2179 | -61.1985 | 2026-09-03 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 193.6 |
| 940a224d-ed03-354c-a222-94fd28763087 | -11.4895 | -50.3225 | 2026-09-03 17:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| a477c525-77e0-385f-b5ef-f438a9f4ca6d | -6.7123 | -58.9412 | 2026-09-03 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 34730252-438c-30d5-b027-99314a7ae1a0 | -11.7722 | -50.4829 | 2026-09-03 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 7304d4fb-8d31-3b4a-bf12-f0fd4776e6d0 | -4.9329 | -62.4265 | 2026-09-03 17:40:00 | GOES-19 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 7651a518-a44d-3ba7-878a-f9d472695e98 | -6.4114 | -60.0498 | 2026-09-03 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| a922e885-a96d-3af1-af99-ddfa405b4090 | -8.6853 | -62.9307 | 2026-09-03 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 99.7 |


