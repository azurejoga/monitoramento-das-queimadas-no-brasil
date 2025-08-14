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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec493639-3537-3759-93d3-8d136f3470f6 | -10.00843 | -59.2192 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb6f8ae4-2756-3fd2-9ac5-d51115579bef | -7.87495 | -61.81224 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42f21c29-be64-369a-a33c-8c2f35c2c8e4 | -9.16855 | -59.67381 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e39ded3e-230e-38e6-9e82-0aacd46a27fd | -9.20024 | -59.67839 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54880402-5b00-35bf-a989-3fb88d3989ae | -5.79423 | -43.6111 | 2025-08-14 05:10:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d56c85d-b54f-363a-9c5e-fe886b8f33b6 | -7.26104 | -60.62874 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b17dc618-6182-381b-8062-cf95c831d36c | -8.10963 | -61.1949 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b631d833-01a7-3e03-bdea-d0cec191a22a | -7.26817 | -60.62996 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19aed182-6c10-30a2-a1d1-34e9534340e7 | -9.93753 | -60.4682 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c47f0b90-ee02-31c3-9ab0-209a5be58b6b | -8.79936 | -52.04049 | 2025-08-14 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c08c180e-87f0-38a7-a3db-54869b85af49 | -9.15795 | -59.65332 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87b7d111-9246-3039-ab2a-3b3192270846 | -6.09961 | -59.92857 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38b844c5-d118-3261-b629-9d813f5a4091 | -7.13569 | -60.12603 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da9fbb82-422e-3629-80b3-2d2be43e64ef | -9.14207 | -59.66571 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e494ec80-c51c-3353-9324-5f0958678f41 | -10.0031 | -59.2149 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47cb71e3-3079-3aa6-a10c-a5ea88b38c05 | -6.78942 | -58.78501 | 2025-08-14 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1fc09bb-497a-3b82-b2de-abe6776cbf43 | -7.4615 | -57.65292 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9be1a649-5360-36aa-85d9-c894a8f59d99 | -8.57494 | -54.72346 | 2025-08-14 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbc39553-1a94-3428-9453-66271f7c9700 | -7.8169 | -61.33023 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f730e4d-d26c-3bed-958d-7a8c1353385e | -7.09086 | -60.02693 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eec3731d-7649-354a-89d5-1adf5487c52a | -6.86742 | -59.13692 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 306cc866-67a8-379d-a2f1-9178af5aafdb | -9.34656 | -60.33012 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8d8d2de-03c8-33ba-9533-e67a1758ba48 | -6.10311 | -59.92912 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22727947-088e-35d4-a34a-9e1f8099c747 | -6.10662 | -59.92967 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd2570f6-783d-3604-871f-d9cf204a9ce5 | -6.91254 | -59.13679 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8e689acc-e565-3e0e-9695-96018b19b00a | -9.18632 | -59.65729 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 829064ff-80e2-3dd4-98ea-d42af3788351 | -7.07018 | -59.19902 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ddc900a-8361-312e-8fe4-232b49ebc2cd | -5.73876 | -59.89355 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e08407f3-b0aa-366b-94cf-0610f9ab4c4e | -9.55497 | -62.73066 | 2025-08-14 05:10:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ecf6ebf-1c1e-362d-8903-6a150337f169 | -7.14133 | -56.42096 | 2025-08-14 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 818dffc3-888a-3221-90d8-076af2be0c93 | -7.61457 | -63.51847 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 174ae3c8-850b-3002-a90b-8a14a938cafa | -9.5008 | -60.52054 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 53717018-7518-395b-ab4e-c8d48ec4bc18 | -5.73813 | -59.89745 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a2ee1d9-9a68-3452-a6a7-b0e8c0f4de63 | -7.34054 | -60.6285 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc490bf4-7abc-3377-99eb-205bfb4237da | -6.86844 | -59.152 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17c2a9f0-ba91-3e29-b79d-30ed1a6aab60 | -9.06151 | -60.65455 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 161a4b49-b430-3adb-8573-f9b3b39ba276 | -6.95158 | -44.55791 | 2025-08-14 05:10:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6752e532-2b3b-3a5b-9a01-7c1599623b27 | -9.0593 | -60.64608 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50a03ec5-6ca8-3e2a-b08c-08ae73764779 | -6.08524 | -59.95036 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 62a097e7-ae68-3879-859a-0e1921121e24 | -6.91592 | -59.13733 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 72fceb6f-8c3d-38d9-8ca5-f47fc7306f8e | -6.88594 | -59.15111 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5ad70713-ca99-30da-9030-e702d8c5c302 | -7.02408 | -59.83533 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d7ec6bc6-703c-3c63-9975-0ce91ddee7bd | -6.89344 | -59.12625 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9322b28f-3e40-3500-a722-94f544c19113 | -7.81764 | -61.32584 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15791279-1004-332e-afc4-b86c25509ee9 | -6.88933 | -59.15166 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 24008240-27cd-3b2e-9bc8-463b934c6afd | -9.18234 | -59.6604 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84e38958-ed0c-32bf-ae5a-ff4461be22ad | -7.26461 | -60.62934 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88f2cffb-d4c0-39ca-bf30-245f5e125040 | -7.23983 | -59.99947 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80d1caeb-d4f1-37d4-b7a2-232905a2bcc1 | -6.8905 | -59.14441 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f48c67df-6479-34e4-8cb9-0e0121fd03f3 | -8.10459 | -61.2028 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ad2f0a22-1414-3a43-b5dd-25c23db19ce4 | -5.7419 | -59.87401 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2df419f7-97a4-3600-8898-9dbc53f41d79 | -6.89609 | -59.15276 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4dd1741f-6f2c-32c8-9637-a3ce7a712510 | -7.12877 | -59.64269 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff582a5e-06fa-3987-ab47-64f2ce705ee4 | -6.90578 | -59.13571 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 759fb1e4-eb77-3dc3-bee1-d57bcfdd72e6 | -9.18333 | -59.67558 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e6fdf5e-9daf-3dbf-aa35-af246c50cf31 | -5.81081 | -59.22566 | 2025-08-14 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1d6b3f5-0c72-37d6-b58d-0cf6b76301db | -9.2044 | -59.65283 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb8d811b-fde2-3f12-898e-6d2dcf5cb902 | -6.91033 | -59.12897 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 374173e8-efb2-3d64-b5ae-abd0e99e1015 | -7.09149 | -60.02306 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af330906-32d0-34c3-9a88-970b583edfbb | -9.1891 | -59.66151 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5f6304c-6f6b-3793-b577-f90060d3f0f1 | -5.73839 | -59.87345 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e7eef9b-0405-3342-b5ee-95b39608c981 | -7.62789 | -63.51675 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cc93371-bd7e-39e7-b1e7-896285623221 | -7.25273 | -59.98578 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5e8fc8e-336c-3f56-b888-dbf07fad5d9e | -6.92432 | -59.14986 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d519d483-5926-3974-b46c-5e28355cc511 | -7.63144 | -63.52143 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e3f164f-b170-3642-aaa5-f65904f51a99 | -7.31913 | -60.62497 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a9f20dc5-4ada-3ba3-b2f5-a98c9856dbf2 | -10.36155 | -50.81396 | 2025-08-14 05:10:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0391c917-40ec-3c1d-898f-59a2d58653d0 | -6.61381 | -43.88572 | 2025-08-14 05:10:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ea9876d2-3216-362e-a1b4-37d418bbf070 | -9.60768 | -55.13824 | 2025-08-14 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 002b5f8b-f834-37e8-a465-c1cba876dbeb | -9.06566 | -60.6512 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f649043-821e-3d3c-87e3-ddac80bebac4 | -6.11267 | -59.91461 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dbf5790-cfb8-3843-b6b1-b2eb05e95dca | -9.38448 | -61.53238 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e8127a3-5dad-319e-a286-e0ac89a925df | -6.87859 | -59.15364 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3390f283-7a07-3dd6-98b1-e20c88d8420b | -9.14046 | -59.65418 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd4490ed-7d6e-38ea-8578-4c54f385a3a8 | -6.8736 | -59.14165 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f80ba7f2-d6a3-3314-8c99-bddc55ff5d26 | -6.89785 | -59.14188 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92ce52d8-f316-3d5e-84f8-6990c10cdaef | -6.8859 | -59.88454 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 643a4d74-3a20-3089-93fc-8885cb668ee4 | -6.89947 | -59.15331 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9138ec09-8801-30bb-929a-b891728286ff | -9.15736 | -59.65696 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5d1d09f1-4ffa-3057-8976-73180e829a3f | -6.45193 | -44.56592 | 2025-08-14 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c6450e04-bf6c-3416-900e-4aae02640285 | -7.25212 | -59.98959 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01c0b0b4-d7dc-3e5d-aaa3-221b640e4c76 | -6.89668 | -59.14913 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d8859c0-e97b-3a27-81c7-3a070846942b | -6.88477 | -59.15837 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 82076edc-d348-397c-9e30-1ff41ee8ba08 | -9.14942 | -59.66316 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e94f9c7d-90fa-3977-9d42-31fc2167edc0 | -6.8708 | -59.13748 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e92479b-2716-379a-b75b-80ea8c5a0185 | -6.87521 | -59.15309 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a420bcc-0c3f-35da-a09c-5e63ff1215a2 | -7.53044 | -61.3868 | 2025-08-14 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| def5f8fe-79cf-312f-837e-1d8451f5aa6a | -6.90637 | -59.13206 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 736345df-ac98-3cc3-86fa-88b9358c3e8b | -9.19029 | -59.65419 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bd0f79e-a932-3521-a06f-595c544b0f58 | -5.75568 | -59.90027 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbca790f-15c7-391e-b02f-6a2cc3fb5ec4 | -9.50108 | -60.5405 | 2025-08-14 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 296af66c-c609-35e1-86fd-7cd38642d262 | -10.34955 | -57.59879 | 2025-08-14 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 859e76c3-4922-389e-aea4-276686925a1b | -6.45274 | -44.55981 | 2025-08-14 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6133667-e76c-3a1b-9400-88a260efa019 | -7.0724 | -59.20688 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e43ddf10-31ae-386c-809e-e1d6a6f108b5 | -7.26539 | -59.9957 | 2025-08-14 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a329de1-5a4f-3885-b5e5-54b80b912e31 | -9.1337 | -59.65308 | 2025-08-14 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1c3c71b-084e-3a7a-a20a-8a6af0608053 | -6.09132 | -59.93529 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed542194-ac32-30de-be0f-a4273f0c7d53 | -5.88457 | -57.74288 | 2025-08-14 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3164df2-230d-313b-88d3-d372ac47d11d | -6.63178 | -59.99898 | 2025-08-14 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09773759-2bbb-3b63-b4b8-ea42d1bfef34 | -7.61035 | -63.51773 | 2025-08-14 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README28.md)
