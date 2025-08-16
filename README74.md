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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e6c068e-d142-3538-8702-67b3b188b516 | -7.12613 | -59.6558 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9e0a21cb-2411-3f5e-b571-c9a565aaf841 | -7.94487 | -63.21469 | 2025-08-16 06:42:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2cf07f59-2569-3d14-89b5-f4f343de428f | -6.93297 | -59.65075 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7b0751b-1648-3e9b-adb0-d37b040efa27 | -8.96823 | -61.68747 | 2025-08-16 06:42:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7a8a6961-a582-30f2-b5c6-a916c01dbbc4 | -6.93431 | -59.6419 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 820c14ab-a91e-3825-8566-22d7fac0928c | -8.96052 | -61.6761 | 2025-08-16 06:42:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a593dadd-755c-33ec-a481-b5421481edbb | -8.97916 | -60.54731 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3c16ba34-07c9-35eb-b0d2-4113c46a5900 | -8.99082 | -60.53055 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 23b56b9d-68a0-33b7-9b7c-7687ef37de9e | -9.16989 | -59.64667 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 2e83203c-ce65-3262-a9a3-782767181fb5 | -8.89399 | -60.7421 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4fc4550-c37b-31b0-b26d-81a4a8b29c7f | -6.12999 | -57.92744 | 2025-08-16 06:42:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 65dc298a-526a-3128-a1c5-902ed7a77df2 | -9.16244 | -59.63652 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 2bb83a8d-9398-3a77-891c-07a5b395c73a | -8.98666 | -60.55772 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 88cbf770-6c9d-3971-861b-3d61d8f4fd72 | -8.99497 | -60.50344 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 1f7fe816-cd25-333b-a38f-93c986c1959c | -8.98805 | -60.54865 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 22a87601-7ae1-3727-8ad9-a0f5b8e3ef02 | -7.52111 | -61.31678 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6d68ecc4-9e9f-37af-8ff3-af02a47cf0f4 | -7.52261 | -61.30701 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f9e3f745-fe21-3ac7-bd72-b61e0c441040 | -7.82298 | -61.3278 | 2025-08-16 06:42:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 15553e2c-3560-33db-8dc2-aed96388e9ec | -8.98609 | -60.50209 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 528f1705-9dc8-3a12-9c5e-de764df4ed33 | -6.79692 | -59.82341 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f27a352c-77ee-3bb3-89c2-c98647f12438 | -7.67337 | -63.30993 | 2025-08-16 06:42:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b5a19c83-13ae-3574-83e5-52f779b78450 | -8.98055 | -60.53825 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| e029ac3f-ac2f-34cc-bd9f-cf7ef358af9f | -6.79828 | -59.81449 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e94b84c6-0730-30f0-8012-21b09f4f890d | -6.94286 | -59.52576 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 96e515da-08e8-380f-af7d-4dfc35f56834 | -6.9402 | -59.54339 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 198ea6e4-a217-30be-8fd2-d2c35ccd530a | -6.93781 | -59.99392 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7fc66947-a91b-3ff6-a4b3-e6c8a5879ca5 | -8.99773 | -60.48539 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| abcd4da5-599d-39eb-9db4-eeb1117939bc | -7.92715 | -61.73965 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e5147adb-22a6-3d85-bf28-70f7f8ee3ef8 | -7.55887 | -61.42045 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9ead72ac-8556-3f14-b225-cbf27065d2e3 | -8.98332 | -60.52015 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 60bf2277-0bbe-33f4-86fc-dfc8b41ee4ed | -8.457 | -64.05233 | 2025-08-16 06:42:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 87f1c4d7-1f2f-3763-a043-6091f7502248 | -8.98471 | -60.51112 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0eb8699e-252a-33d0-a590-1e2c8fd00ca3 | -8.97438 | -61.70876 | 2025-08-16 06:42:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| cda9b03f-57aa-3a6a-8ea7-a46f93612ed6 | -6.9314 | -59.54209 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2a04f8fc-0491-3960-91f0-bb3d3ccb62a1 | -8.9786 | -60.49171 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| b95bc9b4-e10c-3706-a8be-acef9a9c6b41 | -6.66255 | -58.81254 | 2025-08-16 06:42:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c8d094bd-6ce8-3976-b1e3-ed89987dff72 | -9.50987 | -60.52701 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 8152bb66-e464-3ec8-9ff0-5817fe6b093d | -9.00109 | -60.52283 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fbdcc6a3-8383-31ba-b693-ac1220d6ab63 | -7.90831 | -61.73675 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9d820f19-fd34-3ba4-9f18-d3947d7684a6 | -7.90672 | -61.747 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ec2e6d9b-b329-34dd-b155-aa3b60d8158d | -8.9698 | -61.67754 | 2025-08-16 06:42:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 8ccc86c2-f405-3dc8-80aa-357e663c910e | -8.99971 | -60.53188 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9d2f3270-0cb1-3174-91d0-b3f95864fcb2 | -8.98193 | -60.52921 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 66160eda-0321-3a74-9147-0a9110713607 | -9.50848 | -60.53602 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 35695e94-ac29-3bf7-b693-2a1fe933d574 | -7.91931 | -61.72799 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 5121cf08-ed8e-3edf-9c42-27e8aaf720c8 | -9.15498 | -59.62637 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c3ce107e-e4c2-3f92-90e1-fc2f6b9a1c1e | -8.97721 | -60.50074 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a7ffd253-c8ab-3103-95d0-a77b9c98e146 | -9.16377 | -59.62768 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 6bc698b9-767e-3ece-b841-cc042f9c24b6 | -8.99221 | -60.5215 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 55b7beba-2b2c-3df8-b963-1a790559034a | -6.94419 | -59.51693 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 20dbd5dd-3650-399c-84cc-b0b5367d029c | -6.9255 | -59.64059 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8beaa81e-6f7e-3028-8db9-95fee5942a16 | -7.87664 | -61.81608 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9cacce1c-7393-3d2c-8f0a-5ae1e1e0c3c3 | -6.13891 | -57.92868 | 2025-08-16 06:42:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| b0e59626-0bdb-394e-bc49-79c1b3931403 | -8.97595 | -61.69884 | 2025-08-16 06:42:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 28.8 |
| bbf5b6e3-225f-36ca-8a5c-4eaa0ba3831d | -9.15579 | -59.6807 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 97036f64-32f1-31d0-9d88-a3bba433e4aa | -7.50321 | -63.82154 | 2025-08-16 06:42:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fcd921f3-8ae4-3e6b-886e-34f9bab1e87e | -8.97777 | -60.55637 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0d8315d4-7fc0-3f41-9028-e450245f13f6 | -6.94153 | -59.53456 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7d42fc5f-df41-36f1-8e85-7f455f55ba38 | -6.65244 | -58.82004 | 2025-08-16 06:42:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c29e5f28-aec5-3f26-9988-e18b72a5c68c | -8.98943 | -60.5396 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b67fb9db-32b1-3937-bebd-c99cd84ef5c0 | -8.98747 | -60.49308 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| c08c958a-5e11-3dfb-9676-bd71b8aee27c | -7.9513 | -61.74909 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f38cd057-3703-3345-a998-ad670204ee6a | -7.91773 | -61.73822 | 2025-08-16 06:42:00 | AQUA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 89da2096-ec12-38d8-9496-78aa0d37837b | -9.4954 | -60.55495 | 2025-08-16 06:42:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 59f51af8-47be-3861-9ca2-04a0978aa0e7 | -7.50263 | -63.81451 | 2025-08-16 06:42:00 | AQUA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| d7ffbcc8-5da7-38a6-ad70-a5475dfc5e9d | -7.03994 | -59.61821 | 2025-08-16 06:42:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| e090e8c2-63a0-36d2-a31f-1a10d6a536e2 | -8.99635 | -60.4944 | 2025-08-16 06:42:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 65d1fb12-c693-3ee0-9d0b-6a100350777b | -10.04553 | -59.11457 | 2025-08-16 06:44:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0a5d096c-78cb-3826-8f84-9891cf83d807 | -14.93171 | -54.69556 | 2025-08-16 06:44:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 2fcc9d76-8184-3762-990f-414762d1586e | -14.86074 | -60.08817 | 2025-08-16 06:44:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8cb23f45-2440-3227-a1b7-3aa039919466 | -14.95206 | -54.73632 | 2025-08-16 06:44:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a8bd11dc-de9b-3451-9482-1189e2f9b000 | -10.11152 | -57.76723 | 2025-08-16 06:44:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 783c97fe-f7cd-3bd6-8ece-b5acf08e2d89 | -20.39351 | -54.77322 | 2025-08-16 06:44:00 | AQUA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 26e58601-2046-3934-a238-b26cfadaddce | -14.93024 | -54.68866 | 2025-08-16 06:44:00 | AQUA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| daf5bf51-01a8-33b3-aa1a-3f900cfc3881 | -13.1156 | -57.12943 | 2025-08-16 06:44:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7e49db4e-642c-3281-98da-5da03f170c63 | -14.87096 | -60.08032 | 2025-08-16 06:44:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 97b11ded-a1e2-3e1d-814d-393341c29d6c | -14.86961 | -60.08954 | 2025-08-16 06:44:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| aa5564b4-fa55-37af-bfcd-7e7485ea7094 | -20.38764 | -54.77977 | 2025-08-16 06:44:00 | AQUA_M-M | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 6d52210d-d89a-3a44-803d-f157d800ba22 | -8.9974 | -60.4955 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| adecf9e1-e12d-37fa-ab2c-cb6c6d1a75e8 | -9.1709 | -59.6374 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| ead357f0-f219-3213-82d7-a6d18c93135d | -8.9787 | -60.5156 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a8cf6b0b-3b12-3d5f-aae3-0483bd76e287 | -14.9628 | -54.7351 | 2025-08-16 06:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 51715b4b-633c-3b9c-9153-e91b9a9b5c5f | -8.9788 | -60.4964 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 1563d081-f788-306b-8945-8e1cee2af386 | -8.9708 | -61.7033 | 2025-08-16 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| db634bb9-3f89-3c28-aa39-74ca10617e97 | -8.9973 | -60.5147 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 38c5ad97-25b5-32fe-bddb-b99abc6fb869 | -8.9971 | -60.5339 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| ed2dc333-2bc6-3cd3-bb22-58817dc0c7e5 | -6.9487 | -59.5297 | 2025-08-16 06:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| aa9611ab-e267-3bc0-a488-9bcc70769c62 | -9.1708 | -59.6568 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 6fc1ae95-b79a-3199-826f-5d07ecce6d43 | -8.9709 | -61.6842 | 2025-08-16 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 2c57b124-3d70-34b8-9cf8-4bac73e07db1 | -8.9785 | -60.5349 | 2025-08-16 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| fc6c14c0-8562-38a5-ba40-07400cffc851 | -14.9628 | -54.7351 | 2025-08-16 07:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 5f10f714-a9e8-339a-9391-252279fc01e0 | -9.1709 | -59.6374 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d5efe0f5-9eec-3962-b90f-9a048759ced7 | -8.9973 | -60.5147 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 103122ed-1c40-3283-85e1-2a93e6d8eae6 | -8.9971 | -60.5339 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9291f467-87fe-3e4c-bf18-d22ef4b933d5 | -8.9708 | -61.7033 | 2025-08-16 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 0dd4522a-7396-37d9-92d3-7f0aedc36a94 | -8.9974 | -60.4955 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8205f28f-5791-382f-93f0-11a0bb62cef1 | -6.545 | -43.0373 | 2025-08-16 07:00:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 67e016cf-7a37-3282-9430-1e8537a99abd | -6.9487 | -59.5297 | 2025-08-16 07:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 4078ac93-f1b9-3679-bed9-20e273570705 | -8.9787 | -60.5156 | 2025-08-16 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 170fd7a1-9914-3a33-b510-7f1dedab5319 | -14.9632 | -54.7143 | 2025-08-16 07:00:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |


[Clique aqui para ver as próximas entradas](README75.md)
