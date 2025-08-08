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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5ec8f2f-177e-3e2e-b0e4-df7164035f3d | -8.5211 | -43.3063 | 2025-08-08 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 7ebb2a88-e8d2-3f9e-a67a-db9154f345f0 | -5.9711 | -44.1542 | 2025-08-08 00:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| dfd4908b-5767-3950-98f0-f229dcfe3f31 | -8.9213 | -60.7489 | 2025-08-08 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 4d53c351-74fe-3ed6-af8b-a52b8a64a5bf | -13.054 | -56.8545 | 2025-08-08 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2a7954ec-f631-3b62-98ef-7273988eda60 | -5.8267 | -59.2256 | 2025-08-08 00:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 62788774-bbe2-330f-8b6a-319667935bfb | -8.9041 | -60.5577 | 2025-08-08 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 91ea3947-b837-3291-8e74-a58c4f3d2bc0 | -8.9213 | -60.7489 | 2025-08-08 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.5 |
| e848acc0-9136-3e8e-8d1c-626647eb55bd | -9.0832 | -45.0728 | 2025-08-08 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| ed72dcec-c517-376c-a5f0-21adee21d884 | -10.6247 | -44.767 | 2025-08-08 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| a57b9071-fb6a-37eb-ad35-95a303aac7fa | -10.625 | -44.7439 | 2025-08-08 00:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| a7471345-b325-354d-a0d7-2d1f48bff7a4 | -9.0642 | -45.0749 | 2025-08-08 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 283e1b1a-71fc-308b-8d9b-2f7ec2a214e6 | -8.9042 | -60.5385 | 2025-08-08 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 78f96028-a42e-3268-9164-d6fed6c350d0 | -8.9215 | -60.7297 | 2025-08-08 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 894349b7-ba14-31d3-9f76-bea9bb6ece41 | -8.5208 | -43.3298 | 2025-08-08 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| 6173e44a-2372-3703-9a68-b5cb6419ee56 | -5.9711 | -44.1542 | 2025-08-08 00:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a8049fe0-6ded-3cab-bb11-b1650a1bb605 | -8.5211 | -43.3063 | 2025-08-08 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 6c341cf9-1281-35ef-8216-56b620acbd9c | -7.8918 | -45.3348 | 2025-08-08 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 13346c6a-c0cc-3ecc-b6a4-5aa8d696b073 | -6.725 | -43.7915 | 2025-08-08 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 1697ddd9-7159-31bc-8655-eb626c55ac45 | -9.0642 | -45.0749 | 2025-08-08 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 2f052f0a-fb2a-3c79-971a-695586c1b01c | -13.035 | -56.8562 | 2025-08-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| c511dae4-6442-3903-8a77-0674dbb48075 | -10.625 | -44.7439 | 2025-08-08 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.8 |
| b40e5af8-cbf5-389e-a254-c84aa964e833 | -13.054 | -56.8545 | 2025-08-08 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 79142c76-70ac-3533-8e8c-3f19cdc331ba | -10.6247 | -44.767 | 2025-08-08 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3ecc6694-12ca-3b11-a31b-5a353fae3a77 | -8.9042 | -60.5385 | 2025-08-08 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f761df63-53ac-31fd-b31c-5d8eec5c3edc | -8.9213 | -60.7489 | 2025-08-08 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 030ea4c1-0f96-3b99-a185-3aeae17a56c5 | -9.0646 | -45.052 | 2025-08-08 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| de78c5b2-19f1-35d6-8178-4114956d5369 | -9.0832 | -45.0728 | 2025-08-08 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4a174163-06fd-34a9-b4f0-0266bd3ac2a1 | -8.5211 | -43.3063 | 2025-08-08 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 9fb6694e-b3cb-38c4-926f-884267c7d733 | -8.9041 | -60.5577 | 2025-08-08 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| cbf2bc52-8398-3345-ae55-d2d66045fdf6 | -22.8083 | -55.5644 | 2025-08-08 00:50:00 | GOES-19 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 67a125c9-6d4e-35df-aa4c-625460b49dea | -7.9106 | -45.3329 | 2025-08-08 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bd30f06e-e97b-3c42-86a7-c0060eb4b03d | -8.9215 | -60.7297 | 2025-08-08 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5f030d64-d95e-3b79-a3b7-c5d073f39f83 | -22.8078 | -55.5862 | 2025-08-08 00:50:00 | GOES-19 | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | 154.3 |
| ad3067a0-d388-3627-a046-d1f4ea7e1b5b | -7.4074 | -60.0108 | 2025-08-08 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| b842f27e-a50e-384c-aa7e-ae62229daab6 | -7.8915 | -45.3575 | 2025-08-08 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| cb27486d-98fc-3dfc-bd4c-6902760d1837 | -9.0835 | -45.0499 | 2025-08-08 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 65fdb310-db9e-38ee-9d3d-f32e4e5fa4cb | -9.0832 | -45.0728 | 2025-08-08 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 923cc6cd-a708-308e-b0ad-0d66db557cfc | -8.5211 | -43.3063 | 2025-08-08 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c183d012-9a67-3a34-84cf-476a109eb055 | -9.0646 | -45.052 | 2025-08-08 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 4f0a1eca-9faa-3f90-b564-2a97471eeb2a | -8.9215 | -60.7297 | 2025-08-08 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 30a9c5f1-201a-359e-bdd6-a78491a4ad8a | -13.054 | -56.8545 | 2025-08-08 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c34147ce-8b4f-323a-bb7a-009529184e4b | -7.8918 | -45.3348 | 2025-08-08 01:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| e82c9147-4270-3eff-9761-7cc3718164fc | -8.9213 | -60.7489 | 2025-08-08 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 0a9d10bf-6486-3064-87c0-852a877f832e | -5.8083 | -59.2262 | 2025-08-08 01:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b8073fad-35a3-3861-b248-cd1d4c347e01 | -9.0642 | -45.0749 | 2025-08-08 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| bfabca6d-ea90-35e5-b096-ad7e645aff18 | -13.0362 | -44.086102 | 2025-08-08 01:04:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c19dccb9-7719-391c-88be-1d8389566249 | -7.0678 | -55.4091 | 2025-08-08 01:04:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e2971f7f-db41-3f25-8d44-8b4dfea32c3b | -8.9216 | -60.7425 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4ef4fef-b70b-331f-a12a-08d6318b234b | -5.812 | -59.223202 | 2025-08-08 01:04:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc355ea-4c72-39da-8428-9e5c91afb2be | -9.0633 | -45.043701 | 2025-08-08 01:04:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ba801567-ee07-3cb2-b6ad-fb63f1c74453 | -9.7047 | -61.276798 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6838be52-290a-374f-977c-dc402224ded3 | -21.3915 | -48.678799 | 2025-08-08 01:04:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a242cecd-5292-3af3-a6a4-748ecbb35257 | -9.0633 | -45.084099 | 2025-08-08 01:04:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 72338303-e097-39f4-a537-a5f0706a9965 | -9.4793 | -57.846802 | 2025-08-08 01:04:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be14480d-5648-3963-9fcc-ea0d28b363d9 | -7.0425 | -59.1777 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d24ef087-41a6-318f-8b3c-65e642ea9542 | -9.4773 | -57.837601 | 2025-08-08 01:04:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 953df0af-81a2-3237-bea1-145842f91aa8 | -7.0523 | -59.175598 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 091dec70-5a35-3360-b8c1-c1de1d700d85 | -5.8218 | -59.221001 | 2025-08-08 01:04:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 845482cb-7094-37ef-8ea4-204ba7e491ad | -8.9314 | -60.740501 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e6a03d9f-b96d-3c1f-b223-2925bcda0714 | -13.8962 | -51.835602 | 2025-08-08 01:04:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4e79201-a9ad-304e-a44f-947dd0ae3f66 | -7.884 | -45.345798 | 2025-08-08 01:04:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e23a3dab-b11f-3199-997d-8e044101090f | -7.0577 | -59.153198 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7891e92f-1eba-30e7-aa94-e93a1208a94e | -8.9111 | -60.547298 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd5afb4d-3668-309a-8bc7-76fe36ed157b | -23.372101 | -47.329498 | 2025-08-08 01:04:00 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e589b5bd-1442-35b2-8240-3aae13ddca58 | -8.516 | -43.286301 | 2025-08-08 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0472d44c-d6e4-398d-8092-c790b79f9109 | -5.9708 | -44.1563 | 2025-08-08 01:04:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a78492c3-3d17-3bec-907d-6137f52ee7f1 | -10.8252 | -49.379299 | 2025-08-08 01:04:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49049c95-7bdb-3e54-ae36-dbea65487795 | -9.7204 | -62.391102 | 2025-08-08 01:04:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b3f2c5e7-c1f9-3e40-867d-0cd9baa00937 | -5.8846 | -57.747799 | 2025-08-08 01:04:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 450c2412-a951-39ba-bff9-c90534e1474a | -10.0905 | -51.635399 | 2025-08-08 01:04:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e01838f-6f80-3265-9994-5c07989dab68 | -7.0795 | -59.1591 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34f4dcea-8d6f-35d8-a5f3-b6017e35ddc5 | -8.5227 | -43.311901 | 2025-08-08 01:04:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a664c00e-0ccb-3891-9921-15ea17a87aae | -7.0479 | -59.1553 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a631d2a4-cb6d-3472-bf60-f57206a551b8 | -13.0463 | -56.851002 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3bba669-e392-3094-a33f-d16f4fc75385 | -9.7176 | -61.290199 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a354dd9-2546-3321-b1e9-ffaff0aaf2e9 | -7.4023 | -59.984402 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84a3fa58-9eb2-3294-a767-32e92a8c7798 | -8.9256 | -60.7131 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| da0732a9-4043-35a7-98c4-d9a4c73d7a6a | -7.0599 | -59.1633 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f2e90cdb-da41-3a5b-9f00-f26f6581eaf6 | -11.7414 | -47.506302 | 2025-08-08 01:04:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 53b8b2ea-a667-38d2-93d9-d426b9bd8d29 | -14.3555 | -51.097401 | 2025-08-08 01:04:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 97ed0915-6c40-3fb1-9e53-01b09d2e7fcc | -12.5741 | -47.153 | 2025-08-08 01:04:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3cde28cc-ecb0-301e-94a1-417833fbf407 | -9.9294 | -60.4482 | 2025-08-08 01:04:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a5925725-a822-3064-9560-6506900a041c | -7.0448 | -59.187901 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aed06bc3-b4fd-3ab9-950d-51a10798f6e4 | -11.7511 | -47.503799 | 2025-08-08 01:04:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 131b1986-6646-3679-842e-9a21832a1025 | -8.0644 | -49.715099 | 2025-08-08 01:04:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87052933-9d59-30b0-8e10-3e1847996700 | -8.9245 | -60.756302 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 978fd782-4cb3-3de5-b467-e2096e80e967 | -13.0385 | -56.862202 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5ac2d32-e9cd-3e91-aeca-86839dd447f3 | -8.9083 | -60.534 | 2025-08-08 01:04:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 981f6293-fae1-304b-8e59-d1fc82cd736c | -22.811199 | -55.589001 | 2025-08-08 01:04:00 | METOP-C | ARAL MOREIRA | MATO GROSSO DO SUL | Brasil | 5001243 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 514fa66e-a674-3088-956a-85acc0225cff | -11.4547 | -47.310699 | 2025-08-08 01:04:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46ae87c2-0d9d-3b31-9fb2-a0bde7cbfa65 | -11.7989 | -44.927299 | 2025-08-08 01:04:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d416461-38f5-30aa-8bdd-067f8f613875 | -9.0682 | -45.062698 | 2025-08-08 01:04:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dd9f9c8e-b9e0-31a8-94f8-1d6f8b3deab6 | -7.0501 | -59.165401 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e19b2016-0cc4-3da5-a779-cf44c7d7c620 | -7.0568 | -59.1959 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35108121-098a-3490-b7b7-616a41b90b6e | -7.0675 | -59.1511 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12bd02b7-e5bd-39c1-aeae-0aa4bad3b2a2 | -7.0403 | -59.1675 | 2025-08-08 01:04:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ef3a425-9531-3f77-b963-f5c3bbe9fbc7 | -9.9379 | -60.489101 | 2025-08-08 01:04:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03b4d929-7e01-35ca-8d37-5227ac7dd714 | -13.0365 | -56.8531 | 2025-08-08 01:04:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb9ef33-e973-3420-b64d-ed35379dae06 | -11.0268 | -45.057499 | 2025-08-08 01:04:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 80e7d5dd-0282-36fd-b280-a98c6321ad95 | -23.374201 | -47.3382 | 2025-08-08 01:04:00 | METOP-C | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README4.md)
