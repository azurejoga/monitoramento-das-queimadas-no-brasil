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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd31fbf9-1172-3a7b-82fb-1c469ccb3db9 | -15.44307 | -48.43795 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bc1f3cc1-c425-32d7-8366-ddd7a85d285d | -11.69351 | -50.99143 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2c65e839-3feb-3873-8bb0-720a2bca8551 | -12.84354 | -44.33584 | 2026-09-22 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 4c44b954-086a-3ba8-a7c6-8ddb02e4d9cd | -12.54319 | -50.06457 | 2026-09-22 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dec6f500-d666-342c-9d8b-e9673083f204 | -13.40445 | -49.47703 | 2026-09-22 04:49:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2779d338-1402-3ca7-b284-b0ee54b8d007 | -13.20972 | -51.72401 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a85fda34-ced2-35f4-9081-52caf052aab6 | -12.56328 | -45.97573 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 427a6ba6-23f6-315c-a615-87738918aef8 | -13.87768 | -48.56565 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b9379e41-34b7-3807-8fed-e64cd421de4a | -10.88087 | -53.96283 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68a0f17d-e46d-3d67-a1e6-438eeef01fe2 | -10.60549 | -53.99018 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c636c0a-2ba2-3c56-a84e-c8269a8d1962 | -11.33088 | -51.36678 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4017c2a-ec0f-3d3c-8ca0-de3260a3248b | -15.56755 | -48.79469 | 2026-09-22 04:49:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5cc4a0c6-a01b-3313-85ab-315a70541c70 | -13.47155 | -46.9148 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab175000-3dac-3ba3-a3a0-5829d30f414b | -12.88978 | -50.93639 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8c62166-2aeb-3a6f-99dd-2619f5534b9a | -13.92834 | -48.56759 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cf42be38-b5b5-37c4-9208-63e00fe11050 | -13.22359 | -46.93244 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| caa82c7a-8aa4-306e-ab3f-f0f1830cee7b | -11.41839 | -47.34429 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7320c86-dfcb-3983-8369-259beb325688 | -11.94723 | -46.51524 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f41e73-3092-36fe-9d2e-9b0f8b281b88 | -12.43564 | -47.01133 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5f65d79-9284-3105-b345-b3e4cd463dc1 | -13.29833 | -51.76699 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87d1d3ac-5655-3922-89b1-2afca2834447 | -13.51584 | -51.52327 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68fed16c-601b-399c-97ac-320b4c4b680f | -14.75179 | -48.43325 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2dd860c7-2a86-35c3-841a-2bd5d589d1db | -12.086 | -50.02701 | 2026-09-22 04:49:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69979b3f-abef-3eed-a958-7c9f45a83f8f | -11.16236 | -51.11326 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 48e9275e-0b05-3ea0-99db-d9eb4ab15a04 | -15.25523 | -47.60728 | 2026-09-22 04:49:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aa5c2f19-c0c8-313a-b3b4-32355f0640b4 | -10.90136 | -54.0729 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b75fb2ce-35a1-3824-a588-20c7b10dc05e | -13.86637 | -51.853 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3b5ab556-ff05-3fa5-a7a6-a2f14e7253e0 | -12.4029 | -47.06502 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9378c11a-74b3-3d0a-9341-c4a48b88675c | -10.72174 | -54.00922 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a3e9b37-31aa-3d70-8709-0e59b8b726e1 | -9.89651 | -57.05887 | 2026-09-22 04:49:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1d42945e-e891-3945-bc59-962831efe386 | -15.3582 | -48.1126 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 846945cc-44ed-34fa-b7c4-4270a47a40d8 | -12.14155 | -61.16346 | 2026-09-22 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d7a276fd-35b3-3648-9f9c-4d0f9bcb7169 | -15.44864 | -48.48613 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdb0f6fc-58b9-382c-8476-f724990809db | -11.15396 | -51.1009 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 0b00c5f1-c913-3998-937c-76861cd3c0bc | -12.36474 | -50.19954 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fc2724b-c502-3d70-80f2-d83f9cdfdd58 | -9.29782 | -60.53504 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f03971d3-1926-3b7a-b7a1-8ce3f5fed26b | -12.77167 | -52.84394 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e113adc-4cc3-3757-b5a8-1cea33deb209 | -10.9098 | -53.95619 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 286a8837-dfe2-3f0c-bd7d-5484686d26cb | -9.76562 | -65.05785 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72c9ee88-8ff0-307c-9c86-d1d0a3192f90 | -11.84176 | -46.81878 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd730bb3-1d29-3487-85a9-4fc4c8220ede | -11.1629 | -51.10966 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5d4b5b5d-6a4f-3384-a1ae-5cbaffafb956 | -12.56725 | -45.96979 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| efbd0642-9959-31a9-92a1-17ae50e1d4a5 | -12.9532 | -50.93097 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ce01c1b-963f-30a2-8f85-dfb6217be768 | -12.84931 | -54.04602 | 2026-09-22 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2bfd05a6-6fb5-3dee-8658-ec66af192288 | -13.21462 | -46.93523 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 071bd102-5bdd-34b5-b234-7cd2f04b109e | -12.77387 | -52.85151 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9578a1f6-2730-3a9d-b8c3-f6e38ca154a8 | -14.93104 | -49.95442 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6088ce72-6128-300b-aea3-52d5bbb96546 | -11.32402 | -54.04651 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d7711d-b46d-317a-b5ed-a99051f41303 | -9.19169 | -65.85612 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62562112-9557-328d-9e6d-872ec35ee098 | -14.31468 | -50.49006 | 2026-09-22 04:49:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02d68032-063d-389c-b146-1be071b8cad7 | -13.33734 | -51.31192 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1f48537-59c0-378d-9ca9-097d20917106 | -11.69969 | -50.99613 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 8fb03a23-457a-3a68-9a2b-8c2237469792 | -13.27616 | -51.32866 | 2026-09-22 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e9cdb61-3f3b-3da5-8e51-446c28efc14e | -11.01617 | -54.14509 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67857b48-a20c-36ac-bea4-a2d63e55d9e5 | -12.03112 | -47.81339 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 18455018-0d33-3ce2-bd21-a56add8d514c | -10.15339 | -58.76127 | 2026-09-22 04:49:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc07ce96-39fd-3fd9-97be-e6dba80b02ff | -11.34984 | -51.39894 | 2026-09-22 04:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 348f449f-62dd-37a0-b6ce-015ca27101a7 | -11.7782 | -47.44175 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1aba6a5-29c7-32cf-9ff9-4fa386abf3ca | -10.90196 | -54.06918 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ff545e3-155b-332a-a016-e4eb8afa5e67 | -9.186 | -65.84779 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67d843da-9090-357d-9328-7fdc7b5e1570 | -15.59888 | -48.32417 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 830e2f8c-22b6-376d-92c1-2da45110524f | -10.71774 | -54.01239 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0347bc4-1ee9-3745-9864-954664fdc230 | -12.43291 | -47.08047 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f114847-009a-3543-9419-af78f4f3bde1 | -11.31844 | -54.03799 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fe859ce8-cc9a-36e3-bf73-dd4f01817368 | -16.66022 | -49.28416 | 2026-09-22 04:49:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88d8da3f-eaad-3748-a013-cf8b6868b328 | -12.56389 | -45.97118 | 2026-09-22 04:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 75710778-2744-3d15-ade7-509f442d77f2 | -13.33452 | -51.3077 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0689efb2-e073-33da-b1fb-adecb1000bc9 | -13.22256 | -46.94033 | 2026-09-22 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3392aec4-ac55-33af-a4b8-2145948e7a27 | -12.96287 | -50.98899 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a87e1837-ffbf-32df-88ab-20bf381e1f74 | -11.32243 | -54.03485 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9fb794c1-7762-3652-a392-35eb46e48043 | -10.52791 | -54.49127 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa5b316d-7fe6-3f17-92d0-eb036b8886ef | -14.69443 | -45.67863 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f057c5b2-8620-35f8-a111-84cd26a71e2a | -15.56867 | -42.64083 | 2026-09-22 04:49:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2a2b31c1-53fd-3708-b931-41d7b56d6ce5 | -11.96619 | -64.04143 | 2026-09-22 04:49:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2089ee3-9690-34d9-81f1-af553e77206d | -15.35558 | -48.10131 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ad3c60-3734-3816-be61-a2872802b140 | -14.76989 | -48.44708 | 2026-09-22 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d602c70f-a314-3d81-adfb-d7f98255a511 | -14.58553 | -52.17371 | 2026-09-22 04:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a95546a1-6c96-3b95-bb1a-ce4b8da400aa | -14.94308 | -49.89616 | 2026-09-22 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37c3a6ab-ae79-3584-9314-78efe6aecdce | -14.1745 | -47.87202 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04d081ba-a00f-32eb-bd7c-4d1b07afe6cf | -12.44143 | -47.01563 | 2026-09-22 04:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4094caa8-42d8-3892-93a0-984b5b38c51f | -15.36223 | -48.11316 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9ca02e9-ec5b-3c81-986b-3eddf4f61c1a | -11.32462 | -54.0428 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 53cf96d1-e616-3ad9-915d-b29958fc36ef | -11.43839 | -47.34755 | 2026-09-22 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d63c8ae5-dad5-3fb4-8031-a9bb90c0b193 | -9.27968 | -60.62122 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5d69376-32fb-330c-a017-ac98c70b8581 | -12.84266 | -50.99 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e5ebbbe7-91b4-383e-adae-c4f1c8cb71d9 | -12.84282 | -44.3417 | 2026-09-22 04:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d6a6e19a-8837-35bd-b4b8-b486f5083603 | -12.92673 | -51.01462 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de660900-70df-3354-92c9-384821e790de | -13.54217 | -47.66515 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0186e51d-12a3-3426-a0ac-98a71d89d856 | -10.92058 | -53.95414 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27473761-a3c9-33cd-9f14-eaec1a928a30 | -14.67627 | -45.67109 | 2026-09-22 04:49:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b420d560-d6a7-34a8-8a18-ddc45bfc0e7f | -15.35914 | -48.10548 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 283a802b-0e81-32f3-b5d3-ae35e6efba6e | -11.84696 | -47.60891 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec0e8b20-e23a-34d0-964c-9a8c115fa33d | -15.44469 | -48.48563 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9b16b69-6c7a-3b72-9eee-c311b8c2659e | -15.44238 | -48.44312 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e88ab7fc-7f88-3783-b6c7-3f23a5682724 | -12.8499 | -54.04237 | 2026-09-22 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9dc522e0-3df5-3efc-abcc-7b32b29e319e | -13.91681 | -48.56591 | 2026-09-22 04:49:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a596204e-c9f5-3bb1-887a-a55f0acc867b | -10.15124 | -58.76348 | 2026-09-22 04:49:00 | NOAA-21 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27b1acdb-0c0c-3b3c-9efe-013a4479c723 | -15.35867 | -48.10905 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0b448df-f3f6-3db7-a61f-19b37fc5ec64 | -10.87869 | -53.95488 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 758b3da7-6997-37f1-b995-353623271c92 | -11.1668 | -51.10659 | 2026-09-22 04:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |


[Clique aqui para ver as próximas entradas](README70.md)
