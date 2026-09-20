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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e32a83e-a5cf-3acd-8f29-b8ed1cd7b98d | -3.69422 | -60.564 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03be1b03-3f03-30fd-9963-5ce4e7735be0 | -5.75962 | -57.44776 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 179d0f50-5d8c-38c4-8d13-1d5e77667ea8 | -4.38578 | -55.25547 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bdb4089-abfe-388d-87b3-cc536990d320 | -9.93969 | -60.73176 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d7fd58d-18af-3560-ad31-88c403a72838 | -10.90895 | -53.98344 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff2b28f3-cb6a-346e-a39c-09303d1d8b9b | -11.22004 | -54.06776 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6cf4a693-bc11-3f31-be3f-62d80a1198f4 | -11.21931 | -54.07322 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 153ac26e-283b-3ffe-9909-6624450347cb | -3.39204 | -61.29591 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6156f04e-9a13-3af0-9e22-6eaa5a6c27bf | -10.90883 | -53.97842 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 44cb6c83-b31e-3374-a030-100647cc66e8 | -9.94024 | -60.72823 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 428a2257-e2b7-3734-989b-e8bbbba43949 | -3.23591 | -61.20944 | 2026-09-20 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39d0e582-a1be-32b0-9f2a-9f1bde42c8b2 | -9.93413 | -60.72366 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b77eb2a-0c9c-348b-83ae-f000d682a6b1 | -11.41749 | -51.4651 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05431525-253f-3755-962a-6a5b5bf1f248 | -10.87142 | -57.14821 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eec63cde-d682-3b5e-b545-0f1d456cb0bd | -11.21307 | -54.08327 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8a8ba0ec-c2d4-3b6b-a441-3d4367faabbf | -4.51901 | -55.47467 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f83f6f7d-1ddb-3087-b959-6e711fa28985 | -11.19819 | -55.03114 | 2026-09-20 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03faaedb-6112-3e94-b15d-735536335f5c | -3.38478 | -61.29842 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 156f08b3-6891-3400-9520-ed0ef7f088ee | -11.37829 | -51.40118 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2917cc0d-a3a3-3f1a-b9d9-55067fe1d4f1 | -11.03708 | -54.15895 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 34f74fe0-7682-3c44-9eec-333018c54e39 | -5.85639 | -53.50347 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 18d7abee-e7ad-3930-a6bf-e1c93609a65d | -3.69212 | -60.599 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 39e011d9-8e9a-3746-9c16-05234debba20 | -5.75748 | -57.58223 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e358dd60-c5ab-3218-a584-3a0d4580b08b | -5.89237 | -53.64648 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9a4cc2bc-1e31-302b-bb6c-2f8b14b3a8a3 | -10.95604 | -57.203 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecc5c798-2ca6-3b14-9d65-8ca2c585a12a | -7.15959 | -47.42964 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5d3ef474-c799-3227-93d9-afe4be2f6d56 | -11.23285 | -54.07606 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fa12b683-61fa-3ef9-a300-194f1b95971a | -4.70232 | -55.69774 | 2026-09-20 05:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cd24d84-ebe6-3cbe-b473-ac6bd2a73e11 | -11.20442 | -55.03318 | 2026-09-20 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f0b8efc-a9bd-3615-a2b8-c6b229ec74a0 | -11.05419 | -54.17712 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 41557c43-b4b2-3967-a4c1-025c0029699e | -16.74 | -49.36048 | 2026-09-20 05:25:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b7624b9-990f-3ed9-a4a8-5990bf187a05 | -11.23216 | -54.08148 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8765963d-7365-33c4-b06b-34fbcd2f2153 | -3.60459 | -59.01815 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a0a9c37-8f1f-338d-9554-55788f00c718 | -11.42276 | -51.46987 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| baabc882-3a70-344d-889e-ab98115e6c1a | -5.9774 | -55.35752 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad7c20d6-d352-3fd0-9392-656ab08beb4f | -10.93158 | -53.95418 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d95cd199-277f-3991-8480-472b1eeeae29 | -4.6167 | -55.75861 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f57ce97e-f415-376d-92ad-3d4822384dca | -6.09726 | -55.56249 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ce8d96b-ab72-3c23-948f-28e1e8415ad4 | -5.2273 | -47.57969 | 2026-09-20 05:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d73c54de-6884-3d31-a7c9-d608f2387554 | -10.92469 | -53.9697 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 928ea7c5-607c-3ece-9466-791c1ad77c9e | -9.71025 | -65.09014 | 2026-09-20 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6f42d77-d4b8-38b9-8887-0fe11c05da9e | -4.54921 | -54.9341 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5b80335-3b22-35b7-8515-133c7e4e83fb | -3.69591 | -60.57485 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fee3f4b-71ae-38ef-8a4b-49791fa88505 | -6.75904 | -47.92029 | 2026-09-20 05:25:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c93e91df-6b5f-3596-8153-173e15d60e87 | -6.10486 | -57.62506 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1b3f4342-4bfe-3b0e-8e38-d4ed28df4a80 | -3.69314 | -60.5709 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 776618c2-7607-3a62-ba00-d74ef2134780 | -11.11758 | -54.02988 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6febf6f4-c959-3153-8100-b800094ddf06 | -5.84629 | -53.54151 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a62ec3f7-388c-37bb-bef8-993b30da3325 | -6.19653 | -55.45161 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93267b50-2e05-3f61-81d4-a54bcab0c80b | -11.75109 | -54.563 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc32cd96-d705-36d9-805b-9116515f8b96 | -5.85365 | -53.52285 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| edd90037-f8df-3a64-8911-2543a29513a2 | -9.93746 | -60.72419 | 2026-09-20 05:25:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dad62986-1395-3a33-90a2-15e2c2f37464 | -11.94522 | -55.92906 | 2026-09-20 05:25:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 763af7e4-d352-3ca7-bb6c-3eea115cfd91 | -7.16612 | -47.44544 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bf7a88e7-8c63-398a-89ae-132e5de3176e | -13.88653 | -48.58695 | 2026-09-20 05:25:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a4d0cd71-8171-349b-960b-fa7ee8f857a2 | -10.87556 | -54.0873 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e4df0ba4-8f6a-3439-b73b-4e65f1a018a9 | -3.69055 | -60.63057 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1893799-5679-30f0-a4ad-a573528dc9c3 | -5.79012 | -47.36676 | 2026-09-20 05:25:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff2e6522-c07a-352d-9e4a-ccaacf005d14 | -5.86821 | -51.57135 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d0d16e-88db-39da-b181-a424e44466b4 | -10.91433 | -53.9738 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf87c829-c179-37b5-a298-fab03310d324 | -11.1166 | -54.03163 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0c38e4af-6041-3593-acc1-7f15e4aa49a2 | -5.74365 | -57.60099 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00ac7b0f-5698-3efa-a073-713470ebf7a1 | -5.80593 | -57.7378 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 945a4d67-e9b0-39fe-a5de-a4efd46857a8 | -5.76323 | -57.44823 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b360fbc-e615-3c6d-8044-7f209481fef2 | -3.6932 | -60.5921 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6e52d4c0-4c3a-393e-ad55-bc60ece66c85 | -7.1626 | -47.47242 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e63304f2-d378-3f75-aa7d-e3c870bf17c1 | -6.33939 | -55.29547 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67cd2542-67da-3a0e-b1e7-893637d973ab | -3.88467 | -58.94584 | 2026-09-20 05:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f9bbb47-c628-3db0-a514-62704e46245f | -7.17306 | -47.44679 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5fc751f1-1bfc-3085-b766-42ceba24ee19 | -6.1558 | -57.70003 | 2026-09-20 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f4b73dc-02e7-33dc-b008-2830220e24a8 | -7.52291 | -47.33603 | 2026-09-20 05:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 837d3bbb-2b0d-3f0f-993a-3e08d4d8329b | -4.48957 | -55.48146 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 00bc5fee-ae09-3b93-8198-555f6f56888d | -10.87966 | -54.0932 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49f94862-9401-3096-8738-11f08f165593 | -11.03297 | -54.15308 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76246029-f4a4-3cae-93c8-3e26a9499b9c | -11.21838 | -54.07398 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7049df2c-d89b-3704-a986-5e7bfd45d402 | -4.49674 | -55.48782 | 2026-09-20 05:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56a1abd4-70f6-3bc5-97de-ad9c7b5b80eb | -14.05095 | -52.0912 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d9aa74a8-34bf-3d5d-a13d-d63f2ceeb7ad | -11.19757 | -55.03569 | 2026-09-20 05:25:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b3a7235-c11a-37e9-86ba-d8859c874281 | -11.22896 | -54.07455 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f554f433-73df-3015-8a84-78d530024c56 | -3.38143 | -61.2979 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 254b048c-130e-399f-85e5-f5687703800c | -11.09757 | -54.03244 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 2fea2717-fd2d-3f09-8bbe-a6b996dd67ca | -11.03162 | -57.23666 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eda29abf-68c4-3dad-9168-7e4a1802c103 | -5.8468 | -53.5712 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2510da02-4998-30da-81ff-27415d2a5b53 | -4.56033 | -56.15417 | 2026-09-20 05:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e8204cd-2e0b-3d46-b12e-88f2e085ef23 | -11.0323 | -54.15831 | 2026-09-20 05:25:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 97127b5e-b9c1-3ade-9474-14eebe88543c | -11.73764 | -54.55597 | 2026-09-20 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a5bcdd-be73-3180-a1f1-c98af6f46955 | -14.05142 | -52.08695 | 2026-09-20 05:25:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4861861-64cd-3a63-89f9-3baa5999c28a | -10.95995 | -57.20344 | 2026-09-20 05:25:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4f17b18-8c07-3236-b453-65558ab92d18 | -3.68556 | -60.61919 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89ccd8e4-5775-3028-ac36-5f9453ddc8ca | -12.47362 | -50.05038 | 2026-09-20 05:25:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d16aa4f7-186a-3f5b-b5ff-fc23f0f24cf8 | -5.72804 | -53.45686 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a410a8f-9df0-3654-9c26-dd384dd4b3ad | -5.79537 | -51.8639 | 2026-09-20 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 48b4afd3-f2c2-335a-a6bd-fdeb787d278c | -3.40823 | -61.30206 | 2026-09-20 05:25:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 646b5db7-5a22-3afc-94b7-b0a94fe764a6 | -10.66824 | -58.83816 | 2026-09-20 05:25:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a4a5234-6a45-3b11-a4c7-81fdf6fb4619 | -3.39697 | -61.06926 | 2026-09-20 05:25:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a331bca1-2a5f-3afe-b52c-45c972e67fa6 | -3.73019 | -60.61549 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38d53410-88fb-33f4-acf4-1d9ae10e245b | -3.69164 | -60.62366 | 2026-09-20 05:25:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 348ef3df-a9ad-3c63-bb44-169f7c8116c2 | -14.04847 | -54.02455 | 2026-09-20 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d450fd9-9cfd-3273-ade1-645e037df6f9 | -3.60755 | -59.06536 | 2026-09-20 05:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a66c3c71-c02e-3bb5-a482-62b27c098037 | -5.8456 | -53.54635 | 2026-09-20 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README97.md)
