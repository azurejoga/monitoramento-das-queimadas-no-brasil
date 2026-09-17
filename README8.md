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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f60a431d-1d4f-38b6-a98d-ddf873a8ada4 | -9.09973 | -61.03597 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 56e5de96-af57-3eae-a7ca-33ca4acbda54 | -8.92021 | -62.40796 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5839c5c6-9634-3d72-a8a4-77cad5a5557a | -6.80826 | -59.18492 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| da137860-fc69-306a-b6b4-712aae6cd2a8 | -9.17252 | -66.05198 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e65d1ace-f55e-38d6-819a-bf6fe8ebeab6 | -6.85054 | -62.9008 | 2026-09-17 01:02:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bfb65ff0-fc98-3aec-99f2-1c22facb0a86 | -9.29196 | -60.53591 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 88e0a3bb-be42-3e81-9e76-664461c56ca6 | -9.0359 | -65.92783 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4bab600-f6e2-3e54-b266-db5d0ca98d4a | -9.17121 | -66.04216 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| df6cb669-5448-3b8b-bfdc-520e7e906986 | -6.90935 | -59.03733 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 4d61e5c2-a62e-38be-b0b6-457838e62135 | -9.09475 | -61.00206 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 0340dbfa-1bbb-3037-86fe-bcf4c244b899 | -9.06213 | -65.91434 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4e50e8b8-52f2-34b0-95e6-ab081bc64865 | -9.47915 | -65.66053 | 2026-09-17 01:02:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6ea12c03-e5a6-3d95-9f12-b8fd7d02b25b | -9.09308 | -60.99073 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f96fd84d-e0de-30f5-8be0-26486c26cc27 | -8.76034 | -66.5573 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2e45b2a8-2a7f-3970-8855-ebd88ff3167f | -8.00318 | -61.37777 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 58b4a269-5c3d-3080-884a-004802aa463f | -8.76169 | -66.56757 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6ac6251d-cafc-3610-b1b6-1ee7a123dbda | -6.79649 | -59.18671 | 2026-09-17 01:02:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 92f3c4fc-41dc-30d2-adc4-86942dfd165a | -8.22561 | -61.4999 | 2026-09-17 01:02:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38ce1031-7271-3ea8-841c-6095dc1fc6b1 | -6.43718 | -60.01386 | 2026-09-17 01:02:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a2c221d7-c0e2-33a8-a98a-43e7516c7bd5 | -9.10129 | -60.9779 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 4b287c10-2c69-362a-83fe-db6aaeffe6de | -8.65456 | -66.59888 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a52a69bc-9871-3126-86a5-b63d399c136c | -8.15606 | -64.05945 | 2026-09-17 01:02:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 881803d7-1a28-3cef-940e-8bb2068ffe73 | -9.075 | -61.00501 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 16693a0d-528b-3dbb-a3ce-3b4c32177576 | -9.27583 | -60.62988 | 2026-09-17 01:02:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| c811117f-7421-34c8-afae-0946296d6529 | -8.87709 | -66.67259 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d2b21b7f-a27a-3652-9873-59c2d52b1ff8 | -9.40485 | -62.70238 | 2026-09-17 01:02:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b870e7fc-8cf3-3df2-a9eb-00ee8ccd760c | -1.61758 | -55.57599 | 2026-09-17 01:02:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 4229074c-a746-387f-990e-23433da61c17 | -9.10305 | -65.95219 | 2026-09-17 01:02:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 599d17c3-715f-3f14-8db3-31259ecdbcb0 | -10.8343 | -54.0933 | 2026-09-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 56c5d70a-25fc-3079-8dd1-167ac091d231 | -5.1624 | -55.9338 | 2026-09-17 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| a1eefa3b-df4d-3124-9e9f-8db36ed1bc15 | -6.9147 | -59.0295 | 2026-09-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 0c8a4a36-2a5f-3427-8a56-1f2e4ea45043 | -10.7223 | -54.0008 | 2026-09-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 770c579d-a86d-38d2-bba3-1b1630eae775 | -8.4621 | -44.9122 | 2026-09-17 01:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 71b1841d-50f3-39dd-abe6-89dda4d0d73b | -6.3657 | -58.2771 | 2026-09-17 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 4dbcf570-b7d1-34a5-9f2b-9004274f67b5 | -4.5045 | -54.9646 | 2026-09-17 01:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 0102669e-44c7-3294-9b4a-2d85dd7d1565 | -6.9309 | -63.0301 | 2026-09-17 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 442350a7-20e9-3c72-ac94-05fc0a26ae8c | -9.2753 | -60.6355 | 2026-09-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| be81c918-de84-341e-8c06-ff51fd201a94 | -8.4982 | -57.6468 | 2026-09-17 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| ee03859e-ccc0-339f-bd92-9f0b99579b4c | -9.112 | -45.7294 | 2026-09-17 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ed41bb6f-5466-37a5-8a19-cb22a91f8a94 | -10.834 | -54.1138 | 2026-09-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 190.4 |
| a9b568ca-d8a5-326a-8cca-dda5171a97ad | -2.6965 | -57.6278 | 2026-09-17 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c39980d9-16d1-3ded-b997-641b54992032 | -5.7754 | -45.1053 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 453.0 |
| 47b79b41-7177-3986-9b3d-7ced0a05015c | -2.908 | -54.171 | 2026-09-17 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 05d9d815-1154-35dc-ba32-39c8583744e7 | -8.7604 | -66.5623 | 2026-09-17 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| edf08791-4499-3f0b-a73f-c9823e212aa7 | -6.713 | -58.8058 | 2026-09-17 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 279446c3-c8d7-3bf2-bbe4-62600295d4dd | -5.4589 | -44.9687 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0750b811-6d6f-3163-a03f-796c1047eaf3 | -2.9581 | -50.3359 | 2026-09-17 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 0b8228d9-b2d5-3ae7-98ac-bcf1acb1763e | -5.7567 | -45.1067 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 170.9 |
| 804d263e-a08f-3ec6-8fe5-860679e6ff42 | -5.144 | -55.9345 | 2026-09-17 01:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 34be0385-ae13-3470-86e4-b85fb571dc65 | -5.647 | -44.8192 | 2026-09-17 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 4c42fb57-a857-39a6-ab87-791fc698026f | -4.54 | -42.9535 | 2026-09-17 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2d175f78-322f-350d-9962-d57c637f3add | -3.4757 | -54.6972 | 2026-09-17 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 278f2dfe-5205-37fe-9c5b-f1251821656e | -13.3949 | -57.0242 | 2026-09-17 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 758502d1-52fc-3ce2-a508-02856bbc4172 | -8.5168 | -57.6457 | 2026-09-17 01:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 0c79746b-0209-32a7-b096-218d706b3051 | -8.4796 | -57.6478 | 2026-09-17 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 88784350-efd4-352e-8aa4-db25e879123b | -9.4102 | -62.7113 | 2026-09-17 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 3bcade15-89c6-344f-9a59-fc4276c44d23 | -3.4757 | -54.7171 | 2026-09-17 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 168.6 |
| 10098947-d019-3e0d-81cd-460e5f0f512d | -5.7752 | -45.128 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| bb9ac8fd-6e30-3d64-98bf-64c90285d988 | -2.9582 | -50.3149 | 2026-09-17 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| f9a26b57-4ab3-3cc2-82c8-fdadc7c84cce | -10.8532 | -54.0916 | 2026-09-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 0a9593af-fe4c-3067-a95b-936732121e63 | -5.7756 | -45.0826 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 264ca39e-0e22-3347-970b-720a6e2c5f9e | -6.3656 | -58.2966 | 2026-09-17 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 271555dd-c8a3-30aa-a756-3ed33cc18a4b | -2.6966 | -57.6084 | 2026-09-17 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 5ae232fc-ae23-34c4-a403-a4dcc1f50cf2 | -9.1057 | -60.9511 | 2026-09-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.6 |
| a3684d1f-cae1-3c78-837e-049c4a819a9e | -9.1056 | -60.9703 | 2026-09-17 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 1b08fac1-07de-38ed-bb61-10b63d769075 | -5.6472 | -44.7964 | 2026-09-17 01:10:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| eac6ff81-36e6-3fc3-b28e-535d0342452d | -4.5589 | -42.9289 | 2026-09-17 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 573282a2-4c8f-3687-b01b-97da520feebf | -3.494 | -54.7166 | 2026-09-17 01:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 430814f1-3c9e-36fc-a475-b98b25bb5736 | -8.4797 | -57.6282 | 2026-09-17 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 65fabe99-132d-3de8-8a54-5a160c30304b | -5.4591 | -44.9459 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 6d111974-b695-31fd-a6b0-ad658ae6eefc | -6.8962 | -59.0303 | 2026-09-17 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a7bc568f-b96e-3e96-b989-69cb6214abb2 | -9.131 | -45.7273 | 2026-09-17 01:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 357db91a-ec6e-3b3e-9ed2-2c0c5f0eb01e | -8.4983 | -57.6271 | 2026-09-17 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 5a591740-cf8e-3eff-9517-aea1e6fa31f7 | -10.8529 | -54.1121 | 2026-09-17 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| b69736df-40cf-3a9d-9957-623e2db3d77d | -4.5587 | -42.9523 | 2026-09-17 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 08ef1b56-f285-3dfc-8320-b5c6bff6ddef | -13.3758 | -57.026 | 2026-09-17 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 674d9803-bbaf-3c5a-81dc-396529526b12 | -5.7565 | -45.1293 | 2026-09-17 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 9014fd8f-2139-3877-8268-b365f571a41f | -5.76 | -45.09 | 2026-09-17 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 292ff11d-8f9c-3ec6-8abd-47b34e585e57 | -5.79 | -45.1 | 2026-09-17 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ee19fd7-19e4-3e9d-92b5-b9029cbea90a | -2.6966 | -57.6084 | 2026-09-17 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1af5d6c9-e98f-3fe9-8cf1-2be736b16527 | -9.112 | -45.7294 | 2026-09-17 01:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1ac2fe40-742d-3296-871f-0051abfeade7 | -5.7752 | -45.128 | 2026-09-17 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| f27abc2c-ab23-3d26-b88c-508e848f0ef2 | -10.834 | -54.1138 | 2026-09-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 035e6a8d-76ee-39a9-b83c-1f1b26188ccb | -5.6472 | -44.7964 | 2026-09-17 01:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| d0d47c09-dc01-3f44-a849-b247668e5e17 | -9.1056 | -60.9703 | 2026-09-17 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| ce30e41c-4773-3da6-9bb1-ae46744e7958 | -5.7567 | -45.1067 | 2026-09-17 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| a252fb09-a502-37f5-9110-81c33fb9c3da | -10.8154 | -54.0949 | 2026-09-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| aa3758a6-4c6c-33c1-a361-421046d5262d | -10.8532 | -54.0916 | 2026-09-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 9ac4c88f-8a9e-36ac-a6df-2e6ef7d7978a | -6.9147 | -59.0295 | 2026-09-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 0eba6455-d03f-3b6e-bdff-e6cacc686df8 | -3.4941 | -54.6967 | 2026-09-17 01:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| b1c2e319-4489-34e9-80d2-66aaf109fd33 | -6.8031 | -59.1886 | 2026-09-17 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 0d9e1b8f-1b27-3170-8bdd-b993d84b9a0a | -7.1384 | -42.1529 | 2026-09-17 01:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 9d7058a1-cd74-3acc-9ec9-78b75cfa6c34 | -8.7604 | -66.5623 | 2026-09-17 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| e00a2831-01ed-30de-a424-abdf8a568fe5 | -5.7941 | -45.104 | 2026-09-17 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 079db004-17b8-3714-b3f0-88e82ff4c068 | -4.5045 | -54.9646 | 2026-09-17 01:20:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e5c6264c-6ff7-3857-8096-7e7b2e57edf0 | -2.908 | -54.171 | 2026-09-17 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b325cfba-db40-3c9e-9e61-bb37e31edb63 | -10.8343 | -54.0933 | 2026-09-17 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 0b1b3438-4415-3164-8e8c-e1425a633730 | -6.3656 | -58.2966 | 2026-09-17 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| f70f7e17-cb5f-33ee-a553-5382a96fe57b | -7.1381 | -42.1768 | 2026-09-17 01:20:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| 23a4d4ea-4021-3e5d-95a4-e69798b9f0d9 | -5.7756 | -45.0826 | 2026-09-17 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |


[Clique aqui para ver as próximas entradas](README9.md)
