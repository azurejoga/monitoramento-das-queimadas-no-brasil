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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4aab06a-896a-367e-826d-7107c789a3d7 | -20.44343 | -51.98836 | 2025-08-07 04:55:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2ded3c2-6d8e-30df-83be-613b0f148ae3 | -22.3412 | -47.20515 | 2025-08-07 04:55:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03548863-1e6c-323c-907d-2abf77f6f40b | -22.33568 | -47.20787 | 2025-08-07 04:55:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4807ae60-d499-3745-aafc-eb222289a8a0 | -18.71443 | -47.51098 | 2025-08-07 04:55:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81462810-ca3f-374a-a01a-4b509937c02e | -18.8458 | -47.05332 | 2025-08-07 04:55:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc87535c-6c5e-3e43-a22d-c61f3a1b71b3 | -19.84853 | -49.08263 | 2025-08-07 04:55:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d136cf40-f15a-30fe-bde8-a33db97e6ac1 | -21.23669 | -49.08257 | 2025-08-07 04:55:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| c69885dc-f9ee-3f16-ae7e-66af9a2516c8 | -19.8848 | -48.33197 | 2025-08-07 04:55:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 211cc2b6-851d-325e-be35-23ee751e68df | -21.24122 | -49.08331 | 2025-08-07 04:55:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 6974df8b-8232-3517-8b59-8c9d9605a6de | -21.11357 | -47.03915 | 2025-08-07 04:55:00 | NOAA-21 | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4a7e70a-7576-337f-9a4e-374e12349292 | -23.53874 | -51.46418 | 2025-08-07 04:55:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fd4109a0-eae1-37ce-91b3-29a5734e9f2e | -19.88704 | -48.33285 | 2025-08-07 04:55:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de39c82e-875a-3c14-a180-6c36d18383fb | -23.5383 | -51.46782 | 2025-08-07 04:55:00 | NOAA-21 | APUCARANA | PARANÁ | Brasil | 4101408 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 49a1d890-65f9-3aac-a9e6-4042abac2926 | -19.8446 | -49.07742 | 2025-08-07 04:55:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d5b0eae3-0d7b-3dbe-847d-11a47781f49c | -19.47416 | -55.40873 | 2025-08-07 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2875f7fd-5f1e-38c2-ac7a-14af95f750d1 | -18.84517 | -47.05315 | 2025-08-07 04:55:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6568ccb-0112-3c79-8ee8-2809486bbbc9 | -22.34008 | -47.20641 | 2025-08-07 04:55:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83b5bfea-b389-3118-9d2e-3de7c072be94 | -21.38758 | -50.29851 | 2025-08-07 04:55:00 | NOAA-21 | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f22a22f6-9d79-318e-ab13-d779a4b7000c | -19.84907 | -49.07796 | 2025-08-07 04:55:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39eef4ce-d1b8-3c70-ab4a-5cc5d421f316 | -21.3871 | -50.30259 | 2025-08-07 04:55:00 | NOAA-21 | COROADOS | SÃO PAULO | Brasil | 3512506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 659e834e-68ce-32fa-a72a-afa03fbfabc7 | -20.4428 | -51.99316 | 2025-08-07 04:55:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 569fa4d6-6574-3b31-b633-c4627a2364bd | -25.13206 | -50.18799 | 2025-08-07 04:57:00 | NOAA-21 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 13fb76de-47ff-3958-bd3e-6fc70b2d0f6b | -10.6247 | -44.767 | 2025-08-07 05:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| a873279a-605b-3eff-9573-cffcf385b0f1 | -10.6438 | -44.7645 | 2025-08-07 05:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 28b56118-4a0f-30be-9827-25acff09c8ff | -8.9215 | -60.7297 | 2025-08-07 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| f6ddc362-c086-3c09-82b8-5c4b764adf14 | -7.4074 | -60.0108 | 2025-08-07 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 74845f0f-06cf-3016-8133-9ef5f65a5732 | -10.6441 | -44.7413 | 2025-08-07 05:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| a9b59dd8-945d-3380-8f9d-81e83095762b | -8.9213 | -60.7489 | 2025-08-07 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 2a8ee04d-7bbe-3e77-85cf-0ebce4dd0c72 | -10.625 | -44.7439 | 2025-08-07 05:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 11dd591a-822d-3ef4-8b20-70983efddf91 | -10.6438 | -44.7645 | 2025-08-07 05:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 101.8 |
| b29aca8e-1e7f-39ae-94b6-fb6c64cec420 | -8.9213 | -60.7489 | 2025-08-07 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 114c91a8-c8cc-36ac-8d0f-4cff805ab1c6 | -10.625 | -44.7439 | 2025-08-07 05:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f276645b-0cdd-3a87-8dd6-115646774d02 | -10.6441 | -44.7413 | 2025-08-07 05:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| b0850c4b-6c28-3300-9ce4-2ef4ece0ac37 | -10.6247 | -44.767 | 2025-08-07 05:10:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| d86f92df-e7a4-3795-b2e5-df6755d4b0ed | -7.4074 | -60.0108 | 2025-08-07 05:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e0d1ef91-d6d2-3243-a786-fe64c2d49b1e | -8.9215 | -60.7297 | 2025-08-07 05:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 58d912fc-333f-345b-a40f-6e9881498c20 | -6.95311 | -51.63181 | 2025-08-07 05:18:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe6016b5-d5c8-359a-a8e3-c1fa77104c65 | -5.81509 | -59.22909 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba9d11e3-9123-3f09-944b-506503b4e44b | -4.31389 | -48.07935 | 2025-08-07 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 076a6d26-ae89-3c19-a45d-7b17fd42428b | -6.94836 | -51.63117 | 2025-08-07 05:18:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 268985cc-45e8-3537-95ad-b74f0e8d4142 | -6.67379 | -59.17637 | 2025-08-07 05:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b32207f7-9d6b-3324-b0f1-8016fd5fb30c | -6.4143 | -53.37901 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb852067-ce6f-3b21-9789-59299d5ccb04 | -6.54775 | -56.19864 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b94decf-7d33-32bf-835c-813e2264c120 | -5.79607 | -59.22633 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 550f6d87-f976-37c1-b6a6-232dc68b6cc2 | -3.51673 | -47.20871 | 2025-08-07 05:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7a0439a-4cb4-3831-bda3-ec53fa91005a | -6.41958 | -53.37205 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d8298c2-d0cf-3ee1-a983-e0a4a67859f0 | -6.65165 | -58.82103 | 2025-08-07 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71d921f1-96e2-3119-a25f-1d920608e5ef | -3.51589 | -47.2118 | 2025-08-07 05:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96486849-6e34-3101-96ac-82be26cee959 | -6.36239 | -53.31778 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8af6cbd-975a-3c68-88b2-ac3c9289a912 | -3.58126 | -53.26785 | 2025-08-07 05:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ae92935-cfb1-39d4-94d7-125235e93292 | -4.03155 | -48.07001 | 2025-08-07 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| badcee36-0ab6-397d-9c7d-38c3f343833d | -6.54836 | -56.19467 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ebdfd6bc-0bb8-35ef-bcbd-d4601f8c4b98 | -6.91309 | -52.84272 | 2025-08-07 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 924435ec-41f5-3bf1-80a0-f2340458bf57 | -6.51407 | -56.20572 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8de794e-6a2c-3aea-a195-7eb850254501 | -6.41485 | -53.37523 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75b562c2-bd79-32e1-97f0-aa3275c3305e | -6.41651 | -53.3639 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95960ce4-2dcf-33e8-b440-4d95d2f14f8b | -4.13117 | -54.89868 | 2025-08-07 05:18:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb9162b-acef-3a9a-a677-1f6651838f7c | -3.5161 | -47.21313 | 2025-08-07 05:18:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 708b8325-5baf-34d8-bd88-9231e1ed72c5 | -6.92618 | -52.84458 | 2025-08-07 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 63e5859b-bd67-34e3-8539-4cee16b3a036 | -6.91745 | -52.84336 | 2025-08-07 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5bb8e38c-ceda-3906-8d1e-634048e4b619 | -6.68269 | -58.86145 | 2025-08-07 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9038f8a-ae55-331b-89a4-5deb669ac993 | -6.52378 | -45.58031 | 2025-08-07 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e7e9901-e409-352a-b73c-2e4af03116d6 | -4.31329 | -48.08344 | 2025-08-07 05:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95138305-b7cf-356f-ad33-7ae5fab202c8 | -6.42431 | -53.36887 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a51b90ce-f5eb-3e88-b23e-33780dba5520 | -6.67046 | -59.17584 | 2025-08-07 05:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38c5be0f-dcaa-316a-a026-03b602135800 | -6.64114 | -58.82292 | 2025-08-07 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b8b2d3c-4323-3eb4-b01e-737f75aea92d | -3.52196 | -47.21272 | 2025-08-07 05:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca18a62f-a8ca-3b18-a666-e6cb5f685828 | -6.41178 | -53.36707 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2d426d9-c14f-3651-8779-99dd78e49894 | -7.60078 | -55.19902 | 2025-08-07 05:18:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b71551bb-29d3-33a1-8e3c-c80e5ec3aaf3 | -5.87524 | -57.75234 | 2025-08-07 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a36c95eb-bf7d-315f-b30a-989486a03a7f | -4.02692 | -48.06101 | 2025-08-07 05:18:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3eee297-c66c-3b92-aad2-629e4fdb2feb | -6.64089 | -60.001 | 2025-08-07 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e9f64fc-5ad8-3b4e-a2e4-9545f8fba772 | -6.63418 | -59.99993 | 2025-08-07 05:18:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19e0dfa5-adaa-3a0f-95c0-dc0784ccdbc5 | -6.76391 | -59.47988 | 2025-08-07 05:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 794d9e07-6d45-3e24-9073-5cd6c28eccf2 | -6.92181 | -52.84398 | 2025-08-07 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5fb9e6c4-ca80-3a46-bfdc-45dff72a11a0 | -6.41596 | -53.36768 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bfaea21-f8c5-3117-96a4-d9e9b05718dc | -6.95299 | -51.63066 | 2025-08-07 05:18:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e137a2e0-7cff-334d-98c4-f222e14f573a | -6.69743 | -59.43002 | 2025-08-07 05:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2788743-23ec-3d35-b545-119cd0ace2fc | -6.64446 | -58.82345 | 2025-08-07 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56be636b-af67-3db4-b55f-a42deb66f396 | -6.4154 | -53.37145 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5f3f59c-bc25-3e63-b038-99ac2c04f5a8 | -6.52457 | -45.57427 | 2025-08-07 05:18:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e3d0bac-1541-3c3f-a963-a703e097b4e4 | -5.00141 | -56.04028 | 2025-08-07 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6986d18-4399-3ded-aa7c-f8da0012709d | -5.73024 | -49.09994 | 2025-08-07 05:18:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0609be42-2bca-3c9d-a67e-b415496680e1 | -5.00185 | -56.03751 | 2025-08-07 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| aa9bcd70-85a8-3712-9ba8-d98f20ab205c | -6.76058 | -59.47935 | 2025-08-07 05:18:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| da76e974-b4c5-379b-a14a-8d53db3cd47d | -5.82149 | -46.21746 | 2025-08-07 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a797d4b1-b0da-3697-9bab-c60c49d2617a | -6.91686 | -52.84748 | 2025-08-07 05:18:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40521d3a-b82a-3071-90f3-4c2ad44c6984 | -6.53886 | -56.20947 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e460c91-c301-323e-87f7-a032648ed74c | -5.72471 | -49.09906 | 2025-08-07 05:18:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 899943b1-8948-3f4e-ac3e-c74d7fc5427a | -5.7994 | -59.22685 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 631e4ac7-3d25-3249-ba21-2deb56fad046 | -5.81232 | -59.22507 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23a22d0c-ac11-31ce-be5f-e8e478e56f72 | -5.87914 | -57.74934 | 2025-08-07 05:18:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e9f5d4c-697a-3184-bbb2-8c1541a7c6ad | -5.8207 | -46.22323 | 2025-08-07 05:18:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d9fc35a-0acc-3dbe-8e01-9c431518e0a8 | -6.6406 | -58.82639 | 2025-08-07 05:18:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd1dc2e5-4609-3f98-b051-7d0a89010bda | -5.002 | -56.03635 | 2025-08-07 05:18:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fabbd7b-6937-3490-a8a3-add56ae5e899 | -5.81841 | -59.22963 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36b5615f-cdc4-399f-bc55-ceca6d7b6634 | -6.53471 | -56.21292 | 2025-08-07 05:18:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3405c715-aedd-396d-9ae3-75280d78ad69 | -6.42069 | -53.3645 | 2025-08-07 05:18:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e62aefb7-3189-3638-8de6-2f2fc6b80ef3 | -5.80844 | -59.22803 | 2025-08-07 05:18:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45cc691f-5181-38dd-b807-3f8e8f1c6896 | -3.61952 | -52.60398 | 2025-08-07 05:18:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
