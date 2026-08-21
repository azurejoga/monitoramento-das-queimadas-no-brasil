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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eec31f82-1b77-38ba-8a56-c9561e260efe | -9.44601 | -51.63187 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 836a75bf-18d9-365a-ba07-e35b3d396178 | -8.18367 | -54.98782 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88c87631-aa7d-3b58-8cbb-2a15164653d3 | -6.89048 | -59.42507 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e158d4b-22a4-3628-9f37-44e15cdfd4e4 | -6.54831 | -56.55088 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d30c8eb6-155a-3ab9-8192-5074d12e745a | -7.36461 | -55.51608 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97ab1f5c-8666-367a-8783-ffdc92c87d49 | -7.06896 | -59.96814 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4385657d-509e-3447-bf60-b9fedce37d6c | -4.46931 | -55.39574 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b929bb3a-f5db-3511-b431-9a9d72c1b162 | -9.46958 | -51.63557 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00760e68-3e99-3f7c-b4f2-02598457e8ee | -6.33649 | -46.52379 | 2026-08-21 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 154b259e-14b0-3454-be5a-56debef5644d | -4.01567 | -48.06556 | 2026-08-21 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d0cef2-f996-397a-adfd-4b63998bbcc9 | -6.20396 | -55.49254 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cb9c6c5-3f17-37f7-8267-7ad302995233 | -8.09661 | -51.67336 | 2026-08-21 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b91e79b9-3a90-351a-a3c1-8c35df1dbdc2 | -8.57081 | -54.6684 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0d37e24-0dd6-3e6c-a486-6cb13e3bc37e | -6.34319 | -44.08181 | 2026-08-21 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7fed0db5-b4d4-3a6b-a253-55a34c5b065e | -9.42048 | -60.41343 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 01362fc9-2c19-30d2-a387-fc0a41cfbf4a | -6.54708 | -55.17398 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 039ba769-a385-3c56-a67a-b6f929257dfa | -8.54581 | -55.31228 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf9f1d84-00d9-3705-9c1f-1de068b3c110 | -4.9582 | -56.2654 | 2026-08-21 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b25eb9a2-dfa0-3918-80d3-9a09b00e7250 | -9.06163 | -50.88616 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a4aee738-641b-367a-9b39-77dfdeb19c00 | -6.86134 | -59.44487 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5aed0a8-086f-386b-b814-869b99ffb452 | -6.81842 | -59.39359 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 07d54d9e-e362-32ec-a146-45f2fa3884f8 | -4.71834 | -42.77312 | 2026-08-21 04:46:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8989773e-15ca-3b17-8641-c5ec0f2208cf | -7.60111 | -60.83012 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6e471da-076e-3701-b888-ef22264d085d | -9.99453 | -53.93606 | 2026-08-21 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2c3471c-0ed8-3ae3-86ab-3980d088d7c7 | -6.89508 | -55.72394 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 591e1321-533b-35ae-bf26-9ce2a3e5272b | -9.40806 | -60.42379 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f30c68d1-74db-3b1b-9537-980529f788f9 | -7.14088 | -47.50666 | 2026-08-21 04:46:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a8074ae-dccd-38bf-8cad-701b5b96d97a | -6.44083 | -54.94855 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 473fd18d-1196-3940-92aa-a1f0df60086c | -6.59915 | -56.37103 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a0f430c-a695-3253-9679-62117a58ff02 | -6.12359 | -59.90442 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9462f0c3-2a03-31b5-8ced-7e91b859f93b | -6.42725 | -52.72653 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c03aa2e7-6997-3462-979c-1613322c303f | -6.89201 | -55.71845 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0909826c-31d0-32a0-b413-d9ffbcd9209e | -6.88749 | -59.44201 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0b15c46-b574-397c-9fa4-e0492a951ecb | -11.32316 | -45.01455 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dad5f0c3-ad0a-389f-93af-02c49a89a92b | -8.66889 | -54.57837 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d838278f-e3b3-3a4e-9636-b911f058d521 | -8.58796 | -54.74319 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e97b4833-4f63-350c-b05e-d764624d2422 | -9.5109 | -51.63137 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19686055-5dec-303d-a64d-de0c67bde80a | -6.10039 | -57.87038 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a68eabb3-9e22-31bf-8035-b1298ac57bd1 | -9.05937 | -50.87867 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6eb107d-9eb1-38c5-b190-e504833691f4 | -8.6684 | -54.58744 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad56a718-ef26-382b-8469-bedd0b18a483 | -10.52226 | -50.77685 | 2026-08-21 04:46:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cf654143-7ac5-3d52-aa39-e626e087c6bb | -6.69569 | -58.9384 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 04923881-beb3-3881-b543-7ef310e62c70 | -5.60903 | -45.70918 | 2026-08-21 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d08e50de-d0d9-328f-8a2f-47abb94bdae8 | -6.12089 | -59.92025 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 990124d4-b8e4-3eb3-bbaf-18b3f02ef50c | -7.13582 | -59.64289 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1650c5d8-6ad5-31fd-a204-e6fb4a360bc6 | -10.12282 | -48.81251 | 2026-08-21 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f23336c6-8e00-3042-8d05-ce5b944973e8 | -7.0638 | -59.96735 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 223f197f-5c23-345d-9318-881e4a745334 | -11.35798 | -46.00486 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1647c27d-6921-3308-aaa9-1961bd1bd4b6 | -4.01217 | -48.06499 | 2026-08-21 04:46:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 52da994e-090e-3feb-93bd-3a0f0902d077 | -9.4305 | -48.25293 | 2026-08-21 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3e9d4dc-c057-3c35-a87c-3b5f88cdd411 | -8.56858 | -54.65961 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830f0d62-4584-3fb2-b12f-173402a79738 | -10.30292 | -48.22847 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25234a36-f65c-3280-8608-c5f3972dc182 | -10.82794 | -51.00075 | 2026-08-21 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de2fcbc2-680a-341b-a6f6-02388f735a00 | -8.62791 | -54.72436 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc8b08a4-bd43-3443-be69-44e41d7faf09 | -11.32838 | -45.01085 | 2026-08-21 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 64025b3d-3717-3fc3-b445-f1ee96817322 | -7.00961 | -56.54172 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75fde456-6857-3760-8416-09136627e2df | -6.58284 | -58.99493 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0e9409cf-df19-3ba1-91b3-ab046b163ce4 | -6.42718 | -52.74885 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 01bbcb2b-9c5f-3157-8baa-0e814e3ef8bb | -6.2481 | -55.41543 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 44f58c5a-32af-3053-95e5-ac37ee836dcb | -3.67304 | -50.94873 | 2026-08-21 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ee1f3c3-440d-3603-9356-b9a173e43888 | -7.77969 | -61.15921 | 2026-08-21 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05afe0fe-31e5-3f3b-ad79-934e9dfd8443 | -10.63712 | -51.60214 | 2026-08-21 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 444d4696-b443-3758-8278-c93647f3e008 | -9.41224 | -60.54441 | 2026-08-21 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a52ad4e7-3af4-30ee-992b-07d9be6283e9 | -6.42941 | -52.75666 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f6a31b8-ff08-3082-a7cd-d0bc77fac136 | -6.86759 | -59.43859 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d7fc291-b990-311c-b91d-89486b55474f | -3.38227 | -59.53111 | 2026-08-21 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efc7ccd1-1fbf-366a-a1f9-a5c53452d2ec | -8.11342 | -50.04257 | 2026-08-21 04:46:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 313284fd-54c3-3ba7-bf9c-3e209f4abff4 | -5.60848 | -44.00851 | 2026-08-21 04:46:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 76244a23-f572-3a49-a5a2-49bdb64222cd | -8.21078 | -55.05119 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 13adebc1-f238-35f6-bdad-e07d4a036e5d | -6.88985 | -56.43198 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eac9362d-f9e4-3c60-80ad-b6b8ea7c487b | -6.00234 | -57.83628 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60b40578-a235-3bc6-931f-191ff6ff3a89 | -6.60382 | -56.36807 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42eeb597-d63c-3330-8589-2ee14e6986a7 | -7.01661 | -48.0381 | 2026-08-21 04:46:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 11b5aef2-8aa8-3055-b240-ac82fcda6da5 | -7.62855 | -45.75674 | 2026-08-21 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28dc7839-8eb9-3e86-a31f-47177e8c9830 | -8.3755 | -62.69999 | 2026-08-21 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b310daa7-c59f-3e44-8c6e-52636a80f960 | -3.38281 | -59.52781 | 2026-08-21 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e47948c1-a610-34df-9bf2-69ace550d671 | -8.49602 | -54.86649 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 954bde08-5bd8-30b8-99ba-4722584cf418 | -6.00678 | -57.86518 | 2026-08-21 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95ac0b08-9481-3cac-980b-1c9e5e7a8022 | -9.05496 | -50.88518 | 2026-08-21 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| df06db3e-9bc3-3723-b337-eff93d5dce86 | -9.21782 | -60.77837 | 2026-08-21 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27aae078-d128-330a-bd02-632bcd7540dd | -6.86597 | -59.03376 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 39a3aa17-f5d4-3a91-90de-7b2d5c905b05 | -10.75664 | -50.31681 | 2026-08-21 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b91abcd6-8b6a-34f2-91d3-b849ecc5f5fb | -6.87321 | -43.73508 | 2026-08-21 04:46:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 47e720de-efbf-3814-bcd4-cecddd17d293 | -7.44713 | -60.00688 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7397bfb2-3faf-3455-a9bd-1ab9f61ef0e5 | -4.45355 | -55.39315 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b577bb73-c175-3dd3-963e-b1d687b85717 | -4.18761 | -49.41044 | 2026-08-21 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54302ef1-a997-3b2f-9746-125b1514ca23 | -6.3847 | -54.95507 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a8500342-a82a-35e8-ab03-9af737017629 | -6.8994 | -58.98451 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5955355-ed69-30fb-afa2-d509a1202a9c | -10.36261 | -48.23732 | 2026-08-21 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3053a282-511b-3cc1-9f34-540afaa61082 | -8.49395 | -54.87925 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e20a011b-ba3d-3428-abf0-ec249db674dd | -8.59763 | -54.70672 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 509936af-e671-3f72-8a0a-4db686692d7c | -4.11047 | -54.92602 | 2026-08-21 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96687698-dcfc-35e7-88fb-1e1605a893b9 | -6.02286 | -50.20567 | 2026-08-21 04:46:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8672897b-2254-3bbe-934d-611cf03c52ec | -8.55015 | -55.31905 | 2026-08-21 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a824142-f3a0-39fd-a165-054a8dcf0a2f | -6.96746 | -59.30504 | 2026-08-21 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 959df712-b6ac-3d57-aab1-7be409e8e891 | -6.22412 | -55.61908 | 2026-08-21 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d11c1d8b-e273-3bff-8f0c-9db607512336 | -8.57148 | -54.6643 | 2026-08-21 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c4d8831-0905-36e3-b5be-e9c49789c90f | -9.51698 | -51.63589 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d13cb15a-8e7e-3392-adc9-e2e8afe8595c | -9.4531 | -51.60804 | 2026-08-21 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| acc6a36e-af7c-3e5c-a363-68369be38943 | -8.33508 | -46.50327 | 2026-08-21 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README38.md)
