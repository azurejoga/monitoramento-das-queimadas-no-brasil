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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15fb2818-e38a-3d84-a78d-f2d8ba56fddc | -10.3116 | -45.3136 | 2026-09-14 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 272bb42a-f31f-35c3-9824-813c1c79533e | -11.2391 | -43.4413 | 2026-09-14 14:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 8399b548-8a3d-385f-8c5d-c6d17c955781 | -11.8154 | -46.5899 | 2026-09-14 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 265cf6fc-86f0-3dd8-878f-8fa24afd976d | -5.1255 | -55.955 | 2026-09-14 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 2f484615-b548-369c-830e-8686a2cf4977 | -10.6958 | -47.5175 | 2026-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| a6526972-2b76-3c9e-aeb4-6f90bfa6ef74 | -9.7036 | -54.371 | 2026-09-14 14:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 97aa4fe8-5d47-3795-a3a9-3fb5d4bf1a56 | -3.4089 | -58.2142 | 2026-09-14 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 155.0 |
| 00413dab-0f1f-39c3-9896-b5deef8f1fde | -8.5415 | -54.7187 | 2026-09-14 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1f70b0a6-792d-3ac1-98c3-4a737c3c0ad6 | -6.5838 | -58.8304 | 2026-09-14 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 414eb07b-a452-3b41-91da-f1d627703e1b | -3.5893 | -59.0773 | 2026-09-14 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| a228f431-e736-3fb1-8c42-6dad40de6ba6 | -2.884 | -50.4219 | 2026-09-14 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| f87c98c5-bc01-3574-a7b8-cadf33b6e555 | -3.3493 | -59.8288 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| ca7b3063-14ea-3e74-bd5d-2b8496a5e81f | -4.115 | -60.6886 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 960a2414-484e-3b0f-8c1b-f43f829660f7 | -9.9956 | -50.2675 | 2026-09-14 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 89126e2f-979e-369e-b1e9-018bbf41aa8f | -15.5572 | -48.7953 | 2026-09-14 14:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1828aae8-675b-3b74-95b4-4b80862dd5a6 | -6.8445 | -55.581 | 2026-09-14 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 823f8137-e8bc-3e70-bca0-2e76c44d49a9 | -3.728 | -61.7555 | 2026-09-14 14:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 35a9a9d9-6613-3b69-9f9c-a3d4449409e4 | -7.1048 | -41.7971 | 2026-09-14 14:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 151.7 |
| b5170703-6ce0-3674-b09b-914d8e1f9ba2 | -10.87 | -46.35 | 2026-09-14 14:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b531b4db-eced-3def-a7d3-7a90c01ec585 | -10.81 | -46.29 | 2026-09-14 14:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb53d1f-0de2-3f9b-be5f-40a026f21282 | -2.91 | -50.4 | 2026-09-14 14:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe065bf0-cb54-3369-b074-fcf2024efb2b | -10.81 | -46.33 | 2026-09-14 14:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 58c1bf54-788c-368c-9d48-63437ed36091 | -9.5 | -45.5 | 2026-09-14 14:15:00 | MSG-03 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 448fef33-2d1c-318f-9b37-1badadc82d38 | -8.8081 | -45.8753 | 2026-09-14 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| c7283d23-97c8-3306-a6aa-1e53ca928b0e | -1.7133 | -54.9521 | 2026-09-14 14:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 560d31ad-80bb-3411-b085-fc93070001d1 | -2.9531 | -42.8469 | 2026-09-14 14:20:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 7b7e637a-cf11-3261-aa31-a686ecf4c6de | -3.314 | -59.3706 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 3018ad08-39b9-3584-93f9-5d4fa035fd04 | -3.3505 | -59.3891 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a8ff8666-00fa-392e-92bb-762b61194945 | -10.2922 | -45.339 | 2026-09-14 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 6906a871-6b88-38f2-8b30-ebcbde1eee60 | -6.1109 | -57.684 | 2026-09-14 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 196.2 |
| 74981562-ac5a-390a-b4f1-7f7e2229aaab | -14.1852 | -47.4296 | 2026-09-14 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| af762bfd-0dc6-3681-8609-43b8b8e55f3e | -10.4519 | -48.6453 | 2026-09-14 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 240da1ee-1d14-3380-944a-8ecdab161299 | -3.8096 | -58.8994 | 2026-09-14 14:20:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c8e1deaa-85bd-3b85-a516-ee07bae7a47e | -9.4936 | -45.4818 | 2026-09-14 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 5ad0e259-be2f-3f35-9d6d-bf38a4c81f28 | -10.6832 | -54.127 | 2026-09-14 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 4cf4dcc4-3f09-3d17-8555-f8d6dee7d17c | -12.1265 | -44.199 | 2026-09-14 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| dcc6458c-d5a1-3cfa-94db-6c004082920f | -3.728 | -61.7555 | 2026-09-14 14:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| a8403e5a-0db9-38ff-8b4d-412b1ba793e3 | -7.3017 | -51.7525 | 2026-09-14 14:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 1709b47b-0c11-3e49-ae84-4acc366fc410 | -3.1514 | -58.644 | 2026-09-14 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c8f38830-7864-376e-aff5-b311c522ba85 | -6.5837 | -58.8498 | 2026-09-14 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 150675da-c4f8-3b7a-8f44-516c5234a401 | -3.6076 | -59.0769 | 2026-09-14 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b327beba-91db-3d7d-9bc0-28bab60343ed | -3.4089 | -58.2142 | 2026-09-14 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 637457b8-517a-3fcf-9cbb-678c5a08f412 | -2.921 | -50.3999 | 2026-09-14 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.2 |
| 3afc9bf2-9d4e-3bbb-acc2-ee171b741f97 | -3.6077 | -59.0577 | 2026-09-14 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 9d64e7d6-67f4-3298-9495-7f1b81b82e2a | -7.1048 | -41.7971 | 2026-09-14 14:20:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 138.6 |
| ca23e941-c348-3933-8862-5ff0b1fe1208 | -7.0471 | -45.2765 | 2026-09-14 14:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| a115e772-87b4-3965-9502-0bdcc041e927 | -10.6827 | -54.1679 | 2026-09-14 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 171.3 |
| 2caf8604-6510-3e45-b03c-1ff6dac530d8 | -10.3116 | -45.3136 | 2026-09-14 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 197.3 |
| 84bd3107-c62b-3cd2-8720-c1a49fc7beb2 | -3.1697 | -58.6437 | 2026-09-14 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 31779707-aac4-3c2c-9acc-44cfb2ba598f | -3.3493 | -59.8288 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 6643feea-7708-317a-94f8-c75dd869b16d | -5.1255 | -55.955 | 2026-09-14 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 1c88928b-7fba-3c5f-b891-14da4d3dac89 | -10.4914 | -51.3212 | 2026-09-14 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 6be95d85-ad15-3c2a-ad93-c1f02cff6af4 | -6.5838 | -58.8304 | 2026-09-14 14:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| ad7f3f0a-a69a-3f43-9c0e-83e5ee895d62 | -10.7842 | -50.6133 | 2026-09-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1d7d8c27-e992-3556-a7b3-16b26b0d7aae | -15.5572 | -48.7953 | 2026-09-14 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 321740b8-9cce-395d-9c56-59c9cac2878f | -10.2929 | -45.2932 | 2026-09-14 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 044b558b-94fc-3e5b-aaba-bd8bf54cf6e9 | -10.6829 | -54.1475 | 2026-09-14 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 226.5 |
| b0e55edd-2c19-3214-87be-f6144a1f82f9 | -10.7839 | -50.6346 | 2026-09-14 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8f9dc829-4e49-3f40-aea8-9161582ffe88 | -3.4089 | -58.1949 | 2026-09-14 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| f133e4bf-cf7f-33bb-8671-6b2bd2df78a6 | -3.3871 | -59.4075 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 5e4e2c51-520b-3066-8271-4e6afec37873 | -2.8839 | -50.4428 | 2026-09-14 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 4da5aef1-039c-3740-a25f-87291422a22d | -11.838 | -46.3834 | 2026-09-14 14:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 447e22ab-b526-3385-ae2f-2ec3900542a0 | -10.2926 | -45.3161 | 2026-09-14 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 155.2 |
| f7ce6a95-79fd-3b0f-8b2b-a5d5f4cf458c | -6.1111 | -57.6645 | 2026-09-14 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 5f38e315-5a30-33ba-a4d7-990be48920bd | -2.9025 | -50.4004 | 2026-09-14 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 142.4 |
| f78de8cf-d135-32be-a2ed-ec22f684c93a | -4.115 | -60.6886 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d5c84b34-6710-309f-b695-5cf96c833028 | -3.3494 | -59.8097 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5f040414-cf52-3224-97dd-e8de3031f24d | -2.9024 | -50.4423 | 2026-09-14 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 95ceabda-9dd1-3a5d-b72f-0ce797716a5c | -6.1108 | -57.7035 | 2026-09-14 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 578ccd3d-8cc8-39d5-834d-1e0d5d727021 | -6.0255 | -59.9484 | 2026-09-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c563b2ab-3ead-339d-a6ac-c583b5d1cd87 | -10.9506 | -57.1895 | 2026-09-14 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 327b9f06-2c7e-3901-9c44-3a246027f829 | -6.0256 | -59.9293 | 2026-09-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1799da2c-04ce-3c65-87d5-0b66c232efe8 | -4.1334 | -60.6692 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 002d3c15-7512-38be-b504-2418a428c3fd | -9.8989 | -47.6095 | 2026-09-14 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 5d673b9c-1390-3255-bc91-3ac1f67d53b1 | -10.312 | -45.2907 | 2026-09-14 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 8537b9d5-81f2-333b-96ea-95c4b13db7f8 | -15.5768 | -48.792 | 2026-09-14 14:20:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 22cde3b7-91f9-3892-b0ad-ee43cc642d16 | -10.7145 | -47.5374 | 2026-09-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d6727b61-b426-3caf-a0a8-94ab8e4aa4a3 | -14.205 | -47.4039 | 2026-09-14 14:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0bb746bc-a084-334f-8947-77bd59587d98 | -10.433 | -48.6474 | 2026-09-14 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| b634a381-495e-3209-9976-3ce0c56dbee4 | -16.9909 | -45.4594 | 2026-09-14 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3b617a0a-5b7a-3a3e-a24f-197d967a52a2 | -4.1333 | -60.6882 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 117.3 |
| c941bc25-a541-34c7-a934-cdbd67171b7e | -8.6194 | -44.4357 | 2026-09-14 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 159.0 |
| bffac49f-f326-3c95-ba46-13dfb8318215 | -10.2206 | -50.373 | 2026-09-14 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 9cce592d-7188-3ec2-812f-bb4eb94ff090 | -6.3747 | -60.0319 | 2026-09-14 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6109e0b4-3ead-3486-a824-b305c5b6d435 | -13.4458 | -43.8128 | 2026-09-14 14:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 19eff9fb-4536-33c1-96bb-886ce45a6b44 | -9.7036 | -54.371 | 2026-09-14 14:20:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| dec14449-555e-3471-a52a-856a366f706e | -15.5763 | -48.8144 | 2026-09-14 14:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 2b62679c-548e-3235-90b2-0478edd526b2 | -10.5667 | -51.3349 | 2026-09-14 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 312e908e-c659-35db-a4b5-e249f6c7a492 | -7.0859 | -41.799 | 2026-09-14 14:20:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| 43038911-3972-3a6a-8671-58e8999d7870 | -10.4917 | -51.3001 | 2026-09-14 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 689406f9-f529-3a46-a97a-a1a65052cb53 | -11.2391 | -43.4413 | 2026-09-14 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.0 |
| 44cb2629-8482-3a08-a1a8-993ced4a6a6a | -3.5893 | -59.0773 | 2026-09-14 14:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4ffcb102-bf31-35bd-9d13-5669be430e55 | -6.8445 | -55.581 | 2026-09-14 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d56e6bf8-1877-3724-9f26-c0d803b7bc2c | -8.5809 | -44.486 | 2026-09-14 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 18478efd-bcda-3373-bc65-9362c1ec1ffe | -10.6958 | -47.5175 | 2026-09-14 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 6ae2e39b-dc80-32b2-899c-1c14f4d57148 | -3.3676 | -59.8285 | 2026-09-14 14:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 168.5 |
| a495b3c7-6454-3ed3-a1c5-0803eb0b73f2 | -15.5121 | -43.8455 | 2026-09-14 14:30:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 37b843b2-8eae-32a5-a1b1-b29121c606ae | -4.115 | -60.6886 | 2026-09-14 14:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| b00cb24c-168f-3ac9-a99b-179c45542aad | -11.3543 | -46.7649 | 2026-09-14 14:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a04b9725-380b-38cd-a28b-0008ff226ae1 | -12.1265 | -44.199 | 2026-09-14 14:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 270.9 |


[Clique aqui para ver as próximas entradas](README74.md)
