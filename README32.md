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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7caded1f-89f0-346c-b3d9-9742257fcfd3 | -11.44025 | -43.44344 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 660757a3-4b4d-3d4c-867f-7b3ebf051854 | -9.80737 | -44.74112 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27f2a596-eadf-3bc6-ab5c-65e348086e69 | -8.94457 | -49.79823 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50aa92e3-f955-376e-ae73-3d4270cfaae7 | -9.7822 | -59.02456 | 2026-09-30 04:34:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d40ed02d-a47e-389c-b9d5-c3a9d3f6af5f | -9.79182 | -48.22619 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fbaedb2e-a6d8-361b-a31d-ae193436a8d6 | -11.36052 | -50.97927 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26ed4d8a-2122-3344-a7cb-ee5b25407208 | -11.26212 | -43.52834 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85ae34e9-626b-37a7-b8ad-70fd622f9406 | -11.09466 | -37.14695 | 2026-09-30 04:34:00 | NPP-375D | ARACAJU | SERGIPE | Brasil | 2800308 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 051be049-4ec4-34f8-ac65-5f578091c27d | -14.12236 | -46.26091 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd3c0cb3-3596-3534-b747-d2c8ef58d5b9 | -14.50159 | -48.29632 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e954e73-c719-3640-a0b1-4b8ff25d29e7 | -11.16714 | -44.77318 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 863a7e77-e0d2-330b-be06-f899e4bcf8d3 | -12.3064 | -47.96006 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2bbd946-c361-354c-b73a-6b6c78a1405e | -10.89859 | -43.86378 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83a0152a-24b8-3586-8a0f-393bf043f098 | -11.399 | -50.97512 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9143e4ed-02f3-3583-b09a-f81ad72f5da7 | -15.75541 | -46.04078 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 216113cd-4462-3139-a7d8-de901b0cb296 | -11.17504 | -44.83314 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6429ca1-f39e-3949-914e-114ceebc5e05 | -11.16268 | -44.77982 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6a20ab2-9c8f-33de-bfbe-04bf58e6eb1c | -11.81556 | -50.42647 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bb26dd88-b764-3ba8-b553-956771d863f1 | -10.8288 | -48.70054 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| febe7609-d1db-3d75-9d82-841e6eddc4b5 | -8.32109 | -54.75602 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e726f9f-a735-3788-8750-f3121a924181 | -12.30983 | -47.9607 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f18c99-58d5-37c7-8c17-edb1e58b57cd | -10.29024 | -44.63901 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d96eee50-f057-38f1-b45b-d7c8fe8ae81f | -12.06809 | -46.46233 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a720c817-4730-30b2-86d3-259779ba9cee | -10.51696 | -45.37083 | 2026-09-30 04:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a042768e-9cd0-30ea-a725-bb55ff3c12d9 | -9.92716 | -50.15013 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd6920a5-93c1-39a8-9f2e-613351305b86 | -14.01463 | -42.91202 | 2026-09-30 04:34:00 | NPP-375D | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f275e94c-94b6-328d-b0b0-547a2bccd152 | -11.71613 | -43.45116 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6afb727d-9661-38a7-b545-fd86a1ca41e5 | -11.31138 | -50.97842 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4639afe3-eeb8-3748-b11b-6ca4eca65498 | -15.75597 | -46.03714 | 2026-09-30 04:34:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d640218-c458-3b50-ada5-53faf77dbd96 | -14.5274 | -48.28926 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11561ac1-4ccb-3738-8cf4-af0bc736ed24 | -11.84188 | -45.02699 | 2026-09-30 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 214d7ace-0162-3e94-8884-38bedd37393c | -8.0639 | -55.34177 | 2026-09-30 04:34:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8642c4d-33a8-34ce-8aa4-baf089ec41d4 | -11.83208 | -50.47078 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99080625-cef3-3b28-9462-2afb8586c962 | -17.10117 | -46.46955 | 2026-09-30 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1f3e7df-ec2d-3591-8203-325d1a920693 | -13.36676 | -46.81901 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 625fb035-f401-3b97-be98-bc4645092d3f | -11.43154 | -43.43007 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0535546b-93b6-3f94-9311-54e40a343ecc | -11.43563 | -43.4267 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e5c6cfe-8dbb-31a6-be49-772d73810927 | -8.49006 | -54.91104 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c461a65-b664-35b3-b818-fe7b43654107 | -9.82078 | -48.20608 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21c5c5cf-8b65-3438-839a-f370ab8962e0 | -12.07143 | -46.46289 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99403d6a-72ee-370b-8828-75b1adc7eef1 | -14.6896 | -48.02735 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1412795-b2ff-3308-8dee-32e5b923197e | -9.0679 | -51.53071 | 2026-09-30 04:34:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21adcbe8-b378-3fbd-a64c-75902037eeba | -11.16831 | -44.81011 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe27ca2f-9d92-3a44-86b7-15de834de707 | -11.44144 | -43.43562 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7e5907a8-1a1a-3359-bc33-baccfbdcab30 | -11.35321 | -43.35073 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75b8a0ac-6e98-3091-9ea4-11d9bddb2ea5 | -11.17726 | -44.81886 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e68033ab-311f-38ca-8567-defb87c0bf79 | -10.24438 | -44.6026 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c377e55-dcfa-392b-bf3e-8e476778ea7c | -10.72769 | -50.50475 | 2026-09-30 04:34:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 536f47ff-7f4c-39e4-9916-ac167d771caf | -13.27828 | -43.63611 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e260f165-17b5-3061-b538-029bf3c42ff3 | -14.50375 | -48.30446 | 2026-09-30 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0340539-5485-3939-8a7e-f30725fa5147 | -15.3752 | -47.91618 | 2026-09-30 04:34:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcdaa81f-405a-3008-86cf-0a22ad479f80 | -8.26499 | -54.75805 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17d94040-c553-3ed9-8481-4032a333cb74 | -9.78908 | -44.81419 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 294c5480-daa2-3d7c-b27f-fa089e6a9d50 | -10.28968 | -44.64259 | 2026-09-30 04:34:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6af9e2b6-fb19-3f45-9086-04025c838fc3 | -10.77793 | -47.72015 | 2026-09-30 04:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 417f7000-ea52-3743-a7ba-6df880ddf08d | -12.4378 | -44.17039 | 2026-09-30 04:34:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2bda240-0afb-315a-a8cc-fe9171018102 | -11.37656 | -43.36238 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 49700571-06a9-3165-b8cd-b7895c553cf0 | -8.30158 | -54.70777 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8eaf3e4-5ffb-3a43-a68f-cbf6aa59055d | -13.38287 | -46.82538 | 2026-09-30 04:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ef8a16f-9ea4-31cd-a138-ff69c82dee40 | -11.40243 | -50.9795 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6ad6878-c2cc-362f-a005-3b35855444d6 | -8.31493 | -54.75853 | 2026-09-30 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea26ac70-c478-328d-8bce-49a8b05f8763 | -12.31109 | -47.95316 | 2026-09-30 04:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 763f0f49-c6ed-3cf3-aa1d-8a200e2ab689 | -11.37848 | -43.37767 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60e91b58-d276-39f0-85ce-2ca3289e4c67 | -14.74388 | -47.13766 | 2026-09-30 04:34:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ad59ed3-a62a-31f9-9d67-c613eeeb37d6 | -11.36254 | -43.36021 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9aea3ac4-73eb-349e-b365-1fa5257b5f0d | -11.15987 | -44.7757 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c1bc53b-b941-3ecf-8a2b-a671ec171991 | -13.37993 | -44.01586 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 826c4036-5b62-308d-b4e7-a1a9f7cc7bfb | -13.27831 | -43.63734 | 2026-09-30 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef001956-c0ba-321d-b50e-789f41c2aa13 | -10.70986 | -50.84286 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9aa239a6-1f28-3434-a345-551f74d87f19 | -11.43213 | -43.42615 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6fd99314-f0f7-3db0-803f-a6f8b98f5716 | -11.85359 | -50.97223 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d65f0b6-b1ad-36e6-9e21-f0ada61c019f | -10.89916 | -43.86003 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6bee38e-cfee-347d-9b70-194801849734 | -10.70632 | -47.83028 | 2026-09-30 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e7b2d1e-1cf7-3363-aedf-fa188328aa7c | -12.24761 | -50.25089 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64bd108f-3617-3b0f-93b4-b56422422e3b | -11.84295 | -50.47794 | 2026-09-30 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9ba9ecf-ccec-358f-b804-edda61b4a792 | -11.36433 | -51.02896 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85948228-d60f-3b4b-9c46-c5448056ec3b | -11.39328 | -51.00786 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e68822a-fdc7-3842-927f-8b1e8475b535 | -8.94152 | -49.79255 | 2026-09-30 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b054b7d1-0e61-3e6c-92e8-a3d56fa0dd43 | -13.32351 | -43.95943 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf090bc1-c787-3433-9021-fdf6ca0790d9 | -11.17335 | -44.8219 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b0979ecc-efdd-3ff7-abf5-d173de5c737c | -9.7824 | -44.81312 | 2026-09-30 04:34:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7ec8d5e-a94b-3aaf-92ed-07a6dfd37055 | -11.1879 | -44.83887 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8afb42d8-49d5-386d-9d1a-efcf515073ef | -10.08742 | -50.30973 | 2026-09-30 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6d66d7b3-4a7a-35b9-95d8-2a0b546b7f88 | -13.18571 | -48.55484 | 2026-09-30 04:34:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e9b3b53-ec88-3c77-b73c-2b3f4380d59f | -11.40117 | -50.98675 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5e169e7-aee1-373f-a9d5-e08d96f8d14c | -14.12901 | -46.26202 | 2026-09-30 04:34:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c274f560-34de-31c8-a1db-6f953436aff0 | -11.67937 | -43.50574 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1184ecb-da23-341b-bbc7-1f6d26ddfb11 | -11.2979 | -50.98352 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8081b671-86ad-335c-9d7d-68013614ec9a | -11.41814 | -43.42398 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6e1543ac-ea39-3822-8704-8719c20714ca | -9.80877 | -48.21233 | 2026-09-30 04:34:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ee7c9ef-620f-3b90-92b6-da115d47be11 | -11.85297 | -50.97581 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86303a6a-a4af-3c2f-8393-a5e7d3c0635f | -10.70302 | -50.83412 | 2026-09-30 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cf6b9b2-0376-3bc2-a6cb-11a7bff70fdf | -10.81874 | -48.71644 | 2026-09-30 04:34:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88308906-c492-33e1-bbcb-b03b854edbc4 | -12.14821 | -47.20124 | 2026-09-30 04:34:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fe691dc-271b-3922-8158-ef5c5c683a7e | -10.71328 | -47.83142 | 2026-09-30 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ceaac4e2-2fb0-350b-93dc-24abcb32b671 | -11.9681 | -51.00725 | 2026-09-30 04:34:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a38ba0aa-a068-343e-ae82-33211ee5eb73 | -11.71671 | -43.44723 | 2026-09-30 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c950b1a3-7fb1-3242-bccc-737e750acf02 | -11.394 | -47.43411 | 2026-09-30 04:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3384941-d89c-30f4-a0a8-09914d56c554 | -12.03107 | -47.80922 | 2026-09-30 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bea73e6-8458-30e8-b974-dc5e4761971f | -11.16434 | -44.76905 | 2026-09-30 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
