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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51c23c2c-17e2-3b78-9640-05ac7fbad3f0 | -6.9884 | -59.0457 | 2026-08-17 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| b4a9d5e6-9bd9-3237-9ca6-cc78da79127b | -7.6053 | -45.7238 | 2026-08-17 14:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 141.6 |
| f3c39221-2a99-310e-b21c-1a809fa1b75e | -9.2184 | -60.7921 | 2026-08-17 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 203b6b8a-c5db-35ed-9025-b83cfbd658e5 | -6.9884 | -59.0457 | 2026-08-17 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| e537a293-babf-31a6-adec-4bd2a1773126 | -5.5072 | -43.6808 | 2026-08-17 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5f0834ee-dade-30c0-a4e2-4b8eda41e6e7 | -7.1363 | -47.5205 | 2026-08-17 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| bbbe3834-3319-36fa-8343-8da341944042 | -9.127 | -46.0214 | 2026-08-17 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| baa4d56e-e129-3692-8269-864be4d5c540 | -9.2184 | -60.7921 | 2026-08-17 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| c36bfb03-1fbb-3241-b89a-d3b32f843c1d | -6.7832 | -59.4401 | 2026-08-17 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 585121cd-4117-3ac8-b5fe-90e13ecc20a2 | -11.1159 | -49.9138 | 2026-08-17 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 6fac3179-368c-3b53-bc22-ea003714e2cf | -9.7908 | -47.223 | 2026-08-17 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| a26d0bbd-c2b0-316d-b87e-9fa6a71e37f4 | -6.9886 | -59.0264 | 2026-08-17 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b6e564e2-7e19-3187-95d1-b1bd46815e7c | -11.3239 | -46.2955 | 2026-08-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| e4da7012-2526-37c1-a284-1e7a38922c07 | -12.5392 | -47.9 | 2026-08-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 8038dd48-e793-3dee-9548-fc3488b9c702 | -22.0767 | -55.9708 | 2026-08-17 14:10:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 956dad56-e716-337b-9620-5017d6399db3 | -11.4904 | -46.6118 | 2026-08-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 234.9 |
| 599b4572-c6b0-3b6b-89e8-2b1df0efdf4f | -2.1729 | -54.4265 | 2026-08-17 14:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 164c38c5-fdd7-3599-a27e-4a0d1be76c64 | -7.3824 | -55.4924 | 2026-08-17 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bac70366-4763-333b-9dc2-9f822b2cfe80 | -15.2645 | -52.896 | 2026-08-17 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 276dcdc0-fb0a-3874-bab6-09931a9c152f | -11.5099 | -46.5866 | 2026-08-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| b260cc47-ac2c-38be-877a-88402860b380 | -11.3235 | -46.3182 | 2026-08-17 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 600.2 |
| 15cf5fa9-9cdf-3442-91bb-20a658b29b28 | -12.5396 | -47.8777 | 2026-08-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 8424cf47-419b-378b-b5e9-93781e996bdb | -13.4123 | -54.3324 | 2026-08-17 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 160.9 |
| ba309309-10ef-3cca-a9f7-bef8a1e12b2d | -10.951 | -57.1497 | 2026-08-17 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| f2f88aa0-4e33-3b2f-9bbc-49be5f31ef0f | -13.5128 | -46.2219 | 2026-08-17 14:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 31eb9ddb-867d-3964-a2fa-95e3dc010603 | -15.4579 | -52.9334 | 2026-08-17 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d3917079-fec1-348a-979d-10f72bf93d89 | -8.5212 | -54.9016 | 2026-08-17 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 8a502a17-1df2-3178-9569-126eee60436d | -13.5124 | -46.2449 | 2026-08-17 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 0a532306-71ed-3ad4-9ffc-e5cc263726f6 | -6.7123 | -58.9412 | 2026-08-17 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 7c7137a5-d3d3-38a6-9e1c-47d631f4f05c | -14.4678 | -51.9832 | 2026-08-17 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e27df4c5-43b6-3799-b02b-503527a07038 | -10.9322 | -57.1511 | 2026-08-17 14:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 1f1cc6d3-58cc-3085-8730-0c64937271ef | -7.6053 | -45.7238 | 2026-08-17 14:10:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 7dd66d61-c0db-3aa2-89e0-b923ba2a954a | -9.1998 | -60.793 | 2026-08-17 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| dd997f07-95fb-349b-b314-03a42678424b | -14.4868 | -52.002 | 2026-08-17 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| e9e5ae60-0160-3b94-8a96-62939cac16fe | -10.2872 | -48.2483 | 2026-08-17 14:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| eb05978f-945d-3078-923c-30ac6b301ddc | -6.2565 | -47.7393 | 2026-08-17 14:10:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2835231c-775b-388d-b562-5803ba96cd24 | -6.2378 | -47.7406 | 2026-08-17 14:10:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6fd55e15-29fc-3820-9b8a-0deafd61565a | -11.4907 | -46.5892 | 2026-08-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 6f9e93ed-e90c-33cb-a26d-4dfee44741d7 | -9.3382 | -62.3344 | 2026-08-17 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5977ae14-119f-3a00-8a42-52e9cc2b8bb5 | -12.7009 | -48.5195 | 2026-08-17 14:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 8f0a14c5-4644-3b14-afea-80626263107a | -15.4384 | -52.9361 | 2026-08-17 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 043d9829-638e-3214-915b-3ac71bddf8a5 | -6.2563 | -47.7611 | 2026-08-17 14:10:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b3200114-9fbe-36d0-aad1-aa79defec20a | -8.9601 | -60.5165 | 2026-08-17 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 913fab55-faca-355d-a062-8ba4d1a4dd88 | -6.7087 | -45.373 | 2026-08-17 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e2203ecc-0b77-320c-8bb3-e97682757605 | -12.5588 | -47.875 | 2026-08-17 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| af6f05d6-3109-3a52-ac81-c9fcb2b6a671 | -11.5095 | -46.6092 | 2026-08-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 367.0 |
| d4711f2c-5d9a-3ba8-8641-4666e294fc64 | -11.472 | -46.5692 | 2026-08-17 14:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 492e98c7-46ed-3b13-b022-83ba4502d319 | -9.3196 | -62.3353 | 2026-08-17 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| c1f7f46a-cf1f-3b72-bd50-d7733a68924d | -5.5074 | -43.6576 | 2026-08-17 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 36d2c3db-93aa-3b10-978a-ca9a72a864b3 | -14.3878 | -53.3037 | 2026-08-17 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e86d8715-6c82-304a-bcaa-f896b17826ed | -6.7831 | -59.4594 | 2026-08-17 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 1fb58408-db51-31c5-b0e9-bc5507b57524 | -14.4871 | -51.9806 | 2026-08-17 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| f5f98b17-906e-3cca-8f73-d088543c4a4c | -6.7647 | -59.4601 | 2026-08-17 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 1d21aa1d-a446-3f7f-a2bf-e9eeaa5013d4 | -11.31 | -46.32 | 2026-08-17 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 26454dc3-247c-3e7e-a5fb-ea2fd8a74577 | -9.3382 | -62.3344 | 2026-08-17 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| faa925c3-3279-31d9-9324-eb8800c7b6c0 | -9.3196 | -62.3353 | 2026-08-17 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 59dfce10-4eeb-3c86-a187-810b188185b3 | -9.1996 | -60.8122 | 2026-08-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c6773c21-6234-3918-b2a3-9a3e2c5d3fd2 | -6.2563 | -47.7611 | 2026-08-17 14:20:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f3f5540c-bdc9-3e2b-bc8c-2f45d3ac3670 | -15.2839 | -52.8934 | 2026-08-17 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| d787c900-5757-3af4-b268-8f6f5b24189e | -7.7881 | -47.8607 | 2026-08-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| c2555a66-6bf7-3af5-8d11-379d3a5768ae | -6.7123 | -58.9412 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 5430995c-3a87-367d-9ba6-b1acd95a8fb7 | -8.96 | -60.5358 | 2026-08-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 395c9207-1a85-3412-9efc-09a0c5250685 | -11.1159 | -49.9138 | 2026-08-17 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 3eb6b622-751c-30ef-927c-7b66ce3f4c63 | -14.8619 | -46.6351 | 2026-08-17 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| e61a0f6b-cf4e-3b19-8a52-a2d940326982 | -6.7831 | -59.4594 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.1 |
| ff4f91fe-3b18-3702-aa91-7e6160d5e885 | -6.9886 | -59.0264 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b5b3ecb1-8612-3f2d-9fe5-0667e31e33ec | -14.2751 | -53.1287 | 2026-08-17 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 9c9c5e1a-4605-399e-8ec6-d8a347ee4b3b | -13.5124 | -46.2449 | 2026-08-17 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c44ff3bf-87a5-308b-97de-c17bf6d4e48a | -7.3824 | -55.4924 | 2026-08-17 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| d2dc1c20-ce9f-38e2-99d6-d1024b55befa | -10.5275 | -50.0208 | 2026-08-17 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| bce38a7f-4b20-35e9-888b-0fa44b92bec8 | -6.7122 | -58.9606 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| eac68b37-8f8e-39c5-8017-8d4a6e20d49c | -10.5085 | -50.0228 | 2026-08-17 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 4367ca5d-38c2-3e43-9cc1-81a34b4ca104 | -13.7836 | -53.835 | 2026-08-17 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 4eab1435-27fb-3144-a7ca-147b825f505c | -15.4384 | -52.9361 | 2026-08-17 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| fb2aeb60-d4b8-3b1a-b53a-b8ba6c47dfa2 | -11.3235 | -46.3182 | 2026-08-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 671.0 |
| 75066476-dbbf-3e1e-a97f-2a371338ce8f | -9.7719 | -47.2251 | 2026-08-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 93d6cfc4-19fb-3917-b5f3-708e4af15388 | -6.9701 | -59.0272 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| a77da7cb-c514-36cb-b2b4-e11cafca4175 | -12.5588 | -47.875 | 2026-08-17 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.6 |
| fe6e32d4-a658-3902-af79-70499c12c5da | -13.5317 | -46.2417 | 2026-08-17 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3a244605-9f40-3b5c-80b8-06fe490c4226 | -11.5099 | -46.5866 | 2026-08-17 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| ac7658a5-f481-3cbd-8721-4ab24ea322e8 | -10.9322 | -57.1511 | 2026-08-17 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 44ff4327-de89-34e7-9395-25cc4679ec77 | -22.0767 | -55.9708 | 2026-08-17 14:20:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 3b57c251-5625-3c17-a23e-249d6d6a9b46 | -11.5095 | -46.6092 | 2026-08-17 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 0632b3ca-7f0a-38dc-aa6c-aa432d7b4482 | -9.2184 | -60.7921 | 2026-08-17 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e5d268b2-faf0-3a74-90eb-1341878817b2 | -15.2645 | -52.896 | 2026-08-17 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 5162f14e-dfee-33ee-998f-c92923c4a344 | -11.3239 | -46.2955 | 2026-08-17 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 06ef1b0d-7f4c-3938-b3be-63f0695e6464 | -14.2947 | -53.1052 | 2026-08-17 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 27f688a1-70c9-304b-b22d-55a0ff3965e1 | -7.8071 | -47.8372 | 2026-08-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b874e8e7-36f2-3448-9686-26a6926aa7ae | -15.9233 | -56.4774 | 2026-08-17 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 496ecf78-adfa-3917-a9b3-160d34ec7385 | -15.9035 | -56.5002 | 2026-08-17 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 975eb59f-d0c0-3973-b62b-0691d636087a | -6.97 | -59.0465 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| e456a085-8d78-3961-9b7c-5ec953a59883 | -11.472 | -46.5692 | 2026-08-17 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 194.6 |
| e4eb73f3-81cb-3fed-895f-c8069e7572de | -6.7647 | -59.4601 | 2026-08-17 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 2c82d012-af84-367b-86e9-15a3d4db20cf | -6.7087 | -45.373 | 2026-08-17 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 279f5229-0190-38e7-ba6a-14142fe6252c | -11.4904 | -46.6118 | 2026-08-17 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 204.2 |
| df9329bd-53b6-3fe4-b0f0-6fb35df1f314 | -12.7009 | -48.5195 | 2026-08-17 14:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 9bd0e279-f86c-321a-8d56-69593f31e76c | -9.7905 | -47.2452 | 2026-08-17 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 816529fe-3c3a-37fd-a170-ba25ed5e8814 | -10.951 | -57.1497 | 2026-08-17 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 8fbe0345-24c8-3dd4-bd0b-1777e8f3909a | -6.2565 | -47.7393 | 2026-08-17 14:20:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 733c6219-58b8-378a-aeb9-69fc62a21201 | -7.8068 | -47.8591 | 2026-08-17 14:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 154.2 |


[Clique aqui para ver as próximas entradas](README72.md)
