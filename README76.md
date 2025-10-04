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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52288e44-425f-3350-9dc5-9f37f72e0499 | -10.33662 | -50.33027 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dc06b5c2-1339-352f-9c45-dd25e93b54b7 | -9.11279 | -44.39501 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cdd290b-96d9-3b99-8a6c-6fb159f2bfca | -9.93912 | -43.57522 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 236232f8-c1e3-327d-bf60-8f8f16d43cf3 | -10.98861 | -46.67183 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ab1b179-178d-389b-abaa-8966c5e7742b | -9.90865 | -45.95729 | 2025-10-04 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a468cb63-9b36-373d-8593-49b2084d8283 | -7.73421 | -46.3158 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de99c603-8e7d-32aa-bfaf-5207febbb5cd | -10.12584 | -52.34509 | 2025-10-04 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8cc278e6-3571-3b4c-948d-1f826e6576ea | -13.57621 | -48.17635 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 828bdbbf-e7ff-30c1-850f-9f3aaaa446fe | -9.94823 | -43.75476 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b95e2052-225c-31b2-8bad-9c48c46c29bc | -13.3167 | -47.25864 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04e25a69-2846-3d42-a7fd-5337f4bc9610 | -9.95098 | -43.75878 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ee4d0c4c-de44-3d59-9733-a9f9b2b29a14 | -13.09041 | -47.07067 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4fdb00a5-3056-33c6-aede-641d775c0f90 | -12.04364 | -45.18942 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e9037b0-25e3-3c80-8e06-6fd5056be6da | -15.34784 | -46.29742 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b270381b-fe3e-3c3f-9d4a-f29bd67fd122 | -14.89147 | -48.38721 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8737b2c1-c507-313e-be9f-f978009b42db | -12.04306 | -45.19299 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eda8bd7-117a-3961-a084-b370b3bf9383 | -14.2448 | -46.09469 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 345a67a8-58e6-3583-b701-715ef7149b83 | -8.7099 | -47.9761 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98acc2b2-0464-3de6-b8ed-a6d2e2635f00 | -13.24015 | -47.83889 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5ed9df08-4139-39b4-a091-57fc9e99bc86 | -9.28743 | -45.67808 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60ec2772-8ec0-3855-b840-71a074ff0772 | -9.34521 | -45.79644 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c78105d-7234-3a0e-a990-62b1280b5093 | -11.70511 | -44.43755 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 677ce124-2c7c-32e6-ba50-c5bc377028d1 | -9.33667 | -45.65454 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc9d6004-08f1-35c0-9112-24f98ef2a2b8 | -11.10079 | -47.71245 | 2025-10-04 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fcccecd-cd39-3191-9832-f7363e871b36 | -13.11028 | -47.89691 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ddb6a11-c7b1-3c63-bd51-1876d13ba521 | -13.17546 | -50.92897 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee91a582-0f77-39a5-a6ef-e0bec73f4040 | -12.81386 | -46.86486 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6c82959-5136-3586-b247-842477a262b7 | -13.48965 | -47.24335 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 474cc8f7-5523-3cf3-9dee-1a1079519cf0 | -11.25551 | -47.79099 | 2025-10-04 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa90f084-8234-3283-a11b-ac83b5740c98 | -11.11804 | -43.39585 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0b4acec-6f7c-36b5-a1d4-81ddcd7f16b2 | -10.27593 | -44.34554 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95ce9061-594f-34d9-b4bf-334c25a38f1c | -11.54974 | -47.67484 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 70a8c92f-3be3-325c-bd84-0beaa326b1c2 | -9.32292 | -54.52927 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a601e364-e197-37e3-9726-e676b10fa071 | -15.35972 | -46.288 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e2aba2a-f588-38b3-8405-ba25610b34e8 | -13.12832 | -47.81329 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07c7c918-0ecf-3685-8a7f-d2c3df3d890c | -12.03582 | -45.19545 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bebc00f4-e4fa-3245-9cb8-6339af73c542 | -11.88402 | -44.99926 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d92352ad-d242-31bd-96fe-baf3252c9fe7 | -10.24147 | -44.94209 | 2025-10-04 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 971762ec-8703-3ff7-9d08-ff3f793b2d7e | -8.62144 | -54.98951 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4feaea9b-fa4e-3f1c-83a9-060e80d01901 | -9.06444 | -46.64035 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a8b2b73-c75e-30d6-bd64-0c03984012dc | -13.31909 | -47.18044 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5c0c2b8-9cc1-3d9e-9299-be0b9685afcc | -10.02561 | -44.01782 | 2025-10-04 04:14:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa974740-eb58-3c00-980e-a29d7e9f8c70 | -10.59766 | -48.70475 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f30014fb-6d54-36e6-aed6-bd927cc7a5f7 | -10.34281 | -43.72918 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc820351-d01d-3930-9e62-13f6cf3f00c1 | -11.56509 | -47.67329 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04a59815-6ed8-313b-9214-a488cab61ea6 | -12.64918 | -46.97735 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c50e9e7c-4c92-3598-ae39-4a2fee29ae0d | -9.3296 | -54.52631 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2fbc3089-e886-3da3-9377-eee85311fb1d | -13.30029 | -47.5933 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e0432426-0c28-330f-81ae-222119a21a90 | -12.59064 | -47.00404 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6702599b-8cf9-3ccd-94c8-b541131a2a52 | -8.70678 | -47.98899 | 2025-10-04 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36d02429-215e-3b2d-acca-1c582d7c0815 | -14.89429 | -48.39264 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a1adbcd-f1c9-324a-aa67-1dd5b910d6d0 | -13.31875 | -47.24648 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d15e64aa-6ab0-3f27-8e88-74a6e58330ec | -15.2936 | -46.29163 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d69899c1-98fa-3fd9-a998-ab3324f41588 | -12.02467 | -45.20093 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f860594d-7c73-387c-95b9-5cb2935d2cf7 | -12.37535 | -46.50934 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef9500bc-3d87-35b3-9b58-74855a15c4b1 | -14.20051 | -46.65813 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d776421-b55c-37a8-9598-42aa2505efaa | -10.33069 | -50.33816 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d6e7f71f-272e-3380-9190-f08404540a4e | -13.46878 | -47.26011 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3ca9e36-2711-3cdd-b15a-ce62a59a54da | -13.29518 | -47.82144 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb7e6442-fc0f-38b7-b569-46878cd86db5 | -14.30632 | -45.86575 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19ed5e92-0500-3d8f-adcc-dbfe2576f661 | -12.22789 | -43.76845 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdfe7ddd-2ea2-3dff-b68b-8627c4cf397a | -9.94027 | -50.89515 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f412553-80ba-3f61-ab14-37fe9cc95a84 | -14.63306 | -48.25419 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dba44aeb-6f48-3792-95b4-a48538efd648 | -11.56875 | -47.67397 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d6743a5d-2b30-3cc3-ab95-a81533ddf80c | -9.10435 | -46.71114 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5135b21d-7a6e-3a99-b719-f36619793006 | -14.91969 | -46.89284 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 424a9fd7-5553-3b32-9eb2-379a7844a0b6 | -11.78746 | -46.83908 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c64f713-207d-3bdf-9a79-8bdcc787b2c1 | -14.89388 | -48.35152 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b463d6e-dc94-3fcd-a930-aeb8832f4fd3 | -14.40855 | -49.44324 | 2025-10-04 04:14:00 | NOAA-20 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e3fac50-e51b-3803-9b5d-77858e1af26b | -9.99042 | -48.2792 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b413c72-869d-3497-b37a-2ddaa910dcf7 | -9.11555 | -44.39909 | 2025-10-04 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a731131d-6b56-3aba-939d-36f936d9279c | -11.83284 | -44.91424 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 913b8243-dc2a-32ca-a9aa-37581401da2d | -9.33861 | -45.77184 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 755987f3-db39-39a7-a84e-6a9622d4ab9e | -12.57354 | -54.74445 | 2025-10-04 04:14:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e87627a3-c477-34ab-a338-b7f299993367 | -11.909 | -46.3768 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51c3e0d0-85ae-3136-8b8b-23e9b27e0d71 | -13.22061 | -47.82251 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35c0be34-f5f6-3c3d-afc8-ba0097af5ade | -13.39817 | -47.54991 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c191255-b316-315b-a8a3-37a91b25dce0 | -12.71314 | -48.55446 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1846ce55-caaa-3b38-b519-c338e71975f9 | -9.10723 | -46.71611 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48b42d5f-c367-3113-b33a-8230ca3b7714 | -13.69996 | -47.35198 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f761225c-a0fd-3ff2-9ac0-d81a56f7cb7a | -11.45335 | -45.14344 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 63b1ffcc-cba8-310e-b615-28e93444558b | -9.343 | -54.52008 | 2025-10-04 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 36b77188-b66c-3a3d-94c0-f6f50b124104 | -13.32395 | -48.09618 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bc681063-84d8-398d-bf70-0d97ed0ab8a1 | -12.07672 | -47.98973 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d404bf45-f900-34a4-9328-a894429cd07f | -12.38081 | -54.46207 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47aca75a-096f-36f1-8c1e-1fae701e2acd | -11.63295 | -45.05959 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 398e095c-3cc5-32a7-9e74-44fe8dd65bd8 | -12.91762 | -54.73609 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3bcddb95-c2af-358c-b149-c1a893a3d201 | -9.63217 | -55.13211 | 2025-10-04 04:14:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 888a92b1-ef93-389e-b288-ee9fd5b42916 | -13.39102 | -47.54888 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cb81b754-967a-3ab5-80cb-862a686e57a3 | -15.3134 | -46.27612 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c6022a42-e288-3232-a8b0-f07a1804a2e4 | -11.50431 | -45.01276 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befea24a-f32d-3158-a10e-16bff52de504 | -9.9312 | -50.24511 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87d8f208-f867-3b55-97ca-2fb78b084ff7 | -8.4683 | -46.93089 | 2025-10-04 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 266c1ad3-cbb7-37f0-9d9d-e8e8364fb254 | -12.22735 | -43.77195 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46d9e338-2de0-3443-a187-adabb41213e1 | -14.67649 | -48.26261 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 75e538b8-c925-3d39-8848-9a8cd8c653c8 | -7.77306 | -46.28057 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7595f37c-d2bb-3473-adf5-9667ac001eaf | -11.84174 | -45.02871 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c9b4af34-8b4f-3fb8-a09c-9271b9083fc3 | -13.31561 | -47.17968 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd95f32b-364d-3581-ad5b-195549129913 | -13.93769 | -48.17149 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f112c39-b23d-3bfc-8ab0-c7d5c6bc2d24 | -8.46681 | -47.42184 | 2025-10-04 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README77.md)
