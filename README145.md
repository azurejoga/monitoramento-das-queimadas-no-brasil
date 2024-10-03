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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7cd46a2-811d-3abe-9750-eb60e561ba40 | -16.07665 | -50.32755 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e3d80a4-cd5c-3e7c-a6d2-f48f130e78ea | -16.07432 | -50.31874 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 43e177c8-63b0-3219-beee-5dae6c74521e | -16.07417 | -50.31707 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e602810-72c7-34e7-8d5c-75a2329e1ccd | -15.35112 | -51.5538 | 2024-10-03 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89c8e252-b01a-3f0f-8818-d650c83253db | -15.34752 | -51.55325 | 2024-10-03 04:53:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b9060ca-e9a1-35b7-b9ef-f2da0dda197f | -18.26097 | -50.8234 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdca4002-4080-37b0-90fd-51b6add2887b | -18.25778 | -50.8259 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28a5045a-423e-39c5-8182-fb9f66f95413 | -18.25708 | -50.82298 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30682921-020c-3b56-84bf-93432c773022 | -18.25522 | -50.81517 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84900ff2-d8e3-33aa-bbda-369cb878fc72 | -18.25458 | -50.82015 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54a31f17-2374-3316-98c2-3c903364124e | -18.25389 | -50.81747 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d637594-811c-30b2-a049-0ef6fa20e3d3 | -18.25319 | -50.82261 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25e2291a-f41f-3cf7-8a48-ab50a15b2f0d | -18.25065 | -50.81223 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8bd31e5-968b-3e48-aa78-88224f08cf28 | -15.6767 | -52.50686 | 2024-10-03 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6d2497ef-7257-31df-af41-53858ae6e5f1 | -15.67323 | -52.50629 | 2024-10-03 04:53:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f9cfc989-17ac-311f-bab1-bcaea96b7470 | -17.72423 | -53.07649 | 2024-10-03 04:53:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90ecc75f-f1a8-3c59-b285-b8c770b8fe35 | -17.62083 | -53.15594 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69ac7396-2eb4-34f4-a4f6-6f6120bb4232 | -17.61851 | -53.14769 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4733fb02-02f4-3410-8fff-dbd0f379ee3b | -17.61507 | -53.14712 | 2024-10-03 04:53:00 | NPP-375D | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 854accf2-5bf5-3dc3-aa9a-b3512ce4e71c | -19.72349 | -45.07479 | 2024-10-03 04:53:00 | NPP-375D | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b3eebe6-6dd9-3900-be19-3c87c053e249 | -14.17985 | -60.25485 | 2024-10-03 04:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10c78a42-2d4f-33fa-b0e9-1027ddc77116 | -14.1791 | -60.25889 | 2024-10-03 04:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f15b45f0-398c-3cdd-8698-3680f890728b | -16.55428 | -58.22779 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| e0594243-1ea8-32e3-94ec-469ce85265e7 | -16.55353 | -58.23215 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| ecc25c85-cb3e-3e54-b050-715cdca9c96e | -16.5529 | -58.214 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 9152f8ae-ed50-3b27-8999-68392642bf70 | -16.55278 | -58.23652 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| fc63fe19-982b-3908-b4f7-6da20070db8b | -16.55215 | -58.21835 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 6cc8bef1-da0e-32e2-a8b1-7c4a2e414d23 | -16.5514 | -58.22272 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 8b92cea1-8e8f-303b-8db4-96ac2d94c2ce | -16.55065 | -58.2271 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.4 |
| b521a9f1-b47a-3e1f-88c4-d6b31a91bbee | -16.54989 | -58.23147 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 31d360c1-595e-33c1-a929-6cc290137d3c | -16.54928 | -58.21329 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 1926fa44-17e5-353e-b351-b546c89d207b | -16.54914 | -58.23584 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 4acfdc4f-6724-36d3-8b1e-11c928e0396d | -16.54852 | -58.21766 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| dcd5845d-4b1b-3d21-bd1f-67aa847f6bc3 | -16.54777 | -58.22203 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 64b10797-77e5-3592-a286-54e8401ceb66 | -16.54702 | -58.22641 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 74fdd4d3-ac28-3a0c-9d57-636e91318374 | -16.54626 | -58.23079 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| a38780ed-03c0-3340-9221-9b2791fdb9f5 | -16.54565 | -58.21259 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 96551091-b9ab-3b33-adf4-29e68b669939 | -16.5449 | -58.21695 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 090943f5-0ee5-3d5f-8b6f-ef85872aacf3 | -16.54414 | -58.22133 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f3e05baf-3041-3161-84d2-76fc42e1c805 | -16.54339 | -58.2257 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| d55d111e-2744-38b1-8797-eafca56f8371 | -16.54263 | -58.23008 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| c45adc3a-5733-3e87-959c-b5dddf444609 | -15.38187 | -58.1519 | 2024-10-03 04:53:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae5428ad-1019-37b7-8ef6-94b4eeacd6f4 | -15.37018 | -58.1537 | 2024-10-03 04:53:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1083abd9-9f60-3f97-975c-0711e1b8922d | -15.36576 | -58.15734 | 2024-10-03 04:53:00 | NPP-375D | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e551ca08-8d46-382a-a2c6-7621a0405cce | -16.73337 | -58.46763 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a3fd6e46-adf6-34b8-abd8-e38b196a1ac1 | -16.7297 | -58.46694 | 2024-10-03 04:53:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 35393380-bccb-3ebc-a90b-d2f34886ba85 | -18.89493 | -54.51562 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1e68e12-15f7-306e-9b43-e99c87393ac4 | -18.89436 | -54.51935 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f44cf80d-31f2-3581-8b1d-744baa8e6beb | -18.89158 | -54.51505 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bdfd70b-0501-38dc-b698-9cb5f9126b11 | -18.88157 | -54.49044 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 44327823-3926-3af8-a6b7-966b19ad3bd3 | -18.86919 | -54.52652 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddb6b9df-ae6b-31cb-8e1e-7aacc402b60e | -18.86585 | -54.52588 | 2024-10-03 04:53:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 308bc181-3f9f-3d1d-ae3f-042e5c5388dc | -18.85586 | -54.47851 | 2024-10-03 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c072ceb3-81fc-3d59-a1d9-66b1a25a0ec5 | -18.85529 | -54.4822 | 2024-10-03 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c081c8f-99ce-328d-b0f1-56cfef5b596b | -18.85306 | -54.47427 | 2024-10-03 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a06a6ea-a671-361e-ac0f-114d60d6b83f | -18.8033 | -54.47421 | 2024-10-03 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e67eda4-4082-3a92-8b59-fbaf5b2a3eb7 | -18.8016 | -54.48534 | 2024-10-03 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bccd4acc-0efe-3a2b-888d-51336bb5c6b9 | -18.79938 | -54.47738 | 2024-10-03 04:53:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a13b957b-d953-35da-afcb-94cb40159d37 | -20.98023 | -54.69333 | 2024-10-03 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33969017-bcf7-37fd-8917-952f48a57214 | -20.7775 | -54.81236 | 2024-10-03 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5b17479-980c-3f95-8ace-cff27d406235 | -20.77357 | -54.81554 | 2024-10-03 04:53:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbd5e5aa-f809-3eef-b519-4c2ed3b02f8a | -20.54907 | -54.66584 | 2024-10-03 04:53:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7907b3b0-0d80-3a99-979b-fd6b7ec67f33 | -20.0093 | -55.4584 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbdf3dd7-ee62-3cc7-ba3d-e4d525f729ef | -20.00597 | -55.45782 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d24a58a7-429e-3c1e-bb6b-fa17a850e107 | -20.0054 | -55.46151 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13155e84-ff85-3926-876c-54a0ca47c354 | -20.00321 | -55.45355 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 866a87cd-c6cf-3c50-925d-07920ebb1912 | -20.00207 | -55.46092 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b360d8e2-a487-3b88-9e08-a5e409e0cad5 | -19.99988 | -55.45297 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc97ba0d-2644-3e69-808d-d0fb0e7dc926 | -19.99931 | -55.45665 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b720e7a-4426-3096-b139-1da3f3bb562a | -19.99655 | -55.45239 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a6109e58-93ec-34ab-8302-77205ed6fbaa | -19.99207 | -55.45918 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6c2709e-03bd-373b-9077-0c56bdcfcd14 | -19.96475 | -55.48088 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| edd75332-0810-30ae-ae65-b4425dffa43e | -19.96199 | -55.47661 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9af90f1-f8ea-3733-abdd-f78f1f1c1075 | -19.96142 | -55.48029 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e25b395c-d9b7-3aa2-9ff3-3289e2c26743 | -19.96084 | -55.48397 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccdd0d79-8672-32ca-964f-e1d5f290176b | -19.96027 | -55.48764 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12f730c5-6e32-3fa3-97e4-f9075cdc7f4a | -19.95904 | -55.47971 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5d088a1-7bcc-3266-b860-3a349ca52836 | -19.95847 | -55.48339 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01829acb-929f-3ec2-a579-df0b464d00ea | -20.05314 | -55.95327 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 87824c41-9ded-36f7-ae08-5046575ba5f2 | -16.143 | -55.91729 | 2024-10-03 04:53:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 105e6216-d0cf-32d4-ad39-27fee2df5478 | -16.1424 | -55.92096 | 2024-10-03 04:53:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 4713cb2b-9f31-31ba-87be-58a0d72e5015 | -16.13903 | -55.92041 | 2024-10-03 04:53:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9cd5a7fd-5044-3f2c-9ba4-0df5c33ca914 | -17.15256 | -56.15833 | 2024-10-03 04:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6267fc9d-4a4e-32eb-be0f-c9d61529e3d8 | -17.15195 | -56.16203 | 2024-10-03 04:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e9ebbe63-5eb7-39c4-ad49-42a4e877fe16 | -17.15135 | -56.16573 | 2024-10-03 04:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4f98bb98-8424-39b8-a0ef-a95e8ba64f70 | -17.15074 | -56.16944 | 2024-10-03 04:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5980b861-c170-350d-9675-1060c5c085d0 | -17.0564 | -56.08499 | 2024-10-03 04:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a5535e2e-d2b8-37c0-8489-de8563243ef4 | -16.91717 | -55.86452 | 2024-10-03 04:53:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9308e43c-da88-3a43-858e-981628860651 | -20.05589 | -55.95754 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7ccea685-2482-323a-9276-b40552afaa58 | -20.05256 | -55.95695 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3f192661-9998-3ef3-a38d-1db6a9f5c939 | -20.04981 | -55.95268 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9b9a6434-4db0-355b-8b2c-feaffdcbefee | -20.04922 | -55.95636 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 21af4994-15ca-3291-b0a2-a72c6b42d721 | -20.04864 | -55.96004 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| aaae5085-c735-3556-8e50-00a39d76bcec | -20.04531 | -55.95945 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 79f3fa26-a987-3834-9387-52747842fc5e | -20.04198 | -55.95885 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b5b660fd-c8f3-36d7-851c-60f463b220d4 | -20.0359 | -55.95399 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fec6750d-003d-3f6e-ac12-630fa945f2c5 | -20.03532 | -55.95767 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c2cad45-4d46-3c3d-be10-b7fa19102122 | -20.03199 | -55.95708 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3a8b30b2-8727-35da-a38d-eeb851badeb0 | -20.0314 | -55.96077 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f87269b6-c495-36f6-8161-3915f8e50487 | -20.02866 | -55.95649 | 2024-10-03 04:53:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README146.md)
