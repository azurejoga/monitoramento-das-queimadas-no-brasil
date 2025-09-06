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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90d3eace-9139-3562-ac8d-c3ecb200daa9 | -10.23417 | -50.54637 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51445397-dad4-3cba-8606-404b58bbcbd5 | -9.70368 | -49.48957 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 83722f77-3d29-3574-8578-89fcf6b35b0b | -12.98773 | -48.04878 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1f12025-91a6-305e-be75-e52894113475 | -11.49781 | -55.5268 | 2025-09-06 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64cb4993-dd7d-3b58-88f6-0b9b04e42cbf | -12.98447 | -54.78977 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c29400e-483e-3119-b73e-0c43fe4e3c28 | -12.96173 | -54.82558 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec5b6700-58e5-35e1-8160-3d0488318d4b | -12.63147 | -56.98733 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68c32098-f020-3afe-9f16-db47a2def4e5 | -12.96855 | -54.81504 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2707b8ab-c01c-3f79-86b2-0ef59940780b | -9.98752 | -51.62474 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4af06322-d36e-3d3e-bd64-0bfc670fe7f3 | -10.75649 | -46.35088 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e112c92-918e-3812-9ceb-42b61c7a0197 | -11.08855 | -51.99855 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b054f64-3cc1-3368-90e7-b2ddf4dad13d | -12.96803 | -54.79606 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae3c756-292e-36fb-9831-01e10641557e | -12.96322 | -54.82353 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ec26f8e-bd41-3a7a-94ce-a994a2e97a8d | -14.57672 | -48.07876 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1342c754-8d3a-3c7b-9d91-3b57fc2cc9dd | -15.69089 | -53.58725 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c556706-1d9c-3254-9a3a-b8ce8d83d434 | -10.24244 | -50.55845 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd0e853f-d58b-3612-a381-39d438692cf4 | -12.99835 | -54.82034 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5e4fd771-d4b1-319e-a227-740b96c195e0 | -11.59081 | -52.19012 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0ced33c-9839-3924-bc68-e4612fa8e6ce | -12.96403 | -54.81894 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 48a2ff7a-4a64-314c-9c2a-cced5a50f36c | -9.39331 | -54.74914 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac3f8849-50f8-332f-82c7-5a7bd27eff28 | -12.96328 | -54.81638 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b0d2acc-29eb-3aba-b7b3-fe4077a45f5e | -15.06895 | -50.06947 | 2025-09-06 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e6bcb4d-c3b2-322a-9ffd-3a448562d7dc | -14.57285 | -48.02251 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44b3a6ea-976d-3d35-82eb-6e493f263224 | -12.48577 | -53.85046 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e990732-dd6f-3df9-9ab3-2c61c99d9459 | -9.24551 | -57.07712 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c295cff8-6046-36d1-9855-fc9fad3daade | -11.68772 | -52.19849 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4573dd9-ffcf-31c8-a6e8-f9040be0a6a9 | -16.60528 | -48.94975 | 2025-09-06 04:40:00 | NOAA-20 | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd8d949f-f068-3567-836b-b0fb983a3c84 | -9.70646 | -49.49362 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f9661530-7f31-3fed-a239-2869f7405b9a | -10.60021 | -44.33052 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 5abef2ab-62d5-3a4e-89fb-ef079264d100 | -9.96767 | -51.66225 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f1d388d-ed95-3976-92f8-bbcf7413ba0b | -15.86028 | -52.28953 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1e57614-9923-357e-ae1e-54b8476d23b4 | -13.90148 | -48.02176 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02fb0652-6bb3-3860-8832-fcab26fd8146 | -16.41672 | -47.82286 | 2025-09-06 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 846e4678-f11b-38db-8f75-da5676bab097 | -12.99756 | -54.82489 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c120db97-964f-3ea6-9932-3aeabe75fb4b | -10.78276 | -47.75134 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04588659-c1e4-36bf-9041-691ea29bf08d | -15.7257 | -53.58974 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cae9d51-1157-3967-9343-3515261d0604 | -16.32534 | -52.95937 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87605e65-2417-366b-a22a-3036817aac09 | -13.71714 | -46.91351 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 834cf49c-d166-3e09-902f-0a5996ba9c1e | -13.00363 | -54.81197 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2837178-d04d-3273-a40f-e51923970b31 | -12.4698 | -48.03866 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 335339bf-e509-3a0f-8838-91a9c8587ca3 | -11.00359 | -46.02277 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d2801a7-1232-3b8d-a7fa-2e78cfbdf1c7 | -12.95304 | -54.78622 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc6e67ff-b312-333e-8a52-eb3fe7cdd8e5 | -12.60432 | -56.99073 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9226fdb6-7ec9-320b-ae06-6e798d27a0aa | -16.29115 | -45.68458 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da855616-db5c-325c-b945-9e3487f2a525 | -11.10981 | -52.01702 | 2025-09-06 04:40:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f0e8af6-aee6-3f62-90f8-5bd944f25d8c | -13.01015 | -45.22414 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cb0a73c-ebb6-3b52-8048-9cb61229a4b6 | -14.57244 | -48.03022 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 451d1edb-8225-33d0-9f07-b4941fbab962 | -10.21753 | -49.72225 | 2025-09-06 04:40:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d30fe574-5b0f-3e90-b5ca-774f23ab1124 | -10.60884 | -44.33173 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 261f06a6-00c7-3d92-b0f3-f77eb875118b | -13.04999 | -47.10081 | 2025-09-06 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a53ac598-4ca2-3c98-991b-406b378e9af3 | -9.98811 | -51.62113 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95354da6-da9b-318e-9efb-3a5aa782abc4 | -11.61387 | -52.19778 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd005598-cc0a-37e9-80d8-dc3e8b70fcb4 | -15.72888 | -53.57062 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9d8670b-61e9-38e2-abc7-ad35b2034672 | -10.13554 | -55.16223 | 2025-09-06 04:40:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5941c2c-15f1-38b4-bfbc-514a8ddc41a0 | -15.7214 | -53.57326 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ff635e1-f09e-358e-8f14-476f71f7820d | -14.5754 | -48.00505 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f8dbbf4-b935-370b-bf8e-81884e1de582 | -12.95026 | -46.57112 | 2025-09-06 04:40:00 | NOAA-20 | NOVO ALEGRE | TOCANTINS | Brasil | 1715150 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d4f98910-2abf-3f0b-ba9c-dd1b19cc5f01 | -13.55112 | -48.12282 | 2025-09-06 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b86d3d9-59ab-37d5-b1ed-81f1ada959ac | -14.58035 | -48.00019 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fa54cc0d-b4e3-311b-a0ee-e75908c5ae20 | -14.56267 | -48.01601 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 443fe3f7-ec51-33ce-8adb-031e65a28395 | -14.57604 | -49.13172 | 2025-09-06 04:40:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5fe4580-5637-3b0a-8622-02b81d19c689 | -12.49793 | -53.86535 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9963bf82-10d7-30f9-91c1-5346fec8ec74 | -14.3368 | -60.32879 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d4b334e-ba5b-3c33-a71d-5013d2c21a37 | -11.59419 | -52.19068 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d62f724c-809c-3a18-8318-c73db6287f45 | -13.00128 | -54.82557 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b086ed71-30b5-3540-8801-7ea8fa688ad1 | -14.57911 | -48.03548 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07dca8e0-226a-33e6-b473-eeecba048c33 | -11.60574 | -52.16244 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 123cd849-c753-3acd-98a0-7c6fa654e2fc | -16.32046 | -52.94715 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de07a9a8-afa0-3109-a5ed-be2a18457d30 | -11.48862 | -55.50906 | 2025-09-06 04:40:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3c8016a-b96e-3b1c-922d-276759049fdb | -12.1811 | -53.89593 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8448b28f-8318-39c4-bf5e-1827b581b493 | -9.68289 | -51.10565 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6372038-234c-353a-b596-29357aa67606 | -10.44681 | -53.60976 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58d53168-7e8c-30a2-bf2c-fc872e580a1e | -12.55626 | -41.3063 | 2025-09-06 04:40:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6cc1627f-5a46-3663-a95c-e188393b7043 | -12.96669 | -54.78183 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36923674-70fd-31a1-a97a-240d828517a6 | -12.9776 | -54.80721 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0dd0f01-6599-3c0e-8e0b-c627fcd33338 | -15.18861 | -48.04664 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3dd34522-96d7-3f8e-ab5f-251426314189 | -15.72355 | -53.5815 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ef88bd7-8c01-3ee1-8953-4ee7169e4f7d | -12.95211 | -54.81435 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26a4ea58-3f50-33d3-9e83-9cfe25fb6edc | -15.72656 | -53.60571 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c5997b5-0125-359f-94f4-3a5523c8707b | -13.71297 | -46.88767 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a21e1cde-ba96-3664-be0c-4a89b50dc2cc | -15.63855 | -41.85767 | 2025-09-06 04:40:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f2d7e41e-efb3-35f3-8e09-828c19727434 | -13.26372 | -51.80614 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a61690a7-498b-3acd-ace6-37bd38a0f6d0 | -14.57491 | -48.0125 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0fafe38-7792-3461-8b3c-3cab72e15abe | -9.68176 | -51.11273 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e9da7f7c-13b4-3a2c-94b4-18b4d9793f5e | -9.68183 | -51.09098 | 2025-09-06 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 019d5ff7-fff9-333d-b820-512603b05f48 | -9.24179 | -57.07158 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a07b52a2-dee9-39bd-8193-41c859d45272 | -15.54011 | -48.40661 | 2025-09-06 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff97939e-ed39-3dbc-9c67-8a8c02ecc989 | -10.97198 | -46.81555 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 389ab0e0-5337-3cf2-a4e9-8a91dc51c61c | -12.9096 | -48.01789 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e1e6e20-f149-3972-a518-a078296afc6d | -13.8898 | -47.9497 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd6867f8-c39d-33ab-858a-40f11dd3948d | -13.2909 | -46.845 | 2025-09-06 04:40:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 119b8699-3f5b-3a33-969b-2d38ad05bcbf | -14.11459 | -51.71407 | 2025-09-06 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd702440-f00a-35cb-bdd9-f873d6ae9b4d | -9.31913 | -55.22304 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 487ecb53-6310-3823-aaa4-ea072aad1507 | -12.98558 | -54.82748 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ded8ec92-319a-3474-81e4-029e340d7b61 | -10.77374 | -48.27434 | 2025-09-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9f09be1-8cb3-3c42-8262-1d7177730707 | -13.32791 | -51.72535 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b19a599-a2bf-39d2-9858-dbaf556a204c | -14.18332 | -53.06932 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cdb8c913-3645-3bcd-906f-fcb8ddbf4eee | -11.01229 | -45.93266 | 2025-09-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dee079ba-bb29-352d-831b-26b3949cf4a8 | -16.32992 | -52.95253 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 13990526-812a-3d0c-a171-e1ab801ae994 | -13.00049 | -54.83013 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README68.md)
