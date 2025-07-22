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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d32256f-8881-3f3e-b32e-45480c8876ae | -8.6815 | -46.9405 | 2025-07-22 12:40:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 868a9bfe-3c4e-304f-a02d-7b31bbac5ae5 | -6.9804 | -42.7854 | 2025-07-22 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 114.9 |
| 2967ae55-be29-3a12-badd-11cdfb88998e | -6.9801 | -42.809 | 2025-07-22 12:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| 1302f731-16cb-37a7-b5f9-28be00efaa6d | -9.40422 | -48.00812 | 2025-07-22 12:49:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| c3ba4b29-5b90-3257-93f9-418de7621111 | -8.09687 | -46.27443 | 2025-07-22 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 277d36a6-6034-34b7-91f9-96fc7ee4fa0e | -3.17767 | -49.44127 | 2025-07-22 12:49:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9053922a-456e-3bd4-9efc-3eb6cafe9e88 | -8.68721 | -46.93914 | 2025-07-22 12:49:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 1825789f-21d9-32bb-9d42-97e01a83ff78 | -6.39187 | -44.8587 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 40fb125e-94db-3a19-bdea-49a7de12c042 | -6.39641 | -44.85382 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.5 |
| ef9c9cb5-7d5b-349a-b5ff-ffde67c0dc3d | -7.02616 | -45.85867 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| de20baee-4b9c-3be8-b35e-9f311fdcbbdb | -8.10441 | -46.8245 | 2025-07-22 12:49:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 820a3706-e274-35ba-ba5c-08f8522d2cda | -6.57175 | -45.61071 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 438f2238-f370-3d9c-9ae9-a3bfc6233528 | -7.04064 | -45.86092 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 358.6 |
| 80be4bcd-6abb-3ea4-b6d7-21486008cff6 | -6.79749 | -45.62232 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 693478c7-57b1-3abc-8480-2f940e4ba048 | -8.82338 | -44.52895 | 2025-07-22 12:49:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| e6fcd9a4-be81-3d98-b21c-fb7fa44fdf96 | -7.23785 | -44.75779 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 7fb7c870-bf20-3e64-b3ef-efa566ff8966 | -8.08525 | -50.08257 | 2025-07-22 12:49:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 9d8cbaff-e3a6-33ef-91a3-c02149576a74 | -7.02948 | -45.83224 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 1b5b42d4-040a-34d3-b895-2c0fb042c937 | -6.67111 | -45.65166 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 8ec89796-9f3f-3ee5-920c-b395690e4c7b | -2.46258 | -47.73741 | 2025-07-22 12:49:00 | TERRA_M-T | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 3504c45b-faa8-3a00-ba43-5b5b68501d3a | -8.68029 | -46.93237 | 2025-07-22 12:49:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| d39acec2-f3d4-3dc0-af1c-7bf910ab9b6c | -8.67735 | -46.95521 | 2025-07-22 12:49:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| ccb0db7d-04b0-3496-a05d-bb4912c2796c | -7.04399 | -45.83453 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 309.2 |
| 13c101cc-66ba-357b-9714-4757f0bb921e | -6.56791 | -45.63028 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 30.1 |
| caf6712d-9b47-3f5c-a9bd-70dc35b31c03 | -8.09992 | -46.28148 | 2025-07-22 12:49:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 5ad422a2-c174-34e2-ba19-3c48ccfb1559 | -6.66751 | -45.67876 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| f93da16e-a0aa-34f7-9117-415908bf2b08 | -7.28276 | -60.17386 | 2025-07-22 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e00766a3-ddb2-3dce-8756-bd4830df8eeb | -6.79392 | -45.65041 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 2ed82ba2-01ad-3c49-97c9-61294fd21e3d | -8.67359 | -46.93689 | 2025-07-22 12:49:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| b60da972-2091-3879-b199-8cc43700a21b | -6.11293 | -47.78717 | 2025-07-22 12:49:00 | TERRA_M-T | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d86e7f01-595e-35b4-9504-a328ae18ed05 | -7.23389 | -44.79033 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| e60f9dfe-e5e2-3f47-80f6-bc998268f902 | -6.67253 | -45.65722 | 2025-07-22 12:49:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 38998c82-dd5e-3951-a2cf-b5e20939ab29 | -7.24047 | -44.78406 | 2025-07-22 12:49:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a5311ad5-fd98-38e4-b9a1-5b0de6231118 | -7.97621 | -55.30109 | 2025-07-22 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9ee066d6-90a2-3c41-82db-160bd23236d9 | -6.9804 | -42.7854 | 2025-07-22 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| f844863a-660f-3a30-b48a-e1b09317fa75 | -6.6682 | -45.6697 | 2025-07-22 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f1987fb1-34ab-3155-90ad-417378ba0d94 | -6.9801 | -42.809 | 2025-07-22 12:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 110.1 |
| 669b909e-7c8c-3458-84b8-80e5cab5be17 | -17.57467 | -47.5022 | 2025-07-22 12:51:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 70d83425-573c-39cc-a5ef-ec3a21fba2ce | -11.86699 | -44.48743 | 2025-07-22 12:51:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 064ad972-0d80-3699-8e09-cd950b35ca28 | -10.55716 | -50.38354 | 2025-07-22 12:51:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 3a099fad-0cfa-3653-ab33-5a022845bd88 | -14.19482 | -45.33105 | 2025-07-22 12:51:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3e9d4a8b-1eae-338a-80b3-e4d27cd391d0 | -12.49994 | -57.77758 | 2025-07-22 12:51:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bc80f66c-322a-3dd1-8a92-f650d705d3be | -11.30865 | -55.11348 | 2025-07-22 12:51:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 89bba38b-9c8f-3390-8ea7-dc4261c46233 | -16.21066 | -48.60435 | 2025-07-22 12:51:00 | TERRA_M-T | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5ca70867-81df-3251-8daf-c696f7028fa5 | -11.86058 | -44.52278 | 2025-07-22 12:51:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 0af8abbc-a706-37c2-abd9-de821c09f7ba | -15.02106 | -49.25272 | 2025-07-22 12:51:00 | TERRA_M-T | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 4810327c-484d-37c4-9d48-6ca8d1927cd4 | -17.55973 | -47.50054 | 2025-07-22 12:51:00 | TERRA_M-T | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 51f23913-b32c-3d75-b14e-87cefc9250b4 | -15.35578 | -47.05252 | 2025-07-22 12:51:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 728caa23-3659-3d9f-ad1c-ff5819c51d74 | -14.19927 | -45.33857 | 2025-07-22 12:51:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 169aeda9-030e-3b67-82cf-83486a9dc80e | -12.28987 | -50.28334 | 2025-07-22 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7c3673fa-d82d-3923-a4a3-32642d79f3bf | -10.82134 | -49.56518 | 2025-07-22 12:51:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6ff1b689-a30c-38ac-ac1a-2cbc5177433e | -12.28892 | -50.27726 | 2025-07-22 12:51:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cc15a0f0-8086-342e-9240-f80ca9094298 | -12.58386 | -56.97375 | 2025-07-22 12:51:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 2d1821ca-4a7d-3561-a4a8-0707029d55f1 | -14.68728 | -52.68363 | 2025-07-22 12:51:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 23d523c3-afac-3080-b729-d11c3bc6cc33 | -12.50159 | -57.76682 | 2025-07-22 12:51:00 | TERRA_M-T | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 334afee9-8717-38fa-a331-9d11aa5c202a | -12.29061 | -54.95346 | 2025-07-22 12:51:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 00a9757f-720b-3d02-86e8-d112497e80d9 | -11.86278 | -44.52794 | 2025-07-22 12:51:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5549919a-4aef-3515-8294-bae28a4a4cc0 | -11.37903 | -50.66698 | 2025-07-22 12:51:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4a777dfa-7a5e-397b-aaef-77b2d3e3a06a | -18.60707 | -51.8028 | 2025-07-22 12:53:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 35.0 |
| f4e5ba5a-a894-3ff4-bc06-fb9e1d7cea98 | -21.69083 | -57.38624 | 2025-07-22 12:53:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 21f454de-9774-31e6-a6e4-a847973bc851 | -18.68791 | -47.53786 | 2025-07-22 12:53:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 27.7 |
| f1b08793-8e6c-3731-af48-24052fca6e8d | -18.60541 | -51.81705 | 2025-07-22 12:53:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e02c2e03-d851-3c74-ae87-c00c4f8496d0 | -21.6434 | -53.48358 | 2025-07-22 12:53:00 | TERRA_M-T | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a2bdda55-eb7f-3c75-b7f5-7c62412546f4 | -18.08947 | -54.28446 | 2025-07-22 12:53:00 | TERRA_M-T | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c397f99-e010-3e1f-8502-dd78493e5c4a | -21.68945 | -57.39573 | 2025-07-22 12:53:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 4ee4999d-6a62-3a4e-a597-3578f209a33f | -18.68598 | -47.54436 | 2025-07-22 12:53:00 | TERRA_M-T | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 520e81d0-50c5-3128-b15d-4319b4469293 | -21.59334 | -57.60721 | 2025-07-22 12:53:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d8a820f7-0df6-378e-acbe-94f1f0858d98 | -19.55214 | -56.92989 | 2025-07-22 12:53:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 34929a14-4cba-3752-9382-4370504580c7 | -21.59474 | -57.59767 | 2025-07-22 12:53:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 5429fa52-2ee4-3c4b-b998-a133fef9dcec | -18.5195 | -56.41705 | 2025-07-22 12:53:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 54944862-7fec-3bf0-9e31-3f32405bd86f | -21.64191 | -53.49589 | 2025-07-22 12:53:00 | TERRA_M-T | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dc74e42e-182c-3731-b3b0-3e997b75fc9d | -18.60276 | -51.81029 | 2025-07-22 12:53:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 3d6cb1d1-6c4c-36b1-821b-452401c11a2c | -19.79404 | -55.35231 | 2025-07-22 12:53:00 | TERRA_M-T | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a597e03a-4d2e-3d59-9d20-deb2ea6e255f | -19.79538 | -55.34262 | 2025-07-22 12:53:00 | TERRA_M-T | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8fdffe8f-5818-3e6b-8196-e28c9462f38d | -21.63586 | -53.54549 | 2025-07-22 12:53:00 | TERRA_M-T | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ab991d36-1280-36e0-bb12-85f94409eb7f | -18.6045 | -51.79613 | 2025-07-22 12:53:00 | TERRA_M-T | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 82c38292-1454-39fe-8c7f-20c44fc33272 | -22.31136 | -53.17089 | 2025-07-22 12:53:00 | TERRA_M-T | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 1f0a9e76-fa88-391e-a5ed-7dc1eb609909 | -21.42852 | -54.15955 | 2025-07-22 12:53:00 | TERRA_M-T | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c1e67f29-baed-34f3-86e3-6cbfcdedc6c2 | -6.9804 | -42.7854 | 2025-07-22 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 127.5 |
| 98e0814b-22cc-316f-a64e-51e480fbff71 | -11.871 | -44.5189 | 2025-07-22 13:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| cb7471fb-b2ed-3d05-a679-2ef1088b4b4f | -6.6682 | -45.6697 | 2025-07-22 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6c96774a-6a95-3468-98d0-97d6e2fde0e0 | -6.9801 | -42.809 | 2025-07-22 13:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 131.7 |
| b71e0343-ba01-3ce1-9a89-2089dd76b5c1 | -6.6682 | -45.6697 | 2025-07-22 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 3cbb1acd-01fb-3175-9abd-d02ba8a64d9f | -6.9804 | -42.7854 | 2025-07-22 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 167.3 |
| bf00cc06-d43f-3fbd-a084-0d50be12d0bb | -6.9615 | -42.7872 | 2025-07-22 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 3e49e20c-67d4-3fa2-b159-f6e0761405aa | -11.871 | -44.5189 | 2025-07-22 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 40b4f5d0-2bda-30e0-8b72-f998d3af47c2 | -6.9801 | -42.809 | 2025-07-22 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 126.9 |
| 28ff8c04-ff0f-374e-952c-645e3be2fae8 | -6.9804 | -42.7854 | 2025-07-22 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 191.1 |
| aabb1466-7e8a-3662-a311-2ffae88ec3c7 | -6.9801 | -42.809 | 2025-07-22 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 132.3 |
| 7b9a99aa-eb81-35d7-9851-8955398ab64e | -6.6682 | -45.6697 | 2025-07-22 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 6511a0e4-eda0-3fb4-bd9f-c593e5c3707f | -11.871 | -44.5189 | 2025-07-22 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 152e2a99-a7bb-37af-9137-93311b320a1b | -6.6684 | -45.6472 | 2025-07-22 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 193.5 |
| 6457811d-34a6-3da4-a643-20834224663f | -11.871 | -44.5189 | 2025-07-22 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 134.8 |
| d6d66992-b047-345d-add9-e033f9219614 | -6.6682 | -45.6697 | 2025-07-22 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 346.8 |
| a0f5e253-aea4-3a90-ae52-b4db39b80a4a | -6.9804 | -42.7854 | 2025-07-22 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 187.6 |
| 266a6cf9-3d5a-342f-9994-4c5f461f2718 | -17.5748 | -47.4996 | 2025-07-22 13:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 29f56280-ae83-3a4c-bfe6-4c38b90cba74 | -6.6684 | -45.6472 | 2025-07-22 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 220.1 |
| 93dabf51-f486-3e75-b3ea-6949786f0ced | -6.9801 | -42.809 | 2025-07-22 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 149.6 |
| d6c22d2c-8f68-3c36-883b-c7a3a5257b95 | -17.5748 | -47.4996 | 2025-07-22 13:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 119.7 |
| 0ad16edf-4e8e-3058-9828-52a0fafb7b67 | -6.6684 | -45.6472 | 2025-07-22 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |


[Clique aqui para ver as próximas entradas](README22.md)
