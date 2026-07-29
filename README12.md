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
| 19011e7f-f422-382f-b94a-f8e43a7c2744 | -6.86994 | -46.00478 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95e06122-7d8a-33be-bae9-4173cc3953ad | -11.74759 | -46.73552 | 2026-07-29 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d3152f8-1236-37fd-8b91-f1ed44390acc | -11.9363 | -43.38324 | 2026-07-29 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f2627ac7-c751-3655-a3c7-729bf40e1da5 | -7.34203 | -45.8543 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d39d8145-d9f6-3207-b013-e80a7d2278be | -7.82678 | -46.50845 | 2026-07-29 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0402791-68e7-323f-9f04-705fc80b3af0 | -7.34961 | -45.84795 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 722513a7-4f0e-3fe3-9bad-03a16864f77f | -6.87601 | -46.00931 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 63857c18-a6f3-34ad-986e-efe22094ba8d | -7.33593 | -45.84977 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf738e3f-6b2a-3d78-9596-a28124d8498b | -7.33871 | -45.85379 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5705ff02-0ce8-3141-9d7b-89b9262d6c68 | -6.844 | -42.88738 | 2026-07-29 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 20e74777-783b-31d1-85f2-280e2021b919 | -9.09757 | -50.60992 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1ed9b26-1691-30da-a0b6-fdd1c7eee7a3 | -7.35179 | -45.83394 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 089c5e67-2e8c-38a6-9bff-aa865c2668d1 | -7.35234 | -45.83044 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 7b01ee67-ad67-3abc-a539-70e713bb0e16 | -7.90431 | -48.28114 | 2026-07-29 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68a78c20-f98f-38d2-af0c-7cf7884b90e5 | -10.9337 | -43.05566 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 7ff07fe8-6d53-377a-99ed-d4895132ef25 | -11.52992 | -47.5606 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c89dff5d-02c5-3f4e-bee5-9159a28a377a | -11.54602 | -47.56675 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1a31227-4582-3669-8100-563e32565a02 | -7.33981 | -45.84678 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c619252a-0744-3c0c-8701-6a40b2587805 | -14.0523 | -53.95903 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8daca81-35b6-3e00-8a3d-ec474e4d7d0e | -18.65566 | -48.2343 | 2026-07-29 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| c59be16e-29b3-3c8b-8fcd-2531bb15c828 | -14.06121 | -53.98092 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| adc6909f-051c-38fe-924d-e59783891df3 | -18.53805 | -56.8147 | 2026-07-29 04:34:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a4f92648-fead-3de6-8fba-5930d72c8807 | -13.30188 | -54.32993 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1128d753-1ea1-33c1-8c5d-b750abbd1427 | -14.18858 | -51.91153 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4767885c-74a7-38a8-a74a-7dabc92c2984 | -14.07024 | -53.97881 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aebb08a-6d6e-38eb-953b-af7e76aa3d05 | -13.99336 | -53.94518 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eacb0c44-d0c6-3d63-b247-34540942ac98 | -15.40386 | -55.91346 | 2026-07-29 04:34:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 664ab412-a739-35d1-98d3-59771b3c4a1d | -13.15307 | -51.30053 | 2026-07-29 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 220301ce-1c22-370c-a982-6ed020e8181d | -14.21781 | -44.65885 | 2026-07-29 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46b29940-0a97-382d-a1f4-cce4fb23f43f | -14.08704 | -53.95778 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7df6c0c1-4cc7-307b-b8c3-1e38bf175f89 | -15.43782 | -41.37895 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 9da13d5c-a002-317d-9c29-92977321bdaf | -19.35881 | -49.49775 | 2026-07-29 04:34:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 809a59fa-7e40-3668-8b3f-7fb3c2c68753 | -14.72987 | -47.13618 | 2026-07-29 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f331b91f-1946-38d1-b468-542d04c86808 | -15.43667 | -41.3842 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 88b193b0-c1d1-3a45-875d-d80a9c91b65e | -18.80019 | -51.24628 | 2026-07-29 04:34:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd7182fd-f557-36e7-a1ad-7ef2a776a927 | -13.48137 | -44.0344 | 2026-07-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b294bf36-a954-3077-bc80-a2d9800fc8c5 | -12.29598 | -50.34226 | 2026-07-29 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c7c3a2b-c235-3e02-b959-ec72f492be74 | -13.56577 | -49.04783 | 2026-07-29 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 12babaa9-2f19-3b5c-b48f-d4438f717526 | -18.52124 | -46.17843 | 2026-07-29 04:34:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1128c16-84ff-35b0-b2d6-2851e0095ed5 | -14.839 | -41.24524 | 2026-07-29 04:34:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bef44549-dfdf-320d-bd2c-cf2ea7fd49a3 | -13.75395 | -49.4329 | 2026-07-29 04:34:00 | NOAA-20 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f14b266f-8fbd-3792-8b83-e0a19135f2c7 | -13.71153 | -51.91766 | 2026-07-29 04:34:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71f7031-7da7-39a5-af7e-69181ffc425a | -13.1516 | -51.30911 | 2026-07-29 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55b920f9-e7f9-3dce-b822-cd86c006f79c | -15.44185 | -41.38008 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 8fcc3c09-e3e6-3306-95db-bce5903a5e8a | -15.39953 | -55.93542 | 2026-07-29 04:34:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 367c95e5-29d0-3da6-81bd-a2d2a8d5bbc9 | -14.02666 | -53.97593 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3159ac3d-6a83-3ebe-9185-e2204ad1a533 | -14.03124 | -53.9794 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59335ad7-310e-31bc-8fc1-08b7ef9ae8da | -14.06062 | -53.96075 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0ff6a6b-95a5-3e50-8355-d186f48f6099 | -14.18662 | -51.90817 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d125e2b-00c1-30d2-b024-4c5d3bdf31b9 | -13.98427 | -53.94768 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa3e5755-a42e-3aec-81a6-431042ff5167 | -13.56968 | -49.0448 | 2026-07-29 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f970701-7513-3fa3-a933-fb6a464fac73 | -14.72483 | -47.14659 | 2026-07-29 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9b068544-dbff-303a-bf02-e2a1a7d16a45 | -15.06602 | -41.21866 | 2026-07-29 04:34:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8c013f73-1f6a-3083-b5b1-4f85b33035a2 | -14.51824 | -47.75745 | 2026-07-29 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca58099b-e2ee-39ca-97f2-7a03cf6e30c8 | -15.44646 | -41.3806 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 7a90b7e4-aed4-3c76-92e2-81c8d84dfd68 | -13.45294 | -44.04225 | 2026-07-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0996df43-c915-317b-9d18-4e59cb068496 | -14.00086 | -53.97524 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 854109da-3381-3ed0-ad8f-b8e893f92075 | -15.44705 | -41.37581 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| cbc380cf-5663-39d4-93ac-63b419413a5e | -14.02319 | -53.97118 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6915608b-67e3-3afe-8c9e-289d9fa2c541 | -18.80409 | -53.14122 | 2026-07-29 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 800a9e25-ed98-3c42-b70f-24a479b3fa14 | -14.03916 | -54.1004 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9467f5e0-6904-3c5b-9188-79f2058699b7 | -14.18954 | -51.91335 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a5803df-6079-3d5c-b4ee-4a03689a4aef | -14.01901 | -53.9704 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6095e32a-7fc2-3ceb-94e3-f67bb2bdaae1 | -15.43722 | -41.38362 | 2026-07-29 04:34:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 0376a354-e382-32cf-a0e4-83501a20f082 | -14.06679 | -53.97407 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 847a48e9-1965-3428-a19f-98eb786bf4df | -14.03154 | -53.97276 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f7892ec-04f8-3dbb-abbf-957c973abe85 | -14.06954 | -53.98265 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58af959d-52d6-3c3b-b350-00a9d9ad3b5f | -15.40416 | -55.93635 | 2026-07-29 04:34:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ae85d69-cc96-3b3e-9f19-31ecfd7840ec | -15.87074 | -49.61289 | 2026-07-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a97e4b5-3222-399d-bf2e-be2abffd49e4 | -15.87825 | -43.60155 | 2026-07-29 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fb0ac84-eec4-3211-9033-c68585fe361a | -13.48072 | -44.03906 | 2026-07-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 456d10d0-dde8-347a-a921-d6520dd094e4 | -14.39196 | -48.02092 | 2026-07-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02775f72-61f7-3a47-a297-2a0ada860f8e | -15.86741 | -49.61232 | 2026-07-29 04:34:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7179075-a0ac-324a-9bcb-f16c82cd15b6 | -12.32576 | -54.0961 | 2026-07-29 04:34:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f4e4c7f-32a7-32f3-b9c3-f5ec8cfdf567 | -14.39483 | -48.0252 | 2026-07-29 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a9ad96b-38a8-330a-abf7-032b17e7bccc | -15.32703 | -43.02279 | 2026-07-29 04:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07148359-ebe0-3a39-a09e-ee518249058b | -14.03431 | -53.98143 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 76d6ce94-4df6-35d0-bbbc-72d41b7d1b58 | -13.4567 | -44.04285 | 2026-07-29 04:34:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fdc8720-e94d-3b67-9ff2-bc79f5691799 | -18.80595 | -45.74305 | 2026-07-29 04:34:00 | NOAA-20 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f6f7d77-3bbf-3133-8ec0-2df925521b55 | -14.2076 | -43.97496 | 2026-07-29 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88d2ae3f-6da0-3358-8cfc-a02641f7c678 | -16.14932 | -48.61509 | 2026-07-29 04:34:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a031dec5-84cd-3aed-8340-9a2a149bbe81 | -17.72573 | -48.63135 | 2026-07-29 04:34:00 | NOAA-20 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0629cdf-ce67-3b54-9128-95658215598d | -15.1766 | -43.85266 | 2026-07-29 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9baa86a0-20d1-330c-870c-a32c34b9d8ff | -20.30127 | -46.35332 | 2026-07-29 04:34:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9128ef8-a3dc-3a5a-89e5-83bf932dd503 | -20.03465 | -46.36309 | 2026-07-29 04:34:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9abd1d7a-fda1-360a-b1b5-13d71b893f0c | -15.87426 | -43.60095 | 2026-07-29 04:34:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b11ba94f-806f-3854-a61b-34e028e08dfa | -18.79958 | -53.14507 | 2026-07-29 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6452018-b64d-3ea7-a74a-118857f54b39 | -14.03197 | -53.97546 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4ac8bb-262b-352e-a51e-b4b05fb68845 | -14.05646 | -53.95988 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70ab1e06-b116-3d8f-b570-19d151165584 | -13.09613 | -49.46226 | 2026-07-29 04:34:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d277ec5-c883-3bbc-9f35-46f313f744d6 | -14.72148 | -47.14604 | 2026-07-29 04:34:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94f5eb51-e3ed-3354-884a-a9a5c9bd8c46 | -14.18938 | -51.90704 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d48b73f0-9dff-3810-8ddd-82fa29e8628f | -14.19107 | -51.90435 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27dd66ec-1a2d-3784-bf0b-c146154524a1 | -14.03084 | -53.97672 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1436364a-cf94-3895-bb99-f0265ae0143d | -18.79679 | -51.24566 | 2026-07-29 04:34:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 675f73d5-4092-38f7-93a0-a943258ab76c | -14.19017 | -51.90257 | 2026-07-29 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff048012-1b17-3596-9c24-af2c5ba5b04a | -18.80327 | -53.1458 | 2026-07-29 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cca666eb-4aa0-3cab-943a-1406fd7e8015 | -14.01555 | -53.96564 | 2026-07-29 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7812278-a6e2-3cb5-b78e-ff95bd19475d | -13.5691 | -49.0484 | 2026-07-29 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2930515-d198-3547-ad84-ffc9cae32909 | -16.05385 | -41.44649 | 2026-07-29 04:34:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
