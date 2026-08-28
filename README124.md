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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1bb023f-2a87-3d67-9cb5-9ba1ad28ed2d | -6.23791 | -53.48007 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a413a952-235e-3ebf-b499-1c37b42e5b65 | -9.69849 | -65.09579 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 6f3708af-d947-3a50-be78-8f765f35e8ba | -6.76598 | -59.46421 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 24e86c36-83ed-3c2d-8366-75ce698c57e5 | -6.45078 | -43.0807 | 2026-08-28 17:28:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cdaabe82-1284-30a3-b4ee-4d8462b2c229 | -8.56957 | -63.02231 | 2026-08-28 17:28:00 | NPP-375 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e865e629-a925-3153-81de-fce1f1306e6e | -6.82451 | -55.61378 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 6e692aa6-7ed9-33f2-9f85-7ea5350586f9 | -10.38891 | -61.24366 | 2026-08-28 17:28:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d084688e-8523-30f0-974b-9a35aeab62ef | -6.56581 | -56.53744 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6c2a044a-440c-3636-9214-69bc8db139b5 | -8.53735 | -55.3429 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 35684212-5c23-34bd-9955-2ac21fbba788 | -8.77946 | -68.98092 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 7d266126-796e-3b11-aa8e-b9b0a3a09e46 | -6.14866 | -57.94332 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3954879-1d09-3954-8835-4ab328369e1d | -4.05248 | -56.23351 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba5b288f-dbe0-3cec-be81-a915d39ecd0d | -6.12632 | -57.86377 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 8acb3357-224d-31a7-ad75-e4c2c0c3a5d2 | -8.54466 | -55.32337 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92ae9cf4-5235-3da6-9eb4-6eadc8f68b07 | -6.14388 | -53.7004 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 16b23be9-4da8-3a0f-8d66-278c51d4ca66 | -6.5971 | -55.43211 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 934c6b40-36d4-353e-ac75-675304b04d8e | -8.11549 | -51.66927 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 9498c6b7-373b-3c31-b9db-6084b791358f | -5.89494 | -57.7635 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 49d93f44-a399-3a01-a901-d40c2390ad0b | -8.63863 | -66.54239 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 228f5a02-57d4-31ae-8e3e-1ba87803d91a | -10.57701 | -57.49445 | 2026-08-28 17:28:00 | NPP-375 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6223f7cf-465b-3c20-a46e-61cc0006df32 | -11.41084 | -62.11755 | 2026-08-28 17:28:00 | NPP-375 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 08903953-3cfc-3c48-bfeb-b7749cc41fb9 | -9.97027 | -53.9376 | 2026-08-28 17:28:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a21ffb2b-2c34-3afd-9768-d5271e460ebe | -7.09933 | -55.47823 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 5e1d9375-153f-3bef-9bb4-c6772164c3b4 | -4.92587 | -55.76725 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| dcca0e87-06ba-3b6f-960a-27de68d793b3 | -5.98512 | -57.75652 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ab620aed-04bc-3c22-b272-9bde87f3d7cc | -7.60187 | -61.35299 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 437bd9d7-93ab-3116-9860-6544cf893aad | -10.05373 | -68.84288 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 917b3d42-929f-34e9-85e6-072ecf08933e | -2.72424 | -47.03695 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 02ee1dd4-e704-3cab-9ba5-00f9fa816dbc | -6.15459 | -57.80191 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 289b2f43-20f8-338b-aefe-0c457ab5a8cd | -8.06633 | -45.88913 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 9db143ae-f766-37fe-9e0e-0fe334899628 | -8.04229 | -45.85854 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| db0fcfa4-cec6-39db-b24b-e26d572dfbf1 | -8.67266 | -49.54752 | 2026-08-28 17:28:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 850c6171-6859-3a05-af76-a5756dd33644 | -6.26304 | -55.41451 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| feb385ae-9195-3470-850f-e1ae97667d61 | -6.76714 | -59.47215 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 4e939987-588c-3bbb-8091-f641e3a3cb44 | -6.84742 | -59.94462 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| fdb07e01-ca2e-336e-9503-7b2574a06d84 | -3.42851 | -54.82912 | 2026-08-28 17:28:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e91a76f2-e1eb-36bf-b79e-e5b873e29039 | -6.08767 | -51.749 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d95b60ec-33e9-34d4-897d-9ba9e7fa8625 | -8.11329 | -45.47585 | 2026-08-28 17:28:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ba1b4748-d44e-3e85-8ca8-8d67256e8610 | -8.93764 | -50.71356 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e7d4da65-97cd-3a07-8a71-75fa7f8d0daf | -10.50668 | -64.51579 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a97676b6-1cbe-3508-9cbd-4a5126c8ca81 | -7.3523 | -55.17339 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 3f282c3a-e25d-3b45-96ee-58c1a6770c51 | -3.2232 | -48.61453 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| dd179056-c430-318f-9897-f02abc59f73d | -7.5871 | -61.33447 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 4e6f03fc-8001-3811-a389-6778f43e088f | -4.8157 | -56.0873 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eadceae1-9768-3a69-a384-7b1207994c4c | -7.27997 | -49.95434 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 836848b1-258b-3415-b1ae-fddf69d49660 | -7.83189 | -51.3618 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4f46d81-235d-39cc-8a84-f8fa12fc1d88 | -5.47683 | -45.12011 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| bc3ddced-d32d-39ed-83b0-34fda52efef6 | -6.67182 | -59.07423 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 5c9d6b2e-881b-3807-ab54-888df05c1f16 | -4.35748 | -55.12677 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 1b396f71-7a90-3f90-b177-618bc91bd9da | -8.49536 | -70.4567 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 42d69cd9-e22a-3a45-80c6-02eb629ea976 | -6.01331 | -57.78453 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0add5338-f129-3fa1-9a3d-42973586fcca | -9.69199 | -65.08685 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 6a249bd6-af78-388c-b9f6-28e8a96bdce3 | -6.7819 | -59.44976 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5d782e08-d4b7-306a-8c75-5b87c3128f35 | -8.8082 | -50.048 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0740c49a-4ecc-3856-89a6-2adf2d160320 | -8.58903 | -54.82481 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b18cf2d6-c6fc-3442-83ac-a44c8b99ea0e | -6.02053 | -57.78703 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48fcb4e1-093c-3b60-adc9-abe0adf0d9e0 | -3.93254 | -59.33336 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 37f31031-28cf-34c2-90d1-c18c101da733 | -8.5511 | -70.47632 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e2ee5cca-9438-3088-a152-84a16c9469ec | -6.04326 | -57.80154 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f7f185fd-f10f-3016-a4b8-52b90f1301ef | -9.92117 | -60.43265 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 5a62684d-7fe3-37b0-982b-1d4284121914 | -9.61175 | -55.12084 | 2026-08-28 17:28:00 | NPP-375 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 78adacc9-0489-3ab9-9c77-8bdd14029c24 | -7.35854 | -55.16869 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 65a4c4fe-6e43-3ba7-a81d-a176a5ab3ba4 | -8.82889 | -49.63646 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7ee8d673-f686-38b2-9bf3-c3134adcd83d | -4.60484 | -54.86665 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| eb2b17e8-a989-3f23-859d-820f1663f633 | -10.48824 | -64.49376 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6d5c592d-674a-3634-b110-bfc149731cbb | -7.92227 | -61.36763 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| fee6923b-d247-3e07-9aa1-42e2b664075f | -4.47165 | -55.89775 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1726f9b-3e5d-36de-b029-3d8483a2b63c | -6.83517 | -59.73647 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6108bab3-1a37-3b2a-bab3-a1ec0a52dc0e | -6.7966 | -59.45158 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 36e43238-d49a-3386-8291-a747e2dadb94 | -9.0305 | -69.58498 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 84851088-53b7-3a68-96b3-fba4a847d53a | -8.4439 | -70.70377 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 4b59ede1-0feb-33f7-bce8-af1773f1b3a1 | -6.54665 | -58.59222 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5f82bab7-07b0-3ae7-b449-44fa2246522e | -9.16579 | -59.57889 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4f98e20f-9f6e-3968-a3da-12b5f7058d26 | -10.75592 | -54.00583 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 36b7f222-6677-3596-a246-3a14b9050b8d | -6.33093 | -57.74216 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 90312cd6-676a-355d-a845-aaeae2a1d5f3 | -8.59856 | -54.77397 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 744f779c-5f13-35c1-a660-eb6762f13420 | -6.78484 | -59.4453 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 1e1f7772-13a8-3c86-8072-2fa42eef62e5 | -6.58917 | -55.42591 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 58e4b823-da06-319f-9917-e44bf3a36874 | -9.92707 | -60.44666 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 43924b8d-32f6-3744-8ee2-c8c09f798e4a | -8.05034 | -45.85692 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bd27ac06-107b-31ab-962c-712b8dc2090c | -5.78767 | -57.56555 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a144357f-0bab-358b-9fc1-f908c106c4b4 | -9.69766 | -65.08938 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 744fe65c-55da-3560-943c-b4ce4fc7e48a | -6.72756 | -48.7407 | 2026-08-28 17:28:00 | NPP-375 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 5b7f6577-873d-371d-99df-8d7bcb86623c | -3.42989 | -54.82572 | 2026-08-28 17:28:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8833f77f-d6fc-357b-b6d0-d81fc2581a68 | -7.59187 | -63.36532 | 2026-08-28 17:28:00 | NPP-375 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7f8a9d9b-ef7e-317d-962a-d307924ac8d1 | -6.17322 | -55.46602 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| c9f3eb6e-40e5-3254-9a6a-83bc1e1c6628 | -5.14684 | -56.27211 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a169d7d3-30b3-3038-a1e9-f37843cbf993 | -5.88492 | -57.76506 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| c05fa129-8aca-33d7-bb79-567179fc8f9e | -6.82616 | -59.57735 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e5ec60c-f09c-3cae-8ef6-76997e3a0acb | -5.91645 | -61.29979 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 3ed1e459-ddd1-3971-b3c4-2175b1a84950 | -10.2605 | -64.49987 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d25a97a2-e4df-3dd4-80ca-ba5b61af06a8 | -4.33302 | -54.90382 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 44ec4461-90dc-33e4-9774-5ec5c67fba0e | -6.61012 | -55.44871 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c116f8a1-f880-3aea-aed2-e27d91727754 | -3.93597 | -59.33286 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 3dc9de4d-2ce4-304a-8cf9-01dc1d46e36b | -9.0868 | -50.59935 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9d01c72f-11c9-328b-9ae6-210279f42033 | -4.39209 | -55.45832 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 6c997948-f5a2-387c-8767-7cf93d9513e8 | -4.90164 | -57.51708 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c1d2b48-3d22-38cc-903d-24ea5b6da371 | -10.4765 | -64.48318 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.7 |
| f3e5e6d8-0423-3af9-bc6c-57aa718cf6a9 | -8.59572 | -54.77821 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 0d0af851-da75-33d2-ac0c-37fffd50e03d | -9.44692 | -51.57919 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README125.md)
