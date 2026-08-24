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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d216e30b-5a5c-3ba3-8a6f-63ba5e1759e7 | -14.41709 | -51.78305 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12c1d77e-c652-3d73-b395-771920b5fc6c | -12.11051 | -50.62817 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab12997a-c26b-33b0-b4bb-7f28143ef288 | -11.11557 | -49.88961 | 2026-08-24 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f209e9a-19a6-3e5a-9b5a-d2169b8e5a9a | -9.49888 | -60.50087 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99ec31f2-2fb7-3825-bbe4-9a73716b8167 | -9.46131 | -56.92038 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b612ee83-0306-3c62-9264-55efd5346aa9 | -13.14873 | -51.38712 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e47b1919-4f04-3057-a226-181c4725ac00 | -18.69886 | -47.47378 | 2026-08-24 04:46:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5b58d9cb-3a8e-3f0b-a47f-ef4070d7f29c | -12.11714 | -50.60756 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 513d9bb2-226c-3dd1-a364-3d45c250a2be | -10.81084 | -50.94309 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7168f41b-d84a-3685-b61a-702c43c42941 | -12.09725 | -50.62603 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1a29e77-a1a0-39e9-8e12-0850dff6c498 | -19.48392 | -44.33949 | 2026-08-24 04:46:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17606f9a-27c1-33d9-b30f-5415a238250b | -12.48055 | -54.18281 | 2026-08-24 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 188890a3-9c40-38eb-897c-2504c2302dd3 | -11.6811 | -54.5524 | 2026-08-24 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81e1b2ae-93c0-3ecc-a568-ccc88e2589f0 | -13.17123 | -51.39433 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 09f72a4d-b541-3a75-bd0a-69e27c0778a2 | -12.7565 | -48.37412 | 2026-08-24 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72e55792-0912-3fa7-ae48-d50a278c909d | -8.37625 | -46.46756 | 2026-08-24 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3787696-eae3-3c84-901b-00db21580adb | -18.56148 | -44.42265 | 2026-08-24 04:46:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7aa26a5-a216-3b6f-891a-4c528844f665 | -12.10609 | -50.5914 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9221150d-f3b5-3ad5-926a-294f1307433a | -6.80125 | -59.59535 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e593d56-d071-37c7-be40-fca1b07bc4e4 | -9.97446 | -57.8848 | 2026-08-24 04:46:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94543344-b229-392f-b3fe-b3fcd437c0f5 | -11.54939 | -46.9618 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9fe1a3d6-b342-3ba8-98a1-03a21a0688ca | -12.82038 | -48.47864 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19b88903-3165-3db9-bba3-d294c8240f4a | -6.5547 | -58.58899 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99c6b3fe-7cd6-37cc-a778-938bd7a64b47 | -8.54856 | -54.84859 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc20d33e-c4f6-3d30-ac2e-6abf10c3b0cc | -14.31536 | -51.84645 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bcf8e2e8-4e88-319e-9f85-865f3c1323ef | -9.68258 | -47.8924 | 2026-08-24 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ead2e24-a732-3189-b54b-ed30b2f28cd0 | -10.6994 | -47.75597 | 2026-08-24 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f4681f1-716d-338a-88d7-544c8ae57aa5 | -13.27268 | -51.44038 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36ec2819-59eb-3432-b10d-a01de95c8b89 | -10.04179 | -46.43439 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 777fd639-4a8e-3848-8e13-d78ca7f2642a | -6.89487 | -55.70055 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6c33fa3-b42a-31c2-9611-b8f0abc9575e | -19.0103 | -42.13125 | 2026-08-24 04:46:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a4e090a8-978f-3f6c-9e89-0823b5c75cf4 | -7.77064 | -48.24825 | 2026-08-24 04:46:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc253ac9-4de2-34c9-b84a-eae7f3e6d75b | -13.88447 | -54.01754 | 2026-08-24 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e2a0f75-9085-3d4b-8075-6d76ecdfb130 | -12.11216 | -50.596 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83cecb7b-7e1e-38b2-a31f-341e178b7519 | -10.82464 | -50.94175 | 2026-08-24 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d76a8b80-2327-3621-b247-e29834f1b79c | -15.12269 | -42.92049 | 2026-08-24 04:46:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 216d4260-b709-322e-9918-b8fcb9a1f5c6 | -12.08395 | -50.58096 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 60d8a3be-8723-3787-887b-a2abcb666e97 | -9.44955 | -51.58782 | 2026-08-24 04:46:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b89c52e8-6ef7-3e95-867b-b855a3565918 | -8.10249 | -47.48433 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52447416-0973-3c0c-a01d-477e9c76df46 | -10.06655 | -46.37067 | 2026-08-24 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2eb201b-1e2e-3f57-b827-3e330f40651d | -9.50796 | -60.49856 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fd3eea6-5346-317e-a27f-5d9d71ce00ff | -8.61922 | -54.73948 | 2026-08-24 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8fb1c1e8-e1d5-34ac-99d9-6438cd73009d | -14.31318 | -51.83879 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3d5d58b-892d-3b88-8275-dcc703247eda | -12.10388 | -50.60542 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b1967cfc-bcb8-300c-9ced-c418a96026d4 | -18.69662 | -47.47487 | 2026-08-24 04:46:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1d1a16b-4632-382e-a1f4-e982d48d7d79 | -12.08339 | -50.58448 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a16e60bf-c8aa-3f55-a681-8570847303d4 | -8.92379 | -48.53593 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdc6baf3-7b9e-310e-8d57-b61ddb27ba9a | -9.051 | -50.77214 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4c66fc13-0b7c-3390-8119-e327caab4aa6 | -14.58198 | -53.03212 | 2026-08-24 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 765fb8e1-9a22-337b-9c35-42afc185b0cb | -11.91303 | -55.90174 | 2026-08-24 04:46:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c213c4c-9b7e-3617-9687-8b6cc67b0fa3 | -11.59795 | -56.28734 | 2026-08-24 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 560b0647-4c04-31be-aa9c-a56cfeb43055 | -11.8644 | -51.68385 | 2026-08-24 04:46:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76ce938c-2536-37f3-ae4d-c1398488e430 | -8.34089 | -49.28984 | 2026-08-24 04:46:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acfb9558-89c7-3cc4-a795-f0a76530e206 | -9.06126 | -60.43916 | 2026-08-24 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86c9c138-1cda-32a9-b45d-6ed22ad0a061 | -12.88999 | -48.47357 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0251cbb-a103-3ce0-84df-f90a4e2e8e07 | -12.09284 | -50.61085 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a6c090e-4f02-3278-99fa-f79c1e2fb2b1 | -10.73038 | -47.98443 | 2026-08-24 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6fa3e65-810a-38c5-8b97-0d07e8bbd0a1 | -11.19889 | -55.07369 | 2026-08-24 04:46:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e582cb2-d1b9-3635-a1af-2de22bbf8a56 | -11.37914 | -54.07954 | 2026-08-24 04:46:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5120855-43f0-3d23-8af8-17b4145c2cce | -12.89182 | -48.48553 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 336d266f-f8c9-3fe5-bdb0-9e63008fe81f | -6.54917 | -58.52905 | 2026-08-24 04:46:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fe93fc3-b076-3741-acee-3175944fce35 | -12.7423 | -46.46471 | 2026-08-24 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 30804f91-ae32-3247-baa6-53258b40d2d9 | -8.10976 | -47.48853 | 2026-08-24 04:46:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d95ca2ce-8fe8-38af-aa5e-74d134ae5dbf | -9.49814 | -60.50468 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0036de50-a49c-3c0e-9a7f-26e69c889713 | -12.08842 | -50.59568 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9d138d0b-df60-3aa9-a64a-4f30dc0cc312 | -14.32294 | -51.75645 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| d3d6b8e6-0bf4-3ad4-9ee6-593daccb51b6 | -6.74453 | -59.65411 | 2026-08-24 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4d1f7fd-0d3d-31b8-8fa5-e3618286422c | -12.10609 | -50.613 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3626e42d-8f5d-3f20-9b73-24d964dda484 | -12.11493 | -50.62166 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 49897501-0c5f-34dc-823e-828da125c9c8 | -10.53171 | -50.77504 | 2026-08-24 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 275a2e9b-7eb1-3b3c-8ef5-24ee091edf39 | -8.54265 | -55.28332 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e73120a-e03d-3ccd-bb11-61ae18d7a8da | -11.54875 | -46.96628 | 2026-08-24 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a4698eb-d04d-338a-8388-da89279c1df8 | -19.93389 | -45.06978 | 2026-08-24 04:46:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a39121fd-84ac-30b5-b204-c4547416124e | -6.89559 | -55.69641 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35042803-ef38-3894-aa48-d90c36cbaf34 | -12.8935 | -48.47416 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 170c44d1-f9be-3e78-8482-2789128bf3a3 | -13.88731 | -54.02215 | 2026-08-24 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cdfce702-047a-31f1-ba10-2971372281e8 | -18.31758 | -47.20063 | 2026-08-24 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c1ca8ca0-b59a-3772-82dc-f5e7905e4236 | -12.41283 | -42.90431 | 2026-08-24 04:46:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 18388f5c-49b6-38a9-bd4a-e87709103234 | -11.90781 | -55.90801 | 2026-08-24 04:46:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c3e6bfb-f679-3e35-80e4-c17259b90ea1 | -12.86539 | -48.46953 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55d84c21-3ab4-3f7c-8981-07f47e55c39b | -12.12433 | -50.60511 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32aa7b42-27bc-3e92-9f65-6b10f6d9d87a | -12.11659 | -50.61109 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e607a077-6bf8-39f5-97bd-ba6024a1abf1 | -12.11107 | -50.60296 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a83e6be2-2917-3673-b6ba-8fddab98cbd3 | -9.47099 | -56.91742 | 2026-08-24 04:46:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f04c6fa3-3d1e-392b-91f8-9ec1f581da5f | -6.61235 | -58.38236 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b501b816-913f-39a8-923e-fe0dddd08f3a | -8.10589 | -51.66869 | 2026-08-24 04:46:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4adf78c0-8825-3789-b8e3-a4b33e7e226d | -12.12101 | -50.60458 | 2026-08-24 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ad73c3d-c810-3775-8d3a-8e1f2e923c5f | -13.68845 | -51.83673 | 2026-08-24 04:46:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27d94b54-904b-350f-a572-12d906cdef41 | -7.78269 | -56.28441 | 2026-08-24 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ab28435-c445-3f4b-890b-c9f26212793e | -9.39724 | -60.58976 | 2026-08-24 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d8542c0-aa6f-3f9f-9b49-29a0db24c17d | -8.5467 | -55.284 | 2026-08-24 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57cfacdf-9cfa-31c9-aa55-8133e932ee0b | -6.61126 | -58.38862 | 2026-08-24 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46a71bec-12fc-3b86-911c-23b116221a65 | -8.92604 | -45.73653 | 2026-08-24 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84afd17b-87b7-33c3-abf6-5f4080d39d09 | -8.98864 | -50.75813 | 2026-08-24 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6734ad67-1c68-36b0-bb5d-ac4680940eed | -9.96372 | -48.32851 | 2026-08-24 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e87cab5-db3c-33e1-b1c5-27a5c0f775fa | -13.27655 | -51.43739 | 2026-08-24 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 295eb35d-76e5-3544-812c-ddf940699ac4 | -8.92746 | -48.54023 | 2026-08-24 04:46:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0bcbbda-d483-3741-8765-c00d5ed13d88 | -14.31849 | -51.763 | 2026-08-24 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0be53b9-e752-3527-8a4c-45fce44cc6b8 | -10.55204 | -46.31877 | 2026-08-24 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f8adf3-e847-38d3-9f92-ec58fb7658d7 | -12.89237 | -48.48181 | 2026-08-24 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README31.md)
