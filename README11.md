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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7b61bbc-99ec-3206-8307-3484feca59e1 | -6.5636 | -62.9096 | 2026-09-10 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 6aabd67e-7659-3298-8471-e804546197b6 | -6.5452 | -62.9102 | 2026-09-10 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 44ffb0ad-9e4b-3846-944d-4842a702324b | -2.7331 | -57.6271 | 2026-09-10 02:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 7f04bc48-8bcd-355b-8528-aac9be6336a9 | -6.5453 | -62.8914 | 2026-09-10 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 68d2facf-8d64-38ee-b30d-9c9cd5ab9ebf | -5.7569 | -45.084 | 2026-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 9f29740d-a669-3ec2-9394-613c732225ce | -6.7863 | -58.8995 | 2026-09-10 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| d6691751-1034-3147-961d-af3e95f4da9d | -5.7756 | -45.0826 | 2026-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.6 |
| 2deff3e2-c9b9-34d0-8a90-806cd405932c | -5.7567 | -45.1067 | 2026-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d352d1e1-3d52-394f-a94f-9dcd75a0b8a0 | -13.4453 | -43.8366 | 2026-09-10 02:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| c37f5019-8161-39ae-a3bb-e77956fd9328 | -20.5381 | -57.459 | 2026-09-10 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 05fd40f6-2bdf-30bb-b290-82a76b9b552e | -9.006 | -65.4 | 2026-09-10 02:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f199ac65-1a6f-3fd5-9e61-c587520ba35b | -5.7754 | -45.1053 | 2026-09-10 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 4a9069e3-7548-3875-a47c-e9f18a41c617 | -6.7864 | -58.8801 | 2026-09-10 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 8e4d93c0-3366-3547-a7ba-f44855b0b312 | -9.1626 | -58.3143 | 2026-09-10 02:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 5737acba-0af4-3178-96d3-3de16f14525b | -6.5637 | -62.8908 | 2026-09-10 02:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7a1f99ac-a363-3027-8930-e6f46f61b224 | -5.7569 | -45.084 | 2026-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 812abbdd-bbf6-34df-a20e-3642e901ad3f | -6.5453 | -62.8914 | 2026-09-10 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 4b3c8fb9-97ae-33eb-938e-8f252666b06b | -5.7567 | -45.1067 | 2026-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 16dcf71d-6cb1-3d5a-963a-97d439a594fa | -6.5637 | -62.8908 | 2026-09-10 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 4f47f516-434b-3fe9-bfc3-bd28d1b27175 | -6.7863 | -58.8995 | 2026-09-10 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| e0a71c81-c053-3854-9011-2f3e8a79ced8 | -2.7331 | -57.6271 | 2026-09-10 02:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 9f5ce468-36f6-3eca-82a4-45a3da0828aa | -6.5452 | -62.9102 | 2026-09-10 02:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| a3e2c89e-4e30-36cd-adab-f77f4ea617f1 | -5.7571 | -45.0613 | 2026-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 8574262c-a35c-3c51-8e95-27b932a8d4c6 | -5.7756 | -45.0826 | 2026-09-10 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 65575224-7e15-377c-91bf-61c6e9ee69bd | -6.5453 | -62.8914 | 2026-09-10 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 9191a6f8-1d63-3b81-9b7b-24f9d5875b05 | -5.7756 | -45.0826 | 2026-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 23cb506a-934d-3924-9937-9cefda260c30 | -6.5636 | -62.9096 | 2026-09-10 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 9d2a27c8-7493-3b5f-8ece-03e1f702a306 | -6.5637 | -62.8908 | 2026-09-10 02:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 1a4fdf8c-392d-34f9-9aed-19432e466581 | -6.7863 | -58.8995 | 2026-09-10 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 75a7ca4a-9fde-3bbd-afd3-591ca830a9f1 | -5.7567 | -45.1067 | 2026-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| ec5909f4-3873-3552-a535-8720e42d75a2 | -2.7332 | -57.6077 | 2026-09-10 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 7ffa794b-06ac-3d6f-bbfb-6c73bde00d7c | -5.7569 | -45.084 | 2026-09-10 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| 4dac689d-b049-3ef9-863d-3035e04ecd92 | -2.7331 | -57.6271 | 2026-09-10 02:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 0826af14-a788-3f78-8688-0de2b2035912 | -8.2379 | -44.7525 | 2026-09-10 02:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 3710b89c-6f5e-3444-8a56-9ab7b8909960 | -2.7514 | -57.6268 | 2026-09-10 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c1322f9f-68c9-3f33-9776-0acc3f575298 | -6.5637 | -62.8908 | 2026-09-10 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 842914f6-0af6-3e96-958f-d6f912c83ba9 | -6.7863 | -58.8995 | 2026-09-10 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 9f219e04-6185-3c18-b7bf-5a084f3bb5a4 | -6.5453 | -62.8914 | 2026-09-10 03:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 5b9883cf-70cb-3a52-a3c6-12511dce143c | -2.7331 | -57.6271 | 2026-09-10 03:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| cd44c782-cfd5-33ed-9536-8e61f10559d6 | -13.2678 | -61.6164 | 2026-09-10 03:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c72f350c-9938-387d-81a8-135363e8cc7f | -20.4992 | -57.3807 | 2026-09-10 03:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 3ab6c2a5-ec6f-32c0-868f-02bf75ad6358 | -8.2379 | -44.7525 | 2026-09-10 03:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 6a1437aa-8f70-3066-8fe6-9a49e1568f0d | -13.2869 | -61.6151 | 2026-09-10 03:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 7a3fb5bd-a819-3d89-8510-04029c105f7d | -5.7569 | -45.084 | 2026-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 163.4 |
| f7666715-ec52-3565-bf8f-78f2c9022ffe | -5.7756 | -45.0826 | 2026-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 191.9 |
| 41ac2d75-70c0-37ab-9814-b167f19353eb | -5.7754 | -45.1053 | 2026-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| f2a83e5b-273b-3d14-8400-c3b45f55ab5c | -5.7567 | -45.1067 | 2026-09-10 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 28b8c124-b856-3291-95e0-780407d8a3ee | -13.4453 | -43.8366 | 2026-09-10 03:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 967f955c-6d16-350f-899c-575012d11425 | -13.4453 | -43.8366 | 2026-09-10 03:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d2ddcf36-7fda-3768-8b73-5c8855af8681 | -6.5453 | -62.8914 | 2026-09-10 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1e67983d-ba9f-3340-8421-5cdc39f1fa5f | -6.5452 | -62.9102 | 2026-09-10 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| c3ea60e2-fb94-3785-85f2-0be0ee2bfbdc | -6.5637 | -62.8908 | 2026-09-10 03:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 9a7f4729-9c68-3131-b94c-d97f0e66a6f3 | -6.7863 | -58.8995 | 2026-09-10 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| ae009b85-e6e3-31b8-ab75-1486a6bc9eef | -8.2379 | -44.7525 | 2026-09-10 03:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 292aece2-a257-38b2-9cc0-7eb5017d890b | -2.7331 | -57.6271 | 2026-09-10 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 120.3 |
| b1a0807a-d479-3bd2-ab0f-8ce5cbe79c42 | -12.83 | -44.35 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db7e1d7c-834d-3ed5-849f-10b9f972278f | -12.89 | -44.37 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 193a3c79-addb-3647-9527-b9b1eb043ce0 | -12.83 | -44.4 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 440fa062-852f-36e7-b102-f51884cf44f3 | -12.83 | -44.3 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e63a5a85-b932-391a-8dbe-2938c40d1d34 | -12.86 | -44.36 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4e34aa33-7fee-3cf5-a4b1-5492ae41fc8d | -5.76 | -45.09 | 2026-09-10 03:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a17710a2-14f1-313b-91b3-74212a6fbaa6 | -12.86 | -44.31 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76e6c337-25a4-3170-bfdd-bc4d0ff7d882 | -12.86 | -44.41 | 2026-09-10 03:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f41cf03d-c7ad-353f-8f01-6132b67576cf | -8.2382 | -44.7296 | 2026-09-10 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 826b697d-3ce7-3876-b2af-e61f38ab2c83 | -2.7332 | -57.6077 | 2026-09-10 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 0b21b52c-ec0e-35ef-9f29-246827ae8d7e | -2.7331 | -57.6271 | 2026-09-10 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 570f7f1a-4d47-3338-99f4-b6c45137dadf | -8.2379 | -44.7525 | 2026-09-10 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 5b26fe25-601e-34da-a1d6-cd31e2bd0100 | -13.4453 | -43.8366 | 2026-09-10 03:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| dc8cd559-c1a7-36db-bae8-280a6687564e | -6.5637 | -62.8908 | 2026-09-10 03:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| eb0864bd-d396-351b-9762-197968fbabdd | 0.2483 | -51.4597 | 2026-09-10 03:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 9b727ebb-856f-335b-ab36-69c818dea0ce | -6.5453 | -62.8914 | 2026-09-10 03:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6e7ca3f2-c0db-3f2c-a938-c6546ef8cc44 | -6.5452 | -62.9102 | 2026-09-10 03:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 0329150a-193e-3fd8-ae55-2a86f0b75c27 | -2.7514 | -57.6268 | 2026-09-10 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| c249aace-3453-31c9-b8d3-924e78a39c90 | -2.7148 | -57.6274 | 2026-09-10 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e93bc5e2-d2db-3b3b-b03b-d668412d9cc0 | -6.5637 | -62.8908 | 2026-09-10 03:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2a8200df-6db0-3574-aef1-cddf5dc8fe84 | -2.7331 | -57.6465 | 2026-09-10 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 4af19314-dec5-38e5-8326-8c91d03b4552 | -2.7331 | -57.6271 | 2026-09-10 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 25bd432c-8ea6-3bfe-baae-eea6913ff37d | -6.5453 | -62.8914 | 2026-09-10 03:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| f5c420e2-3f7a-3224-be12-3e0b1c915a7a | -13.4453 | -43.8366 | 2026-09-10 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e1f72b93-0261-3cf1-997e-fa6c950b38cc | -2.7332 | -57.6077 | 2026-09-10 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a9bc43b2-be6b-38b9-9eed-2c1ca1c87cc3 | -7.04872 | -42.72753 | 2026-09-10 03:30:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f3c43836-577f-339f-b875-f7947ac16529 | -7.98105 | -43.99221 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d73f4510-0aee-3c7d-ba26-a991f53c4bd4 | -6.09335 | -44.14051 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90874390-79a7-3881-af7f-215061574efe | -6.16193 | -44.63897 | 2026-09-10 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6da67124-5f4b-3fdb-9c3f-50f491ec535d | -5.65577 | -44.29482 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5adaf9b3-0d7a-3a0d-9ef3-e9d66b2acbc0 | -7.1142 | -42.14794 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 94d0a6c5-5e03-3c48-bd20-e002e8e64e1c | -7.11938 | -42.11838 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0dd3a297-a30a-391a-870b-b27f890121dc | -7.11204 | -42.12468 | 2026-09-10 03:30:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 90a55933-226c-3377-8e73-1f93f451bcfb | -6.7649 | -44.56588 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 17d8d206-c6ad-3271-8478-1e6650803206 | -6.09433 | -44.13521 | 2026-09-10 03:30:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a245a871-0e79-30b9-a3d2-59c7941c8318 | -5.65483 | -44.30015 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ba28069-6201-3ab3-afdb-eaecd6539249 | -5.65525 | -44.29679 | 2026-09-10 03:30:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8eec20e-9f00-3c82-93da-3d982c689980 | -7.97766 | -43.97661 | 2026-09-10 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 79298ecd-ecb9-32a1-858e-07651d91365c | -5.77342 | -45.08179 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 4a07cbcc-1a31-31fc-91cb-18f81e57bca4 | -5.55405 | -43.43636 | 2026-09-10 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e5653f1-0635-37a0-9b89-7380fea19d62 | -7.50203 | -45.27175 | 2026-09-10 03:30:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3148bc1-1289-308f-b344-eacfe8477cb2 | -6.16849 | -44.64017 | 2026-09-10 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 6955b67b-dff0-3502-b579-494c188ef9c0 | -7.99159 | -43.96998 | 2026-09-10 03:30:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce9f00b9-613c-3063-9bc0-a5754776aa43 | -5.7574 | -45.09277 | 2026-09-10 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 07aab75e-82f0-3a47-ad1b-e91bbccbc5c3 | -7.98373 | -43.97802 | 2026-09-10 03:30:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README12.md)
