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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84b5d393-89d5-3c77-8bc6-818e35bf46ab | -11.28256 | -52.76003 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d1b3d5e-7df5-3293-bd99-ff9e26c886e9 | -9.74364 | -48.57101 | 2025-08-05 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 843465fc-94ef-352d-9450-a5160b4e4228 | -11.75342 | -47.54541 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ecabdb7-cd1f-3ba0-9270-0dbf25a9f45a | -13.04661 | -56.87521 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 523f4466-036d-3cc0-942b-1f9d9decd18d | -12.95154 | -48.2527 | 2025-08-05 04:40:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5fcc341d-9fc7-334a-a648-65d1942a6705 | -11.78662 | -44.99797 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e896fb7e-76be-3947-9472-05fdc65d81a1 | -11.92957 | -44.92831 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7fad4384-f46f-3e51-82be-6d36cee03fd6 | -10.44943 | -44.38898 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5aeb6e2f-b8b5-3831-b1e1-202b2eccce2e | -9.69427 | -51.93833 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3dc6ce3-6680-396b-9d95-4ec5f2ffb91b | -13.07586 | -56.88444 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3122a7c9-24d9-3760-9f9e-61453abdef83 | -12.99054 | -47.45664 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c45b3c1-6c24-3fda-83b3-d7fb34badff2 | -13.04731 | -56.87125 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 29de1cb4-4f82-3d72-b66a-99dcad335cff | -12.38846 | -47.04818 | 2025-08-05 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bd65d4a-4fc2-3c7b-8721-e5927da74a07 | -13.0508 | -56.87597 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 38b86896-5631-3bd4-88fb-bf19d35611d0 | -13.05551 | -56.90084 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44052e86-8883-3975-8114-d782c779e8c6 | -10.4689 | -44.37581 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5738fa2-4cfd-3829-9bf3-60ee944bc9cd | -11.92026 | -44.96546 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 833eb655-6d3f-3a13-9769-52e2a505e2f2 | -11.81245 | -44.26099 | 2025-08-05 04:40:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c26eacf-1a58-3698-9378-9c20934bbc64 | -15.3905 | -40.84407 | 2025-08-05 04:40:00 | NOAA-20 | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ce7c38bd-e0d2-3f69-bb82-35b248bf221d | -11.79031 | -45.00229 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d84a768d-dce9-3483-8dc9-01acbb533caf | -11.92929 | -44.96257 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acf069ce-f694-3f84-ad60-bb4d1a262b53 | -13.05918 | -56.87753 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ef2c7b0a-d614-3f77-86c3-541680dee7b1 | -10.46948 | -44.38718 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8cffc65-7438-33d2-ab3c-99fed0582da1 | -10.77678 | -48.79885 | 2025-08-05 04:40:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b0403e2-fd34-3068-8a5c-1c30b191dba2 | -11.76878 | -44.97154 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df1be1b1-1837-354c-8be9-44ce1e87f715 | -9.70841 | -51.93695 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7a29f93-38b6-3233-a701-0fcf8b927b8e | -12.95095 | -48.25678 | 2025-08-05 04:40:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2b9da86-fbd7-3468-9049-941c1c8c19f1 | -10.34263 | -44.90422 | 2025-08-05 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba901032-acb7-3fc3-96bb-ef129c3f331a | -12.6823 | -48.11909 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c623543-3808-3a56-a368-e8749a9835e9 | -10.34627 | -44.90855 | 2025-08-05 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2adc7bac-d6ed-3841-bb45-ce2493d702d5 | -11.74619 | -47.5443 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0003e535-8aac-3076-8cd0-8062d59fb34d | -13.0041 | -55.972 | 2025-08-05 04:40:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab771e3c-f4fd-3f00-a149-9fe8c178a1a1 | -13.00231 | -55.97387 | 2025-08-05 04:40:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e25c7ed6-e605-35aa-9c03-76dedad973f9 | -13.04591 | -56.87918 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c4c9203-8aee-3ef2-80e5-6ff7b71ed12c | -9.69368 | -51.94199 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed189144-77ee-305b-8525-7a1cbbf510e6 | -13.06822 | -56.87885 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 595fdd5f-2471-3f4a-b32f-383a0cc276c8 | -14.51006 | -52.0702 | 2025-08-05 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47447eee-8343-374e-b263-5939cfad3477 | -10.47595 | -44.37185 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d102c9d-2afc-326d-800c-0023e77a6a31 | -12.71021 | -48.10229 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddfd3aa3-c7e8-3bb3-b637-d51a44825e9d | -11.74656 | -45.00765 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b08b13-bec6-3274-980f-684d0fec01b3 | -12.67402 | -48.12613 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 75495177-cd71-3140-86d0-572dfb02cad0 | -10.80905 | -46.50875 | 2025-08-05 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67e94874-4133-379d-879a-5fa3767cc67a | -13.05971 | -56.90159 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a45bc31d-1e14-3601-a2d4-da7b40b9bdfc | -12.22098 | -44.195 | 2025-08-05 04:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e5f485a-ce1b-33d3-83ae-01779f8c5faf | -13.08341 | -56.91436 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 07134196-6c4e-3ea6-ab38-6d44396d08c5 | -11.9183 | -44.98005 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95b3ee42-d838-33b1-9030-ab8d1ff18aa8 | -13.04448 | -56.91169 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41b83064-60a6-39cc-b47a-ac1682ba0f09 | -12.7188 | -47.79153 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6410cdc7-cd77-3ff9-a14a-8cd9789d33eb | -10.47108 | -44.37528 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12a392c5-41df-33c2-87e1-61caaed5b6ce | -11.91337 | -44.95238 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81809f9b-7fd7-35f4-bf8b-3453dd178eb7 | -10.53054 | -42.54935 | 2025-08-05 04:40:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 52206207-e32a-3b44-967e-59d0cb2480db | -13.07168 | -56.88358 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 898f7611-88cd-3e96-bf20-c232641ebe5a | -12.51822 | -47.19111 | 2025-08-05 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50834850-24b9-379f-a503-ab9f565a97a1 | -10.78411 | -48.79644 | 2025-08-05 04:40:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| df6eba61-0948-319c-8344-0389d5ba9597 | -10.46677 | -44.3746 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9594eb2-bc00-35e4-85a4-a5f8ad5bb435 | -12.22309 | -44.19827 | 2025-08-05 04:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d85c0f6-3f4c-3690-bb38-06043ff34a32 | -11.718 | -47.77415 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7da8d2b-a29d-3c74-8a4b-acdd29e38955 | -11.04188 | -47.61361 | 2025-08-05 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c579e5fa-16fd-3780-bea6-c59b6bde2a41 | -10.92523 | -48.37243 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e98f1fa-c2b8-3ec0-a900-22467c07d5f7 | -14.4812 | -52.08001 | 2025-08-05 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ae7be03-9a27-3556-a0ed-df4da1ad8f79 | -10.60007 | -45.25791 | 2025-08-05 04:40:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0140bc9-40ae-3c26-996b-43b0d66d8c84 | -12.38523 | -47.07104 | 2025-08-05 04:40:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0969bb12-6d1f-311c-82e3-de1f37655ff2 | -13.0675 | -56.88275 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e516b13f-5bf7-392e-978f-d040cce2e5bd | -11.9193 | -44.94034 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09a77576-b8c5-3235-9ae0-5be41da85d6f | -11.75167 | -47.53988 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f76de8b-dec2-3250-8edb-ed2fd28cd2c4 | -11.79084 | -44.99854 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd4c0400-b8f5-3c4b-a1f5-c5ae74f16ac4 | -11.06715 | -48.3624 | 2025-08-05 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0eb1f16-57e0-31e1-ba1e-09737a598569 | -11.74818 | -44.99594 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90417715-f308-3aed-a486-c40c4e3882c4 | -10.44511 | -44.3884 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 386fc638-dd55-340f-b7d2-124d346ab7f8 | -9.31488 | -50.3201 | 2025-08-05 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ec756196-12cf-3214-8a81-9315f7c95225 | -13.08484 | -56.90647 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7e91aee8-3cac-3860-b195-b127bbde34e3 | -10.9114 | -48.37027 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa012e12-3695-30ae-9f32-8365236abf9c | -9.31158 | -50.31957 | 2025-08-05 04:40:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4a70a69d-59c3-3b47-814d-a08d7691b6ef | -10.4479 | -44.36853 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7e7783c-1de1-31ee-9a45-c6abb003f229 | -12.68832 | -48.07786 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0454abc-3f76-3423-a9a1-dd9bfcd2b786 | -11.75529 | -47.54042 | 2025-08-05 04:40:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94473cba-eebd-3b3e-a9da-706b6bd064d8 | -12.54775 | -44.72314 | 2025-08-05 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d457875d-6eb4-3335-ae6e-2c9ef4044e3b | -13.05495 | -56.88036 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e5e07a48-7a61-3245-80a3-9d2ea6fe127d | -11.03769 | -47.6172 | 2025-08-05 04:40:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a4ed943-2d63-3aa5-95f2-1f617a3a87e9 | -10.90507 | -48.36533 | 2025-08-05 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6db3dbc7-8f69-3668-8ccc-eb9c563aa0ec | -9.74307 | -48.57471 | 2025-08-05 04:40:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4dcda711-8583-3c67-8863-738d6a4faf84 | -12.71518 | -47.791 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77b5099a-bbb0-30a6-8ad9-94aa616a5899 | -9.55739 | -47.88103 | 2025-08-05 04:40:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca1a9b59-2ad4-3916-aec3-6f6261e0c1f2 | -13.0501 | -56.87993 | 2025-08-05 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 438b6dd7-dd93-3a2d-8dae-a05d826efe83 | -11.27526 | -44.64618 | 2025-08-05 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeff425b-8b5c-3ab4-bbc1-a99876eacc52 | -11.06774 | -48.35854 | 2025-08-05 04:40:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c13a8678-722e-343b-a513-5c9f789c63e7 | -10.44567 | -44.38447 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67cb6f2e-fd32-34ae-92f8-68d741eee5ff | -11.92077 | -44.96165 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ff548556-da53-3573-85e1-c66e6f9cbb26 | -12.441 | -48.71798 | 2025-08-05 04:40:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a7d6b09-0021-3c30-bea6-553ea6eff39e | -10.46777 | -44.38375 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0c83c418-af3f-3fef-bf54-b24886c911cd | -9.69646 | -51.94625 | 2025-08-05 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25fff67c-f20a-3f92-bf6d-42873cea34b9 | -11.78677 | -44.99691 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b695153a-a336-3bae-a57f-fbbd3e1cd4b2 | -17.21061 | -44.83215 | 2025-08-05 04:40:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| decf01ac-cf08-3d58-bc35-18e54533e68d | -10.45432 | -44.38556 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b52787d-5068-34ca-9683-e72230a28b92 | -10.46403 | -44.37909 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2b9567d-93f1-3b76-aaac-b70c48fccc4f | -12.67756 | -48.12672 | 2025-08-05 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c42a9d69-3630-3029-9316-a1315ee0fa90 | -12.54718 | -44.72738 | 2025-08-05 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aabc6319-9ab9-3cee-af46-d0632f47d4b1 | -14.46677 | -52.08492 | 2025-08-05 04:40:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddaba103-e42e-3ef2-9c59-0e9f1a6e5374 | -10.47432 | -44.38392 | 2025-08-05 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 27b10292-855d-305e-a6bb-c01d8d833b04 | -11.79049 | -45.00126 | 2025-08-05 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README27.md)
