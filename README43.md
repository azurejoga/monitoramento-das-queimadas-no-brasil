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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e06ae5a-80c3-386e-8cae-6dd679ab488c | -5.09511 | -56.14962 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47ababff-5949-3d4b-b26b-5b3f52074a90 | -5.17171 | -45.45502 | 2025-09-05 04:55:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba20ffa6-acda-3d46-a9c2-86053d63bfb0 | -5.98647 | -44.73941 | 2025-09-05 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 24866a42-8cc7-3837-8129-fff45f90d1de | -5.19938 | -43.69604 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12d42e4c-18a3-3c7a-9fa0-84d023583c7f | -6.59171 | -44.55673 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 60555ef2-73cf-3e33-8caf-2f4420c220db | -6.17255 | -47.28596 | 2025-09-05 04:55:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5ecf095-a413-3188-b2fd-59922e95f1c3 | -5.2057 | -43.69285 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13556560-edeb-3c02-9cdc-369dc74028f7 | -5.10203 | -56.15075 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fccb39ac-b201-3872-a868-809a1327a127 | -4.99722 | -56.25936 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 724717a3-e319-33e2-b23c-b4fcc4e6c760 | -5.3459 | -49.02911 | 2025-09-05 04:55:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 487816f9-e9c8-3d20-ad2e-4fac51f81711 | -2.34828 | -47.58427 | 2025-09-05 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a5b0d917-e378-3b5d-8b79-d2a9808164bd | -6.9073 | -45.18813 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8da29dc-0507-3361-9a15-e26b1f3c0ce3 | -5.86522 | -46.1087 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8084503-58e7-350f-9a83-87ec6ee2948c | -4.70742 | -55.98874 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0a9dbc4c-6267-3434-84c4-3f9bd0121110 | -6.59784 | -44.55331 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12d35fc4-811f-3481-bd80-8bd8baf7b40d | -6.28719 | -43.50128 | 2025-09-05 04:55:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 946bb8ac-dd0d-3afb-911e-2c7488bc1be3 | -6.72427 | -45.92203 | 2025-09-05 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 90bff366-88ef-3055-9477-543f89ff51aa | -2.95037 | -51.66402 | 2025-09-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9d0a6e5-cfba-3dce-b719-66cfa192633d | -6.54889 | -43.91257 | 2025-09-05 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 59416f66-f831-3e46-a972-d50a16d9190e | -4.0679 | -48.04324 | 2025-09-05 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66d72f1f-a636-38fd-89f6-2f3524ad112d | -6.20265 | -43.34759 | 2025-09-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55448157-311f-31fc-85c7-4c7aa2f2a6a0 | -5.62867 | -45.7305 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b820214-9b6c-36a8-a4c6-46b13b82f493 | -3.32686 | -54.90617 | 2025-09-05 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d794b396-9e5c-380d-82c4-fc8ac25a8d2b | -5.87062 | -46.03572 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ede527f9-3eab-3bba-b9ed-96d763f74dec | -5.20374 | -43.69906 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62ae866f-88dd-3d8f-a053-1ff0da2f61e2 | -5.8809 | -45.57979 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ab6ddae-e7c2-34af-8ed6-53a0f55298fa | -5.54162 | -43.07138 | 2025-09-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a2959dc-7f5c-3e34-982e-d3363a4a46a6 | -5.69038 | -53.75218 | 2025-09-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 679debff-dd4c-352d-ae2f-9851df1ef227 | -6.0275 | -43.70089 | 2025-09-05 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01aa7aa9-ef33-3917-98c2-4f57c18c8da6 | -6.13517 | -43.30696 | 2025-09-05 04:55:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01e6436b-7a38-342a-b736-b763164587e6 | -5.88357 | -45.57795 | 2025-09-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9851529e-3a94-3144-8705-b6596280b7ff | -4.99437 | -56.2549 | 2025-09-05 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe2ed6d-f1a2-30d1-8809-8c44ad5b10ed | -5.94316 | -43.02087 | 2025-09-05 04:55:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 11186651-3e10-3cfb-8ffa-d3541de0ffb6 | -5.21088 | -43.6979 | 2025-09-05 04:55:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60bc6a2f-40f6-35f9-acd0-c73232290614 | -6.59073 | -44.56388 | 2025-09-05 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 623986ef-1f0d-37c2-a752-9f9684124a60 | -2.34345 | -47.5875 | 2025-09-05 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f562bbad-090d-35e9-a7e7-8aadf70c7e03 | -3.67572 | -49.02077 | 2025-09-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ed6e0e4-7688-3a6a-b392-941a27100072 | -7.20973 | -44.1887 | 2025-09-05 04:55:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2ab8727-0463-3e15-bdc3-721333c61377 | -6.89178 | -45.18229 | 2025-09-05 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6886a972-d9c8-355f-9285-2de26250d393 | -3.10936 | -47.50024 | 2025-09-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56587cb7-d9d0-3bd3-a8a6-56fabb15c900 | -10.76895 | -48.28323 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0bf5c32e-6d8b-3420-82d0-43a77da53d8b | -9.64215 | -47.10133 | 2025-09-05 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4b1bea0-88a7-3172-a415-221ef993c0d4 | -7.88865 | -45.31107 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04e26024-ae3c-3950-b903-4c4b28234421 | -9.33917 | -55.20973 | 2025-09-05 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 10dcd4ac-2731-3b08-aeef-af2a26616b94 | -7.33255 | -59.64413 | 2025-09-05 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69bd103f-b1ab-3829-9a6c-9903cdfe8876 | -7.20104 | -46.20258 | 2025-09-05 04:57:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20da9bf8-ce27-31fb-8765-c4939311b59d | -12.09657 | -44.72227 | 2025-09-05 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69d44dd3-b706-3e4a-8c72-37a79dcf59d3 | -7.90021 | -44.93215 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cc3ce49-7dee-39e2-b803-469b4fce802a | -12.50421 | -44.75918 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d765b0e-ab52-3416-903f-eedc67b38b2b | -9.62767 | -55.36026 | 2025-09-05 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6eef28a0-12eb-370e-9944-fedea49b43fd | -13.00357 | -45.23038 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 188fc9df-fbfd-36e7-81a5-c084e711777e | -12.98056 | -48.05825 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 94105711-0e1d-321d-b40c-f94b4a9b8dac | -12.97381 | -48.07304 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9aefda4f-cfd8-32a4-9382-418d6407e382 | -12.51825 | -53.83383 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3072dc7-51a9-3a45-a4f3-d6a6dbd62962 | -11.64099 | -54.5378 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88dc999a-cefd-39e5-b522-8b639726fabc | -11.86233 | -51.45684 | 2025-09-05 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e843700-d02f-3b3a-a32d-53d7862eb789 | -10.88352 | -55.38774 | 2025-09-05 04:57:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4d85e63-2e92-3466-a4eb-e833ae7cb2b2 | -10.76829 | -48.28798 | 2025-09-05 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9a8bd8d-b141-3c81-b051-a590ca377a11 | -7.30298 | -44.07106 | 2025-09-05 04:57:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe255222-171f-37ff-b503-4f0d2300e975 | -8.07208 | -52.35051 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c1b96f43-361c-3b46-b4d2-9f2cff839e6f | -9.70039 | -48.99005 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34515197-dee7-3c65-aec9-b78503e8b11b | -7.69869 | -50.28965 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 184fdc91-8687-392a-9c55-01ef3451785f | -10.78867 | -56.29851 | 2025-09-05 04:57:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f18e55dd-a1b2-34c7-a5c8-48444f14fadc | -9.98566 | -51.6203 | 2025-09-05 04:57:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fec6314-72ca-31c5-9cd7-e0711dc97546 | -11.59038 | -52.18213 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6aa2ba0f-1d04-3b8e-98ab-5d7bf39a9881 | -7.75819 | -48.7871 | 2025-09-05 04:57:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e6563ce0-f89f-365b-9f5e-f206d8c69157 | -6.32169 | -58.17589 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49012a0b-8522-3c1b-b486-8b4e5a27ac81 | -11.58253 | -52.1852 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52c9b69a-7cb1-3207-8390-b411b7250098 | -11.58223 | -52.11137 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b391d2-92e3-3e87-9b5d-edc473903246 | -6.26883 | -53.44039 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28def4b6-414b-3f31-b4f4-c76c028d9759 | -13.1017 | -57.10751 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ff152ed-34b6-3888-ba6d-d8e4bdc395b5 | -9.54632 | -59.7344 | 2025-09-05 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4be70055-3760-3d3c-8a12-bf0c76170a54 | -12.99211 | -54.81707 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7ac9e1e7-e1c9-38ff-a1e8-b65b4a160708 | -10.16189 | -46.25688 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7703e56-967f-38fd-9b9c-c4154d993ef8 | -7.05239 | -50.86 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51e26c0c-9856-31d5-9ea7-f8325244e039 | -9.07642 | -47.00592 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 7b6e97d6-685f-31c6-aeba-e41ae0597eef | -8.01118 | -45.43815 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ad0f18e-7458-3f40-8570-d1ef05f16d70 | -12.98041 | -54.80417 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63e78dc9-5bb0-3be9-a274-11feaa85ac53 | -11.61655 | -47.79693 | 2025-09-05 04:57:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4074dff-cff8-3b8d-9e5b-72651aa68e68 | -8.97294 | -44.45667 | 2025-09-05 04:57:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04038aec-426d-3fd6-9a46-0dcb4bd89efc | -9.07005 | -47.01618 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33967ccd-6ebe-39ea-9cfc-b1b527adb6e9 | -12.98932 | -54.81295 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2debf43c-59ca-374d-93aa-2610576cb43c | -7.68578 | -50.29776 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59c2b6d4-7132-31be-aa9c-6e65171928a1 | -9.75823 | -46.91526 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 40f7d0a7-63b9-341e-8e27-3e4f6fd7c2e3 | -12.83747 | -44.45636 | 2025-09-05 04:57:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e078e4a5-18cc-34b4-814e-eea1de5102bc | -11.19967 | -55.01804 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7a605ce-8313-3b45-a36d-a67edac3ce48 | -7.05604 | -50.8607 | 2025-09-05 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0ae48ee9-56fd-3b22-b33b-a7c06701b086 | -9.71169 | -51.07853 | 2025-09-05 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f73d309b-9e79-3ffc-9529-799551a2311b | -12.64094 | -56.9896 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf67dbd5-8336-3419-9d88-49aaf521e2d2 | -8.19172 | -49.60024 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bbb0d993-62a1-3c27-abd9-c21186dcef75 | -10.47934 | -53.64184 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 261c6c4c-f6f5-3bdd-a268-12fd3b183f92 | -7.81931 | -46.08918 | 2025-09-05 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 044741a4-9e56-3987-9ab5-1f8af019864b | -7.66588 | -56.75012 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f8456ca-8146-376b-929f-a5ffcb5fa355 | -12.9107 | -57.00804 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3668f804-2c53-3615-9d6d-5dd7069cf8ce | -11.61854 | -52.19776 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34f92d91-4f17-3326-a952-ca9d971f9aef | -12.93711 | -48.05508 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1de3cb1-a447-3f63-8144-489fc26c737e | -12.94907 | -56.99585 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65dd0e1e-4170-3aa2-803c-07d933a65aab | -11.61274 | -52.18111 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 069e0ef9-4821-35b8-bec4-7ef602fcfda2 | -12.88263 | -56.94725 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f2ebb07-0a40-3bf6-bfef-b9650402f43b | -13.85682 | -46.25792 | 2025-09-05 04:57:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README44.md)
