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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44f05a9f-abc2-3768-9704-6c94acfe5bb2 | -3.1116 | -53.7436 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 9f565d64-2eb7-39ff-ba37-9a99b091e05e | -8.852 | -66.7827 | 2026-10-03 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f65de5fa-9655-3b90-87ad-e8d1f808ad80 | -3.7137 | -50.6674 | 2026-10-03 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 6c635642-5ce9-3250-9059-08708f5f2485 | -9.6923 | -57.456 | 2026-10-03 00:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d9bdd684-77a7-305b-87b0-1b603603ff0e | -5.7378 | -45.1307 | 2026-10-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b5c1aaa6-78db-38d3-bdcd-86690dd29d5c | -11.6395 | -43.5455 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 0953599a-861c-3e50-97c2-f85c78a7ca27 | -2.9042 | -45.3944 | 2026-10-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 891b53f6-098c-39ed-91bd-25d807602119 | -6.8579 | -59.2829 | 2026-10-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 2fba5286-b4c0-3248-8fda-29b3a84ae7cc | -3.2768 | -53.8199 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 18ca366f-1fd9-339f-8165-18b8cf96871d | -3.1839 | -54.0839 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1cde24e3-8785-3b4d-a05f-e8fecc5616f8 | 1.7854 | -55.5856 | 2026-10-03 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| b4805d41-91a5-3706-9664-66e2d0a58185 | -5.6134 | -44.3876 | 2026-10-03 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| cd2a3fa2-1474-332b-83e6-c0af55a9f278 | -6.8393 | -59.3029 | 2026-10-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| b9a5810e-3290-34e3-b2e8-d1d988d97675 | -3.4278 | -52.8227 | 2026-10-03 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| b8772dfd-99ae-3b0c-a5f2-c067dcb3e4a6 | -0.9147 | -47.9069 | 2026-10-03 00:00:00 | GOES-19 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| c3f57b37-e946-3cbb-a8b3-2176d92a365c | -4.4506 | -47.9329 | 2026-10-03 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 4855181f-4b34-3d21-9dfb-25f3fa6649d9 | -3.13 | -53.7229 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 10dc3c3b-9fcf-34b5-8b85-4488f42075a7 | -2.8855 | -45.4175 | 2026-10-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 195.3 |
| 29c22e33-10ab-32ea-82a1-ab1e7184c9ac | -5.9384 | -43.6482 | 2026-10-03 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| e48fb75f-e717-31bf-b658-4e43589aca57 | -3.4277 | -52.8431 | 2026-10-03 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 102.0 |
| cc9f848b-1e85-3691-9c3c-3b73c44968da | -3.1483 | -53.7426 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b7e8df0f-fcd5-36bc-94f3-038c635fcac8 | -4.4507 | -47.9112 | 2026-10-03 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 432f3728-0977-3875-acad-d6af7e6db767 | -11.0067 | -59.1381 | 2026-10-03 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 6108788d-976f-3cfa-b6d8-d813e94b372a | -11.7375 | -43.4356 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b0e86e64-3f08-391f-9f9e-54f29e52b727 | -6.8436 | -58.5678 | 2026-10-03 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2c960b25-3d7b-3c53-b2c0-da482b2cae6b | -10.9881 | -59.1197 | 2026-10-03 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 71f0265e-c3fa-3a7a-b4c0-7e64eadad5b4 | -13.556 | -44.1009 | 2026-10-03 00:00:00 | GOES-19 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 564ea3a9-92c1-36ba-a841-3d47843fa7f0 | -11.6981 | -43.4891 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b1863f89-d72e-389a-a360-168d6f738bd9 | -3.4093 | -52.8233 | 2026-10-03 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 59e0b269-ddad-3449-a65a-e1c631b4c392 | -2.8856 | -45.395 | 2026-10-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 185.5 |
| afc64500-6f09-3847-a9b1-90f65ec6b4b7 | -2.9041 | -45.4168 | 2026-10-03 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 036c1426-444f-3192-b45d-46fb57f48cf0 | -3.2952 | -53.8194 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1d619659-f203-363f-a206-6c9687b9a502 | -5.7376 | -45.1533 | 2026-10-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 77490260-4069-3bc3-af6b-62379d28acbd | 1.8037 | -55.5854 | 2026-10-03 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 8a97d2ca-6eab-3321-9efb-1d6cf54a6988 | -11.6977 | -43.5128 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e39ba8e9-f189-39ec-aba7-5f3f37bda286 | -10.9879 | -59.1393 | 2026-10-03 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| efef1f5b-18e6-3034-b0d3-1dd346cc2ec6 | -11.6588 | -43.5425 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 15c39dc1-90d6-3438-b6bc-ce85ec24d62c | -11.6583 | -43.5662 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 79de89dd-2344-35ff-bc21-f56ba180b01d | -11.0068 | -59.1185 | 2026-10-03 00:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ea3e19af-f0c7-3e86-a8bd-19988effc54e | -11.7174 | -43.4861 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.0 |
| ab30ae45-646b-3ac7-ba2d-c2143cbd0466 | -3.2767 | -53.84 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 9b19e316-68dd-3fa2-86bc-2bda02d9c08b | -5.9569 | -43.67 | 2026-10-03 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| afcd2d84-7d37-3ce6-afd9-2b0cb768d1d1 | -11.6391 | -43.5692 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 225.8 |
| 50292394-51e9-3acd-ae1b-ec2791c159ae | -6.8252 | -58.5686 | 2026-10-03 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 2179adf9-416f-36ac-8481-6e672b5c58fa | -6.8394 | -59.2836 | 2026-10-03 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 88375c14-1baa-35b0-9987-319668de2d2c | -5.7355 | -43.2916 | 2026-10-03 00:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 76a7aad7-698f-3f3d-894a-31bcc617a87c | -3.1299 | -53.7431 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 216.8 |
| fed8ae0b-08d9-3e41-a7ca-9c7f56c33f9b | -3.4093 | -52.8436 | 2026-10-03 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 139.6 |
| b3213501-a03f-3236-a711-bdca4cb31f01 | -11.7169 | -43.5098 | 2026-10-03 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 158.3 |
| e1319679-314d-35cf-8d2b-63603f932caa | -5.6136 | -44.3647 | 2026-10-03 00:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 0ed4e1b3-d4cc-313a-b40b-3ad0c1c3a116 | -5.7563 | -45.152 | 2026-10-03 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a79a1de2-68a2-3ce4-a9d3-8a93e5330667 | -3.2951 | -53.8395 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 03108d72-fd08-3426-992e-afc1f4ad8140 | 1.8038 | -55.5656 | 2026-10-03 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 98fb1f78-61dd-3bc8-80db-4291a75ad47e | -3.1299 | -53.7633 | 2026-10-03 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 4b017239-bdeb-3ed1-a431-cb7793cedc4a | -2.9845 | -53.2617 | 2026-10-03 00:00:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3735f226-85e7-322a-887c-7fd876124588 | -3.7138 | -50.6465 | 2026-10-03 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| c66fb00f-fb04-37c2-ada4-f11c42858e5f | 1.7854 | -55.6054 | 2026-10-03 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 1a9a5fa6-aca5-39ee-adc5-5082f83bf605 | -6.7401 | -44.1371 | 2026-10-03 00:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 3e620034-bdbe-33d2-9189-8762e8f5f0bc | -5.9571 | -43.6467 | 2026-10-03 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 38fe85c8-212d-3818-a2b9-6dc8154e71e7 | 1.78434 | -55.60069 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| f8c5419f-bcd6-312f-b67b-6cb7fc6b7b25 | 1.81284 | -55.56019 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7057a0a0-7d73-3934-9cb0-24f1332e6836 | 1.79758 | -55.5877 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 60d64d1f-ee6e-3581-9f8e-5b9165e7d1d2 | 1.7467 | -50.80421 | 2026-10-03 00:01:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e136878c-0392-38db-a4ce-3abbddc7f521 | 0.07702 | -51.41977 | 2026-10-03 00:01:00 | TERRA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c259ce9-479a-3b7f-924b-83da599a8444 | 2.35285 | -50.76153 | 2026-10-03 00:01:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3b03a0e3-4907-301b-a1cb-f0fd53a41481 | 1.7379 | -50.80298 | 2026-10-03 00:01:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d31e17eb-6239-3a25-8f8f-17fa8330edd9 | 1.7543 | -50.81419 | 2026-10-03 00:01:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c1291f2f-fc2a-37b5-9513-dfb91c9eaae7 | 2.35405 | -50.75277 | 2026-10-03 00:01:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 73a4b676-132b-3cc6-9aff-8eb244d3254a | 2.56325 | -50.96373 | 2026-10-03 00:01:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7c11df8c-af8a-3f69-835f-7ecd6470f49a | 1.91913 | -55.78296 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b9537396-2cc3-30c9-813d-9af1501da12f | 3.30333 | -51.35415 | 2026-10-03 00:01:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b1aeb78-053b-3510-85ae-a5301ba0dc0a | 1.78225 | -55.61527 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 32e3a539-bb6b-319d-a228-d4a47f691002 | 0.60084 | -51.56561 | 2026-10-03 00:01:00 | TERRA_M-M | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f8a846ce-aa87-3125-bdf0-b288a708d0e8 | 1.81079 | -55.5747 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ae396090-691f-3963-bd00-d9afeee2771e | 1.79551 | -55.60228 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| ae84ef07-3167-38eb-b120-645554e17036 | 1.79964 | -55.57322 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| addaf71c-6261-3737-bba9-9bf0dd77f22b | 1.79344 | -55.61682 | 2026-10-03 00:01:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 96d78e09-440c-34eb-af91-3008a0104767 | 3.69285 | -51.59412 | 2026-10-03 00:01:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2df40b02-4bab-3903-aa6f-d15652e51430 | -2.8855 | -45.4175 | 2026-10-03 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 239.2 |
| ff65b979-5b31-3f0c-81b7-2da445a3f7d7 | 1.7854 | -55.5658 | 2026-10-03 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 2d10fd0f-359c-35e4-a54c-67dbf5068f17 | -3.2951 | -53.8395 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 46bb2674-7001-3400-8e50-649b28929f2c | -3.2767 | -53.84 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 20195758-9481-3351-8017-bf6c104519dd | -11.7169 | -43.5098 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 194.3 |
| 1cdab394-a646-3105-9326-ec36a16d6199 | -3.1839 | -54.0839 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9c304d97-19fa-343e-aa1f-9bd99605be46 | 1.8038 | -55.5656 | 2026-10-03 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 64ec4305-5d06-3d58-9b1e-0f801e4f76ee | -11.7187 | -43.4148 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 5c57c553-c71a-3440-a238-d1dd0ef755f4 | -5.6134 | -44.3876 | 2026-10-03 00:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8c279b88-2534-3cb0-be4d-6187bd8cf850 | -10.9879 | -59.1393 | 2026-10-03 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 2ff6b2ee-6434-3c8a-8c43-31d6cde057e7 | -3.1838 | -54.104 | 2026-10-03 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 9d3dcc56-46e2-329f-95a3-cbc20bb71bb7 | -11.6391 | -43.5692 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 88ee15ff-f3ba-3d97-9d3c-f9c9a755a376 | -10.9881 | -59.1197 | 2026-10-03 00:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a31b459d-ef9e-36cb-bb2e-2cfd41c1635d | -0.8962 | -47.9071 | 2026-10-03 00:10:00 | GOES-19 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| eb96e957-fdd7-378f-b851-886da4f8eaa7 | -5.9571 | -43.6467 | 2026-10-03 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| a1133cc5-1de0-31e1-bc67-9942988e7d38 | -0.9147 | -47.9069 | 2026-10-03 00:10:00 | GOES-19 | CURUÇÁ | PARÁ | Brasil | 1502905 | 15 | 33 | nan | nan | nan | Amazônia | 45.1 |
| e215879f-9c12-39ec-859e-917fb6173c17 | -4.7434 | -43.2679 | 2026-10-03 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6b4dab1a-b57e-30dd-b244-2e3ba278aeae | -11.7174 | -43.4861 | 2026-10-03 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 207.1 |
| cc2890b6-edaa-3373-a311-c6ece1fafa61 | -6.8394 | -59.2836 | 2026-10-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 81a166c5-af25-30b4-bcec-8fe604e132ac | -4.3588 | -47.7636 | 2026-10-03 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0771136d-6e0d-390a-9dc6-c757ff7a226a | -2.9041 | -45.4168 | 2026-10-03 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 5dc4600e-2bb9-3392-bff2-4cdc61091ce2 | -6.8579 | -59.2829 | 2026-10-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |


[Clique aqui para ver as próximas entradas](README2.md)
