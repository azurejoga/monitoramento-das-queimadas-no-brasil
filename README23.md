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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59abf869-61f6-3802-904c-20cbca639052 | -7.1294 | -49.18365 | 2026-09-30 04:32:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf68ddf8-e517-3a57-8c53-df7221afac2c | -5.10594 | -45.03884 | 2026-09-30 04:32:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e8ead26f-5b32-368f-bbc1-cb238f6a41ad | -6.1642 | -44.6185 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8202ce9-33a3-316d-8cf1-efd09e1abaf8 | -8.97459 | -44.17001 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| feb7e810-80a3-39a2-917b-b850fd163ec1 | -7.81021 | -45.81683 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c73a21f8-416b-3fdb-97b0-fcd84282a90e | -3.3763 | -50.95496 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b9a828ea-e866-3cb5-af06-35fce4254382 | -7.83366 | -45.82057 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f0322858-0233-3923-837d-9ace0f2f43a1 | -2.99582 | -51.04394 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52711de8-9ddc-3959-9788-c96f96bd7b0a | -6.18695 | -44.64701 | 2026-09-30 04:32:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7eb0edb-1e70-30ed-a242-e4ab2ec2de7d | -6.21268 | -42.51369 | 2026-09-30 04:32:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 2a239013-77a3-30b2-a5d1-ed1c494a2a08 | -3.25056 | -50.81085 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| f881822e-1242-3279-b035-3e913925529f | -4.46648 | -45.58389 | 2026-09-30 04:32:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2131a4d-5335-3ea0-aa1f-ccb818315d31 | -5.74833 | -45.16956 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 00ffcf3a-a659-3a51-80aa-fbd9fd89221b | -5.0311 | -43.56962 | 2026-09-30 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 908c2d05-d5e7-3e19-99b3-e2afdabbd757 | -7.81299 | -45.82091 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 863dd2e6-fd9d-3c4b-ae7e-9e9b2820087c | -3.26936 | -50.14094 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc450333-ab2b-35f5-900f-501afb124b92 | -4.80272 | -45.64387 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e1846b-43dd-395e-b4f7-735809b8f961 | -7.03049 | -44.29161 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 278e7aec-8e7d-3d47-ac79-2f9b4608712d | -2.37634 | -47.60728 | 2026-09-30 04:32:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0825965-4cb2-3afb-9feb-d0252d267dcf | -7.92904 | -47.37615 | 2026-09-30 04:32:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d86cf830-9cb6-3eb5-9614-716522f299cc | -8.83563 | -49.711 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 144619f5-a330-3de8-be35-44e60f168724 | -7.82361 | -45.81897 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8dce6664-1e45-313c-9bfa-58a95ebb4c50 | -9.09291 | -47.17139 | 2026-09-30 04:32:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f531bf9-fd9f-3bdb-81af-a341a5f84b19 | -4.14128 | -48.89759 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d4efbe9-8693-3fd0-8915-0e0603e9b163 | -4.36054 | -47.77708 | 2026-09-30 04:32:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9f00cab2-4f22-3071-9b3c-e0485c2dc089 | -6.92495 | -44.55742 | 2026-09-30 04:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93e91609-ed24-3667-bc6e-80c370d39226 | -7.42598 | -55.18111 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b9b8088-2684-3f32-8dc5-2408dfcb642b | -7.18885 | -46.50654 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b5e4ac2b-c50e-3141-aa2d-16bcd7767068 | -4.11657 | -48.82544 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7b7a2c9-7cf4-3114-8e8c-28aa4c0fb898 | -3.23163 | -46.94535 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11fd1fed-cd23-3350-925b-a5899d05d31d | -7.72052 | -47.05999 | 2026-09-30 04:32:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9475423-2b76-3b21-9c65-94b84c885143 | -6.92773 | -44.56142 | 2026-09-30 04:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f828a058-f47c-39ad-86bf-b69ae49cf271 | -6.13284 | -53.05566 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f89e1917-5e7b-3cb2-b480-f9d3432c7a52 | -6.12682 | -53.30187 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7fa1449-5fa1-3de3-b77d-3d729911427d | -8.8404 | -49.70674 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c6a8cae7-5669-334e-bcca-025748d15f8b | -7.43169 | -55.18237 | 2026-09-30 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65f60453-c93a-3b38-adeb-b3ef0e2ebec2 | -6.33239 | -51.16068 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a5c7205c-fcfa-349c-ac3b-eec91bf5ad3c | -8.8314 | -49.7132 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8082d75-5e55-3ad4-91a4-33681b916afb | -5.8738 | -50.16365 | 2026-09-30 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 70102771-84d5-3a6f-a136-abb61e51fd6a | -3.56478 | -50.25432 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94b43172-66f9-3908-b560-28a3e7565e10 | -8.58857 | -50.41551 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12193763-bc20-3f2d-8edf-98752bf49792 | -7.84983 | -45.8268 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4147c6f6-e577-300d-9dec-3813d79028d7 | -6.12826 | -53.05179 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c7846c9-4320-3253-a288-d20575d21206 | -6.12739 | -53.29863 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c4265d8-61fe-3f17-8ec1-8379536d42a6 | -8.77285 | -47.84201 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 590a8163-7749-3ce7-9bd8-732db55972c9 | -3.24692 | -50.11662 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8926c848-f913-318a-bea7-e6245dd76c6e | -3.85867 | -49.74317 | 2026-09-30 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6b75b24c-d90c-3d7e-87e5-8c9eacba7ff5 | -6.09979 | -53.09339 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 755c4bf6-d7bc-34d0-81de-69569d672be6 | -6.12536 | -53.27962 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3a1dee3-470b-3dfc-b1a5-f91075274531 | -3.23817 | -46.95059 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa7abf8b-16d6-3eaf-9194-8416a1008084 | -6.99676 | -43.86185 | 2026-09-30 04:32:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f3c8f6d-09ce-354e-b28e-f24ab4695056 | -3.95798 | -49.04979 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1c46303-135b-3913-b4b1-9df318028fcb | -4.11742 | -48.82041 | 2026-09-30 04:32:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| a163d2d3-eae1-3f3e-af7b-9ab2c48b79b0 | -7.50533 | -44.54559 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44bf157a-7354-3abc-887b-05c861b33fed | -5.74387 | -45.17604 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 363d5c47-d7b1-3346-a999-af63ad65380b | -5.73618 | -45.05291 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 427f52cd-d7de-37e2-99c1-2886bc516393 | -7.37968 | -44.77911 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ef1605b-cc55-3dc7-917d-e369c1ab1233 | -7.49446 | -45.80211 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3cd4d31-281e-3ce3-8351-21699ebf8af4 | -3.03252 | -48.41505 | 2026-09-30 04:32:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d13cdc20-9ec3-3204-adbc-c7a5c785d26b | -6.32714 | -51.16439 | 2026-09-30 04:32:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c916b41f-5f01-3f76-8a89-dad1e35911ca | -7.27102 | -45.31926 | 2026-09-30 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f1c9dd7-2464-3940-bb5a-b146e8ac6aae | -7.50866 | -44.54611 | 2026-09-30 04:32:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46419e13-c642-3666-8fd0-7df19b1cc5ec | -5.71641 | -46.19448 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd89f254-aa20-3e9c-9fa6-9bd5a312d19b | -3.22926 | -46.92929 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24edb873-95d6-31ed-b29f-df43a1a93b5d | -3.14843 | -54.07675 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffa90a00-2404-3f67-b750-ecd80821e7a3 | -3.16293 | -54.0955 | 2026-09-30 04:32:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da6dba72-4cf6-376c-b29a-833e29bbf806 | -8.98582 | -44.17204 | 2026-09-30 04:32:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 555d553e-7f2d-3376-93a3-f4e13f5a046b | -2.27477 | -48.75434 | 2026-09-30 04:32:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f67ac910-72a8-3387-8e37-ed49788b5997 | -6.36656 | -46.2562 | 2026-09-30 04:32:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9712931e-3a2b-3dfe-a7e4-c13e4cb88050 | -3.11257 | -50.28036 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8908e239-7bde-3b18-81e2-961c4de21739 | -3.74897 | -46.13915 | 2026-09-30 04:32:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5c956d2-8f59-3fb7-a3e9-2dacec16279b | -6.59911 | -43.9225 | 2026-09-30 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dfac92ea-4a32-3c22-bc13-215e77297b2f | -2.97948 | -51.04417 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| eaef23e8-ebf1-3947-9394-a418629a29a7 | -6.10491 | -53.09431 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6611933-ceb6-327b-b19f-3d00aab9267d | -3.23365 | -46.93305 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7fa062a-4dba-38ad-9cc3-fa74c2d27fa5 | -8.83696 | -49.704 | 2026-09-30 04:32:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9f0fac1-e3bc-3d33-8f2e-a9cea5116a90 | -2.98187 | -51.02944 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a086ae38-a094-356a-9ae3-deeaa5b4667c | -6.1248 | -53.2828 | 2026-09-30 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5d79a8c-98b3-3ec6-9c5e-e66edfce8f59 | -7.02871 | -44.62714 | 2026-09-30 04:32:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8930ff4-6149-3f17-8a8b-3e2930cea78e | -1.4911 | -48.90978 | 2026-09-30 04:32:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a0e4b5-750c-32a6-a0ac-2663e2863d6f | -4.81682 | -45.64249 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d94ff876-9fc0-367a-9bc5-5eed3c871d28 | -7.01693 | -45.29675 | 2026-09-30 04:32:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f067a449-d2c8-33ad-92c7-d852f5aaa2ba | -5.74555 | -45.16552 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0aa31b51-b2dd-3d7f-80f8-a9cacf93012a | -3.38252 | -50.94615 | 2026-09-30 04:32:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22bc9d00-ec0b-3b29-a4bf-445c81a63627 | -5.32801 | -46.19781 | 2026-09-30 04:32:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 176fd643-398c-3531-a38a-4128423205bd | -6.9244 | -44.5609 | 2026-09-30 04:32:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a088f518-aacb-3385-b25a-8d0230cd9709 | -4.8033 | -45.64026 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e55641df-3017-3e02-91ff-e99499bfafd1 | -2.98811 | -51.03262 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b2ff0ad5-5655-312d-aa56-8ffad530f1da | -5.72891 | -43.28319 | 2026-09-30 04:32:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 066f64a6-6fac-3069-be54-1c599d225f6f | -6.32889 | -43.91649 | 2026-09-30 04:32:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f1538ad3-b8c4-3759-a608-b4147716ebb7 | -3.1037 | -50.27886 | 2026-09-30 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c878c0c4-b45c-3d62-ab81-47f31efbe7a2 | -8.39013 | -45.44518 | 2026-09-30 04:32:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 166b1d62-6b91-3fa0-bd69-f04f2183908e | -3.22306 | -46.94505 | 2026-09-30 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc65d876-a630-3629-8ce5-812f0b22af8c | -5.73943 | -45.16094 | 2026-09-30 04:32:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4504866c-8716-3a7b-9aea-44e2a51453d0 | -7.50103 | -46.65176 | 2026-09-30 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5845efbb-ed28-3536-9bca-4df41c371b2b | -7.50628 | -55.03938 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d86c8d51-5e3a-3fad-9155-3f39549e5247 | -5.0272 | -43.57259 | 2026-09-30 04:32:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7da20063-cb72-399f-8b9f-d1a305b6cb14 | -4.80948 | -45.64499 | 2026-09-30 04:32:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5be55318-06de-3923-9b60-0bd3d93455bb | -6.7473 | -55.08044 | 2026-09-30 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab201294-1407-30b0-97c7-87322c033288 | -7.84648 | -45.82626 | 2026-09-30 04:32:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |


[Clique aqui para ver as próximas entradas](README24.md)
