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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78a999cf-3983-3af1-9268-3d1ac5927a73 | -5.9713 | -44.1312 | 2025-09-24 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 77ac54be-46b8-30b6-8b40-34cbad3f4fae | -9.5781 | -47.5782 | 2025-09-24 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 159.1 |
| b90e1ec1-886e-33be-8171-5e624ce62320 | -10.8336 | -44.808 | 2025-09-24 13:30:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 189.4 |
| c774850b-e11a-35e8-a8b3-4b36639ea51a | -4.7846 | -42.7737 | 2025-09-24 13:30:00 | GOES-19 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 501b3273-f14b-3627-83fc-fa429e5810a5 | -4.7335 | -42.1152 | 2025-09-24 13:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 0e7c12f1-1269-38f1-99a5-458b28e1b157 | -9.5595 | -47.5581 | 2025-09-24 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 07e64193-8bb3-3344-bb80-8de428f7366b | -11.4229 | -44.9563 | 2025-09-24 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| a0f25f56-ca26-338f-acf1-ba099c9db6d7 | -9.1937 | -45.2886 | 2025-09-24 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 045038d2-3010-36ca-a423-3d3bf6fa8606 | -8.5173 | -45.0206 | 2025-09-24 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 444eeb84-8adb-378f-9efc-2ff080649040 | -20.5445 | -57.1224 | 2025-09-24 13:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9f23c655-e0e4-3831-a966-42782079b652 | -11.0253 | -45.9046 | 2025-09-24 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| cba3691f-0e3f-32af-951e-9042c0a815fa | -6.4129 | -43.0958 | 2025-09-24 13:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 216714e3-8267-3921-a05a-5cbc195ad991 | -11.4233 | -44.9331 | 2025-09-24 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a017e856-0a6f-3573-a94b-56dba748ba3b | -9.7418 | -46.6714 | 2025-09-24 13:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| aa8e05b0-91d2-3cd5-aba5-9ab805e36ed6 | -6.4317 | -43.0942 | 2025-09-24 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| dbb3a0ca-c57a-3f80-a4ce-762affc11801 | -8.3139 | -46.2183 | 2025-09-24 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3f97289d-fd31-3fc3-8ede-fcb8f1c73f9f | -11.5225 | -43.658 | 2025-09-24 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 360b0516-51fc-3919-b529-84cb3270326f | -9.825 | -46.1453 | 2025-09-24 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 37d7ead1-185b-381d-96d9-be6ee9e089fe | -11.0249 | -45.9274 | 2025-09-24 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9342eef3-3b08-359f-876c-c238bab803a8 | -3.8651 | -40.3596 | 2025-09-24 13:30:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 5bb85ab7-d6ec-3aae-9f58-ec104acbec38 | -11.5225 | -43.658 | 2025-09-24 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 162.6 |
| d3861463-de52-3cc5-b197-a16e248c57a0 | -10.3378 | -46.0835 | 2025-09-24 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| a92bbbb1-30ef-38ef-8986-eb8afc0a0801 | -11.5032 | -43.661 | 2025-09-24 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 16eb8bc8-2cb2-331f-ba97-772096c1e927 | -4.7337 | -42.0914 | 2025-09-24 13:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| 2a5111fc-c185-36d7-8d19-d479a516cffb | -11.4233 | -44.9331 | 2025-09-24 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 4e7c55fd-73e8-3865-acb5-2d1a4140ec32 | -7.6015 | -44.4262 | 2025-09-24 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 64af6f81-c0a5-38ca-b012-a4ca97be2761 | -9.5595 | -47.5581 | 2025-09-24 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 7eb74e35-9e0a-34e9-8718-7a50ebcbfabf | -11.4229 | -44.9563 | 2025-09-24 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 6a6b4c05-86a9-3d7b-9830-a5447e91cfef | -3.8651 | -40.3596 | 2025-09-24 13:40:00 | GOES-19 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 103.2 |
| a601774d-7345-39c9-b429-37f7e5f2ada4 | -6.4317 | -43.0942 | 2025-09-24 13:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 16f399e8-9a43-3145-ac0f-2443811cb5c5 | -11.5229 | -43.6344 | 2025-09-24 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 1d834264-0a48-39c8-ad78-f4495a8a0bee | -6.4129 | -43.0958 | 2025-09-24 13:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5fc73796-78ba-332d-9d63-76ceb52e1e43 | -20.5445 | -57.1224 | 2025-09-24 13:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b9f49411-f70c-3fba-9bae-6dec8645cf68 | -11.4037 | -44.959 | 2025-09-24 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e36c0b62-f85f-31ed-b7f8-179005a35888 | -11.0062 | -45.9072 | 2025-09-24 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 95d63fe0-17dc-3bb3-8af7-7ce18a23b6a5 | -10.8425 | -45.4274 | 2025-09-24 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 241165ca-d7cd-3b0e-85ad-112d4e4dd017 | -8.3139 | -46.2183 | 2025-09-24 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| da881d3a-5861-3e62-9480-6432c1f9da10 | -11.0253 | -45.9046 | 2025-09-24 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4b15bec2-dce2-3385-b11b-87f3cec9dd62 | -4.7335 | -42.1152 | 2025-09-24 13:40:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 255.4 |
| 7099907c-02d2-3d9d-aae2-61be46d0614c | -4.7974 | -43.5435 | 2025-09-24 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 284871e2-058f-33f6-b41f-5a2672519840 | -10.8616 | -45.4248 | 2025-09-24 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 87ffcd53-1bf2-3b7e-bf9c-d8a69b72f2e7 | -8.8417 | -46.187 | 2025-09-24 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.9 |
| a4321c0a-c9d1-3a20-878a-1e0edcf8a12e | -11.663 | -44.3639 | 2025-09-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 7c330d36-87fa-3d0a-b59b-db93fee05ecc | -11.6442 | -44.3434 | 2025-09-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| f17fbc3b-1212-3d86-9481-7026eb3dfa60 | -11.0253 | -45.9046 | 2025-09-24 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5cf9927e-7678-3955-ae8d-b3b459231fb9 | -8.1805 | -46.3657 | 2025-09-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 3b45f26d-3698-3ab4-8f6f-9583159bfe9c | -11.4233 | -44.9331 | 2025-09-24 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| eff28ead-b5ce-3447-b42f-3b089b24f257 | -8.8417 | -46.187 | 2025-09-24 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| e9b1f632-3bca-33d6-98af-5a0944291c88 | -11.6822 | -44.361 | 2025-09-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 4a125105-0d8b-3853-be79-12697d22fca8 | -10.8425 | -45.4274 | 2025-09-24 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 74614007-84cd-3d2b-9102-2a88f304e617 | -7.6012 | -44.4492 | 2025-09-24 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 65f2c040-5a63-34f8-a04b-455a8500d4d6 | -11.4037 | -44.959 | 2025-09-24 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 720835ea-8667-32d9-a59b-7ff04541df74 | -7.6015 | -44.4262 | 2025-09-24 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1635f831-f87f-3215-99c7-8910d8003f0e | -11.0249 | -45.9274 | 2025-09-24 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 2212d5ca-c894-39d2-9416-b3b823234641 | -4.0146 | -43.2641 | 2025-09-24 13:50:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 727539a7-806c-3b0c-9974-cafb9d39ded6 | -6.6039 | -44.6082 | 2025-09-24 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e91202b5-86ce-3567-a487-d5d8b29a44d3 | -20.5445 | -57.1224 | 2025-09-24 13:50:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a480ca84-3c60-39ba-9000-08d10d0e91db | -5.7605 | -42.6088 | 2025-09-24 13:50:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 15d25a3d-560c-3b86-bc3a-4b3a26a3eb62 | -11.4229 | -44.9563 | 2025-09-24 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| b4fb1603-6b72-3ccf-b0bb-456aa5362a64 | -11.5229 | -43.6344 | 2025-09-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 69b47827-13fc-373f-82fe-92c4da95f82b | -11.6461 | -45.3158 | 2025-09-24 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 67042b0e-47ef-3ed6-9d00-3a02900a80cd | -6.4317 | -43.0942 | 2025-09-24 13:50:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a60dea7b-bbe0-307d-81b6-ae56e567bcbd | -3.7814 | -41.7196 | 2025-09-24 13:50:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 186.5 |
| b78aaff6-314f-358f-9d1e-07c6f5b5722d | -11.7014 | -44.3581 | 2025-09-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b86b1c27-c930-342b-9beb-43a8ff9015d1 | -8.3328 | -46.2164 | 2025-09-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| a18972a9-f6b5-319d-a585-4e6ec6077c9a | -5.1651 | -42.0614 | 2025-09-24 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 158.9 |
| e0bb4d3d-021e-3cab-a08c-cb096b8ca891 | -11.6438 | -44.3668 | 2025-09-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| ffe4658a-8ab1-377d-9226-d33efd95a591 | -11.701 | -44.3815 | 2025-09-24 13:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 7af1873a-9c36-31f2-be7b-b9026e96d787 | -8.3139 | -46.2183 | 2025-09-24 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 676272b7-6f11-3b21-92ae-9b6013722cb8 | -17.951 | -55.8522 | 2025-09-24 13:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| 9bd3eb3e-9ac1-3557-a07e-a62ebffc2381 | -11.5225 | -43.658 | 2025-09-24 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 7b52c657-7c81-3227-9d89-3334375b6b17 | -12.3184 | -44.2154 | 2025-09-24 13:50:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 150.2 |
| eb179f08-31f3-36f6-88a1-b5304fb3d49d | -9.5784 | -47.5561 | 2025-09-24 13:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 81a99058-bc29-3ef9-a136-8a920a5a0fc3 | -10.3188 | -46.0859 | 2025-09-24 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7eb52ca1-c64c-3913-bc60-ea5d55ea0868 | -11.701 | -44.3815 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 940a9bae-c22e-343b-afb1-07bf8b22c0d0 | -17.951 | -55.8522 | 2025-09-24 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| 7edf50ce-6173-31e4-bbea-9196f56804d3 | -10.8425 | -45.4274 | 2025-09-24 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e7d74d82-ff8c-30d1-a36e-fc3776f2da91 | -5.7605 | -42.6088 | 2025-09-24 14:00:00 | GOES-19 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| d700c846-515b-3d38-9f05-7c007c1d7c0f | -8.3139 | -46.2183 | 2025-09-24 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 9a097cb7-2749-315e-8f63-758e34facae5 | -11.5225 | -43.658 | 2025-09-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 3dd77d1d-0136-3c05-b1e1-a0070d61b6d3 | -9.825 | -46.1453 | 2025-09-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c2761718-af0a-3683-9183-771457885859 | -11.6442 | -44.3434 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 3993f55c-650e-3d6a-9bc4-1f03e3158e63 | -8.8417 | -46.187 | 2025-09-24 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| fd73c234-7b7a-3ef2-ad2b-c03faf893b16 | -3.7814 | -41.7196 | 2025-09-24 14:00:00 | GOES-19 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 271.2 |
| 5a66cb0e-5163-3d55-9833-dbbe082904a1 | -6.4129 | -43.0958 | 2025-09-24 14:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| daa1d4d2-82c9-326b-ba42-b06196702c52 | -11.4229 | -44.9563 | 2025-09-24 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| eab17a39-029b-3781-a5ec-db5ffb8b8ff0 | -11.5032 | -43.661 | 2025-09-24 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| edae8b8c-95a6-3e2e-b624-dc97f2d207ed | -9.1937 | -45.2886 | 2025-09-24 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 661d1973-151a-3393-b9b1-d32e71616be6 | -11.0253 | -45.9046 | 2025-09-24 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 48549212-504c-39cf-b085-bc18cee19a3c | -4.7974 | -43.5435 | 2025-09-24 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 667a96c5-d707-3e0b-bcf7-ebdc29a99483 | -4.7337 | -42.0914 | 2025-09-24 14:00:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 143.7 |
| b99de712-4413-3106-966f-aa61f1753eac | -17.9506 | -55.8731 | 2025-09-24 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.7 |
| 6b3b7288-2cc3-33df-989a-b055033fe208 | -20.5445 | -57.1224 | 2025-09-24 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c90629ab-b225-32f9-88ca-27e700012865 | -11.6438 | -44.3668 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 4b888802-adbe-3090-99fa-3a51b358ce71 | -11.6461 | -45.3158 | 2025-09-24 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 768a15ac-44b7-30c9-8bdc-882f4c157a04 | -11.7014 | -44.3581 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| bbe45ac1-6871-30d5-ad27-8a92b6be1969 | -11.4233 | -44.9331 | 2025-09-24 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 54bb9590-612e-31b2-b4f6-a62d0301c5a0 | -20.5648 | -57.1194 | 2025-09-24 14:00:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 86.5 |
| f53c8397-d9e7-3a64-afd2-08c0b08571fd | -11.6446 | -44.32 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.2 |
| ebe6a8be-5752-3717-a528-14b455aecbad | -11.663 | -44.3639 | 2025-09-24 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |


[Clique aqui para ver as próximas entradas](README24.md)
