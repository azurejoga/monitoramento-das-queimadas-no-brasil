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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 222fce93-fa90-3811-99d0-4bcbfd0a8938 | -3.5632 | -47.3629 | 2024-10-30 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 15b17b04-8c70-3f5f-acb0-fbdf686f70e7 | -3.5688 | -50.043 | 2024-10-30 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 6128db3b-aa88-3755-9dd2-acf0e034a949 | -3.5689 | -50.0219 | 2024-10-30 00:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6a049d1d-9a06-3fef-94a8-217b73753eee | -3.5817 | -47.384 | 2024-10-30 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 287.4 |
| 13418e7e-415c-35c2-8b19-061a4612d759 | -3.5818 | -47.3621 | 2024-10-30 00:45:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 0d41c4f8-1a15-314f-8cc8-cde4c35d8970 | -3.8036 | -51.1852 | 2024-10-30 00:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0fce3b2f-743c-3c86-9568-35ca0659da8c | -3.8037 | -51.1644 | 2024-10-30 00:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 238.7 |
| 5d18740e-c114-3c0d-b844-9a33a3620e8d | -3.8038 | -51.1436 | 2024-10-30 00:45:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 73518d0a-64fd-32ed-85ab-59c1fe6cd05d | -3.9326 | -41.4957 | 2024-10-30 00:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| f9aecf6a-d1a6-3507-9cc3-9832e47d0db6 | -3.9327 | -41.4717 | 2024-10-30 00:45:28 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| af8092a8-2578-3f6c-88d5-fe623a9540c4 | -3.8221 | -51.1637 | 2024-10-30 00:45:28 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 69ba6c5d-1f19-3977-8293-7bb74f067f44 | -3.9486 | -48.1291 | 2024-10-30 00:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 5a32269e-25aa-35d5-89ff-df686d4f1ecb | -4.0705 | -46.2836 | 2024-10-30 00:45:29 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 21f7293b-fbd9-3059-8490-d53bdf550905 | -4.2561 | -43.46 | 2024-10-30 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4950655c-5d5e-39f3-acc8-02cd3d9ed31b | -4.2563 | -43.4368 | 2024-10-30 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 4a4643fa-e73a-33a8-8833-f696971cb357 | -4.2748 | -43.4589 | 2024-10-30 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 30338aa3-2d55-386e-9416-a003aa5adce4 | -4.2749 | -43.4357 | 2024-10-30 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 146.4 |
| c7879668-5d45-367e-80cd-21fc51940510 | -4.3473 | -43.779 | 2024-10-30 00:45:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7a99d186-b722-3d38-9c78-a3e416769128 | -4.2496 | -50.6677 | 2024-10-30 00:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 9a4d7e2c-74a0-36dc-a2b6-31412c375897 | -4.2679 | -50.6879 | 2024-10-30 00:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| bd947b0a-dcba-3d78-a5b7-ba8cf2fb2fa7 | -4.2681 | -50.6669 | 2024-10-30 00:45:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 758423ca-c1cb-393d-bf78-d0a362849ae3 | -4.4269 | -45.8199 | 2024-10-30 00:45:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 33a498e1-5cb4-3ce6-b38d-1751f82cd5ec | -4.4971 | -46.4618 | 2024-10-30 00:45:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 8d22bd62-ad30-3006-885e-0752da4aa23d | -4.5157 | -46.4608 | 2024-10-30 00:45:31 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 85207fa7-e58e-3760-ac43-6630982f5690 | -5.2306 | -47.9566 | 2024-10-30 00:45:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 90951005-65e9-3ce4-8ccd-9873b1696e49 | -5.2308 | -47.9349 | 2024-10-30 00:45:35 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 1617153a-f199-3563-ba56-0fc6537aa75a | -5.9788 | -45.3621 | 2024-10-30 00:45:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| ca551a3a-ed3e-34f5-acaf-309c3964d0bd | -6.8408 | -59.0519 | 2024-10-30 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 10962f4d-2cc3-3612-a1ce-a3801427293a | -6.8409 | -59.0326 | 2024-10-30 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4cf4e9b9-7081-30d7-b61b-66d73311b01f | -6.8592 | -59.0511 | 2024-10-30 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 695af44e-6af9-34a2-9fbb-be9bf066be2f | -6.8593 | -59.0318 | 2024-10-30 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| f883f017-053b-33c0-b7f7-f144999c025b | -7.8736 | -46.9065 | 2024-10-30 00:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 160.0 |
| 97143480-8743-33bf-a683-80c9cd59ce56 | -7.8739 | -46.8843 | 2024-10-30 00:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a95f6e51-9307-3811-959b-5f6e03b0076c | -7.8924 | -46.9048 | 2024-10-30 00:45:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 80e99f47-b2d1-3bf7-a55f-15e83902bb74 | -10.6984 | -44.9186 | 2024-10-30 00:46:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 5f4cd746-7449-3e01-8f4a-3c9d31aee618 | -10.7171 | -44.9391 | 2024-10-30 00:46:06 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| c51aca9e-a825-35e1-8dac-864f85759236 | -10.7175 | -44.916 | 2024-10-30 00:46:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 231.0 |
| 8fd56a92-b15f-3b07-8988-de8856813f39 | -12.899 | -45.0549 | 2024-10-30 00:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| ef062891-773e-3268-979c-e325b76f2b83 | -15.8211 | -42.4953 | 2024-10-30 00:46:34 | GOES-16 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 7dce69e7-6f47-343d-be3d-cf49a2f1e437 | -24.032499 | -54.112598 | 2024-10-30 00:46:40 | METOP-B | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 94e3998a-ef47-34df-a6b9-fdfff6203be1 | -24.022699 | -54.114601 | 2024-10-30 00:46:40 | METOP-B | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6ec487f-d6bf-3fe1-b345-f54ab0605d04 | -24.0247 | -54.126202 | 2024-10-30 00:46:40 | METOP-B | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9104d83-8c10-3bba-861f-323be2b621bb | -24.0268 | -54.137798 | 2024-10-30 00:46:40 | METOP-B | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3df12957-3520-36ba-9910-132a5641a634 | -24.006701 | -54.082001 | 2024-10-30 00:46:40 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2867db13-4be7-3fbc-b936-566683794f97 | -24.008801 | -54.093601 | 2024-10-30 00:46:40 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cab3210a-7a0b-3527-9be7-e10d4b633497 | -24.010799 | -54.105099 | 2024-10-30 00:46:40 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89e4d307-a836-3c24-8f3f-54bab367f86b | -23.9991 | -54.095699 | 2024-10-30 00:46:41 | METOP-B | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3342d78-ccdf-3c3c-9601-60fd40253803 | -22.0968 | -46.891399 | 2024-10-30 00:46:48 | METOP-B | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 08fdfed4-1b5e-3fa5-b449-75a55a6515e0 | -19.5862 | -56.7136 | 2024-10-30 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 67.0 |
| d2e53235-df99-32a3-b924-47a4cf47d852 | -19.6063 | -56.7108 | 2024-10-30 00:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 62.9 |
| 86071903-a433-3054-9aac-4c8b72bc0ac5 | -21.8829 | -50.3335 | 2024-10-30 00:47:03 | METOP-B | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83d02dd9-ef1d-3018-a907-9a7c97456c5a | -21.884501 | -50.341 | 2024-10-30 00:47:03 | METOP-B | HERCULÂNDIA | SÃO PAULO | Brasil | 3519006 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d169a1d-a092-328b-b103-267b07fc6a34 | -21.691799 | -49.767899 | 2024-10-30 00:47:04 | METOP-B | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cfdbacfd-0fc2-389f-938b-730ad324618c | -21.3951 | -50.064999 | 2024-10-30 00:47:10 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1452b707-a7f1-3afb-9a39-ddb967647eab | -21.3967 | -50.072399 | 2024-10-30 00:47:10 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc807b95-e50b-34d4-b8e4-2cade5a4db03 | -23.9923 | -54.1106 | 2024-10-30 00:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| 31552116-0d92-3843-9861-688d05b01bf6 | -21.5795 | -54.1749 | 2024-10-30 00:47:21 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3012f5ca-1d7d-3294-af42-cd47dc6f3cc9 | -21.581499 | -54.1856 | 2024-10-30 00:47:21 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ac9333ab-64cd-3968-a288-40c5eda0a2a7 | -21.5835 | -54.196301 | 2024-10-30 00:47:21 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 51747d77-0792-37e7-a544-1670a974f7f9 | -19.6362 | -56.673901 | 2024-10-30 00:48:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 231eae79-2ab0-3a6c-b3a1-4ae59bbaf083 | -19.6264 | -56.6758 | 2024-10-30 00:48:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d528c1e-22ac-37e4-b6ed-b9ad1ce7f91e | -19.597099 | -56.681599 | 2024-10-30 00:48:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| efd7c76b-1bd6-3491-a825-082feaa53ace | -19.599701 | -56.695801 | 2024-10-30 00:48:01 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6feae353-d451-31d1-a7f7-bcedd09b5640 | -18.7549 | -55.5709 | 2024-10-30 00:48:11 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6fb6dcac-3b44-3b38-a998-04342bde25ca | -15.8291 | -42.463299 | 2024-10-30 00:48:11 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fc4487de-2bfd-3f9b-98d2-53caf57fdfaa | -15.8195 | -42.466 | 2024-10-30 00:48:11 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d02b057f-df12-3049-a1c7-c3a4a5330302 | -15.8238 | -42.4827 | 2024-10-30 00:48:11 | METOP-B | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| df790057-c1a9-32ad-b30d-b458cf99b4e6 | -13.7763 | -40.658699 | 2024-10-30 00:48:36 | METOP-B | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b8b88df0-f2f4-3e80-84a3-07049b0e362f | -13.7828 | -40.682499 | 2024-10-30 00:48:36 | METOP-B | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c79e0870-7a04-3495-a590-959db019f71d | -13.699 | -46.0849 | 2024-10-30 00:49:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1e951ef-0799-3709-a2ae-b27163ee1320 | -13.7016 | -46.095501 | 2024-10-30 00:49:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b1180d62-e922-3803-9487-7b5c799d9b71 | -12.6759 | -43.801399 | 2024-10-30 00:49:07 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c1a63fe3-229b-31e4-a946-89ac0460ed76 | -12.6624 | -43.788601 | 2024-10-30 00:49:07 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d9f1381-6621-38eb-9669-ff4ea3c4d3e9 | -12.6662 | -43.804001 | 2024-10-30 00:49:07 | METOP-B | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 138fc08f-961b-3ec0-8cad-c2bb7c44efba | -12.9141 | -45.0387 | 2024-10-30 00:49:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 187f22f6-0ce5-328d-a170-a0c09496ae56 | -12.9013 | -45.028599 | 2024-10-30 00:49:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db97dce1-d222-3f1d-bcd5-bb0764481575 | -12.9044 | -45.041199 | 2024-10-30 00:49:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8130e634-e32b-3bb3-b0d9-504ff6f05780 | -12.9076 | -45.053699 | 2024-10-30 00:49:08 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf6ff515-6af5-3acb-a816-7aedf35741e3 | -11.8926 | -43.808899 | 2024-10-30 00:49:20 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 040a060f-3709-3740-8ce1-5d406f379f13 | -12.6381 | -46.870998 | 2024-10-30 00:49:20 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9176fa3-f6a0-3e06-a793-dc894753ae2b | -12.6053 | -48.7416 | 2024-10-30 00:49:28 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bece9847-e71f-3cb9-9f20-28e36b48c148 | -12.6071 | -48.7495 | 2024-10-30 00:49:28 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 098645d6-4ab0-3b53-9976-d5daa6348a3e | -12.609 | -48.7575 | 2024-10-30 00:49:28 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8096e2e0-b2b5-3d87-b35b-ae71690eee92 | -13.3838 | -52.385101 | 2024-10-30 00:49:28 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b99031a-2f5e-3d7e-b8bd-5bed369ce4cb | -12.1038 | -47.228802 | 2024-10-30 00:49:30 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c005740-eafe-3be8-abe9-7ccb2cd84eec | -12.1061 | -47.2384 | 2024-10-30 00:49:30 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 773c9d08-3876-3d68-bc6e-76b259265f16 | -11.8917 | -46.518799 | 2024-10-30 00:49:31 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be2a5481-ebf5-3cfa-96bf-b7bbd647b786 | -12.0144 | -47.634102 | 2024-10-30 00:49:33 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 285ec21c-00d2-3832-9cd6-9001811a98b2 | -12.0165 | -47.6432 | 2024-10-30 00:49:33 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 32e54853-ca27-328a-98ad-509c2c04244a | -10.8847 | -44.5229 | 2024-10-30 00:49:39 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 38ebe89a-894b-3b01-90cb-fa3926d872de | -11.0688 | -45.3489 | 2024-10-30 00:49:39 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3db9132-fd00-35ff-bca7-958ddf1b521c | -12.3884 | -50.999298 | 2024-10-30 00:49:39 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8bd4211f-bb15-3c25-ad21-4aebdfd06b09 | -12.39 | -51.006302 | 2024-10-30 00:49:39 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 121275f6-09bf-3515-bc03-a852cff2c8e9 | -11.7365 | -48.338501 | 2024-10-30 00:49:40 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c82060c7-e2e5-358f-88f9-9be66c8b7039 | -11.7385 | -48.346901 | 2024-10-30 00:49:40 | METOP-B | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 96ebae08-40de-3e66-8692-94be6aa5c59c | -10.7298 | -44.896198 | 2024-10-30 00:49:43 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4668678c-e641-38eb-91b5-d60096ababf3 | -10.7332 | -44.91 | 2024-10-30 00:49:43 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6b27fef2-ff84-3f2b-81a3-4fcc66d3ec25 | -10.7201 | -44.898602 | 2024-10-30 00:49:43 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 817f5e89-37a1-34eb-be26-beebe137c63e | -10.7235 | -44.912498 | 2024-10-30 00:49:43 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4cc48e5-e09d-30b0-959a-2b034693a809 | -10.7269 | -44.926399 | 2024-10-30 00:49:43 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
