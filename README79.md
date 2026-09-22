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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dad31d10-088b-3ac1-b283-699042f4369e | -4.30688 | -55.59526 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ee07786-7e9e-3459-9d65-1f51da99080c | -6.09942 | -57.62455 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 653cfd11-03d2-321a-816a-5a78838c5dd5 | -3.06397 | -54.40192 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 729a24bd-e714-3e05-8b7b-59200f87954f | -2.99934 | -54.16902 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00c38627-b84c-3038-88e5-11700d99c54c | -3.39203 | -61.06562 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e4ef1a-4df3-34b9-bb5a-7b471c79b1f9 | -11.96485 | -46.51569 | 2026-09-22 05:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aaa331c-c482-3d60-9c05-b5e6bbb0bb7c | -13.21859 | -46.93703 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 690e8d02-7129-36b3-a39b-aa2c1f4299f9 | -3.82168 | -59.3315 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0252aa49-8ceb-3805-ad5a-5dffcd9bbcb2 | -6.09888 | -57.69217 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 577da17b-67fa-3d2b-9028-2f826b739394 | -6.9192 | -59.62955 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83d85e14-4d28-358e-893d-b32d19618941 | -2.02503 | -48.77642 | 2026-09-22 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc31c693-402d-3aa6-bb7d-3fbb8b537d1f | -3.2008 | -57.83783 | 2026-09-22 05:23:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b23c19a-bb66-371b-9404-daaa55d3fb0f | -3.82059 | -58.89341 | 2026-09-22 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea312009-ba79-3479-a929-c07302c06c85 | -4.58515 | -55.11332 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504e2701-4149-345b-9241-be1cd6add026 | -6.45729 | -59.98651 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dee43e9d-8e14-32f1-9a42-4574154e40de | -3.36454 | -50.76383 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb459fb1-642d-3914-8a00-6d4c2c52beeb | -4.56247 | -54.91943 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b5f0701b-4a33-3917-ad37-bf91aaf5c39b | -3.22402 | -53.95328 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 53ee1753-9df5-3499-be67-207aa09e2ac7 | -6.12363 | -59.95073 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 957d37da-fc6f-3e1d-bdc5-bd2d5907bd4c | -3.49029 | -59.56982 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c487975b-b7c7-3e55-9841-1ec545b2ab84 | -9.09753 | -65.37801 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8910457d-a225-3705-8dbc-0fe3b35e10f3 | -6.79518 | -58.90285 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fef70234-0e62-386e-8cf8-d0fa1e8b2893 | -7.56182 | -55.11224 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b74b7ef5-5f7e-3282-935c-00e481fa1542 | -6.45571 | -59.97414 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aaeb472-1ea8-3ca0-b1a2-56bd0fdc2832 | -13.8577 | -51.847 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a30270ff-8ce9-3954-8433-41db3a21f774 | -6.97763 | -47.50058 | 2026-09-22 05:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba5a62d9-dda3-3fb6-9327-f34275e29522 | -9.1129 | -65.37696 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b270887-46c3-36a4-91ad-90dfe8212e1c | -5.75459 | -45.09359 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 1c8265fc-ad16-30b8-adbb-ac40362834c8 | -6.10511 | -56.10629 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57a41e31-d362-3622-8e9d-9e90227e2507 | -6.43309 | -55.61089 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75d9cf40-4eb3-3085-a27c-fd7a0a5d31ba | -6.83869 | -55.53472 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45f9e6e9-0d04-3d37-af11-97aea5c19ad0 | -5.26109 | -55.92525 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ec789ae-bcb1-36b1-bdef-b452030a7c63 | -13.51247 | -51.51772 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.9 |
| db47baed-1413-3a73-817c-bfb97d79ceaa | -3.05642 | -54.40469 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc9151b8-2d7c-3f78-952c-a97ef486045e | -6.69979 | -56.16195 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec829645-6d0d-3638-8304-9a6f4370215e | -3.58237 | -59.07118 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fbf1e54-b990-3214-b132-0dc73aefc29b | -5.9387 | -59.97926 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4f2bd452-8661-388a-85e1-887a1c72675f | -7.57536 | -57.68131 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fae4d3a0-128d-322e-8018-320bf8bd9ed3 | -11.68027 | -50.98296 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23d9c5ec-25f8-3e05-b675-58c99b369e70 | -7.62355 | -57.61403 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 174885e3-ce17-34bf-9b87-307d29523b43 | -12.84164 | -50.98899 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd288e74-15f6-3e5b-807d-a23430e00158 | -6.73721 | -55.08836 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efd55041-43a7-34d0-9656-aa7e3535bb4a | -5.21192 | -56.07745 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59a8ad2c-b947-3f86-9fb0-ff3d57ed2eb9 | -3.10861 | -60.72013 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7fb33fd1-710c-360d-9bc4-379a67566b07 | -3.68357 | -60.62712 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76236eb5-0e24-3239-b297-ab3809e868e8 | -12.79701 | -54.03959 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1efabaf-185b-3b6d-bda4-af91e13712e1 | -6.11998 | -57.83848 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a858c10b-2ba1-30da-bab2-d8209cdb567b | -6.49929 | -58.38178 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19e5a028-356c-352b-ad55-26421265596e | -3.36024 | -50.76315 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36bb438b-ead4-333e-b81b-33b3fb88abfa | -3.30173 | -57.86071 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe5eb6f4-85fc-3c8b-bcff-1e31baeadde7 | -12.85343 | -54.04255 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfed0842-4d93-3274-9a53-ad77b88e98d5 | -9.28776 | -46.18729 | 2026-09-22 05:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6ff1983-d8c2-3a96-acff-d211a8925f58 | -11.32873 | -51.36422 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e88b8c6-8327-3162-8c5d-ca523734f38a | -3.22577 | -61.05449 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 98456d5a-6606-3e69-bc36-deb3efd858e4 | -7.56641 | -57.68016 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 728ab65b-c0e9-307e-8877-8aa25f6e2fc2 | -3.68562 | -60.56709 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d47c988-7f4a-3d62-9327-faa5b89775da | -4.64674 | -50.99306 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8f1741f5-3903-3f68-bf54-7e5874765cf5 | -7.88345 | -54.72796 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94e09120-b72e-38fa-98d6-f55f56fc2168 | -6.28353 | -57.74277 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bd5784b7-da15-3b8b-a69c-b17c5bd19059 | -6.84155 | -55.53901 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3940dafa-2e7e-3acb-b25a-6880939d7729 | -5.45277 | -49.01619 | 2026-09-22 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87128f53-0620-3a69-94c0-a523eebbf920 | -3.07272 | -54.39159 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e37c1d0-bb13-3ba8-8218-1392d6b8cba2 | -1.45613 | -54.23894 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac1eb383-23dd-3de4-8c9e-d683db6d1059 | -5.82127 | -57.74063 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e4a81fe-db08-3653-a4bf-29d655dfd0c2 | -2.80197 | -57.66591 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c01bcd7-a9a4-3276-ba6e-f027b69f775b | -5.85247 | -52.02958 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ad8e940-4755-3dc7-80f3-7cb99fc47e96 | -3.69967 | -57.29385 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3754dc1-c3ed-3ce7-af6f-97e9672310f2 | -4.64241 | -50.99249 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9914f025-8157-3051-bcc9-2ee2765c51fb | -11.68432 | -50.98609 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f0011042-e040-3f5d-ba9f-99b225dcbc02 | -7.13973 | -48.43894 | 2026-09-22 05:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5fb46f0-f199-36d3-bced-b493d991d3ea | -3.00801 | -54.18233 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8e689c9-8156-3f5d-a080-abcd1f6e4cdc | -3.9281 | -56.04735 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fe1cc02-1f8b-36f1-8509-fdf4e894f8fe | -4.21017 | -59.91236 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a26fc8f-c796-3e00-b909-1f4b98a739cc | -7.23843 | -55.59525 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce40d11a-2746-37c3-852d-7ead12eb6bf8 | -5.82977 | -52.05194 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afd040a4-ecbb-38a2-8dc4-7475b5c6125a | -3.34128 | -59.86356 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65620deb-fce8-33b3-8745-b89f9069b727 | -6.10054 | -57.68172 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| fcb9c1f6-3774-30db-a15b-d2a7a9acbafa | -5.84763 | -53.54647 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a7bb2c2-c609-3281-8990-ead5c270dd5b | -8.31602 | -44.74312 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d0e08112-4cf7-3eb2-8eef-5b101cc5c4d1 | -4.96955 | -55.82563 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6092bc2-b291-3e29-a73b-115d9c567560 | -5.86935 | -52.02886 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b8fb83c-e59d-3205-9109-542cb5d43ec4 | -3.32702 | -59.81421 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dedccb1f-ea96-3556-ac1d-05d18fd11a22 | -5.85723 | -57.55003 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b69a73b-d5d5-36e8-9a13-dfcff50f270e | -6.75112 | -59.06773 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9940e77d-b9c5-35ae-b08d-24b3b9e127e1 | -4.79372 | -56.12472 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 624e26b7-ab63-3ea4-9635-03297720e139 | -13.36448 | -51.30732 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a831159-0edf-3de3-8891-f8b1249feb7d | -6.92069 | -59.9135 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbad6da2-878d-358d-b73b-3c6665047177 | -5.0116 | -56.09335 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67da1ec7-bcf3-3321-91a5-ab47319dd3f3 | -10.4279 | -57.22419 | 2026-09-22 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 719a668e-964f-3bff-a39a-2cb002ba0458 | -1.32967 | -54.66461 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 17a69f70-0381-32eb-b720-281520f8dc59 | -5.80849 | -57.73502 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057029fd-65bb-347c-8db4-ef6bb62c4a52 | -6.03883 | -53.27627 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fe29483-b374-3bcb-9f2f-eb2e5b5c77c5 | -3.92238 | -60.55959 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d6e39233-937c-329b-a3bc-39cdb19b4517 | -4.28289 | -56.26011 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5326efd4-d238-367b-9617-287b8f84ce2c | -11.32231 | -54.05059 | 2026-09-22 05:23:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d21853b-921c-3feb-8edf-bed63d582add | -12.79231 | -54.04416 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76906a07-a91e-30d4-9e21-167287959aab | -5.89664 | -52.09877 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af7246ea-30d1-3aba-9d86-377e6b8855bb | -6.38978 | -60.0248 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a28fd188-3c09-3632-867f-9cb3ef6c081e | -3.44566 | -50.60881 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79523be6-1866-3edf-855c-92d234f2229e | -4.34739 | -55.65322 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README80.md)
