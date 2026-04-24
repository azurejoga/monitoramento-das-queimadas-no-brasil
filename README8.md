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
| d2ff1f38-175e-3a55-9b91-e0a10352edf5 | -13.37 | -43.20299 | 2026-04-24 11:45:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 95465d91-c59e-3cc9-8f75-4d636f87bf15 | -13.37 | -43.20298 | 2026-04-24 11:45:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| c438d5b7-bdf2-3cb7-8d5c-eef7bb0a5923 | -21.18964 | -46.96548 | 2026-04-24 11:45:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e7b93223-6395-350b-909e-837ad9908c85 | -11.97157 | -43.84118 | 2026-04-24 11:45:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d682ff58-592c-3c78-a6e8-b9b93ea7f511 | -11.97157 | -43.8412 | 2026-04-24 11:45:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5a49214d-6678-31d9-a40e-ce1b7edbd409 | -13.38246 | -45.30342 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 51bb94ba-6fe6-3654-bb0f-6bed352eddf5 | -13.52857 | -42.99109 | 2026-04-24 11:45:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 58b00a63-224f-3589-9f5e-190f27a8039d | -17.60226 | -44.61637 | 2026-04-24 11:45:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ee67d618-eeb4-317f-bc14-a8bab1b1f311 | -13.38246 | -45.30343 | 2026-04-24 11:45:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 4c898ce5-488c-3b18-b6d0-1110e6e62dce | -13.00733 | -42.56523 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ddb30aa1-9a35-30fa-a784-747220c31191 | -12.99823 | -42.56396 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 12a38071-628a-3524-8031-ff2662e82f62 | -17.60225 | -44.61639 | 2026-04-24 11:45:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 80f3ebde-f72a-3ad5-af95-bd8b644837f2 | -13.00601 | -42.57481 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f640fc3a-c139-3b69-a45c-dfdf79eb3014 | -18.30567 | -52.90311 | 2026-04-24 11:45:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| cf67f160-f5c3-3389-a12c-d4f26185c4b4 | -15.9308 | -43.73006 | 2026-04-24 11:45:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d40d3357-cf37-32aa-aa76-2da43d78b7b5 | -12.99691 | -42.57356 | 2026-04-24 11:45:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 533ab80d-01db-326e-8fa3-b8e8b73b2862 | -21.18964 | -46.96546 | 2026-04-24 11:45:00 | TERRA_M-M | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40735892-ea2c-3565-8a28-33e9f68cd847 | -18.30567 | -52.9031 | 2026-04-24 11:45:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| e5cfa369-c79d-32a9-a4f8-4e242ad30d0f | -18.2783 | -52.89791 | 2026-04-24 11:45:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 126.2 |
| bcd61ddd-78b0-3158-b4d7-2b6d430808a6 | -18.3013 | -52.92725 | 2026-04-24 11:45:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c18f8dd8-491e-333c-9bfa-be18a387778a | -20.20546 | -46.88226 | 2026-04-24 11:45:00 | TERRA_M-M | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eaab1040-c4cb-38bb-8184-3069a93feb9c | -21.02344 | -45.57309 | 2026-04-24 11:45:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 07271e3a-fca4-3aae-81da-d1c25fbe3f33 | -19.16377 | -40.44547 | 2026-04-24 11:45:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 4f06b41a-4c79-3c92-bfd2-257a4eee3306 | -21.0323 | -45.57448 | 2026-04-24 11:45:00 | TERRA_M-M | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1c01a81a-f7d5-39d9-bd9b-3ec5e0d976d2 | -19.16306 | -40.45187 | 2026-04-24 11:45:00 | TERRA_M-M | GOVERNADOR LINDENBERG | ESPÍRITO SANTO | Brasil | 3202256 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 902bce62-79b5-3651-9bda-f29b0d9b54c8 | -22.83174 | -46.3329 | 2026-04-24 11:47:00 | TERRA_M-M | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 9c5f7d52-00c9-37ba-b6ff-87e96f248133 | -22.83682 | -49.30117 | 2026-04-24 11:47:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8d71317c-af2a-32d4-be38-b9c2ee37a113 | -22.83872 | -49.28961 | 2026-04-24 11:47:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d663eae2-ba57-300d-8829-c1c6234f5f71 | -22.83872 | -49.28959 | 2026-04-24 11:47:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4a1b5860-8571-3bd0-8727-79e214b483a8 | -22.83682 | -49.30115 | 2026-04-24 11:47:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 94d5e9ce-712a-3f21-a129-afae55364167 | -22.83174 | -46.33289 | 2026-04-24 11:47:00 | TERRA_M-M | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 75085fe8-3dc1-388d-b045-f8333d3e881e | -13.3766 | -45.301 | 2026-04-24 11:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 51982de8-fe06-3b14-88b6-401963b076ac | -13.3766 | -45.301 | 2026-04-24 12:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 5c56782f-1987-328a-bbac-cc15e58a77d2 | -13.3766 | -45.301 | 2026-04-24 12:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 7632ad96-ec43-356a-838b-f75ec1e2bd51 | -18.3053 | -52.9167 | 2026-04-24 12:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 55d83b23-009b-3274-bf98-208816ce82d2 | -18.2858 | -52.8983 | 2026-04-24 12:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 7b9f8afd-a7cf-38f7-93b3-a12f719e0618 | -13.3766 | -45.301 | 2026-04-24 12:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| 2d957463-dbb5-3f24-8286-0f4347283d56 | -18.3053 | -52.9167 | 2026-04-24 12:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 113.2 |
| b5a45358-db29-3d5b-8b91-4f7184ef159c | -18.2858 | -52.8983 | 2026-04-24 12:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3a89f6f5-9ddd-3fa8-ab55-7fc409dbf6da | -13.3766 | -45.301 | 2026-04-24 12:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 18b96a2a-9384-3f8a-81e4-e70439b9c1d7 | -13.3766 | -45.301 | 2026-04-24 12:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 5d1de3d3-2957-3ad3-bbb0-3550bc385ec2 | -18.2854 | -52.92 | 2026-04-24 12:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c5e7f9d7-d08b-381c-a53f-6e6703dead88 | -18.2858 | -52.8983 | 2026-04-24 12:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 63d98e16-10b6-3fb6-80e2-a59c39b04dd6 | -18.3058 | -52.8951 | 2026-04-24 12:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 126.3 |
| 02815161-b913-3c9c-a1bf-4f7d71261deb | -18.3053 | -52.9167 | 2026-04-24 12:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 211.9 |
| 4feec6c7-7961-3487-b6ba-22cf02e1b9dc | -18.2854 | -52.92 | 2026-04-24 12:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 80f0066e-5070-3edb-aa1a-0ac03ac4c8b8 | -13.3766 | -45.301 | 2026-04-24 12:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 14c2e943-fd1c-3d84-90cf-4663b8bf2852 | -18.2858 | -52.8983 | 2026-04-24 12:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 198.7 |
| cca6412b-0293-36eb-a64c-1761a72b0d11 | -18.3053 | -52.9167 | 2026-04-24 12:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 280.0 |
| 45bfea62-f08d-334a-b0b3-4dd8f51adc24 | -13.3766 | -45.301 | 2026-04-24 13:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 90bac099-e8bf-3b17-8804-5b153a48c846 | -18.3058 | -52.8951 | 2026-04-24 13:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 053cec44-ee05-3475-b146-1677a5167287 | -18.3053 | -52.9167 | 2026-04-24 13:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 247.1 |
| 17dfd3ef-0bf2-3de9-a8fa-94ef0329e20f | -18.2858 | -52.8983 | 2026-04-24 13:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 5edb04f4-ec36-3246-9fd7-e8cf87e0134e | -18.2854 | -52.92 | 2026-04-24 13:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 2f6d48cf-95db-3a4e-950c-f085f1ecb807 | -18.3048 | -52.9384 | 2026-04-24 13:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 5eecb30c-7cab-35bf-85f1-4b1e75284bc9 | -18.3053 | -52.9167 | 2026-04-24 13:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 266.8 |
| c00c8769-64b4-3aaf-8d3d-96e831212be2 | -18.2854 | -52.92 | 2026-04-24 13:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 5701d31d-ac1a-3791-9c16-ba2ba963eb76 | -18.2858 | -52.8983 | 2026-04-24 13:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 424.8 |
| 33bfdc6e-757e-3ff3-ba76-d41bcb8a7b8a | -18.3048 | -52.9384 | 2026-04-24 13:10:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3e3567e9-90a2-3128-8162-5902dc28ee60 | -22.996 | -53.0003 | 2026-04-24 13:10:00 | GOES-19 | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 81.9 |
| 582206f0-6cd7-3e39-8335-588d322f542d | -18.2863 | -52.8767 | 2026-04-24 13:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| c0e4dea8-3e71-34e9-9064-8efd96c25e52 | -13.3766 | -45.301 | 2026-04-24 13:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 2db9f43a-a80f-3ac7-9adb-c061d82cc860 | -18.2659 | -52.9016 | 2026-04-24 13:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 68.8 |
| d95e723f-645f-336e-a638-c79e8ba1fd65 | -22.996 | -53.0003 | 2026-04-24 13:20:00 | GOES-19 | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| a0363ca8-db95-3339-8a2b-b6f1d60bca57 | -18.2854 | -52.92 | 2026-04-24 13:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 03a701ba-771e-3c30-9126-8c019cc2c264 | -22.996 | -53.0003 | 2026-04-24 13:30:00 | GOES-19 | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 108.4 |
| bb9e5242-dc5b-3b93-ac79-610bf09351ef | -18.2858 | -52.8983 | 2026-04-24 13:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 193.5 |
| f269fb3b-ea2e-3841-8523-17ac5d2c2d2a | -18.3053 | -52.9167 | 2026-04-24 13:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 480.1 |
| d26e761d-6036-352d-a6ac-9c0343b07d1c | -18.2854 | -52.92 | 2026-04-24 13:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 2c996ffb-618c-396b-bab8-349b094f3077 | -18.2858 | -52.8983 | 2026-04-24 13:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 405.5 |
| 25f8e756-b6b4-3d13-ba1a-492d19e8711d | -18.3053 | -52.9167 | 2026-04-24 13:40:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 415.5 |
| 2cd1d5b0-7b3e-3197-88fa-c95ec16a9497 | -18.2863 | -52.8767 | 2026-04-24 13:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 69e99ede-e8e9-3578-bdbc-cbfca87329d3 | -22.996 | -53.0003 | 2026-04-24 13:40:00 | GOES-19 | LOANDA | PARANÁ | Brasil | 4113502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 7b75e706-5eef-31b9-ba13-4887c34e57cf | -18.2854 | -52.92 | 2026-04-24 13:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 237b0cb1-bcd7-3ead-a4a5-f17e754c9f36 | -18.3053 | -52.9167 | 2026-04-24 13:50:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 235.2 |
| 28c92aa4-46f8-3ec9-a970-4119989bf211 | -18.2863 | -52.8767 | 2026-04-24 13:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 35374398-9320-3ed3-9906-18e3dd2482db | -18.2858 | -52.8983 | 2026-04-24 13:50:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 330.8 |
| b0317dc3-7f81-3b8f-a8b1-8ec5fb8e3418 | -18.3053 | -52.9167 | 2026-04-24 14:00:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 235.4 |
| f828b769-9319-31c0-8201-0dd215175eae | -18.2854 | -52.92 | 2026-04-24 14:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| abf01d9a-c789-3c1b-8f43-6b5140fcc915 | -18.2858 | -52.8983 | 2026-04-24 14:00:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 166.9 |
| d82ba117-d6d5-367c-8fef-eaef58d9dfef | -18.512 | -55.5022 | 2026-04-24 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| dfee70e4-1df5-3fd8-9a66-38f020199429 | -18.2863 | -52.8767 | 2026-04-24 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 8d4bee24-0197-364a-9da1-94c64296f0fb | -18.2854 | -52.92 | 2026-04-24 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 914e030e-33b8-31fd-8d0f-ff097e368ef3 | -18.2858 | -52.8983 | 2026-04-24 14:10:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 163.4 |
| 3d717406-9cff-33de-b553-79b2e257141d | -18.2858 | -52.8983 | 2026-04-24 14:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 390.8 |
| dc4a4f13-165b-3cbe-b49c-8ba10f0980eb | -18.3053 | -52.9167 | 2026-04-24 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 95.4 |
| ae36dc52-2519-3f11-9e91-ed9b3857f0bb | -18.512 | -55.5022 | 2026-04-24 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 0c003225-d5c8-3fe6-b18a-21c2586e7dce | -18.2854 | -52.92 | 2026-04-24 14:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c3127f5c-8213-3c85-b6f7-db34e8977e9d | -12.3095 | -57.1808 | 2026-04-24 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 38e5ced1-7659-3f2b-8b33-8826c7b61f27 | -18.512 | -55.5022 | 2026-04-24 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| a4a1cc4e-7a64-3b53-8b6e-a1db38bcc654 | -18.3053 | -52.9167 | 2026-04-24 14:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 11b9021d-eff8-38c3-bd0b-b2148ca0e025 | -18.2858 | -52.8983 | 2026-04-24 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 72dcfadf-6fa5-3211-b769-3bafec71c960 | -18.3058 | -52.8951 | 2026-04-24 14:30:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 259.7 |
| a6a409ac-0432-35e8-a91c-66c9cfbf97bb | -18.2858 | -52.8983 | 2026-04-24 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 41df710d-247a-390c-a5ed-2f38268b48d4 | -12.2905 | -57.1824 | 2026-04-24 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 147db2cd-11a5-3634-8562-81e39728b78c | -18.2863 | -52.8767 | 2026-04-24 14:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| edcaf550-1327-39a8-b854-ed5db59bb0b1 | -12.3095 | -57.1808 | 2026-04-24 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 189bf617-8f8d-33f3-ab0b-ad9ad4775584 | -18.512 | -55.5022 | 2026-04-24 14:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |


