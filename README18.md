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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d3413b7-970b-349f-a9e6-498b67adcf0a | -3.49353 | -50.45914 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dc5a3594-3c2d-3b5a-b859-b5384194cdb1 | -2.72049 | -48.34665 | 2025-11-05 04:12:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 32e756fe-191f-3bcf-9119-8cdc99e07592 | -4.29562 | -43.79119 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5b400df-86b8-3df7-a845-bf36f2fdc879 | -4.46928 | -43.23362 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7fba9c3b-6f88-3e22-b84a-288004109ca8 | -3.4754 | -43.62975 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29d166e4-9b9f-3db6-86e3-bc4782bcb0ba | -5.53359 | -41.09029 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cf61f4b2-b048-353d-852a-550b38ffdb2b | -4.19987 | -46.31104 | 2025-11-05 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4bea0db-f124-3418-8628-905929d27c13 | -5.51315 | -41.15446 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c1dc5b18-9106-3da1-b480-d58c6f1446c1 | -2.65314 | -48.51275 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 555658d2-5894-37ec-925b-f24369a08fbd | -3.58256 | -50.17004 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d6a290a-a1bd-3cc7-923d-670748e3be48 | -1.95816 | -47.51316 | 2025-11-05 04:12:00 | NOAA-20 | MÃE DO RIO | PARÁ | Brasil | 1504059 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20aa9d4f-d288-3904-821c-1cdd8a1b04ca | -4.91591 | -46.72408 | 2025-11-05 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11b58f23-c705-384c-999a-a89508c25e0a | -3.23544 | -50.79922 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6ded1674-4291-37a6-8ccf-08489506a950 | -4.57211 | -43.33557 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a356577-c143-303a-ade8-823c188e96f3 | -3.22616 | -44.40239 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ebaf47c-e17a-3db4-b678-cace89cb40a8 | -4.11169 | -43.88291 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92dacf6a-5619-34a3-a3ef-05018116c2fc | -3.9887 | -48.00383 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e254330-0719-3248-a411-59ee0b4642bf | -5.05469 | -45.82825 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a55afeef-a895-3329-8473-354616af9cac | -2.72506 | -47.38541 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59e80979-7af6-3b35-b229-1d9ba7e26fb3 | -3.44087 | -50.22227 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebb3c163-64a7-3bd7-870b-e1e17a9a653d | -3.48714 | -43.6207 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 618a79fa-056c-32d9-b34c-058ae68387cf | -3.33215 | -44.35409 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bf9d9d7-ab35-314f-b233-18677eb25071 | -4.66134 | -44.53001 | 2025-11-05 04:12:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6443465-85c3-3615-8db6-48c543321654 | -3.47763 | -43.63736 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7bb68fc-13ee-35b6-a301-15baca98b649 | -5.03981 | -43.62031 | 2025-11-05 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0fbcce3-fc3e-36bc-b43f-a75fd0de0b51 | -4.11307 | -48.02185 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3e60e92e-85b5-3923-a3a5-dc6ccf1f17e7 | -1.02617 | -47.06111 | 2025-11-05 04:12:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fd0e902-3b1a-3485-97ac-27df09d91f55 | -4.10426 | -38.32027 | 2025-11-05 04:12:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bb5df0c7-b73b-3255-89f2-9c40380056d4 | -4.55253 | -46.76201 | 2025-11-05 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c8686ce1-98b2-307d-acd1-96763f5ba1b0 | -4.56894 | -44.20856 | 2025-11-05 04:12:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23587e1f-1846-3de7-b3c0-b60f8ecb90f9 | -5.64286 | -43.29233 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d32a075-ca86-3557-8ee2-8243ef36aedb | -3.86662 | -44.43283 | 2025-11-05 04:12:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab83c1e4-fb9c-393f-ac1d-d8a956c36dc0 | -2.98227 | -48.70672 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e8c573db-c1d0-31dd-8d0b-70610fadc6eb | -4.25296 | -48.584 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b7d759b-f665-35f2-9158-ea0ce083c067 | -3.43721 | -50.24397 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 811277ae-fb28-363e-a898-5091c49a0b29 | -4.28748 | -45.66232 | 2025-11-05 04:12:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 777a633a-3296-315b-9eff-590473316b34 | -1.25676 | -49.14659 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6c9988a8-c966-3fb6-888f-31320c261c18 | -6.45946 | -39.85528 | 2025-11-05 04:12:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d23d04d-67d3-34b7-842b-2e1cd545da6d | -2.82977 | -49.40951 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a54159ee-7224-3db6-971c-4341e8c281b0 | -3.4707 | -43.33661 | 2025-11-05 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6adf9a47-f9ad-30e9-90b8-86a5e5e150be | -4.8584 | -44.61405 | 2025-11-05 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ae7daa-dd1d-3071-a7d4-d2e9e44af7ce | -3.96319 | -43.78622 | 2025-11-05 04:12:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 50c29035-223d-362a-9883-e656c323719f | -2.84838 | -49.41268 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9800b84b-3d68-3e0c-bb37-2739c95388b5 | -4.95442 | -45.08433 | 2025-11-05 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01460c4d-5b63-395f-a4a4-1ee8efd74def | -3.23445 | -46.87535 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2b2665a0-2a12-3644-8500-e18ba9c3925e | -3.47932 | -43.62673 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5c53bc4-8ecd-3f9c-bb52-bfd69329971d | -4.10477 | -48.02044 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b6358e95-a6f0-35e7-ac47-5485698dcce3 | -5.25702 | -44.77515 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9474e0f1-c3c3-32b1-aa11-3f53b37937b1 | -4.10046 | -47.28528 | 2025-11-05 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9416f868-53bc-34e9-a9ed-55156af71236 | -3.33498 | -44.35835 | 2025-11-05 04:12:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21c1c58a-c321-3e57-a708-f1170632a0f5 | -2.72794 | -47.39336 | 2025-11-05 04:12:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93ae5a77-cf15-3292-8469-1bcf95541d17 | -6.03836 | -41.04579 | 2025-11-05 04:12:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a17ae8e-bfc6-3a5c-9786-faf1c26c44ce | -4.76491 | -42.65514 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 569e83b4-3b80-361c-8ec8-b4fe1444da46 | -4.94109 | -45.65548 | 2025-11-05 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c11920b8-5495-3785-8168-277f0f2fe90e | -4.58483 | -43.34113 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 653eed03-c693-31f7-accc-5100f760234c | -4.86427 | -42.54021 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1df81e58-df1a-3db3-bde9-dd981c0738fd | -5.77738 | -40.80758 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b31d1c37-1ecf-39f0-b742-07ca04b5578b | -3.22891 | -43.44578 | 2025-11-05 04:12:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| bee138d1-12c5-3b39-887a-c0479a4a2bbb | -5.43036 | -44.65794 | 2025-11-05 04:12:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4efda79-4e15-3819-865d-9ca2cfbafb4d | -2.61507 | -49.23457 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbaebfbd-72d7-34e4-9989-029afd06d65f | -5.37478 | -44.74013 | 2025-11-05 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 67822c8f-b64e-3271-a5b8-0e5f4b6e2716 | -6.16861 | -41.65264 | 2025-11-05 04:12:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fb325d42-fb07-34f4-889f-b3f5ebffd21f | -2.48375 | -55.72795 | 2025-11-05 04:12:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c4e41e5-1b93-3682-a9c2-b9f51b69d6bd | -3.70205 | -49.56747 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8d7b34e2-53ee-3faa-a028-487c3f19ea42 | -3.47386 | -42.86712 | 2025-11-05 04:12:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d19c552-b30c-3130-b115-4608632b7038 | -1.27552 | -49.14965 | 2025-11-05 04:12:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b9915d08-a611-37ef-aa80-bdd0bae5dc82 | -4.10707 | -48.02158 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| edb279e5-1194-3cdc-871d-a87ce2cc8785 | -5.78588 | -40.82076 | 2025-11-05 04:12:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2adbbfd1-d59e-3407-8bf9-a48cd5b55ba1 | -3.23366 | -46.88017 | 2025-11-05 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4bbe6364-48ca-3a9f-a355-c2a65133b749 | -3.47706 | -43.64091 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c24a66e-1d09-30f2-bde7-ac50f28e34af | -5.45407 | -45.39988 | 2025-11-05 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 66d66740-cd39-3dc7-8453-67e1e0ba32b7 | -4.46099 | -43.22166 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c4f07f96-22f7-3393-82bc-60f6854c4fff | -3.49093 | -50.46964 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2e550939-edd7-39ee-9b21-7ac67d7c8627 | -3.48546 | -43.63132 | 2025-11-05 04:12:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc4790b4-8dee-32aa-a92c-c4fa7daa233a | -4.61727 | -45.35242 | 2025-11-05 04:12:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62085a6a-2f5b-32ce-9d95-53873444ddcb | -5.51371 | -41.15084 | 2025-11-05 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| d75156e0-c732-3f85-97bb-b0184599bf05 | -5.11215 | -43.14421 | 2025-11-05 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1cbfe6d4-99ba-3080-875b-125b87c95348 | -4.55768 | -45.79213 | 2025-11-05 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a08bd78-2d7e-3a34-a44a-370740ef60dd | -4.86373 | -42.54366 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7b2ba36a-6a2a-3386-8560-74e85003cfdc | -3.49253 | -50.46499 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f42438b8-d924-344e-9453-84242be6ac18 | -5.39297 | -41.2289 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fd56b1ef-e237-3d8e-b060-bb63b30a21a9 | -5.09248 | -44.70687 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fbcd448e-fb89-3dab-9cef-66cad2f5b1c9 | -5.47503 | -43.57843 | 2025-11-05 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 797adbdc-5004-3b76-ba7e-28f58b7a9418 | -4.29924 | -48.06796 | 2025-11-05 04:12:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 145c4d27-65e5-371f-825e-d2d4caf78bfa | -2.35027 | -48.48918 | 2025-11-05 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdd6733a-728a-38d4-a240-b9a40aba33a1 | -4.58538 | -43.33766 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb56ec5c-87dc-3f99-91cf-82a4abba2c24 | -3.67036 | -42.37673 | 2025-11-05 04:12:00 | NOAA-20 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f7138753-90d7-399a-9ec9-9b8c68cab79c | -5.24366 | -45.73974 | 2025-11-05 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02e9a87c-a6e3-371a-83ab-bc9538a2d6b6 | -3.4048 | -50.83902 | 2025-11-05 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf12b8d0-b362-34c6-adcc-b261d993a772 | -2.80797 | -49.14374 | 2025-11-05 04:12:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7fb1459-6e7c-306f-97ac-ae4e48730f57 | -6.09887 | -41.72576 | 2025-11-05 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 41e50580-e184-3d30-a1b0-a15dadc05f01 | -5.07278 | -41.21321 | 2025-11-05 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 096d1cc6-df9d-3ab0-8145-fb1b3fbdc229 | -2.83594 | -48.82924 | 2025-11-05 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 466d6241-f812-3cb5-9059-81d6d3b1f575 | -4.40811 | -48.95019 | 2025-11-05 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 10598c61-7f1f-3dbe-9e53-a5eae1d0799b | -3.24001 | -50.80313 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7b41291-4b0f-333b-acb5-04eda5270900 | -5.06433 | -44.73021 | 2025-11-05 04:12:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a63386e2-2705-374e-a5bf-b33c03f55ca8 | -2.78767 | -50.31437 | 2025-11-05 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 42352bfb-2f4b-384f-913b-cdc6d9a9a521 | -3.49762 | -49.55392 | 2025-11-05 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2e1af8c-ce1a-3c3c-85e7-0f7bd5222ba4 | -4.57156 | -43.33904 | 2025-11-05 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 072d227e-17dd-3ffa-a1d3-4a498083be2b | -4.76215 | -42.65118 | 2025-11-05 04:12:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |


[Clique aqui para ver as próximas entradas](README19.md)
