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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6de5907f-79d1-31ed-9f07-4209d1dc398f | -14.26568 | -51.74161 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 172.7 |
| 34077ec3-0acf-39af-b483-f134b1faa946 | -14.26272 | -51.77007 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 369.2 |
| f3d8d6a3-a514-3e59-91b0-e70b601dd6f1 | -15.29714 | -53.19296 | 2026-08-24 12:34:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| 187f2675-eb70-36e7-ba18-7359e4abc017 | -14.35336 | -52.88471 | 2026-08-24 12:34:00 | TERRA_M-T | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d7ddb77d-2f76-33d1-86d7-fff86b746d37 | -10.63988 | -52.24759 | 2026-08-24 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d80b42c6-7d3f-33b5-8aef-6e85f1f8e591 | -9.23445 | -60.38326 | 2026-08-24 12:34:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 4ffa33a7-e03e-3328-865a-41cc265044b2 | -15.69401 | -53.80529 | 2026-08-24 12:34:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 77090218-3205-3c1a-b93a-0f7040257c8f | -15.29975 | -53.17023 | 2026-08-24 12:34:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 27415d67-639c-3039-b413-84eccff6ec26 | -9.67909 | -55.09098 | 2026-08-24 12:34:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 681fc41e-2adc-35b2-b1f3-cd70c820969c | -15.3252 | -53.96285 | 2026-08-24 12:34:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 10ff7800-f33a-38b1-9c26-7f576dbeaffc | -10.62923 | -52.26405 | 2026-08-24 12:34:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| af50a8e6-413f-3843-a244-234fc3c7dcd7 | -14.27828 | -51.76476 | 2026-08-24 12:34:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 629d2aee-7471-3d4b-b3ce-cb8da0ff72b1 | -13.1581 | -51.36529 | 2026-08-24 12:34:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 36a16283-86c8-38ab-a44a-68b0b247f481 | -12.0753 | -50.5759 | 2026-08-24 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4f834d0e-ce8d-3c7e-b83a-ea0ef4fed4b5 | -14.2781 | -51.7953 | 2026-08-24 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 99eb4ebd-aaad-3ba2-8ee8-1aee0ffae9f5 | -10.6305 | -52.2518 | 2026-08-24 12:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| f7bf1f74-8194-39b1-a9d4-1fa896feaebb | -12.0563 | -50.5782 | 2026-08-24 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 961679dc-9e31-3c8d-8474-ff1c1377edeb | -9.7324 | -45.9981 | 2026-08-24 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f57e0b98-6219-3a11-8015-8d7028984da1 | -14.3364 | -52.9107 | 2026-08-24 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3e1f4d40-8329-3cd8-b6b0-6a0bf2c98b1b | -6.8305 | -52.5061 | 2026-08-24 12:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 12f69168-d51f-3b9f-a016-f6ea81ec64d1 | -17.7021 | -46.3866 | 2026-08-24 12:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 143.7 |
| b5618328-ba19-35dc-a3a1-b85f0b4cfc30 | -7.2901 | -45.3683 | 2026-08-24 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 00972352-7bb6-3869-ba2e-c2da5b7133b1 | -10.7985 | -50.9518 | 2026-08-24 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 8e211253-95eb-3740-8288-509f838ea964 | -14.2978 | -51.7713 | 2026-08-24 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 9824638c-ceed-3c76-ae7f-53cf18653eaf | -12.0566 | -50.5567 | 2026-08-24 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| b0adff14-2d5c-3200-98b1-2914dc848055 | -14.3558 | -52.9083 | 2026-08-24 12:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| bb158b71-4798-3c11-8c79-1935910cf8eb | -6.8491 | -52.505 | 2026-08-24 12:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| c4abf0c0-5047-3d5e-bf4e-b6c247bcdc8c | -9.7134 | -46.0003 | 2026-08-24 12:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8588a3fb-483d-379e-8559-a271fdf805d7 | -10.7988 | -50.9305 | 2026-08-24 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 904fc6c3-80af-3588-a0ea-8d502343d803 | -10.8174 | -50.9498 | 2026-08-24 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 05c76522-7aec-33e6-b0af-7c1d595883e0 | -14.9582 | -52.6827 | 2026-08-24 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e5013ac3-e2cd-32ea-bef4-211d9b78a855 | -15.2854 | -52.8084 | 2026-08-24 12:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| f456deb7-90e7-3add-b89b-d9234145b622 | -10.8174 | -50.9498 | 2026-08-24 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 5fc032f1-47fd-3d92-a1a1-91f7dd68f161 | -9.7134 | -46.0003 | 2026-08-24 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 202a2f78-cdc6-3ce3-a3d4-62373d2c76f4 | -13.1512 | -51.3854 | 2026-08-24 12:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| d9146622-19ee-3dd6-8109-8f62f0a6bc4d | -6.5596 | -45.2947 | 2026-08-24 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 84f0f436-7325-31f2-9faf-84f7743f771b | -10.6305 | -52.2518 | 2026-08-24 12:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 6d1161f1-5429-3bc4-8ee8-522fc0e8325a | -6.7471 | -45.2793 | 2026-08-24 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 3c535d12-43db-3571-a891-c8ad8bc59852 | -7.0193 | -48.0106 | 2026-08-24 12:50:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f06e2c79-de02-3e5a-94a1-b7b9668d6a58 | -6.8305 | -52.5061 | 2026-08-24 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 58defb59-3c33-3302-9e9a-2cbe7e7d85d9 | -10.7985 | -50.9518 | 2026-08-24 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 7d0a2d7d-d17b-3846-92b8-25d3cf1a79e3 | -14.2781 | -51.7953 | 2026-08-24 12:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| d017b40f-e140-38a4-8eac-cf09eb44d4ee | -6.8491 | -52.505 | 2026-08-24 12:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| fd514840-611e-3184-9880-57b84c0bade1 | -9.7131 | -46.0229 | 2026-08-24 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 0583f96f-c335-3207-a059-198ffe38bd8a | -15.3237 | -53.9617 | 2026-08-24 12:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| c3252aa9-cf69-3270-a003-61416ed4eaef | -7.2901 | -45.3683 | 2026-08-24 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 111.8 |
| a85311d9-46d0-3221-81fb-95b37fceb208 | -10.7988 | -50.9305 | 2026-08-24 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 25f0fb1b-c048-3ae7-8a22-938281d4be79 | -6.5408 | -45.2962 | 2026-08-24 12:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 3acfbcd5-f04e-332c-9406-1b9629565cd0 | -9.7324 | -45.9981 | 2026-08-24 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| ed0cf3bc-6a73-3bf5-a62c-145e3c4388e0 | -7.2901 | -45.3683 | 2026-08-24 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 154.1 |
| eaff6e28-4d29-338d-85f1-e5d29b45129e | -14.9582 | -52.6827 | 2026-08-24 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 962de1f0-830c-3911-8d5f-3023dd5e835a | -14.9388 | -52.6853 | 2026-08-24 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 1e8a38ad-0054-3f44-88c6-79be2efe1983 | -6.8491 | -52.505 | 2026-08-24 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 144.4 |
| 3715d933-557c-32ea-965d-06b30877a2d2 | -6.7471 | -45.2793 | 2026-08-24 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.0 |
| da8c0814-4773-34c5-807c-bf686f64d5a7 | -14.2781 | -51.7953 | 2026-08-24 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2191ab84-27ca-3259-9196-fcf01d57e2ff | -13.1512 | -51.3854 | 2026-08-24 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| bccd8369-a445-3890-8b2c-cb68390748e0 | -15.6951 | -53.8088 | 2026-08-24 13:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f2a7f53c-2d84-3b1f-bd3c-61497c5a2495 | -10.7985 | -50.9518 | 2026-08-24 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| bce59fbf-e55b-3a6d-9c17-1a7c04f3e78d | -7.0193 | -48.0106 | 2026-08-24 13:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| b0b62d09-d6fa-3b32-aa9f-115e0fbe2c55 | -14.9586 | -52.6614 | 2026-08-24 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 5b32c3de-53b9-367c-8604-11f92d01ee91 | -10.8174 | -50.9498 | 2026-08-24 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| c5609bd5-7870-36e0-8eff-1c67916f0fda | -10.6305 | -52.2518 | 2026-08-24 13:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 6ed1aa8a-6188-34f1-8ce0-4afd762c14d4 | -14.9392 | -52.664 | 2026-08-24 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| bf6f696e-fa90-3aaa-a55b-b6ebef80f62d | -6.8305 | -52.5061 | 2026-08-24 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| e6b14277-7297-3e04-8f31-36ab48bed76b | -6.8305 | -52.5061 | 2026-08-24 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| c9cd1b39-2a39-314c-bf5b-4ad5c724a203 | -15.6955 | -53.7878 | 2026-08-24 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 9d81d7ff-7369-3c93-bcdf-ba3e87a7867d | -6.8491 | -52.505 | 2026-08-24 13:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 2a1174f8-0206-3c8c-b608-cc2949f6908b | -7.0193 | -48.0106 | 2026-08-24 13:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 849fe65b-1e14-3fc6-b2e2-b1543139a9ed | -10.0046 | -46.8201 | 2026-08-24 13:10:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4e6b6bc1-10b9-3c39-ac30-87c24ff35a93 | -10.7985 | -50.9518 | 2026-08-24 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e65a13ff-0573-3c19-b8ca-20380acb90a4 | -10.7988 | -50.9305 | 2026-08-24 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 052daa18-6784-3a08-bae2-722a8793c6ca | -15.6951 | -53.8088 | 2026-08-24 13:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 9d4b26c0-ebd9-3883-b967-a452f6ae527d | -6.5408 | -45.2962 | 2026-08-24 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 4f114bd5-34a6-3472-8ae8-fd9004cc8017 | -15.3237 | -53.9617 | 2026-08-24 13:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2e286aee-60fd-37bd-95f4-60cfe727c3fb | -7.2901 | -45.3683 | 2026-08-24 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 3f5162ac-3948-3210-9b8a-95dfc30a44de | -7.8277 | -47.6602 | 2026-08-24 13:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 7a8ce301-7a8b-3a42-8809-53beec2f25ed | -11.4494 | -44.5353 | 2026-08-24 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| babe62a5-8dd5-3945-b0dc-9c0de44dc5d3 | -13.1512 | -51.3854 | 2026-08-24 13:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 31bc3973-e245-37c5-aeb7-faf8ff47615c | -8.1111 | -47.4812 | 2026-08-24 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0c49fcc9-f746-3248-b081-bea1ca907353 | -6.5596 | -45.2947 | 2026-08-24 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 9295ebdb-c2b0-31a5-86a8-d9344316f847 | -10.6305 | -52.2518 | 2026-08-24 13:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 144.8 |
| cea4b3da-0110-330a-8d8b-955207e902f3 | -7.2713 | -45.37 | 2026-08-24 13:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 3f99add8-cd06-3fd4-be74-5c3c608107db | -10.8174 | -50.9498 | 2026-08-24 13:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 46dc9313-969a-38cc-83a1-7b98b9a2be9c | -15.4979 | -53.9813 | 2026-08-24 13:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 33f93522-539f-350d-a656-5d7d0a8f149f | -6.5408 | -45.2962 | 2026-08-24 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 313dab30-b561-3e96-b3ca-fd01abfa3613 | -10.8174 | -50.9498 | 2026-08-24 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 804c3f71-90d8-357a-aa20-84ac1ae3fb56 | -6.8305 | -52.5061 | 2026-08-24 13:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 87de6212-82f1-3158-b2fe-8945652d652f | -15.2854 | -52.8084 | 2026-08-24 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 9a68b838-dd42-383d-9159-e96005ee1068 | -15.6955 | -53.7878 | 2026-08-24 13:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 7a6bbb46-68fc-38cd-b541-3234494cbc3a | -9.068 | -50.7784 | 2026-08-24 13:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c220b68a-6f69-3ccf-8997-3b2c85eaf116 | -10.7988 | -50.9305 | 2026-08-24 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| f113005f-07f7-3ae5-9f94-b6597f4f46f5 | -13.1512 | -51.3854 | 2026-08-24 13:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 217e635d-65a9-3745-9049-930948f143c7 | -9.7134 | -46.0003 | 2026-08-24 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f2c7b10e-71b9-383d-a5e1-677932aa4d0f | -14.9586 | -52.6614 | 2026-08-24 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 6d79677a-0cff-317c-8f4c-01e9f7fdac28 | -10.7985 | -50.9518 | 2026-08-24 13:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 89cc4d31-1e56-3188-ad9b-710eabe432d2 | -6.3505 | -54.7665 | 2026-08-24 13:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| d0845738-48e6-32cc-8324-be4de377e4b9 | -6.5596 | -45.2947 | 2026-08-24 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 17a5c2a9-8bd0-3e4d-a048-92cdfa0a586b | -7.2901 | -45.3683 | 2026-08-24 13:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 10f59ea2-6cb4-3c75-8927-bebddb1d94c1 | -14.9388 | -52.6853 | 2026-08-24 13:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 275.5 |
| 8b5de9ce-91ca-308f-b13a-952729c23b0e | -17.7021 | -46.3866 | 2026-08-24 13:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 84.5 |


[Clique aqui para ver as próximas entradas](README52.md)
