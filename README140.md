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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 409c73a9-cf6f-33d3-872d-8c0cfb978ffc | -12.9273 | -51.0291 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| ffc2c378-dd36-3400-8b41-0835c9f3bc58 | -6.3196 | -59.9956 | 2026-09-22 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 49af18a9-8898-30e1-8adc-de24ab985edb | -12.0836 | -50.0378 | 2026-09-22 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 339.9 |
| 14736ac3-df48-3a62-b574-22ced42b1500 | -12.891 | -50.9052 | 2026-09-22 14:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 43a160c4-ed54-3e64-90ff-58a0c4d0bb0e | -3.4599 | -59.54 | 2026-09-22 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 63e8b357-e33a-3716-aab0-077a527b5361 | -6.1108 | -57.7035 | 2026-09-22 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2f084d17-ddee-3527-a3c6-204e8379314d | -4.64 | -42.0976 | 2026-09-22 14:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 108.1 |
| 62abcafa-cc41-3140-a281-d10c35fa1c56 | -4.6587 | -42.0964 | 2026-09-22 14:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 291.3 |
| 0c061c9b-da5d-341a-8c4f-1b79d45f9087 | -11.156 | -51.1051 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 23aa992c-5033-34de-8cf5-159e5dd60cb5 | -12.3481 | -50.1994 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 939fa80b-9f67-3862-ac8c-ac4d27afda75 | -3.4214 | -60.2086 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 2ef7dd80-6590-3406-a60d-be13331e06e9 | -7.917 | -61.3481 | 2026-09-22 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| eff7e8b8-baa4-34f0-a444-13d19ed3b02d | -6.3196 | -59.9956 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a1ed9dee-cb63-3731-a026-9438e21a14f2 | -9.6009 | -45.923 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 3bd2e7e2-4e2b-3676-b861-0f3b4d936df3 | -10.5561 | -46.7095 | 2026-09-22 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 2b7e2792-0315-3855-9344-d811f6526cd6 | -9.8668 | -45.8691 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 1e32a652-708c-33c4-ba50-3f00d642807e | -3.3138 | -59.4472 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a26a807e-e8c8-3609-93d8-cf3ee5336f96 | -6.7989 | -43.9008 | 2026-09-22 14:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 089d0bb7-e0fe-381a-96fb-51781ff3260f | -9.3797 | -48.3232 | 2026-09-22 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 5a4e1409-6141-3c29-9590-71547a3b081b | -12.1027 | -50.0355 | 2026-09-22 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7e05e064-e4f0-3470-be30-9029d7caf4e2 | -12.8053 | -54.0669 | 2026-09-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 68ca7b90-f98f-3945-8f7d-20a220718cec | -2.9997 | -60.8047 | 2026-09-22 14:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 80f090d6-dcdd-3e0f-8576-fba655c24c8e | -3.8096 | -58.8994 | 2026-09-22 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| fbf1cbf0-4d35-3a2a-80f6-f01e3be1d2a6 | -3.7547 | -58.8622 | 2026-09-22 14:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| f7b609cf-cab6-3ece-9acf-55c32fbc6366 | -11.175 | -51.1031 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 1df28002-e48f-332d-9382-885f9204b534 | -12.3297 | -50.1586 | 2026-09-22 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 360.8 |
| b4df2025-bf70-379f-a51e-8cadf21f1ba8 | -8.7919 | -44.2546 | 2026-09-22 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 39baea99-d48a-389b-955e-f746a7e11ab4 | -3.1901 | -57.8898 | 2026-09-22 14:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9c01113e-ca43-36f8-ba3a-0889dbcaa7dc | -11.269 | -54.0334 | 2026-09-22 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| e820c55e-e959-315e-9276-f9dfd0be7b48 | 3.0196 | -60.1017 | 2026-09-22 14:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 72b816c6-62a3-30aa-af9a-bbb573d3c6c9 | -6.3015 | -59.9387 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 6f24e9d2-d448-3f14-a8f9-99392754f536 | -3.3493 | -59.8479 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 441f8a39-4956-38e0-9034-f285d3e69549 | -3.405 | -59.5411 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 64f94d32-e1f0-3ba3-ac6d-90ce67658d44 | -10.2517 | -45.5039 | 2026-09-22 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 165.7 |
| 5b36991c-693b-36bc-8b02-1c6b408b07e6 | -7.0352 | -44.6396 | 2026-09-22 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 126.8 |
| c71ee588-6b8e-3a96-acdb-3a013cf4a40d | -8.7916 | -44.2778 | 2026-09-22 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| f4e20489-0ccd-397f-a282-dbba21d70502 | -10.2707 | -45.5015 | 2026-09-22 14:40:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 1a27b5a3-0966-3b11-9a7a-08d298d3a07c | -10.2979 | -50.2372 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2be0dffc-7989-39f8-8e05-d016e855f76b | -6.2024 | -47.5245 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| de52c9aa-3929-340a-82d4-f2ce6492f5e9 | -6.3013 | -59.9771 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 92d5d5d3-f25f-3bf2-a380-f9bfbb12c0e7 | -12.9481 | -50.9195 | 2026-09-22 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 5b0e4305-b946-3a86-bf70-aae609383d49 | -3.3867 | -59.5223 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 2bd0b113-0b8c-378e-b0f5-26aa77620d53 | -10.5558 | -46.732 | 2026-09-22 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 40a54b5e-2d5d-3ea1-918d-978a4ed46c1c | -13.2033 | -51.7193 | 2026-09-22 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 432bb354-38d5-3269-8279-2212dac3c035 | -3.4057 | -59.273 | 2026-09-22 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 839bee12-9022-3858-a1b2-546b2d3ce725 | -5.4179 | -60.2166 | 2026-09-22 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| cb9ac42d-7347-3d46-85ce-f7899dd55704 | -12.9286 | -50.9434 | 2026-09-22 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| afc9de88-753b-3ab2-94ec-cc5c15315d92 | -6.1653 | -47.5052 | 2026-09-22 14:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 6c2cdd53-0d34-3dfb-b2f2-3990777460c3 | -2.9906 | -57.2137 | 2026-09-22 14:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 81fa4f87-2c66-3fb4-a03b-5959af5ad951 | -3.4215 | -60.1896 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| c45c2de9-2008-3e2f-a546-0013704c093b | -6.0924 | -57.7043 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| f97ad4ce-d039-39c0-ad1b-220a282346f9 | -3.4634 | -58.329 | 2026-09-22 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 95ab2e7d-5291-368c-93b4-2681ee21e21d | -5.6223 | -43.3701 | 2026-09-22 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 026279a0-c6ee-31c2-91c1-b068e182bfaf | -6.6704 | -47.3811 | 2026-09-22 14:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 83edccb0-2c0a-33ac-af1c-13b2a75972bb | -11.1557 | -51.1263 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.5 |
| d54631e2-8277-3a29-af6a-9134dc97fe78 | -12.2827 | -50.7226 | 2026-09-22 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 4931874e-3cbc-343e-bf23-3159b6220bc3 | -12.8244 | -54.0649 | 2026-09-22 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 261c0c7d-00e9-3b7f-85c6-8da9fe9c21cf | -3.1901 | -57.8704 | 2026-09-22 14:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| eec02942-f5ee-3d0c-bbb4-11337fed1a33 | -9.6006 | -45.9456 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 58dcf6e5-3c09-3e8e-bd20-8a19856f095c | -10.2793 | -50.2177 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 0b0a1bce-dbae-3c40-8fef-2677b8b85200 | -8.8335 | -45.3741 | 2026-09-22 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 37bd3e20-d69f-3079-a140-438bd5c28c2e | -7.5548 | -48.6843 | 2026-09-22 14:40:00 | GOES-19 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 80.5 |
| e3d0ba89-9bdd-3cee-b590-6f414235f865 | -9.859 | -46.4114 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 280.8 |
| bc9ea38e-1c1b-312f-ae70-d565411a964f | -6.1111 | -57.6645 | 2026-09-22 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.4 |
| a647e308-4539-3d98-a1f2-3b1601f9406e | -4.6589 | -42.0726 | 2026-09-22 14:40:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 241.1 |
| 7b306a83-12c1-3c1d-b70c-3b31652bf2a6 | -6.9683 | -47.4899 | 2026-09-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4b40d8f9-e025-31b2-bef9-0a86b39e830b | -6.8032 | -59.1693 | 2026-09-22 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6d20a9e0-b262-3bce-93ec-cd0ba9ac6f18 | -3.6065 | -59.4413 | 2026-09-22 14:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 763b3975-9c89-3b7b-8493-25589eb66dba | -10.7262 | -50.7044 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| dd3c4f38-18a7-3811-91cf-f8c16944606f | -2.8285 | -50.4653 | 2026-09-22 14:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| cd6930ac-a921-39a4-a206-9c356111eac2 | -11.3784 | -44.2195 | 2026-09-22 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| fcbd0dd8-0884-31b7-8ac7-8e21f7ea1846 | -9.5353 | -47.9569 | 2026-09-22 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9918c15d-1725-344c-9675-45dd05e0a6e4 | -9.7883 | -46.0593 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f39e50f6-a6de-3185-a9f5-c0c80f244dc3 | -11.2118 | -54.0797 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e3fa5979-6c01-377e-9a23-0bfec31963a3 | -2.8534 | -60.9206 | 2026-09-22 14:40:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 36d63ac2-d1fc-3081-9330-1fb65e2f6eb3 | 4.0579 | -61.4095 | 2026-09-22 14:40:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a150178e-adc9-3282-bd21-d39f294c4dc9 | -3.2183 | -61.0472 | 2026-09-22 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 821002ab-62ba-3baf-bc39-f8574196f0aa | -10.7466 | -50.5959 | 2026-09-22 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 85557a52-91d8-3e51-ae65-7479ece0cf3f | -3.0542 | -54.4081 | 2026-09-22 14:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| efcdc89b-b80e-3e35-82a5-220630223e39 | -12.283 | -50.7011 | 2026-09-22 14:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 50969b71-1626-3b61-b6e2-67b81d29a4d4 | -9.8665 | -45.8918 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 00921a71-d34b-3726-bf15-3a26a19e044d | -3.2396 | -53.9417 | 2026-09-22 14:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| 49c4f2b7-7d68-32b5-b204-0b78b9ee0c09 | -7.1745 | -47.4517 | 2026-09-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| e4bad2b3-43cc-30da-bf70-de8045489d11 | -5.8676 | -49.7651 | 2026-09-22 14:40:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5f6da2d3-02f1-31da-b892-e8d55859e1d3 | -8.7706 | -45.8567 | 2026-09-22 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ca10ebeb-ce12-32bb-afa3-67609063ae91 | -7.1553 | -47.4971 | 2026-09-22 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 7c52418f-5419-314f-8e8c-b0ed37539186 | -3.9509 | -60.5022 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d7f00511-e244-30ca-b4e8-2e374a16957c | -3.2818 | -57.8491 | 2026-09-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3a6f9515-2791-304b-bdd9-abf7db27d0c0 | -5.9333 | -53.5362 | 2026-09-22 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 5c758932-aa03-3efb-b95d-62f04f9978ff | -3.2817 | -57.8685 | 2026-09-22 14:40:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 4ef5f1dd-94a8-3a75-a114-618864494d11 | -10.4294 | -50.2877 | 2026-09-22 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 518dfc41-9e9e-3216-8fa1-949026af3edd | -3.3309 | -59.8673 | 2026-09-22 14:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| aa1f9c0f-e248-3656-a7ec-1ad653636e15 | -8.3545 | -47.5468 | 2026-09-22 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 89d0d640-6831-3b93-85aa-9bd5d21bbfdd | -3.3 | -57.8681 | 2026-09-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 126.5 |
| c59039f9-ea8d-368d-8676-e97c0bd694aa | -3.4272 | -58.1945 | 2026-09-22 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 88edd4b7-5ffd-38f0-b645-01ac8dff30f4 | -3.4009 | -61.0629 | 2026-09-22 14:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| adf50277-e895-35fe-a8ce-4a57601a1b4a | -7.0046 | -45.7544 | 2026-09-22 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| b6027e72-b4e6-31b9-bc12-0e4ce03365aa | -9.7693 | -46.0615 | 2026-09-22 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| ee4b7e85-a26e-3888-a300-949e375f3baa | -3.3183 | -57.8677 | 2026-09-22 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 98337c0b-c964-347e-b97a-6fb4e6cba4d2 | -10.7223 | -54.0008 | 2026-09-22 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |


[Clique aqui para ver as próximas entradas](README141.md)
