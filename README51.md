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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2b5e3f8-324a-3f1d-b76d-ccd1cb9105ab | -14.9567 | -46.7556 | 2025-10-10 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| c6035ffc-9559-3468-9e49-21c417d03faa | -9.1028 | -45.0248 | 2025-10-10 12:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 1e5f55ec-04b9-33fd-b434-d335df99d4d5 | -11.7585 | -43.3374 | 2025-10-10 12:40:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1163fcb6-aa52-3888-9899-b57ef2fcc495 | -14.9372 | -46.7591 | 2025-10-10 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| e70c0946-de5c-3fc2-beae-5cc9693891ce | -13.8491 | -45.8454 | 2025-10-10 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 251665bc-bb6a-35d2-b1ef-5baf5f003428 | -15.4375 | -47.9871 | 2025-10-10 12:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 4da07264-83e5-3170-8a20-5e20bd5ec41e | -14.2744 | -45.911 | 2025-10-10 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 8e2c05f1-c3be-3ef8-9bc8-f61829e0e1bc | -13.8496 | -45.8223 | 2025-10-10 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e6c77ef9-4ca5-3338-b01d-c978c9457923 | -11.7585 | -43.3374 | 2025-10-10 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 78495b84-5d10-348d-ac81-1f4c87f48040 | -8.5052 | -45.9744 | 2025-10-10 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| f749a015-4807-3d9c-a386-378664f2fa4d | -13.8491 | -45.8454 | 2025-10-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 4fbb3ea3-c318-3327-9d0c-43b3aad730ae | -8.5221 | -46.1301 | 2025-10-10 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| a1f96d12-fd85-3d14-b5fa-5bdbb1508b3b | -12.3592 | -47.2335 | 2025-10-10 12:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 167.9 |
| cf8033d6-6c5b-31fd-8ae3-a7df67f6e01e | -10.1517 | -44.5984 | 2025-10-10 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 229.4 |
| ab3f4f74-97cc-37a7-a09c-7748b11798cc | -13.8496 | -45.8223 | 2025-10-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| e4352741-c797-39be-bde4-8c437bf44b13 | -10.1707 | -44.5959 | 2025-10-10 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 061459f7-0ea7-31ab-9120-ed09cdeb24ad | -11.7782 | -43.3105 | 2025-10-10 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 154.0 |
| f371e85e-c6f4-3bbb-a47a-a37d87624d6e | -13.8487 | -45.8685 | 2025-10-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| cff02c3b-ea2a-353f-ad74-629afc2f414a | -8.5055 | -45.9519 | 2025-10-10 12:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 4694553c-b1ee-30d0-9fdd-1713c3142e72 | -13.8307 | -45.8024 | 2025-10-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 5fa44306-c3a1-3d8f-878b-7b824ac28729 | -10.1513 | -44.6215 | 2025-10-10 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| a2298bad-da51-326e-9209-543f241be5cc | -10.1898 | -44.5934 | 2025-10-10 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f907aa00-de04-33c8-980b-fd161deca12e | -15.4375 | -47.9871 | 2025-10-10 12:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 182.7 |
| fd81aead-26d4-3f95-a770-92c25c472e7c | -11.7589 | -43.3136 | 2025-10-10 12:50:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 349.7 |
| 6e8cc46f-ce42-3cd8-a107-efb48ed171f1 | -13.8311 | -45.7793 | 2025-10-10 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 46309426-f9b4-3c91-b130-42deba5bb8f7 | -15.4179 | -47.9905 | 2025-10-10 12:50:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 50e12fe5-44bb-3bb6-a0fd-cad4efe29b23 | -12.6873 | -43.0884 | 2025-10-10 12:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 80.0 |
| bc8402c5-69ac-3f4b-9d8e-cf81b03e69b6 | -14.9372 | -46.7591 | 2025-10-10 12:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 0c5d9eba-c193-3a57-b88f-c060a19633e9 | -10.152 | -44.5752 | 2025-10-10 12:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 841a7e4e-add7-36b5-b363-d75ddcaf2812 | 2.1312 | -55.80012 | 2025-10-10 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| c3fa341e-1d62-339a-8f92-fcd9218502fd | 1.94695 | -55.73943 | 2025-10-10 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f09cbda0-69b3-3eaa-b95e-9a9dcbbb2db5 | 1.94442 | -55.72185 | 2025-10-10 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 86e400ab-38f8-3dc1-b233-6bdf28a966a4 | 1.94569 | -55.73064 | 2025-10-10 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 475df26f-9587-36d5-bc28-a4b340b4f57f | 0.30512 | -51.01555 | 2025-10-10 12:55:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 1032468c-0f00-3a53-8307-d137126d04e3 | -1.03804 | -48.89429 | 2025-10-10 12:55:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 7e7f2d55-2f55-33be-a110-8823950aec1c | -6.11507 | -51.74601 | 2025-10-10 12:57:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9440e25f-f5d3-35dc-9243-2394fae9e98a | -5.21463 | -46.81493 | 2025-10-10 12:57:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 24356654-2cee-3a7d-9451-91204c2120a5 | -12.074 | -47.99285 | 2025-10-10 12:59:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f45307f4-e041-32a7-9782-15a993c6b67c | -18.77832 | -52.02929 | 2025-10-10 12:59:00 | TERRA_M-T | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 239d0b7b-54c6-3c76-8885-42c6276146e4 | -12.5759 | -61.18902 | 2025-10-10 12:59:00 | TERRA_M-T | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d4558a1c-6883-3fa6-96d0-6d5df06a25c2 | -16.00791 | -59.54288 | 2025-10-10 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9f3af22c-462b-303f-ac3a-69d8a75ffbb2 | -16.01543 | -59.55345 | 2025-10-10 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 65770c32-e1c0-344a-bc7a-91f65991d369 | -18.06082 | -50.27737 | 2025-10-10 12:59:00 | TERRA_M-T | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 770f077c-8429-3c3f-ba47-d5216e93f7ac | -15.97384 | -59.5283 | 2025-10-10 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dda5d017-bc7c-3e95-aec0-9765149036b1 | -15.9725 | -59.53749 | 2025-10-10 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 57206512-3e3e-3e7b-8673-23ee70ddab9e | -17.89211 | -57.66531 | 2025-10-10 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.4 |
| c5ef7a78-db95-38f0-a349-3cc41ec68684 | -19.58705 | -54.02536 | 2025-10-10 12:59:00 | TERRA_M-T | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 32004e2d-bde8-3724-b615-f6cccef7b54a | -16.01677 | -59.54427 | 2025-10-10 12:59:00 | TERRA_M-T | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 80b35c3b-2f70-3b92-9278-4b5887191f05 | -17.91236 | -57.51322 | 2025-10-10 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.2 |
| a8bacae2-a85e-3c10-9ac7-24988c3457b8 | -17.92664 | -57.61861 | 2025-10-10 12:59:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| aa28e044-7086-3bc7-b499-c1d5154b8e99 | -13.36432 | -61.33691 | 2025-10-10 12:59:00 | TERRA_M-T | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 951aabaf-7a3f-33d0-b3fa-7a546600ad1c | -8.5221 | -46.1301 | 2025-10-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 442bf520-ee7c-36aa-9fe1-4559b9c17f23 | -10.1898 | -44.5934 | 2025-10-10 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 500ffd2f-b2b3-3653-958e-1edad8a8130c | -11.7589 | -43.3136 | 2025-10-10 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 354.8 |
| 36476bf1-9665-342e-89f7-e096d262d525 | -8.5032 | -46.1321 | 2025-10-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 183.5 |
| bfe5fd79-3cfe-3ba6-8540-e6ed83f91a38 | -10.1707 | -44.5959 | 2025-10-10 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b89b6b60-db21-37e8-afbc-f344a3a750f7 | -13.8491 | -45.8454 | 2025-10-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 97336db2-40e9-331d-82fb-5bfa4c44b724 | -13.8487 | -45.8685 | 2025-10-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 155.8 |
| bc2c456d-67b8-3caf-83be-b476dbe6f42a | -17.6732 | -44.4534 | 2025-10-10 13:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 71017c01-fe45-36be-8b7b-8121077bafe1 | -15.4375 | -47.9871 | 2025-10-10 13:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 113.7 |
| eab26c70-2ca3-318c-881e-03686b482d4c | -13.8496 | -45.8223 | 2025-10-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 68c4bf62-d7ba-3c77-9aa8-57250bb0bc2a | -12.3592 | -47.2335 | 2025-10-10 13:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| c0f5c406-e700-3140-b2ed-4b32bd51562e | -13.8311 | -45.7793 | 2025-10-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 6c332744-8a69-3645-be37-8e0f77b78606 | -10.1517 | -44.5984 | 2025-10-10 13:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| d37154c3-3a1a-3904-b322-6ea558073c1c | -12.6873 | -43.0884 | 2025-10-10 13:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 33f1a514-2093-3c85-b31c-47176792d4c8 | -8.5027 | -46.177 | 2025-10-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 704348fe-922f-3191-9252-c98443c59eff | -11.7782 | -43.3105 | 2025-10-10 13:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 65bb5c1e-f3a1-327f-9306-658823abdbbb | -8.5029 | -46.1545 | 2025-10-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 2a9b740b-7430-35b1-a585-f5bc4d50c5e7 | -13.8307 | -45.8024 | 2025-10-10 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| d260cb0e-4820-3bba-87a6-6f0c4776e897 | -8.4844 | -46.134 | 2025-10-10 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 1dd9843e-e8b8-35a5-8566-e8f82339f6f8 | -11.323 | -47.5287 | 2025-10-10 13:00:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ef053052-99eb-3795-9600-ce0f94eeb823 | -22.15688 | -57.09227 | 2025-10-10 13:01:00 | TERRA_M-T | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 0f3c8760-608e-3be1-b066-74296464f699 | -12.3592 | -47.2335 | 2025-10-10 13:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| e0c1ced8-8e9e-32de-96ac-227a3aa4f847 | -12.6873 | -43.0884 | 2025-10-10 13:10:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 83.8 |
| 64f58489-fcef-3e08-a8e4-b75b839a8d83 | -13.8311 | -45.7793 | 2025-10-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 7d83d042-db2f-3c54-a200-47218c324883 | -14.4253 | -48.0199 | 2025-10-10 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.0 |
| ee086c58-5fe6-36b2-9e21-c945c329b6c4 | -13.3295 | -47.7417 | 2025-10-10 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ad356230-0ff4-3f66-806d-bb2f527929fb | -8.4844 | -46.134 | 2025-10-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5a24a868-2e3e-34e3-88f3-aa577eb51d6c | -8.5221 | -46.1301 | 2025-10-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 288616bf-4df3-3d2a-bfe8-2ed5178c8f54 | -8.5027 | -46.177 | 2025-10-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 27bb1fac-c290-3e88-aaa6-f72cb3a321eb | -17.6538 | -44.4339 | 2025-10-10 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 04669c0c-f390-3f26-be5a-ac871aa0dbd1 | -17.6732 | -44.4534 | 2025-10-10 13:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 112.3 |
| ecd6a959-c669-3fc1-9148-d21bb0657b24 | -15.4375 | -47.9871 | 2025-10-10 13:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 2c2d199d-8877-3fcf-9198-90c92599a3af | -8.5029 | -46.1545 | 2025-10-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 623776ac-f273-3e1c-b1da-eb028171c96a | -11.7782 | -43.3105 | 2025-10-10 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 203.1 |
| 235dfbff-3de2-3a65-a296-40e1a84e76ec | -8.5032 | -46.1321 | 2025-10-10 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 1391ec82-e0c5-3bb7-8085-e7fb0f242aef | -13.8491 | -45.8454 | 2025-10-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 0912a1c1-6675-3864-b833-9951faa21d80 | -14.4258 | -47.9974 | 2025-10-10 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 3780c7f4-61a6-3bc0-9aa9-9308558b8a5c | -13.8496 | -45.8223 | 2025-10-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| d135dae9-8016-390d-b3c7-1ab622288b6a | -10.1517 | -44.5984 | 2025-10-10 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 635d2fc5-7bb1-30ef-ab5c-b07a8679c326 | -11.323 | -47.5287 | 2025-10-10 13:10:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| f111d185-0dd8-31c4-a756-d3b2ac8267d9 | -10.1898 | -44.5934 | 2025-10-10 13:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| df10ef33-2f74-39b6-bc06-60bf87a3fa0a | -14.9372 | -46.7591 | 2025-10-10 13:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 0ab32274-f3dd-3ccb-b785-313223b030a5 | -11.7589 | -43.3136 | 2025-10-10 13:10:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 352.9 |
| f86292c7-a885-32d3-b501-07c46399db6d | -13.8307 | -45.8024 | 2025-10-10 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| fd050253-ab08-3218-bb4e-495af88aff81 | -8.5032 | -46.1321 | 2025-10-10 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 2b421097-6566-3ee5-aa3d-f2f79078649a | -15.3938 | -47.2938 | 2025-10-10 13:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 3ec96f63-fca5-35af-9ca8-60df6945dbd5 | -14.9567 | -46.7556 | 2025-10-10 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| dee08c55-bec4-3394-9658-8778fbcfb4b9 | -10.1517 | -44.5984 | 2025-10-10 13:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 14b41a5f-9ac3-3e59-a9ab-fb78a646978d | -12.6873 | -43.0884 | 2025-10-10 13:20:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 101.4 |


[Clique aqui para ver as próximas entradas](README52.md)
