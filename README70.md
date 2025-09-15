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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 028a4ae4-10b6-3f27-b66c-f24b5f8f8e13 | -8.9734 | -46.218 | 2025-09-15 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 889.6 |
| 41866909-0ba8-3cda-ba30-8a1610b94f40 | -12.9599 | -47.974 | 2025-09-15 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 6b10c7b3-2aa9-3cb1-b9d3-2e02032dbfaf | -12.6533 | -47.9507 | 2025-09-15 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 4fbafa98-877b-387a-b4ec-be56782fab72 | -6.98 | -44.5299 | 2025-09-15 12:50:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f03ae4c0-6afe-381d-b578-c25bb663fcb1 | -8.9601 | -45.7912 | 2025-09-15 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 119.5 |
| f279ab0a-78bf-377c-8eec-a5a47f79aaaa | -12.1668 | -44.0988 | 2025-09-15 12:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 3a0346e0-6dc9-3ec8-a5f9-14020fe3790b | -11.8097 | -50.5214 | 2025-09-15 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e4df7c8d-75cf-3fa0-8922-71199f2dc016 | -8.9412 | -45.7933 | 2025-09-15 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| c6fc1b84-0b02-394b-b4ef-60af5992b0f1 | -11.6622 | -46.611 | 2025-09-15 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 3b25b90b-c4fa-357a-a292-a297ccc82400 | -6.1884 | -41.1612 | 2025-09-15 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| b38dc8a5-ac03-340a-91da-acd3f414f73b | -6.1695 | -41.1629 | 2025-09-15 12:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 104.8 |
| 2c9e78e4-24b9-38c0-a4da-36d0b7374abd | -10.075 | -47.1908 | 2025-09-15 12:50:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 213.4 |
| 7b80e3bc-5c03-344a-b1b6-f4e565b08756 | -11.81 | -50.4999 | 2025-09-15 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| f51cdfec-0bec-3677-8122-84bc49efba82 | -8.9784 | -45.8344 | 2025-09-15 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 5143841d-b571-3fb8-a93e-e3f93673ca65 | -9.2235 | -44.5052 | 2025-09-15 12:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 13412222-bbb1-3e52-bd03-cbbf8eb2554a | -7.8756 | -43.5643 | 2025-09-15 12:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| e574b8a1-6d31-34f5-9a1e-5f54d2d1e2c3 | -13.9288 | -44.8106 | 2025-09-15 12:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 7ba3fc05-f785-3898-a2bf-8637c1b853a7 | -16.673 | -49.7615 | 2025-09-15 12:50:00 | GOES-19 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 0aa4e15f-4f88-3c41-805b-547846186866 | 1.57823 | -55.73761 | 2025-09-15 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| e2a5c7a0-3870-3609-b745-ac95c6c46ade | 1.70372 | -56.03381 | 2025-09-15 12:53:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 6468d042-58cd-3c6a-91da-229a0360781a | 1.57953 | -55.74672 | 2025-09-15 12:53:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| ba139696-dd1d-3b47-920a-c686701ee96e | -3.49932 | -49.02567 | 2025-09-15 12:53:00 | TERRA_M-T | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| be7d5f44-1389-33bb-8a39-5881e6111d56 | -7.70267 | -48.883 | 2025-09-15 12:55:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 8865a7ac-4d99-39bd-a38d-fa0504eb31ab | -3.65251 | -54.05515 | 2025-09-15 12:55:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 77f045dc-bdb0-36f5-8150-caeb5aee9c18 | -7.70573 | -48.85801 | 2025-09-15 12:55:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d1f99959-f532-3a4c-9d1a-9c692607ae02 | -7.70198 | -48.85102 | 2025-09-15 12:55:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 7ec66073-48fc-333f-b7ba-e6cacbdf338b | -4.54331 | -46.68963 | 2025-09-15 12:55:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 012e83b5-732f-3322-b5aa-6694c49399d1 | -7.69875 | -48.87591 | 2025-09-15 12:55:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ea7b1bcc-476b-338f-b8a3-b32aa8030ec9 | -7.79599 | -46.11337 | 2025-09-15 12:55:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 707a9244-fdfd-3eb3-9f83-f2647acff5f4 | -6.08075 | -50.16412 | 2025-09-15 12:55:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| e83be9da-3dee-35f5-84c3-6cd1979f964f | -6.07607 | -50.17594 | 2025-09-15 12:55:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 56fb0541-45c1-3c89-aa4c-37085b40c1ee | -7.64038 | -49.71332 | 2025-09-15 12:55:00 | TERRA_M-T | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 88d3bce1-bbca-3d34-adbd-d22e29891392 | -5.57813 | -51.97449 | 2025-09-15 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6fc3e4b8-1fa9-3e2d-9cc3-dbf1ca0d300e | -5.81618 | -51.3991 | 2025-09-15 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 3107271d-ed74-3940-8713-38050e332b8a | -5.81421 | -51.40782 | 2025-09-15 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 868508be-346f-33e3-abec-c07f8d3d3347 | -6.0783 | -50.1831 | 2025-09-15 12:55:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| ad3aef55-234f-334e-8bf7-5d20f1a80c84 | -6.07859 | -50.15758 | 2025-09-15 12:55:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 419e1f3d-d23f-3755-b81c-2895ea9ba14f | -5.81427 | -51.41362 | 2025-09-15 12:55:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 70dc592f-5453-38be-b0f3-d2fbc06d4ef0 | -11.79328 | -50.50123 | 2025-09-15 12:57:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| bbbebd35-d62f-309e-9885-ee927a3270e8 | -14.82219 | -51.6447 | 2025-09-15 12:57:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| b6c8274c-8dc4-3651-8472-d8917ebe9c76 | -11.8031 | -50.50792 | 2025-09-15 12:57:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 3e849eea-42ca-34a6-88c1-f3111e502d3e | -8.97243 | -46.24338 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1196.4 |
| e5a16eba-450e-346a-a2f3-21e2314b5ef8 | -14.61596 | -52.04319 | 2025-09-15 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 18d12863-d305-3def-9d41-3946d7a08f1d | -14.51345 | -47.33577 | 2025-09-15 12:57:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a1a64b39-5e5d-38a3-8256-ce6781ab3561 | -10.07569 | -47.20697 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 410.8 |
| 37a9ef43-698a-33bc-93f0-245a083da9ca | -10.92117 | -54.68231 | 2025-09-15 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 041c4939-e80f-30e0-bd5b-733430aec7ee | -12.77979 | -47.20609 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 307.8 |
| 98e23aed-2551-3c0c-b8df-342d193c50fa | -12.7816 | -47.21354 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 423.1 |
| d3e15754-0db4-3be1-a587-3d3e6eb0dced | -10.0752 | -47.16191 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| bd1fc0e7-583b-3f85-a3a3-3706dc2dfe7a | -12.21666 | -55.01484 | 2025-09-15 12:57:00 | TERRA_M-T | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31747211-8629-3d46-b106-a55947316e2f | -9.14268 | -61.16523 | 2025-09-15 12:57:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ce5da041-c39b-3ea2-92cd-68d493afdf6b | -11.62643 | -52.16885 | 2025-09-15 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 33b3adeb-216e-367f-b0fc-18789dc15a59 | -8.44419 | -55.61809 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d228c2ab-5a74-3140-a629-397ea36fad15 | -14.51419 | -47.3435 | 2025-09-15 12:57:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 4f89661f-6b80-309a-bccb-f5bede76d44a | -8.97294 | -46.24829 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 872.9 |
| 5dd55c91-0df2-359f-98b7-aa136303ebfd | -8.95483 | -46.24101 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 358.3 |
| 180a521e-fda2-38a9-9002-444cf53702a9 | -10.91898 | -48.19299 | 2025-09-15 12:57:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| af8ec299-8356-3a96-a07b-6af8b90e2b85 | -10.0875 | -47.20135 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 284.2 |
| 13dc8041-b0db-34b0-a48a-3aa80157f61c | -8.97749 | -46.20661 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 445.1 |
| 05a11e8c-8273-3248-8529-9eaca1dd52a5 | -12.67526 | -47.70282 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| cc847122-4b91-38aa-8007-7f08a7bb7be6 | -12.95686 | -47.98582 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| c9d78eae-31d7-35f3-b761-d75135ab77d4 | -10.07983 | -47.16956 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7653e35a-6e4a-3fb8-9cf7-d35e8a4a1cf7 | -12.64842 | -47.9555 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 46.9 |
| aca4e00c-93c1-36c4-a542-5023a8dfa948 | -12.81434 | -47.21044 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 166.2 |
| a17a0579-124a-315f-8e09-77c15cc37c9f | -8.65326 | -46.35548 | 2025-09-15 12:57:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 17ca55f4-19e4-3813-aaa1-79ca9a578fc0 | -8.95966 | -46.19889 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 2351d536-202b-317b-b503-80a39561e865 | -12.78006 | -47.94754 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| d239d94d-472c-3346-8cd9-68e64e7cc630 | -14.82184 | -51.63809 | 2025-09-15 12:57:00 | TERRA_M-T | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| f33b291f-b6b3-3e90-93c5-5d15e5343221 | -8.96002 | -46.19217 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| d9ab40e4-a3a6-3e68-8e8d-b8ec09703781 | -12.81612 | -47.21819 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| adffa55f-33b2-3cbe-a63d-762c0b4ec45d | -8.42082 | -47.22639 | 2025-09-15 12:57:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9a8d92aa-a837-32fa-9d4e-a55784076d04 | -8.69481 | -54.67843 | 2025-09-15 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9fd3ba0a-4a26-3a50-be8f-fc9cd790f16c | -10.0631 | -47.16747 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 1e48dd60-cd56-32cc-9df4-1a4bc615dfcd | -14.53194 | -47.34307 | 2025-09-15 12:57:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 48749f6a-96a7-3baf-803a-bc8dd749d969 | -8.69617 | -54.66846 | 2025-09-15 12:57:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 61367b3e-3f64-3ca9-bff9-98e17b790bab | -12.66477 | -47.95749 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 10fd3452-ec7f-3ec5-aeb9-db02326b9c17 | -11.0869 | -49.74526 | 2025-09-15 12:57:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 7edb5e52-3718-3e6b-9a54-0ed715ad7f87 | -10.94008 | -47.35739 | 2025-09-15 12:57:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1d4e61c8-2ed1-329e-a7b2-e7a35459af72 | -12.78986 | -47.94329 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f51d3c8e-0531-3f44-a942-b622e9a56057 | -8.59956 | -46.34378 | 2025-09-15 12:57:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| f1e1d378-23b3-3317-bf83-68adbae683c1 | -14.42862 | -53.36325 | 2025-09-15 12:57:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5957dd1d-83b6-354b-965a-54ed945d540f | -8.95498 | -46.23376 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 306.9 |
| 60bbc4a3-c2fd-36f1-91df-edd4f9f4b848 | -12.7971 | -47.20798 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 131.1 |
| c3332d6b-ad1d-3b7b-b31b-058ca5af2620 | -8.60105 | -46.34897 | 2025-09-15 12:57:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c07d55eb-9934-3015-baa1-261365fb2124 | -12.77744 | -47.25469 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 293.7 |
| d3150cf4-00c5-3896-b191-b9160e7d900b | -11.70564 | -59.3126 | 2025-09-15 12:57:00 | TERRA_M-T | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| b9fd5ef8-06f4-3c9c-aa4b-79ce9b9cfdab | -10.96116 | -47.17073 | 2025-09-15 12:57:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 063c20f6-2eb4-38ca-9c75-102af9eabfdd | -8.97725 | -46.20176 | 2025-09-15 12:57:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 395.8 |
| d914ac5e-60bf-3887-9a62-a3ff1fcae04f | -10.90325 | -48.19146 | 2025-09-15 12:57:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 161.7 |
| f905b274-805a-3f71-afae-4e247dc6b0fa | -12.96647 | -47.98171 | 2025-09-15 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 080ca335-fc78-3715-9929-35eeef5e4e8a | -9.14482 | -61.15153 | 2025-09-15 12:57:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| fd8ef0df-ce18-39f9-b845-74c91173ee46 | -8.44289 | -55.62721 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1960df5d-fd23-3154-a1a9-703105f43311 | -12.77539 | -47.24697 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 358.0 |
| ec7717f1-3ba1-39a2-9bbf-556b8e18ee69 | -9.74121 | -55.37117 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 8ff8b591-eb1c-3045-a860-d619d40b7aae | -8.41159 | -47.23162 | 2025-09-15 12:57:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| adae3118-b7a7-3ec2-9f9d-17a4d9cde7c0 | -10.07081 | -47.19933 | 2025-09-15 12:57:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 175.0 |
| ed5a220c-4270-3a06-a9d0-3452575f2fc7 | -11.54764 | -49.03698 | 2025-09-15 12:57:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| dff682de-d1b6-361c-838f-00b31d49fce0 | -8.65179 | -46.35001 | 2025-09-15 12:57:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a5a360aa-3029-36bc-aa03-a358dc379b15 | -12.82043 | -47.17656 | 2025-09-15 12:57:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| f5feb953-8be8-37cb-8499-49ab1eab3b3c | -9.69216 | -61.99752 | 2025-09-15 12:57:00 | TERRA_M-T | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |


[Clique aqui para ver as próximas entradas](README71.md)
