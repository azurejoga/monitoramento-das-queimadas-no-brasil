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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b22be3b0-57af-3adf-8460-37b828d8b3f7 | -11.0244 | -49.6872 | 2026-09-03 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2682ad87-a19f-3d99-99ac-c3d422935c06 | -11.5287 | -45.4703 | 2026-09-03 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 920045ba-ec78-35b7-8d59-db7a46ea04ee | -10.3205 | -49.9567 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 7242f253-4504-3260-a4c6-271314bcb454 | -7.6149 | -44.8833 | 2026-09-03 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 76c4476b-574a-3750-a957-a91f75cc9ed9 | -11.0057 | -49.6677 | 2026-09-03 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5df932f3-83ac-3d58-ae33-e2522e295b69 | -10.3208 | -49.9352 | 2026-09-03 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| c7ea93d2-77d1-31e5-a7bd-91ff98f53ae2 | -5.565 | -60.1739 | 2026-09-03 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 854decdb-feac-3fca-9b4e-7cc4c4ea324c | -13.382 | -51.3352 | 2026-09-03 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 4a3cf306-4832-3f77-8ea2-12282f5be2be | -13.3817 | -51.3566 | 2026-09-03 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c65b11c5-6708-36fc-8f1f-a83d8d222f31 | -9.4538 | -45.6228 | 2026-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| e6140178-496a-3d2b-9e64-9594b3c28bf1 | -11.3892 | -50.6972 | 2026-09-03 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9d67cead-7e9c-3fa9-9e88-3677dcaf28a4 | -8.4235 | -44.9849 | 2026-09-03 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 3cc6b833-bd23-38e2-beeb-93e6b0255e70 | -10.1084 | -50.299 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| fc98e1c4-aa9a-30ce-9c88-2482471cd921 | -7.6169 | -49.9439 | 2026-09-03 14:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| f0b5fbbe-35e0-3a3a-94d6-1d5a65495eda | -14.5634 | -52.0344 | 2026-09-03 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 65273d61-46a7-3bb5-bf64-17a30454c679 | -12.094 | -47.0688 | 2026-09-03 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| d1e4dba8-8169-3a8e-b882-99fbddf6e282 | -8.9598 | -44.4204 | 2026-09-03 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 83.4 |
| a28e23d7-d073-3393-b539-7c9144539cdc | -22.8482 | -49.3487 | 2026-09-03 14:10:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 2cac0585-85e5-31b6-ba30-29aa5ac6e8ad | -9.4345 | -45.6477 | 2026-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 0a065d45-b5c3-3c55-8c94-e0e1ab4c01df | -12.1265 | -44.199 | 2026-09-03 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 0cec2d32-6342-31d3-8162-c5c6357c886c | -7.1123 | -42.7727 | 2026-09-03 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 57305fb2-8ce4-366f-8909-5f4b06a697dd | -8.4049 | -44.964 | 2026-09-03 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 5fb920a4-d7b4-3b6b-b3e8-b90dcc4ed9bb | -15.0858 | -48.0241 | 2026-09-03 14:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 22a606b6-8c89-36e6-8e9f-d91f97c9b068 | -10.3769 | -49.9723 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ca9fc05f-70dc-3e57-a47c-03d80a9b45b8 | -6.7648 | -59.4408 | 2026-09-03 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 6057c858-40e5-3153-a61a-ce9804a37a99 | -7.8071 | -47.8372 | 2026-09-03 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 7166dbaa-3439-321a-aa2d-92337a6d234d | -12.0745 | -47.0939 | 2026-09-03 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2c584fe0-bbed-3184-a171-27205a839493 | -9.6968 | -47.189 | 2026-09-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 95792dba-1a23-3a05-8a1f-79ecc05ff97f | -8.4675 | -54.6631 | 2026-09-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.2 |
| 380ecf90-fff6-390f-a55e-20c230562df1 | -3.8604 | -44.0585 | 2026-09-03 14:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 8dc202e5-e184-3e98-b400-1204c5336bc1 | -9.4349 | -45.625 | 2026-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2a6da595-c951-3c25-812b-9334c02e00fc | -9.6839 | -48.1386 | 2026-09-03 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 988f7cf3-63cc-3f6d-b411-89623ef4ed19 | -8.4485 | -54.7048 | 2026-09-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 510a6c7a-9544-3941-80e3-4dfd97fe2ac0 | -11.5086 | -50.3204 | 2026-09-03 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5f3b48e7-8b03-3fa2-a87d-99471b442833 | -11.3224 | -51.4049 | 2026-09-03 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| aaf315a6-432a-3503-b176-1fd9d82f591f | -12.0944 | -47.0463 | 2026-09-03 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7a10dda6-01fb-343d-a647-c608ccb97404 | -5.3264 | -60.143 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 9b670977-d8e7-31ee-930b-1e607b90e127 | -10.1087 | -50.2776 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fc7a71d7-808e-3d8f-aad6-fe964895a164 | -6.6698 | -59.9443 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 05d33c38-121b-3daa-82d8-0e72455ce8c4 | -8.7631 | -46.4418 | 2026-09-03 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 96e89698-fa07-3fac-b90f-dc136d9cbb3d | -10.4148 | -49.9683 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 72b8d39c-d8ec-3011-80c0-18ad0a66bcce | -12.3434 | -48.1485 | 2026-09-03 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 42a4493b-8b7b-3b11-aea4-a22f6a33ff31 | -6.6357 | -59.4459 | 2026-09-03 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 592112f1-0252-3d1d-8cb1-b5c3a3207a58 | -7.5982 | -49.9453 | 2026-09-03 14:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 64a79b6e-ca56-3c2e-970a-7ec5f4a5d092 | -12.3626 | -48.1459 | 2026-09-03 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 07861b2d-a5ea-3dfa-b148-a3fff392c49d | -5.5098 | -60.1947 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 6058abb7-881a-3da4-98b6-afb0b0aee649 | -11.5479 | -45.4676 | 2026-09-03 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f8b812ed-6798-3798-8d24-03c1cd95e524 | -9.5964 | -47.6204 | 2026-09-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 1dba95e3-c360-38f0-b9d9-6b2eec49e3c4 | -13.3813 | -51.378 | 2026-09-03 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| dc1b4360-b3a9-32ab-bb8b-373568a494b4 | -7.6144 | -44.929 | 2026-09-03 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 0d3da357-f031-3f89-b473-29b65d596f7f | -9.7157 | -47.1869 | 2026-09-03 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e2522bb3-3d80-325e-8eb5-5ea6ac99d0fe | -10.3956 | -49.9918 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| f9db81a9-bc1d-33ba-a2ce-f61a122917d6 | -11.5287 | -45.4703 | 2026-09-03 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 440afbae-11b3-3616-8365-83d9b3b93d47 | -13.3625 | -51.359 | 2026-09-03 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ac28bf08-a768-3d61-ae35-ec28ecde35f2 | -9.6293 | -54.3158 | 2026-09-03 14:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 79ac4434-4d06-3876-9cd7-0b946e555515 | -3.6215 | -60.566 | 2026-09-03 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| b0906cb7-861e-3323-8b09-69ed4c0a86bd | -11.2879 | -54.0317 | 2026-09-03 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 4d89039d-a693-30dc-8369-306af9ce25ba | -11.3056 | -45.1113 | 2026-09-03 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 47203ca7-2a81-3296-847a-f99c0bce238a | -8.4487 | -54.6846 | 2026-09-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 81db3d36-f16f-31a9-989e-d8c0d0716210 | -1.8019 | -47.9586 | 2026-09-03 14:10:00 | GOES-19 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| cfbc0f74-d579-32c6-a53e-a2f389aaced3 | -10.3959 | -49.9703 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 6501b793-cb56-3797-a0e2-cee12695184c | -12.0557 | -47.0741 | 2026-09-03 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 1e7fafea-791c-3eee-9bf7-76f3f4da5ed4 | -6.6541 | -59.4452 | 2026-09-03 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 22924bd0-9792-39bc-9e7e-6af69b602577 | -6.6883 | -59.9436 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.0 |
| c1814dce-83ce-3227-85c0-0dc8aca01ceb | -11.4898 | -50.301 | 2026-09-03 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a49fe56b-4620-30d4-87e3-a79697aae235 | -10.1273 | -50.2971 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 99494eb7-6b97-385a-9df4-f9858b3d865f | -10.4145 | -49.9898 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| f5994451-ac34-3190-aa56-2ba40ace05a1 | -7.5138 | -60.7728 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ecedc14c-15d8-3311-a8fb-ab3cc02a6463 | -12.0936 | -47.0913 | 2026-09-03 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1f1edfa0-cc91-3abf-98df-b93073ace570 | -11.4895 | -50.3225 | 2026-09-03 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 45e618aa-9ab5-3425-9204-9d1f72f5efd9 | -12.0749 | -47.0715 | 2026-09-03 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 257260ac-055b-3c87-b8e8-feddc322752f | -10.8582 | -50.7332 | 2026-09-03 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.8 |
| aa6cf763-a892-36a1-a288-594371ba58df | -10.7154 | -46.2395 | 2026-09-03 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| e70414a4-1f14-39a8-82c1-94f0e327eeb4 | -10.3961 | -49.9488 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 2b10e15c-6181-316f-b7d7-c664b0894857 | -8.4046 | -44.9869 | 2026-09-03 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c6ded1e6-c8e0-309b-b468-2abc2782be39 | -12.1316 | -47.1084 | 2026-09-03 14:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 59b2e109-a9e7-312a-91a0-17ef287d514a | -5.565 | -60.1739 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| ef13ad5e-835e-33d0-b7f3-5e93a90cb30f | -9.4342 | -45.6704 | 2026-09-03 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 1acc6c94-62d8-3285-a1d9-d82b9274b946 | -6.7463 | -59.4416 | 2026-09-03 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e62f6249-927f-3255-83ef-10b010fbf01b | -1.4752 | -54.8157 | 2026-09-03 14:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 6ca61b70-0f3b-359b-9e80-5671598fc884 | -10.6967 | -46.2193 | 2026-09-03 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 45392fd6-9955-3a8b-9e72-1a1fc65ead66 | -10.1456 | -50.3379 | 2026-09-03 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5f29fa7f-355d-3e61-b7c0-74998eb3f5e4 | -7.0979 | -45.7914 | 2026-09-03 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 49e20493-e910-3aec-9cc6-c96e0a1c089e | -8.4677 | -54.6429 | 2026-09-03 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 169.7 |
| 256d0ad1-7f6b-3dbc-ae9c-f2d4d8bf9f30 | -5.5099 | -60.1756 | 2026-09-03 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7de09402-66a7-30c2-a478-8ccf6b7bee57 | -10.9 | -45.35 | 2026-09-03 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 911ae12e-e4df-3556-8776-3b7dad61d817 | -10.91 | -45.4 | 2026-09-03 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e9bfd03-a489-3384-9b03-85b8ea6fbfd8 | -10.93 | -45.35 | 2026-09-03 14:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5343d0-ad74-35bd-8275-0b537e6bf50d | -8.4046 | -44.9869 | 2026-09-03 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d17be80c-13bf-3c65-bfbe-b27b0142a5bd | -12.3622 | -48.1681 | 2026-09-03 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| d284dc44-4e3e-3eda-9f16-c3746c228366 | -12.3626 | -48.1459 | 2026-09-03 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e06e6a3b-6354-3163-856c-0e6694494db7 | -12.1269 | -44.1755 | 2026-09-03 14:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| d6806f62-1d7c-3815-8d7d-43983ecb973f | -15.2866 | -53.8617 | 2026-09-03 14:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 71dad72a-d65d-3d00-9c7f-8fedb4ef88ae | -3.6215 | -60.566 | 2026-09-03 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1e6df8e8-ad4b-35ab-b41e-8cbce7bd3041 | -8.4675 | -54.6631 | 2026-09-03 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 209.8 |
| 8aedd99c-3b52-3848-8f81-d311f4333265 | -3.8604 | -44.0585 | 2026-09-03 14:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 269d525a-ca0c-32e9-b874-c000ec0b020c | -6.7463 | -59.4416 | 2026-09-03 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 5f2830be-f12e-3316-b0c6-590e444515fb | -11.0566 | -51.4539 | 2026-09-03 14:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 20c424a8-f978-3968-ae77-78836718d7da | -10.2214 | -50.3089 | 2026-09-03 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 78b6a760-db94-30f1-9e22-90be52f50fba | -5.5099 | -60.1756 | 2026-09-03 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |


[Clique aqui para ver as próximas entradas](README60.md)
