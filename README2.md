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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0298036-c2b0-3e32-acdc-dfdb42a50b9d | -11.4859 | -65.1198 | 2024-10-18 00:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 56533aef-ab9d-38f8-baae-36f0cb60f70c | -12.4958 | -63.3024 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| ce301022-06f6-3714-8151-823b5cdc5953 | -12.4964 | -63.2258 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b84a34cd-1da9-36d3-840c-43a4cc094434 | -12.4966 | -63.2066 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 01331ab2-060f-39a1-abc2-446c20a1fad1 | -12.5146 | -63.3205 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| c7c87d18-e6d6-376d-b3f5-59f0f51cba3b | -12.5147 | -63.3014 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 109.0 |
| ee057dfc-a0a9-38f1-9735-61953ead2088 | -12.5149 | -63.2822 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| da605100-7c63-3bfc-be02-49a966b0cfda | -12.5155 | -63.2055 | 2024-10-18 00:16:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cc6b62e7-fe20-3841-8ffb-8f0f2f50e165 | -12.5336 | -63.3003 | 2024-10-18 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 81b0c4a9-0228-369e-a206-39915040a437 | -12.5338 | -63.2812 | 2024-10-18 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5a12ef7f-f751-362a-ab7d-73c41dbae64d | -17.189 | -45.4644 | 2024-10-18 00:16:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 65.5 |
| bc1721b2-833d-3a4f-8201-d6632b3f1210 | -17.0191 | -57.4768 | 2024-10-18 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 70.3 |
| b8112942-1723-37d3-8c44-c6ddbb4d8846 | -17.2177 | -57.3102 | 2024-10-18 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 120.0 |
| e777ef7b-8aef-3b85-8bcf-6e4fdba80be1 | -17.237 | -57.3284 | 2024-10-18 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 73.7 |
| 187fa733-0cf8-34ca-8589-f6a2f5810d50 | -17.2373 | -57.3079 | 2024-10-18 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 178.5 |
| def77d85-a611-3759-86ab-3dd0c6b5dc01 | -17.2376 | -57.2873 | 2024-10-18 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| e518d430-0796-3073-923c-bde44bf8d6c4 | -17.7851 | -57.4679 | 2024-10-18 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 87.1 |
| 9d6e5ab2-4c9b-3f08-aa1f-a531b6bec3d0 | -17.7855 | -57.4473 | 2024-10-18 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.7 |
| b08fab25-9329-3214-bbf1-21a991796299 | -17.8049 | -57.4655 | 2024-10-18 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 4a03c159-83bc-333c-baa1-620b3cb927bf | -17.8052 | -57.4449 | 2024-10-18 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 8ae53cf2-d798-3a10-947d-8eb47e0de05a | -17.8246 | -57.4631 | 2024-10-18 00:16:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 1436f7e7-c64f-3eb5-aef9-9be8f36c7a4f | -17.9036 | -57.4534 | 2024-10-18 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| c1ccd1a3-dc9b-3d49-a6ad-4994cfc9db4b | -17.9234 | -57.451 | 2024-10-18 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 35ef9670-53a7-3f37-9d73-0998af508a2e | -18.2982 | -42.1942 | 2024-10-18 00:16:47 | GOES-16 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 127.7 |
| 4b8c0f02-a65e-3965-83af-84106259e07d | -17.9629 | -57.4462 | 2024-10-18 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.5 |
| 258649d6-5282-3be2-b05e-3beba998b89e | -18.0632 | -57.3514 | 2024-10-18 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| e07a0317-31b5-3ee8-ad54-dcd87509b9c9 | -20.7911 | -50.7012 | 2024-10-18 00:17:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.9 |
| 13a39c9c-b4a6-314e-9de3-d5e51bc32860 | -20.7917 | -50.6786 | 2024-10-18 00:17:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.4 |
| 5ce7fe0a-6871-33f3-9964-7f08a676217a | -20.8116 | -50.697 | 2024-10-18 00:17:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.0 |
| 22ce67bd-0150-35d3-aab7-cf5d2ae1041d | -20.8121 | -50.6744 | 2024-10-18 00:17:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| 606515ff-bdfc-35bd-80db-e25385dc4dbf | -21.9454 | -49.7233 | 2024-10-18 00:17:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 100.2 |
| 7a963587-759b-3e14-a88d-11c4ef483088 | -21.9662 | -49.7186 | 2024-10-18 00:17:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 172.2 |
| 9df81d65-e8fd-3938-97b2-37ded2b50cc9 | -23.3701 | -47.3747 | 2024-10-18 00:17:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 003a1c38-9dfa-36cd-b127-cd4077ef605c | -1.619 | -47.0919 | 2024-10-18 00:25:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 05969828-f077-3c9a-ae15-4793f9607a46 | -1.6191 | -47.07 | 2024-10-18 00:25:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 17a1c2e1-39f5-3ff9-a504-b2dabca3f95d | -2.188 | -48.7248 | 2024-10-18 00:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 50dcec0a-7ac7-314f-846d-4ca4cdfe498c | -2.6105 | -49.4811 | 2024-10-18 00:25:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| c8f08813-a2ba-3259-8a13-e9c7c6661227 | -2.7229 | -54.6556 | 2024-10-18 00:25:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d253fa0d-ac1e-3ef4-b274-e2e82b35d069 | -2.8795 | -51.6695 | 2024-10-18 00:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 67d18d04-81bc-3d3e-ab9f-faf7d39d19ea | -3.1382 | -51.497 | 2024-10-18 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 179207e8-64b0-37b9-ac56-4be038837714 | -3.1383 | -51.4763 | 2024-10-18 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 2f65a671-08b5-31d7-9a58-865906c4fb05 | -3.1566 | -51.4965 | 2024-10-18 00:25:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 674eadde-f62f-3221-99eb-1376ff59e5b2 | -3.2862 | -47.133 | 2024-10-18 00:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 501ed71e-325b-3f37-b2ef-d7cb9aaca845 | -3.2863 | -47.1111 | 2024-10-18 00:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| f34d2e84-7ce2-3036-bf0a-c5a12be7b8a1 | -3.3644 | -50.3023 | 2024-10-18 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| c236c55c-d22d-33c0-9dc6-7422fcee4cd1 | -3.7007 | -45.9223 | 2024-10-18 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 8ace13dc-91b8-36a7-abf2-5c10c1bb44a5 | -3.7009 | -45.9 | 2024-10-18 00:25:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 06dad2a2-5d77-335e-b75a-18b101c84879 | -3.8733 | -52.0715 | 2024-10-18 00:25:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3def688d-b560-3db2-8c81-fbc797ebede5 | -4.4072 | -45.9773 | 2024-10-18 00:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 122.2 |
| f025dd8c-24e3-35aa-aac7-884460175632 | -4.4257 | -45.9987 | 2024-10-18 00:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 6b8c181c-5e7b-31f3-a3f1-d03037707a9a | -4.4258 | -45.9763 | 2024-10-18 00:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 258.1 |
| ad60a8ff-c200-3b3f-9d41-c8df3543f983 | -4.426 | -45.954 | 2024-10-18 00:25:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 121.2 |
| cec2e80c-2b1e-3005-9793-a6759b1a14cc | -4.5613 | -48.0358 | 2024-10-18 00:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5fab5cc4-90cc-3e8e-abe0-46e67072bf32 | -4.5614 | -48.0141 | 2024-10-18 00:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2111e277-afca-3443-979c-21e801ac9ba1 | -4.5799 | -48.0349 | 2024-10-18 00:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 47da8c74-267e-32df-b2a7-ce95cf617fee | -4.58 | -48.0132 | 2024-10-18 00:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 5b23c7a6-a9d8-3a14-8995-8491a93338d5 | -4.6653 | -46.3418 | 2024-10-18 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 06ab50d0-34bb-3450-816c-042c10ee98bf | -4.6655 | -46.3196 | 2024-10-18 00:25:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 232e89e6-6c9d-3549-9816-219a1c68dbc0 | -4.9397 | -47.0336 | 2024-10-18 00:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 0b280982-675c-3cb4-9947-6f425491bb45 | -4.9583 | -47.0325 | 2024-10-18 00:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| d1de0a30-63ce-39bd-8f21-6d3856983e31 | -6.6703 | -70.1174 | 2024-10-18 00:25:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1c04909a-5e3e-3114-9d38-11e9f85c92ec | -6.6886 | -70.1171 | 2024-10-18 00:25:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 93f6799c-e97a-3976-94d7-08741e662fcd | -10.2956 | -67.7461 | 2024-10-18 00:26:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 66.3 |
| dda84d05-2cd7-3d1c-8a18-2fae80cf48f0 | -10.2957 | -67.7276 | 2024-10-18 00:26:05 | GOES-16 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 01b22a74-b195-3f8f-9d13-0014878a2cf6 | -11.4859 | -65.1198 | 2024-10-18 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c2a9ffda-bb48-3b53-af81-83af32665a94 | -11.5046 | -65.1189 | 2024-10-18 00:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0372007e-d7d1-37a2-85be-7909b3220d2b | -12.4964 | -63.2258 | 2024-10-18 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f83f99fa-fbc7-3f00-beb2-dbf7b8b3ed19 | -12.4966 | -63.2066 | 2024-10-18 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| ea12944a-9693-3231-88ed-80595dd6dcb5 | -12.5155 | -63.2055 | 2024-10-18 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 13b13a9c-c07a-313b-8c9e-af636210941a | -17.189 | -45.4644 | 2024-10-18 00:26:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 91.0 |
| c4c6896b-b2f1-3029-9127-0b5d45f28b89 | -17.2177 | -57.3102 | 2024-10-18 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 130.9 |
| 29d53e1d-a6f6-3f18-afe4-503f7f2c529e | -17.2373 | -57.3079 | 2024-10-18 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 166.6 |
| 7dfb0079-aa3d-3b0e-abdd-1f21fb3a6e16 | -17.7851 | -57.4679 | 2024-10-18 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 117.2 |
| a683d2d2-74b3-30dd-b0e0-73262a73677d | -17.7855 | -57.4473 | 2024-10-18 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.2 |
| b63b9d36-1f42-3e73-858a-919af840daeb | -17.8049 | -57.4655 | 2024-10-18 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 168.5 |
| a7b8018c-49c3-3871-bdaf-0deaf7d29d86 | -17.8052 | -57.4449 | 2024-10-18 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 47203951-7a0d-3365-826d-a0777248059e | -17.8246 | -57.4631 | 2024-10-18 00:26:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| a4ea2f5d-6b9a-35d9-bb87-6e9ffa2ab6ea | -17.9036 | -57.4534 | 2024-10-18 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 7f4974af-84e3-3373-a607-b2d0493f842c | -17.9234 | -57.451 | 2024-10-18 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.3 |
| 134fc874-0a7b-3b97-866e-8dc58acd7123 | -18.0632 | -57.3514 | 2024-10-18 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.1 |
| 379114fc-5746-3ab1-8872-652a511b77dc | -18.1993 | -56.3399 | 2024-10-18 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.3 |
| e6ecb7a0-119e-362a-ae91-5bbb922bdba0 | -18.1997 | -56.319 | 2024-10-18 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 966157d0-3e20-3586-8d22-94b4e0a85871 | -18.5495 | -43.2208 | 2024-10-18 00:26:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 64.8 |
| 8c9d8c79-9b19-3047-a60a-bfed619f17a8 | -18.2537 | -56.6237 | 2024-10-18 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 773476df-84a6-34d1-85dc-ba4293167ea5 | -20.7911 | -50.7012 | 2024-10-18 00:27:01 | GOES-16 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| b821b7b4-1170-31f5-9bdf-8e11b0788a20 | -21.9662 | -49.7186 | 2024-10-18 00:27:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.4 |
| b218caea-c230-3fc6-9b78-a614fd74e7f2 | -23.3701 | -47.3747 | 2024-10-18 00:27:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| 31efa6eb-6703-31ad-9840-10bdce8077ab | -1.619 | -47.0919 | 2024-10-18 00:35:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 6bef6478-cfcd-3a03-a73d-89c2726fa80b | -1.6191 | -47.07 | 2024-10-18 00:35:15 | GOES-16 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| fbc74478-60bd-37ba-8af9-726efbfbdd45 | -2.6105 | -49.4811 | 2024-10-18 00:35:21 | GOES-16 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 67775e26-c6f5-3544-9625-d8be6fb5cce2 | -2.7045 | -54.656 | 2024-10-18 00:35:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 25461db1-13d5-37ca-9e29-7f5f33f2c2ee | -2.7229 | -54.6556 | 2024-10-18 00:35:21 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e4627176-4cd7-322e-8132-eaa7f9b9e22e | -2.8611 | -51.6699 | 2024-10-18 00:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 667bb39d-1b68-3aaa-8577-1607ef8639bc | -2.8795 | -51.6695 | 2024-10-18 00:35:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 5a84f430-d763-3f7a-b754-797b97c914c0 | -3.1382 | -51.497 | 2024-10-18 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 7d1ce9d1-46e6-393e-88e3-b33289849c3e | -3.1383 | -51.4763 | 2024-10-18 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 4fb9c69a-9609-3926-b485-1eeb33a6d3f6 | -3.1566 | -51.4965 | 2024-10-18 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 74545652-0940-38c5-80a8-14b9347cfc2b | -3.1567 | -51.4758 | 2024-10-18 00:35:24 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 1a81685d-f45e-351a-89c1-0ab5161b0d3e | -3.2862 | -47.133 | 2024-10-18 00:35:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 9b4750ed-a51f-32f1-9a26-baba1c1ebad2 | -3.7007 | -45.9223 | 2024-10-18 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 94.1 |


[Clique aqui para ver as próximas entradas](README3.md)
