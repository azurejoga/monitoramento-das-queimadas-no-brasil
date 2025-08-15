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
| 6c25e239-5c0b-31aa-9a6a-e24be4dee631 | -10.3432 | -64.436401 | 2025-08-15 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 752b689c-7bd9-372f-9e60-ac77bbc47ec8 | -7.9575 | -61.747501 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e31e56d-8124-3f79-b625-b17db1302476 | -9.4033 | -60.535999 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 07f2b055-48c4-3328-8682-bddb4ae42c26 | -15.6722 | -56.3652 | 2025-08-15 01:10:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0a57c13-d22c-3ce5-a7e6-1c74aefeaa2a | -8.1187 | -61.1861 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 31408df9-6c7e-356c-bbd2-332071582dda | -8.9415 | -62.227699 | 2025-08-15 01:10:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1c24e142-1580-396a-8d54-dfcbb5aca562 | -7.1516 | -60.1152 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b040a77e-8315-3bdd-9c36-e995499c05a4 | -8.2959 | -64.000504 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a6c2386-bfce-3d93-b5ea-7107c6bca563 | -6.6609 | -58.8009 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6c8b6143-5f64-38c8-8822-ebe8022ea7f5 | -9.1787 | -59.695202 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e73dd842-4bf4-36ee-8b33-b932989c7315 | -6.0723 | -59.949501 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a56196fc-1b4a-3905-9202-a450254b0cf3 | -9.2123 | -59.6619 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e98e29c9-b8a2-3ce4-8e13-fc68ffc6218e | -9.1792 | -59.652599 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17157e4f-adf5-313b-960b-d903e86c52fc | -9.2086 | -59.645699 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b98b27b4-7920-32de-8a70-8789bd410ee8 | -6.8764 | -59.1506 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6469bb18-8225-32f7-b90c-4d0ecd149277 | -6.6534 | -59.0779 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4e0abf-61c7-3a92-aeb4-558ee4233c15 | -7.2881 | -60.619099 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0dc83a40-04dd-3a49-920e-89873c2e251c | -13.0635 | -57.1236 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8edb2aa3-5555-3e2a-a78c-72ddc62fed49 | -7.6085 | -63.497299 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5dac437d-b993-3bd1-bbb1-5d9f42478d4f | -11.3612 | -55.436001 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cd51ab58-46a2-36e9-aedf-1aa068f10210 | -6.9429 | -59.525002 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2d3deeb-52e1-356b-8692-e8c32ccaa5c3 | -7.286 | -64.690903 | 2025-08-15 01:10:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7748523-e221-360d-9da4-7e6e7a945322 | -9.9243 | -60.470001 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6d97b27b-d6f8-308f-9daa-7646958540ca | -9.5012 | -60.513401 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b62732f-ac05-333a-b65f-df10d177eb2a | -9.0747 | -60.767399 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fabd1a3-1568-394f-aea1-20d61a4ac1d0 | -10.0535 | -59.108799 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38c1281f-8232-3294-9b13-b2ee245a3d45 | -6.9459 | -59.983501 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 13d23647-a237-3a08-ab48-5f9951619d59 | -13.1314 | -57.148201 | 2025-08-15 01:10:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 06113dba-90ea-322b-8718-58cf4a8c82ce | -6.9478 | -59.991699 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6197f0a4-869f-3571-a841-cfa61becc64b | -10.3284 | -63.6119 | 2025-08-15 01:10:00 | METOP-B | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0ee0297-7cfc-3c2b-916e-106be7b19fcf | -6.0762 | -59.966202 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 922ec03c-8f4d-3d3b-a790-d80a1a9c9d46 | -9.1694 | -59.6549 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98f61925-2b25-399c-a54c-946a6ded1047 | -7.0901 | -60.027401 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0df6c9f7-ca6d-3f72-ba74-727449cfe170 | -9.5144 | -60.526001 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79b2003e-95e7-3428-98b0-ef588821f7be | -9.1615 | -59.665298 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cbb8c08a-5b39-3b87-964d-29f7415c3944 | -6.9489 | -59.817799 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ffea82a-dc08-36f9-8aca-6831d274b9ba | -6.088 | -59.928299 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a918265e-4469-3235-8975-7dc9436b9f4c | -11.3547 | -55.4095 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5168ef09-4fdb-3e45-99dd-3449251f11fc | -8.0545 | -61.5844 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d272a572-18fa-3b20-a99a-fc122d85962b | -6.6991 | -58.831902 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| afb256a7-683f-3013-b4f9-33bf87c59ce7 | -7.9461 | -61.742599 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8712859-1c3a-3ca7-87ef-ba757c2238de | -6.4817 | -62.924301 | 2025-08-15 01:10:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1879703e-f298-3685-9a57-ee48e790c376 | -7.61 | -63.5042 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb140b48-31d4-3402-8448-24340aaa541d | -11.3416 | -55.398701 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e735cff8-0e35-3bf4-b0b6-72edc24b1fa2 | -15.6747 | -56.375301 | 2025-08-15 01:10:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6611e76b-d0c6-3322-bea5-7eab131da0a7 | -9.5063 | -60.535702 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20f7b001-9a4e-33b6-982b-6d3f4601ec23 | -7.6327 | -63.513699 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aee8c947-4084-3857-b8c4-01a4fe3e0e4f | -5.4536 | -60.126598 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 84d73e39-dae0-328f-b613-781ecc23e62f | -8.2975 | -64.007599 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b63b595-5a7f-378e-bc02-848a370289f4 | -7.9249 | -61.740002 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2434d3-5f68-3d2c-ab7a-0632f140243a | -6.7044 | -58.810699 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bfa22eb2-bdbd-36e3-9c44-0b2ed4c08ad0 | -6.7013 | -58.841301 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55f41dc9-8c7f-3188-b547-50d5a48ae16e | -7.5419 | -63.475601 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 195493b0-961a-3cdf-b7e7-783d012ff23b | -7.3389 | -60.615501 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a13f0bae-2c64-3acf-85bb-6df1966eb681 | -7.8886 | -61.8074 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b608be4e-3ad6-37b7-8198-4460872fc1f4 | -11.4072 | -58.5429 | 2025-08-15 01:10:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5511cb00-4462-3c9b-8acb-9c477d39a7dc | -6.6751 | -58.8176 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9372091-87bc-36cc-aa77-36c23621e26e | -7.9379 | -61.7519 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 364f10ac-1bf6-38ba-8fb2-ef3fc8b142b9 | -7.5986 | -63.499401 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97d2c9d5-d27f-3948-a66b-53fc44f5b930 | -5.4574 | -60.143299 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8664539-8ee0-35af-9175-18d0ecab60a6 | -7.8576 | -61.806999 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 29b6891d-22db-3e0a-9e04-af1e37cfa955 | -7.0816 | -59.234901 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 318245e2-7207-3391-b667-69a00ff94672 | -9.1555 | -59.683701 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4af9ad5e-f45a-31fe-acef-40dc60793ce6 | -6.8939 | -59.137001 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 17c5d4ef-3624-390c-8119-9b03fde028ec | -7.1301 | -60.111698 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 400892d4-7703-38bb-a422-0163ae0c4db6 | -9.4016 | -60.528599 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab02ac4b-208b-3c32-9c87-1a9698bf81c1 | -7.6311 | -63.506802 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc33e4c-ff68-3cad-9b1a-bcd86cb54f3c | -6.6533 | -58.812599 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32bc5a2e-bfc5-38cf-976d-3c7e62888db6 | -7.9689 | -61.752201 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70c69441-f29c-3343-90ab-7633770762ba | -9.9044 | -60.4277 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba765dd2-5f17-3893-8fc0-cc9d3ba3e560 | -15.6615 | -49.7509 | 2025-08-15 01:10:00 | METOP-B | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a86d35e5-32a1-30b9-ad0a-526677290304 | -6.1154 | -59.9132 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| acde408d-5af3-3741-a331-aded7eafdea4 | -6.0997 | -59.934399 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9e84af0e-9e19-350e-a369-c6da8bbed1e7 | -9.1574 | -59.6917 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b857230-d538-3ba5-bd26-0f88af3378f7 | -6.6946 | -58.813 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8536bcb9-4fe3-30f4-be30-e8c96ee03c5c | -8.6054 | -62.658699 | 2025-08-15 01:10:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e34d9504-7364-3092-a7b6-89c350832b7d | -6.9037 | -59.134701 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9fe16c41-9fc6-3487-981e-0c39ece582c9 | -7.0656 | -59.210499 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| df91f8a4-4d05-3b5f-ace3-161d9d5c741e | -10.335 | -64.446098 | 2025-08-15 01:10:00 | METOP-B | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d34973ee-6c3f-39da-834d-0f4db5b8cb86 | -6.0606 | -59.943401 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b0937d61-f41f-35b8-8f49-b83454323a69 | -8.1203 | -61.193298 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2c5802c-5ffa-3515-9364-f614eedeeee9 | -9.9456 | -60.4729 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c04884e1-25de-3939-a979-2f63a7c88b0a | -7.0971 | -59.212502 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e3c08bc2-71b4-3fd5-8379-f4dc4bfa4481 | -11.3514 | -55.396198 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 58ce901f-74e0-32de-a9bb-992ef30114ac | -9.9375 | -60.482601 | 2025-08-15 01:10:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1155428b-e417-3ad5-864d-c52a669da81e | -6.0625 | -59.951801 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f796ba6-7218-3dc0-a600-e6c5af6b4101 | -7.2468 | -59.991299 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef2ce9d-da45-3539-88e2-6a25da40de15 | -9.189 | -59.650299 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4eeb3f-b275-329e-938f-fcad7ea69a9f | -11.3449 | -55.411999 | 2025-08-15 01:10:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b45dd960-2c88-34e9-92d7-05ea8828aef5 | -7.9477 | -61.749699 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2782ee59-ff1d-3221-9f53-f779a6f568d7 | -9.1671 | -59.6894 | 2025-08-15 01:10:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9c08396-fb96-3689-a1e5-9387b7b6b25e | -7.9579 | -63.448799 | 2025-08-15 01:10:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d8d19037-aee4-3415-afe8-267f4bcd66b9 | -7.0635 | -59.201599 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 811e24d5-4b33-3368-a746-ead322f1423f | -8.9482 | -62.2117 | 2025-08-15 01:10:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6565817-1152-306b-88b2-87baa2279d62 | -7.8788 | -61.809601 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21d145ca-14da-3bf4-9766-e6b20a1da9c4 | -6.6849 | -58.8153 | 2025-08-15 01:10:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1fb5dff8-c856-3ae6-a285-2e034188ca55 | -7.882 | -61.8237 | 2025-08-15 01:10:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dad71167-f2f3-3ed7-9be1-d73980c549aa | -6.0704 | -59.941101 | 2025-08-15 01:10:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d54ceb86-77e4-378f-aa68-871c9b464aa0 | -6.9391 | -59.820099 | 2025-08-15 01:10:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b02f55ec-382b-341f-8272-0a6b4c3fd932 | -7.6069 | -63.490398 | 2025-08-15 01:10:00 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
