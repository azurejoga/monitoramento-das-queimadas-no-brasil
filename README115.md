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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe9a054f-0eef-3745-9a36-e595dd8a850b | -5.9189 | -45.7941 | 2025-09-10 14:20:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| e1a8900b-d7fc-3e87-88da-4159ef4e42e6 | -5.6788 | -43.3425 | 2025-09-10 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| c99c5cb8-bc82-3bfd-8d9f-8380ccfa0d75 | -9.055 | -45.7583 | 2025-09-10 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 98bca7ae-dfac-3aca-ae9e-0356a1a766cd | -4.7346 | -44.4457 | 2025-09-10 14:20:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1e22c315-6360-3ea9-b581-0e37e7ba82b7 | -7.5405 | -48.2521 | 2025-09-10 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 144.1 |
| 5dea358b-5ec4-3ad5-8e3d-86f1a716dd05 | -8.994 | -46.0808 | 2025-09-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 08f49101-53e5-3cee-b7c5-e1fb9ce3c725 | -15.0627 | -50.1527 | 2025-09-10 14:30:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f2ba23fd-8a98-3f99-a6f6-3468fb0e7877 | -10.8319 | -46.0889 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 156.1 |
| d04465a0-7fc2-360a-b217-8d910e1aeda3 | -7.7104 | -44.7598 | 2025-09-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 8bd4abdf-4131-3436-8ecf-4db6fad213e6 | -12.9477 | -54.793 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| cc1cae7c-d3e1-37cc-bbbd-ce0222fa7df3 | -4.7346 | -44.4457 | 2025-09-10 14:30:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| e5e8c9c4-4ae9-3e81-aa0d-6b575bdaff45 | -5.6788 | -45.4738 | 2025-09-10 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| cefd1463-3814-38df-a83e-eeeff8c2d6f0 | -8.0794 | -48.6407 | 2025-09-10 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 183.3 |
| 8ea26554-9b71-31d9-90d7-8602d1046d44 | -9.0579 | -46.9688 | 2025-09-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| a0e5a7e0-441b-3acd-ba68-8a734b3039a7 | -9.8649 | -50.1737 | 2025-09-10 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d07f70bb-58cd-34af-b241-10d1f5477bea | -5.5888 | -42.9282 | 2025-09-10 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 139.4 |
| 2340c36f-810e-357a-ad5e-31d9bba922ea | -7.7439 | -50.316 | 2025-09-10 14:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 06beba71-1168-336d-b2b0-357b9be3fd2b | -6.3615 | -42.6059 | 2025-09-10 14:30:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 8f4ce2d9-2ffd-32d4-b232-dac204cda78f | -15.1021 | -50.1249 | 2025-09-10 14:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 2591c5b7-46de-343c-9fd8-0bb47763eb37 | -12.1885 | -50.6482 | 2025-09-10 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7058ef72-6426-3d07-ad7d-e2f0c3ac2ab6 | -11.2834 | -46.4365 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 43723056-4c92-3dca-bf1f-01f341d1cee4 | -11.1247 | -52.0149 | 2025-09-10 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 408.4 |
| 44e488e6-59e5-3855-9875-1c06bddca5c6 | -12.1889 | -50.6267 | 2025-09-10 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.7 |
| a54db0fd-b51c-3eee-b894-9bb7b5c32d75 | -7.5218 | -48.2536 | 2025-09-10 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 215.5 |
| 1bf8c4a5-7eba-37c0-b788-a349c4e84528 | -9.5137 | -54.6292 | 2025-09-10 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| d97315a3-11e3-3cf8-8d69-6704e18e23ab | -7.9352 | -44.852 | 2025-09-10 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 70db7945-7821-34d4-8703-072b3bd2e814 | -14.5612 | -52.1623 | 2025-09-10 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8b5055bb-c5b4-34e3-b921-efd32384074e | -6.2597 | -43.3895 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| f9f88931-c93c-3c87-985b-814308b9b261 | -6.2407 | -43.4144 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 227.4 |
| f44ddd5a-960d-389c-b3a4-342f436b36d8 | -9.0132 | -46.0563 | 2025-09-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 1a3b3057-77c9-3f2e-bb94-3709e4d1e50e | -5.8079 | -45.6673 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 846d1017-f13f-39c0-961f-0651dbd0e6ac | -6.2595 | -43.4129 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 251.3 |
| 86cfa689-8f76-318e-bd86-336ee32e2d89 | -6.1896 | -41.0398 | 2025-09-10 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 174.6 |
| 40768856-b4d8-3559-bc00-ebac623c1c41 | -14.3882 | -53.2826 | 2025-09-10 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 183.0 |
| a5c08c2d-c50b-32bd-8c23-d2fc8735109d | -9.8838 | -50.1719 | 2025-09-10 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 156.1 |
| 709f0a23-d2c6-31e9-aa30-cc0f74c04e43 | -6.8261 | -44.8863 | 2025-09-10 14:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 443dffa3-09de-3e65-bd40-299e9b5bd43e | -5.9002 | -45.7955 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 01f098c8-e4c9-3f8f-924d-3a32575e5ff9 | -11.4702 | -50.3461 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| 3acbbf99-50f4-3aff-b25e-4d9dd772ee43 | -5.6738 | -43.9 | 2025-09-10 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 4171918c-8fd9-3feb-b114-b234951e8bae | -5.5702 | -42.9062 | 2025-09-10 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 110.8 |
| c1614bc6-40e6-3be8-bf96-077e06d056e6 | -6.2085 | -41.0381 | 2025-09-10 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 95514a56-23f6-39d6-90da-14915f6a157b | -9.7777 | -51.1366 | 2025-09-10 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 758a38bb-2d89-3936-bad0-257955264030 | -14.4004 | -47.327 | 2025-09-10 14:30:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 4731d26e-4370-3c1c-9507-b98b60d16cf6 | -9.6821 | -46.8791 | 2025-09-10 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 145.3 |
| c2b7d050-2b8c-3df9-af23-5460288d697c | -9.5135 | -54.6494 | 2025-09-10 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 88c36cde-84e5-3a3c-8cee-b49f23e96e1a | -7.5033 | -48.2334 | 2025-09-10 14:30:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 189.0 |
| bb68bcf1-5c2a-3473-b646-94b20c9d8248 | -12.1993 | -53.8611 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 77735207-78ca-339c-9ca9-b0d2dd2aebe4 | -14.5609 | -52.1836 | 2025-09-10 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c5e7c581-4706-302b-aa4d-15126bad8b33 | -8.9943 | -46.0583 | 2025-09-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 6c086531-f25d-3789-851a-d49573f4b30c | -9.6095 | -48.0588 | 2025-09-10 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| b11ab151-3fd8-3af6-9deb-9854ec701ef6 | -6.2409 | -43.3911 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.5 |
| d7842e73-78d7-3200-b58e-c816151ef33d | -5.589 | -42.9048 | 2025-09-10 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 146.0 |
| cf5682d6-6cd5-3ba1-b642-3573be34e00e | -9.7589 | -51.1383 | 2025-09-10 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 0a80fdb4-fb35-30b4-83dd-6ad25d7e965b | -12.9474 | -54.8135 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 4089c100-177c-3cf0-907a-4b3f43abb573 | -10.016 | -51.6611 | 2025-09-10 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 111.1 |
| b9efd5e2-7a0e-32f7-8d21-8097b9893513 | -6.8523 | -47.8925 | 2025-09-10 14:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 8d29a3bb-5383-3166-982a-ae4c833e386d | -11.2196 | -54.9975 | 2025-09-10 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 3a990068-91f6-3d21-a7c8-96c89a981296 | -6.3806 | -44.4434 | 2025-09-10 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ecf000f2-e9d7-393d-b817-04aa8edd2d28 | -12.9292 | -54.7538 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| bb4a9691-4ac8-3f24-8773-d1fa49b361b6 | -12.5286 | -45.2987 | 2025-09-10 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| c51b328b-988d-3425-a19c-19f8b088a2fb | -16.5117 | -55.0415 | 2025-09-10 14:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 9a6db0bd-38c6-3312-b26d-aa8df9472458 | -7.7893 | -46.0667 | 2025-09-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| cdce1f97-f38b-3ba2-b6d6-b36690c7184f | -5.397 | -43.4332 | 2025-09-10 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 0642e279-a688-37d0-bc1c-29fb68a04f66 | -11.1187 | -48.4369 | 2025-09-10 14:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b6b1b0ed-5454-347d-949b-08fadde6c898 | -11.507 | -50.4276 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 3fba9225-c86a-36d3-ba33-d9fe1085e590 | -13.1176 | -54.9191 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 8b0ad39c-d425-3db7-829d-74705150f35f | -15.1374 | -52.4039 | 2025-09-10 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 209.9 |
| fb8f751b-e868-3f1c-9ba2-d2002978da7a | -11.3393 | -46.5193 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 6524e3d7-b6f2-353c-b805-52f20930b45d | -6.3993 | -44.4419 | 2025-09-10 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| dc285911-18a1-39cf-b699-7d93057dea05 | -9.1142 | -46.9851 | 2025-09-10 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 6f9b84f7-97ae-36fd-90f8-02cedb131111 | -6.8519 | -47.9361 | 2025-09-10 14:30:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 3ab52073-2259-36d6-874a-8f34141185bb | -12.1803 | -53.863 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| e59e4661-8be5-3c03-8eb7-9e83503154e3 | -15.2881 | -53.7777 | 2025-09-10 14:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| fe6c9a0a-cc90-3e3e-98e6-34f4865e1c8f | -5.679 | -45.4512 | 2025-09-10 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| ef04ffdf-5883-32eb-bfdf-d47c760e3616 | -10.7373 | -46.0558 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 356e0e5b-dc7f-397b-888b-9a11855d1a62 | -10.0155 | -51.7031 | 2025-09-10 14:30:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 83e346ef-11b1-381a-83d5-08ff3b9d25c1 | -12.5796 | -44.6412 | 2025-09-10 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 989201e8-afcf-3926-8b7c-377273f19888 | -11.9535 | -51.081 | 2025-09-10 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 84626cf7-1ded-3af5-a55d-6b2a1dc69ce1 | -9.7599 | -45.4048 | 2025-09-10 14:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 145.1 |
| da459d94-1781-3ffe-b0e0-df5ff59bb6e4 | -19.282 | -47.9946 | 2025-09-10 14:30:00 | GOES-19 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 827f196e-0c4f-32f4-839b-5504390a9ce8 | -9.8263 | -46.0549 | 2025-09-10 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 9d128aee-8c3a-334f-a412-4f2816d86ff2 | -11.1245 | -52.0359 | 2025-09-10 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 356.0 |
| 0301fe3c-5c3f-3c2e-9db0-59d193cdbc8a | -15.801 | -52.2472 | 2025-09-10 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 6776ebd3-505c-3ac9-a577-c38fc601b1fd | -7.8812 | -46.2374 | 2025-09-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| c9b483f5-38a6-3e55-ac6a-575b77ce8110 | -5.6272 | -42.8313 | 2025-09-10 14:30:00 | GOES-19 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| f32d0d21-0b27-3ba4-a6c2-4622d845cba3 | -5.57 | -42.9297 | 2025-09-10 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 30314175-b2e9-37fc-8965-c0c139a757fc | -6.204 | -43.3241 | 2025-09-10 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| e68fff2d-3dd9-34d3-bdaa-4ba779f1a100 | -5.9362 | -45.9498 | 2025-09-10 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 585a10c4-8e11-3214-9315-72da9d32d7aa | -9.0768 | -46.9668 | 2025-09-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 69e33385-b1f8-3b6f-a6d0-d806a51b8dc0 | -12.18 | -53.8836 | 2025-09-10 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| c57c534e-1362-3b94-8676-945790c5d0b9 | -7.8081 | -46.0649 | 2025-09-10 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 63f5e7af-9dd7-30e8-bba3-df44d2e68a7b | -14.7542 | -45.3156 | 2025-09-10 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 7f6390b3-31df-35e3-a957-c5efe2f3002f | -10.7369 | -46.0785 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 449.4 |
| e57f68b6-cbf7-3766-96b5-a2304ad78e82 | -9.7011 | -46.877 | 2025-09-10 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 24dc20df-f383-32ce-a038-5f1c55e54644 | -9.7591 | -51.1172 | 2025-09-10 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 281.8 |
| 700d40a3-dc46-34b6-bd0b-f75a774a96bc | -10.851 | -46.0864 | 2025-09-10 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 285.7 |
| 73ea5784-cb5e-38ab-9087-70746a0217c4 | -11.7706 | -50.5901 | 2025-09-10 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 08623339-bbd6-3ff6-bdb0-a8060aeb8468 | -6.2043 | -43.3008 | 2025-09-10 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0eceb7b1-2004-31bd-be8d-d70f676edf0d | -9.6098 | -48.0368 | 2025-09-10 14:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 6a2deccb-4d62-3502-8ecd-8104d2913b7f | -8.0416 | -48.6656 | 2025-09-10 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 142.2 |


[Clique aqui para ver as próximas entradas](README116.md)
