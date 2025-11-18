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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed85c93e-eff3-37ed-b3d9-83704ea61368 | -9.3969 | -48.4523 | 2025-11-18 00:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 0ee0577b-7523-3c18-8345-72b0800c7db6 | -9.378 | -48.4542 | 2025-11-18 00:40:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 56a74887-02fb-31cb-8e22-80940b8fa771 | -3.0714 | -45.4107 | 2025-11-18 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 726578c1-beb7-32fe-9ba5-ec4232e3ee62 | -8.2851 | -44.0095 | 2025-11-18 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 95210abb-14fe-3a28-b3c8-c936fff99122 | -11.5291 | -48.9559 | 2025-11-18 00:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 3165f1c3-28c2-3e75-b126-284007ed4274 | -2.8298 | -45.4195 | 2025-11-18 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 17912cb8-2bba-345d-b816-cbc34399bbf7 | -9.4769 | -40.3365 | 2025-11-18 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 167.3 |
| 1f8deac5-b7c9-349a-8353-3663005d1ff6 | -12.7386 | -45.3812 | 2025-11-18 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 867ef516-9913-355b-978f-7fd0adccccdf | -2.8491 | -45.2388 | 2025-11-18 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 73.3 |
| e217071a-8353-3832-803b-6c2ec2d4e790 | -8.3043 | -43.9842 | 2025-11-18 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| bf340bd9-d40c-3670-8992-050c20758408 | -3.477 | -46.0656 | 2025-11-18 00:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 272.4 |
| 039aef37-5383-38e6-ac86-a3cf2dfd4fbc | -3.4769 | -46.0879 | 2025-11-18 00:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 388703ad-e3f3-3718-bc3c-fea96b60e12b | -3.1256 | -45.7449 | 2025-11-18 00:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 25d8e81f-fbb1-3122-b3e2-252369d4cd0e | -3.4584 | -46.0664 | 2025-11-18 00:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| acae8cc4-ef15-302d-a1f5-8eb3f897192c | -3.3554 | -44.4026 | 2025-11-18 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| d81462de-7265-37fa-adf8-3330e5b43a43 | -12.7193 | -45.3842 | 2025-11-18 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 079cb772-761a-3cd1-9671-830d57e2179d | -2.5238 | -47.8115 | 2025-11-18 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 2c64ec93-3b44-3fd0-95c6-dc42866b229b | -9.3969 | -48.4523 | 2025-11-18 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| afd7e472-1e7c-35f6-9197-633d441de2a7 | -3.4769 | -46.0879 | 2025-11-18 00:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 18ba8361-6fe1-3e3d-8c42-9614cfaa6b33 | -3.3555 | -44.3798 | 2025-11-18 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| e00e5aea-09b8-3cbc-ae26-98aa56fc4b81 | -4.1949 | -44.2476 | 2025-11-18 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a22f7196-fd13-3ef2-aaf9-0f9ce1ba6767 | -4.1762 | -44.2486 | 2025-11-18 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 3b59b294-35fd-3393-af98-25c2d624126e | -6.6687 | -42.0314 | 2025-11-18 00:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 69.8 |
| 7f524508-ec23-3191-807a-782d48638163 | -3.0236 | -47.8396 | 2025-11-18 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| fd795f82-4f60-3581-b87b-8aac18a355f7 | -3.1256 | -45.7449 | 2025-11-18 00:50:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 2bc834f9-5c8c-318e-9c42-bd0054332c53 | -3.0714 | -45.4107 | 2025-11-18 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| aa7b64a2-ac4b-3d31-bdba-fcf535b835f9 | -9.0934 | -44.3356 | 2025-11-18 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 98bb895b-f395-32b5-a8b8-cf9e219a7111 | -3.477 | -46.0656 | 2025-11-18 00:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 326.0 |
| 076a198b-9c53-3d4e-83d9-168df3caaf0e | -3.3369 | -44.3806 | 2025-11-18 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e9cbb351-6dd7-3f2d-a8c1-f4feb835b089 | -8.2851 | -44.0095 | 2025-11-18 00:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 79dcd79b-1735-31d1-a82c-6b2c2176d469 | -11.5291 | -48.9559 | 2025-11-18 00:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 2f073b3a-1880-31a8-b1e5-772aa0832f0a | -2.8298 | -45.4195 | 2025-11-18 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| cbf09d3a-f3ec-322c-87e4-2a960f795adc | -11.51 | -48.9583 | 2025-11-18 00:50:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 118733ac-6109-302c-8109-9d93d617397a | -10.3535 | -48.9174 | 2025-11-18 00:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| de24b656-25f2-3a0a-979a-c5b4f36d3e72 | -3.3367 | -44.4034 | 2025-11-18 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| b77a3bec-d6ff-3891-91cf-2e6a5ac25f53 | -4.1764 | -44.2257 | 2025-11-18 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ac5e57f2-696b-3746-955a-0b989c890d2b | -8.304 | -44.0075 | 2025-11-18 00:50:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| b52988f0-b51f-34bc-a374-712e6f7b0cd2 | -3.3554 | -44.4026 | 2025-11-18 00:50:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 89231e41-ba3c-3eda-bc10-6679472469fb | -3.4584 | -46.0664 | 2025-11-18 00:50:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| ab828374-2502-3737-88be-2fdc1404a5e1 | -4.195 | -44.2247 | 2025-11-18 00:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 28aacf4e-ff12-34e0-abb5-8a644baaeb93 | -9.3972 | -48.4305 | 2025-11-18 00:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| a7c578a2-951a-307a-9e7c-99bd4af675dc | -9.1124 | -44.3334 | 2025-11-18 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 897758a0-fc87-3e0c-9ba4-4daf1ebb7d9b | -2.8677 | -45.2382 | 2025-11-18 00:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| f40c2654-943f-3c8a-9138-3f907054dc86 | -10.7613 | -44.174 | 2025-11-18 00:52:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 15f8e524-ba9b-3352-b321-7d2f0afac745 | -12.0017 | -49.2659 | 2025-11-18 00:52:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa0d6fde-53b6-327c-adaa-c5f3d356c2c5 | -11.5148 | -48.9478 | 2025-11-18 00:52:00 | METOP-C | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0306e838-e35d-3cba-b39a-4ef5508c672e | -9.4711 | -40.3321 | 2025-11-18 00:52:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d7497cc0-bcff-3afe-9e0b-0a43820d0746 | -11.6577 | -44.740501 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 333018ee-f73b-37b4-997b-d212e7fc1910 | -10.8542 | -44.091702 | 2025-11-18 00:52:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 836a6a60-1e83-35fa-b3e4-b43ca51cd737 | -10.5137 | -43.970001 | 2025-11-18 00:52:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| baea8bc6-e2b0-3642-ae70-a773321cafeb | -11.6644 | -44.725899 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ffed162-718b-3e21-9602-e874b7af0252 | -10.5101 | -43.955799 | 2025-11-18 00:52:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 63dc9682-a852-3e59-b22e-4629253c2c35 | -12.2341 | -49.378399 | 2025-11-18 00:52:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6d0118d-2288-34e0-8f1f-d769da20c3a2 | -11.8479 | -49.225601 | 2025-11-18 00:52:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06189475-323f-306d-9544-6cbdca40c45e | -12.7387 | -45.3862 | 2025-11-18 00:52:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| adc81860-d3e9-36f1-a3d3-551262232789 | -11.5165 | -48.9552 | 2025-11-18 00:52:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8620f404-9db0-3873-8760-65713b916fd5 | -11.9339 | -44.811001 | 2025-11-18 00:52:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b165dff9-66d2-3a35-9578-a572b42045fc | -11.6675 | -44.738098 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92c581f1-a152-3080-abf0-28c8363208d7 | -12.845 | -41.470501 | 2025-11-18 00:52:00 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1b8d275d-55fd-3b24-b00c-d2b4c17a32c0 | -12.2358 | -49.385601 | 2025-11-18 00:52:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a020f1a-700e-34ca-b3bd-93be8873fcf9 | -11.528 | -48.9603 | 2025-11-18 00:52:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cbeb0b10-650b-3a7e-8d9d-d1d79b2c5faa | -10.7578 | -44.160301 | 2025-11-18 00:52:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 097d348d-9d5b-35c7-8b4a-043a08933aaa | -11.2893 | -48.5144 | 2025-11-18 00:52:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb968c00-db33-383c-a0fa-a3072fe75568 | -10.5065 | -43.941502 | 2025-11-18 00:52:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9695db6c-c126-38ba-a236-98ec5b1e8f6d | -12.8546 | -41.467899 | 2025-11-18 00:52:00 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| d0805587-9dfc-36e5-9444-452b3304c2c1 | -10.7647 | -44.187698 | 2025-11-18 00:52:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 07d42575-7581-3b1f-a904-27bfbec9fd6d | -11.8462 | -49.2183 | 2025-11-18 00:52:00 | METOP-C | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac036fb0-8a20-3aeb-9b9c-2d75b4d15e11 | -11.6935 | -44.718399 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 99dae408-9af2-3230-8b66-77bed288747c | -11.6838 | -44.720901 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 60dde3b5-7305-3380-870c-e94ae9eb095d | -12.8495 | -41.448601 | 2025-11-18 00:52:00 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ed6e7e00-c1d9-32a0-9cf2-e553f3d153e0 | -9.478 | -40.3582 | 2025-11-18 00:52:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 71b72b39-b507-3876-b3d9-c4d290645879 | -11.5732 | -48.1409 | 2025-11-18 00:52:00 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88daeddd-9072-3084-819f-83ff0c05a31e | -11.5245 | -48.9454 | 2025-11-18 00:52:00 | METOP-C | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29697d17-b6e6-351c-b7f2-95b0f5688ded | -11.9211 | -44.801601 | 2025-11-18 00:52:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1193bc4d-5541-3d3e-b458-e87effde58b0 | -11.9309 | -44.799099 | 2025-11-18 00:52:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9427063-098e-3e03-9a79-eda448e27cc4 | -12.7361 | -45.375401 | 2025-11-18 00:52:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0238b16-b348-3bb1-a40f-ad76e6405c26 | -12.6923 | -46.7649 | 2025-11-18 00:52:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c5d0405-3b19-3e2e-841b-9adc1f181901 | -11.6546 | -44.728298 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 08c457f4-e19d-3fbd-9bae-d11cb1d5d54b | -11.6905 | -44.7062 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 388602df-9a8c-3b57-a0db-c0445967129e | -11.565 | -48.456699 | 2025-11-18 00:52:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4e8f785-2e83-33fb-b37d-94a04164ace8 | -11.6808 | -44.708698 | 2025-11-18 00:52:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f558d275-1445-39d5-8bab-e0ca5fc1cba4 | -12.6945 | -46.773899 | 2025-11-18 00:52:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13013ad7-a24a-33bd-9119-50bf6e5e491b | -11.5263 | -48.9529 | 2025-11-18 00:52:00 | METOP-C | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2c99d4d-f17f-3b97-b843-f0425a5015d0 | -12.8399 | -41.451302 | 2025-11-18 00:52:00 | METOP-C | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 991f4610-bb87-3206-8ee2-3a0a8c20211e | -10.5198 | -43.9533 | 2025-11-18 00:52:00 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac87e789-da3a-33f6-ba91-74f08bb57b65 | -10.3538 | -48.929699 | 2025-11-18 00:55:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c255c1ce-de7e-33b1-bb7d-7f36913cffee | -9.0928 | -44.315102 | 2025-11-18 00:55:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 331e9b80-e1b5-3f11-9c7c-b9c2045e9428 | -4.6393 | -47.939701 | 2025-11-18 00:55:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 091a2f2a-e8cd-3d7e-827d-916e5c5da102 | -3.1765 | -48.029202 | 2025-11-18 00:55:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8a5a9b-3761-3f33-a041-5f9922188fc0 | -9.3903 | -48.4338 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0f3f04-04b0-34e8-8095-eab1918034dc | -4.7126 | -50.947701 | 2025-11-18 00:55:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 282091c4-facf-3e8a-b2a9-219e557d5c71 | -10.5112 | -49.516701 | 2025-11-18 00:55:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0378523d-7b50-3c9e-b1d7-8475115e4d56 | -3.249 | -50.685398 | 2025-11-18 00:55:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 705f03cc-dcfd-3d66-a662-3a1f1740a9ef | -9.396 | -48.457901 | 2025-11-18 00:55:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c06cc02c-35f2-301c-acda-139bf0e3cdc4 | -3.1301 | -45.743401 | 2025-11-18 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 020d5b85-2f12-3b0b-ba44-71a381954bd1 | -4.6398 | -45.6511 | 2025-11-18 00:55:00 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3df6cc2f-3ec1-36e4-9c52-9dcd89a314eb | -8.2039 | -45.015701 | 2025-11-18 00:55:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 920616f8-960c-35cf-baff-b8b95596d06c | -8.5857 | -44.101501 | 2025-11-18 00:55:00 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 406ed5c9-183b-3a49-8f7b-a628f54fbb22 | -8.2879 | -43.9823 | 2025-11-18 00:55:00 | METOP-C | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cb3bc13a-c6e8-3ec6-a803-0b6d652a11d0 | -4.1783 | -50.199699 | 2025-11-18 00:55:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
