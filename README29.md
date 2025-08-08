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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57af4197-6ce5-3132-b457-a85778b8ef80 | -7.9106 | -45.3329 | 2025-08-08 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 18f49cbe-f0f5-3837-9a03-cb1561975710 | -12.5714 | -47.1584 | 2025-08-08 12:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| fac582a9-dc6c-304b-8a7e-b45920cbe724 | -18.8445 | -47.0483 | 2025-08-08 12:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ce517cd4-245f-3130-8b83-54a5a8c72b67 | -7.8915 | -45.3575 | 2025-08-08 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 255.4 |
| 2e363c30-efb0-3c73-9394-bd76501b680b | -12.5337 | -47.1189 | 2025-08-08 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| f2ba6f67-d690-3fba-a556-796c77369f9b | -7.2415 | -44.6667 | 2025-08-08 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| fc2aa761-e2d0-3492-bda9-c720129a5d1d | -7.2603 | -44.665 | 2025-08-08 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 8b700537-91dd-34c9-99d7-3ff2204d36c8 | -7.8918 | -45.3348 | 2025-08-08 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 6d20241e-a467-30e0-8662-d149721b0eff | -12.5526 | -47.1387 | 2025-08-08 12:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5224afad-f17a-3ce2-bc16-de6b0c6200ef | -7.9106 | -45.3329 | 2025-08-08 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 201.9 |
| f74e8ea5-977c-3ffa-8843-3385747c0dea | -8.0492 | -46.3335 | 2025-08-08 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 60d12c98-dc7d-31e8-b2af-83c04828518e | -18.8445 | -47.0483 | 2025-08-08 12:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d1d096f7-40de-3858-8ca2-b9ce1dfea304 | -7.9104 | -45.3557 | 2025-08-08 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 346778b0-9f8a-3a44-85ad-f7a3484d0635 | -7.2229 | -44.6455 | 2025-08-08 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c6a60724-409a-39fa-8d2d-ad9f0626f602 | -7.2603 | -44.665 | 2025-08-08 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6e959324-de76-3579-b1e3-58afb7e14556 | -12.0972 | -44.7403 | 2025-08-08 13:00:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 051662bb-46f9-339f-9eab-5606485ad379 | -12.5341 | -47.0964 | 2025-08-08 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| bab46c89-adab-337e-8a1d-e55227119e48 | -7.9295 | -45.3311 | 2025-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.0 |
| c5d7e8dd-f5b8-3f4c-b83b-0799973e4c1c | -7.2415 | -44.6667 | 2025-08-08 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 5162b1e0-1676-32d3-953d-18fd6fd2353d | -18.8445 | -47.0483 | 2025-08-08 13:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 30ddbc6d-895e-3891-bcc0-9786658b6567 | -12.5337 | -47.1189 | 2025-08-08 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 129.6 |
| b2635f6e-c2dc-3ae7-aa90-f808c79f8ff6 | -7.8918 | -45.3348 | 2025-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 82bf434e-2bd2-33ec-816a-7dc0cfeba519 | -7.9106 | -45.3329 | 2025-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| d2bd9fbb-60ab-3ba9-98c6-2c45ba49b1d8 | -7.8915 | -45.3575 | 2025-08-08 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 357626c3-0a14-3a27-b5ae-ba2b382afef1 | -12.5333 | -47.1414 | 2025-08-08 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| e88eff9b-6336-3fb7-9d12-c7e958eac273 | -12.5526 | -47.1387 | 2025-08-08 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 35071376-ecd1-3155-86f8-a50ab1e9e244 | -7.2229 | -44.6455 | 2025-08-08 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c7da08c0-c048-35fd-acd8-ba3f4d85403c | -7.8918 | -45.3348 | 2025-08-08 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 217.4 |
| 5f1bc632-590e-32e9-bd0a-dbd7c1e3f708 | -7.2415 | -44.6667 | 2025-08-08 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 96f154a0-9a5f-3fde-9284-1bb19b48b8af | -7.2417 | -44.6438 | 2025-08-08 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 8939ec95-bb3c-3ace-928e-76f3acd60888 | -12.5526 | -47.1387 | 2025-08-08 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| d8ef3900-93ec-312a-9660-575f9f854282 | -7.8915 | -45.3575 | 2025-08-08 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 229.9 |
| 4e43378c-b298-3275-9724-c2ded74c61d8 | -12.5341 | -47.0964 | 2025-08-08 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 011d998b-779a-3f77-951f-e36a0c667f6d | -12.0976 | -44.717 | 2025-08-08 13:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 247be8c1-5b47-354f-9ec9-82c8fb6e21d7 | -7.2603 | -44.665 | 2025-08-08 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e1dc1de4-b64f-3d8b-b77d-6003c5c16331 | -18.8445 | -47.0483 | 2025-08-08 13:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7ada1e22-c08e-38e7-9a24-c583187e7e14 | -7.2229 | -44.6455 | 2025-08-08 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 58ffae5a-0979-3ec0-84b8-520667ffd33f | -7.9106 | -45.3329 | 2025-08-08 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 229.9 |
| e1da4e59-5e51-30a8-a6ef-e3f9b4fee630 | -7.9295 | -45.3311 | 2025-08-08 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9e30a244-a886-3902-b85e-60adf357c307 | -12.0972 | -44.7403 | 2025-08-08 13:10:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| c4398366-38b8-34bd-a300-82d927a3f484 | -6.2789 | -45.2716 | 2025-08-08 13:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 48934fa5-b70c-3ddf-8693-348fca1c0ec5 | -12.5337 | -47.1189 | 2025-08-08 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 133.8 |
| 9234bdc0-e5a4-3d18-9f47-73772a12639f | -7.8915 | -45.3575 | 2025-08-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 928.9 |
| 21e9a8d2-f220-3e3b-af75-1544f70e1472 | -12.0976 | -44.717 | 2025-08-08 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| a485237f-37ce-34e8-84ef-dfcc54abd6d7 | -12.0972 | -44.7403 | 2025-08-08 13:20:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 7d3f53d2-0dda-3ae2-a064-3fed608bdac0 | -7.2415 | -44.6667 | 2025-08-08 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f4e4601c-1a40-30c5-a512-d53aaa129f45 | -18.8445 | -47.0483 | 2025-08-08 13:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8da4fc2d-e048-3dd4-8e97-4e887ff2ef37 | -7.2417 | -44.6438 | 2025-08-08 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 0a1ce4e0-2194-312d-8ecc-e4081fb3e906 | -7.9295 | -45.3311 | 2025-08-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c0ee8bee-add2-3219-8728-87123a613203 | -6.2789 | -45.2716 | 2025-08-08 13:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3a463531-a092-3724-b386-8099df94dc19 | -7.2229 | -44.6455 | 2025-08-08 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| ba7bcbc2-8853-34f8-b28e-d0bef27a2060 | -7.8918 | -45.3348 | 2025-08-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 304.0 |
| 52aa54fe-f8dd-3981-875c-13e85a8fe21c | -3.2009 | -41.844 | 2025-08-08 13:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 89a231cd-f976-3050-b149-fddcccbe0d9f | -7.9106 | -45.3329 | 2025-08-08 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 289.8 |
| 899357b1-f032-3d30-80d1-90739d2f8f40 | -7.2603 | -44.665 | 2025-08-08 13:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 7be5577b-6fa2-382e-b805-4bcfcb1f7d99 | -3.2196 | -41.8431 | 2025-08-08 13:20:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d7ef53fd-59ae-365a-8b51-521ab5cb5f3d | -3.8943 | -41.6177 | 2025-08-08 13:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| c2c2b7d6-3c24-3305-b9c7-4d9fa58cfb9f | -7.2603 | -44.665 | 2025-08-08 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b08bd4c9-5408-396f-adb5-1103b253d45f | -6.2789 | -45.2716 | 2025-08-08 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8d156add-822a-30d7-bb9b-d2e41937e800 | -3.2196 | -41.8431 | 2025-08-08 13:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 5b8ed6d9-3f56-3609-80d3-9c0eb4e6e066 | -12.0972 | -44.7403 | 2025-08-08 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 5c936a2b-44fc-340f-92db-cd4e0ac9732c | -11.7862 | -44.9726 | 2025-08-08 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 38402e83-4837-3625-9428-c351b28a8248 | -18.8445 | -47.0483 | 2025-08-08 13:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ea9f5b06-7793-3e6c-898b-6e3ec5d515ae | -7.9297 | -45.3084 | 2025-08-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a1991b97-49fd-3a5c-b5e8-9dff9c2ba42b | -7.9106 | -45.3329 | 2025-08-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 510.9 |
| 7810d102-236c-3c95-8c66-57bbe963df44 | -7.2415 | -44.6667 | 2025-08-08 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f4c839d7-b339-3d30-87bc-35ab1a1a33f5 | -11.7866 | -44.9494 | 2025-08-08 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 20e48cb1-9e35-3fcc-9c64-2b287a621ef2 | -7.8918 | -45.3348 | 2025-08-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 293.0 |
| cb72692b-f62c-3ad2-9fd4-1f7df4229c94 | -7.2417 | -44.6438 | 2025-08-08 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d082d45a-df96-314e-8c0e-9fd64e826f04 | -12.0976 | -44.717 | 2025-08-08 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 54ccf156-50cd-3a17-916d-012fd8b2f3e8 | -7.9295 | -45.3311 | 2025-08-08 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 206.3 |
| c73f0ab7-9b43-38b0-b7e1-5f13392ecec3 | -3.2009 | -41.844 | 2025-08-08 13:30:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d1033029-9137-3112-b94d-bfb7e96c0c4c | -7.2229 | -44.6455 | 2025-08-08 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 8412eba0-336a-3e86-aeba-1df1311cffe1 | -5.7675 | -43.893 | 2025-08-08 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 979db2bb-fc2e-3299-946d-8570b1f4a350 | -12.5526 | -47.1387 | 2025-08-08 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 328483dc-6f71-39a8-98df-0dc70d91cc65 | -7.9297 | -45.3084 | 2025-08-08 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 83aba379-468a-36b3-920a-acd92b985014 | -6.2789 | -45.2716 | 2025-08-08 13:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 843d2b82-78d5-3f45-be2f-5b13117542a3 | -14.3674 | -51.098 | 2025-08-08 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| d706e2f8-cc7e-3cc4-b55a-7ac25e6376c2 | -12.5341 | -47.0964 | 2025-08-08 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| b923d331-5517-3d66-bb34-42ee650eb656 | -7.8918 | -45.3348 | 2025-08-08 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 151.8 |
| da98992a-cc1e-3ffb-8a47-c575d03df16a | -6.5966 | -45.337 | 2025-08-08 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1fdfe169-8d34-32ea-abac-3f0823a23d9a | -12.5337 | -47.1189 | 2025-08-08 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 303.7 |
| 8ac4e05e-94a9-382b-bae4-a0dae3f62335 | -12.5333 | -47.1414 | 2025-08-08 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 176.8 |
| ac4755fd-ff0a-353f-89ed-ad5b4cfb14ea | -7.2417 | -44.6438 | 2025-08-08 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 86f52c9f-74a5-3b1c-a29b-be62e827ead0 | -7.2415 | -44.6667 | 2025-08-08 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1e8821cb-a2ca-3fc8-8116-594eac69cbd0 | -7.9295 | -45.3311 | 2025-08-08 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 340.5 |
| ac8a43df-adde-3e54-8311-4b1c9ac2d1f5 | -14.3481 | -51.1007 | 2025-08-08 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 78065294-4682-3d82-b7a2-feee11c8e897 | -7.9106 | -45.3329 | 2025-08-08 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 486.1 |
| 1264cfdb-5b41-3059-9093-105f7aac8413 | -7.2603 | -44.665 | 2025-08-08 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a49ddc81-1a72-3fc9-a197-ae1d5f861440 | -11.7862 | -44.9726 | 2025-08-08 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 70a4b4cc-5e7c-3d1c-929c-535da11fd836 | -7.3731 | -44.6546 | 2025-08-08 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.9 |
| eea7c0a9-12fa-367a-abaa-391547adf748 | -12.0972 | -44.7403 | 2025-08-08 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5755e44b-7b17-308a-b045-0603ccab95ad | -11.7866 | -44.9494 | 2025-08-08 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 2483f38d-266b-38cb-9a29-5c53b8d96fba | -7.2415 | -44.6667 | 2025-08-08 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| aa3e35cf-3090-3522-93ba-de7149e63617 | -7.2417 | -44.6438 | 2025-08-08 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 180390ac-8768-305d-bb29-4801c1478339 | -3.2009 | -41.844 | 2025-08-08 13:50:00 | GOES-19 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 9b756ec7-f61a-3066-b37b-dcdfb87f958f | -6.6151 | -45.3581 | 2025-08-08 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| f47d9ac4-fc31-3266-81df-df273e91ecbb | -7.2603 | -44.665 | 2025-08-08 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5afc40b4-1eb5-3f37-8fc9-8fb8bcc08180 | -12.0976 | -44.717 | 2025-08-08 13:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| e23a6734-064e-3589-97fd-efcb65e4fc48 | -7.2227 | -44.6685 | 2025-08-08 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |


[Clique aqui para ver as próximas entradas](README30.md)
