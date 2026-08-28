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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 355891c6-4fc3-3d84-9b22-2b1cb769215f | -4.3022 | -59.4634 | 2026-08-28 18:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 99e2d369-e9a9-3472-adae-9800def53cdf | -8.5975 | -54.715 | 2026-08-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 5831b4ec-54f9-3efc-b690-c03e4a6ed4f5 | -10.4693 | -46.1802 | 2026-08-28 18:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 41829fcc-ec6c-369d-bd10-197b23b5fd6d | -8.6311 | -66.5287 | 2026-08-28 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| c9309d5a-8d0e-3fa2-af86-d38946bb6fb8 | -8.8184 | -49.6308 | 2026-08-28 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 6d2ab7f9-7bd3-3f4d-bdfc-9080d4dac33c | -7.529 | -61.3635 | 2026-08-28 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 4e4d33f4-b9c0-3a57-a1d7-9b057afd3219 | -7.3663 | -55.1734 | 2026-08-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 6df14682-b44f-33a6-a76f-8cf6315cc848 | -12.7797 | -44.2576 | 2026-08-28 18:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 18a09407-d63a-36c1-a078-b66b43014f50 | -6.9336 | -58.9514 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 175.0 |
| 0e59f35e-d432-365f-8622-5a6767347fbf | -8.1432 | -64.0053 | 2026-08-28 18:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8a8befd4-a0d8-3014-8067-9b6dbbec371b | -11.1452 | -45.5694 | 2026-08-28 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4684cac6-f484-3711-b83d-2e651b9219b3 | -6.2538 | -55.4109 | 2026-08-28 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c0ece285-d409-33bc-abc7-075bf223f53d | -8.8576 | -71.3159 | 2026-08-28 18:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 87ec37bb-adf4-3ea9-932e-ad75a2ed0b0b | -8.8886 | -66.893 | 2026-08-28 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a7be59a0-ae1e-3d97-b9fd-d38fb52a9593 | -6.3677 | -54.966 | 2026-08-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 2b3b6edc-c899-3f04-9230-f1b479da8b9d | -9.1525 | -49.9639 | 2026-08-28 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 53f702b6-47a7-3d05-81d3-7b55c32c30a0 | -11.0247 | -49.6656 | 2026-08-28 18:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 3bf98c2f-c2e7-34f6-b82b-a8dc1b9f8240 | -14.8817 | -52.6293 | 2026-08-28 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 947.5 |
| 27d73401-72d8-3a92-97cd-a83c1035487e | -8.87 | -66.8935 | 2026-08-28 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 47479ea1-e3ba-3c33-878f-151e3d445da1 | -11.2128 | -53.9976 | 2026-08-28 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 269376d1-9efe-3ac3-ad24-0f3877d12f89 | -6.1841 | -57.7786 | 2026-08-28 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| f81024c1-f28d-37e4-8f15-f1317a9f822b | -9.1711 | -49.9835 | 2026-08-28 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 20047790-ad48-3d4c-bf1d-3db11e32f708 | -14.8627 | -52.6106 | 2026-08-28 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 72d7fdf5-bcac-387c-9ff3-14bce4ae5b09 | -6.8569 | -59.4564 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d87b4000-9dd4-38b7-953a-47ab40dff9e1 | -6.8542 | -59.9372 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| b476b66b-53e9-3fc7-8591-42dace1bf4f1 | -6.5865 | -55.4346 | 2026-08-28 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e0213e47-78df-3826-a24c-0660626ae268 | -14.8814 | -52.6505 | 2026-08-28 18:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 110.0 |
| a2e9554f-b697-38bc-b91f-82da3ecf4569 | -10.3897 | -61.2118 | 2026-08-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| c01a53f2-f984-3d72-989b-f2acd2d59e4f | -8.6487 | -62.8376 | 2026-08-28 18:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2d039761-5444-3443-a357-9f412475fa5a | -11.2314 | -54.0164 | 2026-08-28 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b93f0b4c-c69d-3296-a62f-d73ec23f0cbd | -6.1795 | -45.9097 | 2026-08-28 18:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| a054b5f2-90f3-31f5-b438-5bcdc79b9aaf | -7.3478 | -55.1744 | 2026-08-28 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c3990c03-5b3e-3f4c-9b8c-bfd32fad4a9a | -6.7513 | -55.6853 | 2026-08-28 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 85f7af98-0f70-3233-9d99-233664d17db9 | -6.7094 | -59.443 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 52e0717b-fd06-3393-a866-ece51b0b266a | -4.3021 | -59.4826 | 2026-08-28 18:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 12761387-05fa-37ab-9f3a-3b24981f859a | -9.1711 | -59.618 | 2026-08-28 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 75a628c9-616b-36cb-b8ea-aa82b9208b92 | -10.3205 | -49.9567 | 2026-08-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 78c3c331-87e7-36c4-8ee3-edba7c8def31 | -9.1713 | -49.9622 | 2026-08-28 18:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 90d6f027-eb5b-3157-b371-5cb7fc587207 | -10.4689 | -46.2028 | 2026-08-28 18:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e170e605-4fbf-3a40-984e-d47ba1edc684 | -9.4329 | -51.6926 | 2026-08-28 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.9 |
| faa84805-fc8c-3ada-a54b-55ca7b6a7f06 | -9.2093 | -59.4803 | 2026-08-28 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e47ba893-2258-339d-b95c-cb311fbb259b | -10.3013 | -49.9801 | 2026-08-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 97bfadab-916d-3600-9cf2-cb282c2305f2 | -14.1838 | -52.8245 | 2026-08-28 18:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 8ebd99e0-a8bf-30e5-a084-90fd35717b24 | -8.1617 | -64.0047 | 2026-08-28 18:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5874425d-f332-30f1-943a-43f05760f080 | -6.8386 | -59.4379 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4749f800-e110-31e7-a3d1-89b11d5c1d9c | -7.5104 | -61.3832 | 2026-08-28 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8095fa79-89c2-39f3-8917-e551c5341626 | -11.9684 | -45.4985 | 2026-08-28 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| acc59faa-4bb4-3930-ad74-e55ba9ca23a5 | -11.025 | -49.644 | 2026-08-28 18:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 2a2c9e03-d510-3131-8583-54be0a5a63c2 | -14.1645 | -52.8269 | 2026-08-28 18:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| b2c5d0b5-61cb-3003-827a-941fc22e9dea | -6.9521 | -58.9506 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.4 |
| b9c563be-5cf7-3b37-ac5c-69ed8963e72e | -14.5448 | -51.9943 | 2026-08-28 18:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.1 |
| cb082d6a-92dc-3cb0-b52a-c6a84533003b | -4.3205 | -59.4821 | 2026-08-28 18:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 8f8d34a9-6d53-3bcc-9a8f-a9b4f7e84ddf | -8.3785 | -70.8456 | 2026-08-28 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 65.6 |
| cc9cdfbe-5779-38e3-8351-42d8734e6a74 | -14.6024 | -53.1508 | 2026-08-28 18:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 473d934e-81fd-3866-9746-896150094849 | -14.8821 | -52.608 | 2026-08-28 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 772.4 |
| e33193b3-a69e-3aa4-b7e0-c498428d7f23 | -6.5323 | -55.2378 | 2026-08-28 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 129.5 |
| b6b4e749-037f-3440-9077-6b3c391e815f | -14.8624 | -52.6318 | 2026-08-28 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 164.3 |
| 310bb62b-3db5-3859-8c76-7d7a7fa5c4e4 | -14.3182 | -51.7046 | 2026-08-28 18:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9f9e83a2-8d2e-33e8-b04e-8aa6c450ad7c | -11.006 | -49.6461 | 2026-08-28 18:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 00aa493f-11f5-397b-bbdb-e9210f2e85f3 | -6.857 | -59.4371 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 7b80c592-fea7-3f7a-addb-b64cb560ebb1 | -9.1976 | -61.1 | 2026-08-28 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3676cb67-345e-3c72-91cf-eca240cefb0c | -7.5662 | -61.3049 | 2026-08-28 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 4d13ec69-d882-3314-bef3-f84eef630ebd | -8.776 | -50.0616 | 2026-08-28 18:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 7e0ba37a-2882-3366-bd9a-b9cced5af6d7 | -6.8357 | -59.9571 | 2026-08-28 18:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 3230f4cc-1257-39da-88a2-a7d3e581731c | -7.4735 | -61.3846 | 2026-08-28 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 80c8b912-2325-30ee-aa00-9742d4e296f0 | -9.7878 | -43.5506 | 2026-08-28 18:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 109.9 |
| ec6f375d-a9b4-31dd-881d-a3caae08e490 | -6.8358 | -59.9379 | 2026-08-28 18:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 02e9a76c-260d-38f3-b13c-789be30b8131 | -10.4499 | -46.2052 | 2026-08-28 18:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 845c0acc-915b-3f0f-9514-642772144b0f | -11.6212 | -54.5947 | 2026-08-28 18:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 08f51ec1-a4f6-3c9f-b831-c460fb4c0ec7 | -6.8571 | -59.4179 | 2026-08-28 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 758acd1b-a4ec-389d-a8d5-703e9c94b268 | -3.2361 | -61.2359 | 2026-08-28 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| e9d4adaf-f604-373a-af5f-951fa39ed72d | -8.5365 | -55.2826 | 2026-08-28 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| a7bfe97e-4ccb-391c-b941-8d6b962ae864 | -15.6139 | -56.4103 | 2026-08-28 18:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| c31402b4-65c9-3651-9097-b69492f27f6f | -7.5289 | -61.3825 | 2026-08-28 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 43369009-81cc-3866-ad4a-b80b6b039f3a | -14.419 | -52.5837 | 2026-08-28 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9f7a3a2b-756b-3951-b5aa-05c3c20517fd | -10.3898 | -61.1925 | 2026-08-28 18:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 792843d9-79ef-381c-b32e-2985eb8499c4 | -6.0005 | -57.6689 | 2026-08-28 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 934b685f-7c05-343e-8349-b50043d6cbb6 | -10.3391 | -49.9762 | 2026-08-28 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| e6ee2233-aee2-3d1e-acb4-cb76e95cc700 | -9.4825 | -66.6347 | 2026-08-28 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 9a9e7251-f679-372a-854e-0e011adf534b | -7.5478 | -61.3056 | 2026-08-28 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 161.9 |
| ce658563-b1a6-3f37-852c-dc77a700ae2f | -8.631 | -66.5473 | 2026-08-28 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 54c860da-0cc0-35d4-933a-e28533c82173 | -9.4517 | -51.6909 | 2026-08-28 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 898549c5-9019-37a8-a4ad-f2b6b6018b9a | -7.5479 | -61.2866 | 2026-08-28 18:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5f7d06c5-1bd1-3240-bae2-9341cdacbd30 | -26.61102 | -50.35324 | 2026-08-28 18:43:00 | AQUA_M-T | MONTE CASTELO | SANTA CATARINA | Brasil | 4211108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| d5e6b835-279b-3910-9081-67dd90776a52 | -26.60481 | -50.35923 | 2026-08-28 18:43:00 | AQUA_M-T | MONTE CASTELO | SANTA CATARINA | Brasil | 4211108 | 42 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 4b3aaaf2-27d7-3022-acf7-c9342c6a38ce | -27.25634 | -49.50002 | 2026-08-28 18:43:00 | AQUA_M-T | LONTRAS | SANTA CATARINA | Brasil | 4209904 | 42 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 5c02a801-3df1-34f4-910b-b8deaf67d604 | -27.15412 | -51.97068 | 2026-08-28 18:43:00 | AQUA_M-T | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 129.6 |
| 888147d7-b676-3c6f-a6a6-d4e39bc61ebd | -27.1425 | -51.97906 | 2026-08-28 18:43:00 | AQUA_M-T | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| 903f88b0-b79d-36b7-9541-18baeb600156 | -24.49938 | -48.97559 | 2026-08-28 18:45:00 | AQUA_M-T | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 86e0fd6b-7988-38e3-9a71-39476cbb4bdb | -21.64438 | -46.06182 | 2026-08-28 18:45:00 | AQUA_M-T | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| aa2d9223-9581-3c7f-9a1c-40a9fb15e933 | -21.32532 | -45.92749 | 2026-08-28 18:45:00 | AQUA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 1bd382b4-d2e2-3284-94c5-4b8eb5001d89 | -23.1995 | -46.97853 | 2026-08-28 18:45:00 | AQUA_M-T | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| c3a32836-2873-3fd7-be71-3e4a18a2360f | -21.05395 | -43.92964 | 2026-08-28 18:45:00 | AQUA_M-T | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.2 |
| 34340b71-9859-3487-866a-5e070fdb5432 | -23.20114 | -46.9915 | 2026-08-28 18:45:00 | AQUA_M-T | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 88cd00b6-1060-3226-8d4f-7aa232356541 | -21.03079 | -40.91017 | 2026-08-28 18:45:00 | AQUA_M-T | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 23.3 |
| bb378ebd-ec22-3203-bcad-071849b507ac | -21.32676 | -45.93805 | 2026-08-28 18:45:00 | AQUA_M-T | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| e5c85483-2a1f-3efb-b19a-721e2165eeaa | -24.90083 | -48.47532 | 2026-08-28 18:45:00 | AQUA_M-T | BARRA DO TURVO | SÃO PAULO | Brasil | 3505401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| aba69b9b-093f-3d00-8ec4-703ec44a8022 | -21.05333 | -44.43656 | 2026-08-28 18:45:00 | AQUA_M-T | CONCEIÇÃO DA BARRA DE MINAS | MINAS GERAIS | Brasil | 3115201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 5726bd74-0e91-3d9d-a7f7-716d1f610017 | -21.02897 | -40.89895 | 2026-08-28 18:45:00 | AQUA_M-T | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| edfe7cb6-30d9-3fb4-a37a-c9368c9d711c | -23.49618 | -45.39366 | 2026-08-28 18:45:00 | AQUA_M-T | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |


[Clique aqui para ver as próximas entradas](README161.md)
