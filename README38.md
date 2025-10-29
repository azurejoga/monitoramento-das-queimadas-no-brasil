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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b3ec435-cde4-3b8c-96a0-f3a17a71159d | -6.29361 | -41.88172 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2cdec6e5-f54f-3393-ba0f-229773bd1567 | -7.00045 | -42.79292 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d887fbb1-d5b9-32d9-8b81-64e1b1e2f391 | -7.64427 | -46.91861 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 712a85df-4ba1-3b76-98d5-c5a54d0cf567 | -6.17015 | -41.66876 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e62393c4-6305-3e79-975c-cb3bcdac175f | -7.95732 | -45.45113 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 470c3a80-d34c-3c53-b27f-d3c460726563 | -9.09671 | -47.81942 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8b3b459-94cc-3f87-8159-137eaf6a2332 | -7.81572 | -46.41876 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76d7c7d-9703-3a0c-b425-0e0d45e1267e | -5.48267 | -46.43981 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec23a79d-69d6-393d-9c1d-5a2204098668 | -6.15753 | -41.82496 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a9fb094-1194-3b53-9454-41ea0d7d9d8a | -11.26239 | -45.52147 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7ad2a24-982d-3140-982f-470bcfa5bd0a | -7.30875 | -46.31525 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d1bc550f-6898-31a6-b087-90dcb3f7638e | -7.78943 | -46.47393 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36060a30-cbed-34a7-923e-5d4030eaa33f | -9.44544 | -46.88914 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d85ae7f-a934-3f7f-9da5-23078f91b304 | -7.07429 | -44.92119 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c131eab5-6c54-30ce-a9cd-e1e9494ab63e | -7.33739 | -42.47297 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4b71e192-54e0-34ea-aedd-2b31f27cc1ee | -10.75224 | -44.75439 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dfaeac7-c2b0-3d48-9ef7-c169f5c31e4c | -7.28202 | -44.09964 | 2025-10-29 04:23:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 469be1a8-0ef0-3450-a769-594263c2e37e | -9.89194 | -47.44763 | 2025-10-29 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff204977-5036-3336-9550-ff677c980f5d | -9.73494 | -44.06104 | 2025-10-29 04:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5a2286d5-ada1-3789-8d8e-23f492ac7a07 | -8.22049 | -50.47967 | 2025-10-29 04:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7c70152-7476-3363-a484-d26959d34507 | -7.85247 | -44.22871 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5941d8e1-ba82-3f03-b3f4-d1ce6e5cc7a8 | -7.42223 | -45.98116 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f52c7312-d652-321e-8e4e-74654ec6f58f | -9.54483 | -46.92388 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b0eb850a-00de-3f88-a001-a3f3d1cd85b9 | -7.28406 | -46.89514 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 412aa2be-1798-34e6-8c4e-b9a8f668de0d | -10.91821 | -47.60676 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e11f5e0d-4b60-3de6-927d-a30fdb723ccc | -8.32486 | -45.37764 | 2025-10-29 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 384c6909-f7d5-3a21-ac14-1010f87494e6 | -9.90097 | -44.90729 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b32dd1d4-11da-340d-86b9-5fa9e5c8f203 | -10.83788 | -44.42081 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 547e1f59-d56f-3e3c-ab7b-7a472231b169 | -10.20995 | -45.95302 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a60d2124-fbb8-35ac-bea7-76efff37587d | -5.71118 | -49.30835 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26606c71-6057-3afa-a563-6c58082f13de | -6.11632 | -42.44533 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a57f8f97-d2dc-3599-9991-b69974b5d1ef | -10.94269 | -48.03293 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76c8beea-22bd-39be-ad1a-c8a1fbd090da | -5.10128 | -46.1826 | 2025-10-29 04:23:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd49891a-8324-36eb-997e-972661ad634e | -10.36863 | -44.27031 | 2025-10-29 04:23:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e71843-cff0-3292-8c7f-3a67e2c22bf7 | -8.5532 | -45.68534 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bff6e14-4ea2-3e8f-b286-29eda191fd4a | -9.09321 | -47.81882 | 2025-10-29 04:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79cf571c-d9ee-3381-80af-0647b5e97f17 | -7.96973 | -46.71981 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5a16964-ab01-3c28-8e29-f6f7b191bd8d | -10.33097 | -47.22148 | 2025-10-29 04:23:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc50c211-ef70-3edb-99af-2da5dc8ef8d8 | -7.81631 | -46.41514 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af87e4c9-4365-3b2c-b20e-331e2e53bdcb | -9.58092 | -46.9373 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fae164e-8a22-3131-9651-1449c737f10f | -6.60492 | -44.6368 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 572023a2-9900-3dfa-b759-691040e02374 | -10.92689 | -47.59665 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3dc98531-e794-389f-94af-bb2ca3ea5cb3 | -10.57054 | -49.8402 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d575ab36-b68f-3a47-9c1a-dfab037eb225 | -8.51165 | -47.19872 | 2025-10-29 04:23:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00bff4a5-a26d-377e-8cdd-4bfa072d1f1b | -7.85582 | -44.22924 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1062b142-5170-3e81-8d93-5b233dab3f3c | -5.97695 | -46.31993 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a312ea66-0830-3d48-942b-cee6696aad84 | -5.56441 | -46.36501 | 2025-10-29 04:23:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd3f1ffb-637e-3487-a40e-888c7389496f | -8.01079 | -46.2033 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63347458-a9a8-384a-9b6f-eaec3b1550bc | -6.16771 | -43.75666 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7547e14b-557c-3420-9a6b-3f2566d1b446 | -8.0007 | -46.20172 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f36e1df2-b188-391c-884b-e51495a1b134 | -10.87053 | -44.41098 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4f065cb-bdab-3389-93e1-c3420413e1e3 | -10.92629 | -47.60037 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44d317f2-1d6a-3b11-9c7a-c554fdb3b809 | -10.43259 | -45.05282 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acb0d802-e605-3fd6-b5df-25ff9d3180a8 | -8.19399 | -44.44812 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2d80ed1-da2c-3ee2-9b0a-0ab326e0f2e3 | -5.80878 | -43.03136 | 2025-10-29 04:23:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0ae1cf1f-f585-3c5d-a32b-f673b9050422 | -10.22431 | -47.5518 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4de21622-054f-300f-989e-8c164f319cbb | -8.55428 | -45.69991 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 847cb9b8-a04b-30fd-8240-01d3542947b8 | -7.07541 | -44.93562 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| afdf8d1e-08ef-3021-8e88-526a16b534f7 | -6.73585 | -48.0662 | 2025-10-29 04:23:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac870e05-4060-3ebe-a1b6-de34ce456739 | -6.67429 | -44.69048 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f5cab20-48e1-348d-bae8-67dad07b2828 | -6.4604 | -43.55465 | 2025-10-29 04:23:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14055df3-2291-3c28-83b8-aa3951b68275 | -8.52235 | -44.09658 | 2025-10-29 04:23:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c770889b-efdf-3231-99a0-53510afc126c | -10.93739 | -47.80685 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c59fb353-f041-3cee-b92e-a199180ac1f5 | -10.50407 | -47.72088 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97b0a2f7-7d90-36dc-b416-d061fc8a16e3 | -6.79254 | -48.6199 | 2025-10-29 04:23:00 | NPP-375D | ARAGUANÃ | TOCANTINS | Brasil | 1702158 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d634f17-f9ff-3bfa-988a-2d64ab33473b | -10.61528 | -47.89545 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f46a0a7-997b-3c11-8d1e-29a3a6a62148 | -7.96213 | -46.74497 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c7fffcc-7567-3251-b171-82c5462f9627 | -5.33555 | -45.43499 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52580f62-05d5-3274-8c3f-9757bae1576a | -7.06767 | -44.94151 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 47ac81b9-0ac0-37b2-9b8e-56d844fc6f73 | -9.96102 | -47.13457 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3a4634ec-6882-3a52-bb31-7135e1754eb4 | -6.10005 | -42.45853 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 14ac0b85-6e7e-333b-9fa9-08cc7e835175 | -10.70492 | -48.0094 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ad126d0-09b3-3eea-9670-64b4658517df | -6.10789 | -41.73211 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6f4f3974-7d87-3560-b671-53c6cbf71d92 | -11.11202 | -44.01725 | 2025-10-29 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c27b8c37-8531-3e30-9d56-41a426a22627 | -7.12705 | -46.9866 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11643d7a-8cb5-39c9-97d2-bc138f6b2041 | -5.33679 | -45.54417 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24ca28cc-6a24-3672-af63-1efeba692f6c | -8.54931 | -45.68832 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 039585d3-6cc4-377a-acfb-cdc6fb4ba93c | -10.87109 | -44.40734 | 2025-10-29 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d56b4b9-71b4-3550-8ef2-a39050c77647 | -7.286 | -44.97291 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f7004d8-54b7-3256-95a1-42353e32179a | -9.26597 | -46.26999 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ba0a33d-d91b-3a8f-a7fe-87a3d4e0e918 | -10.90685 | -47.8063 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8ca2d96-3881-3646-8e90-3ed419926ac5 | -7.70158 | -46.90469 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f77ad1a-4c4a-3935-8aa5-cc97ed4c0ffc | -7.44979 | -47.15927 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64df2683-76a9-3147-a2e9-2f9d493cf89f | -7.80237 | -46.47977 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a7f2562-6374-37b6-ace1-9206e957e6aa | -8.00406 | -46.20224 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e342856-2bb4-342b-bb2d-cca861db9731 | -6.20473 | -43.26598 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9bbf4916-f924-389a-b5ee-a8f570a34637 | -5.33959 | -45.54822 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3dc89ac6-68ec-3e94-8390-f730e2a0adef | -10.87882 | -45.07653 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f80eb7c-3f7d-3bed-8145-b7e5c2976d0e | -8.00234 | -46.21303 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 87389a6f-9717-335c-b464-872e9ba1ae32 | -6.16491 | -43.75262 | 2025-10-29 04:23:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| ff73f850-6515-3602-8c79-c42117a77df1 | -10.62334 | -47.97627 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a18ac789-7302-373d-93ac-8e3da65b3574 | -10.77046 | -44.08411 | 2025-10-29 04:23:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04149107-3bca-308c-ae0e-079fb8897d6e | -7.40753 | -47.17192 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3b750b8-bf9f-3983-a7c0-841ed83bef3c | -8.54686 | -45.68836 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e410b400-e63d-34e9-a780-fbad52f887a9 | -7.76701 | -46.52626 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9c472af-5d75-3758-a5ca-fc62380e7bfe | -9.48924 | -47.00525 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 8bbee8d9-f41c-3660-ad03-ab508743cbde | -5.18979 | -45.62613 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c74a63c-e065-3990-9b73-9d26dd1ab266 | -7.90386 | -45.67912 | 2025-10-29 04:23:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1549f97-b3bd-3e0b-8a7a-35ca666d9c79 | -9.50934 | -46.51777 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cc8e690-99db-39c5-9863-6edf5f73160c | -4.60025 | -48.78739 | 2025-10-29 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
