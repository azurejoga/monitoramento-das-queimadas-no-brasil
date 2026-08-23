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
| 0d39b913-d3a3-3252-a42c-1363d7f37caa | -10.8361 | -50.9691 | 2026-08-23 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2cf80773-5a9e-3313-a757-975454c909c9 | -16.0706 | -50.4332 | 2026-08-23 02:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 3f88187f-9999-3931-87a4-febe37592f8d | -5.7799 | -57.58 | 2026-08-23 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 295a35f3-1869-3b16-b57d-3e0eed7634b7 | -13.1889 | -51.4234 | 2026-08-23 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| db1b3d12-168f-3ae8-bdb8-986a82e5e674 | -13.1697 | -51.4258 | 2026-08-23 02:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7b3592a0-d23e-3a12-9415-92f8961b1315 | -6.9514 | -59.0666 | 2026-08-23 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 549c97d1-e632-37c6-bbe8-b84c37ff83c1 | -16.0706 | -50.4332 | 2026-08-23 03:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ba21a2b4-530e-330c-823c-3f7deca9fd3e | -6.8188 | -59.6696 | 2026-08-23 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| fa6494ee-1745-3d3b-a966-f034ba7b6e52 | -6.8061 | -58.6663 | 2026-08-23 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3bf5b304-9781-3fb9-97e3-d517947d406d | -10.8547 | -50.9884 | 2026-08-23 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| d99b683c-97ea-3b9b-ad2f-9222066bdd2d | -13.6806 | -51.8511 | 2026-08-23 03:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 6f47c075-e911-3a22-9576-bb14b2fe3118 | -6.1925 | -53.5231 | 2026-08-23 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f5e7ff0e-4d9c-31d7-b914-e4adcc7b857d | -21.454 | -46.1371 | 2026-08-23 03:00:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 83.8 |
| 82e11ec3-76b5-3a6a-805a-80ab6cab54ec | -13.1889 | -51.4234 | 2026-08-23 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| c6e83033-d84e-3c0e-86e3-206d1d5784c5 | -9.4582 | -40.3143 | 2026-08-23 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.8 |
| 20d9a2d0-f87d-31c6-a327-a3a95fd32072 | -13.1697 | -51.4258 | 2026-08-23 03:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 07488b8f-8cd0-3f23-aa9b-741ba01845dd | -6.8062 | -58.6469 | 2026-08-23 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| c434e042-ae15-3fe3-9aa8-bced9e5717da | -16.0509 | -50.4363 | 2026-08-23 03:00:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 1d27a943-bb20-3caa-b2ed-104fe21011c7 | -5.7799 | -57.58 | 2026-08-23 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| bc53777b-87aa-33f0-92ba-c561fb757866 | -10.8361 | -50.9691 | 2026-08-23 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7a775952-41fc-3b52-b609-3fecf4e5044c | -10.8358 | -50.9903 | 2026-08-23 03:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 112.3 |
| ca04b5fd-aa02-31e8-951d-49ba193827bf | -6.8027 | -62.9024 | 2026-08-23 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 9d41cd5b-ebcc-3143-b1de-35d9f8df47af | -6.9699 | -59.0658 | 2026-08-23 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 37d72284-d659-3c1f-9989-dc70603aea61 | -6.9513 | -59.0859 | 2026-08-23 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4f5246f4-aa0b-315d-8b7e-4d14957f591d | -6.8026 | -62.9212 | 2026-08-23 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| bb75c3d1-277d-3c0e-89b9-35a881cc8494 | -10.46103 | -37.14702 | 2026-08-23 03:04:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0a2dd146-0d55-3a31-8ad3-3cf716e871bd | -10.45403 | -37.14591 | 2026-08-23 03:04:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5505c6f5-a8b5-36e0-951b-e613bbc9894b | -10.45273 | -37.15225 | 2026-08-23 03:04:00 | NPP-375D | NOSSA SENHORA DAS DORES | SERGIPE | Brasil | 2804607 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e3e453ea-b0ef-3c0c-9de9-eabdf71f4c6c | -10.8361 | -50.9691 | 2026-08-23 03:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| ceae1a0b-5c3e-3c48-9c6a-006a309220ac | -13.1697 | -51.4258 | 2026-08-23 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 25a4a7c3-9bb9-389f-9ce7-69cc8a7950ca | -6.8062 | -58.6469 | 2026-08-23 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| bc432150-02b2-32cf-ac9a-7192842e3b36 | -6.8027 | -62.9024 | 2026-08-23 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 16179ccf-818e-3ff9-a3c1-d6f21d809dbd | -6.9513 | -59.0859 | 2026-08-23 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 53085699-2915-3f1e-aad2-4d834b36de95 | -6.1285 | -57.8393 | 2026-08-23 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 1ed3b9d8-38a6-3169-9062-d384f2c54157 | -12.7413 | -48.4036 | 2026-08-23 03:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5fff41fd-2860-388d-bff0-5cd42665ba19 | -13.6806 | -51.8511 | 2026-08-23 03:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 01236c7c-a32f-3a5d-bc55-de880c7a698e | -6.9699 | -59.0658 | 2026-08-23 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| f6197428-3750-3197-8c5a-19620873e8de | -6.1925 | -53.5231 | 2026-08-23 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| e7793ee5-b9a2-30f4-8cc9-c06986e72939 | -6.9514 | -59.0666 | 2026-08-23 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 3533223a-b30f-36fe-b2f4-98be48b7b157 | -16.0509 | -50.4363 | 2026-08-23 03:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| be3d88b5-cd33-36d9-b3b0-35624a627a97 | -6.8188 | -59.6696 | 2026-08-23 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bf963811-9155-3faa-8969-e5df9cb13727 | -16.0706 | -50.4332 | 2026-08-23 03:10:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b2d2a4a8-6c1f-3268-b506-f613d89ddbf7 | -6.8061 | -58.6663 | 2026-08-23 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 49d72eef-5c82-3a8e-9c8d-4793c1fdec8f | -6.8026 | -62.9212 | 2026-08-23 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 3c122e02-7f40-3ddf-9047-d8ddf50677f1 | -21.454 | -46.1371 | 2026-08-23 03:10:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 66.9 |
| f6af9395-96f1-3b47-ad86-2e1de029a11b | -5.7799 | -57.58 | 2026-08-23 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c6aa4347-2674-38c6-b962-22ac878b2adf | -6.1286 | -57.8198 | 2026-08-23 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b6b0994b-0c3a-3c1b-b6ca-e6e2d7586f53 | -12.7416 | -48.3815 | 2026-08-23 03:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| f0cb1094-03f3-36ad-8889-15f11a35e7d1 | -6.8027 | -62.9024 | 2026-08-23 03:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4b6d2653-4223-30df-bbe8-607201d54db9 | -6.6765 | -58.7492 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b753008a-626c-3fea-9e29-14e8662d593f | -6.9514 | -59.0666 | 2026-08-23 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 8e98a466-afd3-36fa-a91e-54751ba615a6 | -20.2752 | -48.6749 | 2026-08-23 03:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 025b85a6-e17d-30d6-b7f9-6ba7b5081caf | -20.2758 | -48.6518 | 2026-08-23 03:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 10826f19-05ca-334d-ab16-cb5f5b01e94e | -12.7605 | -48.401 | 2026-08-23 03:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 5dbfe5b4-e07b-39ac-a6e1-57ef7ba061ad | -20.2764 | -48.6287 | 2026-08-23 03:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 54.9 |
| ab757557-1353-3f8c-af77-4efb4ff89bcc | -9.7996 | -46.5977 | 2026-08-23 03:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 0891c0c9-5482-3685-9b01-daeb9be5f583 | -6.6766 | -58.7299 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 771b2bec-050f-3cb0-aab7-bee1ef13364f | -6.6581 | -58.7306 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 54205f1d-4605-3b9a-8b47-5e996afbceab | -9.7992 | -46.6201 | 2026-08-23 03:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c74636b3-1545-387e-9ec3-60ebaa7040ff | -6.7135 | -58.7283 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| fe6fa46b-9379-39ca-8ce3-83f34b0871e9 | -13.1697 | -51.4258 | 2026-08-23 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 085519df-f938-32c6-9b2b-c5955fec73af | -6.1101 | -57.84 | 2026-08-23 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 84a1db83-9eba-3d0a-a69c-ff24e4e73730 | -6.1285 | -57.8393 | 2026-08-23 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 071cc3ac-77d4-37ce-aa18-f552900627d3 | -16.0706 | -50.4332 | 2026-08-23 03:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 69.9 |
| b652663d-9dfb-3dfa-8844-f3db0dac4143 | -20.2554 | -48.6563 | 2026-08-23 03:20:00 | GOES-19 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 50.6 |
| f9863037-75b4-36ee-9a71-170c6fc0c71f | -6.6949 | -58.7485 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2e47eb4c-5347-302c-9646-f860a9487973 | -6.9513 | -59.0859 | 2026-08-23 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| dcb9c250-2bce-34a0-bed9-3a04c951fc05 | -6.8061 | -58.6663 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1373cfa4-7c08-3af0-ae39-e726c5469202 | -13.6806 | -51.8511 | 2026-08-23 03:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| b5d07537-3981-3471-bf24-00a03554191d | -21.454 | -46.1371 | 2026-08-23 03:20:00 | GOES-19 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.5 |
| 76c99a38-42d0-398d-a9af-8659037a704d | -6.1286 | -57.8198 | 2026-08-23 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 7e4f2c7b-c4be-3f67-96c8-8884ae3fa5e7 | -16.0509 | -50.4363 | 2026-08-23 03:20:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 50819a5e-9393-30f7-a829-dfe71e2d28b9 | -12.7413 | -48.4036 | 2026-08-23 03:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| f5cad01e-f034-328b-9ffa-91fb18a46b84 | -6.8188 | -59.6696 | 2026-08-23 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| fcbb77d6-1736-3622-b836-9543a9d42ee3 | -6.8062 | -58.6469 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f694b16e-d429-3231-b983-7a3d2396c0c4 | -6.695 | -58.7291 | 2026-08-23 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 85d6ead4-8422-378d-88ac-da1e3afdacc1 | -12.7416 | -48.3815 | 2026-08-23 03:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 7a73f899-5ab6-36d4-be97-6ca899a603f6 | -6.9699 | -59.0658 | 2026-08-23 03:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 9a150386-fb00-3706-99a2-49dcf7b3e0c0 | -6.1925 | -53.5231 | 2026-08-23 03:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 73c8cbbf-cb1a-3b1e-bb50-3d60d9da4463 | -5.7799 | -57.58 | 2026-08-23 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| cb082432-a415-35ac-96dc-16de109df2aa | -4.17145 | -42.44252 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a59dd122-53fd-3c5c-b0d7-ff2cc721d920 | -4.17586 | -42.44197 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc3cc0cb-5e2b-3dc6-81f4-6ff8be494187 | -4.16299 | -42.44844 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 603e0e94-d191-334c-bc9a-3e4ffc6b2441 | -4.17461 | -42.44907 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 57af9175-f21d-3548-902c-fe00e9a044fa | -6.47348 | -42.47614 | 2026-08-23 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bf10a41b-9aa3-3f15-92d5-ab03bb0f681d | -7.29765 | -43.00097 | 2026-08-23 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f49ea089-734f-3e37-8b72-ef1d1dc8e8d7 | -6.72557 | -39.27544 | 2026-08-23 03:21:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 939e0c32-4092-39c3-a527-4c10e60c01b7 | -6.46659 | -42.4747 | 2026-08-23 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 470450af-b1c9-31cc-a34e-822dd5713bf3 | -4.17015 | -42.44965 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8786cb6e-bc1d-3983-986a-e52dbcbdd36e | -7.99074 | -38.32841 | 2026-08-23 03:21:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d321eb47-0841-396c-8656-176ad4961e3d | -7.99019 | -38.33146 | 2026-08-23 03:21:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 826c0361-4bc7-3aa7-8e9b-d041f6f580c3 | -4.16746 | -42.44777 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5ec0f245-5c75-3bad-b12c-7fd787c0a436 | -4.1603 | -42.44654 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d89c3f31-436e-3020-b6f7-28798fbf04e8 | -4.16871 | -42.44067 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| cb4815e4-3751-302e-8183-4ff971683011 | -4.16429 | -42.44134 | 2026-08-23 03:21:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87258fe1-b1a2-35b8-a266-f651ff62cd3a | -12.26373 | -43.12129 | 2026-08-23 03:23:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 96e36312-55d0-3746-9d54-263f58978748 | -9.4811 | -40.35992 | 2026-08-23 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c656f0a0-de96-3bd3-b348-6ef1871c754e | -9.45178 | -40.32407 | 2026-08-23 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 07a3a813-e0af-3328-806f-b81f15d6f2c0 | -13.43477 | -43.86163 | 2026-08-23 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c4edf47-2859-356b-a90e-56101cb9e5b4 | -11.43325 | -44.54181 | 2026-08-23 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README9.md)
