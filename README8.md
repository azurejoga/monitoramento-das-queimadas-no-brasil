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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1423d3a0-bbc4-37d1-9b41-55a537a906a0 | -7.7611 | -49.198898 | 2024-10-11 00:45:46 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| b5b87274-ca7b-3ce3-98af-9d70dd239963 | -7.7628 | -49.2062 | 2024-10-11 00:45:46 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d79d930b-255a-3a64-a436-6decf2719e38 | -6.5697 | -44.169201 | 2024-10-11 00:45:46 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 468ba06d-1be1-3a39-bcab-b0b7dc3b7101 | -7.7513 | -49.201199 | 2024-10-11 00:45:46 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c1d8a4fb-ca92-3d56-95b4-ca096f2631f7 | -7.753 | -49.208401 | 2024-10-11 00:45:46 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 96e56cee-238c-3704-823a-7b2a9992fb85 | -8.896 | -54.563301 | 2024-10-11 00:45:46 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dae86792-5e3a-3d62-a26e-f1635e1973b0 | -7.0786 | -59.4087 | 2024-10-11 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| bf66835d-bef5-349a-847e-6cb70244d16a | -6.4372 | -44.259899 | 2024-10-11 00:45:48 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7750858-40bf-350b-8bca-3f835d78a271 | -7.2232 | -47.582001 | 2024-10-11 00:45:48 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28aba980-dcb8-3011-bedc-94b1f1e457ce | -6.4539 | -44.371899 | 2024-10-11 00:45:48 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af87c302-7131-31b7-be35-bdd74a03e330 | -6.4409 | -44.3606 | 2024-10-11 00:45:49 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d67aee2a-f24c-39a8-9125-160a68a608b1 | -6.4442 | -44.374199 | 2024-10-11 00:45:49 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be646370-b54b-3c05-9a10-570b418a8e2b | -7.5997 | -49.395 | 2024-10-11 00:45:49 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 920bb9fa-9276-3505-bc28-8ab7f8b5612d | -7.6013 | -49.4021 | 2024-10-11 00:45:49 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36eda1be-daa4-3398-9811-2d11d3507667 | -7.6867 | -49.822498 | 2024-10-11 00:45:49 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0f0801-d5bf-395e-ad27-71eef9f8bd35 | -7.6882 | -49.829498 | 2024-10-11 00:45:49 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072298f0-630d-3aec-bd39-abbe1a14acfc | -7.6784 | -49.831699 | 2024-10-11 00:45:49 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5dac525-10f9-3e1d-8ed5-bce51007031a | -6.389 | -44.3587 | 2024-10-11 00:45:49 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4135fb96-ec00-37b7-9b6d-fbac3a514dec | -7.5865 | -49.563202 | 2024-10-11 00:45:50 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f514b840-a7fe-386e-a65a-b048d810f084 | -7.5881 | -49.570301 | 2024-10-11 00:45:50 | METOP-B | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13195595-d32f-3ef3-8793-305b09ac1879 | -7.332 | -48.586601 | 2024-10-11 00:45:50 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa43098-0208-3b7d-9e08-a2ef471463eb | -7.0263 | -47.355999 | 2024-10-11 00:45:51 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afa1acdb-e606-3d62-a3ed-bf794ea40058 | -7.0283 | -47.364799 | 2024-10-11 00:45:51 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5e2b44dd-b024-380c-95dd-87f3cb313859 | -7.0304 | -47.373501 | 2024-10-11 00:45:51 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4fbdd68-92ad-3f4a-9898-005a1413bdff | -7.6786 | -50.241798 | 2024-10-11 00:45:51 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a07df952-c67a-31d8-8fba-381fce45b9a6 | -7.6801 | -50.248699 | 2024-10-11 00:45:51 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5c9aa5d-525f-3783-940f-1a094f8589d3 | -6.7963 | -46.462299 | 2024-10-11 00:45:51 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| beaa2568-4aee-3131-a487-48bdb8d6593b | -6.7986 | -46.472198 | 2024-10-11 00:45:51 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2a32a26-7301-37f8-9c4f-cd1f7d4a1be1 | -8.6139 | -54.585098 | 2024-10-11 00:45:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24b80218-263c-3d40-a088-351bb1208242 | -8.6159 | -54.594299 | 2024-10-11 00:45:51 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bbc3035-35f1-365d-b5a9-5ead0052420a | -6.8431 | -46.924999 | 2024-10-11 00:45:52 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1764be3e-fd32-3cc1-918b-38f00ca77f4d | -6.1976 | -44.375801 | 2024-10-11 00:45:53 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76fbc82a-357c-3b1f-ad0f-03663cf64732 | -6.1845 | -44.364399 | 2024-10-11 00:45:53 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7d4f149-b7d1-3069-8ab0-2c33807410a0 | -6.1878 | -44.378201 | 2024-10-11 00:45:53 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ffbb41b-845b-3fd5-8012-c45a28a30f2f | -8.4417 | -55.4692 | 2024-10-11 00:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 7d43491d-b444-3d79-a065-b17350fc53bf | -6.922 | -47.705399 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 905397d9-2c70-3d40-9d8c-b8c9c7eee029 | -6.9278 | -47.730598 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df8490b6-f53f-34de-b023-a523ddfb31db | -6.9298 | -47.738899 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9770ca33-f837-3357-9546-fd6c9bbb267a | -6.9141 | -47.716 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9809aba0-5869-3457-8a17-277bcd44e9d0 | -6.9161 | -47.7244 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0d2f1f4-b4f3-3b84-b48b-8785f9d8c90a | -6.918 | -47.7328 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 520595ba-b53b-345f-a435-75136f667fd5 | -6.92 | -47.741199 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f5e54213-e11f-33a9-8292-d5e614e8e1f1 | -6.9219 | -47.7495 | 2024-10-11 00:45:54 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 62e4d919-dc55-3d11-93f1-6035107f8084 | -6.9239 | -47.7579 | 2024-10-11 00:45:54 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8e83fa6-999b-30b8-8765-133666e10897 | -7.0313 | -48.534698 | 2024-10-11 00:45:55 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebd05cbd-b1fe-34bc-a5ce-fe112e12cc39 | -7.033 | -48.5424 | 2024-10-11 00:45:55 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b2d99e7-28eb-30dc-ab8f-28798549e60b | -7.0215 | -48.536999 | 2024-10-11 00:45:55 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc6925e9-2710-37f1-acf8-c9ce94dda3e3 | -7.002 | -48.5415 | 2024-10-11 00:45:55 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 049af808-1f42-32cf-a9ea-a5098d75b8ac | -7.1397 | -49.1418 | 2024-10-11 00:45:55 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f8acc10e-9cc0-3203-8881-38929b65612c | -6.0642 | -44.6353 | 2024-10-11 00:45:56 | METOP-B | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d626198c-0517-3b43-8061-e0634f47fafd | -7.1103 | -49.148499 | 2024-10-11 00:45:56 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| feb3ce01-18be-3e95-9091-fee23a3c7b57 | -7.112 | -49.1558 | 2024-10-11 00:45:56 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 71427ff6-5b8c-3577-8400-9cde8c460dbc | -8.4381 | -55.440399 | 2024-10-11 00:45:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 060abf9c-5544-3d21-b10f-2848768c687d | -8.4402 | -55.4506 | 2024-10-11 00:45:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc9df98-b428-3d23-8f5d-4747d748cd5b | -8.4424 | -55.460899 | 2024-10-11 00:45:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd8cd00-ad39-3371-9f00-c4605b77a5d3 | -8.4283 | -55.442402 | 2024-10-11 00:45:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b7c52bb-2dd1-3acd-91f8-5b33da9db8c3 | -8.4304 | -55.452702 | 2024-10-11 00:45:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57fa9beb-20c0-3182-876c-37c0f59a87a2 | -8.4326 | -55.462898 | 2024-10-11 00:45:57 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac91531f-796c-3ca5-910e-653eb5438df9 | -5.8053 | -44.112499 | 2024-10-11 00:45:58 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 897b68f0-10ea-354f-a43c-d94ba96fe01b | -5.8088 | -44.126999 | 2024-10-11 00:45:58 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ef462faf-7533-3520-a8de-c9fa99d7d51a | -8.2991 | -55.363899 | 2024-10-11 00:45:59 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a369cef-c4a8-3fb0-a7c5-2a138e60c520 | -8.2871 | -55.355999 | 2024-10-11 00:45:59 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4871766-fa9f-3367-8e71-21ccd6b48364 | -8.2893 | -55.366001 | 2024-10-11 00:45:59 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abc9e1e9-2c7b-3d0f-92d8-9ed112e4400c | -8.2914 | -55.376099 | 2024-10-11 00:45:59 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99b0a7e4-9418-3c0d-9e73-0ff6f85ff0e5 | -8.2774 | -55.358002 | 2024-10-11 00:45:59 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a890f92-14c5-3558-aa47-7ae978e0b4e3 | -8.2795 | -55.368 | 2024-10-11 00:45:59 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8372aa65-f315-3eb6-aa6f-151c3052fa18 | -9.5852 | -44.3923 | 2024-10-11 00:46:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a1934c49-c78e-3e2b-a4f9-c43881f6a9d7 | -8.2302 | -55.2328 | 2024-10-11 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d106c102-12ee-3ddc-b3a0-f0535c12ea2b | -5.7428 | -44.323399 | 2024-10-11 00:46:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9505dca-a0c3-3a9a-8436-f9dfdc17f3d4 | -5.733 | -44.325802 | 2024-10-11 00:46:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c8e7353-8ff7-36d8-916a-e0c1bfcb4634 | -5.7364 | -44.339802 | 2024-10-11 00:46:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52fe22c1-db28-38bd-9cd1-b6bce164dead | -7.1726 | -50.739498 | 2024-10-11 00:46:01 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c74a3ad-b9e6-3d67-8cd7-e7628125bee1 | -7.1757 | -50.7533 | 2024-10-11 00:46:01 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d025a4-973e-3dfa-b5df-ec041192f195 | -6.7779 | -49.092899 | 2024-10-11 00:46:01 | METOP-B | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d073c8ba-fcd3-33ee-9b07-6f6d4cd56076 | -6.7796 | -49.100201 | 2024-10-11 00:46:01 | METOP-B | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5470973-46dd-3c9a-91a1-eedf8742738a | -5.973 | -45.724201 | 2024-10-11 00:46:01 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a94724d6-f341-3bcb-be38-c6e5e930ffd0 | -5.9757 | -45.735401 | 2024-10-11 00:46:01 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6011136e-8efd-3724-8235-0f9e2607388a | -5.5678 | -44.107899 | 2024-10-11 00:46:02 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77a9b806-1a89-3768-b8a8-f2e34af71060 | -5.5581 | -44.110298 | 2024-10-11 00:46:02 | METOP-B | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0a1aec48-b8be-32dd-a813-3fd9decb4b51 | -7.1959 | -51.210499 | 2024-10-11 00:46:02 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68a6c62e-0d0d-32b1-8b79-aa8407c6ccf1 | -7.1975 | -51.2174 | 2024-10-11 00:46:02 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3172fd57-63f3-39bb-a970-22e85a04ea63 | -7.9675 | -54.723499 | 2024-10-11 00:46:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 054cec43-a426-3567-90ed-0aea63525fc4 | -7.9636 | -54.752998 | 2024-10-11 00:46:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e33e96f0-cbdf-3b87-9f0a-b5412abd157c | -7.9656 | -54.762199 | 2024-10-11 00:46:02 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ebccb55-be7c-3ce1-848f-5d54189e1397 | -7.9169 | -54.869202 | 2024-10-11 00:46:03 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02e70fcd-35da-30e2-be90-938a34565a04 | -5.9831 | -46.334499 | 2024-10-11 00:46:04 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bec8e0e-39eb-3e7b-98d6-2bd56c7f81f0 | -7.9071 | -54.8713 | 2024-10-11 00:46:04 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e82bf81-0d36-36f5-bcd6-3e12462332bb | -10.3632 | -55.8554 | 2024-10-11 00:46:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 464c26c4-86d4-307c-8ff2-a51570d24b75 | -7.8483 | -54.8839 | 2024-10-11 00:46:05 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a78c94e-1999-351f-9044-4082265018f4 | -7.8503 | -54.893299 | 2024-10-11 00:46:05 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c18cea20-0be5-3ab9-8cdc-d3fb9d7df97c | -6.1288 | -47.265301 | 2024-10-11 00:46:05 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a00b7efa-1f5f-30d2-8569-b912f0df2c87 | -6.1309 | -47.2743 | 2024-10-11 00:46:05 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59bea8ad-6b4c-32b0-b9cd-8263e7d1d813 | -6.1169 | -47.2584 | 2024-10-11 00:46:05 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7044d0c6-23c4-3f4b-9e3f-4ed0498b50b5 | -6.119 | -47.267502 | 2024-10-11 00:46:05 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 375ebf35-1383-397e-b7de-2d4af77204e3 | -6.1211 | -47.276501 | 2024-10-11 00:46:05 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 07226bb5-bdc2-3e80-bf3e-3ec82af8479b | -6.915 | -50.739601 | 2024-10-11 00:46:05 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f14fd71-af65-3dbf-aa43-642c4d057842 | -10.4713 | -49.9838 | 2024-10-11 00:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d8a36857-9007-3a63-82c4-022a6cb7c54c | -10.6171 | -47.704 | 2024-10-11 00:46:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 3d884559-0934-3e3e-b767-5ec91dae55c6 | -10.6962 | -53.0354 | 2024-10-11 00:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 47139e68-954c-38d7-b321-18636f5df82a | -10.6965 | -53.0147 | 2024-10-11 00:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 141.8 |


[Clique aqui para ver as próximas entradas](README9.md)
