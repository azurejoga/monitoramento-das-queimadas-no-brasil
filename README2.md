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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eba2b0b9-81a5-3fab-8a57-c07e69e05d71 | -8.7211 | -48.3222 | 2026-05-19 01:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 609d2af7-9875-320c-a518-e5b9fa84329c | -14.1638 | -52.8691 | 2026-05-19 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3239b33a-21b1-3022-b36a-5cc871b61f72 | -14.1635 | -52.8902 | 2026-05-19 01:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| ba2b791d-ad80-32d3-b311-cba43c1e9a0a | -8.7211 | -48.3222 | 2026-05-19 01:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| d44fdb6b-5ed7-3a39-8aa1-862e23eb1381 | -6.4021 | -44.1658 | 2026-05-19 01:40:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| fe20e177-b337-3ddb-9c2c-9cef7dab6b60 | -14.1635 | -52.8902 | 2026-05-19 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 08cfec6e-1a54-327e-a39a-40a050eb88e1 | -14.1638 | -52.8691 | 2026-05-19 01:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 06eac0c6-0a32-344b-9ed9-16e76d110437 | -14.1638 | -52.8691 | 2026-05-19 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 77.2 |
| fd24fabd-18fe-339b-96a2-4b44758cccdb | -14.1635 | -52.8902 | 2026-05-19 02:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 98aaab0f-6b49-3114-b836-6e9bed0db7be | -14.1635 | -52.8902 | 2026-05-19 02:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 02383432-d5bd-33b9-b2f5-46ff46986a6c | -14.1638 | -52.8691 | 2026-05-19 02:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a6a2d5bc-7193-3fbb-980f-d565f65c4927 | -14.1635 | -52.8902 | 2026-05-19 02:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 57b1c0be-3329-3fa9-b2ae-7548caae0e89 | -14.1635 | -52.8902 | 2026-05-19 02:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d174d470-9f88-3915-bb92-6c1e3c46661d | -14.1635 | -52.8902 | 2026-05-19 02:40:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 48da8d84-8d82-3873-b3ac-16b0e7fb332c | -14.1635 | -52.8902 | 2026-05-19 02:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 037f0704-0f52-3c08-ad95-66423b012b57 | -14.1638 | -52.8691 | 2026-05-19 02:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 9239e56b-605f-34ac-af72-982814c90770 | -14.1635 | -52.8902 | 2026-05-19 03:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 61.1 |
| a48e94ce-4f36-3feb-826d-455f6439c59d | -9.39569 | -37.17231 | 2026-05-19 03:02:00 | NPP-375D | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c525a270-bef4-3f73-842e-1e41a8c81cd2 | -14.1635 | -52.8902 | 2026-05-19 03:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 2cdbe086-52ed-35aa-af18-2ea56cb45807 | -9.73827 | -37.25829 | 2026-05-19 03:19:00 | NOAA-20 | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9260247c-c673-389f-b82f-415185b23f26 | -9.39557 | -37.16896 | 2026-05-19 03:19:00 | NOAA-20 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5d78ee35-69c2-3818-9a85-cc561014fdf1 | -10.65035 | -42.31672 | 2026-05-19 03:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e9ee7e03-9ab3-36a9-9156-77dbd0e011d1 | -9.3232 | -40.21152 | 2026-05-19 03:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2dc8f307-5ebf-3218-993a-ff1cc976de10 | -10.65149 | -42.31106 | 2026-05-19 03:19:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e4555e15-1d4d-3dc1-80ca-82aba3ad33ba | -9.39461 | -37.17435 | 2026-05-19 03:19:00 | NOAA-20 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0e83ae5-7861-3082-9989-a0aad9402446 | -14.1635 | -52.8902 | 2026-05-19 03:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 2d5dfa00-cdd2-386e-9ddf-a3e5efbf6179 | -13.36511 | -39.90962 | 2026-05-19 03:21:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7aedb5b8-c19b-3c0d-b958-fba1fb9ad5b5 | -12.21333 | -38.98083 | 2026-05-19 03:21:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41288a6c-7715-315e-871e-5a6322f9db6f | -12.46657 | -38.35132 | 2026-05-19 03:21:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 8dfe2c80-e13a-38a6-8af9-d41ebdb5f744 | -12.46566 | -38.35003 | 2026-05-19 03:21:00 | NOAA-20 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a9d787ee-6796-3a19-94b2-b526796f142d | -12.13222 | -39.40891 | 2026-05-19 03:21:00 | NOAA-20 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d5854bb0-a531-31ba-a7c3-82ce11cc27e6 | -12.21274 | -38.98397 | 2026-05-19 03:21:00 | NOAA-20 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2af5422d-f229-3284-a826-407872677fcf | -14.1635 | -52.8902 | 2026-05-19 03:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| d86f0a18-307f-33ea-a06c-1a0033cbab86 | -14.1635 | -52.8902 | 2026-05-19 04:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 08789c76-813e-3080-b1d8-0b3673fb3549 | -9.47606 | -46.07565 | 2026-05-19 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 733080a9-6516-32f2-84e4-379b8e97ef64 | -8.71895 | -48.32753 | 2026-05-19 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8e24e2ca-79b3-37bf-b81f-16dd516244c0 | -8.73335 | -47.97697 | 2026-05-19 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e618378e-f68a-3052-84ef-025dc8c8cf43 | -8.33273 | -45.3609 | 2026-05-19 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3b82f64-8f95-3471-8670-4494f282f131 | -8.70318 | -47.92183 | 2026-05-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db1fde34-f144-3d87-bd5f-f4865cf417a3 | -8.72334 | -48.32824 | 2026-05-19 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b1e3ff86-3e2c-3806-8db8-36a774476df1 | -6.39106 | -44.17078 | 2026-05-19 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 2f9ce8c6-dfb2-36fe-b90d-39bcdc2b1c55 | -9.61759 | -40.34338 | 2026-05-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 15613e97-8bd1-3029-8d31-3792ec56c59f | -8.7182 | -48.3318 | 2026-05-19 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7a57a995-f497-3460-b81d-e3d5482e0e02 | -6.39524 | -44.16737 | 2026-05-19 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 0f61a64d-b0b9-38b9-9d5a-5c47ae157657 | -8.72836 | -47.98037 | 2026-05-19 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42a40457-168b-3b0e-aafb-ef753b023114 | -8.08066 | -44.10963 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5e994c13-e53f-39e6-a2be-245dd1d1d87a | -7.96703 | -45.27989 | 2026-05-19 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd86c2b9-77fd-3bbe-8bc3-4857f023334b | -8.07535 | -44.12057 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fd077ee-a8ae-3ebc-bcc9-17a8aa7f26a3 | -9.30048 | -45.4823 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44f42d5b-7644-34ed-aa8b-16043a1c5aba | -9.29684 | -45.48167 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6873a8a7-1974-32f7-9e3a-63ca89ecd55f | -9.31068 | -45.48845 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b79089d-b1db-3dbf-ae0e-bebb7a615767 | -9.3136 | -45.49335 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecf35b80-8e9a-3014-8675-7611883c9865 | -8.70745 | -47.92255 | 2026-05-19 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37d98c63-c1ab-3aa7-bc37-6db2fc7bc72a | -6.38753 | -44.17023 | 2026-05-19 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c2f6083a-3e5d-34d5-98ce-745e540a2b75 | -7.96845 | -45.27124 | 2026-05-19 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 38c00e56-0d74-332a-a89d-ad84dcdb8602 | -6.39042 | -44.17477 | 2026-05-19 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38764953-7c9c-3252-8036-640ad2cec84b | -8.07882 | -44.12112 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9f96538-7224-3651-b981-d5fdc0aacc47 | -9.61703 | -40.34708 | 2026-05-19 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 36d6f14f-2170-3db0-bde1-ad4903878d28 | -8.07473 | -44.1244 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d1a8eb8-bd00-3db1-ab41-d860e9d2251c | -8.73264 | -47.98111 | 2026-05-19 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe2b514f-718f-39ea-b969-1592e2195baa | -9.29756 | -45.4774 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36c8a832-fdec-323f-b58b-36c986af3b3c | -8.72906 | -47.97625 | 2026-05-19 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2cbe72d3-4018-3685-a90f-b3d75f1f2c8f | -7.96774 | -45.27556 | 2026-05-19 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 50bc0af5-8479-3e58-a0e1-abadab158a6d | -9.29392 | -45.47677 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e6cf7ca-aad5-3a93-a7ce-0df9515eef61 | -8.08412 | -44.11018 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8207c19-8a31-3b9b-a5bd-ab11fad2e81f | -9.39846 | -37.17392 | 2026-05-19 04:08:00 | NOAA-21 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2dbbe107-0823-3f08-a7a5-05321633f57a | -8.07373 | -44.10851 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21bc4acc-4f8d-3072-97c8-53a4f4ccb186 | -9.34579 | -40.67957 | 2026-05-19 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.3 |
| cd550b2c-0bc9-383f-90dc-2aa09867cd17 | -9.30704 | -45.48782 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 247160ec-cf81-365f-b7cd-280885811311 | -8.72259 | -48.33253 | 2026-05-19 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af3fc776-d1b4-367a-b331-b1d9aa9f1527 | -8.73193 | -47.98528 | 2026-05-19 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ce9526a-ae35-3213-b737-fbeb096cc93d | -8.08473 | -44.10635 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cba28c94-6e3b-3c2c-937a-32c8c70c14fe | -6.39171 | -44.16681 | 2026-05-19 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9f242633-d635-3abe-acde-5651bc76faef | -8.55385 | -45.98745 | 2026-05-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e5424aaf-e724-34b6-a7a3-703b14ff8a17 | -8.71455 | -48.32681 | 2026-05-19 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4dbe1e9e-6222-3c34-9172-45fcaeaae401 | -8.07719 | -44.10907 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2ffc040b-dbd2-34fe-acd3-9973584a9ed5 | -9.30996 | -45.49273 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcb8c708-1192-3e26-9c04-756177c37082 | -8.72183 | -48.33685 | 2026-05-19 04:08:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac3cc9ce-dd37-34d5-9c75-efc3d519c7bf | -9.3034 | -45.4872 | 2026-05-19 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1bc9b846-470f-3758-a423-6d6ac786ac11 | -3.35539 | -43.1698 | 2026-05-19 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b4cbd46-5818-33a7-b708-c17cfc6a359b | -8.55344 | -45.9898 | 2026-05-19 04:08:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c6531170-5f59-3245-a40c-98405e9fc705 | -8.0782 | -44.12496 | 2026-05-19 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 962b3c0f-d6a9-30bc-ac98-5a8c29a736ca | -9.39894 | -37.17047 | 2026-05-19 04:08:00 | NOAA-21 | SANTANA DO IPANEMA | ALAGOAS | Brasil | 2708006 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| abec4ffc-5307-3f6b-bf2f-5b13dc7df73b | -10.67053 | -49.70457 | 2026-05-19 04:10:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27a54a87-609d-3e9d-aec7-d82f4e61607e | -14.28512 | -39.84679 | 2026-05-19 04:10:00 | NOAA-21 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 32e559a3-66fc-3808-8adf-94c9ae800405 | -10.99304 | -43.7226 | 2026-05-19 04:10:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4208a3ae-87ee-3657-9f79-a540e946a4b2 | -11.27747 | -44.6499 | 2026-05-19 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17fcaa29-1cc8-3095-a73d-d127deb75c46 | -13.53022 | -46.71459 | 2026-05-19 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f39c42e-b56a-33c8-a396-6aa5c5f01b8f | -11.27328 | -49.48074 | 2026-05-19 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a03c79-3c34-38c6-96ad-4afa2d0fd270 | -12.00546 | -43.84429 | 2026-05-19 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5b449f5-c52b-3e6c-a482-524626084967 | -14.15644 | -52.88118 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97e8ef67-93b4-3798-b941-d00f75533dc5 | -11.31344 | -47.41818 | 2026-05-19 04:10:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c06776d4-768a-3dad-b97c-0115a9dffb58 | -10.45404 | -47.93461 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bf74a552-f36e-310c-8c2c-1f0f4ff3bacc | -14.16251 | -52.87886 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 76d1e522-5f68-3e5a-94ab-d65f506c626e | -15.32914 | -47.84155 | 2026-05-19 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20959945-9847-3653-ae40-0ab5b22f7c14 | -10.45755 | -47.93903 | 2026-05-19 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0301ea39-61e2-34d9-845f-a307ee34531e | -14.70531 | -48.32361 | 2026-05-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe2fa18-184b-3261-8aba-fdae72d6e1f3 | -10.57402 | -46.66891 | 2026-05-19 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 83ff102c-ecfd-3d3f-9dfd-9c02febc1ab8 | -11.84645 | -43.96296 | 2026-05-19 04:10:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74323933-c109-3e6f-a753-30353b934d60 | -14.15856 | -52.88827 | 2026-05-19 04:10:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README3.md)
