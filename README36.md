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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7baf17c-4ead-3e31-977e-78b75f6241c2 | -4.89746 | -55.81299 | 2026-09-05 06:44:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 46cf2288-e4ad-3f44-9a1c-0daa54439abd | -6.1187 | -47.22545 | 2026-09-05 06:44:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| ed5bba2f-4988-3b75-ac43-1e3ae39c6d4c | -11.96214 | -43.28484 | 2026-09-05 06:44:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 9be92895-c2f7-3bc4-aa48-4cb17149e2f2 | -12.43302 | -43.27383 | 2026-09-05 06:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 2556aecd-7b74-3bf5-ab7d-c019a4820896 | -4.36118 | -47.7752 | 2026-09-05 06:44:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ccfe40b5-7dcc-3293-a95e-9d6a69c1b67c | -5.92516 | -47.89428 | 2026-09-05 06:44:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 635e38aa-d21d-3e14-b141-0d990dfdb8fb | -12.4395 | -43.4019 | 2026-09-05 06:44:00 | AQUA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7251ee13-178d-37ff-b70c-89d949c9f397 | -6.35236 | -46.11363 | 2026-09-05 06:44:00 | AQUA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 610ba5e2-8619-3d1e-a7fa-df18f752a376 | -5.76829 | -45.07047 | 2026-09-05 06:44:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.3 |
| f0ef93b3-eb55-33a7-a658-073ecad922df | -5.41865 | -43.25648 | 2026-09-05 06:44:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b02c1607-f1eb-35d3-828b-f8fcef14352a | -5.40846 | -43.25499 | 2026-09-05 06:44:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f7331b09-5ccc-386d-a156-dae7bf5470b1 | -5.92652 | -47.88531 | 2026-09-05 06:44:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 7a6833bc-3764-3105-bb80-241f3a1ad065 | -4.67988 | -55.63396 | 2026-09-05 06:44:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 3a8d59ec-f544-3966-813f-89ac28150a03 | -22.1703 | -46.92316 | 2026-09-05 06:46:00 | AQUA_M-M | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 17.1 |
| cec9fc16-40ae-333c-a281-f03ee89d7242 | -9.5306 | -68.63322 | 2026-09-05 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d142008c-e4a5-345b-b6e3-3323468b302e | -9.53755 | -68.63406 | 2026-09-05 06:46:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bba7f2b2-c6de-3213-afbc-66295a88e5b5 | -7.36311 | -73.28108 | 2026-09-05 06:46:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2529277-ff62-3170-8a9b-011eb7adde03 | -5.3462 | -56.0256 | 2026-09-05 06:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 387a607b-049d-3ece-8093-1cc373dbff90 | -6.6514 | -59.945 | 2026-09-05 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| f861b49e-b36d-372a-b7da-3c63f0ee4623 | -6.6698 | -59.9443 | 2026-09-05 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 8b723ba9-077b-3ee8-b5a1-d6f296118491 | -6.6513 | -59.9642 | 2026-09-05 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 67e49c3e-d2a4-3d9c-8f5f-e592ff7361e7 | -6.6697 | -59.9635 | 2026-09-05 06:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 31efe71b-b037-3b9e-99ed-183dd153681a | -6.6513 | -59.9642 | 2026-09-05 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a856600d-dd9f-30b8-a547-45f5c54245c6 | -6.6698 | -59.9443 | 2026-09-05 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 09df6005-4a12-32a8-80ee-7443afc873b7 | -6.6514 | -59.945 | 2026-09-05 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 5686e9fb-e36a-3a59-86af-8a425c4aa8f6 | -5.3462 | -56.0256 | 2026-09-05 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 03245561-058e-322d-8be0-db1a0b6c965b | -6.6697 | -59.9635 | 2026-09-05 07:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6b646b69-1058-3f26-8762-561881b67ad8 | -6.6697 | -59.9635 | 2026-09-05 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0bbf01de-f36c-3448-9ae0-29da288b633a | -6.6514 | -59.945 | 2026-09-05 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 21782d6b-47ef-3042-9123-a9ba770ac557 | -6.6513 | -59.9642 | 2026-09-05 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 93479ec7-3022-3487-aa90-68b6060a424d | -13.4264 | -43.8163 | 2026-09-05 07:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 4626c740-8eb3-33e8-be80-bcf20081dd62 | -20.3341 | -44.5454 | 2026-09-05 07:10:00 | GOES-19 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.3 |
| 619a421f-28fb-3830-9b25-c1ca3a06bc8d | -6.6698 | -59.9443 | 2026-09-05 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 5c2ce769-db5e-3b73-9922-454ff1c21ce6 | -5.3462 | -56.0256 | 2026-09-05 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5ec05bb6-d587-3c76-819f-aa7eb0791eeb | -20.3135 | -44.5509 | 2026-09-05 07:10:00 | GOES-19 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| a74048f6-602e-36c2-a3b1-350a2e4516a4 | -6.6514 | -59.945 | 2026-09-05 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 22c809d6-ae1a-3db5-9d41-dec3c602300f | -20.3341 | -44.5454 | 2026-09-05 07:20:00 | GOES-19 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.4 |
| 10e472ca-8758-30ba-b643-dd6acc759ac8 | -20.3135 | -44.5509 | 2026-09-05 07:20:00 | GOES-19 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 35762cdc-304c-374f-a02c-f4f2637cc0c3 | -20.3333 | -44.57 | 2026-09-05 07:20:00 | GOES-19 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.2 |
| 9a5cfe06-54c0-38b4-beca-44ff551f9c75 | -6.6698 | -59.9443 | 2026-09-05 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| b5e5132b-abdd-3c57-b7b9-cfb82fce5f07 | -6.6697 | -59.9635 | 2026-09-05 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| f893736e-0d49-3863-8037-1c6f6fdf6cd4 | -6.6513 | -59.9642 | 2026-09-05 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| a7e4ff25-8f40-3b60-88ff-74af09929edd | -13.4264 | -43.8163 | 2026-09-05 07:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| e2303b9c-46a0-3957-a0d5-39521d1a3651 | -6.6514 | -59.945 | 2026-09-05 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 282bb06d-1383-36e9-8c6c-bcd4fcff4fe7 | -20.3341 | -44.5454 | 2026-09-05 07:30:00 | GOES-19 | ITAGUARA | MINAS GERAIS | Brasil | 3132206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| 551f5897-e955-3ef1-b375-7112df779b1f | -6.6513 | -59.9642 | 2026-09-05 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 4352df8f-85d3-3556-ab16-359f439b3faf | -6.6697 | -59.9635 | 2026-09-05 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f97f1ed4-475c-3f0b-9efc-7afebdff5145 | -13.4264 | -43.8163 | 2026-09-05 07:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 676046c1-c99c-3e86-b5f8-68742cb51e78 | -6.6698 | -59.9443 | 2026-09-05 07:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 94f203f0-8926-39a7-b9aa-34b0509b14b5 | -3.7645 | -61.7737 | 2026-09-05 07:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 50e9ee77-88d8-30ff-9895-4a1c963d2110 | -6.6697 | -59.9635 | 2026-09-05 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c5206b5f-072b-3ccd-ac7d-db3be0911810 | -6.6514 | -59.945 | 2026-09-05 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.0 |
| ca47e15e-e1ac-3a34-b57b-85c8a4ab8612 | -13.4458 | -43.8128 | 2026-09-05 07:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 20e528c3-a86e-3fc2-9632-ce97e12d7c06 | -13.4264 | -43.8163 | 2026-09-05 07:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 3935f36a-409e-3520-9025-62c41a838d9f | -6.6513 | -59.9642 | 2026-09-05 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f6151f88-053e-3885-8e13-f4ef412cd771 | -6.6698 | -59.9443 | 2026-09-05 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| c9f3412b-a75e-3623-93a9-71c55d52491d | -6.6697 | -59.9635 | 2026-09-05 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ac949317-9ca1-3ede-8131-e864b5bc9197 | -10.749 | -60.729 | 2026-09-05 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| e5a12de3-3a71-3bbc-894f-b6c3f29653e0 | -13.4458 | -43.8128 | 2026-09-05 07:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5d5c6322-6888-3eb7-83eb-434160ca5b86 | -6.6513 | -59.9642 | 2026-09-05 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| e713cb3c-0b45-3d23-a333-3a6c7111c436 | -13.4264 | -43.8163 | 2026-09-05 07:50:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 0c13020b-212f-3cc9-856d-a718435deaa6 | -10.7488 | -60.7483 | 2026-09-05 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| b68ad870-46c2-3f5a-b474-2ec37052a326 | -10.7676 | -60.7472 | 2026-09-05 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 37def9de-97ef-3a02-a469-f071bd6558c7 | -6.6514 | -59.945 | 2026-09-05 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 93193ed7-b4bc-3c82-86c5-c18241219b5d | -6.6698 | -59.9443 | 2026-09-05 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| cc321a3a-9c77-388a-9f39-828417ee1fbd | -10.7677 | -60.7279 | 2026-09-05 07:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 2155063e-3098-38e6-a54e-646ef4734c7a | -6.6698 | -59.9443 | 2026-09-05 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.8 |
| b82139e6-1f7d-3544-a03c-d6651ff4dab4 | -10.7677 | -60.7279 | 2026-09-05 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 03dd52c2-b1e1-3bb9-b1bf-4dbe6de64198 | -13.4264 | -43.8163 | 2026-09-05 08:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 44c743c8-a4d6-39bc-bb95-bfaec0a17692 | -6.6697 | -59.9635 | 2026-09-05 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2acc24ac-e21a-3343-b748-b5be6256f20b | -6.6513 | -59.9642 | 2026-09-05 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| ea98bd42-8b4e-3cca-a041-a22fa2ca4990 | -6.6514 | -59.945 | 2026-09-05 08:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.7 |
| da14ab53-c3c4-3271-9bd8-c174cfbd9965 | -10.7676 | -60.7472 | 2026-09-05 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 6d4a4777-8641-347d-b5ee-6b6e0f4e4aa3 | -13.4453 | -43.8366 | 2026-09-05 08:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 99289f90-fdc7-39a2-82b5-924a2d30d83a | -10.749 | -60.729 | 2026-09-05 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 017ae5db-1af1-33e8-86fc-f3030f4c980f | -13.4458 | -43.8128 | 2026-09-05 08:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| ee3f34e6-6e7c-3ba5-85df-7b7b8924ad9f | -6.6698 | -59.9443 | 2026-09-05 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 945bd975-5676-32b1-94bb-e3090e97c6ae | -6.6513 | -59.9642 | 2026-09-05 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c753b6d1-6d9c-356b-8d74-eceb2871704a | -6.6697 | -59.9635 | 2026-09-05 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 40e23762-c7b1-34ed-85cd-48b9a0cec1a9 | -6.6514 | -59.945 | 2026-09-05 08:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.0 |
| d77cf625-a659-3e99-8997-c0b29ae23c27 | -10.7677 | -60.7279 | 2026-09-05 08:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 0f206517-f7f8-3820-9004-30b5ccc5b75d | -6.6697 | -59.9635 | 2026-09-05 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| bb3eb742-d3e8-36cf-83cd-e9bcb734725c | -6.6513 | -59.9642 | 2026-09-05 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| da3245e5-ed2b-326a-b32f-1e7770d79656 | -6.6514 | -59.945 | 2026-09-05 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 116.4 |
| f577805a-7519-37ad-8d84-a6f70cecfd64 | -6.6698 | -59.9443 | 2026-09-05 08:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| c3604f38-5378-3b67-9d41-13e12f87ac31 | -6.6698 | -59.9443 | 2026-09-05 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 0d1d8fd7-dc47-3c18-92e7-d246741ea73b | -6.6697 | -59.9635 | 2026-09-05 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b2744e63-94ca-32a8-9b99-0aa10426f496 | -6.6513 | -59.9642 | 2026-09-05 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2f644e17-b88e-3177-80bc-08706a5c30aa | -3.7645 | -61.7737 | 2026-09-05 08:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 7acb3131-eb7d-3055-9f21-2091e8b7a049 | -6.6514 | -59.945 | 2026-09-05 08:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 99d735c5-3c1f-339f-af9c-a8d992e11988 | -6.6697 | -59.9635 | 2026-09-05 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e94dc497-e05b-382c-9bb1-17de5ea38916 | -17.1078 | -56.8304 | 2026-09-05 08:40:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.3 |
| 035dffc5-5cc1-395f-8075-563be0ae8f40 | -6.6513 | -59.9642 | 2026-09-05 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 476df99e-bd11-30f0-87f6-c444b0cbe89c | -6.6514 | -59.945 | 2026-09-05 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 01304ec9-c0ed-3e69-91ec-198dbf59eca0 | -6.6698 | -59.9443 | 2026-09-05 08:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| f6e88676-aa80-3bee-8a22-825ec882cefa | -6.6698 | -59.9443 | 2026-09-05 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| a1682f34-c32c-38a7-9bf2-bf273e01029d | -6.5963 | -59.9087 | 2026-09-05 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b4548837-f984-3916-bdc1-df3124e414f8 | -6.6513 | -59.9642 | 2026-09-05 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 53124354-1f06-3455-b2e7-15ff12003a8a | -6.6514 | -59.945 | 2026-09-05 08:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 8602d289-feb9-3b21-8985-5f614a43d248 | -6.5962 | -59.9279 | 2026-09-05 08:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |


[Clique aqui para ver as próximas entradas](README37.md)
