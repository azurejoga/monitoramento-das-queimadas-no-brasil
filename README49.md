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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0d8dc41-1252-3449-93a1-2086a3ec1785 | -12.8803 | -62.531 | 2024-10-02 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7d82ec21-099d-3759-b055-2370d5ca7ba0 | -13.198 | -48.6267 | 2024-10-02 03:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 149.6 |
| e3367fca-310b-334e-8d3d-96790262fb37 | -13.1984 | -48.6046 | 2024-10-02 03:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 2bac9f04-80d6-36ce-bf55-8c408908f9ac | -13.2169 | -48.6461 | 2024-10-02 03:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 99747be4-6bce-3387-8e67-aa31365660ee | -13.2173 | -48.624 | 2024-10-02 03:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 192.5 |
| ab98a2b1-66b6-3833-8b7d-9e9ed42f543e | -13.2177 | -48.6019 | 2024-10-02 03:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 1e01e9b2-efcc-30f4-9051-1b088e82905b | -13.1118 | -51.4542 | 2024-10-02 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c2fe52cf-77db-3e95-abeb-f7c0380ad52b | -13.1122 | -51.4329 | 2024-10-02 03:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 175.1 |
| 39710e76-4c59-34af-8e7d-b25dc9d9682d | -15.3708 | -55.8431 | 2024-10-02 03:16:33 | GOES-16 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 04507511-0ad2-39d1-9f48-bbdcb67737d2 | -16.109 | -53.5215 | 2024-10-02 03:16:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 5f5e5d07-44fa-315a-aa7c-ef6f297fcd9f | -16.4746 | -57.3144 | 2024-10-02 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 121.6 |
| c430c0ab-b45a-34ff-9160-0b557684aa84 | -16.475 | -57.294 | 2024-10-02 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| c4728ece-4057-3784-8f7f-415713874134 | -16.4942 | -57.3122 | 2024-10-02 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| eab36f02-d69b-32e8-b9c5-c2f00e78561a | -16.4945 | -57.2918 | 2024-10-02 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.5 |
| d1b1380d-3208-319f-a318-e5d8c4b49560 | -16.5137 | -57.31 | 2024-10-02 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 2c7f0745-1fa1-3b21-a789-e182fc116a98 | -16.514 | -57.2896 | 2024-10-02 03:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.8 |
| 23b3634b-5fb7-394a-9258-92620b4aaa2b | -16.6124 | -57.2375 | 2024-10-02 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.3 |
| 9cea8969-e667-3ae3-a1b6-52033febf7e1 | -16.6127 | -57.217 | 2024-10-02 03:16:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.3 |
| c670bdf2-3c97-32e3-9295-dc8c34cc9725 | -16.6319 | -57.2352 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 8a696a2b-5607-368c-a370-77927c58d13b | -16.6322 | -57.2147 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.4 |
| 18aa6ba9-c045-3ab7-a1d8-f5e4f838da81 | -16.6717 | -57.1897 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| c5d6f26b-2c62-32cb-a75a-c2996c08b965 | -16.6868 | -57.4741 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| b06e83a3-714d-3691-b955-52f780c1e67d | -16.6887 | -57.3513 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 0dd745d4-6c89-35b4-b792-7f37435db603 | -16.6909 | -57.208 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 33343157-4980-3f66-a456-811214d1cca3 | -16.6912 | -57.1875 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 188.9 |
| a3ba7b2b-0cd4-3eb6-a666-b24a6b3e8a32 | -16.6916 | -57.167 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 9add66fa-be12-3171-9acc-b670b954e383 | -16.7063 | -57.4718 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| a1f45629-f50d-38ce-be44-28ad64b8b245 | -16.7108 | -57.1852 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| c752c30d-40ad-397d-98e5-2813a3409c1e | -16.7265 | -57.4287 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 125.0 |
| 94d66bf5-34aa-3403-b204-0001bd284beb | -16.7269 | -57.4083 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 3c292b47-b58a-3f87-8995-2f0ba976c139 | -16.7452 | -57.4878 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| 890cf78f-e0d9-3b0b-aab8-5972ed30b043 | -16.7461 | -57.4265 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 5d0eca9f-b2da-310e-8790-90782bbed5f6 | -16.7647 | -57.4856 | 2024-10-02 03:16:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 3534bc38-6161-31d8-9e4d-119b882cc056 | -16.7862 | -57.3606 | 2024-10-02 03:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 198e2d13-d922-3ba5-8425-8acee92996c8 | -17.0705 | -56.7114 | 2024-10-02 03:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.7 |
| 212bf23f-2600-3645-a3c0-d12f239a302b | -17.1581 | -56.1637 | 2024-10-02 03:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 71.6 |
| 55f794d1-c272-3456-9943-bd0ebdcad20b | -17.1971 | -56.1795 | 2024-10-02 03:16:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.0 |
| 0feed594-e5cb-306c-bdee-3c4458416a7e | -17.1974 | -56.1587 | 2024-10-02 03:16:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.2 |
| d62be506-25de-34cc-956e-5959bbca6abf | -17.5713 | -40.3079 | 2024-10-02 03:16:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 198.6 |
| 640501ff-a1b4-3bfa-9869-1d50f95f9b8f | -17.5721 | -40.2819 | 2024-10-02 03:16:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 126.4 |
| db1beaa9-707d-35fe-9ed5-131869a95b4d | -17.2164 | -56.1977 | 2024-10-02 03:16:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.4 |
| f3244e90-8217-335e-878d-e285c52fe10d | -17.2167 | -56.177 | 2024-10-02 03:16:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.4 |
| bd7c070d-7f9d-339c-8189-e4c948973da5 | -17.2171 | -56.1562 | 2024-10-02 03:16:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.7 |
| 9c77aa91-4997-3608-b4fd-497c835add5d | -17.2364 | -56.1745 | 2024-10-02 03:16:43 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 497d6d95-8838-3453-95dd-311caa87c655 | -20.0849 | -51.3337 | 2024-10-02 03:16:57 | GOES-16 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5e212618-9f71-3638-88f4-9a5fa315f805 | -21.3456 | -55.6841 | 2024-10-02 03:17:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 582a11cb-8b7c-36e7-ada9-9dc85644d566 | -21.3656 | -55.7022 | 2024-10-02 03:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| aa73b527-76f8-34b3-96af-2fc4dca9d0c4 | -21.3661 | -55.6807 | 2024-10-02 03:17:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 20463bb8-313a-30e4-9faa-1ac69047188e | -23.175 | -49.5943 | 2024-10-02 03:17:13 | GOES-16 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.1 |
| 87d80bc7-6f8f-3537-b117-b173ec16659f | -3.2136 | -46.7843 | 2024-10-02 03:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ad667ad4-5288-35e0-b420-bbf6bde895d4 | -8.4643 | -62.7124 | 2024-10-02 03:25:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 224beb53-77d0-3d04-a996-365b101b0e8d | -9.9554 | -64.8984 | 2024-10-02 03:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c5b436af-bfac-3502-9aba-2067fc5b7a07 | -9.9553 | -64.9172 | 2024-10-02 03:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7a8e2953-ccd5-31ad-9837-b5156185c5a5 | -9.9368 | -64.8991 | 2024-10-02 03:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 699825b9-79fe-342c-942c-c215b472d274 | -9.9367 | -64.9179 | 2024-10-02 03:26:03 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 92bcf437-6b0c-3833-b425-56bd79cacadd | -10.867 | -69.495 | 2024-10-02 03:26:08 | GOES-16 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1e0a05a1-35fa-3893-82e1-4ddc53db8bcb | -11.6931 | -64.9974 | 2024-10-02 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| bbac5d09-1c8b-3f0b-8870-4411e9f1b2ea | -11.6743 | -64.9983 | 2024-10-02 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0f3481d9-5c05-35bf-90f3-f3525a75ddb7 | -11.6742 | -65.0172 | 2024-10-02 03:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 90074f88-49e5-3524-bee1-7a853977da94 | -12.2946 | -47.6446 | 2024-10-02 03:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| a3bebea8-2079-31a7-bcb3-415b60c3f873 | -12.7054 | -63.0798 | 2024-10-02 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| c36a1dd6-b1c0-3166-a1f8-db7c78a2b670 | -12.6486 | -63.1022 | 2024-10-02 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 148cb84f-2ae3-3eac-886e-b80c6f4f2ee3 | -12.6484 | -63.1214 | 2024-10-02 03:26:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 63b892b4-76f8-3ccd-b8a7-ea026c12cf02 | -12.8803 | -62.531 | 2024-10-02 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 42.8 |
| af7eebac-e6a3-345c-96af-01400b62927e | -12.8614 | -62.5321 | 2024-10-02 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 149.4 |
| ada77524-1c38-31c0-b56c-1fc4053b7626 | -12.8612 | -62.5514 | 2024-10-02 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| edbc3dc6-8172-3aab-8f7f-e4adbccae29a | -12.8424 | -62.5333 | 2024-10-02 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 111.7 |
| b0c80432-cde3-3c5d-808b-5e7e3674f3d1 | -12.8423 | -62.5526 | 2024-10-02 03:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 6be747d3-3d4f-3ee0-ab8c-80a47c4a29aa | -13.1122 | -51.4329 | 2024-10-02 03:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 88719334-f3d6-3f7e-95d5-3ba2f67b9ed3 | -13.2173 | -48.624 | 2024-10-02 03:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 79e4a5f0-09b5-3a32-8f99-d054802d4e17 | -13.198 | -48.6267 | 2024-10-02 03:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 06c9a4f3-c0db-3bcb-9047-1b442e3810b1 | -16.109 | -53.5215 | 2024-10-02 03:26:36 | GOES-16 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 82cb9e83-d9ad-3bad-9b5c-66b0bdf94b65 | -15.8936 | -57.155 | 2024-10-02 03:26:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 66d7a33e-9860-3483-9963-3d64d4a65aec | -15.8933 | -57.1754 | 2024-10-02 03:26:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| ebeebfb6-b10c-3e89-8353-592b08c8c2f0 | -16.6127 | -57.217 | 2024-10-02 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 52.5 |
| d8cac600-915a-3eed-9d97-fe2a037e4c39 | -16.6124 | -57.2375 | 2024-10-02 03:26:39 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 57.1 |
| cb002ce6-5a76-30d8-859a-bf09c5f37798 | -16.514 | -57.2896 | 2024-10-02 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.6 |
| f90bf3fc-9b1d-3f11-a918-829536e7a6d2 | -16.4945 | -57.2918 | 2024-10-02 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.2 |
| 8f7ef62c-684f-30ad-88fd-87eac6a68515 | -16.4942 | -57.3122 | 2024-10-02 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.5 |
| cbbdbe25-06ed-3d22-8607-eef9c62562b3 | -16.475 | -57.294 | 2024-10-02 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.9 |
| 35163eb7-ff5f-358d-b094-dea29fd02ce7 | -16.474 | -57.3553 | 2024-10-02 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| fa67bcb6-fb72-3df5-be5f-d115f5034016 | -16.4746 | -57.3144 | 2024-10-02 03:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 113.9 |
| 734168a7-2f24-3c93-a869-47261c35aa3a | -16.8096 | -55.9177 | 2024-10-02 03:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.7 |
| 88efc97a-3611-3378-90c9-e2389ed4abde | -16.7862 | -57.3606 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| 8ac0330c-12c2-3290-b2a6-8a545553494d | -16.7647 | -57.4856 | 2024-10-02 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.2 |
| 5415f4cf-e77f-31bf-a687-0db095acec44 | -16.7461 | -57.4265 | 2024-10-02 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 43b61278-44f6-357d-8835-7a59076faf29 | -16.7452 | -57.4878 | 2024-10-02 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 26ed77c8-61da-3e42-b2d4-2f2e70963ef3 | -16.7265 | -57.4287 | 2024-10-02 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| cb35f581-6cce-39f8-ab18-4d47724cd99e | -16.7108 | -57.1852 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| ab4d139e-e212-3450-aded-68571120133e | -16.7063 | -57.4718 | 2024-10-02 03:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 49834988-2855-3e57-b2c8-d3664c5cb4cc | -16.6916 | -57.167 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 88.2 |
| 475bb0f5-e9f1-3ab1-afc3-282719bbd637 | -16.6912 | -57.1875 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 241.0 |
| a8e7e436-e014-37f0-906e-d3900a5f1fdb | -16.6909 | -57.208 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 26ff485d-3cf9-30af-b68a-c9367eefd8ca | -16.6884 | -57.3718 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| 282ae8e5-ef7c-3233-841d-bbcb61a61404 | -16.6717 | -57.1897 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.4 |
| c41e1434-55b5-3b17-88b4-481e88068dc4 | -16.6518 | -57.2125 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 4c638c1b-2b21-3bdc-83d4-a0f9c2aa2e47 | -16.6322 | -57.2147 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| ed331548-156e-3329-8ffa-325af399f00d | -16.6319 | -57.2352 | 2024-10-02 03:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.7 |
| 424944dc-b3e7-3036-beea-636b0dc742b6 | -16.8695 | -55.848 | 2024-10-02 03:26:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 74.2 |
| 7bedc8cd-2d4c-389a-a549-41c03822e799 | -16.8386 | -57.7628 | 2024-10-02 03:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 25.0 |


[Clique aqui para ver as próximas entradas](README50.md)
