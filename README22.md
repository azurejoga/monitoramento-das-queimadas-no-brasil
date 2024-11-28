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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91df9d80-922c-37be-9145-a2ff16af0d7f | -2.5963 | -53.9771 | 2024-11-28 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| a4fc84b5-c624-3745-bf4c-e66ef1bcb108 | -1.6629 | -52.4744 | 2024-11-28 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| b0fff0cd-3975-3832-b380-3ece2fa7b56a | -18.7781 | -55.84318 | 2024-11-28 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.5 |
| a1ba7874-8788-3010-9cc6-cf650d093d5a | -21.60688 | -57.49904 | 2024-11-28 01:45:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 85983a1d-65be-3687-9145-9d13f5977abe | -18.77606 | -55.83039 | 2024-11-28 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b6703170-399c-3e67-bcf3-a009c9c97f9f | -18.76783 | -55.84505 | 2024-11-28 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 6f8ea15c-c1e3-3124-b122-51ca3a09b847 | -16.07805 | -59.71415 | 2024-11-28 01:47:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c825a126-2bf9-312e-b16e-af98b584d071 | -16.16427 | -59.60959 | 2024-11-28 01:47:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 87f58b07-f9d9-3d37-9206-2ca2f9da8c37 | -17.63348 | -57.57072 | 2024-11-28 01:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 329ebdec-3145-3f54-a357-3b3b0695808a | -17.56618 | -57.47951 | 2024-11-28 01:47:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a74451d3-a427-3395-a871-3dd54fb30ebb | -16.88719 | -57.51587 | 2024-11-28 01:47:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 175d3f2a-93b9-3e03-abed-86e47c68a81e | -12.58466 | -62.00694 | 2024-11-28 01:47:00 | TERRA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ea6f2dbc-45ab-3e57-bfb4-f8376903ca01 | -11.83819 | -62.67666 | 2024-11-28 01:47:00 | TERRA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5d9f4dc-cf32-338f-b15d-268ad13c2ca2 | -17.57434 | -57.59788 | 2024-11-28 01:47:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ad5c9bc3-c7ee-31a9-a74f-ead35bcaef10 | -16.07761 | -60.10642 | 2024-11-28 01:47:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| dd3dcfa2-6ea4-35ea-a5aa-096df5971e1a | -17.57592 | -57.60842 | 2024-11-28 01:47:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 818a4219-ffa6-3742-96db-53cc9022aef9 | -15.69249 | -59.14857 | 2024-11-28 01:47:00 | TERRA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d62d8259-55b2-39e4-b7dc-157d0e94646d | -16.07673 | -59.70491 | 2024-11-28 01:47:00 | TERRA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 77786960-fc01-3c47-a801-aaaa786dcf9f | -16.0789 | -60.11561 | 2024-11-28 01:47:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 390be412-167e-317b-b0fe-8dd6b715736f | -3.1045 | -53.81462 | 2024-11-28 01:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 32a1abfb-1087-397e-93cb-48562d9cb32c | -2.84048 | -54.11781 | 2024-11-28 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| cfa6d158-e125-35a8-87e8-0fb48f43c4bf | -9.61429 | -64.68768 | 2024-11-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 43e52fa1-9b7c-329f-9f59-6fc6b8a75010 | -1.16254 | -53.67924 | 2024-11-28 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 312ec52f-e315-3513-8589-579ad7eb3934 | -2.59622 | -53.96372 | 2024-11-28 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 2baeb80d-a7a7-3bd9-bb31-272fd325bb1d | -3.91963 | -53.66601 | 2024-11-28 01:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 95614bbd-1c00-3a3c-9701-fbc34d18db35 | -9.77953 | -64.78027 | 2024-11-28 01:49:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 69d26050-99d3-37a4-be41-3dea70239a1f | -2.7617 | -54.12969 | 2024-11-28 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2bd8c8a0-f226-36ec-bf46-b24472688197 | -2.60405 | -53.96786 | 2024-11-28 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 8760f7c5-4a5a-31f8-81bb-d45b5db70f70 | -3.09635 | -53.82072 | 2024-11-28 01:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 6538f307-915c-35fa-b51a-c7c88f9752b4 | -2.83435 | -54.11345 | 2024-11-28 01:49:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 1ee87fed-2437-3841-8e01-8a9609a26942 | -3.80166 | -52.35789 | 2024-11-28 01:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| cbf53852-2dd5-36a7-9dc0-b0bec672ecbb | -2.58807 | -53.97036 | 2024-11-28 01:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| b91aa16f-1c93-3e6c-92bb-1cbdfb951edf | -1.3329 | -51.9463 | 2024-11-28 01:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a5b3778f-d3b3-3ca8-af61-f9d69f7a59fc | -1.6812 | -52.4946 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| b4e27b89-439a-3f0b-ba88-e78c7082d04e | -2.8794 | -46.862 | 2024-11-28 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 311a6ef2-2f93-3f2f-99e4-6ebc7930a414 | -1.6996 | -52.4943 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| bc875bb7-2e43-3e19-98d2-6405f3babd43 | -3.9562 | -50.1969 | 2024-11-28 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 1bc5818f-b7ea-3588-ac95-69056fb96b25 | -2.7234 | -48.9034 | 2024-11-28 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 209221ff-ac2a-3d04-8de6-20d306d0864c | -1.6629 | -52.4744 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| aa57a4f7-f208-3095-a215-ecb1c83cd9e1 | -5.9788 | -45.3621 | 2024-11-28 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 230.9 |
| 7f150173-4c91-353e-a086-5e6862a3f569 | -2.9909 | -51.4598 | 2024-11-28 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ff63368c-0afe-3544-ad9e-dbca805033c8 | -2.9909 | -51.4391 | 2024-11-28 01:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 5f26fe1c-84d1-3f9f-92b4-fc974e28139f | 1.2537 | -55.9467 | 2024-11-28 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 8b0a04c8-4446-3ce3-85b1-f334eee22c93 | -5.979 | -45.3395 | 2024-11-28 01:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8e5db8b3-b1d1-37b6-ad97-c7bc2b31d4b0 | -1.6812 | -52.4742 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ba65dca1-77fe-3d27-b68d-ea077cabc893 | -1.5897 | -52.271 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 147.9 |
| 77702e09-05b7-3951-92fd-5bd0c68ad539 | -2.3965 | -47.1617 | 2024-11-28 01:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 7b87b25e-0ad1-31da-aa3e-c7ee5f9453e2 | -2.8795 | -46.84 | 2024-11-28 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| c29785ca-2c05-3619-8e27-581d941d2daa | 1.2537 | -55.9664 | 2024-11-28 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| a9c50d67-7039-3192-a0b1-6b1b93696bf8 | -3.3837 | -50.1125 | 2024-11-28 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 65801164-67e0-348b-aa99-da2391d3ee1e | -1.6445 | -52.4543 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 54642f4d-63a6-3220-87e1-2ba5fa8ed5fa | -1.5713 | -52.2713 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| ff5ed12d-8ac6-3b0d-ba99-03852496d64c | -2.5963 | -53.9771 | 2024-11-28 01:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e373bf30-feef-36ae-9edf-5747f5fcb67a | -2.8609 | -46.8626 | 2024-11-28 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| b5fa043d-b76f-35c7-8122-cb3d58aa02a8 | -3.4022 | -50.1119 | 2024-11-28 01:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 94d6e41c-af9f-3ccf-9eae-33bad480b4f5 | -6.0862 | -48.0339 | 2024-11-28 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 71918e82-1a26-30ba-b7a5-24d1451ee10e | -1.6445 | -52.4747 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 96ac7f76-2317-354a-8f10-b05ce570a099 | -3.1113 | -53.8242 | 2024-11-28 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6b4af8f3-a6ad-3d7d-8424-80cbb1ebdc21 | -6.1048 | -48.0327 | 2024-11-28 01:50:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6d924f64-949f-3f74-879e-4ca6cc07298d | -1.5898 | -52.2505 | 2024-11-28 01:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 75402a00-3b4b-3bbe-b5cc-633c5dee773c | 1.2538 | -55.927 | 2024-11-28 01:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9d93e973-8382-3f9d-ab12-39e30d0c3c9c | -6.1735 | -42.6221 | 2024-11-28 01:50:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 50.4 |
| 31229a48-e6da-370a-a4da-c84ee430f0f3 | -3.1114 | -53.8041 | 2024-11-28 01:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b8d6231e-9786-343c-ab9b-4200d120235a | -2.861 | -46.8406 | 2024-11-28 01:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 9ec1883c-493e-3944-b1c9-99a6118b8504 | -2.7419 | -48.9029 | 2024-11-28 01:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| a67a03e3-80b2-30b3-8ba4-ace7894ebc05 | -4.7722 | -44.4205 | 2024-11-28 01:50:00 | GOES-16 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 348a589e-ac41-33f0-83cf-5dc13d640d37 | 1.24858 | -55.95348 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0b14fed2-7903-3071-afa8-6d1966987470 | 1.25227 | -55.92681 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b87e3f10-03e4-3bc8-967e-37a043cbad35 | 1.26319 | -55.95564 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| d45a09b4-4be3-37d6-b801-fb97d66d71f8 | 1.90093 | -55.74609 | 2024-11-28 01:51:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 6806c9ee-bd4f-3f47-86b1-bed344b4c662 | 1.24488 | -55.98025 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ff77a048-8d41-3cee-9d0e-5511ecc4a4f8 | 1.47426 | -55.9756 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 86f0adab-b86e-3d0d-a372-83d9e6fee3b3 | 1.31536 | -60.413 | 2024-11-28 01:51:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 07367405-202a-3622-a107-9571dc83edcc | 1.25948 | -55.98223 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9303275d-06d9-32ff-bdc0-7e9dda59d14a | 1.47378 | -55.96995 | 2024-11-28 01:51:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 67932b63-b350-3157-bfa8-36450df7f9d1 | 1.89931 | -55.75131 | 2024-11-28 01:51:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 39f94021-fad4-355c-a237-9044f24b45ad | -1.6629 | -52.4744 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| d4f7d0d0-a231-3c2f-9be0-384519988ef0 | -5.979 | -45.3395 | 2024-11-28 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 93bd1789-6847-3a1b-8e60-d7314c8fd310 | -1.6812 | -52.4742 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c31ab7d1-d9b0-3378-9877-4d9d0832d3ef | -1.5897 | -52.271 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| bd8301b3-a074-3829-8ec4-b3f17f52d8e6 | -2.7419 | -48.9029 | 2024-11-28 02:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 5cad15e3-48f4-3612-a2ad-a426494f8dd1 | -2.8423 | -46.8632 | 2024-11-28 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7fd629a3-84d6-3e98-bcca-ef6fff905bac | -1.6812 | -52.4946 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 4d401b82-14dd-3652-95aa-118ac6d7607b | -2.8795 | -46.84 | 2024-11-28 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| f1d8ed79-7198-367b-be39-89466fb1d251 | -2.8609 | -46.8626 | 2024-11-28 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 7932448f-2cf3-3c9c-a3f5-faaa95932bf2 | 1.2537 | -55.9467 | 2024-11-28 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f96d9890-6428-3d62-930e-e87877fd479f | 1.2354 | -55.9469 | 2024-11-28 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| de6a1906-0905-301b-9f93-4a57688dc137 | -1.3329 | -51.9463 | 2024-11-28 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 28a13ad3-5abc-3614-bb10-cfeed8f1bda7 | -3.3837 | -50.1125 | 2024-11-28 02:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 30b8c2a3-fd4d-3c5f-8917-f8092e3839ee | -2.8794 | -46.862 | 2024-11-28 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 87436ba3-77e0-3be3-81ca-d4547d75adf7 | -1.5713 | -52.2713 | 2024-11-28 02:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 21c713b0-053d-3528-98cf-6e932d0bcab7 | -5.9788 | -45.3621 | 2024-11-28 02:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 1ee6c541-a329-3f94-924f-c49378983bde | 1.2538 | -55.927 | 2024-11-28 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 2495b636-ba89-3012-a53b-75366e9b2e73 | 1.2355 | -55.9272 | 2024-11-28 02:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 6286f1a7-4a93-37c6-b2c2-d82cd4124cd4 | -3.9674 | -48.0851 | 2024-11-28 02:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 4de3fe5b-7af3-3942-a533-96a844871312 | -1.3145 | -51.9259 | 2024-11-28 02:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 38a680ef-50ff-3966-9ac6-1b03df9eafce | -3.0929 | -53.8247 | 2024-11-28 02:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2dccab27-fb7c-3fae-9cce-dc6ef6bb8872 | -2.9909 | -51.4391 | 2024-11-28 02:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 19ddd0b4-7f66-381f-84d6-af4f0ee660c1 | -2.3965 | -47.1617 | 2024-11-28 02:00:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3f89d806-45a9-337c-9b5e-daae92decb33 | -2.861 | -46.8406 | 2024-11-28 02:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |


[Clique aqui para ver as próximas entradas](README23.md)
