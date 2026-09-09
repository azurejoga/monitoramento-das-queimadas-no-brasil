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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48a2a10b-42b2-37c8-8321-ccca6152a90f | -5.6733 | -50.096699 | 2026-09-09 00:25:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41b55b2f-5329-32f9-9304-e745bd230c7c | -10.7248 | -46.004002 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e3bdfe0-4e69-3533-8b42-22ec6149de2c | -9.6902 | -43.454899 | 2026-09-09 00:25:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c95f1506-30b2-33b7-ac24-ed79f7c38dff | -4.437 | -54.833099 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8b71fd-c108-3587-b578-59b6cd532073 | -3.6793 | -54.533401 | 2026-09-09 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b33fbf8-3d3b-3d8f-9966-e6dc713d5786 | -13.2501 | -61.632599 | 2026-09-09 00:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0aa2a3-d627-3181-b68e-70ea57c3c2f5 | -3.1472 | -60.623001 | 2026-09-09 00:25:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d3b26b2d-25ba-387c-9a8b-4af5c2ff3b48 | -12.8458 | -44.379799 | 2026-09-09 00:25:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7fbbc25a-0b2a-3eec-bc98-f91bda10eb28 | -8.7363 | -62.3652 | 2026-09-09 00:25:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c2a74d92-d9c4-33da-81a8-9e7fb163f469 | -4.5765 | -56.237202 | 2026-09-09 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703080ef-c828-3b39-87ee-5d9037794dc8 | -9.254 | -45.645699 | 2026-09-09 00:25:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 34fabd34-4e4c-3985-a0c9-2217f2a78efd | -10.5405 | -47.1021 | 2026-09-09 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c7aeb9f-ec2b-35f3-8dfb-ece09d49e5c1 | -2.9272 | -50.4701 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7503372-5060-38bb-9033-81b2cd31f672 | 2.6623 | -60.1707 | 2026-09-09 00:25:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9ba839-03fb-33de-b4f9-9e0c53148c9e | -3.3618 | -59.417 | 2026-09-09 00:25:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d828369b-cd12-3b4b-9126-63483dd9ccf7 | -2.9328 | -50.449501 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfd72422-e893-30fe-b69a-b41bbc6c1535 | -3.5391 | -48.189201 | 2026-09-09 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5eaca56-886d-3074-99b8-4f782df12632 | -6.152 | -44.6604 | 2026-09-09 00:25:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f630cc1b-6257-37dd-938d-1c1604cf2541 | -7.1219 | -56.501598 | 2026-09-09 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6078a6-3b12-366d-8b0f-d8788d5efc95 | -9.7738 | -43.499802 | 2026-09-09 00:25:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12ebe8ae-13f0-3410-a0d9-27d0db9ca7cc | -6.7996 | -58.937099 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 742bbd20-af0b-3152-a900-9bc487cea628 | -10.7535 | -45.9533 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa3004b6-c8df-37eb-bd37-ec391f10a3c9 | -2.7681 | -49.469398 | 2026-09-09 00:25:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5b22c5a-b500-3df5-84ac-8dc1ad14b7f9 | -3.3693 | -59.4044 | 2026-09-09 00:25:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6146638-796b-324a-be56-3ab2450eae3e | -11.0009 | -45.084702 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3844a99c-cadb-348a-a38b-be079d469746 | -6.1471 | -44.640499 | 2026-09-09 00:25:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9766b9-3839-3759-aae6-51456889516d | -10.5 | -47.062901 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0533f3e1-40ff-369a-b472-e45c9c5449d6 | -3.15 | -60.635502 | 2026-09-09 00:25:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3942b4-7875-3e3c-8f1e-a896687f2ad1 | -7.0856 | -59.797001 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2bff361-ad5f-374d-8fbe-0691ac1d9974 | -10.7307 | -45.9445 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15d35569-02ed-361a-9521-1c12a8df22b6 | -8.0874 | -45.676102 | 2026-09-09 00:25:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2a2031-69cf-3861-adc3-1566df6c5778 | -3.2566 | -50.068699 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2efda9cb-c46b-3a22-99bf-0b884b4c4c9e | -4.9145 | -55.815498 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a875b0c-e8e6-38dc-aaf0-a08dbe6ebb83 | -6.3558 | -43.5811 | 2026-09-09 00:25:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92c5d815-3590-3980-bb86-0bad7898bbf1 | -11.6442 | -52.854698 | 2026-09-09 00:25:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5603c3b5-8b04-37f0-be17-0ff17f484806 | -10.5097 | -47.060398 | 2026-09-09 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1336b980-81c8-3639-a82a-1c07f16896e9 | -5.7591 | -45.065201 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a76b33d5-62a5-3af9-b314-adb9fecb355c | -10.5126 | -47.072102 | 2026-09-09 00:25:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 537e4427-0936-31eb-96c7-08bc9e4d91e0 | -5.3706 | -56.015999 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f954295c-6a0b-3b00-8342-90f5c30b09cb | -3.9614 | -47.5826 | 2026-09-09 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0ffd62a-8bd7-3126-80d9-59871a86f29f | -5.601 | -44.838001 | 2026-09-09 00:25:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f2dc6d4-8e26-3073-839b-1837c0302aaa | -4.4355 | -54.826199 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c97a510c-1d9a-36c5-a28b-36f60eb29c32 | -9.7588 | -43.481602 | 2026-09-09 00:25:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b3507e6-c71a-35af-b496-ce3b6b9bcb13 | -10.5028 | -47.074501 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c792ecf8-f3aa-3b96-b978-4229b90a6871 | -3.8083 | -55.884899 | 2026-09-09 00:25:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e2289fa-4284-38e3-8bda-3b4f8c74008d | -10.7404 | -45.942001 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9aea229d-e7a9-3839-8757-424b8a7cc14d | -3.8029 | -52.3997 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 676e4efa-4843-37b9-b52d-9b8e6a7c6d88 | -5.754 | -45.086399 | 2026-09-09 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c8f6eeec-f081-3388-9686-109a969a40cc | -3.7914 | -52.394501 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8cd1e1f-5625-3854-8935-9ad211f21536 | -2.56 | -54.731998 | 2026-09-09 00:25:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00a3cb50-8ce3-3a33-a8df-1fab1df6d1e2 | -13.2404 | -61.634499 | 2026-09-09 00:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5e98efc5-f135-3f6a-a572-e0899b7690af | -2.7323 | -57.144901 | 2026-09-09 00:25:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9da2418e-11fb-3eb5-86b2-1411b57029c2 | -2.5615 | -54.7388 | 2026-09-09 00:25:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab30699a-0b49-365d-b8ee-9c3f009498fa | -3.8536 | -54.300999 | 2026-09-09 00:25:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8b689bf-9ef6-3038-bd20-4de5182b4fd4 | -3.2322 | -47.232399 | 2026-09-09 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1429f071-b273-3114-92c8-ff54c15a488a | -2.7657 | -49.458801 | 2026-09-09 00:25:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8dc6427-abc8-3207-b362-79ba0c7967fd | -10.6474 | -58.7449 | 2026-09-09 00:25:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74b00462-c28d-326b-a1aa-d6346be17c48 | -10.2989 | -46.873402 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 513e5ae5-9e6c-3da4-8862-c96c5f370d4d | -14.2807 | -44.572201 | 2026-09-09 00:25:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5e02b3e7-2892-3440-95b0-ec19e9a116ba | -6.3995 | -55.230801 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e2cf83-4d7b-3458-84f6-032ec7753e65 | -10.65 | -58.757099 | 2026-09-09 00:25:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b8c30dd1-39c0-3a7a-885f-32fec142bf6f | -7.1317 | -56.499401 | 2026-09-09 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e7231b-2a74-3bfc-9c5e-8a68ddd18e4b | -3.2687 | -50.076 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f573dcd-fe5e-3ba1-a4fa-6c6d1856c150 | -3.6837 | -58.508499 | 2026-09-09 00:25:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa289bbc-d818-32b2-92bc-bd900a7d15e9 | -1.6105 | -54.907001 | 2026-09-09 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 171e8c36-ae1a-39ef-bdc5-b4281f96cd5c | -14.271 | -44.574799 | 2026-09-09 00:25:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c60ca2b4-00df-3942-bf4d-c1034aa26763 | -10.2891 | -46.875801 | 2026-09-09 00:25:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5f086c91-ecf2-34ea-aa71-f924284c366a | -2.9447 | -50.456402 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95df0859-f6b8-3465-9762-0cf0738ecfd1 | -4.0028 | -51.0257 | 2026-09-09 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a39359fd-f11b-3eac-ac0e-4dc7408f7fcd | -5.8043 | -53.815399 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9a899f8-8b12-3d7b-80eb-30e22c10190f | -4.5748 | -56.229801 | 2026-09-09 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9a1c540-8d40-303f-9cd2-ae745c8c3eb0 | -3.7773 | -58.838799 | 2026-09-09 00:25:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| afd8c792-383c-3302-8acd-189280ca00d1 | -1.6089 | -54.9002 | 2026-09-09 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a70098-56f8-331d-a211-82d55f581e75 | -5.8193 | -53.790401 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d21e89b-1f3d-3353-b266-31657a8c1bb1 | -10.737 | -45.928299 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e8551faf-b0e2-3aac-a85d-ea7662f3d3a7 | -10.9913 | -45.0872 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 41ed9622-ac8e-392f-ae9a-4ba5f4cd544b | -6.3896 | -55.233002 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb64583-579c-30d6-aa93-1e9b99f3b391 | -4.2912 | -49.073502 | 2026-09-09 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c5fe4db-1188-36b0-a953-82f3fa642d48 | 2.6645 | -60.161098 | 2026-09-09 00:25:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a5f9f3a8-5118-3b69-8e81-69ca74401103 | -6.7851 | -58.917301 | 2026-09-09 00:25:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5978dc6e-ccac-3e77-82ad-8c844025e3e3 | -6.2468 | -47.334801 | 2026-09-09 00:25:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c1e686e1-8218-3a7c-8712-fe26881d4c09 | -6.1617 | -44.658001 | 2026-09-09 00:25:00 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 517a465b-589f-3a24-b943-b1984637323f | -10.6598 | -58.7551 | 2026-09-09 00:25:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5448a311-e8b5-3d10-9252-fc0603d6d839 | -4.5781 | -56.244701 | 2026-09-09 00:25:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541bb4d8-6cb1-3d37-955e-02676188ab75 | -4.2962 | -49.094898 | 2026-09-09 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b0d260b-92b6-3c47-bb4f-1e49735b8f20 | -3.9626 | -59.353199 | 2026-09-09 00:25:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c44b85e8-24f6-30f4-bdf8-1e5541397aaa | -5.2185 | -55.979401 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c44666-b6c4-35ce-a76a-fb87d2b569ad | -10.9874 | -45.071701 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12481fb0-bbc9-3de3-a0ae-ce8da17f750b | -2.9489 | -50.4748 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e46d6f50-317a-3978-83a6-48548f1d1c3d | -5.8028 | -53.808498 | 2026-09-09 00:25:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcebe75b-efa6-38dc-be27-0c780ddb2a5c | -10.7438 | -45.9557 | 2026-09-09 00:25:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 625c4c8b-31d6-342c-9cda-fc9804ee0b35 | -9.7641 | -43.502399 | 2026-09-09 00:25:00 | METOP-B | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 580ae3bd-0800-3833-aa02-32ec71d7d86c | -4.3793 | -55.034599 | 2026-09-09 00:25:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 755d6f0f-ac07-36e6-8c68-aa64a9d592c4 | -5.3723 | -56.023399 | 2026-09-09 00:25:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 082f624d-f977-35a0-8ff3-55e007bb80d2 | -2.9391 | -50.477001 | 2026-09-09 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d203b8-84ca-3ea7-959f-9c0e22b4fd5c | -3.4341 | -47.262299 | 2026-09-09 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11be6b3e-eb34-3f73-955b-32f740f11a1d | -13.2443 | -61.655499 | 2026-09-09 00:25:00 | METOP-B | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 90456a56-c3d2-3b11-bda7-c89121b5a41d | -6.2499 | -47.347801 | 2026-09-09 00:25:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e2850f2-0998-34c6-a19e-66781c9c2009 | -4.0009 | -51.017399 | 2026-09-09 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04dc7ba5-1837-30e5-bcd3-6f1dde125716 | -1.612 | -54.913799 | 2026-09-09 00:25:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
