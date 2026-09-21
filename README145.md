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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c3c90d8-b8bb-3fed-9d21-dd008f1eb558 | -9.8689 | -48.4252 | 2026-09-21 15:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 7d7685be-1db7-3c94-93f9-0c353d80d908 | -7.5477 | -61.3247 | 2026-09-21 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3c4d0624-e78b-3ef3-97aa-624ab458ca5a | -10.809 | -50.1836 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1ccd5137-6ae8-33c6-bec1-31864f9b0c2d | -5.9196 | -55.7046 | 2026-09-21 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c67be0d7-8287-3858-87df-17e8ee937495 | 1.2794 | -50.8718 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b56338b6-a8de-3f03-9293-be64ee3e7087 | -6.6014 | -58.9844 | 2026-09-21 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 69ee7907-ab64-3485-9f93-1c8b5d8e4895 | 1.2424 | -50.9346 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 16d27f40-7894-3e1b-ad10-a06e042bf0f7 | 1.2427 | -50.7472 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 22b3485e-4454-35ff-b2a5-575979d3c257 | 1.2608 | -50.9968 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.7 |
| e4d86cf1-4057-39b6-9311-2185996c0707 | -6.1653 | -47.5052 | 2026-09-21 15:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4c9c2f89-ac1b-3115-a135-c1c69bd4233f | 1.2424 | -50.997 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.7 |
| b5a6ac29-1d3b-3090-ac23-46980ea7355b | -3.0763 | -44.3684 | 2026-09-21 15:50:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 39e0cc0a-9c43-322f-ba5b-129377bd4f5d | -6.3383 | -59.9374 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| bfd0f6f9-9985-3d07-80b4-0843e4185e95 | -10.3363 | -50.1905 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 10e6b49e-e9c8-3c25-b579-c7b53c66ad47 | -6.5449 | -44.8871 | 2026-09-21 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| b904669f-a21f-30da-a7ce-1b6b717d5de2 | -6.7369 | -55.0874 | 2026-09-21 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| fa251268-d342-36d4-bb4f-4d03284f64ce | 1.2423 | -51.0178 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.5 |
| b003ffa9-1e0a-3a14-898b-fbc8c24695fd | -2.8608 | -57.8188 | 2026-09-21 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5a1c6ba1-4595-3b2f-a41c-4b536c08042d | -10.9361 | -50.5759 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 23622be9-a891-3218-867d-a3459adb6f9d | -3.4828 | -57.9803 | 2026-09-21 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 9282fe90-48e0-3774-aa15-15ca622d9d26 | -3.3139 | -59.3898 | 2026-09-21 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b331143b-0e8e-3ddd-9efe-41b4abb9a681 | -10.3171 | -50.2138 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 51c2c0a4-8070-39bd-9e96-b6f602fa76b8 | 1.2608 | -50.976 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 5999a9dd-255e-3893-b2c3-b56b254d7ecc | -1.1345 | -49.2123 | 2026-09-21 15:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c4a8b149-3451-3973-9ff9-3b3a2851abf0 | -2.9156 | -57.8371 | 2026-09-21 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| d24cbb8a-f454-3e51-aa27-c81e25fe67fc | -3.4461 | -58.0199 | 2026-09-21 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 64412891-fc34-3315-86f3-df148971e102 | -6.5761 | -45.5194 | 2026-09-21 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a91e7c61-5dc5-3c79-be22-b8f89125e8f3 | -10.2979 | -50.2372 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 78d87248-5df0-3e44-96fd-b3836ee86487 | -2.8974 | -57.8181 | 2026-09-21 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e87b73a8-0d01-38f3-b21c-4e1230c4ac08 | -3.6448 | -58.9031 | 2026-09-21 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 05ef741d-ff73-3174-8dbf-207c1e7dd830 | -6.5634 | -44.9084 | 2026-09-21 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 9d7b4734-7fcf-370e-96f0-857b146bd46b | -6.9225 | -42.9088 | 2026-09-21 15:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 82d09beb-0df3-35c1-9b33-320308e9f45d | -6.5829 | -58.9851 | 2026-09-21 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d28149ec-75a0-3ee4-9247-89df74543c8f | -1.0243 | -48.83 | 2026-09-21 15:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c2f2a416-b13b-3053-ad67-dd22aa574f04 | -6.7485 | -59.0557 | 2026-09-21 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 51859664-b83c-366e-a48f-bab9be782c12 | -10.7652 | -50.6153 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 7855a0e1-89ef-3a73-8445-68440916fd20 | -6.4372 | -55.6411 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 81840633-6689-3a2e-acbe-ed131833688f | -2.9709 | -57.7197 | 2026-09-21 15:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 3c9e34fa-4d75-36c5-b42e-68e07ce9fe0c | -3.3638 | -61.2904 | 2026-09-21 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6ab5b045-55b1-3fa1-bcf0-78c4b74b06a6 | -10.707 | -50.7277 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| a8269d68-4acc-3156-9957-ae9388471c27 | -7.3291 | -55.1955 | 2026-09-21 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 709d0176-7794-35e7-a3f5-61ee293864f8 | -9.3986 | -48.3213 | 2026-09-21 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 93f8ca44-b291-3ccc-901f-1592f6c694d2 | -10.126 | -68.2891 | 2026-09-21 15:50:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 5cec5d11-a229-3f02-9239-720251a4c072 | -8.1688 | -54.7432 | 2026-09-21 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5ebdc605-1e85-3fc0-8127-e8997cc30206 | -10.8735 | -53.9668 | 2026-09-21 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.2 |
| c43d50cd-70ea-3a20-9882-44a8e7e72f51 | -10.955 | -50.5738 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 7f96b013-01e8-3b55-9986-c0577cb0ce08 | -10.6947 | -50.2386 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 34fd9349-bb50-3a97-a88b-04259e31afb3 | -10.8279 | -50.1815 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c8996778-df13-344f-854a-c37f20c760dd | -7.5661 | -61.3239 | 2026-09-21 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c1f5e845-6a3a-3698-9e40-9e5e2fda891a | -3.3455 | -61.3096 | 2026-09-21 15:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 4a50269d-bf55-3919-aaef-b37edd3f5ab1 | -4.0944 | -52.1252 | 2026-09-21 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 685b2ad0-4aee-37ad-8061-c85f9f73a3d5 | -10.6944 | -50.26 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 3d3c4055-9d2c-3489-95f2-ed8661def91c | -6.7123 | -58.9412 | 2026-09-21 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d6d5c3a2-3fcf-3217-94c0-0417ea3490a6 | 1.1687 | -50.977 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5dc9a7be-d7e8-3341-b56b-f88cc49bce12 | -6.4301 | -59.9916 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ecf93fae-879b-3b17-ae56-03aa231fccbc | -10.7466 | -50.5959 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 09365078-9bdf-3a2b-a6c4-05c0e0ecad7a | -10.7061 | -50.7915 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 255.7 |
| ef072192-f1dd-3d16-89ae-d426a78b6e7b | -9.5595 | -66.0172 | 2026-09-21 15:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 101bba5d-bf1b-3e7c-a444-b8ef3b441fb6 | -7.9152 | -72.9324 | 2026-09-21 15:50:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a387765b-9e85-3fa8-b24e-52cdc8dbbebf | -10.974 | -50.5718 | 2026-09-21 15:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f5a35d3a-d80f-33a9-97e0-d2c44a367654 | 1.2059 | -50.7685 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ee2da13d-b291-3a29-b9bd-a75538b2b53e | -10.279 | -50.2391 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 2fe8b374-e1c6-3d12-ac51-f75242c2214c | -6.8468 | -55.2617 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f6ff79e8-61b6-3cdb-8ed1-a3f95d1c9173 | -0.803 | -48.6825 | 2026-09-21 15:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| aa81cdfb-032a-3c45-8d6e-64271822d4b9 | -8.1874 | -54.742 | 2026-09-21 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 71b3922e-6889-3f8a-9984-e0d2c45f62d5 | 0.7937 | -59.2099 | 2026-09-21 15:50:00 | GOES-19 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 387447ee-b575-315f-8148-a4e355b9c5de | -6.5444 | -44.9327 | 2026-09-21 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| cc0c5899-8c98-3a3c-93c2-a6493a1f6051 | -2.9525 | -57.7394 | 2026-09-21 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| ea4fa89d-89c3-382f-a9f0-c43ed3a4db06 | -10.467 | -50.3052 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a583b100-c6dd-398a-b413-8a43b6e8360b | -10.336 | -50.2119 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c9d8df76-7bc0-3c4d-8532-98d883956f39 | -0.803 | -48.6611 | 2026-09-21 15:50:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 2d659535-1690-31b9-a23c-29d97cecacdd | -10.3919 | -50.2702 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 389fc86f-d511-3ac5-ad54-ee911a14d5e5 | -7.822 | -61.8084 | 2026-09-21 15:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 259.4 |
| 0e41674c-676e-3f83-aa4c-1070a411e05c | -9.1243 | -60.9502 | 2026-09-21 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0da1f91f-b398-308b-87cb-ade631eb9d46 | -8.1686 | -54.7634 | 2026-09-21 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| c7c04180-4326-3658-bb57-4657f080ef65 | -6.9223 | -42.9323 | 2026-09-21 15:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 247.0 |
| 759013b8-0472-387e-9db2-c440b4c37a4a | -10.6694 | -50.7103 | 2026-09-21 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1aaa73d7-0513-3ec7-8ce9-87cb4de7bb5b | -3.3549 | -57.8863 | 2026-09-21 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 67c057ba-9f1f-36cb-9b67-c28cd5b1006d | -6.5759 | -45.5419 | 2026-09-21 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |
| bee34c2b-f3ae-3a1d-bae5-e29df3a992f3 | 1.2054 | -51.0597 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0004976b-07a9-39a1-967c-acdd1ca8aba7 | -6.3012 | -59.9962 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 07d27e00-d22c-3e92-814e-971d83f5d53c | -3.6077 | -59.0577 | 2026-09-21 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 60caf786-75f8-3655-a496-a717748cddbe | -6.8651 | -55.2807 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 7c0117d1-32d6-3017-8bcc-1bc2dc702864 | -9.8686 | -48.447 | 2026-09-21 15:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| dce493a7-41aa-3d7c-80a6-0e55cf769706 | -10.67 | -50.6678 | 2026-09-21 15:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 1e59edb7-5b80-3254-bc87-f342acdf40db | -10.1964 | -53.9232 | 2026-09-21 15:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a2292bb8-53b3-38d0-9889-68c7596716e6 | -3.1698 | -58.5859 | 2026-09-21 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 84e2e4a6-b8e1-3e06-8161-a1d4ad2226e1 | -8.2388 | -55.2616 | 2026-09-21 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 320.5 |
| 21b475c1-3a18-3c01-ac17-664cb3dc6e0a | -9.1711 | -49.9835 | 2026-09-21 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 9c960bdb-121c-3040-bb8e-5b358570ab20 | 1.2978 | -50.8923 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.4 |
| c2e2c697-3459-3a02-8253-697e6cf8f7c9 | 1.2792 | -50.9758 | 2026-09-21 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.5 |
| e55c9430-4482-32db-afd2-163106e5bee9 | -3.6631 | -58.9027 | 2026-09-21 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8129bd94-b25c-34db-ae5a-9296523f79f8 | -3.1881 | -58.5855 | 2026-09-21 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| b86e0f1c-f51e-3918-a488-e021303ced76 | -10.4486 | -50.2644 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 30762f9f-749c-37d9-ae30-96eb5bb87938 | -6.392 | -45.1948 | 2026-09-21 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 244.0 |
| 6ac66c61-da00-38e8-98de-0d1fee64788c | -10.2982 | -50.2158 | 2026-09-21 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 2d67e55d-008a-3269-9c88-1f3dd96a79ca | -3.1514 | -58.644 | 2026-09-21 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6d6d1f04-031c-38a9-b3dd-09c9ee185fdf | -3.3322 | -59.3894 | 2026-09-21 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| d2fa790e-dba5-3ddc-a55b-22e7e4b1e1da | -3.2955 | -59.4284 | 2026-09-21 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 47862fd4-df6a-3f7c-958d-d6da427ccecb | -6.2832 | -59.9202 | 2026-09-21 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |


[Clique aqui para ver as próximas entradas](README146.md)
