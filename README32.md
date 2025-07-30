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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93b700f1-cc8f-3b17-8315-e87299659f56 | -18.56426 | -54.75998 | 2025-07-30 04:53:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e640b446-3aff-3bd2-985d-50dc2742462c | -16.10594 | -47.91866 | 2025-07-30 04:53:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66a32e83-6207-3e98-8c03-82bb8f4bc9c2 | -17.48392 | -46.73694 | 2025-07-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 56279aa5-09af-34f1-b43f-b81c3caea2cc | -17.97994 | -45.60293 | 2025-07-30 04:53:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1d4de694-238d-3cf9-8c70-b25196670913 | -14.4127 | -59.33833 | 2025-07-30 04:53:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e1732337-d5fb-3bb5-8a2a-bd3dd0efd410 | -19.74314 | -42.102 | 2025-07-30 04:53:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d1a9a552-bbd0-307a-9596-fcdc327c4e83 | -19.09781 | -44.40752 | 2025-07-30 04:53:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15bf31c3-d55b-3c64-8e6b-1090d6e9ca70 | -18.44623 | -54.6649 | 2025-07-30 04:53:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e5b17c3-9109-35bf-aa3b-dee4b18fc148 | -20.47774 | -53.67603 | 2025-07-30 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d19c63c6-eb7a-3b40-a49e-7b45ebfbc516 | -17.48896 | -46.73763 | 2025-07-30 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c2c31e0-fa93-3066-b9ec-708b7572c787 | -18.40354 | -53.3275 | 2025-07-30 04:53:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a2211d0-9900-39c4-844c-04d8b9ad9858 | -20.29033 | -54.07409 | 2025-07-30 04:53:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a1f92461-992a-3bc6-8b96-f52e7e09b484 | -21.33792 | -55.63003 | 2025-07-30 04:55:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67a9a878-95eb-3d38-8129-5ad52ceebc46 | -21.33735 | -55.63374 | 2025-07-30 04:55:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1190d5c6-0bec-3574-b079-7aacd1cd2bcc | -21.04903 | -55.9828 | 2025-07-30 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab3e5d1a-6406-3c8a-923f-b45e4007e3e8 | -21.33403 | -55.63316 | 2025-07-30 04:55:00 | NOAA-20 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19a54cea-e93a-348f-a379-9fb27f71296b | -21.98575 | -46.82057 | 2025-07-30 04:55:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fcf5d7c-d3d0-3443-8024-958cfeab988f | -21.32256 | -48.69747 | 2025-07-30 04:55:00 | NOAA-20 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 51730a6b-5d87-3e08-ac0b-c4e8eae9ceff | -21.98442 | -46.82002 | 2025-07-30 04:55:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9eba2b04-4a66-3e61-a171-ab13914e1043 | -22.9944 | -49.78358 | 2025-07-30 04:55:00 | NOAA-20 | CANITAR | SÃO PAULO | Brasil | 3510153 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 574b6282-55dd-3ff0-b3a0-1d34eac033de | -21.38923 | -48.67458 | 2025-07-30 04:55:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e188b9f-08e2-36b1-8f23-10cb0b8fa621 | -21.04845 | -55.98648 | 2025-07-30 04:55:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ed8508e7-ec6d-37d2-85ca-1e2cf6a99f11 | -23.00371 | -48.63142 | 2025-07-30 04:55:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2e70619-ec23-3055-a2fe-e5d1ed8d8977 | -10.6169 | -45.2512 | 2025-07-30 05:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| a5ff1c46-70ba-3de5-8cdd-371eb43c9a75 | -8.5211 | -43.3063 | 2025-07-30 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 200dda49-82a6-399d-b58d-f178b8d86b8f | -2.9108 | -48.254 | 2025-07-30 05:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| efce57dc-532c-359a-a486-cb594418801e | -10.6169 | -45.2512 | 2025-07-30 05:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 49.8 |
| cad65538-b1a5-3a70-ab43-fd523e64a302 | -8.5211 | -43.3063 | 2025-07-30 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a8b4a3a8-64cd-3c34-a5f2-624301a351ff | -10.6172 | -45.2282 | 2025-07-30 05:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| ccd73425-6c2f-30fa-84bb-adb6be29f542 | -10.6169 | -45.2512 | 2025-07-30 05:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 41411757-5677-35e8-8cfc-64114ff8aef4 | -10.6169 | -45.2512 | 2025-07-30 05:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 8e38638f-8e81-3d29-9237-c8c5fed6a265 | -4.65021 | -43.12915 | 2025-07-30 05:31:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f55aa14a-5a51-345b-91e1-4cdf52bd92b8 | -4.65165 | -43.11983 | 2025-07-30 05:31:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| cc316e64-97a5-37ba-b99c-1cc6489aefb9 | -2.90155 | -48.2581 | 2025-07-30 05:31:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| eb4b3aae-b5bb-34b4-a28e-86988ebd8d39 | -6.53967 | -43.34679 | 2025-07-30 05:31:00 | AQUA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9146778f-1cc3-31aa-be8e-002c98dd8050 | -3.82362 | -41.56851 | 2025-07-30 05:31:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6a757ee2-5e1b-378e-916a-05f731eec1ad | -7.94088 | -44.08883 | 2025-07-30 05:31:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fd80052b-489d-39f0-8098-f9b1ed802c1c | -3.50472 | -43.24644 | 2025-07-30 05:31:00 | AQUA_M-M | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 06b68066-43ad-348e-ba7b-c249a15d3e42 | -5.67501 | -43.6772 | 2025-07-30 05:31:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7a52a119-efff-3e6e-8d63-3b72d305365d | -7.77565 | -44.99516 | 2025-07-30 05:31:00 | AQUA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2c8ad7c1-c55c-357a-b55f-a493cf61f1d0 | -8.62231 | -45.88522 | 2025-07-30 05:31:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f3453242-4df1-3cea-bb37-54216828944b | -9.55821 | -40.31926 | 2025-07-30 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 40d9438e-88b2-3c5e-8172-52b95861e36b | -6.05646 | -44.25156 | 2025-07-30 05:31:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 45221814-bd4f-3654-9ac2-ef9db47068d7 | -4.59485 | -43.30763 | 2025-07-30 05:31:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 46753eb8-92aa-3f42-b6ff-a3fa5e03e4ed | -9.39439 | -45.48957 | 2025-07-30 05:31:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 53a15000-5c27-3915-b3f2-3827e05d57ed | -8.51555 | -43.30717 | 2025-07-30 05:31:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e6ba91e8-8dbd-37a3-9fc4-82fec2d97f84 | -6.88291 | -44.72927 | 2025-07-30 05:31:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3dfe1821-dc56-39bd-9e5f-578c2733f8ea | -7.15453 | -44.04044 | 2025-07-30 05:31:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26f5c8a7-589c-31ef-8277-9b43223a2730 | -8.94934 | -46.73742 | 2025-07-30 05:31:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5fff07d3-229d-3972-b88d-a469eaf75f5a | -9.55674 | -40.32952 | 2025-07-30 05:31:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 5f8712f8-be32-35d8-9cce-ba0aea0f6135 | -5.40011 | -43.2434 | 2025-07-30 05:31:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ff56119-38c8-3d8b-92eb-bc86f7074379 | -8.01138 | -47.67763 | 2025-07-30 05:31:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 93706020-9abf-321a-9f1f-43400c65dce3 | -2.90499 | -48.23596 | 2025-07-30 05:31:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d8150032-8319-3e6f-ba2d-08e82c159d21 | -7.15306 | -44.05004 | 2025-07-30 05:31:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30397ba5-df4c-330f-ba7a-1e2223e31a0b | -8.51417 | -43.31617 | 2025-07-30 05:31:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.0 |
| 5c866d76-7512-3332-a89a-ad56b6f0c26e | -13.07789 | -47.3001 | 2025-07-30 05:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0d70ed6c-fd90-37fc-82ec-434297c3b559 | -11.45988 | -45.11699 | 2025-07-30 05:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 4f69a7f2-e8be-32ed-ae27-6546130b76e4 | -11.4545 | -45.10937 | 2025-07-30 05:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 660f8789-9e80-324a-b5f8-b1ec4a7b1c0d | -11.55837 | -44.25746 | 2025-07-30 05:33:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b3415d60-3d7e-3d6a-ad84-996907977526 | -12.72617 | -47.00475 | 2025-07-30 05:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| bbaf2022-21d0-3df0-ad8c-fb842f32cad8 | -13.08833 | -47.3011 | 2025-07-30 05:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 1825eab5-8bc2-3d97-9c16-1d708814ccd4 | -10.60912 | -45.23475 | 2025-07-30 05:33:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 352d3817-cb38-376a-aa9f-dfe5c7c99286 | -10.60748 | -45.24498 | 2025-07-30 05:33:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 84847ad6-681f-303c-a68d-799ef75558fa | -10.61687 | -45.24644 | 2025-07-30 05:33:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 7b812d0a-08ab-3c14-a119-fdd546a1105c | -11.46146 | -45.10707 | 2025-07-30 05:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 35760f97-6822-3fb4-88cb-e3a19394e8b3 | -12.72668 | -46.99746 | 2025-07-30 05:33:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f6aaf86a-da14-3f78-89bc-574b1e3a958e | -11.47068 | -45.10863 | 2025-07-30 05:33:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f5d84509-1450-3766-b056-efcf4e4d492f | -12.80683 | -45.4371 | 2025-07-30 05:33:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 130165fa-cc32-3087-a84e-2d364c889cc6 | -10.61851 | -45.23616 | 2025-07-30 05:33:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 47.0 |
| c50e3188-1e07-308c-9a2f-fcba0529aef2 | -10.52315 | -42.55175 | 2025-07-30 05:33:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c7ae21dc-565e-3760-a4bb-d1ba748696a5 | -10.602 | -45.23834 | 2025-07-30 05:33:00 | AQUA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bf3f86a0-e377-38e6-982e-f13bf1ed4714 | -15.7664 | -49.95527 | 2025-07-30 05:36:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 11441cab-2bb9-33ec-ae08-2b9d660a1be3 | -6.55718 | -56.18973 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 715571f0-d055-35a9-9220-6046cb6acaf1 | -6.4976 | -56.20488 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f4da195-91c1-3b88-bf05-61f3200dbae7 | -6.55814 | -56.18278 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7a2967-bd34-314b-96f8-84b7d2041985 | -6.61994 | -59.98299 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 00984045-c692-38df-b627-96d0b55d6862 | -6.50535 | -56.20684 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6147f957-9206-3d40-9f4d-6e5c64911b42 | -6.52877 | -56.1963 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cf6a6748-32a1-3977-8669-696760ac0a36 | -6.54541 | -56.19524 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63d20a01-4c15-3375-8642-d445b2bd3d18 | -6.54495 | -56.19862 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 93c8f604-0965-32b9-bddb-c86dfc25b681 | -6.50981 | -56.2145 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e516f3f6-993e-3c60-8ac9-16b80fae96b7 | -6.56942 | -56.18086 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f30216aa-cb63-3b30-ae8a-c31e745bcd79 | -6.55178 | -56.18895 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ccb99af-c2ad-3866-b5e0-bd2b595d8fd6 | -6.53509 | -56.19025 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c0b4a365-eb4d-359d-ad61-d17a096d66f1 | -6.49564 | -56.21866 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f2633b2a-f0cc-3d40-820a-0f66b46f8c37 | -6.53462 | -56.19369 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7672171a-6182-3e25-8689-5cdf6c809628 | -6.62358 | -59.98733 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc03970d-fbc6-3fce-9716-eece72145704 | -6.68295 | -58.86392 | 2025-07-30 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c925d877-164d-3557-be12-9e1263de9938 | -6.5567 | -56.1932 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46390b6c-464b-34c9-9fc2-4847a4b1d30d | -6.52104 | -56.21272 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd7a6c8a-d65e-3ddd-ad62-36a1a86c88be | -6.50103 | -56.21942 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3f3f072c-ce96-30d5-821b-c84de97fdd60 | -6.50582 | -56.20338 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 79b2efb4-5f5d-33a8-9ba1-c79c964cee1b | -6.49273 | -56.21907 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 44c22744-dad6-371f-a355-e7b75d60ce27 | -6.52151 | -56.20926 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1cddb20c-0a9d-35dd-8329-18afef89c842 | -6.52736 | -56.2066 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fbf5e83-512a-3d19-a81d-f3528292c627 | -6.62304 | -59.9911 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12618a18-782a-35ed-9ec6-cfdd6a4f9bab | -6.52338 | -56.19544 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0672040a-736c-3828-8e77-ebb2daae28be | -6.52291 | -56.1989 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ff4fbfe-f3e1-35eb-a0d9-8577673e3cdb | -6.62721 | -59.99166 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e616a979-ce2b-3dc6-b29e-604d67fc2078 | -6.45477 | -53.36319 | 2025-07-30 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README33.md)
