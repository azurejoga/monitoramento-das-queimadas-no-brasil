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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98c32ed4-1e92-3f5a-ac69-abd013887352 | -10.8624 | -45.3789 | 2026-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 310e6652-d8e9-38d8-9b5f-4fce6dc633c1 | -10.8631 | -45.333 | 2026-09-01 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 596bb0ab-30eb-3ee0-a1e4-910f0b8aadb8 | -8.7817 | -46.4623 | 2026-09-01 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 7773c66d-6261-3fd1-b424-d0b29fcc6a89 | -8.7819 | -46.4399 | 2026-09-01 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 35d2beb4-7573-320f-aaf9-81af8e5c6fb4 | -6.9553 | -55.6151 | 2026-09-01 12:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 416b8eb7-dda0-35fb-8b15-a866884c63f6 | -10.1321 | -45.8825 | 2026-09-01 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| daf57a59-a235-3ff4-9f6e-b6f0efb57636 | -15.4429 | -52.681 | 2026-09-01 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 92e68def-2421-3c99-9ce8-747095994c7d | -10.1324 | -45.8598 | 2026-09-01 12:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 269.0 |
| 42e37988-ee57-3410-9b1c-ceedaea851f2 | -8.7817 | -46.4623 | 2026-09-01 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 0716baf8-ad7c-3252-914d-b8c17c1651dc | -17.1345 | -46.8516 | 2026-09-01 12:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 831323c5-b776-3132-b466-8c022d233946 | -11.2673 | -45.1167 | 2026-09-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 67d97fa1-49d1-3da2-be43-cea100d45fc5 | -6.9552 | -55.635 | 2026-09-01 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 03ff2440-22ae-3711-823b-17bf0e426d79 | -3.8604 | -44.0585 | 2026-09-01 12:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 324f3cea-eacd-35c2-a900-b018f336beea | -17.4644 | -52.4045 | 2026-09-01 12:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 89b0445c-4121-30d8-853b-c2790237538f | -10.1321 | -45.8825 | 2026-09-01 12:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 278.9 |
| e646e1b1-f718-3943-bbf6-5068bf9fe55c | -15.4429 | -52.681 | 2026-09-01 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 8ff75bc4-6acb-3d23-a596-d74649ddba39 | -10.8627 | -45.356 | 2026-09-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| d4f9fe35-9787-354a-9ace-3cf3213b7972 | -14.4204 | -52.4989 | 2026-09-01 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f744dc5e-70d6-3029-975c-d83552065425 | -14.4397 | -52.4964 | 2026-09-01 12:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 000c9fd9-43b3-3c7c-85f9-9fafa9812aec | -6.9553 | -55.6151 | 2026-09-01 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 95f701d9-6d90-3923-87e3-fd728ac8ccde | -6.9737 | -55.6341 | 2026-09-01 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 71ade633-c363-3a21-8cab-1722ee507902 | -10.8818 | -45.3534 | 2026-09-01 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6d88866a-a0e7-3437-b380-4a34ce0688b8 | -15.4429 | -52.681 | 2026-09-01 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 30c42fb4-42b1-3bf0-a7d0-57e6c1145f2c | -10.696 | -46.2646 | 2026-09-01 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 6b76789a-b24c-3ed6-8203-3e9b7750ea9b | -17.9493 | -44.5817 | 2026-09-01 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 828f78a9-62aa-337c-bf3d-28e0cdce562b | -10.1321 | -45.8825 | 2026-09-01 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 85d8275c-dc25-35cf-9648-81eaa92f462e | -17.9701 | -44.5529 | 2026-09-01 12:30:00 | GOES-19 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 221.9 |
| 56041071-cadb-324b-854d-5a5fb3e2ec66 | -14.4397 | -52.4964 | 2026-09-01 12:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 08d3476f-d7cf-359c-9152-cc594a23016f | -15.4235 | -52.6836 | 2026-09-01 12:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| a0a946c7-d64b-3d28-a3c1-79544f7fd170 | -10.1324 | -45.8598 | 2026-09-01 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c2b62546-1a0b-37d0-a9aa-934535f9ef3c | -12.8839 | -45.8412 | 2026-09-01 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| d216a743-54a0-385f-9584-44fa69a999f1 | -10.6964 | -46.242 | 2026-09-01 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 65dd5b4f-0e0c-34bc-9e1c-2f8b4108765b | -14.6732 | -53.5408 | 2026-09-01 12:30:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| cb1774df-e07f-3240-b2a9-64dcb7935314 | -12.9032 | -45.8382 | 2026-09-01 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 14d43b0b-3d8f-3cb8-b295-442f9145c6c6 | -9.9912 | -46.4409 | 2026-09-01 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 2129f984-16a0-318e-938e-b0ff3e776d76 | -9.6679 | -46.5455 | 2026-09-01 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 95fe222d-a0e0-357f-aca0-61200e5d5814 | -17.9695 | -44.577 | 2026-09-01 12:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 574.9 |
| e7a800a1-1b1c-3428-8294-5567ca4b2977 | -6.9553 | -55.6151 | 2026-09-01 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| f421bd6c-a9f9-3b8d-9367-534ce254565e | -3.8604 | -44.0585 | 2026-09-01 12:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 0a1488b2-4080-3bc9-a56c-0957f78cf5c1 | -7.905 | -44.2346 | 2026-09-01 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 200ac7a5-f5be-37aa-b5fe-b57fd460cb09 | -7.9048 | -44.2577 | 2026-09-01 12:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 104.7 |
| c0b420c6-f18e-35bc-b3cb-f73ae48a23b7 | -11.2317 | -46.1041 | 2026-09-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 503e13ad-4c6e-33cc-9eec-921ef2a37c08 | -11.213 | -46.0839 | 2026-09-01 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| cce5b34b-165f-3f6a-8373-af3f2aa48706 | -8.2788 | -54.9376 | 2026-09-01 12:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 26223cec-ba2c-3271-b73f-20aa02319fc0 | -6.9552 | -55.635 | 2026-09-01 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| ee7eb5b4-2c09-3bcf-8597-640f231744fe | -9.4349 | -45.625 | 2026-09-01 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| af653c64-449f-34f9-b24a-58333abd569e | -3.8604 | -44.0585 | 2026-09-01 12:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 98aa2ec8-49fb-360b-ae90-91c981ea0448 | -6.9553 | -55.6151 | 2026-09-01 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 3208db9c-1156-350a-90b1-c4910fa912a9 | -10.696 | -46.2646 | 2026-09-01 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 1cb7b7b9-7dfb-3c6a-816e-691a17758e99 | -14.4397 | -52.4964 | 2026-09-01 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 83240a4b-d73b-31f3-ad2b-bf60f08b2cd8 | -8.7817 | -46.4623 | 2026-09-01 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 1b2978f0-5fd1-37c2-8e26-29e4bd81fdbf | -6.1659 | -57.7403 | 2026-09-01 12:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 935c20f6-cd15-388b-9322-d878340c0037 | -6.9552 | -55.635 | 2026-09-01 12:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| d4524a06-bf61-3b86-b4d3-294b1ab42e5e | -10.1321 | -45.8825 | 2026-09-01 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 390.9 |
| fa66cda6-bc5f-3a03-8839-260df2e9fd8a | -11.2317 | -46.1041 | 2026-09-01 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 0d3694b6-034f-3600-86ac-017cc15e43b4 | -8.2788 | -54.9376 | 2026-09-01 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| f8b7d54d-6335-3621-86d8-6c7d5c539ca6 | -10.1324 | -45.8598 | 2026-09-01 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 391.2 |
| 05a678cb-23bb-3f4f-bbc8-dc6a4483ac0e | -10.1131 | -45.8848 | 2026-09-01 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 6c894fe5-34bd-3ce2-8c6b-6e697573c9bb | -7.8904 | -47.0821 | 2026-09-01 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 731f856a-8060-3e3b-b693-4a92ea284e4f | -11.8056 | -46.0476 | 2026-09-01 12:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 44abdbcf-6487-31a2-8a88-0bb5fe4e1204 | -8.279 | -54.9174 | 2026-09-01 12:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 28f896a3-9ced-3dd8-b45c-74236ba92f37 | -10.1134 | -45.8621 | 2026-09-01 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| a78dcf08-985d-3031-8e20-2384df303cc9 | -11.5479 | -45.4676 | 2026-09-01 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| a3861814-da92-393f-aae4-33bf2b5b7d2e | -10.0364 | -44.6825 | 2026-09-01 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e7568f1e-b8c2-3516-b286-758b2d46f7fd | -14.4011 | -52.5014 | 2026-09-01 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| f6e6b585-7e9e-3e1b-9942-5ca339fcc7d6 | -14.4204 | -52.4989 | 2026-09-01 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| b552f2a5-57e2-312c-8e54-70514123aba9 | -7.8716 | -47.0838 | 2026-09-01 12:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 57d30dea-bba9-31a4-a94a-2648221da97c | -12.8839 | -45.8412 | 2026-09-01 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e9af427c-7535-3a3c-a68a-5bf632810e1d | -8.7819 | -46.4399 | 2026-09-01 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 9cdb6fc8-53cb-31d6-aa4a-0686e56e8dcb | -12.9032 | -45.8382 | 2026-09-01 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| acc87862-3fbe-3c86-8024-3f3d74605e73 | -10.036 | -44.7056 | 2026-09-01 12:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 32c1ab02-b018-30e7-8acd-96c631960627 | -3.879 | -44.0576 | 2026-09-01 12:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 62e6f081-db50-31fb-9d3e-9775e0496b32 | -15.4429 | -52.681 | 2026-09-01 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 48dc8e39-c7d1-32a3-9c28-76973566f644 | -15.4235 | -52.6836 | 2026-09-01 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 6bba60cd-81f8-3511-8802-19f76b767b1d | -14.4587 | -52.5151 | 2026-09-01 12:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 1a4e899d-95ba-3985-aa63-28688dad24ad | 4.36505 | -60.89491 | 2026-09-01 12:46:00 | TERRA_M-T | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bb79a195-fca5-3ab7-b8cd-75976fbc3524 | -8.93711 | -62.3613 | 2026-09-01 12:49:00 | TERRA_M-T | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7e7d41ec-3b44-37d5-af30-01570302ff43 | -7.35804 | -60.58509 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 629e17a7-e37c-3994-9e21-4413656382e3 | -6.65748 | -59.42808 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a9eea2cb-b9c1-36af-8541-f8f4a7bcc09a | -7.30855 | -60.56169 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 167851ea-0299-3653-b9bd-29c6174038f5 | -3.51075 | -59.04398 | 2026-09-01 12:49:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a8d2204e-e6c1-3c65-b576-6663b5abafcd | -8.87976 | -66.88227 | 2026-09-01 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 82229311-c3ba-3628-8da8-3cb1d4fe3f0c | -8.27776 | -54.92161 | 2026-09-01 12:49:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 9100f725-8115-33e1-a63a-0f0702095e2a | -6.60211 | -58.59537 | 2026-09-01 12:49:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| fecba433-4d23-3021-9f27-a229681da40d | -3.13098 | -61.18076 | 2026-09-01 12:49:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3be45114-fdeb-31cb-8281-6fd2d97c9a5b | -3.12324 | -61.23553 | 2026-09-01 12:49:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 8d106894-d13c-321a-bcd4-d7a721b78560 | -7.189 | -60.69046 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8adf15f7-98f6-3e24-aaf9-64396f68a94a | -8.58899 | -66.9758 | 2026-09-01 12:49:00 | TERRA_M-T | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| aff07bf0-3b18-348a-b302-ab310324ee31 | -3.63487 | -60.55444 | 2026-09-01 12:49:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dc744835-3ae6-3e8c-9548-21bf50c9e8f2 | -3.34643 | -59.42437 | 2026-09-01 12:49:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6c7a0296-4e16-3590-84d1-f6ec0ab473e5 | -7.20152 | -60.67056 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| c85b4c7b-f03f-301b-9064-b26d2da74fcf | -9.83545 | -64.97732 | 2026-09-01 12:49:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0066e5fc-d241-371d-a5db-8e2f137c7fde | -8.2556 | -62.7534 | 2026-09-01 12:49:00 | TERRA_M-T | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e823069b-26ac-3600-84b0-5cc7d1271b3b | -6.94505 | -58.94573 | 2026-09-01 12:49:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ff340d60-e476-3b81-adb1-939b0d8bf464 | -8.53282 | -55.32278 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 250abd04-3420-39a7-9f99-56c11a36d16e | -9.46806 | -67.45111 | 2026-09-01 12:49:00 | TERRA_M-T | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9851fd9a-767a-3b63-be86-2f1e104f000e | -9.14989 | -60.93749 | 2026-09-01 12:49:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| aaa972b9-03b6-3ab0-80a2-2e410be12320 | -6.94523 | -55.62795 | 2026-09-01 12:49:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6caf6881-ce47-3a7f-a993-70672f4228af | -3.62561 | -60.55319 | 2026-09-01 12:49:00 | TERRA_M-T | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ce4550d5-3ba6-3b71-a596-1ea10f97ca84 | -9.1101 | -60.91528 | 2026-09-01 12:49:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |


[Clique aqui para ver as próximas entradas](README93.md)
