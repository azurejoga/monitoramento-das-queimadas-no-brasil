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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff9a9673-af2e-3c3f-a74b-dd88828f2bc5 | -8.18421 | -48.17843 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40cfb61c-4ca1-3d20-a888-e6b5acd11fdf | -8.97029 | -50.1857 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5bcde51b-5707-3b4d-8187-cf26cd811621 | -10.78439 | -49.2592 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bb33f49-7e53-3460-8df6-d112501d27ff | -10.53415 | -49.5476 | 2025-10-28 04:44:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e05b56f-c2a8-3cd9-a71a-f0df885e276d | -12.07539 | -45.64493 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45f82deb-cf16-398d-97bb-b5060f1166b5 | -10.39201 | -45.30635 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3667c2e5-9064-3d26-ad71-dfa5c35a9f22 | -12.24037 | -47.92102 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12350391-674f-3c06-bcb6-c2e52088f642 | -13.31983 | -47.44372 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a0bf9f1c-c706-331c-8a1e-db2d36c6f448 | -10.98994 | -50.3549 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b34505a9-a0a9-3b10-9d8a-e23a33992cda | -8.11994 | -48.81751 | 2025-10-28 04:44:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aae619cb-3e36-31c8-a469-3977c1c719c2 | -9.88121 | -44.88568 | 2025-10-28 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 965cf2b9-5bca-3655-90a2-68b21994473f | -11.28396 | -45.51495 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.2 |
| d414d767-5e67-3c9a-8d90-bb709b3f12cc | -14.53468 | -47.99794 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 010bc0d3-f2c7-321f-a238-eb2db5f87ec1 | -13.31121 | -47.6904 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d860d3c1-ed48-320e-84ee-024bf4939fa9 | -10.28986 | -47.20381 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd644043-070b-3298-9850-ff0910093f82 | -9.58528 | -46.96181 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c362059d-919c-3b5c-980b-c740bd025304 | -13.25413 | -47.72937 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 189a1e64-756d-36fd-8581-f4d1a588b8e6 | -14.54023 | -47.97988 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f4ac17-c334-33ea-9656-cb86a3f89007 | -10.58461 | -49.79568 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 273ec71e-0ce6-3620-8c5a-e48a8e3225a3 | -13.22173 | -47.10238 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f8bc0be-d18f-3789-8b38-762f3f3ab075 | -8.44493 | -48.20707 | 2025-10-28 04:44:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d752a877-6785-3bb5-913f-a3b29a69b63d | -13.23254 | -47.08081 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 55254b31-59bf-3715-98d1-2117d7c09da9 | -15.56791 | -43.25828 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 21b86b36-73b7-35c3-b745-f99d89bec639 | -14.05834 | -44.40075 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 42e2ed56-5ea4-36e8-90f3-f4525cd9d57b | -15.57437 | -43.2055 | 2025-10-28 04:44:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| f6b3d53d-8ad0-358f-94ba-5c9d444b01df | -13.91183 | -48.48682 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bf44a40-a18b-382c-928d-c3a330a6dc53 | -12.0851 | -45.66482 | 2025-10-28 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c77f9756-bbc0-3723-9a4a-d8be84186a35 | -10.94021 | -47.66241 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b8394f8e-71c1-3a48-aa2c-cc405df68fa3 | -9.05612 | -46.94276 | 2025-10-28 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f753185d-9c83-3cbc-a205-cd1444ac7ba1 | -13.54241 | -49.57278 | 2025-10-28 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47197c73-35ba-3629-9ea9-212b7af6b4a5 | -13.36155 | -47.39022 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c649ef6f-8433-37a1-bfbc-f8e934971a8c | -9.27247 | -45.57184 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efa45170-115e-377f-94f3-ca2dbd11eb0b | -9.31114 | -45.84948 | 2025-10-28 04:44:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c07b9628-d358-38c0-903d-5a3836a088f1 | -10.29111 | -47.19537 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cc4755a-cb54-3ebe-ae12-2f909f96f02c | -14.14737 | -46.99148 | 2025-10-28 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bc631d3-0c4d-3af1-a411-a925d9c438fb | -13.55101 | -47.16777 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 211ee419-cdb2-3e6d-b87f-d6cff67f6fa4 | -9.33537 | -49.28334 | 2025-10-28 04:44:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce01d6ff-93bb-3861-9ca4-a37a4a668c31 | -13.55921 | -47.16439 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbff95e9-fbdb-3cb1-9233-83371a4c1e52 | -12.59215 | -52.85376 | 2025-10-28 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0412b3-eeba-32dc-aa49-34b9e46df45c | -10.57584 | -44.53114 | 2025-10-28 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d5401e1-7110-312e-bd59-38ad1fbe46f4 | -8.61915 | -47.70775 | 2025-10-28 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 441b9e10-c068-3935-997d-413129c48162 | -9.53559 | -46.94533 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0159ea6-6ffa-370f-b35a-40660bf482d9 | -13.36093 | -47.39458 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4feace1-7394-3a69-b036-c8c42c3e2588 | -13.36244 | -47.67259 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 570324da-5382-39da-9f81-2779ad95512c | -13.24491 | -47.96791 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e098ddd2-1fc7-3cb4-b0f3-5329b2603f5e | -14.66746 | -48.41235 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 522a2688-4466-3b58-bafc-916e0dc2f0f5 | -9.96363 | -47.09478 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5329cb4-7a2c-3d0a-b038-2e612fa600bd | -10.40515 | -45.29765 | 2025-10-28 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31f95d28-93ec-38dc-9fc4-e782b067d9a6 | -10.75851 | -49.78291 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a6d64e3-de78-3d53-9262-5bd969dc93b4 | -13.27054 | -47.87066 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a6cf7b4-fc7b-39a0-96ab-d993a8aa32fa | -10.85707 | -48.96437 | 2025-10-28 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e3b202f-7ddb-3638-8227-c12c50e79dac | -12.61898 | -44.24966 | 2025-10-28 04:44:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a0013a19-8f32-361f-a93d-df3a834b03a4 | -13.87736 | -48.49933 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5b18105-d7df-31e9-8118-da4978083b17 | -13.7908 | -48.50296 | 2025-10-28 04:44:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57406809-6d56-3d93-8310-d55ce4e4ca22 | -10.92001 | -50.26469 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09897e05-5a11-3e9b-9f49-b42f9003c454 | -11.07809 | -48.3319 | 2025-10-28 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03eaff83-bdce-3c3b-9705-16cbae52f7e3 | -9.56154 | -46.97125 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c38ae9a4-7f11-3cd7-bff2-0b27ab386ed2 | -13.54331 | -47.14064 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e6da646-8043-3fda-bb5e-98fb0cf554b9 | -9.96063 | -47.08997 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3cd3d2b-50dc-3f57-b1b0-6626ae967d44 | -9.1696 | -44.57415 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a65bce85-3deb-3686-b797-0ed16925e003 | -9.95636 | -47.09372 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab22af3e-db02-3105-99d4-3b9648f8f1e5 | -11.03087 | -47.8544 | 2025-10-28 04:44:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54731660-665a-322b-8c3a-ebd503a0f9b0 | -10.29886 | -47.21806 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6894a9a-21ec-3bc6-b355-95c0f483d8de | -14.05773 | -44.40538 | 2025-10-28 04:44:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cc0c709-f3f9-3640-bd40-b16a5e594a2e | -15.3138 | -48.02399 | 2025-10-28 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2aebfea5-c56f-3821-8b81-d3bb4d11cabb | -8.6853 | -47.13057 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1477cd7-7170-30e7-886f-5c325cc579eb | -12.0844 | -46.39065 | 2025-10-28 04:44:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91074a75-3a27-322e-9863-6abd1eef2fb8 | -8.25617 | -46.89424 | 2025-10-28 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9615d6cb-6703-3bbf-8aba-3c23ecbc549d | -11.946 | -43.33958 | 2025-10-28 04:44:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16b33679-c4de-3ac5-bbed-b5a87eb8055b | -9.17321 | -44.57875 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0f1a943-a1ce-3a35-b3c8-32c3e1296115 | -9.85819 | -47.70676 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5d29ca9-6e6b-36d6-9bc6-2a0a9e6342db | -13.26142 | -47.73049 | 2025-10-28 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83fa9ad8-c4b3-31d8-93ee-a68bd23da819 | -15.17431 | -47.21283 | 2025-10-28 04:44:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9eb727e8-a863-302e-9438-0b640f2cb963 | -10.77106 | -44.76194 | 2025-10-28 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11a89868-4d90-32e1-abfb-59609b56b6e8 | -13.63166 | -47.02844 | 2025-10-28 04:44:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e2c5f191-0d60-3d31-a199-c730397c1bd7 | -13.38595 | -47.35249 | 2025-10-28 04:44:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be942577-2216-32e8-9a6c-09cf1b2c7db5 | -14.53597 | -47.98358 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea341fc5-3590-3205-8e00-ff6009955987 | -14.66388 | -48.4118 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 423b6f72-249e-3e9a-9156-26371dca5582 | -10.56408 | -47.89684 | 2025-10-28 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 932bfae5-349b-3360-9af5-9a5f87ddf801 | -9.53972 | -46.96788 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c62e761-1ff8-33f4-9910-428acfc69b62 | -9.76622 | -44.99846 | 2025-10-28 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb01240a-bd87-3a67-8d06-a6928d47519f | -10.30638 | -47.16759 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee4c54fd-7089-3ac1-9277-d420c5617573 | -14.54087 | -48.00185 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc72da02-0922-30d3-90de-05281c227bd9 | -10.86425 | -49.64279 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76d8fdc3-e89e-3eae-bef3-13b5afe95a79 | -10.28547 | -47.23331 | 2025-10-28 04:44:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a300acf-c8e9-3e44-9db7-6cfa005c596f | -9.91942 | -47.68366 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9e8e3c9-91da-3eb8-ae4d-b72e71ee69c6 | -9.09313 | -47.81604 | 2025-10-28 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 923dc7b5-277f-30ca-9a0d-1a1485513e41 | -15.19683 | -43.78403 | 2025-10-28 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24dd93b4-849c-3b6f-9855-2dc8c378f928 | -10.58183 | -49.79161 | 2025-10-28 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| c5378e42-3086-3314-859b-742ae47a67b5 | -9.56218 | -46.96693 | 2025-10-28 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 038639bc-4ad4-3e00-b55c-19aba7317a69 | -10.62931 | -42.31701 | 2025-10-28 04:44:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 8a126f9a-9f94-31ae-b44d-a31fb0fbf97a | -8.56108 | -47.02099 | 2025-10-28 04:44:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 824ca7a6-bd40-3ef5-8a0f-342f2440993c | -10.5308 | -49.54707 | 2025-10-28 04:44:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb281a1b-c4dd-3905-946e-0e25e0ad67b1 | -9.13592 | -50.70026 | 2025-10-28 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2417a51b-5afd-36b0-82a3-38c8fd80ae7f | -13.74722 | -48.40471 | 2025-10-28 04:44:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a4a569e-f787-3ae4-99f2-9cec6d4c4e1d | -9.5877 | -47.85284 | 2025-10-28 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fc95d340-863c-3f0c-9ca5-c11b8dc3032a | -14.31489 | -46.51785 | 2025-10-28 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 7ede62d6-3f40-3f12-a64b-dc9784ff66c5 | -14.64296 | -48.40445 | 2025-10-28 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cf0b88b-5b63-39d0-be23-66a3ecc0522e | -9.79806 | -48.38694 | 2025-10-28 04:44:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7ab4437-eeef-36a0-a28a-1a3f42044143 | -13.55982 | -47.16019 | 2025-10-28 04:44:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README66.md)
