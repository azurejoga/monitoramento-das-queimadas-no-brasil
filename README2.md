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
| d183394a-3c21-3150-a816-2ab2150ac71d | -7.8118 | -46.5602 | 2025-06-18 00:17:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7183ca5-2ba7-3ddf-ad9e-1e047c80e3b7 | -20.984699 | -47.393101 | 2025-06-18 00:17:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 69c58ef5-3bfd-3ec5-afb9-74d5303529a6 | -9.4222 | -48.424999 | 2025-06-18 00:17:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db292ae7-69a3-3e1b-9855-6fef2e19e960 | -8.7321 | -49.019402 | 2025-06-18 00:17:00 | METOP-C | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb7f0d83-49ef-3720-b258-589fe782881c | -14.1941 | -45.5149 | 2025-06-18 00:17:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef5fd12-af96-3dc9-a20e-13f68e64797b | -8.7267 | -47.988899 | 2025-06-18 00:17:00 | METOP-C | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6314ee0-d12b-3c95-8a8b-f53c0f0bd8b4 | -14.1922 | -45.5056 | 2025-06-18 00:17:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 65a32f30-1f50-3eaa-bf3c-3aeea3cf57f8 | -11.1429 | -53.901402 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffd7b419-77df-32a1-ba8e-ec981784b5bf | -6.1297 | -42.5238 | 2025-06-18 00:17:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffbd42cb-753f-37fb-99d0-3ff8b82a9ae5 | -7.8137 | -46.569 | 2025-06-18 00:17:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| da21b1ad-305d-3e66-9323-9da3e75fc303 | -8.5968 | -48.050701 | 2025-06-18 00:17:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9984546c-f37c-3fbc-83c0-a4a792d8499f | -12.3397 | -49.302898 | 2025-06-18 00:17:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 993d02c1-78f3-3207-9c92-70ea504baf8c | -6.3708 | -43.755901 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae0f5f7b-8faf-39e3-8cef-cfe83c04834e | -14.4352 | -48.883598 | 2025-06-18 00:17:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f5cafeb2-f481-3238-ac71-dd4b0aab58b0 | -10.6548 | -49.3536 | 2025-06-18 00:17:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c4ca8748-6d03-358a-9fb8-a5bd403d4949 | -6.6745 | -43.1898 | 2025-06-18 00:17:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 0f1ff544-8f4e-3ba1-9b53-c5871d32d32b | -11.1179 | -53.875 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e68ef118-a883-3e5b-997a-fcc352dbdbcb | -7.5501 | -45.655399 | 2025-06-18 00:17:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89048c7f-bb07-3198-9b23-bbbd41188225 | -6.0454 | -44.0462 | 2025-06-18 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6a4037a-0db1-3e4a-8486-67c39ea77c8c | -9.8573 | -47.876499 | 2025-06-18 00:17:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 102ba6bb-7650-3a32-978a-db3a8107b81f | -12.3367 | -49.287701 | 2025-06-18 00:17:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1122055c-ecc6-3bc7-b680-a1ddff3f940a | -5.0579 | -43.244301 | 2025-06-18 00:17:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| acd8eb19-5cab-3fc9-bf32-2d38fd24a917 | -10.6646 | -49.351601 | 2025-06-18 00:17:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dae512b2-dce1-3e13-ac19-e81c45017b52 | -6.3791 | -43.746799 | 2025-06-18 00:17:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed4cf047-b9d3-3d02-8cc3-11a9ef275854 | -10.6578 | -49.368 | 2025-06-18 00:17:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e669f68-03f8-3559-9c16-f5722dede132 | -7.5403 | -45.6576 | 2025-06-18 00:17:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 339710dc-11a0-3fb5-a9a2-f95ce0a6410c | -10.9823 | -45.1045 | 2025-06-18 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3788611e-d600-358b-b8cd-661bd50fbd53 | -14.2019 | -45.503502 | 2025-06-18 00:17:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 62e571ae-bacf-3e64-91f0-ce13567c97d6 | -10.9886 | -45.086201 | 2025-06-18 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f1753e9a-ad8d-3ce8-aa92-722b4dc0cd48 | -4.8366 | -43.178799 | 2025-06-18 00:17:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4133a5eb-5a22-33ef-8716-c65cdf084c91 | -11.1275 | -53.8731 | 2025-06-18 00:17:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf3fb20-70a1-37e4-9700-3a6ed39013b1 | -7.804 | -46.571098 | 2025-06-18 00:17:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1445348f-73f9-3b57-840f-03532c289c59 | -9.4125 | -48.427101 | 2025-06-18 00:17:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 213ba2b4-250d-3be0-a8fb-01660d273bdc | -20.997299 | -47.4067 | 2025-06-18 00:17:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dd73b042-a607-3da0-a899-8bb347c9eb54 | -5.9172 | -43.439499 | 2025-06-18 00:17:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3105e418-1e98-3de6-ac37-713ec9a862eb | -14.4284 | -48.900799 | 2025-06-18 00:17:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 33328b20-3fd5-3880-aa61-bd1ad80a71c8 | -6.1383 | -42.9646 | 2025-06-18 00:17:00 | METOP-C | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6258ceb2-0795-3dc8-97c6-84151764bef3 | -10.9921 | -45.102402 | 2025-06-18 00:17:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b14ea66b-fb6e-3d92-982c-19db085b1a0f | -7.2782 | -49.994202 | 2025-06-18 00:17:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ada9275f-62a0-3efc-b271-3fb6c5513b96 | -6.0438 | -44.039299 | 2025-06-18 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 08ad5914-d0f9-3ce1-bb7b-8f722e12dbeb | -5.6145 | -45.966099 | 2025-06-18 00:17:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 589df6f6-bd65-35a2-b93e-3a36346fd967 | -6.2392 | -43.359901 | 2025-06-18 00:17:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 28837771-28a9-3d3c-841f-89686536de87 | -9.1476 | -48.959099 | 2025-06-18 00:17:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76ec7fd7-5cae-3938-ab6b-55ed0fb16035 | -6.1123 | -45.938202 | 2025-06-18 00:17:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ada6346d-6edb-3bf2-916b-9bdf9a381fcb | -14.4411 | -48.9142 | 2025-06-18 00:17:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5a8d806-b198-35f1-ad82-4bcb74a7c6c7 | -12.233 | -44.201199 | 2025-06-18 00:17:00 | METOP-C | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 96389b48-f0da-321c-b5e4-59ec1808f290 | -6.034 | -44.0415 | 2025-06-18 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dfabfc15-6334-3713-b9c1-90656a0eac9f | -6.0356 | -44.048401 | 2025-06-18 00:17:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d705743e-b624-3cc7-8853-da06138377d7 | -7.5449 | -45.631901 | 2025-06-18 00:17:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bd4ff4da-fa23-3b49-8db8-1e157a98ff4e | -9.4099 | -48.415199 | 2025-06-18 00:17:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d9103afa-3f34-3f09-9140-9ec26c744508 | -6.1313 | -42.5308 | 2025-06-18 00:17:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4c5a8925-9d59-3413-9c74-00c3145f107d | -11.5813 | -44.838299 | 2025-06-18 00:17:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3fbe658e-ed31-3614-97d6-0522015adf2f | -6.1329 | -42.537701 | 2025-06-18 00:17:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b10b6519-ba35-3e6d-89be-278141f1706b | -5.909 | -43.448502 | 2025-06-18 00:17:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a994f9b6-31e6-38fe-bb06-0584d92dd9ba | -6.1231 | -42.539902 | 2025-06-18 00:17:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 69226793-5aaf-3c66-b6ba-af3034789479 | -11.9709 | -58.7362 | 2025-06-18 00:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 50.9 |
| bed1b5f6-0374-3f2e-89f6-cd434f41766d | -10.6501 | -49.3617 | 2025-06-18 00:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 0604d8de-fc58-3697-85b4-1ca1c0e2a0f5 | -6.118 | -42.5323 | 2025-06-18 00:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 2ee4c428-7e05-3258-b4c5-bbb6e26f168e | -14.4467 | -48.9063 | 2025-06-18 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 86416d63-704c-383c-bfc0-cb9bad897b5a | -11.1382 | -53.9223 | 2025-06-18 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 310.2 |
| 18c31ffd-c6ea-3481-904c-fde6ee67954a | -14.4273 | -48.9093 | 2025-06-18 00:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 156f81dc-b3a9-3858-bb32-197cb0e18421 | -11.1568 | -53.9411 | 2025-06-18 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 5a9da0ee-f1a9-30b1-89e5-e7248cd58581 | -8.7317 | -49.0151 | 2025-06-18 00:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0cd29dcf-982b-3f43-b167-779937df752f | -8.7129 | -49.0168 | 2025-06-18 00:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 864c8496-fc7f-3301-93ff-2ca41d508188 | -11.1571 | -53.9206 | 2025-06-18 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 937c0892-e225-36ec-83cf-6ae5f202fc20 | -20.9845 | -47.3955 | 2025-06-18 00:20:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 88.2 |
| d384fe4c-3190-3f72-9b62-4c82bb91af2e | -21.0051 | -47.3904 | 2025-06-18 00:20:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 83.7 |
| b2b9b87c-d677-3a89-baff-b672408108dc | -14.2052 | -45.507 | 2025-06-18 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 6659fac7-328e-3b6b-9821-cdac9944b1ed | -22.7866 | -49.3172 | 2025-06-18 00:20:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 9e2ebb2a-b3d5-3f6f-b40e-96f18622e07f | -11.1379 | -53.9429 | 2025-06-18 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 371.8 |
| 29f1f075-8253-3d4e-a0bd-7ab7ee7b62f2 | -11.119 | -53.9446 | 2025-06-18 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 2c125d94-9df3-3091-9258-f15589aae288 | -11.1193 | -53.9241 | 2025-06-18 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 07250fdc-c68f-358b-88c0-9e6b823a15dd | -22.7866 | -49.3172 | 2025-06-18 00:30:00 | GOES-19 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 47.3 |
| aaedce5f-4ea3-3d75-a830-c28ddc33e390 | -11.952 | -58.7376 | 2025-06-18 00:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 06fc9842-9630-32ec-bd8c-e428dfe7ebb0 | -21.0051 | -47.3904 | 2025-06-18 00:30:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 68be31a0-055e-32df-b0ee-533f5bd5c004 | -14.4273 | -48.9093 | 2025-06-18 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 6600be4a-871f-34bc-9a3a-02030a4a06e2 | -10.9167 | -56.8336 | 2025-06-18 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 92dce7ff-d79d-3738-8a99-03614d27941e | -5.9028 | -43.4418 | 2025-06-18 00:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 21910e9d-37fc-3e25-80df-2b719b38abb8 | -6.118 | -42.5323 | 2025-06-18 00:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| d7f8dbbf-4ea0-3b39-aefa-af6d083ff6e4 | -10.9164 | -56.8536 | 2025-06-18 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c6d00e02-efef-3416-8b84-1105ec55e83b | -20.9852 | -47.3718 | 2025-06-18 00:30:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 41.3 |
| cf7a05ef-a42d-38d7-afae-e114153b49cc | -9.4994 | -56.0788 | 2025-06-18 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b7e3a93c-b363-33f9-be30-26a1439af15f | -8.7317 | -49.0151 | 2025-06-18 00:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 2ab314e7-d1aa-3ebe-9247-d225933d184f | -20.9845 | -47.3955 | 2025-06-18 00:30:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0840ce47-a903-3cdb-89e5-3527dcc5ddbb | -8.7314 | -49.0367 | 2025-06-18 00:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d2f4004e-1c56-34c8-85c3-d8980b661251 | -14.4467 | -48.9063 | 2025-06-18 00:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| b33a490b-008d-3ade-8a1f-15af605e5d30 | -9.4993 | -56.0988 | 2025-06-18 00:30:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 4c3b54a3-ffad-317e-81ea-2e52dcb99579 | -8.7129 | -49.0168 | 2025-06-18 00:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 01f2ddb0-1c7c-3d31-95ae-a431b06e5207 | -9.4807 | -56.0801 | 2025-06-18 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 1ecc6852-34c3-3325-8c8b-9354e2511e29 | -8.7129 | -49.0168 | 2025-06-18 00:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| bfd7ef07-eb76-3cc6-81d7-2044826912ba | -5.9028 | -43.4418 | 2025-06-18 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| d217875a-102f-3cc6-b499-3cdc7f4e0dce | -9.4806 | -56.1001 | 2025-06-18 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 9bda519d-ae72-3d8b-9a09-c20c35eee3bb | -9.4993 | -56.0988 | 2025-06-18 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| de783d03-f532-394f-899c-1d5661875dac | -11.952 | -58.7376 | 2025-06-18 00:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 72d74464-c5ba-395a-9381-554857dcf0a4 | -10.9164 | -56.8536 | 2025-06-18 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| ea1a8f78-6a03-3458-96c4-ba9244dd2063 | -6.118 | -42.5323 | 2025-06-18 00:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| f6dae2d7-4915-3b56-afca-de02da7206d0 | -10.669 | -49.3597 | 2025-06-18 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| d0b8e243-859d-3b81-91f8-e00a75e1cc22 | -10.9167 | -56.8336 | 2025-06-18 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d2ff36ea-1108-39b1-95f6-eb78cd59d368 | -14.4467 | -48.9063 | 2025-06-18 00:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 1eee9e70-27b2-3820-a769-097218c5f9b5 | -9.4994 | -56.0788 | 2025-06-18 00:40:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |


[Clique aqui para ver as próximas entradas](README3.md)
