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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 239a2e55-50b1-309b-aae8-e9a1215c4439 | -4.82442 | -47.32259 | 2024-11-19 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4c53bcd-da6b-3f11-929e-a6a059c09f11 | -2.48632 | -49.03314 | 2024-11-19 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f2352a2e-e7f2-35e4-b7ab-f37c031f5649 | -3.47014 | -48.25677 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26b4d160-5d58-358b-b038-3300887ebc0b | -12.64139 | -48.81377 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a227c8c0-c4d1-374b-b782-c757ae16eb13 | -5.86347 | -39.6635 | 2024-11-19 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| b297a1fa-9c15-310e-a688-37c2618154ef | -4.54173 | -48.02014 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 74f358f1-40af-3fcf-942b-9d843d3cdb7e | -6.93054 | -45.08619 | 2024-11-19 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 28c12d1f-4b20-33b3-8c49-c4fd44733ac2 | -4.5454 | -48.03285 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40edc608-5495-34ea-94ff-0f8e7188b2f4 | -3.75286 | -42.7322 | 2024-11-19 03:53:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 191dd07e-d3af-3546-8bcf-70114acd7cab | -5.54781 | -47.05245 | 2024-11-19 03:53:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84da2ac0-d184-3d4c-bcc9-644301d726ce | -3.54636 | -51.53582 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6853720f-9c5d-3577-9208-30d0fdce63e4 | -12.27901 | -43.52525 | 2024-11-19 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8887ffcf-0470-38fc-b60b-97ad7bc98ca7 | -4.30087 | -46.74717 | 2024-11-19 03:53:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d92a1e8d-42c8-30ca-a781-c126e365edd0 | -6.64442 | -41.4439 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2cdd9f1f-999d-314f-9a9d-6fc6a97a2f39 | -5.51294 | -41.06972 | 2024-11-19 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b37bcd3-eb63-3e53-a47a-aedbc7039fc2 | -4.54607 | -48.02895 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1581dea-782a-3861-b3e0-284cb75b68e3 | -10.00582 | -47.56417 | 2024-11-19 03:53:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d762a795-90c3-3b3a-9088-511c9b91b5ca | -4.22573 | -47.18658 | 2024-11-19 03:53:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6b41e3e-761f-3544-852b-86015d6bdad1 | -4.57379 | -48.01776 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ced920fb-ef17-3ed4-826f-d17fcfab6bed | -4.99297 | -44.33712 | 2024-11-19 03:53:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| faef71c6-6c77-3935-baad-862224c68ace | -4.48874 | -46.71911 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef97f97f-6541-3a78-91b8-123cdcbd2145 | -8.61388 | -35.0707 | 2024-11-19 03:53:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| aa2e2480-fad8-3d3c-a280-bc9ee893643c | -6.52725 | -40.71112 | 2024-11-19 03:53:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 33a2a89d-8122-376b-802b-0dda9bca520c | -9.97441 | -48.86838 | 2024-11-19 03:53:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ec86d84-06b6-3b60-bff5-da40af1a2643 | -7.38333 | -35.10596 | 2024-11-19 03:53:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d4f476ac-f440-3e4d-8e9f-4909b85afe24 | -10.4429 | -44.88665 | 2024-11-19 03:53:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b55957f0-a03e-3256-aef8-3cb85f080329 | -4.98933 | -44.33197 | 2024-11-19 03:53:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| bf8fae9b-6e28-34dd-b002-7da0260102eb | -3.54926 | -51.54207 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c7e8057-ee4d-3b09-bef1-a9e0f857cf5c | -10.97328 | -44.53757 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 52a1e48c-6fc0-32d3-957d-db025c605b23 | -4.97214 | -41.80403 | 2024-11-19 03:53:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cac804d3-ba69-3104-9772-639e12f27be5 | -4.48925 | -46.71608 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e7b3b67-9344-384d-af89-ecaa75754a08 | -3.23296 | -42.69458 | 2024-11-19 03:53:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0948820e-c3b8-3e37-8d0d-5c18b64134be | -4.3159 | -38.49027 | 2024-11-19 03:53:00 | NOAA-20 | CHOROZINHO | CEARÁ | Brasil | 2303956 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0f0d244-35ab-3d10-a842-6a70f228feac | -10.84478 | -44.26269 | 2024-11-19 03:53:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dabb37fc-af9d-3ae4-8325-f6fce3805bdb | -11.02154 | -41.73879 | 2024-11-19 03:53:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70b8d25c-1d21-3cba-920c-04a31140e5e9 | -10.99081 | -43.71932 | 2024-11-19 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f5b7ca25-9508-3994-b2d8-195633ed3f4f | -4.48349 | -46.71848 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a535c226-f3ed-371a-bdc7-f5f26bd26859 | -5.5321 | -39.17675 | 2024-11-19 03:53:00 | NOAA-20 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24027803-6798-37a8-ac6b-7721e3b1e2ee | -5.87811 | -39.62494 | 2024-11-19 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| df1bc1ff-e521-3f40-b11b-32fa975639a5 | -3.54761 | -51.52881 | 2024-11-19 03:53:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f8aa22c-9804-3b36-8cf8-fb3993b37d84 | -3.97982 | -49.92093 | 2024-11-19 03:53:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f9ec1ce-7d8b-36b0-bd0c-83a7e5f6af49 | -5.71686 | -41.64228 | 2024-11-19 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 90a01268-2929-386e-82cc-ff242d19785e | -10.00637 | -47.56114 | 2024-11-19 03:53:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d6bb883-25b3-3742-aeef-d65688578f6f | -6.92899 | -42.81205 | 2024-11-19 03:53:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d5971c98-9317-354a-98ba-b267ce70e0da | -6.64376 | -41.44797 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 042ae01d-307b-36ed-acac-5c564e7db103 | -5.8601 | -39.66296 | 2024-11-19 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a798f470-d373-3be2-9431-8b29f26f2d13 | -3.36713 | -45.33311 | 2024-11-19 03:53:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e2de2261-dbff-38c4-a30d-eeff78aa0281 | -4.38277 | -47.76005 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b6773de-716e-3b5a-8cb6-af33657e5922 | -2.22975 | -46.48042 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d6e62e0-5670-3873-917c-a44f5c149d0f | -2.00176 | -44.80005 | 2024-11-19 03:53:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 00d09885-8383-3266-a467-6d89c6deda46 | -4.09466 | -44.85601 | 2024-11-19 03:53:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a27dada-5b6e-37cf-8330-a78286399471 | -6.29177 | -43.84673 | 2024-11-19 03:53:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c640dea-53f4-3430-99d7-e4cbbb7c2c7b | -7.30844 | -40.03946 | 2024-11-19 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2c8c1146-ce49-3458-a8fa-5b92ad5e0740 | -3.58833 | -43.62431 | 2024-11-19 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ebba902-7a32-3ffa-8b60-9e6eb6316d1a | -1.83652 | -46.28585 | 2024-11-19 03:53:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c427099-3721-3dbb-abb6-9b5a9eaa8037 | -7.87907 | -34.83889 | 2024-11-19 03:53:00 | NOAA-20 | PAULISTA | PERNAMBUCO | Brasil | 2610707 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 533ed197-7cb2-38c7-9283-be0b494ef29a | -3.22833 | -42.69746 | 2024-11-19 03:53:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aae75fa2-84db-31ef-84f7-c8fe3f4af9ff | -4.65539 | -44.0872 | 2024-11-19 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5512f4d5-c131-3580-b6be-f5616d8bf994 | -4.55374 | -48.01827 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d268903f-c42b-3f22-a19f-d8b6352495d0 | -4.1097 | -43.58681 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 5ab604e5-f981-30d9-9870-9ccdd73709aa | -13.25168 | -43.65301 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8ee3444-6dd3-36fb-b2b3-12a411f8bffe | -6.33571 | -40.70547 | 2024-11-19 03:53:00 | NOAA-20 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f7acbcf9-a2ef-3ecd-95fd-1c1bce012e7a | -9.97506 | -48.86495 | 2024-11-19 03:53:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec5e29dd-5870-34d2-8ee2-8553934dd4b5 | -4.94743 | -47.80359 | 2024-11-19 03:53:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a18905cb-7972-3319-a7e6-c34a1ac4d4d0 | -4.48935 | -46.71796 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f29b7183-e1c4-3716-8d09-206ecf6b83c1 | -4.39073 | -47.78109 | 2024-11-19 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 709661f7-676f-320f-80d2-eb58f46260bc | -4.54307 | -48.01234 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29de88fb-1e54-3bfd-a207-97fed6f54894 | -3.50537 | -50.23292 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 305c9831-3dc3-3b6a-be8a-478b8b5d79bb | -4.55509 | -48.01034 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d5e2448d-fa36-350f-a31b-a4b894887c09 | -11.4886 | -43.22358 | 2024-11-19 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9df231dd-de13-33f8-9f6b-77b898037a2e | -6.56812 | -39.43506 | 2024-11-19 03:53:00 | NOAA-20 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d2496332-dfbf-3cff-856c-028d52fdfe05 | -3.23238 | -42.6981 | 2024-11-19 03:53:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bf3e29a-a1dd-379a-acbb-6801bc194d18 | -12.64519 | -48.82419 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03389de6-08bb-3def-bb3f-bb5d10e70a29 | -4.57596 | -45.6482 | 2024-11-19 03:53:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dc41e68-836c-36b2-821a-0e32c7bd98de | -11.48712 | -43.22043 | 2024-11-19 03:53:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5d9c76fe-f541-36a0-bc72-da5b6f65c2c5 | -6.87721 | -41.21356 | 2024-11-19 03:53:00 | NOAA-20 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3d39ccac-dd32-3bc6-a48a-00a0bdf7e41f | -3.39452 | -50.10087 | 2024-11-19 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 520e8212-84dc-32f9-b874-8a85ed817ab4 | -2.32337 | -45.64886 | 2024-11-19 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f92cdbd3-dad7-3784-b1f8-fdb06156a22a | -4.57645 | -48.02219 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0a77fc4-17ea-3603-b31c-a734420af313 | -12.44964 | -43.57527 | 2024-11-19 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b45d372f-054d-3e14-bf74-86d903b7bf8f | -7.25559 | -38.53076 | 2024-11-19 03:53:00 | NOAA-20 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1448911e-9a4c-3710-89b5-a0d4f2bda575 | -7.0058 | -45.61511 | 2024-11-19 03:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89b12f2d-c375-3ea4-8fba-c8ed1552beb6 | -10.40603 | -44.48199 | 2024-11-19 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef2b390b-7e2f-3183-862f-92a548999561 | -3.48205 | -48.25046 | 2024-11-19 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dd1a2d01-8954-3db2-9e85-5e852ba26721 | -5.3874 | -40.65906 | 2024-11-19 03:53:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2a7e2e2b-4220-364b-a2e2-67fd1b0bc74f | -7.22611 | -39.96005 | 2024-11-19 03:53:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 517fb58d-7ef3-31ea-ad34-b4c4a7e503ef | -4.35703 | -45.28584 | 2024-11-19 03:53:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2e694cbb-3098-3f3b-a259-88f44e4609c0 | -12.64598 | -48.81803 | 2024-11-19 03:53:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f05a1744-bd49-3077-81a8-4c4f4e6b259b | -11.87349 | -38.34952 | 2024-11-19 03:53:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d4e7ca60-777e-3cf5-86f0-8a4d1d3c175e | -2.31787 | -45.65093 | 2024-11-19 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a09a6eaa-3846-3b3b-9bd0-1770ed4f8cf8 | -5.95096 | -39.66603 | 2024-11-19 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3b26d211-8b84-3444-850c-2993a7163be7 | -12.27451 | -43.52913 | 2024-11-19 03:53:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fe8ab6c8-5c49-3624-917b-aee8fbf8de78 | -5.86937 | -40.17808 | 2024-11-19 03:53:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0576bca7-dbf3-3e79-a4ac-50ae4a317e56 | -4.57966 | -48.49488 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ac8aefce-ba9e-3151-8aef-693e33de3f99 | -2.32289 | -45.65177 | 2024-11-19 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8f3284d-93cb-37cc-acce-10e1a8274d16 | -4.99372 | -44.33273 | 2024-11-19 03:53:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9f3c485a-deb1-3ade-b508-d1b8b64974ef | -4.11752 | -43.59222 | 2024-11-19 03:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3aa797a4-163c-36a8-a1c5-df5ba6711d22 | -4.57577 | -48.02618 | 2024-11-19 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7376384e-8be7-3eb7-8e9f-92d78a9615b5 | -4.4841 | -46.71732 | 2024-11-19 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef5bf774-bda2-38cf-91fd-38d26ff4eb1f | -5.69028 | -46.22948 | 2024-11-19 03:53:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README18.md)
