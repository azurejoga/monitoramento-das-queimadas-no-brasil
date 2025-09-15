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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3725e9b9-1bb7-3729-b19f-026146bab45e | -12.00872 | -47.75272 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5c69ef05-a475-3e27-951e-ea760160d8ff | -4.85959 | -45.73012 | 2025-09-15 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c6f296f4-0ee6-3b52-8ff6-875449c00ad5 | -10.79076 | -45.98136 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e6096b0e-2177-3a86-a60b-fffe5fc47b45 | -10.93367 | -45.50439 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3042907f-765d-3ddf-aee9-4f0e678fad17 | -11.44153 | -43.54662 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 34c71e56-9f43-31c9-8e22-6e1d38e01b93 | -5.63959 | -45.95189 | 2025-09-15 00:33:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| dccf894a-9831-37dc-94a6-cdc3d550e401 | -5.33115 | -45.8028 | 2025-09-15 00:33:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 21209bcc-e7a1-35ac-91fc-54179e982ba2 | -5.94091 | -44.86644 | 2025-09-15 00:33:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 50b135d7-bbd0-35b1-ba29-d09a5c4c3e64 | -7.69759 | -44.68745 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 93950a51-41f7-3ecc-bf74-012b5f1ae95e | -7.85105 | -46.11213 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3709c36f-6fb6-3d97-9bd6-5b0962b58416 | -6.68186 | -45.51189 | 2025-09-15 00:33:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ef2784fc-a0d6-3330-83ed-c8bb5e770fb0 | -8.64116 | -46.36135 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4160cb00-1551-31c6-952d-359d59b7f0a9 | -6.81438 | -46.93416 | 2025-09-15 00:33:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 11960b83-cf7b-34c4-adb2-56237b0d8f8b | -6.40667 | -42.6364 | 2025-09-15 00:33:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| f0921abd-493a-3f26-925d-4bddaf0ab344 | -11.35799 | -43.49298 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 38f80012-aae9-3b53-a16b-6bdb2a14ba51 | -9.01248 | -49.76992 | 2025-09-15 00:33:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3e87c704-d6f5-3eec-84b1-2c8a720f47b1 | -11.65378 | -46.59571 | 2025-09-15 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 7a3186b1-c0b0-3894-a789-58c7a52072c1 | -7.70997 | -50.35694 | 2025-09-15 00:33:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e4974694-6ae4-3632-846f-dce1114be5c1 | -9.00509 | -48.02446 | 2025-09-15 00:33:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a5db9649-1bfd-3ee2-bf9f-740b20e67e3c | -12.1616 | -47.59005 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6e4bc373-f679-372f-a6f5-79301fb2a1a3 | -9.00673 | -47.04405 | 2025-09-15 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| acbb095d-eb7f-3668-b950-4d962ca25d2a | -11.47964 | -43.61394 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 07d8657f-608e-3bf4-9a7b-8882266293d5 | -7.97439 | -45.65383 | 2025-09-15 00:33:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f6dedc7b-a7b8-3bf0-99b9-73fc63ae6f6c | -11.65508 | -46.60485 | 2025-09-15 00:33:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b0b9af0b-79d4-3131-8585-bf783e991fb9 | -5.28162 | -45.25335 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 0e62ccdb-5875-3afd-88f7-d3d905d20236 | -11.33 | -43.49042 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d3efe5fc-8b16-31f4-a95c-e9496e6fcdbd | -8.08129 | -44.50355 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 878ce409-a06c-3942-9130-9dea8601f412 | -11.33199 | -43.5036 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ff5942f5-e812-3da7-8c09-cfcfa7e327e1 | -12.00995 | -47.76171 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 8733761c-9011-3211-8bce-5fe34cf5e7e4 | -8.91255 | -45.49464 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 2471e9e0-4ea3-34d0-9688-914928dba77f | -8.10944 | -50.16793 | 2025-09-15 00:33:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 054f7f73-0d33-3fc2-8d5b-6e89fb0a1c00 | -5.34099 | -45.80137 | 2025-09-15 00:33:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f5e8d0c6-0787-327f-a287-19c9d79f6aa3 | -8.40079 | -47.25855 | 2025-09-15 00:33:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 752d3096-7b09-3502-9e08-1ac0b5aff445 | -11.34252 | -43.50187 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fb1e1162-948c-32d5-868c-892e2c8f544d | -7.39525 | -49.99643 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 45877717-8afb-3d29-a5d8-552f33d3501e | -4.32655 | -46.74302 | 2025-09-15 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.5 |
| be8a3afc-5fb8-3a86-a9e8-fafdb7328691 | -12.00112 | -47.76299 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| b679ccba-e485-390d-b073-80006fb99f04 | -11.33692 | -43.49633 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 6bc71442-1699-35de-83e7-ec96a7b2f025 | -8.91898 | -45.47178 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8ef9617f-50c5-313d-a01c-0dd00ecf98b4 | -9.04762 | -45.72298 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 703b45f8-7f2d-30fb-b74b-256f6a362f34 | -8.91563 | -45.51569 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e2fe3d9a-275a-3954-b54b-e14a0cd6272f | -7.69463 | -48.87215 | 2025-09-15 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24c03c4a-b6a0-31de-aca5-42b20dc79394 | -10.74508 | -44.78691 | 2025-09-15 00:33:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8bb71262-59ad-3aa9-bd65-bb77900dab5e | -7.535 | -43.98944 | 2025-09-15 00:33:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2333be0c-feb6-3651-9e5c-98f9133cd37b | -8.89887 | -46.16594 | 2025-09-15 00:33:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e43496c-2e7d-330a-bbba-a8cb10e1c641 | -12.00559 | -46.66737 | 2025-09-15 00:33:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 723a8f36-bceb-3218-96c8-dfbdb45b57c4 | -8.99382 | -45.78876 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 22526c9c-5d5a-3691-b3fb-066c4d6358ab | -8.96567 | -45.7932 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| de3e442a-a116-331a-9759-2d8cb4c5b232 | -7.64536 | -49.73304 | 2025-09-15 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 4eb62ba4-93d4-3b69-b358-b83cc8f4b04e | -8.19222 | -46.76556 | 2025-09-15 00:33:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0def8f88-863e-3a95-9140-afbd230d5e95 | -9.72756 | -46.8609 | 2025-09-15 00:33:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8814439d-0747-3544-bc2b-4687c36b4598 | -11.39451 | -43.6596 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4220afd4-8b2e-3d03-8346-cf95023690c1 | -7.63758 | -49.74361 | 2025-09-15 00:33:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3120ff64-516b-3b43-9671-dd2d33f4b2cd | -7.70347 | -48.8709 | 2025-09-15 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bf1164d4-cb92-3712-964e-01879f88f970 | -8.18317 | -46.76685 | 2025-09-15 00:33:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 253675d6-5305-39f9-9b4e-49c886c8c18a | -12.65653 | -54.69865 | 2025-09-15 00:33:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 8c68ef06-2d11-3958-97da-5cb86fdc3071 | -6.9164 | -46.15694 | 2025-09-15 00:33:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 14b67c29-091f-3cde-b81d-5ee6c0c69901 | -7.86589 | -43.57361 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 327.3 |
| 92fe879a-6d91-30d1-af25-d504f213bd9b | -6.97788 | -44.54579 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 804e507e-52a6-385f-b993-a86c657d8b57 | -7.69582 | -44.6754 | 2025-09-15 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 2ad82850-9a7e-35db-8b9a-6018f0c8c6ac | -5.18839 | -45.1732 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| e89a1621-b5f3-3aeb-9fa3-b77dc9221581 | -10.66198 | -46.23733 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9103f87f-6bc2-3ad8-a165-69ef6ab1475a | -11.4049 | -43.65788 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| e136ad13-3d80-3983-9ff2-0128b6f2de38 | -10.67035 | -48.67838 | 2025-09-15 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe708f94-49ea-3f3b-ad65-77cd566ea490 | -7.69342 | -48.86325 | 2025-09-15 00:33:00 | TERRA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 36.4 |
| ab9ee2bc-02c5-357b-8959-77f1331aa244 | -8.99092 | -45.76854 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 53543d6e-4148-375c-b23e-6dbe1df9c928 | -10.86356 | -45.46012 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 164795da-cf46-31ec-8f47-d2e5c17e0037 | -11.34055 | -43.48871 | 2025-09-15 00:33:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8b400ec7-90ea-3d50-aece-e04da1cd7056 | -9.00802 | -47.05313 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 266c63cf-4de2-312e-9f6a-e068512bcc97 | -11.99989 | -47.75401 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 25da1646-2e62-338c-907f-cd30a40e243a | -7.22125 | -49.59703 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5a0bc62c-1ab6-33fe-b375-5c55adc5d57f | -11.7637 | -46.65718 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b170ec3f-76e8-394f-b3b1-d7cbbe39f71b | -12.07471 | -47.56332 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 45b155b7-cc33-391c-a045-ac08b2643a29 | -4.41095 | -47.60863 | 2025-09-15 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8ab3d542-db20-38d8-834c-8c2e918fe767 | -5.47565 | -44.68964 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 788e2031-05f5-39d2-8096-afcce35ab2e0 | -10.68275 | -46.2532 | 2025-09-15 00:33:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 92a4c43e-dbb4-3366-ab5d-bd201d81c2f9 | -6.97069 | -44.53972 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 344ea93c-2a4d-3ba7-87f8-4dc07f694eae | -5.70147 | -49.20336 | 2025-09-15 00:33:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e7be80af-d5a7-3155-a756-245ecb56bd7c | -11.77234 | -47.57068 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d8abd931-a8b3-38f2-a56a-10b1f98d3ce4 | -10.0779 | -47.18876 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f582ffa8-ee8e-31c9-82b0-42d72fb2f96b | -7.40436 | -49.99518 | 2025-09-15 00:33:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a0d02db9-d142-31a4-a97a-9491c38e676c | -8.90455 | -45.50671 | 2025-09-15 00:33:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d45fa988-a4eb-3a0c-bd18-5e56b7604cb1 | -9.00931 | -47.06222 | 2025-09-15 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4bce9b3-bb3e-3bf9-916f-a5b81419fda3 | -10.74347 | -44.77608 | 2025-09-15 00:33:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 94272b97-8ac2-3e67-a346-3bf6d94489a6 | -7.857 | -43.58981 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 480.5 |
| 14f6daaa-f550-3980-8fe9-1b116256e94c | -10.92435 | -45.50583 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 085c911c-382f-38e8-87bf-240357ad025c | -5.74248 | -43.92484 | 2025-09-15 00:33:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 07524992-df63-39af-83fa-3337f2aaeeb5 | -5.20068 | -44.31714 | 2025-09-15 00:33:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4d6729a0-a8f5-3093-ba53-7de55696b9c0 | -11.37626 | -47.71381 | 2025-09-15 00:33:00 | TERRA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d2b0b6a3-8271-3d7b-9da9-006f46e9049e | -6.97256 | -44.55259 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ff022596-a9cc-3dc4-b062-aa5311aaf17a | -11.77258 | -46.65588 | 2025-09-15 00:33:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45470b35-f38e-364f-a557-140622664ccd | -7.85676 | -43.59621 | 2025-09-15 00:33:00 | TERRA_M-M | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b16f354c-48da-38a3-a2ba-cf8b0f6a55fb | -10.40338 | -48.61427 | 2025-09-15 00:33:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 08082488-c672-3427-be21-116b62ebcfb2 | -11.77868 | -47.55149 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 27bf91c0-744f-3112-9377-869ec4183952 | -5.15373 | -46.00473 | 2025-09-15 00:33:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| b31d0358-3a63-3273-9d24-8e0ee6deb204 | -11.77992 | -47.56044 | 2025-09-15 00:33:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 59af3159-2ef8-3777-98ba-ed428f98e227 | -6.15615 | -41.18987 | 2025-09-15 00:33:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| a15c8a53-fdd0-379c-ac16-5d22fd4a6601 | -10.89013 | -45.44557 | 2025-09-15 00:33:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 53b9ad2a-b353-377f-960e-0ccc467470b3 | -6.98114 | -44.53778 | 2025-09-15 00:33:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d61c5af6-b9a0-36ec-9e41-2554dc9a92d2 | -10.90619 | -48.18372 | 2025-09-15 00:33:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README5.md)
