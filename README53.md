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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| edec9694-158d-313c-8158-80e11926a2c7 | -7.73289 | -50.29689 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ac9ab9b-217b-3058-b9e3-4d7b9815410a | -8.29419 | -45.16773 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 541bba08-dc3f-31d1-81a9-01ee4db6528c | -6.71302 | -43.09335 | 2025-08-28 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 58087b44-6d80-32d0-a2a2-52d0a256c78c | -7.74945 | -50.27588 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1d37567-107c-301c-b681-f13e9d4a296d | -7.57092 | -63.86451 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66806686-f712-3b6e-8fdf-48f1bc3c468c | -4.08062 | -48.04618 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0e84aa7-b6fa-31b9-a59f-932b71d9bad0 | -6.91039 | -62.93876 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fabaaad-2f87-3aad-8ea0-9284b24ab65c | -3.24109 | -50.80302 | 2025-08-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb0460f5-9b8c-3f2a-a9e7-d8f8cbe60e97 | -6.89946 | -62.9349 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8512521d-218d-3d36-bc17-d9873fc72cd2 | -7.06102 | -44.36707 | 2025-08-28 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 61a62e63-e70b-3155-9854-861833ac2e38 | -6.22504 | -43.36356 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21c6b2e6-6af1-3957-b924-33012766a72f | -3.75996 | -49.05874 | 2025-08-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c1719fa-1fd8-3a85-bac3-26fa317de81c | -3.09931 | -54.59492 | 2025-08-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aea2365-84f1-3bc3-9e5f-126ad94efd47 | -6.22567 | -43.359 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cdbf9741-2bdf-337e-b643-117e5a4ad3f7 | -8.28722 | -45.1781 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 75ccd575-7559-331d-9dd1-22a358864346 | -4.89078 | -55.80979 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3e10798-654c-3c5d-8409-82e5ea1b80ca | -9.45563 | -51.94922 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| eda4b857-c5b1-3aaf-b09d-33b9a3aad094 | -4.05685 | -56.32935 | 2025-08-28 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8af9dff4-31ad-3522-8efe-32d75de0f4c7 | -8.44636 | -43.66276 | 2025-08-28 04:57:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e712222-2a83-359c-8b8d-2d3a997755c3 | -6.15973 | -44.18427 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e6edac9-f557-32ff-8e2a-3c4bf198a56c | -6.87139 | -43.60212 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4b9e533-243a-3680-8e29-8153683fef3c | -8.0879 | -44.9834 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b05c72e-38cf-34a8-a49b-c67080fa4257 | -6.65559 | -53.19021 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7f44945-3d0d-39c0-9c76-fac605283ac2 | -7.74739 | -50.27899 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 496c00f4-98ed-37b0-abd5-1bf1fee57266 | -8.28173 | -45.17731 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.8 |
| fb0256e8-945a-3ef6-8372-92d7a4a2b1ac | -9.45624 | -51.94495 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 71def9c9-0f5b-3ba9-8fe7-1a0ad2be5a73 | -6.85944 | -43.6216 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bed92af3-92df-3482-89dd-0d3f566f4eb8 | -6.90481 | -62.94087 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3db57082-90c3-3ea1-be1e-74c1036279b6 | -7.34901 | -57.63003 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a6de00b-8b65-3d95-8855-55755691b7db | -8.29321 | -45.17511 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c1b00645-0617-3446-bfb2-cef398233e0f | -10.3707 | -45.1695 | 2025-08-28 04:57:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1236ee57-4844-32ff-a07e-934d26149761 | -9.66469 | -48.31626 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f0be31e-138d-31e9-8067-2449df718d32 | -8.8624 | -47.18557 | 2025-08-28 04:57:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 325c6741-4040-3f76-923f-cfa116a2add3 | -7.45061 | -57.62957 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eddc90b6-24a9-316f-804a-291188d41cda | -9.45861 | -51.95401 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0b5e9fc-7dfb-3605-a2ea-ab9e8e485688 | -9.46764 | -51.94236 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5801a47a-869f-3581-91da-b40ef864caa6 | -6.81429 | -44.99817 | 2025-08-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8672f65e-3eac-30fa-842b-946b17a74bd6 | -4.79866 | -47.25832 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1fb1eb2b-bfa7-3ba2-9630-dd1739d68dcf | -6.44382 | -44.57757 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| be5f4090-1719-35de-9ee3-a1a702d4dea4 | -6.92318 | -62.94814 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 117d7e26-04c5-31f2-8a56-6cf4d4483286 | -9.45501 | -51.95353 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c6d7fdd2-a708-3279-ab0b-951c83860e08 | -6.86004 | -43.61724 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9357dc6e-810a-3844-b6e4-a74e4b122c4f | -7.19551 | -44.06272 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03e7bb6a-0323-3956-9855-6b1335d5e83e | -9.45358 | -51.95063 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c48d4c4e-cb31-3b94-8129-891076805d7a | -7.73574 | -50.27769 | 2025-08-28 04:57:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88c7e941-198a-38f3-a47c-410b484bc098 | -6.57187 | -47.383 | 2025-08-28 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f174b7e-2e61-36e8-8a59-47d21f87fcf1 | -15.66969 | -52.74102 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| beac8370-f858-3e91-bd52-29c9ccd9444d | -11.23238 | -55.0514 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6088b5bf-22a1-34c9-91c5-c832d66cc186 | -15.18851 | -52.33734 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e9db0b1-3d06-39b8-9e89-d1643aa35853 | -9.54274 | -68.58142 | 2025-08-28 04:59:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2bed1e4e-0026-327a-955b-dc14e620faf2 | -9.39715 | -60.51999 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66141d3e-80d3-3fbe-9a4d-4291df5946e8 | -13.52083 | -46.88297 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f940a76a-a209-3068-82f5-da386f5dc3fc | -13.45574 | -46.84757 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29350677-6760-3837-a407-e70f82921867 | -12.67586 | -48.17372 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d150512e-401d-34e8-a02e-3f7204a0575c | -9.73167 | -64.90324 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4b56816-e3bd-36ee-a058-644f6013cf59 | -12.7287 | -48.18283 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 797ba4a3-a5fe-3fe9-b14e-b33cb406151e | -9.23205 | -60.91465 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e24f1a71-02d3-37a7-b57a-cd2769a85701 | -13.66997 | -46.88637 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9723801-abe0-3c11-89e4-970fa170d86c | -14.31496 | -60.35535 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0c16b39-09b3-38c6-ac91-2f5df1621876 | -10.47529 | -57.93451 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 15efbbe1-31c4-3ab3-a7c3-f28c90aef48a | -13.18643 | -45.28514 | 2025-08-28 04:59:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3213461a-7432-3c6c-8471-fcca2590583a | -10.61234 | -54.90576 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ed669ce-2d4d-3b50-bac0-9ac53d8199d9 | -11.36671 | -63.26795 | 2025-08-28 04:59:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8d6a6dd-f4ac-331b-ab26-e69f2c86662b | -12.41069 | -46.4836 | 2025-08-28 04:59:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c4e5f19-c1b4-3d94-a771-3aba0117560e | -8.87484 | -60.76888 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eee0bfe-146e-3bce-8c32-1b6e0d9fb3fd | -8.94906 | -65.96189 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e02c1f6-3a31-3d3d-bed6-b57659ecb052 | -11.61134 | -46.2155 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ea250187-0fb3-3237-875d-c1f6e12d51dc | -8.93105 | -65.94212 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 002efc86-b679-3728-ac0c-adf97f0b3afd | -10.47065 | -57.96225 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 285cd4ef-ff89-36fd-a815-7b87ca5cf11c | -11.33394 | -43.52776 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 710e16ae-9a03-3afd-8857-670268ad1389 | -9.13363 | -65.78368 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f003949-0d28-33f1-91f5-58b631c3801c | -14.26575 | -53.08078 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b936629-a856-311e-a5fa-7d04100fa6f6 | -14.3451 | -53.35433 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3610b9d9-5ebd-349a-8da2-a09b4b412a8d | -11.57509 | -46.4173 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ef06af2-58ed-3a3e-b58c-6d96601848c1 | -13.61855 | -48.23585 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| be942a15-641d-3021-9b79-3aa4690d357f | -15.62082 | -52.75001 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ed5366-cb4a-3048-aa13-245d27079b46 | -11.16805 | -50.5397 | 2025-08-28 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4902db8b-8ac3-3371-a50c-9bc1c4be6fa5 | -13.51253 | -46.86269 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2309728c-ca03-3d3c-a224-92791122654c | -13.51599 | -46.8787 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86f4ea52-2ebb-3224-96bf-5050bfaa752a | -11.34159 | -43.54163 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 40fe33bb-7aea-3760-a191-37b34daf897f | -10.28526 | -64.49403 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97238d67-2842-3fad-836c-06dbe156ccd7 | -8.92165 | -65.92663 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 872d7012-b9a1-3748-ba4e-7e33ea61a1a4 | -9.15236 | -62.35361 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99299d4e-958d-3fa6-a2ce-4dbe43a1a6d3 | -10.03435 | -59.3591 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc028208-77ab-318f-8a6a-86c6c33b38cb | -14.14018 | -45.40674 | 2025-08-28 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 680d646c-a445-3c87-a7c5-f5ecb960fba2 | -13.52133 | -46.92358 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e3829ef-c071-3c1c-bba7-0cf22c8b71a7 | -13.62745 | -48.24334 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7f20857b-686c-3a7c-853b-e3f451fe36da | -14.32237 | -53.05764 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e60a30b8-2b67-3d67-9e40-a8a062ff3841 | -13.53096 | -46.88784 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| badd997b-9d25-3beb-a4af-439376e2f38c | -10.48319 | -57.95201 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6be29bc3-522e-30f8-937e-ba0955ee59eb | -12.93088 | -46.32202 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8babc4e3-0f73-3fb2-864f-fb7df5c2c7dd | -10.60748 | -52.33255 | 2025-08-28 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42b7297a-6a09-3f80-accc-2436a476ffc3 | -12.67495 | -48.1857 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cd3a8ae3-c413-344e-b9e1-18a5222259aa | -12.18625 | -47.18209 | 2025-08-28 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07d4899a-2bee-35f2-b0b9-106c80a888d1 | -13.59677 | -48.21928 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 77365004-8b9b-3734-b4b9-c3cb1d6bf915 | -9.10439 | -60.32774 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 630f7499-1950-3733-aa57-6c64bc542274 | -10.47683 | -57.94691 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87892215-142e-3e1d-8b4b-f4aae6b3161a | -13.6348 | -48.22301 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6679ebb-d9df-304b-9e99-68c79f3fbc6e | -8.25754 | -61.45839 | 2025-08-28 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8843a1fc-74e3-3854-81be-c5fe30e61bb2 | -12.67928 | -48.18464 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README54.md)
