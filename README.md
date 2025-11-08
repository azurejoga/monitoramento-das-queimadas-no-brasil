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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b4a8527-0ddc-3c03-a2e9-fb4422c3353e | -4.7023 | -46.3842 | 2025-11-08 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 176.0 |
| fa06c98f-90c2-35a9-a8b5-96d3ca5ebac3 | -3.4058 | -45.4424 | 2025-11-08 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 111.5 |
| b743f97b-fb36-37d2-9b18-6668f2f12ddc | -4.3925 | -45.3728 | 2025-11-08 00:00:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0e10859c-4401-3c09-bf32-7ee7fa07b3a4 | -20.1893 | -47.3735 | 2025-11-08 00:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 11d4a223-4f01-3c5d-b836-ea54cdc9060b | -3.3464 | -50.1979 | 2025-11-08 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| d01c6873-3f1f-3d07-abe8-a5a75ad8b33d | -4.3846 | -49.6723 | 2025-11-08 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 87ba7d61-db75-3792-b0b6-fe5a370a22af | -4.6835 | -46.4074 | 2025-11-08 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 680.3 |
| 30816687-123e-3314-941f-6e906696065e | -4.1161 | -48.0136 | 2025-11-08 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 84d8e2d9-5ec3-39e5-b6d1-e13e801fa09a | -20.1886 | -47.397 | 2025-11-08 00:00:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 152.4 |
| e308e311-6ace-306a-915d-85842bc17c2b | -4.4633 | -43.2152 | 2025-11-08 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 262.9 |
| 4417c322-1efd-394b-89c4-5b52485732f7 | -4.3927 | -45.3503 | 2025-11-08 00:00:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f586d895-c999-3fd1-a1a7-e9b64609daed | -4.482 | -43.2141 | 2025-11-08 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| fe24e45a-aedd-3a7f-b478-8ae613dc686e | -3.0909 | -45.2074 | 2025-11-08 00:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 43d2b27b-f87d-3cb0-9a30-bada73685b02 | -4.6837 | -46.3852 | 2025-11-08 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 297.1 |
| c053a0ed-d4fc-3dcd-a916-5f54c2ec0ac2 | -2.7026 | -49.5422 | 2025-11-08 00:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 9460fb4a-97a0-3521-b529-386e6b7bcafd | -4.4632 | -43.2386 | 2025-11-08 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f491a9e5-43d7-3f69-b525-9db2ef5bcfdb | -3.0908 | -45.23 | 2025-11-08 00:00:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1407b559-960a-33cd-bcfe-0c4cd4fe2257 | -3.6601 | -50.2711 | 2025-11-08 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 469382ec-9246-302f-91c7-24184c4d9180 | -4.4635 | -43.1919 | 2025-11-08 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 9605e345-307f-3df4-8604-0456c95b67cf | -4.7021 | -46.4064 | 2025-11-08 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 389.0 |
| 1d2b57a4-355f-3501-bb2b-860bbf2d34b7 | -3.6601 | -50.2711 | 2025-11-08 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e5e00468-2b9d-3db3-8796-eac36f637390 | -4.6834 | -46.4296 | 2025-11-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 1bd79cee-76e2-3538-9609-392ce8241ebb | -3.3464 | -50.1979 | 2025-11-08 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 2ca873c2-1d1e-3550-81b0-f97a6d8eccc3 | -4.4446 | -43.2164 | 2025-11-08 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 315220cc-2dce-3845-b351-bae678c2c8f2 | -4.3927 | -45.3503 | 2025-11-08 00:10:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 42c82b35-32a1-3cdd-844e-162f396953a1 | -20.1886 | -47.397 | 2025-11-08 00:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 200.4 |
| a3386547-26da-33bd-983e-a314b9e2d192 | -3.4058 | -45.4424 | 2025-11-08 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 104.4 |
| de27efa7-5258-3f7f-98a5-a6515eff6326 | -4.6837 | -46.3852 | 2025-11-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 276.2 |
| 8b031c96-a09e-3da8-9492-cc3de69c9a7b | -4.4633 | -43.2152 | 2025-11-08 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 242.3 |
| 39a868b5-7b14-3ca3-8e93-c3e4c2cd2334 | -4.3846 | -49.6723 | 2025-11-08 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| b96332f2-2783-3e2c-8dc7-65264fecbd6e | -4.482 | -43.2141 | 2025-11-08 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 19bc93a1-0d07-36cc-81fd-bf46ef4eb62e | -20.1893 | -47.3735 | 2025-11-08 00:10:00 | GOES-19 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 6d977238-aca7-32e1-b740-069ba484270a | -2.8308 | -49.8346 | 2025-11-08 00:10:00 | GOES-19 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| acf28d44-161c-3e3e-888f-386f60d0c9a1 | -4.7023 | -46.3842 | 2025-11-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 6b70cd5f-9653-36db-ad19-7e06790e7c7d | -4.7021 | -46.4064 | 2025-11-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 195.6 |
| da96299a-c887-3a54-877a-3e0a223dd7ab | -4.1161 | -48.0136 | 2025-11-08 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| c03b6468-38fd-315f-97b7-2b4766b9357a | -4.6835 | -46.4074 | 2025-11-08 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 558.8 |
| 75ed74a3-af9c-3b4f-8eae-c9d71dc00d25 | -3.3463 | -50.2189 | 2025-11-08 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| d42a7ba9-f60d-3d95-8aaa-2e68f6e45831 | -3.2991 | -44.4735 | 2025-11-08 00:10:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| e1fbed9f-c941-383b-bc36-685fb70f15cc | -3.0731 | -45.0501 | 2025-11-08 00:10:00 | GOES-19 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f4f9310a-88ea-37cd-b834-c12705f8f211 | -7.7929 | -46.6376 | 2025-11-08 00:14:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 867a45c5-d820-3925-b213-e01ced060f61 | -6.651 | -44.472 | 2025-11-08 00:14:00 | METOP-B | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4445746f-3d21-3325-bd0b-ce36770f07a1 | -3.0273 | -50.258499 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 240e0d1e-889e-35d6-973f-d95f4beb3e74 | -4.6267 | -45.886501 | 2025-11-08 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| adecdcdb-f907-393e-b1a7-c5f3c0e257dd | -13.0507 | -50.277302 | 2025-11-08 00:14:00 | METOP-B | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8e098ef2-c599-3024-b508-6b762ac464f1 | -4.514 | -41.916302 | 2025-11-08 00:14:00 | METOP-B | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63f8773b-1bae-30c3-b43b-511d6817a260 | -4.587 | -45.980598 | 2025-11-08 00:14:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71ea5b6f-5cce-3815-9e1f-fb736f605a0f | -5.6512 | -46.388901 | 2025-11-08 00:14:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78acd250-b539-3c59-baed-644f2be8f6be | -8.2001 | -46.967098 | 2025-11-08 00:14:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9a78185-887a-325f-a837-73d750ded446 | -8.0677 | -47.1078 | 2025-11-08 00:14:00 | METOP-B | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 575a8973-d21b-34d3-b653-45c902191994 | -4.825 | -45.5905 | 2025-11-08 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 462e40d4-0eb2-3f2e-a829-b22ab3ccecc4 | -5.4712 | -46.104801 | 2025-11-08 00:14:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5dfcc6d0-97e1-3926-9284-4ed30e8e8c41 | -5.6375 | -42.996799 | 2025-11-08 00:14:00 | METOP-B | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1e9b44be-e404-3868-8240-56381342baed | -4.5772 | -45.9828 | 2025-11-08 00:14:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 99cf9959-639e-3967-b4a0-9cd0d2fb6189 | -15.1847 | -49.503502 | 2025-11-08 00:14:00 | METOP-B | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb73d29-e441-3335-a74f-e4fbde3f23a1 | -14.6739 | -51.884701 | 2025-11-08 00:14:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4502834e-0c7b-348c-924c-a662902d265f | -3.1462 | -50.5998 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3101fa9e-55fe-3241-906b-5f38311f279e | -7.5748 | -42.294498 | 2025-11-08 00:14:00 | METOP-B | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 63d38145-57e9-36b1-8b61-343897a3b04e | -9.4939 | -47.338799 | 2025-11-08 00:14:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddfd20dd-ff34-3de1-8b05-90d095b233f8 | -9.1397 | -51.287201 | 2025-11-08 00:14:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5edd88-5e2f-311e-bda3-72f9e8667fd5 | -4.4263 | -47.592602 | 2025-11-08 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad8199de-6677-387f-ada4-aad4bf080bc8 | -4.3546 | -46.794601 | 2025-11-08 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ffa3ea30-db7e-3a70-84a0-eee98a82ad30 | -8.0091 | -38.5229 | 2025-11-08 00:14:00 | METOP-B | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 356c90e8-4389-3826-ac86-063f36e66fee | -4.8397 | -45.6092 | 2025-11-08 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4c8a16b-383e-38f3-b27d-4022db014d24 | -5.3471 | -47.117901 | 2025-11-08 00:14:00 | METOP-B | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 343a055b-4f77-30fc-aad3-356351129cc6 | -2.8262 | -49.828201 | 2025-11-08 00:14:00 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2079cee6-cd5a-36c6-97b7-f868aab33155 | -6.2185 | -47.317699 | 2025-11-08 00:14:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb701ad6-267b-3cb5-9085-5f5b289994de | -6.7258 | -44.139301 | 2025-11-08 00:14:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b5b48f8-27ec-3a38-b71f-0cb98f67c594 | -4.3686 | -45.356998 | 2025-11-08 00:14:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad0f43c8-5f72-31c8-b0ae-3ddf34868597 | -4.6725 | -46.390499 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30c45c55-4ec6-3ac1-8d74-fe4b758b8e7f | -4.6903 | -45.8503 | 2025-11-08 00:14:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3f6b037b-729a-32bc-9d17-b629fd8ebfaa | -4.6823 | -46.388302 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff235549-34c8-3dd0-80a6-b465cb65a02f | -10.1289 | -46.520199 | 2025-11-08 00:14:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 97e604ac-2e60-3f62-a73a-7cf281b15f79 | -8.0187 | -38.520302 | 2025-11-08 00:14:00 | METOP-B | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 0a9216a7-c261-368c-87bb-bfe17ebbee8a | -9.1089 | -48.897301 | 2025-11-08 00:14:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ad05658-bf6f-307e-ac5e-1f33b7ba0672 | -4.4244 | -47.5844 | 2025-11-08 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d28bc0ce-e133-35e8-ae67-6e9c77361e71 | -4.4897 | -45.128399 | 2025-11-08 00:14:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6034cc34-c290-394c-bd6f-c07e3421ae99 | -5.4367 | -44.649399 | 2025-11-08 00:14:00 | METOP-B | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 66caa19d-c9d8-3fd1-bc72-fec8641e4490 | -2.4251 | -48.030701 | 2025-11-08 00:14:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c86c1c8-35b7-35d4-9911-935751fdfd73 | -4.4631 | -43.197399 | 2025-11-08 00:14:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b55dc7e9-53c7-3294-9bf3-e49190ea5d94 | -4.6943 | -46.395401 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6be1e3-6eb3-3749-b709-287f60c3bd70 | -5.4402 | -47.741299 | 2025-11-08 00:14:00 | METOP-B | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bf714dd7-3053-3033-85c9-8b31b5059ff2 | -6.0158 | -49.123299 | 2025-11-08 00:14:00 | METOP-B | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 042223dd-7b17-3f22-bcd6-a349f1a594ab | -8.9026 | -47.815899 | 2025-11-08 00:14:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac2cac6d-02c4-36c3-864a-1202f1ea6703 | -19.4785 | -53.929199 | 2025-11-08 00:14:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2a112fdd-4457-37c7-b258-c63361d8ef87 | -6.2204 | -47.325802 | 2025-11-08 00:14:00 | METOP-B | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7619b01e-fdbf-34cc-9d94-60ba8a0cbf75 | -5.4142 | -44.814701 | 2025-11-08 00:14:00 | METOP-B | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f162506-d109-3510-b16d-c28913d8a359 | -13.9343 | -50.0401 | 2025-11-08 00:14:00 | METOP-B | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c7c65170-28cf-3c2d-b294-0f296c43e431 | -3.1446 | -50.592899 | 2025-11-08 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e53b978-287a-31c8-9d12-d4fb96894f31 | -4.9175 | -44.5438 | 2025-11-08 00:14:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bb9d015-47f7-3063-b1b6-66782bedfbca | -6.3 | -48.653301 | 2025-11-08 00:14:00 | METOP-B | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9ec3840-8f6c-34d3-bcc9-04f2487220b8 | -7.7578 | -49.256901 | 2025-11-08 00:14:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5672421-5e26-3ebe-b7ee-f0e991e1c117 | -4.2879 | -45.671101 | 2025-11-08 00:14:00 | METOP-B | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9320d217-665f-3b26-a17a-039d8e3f5ead | -4.6921 | -46.386002 | 2025-11-08 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79aee306-b8f5-38ce-9131-4007e2b6c520 | -9.1299 | -51.289398 | 2025-11-08 00:14:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 376abc64-6e39-3f5d-823e-18faa70d5391 | -17.877199 | -52.383999 | 2025-11-08 00:14:00 | METOP-B | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fcf8b011-0427-326e-9aba-9549283f368c | -2.427 | -48.038898 | 2025-11-08 00:14:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5486ec-9595-32ac-99b3-4cb0fd3a79b0 | -7.5667 | -45.851398 | 2025-11-08 00:14:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c3da7c8-c460-393a-a34a-dc5e083c0092 | -7.0375 | -46.981098 | 2025-11-08 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9bbc7df6-6119-3364-a54a-2a785b9ea2b0 | -14.4894 | -52.129398 | 2025-11-08 00:14:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
