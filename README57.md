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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4735806-8137-3871-b328-ed54679ee3f3 | -5.50215 | -42.63278 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 372b5373-13bc-38d7-a0dd-f95f1c0d3866 | -7.94514 | -43.82616 | 2025-09-03 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f92710a4-2740-38ea-b486-ff86e9336c24 | -5.90752 | -57.74853 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 09251694-6cce-36b2-88f7-7f56bea7439f | -5.92547 | -57.72379 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ba736e10-5095-31a2-bc89-45a9f9a71ff6 | -11.60284 | -52.12323 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6a5d152-3a83-3973-af4b-f0d72c6c954c | -11.62972 | -52.05925 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f501c421-509b-300a-bf3f-92c67154be75 | -9.33514 | -55.22193 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c372a2b8-74e9-39d3-8d5c-10f205ea8ae1 | -8.86306 | -52.02586 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f87fe736-4e8e-3af1-8370-e58c688b829a | -9.9596 | -51.62386 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdb7fe7c-b81b-36f9-943e-cb84b5a2f714 | -11.00465 | -46.93669 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66cae2c3-5da2-35ce-b1d8-6436e6d8d269 | -6.40978 | -43.7568 | 2025-09-03 04:46:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 78d25b0c-216c-3e79-83c0-a4a5c68c1473 | -5.51563 | -42.64692 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ce2ce7b7-7cf7-3264-ade4-1acb51e2615a | -9.7307 | -49.00425 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2e26029-5dd5-306d-9a00-828c97102c2c | -6.43675 | -58.13486 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ea17c26c-efd6-3de9-8cd4-b0d582ee7b8a | -5.90976 | -57.73515 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d4d751bf-2344-3c49-a05a-6eef4867d3ec | -10.5447 | -50.42033 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03a3d6a8-fffd-346c-8e12-2d22c377a8ad | -5.90381 | -57.74316 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| da252a9d-bf7c-39ce-bb3d-d4482a5abb44 | -11.01287 | -46.82258 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23472550-f4a7-31b0-90a8-c6efed45837a | -6.89636 | -45.56763 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64069a0b-5aad-33ea-9909-f9706198f9e4 | -5.9027 | -43.35875 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54182199-e0f9-3988-86f9-bd6c0f09e7d9 | -6.79213 | -52.83014 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 437564d0-9c66-372a-b1bb-5c77d69e5557 | -5.87225 | -57.76604 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 97a43165-5244-30e1-bc2c-ffec42a50f15 | -6.43324 | -55.62375 | 2025-09-03 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45566ad9-614a-33a0-bf1d-31b9f97aed4d | -6.78212 | -52.80621 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56542254-989c-3f46-8601-bd661bb62e6a | -6.64881 | -45.90696 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f287f2a-b8de-38d8-9649-3949e5cc8605 | -10.49444 | -50.33351 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73eb5640-b60b-3e73-b4ae-ed9f1dbea598 | -9.65075 | -48.07353 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b4254062-45a0-36a3-b573-edbe0dffde3b | -11.21597 | -55.07388 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1cc8d55a-0ab5-3f76-ac88-ac52b6443fb2 | -9.73237 | -48.9978 | 2025-09-03 04:46:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4c2d5ee-8992-3a8e-95cf-143cc6f9bd30 | -8.33728 | -47.46485 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d98fc1b-2a92-3ac8-aaf1-2d42bf8a1984 | -7.63841 | -43.92469 | 2025-09-03 04:46:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1492170f-ff79-3efe-b4e0-3a9b9c0704ed | -11.60825 | -52.06659 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42ea861e-3419-325a-8d4d-f4df46bcdcc6 | -9.76825 | -46.92304 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55c285c8-514a-30b3-a2a7-446c4fd52dd9 | -3.4824 | -59.25764 | 2025-09-03 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bc9c568-73ac-37a3-b789-30348e43a44a | -7.005 | -43.22129 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e149977c-623c-30db-bcdd-99b059a41fa1 | -11.61057 | -52.13883 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1e850714-3a1a-36c0-9811-80fbf5cacce2 | -5.03502 | -49.22831 | 2025-09-03 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7fe51f8-0f0c-328e-8143-872f7b5e0e06 | -10.9913 | -46.82676 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18e90186-fd16-338c-b6be-94893a5c1e8e | -5.9031 | -43.39145 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d33b6cc-8c2f-34c4-a131-13d0ea2b5ce0 | -7.70236 | -48.72906 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 20.2 |
| b1ab6fed-8d5a-3465-8660-bef1d26706ac | -6.05799 | -58.00447 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b8f49f3a-2eb9-3971-bc30-2cd12ba05626 | -11.43692 | -46.91005 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c5cfe9b-2a51-3250-8437-8d879f47394d | -9.79979 | -49.98943 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65818142-f10e-302c-9612-07c438e98c8f | -6.78095 | -52.8135 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1fe40552-9675-3ee5-b1ef-65133af55bc5 | -10.08963 | -54.76902 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b027dc1d-02b3-37e9-a398-e27fc3a3e419 | -8.09429 | -47.59269 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b6f82a6-7699-3cb3-bac6-2372e7278554 | -7.22277 | -45.31391 | 2025-09-03 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88de06ba-b7cd-3dcd-8655-0a75f8dbcd82 | -7.92733 | -44.94104 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07e84269-8e41-3513-bcf6-c7df2ee182e4 | -10.45973 | -53.62186 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 402249af-8201-388c-a300-be665af0eb3b | -11.68048 | -52.21507 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26b45d6d-ea33-3669-9313-86ba2fd5f535 | -10.7293 | -49.59007 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3510e12-ebfb-335d-aa9c-7567e697218e | -11.79661 | -51.52913 | 2025-09-03 04:46:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f84e9354-2b00-3433-92c9-015146146029 | -5.89914 | -46.16437 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2b549d5-0536-37f2-89d7-f7c1007d0bdc | -11.91053 | -50.61535 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60d923f5-5ac7-3dc4-b704-ecb7d4493832 | -11.96817 | -45.79336 | 2025-09-03 04:46:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3620e454-1b69-34a3-9539-8584f95cf0f3 | -5.86995 | -57.77958 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ff33896d-12cc-32eb-ba76-30b5dda369bf | -11.63466 | -52.04925 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a73e76dd-c3ad-3dd2-a845-72282abf9b98 | -7.01519 | -44.34975 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7364bb0-e692-3c22-b81c-f19895f9370e | -9.1959 | -45.19621 | 2025-09-03 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23e9158c-184d-3266-9caf-76c806d1f3bb | -11.04062 | -52.04394 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dddbf3f-280c-3e7b-90b0-32047865b828 | -5.79966 | -43.23217 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6009c5c2-1681-3cb1-a34f-bcbe6089944e | -8.88547 | -45.82938 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48a723b8-0f02-3b71-ae28-a2b963adb222 | -6.23992 | -42.4268 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 05ca542e-85f0-3ba7-a4cc-874ba1e9cbbe | -5.82128 | -45.37564 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b80cda23-fdb1-3aae-ba2d-cde547534124 | -6.69515 | -48.39724 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 59f1bc80-49dd-39fa-b1c7-223e0c169d6e | -7.71697 | -50.29334 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2f688ac3-4e44-342f-8927-8b6e26907eba | -7.78187 | -45.44246 | 2025-09-03 04:46:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4319f482-2080-3470-9485-e42c5b7a6c27 | -11.2153 | -55.07794 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5501f6ca-3761-3843-a4dd-a4c915d143a7 | -8.83386 | -52.01412 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779d9a39-f7b7-311e-a0b6-d038876a5aa7 | -8.3649 | -48.31148 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62a3970a-c95e-36f7-83d3-8dda4454c69b | -7.52888 | -47.46359 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d0e0c30-9ab2-34b9-b49b-01fc30192baa | -8.88175 | -45.82494 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e9fe39c0-3cb7-3221-9e80-b4eb3b794ef2 | -9.79066 | -49.98036 | 2025-09-03 04:46:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd0dc42f-e067-3e6d-87f6-e4ea33a3f79c | -10.2805 | -54.26936 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e267306-ca12-3f81-950f-38e9a92900ce | -9.68983 | -51.03832 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b0f2186-e4eb-3114-a742-818f417aa64d | -6.47308 | -45.41436 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6d1a2160-9a01-3715-8e52-5a252713eff9 | -9.63347 | -47.86629 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2e69017-7f57-3712-b725-9c9fa048f7ef | -6.40318 | -51.61488 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8d22e28-638a-360d-9a7d-ae294dea3ca7 | -7.00043 | -43.26239 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f3940832-7308-3d62-8d84-b00fd6d8cedb | -11.67214 | -52.15993 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 45638261-803a-3c27-b1da-2c4b1d2f6b27 | -7.71033 | -48.72483 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61a8ddc5-e7bb-3d25-98bf-08c2e42bde60 | -7.70583 | -50.29902 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c4cacec1-ddcb-3cd2-a892-6cf7181b77cc | -10.84309 | -47.45032 | 2025-09-03 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1e2ff6a-1606-3c10-b541-bfc015344a92 | -10.4927 | -53.65345 | 2025-09-03 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a29a537-f60a-3ab7-8207-3b2bead76904 | -7.26192 | -57.5429 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed7bb64f-bbc2-3687-956b-014f9367c1a2 | -5.54765 | -51.34123 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37f0658f-e277-342e-9493-dd6edc133fc0 | -6.82992 | -52.81016 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c233068-95e8-317f-ac27-e6817264895d | -6.70169 | -48.40206 | 2025-09-03 04:46:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e1774924-70cc-3be4-a107-742474a651d5 | -11.60505 | -52.13076 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| af3250e5-c5c1-3cae-b45c-666553f71d38 | -6.90058 | -45.56819 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daa963d5-82be-3dbe-9d4e-48b0e5c04721 | -6.09448 | -43.28954 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c6ae03d-a536-3401-9499-ddca5da51d10 | -6.92911 | -44.26281 | 2025-09-03 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b7bcd1b-f6f5-380d-a710-9bf04329c41b | -10.74609 | -45.27195 | 2025-09-03 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c4bad61-777f-3784-9ba5-d6cf486c9dc9 | -6.87994 | -45.56197 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2423fccd-6465-3124-ae04-2ccb3ec8bbd7 | -7.90342 | -46.43728 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e834199a-de96-3e12-a163-9173236d91df | -10.91888 | -50.86693 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b878228f-bbd5-3316-a794-897590827f4c | -7.9053 | -46.48107 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f35f17dc-b819-3302-8d29-eedaed74ddc2 | -6.82655 | -52.80961 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87dcf31b-ce69-328d-96ac-af5068027b60 | -9.65062 | -47.8546 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 61ede2f2-5f26-38b9-b01e-a80099cc9442 | -6.75591 | -56.39242 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README58.md)
