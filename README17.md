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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4845d47a-d531-3ab3-a8e2-2cf393e860fb | -3.56919 | -59.44979 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ca756c0-e441-3c23-b00c-469292641944 | -6.6193 | -59.98542 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f994222b-97e9-3607-b2c3-8aa8ab96a700 | -8.28819 | -55.10342 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8b6936ab-cd0c-33c0-98cf-ded2d7a17e39 | -3.49429 | -59.17002 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b800b025-1d16-35a6-ad4c-5da8fbe699ec | -6.89338 | -59.21383 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5d9c07d0-51c7-3f06-9ea1-e368c502a3b6 | -8.49374 | -57.60939 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| bff1a034-187b-342a-844b-96ad8ee996a8 | -7.29471 | -59.53477 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a2fe232e-8262-3fa5-92e3-b9195b449842 | -12.09111 | -50.75804 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 4a67889b-5298-37d5-af18-0551f6b8a01b | -12.08542 | -50.76569 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 24a03693-034c-35d4-b98a-95855bbf636f | -3.44561 | -50.11249 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 8bc63d30-6fe8-34fd-9e0e-2886f19936a3 | -8.13279 | -54.82417 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 2c5e711c-3bfe-393c-92b5-df1050279f70 | -3.78721 | -60.75895 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 3ca9f419-dfe5-3ac8-ab9b-d227e969557b | -10.42168 | -49.34196 | 2026-09-24 00:39:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 19cd5c42-a067-3b77-b11b-12990250d7df | -4.89334 | -55.97397 | 2026-09-24 00:39:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 22c3ea14-05c4-3363-9792-33a9fea041dd | -4.02343 | -52.07949 | 2026-09-24 00:39:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 07cdd43b-9487-3fab-ab95-adf66084430c | -8.45512 | -51.48653 | 2026-09-24 00:39:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a788935b-0b26-31d7-b421-6266483ae9a2 | -8.35038 | -62.81013 | 2026-09-24 00:39:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| ff9557a6-cdd3-385c-bd29-a2983e697b60 | -3.81483 | -58.88914 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 147d1419-a285-3fe0-922f-efb0c50d9329 | -11.7885 | -50.98099 | 2026-09-24 00:39:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7004c44e-fa18-3a61-9f96-1ba23d0dc36f | -3.80589 | -58.89041 | 2026-09-24 00:39:00 | TERRA_M-M | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 59b55256-2145-385a-b5d9-4f6a734c56a3 | -9.20926 | -60.47222 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66daa01f-70ce-3c74-8a77-a313e5cec7a7 | -3.68502 | -60.55334 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| abc39d06-d226-3cbb-b7f5-e92d38fbe634 | -8.58697 | -62.51133 | 2026-09-24 00:39:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 8492a67b-5620-3f54-89f9-2c6438bdb4f7 | -11.96172 | -50.78773 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 51448aa5-879f-3218-ba0a-e053737b46ae | -7.05027 | -62.94169 | 2026-09-24 00:39:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 61035dd0-e401-3f76-b910-76440394070f | -10.85684 | -57.17183 | 2026-09-24 00:39:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a00309bf-ac10-3f7d-b2b9-a9b19aeb7942 | -4.21914 | -63.07912 | 2026-09-24 00:39:00 | TERRA_M-M | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7c263986-8edf-3870-8dcf-0b96a91db213 | -11.97138 | -50.76147 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| bfe0b20e-2787-345f-9c07-1564dda845ec | -5.11124 | -60.2663 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 5e52df56-26da-3e18-9e20-bc6613289d1d | -3.68744 | -60.57102 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 5d7acd6c-4d54-3b9f-819a-60dd50edac78 | -8.35671 | -57.68283 | 2026-09-24 00:39:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 835fd37b-0071-3123-b7ad-35ec9be13bda | -8.4558 | -48.70356 | 2026-09-24 00:39:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 80841bba-aa37-3b7d-94a8-398fcb1fd8dc | -3.45312 | -50.07726 | 2026-09-24 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 8286ad27-8768-39ab-b4c3-01694eba577a | -4.06224 | -56.23251 | 2026-09-24 00:39:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0faf33e7-60cf-34a3-9597-a6b5dfd818a2 | -9.15542 | -59.45248 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98c90c55-f361-3c17-a50e-037b4881dc2a | -8.88868 | -62.55156 | 2026-09-24 00:39:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ae0ff4f9-344d-37c4-826a-c1997f6ba789 | -4.13634 | -56.32755 | 2026-09-24 00:39:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 4d5227a8-a569-3b75-b88a-16b558938359 | -6.6245 | -59.94208 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 72916a50-d611-333d-a9ae-009940353142 | -6.63213 | -59.93195 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 009a1b5b-cf1a-386b-93b7-086e70f269b8 | -7.58818 | -57.65897 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| faf32d30-2207-3720-b649-49955d2208e4 | -9.48052 | -56.76288 | 2026-09-24 00:39:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8be522c6-e261-376e-a144-09eb69131c50 | -11.20589 | -54.13205 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 2dbe0c03-2243-353a-aa3f-e53bb117a7fe | -6.7698 | -63.14848 | 2026-09-24 00:39:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b121694e-3b6d-3cf6-b369-c50a3b6fdb33 | -3.71218 | -54.19434 | 2026-09-24 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| badd30e2-38d5-30fb-ba62-d5a10f1e9a2a | -9.14679 | -61.3961 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 42775810-7b7f-33ab-990c-324d4071c487 | -6.8946 | -59.22265 | 2026-09-24 00:39:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1d09994-e257-33cd-ae4f-c5d638b05b3c | -3.22889 | -54.31955 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5f65da3d-4425-39fc-906c-2de208ab7cfe | -3.68102 | -60.58994 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 49ab282e-7ba9-3d15-941b-3ef31ba90615 | -3.15274 | -54.6003 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| b31aa51d-518e-313a-9b01-d71c007edd4f | -5.5983 | -60.19481 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 601bd7eb-b01f-37a9-a1c7-8e09f91141e7 | -3.58285 | -59.07811 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f056db31-ccc5-3eb8-a160-38a1b913079d | -3.73195 | -59.42381 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| cede5aa2-7089-360b-826a-554646d532af | -6.35012 | -57.77283 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 62afb9fa-a23e-3769-bff5-84c5d260f4a8 | -3.67981 | -60.5811 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 417e0581-d021-3328-8126-96c1dddfc47c | -3.83681 | -59.38468 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 34b68734-d42b-3821-9798-b5cff49e4b17 | -7.52352 | -61.49476 | 2026-09-24 00:39:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 920fba1b-2541-3393-aac5-d4ea1efea8c6 | -2.989 | -54.27599 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| a8db9ff5-7a4a-3bf8-b781-c56f3534a382 | -3.60088 | -59.40302 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2fb249e-d553-325f-80bc-73e8441cac87 | -6.61077 | -59.92323 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dcd4b2a7-415f-3a63-be69-498ec1448194 | -9.84267 | -48.48544 | 2026-09-24 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 11b7f357-1d9e-3ab5-b104-c4d1efb09bf8 | -3.6786 | -60.57225 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 40f7c15e-abaa-3bf0-84be-8b55e366f94c | -11.96162 | -50.74414 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 6bedb99a-3c65-3e4a-9aba-1358c00fb7cb | -6.5848 | -60.06287 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8b21ba9f-183b-3961-9199-94a98e0e4c7a | -5.14502 | -60.31581 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8356230c-8a92-3b2d-a1c2-6d8fbfe68cdf | -7.51277 | -61.48593 | 2026-09-24 00:39:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| eab722c3-987e-30d3-9d84-28e0ec1d1cff | -6.58946 | -59.89911 | 2026-09-24 00:39:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4cbc41e6-b41e-3b09-bb53-5bec9dce2e33 | -4.06999 | -59.86897 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 81e00e9c-c174-3eff-8a78-90c5dc0f5e7b | -12.1561 | -50.76546 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 5a56b5e3-a3f6-3935-894d-f216c90856cc | -6.2484 | -60.03451 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c3c2527d-c623-3465-989c-3ae3642461d8 | -5.41666 | -60.21424 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f07c3ed5-1b1c-307a-9d17-9fcc58d10467 | -8.44993 | -57.62534 | 2026-09-24 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d0dcac27-0149-3322-a5f8-c90e9f9f04a5 | -4.0964 | -62.09125 | 2026-09-24 00:39:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f379fc4c-5017-3b72-b994-a6cacfb88be8 | -10.90298 | -53.95778 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b13464fd-e0d5-33b9-b524-9c332f8082df | -3.92247 | -59.66336 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8a5d8d1e-5854-32ce-b747-10f950c23285 | -3.74897 | -59.28578 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ab262e55-08e6-36d2-8ba7-b2a438b6abb2 | -3.91367 | -59.6646 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 8963966d-d625-3434-837b-e9fc72a72933 | -8.68622 | -62.89617 | 2026-09-24 00:39:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 5bd6eed8-f064-379f-ae2f-bbad2a53368d | -10.98288 | -54.09584 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8769ff14-ede4-38dd-90a8-e5d2478954c4 | -9.20799 | -60.46268 | 2026-09-24 00:39:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6e772655-9c02-30a3-bd07-653cef156349 | -3.48665 | -59.18024 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c8a7e6f0-ed3a-3449-88a6-c455c9eefc28 | -5.42151 | -60.24973 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 16550edf-c4e3-3e6a-a7fc-32b945fc8b7d | -5.91244 | -59.92802 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ffff7c2a-7103-3a37-aeee-1706994f7716 | -3.91488 | -59.67339 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 05cf53ed-2bca-3b93-98e4-13b05d53880d | -4.43917 | -55.07252 | 2026-09-24 00:39:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1f0fea87-5013-37ae-abaa-e5045bd7ede6 | -8.26083 | -54.77122 | 2026-09-24 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 7b4b207a-48ef-38f9-8daa-3a8fbb319a70 | -5.92005 | -59.91797 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4bd7141b-1ca7-3685-a2e2-b006f00fa8b3 | -7.52217 | -61.48462 | 2026-09-24 00:39:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 7150bdd4-4e8c-32b8-a11c-511dbebf47c3 | -11.95572 | -50.79443 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 0ded8394-9af7-3391-9376-85d3b0a79dd0 | -10.91558 | -53.94938 | 2026-09-24 00:39:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fefe05f2-86b4-3024-a1c6-8fe25f4599f0 | -9.84523 | -48.47783 | 2026-09-24 00:39:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 86c83e23-5bc8-3a1a-830e-58e17c108787 | -3.15514 | -54.61698 | 2026-09-24 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| f8229baa-94c2-3e93-b090-eaa45718b8ac | -11.95178 | -50.77056 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 337.3 |
| b8b9f20e-f168-3928-bc5f-0ecf4bc3eaf7 | -12.08156 | -50.74182 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| fd91ec15-9610-3f93-9a31-974d26764826 | -12.13941 | -61.1657 | 2026-09-24 00:39:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 749e3e1e-c905-3402-9a4a-78521224dad0 | -6.16441 | -59.94688 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1de95bf9-fae6-30c0-9fad-11c665546b25 | -6.52948 | -62.93681 | 2026-09-24 00:39:00 | TERRA_M-M | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 924b6591-e02f-3b53-a8c8-47575c116fdd | -3.68381 | -60.54451 | 2026-09-24 00:39:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 91a05219-1a0a-3766-8011-91beb68c8fcc | -5.24789 | -59.98312 | 2026-09-24 00:39:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80aa9551-90e6-3569-ad0a-35ada98e24bc | -7.45928 | -63.63689 | 2026-09-24 00:39:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d9b04297-2b78-3518-bfb2-b163b7f92635 | -4.03117 | -59.8476 | 2026-09-24 00:39:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |


[Clique aqui para ver as próximas entradas](README18.md)
