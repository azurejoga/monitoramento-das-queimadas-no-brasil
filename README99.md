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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7db130-2971-3d71-a662-541eaf934acc | -10.00756 | -39.16573 | 2026-08-28 16:07:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 59451a4d-2bf7-33b2-800d-511130d7ff0f | -11.2254 | -45.39847 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b62956d2-a1d4-35a0-a049-6ee36eade629 | -9.66208 | -45.71841 | 2026-08-28 16:07:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6fcba26-b58d-31c0-ab61-10402a08b3bb | -2.99455 | -48.94948 | 2026-08-28 16:07:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e10a15be-1c74-38db-8d25-3460ae7e01d6 | -10.92276 | -46.62885 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 171c8d10-dd97-3686-89f0-fc7a62be6bbf | -2.72878 | -47.04441 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 163fc998-2328-3204-b342-e1a410227e58 | -3.93681 | -44.90679 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 452b0596-4d04-357a-baad-1e76a3f42b98 | -10.33701 | -49.98892 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| f921317f-f735-3748-9dfb-f95c4b07cea2 | -10.24602 | -47.99488 | 2026-08-28 16:07:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 33.2 |
| dc1d1351-81ba-353b-b5d9-542cd660bbfc | -9.86968 | -46.33348 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a0fb2330-7505-329d-9801-88349293dd6b | -11.83834 | -47.22184 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| b94934d3-924c-3854-83cd-4b69477de048 | -10.54233 | -46.24622 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5579de8c-30a1-3b09-9cab-5e269f0684cd | -10.24656 | -47.99908 | 2026-08-28 16:07:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 4b80ebce-9348-376f-bf6d-8203af01569a | -12.30546 | -50.57344 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 3f63f32d-16e0-3f66-b8df-0ea486974846 | -11.34915 | -48.39016 | 2026-08-28 16:07:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 53cfc982-0900-3fba-ae20-c4403ba8f590 | -11.07987 | -47.11473 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 645d6f0f-7be7-3fdd-9eaf-b889e5103a7d | -3.00777 | -43.17572 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1a40512e-5fe5-3f42-8333-fc2347b55148 | -1.58229 | -48.40467 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2eaaf809-e30a-362c-8f86-53da190c7618 | -12.20288 | -50.55622 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fc4ed2c1-bff1-3888-8c2a-f782dad9f15a | -9.88155 | -46.34186 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f232b9c-aba4-3f01-8f6b-f37f70bb9e72 | -10.54333 | -46.25389 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7e9c9e5f-bb16-3693-b004-e964395b87ce | -5.34382 | -45.15574 | 2026-08-28 16:07:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| c6611926-f53b-35ab-97bf-b11db5d52c8e | -10.08249 | -46.94516 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bde2ad64-90a6-39d8-b339-bdb716987b2a | -10.00779 | -39.16576 | 2026-08-28 16:07:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 12ab7823-9769-3b1d-9d96-41f3da8b881a | -11.07189 | -47.12449 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2e054cbf-a7a3-3c39-9b77-66e5e91fddbd | -11.24952 | -45.06262 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 97e2a3c5-05c7-3f4c-af1b-aa1ae4a872c7 | -9.04904 | -37.28392 | 2026-08-28 16:07:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 20312970-698c-3499-bd31-b55a7609e7a8 | -10.90335 | -46.64664 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 09efc1d5-d3cf-32d4-8d31-f526155072fb | -3.02278 | -43.62148 | 2026-08-28 16:07:00 | NOAA-20 | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8bc96bd9-ba22-3d78-92f0-9b862aa85fe2 | -10.90858 | -46.64893 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| ff9e427a-8291-30e3-9ce3-2aa43c8d0d1b | -9.87433 | -45.86803 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e4ec642e-ad57-3c3d-a026-3a54b8cd611b | -10.92357 | -46.62932 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2cb4c21f-f1d7-3181-a5ad-f852b9824a76 | -10.5609 | -50.4254 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0dc54fda-7d5b-3561-aea2-fd2f12a0ba71 | -12.32432 | -50.58167 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cbbd7497-c4c9-3900-b492-f22ef70a372d | -2.72958 | -47.04894 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| cc1e4d76-9cb4-30eb-9e23-25310089c518 | -11.41418 | -42.30619 | 2026-08-28 16:07:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 209ee702-79fe-3e65-9247-390d2ba4f39a | -9.43443 | -37.83275 | 2026-08-28 16:07:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 8c118b1d-743a-38b0-a6b5-5e75d2ee4f58 | -1.78558 | -45.77199 | 2026-08-28 16:07:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| ceca178b-27c3-3fd1-909f-9e28e1ec4006 | -10.17783 | -46.85624 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28d9bb5e-f340-3218-aee3-53747a7a92e2 | -10.88462 | -50.50406 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7388e063-14d8-31f4-ba4d-208db63684d0 | -12.32998 | -50.56679 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 044d1ba3-b1f0-34e6-afb4-bc07ced1c960 | -3.70619 | -45.26299 | 2026-08-28 16:07:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 24ff8c59-2e72-3357-a05a-239f179e38d9 | -12.14569 | -50.63222 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 28ee85f6-4578-3d69-9c03-44d6758fed1f | -2.7246 | -47.05093 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 1cc92747-e0c7-3ef5-9b6a-d893e7968f9e | -9.88726 | -46.34428 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 84ea7691-f7d0-363a-843c-deaf379fa69c | -10.02728 | -45.81869 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ddc8819f-5c1e-3d1f-925a-0e66a4b84821 | -11.79439 | -47.65898 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 136b02f7-ef4e-348a-a17f-87cf14a4ea3a | -10.09147 | -46.97528 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e2c008d6-906f-3002-a45c-fe034bc68874 | -2.72545 | -47.05542 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 3abc60be-f8d3-36ec-b44f-d39325853f22 | -10.08535 | -46.96738 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f12f3a3e-6ceb-3c6d-89e0-27b0fd2566c0 | -11.82675 | -47.22992 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d5756cac-4934-30d7-8db0-f960dc1f2878 | -11.2432 | -45.05224 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0a4bbd49-0a5a-316b-ae52-a1fafaff1d20 | -4.66547 | -43.22142 | 2026-08-28 16:07:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 387b6dfd-7261-3115-8731-af5706d3db4e | -11.25303 | -45.05827 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 24c8d885-e145-3984-b768-31862553a532 | -12.05833 | -47.18752 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f7d7f99d-87d1-3abf-8284-a5017d5db20d | -3.92802 | -44.90808 | 2026-08-28 16:07:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a1ea9204-412e-3386-b96a-4d0f7186af5b | -4.37745 | -43.3873 | 2026-08-28 16:07:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fb927572-bd3b-3f8e-a91b-13b4c0c4766c | -11.24735 | -45.05341 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 33720845-0061-3867-ad86-e58d8debfd7b | -11.77519 | -47.62872 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9ec524ed-dcc5-3fb1-a0dc-c56156a99d8d | -10.90624 | -46.62426 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 86157534-43f7-3014-a847-b7be56f79d6a | -11.06953 | -47.12426 | 2026-08-28 16:07:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1a0a00b-2f62-3a62-b53c-ad37f4d28f21 | -2.72413 | -47.04676 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 5d397f1b-472c-38b3-98ff-c7bdc48d4559 | -5.58019 | -47.45436 | 2026-08-28 16:07:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 70cd72ec-5c79-3ba3-a9d6-c255b56be751 | -10.07841 | -46.95724 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a6bbc15a-90b3-3885-b010-c1119d6d51a8 | -11.54774 | -45.49742 | 2026-08-28 16:07:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00b70be7-17f7-3d47-9f99-56799dc1b060 | -10.9172 | -46.62267 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 5e07d639-d502-31b0-96a9-ca0426854a20 | -12.03005 | -47.14514 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 887b97ec-282f-3d04-9da3-b21b133e25ad | -10.54814 | -46.24926 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c0402978-7f3e-3253-b25b-4fc6bd337a2e | -11.7612 | -47.63168 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| f3f92be8-742f-3508-958c-a8fb70255a01 | -1.52071 | -48.32357 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 455bb18b-306c-3c5b-872a-e259d4cccb15 | -4.84965 | -45.39334 | 2026-08-28 16:07:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 43e1ea72-0085-392b-904f-b9b2a0b2fed9 | -12.03372 | -47.18457 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d2fe36a0-79c4-3985-8a49-e26d6d9edd6d | -3.26407 | -42.98339 | 2026-08-28 16:07:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aa2cac05-d629-342c-83a2-cadadbc0f20c | -12.1491 | -50.63156 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 08a5ecad-0e2b-3318-90f0-0f8d788ee02c | -11.83257 | -47.22263 | 2026-08-28 16:07:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 42b9b6c1-aa8a-3799-8c28-8c6762469f25 | -9.88113 | -46.33863 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 47382edb-e407-3e00-80e8-822617889ad2 | -12.25974 | -50.54995 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fc6ee058-6da6-3bd4-bb96-f3ed59808a54 | -10.06734 | -46.95884 | 2026-08-28 16:07:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a36c9e2e-a4b0-3e6e-843a-5cb5d4932862 | -10.55821 | -39.24622 | 2026-08-28 16:07:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 94bdcdf9-947e-359f-960a-58a839f9c1fa | -1.96274 | -48.3776 | 2026-08-28 16:07:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f201d40d-faf5-3260-9390-06d53bb5ea12 | -12.039 | -47.17981 | 2026-08-28 16:07:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 918df890-a44d-3bda-8cb8-21dd75ee910f | -12.20926 | -50.54843 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| abb366e1-3b6a-3a85-9fb6-8c0fbff37f01 | -2.73003 | -47.05308 | 2026-08-28 16:07:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e6358547-886c-3819-8579-42811e171828 | -10.55324 | -50.41972 | 2026-08-28 16:07:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 618c221a-1e84-35e7-b272-0203c5a923d0 | -2.58551 | -48.16566 | 2026-08-28 16:07:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60e59583-981c-3e77-b474-87bdd9f52f4e | -10.00702 | -39.16196 | 2026-08-28 16:07:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 1956ebc5-c5d5-34e6-b592-225ca2581839 | -11.84304 | -47.66282 | 2026-08-28 16:07:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6eb7403f-4a15-3e92-be5c-20705fccc40a | -11.24815 | -45.05156 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5448b6a6-3d29-38a3-a2f5-1764a927704c | -9.79978 | -46.32848 | 2026-08-28 16:07:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a717388e-8af5-3a6e-9162-ecdbbb48e0ec | -11.61938 | -46.7299 | 2026-08-28 16:07:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d332cf9-3004-31f8-a90f-fcb4c1d427fa | -11.24808 | -45.05892 | 2026-08-28 16:07:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.5 |
| f713cb58-f5ec-3afc-b3ba-536941194f96 | -10.54644 | -46.24884 | 2026-08-28 16:07:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9a700d94-23b2-30a8-97db-0730f09f208a | -10.02379 | -45.63419 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2837d9a1-ad91-3979-bfcc-65a8dbe0e935 | -11.0268 | -49.66616 | 2026-08-28 16:07:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e11dfa5d-6454-3a80-a7c7-fd8419f82009 | -0.8854 | -48.19675 | 2026-08-28 16:07:00 | NOAA-20 | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cf16c547-47cc-330c-94fb-e04718a2cfb4 | -3.70104 | -45.25914 | 2026-08-28 16:07:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ff9a3d6a-ec48-3a1a-9c16-84d5eb0340cb | -8.84782 | -37.2776 | 2026-08-28 16:07:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d92b93ca-f482-3077-9f68-0bee7fd8c4c3 | -9.86052 | -45.84141 | 2026-08-28 16:07:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2265167d-862a-3240-a0c3-d2aa9b8bbab4 | -3.4209 | -39.27573 | 2026-08-28 16:07:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 58bb1276-9459-3c3b-adff-dfe05697be8f | -9.62813 | -45.73535 | 2026-08-28 16:07:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README100.md)
