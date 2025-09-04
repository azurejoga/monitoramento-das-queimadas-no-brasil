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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83e31209-8432-3201-8e9c-bc4a9e5f7339 | -10.6577 | -51.5996 | 2025-09-04 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 164.6 |
| 95dfba85-436b-305c-a537-c6c76ecc5888 | -11.0436 | -47.1409 | 2025-09-04 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 10c64439-2991-369b-8a94-feb42c623748 | -12.4593 | -48.0885 | 2025-09-04 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 724f1db7-831d-3376-b816-3a29470ceb88 | -7.7409 | -48.7772 | 2025-09-04 14:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 01e5ab23-81dd-3efb-8f35-2cd2a6360221 | -7.7039 | -48.7371 | 2025-09-04 14:10:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 2ee134b1-4c6a-3c15-b140-302c06822aef | -5.7927 | -45.2626 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 3bc98bdf-1d70-3eed-a6d6-80ba2c3cb0e7 | -18.5665 | -44.0236 | 2025-09-04 14:20:00 | GOES-19 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 99.2 |
| e3b48e2c-02fa-3fc7-ae46-f65623219603 | -7.7036 | -48.7587 | 2025-09-04 14:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 00abb2d2-b35b-33f0-b2c5-3fc1b10bf010 | -12.5173 | -48.0584 | 2025-09-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 71818463-0a9d-341d-b443-bd112ccc4df3 | -9.7108 | -48.9636 | 2025-09-04 14:20:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| f8528b68-0ad8-3ad0-857e-68fa855e062c | -11.7884 | -50.6735 | 2025-09-04 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 24ade49c-59b4-3954-bf50-e83f180ce695 | -5.699 | -45.2918 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 164.4 |
| 144eea98-74b9-39f0-b555-483d4ed1528a | -11.2005 | -55.0195 | 2025-09-04 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| bcb9f06b-fb24-34fb-a42d-f3a9bc069df1 | -8.0799 | -45.339 | 2025-09-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 5d0f5081-4723-3bd2-8967-ae3121c3c9c7 | -16.0474 | -47.835 | 2025-09-04 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d57c7401-a9cb-354c-925e-b3e2b0a33d34 | -8.8848 | -45.7767 | 2025-09-04 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 443adddd-5d5f-3a71-b32e-ef8341587b90 | -6.1667 | -43.3039 | 2025-09-04 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 886d6862-19e7-38d2-b174-f24736bc29c9 | -9.4376 | -46.7947 | 2025-09-04 14:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| a8208bfc-c3a1-3d53-9c9e-8d5a5fafe976 | -8.2001 | -49.5988 | 2025-09-04 14:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 96585040-481a-3912-9447-e194f5986317 | -8.02 | -44.084 | 2025-09-04 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| b571718d-42fd-3696-87ef-73f14c027ed2 | -5.8292 | -45.3729 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 144.3 |
| cbc2cf6d-ee0d-33c5-86e0-ff7f16914fcb | -11.5969 | -52.113 | 2025-09-04 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 225.6 |
| 6bb173a4-6c7a-3f71-98f8-6d32a1cb7cf4 | -6.2062 | -45.0506 | 2025-09-04 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ea2d024a-a220-3afe-bb5a-9b4d09e99467 | -7.2898 | -43.7162 | 2025-09-04 14:20:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| b2c1156a-695c-3474-b584-150b2d500419 | -5.6782 | -45.5414 | 2025-09-04 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 644f44a6-47fd-3491-99d1-b8483ecc170f | -5.6784 | -45.5188 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5f2b1b34-2baa-3f4a-ab27-4a5149f5500f | -11.6525 | -52.212 | 2025-09-04 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 707e5d53-bfb5-3a72-bff5-a3d3259241f7 | -5.6813 | -45.18 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b73ce602-18f4-3031-ad62-29f8ffd59f8b | -4.8862 | -41.771 | 2025-09-04 14:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 180.0 |
| f03a4fe6-60d3-37c8-a25f-764318f3b3f0 | -11.3897 | -43.5839 | 2025-09-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d13af5c5-67a4-39c2-a79c-c5c4e5e3cb40 | -13.8457 | -47.9764 | 2025-09-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 330f09b1-4b1e-344f-aeb0-abd9f8ae1c41 | -10.9855 | -49.7562 | 2025-09-04 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ccea795f-502b-3f39-ace9-0500e5dae434 | -5.7528 | -45.5587 | 2025-09-04 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 1e89b556-c97f-3b96-acf9-386009f87349 | -22.6567 | -43.6825 | 2025-09-04 14:20:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 129.4 |
| 5506afc2-815b-39b3-8063-8d7011617612 | -12.4977 | -48.0832 | 2025-09-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| c161663f-1a8a-3daf-89df-a3e70015889e | -12.523 | -53.8278 | 2025-09-04 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 9b58e3c5-ed4c-381c-9f9b-3ab04a8caf6f | -8.3641 | -48.3334 | 2025-09-04 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 16412dec-c3d4-3523-be52-8dc2fb0368fc | -7.0131 | -43.2291 | 2025-09-04 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 98.6 |
| 44832004-ee42-33d8-a6da-819a1b4fd397 | -6.2977 | -45.2702 | 2025-09-04 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 06f02af3-88b7-391a-a028-1f9d7bc44d03 | -6.8944 | -45.5383 | 2025-09-04 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 7b62acff-f397-3572-ae7d-4d849e35f5c3 | -6.2318 | -42.4278 | 2025-09-04 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| 57f38a28-1ad9-38c3-98fc-023398b1a50e | -11.834 | -51.4551 | 2025-09-04 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 4628e1cf-cdbf-3011-b1a1-8c586d6262e1 | -15.4567 | -52.9971 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 5b56cfd5-9970-3724-aabf-93f3412023e9 | -8.0985 | -45.3598 | 2025-09-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| baaa3a0d-c5b4-308c-92b1-a16bc1d4d616 | -9.5025 | -57.8032 | 2025-09-04 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c4655d53-9b68-331f-8660-cca03be04ca9 | -12.9189 | -57.0074 | 2025-09-04 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| a736ff74-5e02-3748-b9d7-3c64a5ba186e | -10.4655 | -50.412 | 2025-09-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 212.7 |
| 411c236a-ccca-3e67-9567-3a2d9072508d | -17.0652 | -46.449 | 2025-09-04 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 4be24560-fca0-331e-bb82-cca69140b9d2 | -6.2205 | -43.5558 | 2025-09-04 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 316034c7-f23c-35f7-8ae4-2fa48c78f24e | -5.1191 | -43.0795 | 2025-09-04 14:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 0c5ab8dc-149b-30d2-8d78-09cbe4e31bde | -11.0044 | -49.7541 | 2025-09-04 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| ffc9eef4-27ad-3c14-985d-5fd80ad4f9ea | -5.7002 | -45.156 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 0b8aef5a-8bd5-3a66-8f9a-d5ceeb33651f | -15.0059 | -50.0739 | 2025-09-04 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 985795fd-012b-3fdf-80d8-50f890afaf9a | -8.3644 | -48.3116 | 2025-09-04 14:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| e3e199c2-b6a0-3448-95b9-53bdd221dee5 | -10.4658 | -50.3907 | 2025-09-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| c9a36ea7-5462-30a6-bef3-d2e43566c188 | -11.8524 | -51.4954 | 2025-09-04 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| adb03ccd-5c8b-3caa-9247-d0bde5dc070c | -7.9341 | -44.9436 | 2025-09-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 9b739a13-aa53-3121-ade2-5fa97c8eaf3b | -6.0234 | -46.6562 | 2025-09-04 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| d03204fc-be1e-3ec3-94f6-af7e38ebb542 | -6.1665 | -43.3273 | 2025-09-04 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 9c707442-a844-303f-a864-21c382e6ec0f | -8.8851 | -45.7541 | 2025-09-04 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| c4db3bea-c79d-3558-8797-4712aa90224b | -7.7252 | -50.3174 | 2025-09-04 14:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a75fa63f-ebae-39bf-b5f9-17acfee60b41 | -15.5848 | -50.3129 | 2025-09-04 14:20:00 | GOES-19 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 410af483-2169-38e7-8424-14299f8cc8b7 | -5.6775 | -45.6314 | 2025-09-04 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| a6ce5c41-ee9f-3ce5-bf0d-e90ef4efc6bb | -13.8453 | -47.9988 | 2025-09-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 26b7eddb-0c82-334e-b20c-7570f2172e6e | -6.213 | -42.4294 | 2025-09-04 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 78e0e422-1cd0-390a-afe7-90bfcd98d5c3 | -11.8343 | -51.4339 | 2025-09-04 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 14751cbc-89b1-394b-97a1-992124f48b00 | -11.8521 | -51.5166 | 2025-09-04 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4ddb0d72-1cd1-3897-962a-1b7643b80e76 | -5.7 | -45.1786 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 268.9 |
| 20202216-7748-310e-8b4f-324d1eb5bf01 | -5.7177 | -45.2905 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 200.6 |
| e85fec56-4b2d-3f0f-a17b-137f259ec564 | -11.5782 | -52.094 | 2025-09-04 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 7cdfd64e-5de2-38c0-b1ef-140f627fd09c | -6.0232 | -46.6784 | 2025-09-04 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 11568b0c-5386-3ed1-a8e7-a354fffdcd47 | -11.3893 | -43.6075 | 2025-09-04 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| c74b726d-1523-3023-897c-4e863bf21274 | -13.8647 | -47.9958 | 2025-09-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 03103100-009f-39d1-a182-2dbea23d7406 | -4.9049 | -41.7696 | 2025-09-04 14:20:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 174.3 |
| f37c357d-5e2e-35b5-83ce-149f6827c455 | -5.6965 | -45.5851 | 2025-09-04 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0a135ab9-9d77-3a41-a3a1-d7be88a3794e | -5.7727 | -45.4221 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 0fff2a25-704a-3ed2-bc3b-1f8a1bb2b82d | -6.2606 | -43.2961 | 2025-09-04 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 3de2b3f1-ae09-39f8-a1d6-16c0d339637a | -6.8514 | -44.2656 | 2025-09-04 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 90b14288-c8e5-3214-be89-20fb45d695f5 | -5.6992 | -45.2692 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 226.8 |
| b45a5d2b-0d36-3795-8529-68f7b8d04290 | -5.7179 | -45.2679 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 196.0 |
| 5966fdc0-f828-3afd-b724-79559f62da38 | -16.5497 | -55.0991 | 2025-09-04 14:20:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 46162b13-8ab7-3b17-affc-566fcd631a58 | -5.6777 | -45.6089 | 2025-09-04 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 237.2 |
| 250b7b23-88f6-3331-a338-277beeb97d25 | -11.6599 | -54.5297 | 2025-09-04 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 6bfa7f42-95aa-3e5f-8f4a-1e23564f6403 | -11.0436 | -47.1409 | 2025-09-04 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 4ca5aee2-6e37-3ddf-b4f6-9bd9e40a513e | -7.9117 | -45.242 | 2025-09-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a756d60a-0c75-3f26-99ff-6f7f3e9b2fe6 | -15.737 | -53.635 | 2025-09-04 14:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 54a6192e-3dff-3085-bff7-480b72830785 | -7.7409 | -48.7772 | 2025-09-04 14:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 114.2 |
| c542ea10-591f-3265-892a-e4e4bc516206 | -15.4564 | -53.0183 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| b799184e-9b5b-3566-85ec-4107142088a2 | -5.6963 | -45.6076 | 2025-09-04 14:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 285.7 |
| 6b6b5045-12f4-34b9-bc44-255267553d4e | -10.1457 | -46.2424 | 2025-09-04 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.7 |
| aa6cc2ba-17d0-3366-87c1-ab2ac23b5b4c | -12.4785 | -48.0859 | 2025-09-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 646fa044-1a3f-3070-afb1-aa533cdd0d10 | -5.753 | -45.5362 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0108920a-9732-311f-9ca2-8af1050c3637 | -16.3377 | -43.1374 | 2025-09-04 14:20:00 | GOES-19 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 029167c4-c7d7-32b6-a4c1-a38618dd0788 | -15.229 | -52.7101 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a8bd0712-7d95-3f8e-8788-e1fab38c8a51 | -9.9597 | -51.6454 | 2025-09-04 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1ae800cd-a7c0-3af2-b6d5-b88e8259dca2 | -11.7385 | -47.7637 | 2025-09-04 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 770070f6-807d-3daa-b190-8b0e60c8dec8 | -5.7914 | -45.4208 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c6a5ba4f-d5ee-3e7f-b844-0944fcb0e6ae | -12.4593 | -48.0885 | 2025-09-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| 37caf6bf-4daf-3094-9554-d0b118f2994f | -9.6851 | -51.0186 | 2025-09-04 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 1de26a21-75a4-3cb5-9490-7ea180774396 | -15.2026 | -48.027 | 2025-09-04 14:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 47.7 |


[Clique aqui para ver as próximas entradas](README111.md)
