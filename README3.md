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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af7f6ed5-6d89-317c-8c55-651771406f0c | -5.2942 | -41.2295 | 2024-10-30 00:07:12 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50b8a5a3-6877-3fa8-b00d-aaa277e0847f | -5.2746 | -41.233799 | 2024-10-30 00:07:12 | METOP-C | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ace5e380-4074-3010-9bdd-b4378237fae2 | -5.7139 | -43.674198 | 2024-10-30 00:07:14 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30f64345-b9fc-3062-8813-db385227c224 | -5.9846 | -45.335899 | 2024-10-30 00:07:15 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb033631-9cc7-3ae8-8d1f-97e433015179 | -5.9878 | -45.350601 | 2024-10-30 00:07:15 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 56f99a85-d49b-3b61-87d3-4c5ec3595562 | -5.991 | -45.365398 | 2024-10-30 00:07:15 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fc4c2e71-98ef-3e8f-acfb-9d3dd2366a6b | -5.9781 | -45.352699 | 2024-10-30 00:07:15 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffaeb74d-c4b5-3bf9-a0ee-e342a0539915 | -5.9813 | -45.3675 | 2024-10-30 00:07:15 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bdd3b8d2-fca2-38f4-968a-aa818d22d002 | -5.4676 | -43.161098 | 2024-10-30 00:07:16 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 336790e1-b332-3e5d-a8da-85f57218abcf | -5.4699 | -43.171501 | 2024-10-30 00:07:16 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2998696f-caf6-3075-8b82-9764d35e8e92 | -5.5843 | -43.6903 | 2024-10-30 00:07:16 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f98ab85-ab97-3d68-a80d-6fefc080b02c | -5.5868 | -43.7015 | 2024-10-30 00:07:16 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 363ea609-b8fd-3562-bef1-ffe1eb724efa | -4.5244 | -39.011398 | 2024-10-30 00:07:16 | METOP-C | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6d7751f1-cc5a-3c30-980c-98b99c179024 | -24.0123 | -54.151 | 2024-10-30 00:07:18 | GOES-16 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 53.1 |
| 850f7a8c-b733-3edf-a66c-048f135a8693 | -5.5644 | -44.298698 | 2024-10-30 00:07:18 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccec8930-f3f3-3419-a079-875660c58c8e | -5.5671 | -44.311001 | 2024-10-30 00:07:18 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d377464a-f378-3b64-8653-12af0e6cdf2d | -5.5698 | -44.323399 | 2024-10-30 00:07:18 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60aa74a4-fa4b-32a4-9ee7-5662d3ffc3d2 | -5.3063 | -43.405499 | 2024-10-30 00:07:19 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f4756a46-3ba1-380d-ad69-b288f635165f | -5.7635 | -45.538601 | 2024-10-30 00:07:20 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e1af415c-243b-31dd-ab2f-86028f7a45c1 | -5.7668 | -45.553699 | 2024-10-30 00:07:20 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e057d75c-96d6-35cd-99b0-fae7a87bee86 | -4.8844 | -42.613899 | 2024-10-30 00:07:23 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 37e1800b-79e4-3bc0-8b09-106b91970e74 | -4.8865 | -42.623299 | 2024-10-30 00:07:23 | METOP-C | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1c0a103b-6d62-3985-b4a1-56544e0735cc | -4.6195 | -41.522499 | 2024-10-30 00:07:24 | METOP-C | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4acbbc72-49c0-3040-a8ac-4752cc28d4a5 | -4.9555 | -43.163898 | 2024-10-30 00:07:24 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 87fcd738-3a93-3899-b7f2-dc5eeaef92d4 | -4.9578 | -43.174099 | 2024-10-30 00:07:24 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e404e058-adaa-3976-905e-954442faa604 | -4.96 | -43.184399 | 2024-10-30 00:07:24 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8513c1-ef84-3577-9cc5-98ac5ee8ee06 | -4.9457 | -43.1661 | 2024-10-30 00:07:24 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6fa812a6-183b-3833-9fb6-d13ace1f53b1 | -4.948 | -43.1763 | 2024-10-30 00:07:24 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 057ed37a-6f51-32b8-9085-b525151a49c2 | -4.9502 | -43.186501 | 2024-10-30 00:07:24 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e3da304-d840-32e2-b1bb-c4928862e0c1 | -5.4743 | -45.474701 | 2024-10-30 00:07:24 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b954095-e032-3d91-923c-ea50d09e2f2b | -5.4775 | -45.489601 | 2024-10-30 00:07:24 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f167dedf-4b76-3327-a649-c9f8ab13791b | -5.3119 | -44.9189 | 2024-10-30 00:07:25 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3dc7bdd-f56e-3107-ad2c-fd853c6e0b7c | -5.3149 | -44.9324 | 2024-10-30 00:07:25 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb5d8e0a-cd2b-3df4-a2f5-8462659ae2f7 | -5.2348 | -44.893299 | 2024-10-30 00:07:26 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b212789-da7a-3f8e-8009-fc27ee889406 | -5.0749 | -44.2127 | 2024-10-30 00:07:26 | METOP-C | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec89168d-6014-3e17-8a0a-0b99d5625533 | -4.5412 | -42.043701 | 2024-10-30 00:07:27 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2341cbfa-95bb-3a8f-8eaa-8f6392afd6a1 | -4.5431 | -42.052399 | 2024-10-30 00:07:27 | METOP-C | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 50ee6854-1965-3179-a644-61fd2cd63dba | -5.0207 | -44.3381 | 2024-10-30 00:07:27 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e42638c-dbb0-33f2-beb3-0729765e472c | -5.0234 | -44.3503 | 2024-10-30 00:07:27 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e62f5026-ce47-394a-826d-b34180b4a89e | -5.0261 | -44.362499 | 2024-10-30 00:07:27 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 03333d0f-567e-36c2-9668-3704eef48968 | -5.0109 | -44.340199 | 2024-10-30 00:07:28 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e9287ce-9c90-368a-b5bc-2da32d7a2523 | -5.0136 | -44.352402 | 2024-10-30 00:07:28 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fdb575f5-717d-30e9-a7d7-8af4c8e2af6e | -5.0163 | -44.364601 | 2024-10-30 00:07:28 | METOP-C | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be3d3ecd-0af2-38ea-bc2b-a0d2d0cd2482 | -4.5191 | -42.8634 | 2024-10-30 00:07:30 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 64d216ab-b2fe-360f-9196-476e78a06b25 | -4.5072 | -42.8559 | 2024-10-30 00:07:30 | METOP-C | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 79d1d984-9601-36fa-9b6c-f23bbafe6c6f | -4.5093 | -42.865501 | 2024-10-30 00:07:30 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47cf2fd7-5517-33c8-8446-40be3f1b17a1 | -4.5115 | -42.875198 | 2024-10-30 00:07:30 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acb3be19-bbad-3d56-be18-d8d891270de8 | -5.0649 | -45.143002 | 2024-10-30 00:07:30 | METOP-C | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1f2234-6237-3966-ac2b-ee677d375a55 | -4.6772 | -43.8036 | 2024-10-30 00:07:31 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 53a17bb7-f5e6-3445-9734-95217979f7d2 | -4.6674 | -43.805801 | 2024-10-30 00:07:31 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5d11a3-6de1-3e13-9241-c6778f89c309 | -3.8657 | -40.6917 | 2024-10-30 00:07:33 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 20edec54-4016-3aee-a70f-25a5ff780da5 | -3.8674 | -40.6991 | 2024-10-30 00:07:33 | METOP-C | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f81a4290-bc5d-390b-8efd-4a9124d7a1cf | -3.9115 | -41.030201 | 2024-10-30 00:07:33 | METOP-C | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7f5f402d-fd48-3070-b58a-a4d952a99520 | -3.9777 | -41.459499 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e64e8071-8de7-3d8b-bf34-8e0f021846b5 | -3.9795 | -41.467499 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 49b10164-b937-3562-ad40-86389b8c5952 | -3.9679 | -41.461601 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b93258b2-8581-3f18-853c-ee0af10d4354 | -3.9697 | -41.469601 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9311894-2ab4-30ec-9b1c-f97792969204 | -3.9715 | -41.4776 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6d54bf3d-cae8-3e69-b4f0-9a75cf1d0280 | -3.9581 | -41.463799 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1c91e215-866d-3567-93ee-d06df51c2c5f | -3.9599 | -41.471802 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3d277422-11fb-357c-9108-c3b1bf44620c | -3.9617 | -41.479801 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 609b1099-078f-3344-b12b-cf0636a187ea | -3.9635 | -41.487801 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 023a6f52-5680-3302-b956-541ae92016cc | -3.9653 | -41.4958 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 222e429b-4947-33b0-89ae-6f276ccb11de | -3.9483 | -41.4659 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 660551c7-41b2-3d0d-a9ef-af1d54fb8233 | -3.9501 | -41.4739 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0ccabd3d-4e01-316a-b181-f8433318145a | -3.9519 | -41.481899 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 58e9096e-c04c-36c8-849f-d5cc7029d9da | -3.9537 | -41.490002 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 562e423b-28d5-39b6-93df-ce3962858cc4 | -3.9555 | -41.498001 | 2024-10-30 00:07:34 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fc4e7bf1-bee0-373e-88e6-adb3d49b0cc1 | -4.6431 | -44.3433 | 2024-10-30 00:07:34 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf3b0ace-0470-3bee-942c-983af16375f9 | -4.6458 | -44.355301 | 2024-10-30 00:07:34 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 77c3f6d3-e549-380e-89fb-f588105984d6 | -4.6202 | -44.285599 | 2024-10-30 00:07:34 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab959a5-78c4-3cd1-8048-7819d471a34e | -4.6228 | -44.297501 | 2024-10-30 00:07:34 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2b06ab2-71b5-34af-b18d-bfcaaebf5b45 | -4.3379 | -43.614899 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 588befb8-a479-3089-b84d-2a20890be3ec | -4.3403 | -43.6255 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33d0df21-9bba-3020-b8c9-734efee8acd1 | -4.3498 | -43.6684 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f599e369-c801-3f6c-bdfd-45073ee695fa | -4.3691 | -43.7551 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| faf88904-053a-3f4f-9251-9f8b8ce5e132 | -4.3716 | -43.765999 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73f1106d-cd32-3efa-9dbc-a1418b1b20ca | -4.374 | -43.776901 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0143b7bc-d52e-3a4e-b84e-8c588e8c07d6 | -4.2859 | -43.4277 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d939ed8-c15d-33f1-b94a-9d746886880b | -4.2882 | -43.438 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd05440-63e0-371e-abde-9b35a3f89528 | -4.3593 | -43.757198 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3886a0b-e96f-3854-b5cc-9fc57f4db0e8 | -4.3618 | -43.768101 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a074052c-4eec-3154-aa52-13d4229829b9 | -4.3642 | -43.778999 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc170443-c03d-36b1-9f9c-3605506f0714 | -4.2738 | -43.419399 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c54e20ff-0126-3cab-b602-aa3d65793492 | -4.2762 | -43.429798 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8fd108b-69e1-3431-8c77-fa05216af71e | -4.2785 | -43.440102 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 716257e7-f1db-390a-b19a-9fc647d1d50b | -4.2808 | -43.4505 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e2f2d3a3-02ce-3709-9b69-397a55612cfa | -4.3496 | -43.7593 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d324a453-b68f-3ed9-aa49-240c81bcc91a | -4.352 | -43.770199 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b6e3c845-09cf-35a5-bf3e-a4429e6f2988 | -4.3544 | -43.781101 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a2984c9c-4c39-35fd-a09f-61fa953b9f27 | -4.2664 | -43.431999 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 129f9a65-6027-3069-b57a-09e2e02709d4 | -4.2687 | -43.442299 | 2024-10-30 00:07:36 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 781be53c-11f9-39d8-9bf3-91ea242b163b | -4.1536 | -43.065399 | 2024-10-30 00:07:37 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73e3623f-9630-3772-a363-1702ed9dafb9 | -4.1558 | -43.075199 | 2024-10-30 00:07:37 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9b3bb468-159c-3e18-9279-ca0bdc3b722e | -3.8133 | -41.596901 | 2024-10-30 00:07:37 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f8891783-a743-3f59-a737-c420c57e932b | -3.8016 | -41.591099 | 2024-10-30 00:07:37 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eb284f28-985d-3c97-8059-4154f9217f95 | -3.8035 | -41.599098 | 2024-10-30 00:07:37 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e8b96787-7e7a-3006-9c1e-07a9a0a62ab5 | -3.8053 | -41.607201 | 2024-10-30 00:07:37 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e06e0333-7fa9-3ff1-baf8-31f458b00952 | -5.2388 | -47.9058 | 2024-10-30 00:07:37 | METOP-C | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3e22a4e-3ca0-3d2e-9e8e-ef040f3b76d4 | -5.2435 | -47.927601 | 2024-10-30 00:07:37 | METOP-C | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README4.md)
