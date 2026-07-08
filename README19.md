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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b9fa5d3-f563-3f61-a207-1c73fbae2ac2 | -21.79685 | -56.27245 | 2026-07-08 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2424fdde-b703-333f-91ec-d94bd3b0ff53 | -21.36983 | -49.16515 | 2026-07-08 04:27:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 33ee032e-c090-3d8f-b9ef-aba5e883d678 | -19.63427 | -47.5837 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f868778-b42d-3667-ab18-523acee83194 | -21.41762 | -47.05937 | 2026-07-08 04:27:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf6869bf-273f-3b89-b314-347a7a4ebacd | -19.62046 | -47.58505 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e6569b6-6216-3005-a0dc-b6edbb82d6b0 | -19.08798 | -40.08742 | 2026-07-08 04:27:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dda8fdd0-d70d-3d77-abc4-63c51937badb | -20.42123 | -41.5881 | 2026-07-08 04:27:00 | NOAA-20 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f7028815-aa22-3150-9a70-a979b0cb9e31 | -17.57096 | -54.04469 | 2026-07-08 04:27:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a19b4c34-8cbf-3531-a304-aa21cb59d557 | -19.63758 | -47.58427 | 2026-07-08 04:27:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dd4b8b2-a6bc-3d46-a463-04865f6ada4d | -27.5633 | -48.66066 | 2026-07-08 04:29:00 | NOAA-20 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4e0d0f9d-8802-30a1-a846-c34c1a3cf5ff | -23.61967 | -51.78221 | 2026-07-08 04:29:00 | NOAA-20 | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e5429107-9543-33eb-889d-face01842fd0 | -27.65525 | -48.70135 | 2026-07-08 04:29:00 | NOAA-20 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 71814b28-2034-3f17-a6b1-7aaad9269f8d | -12.7553 | -44.5194 | 2026-07-08 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a058e864-c0c2-397c-afae-8700ac89da6a | -12.7548 | -44.5428 | 2026-07-08 04:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 59c8d5be-6da8-378c-8e57-33d84190856f | -21.8033 | -56.2729 | 2026-07-08 04:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 43.6 |
| e3a91960-32f6-36bc-b42c-7461519747f9 | -12.7553 | -44.5194 | 2026-07-08 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| cfd412d1-e975-35bc-9725-5156c0868fa4 | -12.7548 | -44.5428 | 2026-07-08 04:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| c811245c-f7fd-35d9-8f5a-5342bee23f56 | -9.2258 | -48.5782 | 2026-07-08 04:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 00023731-952e-3e01-a7df-366e9521e011 | -12.7553 | -44.5194 | 2026-07-08 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 6229a7fe-bd6b-35bf-8dc2-db05d40a65dc | -21.8033 | -56.2729 | 2026-07-08 04:50:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 37e1fec4-b775-3ec8-bd47-7eda218384ca | -12.7548 | -44.5428 | 2026-07-08 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 12509b7e-ca22-33d2-821c-ab4662bf82e9 | -21.8033 | -56.2729 | 2026-07-08 05:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e0297232-92ec-34e3-8406-cc2954f7b610 | -12.7553 | -44.5194 | 2026-07-08 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 445af0ca-cf8c-3279-8654-6dc0c1a7d274 | -12.7746 | -44.5162 | 2026-07-08 05:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.3 |
| f94a7402-37d4-3e2a-92c4-0fa82089fed9 | -9.2258 | -48.5782 | 2026-07-08 05:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 677398e1-1a81-33b1-a3ef-e59d1b29f844 | -21.8033 | -56.2729 | 2026-07-08 05:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 47.7 |
| a25dfeb0-d9db-355a-a966-53059d980f67 | -12.7553 | -44.5194 | 2026-07-08 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| c36f7737-c408-35c9-a5d6-a30b7ff50d48 | -12.7746 | -44.5162 | 2026-07-08 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| b2e814ac-613a-3a5f-adf7-315abc10cc44 | -12.7548 | -44.5428 | 2026-07-08 05:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 9699ef49-d586-3638-8e5d-ebd99850aaea | -6.59732 | -51.69412 | 2026-07-08 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab4f29bf-2355-3d34-a00d-5200bff53d9c | -5.67026 | -44.30545 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70467d94-6ae5-30db-8073-9a851af272fc | -5.30842 | -47.24189 | 2026-07-08 05:10:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df880361-c651-36d6-af3a-0128593152c2 | -6.42829 | -55.80001 | 2026-07-08 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5194eee1-e8fd-3eda-8ed1-ae5580a1c4e0 | -7.63968 | -50.02004 | 2026-07-08 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ae1e549-3ee6-300d-8641-828bd3335728 | -8.12802 | -47.10031 | 2026-07-08 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ca106f73-32fe-3b5e-8285-36ea6a9bc9e0 | -5.79988 | -43.80445 | 2026-07-08 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cbc64da8-117e-327e-aa04-66dfbec8edc1 | -3.51425 | -48.04046 | 2026-07-08 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| defe2eef-db50-3846-a74d-1475af0c4ff8 | -6.4115 | -51.23465 | 2026-07-08 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 006e9ef0-cc4e-3d4b-9a1e-107c4f92794c | -2.98303 | -54.6058 | 2026-07-08 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66add488-296e-39ed-a6c2-16ece4dd3adf | -5.66622 | -44.31353 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 487a74f4-ee0f-319c-9548-4e2994930678 | -7.90232 | -48.25784 | 2026-07-08 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcd89efc-925d-3f1a-ba70-52b2207ca63e | -4.26489 | -48.61127 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 978e6c91-f6c8-31b8-80f0-c16085373784 | -7.30141 | -46.24818 | 2026-07-08 05:10:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2afb0118-f940-363e-9d7c-1d2626883c92 | -6.9446 | -43.70416 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ece4862-9e98-341d-95ef-5a371ed8d6bb | -7.75817 | -48.41721 | 2026-07-08 05:10:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2083731-d37f-3c81-8115-0c8996fc27d4 | -4.26446 | -48.61417 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 808f71f6-13f4-339f-a632-56a0515ade05 | -6.91895 | -43.70296 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3348f163-9e32-3d2e-ae37-0437f8e5feab | -7.64493 | -50.02107 | 2026-07-08 05:10:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e34e5474-6609-3cea-bcf9-e9d6b0a98bb5 | -6.91531 | -43.70748 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b4932e7-e442-37e6-a03c-b085006785f7 | -4.34446 | -47.7637 | 2026-07-08 05:10:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a1ce766-cbb7-3862-90af-f807f386ff06 | -7.75969 | -48.41993 | 2026-07-08 05:10:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ff65f01-b023-36c2-9795-c3dd56e2b2d5 | -6.91443 | -43.71447 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 41c29ab1-c123-32e7-9610-e8a1e90e9d6c | -5.47224 | -45.4269 | 2026-07-08 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66bfb35e-8364-32ec-93b8-b3328e1883dc | -5.66271 | -44.31068 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 705a7929-0a99-3009-af07-d96f90bc0437 | -4.87197 | -48.91192 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 01f549ba-b2c6-387c-b7fb-4949f5538167 | -5.96434 | -51.40504 | 2026-07-08 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0c28e157-3b70-3ba6-9bc1-db6c72976a4f | -3.66068 | -48.95773 | 2026-07-08 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55d9360d-10a5-3722-ac6b-ace58858bd07 | -5.66353 | -44.30441 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c6f2857e-c4c9-3bd6-b874-e7898daa7ea5 | -7.89967 | -48.25935 | 2026-07-08 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcf26146-6c8b-35b4-8449-761c839fd5a1 | -6.90385 | -43.70796 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9ea4f31a-3547-3355-80f7-f84fade2f49d | -4.57489 | -48.03 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3df947e-6e4a-3b06-add3-46e4aaebeb8e | -6.43221 | -55.79691 | 2026-07-08 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df9e0644-3e31-3db4-bfe3-2fc99c501af7 | -5.66795 | -44.30103 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac97dc50-a24c-3487-9faf-7f654d947ca1 | -4.29148 | -48.35701 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8dfa944d-235e-39d7-896c-99f637e8efb5 | -7.90014 | -48.25595 | 2026-07-08 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97c0e61b-9622-328c-95be-0156ed4add73 | -7.90277 | -48.25441 | 2026-07-08 05:10:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb13e6ea-43c0-313f-941e-ac72002613d0 | -6.92605 | -43.70387 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a681cc1b-a5fc-3993-b91f-141bae16efe2 | -8.12164 | -47.10346 | 2026-07-08 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dad55028-5ccf-338f-9775-8255637c3024 | -4.94694 | -48.24525 | 2026-07-08 05:10:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9cefe4d4-5026-3b35-ab81-b29c7c9acddb | -6.9162 | -43.70045 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ffc3ca11-590b-3d79-89d9-047023538bae | -7.30138 | -46.24338 | 2026-07-08 05:10:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 404370b8-8df7-379d-8da8-3987ac354b06 | -3.49373 | -48.037 | 2026-07-08 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9cfda2d9-5a7c-3d25-b726-ace7ae8289ee | -3.51468 | -48.03761 | 2026-07-08 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d649a6f-16ed-31b2-969e-a4e321b9464b | -5.79889 | -43.80578 | 2026-07-08 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e204cd8-c690-37cc-8011-bc37c3e43ee9 | -6.9251 | -43.711 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 05a2925b-4186-32b0-8239-c6e12a328058 | -5.34418 | -45.35265 | 2026-07-08 05:10:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5332b92b-b281-38fa-8a06-f27d01a861e1 | -3.65989 | -48.96312 | 2026-07-08 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2168fc66-e166-3ab3-900e-137afff1c83c | -1.82668 | -54.48023 | 2026-07-08 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04f55bd6-f206-3a5d-ad68-e7969d8ecc47 | -1.82328 | -54.47971 | 2026-07-08 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bac71345-3044-3bee-92ef-7354fe419dee | -6.91801 | -43.71004 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0dc3e522-aa09-349a-8f5f-b111b0e4b4ba | -2.98644 | -54.60631 | 2026-07-08 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dae2d815-d599-3fb9-b996-a4598d5c0c8c | -6.41329 | -51.23576 | 2026-07-08 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c124bd2a-4666-34eb-b387-e0489f9ddda1 | -6.42884 | -55.7964 | 2026-07-08 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7585cf67-9e34-3503-b37a-35df10ca51fe | -6.93659 | -43.71039 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 068d6642-cb3c-3a1e-b23f-ff5a5e1d373e | -8.12746 | -47.10453 | 2026-07-08 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 75e75d60-f838-3763-938c-14940a7b6f76 | -8.11962 | -47.88368 | 2026-07-08 05:10:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c30c6569-1e50-3a21-b8ff-0793d00592df | -4.94652 | -48.24822 | 2026-07-08 05:10:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cef8c24-08f7-32e0-ae2b-c9042a9a7704 | -3.50954 | -48.0368 | 2026-07-08 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aeecec3b-8093-3005-a7e0-1056c9412954 | -6.92949 | -43.70944 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5b7f6e5-91f3-3392-9014-19c69cdfadaa | -6.92151 | -43.71548 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 579cea61-c600-3244-a0c6-ceff2d786193 | -8.2019 | -49.47744 | 2026-07-08 05:10:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87a51410-39cc-3477-8c95-92e510176333 | -5.80075 | -43.798 | 2026-07-08 05:10:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc1357b0-fc71-316a-b690-222e2727d2ec | -4.28636 | -48.35639 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab2dcb36-803f-3ff9-8458-f042aeca88c1 | -3.5091 | -48.03972 | 2026-07-08 05:10:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8c8155a-f4b4-301b-b9d1-ef2795a66bab | -7.30074 | -46.24813 | 2026-07-08 05:10:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 66afbc74-6d3e-3cd7-b87a-72cbf97b2627 | -7.30202 | -46.24343 | 2026-07-08 05:10:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab21bd63-c8bd-3259-b399-dfb1695d9f57 | -5.65949 | -44.31253 | 2026-07-08 05:10:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f4098a9f-071b-34bb-8fb2-28653cbba1d3 | -6.91709 | -43.71697 | 2026-07-08 05:10:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7eef7880-b173-3382-908c-2c23b0ac9237 | -4.57011 | -48.02605 | 2026-07-08 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9023870c-7b09-3270-9439-11ae5c277b4a | -6.43166 | -55.80052 | 2026-07-08 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
