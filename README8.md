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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89631004-c79f-3196-8d9c-e8540d474ca5 | -7.9121 | -61.7314 | 2026-08-19 00:59:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9959ea4-440b-324c-bc1d-b7a27f85db53 | -6.6856 | -58.939701 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d27d853-c8eb-3c05-be69-ea69c57d21bb | -8.8947 | -60.565201 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0d8e49-7f39-394d-91c6-834d19cb3c51 | -8.5503 | -54.740601 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1e2d68-df7f-3dca-8662-150c8b073bf9 | -6.6074 | -58.957802 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| edb1bf1b-1665-32a7-8b94-e7f92515e116 | -6.0755 | -57.915699 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98d54639-2305-318f-9a1a-1a02be9d0b82 | -15.878 | -55.5602 | 2026-08-19 00:59:00 | METOP-B | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 314e13a9-d8eb-3e47-abdf-d8ff56b45454 | -9.405 | -60.5891 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6f9235e-4e6f-36ee-a614-87c37d515877 | -11.2215 | -55.076401 | 2026-08-19 00:59:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3f5942-fe6d-319c-8e89-1eadce1744fa | -6.6054 | -58.9496 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 36e49453-141c-3105-a5bc-28b160f25456 | -6.7564 | -59.1558 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a84bdf02-6184-3ee7-a247-4e51f253ca96 | -11.1954 | -54.012901 | 2026-08-19 00:59:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7ccd445-05c5-32ce-b5c7-9bd4c760d54b | -15.3158 | -56.4468 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 199bf6c6-b920-358f-8e6d-11c6e42fe613 | -10.6282 | -51.620399 | 2026-08-19 00:59:00 | METOP-B | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ace1b6fb-d902-3a37-8dae-f839b3fa0b2e | -9.0701 | -50.8036 | 2026-08-19 00:59:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6750015-81ca-35cc-8cad-2b9dbf222c21 | -6.875 | -56.417801 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbe64e92-7e22-397f-b155-e8714d24d386 | -9.2001 | -60.776001 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55192d0a-d7e1-32e8-a31c-4bb01344f20c | -8.9518 | -60.544701 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d5b7558-87ed-31dd-8584-56df84e0d1dd | -6.8318 | -56.452301 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0c1786-d06e-3284-aaf0-13a109ff34d4 | -6.7835 | -59.451 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1a264dcc-1211-30c0-9e57-1e829493f9cf | -5.9967 | -57.843201 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1812c149-4377-38ab-ba1a-7c21f2994c91 | -9.2856 | -56.886002 | 2026-08-19 00:59:00 | METOP-B | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a63621f-4a07-36d4-bd21-18a77bd0dd95 | -6.1205 | -57.711899 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df528ce2-88db-3877-9a95-e5d549b5597a | -6.1394 | -57.880699 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7acbeb20-fe2c-3159-bbb5-7acc67b172f9 | -8.5754 | -54.6749 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec5a5a21-eb20-3f4c-bb3d-f7f81d1745ee | -9.4403 | -60.290901 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d384fdd2-d783-3304-b4ed-759b2cd2a458 | -9.4148 | -60.5868 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2fe1420-b7f1-305e-9cab-d8a7c7f00a88 | -5.9892 | -57.855099 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a0e57a-4be3-3604-b09c-ae3596f22bd4 | -6.0035 | -57.872002 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd628894-5717-3504-9c76-59e903f21e56 | -6.6497 | -56.422901 | 2026-08-19 00:59:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3bca812c-1f2b-3ece-9b10-faf2c8c9393a | -5.4945 | -60.119202 | 2026-08-19 00:59:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd1632d0-2f90-37aa-b67d-39bf9dd4e5c5 | -7.4378 | -59.784901 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 68196434-8660-387d-a1b0-456427082fe8 | -6.008 | -50.1894 | 2026-08-19 00:59:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5859082c-9254-3054-aaa3-844e3fdccc05 | -19.741501 | -57.937199 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1004904f-045f-3192-a811-6940b49b1078 | -6.8474 | -59.014801 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c07e110-dfc5-3e35-9a72-84da7c5d8c6e | -9.014 | -60.500702 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a74f0251-f1e4-31fa-87f2-4363a0ce106a | -8.5732 | -54.749802 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 972f4c4c-e846-3a12-b30b-99a5a77f17d2 | -11.2312 | -55.073898 | 2026-08-19 00:59:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87ed926b-39f1-3706-87a9-5c6ec2c660a5 | -8.5795 | -54.733398 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9a0162e-179b-3817-93a7-2cf7bb5ac3c5 | -6.1034 | -57.858799 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18f2e9ea-0eb3-30c7-b039-afeacf00c93e | -3.2193 | -61.253601 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e594029a-1761-392e-aa26-f7daecd098c8 | -6.9081 | -62.900299 | 2026-08-19 00:59:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01f88a00-84f1-3845-b414-be2a4b94559d | -7.1135 | -59.764198 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b2ea5e7c-3a5b-3d3d-bd65-97d93759eb55 | -15.2755 | -56.494701 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1182d15c-0f89-34c2-8da4-ef785f36d8de | -6.7817 | -59.443199 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59918fbe-b31d-3390-8335-b1e2e067c06f | -6.0387 | -57.802799 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e402189-fbc6-3645-8de8-0b2ad03324d4 | -15.306 | -56.449299 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e09850f-e0c8-385e-8579-8cf9f6d38520 | -16.2523 | -57.660599 | 2026-08-19 00:59:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adc787b3-116c-3df5-afbc-36698d16ce76 | -9.4188 | -60.422699 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9134c8b9-5021-303e-b54c-357ea4740623 | -9.0109 | -60.441799 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d09960f5-6cea-3923-9bc2-287fd68b1a94 | -6.4438 | -52.742401 | 2026-08-19 00:59:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c89847-ebb5-35ff-b6eb-057525c917d9 | -8.506 | -54.854401 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f40440a-b1db-32d7-9d89-02b808771a92 | -6.7639 | -59.455601 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b06f7076-38dc-3362-8d78-7669920f5a2f | -3.1015 | -61.188999 | 2026-08-19 00:59:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdadb47f-d8ca-3f5b-bbf4-04acfc4433d4 | -7.0474 | -59.835098 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f812713a-a4dd-3f99-be5e-1d21bb2cb410 | -6.3495 | -54.915901 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f83d33d-9a30-3a6b-ba8a-f855ea02eb75 | -6.1056 | -57.868401 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b511f73f-c9df-30b7-a54f-c5ed264a18a5 | -10.8805 | -57.1259 | 2026-08-19 00:59:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 717d3b0c-3251-3cf5-841f-c15d4587b828 | -9.0172 | -60.5149 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 693d56ca-8e9e-3abf-8433-5e1dd9275ccc | -8.5309 | -54.745399 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cef664b-a35e-3c97-9f6b-1618279294e6 | -9.3952 | -60.591301 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd6ff11-37a2-33b5-8467-db0db2c44db0 | -6.0042 | -57.831299 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bfd8e79-00b0-3b3e-817b-f7aa391505d7 | -9.4019 | -60.575001 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9bfb1c26-fc6e-3037-a646-ffec6e116b72 | -19.751301 | -57.934799 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0810d82d-ba1e-3446-82d0-c426c81c7d68 | -7.4263 | -59.779701 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 226ee831-4e50-3180-8c5e-5b9e93d0ad00 | -7.0606 | -59.848 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 22550014-dac1-3cb3-9d46-9499ea48fd97 | -12.0027 | -53.445702 | 2026-08-19 00:59:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a01ffd5-2015-31c6-a4dd-05f2071433f3 | -6.8824 | -59.032501 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e5a1e4ce-924c-3ef4-bb95-6a8de923f47e | -9.0042 | -60.502998 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2d91e1c-5a09-36f1-bd6b-445bf2099ff1 | -6.8012 | -59.438702 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eca62702-46cb-3419-9ae9-a2533479ffb8 | -8.5692 | -54.691399 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a51b8f9-db8e-3b76-b87a-6f394fb74a67 | -6.8712 | -58.940102 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad2331e-28f2-3c07-9370-0467a37130a8 | -19.0613 | -57.349899 | 2026-08-19 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ca44507b-8ce8-394e-9e53-d30bca04af50 | -6.7032 | -58.926899 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e037cd4-650d-370b-8e7c-a7b315ee0361 | -9.2179 | -60.808701 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db88213e-acb5-3611-bb0d-454e1ecad2e6 | -6.6849 | -59.069698 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5e4d38e-146e-31aa-881a-e5935b3bc516 | -7.5424 | -55.593899 | 2026-08-19 00:59:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62a58dcf-538c-3b22-8cf7-f6964f98635f | -6.7051 | -58.935101 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b8af395-5b43-3025-acb5-81e37b76b452 | -15.2776 | -56.503601 | 2026-08-19 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07a8de58-689a-3d32-a449-bb631ce71a75 | -8.556 | -54.679699 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9ae3d17-fd90-3b17-bdbc-e19d243c52ce | -8.9584 | -60.5284 | 2026-08-19 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11acb6f1-5b1f-3101-8ea3-f764645d2585 | -6.0185 | -57.848301 | 2026-08-19 00:59:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5a0ec39-d5dd-3ac8-8be9-f8ab8524691e | -21.530899 | -52.004799 | 2026-08-19 00:59:00 | METOP-B | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9ce7b2d7-fb69-3fcd-85a1-eec57911bf51 | -8.6502 | -62.823502 | 2026-08-19 00:59:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c3fa228-c2fc-341c-b983-f991a5dc285c | -6.8591 | -59.020699 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aecf34df-9649-3d2d-9469-abeafa2c1795 | -8.524 | -54.717499 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2934015-6da5-305a-8dfe-e437f29eb526 | -6.8922 | -59.030201 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4350413-1553-3abd-8c6f-8f9a9a700aaa | -9.4204 | -60.429798 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ceb1e490-107a-32cc-8fe6-d1b10bd54f05 | -8.5863 | -54.761299 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38b4588a-445b-33a4-b974-a648c41b8599 | -9.4269 | -60.413399 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f7409914-c3b1-3af6-bb69-dd61ba65dc9c | -9.4069 | -60.551601 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05fe5226-0acd-3d11-bfea-1e765a148a34 | -9.3889 | -60.563202 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7e5ef1bd-f726-38b9-8b2d-a8264bac4717 | -7.0572 | -59.832901 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5666d076-9e3f-3b12-a05f-70ffdf61bf10 | -8.5532 | -54.7103 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ec21bb1-1b11-3b08-a5bb-c0095a88962e | -9.3873 | -60.556099 | 2026-08-19 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b4d4840-25ad-3dc8-ad9d-5888a6b7a4fa | -6.811 | -59.436401 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e6c86996-4c45-3cf8-a810-daf293b0eaee | -8.576 | -54.719501 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9c22abd-a65a-3836-8482-46e25bba630f | -6.3424 | -54.886398 | 2026-08-19 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 656ad50b-4780-30a5-a465-c81227ba098f | -9.1176 | -61.597301 | 2026-08-19 00:59:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d3b593a-5c5b-36b7-b974-17274e6663ca | -6.7466 | -59.158001 | 2026-08-19 00:59:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
