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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69291b17-fd1b-38e6-9999-6b18a17c43bf | -6.7391 | -59.201099 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8179eb48-e409-3644-941b-56f64d20b042 | -8.9941 | -61.017502 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 69065bed-a4f4-32ea-b11d-40521f060e22 | -6.9917 | -63.0662 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82e231c1-3bd8-3296-9e50-e5bebb8b7bd5 | -9.035 | -60.969898 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48674188-b46a-3110-a47c-be210a03aa1d | -6.7261 | -59.189499 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9100627-41e5-31eb-95b5-f450066a0dab | -1.0782 | -54.188301 | 2026-09-17 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25c09986-ff7b-35eb-8adb-5346dd9616f0 | -6.6402 | -58.8158 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6230c0d-16ab-313b-aa54-63cefe08dff6 | -6.7723 | -62.910599 | 2026-09-17 01:22:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f740495f-9a40-34a8-afa5-a287b39e09a6 | -10.3141 | -58.327599 | 2026-09-17 01:22:00 | METOP-C | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b970a535-5eaf-3f04-b6c2-aa2ecd6f5a51 | -2.6278 | -57.6152 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 209ecddb-9540-37fa-a854-9a48d4baf3f5 | -12.2576 | -47.985001 | 2026-09-17 01:22:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5ede3c04-c66e-3f6b-b328-bc0ad35b0e16 | -10.8206 | -54.038601 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2efa9a7-1717-36c9-85bd-489349afe422 | -6.8349 | -59.034302 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc664b1-d80a-3023-bb77-73feff0c8a09 | -8.8076 | -62.406601 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e5e83c80-4101-3e64-b19d-4b4b20861967 | -2.6198 | -57.6255 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ff1763d-135b-3f67-a3d4-e82d3f9429ac | -9.8178 | -48.4179 | 2026-09-17 01:22:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f4ed99c-a86a-34ee-8043-51e96f91ab52 | -9.8274 | -48.415401 | 2026-09-17 01:22:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2219b845-382c-37a2-8840-f90fed32fdca | -6.296 | -58.308102 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1e8263a-85fe-311d-bbc9-03447539590f | -4.4223 | -55.505001 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d256169-4b7f-33ef-939c-f4abb47d97c9 | -5.0768 | -55.9627 | 2026-09-17 01:22:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 880bde11-40f3-3bea-bd99-753b26e1134f | -3.7423 | -58.909901 | 2026-09-17 01:22:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16cf91e5-a4d2-3184-b138-78896b0c8a28 | -1.5374 | -55.5844 | 2026-09-17 01:22:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a055f9d-888a-33aa-8285-b0c385028682 | -12.0471 | -57.2029 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9eb713b1-5509-3f9b-8806-5d62b75ca196 | -8.0232 | -61.8316 | 2026-09-17 01:22:00 | METOP-C | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ef0a861d-380f-3e8a-bc11-11f33be42290 | -8.4247 | -57.652199 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 091af4dd-166e-3a2f-b0ad-799d80e674f3 | -6.825 | -59.036499 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 791ac7d4-ce0f-392c-b2e4-0c13932bafd5 | -12.248 | -47.987701 | 2026-09-17 01:22:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 351d3f19-5954-3f3b-ac50-87d1d8d51d6e | -8.4183 | -57.668999 | 2026-09-17 01:22:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c08d1328-d861-3d65-9c78-09a26b727da3 | -6.8298 | -59.057201 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2159c449-40b9-329e-a198-de5dfce1b5f3 | -16.2383 | -58.3717 | 2026-09-17 01:22:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b0e32da-23a9-3ced-9a40-5c99b318199f | -4.4333 | -54.986198 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f49e5311-500c-3d35-ae41-2ef666ddcc1e | -6.8282 | -59.050301 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f5e38d27-16fc-342f-91ff-d0d301610f6d | -10.6523 | -54.026402 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b78ca129-6889-3072-bbce-47848ea3bcd2 | -6.73 | -58.802799 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7627fdaa-5a7c-37e3-8c48-ae8e88cb6d2b | -6.7457 | -59.185101 | 2026-09-17 01:22:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb52c91e-999c-319b-b03b-b540c5127225 | -2.3995 | -54.698601 | 2026-09-17 01:22:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1252874a-7960-3490-a067-ecd8204839c8 | -4.4247 | -55.515099 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 235f476e-8e50-397a-b6cc-3826b95f53fb | -10.7697 | -46.152901 | 2026-09-17 01:22:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30f13d43-a83c-36f4-8a3f-76538c18cf38 | -12.0373 | -57.2052 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bcdc2881-4720-3a01-9cc6-46ae09f00bc5 | -4.4359 | -54.997002 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f94cee01-9c32-3fb7-9798-60c7d7f9585c | -1.0847 | -54.172401 | 2026-09-17 01:22:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 068f2340-4174-3e05-806c-766b7a8ace56 | -14.4901 | -46.633202 | 2026-09-17 01:22:00 | METOP-C | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f993c32c-e592-3874-a529-f69cc61bc90e | -2.6824 | -57.628399 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f402e96c-b3b1-365b-8545-b6f1e198ea9c | -11.7401 | -58.203999 | 2026-09-17 01:22:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2fd5ab8e-46e6-3d83-a9c2-c0c1670e9d4d | -16.2269 | -58.366699 | 2026-09-17 01:22:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11d9c9a3-7f58-3c29-8c23-df31b7eea378 | -13.5929 | -60.573601 | 2026-09-17 01:22:00 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19bcb7c8-9068-3891-a87b-4b59a8c760e7 | -9.3421 | -60.363098 | 2026-09-17 01:22:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afe35ce9-88cc-301f-a7ba-7e2f9ed79ce2 | -4.3141 | -55.048 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f316d044-8af2-34c9-a9dd-1564cae9d370 | -10.7671 | -54.115799 | 2026-09-17 01:22:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5347256-2973-3c0f-95de-a51bdecce5d5 | -2.6843 | -57.636501 | 2026-09-17 01:22:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43c44c37-1767-36b9-b12f-7725b040009a | -9.3282 | -62.723099 | 2026-09-17 01:22:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1988ac10-d584-3f65-948a-229cc3e83a09 | -9.2169 | -60.631802 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45cab9d8-db86-3273-b1ff-ce3668b939d2 | -13.312 | -57.0481 | 2026-09-17 01:22:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee345057-a87f-3c3d-bfda-dcc6a79b8b45 | -4.4457 | -54.994701 | 2026-09-17 01:22:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8d0426c-c1fa-3128-8667-dd653b49b0d8 | -6.2943 | -58.3009 | 2026-09-17 01:22:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5447a41e-a1d2-3384-8c4b-85e36d3d49da | -9.2054 | -60.626701 | 2026-09-17 01:22:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85bc5166-cc1f-39c2-a673-71687dbb5c28 | -8.4982 | -57.6468 | 2026-09-17 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 307.3 |
| 09dc9798-a8ff-3e8d-b0d5-492a9b3c104b | -9.8694 | -48.3814 | 2026-09-17 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| e73a5d9d-bb3e-301d-8160-ef95d4b7ceae | -6.3656 | -58.2966 | 2026-09-17 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| daeb220b-d651-3d2b-bbc7-3c947c30ca14 | -8.4983 | -57.6271 | 2026-09-17 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 187.9 |
| 72b3874f-c92b-3965-b343-daebfe3bbcad | -10.8312 | -46.1342 | 2026-09-17 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 7430c679-2698-32bb-8a23-4d1bfd45a078 | -13.3758 | -57.026 | 2026-09-17 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| a94b48a4-42b5-31af-a9ef-0c95a90d2b36 | -7.1381 | -42.1768 | 2026-09-17 01:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| 28f28926-00fe-37f6-a196-018f432330c8 | -12.4728 | -50.7639 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4986be40-577a-3b9f-a3f9-35416296e160 | -12.4722 | -50.8068 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| fee27ca6-830c-3726-b5e0-bc07f305a84d | -8.4797 | -57.6282 | 2026-09-17 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 81697413-a01a-3285-9029-11bab5ae7f2a | -5.7756 | -45.0826 | 2026-09-17 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| f3787354-2b18-3ade-8bc6-39eddceafbe5 | -7.8221 | -44.8632 | 2026-09-17 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b7b9afb2-0e69-3b42-9c2d-b55608f33acb | -8.498 | -57.6664 | 2026-09-17 01:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 901ee4e0-8e11-3e59-b709-3f929240ba1c | -5.7754 | -45.1053 | 2026-09-17 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 441.0 |
| bdd78529-8d62-37f4-9e1f-e11b56cd2f45 | -4.5045 | -54.9646 | 2026-09-17 01:30:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 438b16c7-d352-3592-b87b-4d15dd76ffdc | -5.6472 | -44.7964 | 2026-09-17 01:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 3aa203a5-3e94-3258-b378-4ef6bc20873d | -7.8033 | -44.8651 | 2026-09-17 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| bef7c6ce-30f9-32dd-b4b6-4e47f76a2c7d | -12.5097 | -50.845 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 42b25fdf-3602-33ea-9656-499c139f8a9e | -2.6966 | -57.6084 | 2026-09-17 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 8d47c8df-4114-3995-94e3-a99fad184b58 | -12.4725 | -50.7853 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 7f4d88f3-3de2-3b7d-992a-17a1d7cd7785 | -10.8532 | -54.0916 | 2026-09-17 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 232d14eb-e856-30dd-b842-b27c9af09bfb | -4.5587 | -42.9523 | 2026-09-17 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| d639efae-d4b6-3600-9b99-b4dc55c31dc2 | -9.4102 | -62.7113 | 2026-09-17 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 69.7 |
| dfc7fe0f-4605-3b55-9ba6-329ce16e5ab1 | -12.4916 | -50.783 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 84bee4c3-294f-305c-b876-00e4806dd0e3 | -12.492 | -50.7616 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 42a12887-ebe6-3ed2-903a-4d1e07fbcdf3 | -6.8216 | -59.1686 | 2026-09-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b6c072f9-691e-3667-baae-19c49e2a3cc3 | -8.4796 | -57.6478 | 2026-09-17 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 174.5 |
| 5c2b0940-32ad-32b5-a1f1-d01c1169ced7 | -9.112 | -45.7294 | 2026-09-17 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 2a440b8a-7c8e-3a84-9886-d941d1b6c069 | -5.7752 | -45.128 | 2026-09-17 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 2707e8d8-dd73-301a-a222-a6b0fd61c6a9 | -7.8036 | -44.8422 | 2026-09-17 01:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a3551fd2-2787-32ff-b86a-d6e6589d6ce3 | -6.8215 | -59.1879 | 2026-09-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 2c0399ee-9950-3be6-bf16-08d814d35e5f | -12.4913 | -50.8045 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 56043475-8c91-37e2-925b-fbc714d90183 | -12.5121 | -50.6949 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 5a9a78f9-0f0d-3d53-bec8-e81791520d0a | -7.1384 | -42.1529 | 2026-09-17 01:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 7d362638-b265-3a85-9e1f-31ab0dd9da0a | -3.4757 | -54.7171 | 2026-09-17 01:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 156.3 |
| cff4fc92-2d79-3856-a692-3c91e6dc2d7d | -3.494 | -54.7166 | 2026-09-17 01:30:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 718da5a7-fa7f-30d4-a2e3-dadd30588036 | -12.5312 | -50.6926 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| dc5b5bfc-0e21-3511-b8c7-4b11ab0c89ed | -6.8031 | -59.1886 | 2026-09-17 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f5653f3b-e98c-3ebb-b60f-2a6e75764b96 | -12.5309 | -50.714 | 2026-09-17 01:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 9719efc3-b944-3187-ac75-6398001844a6 | -4.5589 | -42.9289 | 2026-09-17 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e779ae42-ede5-3a0f-89a6-acc72714c787 | -5.144 | -55.9345 | 2026-09-17 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 62eccb0e-90f2-3aca-9e10-ac74a47cf216 | -9.1056 | -60.9703 | 2026-09-17 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 68d04ee8-a4fe-3a66-a8e4-9fa0e584ec43 | -9.8884 | -48.3794 | 2026-09-17 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 314ccd0d-deeb-3ef8-8835-f31a73f28886 | -2.6965 | -57.6278 | 2026-09-17 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |


[Clique aqui para ver as próximas entradas](README12.md)
