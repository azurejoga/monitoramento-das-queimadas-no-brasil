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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e30644b-4f25-31c4-8800-e3abf46128bb | -7.46458 | -43.96721 | 2025-08-11 00:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 83c5382c-9aa0-3b76-b8e1-f4ee0eeabf52 | -7.46301 | -43.95624 | 2025-08-11 00:28:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| aecbc3f9-876d-32a4-8e66-9c34ad139877 | -5.48977 | -44.39452 | 2025-08-11 00:28:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 5ff159c3-a73b-3fa8-b9e0-272df963c7ea | -8.48952 | -46.00102 | 2025-08-11 00:28:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66239127-9c19-3c43-9fd3-c1de85a3acdf | -8.9399 | -60.7481 | 2025-08-11 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| c4ae7134-37cf-37ba-b7c9-d6ad87accc2c | -7.0799 | -59.1964 | 2025-08-11 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 2de7b627-6b80-3e29-9263-168e066c5166 | -7.0797 | -59.2157 | 2025-08-11 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 41bdda22-8e4c-3952-829f-d4e113841ba1 | -9.3806 | -61.5315 | 2025-08-11 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 70731b99-6dc6-346e-bb1e-6f8c2ed4c071 | -18.8629 | -48.6551 | 2025-08-11 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 0ae86bba-0805-30ca-a2ab-7aa36549bff8 | -7.0613 | -59.2165 | 2025-08-11 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 45935ec4-9a74-3741-9ad5-f439bae53e72 | -7.0614 | -59.1972 | 2025-08-11 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 168.5 |
| cb8b15fb-971a-3639-9c5e-207a973b9ea0 | -18.6293 | -46.8394 | 2025-08-11 00:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 610c2f2c-1731-3b06-93b5-8b7b08e9fab6 | -8.9215 | -60.7297 | 2025-08-11 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| fd04c851-9083-3075-acf1-6ccbd5c3a478 | -18.8422 | -48.6821 | 2025-08-11 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 775a1cd5-cfbb-354f-aa8a-95cc61ef3aa8 | -8.579 | -54.696 | 2025-08-11 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c61663c4-3ff6-3cd6-9554-aa27ba2ddc49 | -8.9401 | -60.7288 | 2025-08-11 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 64bfeee5-5bcb-3c2e-9938-6d0ed3f0154f | -18.8428 | -48.6592 | 2025-08-11 00:30:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 221cb1ff-d8e2-3976-b405-4389c83269b1 | -8.9213 | -60.7489 | 2025-08-11 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| aae6540d-cb22-3035-8d81-508d28117f6a | -8.5604 | -54.6973 | 2025-08-11 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c559b5c2-daba-3b14-b8a1-326f15f51fe8 | -3.22261 | -49.34074 | 2025-08-11 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 278ae909-7460-3a5d-948b-2d9e587737c2 | -3.22391 | -49.35017 | 2025-08-11 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 61017de9-56c2-3b3f-8022-02e89c8913b0 | -3.42151 | -49.04753 | 2025-08-11 00:30:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 899d169a-4e47-38d0-81bf-55c64f2d2a3f | -4.30122 | -48.07433 | 2025-08-11 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a82b795a-d9f7-3eac-9680-289d2b489d93 | -4.11449 | -48.12178 | 2025-08-11 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c845393c-9b54-320d-a498-0013d7ee223a | -4.3 | -48.06547 | 2025-08-11 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 15d356ac-a817-3d20-9969-efd0c41b599a | -4.10572 | -48.20185 | 2025-08-11 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8dce3866-401e-326b-a0f9-3f1f2f3b4789 | -2.33181 | -48.62028 | 2025-08-11 00:30:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 66e00988-27cc-369a-a003-8700a2ecf897 | -4.06012 | -46.93534 | 2025-08-11 00:30:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1db3d011-71ac-3c64-aab1-0595e1f62c5f | -4.1166 | -48.20307 | 2025-08-11 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 58ae82b4-711a-3e43-b8a1-c2dacf48529f | -2.9638 | -49.06641 | 2025-08-11 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db53bcb6-1d53-3e06-a7b7-bea6403e1e7d | -3.43056 | -49.04628 | 2025-08-11 00:30:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 53d88b29-961f-3ee8-9c94-1f0f9bd0920e | -3.43183 | -49.05555 | 2025-08-11 00:30:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 79723c5b-22b8-31ed-987e-3ef1845be219 | -18.6293 | -46.8394 | 2025-08-11 00:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| faf0fead-4511-3cc1-b14c-ff76ee77601b | -8.5604 | -54.6973 | 2025-08-11 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 34c1e06a-981b-3f2c-afbb-2bfbbf3fefe3 | -8.579 | -54.696 | 2025-08-11 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 4b99c14a-4793-3c7d-8df1-3b4835cf75c7 | -8.9399 | -60.7481 | 2025-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| a610e87f-de2b-3f5a-bf8b-de1bc5cc66f1 | -18.8422 | -48.6821 | 2025-08-11 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| c0f574de-c942-3d19-9239-fda34a7ed82b | -18.8629 | -48.6551 | 2025-08-11 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 5d488b60-a563-3b91-ba04-7eb451e04627 | -7.0614 | -59.1972 | 2025-08-11 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.3 |
| fe0b9ac0-a600-3948-8d2f-c75037d17115 | -8.9401 | -60.7288 | 2025-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| ac67e849-5b8c-3a56-89fd-1c47ab024c9a | -8.9213 | -60.7489 | 2025-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 2d728ef8-670a-34f6-98ba-141756a80e48 | -7.0799 | -59.1964 | 2025-08-11 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.2 |
| 6993fcf9-d661-337f-b831-661a4c8aca94 | -9.3806 | -61.5315 | 2025-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| af38f12d-f5b7-3b4c-a5d9-69b84b940840 | -7.0797 | -59.2157 | 2025-08-11 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 073d9f32-79e6-37aa-9605-b13d1adca0df | -7.0613 | -59.2165 | 2025-08-11 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 140cdad8-feed-3876-aa60-4e43f2c75367 | -18.8428 | -48.6592 | 2025-08-11 00:40:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 53b2ad61-395c-31b8-b037-add8d5a2fa82 | -7.8773 | -44.972 | 2025-08-11 00:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.2 |
| db89ee45-197a-306f-b41a-8f50e787c554 | -8.9215 | -60.7297 | 2025-08-11 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 9efbd82a-e0fc-3143-b92f-45ab180dc9ca | -8.5604 | -54.6973 | 2025-08-11 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 3cf7d9ba-e315-315f-b801-61705c691465 | -21.0536 | -50.0356 | 2025-08-11 00:50:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.7 |
| 14984ab7-b3af-3d92-906b-b9b5325333b8 | -9.3806 | -61.5315 | 2025-08-11 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 62731f12-26fc-3ff5-ae15-09f5f50ddb0a | -7.0614 | -59.1972 | 2025-08-11 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 36b1bc0f-d758-3761-8ed2-600f59dfaabb | -21.2521 | -51.033 | 2025-08-11 00:50:00 | GOES-19 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.9 |
| 638b7620-ee7b-3afa-8691-441a5dcb0453 | -7.0613 | -59.2165 | 2025-08-11 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| a9f53ef8-3217-3fee-905e-c3ffac13474b | -7.6113 | -45.2026 | 2025-08-11 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 9d7cf7b3-93e4-3926-903e-e7a303b6acae | -7.6115 | -45.1799 | 2025-08-11 00:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| dcd14ae5-bf76-342f-9572-285dd97dc37e | -18.8428 | -48.6592 | 2025-08-11 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| c519bb4d-909a-3653-b433-61381e4bd93b | -8.9215 | -60.7297 | 2025-08-11 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 5d53424d-56b4-35aa-b2cc-46955f1fab74 | -9.4761 | -40.3862 | 2025-08-11 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 9c228f52-64b9-322c-8584-6e8203e42b75 | -7.8773 | -44.972 | 2025-08-11 00:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1501aea1-c57e-3691-8fb2-80244554abb8 | -9.457 | -40.3889 | 2025-08-11 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 0bfde577-a911-36f6-b705-9d3ceb867048 | -21.0542 | -50.0128 | 2025-08-11 00:50:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.6 |
| f37b3f66-c978-3b10-b31f-15388f8b90ed | -18.6293 | -46.8394 | 2025-08-11 00:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| c51f9765-8e0a-3021-89c6-56c6ee556a46 | -7.0799 | -59.1964 | 2025-08-11 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 166.1 |
| 9d4131bf-d2d3-3996-9ea9-e9c60df1c418 | -7.0797 | -59.2157 | 2025-08-11 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 43e384f3-2e34-3915-84a0-8fdddeea1851 | -8.9399 | -60.7481 | 2025-08-11 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| acbd8993-6828-3590-a105-d57c3935bc6b | -8.9401 | -60.7288 | 2025-08-11 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| e8e03c3d-7d48-3e6c-98aa-a7043dee21ff | -8.9213 | -60.7489 | 2025-08-11 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 98778d4b-d3c6-3b7e-a4a9-c8854ec8365e | -8.579 | -54.696 | 2025-08-11 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| cfd775a6-6744-3573-af23-eca8d8d8ade9 | -18.8422 | -48.6821 | 2025-08-11 00:50:00 | GOES-19 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 18d310cf-9690-3b94-b6f8-d672e0b2502d | -7.2614 | -59.9893 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a550c64f-900a-391c-a57c-52cee13a20c7 | -7.0851 | -59.1936 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 76150d5e-e246-32cc-bb2f-5c3b44dff1f6 | -7.0758 | -59.1521 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d30c10c6-a564-3a32-be69-fd42aa8eaa24 | -3.4155 | -49.0303 | 2025-08-11 00:53:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bae6e52-57dc-30a2-9405-1006a3cf0a39 | -7.0804 | -59.172798 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 64744e19-d7b1-3061-b907-30feb9a5855e | -6.1033 | -59.915699 | 2025-08-11 00:53:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0420cafb-f5b8-3639-8c77-99eed3d6ba9e | -7.0691 | -59.168098 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a56d931-9c90-3ed1-bc9b-7b7959294637 | -8.5548 | -54.691399 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e8dd727-0888-3597-9a7a-36c6cdf7c63e | -8.932 | -60.7234 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf77115a-7825-3a81-91b6-3e9bb2ca6eab | -7.0722 | -59.181999 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 978c945a-22b3-3334-83d3-b09d936d9036 | -7.0577 | -59.163399 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 80c50b47-4c91-32bb-80a4-f78b5fb253bf | -18.8333 | -48.648102 | 2025-08-11 00:53:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dfdec0bb-453f-33fe-bfb7-024309c58b9d | -9.3868 | -61.503799 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3553abad-af28-3977-b928-a7112ecda3ea | -3.4059 | -49.0326 | 2025-08-11 00:53:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bcb128a-5e47-3a13-8b31-2660361551f8 | -18.5989 | -46.821899 | 2025-08-11 00:53:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ccb56994-6760-328f-9a7a-9b36e776e62b | -8.5666 | -54.697701 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c08b74d0-37ec-3748-b002-ccfda0b050d1 | -18.8237 | -48.650799 | 2025-08-11 00:53:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d09b0ea6-d0bb-391a-855b-eb8a08da3c15 | -21.052401 | -50.025101 | 2025-08-11 00:53:00 | METOP-B | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 48b1d713-ff95-32dd-ab1f-22757ea907e1 | -7.0706 | -59.174999 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3992b2bb-7ef6-3e34-a24b-427a4b7fa90a | -8.5703 | -54.669399 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb4a8e89-2f2d-3761-bc0f-1101815a5fc8 | -7.0655 | -59.198002 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59504c51-42c1-344f-beb5-1830c8d87cad | -8.5626 | -54.680401 | 2025-08-11 00:53:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a250af6a-5ab4-3392-9c84-13d5403f5428 | -7.0624 | -59.184101 | 2025-08-11 00:53:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32ad9200-d75b-3895-be7a-5e461f5c1055 | -12.4225 | -54.995602 | 2025-08-11 00:53:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8520450e-3723-39ee-9adc-188722ec1655 | -18.6085 | -46.819099 | 2025-08-11 00:53:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| afe4fd6e-460a-3adf-828a-cc934316642e | -14.9616 | -49.800598 | 2025-08-11 00:53:00 | METOP-B | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 851ce25d-10c3-3444-b9aa-5be3a0d12a8d | -8.9286 | -60.707699 | 2025-08-11 00:53:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 872ad92f-3f7c-37f3-9924-ba966d7fcecf | -21.239201 | -51.039398 | 2025-08-11 00:53:00 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fa5355b4-d5af-3a20-b0f5-eb1d51f1dc81 | -3.4001 | -49.0084 | 2025-08-11 00:53:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bda20589-82b3-30cb-8ecc-17936f874589 | -18.837 | -48.662399 | 2025-08-11 00:53:00 | METOP-B | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
