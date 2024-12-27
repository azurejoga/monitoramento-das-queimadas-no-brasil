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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 876b6b5a-7e2c-362f-863c-1c3fbd805011 | -3.7494 | -47.19086 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c38495b9-26b6-374f-acb1-be45ca4b119c | -3.94397 | -46.98882 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4afe791-990b-3cb8-9c3a-fd953c3aa5c6 | -1.58356 | -53.38549 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7da969ae-c8f5-36b4-b07d-8bf1ddab0620 | -2.28485 | -45.74023 | 2024-12-27 04:31:00 | NOAA-21 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3560a470-ee17-30d9-81de-380120c8c795 | -3.41412 | -42.40304 | 2024-12-27 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ad59c17f-822b-31ec-b9dc-f0fc83f31a65 | -1.44237 | -53.67931 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8c95654-1032-3498-ba20-cbb8c5fa5b47 | -2.71844 | -46.01031 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4caa072-ca22-3506-a368-015d227908b0 | -4.03827 | -47.05992 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27203cb7-346b-3997-9f3f-d5d85940857d | -2.62423 | -46.11432 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b131f9b9-f9f7-342b-bfb9-fc31200f4fde | -1.72709 | -46.2186 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81f0e349-80bc-38e3-a47c-8ec9327668ab | -4.06696 | -47.07493 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db4427ec-9b80-3e9f-8567-7ffc9568a9c7 | -4.04757 | -47.0437 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0bc1eb96-0c14-3608-bfad-fda23917d19e | -1.64523 | -45.8696 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6dba88c4-53d4-358c-94b6-b2d8bfe723be | -2.61756 | -46.11329 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6486c86e-93ca-3969-a21d-f54feb76ca01 | -4.09982 | -45.3092 | 2024-12-27 04:31:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53c2f7ad-6335-3d86-9b2b-6313e6558b81 | -3.89551 | -46.9955 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de8b5d50-2075-3dd0-a9f0-2f1da3bfeb86 | -3.73395 | -47.18144 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c29a7e26-f7e1-337b-95e9-2d102bd3cf02 | -3.88264 | -46.94753 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dc84b33-7a44-3650-8a81-c8115f23f687 | -2.74737 | -46.19833 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c006cf-03f6-3dfd-8502-b85ebbe02217 | -2.76164 | -46.12872 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 80329d86-68a0-35e4-91c2-67d7141d8d18 | -3.88846 | -47.01908 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88168e29-60e7-3d8b-a5d4-b6bc2879dfc7 | -3.99146 | -46.68409 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07203658-4f74-38b7-a737-be27cdfb3206 | -3.68772 | -47.17069 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f7597ed-d82d-37f8-97bc-c7480248cf68 | -3.03858 | -40.12013 | 2024-12-27 04:31:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 559c73d8-0d03-3a35-9732-3fe98fb27218 | -4.16672 | -42.02953 | 2024-12-27 04:31:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81d8d89a-d660-32d2-aef3-69c1e4e4aa62 | -4.20638 | -44.35865 | 2024-12-27 04:31:00 | NOAA-21 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96f98d7f-088c-39f8-9aa1-3a761a30aac0 | -3.82307 | -46.62917 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b09ace4-d4e4-3835-8d55-26d0de79ff35 | -3.73627 | -47.34012 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd25b6aa-3080-344f-a41c-b3e37231f0ba | -3.89891 | -47.01717 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 899baebc-916b-3aac-955a-a42e41ec92ec | -4.03765 | -47.04219 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c6e4f60-e3cb-3348-95a7-ba0d10ae97e4 | -2.80621 | -47.58862 | 2024-12-27 04:31:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10ff7897-6cce-36c4-aef8-7363d396aad5 | -2.63642 | -46.10183 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12e1ead6-77eb-3184-8fd2-da320206a488 | -3.98591 | -46.67609 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ecc3ea4a-ecb9-3ea7-8f95-5a01c7058e7d | -3.90956 | -46.92697 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0504ce25-5ab2-3201-beb6-39c9b3bff5b4 | -3.18688 | -45.973 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14ed2ebc-105a-34d8-86d6-bb35fd5452f7 | -2.695 | -46.59954 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b61fd9b-b562-3b2c-b616-f3124adc349e | -3.89605 | -46.99205 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d639c52-dc9c-32c0-845d-7011eea15eb0 | -2.61702 | -46.1168 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57ec4c97-b1a9-3794-8310-35cff8a9b1a6 | -3.89176 | -47.01959 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f217daa-cb5d-31d2-b6c6-920b02513f1d | -1.49473 | -52.39354 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e15ec02-c2be-3d72-9b85-b291d67501d8 | -1.72377 | -46.21809 | 2024-12-27 04:31:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab5ee9e9-1b6c-35d7-a82f-b34ed7edf6be | -3.20744 | -52.441 | 2024-12-27 04:31:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 416d151f-4a4f-3b08-9a43-df2b0ca1aaee | -3.41359 | -42.4065 | 2024-12-27 04:31:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ebfc0992-56a0-3bdd-8a61-054180bf68f5 | -2.64085 | -46.09533 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2a52289-18d9-3b61-992a-593100a8c793 | -1.48938 | -52.40038 | 2024-12-27 04:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eaaf1f4d-7412-3a63-a290-2ec5800ee339 | -1.7832 | -47.8425 | 2024-12-27 04:31:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ace45a87-263f-37f2-bc47-b4c1731e2f4d | -3.87577 | -47.01359 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10dd71a4-3769-36bf-8d38-45fd19b1d6f6 | -3.9734 | -46.58142 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b6dbac-bc78-362c-833c-0c095546e5f7 | -3.93074 | -46.98677 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41548eb3-b92b-3144-9feb-a79883d5edcd | -2.28582 | -45.57925 | 2024-12-27 04:31:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41480b88-61d7-3757-8b3c-8c6a77ae8e35 | -3.418 | -44.89999 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c033ea44-f461-3d33-a072-10537065d57e | -4.03497 | -47.05941 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e120c555-2c63-3ecd-9955-52d3f0edae59 | -3.19584 | -45.98167 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb3f5f6b-f322-319f-b21e-c62bf9004a00 | -3.18724 | -46.12543 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0c5c27c9-96e2-3a73-9ce8-626aeedf92e1 | -3.94012 | -46.99175 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cab8042e-740c-3d5d-a305-f4574484f429 | -2.64146 | -46.11339 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4357677b-c774-3e49-aaa2-dc96eee654ff | -2.6209 | -46.1138 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb9a7615-078f-31aa-bbbf-3dce15a514b2 | -3.73681 | -47.33669 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9977a76c-f65c-3d62-876b-3b296ee35e82 | -3.1323 | -46.34721 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cf522f0-7b40-38a0-9ddf-9834acdd198c | -3.97645 | -46.34108 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf15ec2a-747b-355b-8e7d-185e55854fd6 | -2.83066 | -46.69115 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f906c3d8-35fb-3e14-a1ae-e43df17f19d4 | -2.61647 | -46.12031 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 59589143-cab8-3f45-bcf9-df23f6af782f | -1.64027 | -45.87963 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0384246c-9d92-3afc-bef2-136e67f41ed9 | -2.7301 | -46.17774 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fef5dc4-2180-3f94-8fbd-739d9dfc81c4 | -3.74064 | -47.33376 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2220a142-84d9-3d16-881b-5fd387d0e84b | -3.54195 | -40.92279 | 2024-12-27 04:31:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b33458b8-0747-3da7-8fd6-398a7615709f | -3.19059 | -46.12595 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e5101f3-31bc-3c67-b38c-179524a3aad6 | -2.69831 | -46.60006 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a0dbbd8-9928-33ff-bc4b-2540b597e1ee | -0.66071 | -47.29791 | 2024-12-27 04:31:00 | NOAA-21 | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c719b9ff-e600-3242-be65-462f37c02423 | -4.24411 | -41.92352 | 2024-12-27 04:31:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 40402022-3482-3cbd-abb1-c410fbc34a1f | -2.96376 | -39.96537 | 2024-12-27 04:31:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc98be72-9a63-32d7-95f7-fe9098651b57 | -1.64244 | -45.86558 | 2024-12-27 04:31:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c927a7f-dd84-3e05-a49e-0b62d81097ac | -4.52634 | -42.0644 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d81ee5b2-dd36-3995-88e6-741abf9af61a | -3.74779 | -47.20118 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d07512e7-6421-3d76-9f2e-6ba712a814f0 | -3.19474 | -45.98879 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ebda05a-791a-3b12-a79f-535ea08483e1 | -3.75109 | -47.20169 | 2024-12-27 04:31:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82a94fd1-0cf1-3c64-bf2f-8bed9278092c | -3.69568 | -43.40854 | 2024-12-27 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6902741b-aaa3-338a-a92f-c94188df401f | -3.92412 | -46.98576 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b9ece6c-6d59-3115-9604-4bc66ac09606 | -3.99092 | -46.6876 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3e5e9ac-303b-3f9c-a87c-ef1e0d0a51d3 | -3.86808 | -47.01945 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cad450c9-3663-3293-b6c6-4150e3403819 | -4.51994 | -42.07895 | 2024-12-27 04:31:00 | NOAA-21 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| c7c9d23a-7139-3a60-995e-26929c8f4675 | -1.89294 | -53.28571 | 2024-12-27 04:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9b4dea73-5e93-3095-ab82-689826c9e4b8 | -2.96633 | -39.96289 | 2024-12-27 04:31:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 46c9612c-8714-3ce5-be78-02d175cb9992 | -3.69946 | -43.4091 | 2024-12-27 04:31:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b8ccc7c-73e3-3294-bbf6-dbed6d16e18f | -4.0109 | -46.71205 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f30d48a4-7634-3884-95ac-112bb0d9d077 | -3.87523 | -47.01703 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de993ab7-d6a0-3cdb-8146-1eff0cca7d9d | -2.3474 | -45.41428 | 2024-12-27 04:31:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eded2da-4cce-344f-9c8b-e9e29c5cbbb1 | -4.70204 | -38.16614 | 2024-12-27 04:31:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 686d98c0-f847-3a71-8055-435cfeed2625 | -3.89945 | -47.01373 | 2024-12-27 04:31:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9813462-d319-393e-81dc-658b9cc26217 | -4.00704 | -46.71502 | 2024-12-27 04:31:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a03ddf47-d4cc-34ff-a2cb-eefd785d1274 | -3.07413 | -41.89711 | 2024-12-27 04:31:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8152dcec-7602-36e1-aa58-2fe0a39c1862 | -2.76263 | -46.07846 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dde289a-8cf9-375c-ac4e-59d1f6d71ebb | -3.90902 | -46.93042 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 394d2a29-3c4c-3bdc-8fd5-4e8ae7bdf610 | -2.58474 | -46.10467 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 294afdb0-c1f7-3694-aa75-145585597a89 | -3.18779 | -46.1219 | 2024-12-27 04:31:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7891adc-aa98-3377-a788-e77d68041ef1 | -3.41102 | -44.89892 | 2024-12-27 04:31:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 50f58542-f3cd-37d8-9635-f01579058c93 | -1.65305 | -45.44962 | 2024-12-27 04:31:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e1d06a6-a241-3fd6-90f9-1e958f90d90c | -2.72731 | -46.17373 | 2024-12-27 04:31:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db373ec4-0bdb-3451-9642-a3f82f867194 | -2.81598 | -45.92718 | 2024-12-27 04:31:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d28e51b9-bb6c-3ca0-8492-cd6333ab8673 | -3.07041 | -47.77126 | 2024-12-27 04:31:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README10.md)
