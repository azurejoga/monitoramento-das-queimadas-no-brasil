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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddf16b9f-c805-3007-ac42-4c5ed6f9a0c4 | -6.861 | -41.6772 | 2026-08-30 15:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 454.2 |
| cf87b4c4-bda6-3353-bd4e-089e00254cc4 | -9.2396 | -60.4256 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 8543628c-575d-3afa-bd96-6e1bf5489444 | -5.8894 | -57.7708 | 2026-08-30 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2a625752-9419-392b-9e2c-9bceb30d7936 | -10.7649 | -50.6366 | 2026-08-30 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2a37ab76-c551-378a-9f00-eae3e6356695 | -12.2281 | -50.5578 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 18c486cd-4a52-3b6a-95d2-fd325dbb5157 | -14.4197 | -52.5413 | 2026-08-30 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 166.1 |
| 0143f79f-d239-379f-8990-ac8ff0dae03d | -7.5661 | -61.3239 | 2026-08-30 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 35ce0a93-30e7-3a73-a5c5-422103da3a1f | -9.1533 | -59.5027 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 237b8776-e5f4-3fdb-9991-8d5d545dc117 | -7.1312 | -42.7708 | 2026-08-30 15:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 144.6 |
| 421a5919-08b6-3f80-b474-415bb335687d | -12.9027 | -45.8612 | 2026-08-30 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 02afa526-3b9f-3adf-906d-57b394b02fd7 | -9.0615 | -65.4169 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 80c085d7-e34b-3bea-8ad6-46037d956070 | -7.2933 | -60.5905 | 2026-08-30 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 49382cbe-9e44-3fc1-a61e-65e7d4210a09 | -9.874 | -60.2762 | 2026-08-30 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 9da525a8-7b3c-39bd-92f7-271570f27412 | -9.9281 | -60.5242 | 2026-08-30 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 9b7538b4-3368-3093-9d59-e5aff81d01d7 | -14.4846 | -52.1299 | 2026-08-30 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| ae865f8c-f2fe-3ae4-9634-1332ad82395e | -11.2317 | -53.9958 | 2026-08-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 140.8 |
| b33683d0-f5a2-3f03-9876-9bd12280b115 | -11.1818 | -50.6133 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 1f1093ae-9eeb-3eb5-a059-a88b08a70b39 | -14.9854 | -48.1753 | 2026-08-30 15:10:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| ed2e7468-810b-3266-973c-40996a7f8e9c | -10.9367 | -50.5332 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b799e345-632a-3c6e-ba28-220ae8336de1 | -15.2283 | -57.6517 | 2026-08-30 15:10:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 0dcd28fe-1059-35f5-adbf-56a157644751 | -4.1515 | -60.7068 | 2026-08-30 15:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 632efe7b-d430-3465-9844-bc594d59b266 | -10.937 | -50.5118 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 1ffd36f5-b2b9-3fcd-80c4-fae189366e97 | -11.3619 | -45.1724 | 2026-08-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 229.8 |
| fdbc6d3b-01a0-3c6b-8eba-248b02f7c3a5 | -3.1998 | -61.161 | 2026-08-30 15:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 3646701c-baf7-338b-9699-47a17b5882da | -8.574 | -66.9569 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.4 |
| a76b7a8e-13c5-3ea0-9887-4cc697fc4d7a | -3.2361 | -61.2548 | 2026-08-30 15:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 59b08224-ca77-3501-8d22-4da3d134f1de | -14.5638 | -52.013 | 2026-08-30 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 7154dd84-2fdf-356a-a5af-5e7dcbe662c0 | -11.1631 | -50.594 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 2cc5718e-b9b2-39ec-969d-6122dab419f7 | -11.2314 | -54.0164 | 2026-08-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 223.0 |
| 53588979-c90c-35d5-9e00-08dde9839beb | -12.3424 | -50.5655 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| f26991d5-b953-3cb5-af8b-b8ab54e0a1ab | -9.2071 | -59.771 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| a80f9bc5-2646-3218-9cad-6bbff0c45351 | -9.0614 | -65.4355 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 7c89c7f1-8681-3b4c-926e-cbf67936d2a0 | -8.5925 | -66.9564 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.9 |
| d5e7693a-ba67-38cf-907d-650d23bcf131 | -12.3229 | -50.5892 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b18d749b-b46a-37f7-ac85-76100f4a05ed | -7.9425 | -44.2538 | 2026-08-30 15:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 9c6129ae-e841-370d-bbcd-e968e65beadd | -13.4187 | -51.4372 | 2026-08-30 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b505aff1-04f7-39e7-8127-8a3f86d2e6a7 | -13.3943 | -51.7595 | 2026-08-30 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 3cb8abdc-780c-3d3a-bff1-0514f2189458 | -11.0054 | -49.6893 | 2026-08-30 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| daa7802b-151a-3b2c-8dac-b26c7876ce9c | -14.4842 | -52.1512 | 2026-08-30 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 114.7 |
| ba115e24-b31a-30a6-9ff4-561280c0fb4b | -12.3811 | -48.1877 | 2026-08-30 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6fe94fab-07e0-368b-bb2b-43cbda80ee35 | -9.1711 | -59.618 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ae2e23c5-1b5c-36fe-a2a4-a6e44cb0593c | -13.856 | -54.1175 | 2026-08-30 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 160.7 |
| db1e975d-5693-3e87-874f-69b819b2ab0b | -12.2277 | -50.5792 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| fee840be-a40d-3e31-b458-2f7c481b581f | -9.1661 | -60.2945 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| a92b952c-145b-39b3-81f0-b5ef6ce59207 | -13.8381 | -54.0365 | 2026-08-30 15:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 94655b5c-2fa2-3124-ae87-c29381bf5027 | -11.006 | -49.6461 | 2026-08-30 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 52b4ffa8-ca96-3eed-a58b-e9da2b30d2de | -7.917 | -61.3481 | 2026-08-30 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 54399400-1680-3104-8cd7-478fd7657eb7 | -10.3391 | -49.9762 | 2026-08-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 73ba0fe6-b914-38ee-b614-0c04f9fca352 | -12.3807 | -48.2099 | 2026-08-30 15:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| 50dd06b1-2a3d-325d-87d6-947591207fcd | -4.9605 | -55.8226 | 2026-08-30 15:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 386bbfd8-1fd2-34d1-9b33-9db4af00b058 | -19.0744 | -57.3876 | 2026-08-30 15:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.1 |
| 272887d6-1ad9-3f19-90bb-662c2719acce | -11.2485 | -45.0963 | 2026-08-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| ba415213-88e6-3259-8949-418beedbce33 | -7.5662 | -61.3049 | 2026-08-30 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e0acf0cf-548d-3d48-aadc-3e46989d4d76 | -11.3427 | -45.1751 | 2026-08-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 162.0 |
| e7d1e126-4fb9-3a29-84ba-49561fda5733 | -10.3226 | -58.0847 | 2026-08-30 15:10:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 8c8fcb62-6fa8-3bfc-817d-b147c9231124 | -8.3679 | -57.6737 | 2026-08-30 15:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 571b05eb-9182-37d5-8972-827c436c9333 | -16.2735 | -42.5653 | 2026-08-30 15:10:00 | GOES-19 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 04a40b59-385f-3698-8197-e97d3a374715 | -7.991 | -46.4954 | 2026-08-30 15:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 9c740fb9-b517-3b77-b0dc-0a85014fbef3 | -8.2414 | -54.9601 | 2026-08-30 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 65213407-c063-3b33-94de-3619cd577556 | -11.6396 | -50.4553 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ad1e1d2a-2208-3d93-97e4-fa5cf94ee7e3 | -10.358 | -49.9742 | 2026-08-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 3a55f320-e0d6-39dc-89b1-fc394b6d5a2d | -7.9611 | -44.275 | 2026-08-30 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 259.2 |
| 252b1939-97ad-3b01-9284-9e8c2959e786 | -15.228 | -57.6719 | 2026-08-30 15:10:00 | GOES-19 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 9dbcaac2-b565-3a9a-8f31-fe3000b4bbfc | -7.5846 | -61.3232 | 2026-08-30 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 881707ae-9b52-36d9-8f7c-c6c0680655c2 | -12.9216 | -45.8812 | 2026-08-30 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 131.3 |
| 060ebca8-7a47-39ab-830f-008d8db22c57 | -11.2294 | -45.099 | 2026-08-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 6113bb26-bc1c-394a-a111-cece0f5b7da1 | -12.3611 | -50.5846 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 4659f1e1-a5fd-388e-b56c-a8c0c2dcf618 | -12.2086 | -50.5815 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 2d222cd3-5c87-3e4f-a3a9-22543e02454d | -8.5925 | -66.9379 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 57318bd8-bfa3-3051-9c22-4026f61bc3be | -12.9032 | -45.8382 | 2026-08-30 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| ad9e0b0a-6ded-37da-bcf3-56333f8232fd | -14.4193 | -52.5625 | 2026-08-30 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| e451dd1e-929a-36b2-8ed5-cfb48041a648 | -5.4876 | -57.1416 | 2026-08-30 15:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| f3481481-0659-3fd7-89c7-e40f323122bf | -10.9559 | -50.5098 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d4543c76-6c16-36c5-ad40-4025ca0b30ba | -14.4 | -52.565 | 2026-08-30 15:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a96dbb08-73b5-31e6-a187-e62aaeb171f5 | -10.7405 | -54.0606 | 2026-08-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3a0ad87f-780d-3bac-8164-a9d1c4fbfb09 | -9.9282 | -60.5049 | 2026-08-30 15:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 393.3 |
| 35154187-72f7-3ebf-9c8c-a5d54962749a | -10.5644 | -46.1683 | 2026-08-30 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 165.8 |
| bc5bfa05-5338-344e-917a-e77995a83533 | -7.5272 | -44.3413 | 2026-08-30 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 41ab0381-e4ee-3fb8-9aff-b85247fda189 | -3.913 | -60.9395 | 2026-08-30 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 6c3b6b2a-ae27-305c-8603-34e58fa2731c | -5.9819 | -57.6892 | 2026-08-30 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| ed67c011-91ad-3df9-ad3b-6be57e42857e | -12.1895 | -50.5838 | 2026-08-30 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 88474840-a66f-355b-bb9c-6966c0538ed5 | -3.9363 | -59.3381 | 2026-08-30 15:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 04566c14-ea13-3742-ace8-1242e9ea9de3 | -9.1662 | -60.2752 | 2026-08-30 15:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 23b68d5d-50bd-345d-9223-27b488bdb04a | -7.3479 | -55.1544 | 2026-08-30 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 66cf97c2-723e-3f8f-9d06-1c23567a6204 | -14.1459 | -52.7871 | 2026-08-30 15:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| a986466a-2b40-3054-9c11-c974f9b4b7c4 | -10.1348 | -45.7006 | 2026-08-30 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 208.9 |
| 40d826ed-ae8e-3fd2-a4ef-cf1a3be02250 | -10.7409 | -54.0196 | 2026-08-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5cb90928-e7df-37fd-ad3a-8a1f1b55dccf | -11.1821 | -50.592 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 23cd0069-3a72-3b04-b0d4-7c7ee220adb8 | -7.2932 | -60.6096 | 2026-08-30 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 701275d0-2a26-3fe4-8cef-03738eb145f2 | -10.4794 | -64.5012 | 2026-08-30 15:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 9fbc013e-1f2e-3737-9627-56508b2fdc83 | -14.5631 | -52.0557 | 2026-08-30 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 6b9acf81-9de1-3c7b-9c7d-7a535635208c | -9.043 | -65.4175 | 2026-08-30 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c642b9ee-cc62-35e7-8c7b-731eef4cdbca | -10.5601 | -50.4022 | 2026-08-30 15:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 467acfe9-7647-3acb-8899-b976baa0d548 | -10.7457 | -50.6599 | 2026-08-30 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 76832816-648a-3d7c-bed5-e7e2fdd841ad | -10.1538 | -45.6982 | 2026-08-30 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 419.2 |
| 94fa24cc-b69e-31f0-addf-4fe35c0380c6 | -11.3431 | -45.1521 | 2026-08-30 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| d6b485d1-d21f-3be0-baa2-e6c6ec17b1da | -10.7407 | -54.0401 | 2026-08-30 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 220.0 |
| e70ea001-3c4a-315a-962b-831863cf26f1 | -14.5634 | -52.0344 | 2026-08-30 15:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 206.8 |
| 49b80f55-4bf3-3222-9b0e-eda1a1e9fc04 | -11.0057 | -49.6677 | 2026-08-30 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f27ae44a-1600-3292-84c4-89f08d719083 | -11.1634 | -50.5727 | 2026-08-30 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README91.md)
