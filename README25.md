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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5776d88e-c3f5-310e-ae36-e5107ef6b0a0 | -8.33787 | -42.43975 | 2026-08-25 04:08:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f730ad7-32e6-3e0c-82df-dd3aea48b125 | -12.86696 | -48.4931 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df1e9c98-3339-3ad9-be5a-29ee73968e01 | -10.37264 | -45.06289 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 21.8 |
| cb06d6f8-b6bc-3f75-b888-2db8c93608cb | -12.12835 | -45.12078 | 2026-08-25 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4ecad59-5b9d-3c27-9572-41464baabfc7 | -10.57384 | -46.31671 | 2026-08-25 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 928ee810-2b85-38ab-be7e-e511444d0f3d | -12.71276 | -48.38826 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76d011f9-6006-3029-8c88-451edc6bb096 | -13.10116 | -43.36937 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ed6939e-fead-36c6-8ea3-209d69c176ad | -12.75786 | -46.44884 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9ccaa8a2-aa5f-3d44-9531-4c51810c908c | -8.1202 | -47.48154 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44b8a0da-274b-3e53-affc-cf067aa1acad | -12.71118 | -48.39666 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bd0fd44-1180-382c-84f4-5234257aa67e | -8.93898 | -50.16074 | 2026-08-25 04:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70d4f613-5e13-3a6e-bdb3-09c4d3c8ded6 | -12.75438 | -46.44919 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b113161f-ef48-3f38-b182-70619bdfbdba | -8.76537 | -45.79097 | 2026-08-25 04:08:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24e7dc98-e980-3ef6-b98e-47402af81ad3 | -12.19846 | -43.18286 | 2026-08-25 04:08:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e93d84f5-4ffc-382e-854a-c218ab6f350f | -13.09032 | -43.36912 | 2026-08-25 04:08:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed1ae8a2-883d-3a5c-9c07-9536b15de8cb | -12.59028 | -47.92279 | 2026-08-25 04:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09d54542-71ce-3eae-869d-e522bae1cd71 | -9.69033 | -46.05524 | 2026-08-25 04:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0e6914d-820e-35ca-93ce-49d0bc6c44b4 | -8.15582 | -46.69801 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469edd40-61a6-3efc-aa3b-acb013ae51c8 | -10.91422 | -51.0704 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| df370fe9-d768-34d6-8c77-d28d15439bf5 | -7.88682 | -46.33171 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 660c4b07-43ae-3228-ba8f-ea82cbc11ed3 | -7.76566 | -46.15546 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae019eb6-9efa-3e40-954f-85c4ffe94e4a | -13.39334 | -40.06559 | 2026-08-25 04:08:00 | NPP-375D | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 596416ef-ef77-3865-b81a-e14a4ecf89c2 | -13.35006 | -48.20073 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0b09017-525e-3522-b9a1-cf3b2b1a6fc3 | -6.84135 | -52.50696 | 2026-08-25 04:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d5aa2afd-fd3c-3be4-bd17-dfe51a1edfba | -9.9808 | -48.32011 | 2026-08-25 04:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7856376-e3ca-305e-bb02-ce274020ce7f | -11.8831 | -43.82475 | 2026-08-25 04:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 441ad617-f675-3762-b73e-7f4630016689 | -8.10201 | -47.49426 | 2026-08-25 04:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41d8db40-09c1-3157-9377-fe4f19cac7bf | -7.67586 | -49.38535 | 2026-08-25 04:08:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e30e92-132d-3fc1-b74b-8cb009e0a72b | -13.44387 | -43.8481 | 2026-08-25 04:08:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa6e1169-09d1-3709-a28b-1c701fb6a8a9 | -10.05287 | -48.45415 | 2026-08-25 04:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3d2c04f3-c256-3d8d-b7af-8bb483e2e501 | -12.78658 | -44.26402 | 2026-08-25 04:08:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eeb3aa53-f3a9-3959-be23-7ecea662f71c | -14.80096 | -48.76801 | 2026-08-25 04:08:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42c18213-7b33-3de6-a682-6215b4c5c401 | -8.33418 | -42.43913 | 2026-08-25 04:08:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6caf9add-e409-3847-a602-8c003d329428 | -10.8695 | -50.58457 | 2026-08-25 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ca840d6-c533-38d1-a06b-cacf81e2c925 | -10.31765 | -50.40822 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e77fbc98-7684-3996-801e-1e875b4c4ee3 | -9.57087 | -49.23361 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebb296bd-9a92-3e71-bd0c-1f98a0c36bac | -12.75156 | -46.43948 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e8e9241-cbc4-3d37-8459-9f4cc6daf594 | -12.85054 | -48.49672 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac67cd60-1adf-372b-ad81-a73e04bbbc1d | -10.8746 | -50.59031 | 2026-08-25 04:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cbf491c-1d1e-318c-8c75-5f0e13ceba2c | -12.86199 | -48.49167 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1898a336-568d-3f1d-bdd4-ef8af5297ea0 | -8.07866 | -44.6472 | 2026-08-25 04:08:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 725b2adc-d8b3-3c19-89e1-c74b2f927128 | -7.886 | -46.33639 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b18c9e0b-03cb-3bd9-ac76-00d773e5a118 | -12.74663 | -46.45996 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6904d988-e3e1-3618-994f-dca22ce041dc | -10.47705 | -50.43824 | 2026-08-25 04:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa40c8c0-a65b-3dad-8468-b9465b99bfbb | -12.75345 | -46.44799 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f04b19e-57c0-3086-a099-98aa7c215e23 | -9.65746 | -48.32255 | 2026-08-25 04:08:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddd04ccd-526a-32dd-862a-28f5aa89b00a | -12.73622 | -46.47388 | 2026-08-25 04:08:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a05302e-6b7b-3b68-b81f-160f9152abc1 | -10.91291 | -51.06824 | 2026-08-25 04:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 467872eb-3d84-3870-92b2-cd6998ad0405 | -9.60157 | -45.37664 | 2026-08-25 04:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10d59375-30c4-3065-a743-c1b7c802b661 | -12.70561 | -48.41554 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6cca23f0-ec87-350d-a44d-4eefb595ee85 | -11.9846 | -45.9139 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22fa6758-9896-3f02-84d6-7704d4427ad3 | -13.35909 | -48.20678 | 2026-08-25 04:08:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 91d17ab8-b281-3f50-a126-be9e35de520c | -9.56528 | -49.23243 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74db68eb-4175-381f-9930-eb4c4419662f | -11.43613 | -44.55311 | 2026-08-25 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dee833e4-4e75-35ee-a7e5-1555d4bc3f21 | -10.36492 | -45.05751 | 2026-08-25 04:08:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 7fd68d93-4bb1-3ddb-a772-6f345ae0a02c | -11.99029 | -45.93224 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf2b97d0-ff40-3443-b94a-cc6d201798f2 | -11.40165 | -45.17064 | 2026-08-25 04:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9f6241d-ff75-3f80-9831-d2687e702ff4 | -11.13592 | -44.48152 | 2026-08-25 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ca9f6dd8-c7a8-33ab-9602-2ba7af4366c3 | -11.99102 | -45.92807 | 2026-08-25 04:08:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 071765f3-bcd5-3d52-b86f-121ecd74719a | -10.5747 | -46.31192 | 2026-08-25 04:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c82d902-0c49-3e53-83ef-ded840b2d3ad | -15.68008 | -42.47302 | 2026-08-25 04:08:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dcef507-b21d-365b-ad85-04a18723bd62 | -7.90242 | -46.3837 | 2026-08-25 04:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43ac7052-9472-3029-b294-e76b8ba03d89 | -12.72343 | -48.387 | 2026-08-25 04:08:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f91f9d-b91e-3114-9778-d013a2e51ddb | -9.53168 | -49.2753 | 2026-08-25 04:08:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26a35d74-6f0f-3ca5-8a22-a03f158bdc59 | -12.88079 | -48.50303 | 2026-08-25 04:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 350ba37d-b578-357f-8343-040892206ac3 | -8.16391 | -46.6956 | 2026-08-25 04:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0924454a-6434-3f05-8843-3fd65c6ebd2c | -7.0057 | -59.2575 | 2026-08-25 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 302.2 |
| 44faa3bd-f84a-3c84-880c-65dbd5cfe389 | -3.5407 | -48.1673 | 2026-08-25 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| ac78192a-bbdd-34aa-b195-047307ed32bc | -11.1252 | -44.4892 | 2026-08-25 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 3a5a46f8-d63b-34f2-9ca2-e90daa99459e | -3.5406 | -48.1889 | 2026-08-25 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 6bc2b9e1-10aa-3ccf-8595-7ea1a5901597 | -11.1256 | -44.4659 | 2026-08-25 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5bc5eb2b-5903-38cf-9b6c-6d0dcd43accb | -6.6226 | -58.4995 | 2026-08-25 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 4234c628-eb85-37be-8f63-3a9ffcab108f | -10.7988 | -50.9305 | 2026-08-25 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 72c333c2-9872-32f4-a1a8-572b5c7d6ae7 | -6.9873 | -59.2389 | 2026-08-25 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 295.8 |
| 673eece4-d6d6-3a89-b187-4b24fe5b98e4 | -6.641 | -58.4987 | 2026-08-25 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 5cf5bca9-35f8-3305-8f15-f443f5d91fa9 | -3.5221 | -48.1896 | 2026-08-25 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 86d8c868-3fc9-320c-9826-82521298d2fb | -7.2903 | -45.3456 | 2026-08-25 04:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 802e55ff-887c-3a63-a9f6-7ef95c297ccb | -11.1443 | -44.4865 | 2026-08-25 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 174.0 |
| 2609b199-9807-3434-a81a-0d1af2377401 | -10.3727 | -45.0537 | 2026-08-25 04:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bc471a3c-2af8-38fe-a178-137592c5a918 | -11.1447 | -44.4632 | 2026-08-25 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 175.2 |
| d3e9aabb-c634-34fd-8c79-e499c8e0069c | -10.7799 | -50.9325 | 2026-08-25 04:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2e5111f2-f3c0-3190-a486-8719cafceed7 | -6.9872 | -59.2582 | 2026-08-25 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 343.8 |
| af699fb1-13d7-3efd-9fa4-3d5f37960d6f | -7.0058 | -59.2382 | 2026-08-25 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 269.6 |
| feaacaf6-ed17-3cb3-8742-fb01a510849a | -7.2901 | -45.3683 | 2026-08-25 04:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 87d75ac3-9841-337d-89c5-819357ac181e | -3.5222 | -48.168 | 2026-08-25 04:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d3ed6243-72ec-3014-9c50-ed294e5e9db8 | -16.48023 | -47.93708 | 2026-08-25 04:10:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e105e993-8806-3178-8dad-98c8cba78941 | -16.39465 | -49.93539 | 2026-08-25 04:10:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f69baffe-56fb-3a61-9c36-6ccf8cef0629 | -14.3782 | -51.96437 | 2026-08-25 04:10:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ca492a4-1dd5-30c9-8eff-eb33eb3b28de | -16.48115 | -47.93541 | 2026-08-25 04:10:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e9f24de0-c3a2-379f-b9be-2b4af75e20bc | -16.63831 | -49.40937 | 2026-08-25 04:10:00 | NPP-375D | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5a90c5e-a0e4-3592-84aa-57f5b7a89a51 | -14.9809 | -52.68721 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40b7f975-2bb9-34fd-8020-a93cae30b90e | -15.24814 | -52.79391 | 2026-08-25 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee06a0c2-c7d9-32d8-8815-aee7784eab74 | -18.97788 | -49.02452 | 2026-08-25 04:10:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8e0611a-b367-305c-9df6-43964b9110f5 | -16.44037 | -43.46835 | 2026-08-25 04:10:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ae746dd-358b-303d-a93e-0b86a53b9e8f | -22.44919 | -47.40995 | 2026-08-25 04:10:00 | NPP-375D | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a0cd1113-dc4a-3265-a6c9-cd3b1f4aa864 | -20.84158 | -48.78953 | 2026-08-25 04:10:00 | NPP-375D | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 393cbf12-cb5b-3807-9c00-d2baf7472606 | -13.86739 | -54.04329 | 2026-08-25 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f524aca5-ed3f-3727-80d1-5111067d02d4 | -20.96854 | -48.8437 | 2026-08-25 04:10:00 | NPP-375D | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c39ade0c-dd55-39b5-885d-ba45768efc7d | -13.8606 | -54.0082 | 2026-08-25 04:10:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 659e7420-0ad3-389f-8098-c9b233029ca3 | -16.25329 | -41.77366 | 2026-08-25 04:10:00 | NPP-375D | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README26.md)
