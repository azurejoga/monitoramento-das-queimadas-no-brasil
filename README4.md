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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b822592d-7249-31c9-800d-51cdc827f956 | -5.2486 | -43.91304 | 2025-11-16 00:13:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 829b04a8-2a4c-3fa0-9ae8-276f0074a394 | -6.56923 | -47.90531 | 2025-11-16 00:13:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c6afb690-80c4-361b-b933-7327539db683 | -9.71596 | -48.90928 | 2025-11-16 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| c9c6466d-3466-3d3b-9d97-77a80231fbfe | -7.71181 | -47.29198 | 2025-11-16 00:13:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| e09f30ae-fbd3-3d14-b775-d5e4ee539679 | -5.51329 | -40.98116 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b5516432-ed45-37b1-9eec-3e544ed2d25b | -9.33522 | -46.57707 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 689da837-c132-3ef6-915a-57003b895b94 | -9.50729 | -47.263 | 2025-11-16 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b3a33ca9-beac-3835-be1e-23cd06d570be | -8.32138 | -45.67521 | 2025-11-16 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b00689f0-264e-3ebb-ae88-b22b631f60d9 | -9.74283 | -43.96699 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 1598c083-2213-3191-890c-11a42e210991 | -9.75298 | -43.97472 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 9a99d74a-7ba5-39e0-a575-969ba627e0d7 | -10.353 | -47.33539 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0f55a8c3-8f5f-3308-8e74-9faa512d4cd5 | -6.61932 | -41.46607 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 1ad4b71d-c111-350a-874d-37d3a179bc94 | -6.68496 | -42.05563 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| ee808ad5-8951-367d-939a-1b811d7ee8fb | -4.62786 | -47.4123 | 2025-11-16 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a1a7d106-906a-3948-93cf-53d7407c19fc | -3.1389 | -41.88283 | 2025-11-16 00:13:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0cb12dae-3bdb-3670-a25d-596632dc299a | -7.18871 | -39.20575 | 2025-11-16 00:13:00 | TERRA_M-M | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 87559c05-62ea-3d6e-a943-a8106ce3f5db | -5.69458 | -45.99342 | 2025-11-16 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 2f69ca3e-18fc-3389-8ddc-822f01cd01c0 | -4.36611 | -44.71511 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2379f92e-7fea-3189-801d-cc1da7e792d8 | -3.63534 | -45.15813 | 2025-11-16 00:13:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f28f7777-6510-3f95-8106-60ddef09f725 | -6.35293 | -46.15901 | 2025-11-16 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a6644237-2440-33d6-8e4f-639e3ed4511a | -6.50879 | -47.63458 | 2025-11-16 00:13:00 | TERRA_M-M | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 53a7e689-5701-355a-9918-41d2df024cb3 | -9.71113 | -48.90174 | 2025-11-16 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| d4a33fa6-abde-3036-bd0f-95ad774311e9 | -7.21287 | -47.98416 | 2025-11-16 00:13:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 45f0dcef-4fbc-3515-83fc-3bb34bc04555 | -3.67256 | -44.17458 | 2025-11-16 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a89a51d6-7222-380a-8eee-edb39f9bcd4c | -3.79219 | -43.3752 | 2025-11-16 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 54e11acd-e306-37ce-a62d-3c00920d589d | -10.3966 | -49.04888 | 2025-11-16 00:13:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d29d49c4-cf2b-38b4-80f7-b8fc652625f6 | -3.93414 | -47.05567 | 2025-11-16 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c9730f18-2a68-352f-9227-fcc942c46204 | -7.4649 | -42.54897 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6186a9aa-2359-3bc4-91a4-42c53101eda0 | -4.24359 | -50.05395 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 15b80333-f948-3e9c-9378-a9e002cc2ab7 | -10.54177 | -47.93375 | 2025-11-16 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a89c8271-a472-3962-af36-04631855c4a5 | -4.68862 | -46.51683 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c52e28f2-4816-3bde-9fb6-a44e9d0862d4 | -3.94673 | -47.21367 | 2025-11-16 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| de25b0aa-635b-34b8-93ce-5c7915e4cf84 | -9.96243 | -44.95114 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 444e2dc4-f2a6-378e-a102-3890696ee16c | -4.22692 | -44.64503 | 2025-11-16 00:13:00 | TERRA_M-M | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bcfb89db-5a43-3f39-be0d-711070e126fc | -3.99427 | -45.88276 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 39bf8eb8-91ca-32a5-8e9c-157f00ec052d | -9.50867 | -47.27365 | 2025-11-16 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| a7cecbda-c4ee-3fbb-9e0c-829eb9fb45ba | -4.8387 | -47.53762 | 2025-11-16 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ed109681-c90b-3e3f-b280-09cd1b82acbd | -5.63831 | -47.74644 | 2025-11-16 00:13:00 | TERRA_M-M | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ca4899b1-411f-3a17-94ef-a62257bfeb23 | -6.12888 | -48.05123 | 2025-11-16 00:13:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 43848d0c-9fe0-38fc-8097-1017f66dfb31 | -9.13566 | -47.70839 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bb3c0314-6dee-362b-9306-7ffbd1809bee | -5.23654 | -44.35312 | 2025-11-16 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 8624d917-a6f3-3f68-b64d-8e190f9854b4 | -5.35505 | -47.21769 | 2025-11-16 00:13:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 215a1dcb-1249-3295-8fc5-600484486b80 | -9.73268 | -43.95927 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| ba8978e2-987f-3811-b113-4fee80a97414 | -5.06909 | -44.34229 | 2025-11-16 00:13:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 89f07782-ae17-3768-a935-2732b2e3310f | -6.7003 | -44.14764 | 2025-11-16 00:13:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bca061a6-860b-33ff-bb7b-e2c8b9fbc351 | -4.1605 | -42.13958 | 2025-11-16 00:13:00 | TERRA_M-M | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a44e16a4-be47-3731-b65e-9bb33062bb6d | -3.66292 | -44.8269 | 2025-11-16 00:13:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e6e4c94b-dd28-3653-b983-abfeee940d76 | -3.68129 | -40.8764 | 2025-11-16 00:13:00 | TERRA_M-M | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 45.0 |
| 02393836-f532-3d83-aa71-c9eb37772477 | -4.0732 | -44.59819 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f0635064-f35f-3ce6-aedf-8e5b62f451d5 | -5.60957 | -46.37609 | 2025-11-16 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6dccf02d-0f2e-33de-b470-6798ac677a9e | -4.15075 | -46.3494 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| fe0d3809-6ef1-3dec-a973-2f78be91e828 | -5.59028 | -44.90112 | 2025-11-16 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 521fa0e2-e1fe-3dfa-8877-303953fbfcca | -5.98996 | -41.92631 | 2025-11-16 00:13:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a8e80c08-cd69-357b-8739-78028035912e | -5.74149 | -49.46014 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 39155961-acc8-3dd0-8428-6e8bef1dd343 | -4.01034 | -42.88936 | 2025-11-16 00:13:00 | TERRA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 289d6473-f8f2-3712-a674-aa110f5971b4 | -4.72654 | -46.38648 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a37bfaf0-ef17-3c88-a2d2-8bb1d86ddfd4 | -6.5407 | -43.40847 | 2025-11-16 00:13:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 17fc2b79-d0b9-3a0b-bd03-dc579ddbe64e | -8.05534 | -43.11231 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| b9eee760-a1e7-3da3-a553-786453d4e843 | -4.65576 | -46.74221 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 216a9df6-229b-3310-a837-79f1d526d73d | -3.57875 | -44.09658 | 2025-11-16 00:13:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 262b8add-0e61-3a5d-9925-b164a04fb5c7 | -8.09502 | -43.00963 | 2025-11-16 00:13:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| a9002a1e-270e-36ab-a560-2e2abab5ddcc | -4.14188 | -46.35065 | 2025-11-16 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd16c6fd-5750-33b3-a3a9-92613e887660 | -9.74156 | -43.95796 | 2025-11-16 00:13:00 | TERRA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 5a8951cd-9a9b-360b-a748-377a43ea8f85 | -9.34707 | -46.5954 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 2392aeff-7894-34d3-94a4-0bcc8d829193 | -8.57551 | -48.8024 | 2025-11-16 00:13:00 | TERRA_M-M | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f9617ba6-1b52-37d3-b101-41a3e104216c | -4.64616 | -44.67522 | 2025-11-16 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a15271a3-acf1-3723-9842-14554d2429b7 | -7.35908 | -46.58466 | 2025-11-16 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 194f60b2-169d-3b38-ba39-a55d9ae91e32 | -8.58449 | -46.05337 | 2025-11-16 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4ace4c33-cb28-3569-82d2-08fa43b53cc0 | -3.59993 | -41.66365 | 2025-11-16 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| dc9ed838-12f6-3138-a209-cf39595f1853 | -9.11854 | -40.46295 | 2025-11-16 00:13:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 11.3 |
| bf3e5166-6d9f-3af5-aa17-587b49e91d22 | -6.51435 | -39.52338 | 2025-11-16 00:13:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 90336d95-309f-34de-9072-1475c04a666a | -9.06014 | -44.7593 | 2025-11-16 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c7526e2c-8486-3e61-8a4a-6e22fbb9938c | -7.64471 | -38.93346 | 2025-11-16 00:13:00 | TERRA_M-M | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 25.9 |
| 7759ef16-0eac-30c4-bf52-bc2eb2c2eca8 | -6.31061 | -43.80244 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 15c99c03-ea1c-34c6-883b-28d9a2cb38c5 | -4.80022 | -41.69016 | 2025-11-16 00:13:00 | TERRA_M-M | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 232.9 |
| e903ca7b-48be-3dce-8aa6-15ee88dc90f9 | -6.68328 | -42.04419 | 2025-11-16 00:13:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 49.0 |
| 0f737087-4926-35c8-8f16-b1a853b0a4c6 | -6.93544 | -39.71604 | 2025-11-16 00:13:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 61ed8114-9b4f-32fc-94ff-6c368455cd00 | -6.3093 | -43.79318 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 4f769cba-c34c-3e40-9038-0c549e504a7c | -8.06075 | -45.657 | 2025-11-16 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c31e040a-b72e-3685-bdd8-9ec41d76a773 | -5.23524 | -44.34392 | 2025-11-16 00:13:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5fcf225a-5630-3641-b2df-203cb0c91759 | -5.33429 | -49.28697 | 2025-11-16 00:13:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 727add55-8bfc-3583-bcb4-71253d25700f | -9.71427 | -48.89566 | 2025-11-16 00:13:00 | TERRA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 7a9435b9-21a2-3bf4-8fa1-e1ec2cad9f1c | -4.65256 | -44.65582 | 2025-11-16 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6dd88747-14e4-3d78-914e-dc337f243490 | -3.85044 | -46.17553 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6872c901-046e-3172-92fc-d821c048fd25 | -9.84721 | -44.18425 | 2025-11-16 00:13:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9d208b62-352c-3658-b78e-8c4e58888de9 | -4.35173 | -44.35198 | 2025-11-16 00:13:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a7e1ed3e-8b22-3d19-a5c3-b65b074a728e | -5.8494 | -46.45025 | 2025-11-16 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 38055bf7-d58c-303a-863e-4afc7279f296 | -6.21823 | -47.27034 | 2025-11-16 00:13:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0b372e6f-2646-39b0-90e7-c5ff91d01095 | -4.33545 | -50.56053 | 2025-11-16 00:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e096ce4d-7347-39b2-a04c-9f6084de091b | -6.21028 | -47.28142 | 2025-11-16 00:13:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8a8e9aed-b2fb-375d-bb72-b7a5787f0695 | -5.83233 | -47.82199 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 18b9d843-c13d-3677-93cb-6bd7e07a6737 | -6.62643 | -43.69319 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2fcce665-5ef8-34a2-96bc-526f08ee71f7 | -3.9486 | -45.95785 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f64e70b0-1cd5-3726-9358-a3b50c98d06b | -7.01822 | -45.16711 | 2025-11-16 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| b01e905e-f1a3-3f95-918a-f61ede66e7a8 | -3.5872 | -41.65182 | 2025-11-16 00:13:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| b5537242-721a-3aa1-933e-be5ca5ccb6b0 | -3.1354 | -41.88964 | 2025-11-16 00:13:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 08f853ce-3acc-3040-9cfd-581d0951b49d | -4.61737 | -47.26865 | 2025-11-16 00:13:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4ebc1590-6793-321a-9fdc-69673d6b2e41 | -7.41103 | -40.05921 | 2025-11-16 00:13:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 3913e5a3-54b8-3123-9bef-8b4ebd61795d | -6.30018 | -43.79447 | 2025-11-16 00:13:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| b431f312-5977-3c66-bd66-da7757c81f5f | -9.34447 | -46.5758 | 2025-11-16 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README5.md)
