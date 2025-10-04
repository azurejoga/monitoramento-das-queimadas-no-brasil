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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08a0ed1b-b404-3c53-be64-007998c6ee1b | -13.8283 | -43.1702 | 2025-10-04 13:00:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 142.0 |
| d43ab19d-0d38-3fee-b14a-708e2adadc6d | -8.1966 | -39.3864 | 2025-10-04 13:00:00 | GOES-19 | TERRA NOVA | PERNAMBUCO | Brasil | 2615201 | 26 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 1786574c-c326-3644-9ec0-4f5582bf2206 | -12.0891 | -45.1814 | 2025-10-04 13:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| d7435954-d72f-3f51-ade9-e0890d2aff5b | -8.834 | -46.7917 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| d65b51fa-3f6d-3e7d-83a2-57055abaaddd | -7.7938 | -42.5607 | 2025-10-04 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 131.9 |
| ee2abf31-3fae-32c6-a0d3-a21fb999631c | -12.6512 | -46.9894 | 2025-10-04 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 1881b76a-c5e9-383c-a233-902cd93b05a9 | -11.5492 | -47.6773 | 2025-10-04 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| a3b47eb0-9049-394d-b6e4-56ad3277cdc5 | -12.7194 | -48.5611 | 2025-10-04 13:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 2e0e58e2-282a-3e8d-81e0-fd5b642ad131 | -7.7491 | -46.2944 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| b2edcc07-a802-3c48-9789-c12e04892b61 | -10.5648 | -48.6981 | 2025-10-04 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 102.1 |
| fae1d0eb-4fb2-3f39-8591-d02450e9bb29 | -13.3233 | -48.077 | 2025-10-04 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 757a4d37-463b-3b92-bee5-38a571e5a4ca | -13.2938 | -47.5905 | 2025-10-04 13:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| e1e2018d-fbd0-3eaa-a11f-85b7544ae76d | -9.3382 | -45.772 | 2025-10-04 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 685ebbc9-a83e-3698-ac6d-247d19f61277 | -12.2341 | -47.8309 | 2025-10-04 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 025c66d2-2016-3950-b545-d7f16dff3c89 | -14.251 | -46.0991 | 2025-10-04 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| b60a02a3-3d58-3377-a4e3-554cd595a019 | -9.3196 | -45.7515 | 2025-10-04 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2cb3e218-fa0a-3172-8d8b-38292c10afe7 | -11.792 | -46.8409 | 2025-10-04 13:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| a3abfe6f-1f65-3ef8-b020-b74dae33bec2 | -7.7935 | -42.5845 | 2025-10-04 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 2d699b3b-a4f4-3113-802d-c66056a5f8ca | -14.2126 | -46.0827 | 2025-10-04 13:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 226.2 |
| 4af94bb1-5dce-3d6e-aedb-c4a731b18fb3 | -11.5683 | -47.6749 | 2025-10-04 13:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 61946437-5585-3d21-a832-fb87480339d2 | -8.5601 | -47.6373 | 2025-10-04 13:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| bbf98687-5cc7-3dd3-9cab-e358317ea8ba | -7.7941 | -42.5369 | 2025-10-04 13:00:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 140.4 |
| bfecd5e4-b75b-3b5b-8e72-41ed530a3f23 | -7.793 | -44.1535 | 2025-10-04 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 534ea83e-04cd-326b-8641-362c9ab09ac2 | -16.0212 | -50.9425 | 2025-10-04 13:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 21d9b600-7ec9-38e9-9f9b-c1d2fbb44654 | -10.5835 | -48.7178 | 2025-10-04 13:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 4b2e6b98-300c-3a5a-a567-41fda86bffc0 | -8.9948 | -47.4845 | 2025-10-04 13:00:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 78f54cee-930c-3a21-b653-edad366f33ff | -9.9396 | -50.2304 | 2025-10-04 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 46d833ca-ac3d-3c82-94cf-788e7de0abdd | -7.7684 | -46.2479 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 9672d285-e73b-3cad-9ec7-26456eddc9d0 | -7.5504 | -42.3965 | 2025-10-04 13:00:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 187.8 |
| f6e0e3dc-a4dc-36de-82b4-b60b90d6870a | -12.8761 | -47.2937 | 2025-10-04 13:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 23a366d4-0dd0-386c-a63c-852651560c32 | -11.8818 | -44.9815 | 2025-10-04 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 4b7dd27a-ffe1-3a32-b8cf-982f6a671e9f | -12.9279 | -50.9862 | 2025-10-04 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| cf292c44-dcee-3884-9a30-ee380b23a58c | -9.3379 | -45.7947 | 2025-10-04 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 65ec9219-7e1e-3783-a685-48da2e7a4341 | -9.1114 | -44.4029 | 2025-10-04 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f010fac9-f579-370b-808d-cf5779d1f8cb | -13.9383 | -48.1852 | 2025-10-04 13:00:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 0818edd7-5804-320f-bfc9-f52cc0926f21 | -12.9471 | -50.9838 | 2025-10-04 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| e8737603-f7dd-3573-bbe0-fb05a08c5f5c | -9.921 | -50.2109 | 2025-10-04 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.3 |
| a4f74415-71ff-3a82-9e0b-2099522f803f | -12.3853 | -50.2595 | 2025-10-04 13:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2e7512b8-afdc-381d-9b0e-12a91c92a27d | -7.7687 | -46.2255 | 2025-10-04 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bbb62eda-06f4-3dcd-bad0-6f1a58773ff1 | -14.672 | -48.2933 | 2025-10-04 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 1150532f-c38b-3d0b-8d7b-c610272237a5 | -14.3899 | -45.9601 | 2025-10-04 13:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 142.6 |
| efab60ee-52a9-3e6a-9d3c-4f210fcea97a | -14.7527 | -48.1462 | 2025-10-04 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| b0715429-5049-3679-a72f-f9d03080ddd7 | -9.3382 | -45.772 | 2025-10-04 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 4d0242a3-370c-3025-ba00-9ce369f55046 | -7.0558 | -42.7782 | 2025-10-04 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| 7a5a7e8a-e2cf-3bc8-8268-79abff3a949a | -13.1333 | -47.949 | 2025-10-04 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 36217061-be2d-3afa-b778-5a8b7d00d038 | -13.3426 | -48.0742 | 2025-10-04 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e5b24194-dfc5-3497-9c34-1901d1713d5b | -12.4364 | -44.079 | 2025-10-04 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ca88f3ae-0b51-3799-9e1c-b829254af930 | -7.0372 | -42.7563 | 2025-10-04 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| e8a9dadf-3b07-3b1e-9430-fa039a3083fd | -12.3162 | -45.3545 | 2025-10-04 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8d0f8a2e-4a02-3e5c-8179-bf01bef1927e | -7.7933 | -44.1304 | 2025-10-04 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a5225a01-7054-374d-a8a2-137ecbb7399e | -11.4877 | -46.7696 | 2025-10-04 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 07ea1f77-dcd6-3637-a999-a92ed7b657d3 | -7.5316 | -42.3985 | 2025-10-04 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 118.0 |
| 6601b926-c176-3ab4-897d-297840f5050e | -15.5211 | -46.838 | 2025-10-04 13:10:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 169482ef-c165-3817-8237-86878b831fee | -7.878 | -48.2021 | 2025-10-04 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 892351bd-5b1b-339f-bf34-3a6b56d806d8 | -7.793 | -44.1535 | 2025-10-04 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7cfe278f-e2ef-36c0-b2d7-ab99728668cd | -7.7491 | -46.2944 | 2025-10-04 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 758e3ad2-3355-324d-9db0-dfc2b178afd2 | -7.7941 | -42.5369 | 2025-10-04 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| ff6527bc-01e0-33dd-96ff-e18bbb7fb942 | -10.5838 | -48.696 | 2025-10-04 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 3645b4a0-f099-398e-ae19-6f7664d6e73b | -7.7489 | -46.3168 | 2025-10-04 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 0decb99d-9a37-307f-9825-db3b8e7057dd | -7.5504 | -42.3965 | 2025-10-04 13:10:00 | GOES-19 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 190.3 |
| bc165996-4c69-3bcd-ae20-ae7e6397edb5 | -7.0369 | -42.78 | 2025-10-04 13:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 209.8 |
| 5ebb04a0-083f-3646-b8bc-cf2604222a74 | -13.3127 | -47.61 | 2025-10-04 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 36c38a14-060c-3db8-bb8d-0857dec1686a | -8.8526 | -46.812 | 2025-10-04 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 94f3a602-5d88-31ae-a775-b692cb9e23a0 | -7.7938 | -42.5607 | 2025-10-04 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 125.1 |
| 203e9795-4fe9-3a4f-8dc4-100c14424251 | -12.6512 | -46.9894 | 2025-10-04 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| 7788af99-b6d3-38cf-946e-5ab8370e0252 | -14.3904 | -45.9369 | 2025-10-04 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 80898f4f-9d71-3484-ab19-7d9759c7d154 | -9.9396 | -50.2304 | 2025-10-04 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| cb057a37-9922-3486-8c45-955af48faae6 | -8.5458 | -47.264 | 2025-10-04 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 698f183f-7c47-3bcf-9eeb-b6848a437ce6 | -13.0959 | -47.8876 | 2025-10-04 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 40b50a29-9cd4-3535-a6c1-e508647fceea | -11.8818 | -44.9815 | 2025-10-04 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 4b69f5c5-0978-3f7b-b6df-89ec445e30c1 | -12.8761 | -47.2937 | 2025-10-04 13:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 542bbad7-347c-363c-be49-9cc7270f2997 | -12.4171 | -44.0821 | 2025-10-04 13:10:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 174.1 |
| 43e9fc1b-9d60-3762-9c61-aca63df5c440 | -13.2938 | -47.5905 | 2025-10-04 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6a2738a3-b6bd-3e0c-b4ad-45d3b8b8cf56 | -9.1716 | -49.9408 | 2025-10-04 13:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 5a4e1fa2-f284-3f5a-aeff-48c4b7231107 | -12.0895 | -45.1583 | 2025-10-04 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e722b9b8-e6ce-3262-a539-58595c7b0178 | -11.5069 | -46.7671 | 2025-10-04 13:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 507.9 |
| 3113c79f-c8a6-393d-a67c-8520b7fce4d7 | -11.1458 | -47.9054 | 2025-10-04 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 142ff6cf-74fe-33fe-93dc-0018a3a149d5 | -12.8401 | -50.504 | 2025-10-04 13:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 38442802-aa56-39c5-bfde-67ea8405e084 | -9.9393 | -50.2518 | 2025-10-04 13:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 4ac146fe-f0e8-3949-a630-f48c54847b79 | -7.813 | -42.5349 | 2025-10-04 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 136.3 |
| 7e876662-0591-3574-bb97-3368a584d61a | -12.3158 | -45.3776 | 2025-10-04 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 7768f218-3bcc-3c1d-be3a-5fd09e105df8 | -10.5648 | -48.6981 | 2025-10-04 13:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 5a13edde-9cc1-3299-a8fb-f0fccf0b3ba6 | -12.0891 | -45.1814 | 2025-10-04 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0555aa5f-3977-359c-a892-f48a0c0dd551 | -11.5683 | -47.6749 | 2025-10-04 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| f3d25f47-7c3c-3f47-b4ba-14922b7641c3 | -14.3899 | -45.9601 | 2025-10-04 13:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 264.6 |
| ce06972d-bd32-3023-93ca-33e382910abb | -10.8241 | -46.5863 | 2025-10-04 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 52583631-e11c-3da6-baad-0bed7b19cef1 | -7.7935 | -42.5845 | 2025-10-04 13:10:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| b5a5942e-740f-3323-a494-d9c77c49d45c | -7.0416 | -45.7962 | 2025-10-04 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| e4dc0b77-c01e-32f4-8c10-23a84de47bf6 | -11.4486 | -43.504 | 2025-10-04 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 3e61ab50-08c4-356b-bb3c-d78465d77ff0 | -11.5492 | -47.6773 | 2025-10-04 13:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 10735569-eaca-30c1-bbfb-815382073aa6 | -15.9574 | -43.3423 | 2025-10-04 13:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 7fb6eb7f-7a30-332f-8649-770463ca2902 | -7.8593 | -48.2037 | 2025-10-04 13:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 224.5 |
| 6ca34434-856e-3b31-9145-7e3a57bc4a4a | -6.8774 | -47.2334 | 2025-10-04 13:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| bf7104e8-6104-3751-a68c-b99af467e0fa | -8.9948 | -47.4845 | 2025-10-04 13:10:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 23fe31fe-291a-3af8-a1d3-ce869156df9b | -14.2126 | -46.0827 | 2025-10-04 13:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 167.3 |
| 1ca2ab8d-86b6-3c01-9f58-15423639b4ca | -14.6716 | -48.3157 | 2025-10-04 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| d07b5386-1d0b-3036-abb4-9f33b0ae8fa8 | -7.7566 | -42.5172 | 2025-10-04 13:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 7569e3ad-b50b-3d51-ab9f-3e79a8ea2317 | -14.3171 | -52.9131 | 2025-10-04 13:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 60feff72-91ef-37ee-8b1a-6e716b2301bd | -13.5912 | -48.1709 | 2025-10-04 13:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d87e1aeb-eb06-3b70-8e48-948b735f7ccd | -13.2934 | -47.6129 | 2025-10-04 13:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |


[Clique aqui para ver as próximas entradas](README148.md)
