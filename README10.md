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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70d4765e-aba1-3f5f-85af-f53df27e6b7b | -4.2128 | -50.6273 | 2025-11-10 04:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 319297c5-cec8-35bc-9137-009b2eee2480 | -5.1209 | -44.72862 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 659e9392-9bc1-34f5-bbe4-0b063112990e | -3.80385 | -51.09589 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 036d1d04-2fe4-3f92-8319-17834bc610ad | -10.45481 | -44.94301 | 2025-11-10 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f81269f4-bf37-3afa-ba92-f912e9560493 | -3.69209 | -50.1842 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36b86d29-c45b-3235-9e7c-35f571ca5034 | -8.70926 | -41.13247 | 2025-11-10 04:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7cc0c90c-5870-3577-9e05-99726b915861 | -4.73045 | -45.85154 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44d77b1d-e3f8-3907-8e04-b13b90fe8a50 | -3.47767 | -48.97732 | 2025-11-10 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86d1dc0b-1e5d-3b00-b07d-00b2811d7241 | -3.25953 | -52.01595 | 2025-11-10 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cf4d849-9005-3a8c-a72c-dcda125cf251 | -4.13401 | -50.77159 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df12d373-b604-323b-8088-d78cf65f03d4 | -7.0511 | -43.94769 | 2025-11-10 04:21:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46e5bed2-9d69-33ac-a778-a256ed69fee6 | -3.31349 | -50.10515 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5afad08-67c3-328c-9bf5-924bdbe5e3ae | -4.64247 | -46.37349 | 2025-11-10 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8186785-547a-3d96-ac41-7142379ac999 | -3.31373 | -50.13081 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e4b900b-b365-3ff3-abbe-42f485f28cb9 | -3.94507 | -51.03799 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 206c0f53-cc34-30f4-99b9-c6bdc1b7ad0e | -3.45032 | -50.47842 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4382ee1-9ddc-3332-a38a-b797a3899a4a | -10.78624 | -44.55977 | 2025-11-10 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72979d4c-48de-3db2-a2e5-e46002c2300c | -5.02024 | -46.83525 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa674768-8cd7-3256-9ad0-b53dbaee6e5f | -6.57134 | -42.90892 | 2025-11-10 04:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c416c0e-4894-37d3-8c86-31705986e053 | -4.80679 | -46.72239 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 241c7ed6-4128-3ff9-acdf-618394c4f8bb | -10.85156 | -47.61618 | 2025-11-10 04:21:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae5063a6-c76b-3b5b-b14a-91ef39765af7 | -5.59198 | -46.29424 | 2025-11-10 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5cb8882-5835-3af1-9a93-0edbca4e74f5 | -8.03901 | -39.69091 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8e639b8e-d927-3dcf-b46e-953199ff4c33 | -5.22222 | -45.03229 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63fb9fee-2304-388a-9e6b-b3e4c1b842ff | -6.81227 | -34.94198 | 2025-11-10 04:21:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bd666975-04ed-308e-8e3b-4c88fed59082 | -4.86525 | -45.11762 | 2025-11-10 04:21:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 966d0cfd-281a-3f70-806e-0c81348a3441 | -3.31783 | -50.10585 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c1bdb9ec-f68e-3539-b64e-a2b8ee37d828 | -3.69308 | -50.18767 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5c857a47-cdf9-3c29-bf94-1eac0bddf6b0 | -2.92702 | -57.78979 | 2025-11-10 04:21:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f85407cb-2475-3a38-aa9e-a19cb902a7a7 | -4.77228 | -46.50613 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4fe71607-f412-3afb-b0e6-88ddc63f456d | -6.21632 | -44.37561 | 2025-11-10 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85533666-5393-35f0-a240-8e471448f4ec | -3.25747 | -52.0635 | 2025-11-10 04:21:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2d73001c-c3c8-32f5-917e-360a1db89d11 | -4.58209 | -46.66941 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc8f4dc9-1915-3dee-9215-a6364d046e60 | -3.65734 | -50.23381 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17f39542-481e-381d-ae8b-9c8e1d9173ec | -9.13086 | -50.09224 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d4ff14-ab3f-3c75-9b7b-95f1cd13d6fb | -3.77613 | -52.2476 | 2025-11-10 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edecab9b-d3a1-333e-bb97-42797d7a5e73 | -9.1287 | -50.08128 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c3b124d-2ff2-3627-96b2-13b50cb7c8bc | -8.70905 | -41.13564 | 2025-11-10 04:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8469060f-e754-38fe-93b5-a1d76319c21c | -4.61352 | -46.66101 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 54b7b563-cbd5-357a-a91b-80a86011433e | -7.26658 | -43.91608 | 2025-11-10 04:21:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20a69141-5ab5-3086-b1e7-476201895696 | -4.91827 | -46.72822 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0c3526f-1242-3175-9944-ab58a205e84b | -4.58331 | -45.54212 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da1cb380-9002-34db-82e2-3cef887e243a | -6.47655 | -43.95135 | 2025-11-10 04:21:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| effd2375-9d7f-38fa-9d76-1d659da9127c | -5.21891 | -45.03176 | 2025-11-10 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e25084e-b5db-3eb5-856c-ffa7786f4303 | -4.7468 | -49.50551 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36a20db1-6afe-3e32-858d-2f58e99e5a19 | -4.90748 | -45.70666 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 344e3cdb-073e-305c-96a1-538f2744e25b | -9.5735 | -49.12162 | 2025-11-10 04:21:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81a91703-7ff8-30d1-85c6-d866e719f23a | -7.88733 | -48.39317 | 2025-11-10 04:21:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b063ee79-1bd7-3c1a-92d8-79b6697daa59 | -4.84173 | -45.85813 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47d58df6-e745-39ef-b40a-96aea58a81dd | -4.91479 | -46.72767 | 2025-11-10 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 475c90a9-73f9-3cd1-9ba5-a78cfaaad5e4 | -3.83735 | -51.20053 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c507c5c-46ee-35e8-96ff-f3e5c17e8248 | -8.04257 | -39.69519 | 2025-11-10 04:21:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2c876559-b26d-388f-977b-7a92835d17b4 | -3.89336 | -52.19534 | 2025-11-10 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce7d8511-e7fe-3ee7-8f9c-d7f877a50158 | -11.21823 | -41.54842 | 2025-11-10 04:21:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 629834b7-9bf6-37d8-bc9e-1ec932311ed7 | -2.86861 | -54.11346 | 2025-11-10 04:21:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 933d4865-bab4-3738-a8d2-ca631e377c73 | -4.90889 | -44.88606 | 2025-11-10 04:21:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f454f68-b6ce-3ef5-858b-d858d109c545 | -3.50649 | -50.08693 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41b72f1c-5f95-3d65-a516-f04046b384a4 | -4.36939 | -43.07026 | 2025-11-10 04:21:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dcb7495-6f8e-39cb-b98c-74fd03113481 | -5.19026 | -46.15198 | 2025-11-10 04:21:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebf379c5-b450-378b-bb44-e37e1ee8c3f8 | -4.12657 | -52.0666 | 2025-11-10 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70214b25-4b2e-37fc-8747-24a8ea5237e8 | -3.58912 | -55.47564 | 2025-11-10 04:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85afe4f8-fd59-36e1-9333-fcf51cbbedcb | -4.53809 | -45.78103 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97f74997-031b-3fe8-9078-d00a71a813cd | -4.58314 | -46.67212 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 225a40e9-a466-30be-8493-0df7cc9e6d39 | -5.64514 | -43.6207 | 2025-11-10 04:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59d506d7-f82d-33c6-a4ab-66009a604172 | -10.3792 | -49.90999 | 2025-11-10 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e92659e7-7f30-3b0f-97bc-70c7cca72f2c | -5.83981 | -38.3525 | 2025-11-10 04:21:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aab4c43f-6344-3631-8e33-faf602846cea | -4.41037 | -45.81311 | 2025-11-10 04:21:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3e311be-08cd-3e17-8211-f7e829e5dd4b | -5.56792 | -51.2075 | 2025-11-10 04:21:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0caf39b-251d-3312-9320-1f4d1e94f7b2 | -3.25452 | -50.07507 | 2025-11-10 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 931ccc34-982c-3660-a977-57136c21ff43 | -5.91227 | -48.32584 | 2025-11-10 04:21:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1766935f-2815-3de8-9241-c856729fe5aa | -5.1242 | -44.72914 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5fbe7df3-3767-37fb-ac90-2bc7d2ae896a | -5.16823 | -38.74372 | 2025-11-10 04:21:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 52134e4f-b1ea-317a-a543-0ce51fbc767a | -10.33712 | -49.63668 | 2025-11-10 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c32bcaa-de0e-3b6c-bb39-51de4d030f5b | -11.90741 | -43.82553 | 2025-11-10 04:21:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b5493af9-8b2d-37b7-a3c7-93c235627a93 | -4.20041 | -50.63532 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 76c75be2-60d4-3d30-8dff-50bc0070c388 | -5.85204 | -47.47177 | 2025-11-10 04:21:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4cd4ebd-f1d2-348b-897b-0a5de4fdbd3b | -4.39876 | -45.9715 | 2025-11-10 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b71724af-7722-369c-8aa1-dfec9ccc65f6 | -4.57997 | -45.54154 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc31d207-718f-34c8-889c-d41062573b19 | -4.59222 | -45.5509 | 2025-11-10 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06a63cf6-eb9a-3599-9a43-872408fcf364 | -4.13499 | -48.82094 | 2025-11-10 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69418731-4d95-38a4-a6bd-6ce844e422fb | -4.92806 | -44.72258 | 2025-11-10 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abcc429a-eded-344e-ac1a-d8e6f1a670b4 | -4.50519 | -43.56802 | 2025-11-10 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a050f05-6812-37f5-9f95-dd04a9eba7a5 | -10.79667 | -44.24755 | 2025-11-10 04:21:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4b1b22e2-ceda-369d-a248-068b21d3c64b | -9.31209 | -41.0541 | 2025-11-10 04:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b69c716-b835-32a6-8de5-ca3248b4ef12 | -10.45868 | -44.94002 | 2025-11-10 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff3b1f5f-72b7-3ce4-8a04-784c2b8870ad | -3.47698 | -49.92912 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54b67757-0260-3ff7-8e36-8cb788700a40 | -9.12691 | -50.09153 | 2025-11-10 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd10bd68-22f7-30ac-a5c2-4af926ee55e2 | -4.63722 | -49.58942 | 2025-11-10 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 757b0b96-7456-30cb-914d-b31c06809902 | -6.69743 | -44.14609 | 2025-11-10 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8376fa2d-71c6-3fdb-a30e-dcc6998eec61 | -9.10195 | -35.41363 | 2025-11-10 04:21:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 757fd35d-1e3f-3575-b3df-a3bdf598f259 | -3.85909 | -51.04713 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a524902-aa0c-394a-b330-483b7a5e6f23 | -4.58147 | -46.6733 | 2025-11-10 04:21:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7007b31d-dd6a-3fe4-9d29-811e4d09cc14 | -9.66936 | -43.89964 | 2025-11-10 04:21:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3456f61c-243d-3248-aad6-1238b9d4b14a | -3.84264 | -50.75077 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7de366f-1378-36db-b1dc-79ed43438682 | -3.83353 | -51.20418 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5d24dbd-d3de-39ed-8430-c881a2105a4c | -3.46112 | -50.02672 | 2025-11-10 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02ae21d7-3b00-3262-9d56-950eb6713e48 | -8.70547 | -41.13192 | 2025-11-10 04:21:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c8476e30-e404-32cf-8ca2-df7eb331c881 | -6.85597 | -40.15667 | 2025-11-10 04:21:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a902b43a-a51e-36fb-af99-71cb0aa21d0d | -5.37264 | -44.72635 | 2025-11-10 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc0fbe43-3e95-3a5b-afd7-fe06adc14c07 | -3.59078 | -55.46602 | 2025-11-10 04:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README11.md)
