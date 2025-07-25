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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1c33ddf-0938-33a1-b825-eee722728419 | -2.91165 | -48.25038 | 2025-07-25 04:19:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a60ece6f-1748-39e7-865f-105536a118d5 | -2.99432 | -49.31913 | 2025-07-25 04:19:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bc15f1a-fb9f-361d-bb30-391c51e67de9 | -4.44688 | -38.44535 | 2025-07-25 04:19:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c51aca7e-d8c0-3cfc-a445-f33f4a84edf9 | -2.86194 | -46.77013 | 2025-07-25 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60bdf425-75ad-3fbc-8f97-6e9cf412978e | -3.32409 | -48.71965 | 2025-07-25 04:19:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7411aec6-7145-3982-816f-9ba954eebfd6 | -7.2597 | -43.0645 | 2025-07-25 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| a5184232-2d28-3e15-be40-233a0d896a91 | -11.4584 | -45.1126 | 2025-07-25 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 2616fd5b-26a8-3b88-9348-5a39cb9c8c84 | -6.6754 | -43.96294 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64eaa378-33fd-3cfd-9a28-ac5505f03910 | -9.85469 | -44.70607 | 2025-07-25 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 71be60c4-86e4-3eb4-a2e3-d83dad2ccfc1 | -6.13713 | -42.96006 | 2025-07-25 04:21:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 255ca64b-2b4f-3789-9921-abf1866c0ac6 | -6.34087 | -43.75003 | 2025-07-25 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 86eacd92-6469-30e0-9584-252784fe8df3 | -6.9502 | -44.56286 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 106e4f59-f69c-3768-bb7a-afbb54f6d35d | -8.09576 | -43.15343 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| edb8d1b3-3c88-3cd4-944b-9b5b0b5cc7e6 | -8.06816 | -49.71609 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bd6a9370-5031-39c6-b78b-9f3ddd1e6ddd | -10.4168 | -47.1962 | 2025-07-25 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 018bea6a-44cb-3c89-8418-3a6618692c9b | -9.59438 | -43.86996 | 2025-07-25 04:21:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 21de071b-7ebc-3e1f-a408-ee1b5aea1062 | -7.91821 | -44.08133 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6797560-f904-3b45-8e98-2d6ea908e331 | -4.1054 | -48.20481 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcbd1ea9-87b8-305e-8b12-8ef6b2e0b97f | -6.99163 | -43.32022 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 39fc183e-3695-3ffd-950d-d595b2a0edd7 | -11.46364 | -45.11959 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2f91fa89-dbb5-30fe-9f02-dce11f589399 | -7.92994 | -44.09403 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33cffeec-52a8-3eaa-8a88-6ffee306883d | -9.59226 | -46.3233 | 2025-07-25 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74d5b1bc-9e98-30f7-aa88-6aeeaa058e20 | -9.85524 | -44.70255 | 2025-07-25 04:21:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1281932e-acec-3e68-b407-9740e91a1205 | -6.99106 | -47.08389 | 2025-07-25 04:21:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dc9f8e1-e420-3fe6-b7c2-4b8b0a4152f5 | -8.09233 | -43.1529 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 95a0d2dd-b1e1-390e-b68c-49568bd41b38 | -7.2603 | -43.07281 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5077d751-6aaf-317d-b803-d26ea1d484aa | -8.30342 | -44.97324 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dbeb4d3-5aee-3e99-be9d-01113b96c66d | -8.16105 | -42.81907 | 2025-07-25 04:21:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f2312622-4d44-32cf-b203-70dc71b73f3d | -6.34733 | -44.10212 | 2025-07-25 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68c7f52b-54fe-398a-8913-fcf7f5ebb38b | -7.91712 | -44.08841 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6bdf7bd6-958a-3a7b-9194-4090d64e49c0 | -10.74267 | -48.18528 | 2025-07-25 04:21:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 32b345e8-9a32-38ae-82d9-1cf2c1028fb9 | -8.20412 | -44.9362 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 708f5272-f667-3ddb-a370-2fc8d8db4587 | -11.45975 | -45.1226 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 98c24141-606f-3db0-a7ff-9d26535eb3e9 | -6.18444 | -40.8779 | 2025-07-25 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 39407698-020c-32df-8675-6746122c61c6 | -7.11179 | -47.84071 | 2025-07-25 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6eb0dfca-e985-3552-8983-6d948e95e067 | -7.26144 | -43.0654 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 52287fa1-773d-343f-8535-a0a6e7d31afe | -6.911 | -44.97933 | 2025-07-25 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff2646ba-fbf4-3722-8242-572568046087 | -7.94106 | -44.08854 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9c5e345-0e35-386a-b602-4b39d2ff973a | -7.84475 | -44.21088 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce4f8156-b997-3e75-90b5-c28745df0698 | -8.51128 | -43.31081 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a57f87fc-e2d1-3366-893f-772cf9fbe74f | -9.02789 | -45.33493 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 020155e0-5a30-3389-91d4-8955714da4f0 | -7.84864 | -44.20788 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90b1a5fe-97cc-3da4-bdd8-33ffd931a62f | -6.92462 | -44.22745 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fca65f1a-8d4c-3a73-b943-e878c9ad4eee | -6.56762 | -41.4982 | 2025-07-25 04:21:00 | NPP-375D | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbf6ae1a-cdc6-311a-99c2-cfc9e83c9e6d | -3.24572 | -51.10443 | 2025-07-25 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 007dac4f-f444-398d-94d3-d12dd09c8eb3 | -7.92715 | -44.08996 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7aac3b1-c870-394e-aa9a-5b0bc788ba43 | -6.89244 | -42.83608 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6fb9ae61-4cc6-3fd8-92d2-5142e5ca2861 | -9.5917 | -46.32684 | 2025-07-25 04:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9445512-a7dc-3b4a-868a-00c36c2ae7ef | -7.11537 | -47.84137 | 2025-07-25 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 22188c9b-9331-3c3b-810a-0a1206e28f15 | -8.89202 | -45.57447 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 8adb09a0-e60b-3285-8320-00d9df68b08e | -8.84157 | -45.59504 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d29b5a2-5dec-3cec-ab51-de324098c3c8 | -6.73887 | -49.64566 | 2025-07-25 04:21:00 | NPP-375D | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63ca2635-076e-3958-b8cd-6962610a583b | -7.90709 | -44.08684 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 54adbd3f-ff15-39f1-9fb1-5fe8b14c53c5 | -6.02033 | -42.92375 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 362ad0f4-dd7b-3d83-9699-92fc30b30c8b | -7.49814 | -49.22263 | 2025-07-25 04:21:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c9462bf-bf5c-390e-8e49-3bcb498a80ed | -6.47433 | -43.48815 | 2025-07-25 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e9fb951-1060-30a7-a36a-ae6363d6f1bc | -8.06728 | -49.7212 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bea4447-b48f-3d40-a675-6b9112a57851 | -7.88789 | -45.54249 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16f37713-cde3-39ac-b5e0-6d789210f96f | -5.48443 | -42.15329 | 2025-07-25 04:21:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3f33df8e-9d16-355b-85f8-e91a339bd5b6 | -8.07464 | -43.15395 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a4ceeb94-c34e-3629-9e08-a3c0b63d9154 | -5.28163 | -44.94935 | 2025-07-25 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd4b1b55-8648-3aa9-8438-eea6d454b0c0 | -6.94743 | -44.55887 | 2025-07-25 04:21:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c814da4-b4bc-3a13-bf74-cf3a121d1f73 | -11.45865 | -45.12969 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d43d4521-ad63-3496-87c8-6dfb60a827a3 | -9.0522 | -46.62181 | 2025-07-25 04:21:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb5030e9-e58e-36ba-9288-93dbd765c079 | -8.12696 | -50.46865 | 2025-07-25 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 333e8416-8d4a-385c-bf97-eb299885c2a6 | -5.30377 | -44.89587 | 2025-07-25 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d80fbcc-c9dd-3f78-bd1e-2ead7e16dcd5 | -8.08149 | -43.15503 | 2025-07-25 04:21:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e10749c6-7540-3ac9-a654-6322a3c3f745 | -6.19816 | -44.38488 | 2025-07-25 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb58a13f-3eb1-3911-9e02-aa5d45961aeb | -7.91323 | -44.09142 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c93782e-2ec5-3813-ad3c-f9389b2462d4 | -7.53247 | -42.43031 | 2025-07-25 04:21:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 14b4c2dd-370f-3a4e-aa15-64ebe7803421 | -7.26486 | -43.06593 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8e74a4f0-2553-3849-9a90-ea9a03a3aa41 | -7.16337 | -43.47523 | 2025-07-25 04:21:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d6c9ab3-4b42-3e9f-aa62-e32911b93cc5 | -7.90654 | -44.09037 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5623be3-8756-343c-88c5-441be09e4fb9 | -7.15301 | -46.09184 | 2025-07-25 04:21:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ffa2d2a-9106-3971-89f3-f12211c3077f | -6.5407 | -43.46551 | 2025-07-25 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6cb8239e-531a-34e0-9465-bd972dc61511 | -7.82041 | -44.56176 | 2025-07-25 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c8df3884-b64f-3598-927a-eea1d6c0a94e | -5.99226 | -45.72924 | 2025-07-25 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afa9a078-157a-34bc-a149-c9911f27116f | -5.8366 | -46.15903 | 2025-07-25 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9fa1a0a-4a51-3375-9832-f90bddf26394 | -8.07331 | -49.72055 | 2025-07-25 04:21:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 849aa5d6-5a74-3e91-9e55-69100b5f8879 | -7.88512 | -45.53847 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c7e59f41-aa22-37bb-a3e8-ae7387289dac | -11.45144 | -45.13218 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dbc733c-f08c-30cd-a990-55ddb836d57e | -7.91098 | -44.08382 | 2025-07-25 04:21:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0b8c78c4-f9d4-3681-8237-74124475cdc9 | -7.26087 | -43.0691 | 2025-07-25 04:21:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f787cb91-de45-356d-8f5a-c09e232f9a5c | -9.13531 | -49.66917 | 2025-07-25 04:21:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45f39342-625a-373a-8b28-83059ab2c614 | -7.86368 | -48.21902 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d1be8ed-a3b9-31c0-9854-53ff6e37c56f | -7.85502 | -48.22631 | 2025-07-25 04:21:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33edc1b8-6de3-382c-8de2-13a42785fc46 | -4.03593 | -48.06297 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 100c69ff-7d10-302c-8ad9-7a3f6675673c | -11.45642 | -45.12207 | 2025-07-25 04:21:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 075fd05e-3fd3-3770-bc2e-9d68b15910b0 | -10.4208 | -47.19305 | 2025-07-25 04:21:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 31b44a26-d63d-3cf8-ba64-263a6c2e1bc7 | -6.18816 | -40.87851 | 2025-07-25 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5aed936e-1177-3416-8bfa-bd4373ff9236 | -7.88568 | -45.53498 | 2025-07-25 04:21:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1eece21a-b58c-3b04-bcc5-4916482364bc | -7.48109 | -49.2297 | 2025-07-25 04:21:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 694a855b-5f98-33d4-be0f-a60c7726ff17 | -8.67203 | -51.21413 | 2025-07-25 04:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9651760f-7d3f-307f-bfbc-69934216f71a | -4.35178 | -47.68867 | 2025-07-25 04:21:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| d3393dd3-7f2e-3b6a-9641-f5d89535c0d5 | -10.50339 | -44.88018 | 2025-07-25 04:21:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48055a7a-388f-3778-90cf-672be333d142 | -8.88039 | -45.58336 | 2025-07-25 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aadbe7d5-a9d5-33bc-95a5-de16e76a2cd4 | -9.34573 | -49.91581 | 2025-07-25 04:21:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9e74eb9-cb26-3c1d-b94e-b4aa3ce9761d | -9.00743 | -45.33524 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e68ecbf-6870-3dd8-844c-0484f549b95c | -6.91426 | -44.29367 | 2025-07-25 04:21:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1204f35-bcc4-3db1-8bbb-2f3d6ea1a1f7 | -8.20357 | -44.93968 | 2025-07-25 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README13.md)
