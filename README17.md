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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eee51c8f-3796-3417-b5ea-2067734e38ba | -11.1615 | -44.6002 | 2026-10-02 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d5279a40-d5cf-3b06-83f4-f9039ec45604 | -5.7357 | -43.2682 | 2026-10-02 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d8b7fa2a-41fa-3925-b501-53097e7f3455 | -13.0183 | -51.3166 | 2026-10-02 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 03f2a3a5-e778-3406-ba57-fd2233c4f8e1 | -10.7818 | -53.7493 | 2026-10-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.7 |
| 9a509731-ae85-363d-aec6-d7176f6b78f6 | -1.2739 | -54.5587 | 2026-10-02 01:40:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| d6650711-802f-3478-aa0b-c94777901bd6 | -13.3481 | -43.8538 | 2026-10-02 01:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 308.1 |
| 62836566-9bf5-3ec3-9bba-d78b0492ad69 | -6.2507 | -53.1536 | 2026-10-02 01:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 15df0cf5-f5cc-3515-98df-0fb3caf493d9 | -10.7816 | -53.7699 | 2026-10-02 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 149.6 |
| 6887b470-96fb-372d-833d-d6091d6b328a | -3.1299 | -53.7431 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 310d4147-0fb9-33fa-a4c6-b6f598868083 | -7.887 | -44.1671 | 2026-10-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9d5022ab-a664-37a0-860b-c74af4b25e8a | -2.0394 | -56.8593 | 2026-10-02 01:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| be624d8f-aa1b-3984-86c5-f2e4de986fb5 | -3.0008 | -53.8874 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 572c86ee-915a-3342-9dfc-0252ffd700b5 | -9.844 | -44.8449 | 2026-10-02 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 1b6a2097-af9a-3b37-ac92-a9535de5ca6f | -11.4691 | -43.4299 | 2026-10-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 985631c8-29da-3f17-9ec6-51ad7954e0cb | -3.0192 | -53.887 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 69ccffb7-6421-307a-ae22-814d4facbafc | -13.0762 | -51.2882 | 2026-10-02 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d6d839a5-d72d-3e48-996a-2a7f2d06f115 | -4.2676 | -50.7506 | 2026-10-02 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 62cd8a2a-f7a9-3139-83b3-9295ea62ca8a | -3.2767 | -53.84 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7ee77d3c-3ae6-3de2-9061-d09b183e7241 | -13.0187 | -51.2953 | 2026-10-02 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 80604475-d4eb-3207-be26-a27e35ab955c | -6.3952 | -56.4158 | 2026-10-02 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 2ed29d23-7a05-3d01-93ec-60eed8479868 | -3.1483 | -53.7426 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 69efa3a0-b789-37ec-a054-6bc0038db0d2 | -4.2953 | -49.1021 | 2026-10-02 01:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| a34e3426-4e9b-34a8-8843-ff2693bca8a6 | -3.2951 | -53.8395 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 3650383a-dbb7-362e-8891-c59cd2d6eb0c | -11.1424 | -44.6029 | 2026-10-02 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4579b6db-fc98-3dba-8819-40ce67a6a9ae | -5.7542 | -43.2901 | 2026-10-02 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| df4af6d1-e1c2-3072-aa71-92d7ceece835 | -3.295 | -53.8597 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 34ea6e23-e817-382f-8beb-4bc37b192cb0 | -5.7355 | -43.2916 | 2026-10-02 01:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| a0c2a3d0-11cd-3d70-bbe9-80c6ad8cc653 | -12.9803 | -51.3 | 2026-10-02 01:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 79c99b8e-e64f-3aab-801f-0fbcc9ce1ece | -2.0393 | -56.8789 | 2026-10-02 01:40:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 5c91f94d-3fd0-3c39-9835-e6801269119c | -6.8952 | -43.6833 | 2026-10-02 01:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3b1c1883-ce9a-3949-8e56-c6153e5e8142 | -3.1839 | -54.0839 | 2026-10-02 01:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| af5dad2b-e570-37cc-91af-94297b6cd78a | -7.8682 | -44.169 | 2026-10-02 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| ba20308c-39d8-3072-953f-0627333585d5 | -11.6964 | -43.584 | 2026-10-02 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 70fa2fdd-4633-3a1e-a271-f42a21ea7665 | -7.4188 | -55.5902 | 2026-10-02 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a6b7a1c4-6530-386a-9ce2-6cb543e99ff9 | -6.0739 | -47.2922 | 2026-10-02 01:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 71672737-22de-36ef-9132-d57d8a020ff7 | -4.2677 | -50.7297 | 2026-10-02 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 47881c0d-1ae6-3c68-9ab5-d9309b25ed55 | -2.0394 | -56.8593 | 2026-10-02 01:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 375206a7-6872-3cb5-84cb-6728738ae373 | -7.887 | -44.1671 | 2026-10-02 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| bc628cf7-0d39-38e7-94c1-ddb93b7b3ccd | -11.7541 | -43.5749 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| 2c48db4b-0aab-38de-98c6-9dd787ba87e6 | -3.1655 | -54.0844 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e786f20a-f011-3acf-ab52-04ef98ce20c7 | -11.6767 | -43.6106 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| a7faa044-12c5-3f14-bc5b-c1b68dedf970 | -6.0741 | -47.2703 | 2026-10-02 01:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 82.6 |
| f53c313b-a4c3-375c-8c98-48b6241684c6 | -6.2323 | -53.1342 | 2026-10-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 12d9439e-6015-37c0-871a-e62863967bc7 | -11.6771 | -43.587 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 1352183f-da40-3747-a653-b60ce46ea874 | 1.8037 | -55.5854 | 2026-10-02 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 43659dcb-f32c-3381-9b1c-ea7641b69bc1 | -11.7545 | -43.5512 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3a561451-0927-3d34-92d7-3d1912870647 | -11.6575 | -43.6136 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c02f1d91-1ad7-3993-a84e-ad2e77817135 | -6.209 | -60.0378 | 2026-10-02 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| d5049b9a-babb-3b6d-8e60-107122a7fc1c | -11.7926 | -43.5689 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| d848cd50-718d-3c40-8f6b-0ba17564dbea | -3.1483 | -53.7628 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e73e4de2-889c-39cb-a689-7416eb2db3fc | -10.7816 | -53.7699 | 2026-10-02 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 212.3 |
| bc730c4e-bb7e-308f-a44d-d63529a9b68a | -10.8005 | -53.7682 | 2026-10-02 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| f7e737a0-863b-3c74-9208-9c6cbe3eef17 | -3.1299 | -53.7431 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 63e03771-a9f3-3ae7-a90f-8ce77442c95f | -11.7738 | -43.5482 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| f8335b68-31d0-398f-af75-8f529e3bf2dd | -11.1424 | -44.6029 | 2026-10-02 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 20454bfd-a42c-395b-918d-2c2fd3181ee0 | -12.9995 | -51.2976 | 2026-10-02 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 0f5be6d5-3516-3e4f-9102-4890d3cbc6e2 | -10.8007 | -53.7476 | 2026-10-02 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 0356cfc2-ef04-3ee3-9cd4-a66e65c14652 | -11.7348 | -43.578 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6c5854e4-fde4-37d5-929f-6cc85bdb1ae7 | -4.2676 | -50.7506 | 2026-10-02 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 2ee15daa-31a0-3491-9429-26c61a8164cc | -3.1299 | -53.7633 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| dc9c29e3-d31c-30e8-9162-b91077aee03e | -2.0576 | -56.8786 | 2026-10-02 01:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 7f360a93-4098-34d0-b20f-ed7fe0fbbef2 | -3.1483 | -53.7426 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 0066ea85-3f47-38ea-80ba-155b8537e8be | -11.3099 | -50.94 | 2026-10-02 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6c50cae6-571e-3ca8-ad8b-5ba419d8132d | -13.3287 | -43.8573 | 2026-10-02 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 118.8 |
| ab2ea7cc-cd12-3b67-b307-fec5ab406868 | -3.1839 | -54.0839 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b6f1970f-2492-33ce-8b21-4a81d4087a0a | -6.0552 | -47.2935 | 2026-10-02 01:50:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 49854fab-a5f1-3926-af3b-331bd7f83bbf | -6.3952 | -56.4158 | 2026-10-02 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9e1a729f-f448-3da2-890b-1f3cc127cd9c | -4.2491 | -50.7514 | 2026-10-02 01:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 45b5fccd-681e-3ed0-9635-ed69d8848bae | -13.0183 | -51.3166 | 2026-10-02 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 74bb8e78-0d28-363b-94c0-b7d68f78c1fe | -13.0187 | -51.2953 | 2026-10-02 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 640bc6b5-d2db-3dcb-8253-4d29658361e5 | 1.7853 | -55.6449 | 2026-10-02 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2ebf7bb6-46aa-3162-b2b6-af92b83b56ec | -11.3425 | -51.3182 | 2026-10-02 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 6466a262-23c1-305e-8ee0-5aae6d94f535 | -11.1615 | -44.6002 | 2026-10-02 01:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d8ba4dba-9322-3d13-b1dc-ee8c1c077df4 | -13.3476 | -43.8776 | 2026-10-02 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 117.7 |
| e48b5b16-cf59-35f4-b8f0-ba435aab9133 | -11.1499 | -51.5497 | 2026-10-02 01:50:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| f75df540-ac62-380b-91c6-6fcfbcd0f839 | 1.7853 | -55.6251 | 2026-10-02 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 157.9 |
| 990123e5-b51d-37d9-93b5-35882294a7ce | -2.0577 | -56.8591 | 2026-10-02 01:50:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 032feaac-1fc6-3fba-9673-fbaf1468c3fc | -4.2953 | -49.1021 | 2026-10-02 01:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b1461f28-11ed-3336-a20b-1b87d5a7f078 | 1.767 | -55.6254 | 2026-10-02 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 979392bf-28da-37b1-a70e-f0428860cdf4 | -6.2507 | -53.1536 | 2026-10-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f760d4bd-75a0-33f3-a534-cf55aa235d1b | -7.0478 | -55.6302 | 2026-10-02 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e692c5e7-22d7-32e5-8530-6b67563806f4 | -11.7733 | -43.5719 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| d3167d35-a0a8-3887-aa0d-054abb99729b | -13.3481 | -43.8538 | 2026-10-02 01:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 241.1 |
| f7b0c7a6-0830-330b-bea9-a9c42321bce0 | -11.6964 | -43.584 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8188521f-2c71-36ce-aea1-e63eaa5404d6 | -10.7818 | -53.7493 | 2026-10-02 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 174.7 |
| 5875c2c5-b780-3dc3-909e-5d6fc95162ed | -6.9317 | -59.2798 | 2026-10-02 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| c404bbfd-376d-37f0-939e-52d61eebb910 | -11.4691 | -43.4299 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| fe1d6bdf-e21c-34ff-9a0f-a6fe48c8aca2 | 1.8037 | -55.6051 | 2026-10-02 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e4f5f416-362d-33c2-b7d8-4a422da65e7e | -3.0192 | -53.887 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 133526b1-103c-3a95-a00f-1ccb0ea1a510 | -13.8568 | -43.6432 | 2026-10-02 01:50:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 7f8ead0c-2875-3bc8-9a7a-d12144c6d3da | -11.3102 | -50.9187 | 2026-10-02 01:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.7 |
| b6630fcf-86f7-3aeb-998d-5ec520e7e98e | -7.2704 | -55.5983 | 2026-10-02 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5ca416a2-a8b7-3fbe-9a02-2703882fe7b9 | -3.1838 | -54.104 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7682c2a3-2421-3f69-9249-faf99680884d | -11.6579 | -43.5899 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 313d044c-711e-3f97-a342-d3cc573d0907 | -12.9803 | -51.3 | 2026-10-02 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| c3423f43-f28f-30c4-8ca8-90b35a1467e7 | -3.0008 | -53.8874 | 2026-10-02 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 282d9350-9ca0-3f55-867d-91503b05fd10 | -6.2091 | -60.0187 | 2026-10-02 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 89d101ef-65d0-392f-baef-7d47d7eb4051 | -11.6959 | -43.6077 | 2026-10-02 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| ba5b591a-c8b6-358d-ac2d-721b9b11dc10 | -12.9992 | -51.319 | 2026-10-02 01:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 99637974-a40d-3445-96c6-6cab23117154 | -6.2508 | -53.1332 | 2026-10-02 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |


[Clique aqui para ver as próximas entradas](README18.md)
