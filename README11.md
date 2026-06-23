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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09d3c604-b896-3919-b846-dd6328b40a69 | -6.36365 | -43.59537 | 2026-06-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8504dd47-3641-3435-ac71-a76ef73cfcf7 | -9.36809 | -50.53938 | 2026-06-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0470a481-d87e-3b04-a311-f5c1acbfcbe4 | -8.3603 | -50.50227 | 2026-06-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3c6b4ca-d201-32b5-ba0f-67756bde44eb | -11.57362 | -47.4389 | 2026-06-23 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a4cf6386-42dd-3850-91ae-dbec575029a4 | -10.90638 | -54.13808 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c17949fc-2a23-3cb5-8f1f-d94c0755e834 | -4.35308 | -47.76165 | 2026-06-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4610513-57c7-3127-9b86-85100665c0e7 | -5.79868 | -43.79209 | 2026-06-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73dcb222-b699-3f95-becd-524b783a544d | -11.29495 | -43.33037 | 2026-06-23 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| dc25ed38-23de-3070-90ef-e6bf8a0a918c | -6.1922 | -44.87177 | 2026-06-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60d408d2-a6c1-3887-96be-c4c4bddb7e34 | -5.82192 | -45.06106 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b26af609-24d0-3ad2-95d0-3890a8567649 | -11.05626 | -49.57213 | 2026-06-23 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e0a8c10-1615-3211-9317-b864d6641256 | -10.59786 | -53.46124 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc778ad0-4c16-3520-ae75-71a79628981e | -11.04692 | -52.46786 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b83b82b-d3c0-374a-86ad-91039a0036d5 | -10.40488 | -49.44754 | 2026-06-23 04:51:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efaa33e3-b1a3-3d1e-892a-84426be8727d | -10.97337 | -48.14965 | 2026-06-23 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96227cea-05b6-351f-ba59-f8eb30cdca8c | -11.05025 | -52.46839 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3230104-b964-3a66-9697-14b3efb95bb1 | -9.22318 | -45.33541 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e84c8ccb-a7c7-35b4-aebe-64c437a2b807 | -6.3632 | -43.59857 | 2026-06-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 999e1b30-23c6-3dc7-b759-5fb30b785394 | -6.36892 | -43.59584 | 2026-06-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dcfee450-6766-353e-8ba2-c85912a1095e | -9.74391 | -47.87766 | 2026-06-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 024b4fae-42b3-321c-9065-a65167619538 | -6.93781 | -51.9452 | 2026-06-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35c3c226-d8a0-3bf4-9ce9-a214a55243d8 | -4.45299 | -48.0224 | 2026-06-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5bc725b-4ff6-3a54-9dd8-9061729c1ff9 | -5.3019 | -43.69141 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b16ad515-d269-3ea4-aea2-60ee66cce9c1 | -8.97754 | -47.973 | 2026-06-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a59fdb8-783e-3aa9-b3ca-13b15da8af3f | -11.05691 | -52.46944 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc3ec2a-0987-323b-98b5-081cee943bac | -4.45309 | -48.02427 | 2026-06-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd75b1a4-5891-3d67-8a25-75b1c8ce11dd | -10.90694 | -54.13456 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c75e3f89-83aa-38c4-8b73-d73922dfbc2c | -10.97286 | -48.15334 | 2026-06-23 04:51:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 66b28140-82c9-3463-bc3c-2a2547887838 | -5.30453 | -43.69327 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77561d6a-dd01-3d79-8a41-4eddd34a79ec | -9.21982 | -45.32376 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f07f13b-382b-30f0-8204-305684395a52 | -11.05134 | -52.46125 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af786fb5-5df4-36e8-89af-493b3976ff7a | -11.05746 | -52.46587 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f7ca9aa-79ad-3984-8faa-6893a6a585a2 | -9.78046 | -48.97421 | 2026-06-23 04:51:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18b0285d-ee34-3d33-80d4-2e04c01fca7e | -9.44918 | -50.84159 | 2026-06-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b47b8cf-72f5-3f84-9953-199aec549392 | -6.57868 | -44.56695 | 2026-06-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8258e65-86fc-3a78-aba2-88c19bcd3e87 | -4.45754 | -48.02026 | 2026-06-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad506174-dc25-33d8-8456-19f315370d59 | -11.05559 | -49.57674 | 2026-06-23 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb3258b3-2cf7-33b9-b1f5-d4faee840eeb | -10.56697 | -46.22217 | 2026-06-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e98c33ae-3dda-397b-94c5-c86c402c099f | -5.83133 | -45.06223 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b4143d0-d14e-3900-8fc8-8bbcc23876d9 | -8.08627 | -46.38988 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b8e638d-fcc4-3170-9575-d38605ed72d4 | -9.21109 | -47.91074 | 2026-06-23 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1a5ea7a-58f0-3094-b882-8dfc7d3b1fb3 | -11.98991 | -45.14863 | 2026-06-23 04:51:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 891e694e-bd7f-3492-b859-10e4b1562e25 | -10.39258 | -56.71412 | 2026-06-23 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e24390d-0429-3738-914b-e0ee404a8228 | -5.82265 | -45.05602 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 168b5709-7959-3f85-b060-c7d4a4556aa1 | -11.30018 | -43.33495 | 2026-06-23 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 101f9b25-c175-33f7-b74d-71a4c38cf657 | -7.35859 | -47.01891 | 2026-06-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa0429a-c4c9-3359-8865-18aa026212a7 | -10.56631 | -46.22725 | 2026-06-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 488cff68-8e60-334a-ad8c-5a1e5f6f5922 | -7.36279 | -47.01947 | 2026-06-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7310e65-d56b-3538-a65e-b1dcc8408cc3 | -9.2247 | -45.32414 | 2026-06-23 04:51:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 84edf170-9c48-30d6-b56c-68ac4457e4ea | -6.19207 | -44.87092 | 2026-06-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d9de618-d5cd-3476-bc74-6f7dd7a6f08a | -7.36643 | -47.02396 | 2026-06-23 04:51:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4cc8b8-e91a-3f98-8bb9-bea1c72d6f89 | -7.35439 | -47.01834 | 2026-06-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3b4de85-67fb-3b8b-babd-f74ea262db12 | -6.37419 | -43.59636 | 2026-06-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdf0a336-ee4a-37d5-bdb4-20e9c4ad7f2c | -10.77145 | -54.10915 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fef638ca-4ee6-31c0-bdbb-05894c9de1f6 | -9.36868 | -50.53543 | 2026-06-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ed8e497-3d60-3ba9-bf20-6600e0cdc148 | -11.47542 | -46.67863 | 2026-06-23 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 003499c0-81b4-3aa1-99fe-4a84d6ec0dc4 | -8.87339 | -46.93729 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb0662a2-0452-3910-80ed-0c9bfc847f2f | -5.82736 | -45.05656 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5ba19c77-f6fc-3d6d-9828-1127b3ad7374 | -11.97897 | -47.11735 | 2026-06-23 04:51:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 187ab0fa-a05d-35b7-be7c-0b207afdb9ac | -11.57852 | -47.43519 | 2026-06-23 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f5b2bbf-d106-3d21-9228-5ba3dac2bcc3 | -10.77089 | -54.11267 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28e0825d-3e9d-3750-8a31-128293a7357b | -5.79526 | -43.6309 | 2026-06-23 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00d50e2f-cc8d-3312-84d5-10edf8c4cdde | -11.38577 | -47.81542 | 2026-06-23 04:51:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c272ce66-c1b9-39fe-bfcb-90dbeb57970d | -11.29447 | -43.33427 | 2026-06-23 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 048d9dec-355c-32ab-8346-1bcb6931d973 | -8.35683 | -50.50174 | 2026-06-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfd2c91c-12e4-353f-91fd-2981a4a9581d | -8.87281 | -46.94153 | 2026-06-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cad3e048-2138-3bbf-b172-a80c7ae0d2bc | -8.97703 | -47.97656 | 2026-06-23 04:51:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a5deba19-1770-3c1c-a379-39949e1e56a1 | -11.05468 | -52.46178 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3eec4f0-25de-3c3e-8c51-5db485ef7be1 | -5.79911 | -43.78905 | 2026-06-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd58c8bd-8402-394f-9384-2bc1c74b62aa | -11.8148 | -47.34328 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19001c5c-fe2a-3765-bf6e-7299dcd13535 | -8.62012 | -47.79721 | 2026-06-23 04:51:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b50cc5f-60a7-34d6-94cd-3edb485f3651 | -9.38294 | -58.20138 | 2026-06-23 04:51:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba2c6fb7-fd36-37d0-808b-abad27b088d9 | -11.0508 | -52.46482 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1e80369-d181-3f7f-8bb8-ce25260c6c33 | -11.8954 | -43.83677 | 2026-06-23 04:51:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb411f03-6725-37cb-84e6-09ff0149837a | -9.21255 | -47.92945 | 2026-06-23 04:51:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f94c725-51c6-3dba-b0ad-9e1835cb0b20 | -10.88234 | -49.54879 | 2026-06-23 04:51:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b2a1a95b-2244-3d7d-bb68-10eabd05e0bc | -11.28209 | -43.34082 | 2026-06-23 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7b71fc2f-6257-366c-a502-7ad21835e419 | -6.25792 | -48.52393 | 2026-06-23 04:51:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bee1e183-77af-3151-ba23-a183f4c5fcc0 | -5.30235 | -43.68834 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0e3fe505-445a-378b-95cd-f735eb5df695 | -11.81536 | -47.33901 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2db7e6f-79f8-3460-8961-c0a869d87095 | -5.30145 | -43.69449 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9187fbb-192d-39cc-988c-0f4f4ea6b862 | -5.30965 | -43.69402 | 2026-06-23 04:51:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1f2e801-4fa4-3b5d-8709-5788bf56975d | -9.82728 | -48.22659 | 2026-06-23 04:51:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da2d9dc-6f21-3177-b657-c4e929f05a0c | -9.45264 | -50.84211 | 2026-06-23 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87647b61-bc43-3f63-a177-0cfd007167cc | -10.11394 | -47.55072 | 2026-06-23 04:51:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b354127-ff10-36fa-8346-85bdc8d52a38 | -11.47425 | -46.68759 | 2026-06-23 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c61400e9-f554-3772-a982-5f951734374b | -7.72634 | -44.56691 | 2026-06-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbe7e4fb-873e-3de1-80ce-69664189af9f | -11.57307 | -47.4431 | 2026-06-23 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec60e80d-5f5b-3ea8-b4e2-d97dc16b1b72 | -11.05358 | -52.46892 | 2026-06-23 04:51:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 321540a6-82e7-3301-b3a2-755653ea6e12 | -11.80548 | -47.34632 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 526aff0d-df4e-3f09-9b3d-95e3a44ee5c2 | -10.77476 | -54.10968 | 2026-06-23 04:51:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ba0186b-86a8-3e84-80dc-fe85af5e575f | -5.92088 | -45.54916 | 2026-06-23 04:51:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c9da84b-7a04-31a6-87ef-1a1039d8c5b6 | -7.179 | -44.87641 | 2026-06-23 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7d49050-0326-3e3a-8daa-fb7b2ac1d607 | -11.28256 | -43.33696 | 2026-06-23 04:51:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f43c5d93-3f75-379e-abc2-74edf438b62e | -8.43782 | -51.56671 | 2026-06-23 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d4859538-c958-3251-8042-f7ff4e9266f6 | -5.82337 | -45.05102 | 2026-06-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e7f6b91-7e4c-3e16-8c4c-30e7dfe76824 | -11.81098 | -47.33836 | 2026-06-23 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 095f2b29-baf4-3fd5-aaee-48605a9d5495 | -11.47937 | -46.68391 | 2026-06-23 04:51:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 48946d5b-92b9-39cb-8ed7-36b99a88b4f9 | -10.54062 | -47.71186 | 2026-06-23 04:51:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad02af4e-dfdb-3d1f-aa91-1db34d7590ec | -10.2363 | -54.26419 | 2026-06-23 04:51:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README12.md)
