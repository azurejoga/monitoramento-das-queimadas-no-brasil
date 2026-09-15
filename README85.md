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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31dd5919-9798-3b6b-9179-b8f569426f91 | -5.8321 | -52.0887 | 2026-09-15 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e25b647b-025b-3a2c-9999-f449127f7620 | -10.3116 | -45.3136 | 2026-09-15 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 186.2 |
| a693eb72-a19a-35c0-a6af-55f73e54f959 | -12.6826 | -54.6763 | 2026-09-15 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 178464db-eb90-3179-9c0b-dcfb3e7e2cc3 | -9.1742 | -56.9358 | 2026-09-15 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 01add929-cba9-354a-b8b7-b7b851a1ec65 | -10.2926 | -45.3161 | 2026-09-15 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 288.9 |
| 6faf0c8e-ea5a-311e-9206-c3e51ba0ff37 | -8.8175 | -62.4898 | 2026-09-15 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 28b56522-ab3e-302b-b994-b7c6788c6e1d | -11.3834 | -43.9378 | 2026-09-15 15:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 0554f48e-4174-3131-9da2-88ae5db6cfe6 | -6.3197 | -59.9764 | 2026-09-15 15:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 87e82afe-f741-37f7-b03e-f59eb02924d5 | -8.8137 | -46.905 | 2026-09-15 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| a7679fbf-c992-392e-9d73-6b0d395ccdb6 | -9.3755 | -50.1779 | 2026-09-15 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 374ce04a-a68b-3468-b38b-92bae2e2b20f | -15.2821 | -42.8075 | 2026-09-15 15:10:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 131.6 |
| f6854262-6dda-3cdf-b792-1411d4a1b394 | -13.5719 | -51.4605 | 2026-09-15 15:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 5fc8ecde-4e97-36c1-9c0e-05cfe5329f83 | -3.4942 | -54.6767 | 2026-09-15 15:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| d82cf612-4e4f-3784-afaa-e99be3dfe82b | -10.6641 | -54.1491 | 2026-09-15 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| eb82afc4-d26b-312d-89f4-c2b1420c5afd | -11.1208 | -40.478 | 2026-09-15 15:10:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 125.9 |
| 2cb2d553-11cf-3d29-81a1-a3d4729da942 | -6.7463 | -59.4416 | 2026-09-15 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 2a8b9087-f6cd-3b51-b225-c26d9ad63daa | -11.2677 | -54.1361 | 2026-09-15 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| f3c2a583-7b8e-3c10-8c1a-a880e6a90354 | -8.8361 | -62.489 | 2026-09-15 15:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 57df35ac-0f8c-336a-a405-31a3dd43ca69 | -4.523 | -54.944 | 2026-09-15 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| dc936821-bec2-3c14-a944-2109e2593119 | -3.4943 | -54.6567 | 2026-09-15 15:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| e72fa5f6-11b7-3799-8c5a-100e589ba0f1 | -12.6818 | -54.7379 | 2026-09-15 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 20c08302-f1a3-3b6f-8eab-962cc21fab13 | -2.7767 | -49.4765 | 2026-09-15 15:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 31c6f86e-20f7-3bec-87c1-0b60122aad6a | -10.6829 | -54.1475 | 2026-09-15 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 4d6af249-33cc-3ace-9c84-65c21e9766fc | -15.3054 | -53.9012 | 2026-09-15 15:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| de93bdca-1c77-3240-89f6-8a285d854077 | -8.6293 | -63.0085 | 2026-09-15 15:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ca2648b8-3985-332e-8dc4-3c1d4684033b | -11.9906 | -52.4695 | 2026-09-15 15:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 933ccf03-00e3-39ee-afc4-0bd84dd013a9 | -9.7548 | -47.0937 | 2026-09-15 15:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 20f4731a-a328-37ed-a855-e7cce044fdd4 | -13.5722 | -51.4391 | 2026-09-15 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| afc22194-ca80-3d2f-a65d-afc44106ad23 | -11.5041 | -45.7939 | 2026-09-15 15:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 218fd765-5140-3442-915b-721e94476dd4 | -3.5727 | -58.5389 | 2026-09-15 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 480.4 |
| 063f8463-1a06-3e35-a27c-9de2ffb47242 | -8.7946 | -46.9291 | 2026-09-15 15:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 305268e1-6d36-398a-ae40-700ef5f1f206 | -15.2407 | -41.3137 | 2026-09-15 15:10:00 | GOES-19 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 114.7 |
| 8701db4f-2d98-3d74-bebd-7b0ba11adfa6 | -9.1337 | -65.844 | 2026-09-15 15:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 8d870870-cd4a-38e6-9271-67713d5c25da | -8.114 | -45.6301 | 2026-09-15 15:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 8c90daba-a0c8-3328-8b02-67c2f710893a | -15.5974 | -53.8426 | 2026-09-15 15:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| bb9837a2-a409-3e22-81cd-9e6b8714b3e1 | -5.6225 | -45.5002 | 2026-09-15 15:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 777c0812-0b70-31d1-89e4-baa694a638d9 | -10.7274 | -50.6192 | 2026-09-15 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 494946d1-cf4f-312e-8ecd-c5253d57f344 | -10.0988 | -45.5685 | 2026-09-15 15:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 04740aba-b8ab-32c9-85cf-6c63c72bc452 | -10.2922 | -45.339 | 2026-09-15 15:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 184.6 |
| 3e8237fc-9ba7-3b88-9931-0f13216b8026 | -5.9333 | -53.5362 | 2026-09-15 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 26632ee4-5cbe-3481-97b4-502468ad2d23 | -6.7464 | -59.4223 | 2026-09-15 15:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 40afb2d7-6bec-3a05-bb16-37151f7ebcc6 | -13.7006 | -51.8061 | 2026-09-15 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 53ed1aad-9892-3393-b73a-bd3f876af9d1 | -15.3598 | -52.989 | 2026-09-15 15:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8e4c4455-2af9-36db-878b-f1f27ea3729c | -13.7002 | -51.8274 | 2026-09-15 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 121.9 |
| d2f2ab2a-1a2f-30f9-aca2-bdd39ba8158d | -10.792 | -46.2071 | 2026-09-15 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 9dbd31b1-bbe2-3b8d-9c66-7fe2600345a8 | -5.3627 | -47.7096 | 2026-09-15 15:10:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8917c5d1-2300-35d4-aa0e-0855360e8bcc | -12.6633 | -54.6988 | 2026-09-15 15:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| a5a9f274-da22-32da-bb76-be3b3706a10f | -15.3602 | -52.9678 | 2026-09-15 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| df5e3ef8-1138-3333-8c40-0e0393d67a5d | -13.4273 | -54.6195 | 2026-09-15 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c5e72c22-915b-3ce7-a689-3f3cfdade6cc | -2.7767 | -49.4765 | 2026-09-15 15:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3e9beee9-eed2-34b3-9a0c-a149cb3a1ad9 | -12.1265 | -44.199 | 2026-09-15 15:20:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 0b2690dd-38df-3922-95e0-6310eebb04ba | -12.6821 | -54.7174 | 2026-09-15 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 2de3f1e2-16ef-3d05-94c8-c49671efdc20 | -9.7684 | -46.1293 | 2026-09-15 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| aed6ca75-45dd-3664-9702-bf4e174c273d | -10.7084 | -50.6212 | 2026-09-15 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| a532c131-111b-3f9a-8842-4455f67e2e69 | -10.6641 | -54.1491 | 2026-09-15 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| f7fdff1e-b7ec-39bf-b9e2-e3a876d6cbfd | -6.6021 | -58.849 | 2026-09-15 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 81d78721-1116-3290-a4fd-2149cc8fa4b9 | -13.7006 | -51.8061 | 2026-09-15 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 4c85c7f6-3058-368f-88a9-c1edc1c34433 | -13.7002 | -51.8274 | 2026-09-15 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 92adf571-0a56-3be4-8e01-5e85221b129b | -8.6293 | -63.0085 | 2026-09-15 15:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 85.3 |
| c5500c93-4e2e-38b6-8202-307dd355b5bb | -10.2926 | -45.3161 | 2026-09-15 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 102.9 |
| af50dec9-e30a-3751-9515-a21b6073c3e1 | -7.7298 | -44.7121 | 2026-09-15 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9f12f200-3def-37d1-940b-2507a18a63d1 | -10.792 | -46.2071 | 2026-09-15 15:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 3d0e838c-aa68-37e7-8789-6042ccb63410 | -6.3197 | -59.9764 | 2026-09-15 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e97480ef-b527-3c2e-a469-59014c23c762 | -6.7463 | -59.4416 | 2026-09-15 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| f0ad3f1c-c24b-323e-b265-ee7004b3e04d | -7.0823 | -42.1107 | 2026-09-15 15:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 118cac2c-478e-38e9-ab7e-04e33f795cea | -9.1337 | -65.844 | 2026-09-15 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| bf82327a-f38c-38de-a0ed-6e8c01463a9e | -8.8459 | -45.8713 | 2026-09-15 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 751cee0d-22af-37a9-95fe-a8240d897889 | -9.7358 | -47.0958 | 2026-09-15 15:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| f69b587f-7946-3228-83e9-f9d1198ddc7c | -10.6829 | -54.1475 | 2026-09-15 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 385dbfdc-48d5-375a-badc-9f797db278e4 | -1.2268 | -49.1899 | 2026-09-15 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 11c1f70b-5327-3ccc-9a1e-c08b990b4614 | -1.861 | -54.4315 | 2026-09-15 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 20dea57f-c1b8-3025-8876-83f0440d58b6 | -10.312 | -45.2907 | 2026-09-15 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| faa53ed4-e27e-31ab-aaed-638e8786e425 | -12.6636 | -54.6782 | 2026-09-15 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 2a143373-65b2-38b3-b354-1ec5b28c216f | -11.9906 | -52.4695 | 2026-09-15 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| aecc187a-2e4a-3be3-a10b-7ef4ab26e852 | -9.1742 | -56.9358 | 2026-09-15 15:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 4e8ddd05-941c-30f0-8cf3-8402182f868b | -3.5726 | -58.5581 | 2026-09-15 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 13b8bce8-e071-3614-85d9-b2109c87e34f | -12.6824 | -54.6968 | 2026-09-15 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| f45763a9-b280-35dd-b743-b86ebd1067c2 | -6.2959 | -41.6824 | 2026-09-15 15:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 165.4 |
| 93fd7eb1-02e1-3159-b44b-6b84517f5afc | -11.5041 | -45.7939 | 2026-09-15 15:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 15f14dc1-2fe3-3773-afce-4eaac373a609 | -11.3642 | -43.9407 | 2026-09-15 15:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 856942c8-24a5-38ca-8246-4a20cb67a806 | -12.6818 | -54.7379 | 2026-09-15 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 8a569e17-0470-3a7f-a9fb-dab010f93f98 | -9.6104 | -46.5967 | 2026-09-15 15:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6b50cd17-feac-3f47-b1c0-c69e14ce1739 | -9.1523 | -49.9853 | 2026-09-15 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 6c1037cf-4e50-3466-8488-c92a3096cc5f | -14.2985 | -51.7286 | 2026-09-15 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1bfbd7e1-1deb-3896-979f-5ed5b8672232 | -15.2859 | -53.9037 | 2026-09-15 15:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 3313783e-46fe-3444-ba1f-f9666bbe2b96 | -12.6633 | -54.6988 | 2026-09-15 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 3643b48c-ec71-36d7-b836-d0565f64efe9 | -10.6958 | -47.5175 | 2026-09-15 15:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3feb9b2b-64c4-359d-8b1e-024d35e7f348 | 4.2971 | -60.9501 | 2026-09-15 15:20:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6de8c09d-02d7-3026-b71a-fedfa2557f29 | -9.1711 | -49.9835 | 2026-09-15 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 4ed620d3-b360-38bd-bfd5-0bdf08d1bbb0 | -15.5584 | -53.8477 | 2026-09-15 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 5c3d0880-e590-376a-a25b-8a4b2672f436 | -14.1822 | -51.7653 | 2026-09-15 15:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a6da0124-60cc-35ca-93c8-001989c06695 | -6.6767 | -58.7105 | 2026-09-15 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4add1203-d2bf-3f9e-b4b8-98edae68a264 | -11.2304 | -54.0985 | 2026-09-15 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| dfde4096-522c-3ecf-93a1-daa1b6e1b006 | -15.579 | -53.782 | 2026-09-15 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 3ccf2edf-3684-37bb-b387-4806823c19fa | -13.4085 | -54.6009 | 2026-09-15 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 61360a3b-b4c8-3944-9a0e-e242f05ed48e | -6.5837 | -58.8498 | 2026-09-15 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| d5eb870c-2487-3312-9916-aabbdc2138d1 | -10.0988 | -45.5685 | 2026-09-15 15:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 81.6 |
| eacd77f1-bd79-3252-b262-9edd0a3281a5 | -10.6827 | -54.1679 | 2026-09-15 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 92579eaf-020d-3532-a944-d8e351614a17 | -15.5786 | -53.8031 | 2026-09-15 15:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 78f044e3-455a-3d6e-9f2c-3399d9c7efad | -7.5397 | -44.8905 | 2026-09-15 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |


[Clique aqui para ver as próximas entradas](README86.md)
