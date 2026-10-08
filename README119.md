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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f2e8fbc5-3400-3389-978e-ec81b7fe3d24 | -3.03602 | -54.07732 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b44e56ae-2966-3e04-bf3f-70ed2fb8a328 | -3.30243 | -53.8615 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a30b6a3-4645-3e28-8f20-a8bd42db1b40 | -4.07464 | -50.34111 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 621bd7e3-1612-3112-be4c-7f78cc456d84 | -11.62469 | -43.69803 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f13b9e6f-b84a-38dd-96b4-0bdbeb5c1911 | -3.29761 | -54.03423 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a4db05d4-b6d0-332d-8771-02e7a5f78939 | -3.05486 | -53.93401 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5716e6d2-2694-3974-a552-fd74140ad7ca | -3.11272 | -54.15969 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 6edaae22-c508-34fc-bac4-d92cfd12983e | -3.70278 | -50.65193 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 959749d9-5883-39c6-8ebd-a4c6e6af5332 | -3.69349 | -55.49167 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd148f42-cc38-31ae-bc87-be4741f6df90 | -3.30564 | -54.03109 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 761a264a-7d65-389c-a2b8-70c8a7e35140 | -6.8061 | -55.30227 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57391f3b-d351-39fe-be40-e68a8887ba57 | -3.0201 | -54.17827 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a1b18eb-ecf8-38f5-8f58-e26d36cdc36a | -7.66467 | -44.94712 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 430f9713-4fb5-39e1-8f82-12e814c8cdb0 | -3.04917 | -53.16505 | 2026-10-08 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2c5c204-b7b1-3999-960b-50f19302ca23 | -5.98638 | -40.9304 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| afda93da-4a5e-3e5a-9bbf-46933351b22c | -3.02727 | -54.08488 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0050930a-95a6-30e5-95ae-e9fafcd9a81e | -6.85008 | -41.77089 | 2026-10-08 04:46:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 20ee2fc9-ac3b-3f5c-b769-1088ae693b98 | -5.78223 | -52.36507 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ce1bae4-e00c-3f2c-843f-efab4797d935 | -3.84236 | -55.97384 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 684644e2-9c4f-3205-9777-f1197f9d8bec | -10.25034 | -49.66146 | 2026-10-08 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7c6f4254-a48b-3b46-95c5-a50a909a9eba | -8.72382 | -45.18211 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 89c0aada-458c-322e-8e65-9d3d3eefd721 | -2.48728 | -56.1228 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 211b012d-f9ae-302a-893c-bd7697d0f74a | -11.22172 | -45.27218 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b05c533b-f9eb-3ccc-a2a5-311d76d904f0 | -7.59993 | -42.38272 | 2026-10-08 04:46:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e58e4212-2e70-3215-b3c1-9f063e7f3f2f | -3.66503 | -57.08999 | 2026-10-08 04:46:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dce4ac9c-fafb-3b36-9813-328c072b8430 | -6.94671 | -45.28669 | 2026-10-08 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 760f6db3-3b55-35e8-8bf2-2a6780f2f7fc | -6.3308 | -43.35671 | 2026-10-08 04:46:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f2355388-7013-341c-ae9c-33c04cebd138 | -6.89805 | -48.71521 | 2026-10-08 04:46:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8291098-b979-36f8-8454-2ae4d1ffc640 | -11.75191 | -44.93526 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1fb08487-69fa-3ef3-9a90-4b0b2e96a106 | -5.73473 | -45.14603 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1f978dc7-d795-3a2c-a29d-2efc3e89a81e | -2.99635 | -54.08904 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f10a023-c2a3-3f54-87bc-8a9fd3623109 | -3.07726 | -54.2628 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e505d0c8-4e67-3bb3-8eac-138a28fae7b8 | -2.85301 | -59.10765 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7990869-37e6-3ec9-b10c-b80b4220527a | -3.33705 | -50.27498 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa7c9e5e-30a7-35db-a862-b09574127480 | -3.59096 | -54.57134 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 363266ab-4fc0-333f-9d88-82b1facce0dc | -3.00518 | -54.24872 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bae3aa4-f763-38ce-a266-8495dce75dbb | -3.2118 | -57.86775 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa06ee48-fa5e-3053-8209-2ef5e200bfea | -3.11573 | -54.1646 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| abc86c26-4bf7-3732-9a30-1bf4a1de9cf6 | -7.00906 | -59.11625 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b397b07-fbe6-3f30-808e-c84670941d81 | -3.05525 | -53.90781 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f0c3bce-9612-3fd1-96de-1b4a6add8e45 | -3.51311 | -54.66958 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 187f11cf-c164-3a6b-94a9-cd816fb04752 | -4.22688 | -46.93353 | 2026-10-08 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c4536b1-aef8-31e9-802b-9b46f76674ec | -8.08361 | -55.30409 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ace9ee95-0c77-31d2-97d3-3485e4cfcf6a | -3.43674 | -56.93657 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7d8c21e-a7ee-3977-9df8-65618fa4279a | -2.84742 | -54.12611 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f3a18773-5be9-3307-933b-4274f5d352ed | -3.44553 | -56.93802 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b317e32-3c6f-3750-af84-a5fb04f84fb0 | -9.45273 | -44.61935 | 2026-10-08 04:46:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25ef0cd9-7ca3-3446-8a45-66adbad82a36 | -9.93494 | -48.78622 | 2026-10-08 04:46:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f821ed35-8dbb-3e52-90b9-c592de54d3af | -6.99958 | -59.11831 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8294e9aa-37fa-3132-892d-2184472d5a17 | -4.06387 | -59.83449 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6a91239d-20d2-351e-b948-5228334ef4eb | -3.29937 | -54.06986 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d812abdb-01d2-3e40-8ad8-cdb4b7f2bf79 | -3.02796 | -54.08051 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 546ede49-ba37-3b69-a22d-3c83cddc2c64 | -5.74518 | -45.05415 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22a11e3f-0e05-3abd-9e05-c27ea7cb9642 | -7.88587 | -55.01867 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3755b486-e595-3b38-9114-80120f02d221 | -3.35436 | -59.50164 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef507d37-8c6f-3cb0-a803-57ebfbe1034f | -3.23093 | -53.88939 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c7c202c-61be-3f05-8a9a-e7a6cb66a6bf | -5.22491 | -60.24319 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c8acb51-d5e9-381e-bab5-5e8de287e70d | -3.27578 | -54.05287 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7978cbe5-7e36-3289-a8c3-986c5b8733fb | -2.50533 | -56.14577 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a68daab-5c0c-3007-865f-0efe34c63873 | -3.07797 | -54.25832 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73a1939c-3fd6-3d90-880f-404d2e533eb5 | -6.09538 | -55.72121 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b7e1b67a-df00-36c3-95f0-82c4d54f0caa | -8.18744 | -45.76951 | 2026-10-08 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2dc3203-fb1b-392c-a300-46fe3cd21e1d | -6.95435 | -51.92574 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87eb05ee-3cdd-35be-9b17-8629a7da9189 | -10.23436 | -58.21566 | 2026-10-08 04:49:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0044d33a-4f11-3e3f-bfdf-0c2581e97f39 | -14.92188 | -48.10945 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a88f7efd-638c-3997-8f77-c6d2a5dfd40b | -13.23336 | -43.39932 | 2026-10-08 04:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f98a76d4-2441-30a7-968a-9052c41d4f42 | -9.47916 | -64.35236 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49036f58-d835-3684-935d-1818f6595c4a | -14.9278 | -48.09594 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e4f399c5-02a2-3044-b52b-75c09947f5de | -13.50771 | -44.36901 | 2026-10-08 04:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 33ab5f48-b368-3fba-a33c-85906e958035 | -14.92497 | -48.1167 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e2853e49-9b53-3a71-81e5-8bcd4d9ed0d1 | -13.30603 | -48.67741 | 2026-10-08 04:49:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| df0b5f6a-2a5e-3740-8db4-1e8ff9308b4a | -9.48469 | -64.35734 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a720733d-581f-3417-9845-bfd20a8b3e07 | -13.1692 | -54.32131 | 2026-10-08 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 654ed263-8e87-37fb-af93-b0000f4f71cf | -11.80761 | -47.34477 | 2026-10-08 04:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4d5dd06-9a16-3f40-99ce-7216a6e84e4e | -10.98824 | -54.22022 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b6eafe37-e332-36ef-ba3d-f1526ed0a657 | -9.07938 | -65.48549 | 2026-10-08 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87d1bebc-5384-3576-8cf5-faf3610e85b8 | -11.74953 | -61.06029 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31f498c0-e08b-3447-81d6-6021b282aa42 | -11.23895 | -54.9619 | 2026-10-08 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bd845f2-563c-323b-99d4-7a4e09a30f56 | -17.12141 | -41.34301 | 2026-10-08 04:49:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 20369302-7c0c-306c-9391-e27ec0410366 | -12.41383 | -54.35956 | 2026-10-08 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17061e87-9a5a-3ca6-94ff-ad40db18380f | -10.64376 | -53.85186 | 2026-10-08 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c2198ab-8c2a-3c58-afe0-3fad3cd3ffb5 | -11.76381 | -61.06087 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d26ab23b-95fe-306b-a656-c38b39b1fb78 | -15.42092 | -43.70188 | 2026-10-08 04:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e6739381-d2a3-3d5c-9a0b-a60794651187 | -18.26055 | -42.16964 | 2026-10-08 04:49:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 660fac8e-4ce4-3de6-9671-5820096024c9 | -10.23364 | -58.21974 | 2026-10-08 04:49:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6fd1d541-29d0-3d5b-9ef5-86c3cecaf86c | -14.92428 | -48.09172 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b226adb5-cc3d-36cf-9d5a-7d450aab2277 | -13.1845 | -47.87738 | 2026-10-08 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ad9c2ab-822a-3c7a-8f15-f168d6149a2a | -10.90082 | -57.08288 | 2026-10-08 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc733bd-f66d-33a2-bf09-7436d0055704 | -14.93669 | -48.10397 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e52651f-3db6-3edb-9c83-180ee530b0a3 | -10.3647 | -57.74262 | 2026-10-08 04:49:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15ae3a7-5f4e-394e-8c5b-a3726b49bc89 | -16.35595 | -55.34169 | 2026-10-08 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7f3c0400-a34e-3441-9f7c-dfb9e691250f | -14.93847 | -48.1075 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2701c962-1de0-3dc2-9c02-469cb24c5e0d | -13.80966 | -52.79949 | 2026-10-08 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c567714e-2efe-3708-9039-12ef62050c0f | -14.9132 | -48.08303 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2a930ba-74f1-3b0b-b793-fd9f61880230 | -17.12191 | -41.33765 | 2026-10-08 04:49:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 96e8b2eb-618f-3a9f-bbd2-f4e2c1a985d5 | -10.81312 | -56.50296 | 2026-10-08 04:49:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86294956-8d41-33e2-b0b4-97f3e3603e42 | -14.92545 | -48.11317 | 2026-10-08 04:49:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e9e54842-29c8-3ccf-b983-b89e744b7519 | -9.47717 | -64.36157 | 2026-10-08 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 638ec2d0-e904-32b6-8436-1ccac6a772e0 | -11.75459 | -61.0612 | 2026-10-08 04:49:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 133a45a0-996e-3832-9137-ad31136590a3 | -12.16991 | -53.23182 | 2026-10-08 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README120.md)
