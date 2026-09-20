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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5f54032-7297-3f81-83e3-34642ec76fd5 | -2.9157 | -57.7983 | 2026-09-20 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b33af6d2-211a-32ff-8508-d5ef1dfb6f1e | -7.5703 | -57.6962 | 2026-09-20 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e4783c2d-7641-3447-9758-bd2e0d1b6e98 | -10.3914 | -48.9133 | 2026-09-20 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 16a5758f-91bd-3187-a8ce-190edfe16b07 | -11.8487 | -46.8781 | 2026-09-20 14:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 38dfa3a8-195f-39fd-95a8-ac773116b76d | -12.1516 | -47.0608 | 2026-09-20 14:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| b3107e1c-38bc-3e0f-b674-0697cca5a20c | -6.3199 | -59.9381 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 1c168317-0fff-3938-9828-c96c013c4c9c | -10.8672 | -56.1775 | 2026-09-20 14:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 46274f0d-0034-3c0a-87f0-156211f8b7d2 | -11.75 | -50.6993 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 315.3 |
| 32e908e7-7733-3f65-8d97-f01075288e4f | -9.84 | -46.4136 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 249.2 |
| e2a5f837-32f2-3637-ad2d-3111f65df701 | -11.3809 | -44.0788 | 2026-09-20 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 218.7 |
| d0c7bba1-0c90-3c31-b180-88b15b08b727 | -9.0428 | -48.1603 | 2026-09-20 14:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ccdbc807-1afb-363e-8f94-1704ec71c59a | -13.5911 | -51.458 | 2026-09-20 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.0 |
| ca7f9708-340c-33d9-adab-270b4cb19cf5 | -2.9157 | -57.8177 | 2026-09-20 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| b11e89d8-1f9b-303f-9178-6c1149018731 | -12.5081 | -50.952 | 2026-09-20 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 02bc2f31-869a-3b00-aa9b-9579074ddcb0 | -11.0256 | -48.3164 | 2026-09-20 14:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 71839db2-04f7-3032-a892-9f26c1b8fbce | -7.3376 | -44.4744 | 2026-09-20 14:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 07cfc966-4f74-30ca-b7fb-e3ef900710bd | -11.4545 | -45.3432 | 2026-09-20 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| ef088355-556c-3cd9-a5d7-bd6bec61b927 | -8.1686 | -54.7634 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 136.4 |
| 7f1ea699-a0ff-33eb-b43c-5feae7e3e63e | -8.0279 | -61.3626 | 2026-09-20 14:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| dec24bfe-dd65-3f18-a945-34887c7d5c57 | -12.7621 | -46.18 | 2026-09-20 14:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 3fbb8b87-67d2-35ea-8862-1964ad87881d | -6.4485 | -59.9909 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 264.7 |
| 7b7359e1-d286-3655-b2ce-3db6c2fe0b71 | -8.7733 | -44.2336 | 2026-09-20 14:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 47ee6f2d-afb3-396c-9dfc-d086550f6398 | -12.0079 | -50.0038 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 2d7a37d5-a01b-3e70-a13c-8f9a2e40d272 | -3.5894 | -59.0581 | 2026-09-20 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 40064949-b42a-3e4b-8d7e-8116274cabd3 | -9.8502 | -48.4053 | 2026-09-20 14:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 5ff34a2f-06f5-3852-9af0-01d36a24bdf5 | -11.4001 | -44.076 | 2026-09-20 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| cb6ff8e2-778e-33c1-a981-9f482c3d0d00 | -11.041 | -54.1567 | 2026-09-20 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 245.7 |
| 59ac5c30-279a-3136-b814-006680c4c086 | -11.1222 | -49.4818 | 2026-09-20 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 742ee7f7-a343-3f69-992a-593099407f3d | -10.9665 | -49.7583 | 2026-09-20 14:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| e7aada4e-99e3-3bad-8783-37d724c1c35e | -11.6621 | -50.2169 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 615d83b5-ef79-395c-9238-e5179157837f | -11.6798 | -54.446 | 2026-09-20 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| a61f2ce8-5236-33b5-b985-527241e87d83 | -12.0649 | -50.0185 | 2026-09-20 14:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| d610a7dc-6ffe-3bfa-9ec8-7b44c3fbf88f | -6.9171 | -41.7198 | 2026-09-20 14:50:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 102.3 |
| f6240a93-4b70-3b4a-968e-2630b8e8fc18 | -10.9694 | -57.1881 | 2026-09-20 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| d0e6104c-3c9f-3789-bd99-88462b10502f | -11.3793 | -51.3989 | 2026-09-20 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 161.7 |
| b61b3f1d-a4b6-3816-8c16-3ac440b8c83d | -10.4103 | -48.9112 | 2026-09-20 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 277615f5-423f-332f-a419-eeb2f2748ae4 | -5.7615 | -57.5807 | 2026-09-20 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 5d8644c8-2b63-3f5e-9138-add44fbcba9c | -9.5539 | -46.5807 | 2026-09-20 14:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 126.6 |
| 4b4924d0-966a-3239-953a-e43a94e564aa | -3.3641 | -42.7589 | 2026-09-20 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 23ef3f90-49af-31fe-b384-b4177d869515 | -10.8757 | -57.1554 | 2026-09-20 14:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 878ed86c-5294-3713-9c8b-433ca424db1b | -3.3494 | -59.8097 | 2026-09-20 14:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 11b4db43-ee59-3428-b659-241b6672036f | -8.4549 | -47.0072 | 2026-09-20 14:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c1858a24-55ad-3def-8270-7c002bfaff0f | -11.0617 | -49.7261 | 2026-09-20 14:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 7b253fd9-10f7-32e0-b79d-1e54b8610c44 | -10.8367 | -50.9266 | 2026-09-20 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 283.3 |
| ba75ffa0-88b6-3e11-ab22-061f07ee0953 | -10.8177 | -50.9286 | 2026-09-20 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 121.4 |
| c5ecc5ce-dfa9-377a-b5f2-d17405e26671 | -3.5356 | -58.6939 | 2026-09-20 14:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f8bbf7c7-55f1-32c5-a0e0-93c735962e4d | -11.379 | -51.42 | 2026-09-20 14:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 241.2 |
| 46479e53-91de-37d8-8a24-94d0cbdb668a | -3.5893 | -59.0773 | 2026-09-20 14:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c5556142-e44d-31ba-bc2e-84f3b7335deb | -6.8215 | -59.1879 | 2026-09-20 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 1e9b1539-3e7e-336c-9cc8-1082a10206a8 | -7.2519 | -55.5994 | 2026-09-20 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.2 |
| ac46afac-4832-339e-9a34-e673101b57aa | -12.0263 | -50.0447 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 31ee7d9a-7338-3fa0-8e73-996cf0c8ae36 | -6.3471 | -58.2973 | 2026-09-20 14:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ce3340d7-0513-33a8-b951-c70a67f516a4 | -7.0262 | -42.0685 | 2026-09-20 14:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| 152185d5-d97e-3a24-a82e-00cf643aaa0b | -11.7351 | -54.5636 | 2026-09-20 14:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| bce585bf-4295-3885-96cc-5bdf3ee1d247 | -12.1524 | -47.0158 | 2026-09-20 14:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 005db6e2-cc1a-3593-9a76-694b78e8a556 | -8.8735 | -49.7328 | 2026-09-20 14:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f39bf9d4-8522-3b35-8edf-ccbc167b412d | -3.364 | -42.7824 | 2026-09-20 14:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 62877335-b72d-3653-a2ec-4ab9ad986b16 | -11.3817 | -44.0319 | 2026-09-20 14:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 189.4 |
| 5215dfa5-4cec-3102-925d-71c258544ae0 | -6.737 | -55.0674 | 2026-09-20 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| ad4308b5-4254-3b9a-a1a1-77e4f21d1649 | -6.4302 | -59.9724 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 160a1965-b069-3483-8dd6-a5bd00321daa | -12.9084 | -51.01 | 2026-09-20 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4c07a518-e14e-34f1-aeeb-10185a0f3e1c | -6.4671 | -59.9711 | 2026-09-20 14:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 198.8 |
| 87445fcd-944b-3c64-ad2b-01ee663b384f | -7.5519 | -57.6775 | 2026-09-20 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 73649965-d228-3f4c-873d-025678a21cee | -10.41 | -48.933 | 2026-09-20 14:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 34f6c527-a9df-344d-983d-7d6664cdd932 | -12.642 | -50.9359 | 2026-09-20 14:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 0269f99d-1a94-3118-bf56-64ff2e4d59d9 | -11.4537 | -45.3892 | 2026-09-20 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 3491fc6f-a9e4-3bc2-9573-b6019d2b7d42 | -9.6964 | -45.8666 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| d3310350-8b08-3bce-9c8e-70d6822617b3 | -12.8896 | -50.991 | 2026-09-20 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 826c66e2-4dd0-38ed-9150-2f7751541c33 | -11.9681 | -50.1164 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 207de0cf-db6c-3512-a141-2b4192cf1065 | -8.4611 | -57.6292 | 2026-09-20 14:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| e4e2ada7-e7f2-382a-850d-8c20768254bf | -14.9314 | -49.9103 | 2026-09-20 14:50:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 94.8 |
| cd5c24b9-1d5d-3455-8f9a-bae1b3a1f559 | -11.731 | -50.7014 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 282f78cc-e51a-3712-a4d9-1b0c55842479 | -6.7666 | -59.1129 | 2026-09-20 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 979aa82b-0798-3b96-8c16-3c310cd0468a | -11.7823 | -49.8152 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 06c3fa0f-ac67-3b27-b1c6-8000ba132014 | -12.8704 | -50.9933 | 2026-09-20 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 1e86b1da-ed87-3743-8a2c-24271873acd4 | -11.0596 | -54.1755 | 2026-09-20 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 365.4 |
| f83c8106-3baf-3267-b9aa-a715112d4895 | -13.5907 | -51.4794 | 2026-09-20 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 165.4 |
| cf88cfb2-8ed2-3c9a-8530-01f17bd4d416 | -5.8088 | -55.7095 | 2026-09-20 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| dd1e106c-3662-3ec9-ba22-e27c40ef2524 | -12.2341 | -50.1703 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 8557531b-cc80-3ecf-b9e5-46778920b4bc | -9.3609 | -48.3251 | 2026-09-20 14:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8ce06f9d-d8e5-31dd-9926-8ea7ac681b40 | -12.0652 | -49.9969 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| bc25cd0d-b4a7-3dc3-935b-f2a61eb2c160 | -2.8974 | -57.8181 | 2026-09-20 14:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| d0251e9e-12d3-37bf-8b73-6b59dcd55935 | -12.8893 | -51.0124 | 2026-09-20 14:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 205.2 |
| 0ef85675-ce9b-3ae7-909a-9bf8c84bbc54 | -9.2682 | -48.2034 | 2026-09-20 14:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 417d438d-b52a-3231-8622-91263b1fd1b7 | -6.8216 | -59.1686 | 2026-09-20 14:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 42a3aa8e-b9e5-39cc-8d75-f3e8273f76a2 | -2.8009 | -59.8957 | 2026-09-20 14:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f167fc83-1982-3c08-8b9d-b636213cbba4 | -7.0617 | -47.5046 | 2026-09-20 14:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 0d559cdb-0c70-3d77-98c3-a0c41145a9b1 | -7.0286 | -45.2554 | 2026-09-20 14:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b4ea69a3-7446-33d4-9c6e-af1f1e6b24b5 | -11.6624 | -50.1954 | 2026-09-20 14:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 10b3ea85-0ec3-3962-afd4-dc49b84551d6 | -9.2188 | -46.2139 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 64c96931-ba43-314b-bd09-f68cd28d46bb | -2.9326 | -58.3397 | 2026-09-20 14:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| b0e99e37-5ea4-3def-b3b2-703896f5a857 | -3.3821 | -61.2901 | 2026-09-20 14:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0ad196f2-f77a-3e9a-9307-f68d4294c924 | -10.7612 | -50.9132 | 2026-09-20 14:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 738fcdf7-2ad3-3cf7-b76b-8f8caac02fc0 | -9.6668 | -54.3129 | 2026-09-20 14:50:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 62e7e7f2-9c07-364f-9e57-99ddca5f0907 | -9.6205 | -45.8755 | 2026-09-20 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 157.7 |
| b2c3a404-bc2d-3e14-bfce-3a8e9b777996 | -11.4541 | -45.3662 | 2026-09-20 14:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| dac676ac-0fd6-3c1f-a193-51b86995a8da | -5.9982 | -52.183 | 2026-09-20 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ce0f551b-2405-3ba7-8663-dd37f9d7fe1b | -11.0407 | -54.1772 | 2026-09-20 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 8017560c-342f-33f8-80be-739bdc807281 | -3.3866 | -59.5797 | 2026-09-20 14:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 52f1f73d-7552-30b0-8b7c-c9bfb5697032 | -12.1328 | -47.041 | 2026-09-20 14:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |


[Clique aqui para ver as próximas entradas](README132.md)
