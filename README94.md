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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49381b0c-28b4-3f51-87a8-9ef51442b7c6 | -3.2251 | -44.3853 | 2024-11-03 14:25:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 6bf63c88-9c31-3fff-bfbe-a53f7b8de546 | -3.2426 | -44.6125 | 2024-11-03 14:25:25 | GOES-16 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e95d0213-86f0-30cf-91a5-ff43d465a6d7 | -3.765 | -44.4297 | 2024-11-03 14:25:27 | GOES-16 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 0abdb1c5-a4f8-3621-926b-3b4a5a1dddd7 | -3.6888 | -44.7295 | 2024-11-03 14:25:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 2c731529-216a-30e2-b6fb-58baa783885c | -3.706 | -44.9782 | 2024-11-03 14:25:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cf9ac7db-a8fe-3080-bfd9-636a29aeb70a | -3.8176 | -44.9956 | 2024-11-03 14:25:28 | GOES-16 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| d437533d-fb18-36e3-9545-71c7f63d0aca | -4.1206 | -44.2058 | 2024-11-03 14:25:29 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| b00f9798-5fbc-3a5f-8604-cec409c48815 | -5.1579 | -42.9128 | 2024-11-03 14:25:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 6b598d0b-8e58-3500-9efe-2b56460b2588 | -5.6003 | -41.6696 | 2024-11-03 14:25:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| 92c863d6-446c-354e-afb5-2ff60d0c74e4 | -5.6005 | -41.6456 | 2024-11-03 14:25:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 86624479-436f-39e4-9280-112d43cd3712 | -5.9927 | -41.9007 | 2024-11-03 14:25:40 | GOES-16 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 251.1 |
| 5ee8a4cb-0c96-3292-9ab3-30aafa2ef0ce | -6.2401 | -41.6153 | 2024-11-03 14:25:41 | GOES-16 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 8fc40ad5-118f-3160-84b9-b5123611583d | -6.9971 | -41.3258 | 2024-11-03 14:25:46 | GOES-16 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| cb2ca004-a883-3a77-b7f3-106eaf352081 | -7.6591 | -42.7646 | 2024-11-03 14:25:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| a06d861e-9d0c-3280-8769-2c13c82949cd | -8.3281 | -43.6091 | 2024-11-03 14:25:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 751ca04e-0dfd-362d-8e19-cd700d380094 | -8.3287 | -43.5623 | 2024-11-03 14:25:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 24e7163b-cebf-3a63-b558-b636d3a1febc | -8.347 | -43.607 | 2024-11-03 14:25:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 910dc596-239d-3ffb-b275-69181a49f919 | -8.3473 | -43.5836 | 2024-11-03 14:25:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 1e74e0e6-b1c5-3375-bd85-3fd56d62acc9 | -8.3284 | -43.5857 | 2024-11-03 14:25:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 40c2615b-63da-3141-af9e-e9f5735a8ea5 | -9.7099 | -46.2488 | 2024-11-03 14:26:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 69a65cfd-a046-3456-bbb4-764c365627df | -9.8018 | -43.8767 | 2024-11-03 14:26:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 120c22bb-e280-37ad-842d-5ba4c9ddca2b | -9.6912 | -46.2284 | 2024-11-03 14:26:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 75fd61ef-bbcd-3fa4-98e7-308b394bb19e | -9.8021 | -43.8533 | 2024-11-03 14:26:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 494f89d8-905e-3deb-8335-a1c62d9d9fa2 | -9.7096 | -46.2713 | 2024-11-03 14:26:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d072111b-d561-3b9b-9b8c-4c0e8690cf52 | -9.7288 | -46.2466 | 2024-11-03 14:26:01 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f46eb61a-e532-3ed4-91ec-e10e1e7893fc | -10.0124 | -43.7791 | 2024-11-03 14:26:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| b8a0d161-15df-3e0c-bfb0-894bab1910b3 | -10.012 | -43.8026 | 2024-11-03 14:26:02 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 0426531e-7a47-363f-a163-c6728519306a | -10.266 | -43.3925 | 2024-11-03 14:26:04 | GOES-16 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| e896f6e3-103d-382e-9644-0f03c9d6cb30 | -10.2473 | -43.3715 | 2024-11-03 14:26:04 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 8477a392-8ce9-372b-850b-cc7bb3b27a44 | -10.2664 | -43.3689 | 2024-11-03 14:26:04 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 97.7 |
| e36da2bd-58c0-367b-9797-98aad7ec82cc | -10.8894 | -44.8927 | 2024-11-03 14:26:07 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 5306a741-79e1-34d3-b7f3-7871533cdd78 | -10.889 | -44.9158 | 2024-11-03 14:26:07 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 93b99fa0-ed4e-3965-b66b-e31abcf8a402 | -11.0176 | -42.9763 | 2024-11-03 14:26:08 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9663e652-f8c7-37a7-9044-547b20609b61 | -10.9097 | -45.988 | 2024-11-03 14:26:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 3752b285-09a5-38e7-8156-9a390297c255 | -10.9081 | -44.9132 | 2024-11-03 14:26:08 | GOES-16 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 5598c904-e20c-3df3-b3d2-8d1155171a31 | -10.9085 | -44.89 | 2024-11-03 14:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 1ab62576-1935-333a-a359-18792d2ec00e | -17.6273 | -57.487 | 2024-11-03 14:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.5 |
| a7d62342-82ef-312a-a6b8-7c8e5a45e43e | -17.6276 | -57.4664 | 2024-11-03 14:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.0 |
| d2acc3ba-4cab-3919-aea4-5d5da2b9741b | -0.803 | -48.6397 | 2024-11-03 14:45:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 2c22be6f-8ab8-3bdf-a11b-a1575148ce4b | -1.4211 | -54.197 | 2024-11-03 14:45:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| be175093-cef7-3356-9804-45de8ab2bf49 | -2.2616 | -48.83 | 2024-11-03 14:45:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fdd7af8b-920d-3c79-838c-c1d393eec4ca | -2.3539 | -48.8492 | 2024-11-03 14:45:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| f0926a4f-2999-3bd8-b22d-edd028a0ac80 | -2.4095 | -48.805 | 2024-11-03 14:45:20 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6f38f3b8-4a5c-3914-8afa-59ac39be16fd | -3.3911 | -44.6973 | 2024-11-03 14:45:25 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 714dbb0e-58b8-3191-8375-6d919e2b9607 | -4.4054 | -43.4746 | 2024-11-03 14:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 50895418-e3d2-3f64-87d3-787d5bc760eb | -4.7662 | -42.7279 | 2024-11-03 14:45:33 | GOES-16 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 7705ce60-5906-3145-a0b4-4e677970ac40 | -5.1579 | -42.9128 | 2024-11-03 14:45:35 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1ce311af-58d7-3b7a-8eb4-ebfc30c19017 | -5.6003 | -41.6696 | 2024-11-03 14:45:38 | GOES-16 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 3a340d27-327e-3792-9e99-b3b9784f009e | -5.7269 | -42.185 | 2024-11-03 14:45:38 | GOES-16 | PRATA DO PIAUÍ | PIAUÍ | Brasil | 2208601 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| 2adb263d-9b86-31d2-9e3c-f0dfb8853533 | -6.6349 | -43.4272 | 2024-11-03 14:45:44 | GOES-16 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 2f4a0433-c578-3d6c-8f77-8bbee8fe5191 | -6.6765 | -43.0491 | 2024-11-03 14:45:44 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| f10041f1-8088-3410-bcbb-27714769fa5b | -7.6591 | -42.7646 | 2024-11-03 14:45:49 | GOES-16 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| 66027e34-5f08-3c69-b02a-b246352cc01f | -8.3473 | -43.5836 | 2024-11-03 14:45:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 202.2 |
| e404aabc-ce17-347b-a0ba-056258caa46d | -8.3287 | -43.5623 | 2024-11-03 14:45:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| fc1843ed-7ea3-3f74-9801-650fa28b252b | -8.3281 | -43.6091 | 2024-11-03 14:45:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| ecf738cc-8ad6-3c64-8e72-a7bb2b3340e4 | -8.3284 | -43.5857 | 2024-11-03 14:45:53 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 5ce079a5-ef24-31e6-855e-805508d46aa2 | -9.8021 | -43.8533 | 2024-11-03 14:46:01 | GOES-16 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 33b4f676-e349-3bad-a6f2-8f0c0023919c | -10.2473 | -43.3715 | 2024-11-03 14:46:04 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 87.2 |
| f2b1b5ac-8471-36d1-8638-527a6143bac6 | -10.3016 | -42.3886 | 2024-11-03 14:46:04 | GOES-16 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 92.1 |
| e685c4c4-3f07-33c2-a91b-277c71af9ad7 | -10.2825 | -42.3914 | 2024-11-03 14:46:04 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 7e3249b6-9dc5-36b6-a935-1a69d9a4375c | -10.2664 | -43.3689 | 2024-11-03 14:46:04 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 194.6 |


