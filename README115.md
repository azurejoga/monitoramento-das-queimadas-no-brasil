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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dca09a5-ef48-3d95-b637-cba302077e37 | -7.5704 | -57.6766 | 2026-09-19 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 32a6681a-f579-3ed1-9622-92b93aaffb5e | -6.0197 | -51.7686 | 2026-09-19 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2d81cb08-ac35-3e6c-8988-5922feac3412 | -11.8934 | -47.6322 | 2026-09-19 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| c366cc29-d4ac-3922-877c-49eb2e0de612 | -11.8937 | -47.6099 | 2026-09-19 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| c24c210d-7101-3ab6-b63e-696278dacaa9 | -12.1531 | -46.9707 | 2026-09-19 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 186.2 |
| f49b5ad9-e544-3532-a6a8-9241822ab964 | -3.4455 | -58.1941 | 2026-09-19 14:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d6bf9d2f-4575-37a7-9832-ce13517a7f16 | -11.836 | -47.6398 | 2026-09-19 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 6ee15e75-2d35-392d-ae17-97a3cfa6c41b | -7.7118 | -44.6451 | 2026-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 233.7 |
| ea22c877-e82d-3f47-ac13-0257a0e62f50 | -10.8732 | -53.9874 | 2026-09-19 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1b8ea0e8-417d-314f-b567-d965316c09c7 | -12.2688 | -49.1907 | 2026-09-19 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| d8cd41ac-0562-3150-8ef0-9cdcbdfda629 | -13.2606 | -51.7335 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 04532249-9df6-3d21-bf15-59419abde09b | -9.6205 | -45.8755 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 4ecade59-3ebc-33dd-b2ec-144c2f9ad1f6 | -9.2603 | -45.939 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| e45def81-3ec7-3676-9f45-4b58c060320e | -7.0448 | -42.0906 | 2026-09-19 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 239.6 |
| 265c010e-02dc-3abf-8842-40a5eac27a5e | -11.3813 | -44.0554 | 2026-09-19 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 199.7 |
| f853ffbf-5437-33bd-a25b-952e0c1412ca | -12.2692 | -49.1689 | 2026-09-19 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| b03920ce-5779-3971-92c0-edcb65c421fe | -8.4296 | -54.7262 | 2026-09-19 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 23924848-5e55-306e-8016-8d0ed13836f5 | -11.6988 | -54.4443 | 2026-09-19 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| a920efae-c3db-3c1f-b156-0eaa38d6fd4d | -5.6408 | -43.392 | 2026-09-19 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 177.0 |
| bfe242ec-70aa-3061-9257-bf045022c556 | -9.0355 | -48.7487 | 2026-09-19 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 98.8 |
| eac0eaaa-75c1-37c2-b808-cfecb857c05f | -9.0167 | -48.7505 | 2026-09-19 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 76.9 |
| c963009b-f640-395c-b016-e26d7fb9fa4f | -3.331 | -59.8292 | 2026-09-19 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0f662f6f-fe16-3ca6-bc1a-f1bc06b901f0 | -7.8027 | -44.9108 | 2026-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 00dbc433-ee00-3b23-b794-43b5169169cb | -9.7134 | -46.0003 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 5cdec235-8784-3553-9bd9-d54b6eb839ed | -8.411 | -54.7274 | 2026-09-19 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 353ec928-81b6-396e-a37a-f11e2d801a19 | -3.3183 | -57.8677 | 2026-09-19 14:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 4bc37557-731f-334c-8456-aa16ab045fd9 | -11.299 | -51.7238 | 2026-09-19 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 6b259cd5-8b90-3dd4-8aec-76bebccf41e8 | -10.0956 | -48.4226 | 2026-09-19 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 15093a20-8448-30ff-89de-0453b42c56a9 | -12.5761 | -49.1071 | 2026-09-19 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 138.1 |
| 51b491a1-7901-330a-b51a-64e532cafa46 | -8.45 | -45.8674 | 2026-09-19 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 93fb4b0b-8c92-37fe-a2cd-4a9aea58ce07 | -13.0168 | -46.9578 | 2026-09-19 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 715030f1-58bd-32b5-a0a1-e6cc566f43d0 | -9.6202 | -45.8981 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 313.2 |
| aad486e4-a959-355c-8494-5dbf648c8109 | -8.1688 | -54.7432 | 2026-09-19 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| b9596d90-f03b-3388-a439-b53743ae811d | -11.0827 | -48.3095 | 2026-09-19 14:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 66c5a1c1-f011-33f5-9805-cde9babcf58c | -8.3365 | -50.8608 | 2026-09-19 14:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| d6d83480-a1b7-3fef-94df-326baf6082e9 | -13.892 | -48.592 | 2026-09-19 14:30:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e9e9b4f2-a486-35bc-9010-b713a8b816fd | -10.7736 | -46.1643 | 2026-09-19 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 94b6fb58-1597-3fbc-90e9-6aacf3914331 | -10.7991 | -50.9093 | 2026-09-19 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| fb33563b-e6a1-3f67-9498-6e90e930ef43 | -4.0089 | -41.2748 | 2026-09-19 14:30:00 | GOES-19 | SÃO JOÃO DA FRONTEIRA | PIAUÍ | Brasil | 2209872 | 22 | 33 | nan | nan | nan | Caatinga | 134.8 |
| e80ad8ee-9a46-3503-8b78-0868165b0c82 | -6.941 | -55.0366 | 2026-09-19 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 067f4abe-4b8b-3224-bd4e-2ae3b7416ef8 | -13.2222 | -51.7382 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 581309e4-07ff-3182-a115-e2d93a9be406 | -7.8595 | -44.8824 | 2026-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 14b15aef-dc05-3452-894a-fa940d9de91a | -8.8639 | -45.937 | 2026-09-19 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| f731a568-0bbe-333f-ad4e-de385216806c | -6.2582 | -41.6858 | 2026-09-19 14:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 178.5 |
| 5d5e4d86-2c46-39a1-985a-59661d196a29 | -10.913 | -50.8762 | 2026-09-19 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.3 |
| e0f2dc7e-0375-3097-967b-e3b70901242d | -8.7919 | -48.6851 | 2026-09-19 14:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 299.3 |
| be9a40bf-7083-3f6d-aa6e-7e60bb3e0408 | -6.2585 | -41.6617 | 2026-09-19 14:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 234.8 |
| c46f457d-bb09-3e40-a3e7-66b2383ccd1b | -11.318 | -51.7218 | 2026-09-19 14:30:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5cff9a35-0e8a-3148-addf-eaed5e3010a2 | -11.8934 | -47.6322 | 2026-09-19 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 70cb2ee5-4c53-3c5c-b346-cb8c3170bbcd | -7.7629 | -46.7389 | 2026-09-19 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 01d12423-1001-3950-9133-3f29850f45ff | -13.884 | -47.9929 | 2026-09-19 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 00ebb443-f44e-3892-8da7-83fa3428f24e | -5.7431 | -57.5814 | 2026-09-19 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f1324f49-5021-3bb1-b1d9-e048518d2bcd | -3.1514 | -58.644 | 2026-09-19 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c86bf9eb-5d9a-3419-9fb4-c589fde57c31 | -11.8546 | -50.0653 | 2026-09-19 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| bb0dabbd-5435-39fe-b1c2-752a89230119 | -8.9412 | -44.3995 | 2026-09-19 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 168.3 |
| f7eb9acc-4ff5-3602-9023-c024f59a7af1 | -4.5772 | -42.9746 | 2026-09-19 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 43d24748-4557-321f-bcef-5ef784da4017 | -11.0608 | -49.7909 | 2026-09-19 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 392d7b19-418e-3253-8f37-63d498ed4f8f | -7.0286 | -45.2554 | 2026-09-19 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6dc7c9d1-b783-3a75-85c3-08f1f08e0968 | -10.5368 | -46.7343 | 2026-09-19 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.5 |
| d241e4a9-3ff9-36c5-85a5-00fe49cab3db | -7.026 | -42.0924 | 2026-09-19 14:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 7a41bc79-cc69-3a3f-8af8-d9139a29b8c7 | -11.3817 | -44.0319 | 2026-09-19 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 7cdfac9e-5cbd-38d1-a289-4f4b68061320 | -9.6016 | -45.8777 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| a713a68c-7e78-315d-b60a-05b4df9013d6 | -11.0611 | -49.7693 | 2026-09-19 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 9fb6bd82-25f8-3e05-ab2a-b8feaae0a799 | -10.9133 | -50.8549 | 2026-09-19 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 46d73540-42f6-319e-b398-f9a04eca3d89 | -11.6798 | -54.446 | 2026-09-19 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 0e96ca48-cba6-38fd-a1ef-55e4a748b769 | -10.7715 | -46.3001 | 2026-09-19 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.7 |
| d6535524-fafd-307d-b6f5-ee96493aa2c3 | -3.4455 | -58.1941 | 2026-09-19 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 7b99ee3f-aaa3-347d-8e11-c21d32d7f597 | -9.0358 | -48.727 | 2026-09-19 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 6a83503e-7644-3554-b4a4-689c0a006b25 | -11.8549 | -50.0437 | 2026-09-19 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 9edfd6f1-e347-3b9f-b72f-7058dd7d9c22 | -12.2879 | -49.1883 | 2026-09-19 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| f2f469e8-7af9-36f9-9610-d5bbdbfb5e94 | -7.4479 | -44.6934 | 2026-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 00b3a8a1-1a55-33a3-a2c2-ee81d0df4efd | -8.6173 | -54.5924 | 2026-09-19 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 6aacba88-bd2d-38fa-806a-b4468f36a669 | -13.6274 | -48.2988 | 2026-09-19 14:30:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 0d4d305d-1fde-3db1-a078-4c3025974d88 | -7.8598 | -44.8595 | 2026-09-19 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 197.6 |
| c371b1c7-071b-311c-87e7-01ef2d6ccc83 | -11.3604 | -44.1521 | 2026-09-19 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.7 |
| 2ed1a591-6c13-3b57-b0ca-6f8bea01cf28 | -12.7085 | -45.96 | 2026-09-19 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 287.4 |
| daa13ba5-cce0-3551-b92a-e58a2ff78735 | -11.7823 | -49.8152 | 2026-09-19 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 67bade98-6d7f-3a08-b1aa-df329fb62674 | -7.5704 | -57.6766 | 2026-09-19 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 46ec5fbf-ae57-3f0f-b05d-812b41f286a9 | -8.4314 | -45.8467 | 2026-09-19 14:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 03f574fc-8c1b-3ca6-b257-bb854b22a777 | -11.1228 | -49.4384 | 2026-09-19 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| a9b62b65-70ba-3be7-bcd1-a626c845b7e0 | -10.6703 | -50.6465 | 2026-09-19 14:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 08a8c43b-c48e-3485-9afd-a02a406aa012 | -9.0361 | -48.7053 | 2026-09-19 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f2c4c10d-eab3-3616-9f83-8e177c1c7adf | -12.2883 | -49.1664 | 2026-09-19 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 3def7119-a3f6-31ce-b746-60b5de9c98b4 | -11.874 | -50.0415 | 2026-09-19 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a1f4713a-b9ea-3ded-8927-324c3d517aed | -12.6037 | -50.9405 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2488874a-5ee5-30e4-891a-53dd2084a5b7 | -9.2676 | -48.2472 | 2026-09-19 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b82f99c1-b117-3a93-b963-409c602a6810 | -9.0096 | -44.9209 | 2026-09-19 14:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 118.6 |
| bef47822-9eb5-3225-bae0-804faa67240b | -11.8746 | -47.6125 | 2026-09-19 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| ed3f7477-5d03-36a2-8eb7-ef27f6edf8bf | -10.7994 | -50.8881 | 2026-09-19 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 13d01b9a-2494-3a57-8071-9fb347da6157 | -10.7133 | -50.258 | 2026-09-19 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 503213be-c9b0-3908-be7b-04017ff1c699 | -8.8827 | -45.935 | 2026-09-19 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 9e2e0048-062d-3e89-8d98-ebd1f65f2105 | -7.7626 | -46.7612 | 2026-09-19 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 357.6 |
| e9bf23f7-a71c-32bc-be47-49b6c3f60b73 | -8.4737 | -47.0053 | 2026-09-19 14:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 154.1 |
| 36896dcb-e940-3182-b58f-dea6d031771a | -2.0765 | -56.585 | 2026-09-19 14:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 5a262038-9f91-3fe5-865b-9a187d03d7ed | -6.0196 | -51.7893 | 2026-09-19 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 15b1b6de-baf4-3662-9695-8a537c53ca27 | -13.0173 | -46.9352 | 2026-09-19 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 818f61a4-ec15-36fd-9b98-b62dbd53c75b | -7.0029 | -49.7551 | 2026-09-19 14:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 6e49e6b3-3ac5-3cc8-b952-cc6a9c8d8838 | -9.2414 | -45.9411 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c41106bb-b210-3252-946a-635a62c07930 | -10.5364 | -46.7568 | 2026-09-19 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 0c107f16-0174-3851-a2d5-fbc0d2180244 | -11.8937 | -47.6099 | 2026-09-19 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |


[Clique aqui para ver as próximas entradas](README116.md)
