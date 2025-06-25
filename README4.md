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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5ac9211-3756-3d15-9f3a-a83df7af4528 | -9.577 | -49.107 | 2025-06-25 01:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| ba4e05dd-c8a7-31c3-8f48-a4499a755dbe | -6.1791 | -48.0712 | 2025-06-25 01:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 384.2 |
| 693f5ae3-5558-378d-8cbe-eb58c28977a1 | -6.1789 | -48.0929 | 2025-06-25 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a22d6ec6-e9f6-36fc-abd0-a76d2fa2763a | -7.2028 | -43.0936 | 2025-06-25 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 5c79bfb7-ff33-34b7-b175-6d4bf350002d | -13.0408 | -48.825 | 2025-06-25 01:40:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 157454a5-54cc-35f6-8bc8-490930f23d52 | -6.1977 | -48.0699 | 2025-06-25 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| c90d25c0-9da9-3630-8cd0-54505db17ed4 | -7.0171 | -44.5725 | 2025-06-25 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 9dbc352d-b83d-31f9-a2aa-faabf2e3e712 | -6.1791 | -48.0712 | 2025-06-25 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 338.4 |
| 5b66be69-5287-34a6-8c6e-eefbc9f38ae4 | -9.518 | -56.0975 | 2025-06-25 01:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.1 |
| e426e390-3ee1-331d-bec9-d9a0c49c4112 | -9.577 | -49.107 | 2025-06-25 01:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 8cfebcb7-1809-38f2-9892-b6393e06259f | -6.1792 | -48.0494 | 2025-06-25 01:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 211d02c9-7b5e-3ca8-9263-75139e401f85 | -7.0174 | -44.5495 | 2025-06-25 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 048b3e68-685e-3b1c-9f40-a144e2dc937f | -9.577 | -49.107 | 2025-06-25 01:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 843709a8-9f09-3c55-b009-ee08042a6c61 | -6.1977 | -48.0699 | 2025-06-25 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 1c194f13-13eb-3b5f-9e05-6aeb1d29de09 | -6.1791 | -48.0712 | 2025-06-25 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 293.8 |
| 98cd18f8-1730-3ffe-810d-e1bc2f374146 | -13.0408 | -48.825 | 2025-06-25 01:50:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| fab180c8-7da5-391e-a96a-e84420c8e4c2 | -6.1792 | -48.0494 | 2025-06-25 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 7f15aebd-de23-374f-9ccc-439faaa86e65 | -7.0174 | -44.5495 | 2025-06-25 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 8051aaed-a3d9-3396-bee9-518603c9ac62 | -7.2028 | -43.0936 | 2025-06-25 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 87c44b38-e6bb-3e8b-a91a-e0108a8e12a7 | -6.1789 | -48.0929 | 2025-06-25 01:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 91fe14a7-8601-3bd9-afb8-b14328d30ee7 | -9.518 | -56.0975 | 2025-06-25 01:50:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 2292122e-d389-313a-8778-8ef223d7c512 | -7.0171 | -44.5725 | 2025-06-25 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 5fcfbc2d-8fac-3ad5-8bab-05d21b957c5a | -7.0359 | -44.5708 | 2025-06-25 01:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 8c16c881-3b62-3a3a-8101-05d085f97961 | -6.1791 | -48.0712 | 2025-06-25 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 259.8 |
| 833b5968-f69b-3b49-9f62-690fe411ba21 | -7.2028 | -43.0936 | 2025-06-25 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.2 |
| bbae0d8e-3132-3469-a3d9-a83bcbb8523b | -6.1604 | -48.0724 | 2025-06-25 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| df82efe1-9b47-3722-abc3-43b0e6622788 | -13.0408 | -48.825 | 2025-06-25 02:00:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| e01fb903-63d1-39d0-893e-4791bd587390 | -9.4993 | -56.0988 | 2025-06-25 02:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 34.1 |
| a679e616-e984-3693-9791-8e221bedf423 | -6.1977 | -48.0699 | 2025-06-25 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 71b1ce70-3773-311d-9c64-c4a098c6a6ae | -6.1792 | -48.0494 | 2025-06-25 02:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 123.0 |
| fc9631ba-b98a-3dc4-9657-30d986f2bee2 | -7.0171 | -44.5725 | 2025-06-25 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 36ee16e1-a17a-3a59-aaa7-3dd176fa6a59 | -7.0174 | -44.5495 | 2025-06-25 02:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7904feda-21d4-33de-b1d2-dd2dc680aa3d | -11.1224 | -46.9745 | 2025-06-25 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 4c9db8eb-cd42-3a4c-a774-6ac146238c0f | -7.0171 | -44.5725 | 2025-06-25 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 4b0744a0-4cc9-3459-b382-f33815d3cfa0 | -9.577 | -49.107 | 2025-06-25 02:10:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 1ac83540-1ac8-30bd-a5df-e4d776cd9a35 | -6.1789 | -48.0929 | 2025-06-25 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 5c660951-2e9f-345b-a8d0-c90dedcd13c3 | -7.0174 | -44.5495 | 2025-06-25 02:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 027ffc07-cdc1-3967-8c1b-cb3928040eb0 | -13.0408 | -48.825 | 2025-06-25 02:10:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 973dfc07-10ea-3558-be26-04f4fd7d7371 | -6.1977 | -48.0699 | 2025-06-25 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| dc2b5bd7-4220-34f3-a76a-f2ccccaee9ab | -6.1792 | -48.0494 | 2025-06-25 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 5ff2cfcc-08f7-3769-bc2f-913ed1034b2b | -6.1791 | -48.0712 | 2025-06-25 02:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 250.1 |
| f7ae8950-a355-3859-9f62-a5c710803847 | -6.1792 | -48.0494 | 2025-06-25 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| af272ca1-81e7-358b-a64d-5a5e3efff6cf | -7.0171 | -44.5725 | 2025-06-25 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 87411a54-d6ff-3782-a7f9-89f5419b38f4 | -7.0174 | -44.5495 | 2025-06-25 02:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 41901a8d-7f09-38ea-8bcb-1236f02a022b | -6.1977 | -48.0699 | 2025-06-25 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 72655c69-9f3d-3e22-8852-758a22330b98 | -11.1224 | -46.9745 | 2025-06-25 02:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 3a42346a-c1e4-34be-a4f5-47d862e88894 | -13.0408 | -48.825 | 2025-06-25 02:20:00 | GOES-19 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| be23232b-b852-351f-a1d2-c94e42721acd | -6.1791 | -48.0712 | 2025-06-25 02:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 3a982d0e-1307-3f1e-bf38-e247cd9d1892 | -11.1224 | -46.9745 | 2025-06-25 02:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 7305a878-38df-3806-b61d-1f628683b191 | -6.1792 | -48.0494 | 2025-06-25 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| d32bb9bf-9ee1-324f-93ed-3d7bbe1176e4 | -6.1977 | -48.0699 | 2025-06-25 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e0898505-d321-3b0e-b514-5d4fd93f8424 | -7.0171 | -44.5725 | 2025-06-25 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| efc5c29a-1dcf-37f8-8c72-a984908e4abc | -7.0174 | -44.5495 | 2025-06-25 02:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 3a6af56d-110a-31fb-8734-218c9222dd2a | -6.1791 | -48.0712 | 2025-06-25 02:30:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 186.1 |
| 29b16476-239d-3400-a3c6-64a89e15505b | -7.0174 | -44.5495 | 2025-06-25 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| d2c4c7c9-67e6-3590-afd9-c3180e182a84 | -6.1791 | -48.0712 | 2025-06-25 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 5a9ff4bf-9dcf-30a7-97be-9777e11d4929 | -6.1792 | -48.0494 | 2025-06-25 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| fa4b14f0-5efb-3b28-8f75-9d74c8db51f9 | -6.1977 | -48.0699 | 2025-06-25 02:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 91d59536-015e-30d6-bc00-7b689fa26345 | -11.1224 | -46.9745 | 2025-06-25 02:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 5219ba2c-9278-3225-a6e1-f6a5a1e79c03 | -4.5429 | -48.0151 | 2025-06-25 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 403e7585-9a74-343f-a4c3-c5f199d46f92 | -7.0171 | -44.5725 | 2025-06-25 02:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| f04fb473-c2b1-33ea-9762-e9e9f5cff6d0 | -6.1791 | -48.0712 | 2025-06-25 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 142.0 |
| a83e0470-bdf5-362b-88cc-b8fd6aba0bd8 | -6.1977 | -48.0699 | 2025-06-25 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 3b92d784-f104-3cef-a945-3d710c3d096d | -7.0174 | -44.5495 | 2025-06-25 02:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 41cbc9d9-d314-32d8-b190-0c6fd3804e77 | -6.1792 | -48.0494 | 2025-06-25 02:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| f162bdb0-78ff-3894-90d9-98eb1c494369 | -7.0174 | -44.5495 | 2025-06-25 03:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 258c9af6-3dcc-3f29-a1d8-873ac64b4d1d | -6.1977 | -48.0699 | 2025-06-25 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 34c0b7d4-3378-3ceb-8e9f-5e427b1fe743 | -6.1792 | -48.0494 | 2025-06-25 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| dacc1b4e-2abc-34fb-8061-83b0037a7075 | -6.1791 | -48.0712 | 2025-06-25 03:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 28a49510-17b5-3a17-bd7a-1c47395273f3 | -6.1792 | -48.0494 | 2025-06-25 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2f4a7da8-55c7-3629-9a77-6551f87f7a3d | -6.1791 | -48.0712 | 2025-06-25 03:10:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| ffe80f2d-137f-3f64-84fb-f9dc0733adca | -5.50446 | -35.59508 | 2025-06-25 03:15:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 991d5a6c-f0db-3e5a-a658-bab4c76fec4c | -5.48554 | -42.14489 | 2025-06-25 03:15:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4c1763f8-47ae-3879-bb59-48acc169e737 | -7.20154 | -43.1059 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 10306e0e-4d98-3d6c-8815-5a1099ad6b87 | -8.05965 | -43.10821 | 2025-06-25 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 838bcefd-5f88-3e2e-bafc-e387ba5bebc6 | -7.20657 | -43.09885 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| d7c44da1-b31d-30c5-bab5-10325daec944 | -9.33586 | -40.20813 | 2025-06-25 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 9ce02814-353e-3667-8642-a4f3fb39a5ac | -7.19096 | -43.10345 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 58f29053-a485-3bbd-ab8c-df5655cc05fe | -7.19807 | -43.10475 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 896f3606-6d96-382a-a4e1-e1c735f3e0cb | -7.19575 | -43.09748 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 895a6ce6-2647-3ff6-b1d6-04f00e1a1309 | -9.33552 | -40.20915 | 2025-06-25 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 3992cb94-5e03-3876-be00-9018e0494f16 | -8.06098 | -43.10144 | 2025-06-25 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 158545de-0ce3-36c9-8bba-fa539a2541a9 | -7.20794 | -43.09175 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| e30c77e3-aa67-3a40-b3c2-0be237f0d703 | -9.00649 | -39.88456 | 2025-06-25 03:17:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7d23181b-dae0-3864-ac44-f901d2269c54 | -7.20287 | -43.09875 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 924d0eb1-366a-343a-ae7e-9a53950a2997 | -7.19945 | -43.09761 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| dc78c762-dedb-33e6-88b4-1cdaa787c9ea | -7.19443 | -43.1046 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 5fb731dc-d56b-3064-b5f5-b23f14542e92 | -8.06534 | -43.11634 | 2025-06-25 03:17:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 02e24853-94d8-320f-b8d0-66398a880179 | -9.54841 | -40.35126 | 2025-06-25 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| a2a78a26-ffb5-3de1-b5b6-791927cae6dd | -9.54921 | -40.34706 | 2025-06-25 03:17:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 290c7a39-f4fa-3e72-a41b-a4cda72aadaa | -7.20421 | -43.09159 | 2025-06-25 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 29f76f13-62b0-3ff8-9d39-7accdb656e27 | -14.34732 | -40.90777 | 2025-06-25 03:19:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b3b3bd51-17b9-3cf2-87b5-e4642ae66c04 | -15.40231 | -43.19888 | 2025-06-25 03:19:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 540bd8f7-ef5f-3497-baa5-43b41a12c6b9 | -17.07368 | -45.9515 | 2025-06-25 03:19:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e74fc51b-5aae-3dee-b4ec-8907fd05a01c | -17.07788 | -45.95222 | 2025-06-25 03:19:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 604fce51-83e9-36a5-8141-477fc3388dd5 | -13.60852 | -43.97501 | 2025-06-25 03:19:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e375b49a-8f4e-351c-94b9-5ab364c630cd | -17.08069 | -45.95327 | 2025-06-25 03:19:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bcb55a4-04f7-3266-8438-337c2a825618 | -6.1792 | -48.0494 | 2025-06-25 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c8c4d4b9-711d-3181-a4ec-1db47ac2d0ff | -4.5429 | -48.0151 | 2025-06-25 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7f025ec5-5e47-38b6-917c-614fec94ff70 | -6.1791 | -48.0712 | 2025-06-25 03:20:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 113.3 |


[Clique aqui para ver as próximas entradas](README5.md)
