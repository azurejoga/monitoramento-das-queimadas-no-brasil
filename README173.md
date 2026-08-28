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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f17ebba2-bd80-3027-8a8d-409e160a60e3 | -7.4953 | -55.2862 | 2026-08-28 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 7ee03fdf-ef73-3806-8fd4-e14f7a917d17 | -8.87 | -66.8935 | 2026-08-28 19:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ec6d98f5-849b-3a1a-9676-6deac8e22cd9 | -6.857 | -59.4371 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 9fee63b8-1522-33b4-a879-b674bff8831a | -11.6212 | -54.5947 | 2026-08-28 19:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| cfd3bb54-4ad9-3d5f-8954-ca0019575162 | -11.2317 | -53.9958 | 2026-08-28 19:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 91406c8f-6558-3dc7-a8fd-716dcc6acdb6 | -11.2302 | -45.0528 | 2026-08-28 19:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3ec3ea8c-8d19-3e4d-8ae9-eb20b27d4b3e | -11.0247 | -49.6656 | 2026-08-28 19:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| dc5faf1f-f54d-3593-b1ba-c38d373e1918 | -9.0012 | -57.5585 | 2026-08-28 19:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 860d60a5-c849-39c5-9f50-7a350ba57a85 | -13.4707 | -57.0574 | 2026-08-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e9c44f81-cb00-3a45-bd15-6e510d865b66 | -7.4735 | -61.3846 | 2026-08-28 19:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b96a4eea-b8bb-3f7e-bdd4-d99ba0413d8f | -2.7304 | -47.0424 | 2026-08-28 19:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 2a5df4e0-d778-3e4a-b51e-62c1f928e38d | -8.5785 | -54.7566 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 834c4c3f-c253-3c5e-8110-f7826606a9db | -12.9244 | -59.8843 | 2026-08-28 19:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| e21d02d1-87b7-383c-8d33-2d07a6de1d2a | -8.5969 | -54.7755 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 184.5 |
| 47ca1b96-9269-3fed-ac11-c5df5d1dd586 | -3.8947 | -60.9399 | 2026-08-28 19:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ad18ca39-5301-3663-b55a-acd0502bbc1a | -13.5991 | -45.772 | 2026-08-28 19:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 562d57e9-0564-3645-9684-6c0e4ad11a16 | -4.924 | -55.7645 | 2026-08-28 19:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7a75ad1a-a273-3206-b899-67d3301a6130 | -12.7608 | -44.2373 | 2026-08-28 19:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 57a3d110-8e5d-393b-bb8b-f889ba6d2366 | -10.3205 | -49.9567 | 2026-08-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| dbcdc315-2ff3-31ca-b19c-795e45b32abf | -9.2477 | -57.0697 | 2026-08-28 19:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 5e6beb27-6a98-3e84-b521-00ccdf88e078 | -9.7874 | -43.5742 | 2026-08-28 19:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| a15bf88d-2203-3b42-aa62-1a9792bcb19c | -7.4734 | -61.4037 | 2026-08-28 19:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3e842c86-4755-31a8-aa04-1fad4dca2d5b | -12.9052 | -59.9053 | 2026-08-28 19:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 108492f4-d155-3fc6-abd7-beaf40ff1b75 | -6.9521 | -58.9506 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| ef22927b-0e59-398c-8dc7-5a8375d87484 | -12.7797 | -44.2576 | 2026-08-28 19:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 234.9 |
| fb7cece2-b39e-361c-a4b9-863c4bbe56e4 | -11.2314 | -54.0164 | 2026-08-28 19:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 9b7b20d5-2b9e-3cc3-9996-7e0816246b8c | -6.7514 | -55.6654 | 2026-08-28 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| aaac82b9-e2d8-3bb8-9918-d45e345b0995 | -8.5365 | -55.2826 | 2026-08-28 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 9603392d-3069-3d1a-bfe7-c0a4d976fdcb | -6.5322 | -55.2577 | 2026-08-28 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| b9f1a8ce-fd22-3fa9-a01c-a92e464f3af4 | -8.5971 | -54.7553 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 92393986-3546-3e87-bea7-f281ed66cc90 | -6.9336 | -58.9514 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 3b57e8ee-b732-315a-ae46-38b5beb5c1e3 | -9.1525 | -49.9639 | 2026-08-28 19:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 41b02dc9-540b-3c1b-ab39-fc47e446d6f8 | -9.1895 | -59.6364 | 2026-08-28 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 458de4a6-3b9d-35a0-8aa3-dc043cddf923 | -4.3022 | -59.4634 | 2026-08-28 19:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 49b2db46-d117-3910-b1c3-b62eb50dfc86 | -11.2128 | -53.9976 | 2026-08-28 19:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 293d821e-6ab6-3dfe-8ae3-0450f25cac7c | -9.1978 | -61.0809 | 2026-08-28 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.3 |
| eaa397e1-968b-3430-95dd-35c4994fb922 | -9.2475 | -57.0894 | 2026-08-28 19:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 450b27cc-8510-30ff-8580-8b12c3a4e035 | -9.8065 | -43.5717 | 2026-08-28 19:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 2f5733a4-7c71-3134-89a2-834e98d7f239 | -9.1711 | -49.9835 | 2026-08-28 19:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 725dbf38-535b-3a75-828b-d60411da03cd | -13.4901 | -57.0355 | 2026-08-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| a1a30605-f9f4-3bf6-8bd4-a79968e0a76d | -6.894 | -59.4164 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| d1d97473-e53c-3274-a324-2219fa1346fc | -13.471 | -57.0373 | 2026-08-28 19:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 3780f2d2-560a-3f4c-a590-5fdb6c0c3b0e | -6.1657 | -57.7793 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| a00a2564-76a1-3c00-8b7f-cb8d14109081 | -3.1998 | -61.1421 | 2026-08-28 19:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5a87be7a-d5d9-35f9-a948-4d2003c02e64 | -12.9054 | -59.8857 | 2026-08-28 19:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| ad3c9ba3-3874-36b7-8535-8d54161379c2 | -9.0198 | -57.5574 | 2026-08-28 19:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 30652e62-93b0-3dfb-8b26-b5019c2399fc | -6.1841 | -57.7786 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 4928ee6c-9c1e-324e-938d-6a5d7e67b19f | -10.9377 | -46.6168 | 2026-08-28 19:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| dec9b878-7ff6-3074-b894-87f90f510086 | -4.3021 | -59.4826 | 2026-08-28 19:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 17f70b50-cd4f-3fe7-9fa2-0fb827f8aa82 | -9.2285 | -59.4017 | 2026-08-28 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| fd758157-0de6-3931-bb01-c41cdbd121c0 | -8.5975 | -54.715 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 0220284c-a9a4-3b49-bcc4-010ce4d9afc3 | -6.8358 | -59.9379 | 2026-08-28 19:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 4130539b-564a-375f-ac0b-c3fbf869d789 | -6.1656 | -57.7988 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 156.7 |
| c56b1495-a874-37d1-85b7-5bedc7ef5ec0 | -6.8569 | -59.4564 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| b424087d-1fc9-3490-9a22-64170ee20467 | -14.1645 | -52.8269 | 2026-08-28 19:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1078de74-4f40-3ef6-b847-25dc51dd7e43 | -9.02 | -57.5377 | 2026-08-28 19:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| e8e91603-2fa8-34a1-88eb-59f28326512b | -8.5781 | -54.797 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 7f9c48a9-1512-3ee9-8fd5-1ff007d908de | -6.1473 | -57.78 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d23bcdac-f64f-3ced-b5f0-df95810efcf8 | -14.1835 | -52.8456 | 2026-08-28 19:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 9f23139f-aaf3-340d-9971-222d51068e68 | -6.8756 | -59.4171 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| f271eea5-3a5b-3ca0-9b63-852e9f8a6fd4 | -6.5323 | -55.2378 | 2026-08-28 19:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| b4ae3ea0-003b-3f76-a27a-e28502c95bb4 | -6.9335 | -58.9707 | 2026-08-28 19:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 2f388160-8e41-3d26-a553-bc77fabf015f | -4.1696 | -42.4346 | 2026-08-28 19:30:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 101.9 |
| a81d8fdd-c151-3d13-921c-8bc64645f3ca | -9.9708 | -53.9419 | 2026-08-28 19:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 161.2 |
| e689e626-69ad-3754-83be-3569fc29b36e | -9.1976 | -61.1 | 2026-08-28 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 760b63de-3556-39cd-a5e3-caff2b0cca79 | -9.1714 | -59.5793 | 2026-08-28 19:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 801fc3ed-3001-3aa7-977e-392c4aec7dcc | -6.1472 | -57.7995 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 194d537a-8c63-313e-bbd0-bb4b218f8150 | -6.8357 | -59.9571 | 2026-08-28 19:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 415bb4cb-20a0-317c-ac86-3223b58c5c33 | -7.3663 | -55.1734 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| cc0e5b67-2167-3f3f-8bbc-c21751e4ea14 | -10.9187 | -46.6192 | 2026-08-28 19:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 458d5a7f-089c-312c-a004-2dc001bef5e6 | -8.5783 | -54.7768 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 04b991bd-4147-367a-84b8-3af9c485351f | -14.9193 | -56.3237 | 2026-08-28 19:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 191.7 |
| e136ba08-3557-3f21-9322-7d02e6217c58 | -6.1101 | -57.84 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f0eb2008-ec9f-3b18-9c75-c43b2df8daee | -10.3202 | -49.9782 | 2026-08-28 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 79729ad8-2338-3588-a1ed-45d8a4d9e2c6 | -14.9 | -56.3257 | 2026-08-28 19:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| af2ac233-4d09-369b-8445-a09d535fcd26 | -6.0005 | -57.6689 | 2026-08-28 19:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| d1b91e14-56f0-3aa3-bf7e-8397af124447 | -7.3478 | -55.1744 | 2026-08-28 19:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| cfa4e812-4518-3148-8771-9f25244b0858 | -6.5093 | -53.2619 | 2026-08-28 19:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 7dbe88bc-ae7a-353b-98d6-59c68d170453 | -11.7598 | -47.6277 | 2026-08-28 19:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 524de0c1-6087-3caf-802d-f3e9127c1e9a | -8.5781 | -54.797 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| e16334c4-a603-303b-acce-e3ed61d1fb75 | -6.1101 | -57.84 | 2026-08-28 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4f5da381-66ac-34d5-99b9-1c74b587d925 | -11.2317 | -53.9958 | 2026-08-28 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 25dfa937-24f4-33c1-af10-1bb4a1c79996 | -6.8358 | -59.9379 | 2026-08-28 19:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 8f61416e-4621-3ad8-b759-ff4968ab0d1f | -11.7165 | -54.5449 | 2026-08-28 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 126.6 |
| 813b79c8-4376-3bf0-a8e3-e57afb3f6f9b | -9.0012 | -57.5585 | 2026-08-28 19:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 0cfa74fd-6074-3c6e-bbe4-dd29a83e22eb | -11.6212 | -54.5947 | 2026-08-28 19:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 2658b205-7b61-3f8b-a305-602a439abdfb | -6.1472 | -57.7995 | 2026-08-28 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 9b1b9ab8-3aee-34b0-8581-643df59cb318 | -8.1617 | -64.0047 | 2026-08-28 19:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 131.7 |
| ba23dd73-e074-3da6-bf2a-2d7c13271378 | -4.3021 | -59.4826 | 2026-08-28 19:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| c5035c7c-2185-37e4-923d-57aa40a9d30c | -9.0198 | -57.5574 | 2026-08-28 19:40:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 212.3 |
| 381d51eb-bd84-338c-92aa-dd47ad83bc6f | -7.4735 | -61.3846 | 2026-08-28 19:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f8113889-62d0-377d-9fd2-8a612baceb8f | -6.1657 | -57.7793 | 2026-08-28 19:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 165.8 |
| 32d35ab2-0a75-3366-a847-fc15f1a7cc65 | -14.3372 | -51.7234 | 2026-08-28 19:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| abb8fcf9-5118-31ed-9514-f6fdca367a27 | -9.4329 | -51.6926 | 2026-08-28 19:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 822f0e08-f4b2-3b95-a725-95c3e8e9d336 | -7.3663 | -55.1734 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 65872dfb-b4d6-3348-bbe4-d3c8121909ab | -6.7514 | -55.6654 | 2026-08-28 19:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 6b93d91a-5131-3460-accc-76518805fa50 | -11.2302 | -45.0528 | 2026-08-28 19:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 40c500c2-c9ee-396e-a719-14f835eec987 | -4.1516 | -60.6878 | 2026-08-28 19:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 46dddad2-17ab-3c02-a06b-c4d74561ab1a | -8.5785 | -54.7566 | 2026-08-28 19:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| c95a9bd9-153c-3397-978e-e7491e43b59e | -11.2128 | -53.9976 | 2026-08-28 19:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |


[Clique aqui para ver as próximas entradas](README174.md)
