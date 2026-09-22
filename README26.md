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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33a5367f-806d-3722-a3d7-6011c72e9965 | -3.2396 | -53.9417 | 2026-09-22 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| b1de0561-99e4-37fd-abc6-d2754fdb3edd | -6.6516 | -59.9066 | 2026-09-22 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| be23ee9b-9268-3907-8be8-4b839eb90607 | -5.7382 | -45.0853 | 2026-09-22 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 64f0edbc-1d3b-3abc-b608-4bdf188170b7 | -5.7569 | -45.084 | 2026-09-22 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 139.1 |
| f457e469-d2ac-3973-a5f6-1eca92015f03 | -10.5906 | -53.9918 | 2026-09-22 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 21401ce4-e9b1-3b2e-8622-8a1cb57ef4f9 | -11.3257 | -54.0282 | 2026-09-22 03:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 083023d3-bd45-3d74-9070-201ea96ad08b | -3.2211 | -53.9623 | 2026-09-22 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 07b4bdef-39b2-3d75-9faf-b7bd837a52cb | -3.6804 | -42.9546 | 2026-09-22 03:00:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| b23b6a21-8be6-374a-afff-e44d39173fed | -14.8465 | -49.2863 | 2026-09-22 03:00:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 3cb9910e-69a2-3321-8fab-ea7708abd6ba | -12.5547 | -45.9605 | 2026-09-22 03:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 115.8 |
| aa0bef04-5baa-3e46-b4d2-c7f34e862ea7 | -3.2212 | -53.9422 | 2026-09-22 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8d3e083f-2839-3308-8c16-edd89fc3a61b | -6.0928 | -57.6262 | 2026-09-22 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| c4883e4e-1cd5-3a04-952d-92336b1cc996 | -6.6331 | -59.9265 | 2026-09-22 03:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 154.7 |
| 929271e5-21eb-39c9-84ee-ff8c098b13c1 | -10.6094 | -53.9902 | 2026-09-22 03:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 182.1 |
| eb6f9149-2684-3110-8d5d-75c8f9128148 | -7.5889 | -57.6757 | 2026-09-22 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e59c05b5-2f2d-3adb-b812-7b40e7a692b4 | -3.2395 | -53.9618 | 2026-09-22 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 9ad660ed-8d1b-3a61-8e86-9c0d74dc741e | -6.59348 | -39.14034 | 2026-09-22 03:04:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| aceade26-7861-3210-a2bd-ee7106bb66f7 | -5.42369 | -36.76123 | 2026-09-22 03:04:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3011dc48-d983-390e-8c6b-aac1cc2dde87 | -6.73382 | -35.04389 | 2026-09-22 03:04:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a104e658-0ec6-30d5-b8b3-06a14bace0af | -5.00919 | -38.02298 | 2026-09-22 03:04:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 950d9251-bb16-3dca-bcd0-bbc8f94d116f | -5.00818 | -38.02863 | 2026-09-22 03:04:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7367b10a-edf4-3030-9935-2b579b5aca3f | -5.42272 | -36.75855 | 2026-09-22 03:04:00 | NOAA-21 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99b838bd-b950-392a-94e6-9086a82c7902 | -9.60605 | -40.62271 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 0a6aa2b0-ae48-38e0-bda5-35e849718bb7 | -9.48177 | -40.32438 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 43822e04-bb17-3060-90b7-7f65329f3811 | -9.60253 | -40.62154 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 71f02e26-f4a4-362c-a66a-6a056689846a | -9.61315 | -40.62407 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 37c4d3b7-e28c-3c1b-92f4-aefa1e1eaeeb | -9.60109 | -40.62876 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 409546fd-bd06-350d-a653-40aa7de95297 | -9.60818 | -40.63017 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c5c8219d-d013-3c9b-8c5c-f183ec0e78c1 | -9.60961 | -40.62296 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| fde22b3a-3c10-39d9-b665-3f10b9d0214e | -9.60457 | -40.62994 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 22878300-5a36-3504-8ebc-8c27980c57d0 | -9.47739 | -40.31957 | 2026-09-22 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d8671d45-902f-309e-8a1c-db1530fd911a | -16.67627 | -41.85267 | 2026-09-22 03:08:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6cb6d786-f566-3463-87be-2441308b799d | -16.67525 | -41.84755 | 2026-09-22 03:08:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a3688919-61eb-3bf8-bd10-21cb8896c4ed | -16.6737 | -41.85453 | 2026-09-22 03:08:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| a27c0d06-936c-3781-ac84-c78643a9d8ad | -10.5906 | -53.9918 | 2026-09-22 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a0d9bb31-3a9d-319c-a39f-eadecbc5a376 | -6.6146 | -59.9272 | 2026-09-22 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 0b94dd47-ee73-3cff-8701-8dbb0c1cd617 | -11.3257 | -54.0282 | 2026-09-22 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 69daedef-c827-3e26-b69f-c34644c2db49 | -3.2395 | -53.9618 | 2026-09-22 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 41297e54-bf15-34f3-aa91-48a0b8356953 | -12.5547 | -45.9605 | 2026-09-22 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 845f4775-f4b4-3502-ab52-815d4e217f9d | -9.5594 | -66.0359 | 2026-09-22 03:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| e2fda9b1-a7a9-32b7-b941-40bdc95843ec | -9.6059 | -40.615 | 2026-09-22 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.3 |
| 47446df0-fdd1-3934-9138-aeaf7f7933f5 | -5.7382 | -45.0853 | 2026-09-22 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 122bf0df-ab44-3d59-98b8-8b9f3acb0510 | -3.6804 | -42.9546 | 2026-09-22 03:10:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 56.6 |
| e8293e90-0c00-3bc1-8607-79e2069e0e39 | -18.7472 | -46.93 | 2026-09-22 03:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 11f20994-7284-3d3d-afb0-b161f369a6f2 | -6.6515 | -59.9258 | 2026-09-22 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 148.1 |
| 37f85dc0-a58f-3689-85af-576e1b4a5701 | -12.574 | -45.9576 | 2026-09-22 03:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 30b39dbb-56cc-32b9-abfc-3e0b4f0bc5ec | -7.5889 | -57.6757 | 2026-09-22 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9fc6f9b6-00e7-380b-8c21-2e06e224bc1a | -10.6097 | -53.9697 | 2026-09-22 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 38621e45-5764-3a9d-8973-8c9c84a3ae39 | -6.6148 | -59.908 | 2026-09-22 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 63e3113a-b56b-38a8-b18a-9d6f689b95a0 | -5.7569 | -45.084 | 2026-09-22 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 20a20e89-c532-399f-a61a-cf30fc10b429 | -11.3255 | -54.0487 | 2026-09-22 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 766ae453-d33d-3a19-8a13-3a771d71f86d | -2.6669 | -54.9757 | 2026-09-22 03:10:00 | GOES-19 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 463f6260-253f-30b2-8a09-352e42416137 | -2.8608 | -57.7994 | 2026-09-22 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 298f3228-4479-31e8-8f58-82e680d5e1ea | -6.6516 | -59.9066 | 2026-09-22 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 73d0e149-76bd-3dee-9083-5c7530a83650 | -11.3066 | -54.0505 | 2026-09-22 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 342682b7-0870-3f2c-8941-1841aafb880a | -11.3068 | -54.0299 | 2026-09-22 03:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 586ecb65-f5e7-311f-b646-1cc3d133ae32 | -3.2211 | -53.9623 | 2026-09-22 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ee0f0838-34b1-3112-87a4-ca45794f0d12 | -6.6331 | -59.9265 | 2026-09-22 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 7ef4a1a2-e770-38e9-9bbe-7c41df6aeffb | -6.467 | -59.9902 | 2026-09-22 03:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 3b2c57a4-f97b-3b89-8026-8895c307b68b | -3.2396 | -53.9417 | 2026-09-22 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 75187ae7-f215-34c6-831b-f3bbcd83489f | -6.6332 | -59.9073 | 2026-09-22 03:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 8952b0d8-87b3-3d96-b2cf-90e950f8acb7 | -3.2212 | -53.9422 | 2026-09-22 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 057c8a39-ccbd-37b0-a28d-d3c1d9ca7027 | -10.6094 | -53.9902 | 2026-09-22 03:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.1 |
| 5b9246a7-a19d-3b47-a563-7d7ad0ae6e8c | -21.60376 | -41.21573 | 2026-09-22 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f75d9061-f7fb-3530-83dc-3af2d9df8f35 | -21.60127 | -41.21282 | 2026-09-22 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 33df67bd-470e-3134-8330-da2f06badfd8 | -21.59787 | -41.21421 | 2026-09-22 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a01be1e1-850f-3915-9f68-822602f056c7 | -21.60017 | -41.21748 | 2026-09-22 03:10:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| d198916a-8047-3cb4-9eb4-f3e5e1fe488f | -14.82 | -49.31 | 2026-09-22 03:15:00 | MSG-03 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 501e6f7d-ea71-356a-b054-3216cefdb3b6 | -3.6804 | -42.9546 | 2026-09-22 03:20:00 | GOES-19 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 9b92c7e3-c676-3b12-8b37-2b323fc010b3 | -10.6097 | -53.9697 | 2026-09-22 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 9f7547fd-6078-3267-a9ea-074860c683fe | -11.3255 | -54.0487 | 2026-09-22 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 240059c6-1f6a-3f92-8c3c-0a669849d64a | -7.5889 | -57.6757 | 2026-09-22 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 09ebb0bf-40a4-3f71-b146-270f6ff2b661 | -11.3066 | -54.0505 | 2026-09-22 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 59b1877a-d882-3f3b-b402-852e4733cc38 | -9.5594 | -66.0359 | 2026-09-22 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 00f1071b-332f-3f64-8b8e-2ac8428d8173 | -5.7569 | -45.084 | 2026-09-22 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| fd45fd9f-cc74-304e-b909-2b9094bbf651 | -18.7472 | -46.93 | 2026-09-22 03:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| fc72d958-7fb0-3fa2-bf87-e0cc111e6f9a | -2.8608 | -57.7994 | 2026-09-22 03:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b82d1ab2-71fe-37d2-9da9-d97ce804c471 | -11.3257 | -54.0282 | 2026-09-22 03:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 1765ec45-9d2e-3829-b04a-c62393d964c0 | -10.5906 | -53.9918 | 2026-09-22 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e9b40497-a80b-3697-8287-b8255ea618e3 | -6.467 | -59.9902 | 2026-09-22 03:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 5fdb2c25-279c-3f77-a7a3-a6d3927aea2a | -3.2211 | -53.9623 | 2026-09-22 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 5d2e1427-89c9-3221-b862-a7d65cd5abfd | -10.6094 | -53.9902 | 2026-09-22 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 1013f894-9a6c-38e2-b55e-5258c1bf13d8 | -3.2395 | -53.9618 | 2026-09-22 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| bcc9106e-2e73-3910-877e-b7f7091c1c05 | -12.574 | -45.9576 | 2026-09-22 03:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.7 |
| eaf26ad6-274d-3c26-9ec9-77acaf48c73d | -3.2396 | -53.9417 | 2026-09-22 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| de78756e-3dd1-32c8-8e97-c08aeba54077 | -11.3255 | -54.0487 | 2026-09-22 03:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| ea7e6968-5b88-3df4-afca-614a57c81ea5 | -3.2212 | -53.9422 | 2026-09-22 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 0f79c559-a148-3842-9157-95e5acf46a98 | -6.467 | -59.9902 | 2026-09-22 03:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 4e9d6025-66a5-33d6-bb34-bbd9c9a9b1c7 | -5.7567 | -45.1067 | 2026-09-22 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| d0598add-ca26-349f-9cb9-1e8b67dfb837 | -10.6094 | -53.9902 | 2026-09-22 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.1 |
| ea7798a5-d4b1-32a2-a15f-38aa369b64ac | -7.5889 | -57.6757 | 2026-09-22 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| a8523df8-221b-3959-af6a-d8b323a64612 | -12.574 | -45.9576 | 2026-09-22 03:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0584957f-0657-3afc-816f-bfdaf071a360 | -5.7569 | -45.084 | 2026-09-22 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 149.9 |
| d6646557-7fc5-333c-809d-ba5d20f439cc | -3.2211 | -53.9623 | 2026-09-22 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7bc2914f-e72c-361d-8117-818f547d952a | -18.7472 | -46.93 | 2026-09-22 03:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7facd8dd-efa1-3d80-b39c-fb10e05c4b57 | -2.8608 | -57.7994 | 2026-09-22 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6ba7ab18-b1db-3a79-a0e6-dd9d9fd0f09f | -10.6097 | -53.9697 | 2026-09-22 03:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 1f9cdd62-9cde-31bf-9ec2-c704155a9b90 | -3.2396 | -53.9417 | 2026-09-22 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c014d411-78da-3c73-9308-22206360ea6b | -3.2395 | -53.9618 | 2026-09-22 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 2d4c2a5f-5204-3a6a-9be3-8452d6994d0c | -5.7382 | -45.0853 | 2026-09-22 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |


[Clique aqui para ver as próximas entradas](README27.md)
