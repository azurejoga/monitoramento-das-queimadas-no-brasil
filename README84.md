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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 214e731a-90cc-3f28-a1e9-6dcc1767e2fb | -10.96943 | -49.74881 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3c4371d-a0ed-312a-aafd-0bb752baf607 | -6.88157 | -59.98601 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13f92ae6-d090-3286-b1d1-e7981f633391 | -5.67166 | -53.74588 | 2025-09-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 038310f0-02a6-331d-90e6-199a05890852 | -6.8388 | -46.40325 | 2025-09-04 05:16:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7c7fa5f5-d5f8-3b29-ba68-9027cbcfb85a | -10.53036 | -46.75725 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73e6e5aa-9160-3ae5-89e6-beb111cfff43 | -10.97464 | -46.85201 | 2025-09-04 05:16:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1267ef1b-564c-3e40-9f23-d2ec68e5363e | -8.43766 | -47.3299 | 2025-09-04 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 13b9b180-635f-31d0-b3a5-897500d30004 | -10.48707 | -46.76472 | 2025-09-04 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebd8d87b-e492-30d3-ba60-43901a783f2d | -6.67702 | -48.39802 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 59118b68-372d-3ef3-ac80-e4f6eb14895c | -5.69448 | -45.94389 | 2025-09-04 05:16:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 821a025f-1488-3223-91cb-b9ecfd4b8746 | -5.27331 | -55.95925 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 03a98755-c2c9-30eb-91ae-94f491c3dcfb | -7.97537 | -46.35646 | 2025-09-04 05:16:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74720c2f-067d-374a-bcd6-829872907538 | -10.48041 | -53.6325 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83071546-d527-3841-b07f-daada788226e | -10.97465 | -49.75354 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d3256984-22b0-3bca-8b1d-a6b7c5891058 | -9.49132 | -57.81861 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb93b931-e790-35f3-b861-f8e37c06bcba | -10.42287 | -50.3784 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54d0094b-2062-3f29-9ac1-8da0d002f015 | -9.60689 | -47.04123 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d4cfd54-46d1-3d31-ad53-57a89097b399 | -5.3176 | -55.85902 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c15a6119-7cc8-3bba-a9c8-80c4732e09bf | -8.37299 | -48.33093 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c8e7283-badd-32f9-9525-2e81f57a3cb8 | -9.33412 | -55.21531 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 722d1a4f-19bc-3387-ae71-2c8de6448595 | -7.60739 | -55.26826 | 2025-09-04 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4413995d-ff62-3183-8968-87918cd51ca7 | -7.71232 | -50.31746 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a70a60e3-797b-3f58-b892-3ed6abc412b1 | -7.68519 | -48.72876 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66515591-f75c-32aa-b55a-80b9ed6b9b2b | -7.34688 | -48.18762 | 2025-09-04 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcb9d6e1-7381-3d2a-a83b-1ae39f1f2106 | -7.71188 | -50.32071 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d56af340-893d-343d-b8bf-52b1d29850ed | -6.16564 | -55.71626 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1f92ed9-705b-3554-8cec-a5df2ac1e5a1 | -9.62092 | -47.03715 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c95c735b-61c8-336d-be95-c1b1cef8fadb | -7.69941 | -50.29328 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70eed7c2-01ea-32a5-8914-674e4903ef96 | -10.46407 | -53.62133 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05bf177f-19b1-38a8-9507-83a63fe8fea3 | -10.1132 | -54.79827 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78ef5275-172d-3506-a422-5077d6316754 | -10.42333 | -50.37483 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 850a371c-7075-3d3e-a6c6-39d6e38b37ac | -10.4918 | -53.64714 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7b374c0-155b-3ab7-a10a-dc50245685fb | -7.69101 | -48.72986 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ffc2483-b333-3853-a223-f3d467439fee | -6.67289 | -48.39883 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5198f7c8-b934-3175-a4ec-4d75cbecb4a6 | -10.42971 | -50.36843 | 2025-09-04 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6fb98b57-1f31-35ed-b9c7-4590f7ea88ff | -8.37164 | -48.33318 | 2025-09-04 05:16:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 996f49ab-e689-38e9-a795-e3548d52d34d | -6.30518 | -57.92987 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b1c070e0-6d9b-3458-95e0-1d6ba952ed34 | -7.90074 | -61.52165 | 2025-09-04 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 980618b0-fa7c-37b5-9891-f114bdde09c5 | -6.84325 | -59.15576 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8bf1afcf-571e-3897-88f9-49b38a90a740 | -6.49788 | -55.88983 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 578bf22c-80d0-3ad0-a0ec-21fe80667392 | -4.98023 | -49.90836 | 2025-09-04 05:16:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be531159-5d09-3437-bff8-35ea576d9226 | -10.45019 | -53.62212 | 2025-09-04 05:16:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c80f5152-988b-387f-99d6-fc7b1319aaa0 | -8.3605 | -52.54704 | 2025-09-04 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44bb7a1d-31e9-31f7-a54a-cefe6d44bcbb | -3.42619 | -59.58053 | 2025-09-04 05:16:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bfbf76b4-fa72-38ea-9129-6b78adbd6e1b | -7.77817 | -50.9682 | 2025-09-04 05:16:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98ea71e0-9859-3367-bce6-3355b2486d5a | -7.38581 | -56.68709 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21dbba6e-bdc3-3338-af13-57fd12dd5db6 | -5.70166 | -45.17147 | 2025-09-04 05:16:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efabd709-88cd-3cdd-9ef8-d27327ad6f7c | -6.77923 | -63.13987 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de28fd63-c088-387b-ba91-6f4bd0cf6116 | -9.6076 | -47.03526 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4afa8511-a18c-30e7-ad5f-1c330a1b17d3 | -6.8715 | -58.93329 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdc62a39-2c34-3b5c-8cf0-9ff6ed3d7a8d | -3.47671 | -50.54272 | 2025-09-04 05:16:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8e29d278-4d5e-39f2-b504-780803c1f916 | -4.61165 | -56.1728 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55084617-cfc0-3eef-bba2-45ab4ee61fe3 | -7.71761 | -50.31807 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aac13384-9e41-3d44-81f9-e167598281d0 | -10.02529 | -46.09522 | 2025-09-04 05:16:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea5ff50d-8708-354d-aaf2-0ca29d4bdc6c | -10.98371 | -46.84211 | 2025-09-04 05:16:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ed3cd571-2499-3ea3-a9db-5db89ebee6c7 | -6.74733 | -58.72883 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 46959936-0900-38e4-87f2-14b56f83135c | -5.11316 | -56.96541 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a523fde9-680d-3ee7-adcb-f885d1d0b311 | -7.07401 | -46.19936 | 2025-09-04 05:16:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 279449f7-813f-3aa8-8911-58243d6298e5 | -10.06793 | -54.79201 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e71b80b-7815-333d-9677-cafe7fa75412 | -3.88434 | -54.21465 | 2025-09-04 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66ff57ab-af92-3f31-a6ad-a8aad6396fb3 | -9.48547 | -54.42664 | 2025-09-04 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c9a783f-bdba-3667-b875-b5e246cfdf3d | -10.97537 | -46.84578 | 2025-09-04 05:16:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0aba52b-a3e0-3c48-81c8-95cd97643cad | -7.69157 | -48.72549 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0b851ae-2cc5-37c7-b0a5-f23ecfc712b9 | -4.98069 | -49.9053 | 2025-09-04 05:16:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 581cf76a-cdb2-3a3c-a9eb-6228b0078345 | -10.11066 | -54.78704 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f98b5a64-749e-3999-bf09-312a03613067 | -7.34625 | -48.19226 | 2025-09-04 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf2c674f-68f0-3adf-9905-908c77b9ef41 | -4.99558 | -56.25672 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| a752d895-d1c1-3b40-87ae-db4dfaae3379 | -7.74534 | -48.76994 | 2025-09-04 05:16:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 57395c0d-df97-3cc7-8daa-e9b1c6080909 | -10.96789 | -49.76083 | 2025-09-04 05:16:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86b7d76b-89ad-3b74-9703-ebd50f890b37 | -3.62185 | -53.70605 | 2025-09-04 05:16:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a76d2d9d-d3ae-359a-b24e-db544fe9e866 | -5.31821 | -55.85497 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b5c26ef-ec39-3188-9909-cd79cdf28657 | -6.86751 | -45.57984 | 2025-09-04 05:16:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 839858d3-c7c1-37e2-863e-80265296d995 | -6.74456 | -58.72485 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a5a324e9-1baf-3e66-8490-5825c20e5491 | -5.30401 | -55.97205 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bb3db01-b2a4-3d6e-81e7-48d57281cddb | -9.60023 | -47.04022 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2106ff67-e209-30a4-bce1-928091a1cb8c | -7.68203 | -50.26946 | 2025-09-04 05:16:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4a4cb14-e21f-31df-9bc5-fd43d870b2f1 | -6.76941 | -63.12868 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0de7ed0-9ad9-3d27-ab12-048dde7f19dd | -9.61155 | -47.02926 | 2025-09-04 05:16:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b923b8da-df01-3c1b-889d-ce8ae6b7e200 | -7.68664 | -48.7265 | 2025-09-04 05:16:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e03f4b83-08cb-34df-a39d-cdae1a39a3da | -6.68677 | -48.41501 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd636641-5376-3223-89d4-027be0232ba3 | -9.47895 | -47.61292 | 2025-09-04 05:16:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b95aad29-9395-3c05-a4ac-65d056841f29 | -6.78681 | -63.14117 | 2025-09-04 05:16:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ca9c1f37-46cd-3da6-a975-a1b5cb1c7977 | -6.68727 | -48.41129 | 2025-09-04 05:16:00 | NOAA-20 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 743cb718-bb5c-3f12-9546-ff5e89ae1a8e | -6.83551 | -46.40097 | 2025-09-04 05:16:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4a2b65a8-77a8-3c82-abfd-23a8ce415f8f | -6.76189 | -59.66893 | 2025-09-04 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e35e587-0154-3070-b780-470fb112c994 | -6.62885 | -58.55378 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a147525-ec3c-3d50-9704-f1e5d02adcb1 | -7.86921 | -57.003 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc17da04-ff01-3b33-9822-b0220063b1da | -9.49815 | -57.81969 | 2025-09-04 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18226389-dbe8-3383-a143-90c95033959f | -10.89746 | -50.83518 | 2025-09-04 05:16:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e761098-d856-38c1-93a1-f08448f9fefa | -7.24995 | -57.55023 | 2025-09-04 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 46bfd77a-1a93-3303-8148-eb08434e62b3 | -10.09305 | -54.79541 | 2025-09-04 05:16:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46d1151e-654a-3775-af1d-1419b5c87e9a | -6.83956 | -46.39735 | 2025-09-04 05:16:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 522f98c6-5de5-33ff-aaa5-f8a8a5fc8845 | -6.53784 | -56.20024 | 2025-09-04 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 838c3a78-3950-3215-bd29-0d9015c06ccb | -6.74125 | -58.72433 | 2025-09-04 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ab36c41e-4e96-301f-9eb3-652748eaec43 | -5.31046 | -55.85798 | 2025-09-04 05:16:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 65a294d5-e9b9-3998-a7c1-1979f6b4d0f4 | -15.41633 | -55.94114 | 2025-09-04 05:18:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6fe82e62-2e6a-36b3-b557-ebb42a620440 | -10.24514 | -61.77397 | 2025-09-04 05:18:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15dba8a3-ed28-3704-8c63-77741b5fb4ef | -15.15185 | -52.38161 | 2025-09-04 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e873f41-1b7c-3c4d-bb12-b5b4cb4fcc55 | -13.10863 | -57.11288 | 2025-09-04 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f777f0bc-26dc-375b-b3c7-00655f666b51 | -11.67228 | -57.34776 | 2025-09-04 05:18:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 35.9 |


[Clique aqui para ver as próximas entradas](README85.md)
