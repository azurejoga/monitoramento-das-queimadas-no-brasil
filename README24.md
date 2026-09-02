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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59dc6109-45c0-3b6b-8e0c-34963bb7ab60 | -12.11102 | -47.05223 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24120162-b73e-34d6-93e5-21980ddacf2a | -8.4675 | -54.72629 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 959a565d-09a2-3584-b518-79fc7bf6111d | -11.67789 | -50.47374 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98c6b662-98a2-3f14-8e2d-e5cfd1f04eb0 | -11.32093 | -50.60304 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ad816ea-e0c5-31f4-b668-3b49f8f14e6a | -12.35007 | -45.68032 | 2026-09-02 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6c59428-38ed-3f50-a2c7-1e82bf755c5d | -8.47725 | -54.70269 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c497d146-98eb-3ccb-97ac-8fd2f0426031 | -6.94621 | -56.46377 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0a19bfef-861c-3c3e-a880-bd68a0e62264 | -12.05329 | -45.00195 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e9c98e65-fe88-3df6-87b7-a12d4a811764 | -11.4833 | -45.08564 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b88ea43d-2d42-37dc-bd7c-3177f29747a8 | -11.90174 | -45.08135 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7431fac-cde3-3040-a31b-49eae0ca96f7 | -10.78495 | -44.76499 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b618cdf5-08d3-3bd1-b475-05d34a5d8b1b | -6.94002 | -56.46279 | 2026-09-02 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 133113d9-2cb6-3c75-b312-2b83e07cdf5c | -12.12264 | -47.06512 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22ec3f24-2935-3cbe-bf95-687587fac941 | -10.90406 | -45.33784 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 380d6080-2f70-3c12-a3c8-c52303ea86b7 | -12.17702 | -47.08873 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 50d2049a-535d-3df7-9239-ad5df46e6d44 | -12.13066 | -47.14357 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 802099e5-3216-3e8f-8f4b-64f766548b14 | -12.14295 | -47.13088 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 70f527fa-3fda-340a-a579-46c45818fffb | -10.72747 | -46.18802 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55ff60db-34d4-34dd-bc5a-d5006cfb2b34 | -8.4731 | -54.69489 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 3a35d425-e7b7-320d-aacd-f02e6316c4cc | -12.37961 | -48.14925 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5292a7a3-4754-3813-9708-f747aa289614 | -12.14971 | -47.10992 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e3559b3-05bb-349e-a757-8427e1a8f0e8 | -10.78605 | -44.75785 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 64c3765a-00f0-34f7-8d25-1532ed07873b | -12.11769 | -47.05332 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1907c19d-8255-305e-bf5b-8112d8f8228c | -8.46939 | -54.71569 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c2d5d174-88c9-3534-8b57-6461e8d34092 | -8.47569 | -54.69565 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bbbff867-6c50-37d3-8f12-b1e138f308c1 | -8.4557 | -54.69907 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1e2d270-1260-3e2f-855b-59948176bde8 | -15.03282 | -48.1869 | 2026-09-02 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 572de4f0-ebc0-36ba-b1bf-486be750e5b7 | -10.77203 | -50.48943 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88c38b44-b6f4-3a3d-a5d2-15fbc62fcd5c | -15.3645 | -47.04292 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8106b394-1c46-3534-b737-80b0f3e36b3e | -11.67783 | -46.73989 | 2026-09-02 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c122c1a5-8b8b-3554-812c-d555c11915d7 | -11.6351 | -54.56416 | 2026-09-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c64d3c1-b09c-3a77-9382-df8dbd4b3779 | -14.11329 | -45.50254 | 2026-09-02 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb3b2e74-020f-3008-8e9f-eb79c6bf608c | -10.78829 | -44.76553 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ee96ef-7117-3079-a1e3-7e4b174a6f6f | -8.47663 | -54.70618 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2c682462-841b-3053-9a99-4e71642793f9 | -12.1502 | -47.12838 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 68d8e7aa-42b0-35ab-b13f-ec576ebb4e75 | -11.29884 | -54.05861 | 2026-09-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 482d497c-de67-3bd1-8932-7b39516e4b99 | -11.62451 | -54.56503 | 2026-09-02 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9280ea78-8417-37b6-9fbc-db61b113d04a | -8.44368 | -54.70415 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f7e4a3b-b5fc-35b4-b67e-4353c39529ac | -15.3474 | -47.04373 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08236211-7291-387d-b278-5a257f35353f | -13.70935 | -43.88169 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74e54c99-c3bd-3ddf-9a96-f1434a65c605 | -8.45362 | -54.74168 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8f449ed6-b92e-3113-8597-4d6a8d4a41fd | -12.15191 | -47.11763 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d82c149-db46-3859-b3ac-e36f8d7a8952 | -11.31189 | -45.16056 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0c560c1e-a8ef-3714-af29-c165e2373448 | -8.49863 | -50.29691 | 2026-09-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08309364-256b-3c2c-a5c1-4de7e2f7cd8b | -11.2914 | -45.16096 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 09c95939-21db-3f7b-bc66-2ed157ee4505 | -11.90114 | -45.0629 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbd2ee67-f29c-3313-8d40-65cbdd01e0f5 | -11.34485 | -50.62799 | 2026-09-02 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| feafca6f-bc0c-332e-a4cd-c6fffb73426b | -11.34798 | -45.41226 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba171e87-9bbc-38c9-8aaf-24cd5e40d4ec | -10.08663 | -46.7324 | 2026-09-02 04:21:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6184a32a-29d5-3f3a-baa3-a4c44e650e3e | -12.13931 | -47.06783 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2c6b714f-a542-3285-932d-afe228afd34f | -13.39951 | -51.38733 | 2026-09-02 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31e12030-61db-3aeb-9905-6ea5dcfb3e96 | -10.70873 | -46.19935 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f94354a-f3fb-3f70-a0cb-63984bce8187 | -12.07508 | -47.12709 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfd6ee91-db68-3332-971d-18a4736239ab | -12.38365 | -48.14604 | 2026-09-02 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 843801d6-2612-3d7b-9135-35578b1fab5f | -11.03727 | -49.66743 | 2026-09-02 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 28a087cf-64dd-3e5d-932b-30b6fbc86856 | -12.14848 | -47.13913 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 92f9a1a1-1578-3477-b729-f7021e44f243 | -10.99503 | -45.07797 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 773c7ad6-a9cb-3e25-a104-72036761f945 | -10.32391 | -49.95159 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40143518-a0d5-3fc1-b1c0-bb365e7a8727 | -8.28686 | -54.91214 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 250b6a9b-3f73-3825-886e-ed10dc3f9e1b | -12.13207 | -47.07031 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46006928-5da1-3cb4-946f-f962086addb0 | -11.29697 | -45.16912 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9e8484f3-9cb5-3169-b287-816686954c5b | -8.72757 | -49.59629 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9431dad9-2317-3c2e-9e84-4847800c47be | -12.15353 | -47.12892 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db85f1e3-dc07-3ebd-93d8-dc63223b36fb | -11.78183 | -47.67876 | 2026-09-02 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ad65f20-4a30-3c2a-a89a-526408f359f5 | -12.13856 | -47.11545 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2b622d3-0f53-3de4-804a-b4dc3b26ef9a | -12.8777 | -45.82951 | 2026-09-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 068122a7-56aa-3bf2-b78d-25169e6dc49e | -8.12005 | -54.95413 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 89a173cd-e6f4-3fe9-a518-d192014a1980 | -11.30084 | -45.16608 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b6ab5b7-1336-3361-b4ee-2ce3df00153e | -15.67041 | -45.8935 | 2026-09-02 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1cc5b23c-6011-3d66-9d3f-6387b823a0ac | -11.82217 | -46.05973 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1898d8e3-4974-39fc-9ca5-1c85f0fe20f0 | -14.9917 | -47.97254 | 2026-09-02 04:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aae3a88a-8f73-3c7f-8329-330e047a5222 | -9.7261 | -47.76782 | 2026-09-02 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dfcb0ca-4202-33ae-9b77-77625b9dfc9a | -11.82988 | -46.05378 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cc9a85a8-d8bd-3667-ab0d-91240182f39d | -10.32047 | -49.10787 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de913621-14b7-382f-b724-c63811ddf2e6 | -9.22402 | -47.97754 | 2026-09-02 04:21:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acf2bc92-6679-366a-878c-dfb66e046677 | -12.13475 | -47.09645 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16addd77-65e6-34c3-8432-4b5b8349af75 | -10.31303 | -50.03835 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21d26333-b2ce-3a01-8462-f296eacfeec1 | -8.44782 | -54.71202 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef7795f9-ff93-322d-974e-d9f90a40f86f | -11.67377 | -50.20062 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff57be3a-ad94-3943-bd9e-e88f263c3b82 | -12.14962 | -47.13197 | 2026-09-02 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 82c215a4-54e4-38a1-9f52-d5e1b8dbdee7 | -12.15263 | -47.07003 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38dc0f9e-75a1-3d21-954c-e85423af934c | -11.30369 | -45.19202 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 438ccfd0-54c1-3606-8914-8a6b640be1d6 | -11.48221 | -45.09275 | 2026-09-02 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 845fc333-fa21-3873-8f4e-d27b25ef26b1 | -8.46859 | -54.73379 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59949237-56ba-3123-a1bf-02f0f4bebe6d | -15.35732 | -47.04538 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10e96688-9bc6-3f38-a204-b8f678f01e4d | -12.13435 | -47.05603 | 2026-09-02 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e9ea36c-cc97-37d2-a7fc-06b858322777 | -10.74012 | -54.03681 | 2026-09-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 700caa88-20f9-32e7-b1c5-8af4022a36b9 | -8.47441 | -54.70253 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2ecaea90-f8de-3e21-b19b-ca94d9067bc6 | -11.29086 | -45.16454 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9f6cef92-c83a-3465-8648-527789aae486 | -8.45796 | -54.71742 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 46ee8e34-f207-39d1-8fc4-e8f495ca70e9 | -10.79163 | -44.76605 | 2026-09-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 764fe0ff-0ec0-3301-8da3-3103e0f97217 | -10.44297 | -46.71732 | 2026-09-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb5ff17c-80e3-3c9a-82c0-9fd4767682cb | -11.83871 | -46.06239 | 2026-09-02 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a976dbec-9295-3394-a396-3bd99be9ae7c | -11.30633 | -45.15242 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 20f5fa90-c2db-3f0d-8f49-d522867259ff | -10.40376 | -50.00689 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 522956ae-dd3e-3f70-a512-3356f64f66ac | -9.94382 | -53.98837 | 2026-09-02 04:21:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9520bb8e-85f5-3ca7-9a9e-42f9ec766125 | -10.90846 | -45.33134 | 2026-09-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1c06634e-1417-3c39-8159-df74362cb00a | -12.46987 | -41.3113 | 2026-09-02 04:21:00 | NOAA-21 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 64003e55-1a30-3eaf-ad1e-ef5f4524d73e | -10.3209 | -49.94619 | 2026-09-02 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0540e33-092b-3711-b085-38a76edaaf5b | -8.43641 | -54.71368 | 2026-09-02 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
