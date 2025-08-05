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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2706d05b-fd16-348d-b737-12d39ab7b6ae | -13.0723 | -56.9131 | 2025-08-05 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 6f96ad9c-0573-39fd-bffc-1ccca9900c28 | -13.0914 | -56.9114 | 2025-08-05 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8c70baa6-fece-3244-8c4e-96084393f276 | -8.9478 | -46.7354 | 2025-08-05 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e3179867-b100-37e0-8576-f69322e06027 | -13.0723 | -56.9131 | 2025-08-05 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 35a38274-9f75-3ceb-9867-eb62a7be25a7 | -13.0914 | -56.9114 | 2025-08-05 07:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 38b4b6a5-1136-342b-82a1-8cf5455c2d5e | -8.9478 | -46.7354 | 2025-08-05 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 071056da-f3f9-3ed0-8a70-8b04fe9d0458 | -8.9227 | -60.5568 | 2025-08-05 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f1239da6-c60c-3c05-b584-b9af5af70b52 | -13.0914 | -56.9114 | 2025-08-05 07:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ad53aef3-1c08-3098-9740-42b3f0653304 | -8.9228 | -60.5376 | 2025-08-05 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| eb98b253-5418-3e33-88c0-e0d9908016b0 | -8.9478 | -46.7354 | 2025-08-05 07:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 11fadb41-4039-32a2-91ed-b86f0bc16b86 | -13.0914 | -56.9114 | 2025-08-05 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c61f9317-a2bd-3be2-964f-85351aa157aa | -8.9227 | -60.5568 | 2025-08-05 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b388c913-7280-3b36-82d4-5baa4157865f | -8.9478 | -46.7354 | 2025-08-05 08:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 143c23f8-aa4a-36c5-907a-385a418b8aaf | -13.0914 | -56.9114 | 2025-08-05 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4ad5940d-b281-3794-80ab-c4be9c91c8bb | -8.9478 | -46.7354 | 2025-08-05 08:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f1e7b733-4140-3bd8-8787-7ba7417f554d | -14.2555 | -51.9899 | 2025-08-05 08:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 52709cf3-4dc5-3099-ab47-4d4d94727303 | -13.0914 | -56.9114 | 2025-08-05 08:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| e8cf544b-7d0c-3dcf-89fe-d62b03891300 | -14.2559 | -51.9686 | 2025-08-05 08:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f4c547d8-1726-3328-8fda-03a4d3d664e4 | -8.9478 | -46.7354 | 2025-08-05 08:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 7be4ac1e-beb3-305b-8eb5-37297c31a1b0 | -8.9478 | -46.7354 | 2025-08-05 08:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 6ccce142-5353-3772-bd48-b6d3dc2f46bc | -13.0914 | -56.9114 | 2025-08-05 08:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 01ba04d6-a7eb-3647-9621-7fc93633bd1b | -8.9478 | -46.7354 | 2025-08-05 08:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 610a4b58-e789-3e73-9e27-9009a84937d6 | -13.0914 | -56.9114 | 2025-08-05 09:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 212bc218-d679-3664-971a-1ed29e021fdc | -8.9227 | -60.5568 | 2025-08-05 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 4ad54a74-cec9-399b-8fa6-73a01cb3aac7 | -8.9225 | -60.576 | 2025-08-05 09:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8bc4dede-8156-3021-9f2a-8a794aa07970 | -8.9224 | -60.5953 | 2025-08-05 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 5f253c6d-aefc-34f7-b69f-f6e66eaa04a5 | -8.9225 | -60.576 | 2025-08-05 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 8dfa354a-0e97-3851-bab2-3f9a73e44438 | -8.9227 | -60.5568 | 2025-08-05 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 7b70d618-3508-38d6-9223-5c284e017efa | -8.9228 | -60.5376 | 2025-08-05 09:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 5a0d8ca8-405b-3bfe-805d-1115e967f039 | -8.9041 | -60.5577 | 2025-08-05 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| cace1bc6-18d8-3081-85a7-d351d27a80d1 | -8.9227 | -60.5568 | 2025-08-05 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 55906b08-fed0-3c9a-a4f7-c8f489e51a3d | -8.9224 | -60.5953 | 2025-08-05 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 243b0c39-3657-3919-a6d3-294443dae68d | -8.9225 | -60.576 | 2025-08-05 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 6d986770-894f-356e-a768-50e88154ad5b | -8.9228 | -60.5376 | 2025-08-05 09:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 46e1d69a-a565-3e84-98e8-6d0196c25d4e | -13.0914 | -56.9114 | 2025-08-05 11:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 682bd4f3-8568-3eff-89c4-9682dfdbc2c4 | -8.012 | -43.2219 | 2025-08-05 11:50:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| 49ff7f27-a1b9-3a66-b20a-813155dfe254 | -8.9478 | -46.7354 | 2025-08-05 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 27e512fe-78de-382b-a1cb-534f7156d1e3 | -8.012 | -43.2219 | 2025-08-05 12:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 2e74a140-0641-300c-960a-19acdc4a5def | -8.9478 | -46.7354 | 2025-08-05 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 67f1eab5-76d1-3135-bfd1-6586408e2a0e | -8.012 | -43.2219 | 2025-08-05 12:10:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 39a40c82-61b4-369a-b497-6891e0f2b903 | -6.78417 | -43.24939 | 2025-08-05 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f9d88d0c-9435-35a6-afd2-02e32af1082d | -6.27273 | -45.27468 | 2025-08-05 12:12:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 69738814-0d27-3989-ae18-d34d9716ca30 | -6.42178 | -44.82241 | 2025-08-05 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 82eb2989-249b-3af0-a3ea-6a46264ada99 | -5.79267 | -43.60673 | 2025-08-05 12:12:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b0f29ded-f4ec-3eff-a3b7-b1300a62611f | -9.57068 | -41.15363 | 2025-08-05 12:12:00 | TERRA_M-T | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 15a5a79f-e964-3907-b38b-2ee98fa6cd8d | -5.79004 | -45.09602 | 2025-08-05 12:12:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f8fe6324-3988-3bca-83d3-6271e77754bf | -8.29466 | -47.46847 | 2025-08-05 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6ec75171-3fde-37b9-896b-be936b45dc9d | -6.56206 | -44.22263 | 2025-08-05 12:12:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| aee369e3-954f-3b7b-8f03-cc390eed4ce1 | -8.00556 | -43.2208 | 2025-08-05 12:12:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 155.6 |
| 31a5db1a-61ba-3b37-ab65-09f5eb69984f | -4.99418 | -43.06276 | 2025-08-05 12:12:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8cf5daf2-e7fd-3788-b016-f5addb284fe5 | -8.38872 | -44.80854 | 2025-08-05 12:12:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 957a646e-1329-36b8-9764-19ba34407aa9 | -8.36452 | -46.55619 | 2025-08-05 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 687d4f50-ae18-3578-8c8b-ac2921a36813 | -7.57362 | -44.88903 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| f1d680a1-4678-3823-b1ff-5332f7082a00 | -8.53082 | -47.48035 | 2025-08-05 12:12:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dd19e42d-45f9-3691-af13-5b0823a75f64 | -6.56332 | -44.21381 | 2025-08-05 12:12:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5246467d-f284-380f-b120-c87ea284b142 | -8.32442 | -49.03893 | 2025-08-05 12:12:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 12.5 |
| c9eb53a7-750e-3d75-ab7f-2165fef5a1ab | -7.08699 | -44.36029 | 2025-08-05 12:12:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6be2df80-293e-34d0-a0e0-c2b6beebc347 | -5.68187 | -41.40333 | 2025-08-05 12:12:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 6cf4ac13-d569-36cf-884a-9f3d292ac5b7 | -7.06429 | -44.39316 | 2025-08-05 12:12:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b94dcf78-6766-3d59-830f-63c9f0355eff | -8.82997 | -45.58697 | 2025-08-05 12:12:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0ad92b0f-2d41-36fc-8397-6b2f85e57369 | -4.4453 | -39.0795 | 2025-08-05 12:12:00 | TERRA_M-T | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 25.7 |
| be680f48-d271-300d-9a16-a03032fadd4d | -7.5829 | -44.44919 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4aae9e81-f609-34f8-a6fa-8e4433bbffe8 | -7.84226 | -45.08721 | 2025-08-05 12:12:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c165f897-51f7-3abb-b8b9-6dba8cde262e | -5.68453 | -41.39887 | 2025-08-05 12:12:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| 1bb0e6c7-1038-3eac-896a-e6c26ced6a9a | -7.75475 | -44.01659 | 2025-08-05 12:12:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9327152d-ab67-30bf-8186-b91b07b232a1 | -7.41606 | -48.13413 | 2025-08-05 12:12:00 | TERRA_M-T | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b4c735c9-fa14-3289-997a-a9789477fa3f | -6.26386 | -45.2734 | 2025-08-05 12:12:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| dc88b851-963f-3ae0-8768-6ffb91fa8b3d | -7.1453 | -44.0792 | 2025-08-05 12:12:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 458667ed-aab7-33c2-9960-d5ae858adbaa | -7.57489 | -44.88021 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c9e33217-f059-30f7-99df-977480324036 | -7.37475 | -44.15747 | 2025-08-05 12:12:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 79c1496c-c82e-37a7-b68f-fc5089db2636 | -5.68345 | -41.39217 | 2025-08-05 12:12:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| f16133e1-b19e-3d0b-9926-841ab76c7445 | -4.80215 | -48.2648 | 2025-08-05 12:12:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| ff1d89de-5734-30e4-93ee-2052ac914e1b | -6.97484 | -42.87456 | 2025-08-05 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 814f74db-3798-305c-9bb7-06b32436961f | -6.76804 | -39.20164 | 2025-08-05 12:12:00 | TERRA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 845f1233-e8cf-33b7-97db-0e345b5b9a76 | -4.77829 | -45.33065 | 2025-08-05 12:12:00 | TERRA_M-T | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fff25bcb-4699-3376-ba30-54f0477d059d | -6.49975 | -45.55471 | 2025-08-05 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 25b4d03d-da86-32ed-9bad-5c8875acc5aa | -6.45109 | -44.55725 | 2025-08-05 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a11e6246-6d67-3e9e-895e-f0f008718eec | -7.56608 | -44.87896 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4b79424f-f499-3edf-808a-8feb1421cf3a | -8.00422 | -43.23026 | 2025-08-05 12:12:00 | TERRA_M-T | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 174aed97-6abb-3c77-9772-d981d75971e1 | -5.78379 | -43.60552 | 2025-08-05 12:12:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 8102481c-87b2-3169-8f78-872c50b6c469 | -6.50239 | -45.53672 | 2025-08-05 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8a5e8897-833a-319e-923b-a95e37cc0a9e | -8.24694 | -47.3343 | 2025-08-05 12:12:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a6ad335a-ec49-359d-ab8d-e90a752a4b8f | -6.77024 | -39.18512 | 2025-08-05 12:12:00 | TERRA_M-T | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 8c769d4e-6c03-34fa-9795-9da386a93b51 | -8.35546 | -46.55843 | 2025-08-05 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 1f83d8f5-e9b1-3fa6-8fb4-cbf951b2b406 | -7.94672 | -43.89939 | 2025-08-05 12:12:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7d3e6646-5adf-3feb-bd7f-d781f1c8af49 | -8.74222 | -46.43817 | 2025-08-05 12:12:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1a6690dd-e88c-3695-9081-16a5bd70781f | -7.36693 | -43.75634 | 2025-08-05 12:12:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d7e3d49d-e4bb-3065-af10-28bfd5714416 | -7.90503 | -45.53791 | 2025-08-05 12:12:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4dc7f5f1-df4d-32c4-b458-9ae6d8881c2f | -7.41122 | -45.31143 | 2025-08-05 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3e2b71d6-0b9b-353e-b1b5-d26333412267 | -6.97618 | -42.86492 | 2025-08-05 12:12:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 1d67c085-856f-342e-ba5d-1ccfc38868e8 | -8.36311 | -46.56564 | 2025-08-05 12:12:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0ec3db16-5b99-347c-891e-8914ecc332d5 | -7.94989 | -47.59365 | 2025-08-05 12:12:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 54d1ac05-0777-31d6-9951-7bdc47ea6eec | -6.42306 | -44.81361 | 2025-08-05 12:12:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 5db207b0-838b-3c0b-943e-27e0e575a1c1 | -6.35089 | -43.38068 | 2025-08-05 12:12:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 671748ef-bc00-314f-a7f8-2549278aed37 | -5.67397 | -43.53819 | 2025-08-05 12:12:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4ccff12e-0a65-3fa7-a1b7-f23aa09de06c | -8.83054 | -44.55205 | 2025-08-05 12:12:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 5bc318c8-a83b-3786-89c0-97ad52925b20 | -6.76727 | -44.98619 | 2025-08-05 12:12:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 182a2a55-5942-36e6-84ec-b6d1bbb742c9 | -7.58759 | -44.79204 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 31df534f-a408-3b68-9c25-3a6681959476 | -7.99804 | -43.14206 | 2025-08-05 12:12:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 3497a70d-5f7c-3472-a30c-efe087c5be0f | -7.38972 | -44.63482 | 2025-08-05 12:12:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |


[Clique aqui para ver as próximas entradas](README31.md)
