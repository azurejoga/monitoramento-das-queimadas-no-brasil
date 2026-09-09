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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc79ab22-069f-3382-bbcc-a98cce69e189 | -6.7875 | -58.928299 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a175eeb7-c21f-3741-af90-3c328d1240dd | -3.1347 | -60.612598 | 2026-09-09 00:25:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e99e0f53-b6b7-3baf-a334-5a3563c201ef | -2.937 | -50.467899 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 260524a4-88eb-36be-b8f4-87a7f6ef8bce | -6.3912 | -55.2402 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 784652e8-2fd4-3735-bfb8-d0a730d3b5c8 | -10.295 | -46.900002 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2b83a0-bb39-3462-a3f6-4947b7362e9a | -3.5458 | -48.1744 | 2026-09-09 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2afdec82-0387-306b-a1c2-c264d61124c1 | -2.8026 | -54.756901 | 2026-09-09 00:25:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9677eead-4d49-380a-9561-f0b53d5db415 | -4.3809 | -55.0415 | 2026-09-09 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d47a45c-ee1b-37c7-8041-da051dc6a989 | -8.7254 | -62.3987 | 2026-09-09 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.6 |
| fbdda3ef-2417-3373-94c7-bb36b978a4fd | -10.5314 | -47.0926 | 2026-09-09 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f69e088f-6714-3b3f-9a22-6dec688422b0 | -2.9391 | -50.4832 | 2026-09-09 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 2276ad28-c951-3435-ab19-60e3b440f6e4 | -6.3703 | -43.5898 | 2026-09-09 00:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 170c6861-74a1-3a75-bb0b-a48b711338b2 | -2.9392 | -50.4622 | 2026-09-09 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| da52a6ec-a219-3a8f-9651-b9627c0a3efd | -10.7574 | -45.9852 | 2026-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 8287444c-2bf3-351e-8bdb-55fa64a7d4c4 | -2.9576 | -50.4826 | 2026-09-09 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 34c6049d-5aea-3c19-9af0-7d7dae709806 | -10.7391 | -45.9422 | 2026-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| fb6072b0-6d3e-3107-843d-80cc484846b5 | -6.1723 | -44.666 | 2026-09-09 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 8dcd0276-6def-3de1-b04a-c24b8f863b17 | -6.1538 | -44.6446 | 2026-09-09 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| fa8dc046-1452-3e8b-a8bc-615a7e86d956 | -6.1536 | -44.6675 | 2026-09-09 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 787f4b0e-ef19-3aff-bfca-edb9adefde1a | -5.7756 | -45.0826 | 2026-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 8e40a1dd-6eb5-3aea-8f89-14d54134947a | -10.3067 | -46.8964 | 2026-09-09 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 79415792-4b54-3a2d-9935-53a2bff1f4b4 | -13.2485 | -61.6565 | 2026-09-09 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ede9c980-d652-300f-b086-c392785818a9 | -10.5504 | -47.0903 | 2026-09-09 00:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 01dd5c2e-cdb8-36d5-bd23-924bcc7bc180 | -10.7582 | -45.9397 | 2026-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| cf4ad802-067d-3886-ad97-33649a32a3ce | -8.7438 | -62.4169 | 2026-09-09 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 255e3a78-6ddb-3e8f-ab02-53a38b64b20f | -8.7439 | -62.3979 | 2026-09-09 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 8121527a-ab58-317a-bcea-c065beec4d65 | -10.7578 | -45.9624 | 2026-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 32b313f7-67d3-36d4-a2ed-4afa4792771c | -13.2483 | -61.676 | 2026-09-09 00:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 262206b0-3a84-3aed-b739-c2b31399f6d9 | -5.7571 | -45.0613 | 2026-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 4d245929-c50d-3963-9543-2bfca2c4a3b2 | -6.1726 | -44.6432 | 2026-09-09 00:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 0bd63d88-537c-3eaa-b593-29e2b1ddd2d6 | -5.7569 | -45.084 | 2026-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 3d385ae1-b628-3501-b7c1-588166f6952c | -9.7695 | -43.506 | 2026-09-09 00:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 73ff465c-da88-36a3-b5e0-0ad02a07523a | -5.7758 | -45.0599 | 2026-09-09 00:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.7 |
| dea79182-c73f-34bc-a86e-f75fb3f69e41 | -10.7387 | -45.9649 | 2026-09-09 00:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f387881f-1796-338c-a1ff-1781bf1243e2 | -20.47981 | -57.44385 | 2026-09-09 00:39:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 33f72d42-be75-3b76-ab35-9700b9005b94 | -6.1536 | -44.6675 | 2026-09-09 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 2d24fefa-41ff-367f-b9dd-45fd1c247342 | -6.3703 | -43.5898 | 2026-09-09 00:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 04723068-89e9-3c4b-a1f1-9f274df8bb8c | -8.7439 | -62.3979 | 2026-09-09 00:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 8a3fcae9-32c7-32b7-8351-d6de66a67ae0 | -11.0006 | -45.0847 | 2026-09-09 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d2683871-bc1a-346d-a522-dff386d30b50 | -10.7387 | -45.9649 | 2026-09-09 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 428c9fe5-9d8d-3c1c-a541-405dc16ffdd3 | -10.2877 | -46.8986 | 2026-09-09 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| e347560f-21b0-3d29-bcb0-c8a49bb6a881 | -5.7758 | -45.0599 | 2026-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 95dc826b-e96e-3749-b8b1-853f49211c8c | -6.1538 | -44.6446 | 2026-09-09 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9e6036db-a172-309b-ac33-2dd4626107df | -10.7769 | -45.96 | 2026-09-09 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 3996ac4c-0a06-342c-bea5-1eb3fb429fca | -10.307 | -46.874 | 2026-09-09 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 161486a8-d481-3c8e-8648-f46513b9c3b8 | -6.1726 | -44.6432 | 2026-09-09 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| f56d76d7-1a71-3d7a-8695-282d1149af5b | -5.7569 | -45.084 | 2026-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| dd6befd1-3f20-3d60-899a-a57108e505a2 | -6.1723 | -44.666 | 2026-09-09 00:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 7fbbbcaf-7d01-3771-bdad-a99c44cb3187 | -10.3067 | -46.8964 | 2026-09-09 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| d3f2e1fb-e68a-3bd3-8036-af00107eb3a3 | -2.9392 | -50.4622 | 2026-09-09 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 385ff661-898b-3c10-a3bd-9a4a4aeeb5ff | -10.7578 | -45.9624 | 2026-09-09 00:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 25c1c908-a283-3496-9030-cd63b4d84b13 | -5.7571 | -45.0613 | 2026-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 4893ac2a-a9ad-347e-84ed-fa2cc46c3972 | -5.7756 | -45.0826 | 2026-09-09 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 179.7 |
| 3478c86d-f5ed-35cb-b990-5da0cb89ffab | -13.25523 | -61.67565 | 2026-09-09 00:41:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e015cf2f-d1cb-34c1-929c-bc84596e67d0 | -13.24252 | -61.65445 | 2026-09-09 00:41:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 27.2 |
| e3db432d-5fbe-3c3e-a381-d2128278398f | -13.2566 | -61.66921 | 2026-09-09 00:41:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| faadf1bf-624b-3e9c-97e1-11ae70ff0db5 | -13.24397 | -61.6657 | 2026-09-09 00:41:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| ba32b171-9c17-334a-a6f6-ad6d77f7b9a5 | -13.23562 | -61.67827 | 2026-09-09 00:41:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 3d7ff579-5a01-3da8-98da-51fbaf62e09e | -17.10905 | -55.90858 | 2026-09-09 00:41:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| e179efa1-46a3-3762-9f03-409b68de3e8c | -12.43666 | -57.794 | 2026-09-09 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6c81410b-ae30-385b-b7f3-93994d0a29ff | -12.29803 | -57.40152 | 2026-09-09 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af661039-70e3-3176-a85e-9720a3020fca | -13.29038 | -61.78032 | 2026-09-09 00:41:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 471821e0-a440-3a42-af5e-8fc1d467c418 | -7.08484 | -59.81551 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7c1f2b43-6dc9-3072-9fef-7034ddbfcd09 | -8.98691 | -60.57779 | 2026-09-09 00:43:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 21c322fa-fe33-3965-87cf-d497267007d0 | -8.72443 | -62.40757 | 2026-09-09 00:43:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 87173b1f-2357-3773-9430-dc06a51b024c | -4.58208 | -56.25605 | 2026-09-09 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0720abde-5136-3e12-9f4e-abc8b0506385 | -6.63638 | -59.43485 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0075b471-abbe-30cd-a608-41cc2740971d | -7.12015 | -56.51186 | 2026-09-09 00:43:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 25738ba8-2373-3943-a196-871c780639d8 | -8.74234 | -62.39416 | 2026-09-09 00:43:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f46bcb51-7ce1-34a4-834f-ed33f8be3651 | -5.44757 | -60.23713 | 2026-09-09 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 18cc1abb-a776-379c-b12b-18e4c2315327 | -3.81576 | -53.77962 | 2026-09-09 00:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| be72f0c6-649f-37fe-bea9-300a734c6f97 | -8.74521 | -62.41567 | 2026-09-09 00:43:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 895e3bf1-6f40-37db-99f2-d317580122c2 | -4.38091 | -55.04492 | 2026-09-09 00:43:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| a44d6ab7-c79a-3914-8aaf-3d62b6a708df | -5.22137 | -55.99481 | 2026-09-09 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4a6d64fc-e4bf-351b-81ed-7241220df23e | -10.65474 | -58.7693 | 2026-09-09 00:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 04321c5a-966d-3c9e-b905-821576fb0224 | -6.86402 | -56.58024 | 2026-09-09 00:43:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 78358cc4-456d-34cd-ab64-4653e1016d49 | -9.49734 | -60.33096 | 2026-09-09 00:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d22b6b8c-bd56-3b42-8f79-2ce7c5c4ecc6 | -8.98814 | -60.58691 | 2026-09-09 00:43:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e6593daa-d930-3833-91b4-f6ea4ee57fe3 | -8.74377 | -62.40488 | 2026-09-09 00:43:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 240c8942-0147-3bc6-8e82-a5eb94c75f10 | -7.12187 | -56.52343 | 2026-09-09 00:43:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 6dd61102-f7d4-3788-ba28-fe472f4084ac | -8.72585 | -62.41837 | 2026-09-09 00:43:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| aa8394ab-e857-3f9a-9743-4b21c342677e | -11.56848 | -61.65466 | 2026-09-09 00:43:00 | TERRA_M-M | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5f4d61e1-1251-3d4d-b0a3-28e9e439967e | -6.79992 | -58.95948 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0419665e-e0f1-347a-bcd6-269dfbab40eb | -6.38939 | -55.25299 | 2026-09-09 00:43:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 63831019-db93-3beb-83dc-99736643c0e8 | -6.63761 | -59.44372 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 9ab8d924-fd45-3f1f-8a7e-1eaa0292c966 | -6.37289 | -62.4985 | 2026-09-09 00:43:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 644f0750-64fc-31eb-b2f0-6e08267a6076 | -4.89678 | -55.91243 | 2026-09-09 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1e5e9e7c-93d1-3f7d-bb1c-70fcf3d4ba11 | -8.7574 | -62.40772 | 2026-09-09 00:43:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e18a24bf-968f-392b-a5f6-caa0eae410d3 | -8.75345 | -62.40359 | 2026-09-09 00:43:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ba53908d-3d77-3c9e-8c36-d27eee464d60 | -6.79865 | -58.95039 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| c55a6ab7-fd12-3660-9a1e-a57c211ed18a | -7.08606 | -59.82432 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b8669989-1cf1-3339-ae80-24b3d524de97 | -6.78847 | -58.94261 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 03d7fb3e-c920-37d7-9de5-c43ca9cdc9af | -3.81259 | -53.75807 | 2026-09-09 00:43:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| a3645ec6-e33f-3512-88de-73f69ed80f2d | -6.56214 | -62.89994 | 2026-09-09 00:43:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| a15f7692-45ec-3212-821a-a8e3f6b3072f | -6.75532 | -58.96599 | 2026-09-09 00:43:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| aa753f1b-4aee-3675-b490-ea89ff2a1f42 | -4.58012 | -56.24285 | 2026-09-09 00:43:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5d003265-ee25-30d0-9bcb-b258982e1fd8 | -9.93201 | -59.60888 | 2026-09-09 00:43:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9f3b18a5-4c13-329b-9bb4-2ffdb4ee21e6 | -4.89846 | -55.90568 | 2026-09-09 00:43:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 32e77e92-7f93-3ae5-9aa7-bfc8c64de3c0 | -5.59479 | -60.24592 | 2026-09-09 00:43:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c13469ad-016e-37b1-aab8-84552c4c86f9 | -9.43267 | -61.02062 | 2026-09-09 00:43:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README5.md)
