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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e86c0db-dd87-39a3-9870-808c8050f10c | -8.5932 | -54.752899 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dde1fe22-ea43-37a9-9358-2f22423df9f4 | -8.5837 | -54.713402 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49b3626d-cb60-36cd-970b-0f24757f1144 | -19.7409 | -57.9533 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3cc5aa03-b772-3a5a-a4ed-723899224d27 | -3.0967 | -61.202202 | 2026-08-19 01:23:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82e36f42-c67f-36de-85ca-cfe042c6b76e | -8.5662 | -54.769798 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3c66d7f-3125-3784-9c90-b23812102a80 | -9.171 | -59.673698 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26545b7a-1e80-32bb-9e51-4d5b3804040d | -21.5291 | -52.007702 | 2026-08-19 01:23:00 | METOP-C | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ce3d565-7c70-36aa-b517-00e7e81b0099 | -6.7556 | -59.1619 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b8ed1bc7-5cc9-32a1-8cf3-847bfc5c60c1 | -8.5564 | -54.772202 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a65c0f51-506a-3626-b13a-4c8b3ac669b6 | -6.1393 | -57.875 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa9559bc-bbb0-3d1c-91a1-7b25f07a53ec | -6.0206 | -57.808201 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 073728a3-fa79-3980-9bb4-e8bf1a8c8e70 | -9.4151 | -60.579399 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 542890b7-d5eb-3762-8cc6-ee7bd4689e4d | -6.7623 | -59.146 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec7f1398-49fe-3ae4-9e4c-f6aff2cb6174 | -7.5695 | -55.568298 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08f82a8b-f53b-3e95-b7c3-f542338fbc0b | -6.8972 | -56.435799 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0fbb24-ddac-36a4-99c1-a529362acaf4 | 0.2457 | -60.519001 | 2026-08-19 01:23:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ebf53c3e-eed8-3efa-b4c3-8ce086074583 | -8.5446 | -54.722801 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56b170d6-1e96-3ffe-8ab8-0d925cb99338 | -6.0079 | -57.8424 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 387d566d-32f6-34c8-9294-419815fe1f0b | -8.5786 | -54.7355 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90e15c2b-d46c-3550-8930-cbd705474eb1 | -6.75 | -59.0471 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| da91f9bd-0d7f-3f9e-bdf9-1511d4769b77 | -19.7719 | -57.953899 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f04213b2-0ccc-33e6-8470-65ec3fdd2c65 | -7.0459 | -59.846901 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55b5184c-803f-3730-9bde-2b9d41f54ec4 | -6.0033 | -57.867001 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eb031cc-a537-3dab-b2de-5c03ce378910 | -11.2238 | -55.0816 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a567287c-f6a0-361f-8faf-e1b4c2f7e47b | -8.5372 | -54.735001 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43c64aac-0e1e-3a14-89aa-c8c32fa5e5a8 | -15.5971 | -49.842201 | 2026-08-19 01:23:00 | METOP-C | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4b7045a5-db0b-3465-b8e2-9cb6f941cbe2 | -19.067101 | -57.3568 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 757a7e07-e186-38ae-89f0-3b75c187bc4b | -6.341 | -54.915501 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c799a81b-e84b-3c91-a210-ebae7fd2f439 | -8.5762 | -54.725601 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd50adf2-61fd-38c7-abd8-c42e613df1ef | -6.3128 | -55.882599 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 102caee0-3bbe-3656-ae72-4466704eb83d | -11.2217 | -55.0728 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80766b63-73e0-3735-b465-ea1e36cebade | -6.7081 | -58.954498 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a2edda1-a301-33cc-9638-3a318a0b76da | -10.936 | -57.1063 | 2026-08-19 01:23:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cf234a5d-691e-3fed-95bf-99780d57a95c | -3.2234 | -61.2607 | 2026-08-19 01:23:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2aef63fe-da2e-3eea-ae19-e986b0bc804c | -6.7737 | -59.1506 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d117998e-6d9e-347a-8d42-9154ae88ed4e | -6.7017 | -58.926701 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f6131bd-044f-380e-8d57-e88bb379becb | -8.5813 | -54.7034 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 755dca94-4a6e-3cba-9625-d0e0b7812a8a | -5.4933 | -60.136902 | 2026-08-19 01:23:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bca109f3-c9e1-312a-b18e-f8934ad8480d | -8.5667 | -54.685799 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91cab7f7-4561-376a-941c-6d5c16480c78 | -9.4224 | -60.427502 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd762de9-5430-3e56-9f15-c170672bef0b | -11.2413 | -55.068001 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51ddaffe-49e3-36e2-a4a8-d9efd53324d0 | -19.7362 | -57.931 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7189955e-1a49-3eec-a7ab-c6cf4f4dcef2 | -6.7891 | -59.4436 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 379758c5-eb53-3ebb-b952-7dada974d0ed | -11.2357 | -55.088001 | 2026-08-19 01:23:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84bdca62-05f1-399a-90cc-c19c396978d4 | -6.7638 | -59.152802 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf03882a-8e7f-37d8-a489-e3bae4ccda3a | -6.1445 | -57.897202 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cc08c73-2ba5-301d-bd9b-25ae6e76a329 | -9.419 | -60.458199 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ad86abdd-8363-39c4-9d69-59b617adc92e | -29.139799 | -50.395302 | 2026-08-19 01:23:00 | METOP-C | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0cbf72f4-9923-3c50-917c-508a82ccd9b6 | -3.151 | -60.265701 | 2026-08-19 01:23:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 34d9b7a7-12cb-38ca-b30a-bd0963573c2c | -29.1471 | -50.382599 | 2026-08-19 01:23:00 | METOP-C | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c283b940-3928-338f-b76f-a962d9604698 | -6.7385 | -59.0424 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75df047f-bb33-30b4-8229-dfb88f9d96a7 | -9.4192 | -60.4132 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38941177-c96a-3c49-939e-815c4d5dff32 | -8.5691 | -54.695801 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1022c066-0f6b-30d2-adcb-0f42068e1020 | -4.1242 | -60.779598 | 2026-08-19 01:23:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64599e45-aa09-32a5-8dd2-66975b95aa9e | -12.0071 | -53.4482 | 2026-08-19 01:23:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 264845ff-19e4-381f-9e46-d2692614666b | -6.6951 | -58.942799 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53469f74-fd04-3913-b3cd-5cd1ba83a13d | -7.0444 | -59.840099 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f19b043e-ca03-3fae-873c-7bad1675b1b6 | -7.0558 | -59.8447 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38e87009-fb25-347f-8d65-d320e9a50da6 | -7.4347 | -59.788601 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2af68696-d277-3f23-8431-42d80cc85f1b | -15.7749 | -55.573299 | 2026-08-19 01:23:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e04dd780-a887-3efc-9d10-27c0b4222ef1 | -9.0089 | -60.511902 | 2026-08-19 01:23:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0f6ff21-2ca7-3315-928f-4367b16c3256 | -6.8594 | -59.029499 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbc1ec3d-f765-3d90-928c-1d899c86a123 | -6.6117 | -58.4006 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb8a685-e999-35c4-b2dc-071e5b1dbcaa | -6.7033 | -58.933701 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8bbd23c8-a619-3544-9534-346891648162 | -21.448 | -48.5037 | 2026-08-19 01:23:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bfd8c756-c234-3eaa-b5b3-375b75ee8b64 | -6.8874 | -56.438099 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2275e7e4-1d6f-38e8-bb9c-27dc41447bf5 | -6.1427 | -57.889801 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 605c35f5-4a35-33a5-9b67-e9535641ddaf | -8.5783 | -54.777401 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a21cd4a2-18e7-3cb8-8b38-8832144514cc | -6.1207 | -57.706402 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52ff03f6-3bc0-3898-a4d2-71df5aee95a5 | -7.5598 | -55.570599 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7aee9118-84da-3b74-9272-c887bcc7e592 | -19.7523 | -57.9585 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 44c688dc-d465-3a29-b03c-64b51c346882 | -6.3459 | -54.892502 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e879062-45be-3104-bbe9-48a843fef679 | -9.3907 | -60.562199 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eccc959e-b6de-3262-b1b9-a61b1d690dde | -9.3923 | -60.569401 | 2026-08-19 01:23:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef1160d-7ac8-3b62-bec6-f2ff2f22e789 | -7.4362 | -59.795399 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d08e3938-ac1d-3bb8-8fd4-60388951c56b | -6.0304 | -57.805901 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8058268f-8db6-37f3-ad5e-3cc23dc4883c | -5.9999 | -57.8521 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb4b016b-d7c2-362b-aedf-0df91c6f4b89 | -8.5544 | -54.720402 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eacaf67-a14f-3287-a312-e04670588a2e | -8.586 | -54.723301 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a660a764-9fb7-3e23-ad5a-dd95d09f1bc9 | -8.5491 | -54.784401 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1724ea4e-f492-38e5-b184-15008a304683 | -6.3606 | -54.9109 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9eff984a-e29d-3b1f-9cd4-fd73368e8abc | -6.0062 | -57.834999 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d941a362-02be-3483-8bf1-36271555e38b | -8.5469 | -54.7327 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e34b0da-3b9f-378a-b10a-e884686383f9 | -6.7572 | -59.1688 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14dca625-cdaa-3ecb-8766-6dc186c3b0dd | -6.0114 | -57.8573 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 137dc7ff-0208-3f60-b396-bd16cdc1ed74 | -19.7621 | -57.9562 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 066c3844-11d4-3587-9763-00f8aed641a0 | -6.802 | -59.455101 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e545634a-3ff2-31fa-b914-7ba60a287438 | -5.4373 | -48.4408 | 2026-08-19 01:23:00 | METOP-C | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fab94e6-512a-356a-9392-3eb760bedc9e | -6.1242 | -57.721401 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 526b144e-582c-3531-8e06-51b50784a670 | -6.4523 | -52.728199 | 2026-08-19 01:23:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 319884bf-31dd-32ef-9d76-4e93b787acf2 | -8.5862 | -54.681099 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e90eb143-f29e-3708-8aa6-4b16c2d03fe3 | -7.818 | -56.576599 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40c9ebc7-896a-3a52-85c1-3b8214b434bb | -14.0444 | -53.697701 | 2026-08-19 01:23:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a88f3469-51c0-3643-af45-171bbfb4e9bf | -6.8815 | -56.412899 | 2026-08-19 01:23:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c612a65-9d5f-3ced-9fa8-a6d69fe0efe4 | -7.5576 | -55.561401 | 2026-08-19 01:23:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 923ea8fa-8bcf-3de3-87fd-ae8cc83613b3 | -6.1305 | -57.704102 | 2026-08-19 01:23:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 021681c5-5b04-3db8-9cde-ce21eae1d012 | -6.8102 | -59.445999 | 2026-08-19 01:23:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 108bb7f4-05f8-33a6-9bcc-e65563d817d2 | -8.5517 | -54.752499 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca01be29-3786-33d5-a5d9-4aec16646164 | -19.775101 | -57.9688 | 2026-08-19 01:23:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2176bf42-ef87-342a-b71c-7aff3c3e97e0 | -6.4119 | -54.953201 | 2026-08-19 01:23:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
