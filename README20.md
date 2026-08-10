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
| 9331a892-796d-306c-b0be-b4550bf4e2c0 | -7.54149 | -55.5779 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4f6ee457-ea82-3218-bb9d-2a32cc299669 | -8.90129 | -60.57165 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 801a0883-932c-385f-82eb-81e378681fa5 | -8.96315 | -60.53797 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 16a87965-3ac2-3f22-a000-55a9cb13b09c | -11.21474 | -54.02958 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4d87654-6508-3a3a-8a61-193bf5233679 | -6.85549 | -56.40885 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82924dd5-8494-3a6b-a9e0-8225adc492f8 | -10.87988 | -60.73428 | 2026-08-10 05:48:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cc83124-c467-38a5-8c64-b543c24ef829 | -6.84969 | -56.41145 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45cba2ca-04f2-305f-b8ec-664631bb5e9b | -9.07167 | -65.4611 | 2026-08-10 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 120460ab-9e71-30b9-8a0d-fc50783ab1fb | -6.84876 | -56.41827 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eae492aa-f0c6-34ed-bcee-6f00c0e04f09 | -9.73793 | -68.42182 | 2026-08-10 05:48:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ddaa2bc-cc31-38db-a85d-1b1ad3314fe3 | -6.43423 | -60.06762 | 2026-08-10 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a21777fb-62d4-3955-a5a9-f3f80cd98d13 | -8.64177 | -63.62116 | 2026-08-10 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3d974ec8-7902-3f3a-85c7-33677f242d86 | -8.6895 | -62.87548 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 785649c7-d312-3778-b361-05ce4e9a1224 | -8.9002 | -60.57926 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d24128b8-3bd4-3330-b5b0-c2b40b4dc03c | -6.85504 | -56.41221 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b16e0510-fe93-3fb3-b80f-63066ed2d833 | -8.89605 | -60.57867 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a03241a0-20c4-3dc3-9c93-14bdc0f2de52 | -6.83492 | -56.41619 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54ef7bf9-3438-3c89-9221-a80711f5cecb | -8.89408 | -60.56286 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 36339506-ba28-38c6-bf8d-6b8d762a4680 | -8.95741 | -60.54873 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ff7e6259-2c6b-33ff-b091-577af9d11a65 | -6.84026 | -56.41701 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0fbf64b9-9787-3d8f-a6a2-ba69e80cef8a | -6.70805 | -58.95008 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fb17aee-86ff-388b-bd99-feb348cedf83 | -8.95847 | -60.54112 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 25208925-f50a-3a6d-9549-242f4273859d | -8.67932 | -62.86968 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b95be937-c5ad-3a45-8f54-cd11d859bc0e | -6.84479 | -56.40736 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20830ab6-3d7d-3b49-8002-35e5f499ddb7 | -6.83852 | -56.41334 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e26956d-eeeb-3c17-89c9-8311434c6fe0 | -8.68652 | -62.87078 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b23b4983-050c-33e5-b4ac-b4b32c5db82e | -8.96156 | -60.54936 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3fb17865-38a0-3843-9e35-23b74ac61750 | -6.85153 | -56.39785 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15a35524-def3-3079-800c-6c21330e83e6 | -6.84388 | -56.41408 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b2cbe3e-2e91-3828-973f-ba4da3a863cc | -9.64362 | -68.96848 | 2026-08-10 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e64d9832-d6db-3954-b89e-53044d6b23ed | -8.90745 | -63.96976 | 2026-08-10 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a75beeec-8cc1-3842-a562-8e5306ac8e17 | -8.0225 | -55.1206 | 2026-08-10 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d5b875c-1be3-3006-bf08-be562259e0d3 | -7.55397 | -55.57171 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e3112f3-38af-33fa-9199-ac05807eb6bb | -6.84923 | -56.41484 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 749a2094-b8e4-3d7c-bc61-61dcbbcd6f77 | -6.82528 | -56.44567 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 178f9ac2-2292-399f-a4de-4d23994eff00 | -10.93826 | -57.1137 | 2026-08-10 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| badc4487-2aa1-3655-a7de-88fd5cf2fa94 | -8.97563 | -60.53983 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dea546f1-0e67-30c7-94e9-ea91dd2ae2b6 | -8.95579 | -60.56028 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1436d192-28f6-3387-9a18-e6e5cfb3fffd | -8.89299 | -60.57049 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 921a485b-ade1-390c-af53-36dbb8451b36 | -6.81163 | -56.4267 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f85784a7-9733-30b6-9a25-a7afb581cb42 | -8.94414 | -60.53933 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 5612f4cd-4941-34ef-be11-9a3123da77bf | -6.71061 | -58.94797 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12b046b9-cfd4-3d9b-8e98-659b81bef6c7 | -8.96049 | -60.55704 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2c3d32c8-bea1-3f04-a543-00f56fa19521 | -6.84659 | -56.4109 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1d0db31-0fa5-3595-a053-5c5c21afa35e | -6.81699 | -56.42731 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ccd77ff-e886-3e59-8fdc-33c2bcb5d9ab | -6.2498 | -55.61915 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9d59d87-6ecc-3ece-8a83-3cba2ad323a7 | -7.5488 | -55.56688 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c5fc7156-7daf-3be5-81ff-d4e4a8dbe39e | -9.37397 | -57.35962 | 2026-08-10 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75b76088-ae76-354b-a391-019725f64fb0 | -6.84524 | -56.40405 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51a8eae6-a9f4-3dcd-8b57-ea2ce878ab54 | -6.83929 | -56.42377 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf67ac82-4c56-35a2-a362-8e2daa5beb9f | -8.68589 | -62.87494 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1305b2e9-5def-390d-8fb7-d4ab718136eb | -6.83945 | -56.40646 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6301e166-356c-30ff-a8d1-b46333e43f62 | -8.69013 | -62.87132 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 975161cd-6613-31d8-900a-1a54b28fbadc | -10.07591 | -60.50279 | 2026-08-10 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ea387c8-abf3-3937-b359-b8f6df933717 | -8.68166 | -62.87856 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f88dc8a-93ec-3ad1-8a00-f90427915dd8 | -10.93736 | -57.1209 | 2026-08-10 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad8c90ed-e102-3762-8236-9d38f0ac2f89 | -6.84512 | -56.42115 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a3dbcd8-0d70-3d45-9fca-c483928e3cb0 | -6.85595 | -56.40548 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c5d89a-98a4-3e1c-9d03-eb7789f00818 | -6.14387 | -57.71549 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| f94ee962-edc5-3903-8ff6-4684b728e0af | -8.94525 | -60.53175 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f0dbd175-499a-37f8-9d3b-52493682be1d | -8.94885 | -60.53614 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8d8b49cb-ed7d-3a01-9f5c-fdf53e493715 | -6.82576 | -56.44229 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dfc5639-8e1d-37b4-8ef0-1108fcc56980 | -11.22069 | -54.03603 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2061f80b-04fc-3ad3-aed6-f6d89e50c9a9 | -7.65856 | -62.54988 | 2026-08-10 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d399e3d5-aaad-3f41-a07f-66082f3ed90a | -6.87219 | -56.64098 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a53c2d36-4465-32af-b8c8-5bf6c61b0a36 | -6.85458 | -56.41559 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d97d65e2-c140-39be-aedf-91ccf2164ea2 | -11.20746 | -54.03469 | 2026-08-10 05:48:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a06c25ca-a041-3098-9b5b-7856ac29bb74 | -8.89497 | -60.5862 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| bd372123-92a9-3fea-818f-eb19aedf72e0 | -6.70742 | -58.95457 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebb72f7f-c6da-3d5a-b06f-c2344532a769 | -6.85146 | -56.41503 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4438691d-25c1-3d52-aeec-f751601aae9b | -8.95942 | -60.56466 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e220c412-d4d4-3f34-8374-ae675490d317 | -8.42989 | -70.26633 | 2026-08-10 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3bf1d12-ef78-3710-b338-d23a05fd0375 | -6.83977 | -56.42045 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ecd6436a-98ef-3e0d-801d-cc38544a1984 | -8.9555 | -60.54871 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9c3e92a-feea-3621-a170-4e38e0c2577f | -6.85241 | -56.40836 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f8872cfe-1876-3090-af86-d48bf89b5f6c | -9.06835 | -65.46057 | 2026-08-10 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21a68af0-d544-39ff-a070-1260ee738785 | -9.97348 | -67.16586 | 2026-08-10 05:48:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4b0201e-35cc-384b-a6a0-4e327e788d40 | -6.09838 | -57.6961 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf49e510-beb2-37f2-ad41-7cd8656a6a68 | -8.95794 | -60.5449 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c739597f-43dd-3c7b-a978-cd437ab8fd4d | -7.65919 | -62.54568 | 2026-08-10 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c976da24-c3a7-3848-aa04-be8535e87bc1 | -6.70994 | -58.95246 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 936e2b15-3271-3056-83cd-dcda62c685c9 | -8.90074 | -60.57545 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ddb4ac7f-00f8-363c-8247-20b19b680219 | -7.48231 | -61.38154 | 2026-08-10 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9afdd36d-f3ce-3f11-a6eb-303b076cee90 | -8.95067 | -60.53611 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d72831d7-0e16-3ca5-bb48-54cd6545e3d4 | -6.24927 | -55.62295 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61c5e732-efcd-366d-9d5d-bd7458131d6a | -8.16801 | -61.51891 | 2026-08-10 05:48:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba40d098-c248-31d7-87f6-0295dfd7c43e | -6.83009 | -56.41187 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b02e625-d4c8-3da0-a72c-d7b850683e62 | -8.95837 | -60.57214 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bbfd611-c086-384b-9cfd-9449b7661ba2 | -8.67571 | -62.86913 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9d2888f5-1628-30e6-8f07-afc8e4c6e756 | -7.54934 | -55.56287 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f84190df-cce3-3a47-8cf6-8d4c1ba6c77f | -7.66281 | -62.54623 | 2026-08-10 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0dbb86c6-3a90-31c8-82b1-b444aca71eae | -8.68229 | -62.8744 | 2026-08-10 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92e90c24-39a9-31ab-a5e1-90037788ce3a | -6.8422 | -56.40342 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d10804c2-7946-3d74-a1b1-1b15a2f22e6a | -9.06464 | -60.39503 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 166e5712-0449-31bd-9104-882f1f6dd819 | -10.93285 | -57.11301 | 2026-08-10 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15bd8b6f-a7a7-334a-96cb-16a75d38fb3d | -6.14796 | -57.72154 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dcb5d4c7-551c-3ab1-a3e7-7c7507ed62f2 | -6.24371 | -55.62194 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 949b8f63-2741-39d4-a138-84eb82580a08 | -7.55451 | -55.56772 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe1e898b-1530-3c40-bbb5-41c97094c09d | -6.85014 | -56.40813 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 43234cfe-3ae9-3b81-beb6-62c76a3cf164 | -8.89462 | -60.55909 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README21.md)
