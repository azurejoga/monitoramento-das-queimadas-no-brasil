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
| f8d11642-883e-30b7-a2b9-6c484fce3eca | -6.81854 | -59.41954 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 14b87a72-4cbe-392c-b873-484a53c5c27e | -10.5243 | -50.7742 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1da58ed3-52dc-34d7-b93d-a529bc2c668f | -12.75815 | -48.47766 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a830b744-7966-36e8-9275-41bb297a41d9 | -9.18541 | -59.45656 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 44a363fa-7b51-32e8-8447-c6e7c8aacfd8 | -6.5374 | -58.53008 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 4ed43b9e-7926-3617-8586-669b6411b7de | -6.11567 | -53.0745 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e02a395f-4d62-3358-bfe0-a3728085d19b | -9.03905 | -60.44823 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 26749902-2db3-3a68-bbcc-dc40ced87e12 | -11.95553 | -45.49122 | 2026-08-22 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 96718885-4d4c-3ea6-a203-8f5e45b367de | -13.4421 | -51.84174 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b9ef4e5-afbf-3e81-b50e-0002d85f29d3 | -10.39704 | -50.43441 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95c7726b-5f14-3ee9-aec9-f7959ee61504 | -7.25655 | -49.90017 | 2026-08-22 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20228f30-4aca-3cc2-b79d-8ca1bd34240c | -6.78624 | -58.63046 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95cb322c-2ec4-30e1-a7a4-4483864e1285 | -8.54068 | -55.3255 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f78148e8-c52d-3291-9cea-142c6c9fb250 | -8.10598 | -50.05175 | 2026-08-22 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02791d4e-1454-32cc-a37d-b1f4522d77a4 | -6.21889 | -55.48391 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 913da75f-1426-3f7d-acd4-8062d5d03057 | -14.12918 | -48.0637 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa169e14-573d-3bd8-94d1-89e032cc13e8 | -6.25651 | -55.41795 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a01b690-06f7-3b2a-8173-495ebbc821e8 | -6.09843 | -57.87397 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4fea4a77-eac4-39c1-aacb-76f07425fc31 | -10.32678 | -50.40238 | 2026-08-22 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 970433dd-3434-3f88-9e82-7fc04c884cb1 | -6.87972 | -56.6412 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d984e96-05b0-3518-b89d-252ee11304fe | -6.91631 | -60.06612 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ef73f52-bd0a-3c36-bf6d-10fadecb5697 | -11.11815 | -46.18827 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80f3b4d9-693f-36b0-b1d1-1ca74bf11d7d | -6.76137 | -58.69272 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc3391ad-36fa-3656-841a-5890e3a70f00 | -7.51633 | -47.64204 | 2026-08-22 04:27:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9af251df-9e2c-3c27-b44a-8d9b7c4b2f8f | -12.00683 | -53.42351 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd32dd5b-aaea-3995-a967-45abf3fb01bf | -8.6225 | -54.68968 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8853acc-79ee-386f-b346-2cda03ffd3d4 | -6.12832 | -59.90659 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d2afd33-385c-36c1-8ce7-4bbe97502b37 | -10.95401 | -49.59412 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a39a5db-e11d-3d44-987c-3a30714365d0 | -12.81532 | -48.41777 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1b445d2-fbd3-3316-b239-44cee6e4e7a4 | -6.3774 | -54.94415 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0673a38-720e-35f0-92c9-c6043efafd78 | -11.44885 | -44.5335 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb07c501-19a4-31c1-a056-81811f7f3b7c | -11.60301 | -46.55041 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7ec08bed-7c37-3d29-a6ec-0ea0f691062f | -8.53535 | -55.33253 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb433495-1bbf-3e27-9d64-30c8624acd12 | -13.38124 | -54.36857 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5ed29d2-c4ea-34d9-9297-c985f5a90493 | -6.91655 | -47.47758 | 2026-08-22 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6bdc6a77-b87b-3f76-983d-4f80f8b503fa | -6.78538 | -59.4342 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| df59f81e-909b-377e-a936-e2cfd89683a6 | -12.25099 | -43.18373 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bf14b767-1229-377e-a277-db59a3967e0b | -8.1578 | -46.71871 | 2026-08-22 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 08013874-447e-335c-8b4d-894715f30950 | -14.28252 | -47.42158 | 2026-08-22 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ec61e741-3992-35b7-ba5a-d8c0428f0382 | -6.53659 | -58.52775 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 23376217-57c3-3577-bfe6-3f544e4a7825 | -13.45151 | -51.76461 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a47cb96-867a-3669-8301-a38d2a0262f9 | -9.44274 | -51.62167 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| edbb4595-cafd-32dd-bd84-835d1ad87b06 | -9.21902 | -59.77287 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f2b5441-faad-39aa-9c51-52af333ecaca | -12.7279 | -46.45846 | 2026-08-22 04:27:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 58908579-ad0b-355d-b33c-7a55237b3062 | -6.79216 | -59.43512 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 93f2d403-32ae-3918-9159-f07aa8937277 | -12.27844 | -43.15744 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 909a5237-56e9-3aad-9452-e08caba347f1 | -6.76578 | -58.70484 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3a7a5ff-90ee-3296-96fd-4273ab290dc3 | -11.63134 | -46.52177 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73da9efb-f527-383a-81ec-834525fc67ec | -6.94576 | -59.31452 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff316124-a7f0-37de-823d-dbcd6b180498 | -12.77171 | -48.39237 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b47ec198-9d52-32f8-996e-96c63c95e8d1 | -11.73472 | -45.58703 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9345d5c4-0d33-306a-aa21-8fb9f199cdba | -11.35624 | -46.36137 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a01c3ef7-3134-3f39-bea6-5203702fd015 | -8.89862 | -60.54543 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 21963c1c-f3f0-30cc-9ef8-7f1121c9dfff | -6.43762 | -54.9609 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c1e483d-30bf-34fd-955a-c264ccad87df | -8.0238 | -51.79517 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33a25147-9a57-3e11-8a8c-3325575a81ee | -6.76337 | -58.682 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1fd581db-fbbe-35c9-a5a0-66e62c4c6de1 | -11.60247 | -46.554 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fcaf96a1-4f16-31a5-815a-79f939703776 | -10.51639 | -50.7758 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b62b8201-cbbb-39f2-b3d0-f9f9276aa9e3 | -9.44363 | -51.61641 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee295a6c-09b2-3530-80d7-278f46b7fc5d | -12.25068 | -43.12769 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a4a6ae01-2b83-3f80-9563-3a9faefdceb4 | -6.13406 | -59.91454 | 2026-08-22 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d1d4cd-1403-3614-aa52-942e09cb1849 | -13.38041 | -54.36869 | 2026-08-22 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fae39b3-bab8-3075-83c7-802e59fd5ccc | -6.43215 | -52.76103 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca5a075f-f5e7-3ae5-bcf7-d936ee58cc02 | -11.35678 | -46.35778 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f72c1d5-68aa-3ed7-9508-556871515485 | -8.53113 | -55.32075 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967e4df1-55a5-3dec-b97c-e19098ef0a3d | -8.52363 | -54.82291 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d3dd9f89-571a-3d23-8d12-0efd04f294ec | -6.78933 | -59.42685 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ed5c1bc1-5d46-3156-8fbf-6b1a0d09ec22 | -5.79796 | -57.54225 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 106a9ceb-4464-3544-a70f-d0f64fad16ce | -6.79548 | -59.41714 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e5871f30-d810-308a-9962-745e032806c0 | -6.01154 | -57.79598 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9202918c-b475-3612-b969-2cdcb12752a5 | -12.76396 | -48.39835 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f98df4f-7164-387d-a1a0-56d5fb343976 | -6.48867 | -51.60276 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e688439-519d-3548-b897-224e65506b99 | -12.75541 | -48.4735 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59647c55-c61e-3d5d-8ffc-347ed6b20203 | -9.15955 | -59.45261 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5d563ed5-ee2c-3e29-a693-581e14e9653d | -6.77922 | -58.66832 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bd5e004b-30af-37ed-988a-78b96876f3ee | -6.81634 | -59.39456 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b1cc72c4-3e17-3fd2-849b-0d6ec296bc43 | -12.5521 | -47.92937 | 2026-08-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7f7e022-1563-3992-8ec2-596b5b1d1f29 | -6.88849 | -56.72459 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e172c20-4215-34ad-b759-81c0f389912f | -8.16166 | -54.99356 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70a5f638-0dc4-3bf4-85fe-94eb35220b05 | -9.47174 | -48.28802 | 2026-08-22 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 54fe83d2-cba2-37d1-aa33-f16b4d79193a | -6.77081 | -58.6778 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4622e502-0ab0-3e86-af29-b27bd38d716c | -10.30303 | -48.21421 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8238d5d8-9bb1-3f77-b4da-db4c8384573b | -6.76635 | -58.66603 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| a0a7ceb7-5e89-3a7e-a053-d6ee94e2073f | -10.90498 | -50.24126 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b36bc67-f7fe-38e6-ae96-7d2444ad5e5c | -8.5396 | -55.33142 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e631f58-38cd-340a-80dd-8709d48ba4b4 | -8.63124 | -54.69666 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 61889251-3aea-36c8-98f4-d6f7cdd353ae | -6.77428 | -55.69846 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21226c88-d8f3-3132-b4d0-2fa844fd0180 | -7.47116 | -45.13474 | 2026-08-22 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0e11c69-6921-3ab7-bc06-33852a69eeb2 | -9.52391 | -51.6428 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 08a7ef99-62e1-3eca-9467-724fe4262358 | -6.90501 | -59.00579 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9b326a64-9762-3451-9e29-04078b91744e | -11.16252 | -54.02982 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e7f3df15-f251-3712-b764-d4c3e0725d60 | -8.80869 | -48.54551 | 2026-08-22 04:27:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 133f89cb-ed2b-3e0c-982d-a45187d8881c | -6.75993 | -58.6648 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2d7b2060-619b-3ed6-8fd5-1b4d7cb24263 | -9.18107 | -59.44447 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e212c3ab-2bbf-3d32-a50b-1c34b49ac836 | -9.17515 | -57.00475 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84c0102b-3f1d-3646-b5cf-0854853711e2 | -10.75686 | -50.25849 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4516fa0a-3dfd-3d7a-98e1-b564741db353 | -10.47088 | -40.54504 | 2026-08-22 04:27:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6cc9f3ff-47c7-3a4b-97d5-e796ed9af077 | -6.41454 | -52.7317 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1575662a-e37e-3e2a-a9eb-80aa3e8a10db | -11.39715 | -47.20267 | 2026-08-22 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61fc6990-4f76-3cb4-9801-65c267af4b1e | -10.68588 | -50.29402 | 2026-08-22 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README26.md)
