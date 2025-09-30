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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9552072-c089-31fc-ad3e-e395104e9d57 | -9.41357 | -54.68466 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81f30246-6ce3-3a1f-ad64-6d07ef3e8ca3 | -9.30746 | -54.5112 | 2025-09-30 05:08:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f387dea7-a705-3a73-aa8d-c1d6ee33dd0b | -6.5196 | -45.22596 | 2025-09-30 05:08:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f909af6a-027f-3ada-869c-435b8ab94f0d | -11.30079 | -53.95615 | 2025-09-30 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68209b13-3bd9-39ea-be29-dda3c3f0cdbf | -11.03014 | -49.81618 | 2025-09-30 05:08:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93976fe7-154c-30dc-99a5-ebb8f845118f | -10.40766 | -48.16492 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f14b1ff-6583-3c85-bdfc-7de3578264d2 | -7.78743 | -55.03036 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba715c9f-892c-30ee-978a-f1a77b61cad1 | -6.94873 | -45.39444 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab5a1586-6c50-3c22-ad35-edda0c18d13a | -10.39481 | -47.805 | 2025-09-30 05:08:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2412eb61-21cd-342c-9f93-f7c3b429f384 | -11.26273 | -47.22696 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9850c879-7823-3c3c-8a44-fdd193d4393c | -12.84323 | -47.01925 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e0f0ca9-1889-3c85-953f-ec23ff89a4be | -13.15307 | -47.42019 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7353c74-3a67-3073-bb90-f5fda3494e82 | -8.99023 | -51.74226 | 2025-09-30 05:08:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe984c8-2621-3708-b1e5-2a1366df9a8e | -10.9551 | -46.49743 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c560a4a8-275e-30d1-bc37-bc6de839eea9 | -10.95184 | -46.47577 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aff5516-cdf5-3310-9a2a-9a1858df26b6 | -10.99944 | -57.05086 | 2025-09-30 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fff06814-8363-3267-b1cb-edbc6007c545 | -10.39807 | -48.14252 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58d325e3-5757-3cfa-9421-479840669deb | -9.37934 | -48.95554 | 2025-09-30 05:08:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b44c2b8-fb32-3928-b194-0ca8c35ac673 | -13.21307 | -47.32272 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae9a7f22-872b-312d-bdc7-5321a65e4466 | -7.04136 | -46.41851 | 2025-09-30 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c4cd481-d338-3c9b-9be2-4a13c63cc228 | -8.436 | -46.94376 | 2025-09-30 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6aa6f2ec-5b37-3fdf-ba34-6d66f4f3c2df | -10.75414 | -45.38269 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a67a288-678d-3aca-b978-55eb8e5a20ef | -10.76157 | -45.37301 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2c962972-2f98-32e9-b790-d4828307e5c7 | -13.5716 | -48.05751 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ef78b96-5568-37d5-a1c7-8b1576783fb4 | -10.1892 | -44.90292 | 2025-09-30 05:08:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f821a902-1b4e-3414-9ed3-36a870bcb68f | -7.82542 | -46.99798 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a1e17ba-6670-3716-90be-2ecf83b25636 | -13.57246 | -48.0956 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e18dec61-7d88-3020-af65-ebaf31495b27 | -13.64071 | -47.33521 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 359b79e2-4d56-31c4-ace4-ad2a7e468fde | -8.86434 | -46.67398 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6cc3eaea-9b7b-3f97-9062-c07dcba4fd6e | -13.23736 | -47.31149 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a9410d0-8376-36dc-8ae8-c820552b3b53 | -10.76098 | -45.37801 | 2025-09-30 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| af168f0a-3bef-3cbe-afb4-798d4b23abbc | -13.57118 | -48.06098 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 744613ed-815d-3e65-9383-e24ce57586e0 | -13.23714 | -48.45081 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab18b884-6d5b-3303-9834-c61da863a115 | -13.09508 | -47.03362 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0ba473b-4085-3621-afa3-84105c2a07cf | -11.74685 | -46.85386 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfe6632d-af03-3ec3-b76f-45c0139d27d7 | -10.66861 | -53.70737 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c652404a-c29b-31a5-8136-a4e99d58bf58 | -7.65278 | -49.56774 | 2025-09-30 05:08:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e15975ce-e263-316d-9340-c96a18d614b5 | -7.81559 | -46.98983 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19e4211f-9180-3e06-a163-82d5bcc8079b | -12.85329 | -46.98388 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7de7d02-01cf-3fd7-b7cf-f43da0ed9aab | -6.94227 | -45.39798 | 2025-09-30 05:08:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec2f6bcd-3193-318c-b5b0-7e9a221cc836 | -9.03887 | -46.70396 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4249bbb2-53de-3c20-a9f1-c58531823022 | -11.60645 | -54.65307 | 2025-09-30 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f8811d2-bc20-314d-b5ee-840d7def8b27 | -7.86464 | -47.25465 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09107557-c56f-3558-8afe-6127fa871b27 | -7.8344 | -47.01244 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ead6b827-c19e-3ed5-9539-112106d4a8c8 | -13.366 | -47.31683 | 2025-09-30 05:08:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e7556e4-5213-3f7e-8158-28f39df86e85 | -11.9236 | -51.5388 | 2025-09-30 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca16675e-356c-32ad-b9e0-1b57834963ca | -7.84311 | -47.26464 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8a44308-9e9d-3690-841b-2cd4cad5f40e | -11.03115 | -54.26684 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16bfb981-df8c-3b3e-b4bb-582de441eb0f | -12.7611 | -46.87392 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da73b860-5059-3e40-9f91-b07c20fa072d | -9.41818 | -54.7235 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c4af37f-81e0-3f4b-8169-db3d068012c3 | -9.96462 | -48.79734 | 2025-09-30 05:08:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b412dc4-9585-3f3a-b14a-d35eadd1c127 | -7.51966 | -46.68955 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d6f2285-9818-3fa9-af8b-3a6c7b3f75de | -11.26179 | -47.23426 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c85bcc2f-c93d-3103-82df-97d254b53ca4 | -13.60155 | -43.46446 | 2025-09-30 05:08:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5030d5e6-2da9-3816-a914-b5aed1e09c7d | -6.47621 | -44.21888 | 2025-09-30 05:08:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67e8b4fc-1fb9-3faa-951c-e12f748bf5e6 | -12.84853 | -46.87627 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfd0d264-9da1-30f6-b25c-51a2b0867805 | -8.00355 | -47.05234 | 2025-09-30 05:08:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2037505b-585b-38b2-a589-00e22e4910aa | -12.87343 | -46.96214 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d6cbef26-c6c0-3746-b43f-45eca24c1ba8 | -12.75176 | -46.85374 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4da6eae0-3b64-3e75-8fbf-67ceb9cf9a9f | -13.66899 | -44.30964 | 2025-09-30 05:08:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 03b2070e-521a-3b03-92e7-2d122bbf937c | -9.32133 | -50.63057 | 2025-09-30 05:08:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16ca7b77-48ad-3919-a244-9a2b5f177077 | -13.36146 | -47.81166 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3a16792-cc87-3615-b03e-14f696c0fa10 | -12.84901 | -47.01959 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5fcb91e-6380-3829-aec2-6c7b5cd775ca | -10.10474 | -47.7889 | 2025-09-30 05:08:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| daa91eea-036c-34b4-9c65-e9e72f939baf | -11.93987 | -43.92277 | 2025-09-30 05:08:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a9a2b00-c4f3-344c-8ad3-d606f3b5345c | -10.08655 | -50.21413 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 07430711-11de-3a7f-b33a-f90186d9a5be | -7.91834 | -48.17949 | 2025-09-30 05:08:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0ffb7265-8ac9-3b80-8002-1e8971859dbd | -12.85711 | -47.00065 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d9f50de6-73f7-3c82-b058-899fad10027d | -11.65312 | -47.49455 | 2025-09-30 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0971abe-65fc-393d-8ecb-7c6acdd21648 | -10.04 | -50.18956 | 2025-09-30 05:08:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9fb6631-92f7-3e15-89a6-bcc815289062 | -7.86423 | -47.25774 | 2025-09-30 05:08:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07f55e14-ed70-32b3-985c-8f49fcb77cf9 | -8.25366 | -45.54876 | 2025-09-30 05:08:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5d57187-9046-32d3-b476-ea8aa204de0b | -6.36679 | -45.6471 | 2025-09-30 05:08:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22b0e30c-ee3e-35c0-80d8-f23a51cbeed4 | -11.75351 | -46.84664 | 2025-09-30 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5108ad12-c883-35bb-9399-c3f8a12d1443 | -8.83438 | -50.66711 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bbd1fc8-830c-3bff-896e-93c6228dd968 | -11.20322 | -47.74851 | 2025-09-30 05:08:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4272aa2-a146-3338-ba96-7d659394fbee | -11.64113 | -54.54165 | 2025-09-30 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e5a7c9-8008-34b6-85c1-b0bf6241f623 | -10.96043 | -46.5019 | 2025-09-30 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 9e4c6ad2-3358-33f6-b414-0ccdb7c92d42 | -8.02122 | -55.41203 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f0e697c-04ad-3f18-b685-2524d3f5ed5d | -11.25623 | -47.23371 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0bdc071-5970-375a-9dbb-000c903022a3 | -8.86387 | -46.67746 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58516439-683a-3987-abb6-5d2e98bb1523 | -9.41416 | -54.70383 | 2025-09-30 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 908f1dfc-abc2-3cbe-9c06-bb9bbc6ed6af | -13.40347 | -47.55267 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 455bd8b9-7b8e-3d48-935f-9a4ebe7f3519 | -10.87778 | -49.40251 | 2025-09-30 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f76462a9-178c-3cce-8f3b-8b7cfb7fb5c6 | -13.59644 | -48.03417 | 2025-09-30 05:08:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5fbcc6e-58de-31d1-91e1-ab074bc49a58 | -9.935 | -47.46346 | 2025-09-30 05:08:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d2a9cb7-bba0-34cc-9f76-da7746513c43 | -8.71334 | -47.9834 | 2025-09-30 05:08:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d73a886e-929d-3e95-a28b-48a28953af65 | -12.79388 | -46.89408 | 2025-09-30 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3aba75b6-28cd-3b85-a0b0-a4232d473ebf | -8.87529 | -46.6344 | 2025-09-30 05:08:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad9a1f4c-75a6-3bf3-8883-9a52c6845c16 | -10.38527 | -48.1599 | 2025-09-30 05:08:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1647c763-9138-33a7-a253-4a0fd36ee0de | -11.88951 | -48.04939 | 2025-09-30 05:08:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ef670ad-8f95-3006-9263-2899a4b6e1f8 | -11.42057 | -44.89803 | 2025-09-30 05:08:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a341480-6a34-3743-839f-32938dee680f | -10.65314 | -48.58837 | 2025-09-30 05:08:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80718e95-9a6f-37c3-916d-41ce148cccb4 | -9.12793 | -47.6439 | 2025-09-30 05:08:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51de632c-06e5-395a-bc4e-9571c3e83424 | -11.14984 | -54.12382 | 2025-09-30 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 9e391359-46ae-3e1f-bfd5-b7a258f2dda9 | -9.4635 | -45.48589 | 2025-09-30 05:08:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f96928a-68a9-3597-9850-5a48df486e80 | -7.04685 | -46.41946 | 2025-09-30 05:08:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6cb2822-59db-3a95-871b-402b9d3c1669 | -11.19491 | -47.22886 | 2025-09-30 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 3ca92946-3c9a-391a-8013-6b9a32ad0d29 | -10.83672 | -47.96543 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b1424cf-2399-3019-9079-29db3b5e9241 | -10.83591 | -47.97165 | 2025-09-30 05:08:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README94.md)
