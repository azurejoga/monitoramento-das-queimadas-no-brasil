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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7fd7195-7dc1-3dc8-b93b-1bbbe2e4eda7 | -15.21633 | -48.17598 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d01ae0c1-318d-3dc4-bf87-fc6576d5e27f | -12.77194 | -50.55918 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 18eec5dd-c541-3eff-aa32-83432071d5a1 | -15.49049 | -45.91573 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 680526f9-e9a7-37d6-834f-f6f92ccf13e8 | -11.82389 | -44.98328 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48346e03-bb55-3e0d-831a-dfc172b67269 | -14.72879 | -48.14571 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18001108-76f2-3f37-b255-395df3ff5179 | -16.08595 | -51.03686 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c201559a-eaf5-3467-a5c5-43400ac67ced | -9.5844 | -54.59077 | 2025-10-01 04:51:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4989b7a4-92a2-3b6f-a0a7-2709df03827d | -11.04998 | -47.82867 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 222ae459-fde5-34d4-9c99-f8d5c7a7589e | -13.91516 | -48.09373 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea81ea61-bdd9-3737-87af-4bd19e7950e1 | -10.90385 | -46.55442 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fdeb606b-c51a-3060-9eee-cb89b0bdb95c | -15.76358 | -43.68118 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5e785432-2318-3d16-b012-6c63d01eddca | -14.6112 | -48.30497 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb8f065d-390e-31a9-8854-d9f82aa5af35 | -11.46167 | -45.01373 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13d2a0f7-2786-3066-aa8b-02aff17f1a88 | -15.41974 | -47.0541 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19befa20-10e1-353d-8093-90aad4c6c888 | -15.75648 | -43.69469 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 094bb897-1aa6-36ce-9e53-619b595855af | -11.76134 | -46.87192 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 176cd124-0c91-321b-9a69-660879c48911 | -13.36154 | -48.10497 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dfee77c-42e9-3948-8c7f-5b48d42f7275 | -14.35188 | -45.90014 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d7a56b42-d436-3d2a-beb1-4f6ac264307b | -8.986 | -50.20114 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0f8497d-e752-3327-a93b-64775235da50 | -14.71538 | -48.15476 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b5c4132-d258-381e-bc66-d24026d3a207 | -14.61044 | -48.31044 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57c0835f-b768-33f4-a514-7aec1879e0b2 | -10.83108 | -45.38613 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9d8818ef-73ea-3789-9568-8692af3e9944 | -10.9369 | -46.50316 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fd4bbe78-3dab-3d5a-b89e-57e39e9ae9a2 | -10.90692 | -46.56272 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c859af2c-9d15-39ae-8571-746ce1677d41 | -10.90809 | -44.78802 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a39e87d1-8708-364d-9cc3-520b0d969d14 | -14.54239 | -48.23112 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb80b2ae-ca39-3b11-9821-5eca2ec214bc | -15.33569 | -46.26787 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3e7de93-5781-3fd6-bb52-c50ba5201de2 | -10.62683 | -48.59786 | 2025-10-01 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f8910a5c-25bd-36fa-bfaf-674af8c7973e | -14.51838 | -48.37315 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ce0d4fcb-7503-30f8-b391-53e25d87910d | -12.87112 | -46.9449 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59f5d5de-e648-36b6-9052-eaa5123f3f2c | -13.37479 | -47.30661 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57dee0c1-022a-3b35-b72a-43926e3d7a6e | -12.24035 | -47.81346 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6d09bcb-f2fe-3440-a076-154dd1a3fbda | -15.16753 | -49.10377 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fadbe294-bac1-30a7-a081-7c29968e25a5 | -10.90164 | -46.56985 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5b0695a7-eed2-303b-a20e-51995c98c8b2 | -10.84702 | -45.41101 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64234b55-0666-3cc4-a7a2-0580b429268c | -9.79321 | -45.93636 | 2025-10-01 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13bea17a-2d88-3112-958a-c3c56341d1ba | -10.90928 | -46.51627 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 006f467b-9e09-35f1-9bab-987918a506b3 | -15.77742 | -50.16024 | 2025-10-01 04:51:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c4a7603-2a69-3a34-81e1-43d9ae1e5051 | -16.12612 | -49.14568 | 2025-10-01 04:51:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1639b98-ecb3-319c-bda9-c0e3d263e4bc | -10.19961 | -44.89652 | 2025-10-01 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 995ea47b-1ba8-302b-963c-eb569e1d5b03 | -14.39283 | -54.91346 | 2025-10-01 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 132c3a09-a9ed-3e41-baf6-0c087e4cc4f3 | -15.41002 | -45.65349 | 2025-10-01 04:51:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d96d9b8b-35d9-3084-a119-7a4a86438b66 | -11.94718 | -43.91555 | 2025-10-01 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 200d2aba-98f3-3c9a-831a-d3fdab8f7094 | -14.76384 | -48.0979 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ee632a4-67b3-30d4-8f0b-24b1454d2ae8 | -13.23882 | -47.3294 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77aac880-bc1f-39a9-9410-add7b7419ef7 | -14.67854 | -48.12715 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f33b6e86-f43c-3b02-9938-ade6a743ae67 | -12.70639 | -46.89872 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d2543da7-6a96-3b58-8ffb-c3f67c501270 | -13.24504 | -47.31475 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8c315049-4d76-31e9-9d55-81f837b1c693 | -12.7604 | -46.91001 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72891b70-c56a-30a7-ac74-35e0175d1c09 | -13.82499 | -47.50554 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2b345695-e372-3264-b030-29d5471b47c0 | -13.1532 | -47.40665 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5ab99c6-1685-3ae2-b4bc-27f6f1829392 | -10.4507 | -48.08618 | 2025-10-01 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5736e833-3cec-3d42-b8bf-1a32f6452fef | -13.15735 | -42.35489 | 2025-10-01 04:51:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c24292ca-efdd-36b4-8c72-35ea7630cd14 | -15.52617 | -47.86518 | 2025-10-01 04:51:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30088eb7-c758-3eb7-be12-c08926d9a706 | -15.36063 | -46.11179 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed2e2239-377c-3089-92c2-7517c77ce52e | -13.10412 | -47.02652 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f04645ad-7673-34bb-b637-6b2efa6f45a4 | -9.44709 | -45.47837 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc90422a-73eb-3ef4-abc0-242e968a6724 | -9.44651 | -45.4809 | 2025-10-01 04:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 996259c2-5bc3-3206-9355-f7430d0529a3 | -15.43991 | -43.64928 | 2025-10-01 04:51:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c64f8cfa-6ac6-3651-b4ce-e8705627b762 | -15.13216 | -46.45258 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45c20e34-0861-3eb5-b5f5-204cf34fe17f | -15.32683 | -47.36698 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cdfe4311-0311-3c00-bd3d-8e42a62b2301 | -14.66014 | -48.12758 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4329fc7-d0c4-32db-954c-b05c1cb107d6 | -15.99615 | -51.18711 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 748597a9-dd78-38a4-bc5c-d89f5c1ecab0 | -13.28554 | -47.22007 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc1bdd8b-400c-3749-8f18-e8d6c3da9ef1 | -12.85177 | -47.02345 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 198644eb-6a7d-33be-a453-4f038b67035c | -9.57143 | -50.94695 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2950b7f-7d6d-3928-b3f0-051225a3d8b3 | -15.76234 | -43.7382 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c87433d-3d43-3bf1-9311-c33321034878 | -11.50383 | -43.51202 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d820ca6-0097-335a-a51e-fb21de670e91 | -10.19301 | -52.55998 | 2025-10-01 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 694e0623-3d71-3c57-aa5f-e0160c3dbcbe | -12.36912 | -50.20042 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9eb15fad-0b7a-3812-9fd1-60df26341db6 | -15.75106 | -43.69398 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2853e26e-eb8b-3a44-b716-0877a2d0d3ac | -16.40928 | -47.05632 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 460ee46c-a2ed-3376-9992-236b70444d67 | -12.91011 | -46.8183 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd4cf91e-6396-3e19-9da3-97a69c885bb7 | -14.89603 | -48.13658 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 818ae5bc-455f-3404-b65d-cfb946d1bf3a | -15.17397 | -49.0857 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a5b8d798-91d9-345d-8a2c-52c08ea1eb9c | -13.98169 | -44.91273 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfe9c49a-6314-3b5b-9387-985390bf5a19 | -13.34414 | -48.14326 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 990195d3-a946-344c-9ac2-7f6a9a8d1a08 | -13.78214 | -48.0274 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41300021-e813-3adc-8f77-ee5926f02254 | -12.87794 | -46.76995 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 020feed5-016f-3b03-a511-f8e389e2230c | -12.83091 | -47.02065 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e810db9e-2f87-30f3-a244-48647491277b | -14.72475 | -48.14555 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7c5d0c6-a44d-3747-9746-cc4992219631 | -16.08716 | -51.0288 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26fa5d37-aba8-38ac-9943-9fcd74716b97 | -16.40154 | -47.04851 | 2025-10-01 04:51:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16183045-bd5b-3542-a55f-c1526908fa81 | -11.764 | -46.8525 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 5e25a2dd-ce6f-3173-9abc-ca7fceb87e81 | -15.17843 | -49.07875 | 2025-10-01 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 516494d2-48a9-3b1b-868b-eab70d6f0e1c | -11.60614 | -45.05027 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1f871520-9990-3ad7-95fb-da31895c58b1 | -10.41852 | -51.645 | 2025-10-01 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7f9035-5031-3c9c-a231-f6014ca4ea73 | -15.2788 | -47.89273 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5b47195-2605-3476-824e-bdc06d77d82e | -15.4974 | -45.91873 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| de9f0896-40fa-36c3-a00e-49490899c448 | -12.06279 | -47.05367 | 2025-10-01 04:51:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 583a0e01-8c82-3c0d-8274-e1131657bc5a | -15.13931 | -48.01253 | 2025-10-01 04:51:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b71b486-4080-3a83-a72d-de59fd4ff19f | -15.2952 | -46.40283 | 2025-10-01 04:51:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac3ede5c-020b-39f1-a16d-570b6a57011d | -13.25494 | -48.44113 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bebdfae2-e19d-3b64-abce-b9fc736e0ff1 | -11.46929 | -45.10038 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b71743b1-1da3-3a74-9971-5b9b2bda4a47 | -12.43423 | -50.17767 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04c759a3-17ec-32c2-b309-abf44937e08b | -9.92794 | -43.68551 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c4abb53-70af-3900-94d5-8e84cab13dd5 | -15.24181 | -49.72167 | 2025-10-01 04:51:00 | NPP-375D | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31dcfd6d-1dad-3e60-9a79-a2e4234fb94a | -13.32806 | -47.34118 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a094de4a-62cc-315f-88e7-af8e1402b629 | -14.88653 | -48.32727 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87282408-9b2a-360f-9a6b-70eb40845ead | -12.80552 | -46.89275 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README93.md)
