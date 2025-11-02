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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f65aa9-a1e6-31bd-9da1-a3ff35d97345 | -2.63011 | -47.29879 | 2025-11-02 05:08:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8927f4a-4a14-31cd-a8a4-01fa14337f6d | -3.50642 | -50.47444 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c74b867-3c47-3374-b0a5-4ac3948bac5e | -3.01887 | -53.96804 | 2025-11-02 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d80393d-e2c4-3746-84c2-ea0fe60e7831 | -3.6171 | -50.48544 | 2025-11-02 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 728a08f6-40be-30bf-b040-c390ec12db30 | -4.1361 | -51.152 | 2025-11-02 05:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 06312fb3-2a2a-3b0d-9889-fc3773d76fe6 | -12.8722 | -50.8862 | 2025-11-02 05:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 371ff966-c59c-3581-b154-5283ec2eb7c7 | -5.02942 | -43.61994 | 2025-11-02 05:10:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f92596c5-ae74-3523-938f-aa2962d90dc5 | -4.13812 | -51.1493 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b4fe526f-29be-317d-a4c0-34d3388ee889 | -3.44367 | -54.5541 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3b15dd0-1571-368f-8359-43b4b46d782e | -10.99617 | -54.00004 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0122af2-48f5-3404-b676-cbd1869019af | -3.55627 | -54.5707 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a1049361-9616-3c01-889d-18cb124ea9d1 | -4.14652 | -51.15051 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c986fcc5-a12d-3ff7-ad07-f4dcfb215c59 | -10.6139 | -52.1853 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3b22261c-5ce7-325c-8656-34da0524cb35 | -9.63349 | -62.06153 | 2025-11-02 05:10:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4cb6d12-a2a6-31d8-ad0a-f06c5e4569d3 | -3.80577 | -51.80507 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b0e1fdb-517e-3542-97a3-55563bf05f30 | -3.61506 | -54.23372 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 295644ce-5792-31e7-9816-2c8a9d36163f | -3.56829 | -54.58411 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42f3a230-aac6-3ebc-ac9d-b2e5155783a1 | -3.79548 | -53.88251 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe8f900a-f9a6-3399-8045-b0580017dccf | -4.70132 | -45.88194 | 2025-11-02 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b71966a4-a129-337b-8673-5af4ad630b90 | -8.52767 | -54.76099 | 2025-11-02 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85f65e41-f57f-3ab4-9247-ede20a364a2a | -3.93745 | -52.20651 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4441e532-6314-378d-aba3-a5bc79437719 | -11.08259 | -54.25156 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0485835-3c1b-3bb3-91c8-678e50f2aa88 | -8.60482 | -54.6624 | 2025-11-02 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 519a88d0-ec62-3065-9b20-794b1ba92d1b | -4.26643 | -48.71716 | 2025-11-02 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e0fc3a9-94be-3894-bb7a-cc477f6aa3f8 | -3.70822 | -53.37494 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 997bb4be-87c3-3768-a3e6-30b8905c059e | -6.00486 | -57.83232 | 2025-11-02 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf3569df-e347-3ee0-8d62-333d813a5979 | -10.5085 | -51.88351 | 2025-11-02 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84d9fda-21fb-34ad-a977-c43d45bf0c1b | -10.73521 | -46.23608 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff72aae0-24cf-3bf2-85a8-7fdbb96451f7 | -5.03054 | -43.61887 | 2025-11-02 05:10:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38bbf8eb-ef56-3d81-a63a-c7a9b462f08f | -10.99162 | -54.0043 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5764a0ac-7b10-39a0-b070-954449f3f304 | -5.03637 | -43.62109 | 2025-11-02 05:10:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1cfcfc1-ce46-3b50-bf18-a65164b67aff | -3.59812 | -53.53747 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7b59184-0f19-3e1f-89bc-683c6c185c24 | -11.57167 | -47.07941 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03877cf4-5f55-3c09-b35b-6d14062febd5 | -10.62009 | -52.18791 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8dfcd56a-ffad-3630-8a5d-d7b08c15521b | -10.5091 | -51.87918 | 2025-11-02 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af021825-15c9-391c-ad4e-1cd4e540c98c | -7.56237 | -56.15086 | 2025-11-02 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4aca8c94-a740-3855-a40d-49956c4c64f1 | -3.56771 | -54.58785 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5eb66cfe-fa0e-3948-a481-31b95c8cd362 | -4.20687 | -53.863 | 2025-11-02 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 568e82ce-5991-3bcc-aead-440915931ad7 | -8.85548 | -49.88043 | 2025-11-02 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bc310b6-c6a6-31a1-a7e0-c048cab06b47 | -3.93186 | -52.19044 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3ea9562-79e6-32f7-99a8-48951ff50b41 | -3.5938 | -54.0401 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 513cf69b-5e2e-3929-881a-bb42371b5156 | -4.14232 | -51.14991 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 71f523f2-42d8-36d6-9c91-28a7695e0a85 | -4.37746 | -49.74592 | 2025-11-02 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6ffc7a8-8464-3f95-89bf-328d7446a3fe | -10.99698 | -54.00718 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e2f3be8-d325-375f-a96a-4907312f9200 | -9.24859 | -62.20291 | 2025-11-02 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55b2f5eb-e6f0-3b63-b024-7f870049c3df | -3.89687 | -52.20835 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9fa0967-76de-356f-9a9a-7279d59b4cf2 | -9.77719 | -57.41501 | 2025-11-02 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3a124b42-85b2-3526-9ddf-8de1705324a1 | -3.80612 | -52.41277 | 2025-11-02 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5760a7c7-2d96-37a2-8746-f096ea156802 | -10.63358 | -52.18559 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f6b2a0b-0d08-3389-99b0-76b81abcad12 | -10.74039 | -46.25961 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef654633-108b-39f3-b9ad-ebb9cd596fbd | -10.73645 | -46.23767 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fa41fc2f-93ba-3978-8cdf-d71ba16439ae | -11.20006 | -53.83879 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab06b626-86c4-3973-9c7d-9df4f548663e | -10.99477 | -54.00966 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e03dcdc7-17ea-336e-b580-82d2d2d83af4 | -11.34854 | -51.45205 | 2025-11-02 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cb5802cf-6a3b-3451-98ae-98a792416077 | -9.14378 | -61.21571 | 2025-11-02 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fbd4936-5b6d-3f7e-8f65-0bef94c741a0 | -4.13753 | -51.15324 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 94d3e850-7007-38d8-a9c7-ee1260eb05eb | -10.61449 | -52.18119 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b09d4f6-819d-3801-b299-6083ee651109 | -3.44334 | -54.55383 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bc6a140-1646-382e-9658-ca6ebc9ad7dd | -7.59657 | -55.69635 | 2025-11-02 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| efa43bcc-9d28-38df-b557-87f01f9c34ba | -10.99547 | -54.00484 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0f95cc8-0c26-3ab9-affc-35576791e14b | -7.56573 | -56.15139 | 2025-11-02 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b7460cd-6b67-37a3-9bc2-db20e514a8c1 | -10.30095 | -53.77676 | 2025-11-02 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5771974b-9eae-3165-968a-52f603326596 | -10.99232 | -53.99949 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bfcf7cb-abc5-33e2-872a-798219db180f | -3.71185 | -53.37553 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c218f61-1a8d-3c9a-b4cf-f490c4f61eec | -10.72882 | -46.24742 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7eac969-d646-36f5-9f2e-1b6ff6c5288e | -5.13729 | -60.38861 | 2025-11-02 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 688082c8-ab02-39fe-8b43-0aed37790bf0 | -10.8026 | -54.90816 | 2025-11-02 05:10:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e47324f4-a2ec-3ecc-b699-39515986488c | -9.82927 | -56.16366 | 2025-11-02 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15ca4363-64ac-3b87-aa76-fa4d2a80c090 | -5.03749 | -43.62 | 2025-11-02 05:10:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3df09d5-b138-3aa0-92bb-3468d4cc9298 | -3.89408 | -52.09638 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8cf16aec-db23-3495-9ede-e69f7854a637 | -4.13392 | -51.1487 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 08ab2653-5794-36f7-97a5-f375f8ffcfc4 | -10.73586 | -46.23079 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d2c10b9-5ed7-3739-a449-2cb8be8eab43 | -4.70196 | -45.87751 | 2025-11-02 05:10:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a88fc63-2621-3a4b-889a-ea69cd38e340 | -10.63757 | -51.76211 | 2025-11-02 05:10:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70ed1b99-edda-3671-a950-b48c440ddce5 | -4.37283 | -49.74519 | 2025-11-02 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbb8146c-5959-3073-b898-da56281b31d3 | -3.56428 | -54.5873 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1e5fa81-d2ad-3f07-bbd3-578945099833 | -10.73901 | -46.25794 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1f0f4adc-1ae1-3df9-850b-2febf6b00907 | -4.13027 | -51.14441 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5dd05520-4e7a-39ac-a0ac-6c757e407bc5 | -10.73836 | -46.26321 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7c0faa2-1290-3a74-98ac-de50b50572b0 | -7.60056 | -55.69318 | 2025-11-02 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bc63030-892f-3fbd-ad44-32be60bc0cb7 | -10.73399 | -46.2588 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c805980-4c51-3d0b-9fcc-62b0943fd8fb | -3.50975 | -54.37484 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e12a34dd-1946-3bed-931d-b84778cfff47 | -4.13084 | -51.14067 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12efbb2e-4bc3-35ee-b4bc-52ee991547b2 | -3.99698 | -50.85568 | 2025-11-02 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80671990-7ab5-3398-b3ad-c133a65e3577 | -10.61634 | -52.18316 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d3871202-2422-3607-b895-ae4d0afa793a | -3.9625 | -52.22571 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff7e561e-767f-3978-9d13-d85af5ae87b6 | -10.73707 | -46.23238 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| adadcc5c-214d-3305-8020-645988939cbb | -4.08891 | -54.23159 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a4c06923-20ef-3888-a540-6f1427f55a29 | -10.6244 | -52.18851 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d84032b-4383-3995-8e64-3c3842b61945 | -10.74785 | -46.29129 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 798ace75-cd49-33c6-a9aa-0e103156aafc | -3.48023 | -59.64791 | 2025-11-02 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| be833731-722c-3003-a633-3ae9649951fc | -10.61821 | -52.18593 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65797334-a589-32a3-a4b0-ee5104f812cc | -11.34817 | -51.45472 | 2025-11-02 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc9f9106-1bfa-30d1-b207-79ab901540b3 | -3.51034 | -54.37107 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a42ba8de-d56c-34e0-b167-c58ab6dd403d | -10.62871 | -52.1891 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8a769d5-af2a-3c9d-94d1-f87f4607410e | -3.78136 | -55.44619 | 2025-11-02 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5623e20a-c035-3a4f-8e0e-6c3bacf8ad40 | -6.31764 | -52.6121 | 2025-11-02 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f25a0c1-b864-3f33-8644-9aeec22e3ecb | -4.13871 | -51.1454 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4e3681d-ae53-30e8-a72e-2851ad5cd252 | -8.60545 | -54.65821 | 2025-11-02 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4f84da4-60ca-34f0-8871-793f10f4dbbc | -9.60417 | -55.10424 | 2025-11-02 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
