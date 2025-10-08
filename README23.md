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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fddbaf4-1668-33d8-b2eb-937b6f7c9766 | -12.99566 | -46.77907 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c7d00bb-2d66-31fa-96bc-f6b26e10fa2d | -13.27935 | -48.04538 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 15dd213c-ca86-301d-be3b-0ad7efe42803 | -14.24517 | -45.86979 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15f861f1-04fc-364d-9a71-42f388ccbb9d | -9.17484 | -46.92401 | 2025-10-08 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a225de7e-f21d-3d6b-b750-da4da2f194b6 | -12.99069 | -46.77803 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 224a79bc-72d1-3b7f-8105-93565ce9f8ae | -8.66944 | -44.71888 | 2025-10-08 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dc42702e-a8db-33df-a1a3-d57aa6368725 | -11.22796 | -47.75963 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41483abc-b0fc-32ee-b03c-0caec5165931 | -11.68788 | -50.96412 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 003c603b-aa12-3f64-a103-64cade3aa963 | -14.01057 | -42.46843 | 2025-10-08 03:49:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f49f6dd4-f373-32f8-bb14-e154a4d446e1 | -10.0905 | -40.77835 | 2025-10-08 03:49:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| b948e561-f384-3fdf-bdb7-c6cc33ca3df2 | -11.50636 | -44.96471 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05a30b93-b71a-3e60-a096-905b6fb6cd9d | -11.86234 | -44.93103 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddf21796-0983-3f1c-90a9-ec13e22d84be | -11.80459 | -45.04256 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e0bb380-88dc-3247-ac2b-b4336f0e2f76 | -8.5169 | -46.29483 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63c3fa02-15a5-3142-8bdb-99ed8c1426fa | -14.39527 | -46.0279 | 2025-10-08 03:49:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9a02f1ee-8e89-3a5a-98d7-896086109720 | -9.18967 | -47.79715 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 20e26b6c-2f21-3be7-9d4c-8cc241a59865 | -8.51699 | -46.29551 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8069bab2-ba60-3917-867b-313a89f2f26d | -13.33456 | -48.021 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8cb72cc-4a42-3068-be0b-7fdec0ba7cf9 | -13.36028 | -47.55602 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c0f74ebd-edb9-3464-8ef5-0d48bef0d53c | -11.21947 | -47.77425 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8da94d62-522b-3cb6-89b4-fd317b4eb881 | -15.24392 | -46.36697 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| dbcd29f3-c7c8-3bc2-b938-077a85a687d3 | -14.77208 | -46.01061 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d16e6dc-5b34-303d-aab2-c99dbe49731e | -3.44752 | -45.59225 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| feb26cdd-2371-3bec-9ccf-be0e86ee3a17 | -14.71063 | -46.08804 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d5a80b8-08cd-3e24-b279-54db0c095cc0 | -13.84855 | -51.86377 | 2025-10-08 03:49:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 370e9dd6-ac1f-3ac7-aeba-9729f3699fa6 | -13.2261 | -47.17623 | 2025-10-08 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 300669cf-45a3-3925-ac49-6fdcabc53698 | -10.39998 | -45.36914 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c3cb46b-be42-347b-b0c7-565f79a1967f | -8.89137 | -46.02857 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a10b44be-a81e-3dda-916d-b0b32ec349bb | -13.26154 | -48.0503 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 354593f9-8d4d-3817-9b26-b533cffc392b | -13.80344 | -45.79689 | 2025-10-08 03:49:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ae3943d-703f-30d5-b1d6-b93420e0f238 | -14.83523 | -48.41707 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72a6e53e-37b5-3c98-804e-8669be05a399 | -14.94216 | -46.79496 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a07feb9-4dd0-3257-80de-6d89618012b4 | -10.46891 | -49.38498 | 2025-10-08 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59184927-6235-3c95-bc4e-badce559a217 | -12.99948 | -46.78613 | 2025-10-08 03:49:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 170204cb-6ff3-35e8-ad7e-be7a17fda394 | -14.70085 | -46.0131 | 2025-10-08 03:49:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b12429b9-a4b3-3146-9685-24358cc5bae9 | -9.18396 | -47.79613 | 2025-10-08 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 9169906f-0a90-3a20-ac90-e5011b966476 | -15.16468 | -45.74215 | 2025-10-08 03:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ccecc476-3889-3208-b022-da1995d248a8 | -13.07224 | -47.9262 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ae57b2a-4c39-3104-b9fe-cadfffcc70b7 | -12.15505 | -51.44607 | 2025-10-08 03:49:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 578d1951-8608-3a28-9798-932879db62bb | -11.85938 | -44.92172 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f412d8b4-15a3-3383-9464-37366e135284 | -13.06434 | -47.93824 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fd7acff-3c4e-3acb-a694-b40a6a37e979 | -14.75163 | -47.86188 | 2025-10-08 03:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2ddb9654-34c2-3086-a3a8-8b78bd1b742e | -11.67041 | -46.39931 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 642e8d8d-d403-300c-b051-dbe6ff8f892e | -10.223 | -48.17411 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bb0e965-8376-3849-830f-dbe2c71793de | -15.66445 | -43.65004 | 2025-10-08 03:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba5e4fb0-a831-38f0-a15a-9056bd341632 | -10.41769 | -48.09868 | 2025-10-08 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3288e2f5-50d6-3357-9323-6b4242de59b5 | -8.23374 | -44.18463 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 458bdd91-f2c2-39e1-addf-4631efb885d2 | -3.23631 | -46.79243 | 2025-10-08 03:49:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdb5d4fe-1248-3687-8dc4-a8e8c30f9fcc | -10.17794 | -45.55503 | 2025-10-08 03:49:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18fa1b90-e0fe-3896-adf6-ebc1a2254042 | -3.89937 | -44.90845 | 2025-10-08 03:49:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 88f127b1-81a6-3173-b50c-12422f3b4973 | -8.7531 | -44.2358 | 2025-10-08 03:49:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0cea2f97-e9ae-3336-96d7-595d852556b0 | -8.67908 | -44.73035 | 2025-10-08 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bc394183-0f45-3692-86c8-11cb7f00500c | -12.23418 | -43.78278 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c850870-58e6-3fd2-b752-0177ae84107b | -15.31318 | -46.1572 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40b76029-0dd7-3059-aba6-fcf6a76972d0 | -12.86469 | -42.62603 | 2025-10-08 03:49:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3c9f9461-e2d0-3d26-8a22-e3b4da375b4e | -15.31224 | -46.16214 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ea27a9d5-006d-3736-a421-f9eb5af99e25 | -11.4438 | -50.20474 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80e7be2b-9727-36f7-baf7-dbb72dacc652 | -13.26033 | -47.78987 | 2025-10-08 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b60e30b-55cb-324d-9b76-3df6abcdd7a1 | -11.71715 | -50.97738 | 2025-10-08 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 300f0fa9-d490-34e7-852d-77e8ae3b211f | -14.52696 | -46.63781 | 2025-10-08 03:49:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ef8b17ea-c030-30b2-bc6b-c7cb9b177d0d | -13.28996 | -48.47587 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c9fd14b-8555-3555-bf3e-4677a3e46b85 | -10.9123 | -47.13742 | 2025-10-08 03:49:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08d98c9f-ccad-3e3b-8ca1-c88fd6f55bb4 | -13.28556 | -48.04239 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68abdc14-b9f5-36ec-8bdf-005d703a167a | -14.94488 | -46.80664 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f5cd2b-56ce-36ce-a464-80146bc23df3 | -9.97889 | -48.78053 | 2025-10-08 03:49:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a4cacce8-f9a6-3fd6-b4af-649a39139cfa | -15.66354 | -43.65513 | 2025-10-08 03:49:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e1e0f9e-ad34-3a5d-81fb-98417b56b453 | -8.52079 | -46.24232 | 2025-10-08 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36b817e7-f191-3809-8d8a-7b01c13e0653 | -12.93998 | -46.85441 | 2025-10-08 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5e6b687c-832b-3264-93f6-5a8b54f03bb1 | -8.89191 | -46.02564 | 2025-10-08 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c131ef37-5366-325b-8933-074dfcd30d6b | -8.22991 | -44.17633 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d630a41b-6514-3346-8ba6-420adeca03f6 | -13.73767 | -45.66971 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 322654d0-dc9c-3146-b96d-2c8b430f1829 | -11.45921 | -50.20399 | 2025-10-08 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| afc457ca-9897-3f1f-a542-27a18cd35f01 | -14.91396 | -46.81779 | 2025-10-08 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bcf77903-4490-3154-b4d8-65d6810af75b | -11.15108 | -47.74473 | 2025-10-08 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aacb02a8-4ec4-3f64-b473-721800862420 | -13.82338 | -41.29193 | 2025-10-08 03:49:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ca78ba01-5b7d-30b9-85b0-eab96c30d19e | -12.24402 | -43.77569 | 2025-10-08 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebee42af-cffc-3d15-9050-ea52468a185e | -14.88266 | -40.56615 | 2025-10-08 03:49:00 | NOAA-21 | BARRA DO CHOÇA | BAHIA | Brasil | 2902906 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e7034aa8-1f9a-39dc-91e0-bd2adda4f307 | -11.84373 | -44.90547 | 2025-10-08 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eb79cf2-344a-3af6-b0de-cdbfc5f01457 | -10.94317 | -51.02863 | 2025-10-08 03:49:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5a841228-9375-33a6-aea9-56775f288260 | -10.38221 | -50.23243 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f054413d-f39d-3fa2-a8d5-064d31f623a8 | -11.69564 | -46.34727 | 2025-10-08 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9622c741-e3da-3b1a-8f80-85997ccf3490 | -8.67162 | -44.71805 | 2025-10-08 03:49:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a53aef46-b1fd-3cfa-8517-0f353dafc577 | -15.19635 | -43.73446 | 2025-10-08 03:49:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ac9996bd-da36-3b20-806b-098c344842c8 | -13.27165 | -47.56552 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66f8626c-4b29-30f3-a425-78bdf4ff901c | -8.2205 | -44.2038 | 2025-10-08 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1156992f-a76e-3b2d-b32b-4da8d040cc2d | -13.25485 | -46.4696 | 2025-10-08 03:49:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fed4565a-8059-3a83-b615-f00a614f09b9 | -13.75524 | -45.75277 | 2025-10-08 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b64bfce7-2eb8-3552-abc5-8dc23bb78c15 | -9.54309 | -47.76437 | 2025-10-08 03:49:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fae99f38-c059-3c2b-88c5-7a6e08b392a0 | -13.29109 | -48.47454 | 2025-10-08 03:49:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45ef4a35-c57c-3406-89ad-d978b55853d4 | -15.26005 | -46.33365 | 2025-10-08 03:49:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c39bcdac-6c45-3399-a311-82c8babd6532 | -12.74379 | -44.72144 | 2025-10-08 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32fd2d04-af1d-3e4b-890a-3375f63485c9 | -11.78476 | -38.42684 | 2025-10-08 03:49:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95d783ac-4bad-3f2f-98a2-abf8f51e7e7d | -4.45202 | -40.76975 | 2025-10-08 03:49:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 023b2936-0467-3166-99d4-f142a4222dff | -13.31049 | -48.02964 | 2025-10-08 03:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 661b3525-3ae9-3df0-8b90-2fc5cdb3f7fc | -3.42943 | -43.14929 | 2025-10-08 03:49:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f14d726-819b-38d3-ae25-c108cf477981 | -13.39342 | -42.69861 | 2025-10-08 03:49:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2aa0ca1c-192f-3cad-aa82-394cbe78ecc4 | -3.44692 | -45.59573 | 2025-10-08 03:49:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b98b4095-615d-3d17-a9e2-744f525e259a | -10.35795 | -50.28577 | 2025-10-08 03:49:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f07fe0a2-edec-3827-9beb-d1947542bab1 | -9.02582 | -45.80323 | 2025-10-08 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6dbd9d9f-d842-3353-92d3-e80f87a757df | -9.02148 | -45.80094 | 2025-10-08 03:49:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README24.md)
