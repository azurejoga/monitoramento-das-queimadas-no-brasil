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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0865c10-c3f0-3d01-ada8-7bf6a699013f | -12.52866 | -57.17954 | 2025-06-01 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16f4817e-9bff-3703-84ed-c8af55951dd5 | -11.45193 | -55.00676 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6a732fe-ad7d-381f-b247-3a785dbaab82 | -13.10221 | -45.26912 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc9b98ce-018b-38b2-bb2f-b2541461dfb1 | -11.14245 | -53.94569 | 2025-06-01 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e808668e-8447-348f-813c-cc118076d2c3 | -12.12505 | -54.59824 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c17ea308-de7c-352b-bbf5-2003ebeefc33 | -11.90137 | -54.78976 | 2025-06-01 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5571fd38-0063-38cb-9e8a-abb81ed1e157 | -14.68951 | -45.09004 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e407536-b29e-310a-a7c6-8a040b658633 | -17.96625 | -45.38111 | 2025-06-01 04:10:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b32f355-272f-3b03-8b04-8cd50db67d06 | -14.68427 | -52.68446 | 2025-06-01 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c97b0a1d-91e6-39e7-a24f-0c84a9e724f2 | -14.66993 | -45.12489 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 994fa9d0-e1c0-3880-a7f7-426c1ef698db | -14.0251 | -55.13229 | 2025-06-01 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eddb6b4-fad9-3910-aded-e3e787a99057 | -14.69599 | -45.11406 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe54e95-e75d-3305-b16c-77637075321c | -12.5294 | -57.19453 | 2025-06-01 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7685d7d9-92b7-3e74-8c64-80c16cd1fbe4 | -12.02219 | -49.52118 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfcdfb60-853d-3ab9-b017-245a5796d0fb | -12.12601 | -54.59339 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 17c327e8-7afc-31cb-b731-7be541686a8d | -15.0595 | -43.86816 | 2025-06-01 04:10:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d21cd2c-5e4e-305d-8eec-a643dcef321b | -16.02784 | -43.67931 | 2025-06-01 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5856ec6e-6a9c-3897-a7f2-b438e74c9775 | -14.6966 | -45.11035 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf47e3f6-edba-3aa0-8e47-5edc25971f10 | -11.07887 | -54.78265 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49d69413-0254-3e40-9d08-f8414cfbce1a | -13.0975 | -45.27621 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97cc52de-76e5-3a66-96c6-4a012d1aa9dd | -14.14039 | -47.9005 | 2025-06-01 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b2ffb25-a6e8-3bf6-abf4-bb695f0f68b8 | -13.09063 | -45.27504 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1adf3979-d06b-323f-9ef0-24c07844a392 | -12.08294 | -54.58511 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7ca5504-326d-3497-b042-8848c619e7ed | -12.01776 | -49.52036 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75f0ba73-43cb-36ca-843b-037d10e1e8af | -12.12411 | -54.60025 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 54740705-93a7-30b0-9afb-49b75fc42f26 | -11.14336 | -53.94107 | 2025-06-01 04:10:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36f5e17e-cf1c-3075-a8d3-d7cd41f73ebb | -14.03024 | -55.13831 | 2025-06-01 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3db36511-ec85-303e-8027-110ec220a40a | -14.45902 | -48.45606 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d10bd3c-931a-3880-a944-1e3fc201e19d | -14.6843 | -52.68665 | 2025-06-01 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 276d3bb8-5de3-3cfc-ac64-c272fe4eac4f | -14.65078 | -45.41155 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99b1395-3f06-3bc6-92a4-ce2fa505141b | -13.10529 | -52.28703 | 2025-06-01 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c95e77-2720-38de-9768-6445449871d1 | -12.01769 | -49.52678 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f0c29e3c-fa85-353b-9a52-078bdb671296 | -11.91331 | -54.41715 | 2025-06-01 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1d2aede-c496-35ed-ac8c-7f06b8ce3a77 | -13.09598 | -45.26411 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8afa387-695d-3e13-bf6a-b9d5f78ad750 | -12.01695 | -49.52476 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f470bcb-cf50-3b57-9565-84818b48173f | -11.83318 | -51.27383 | 2025-06-01 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab7c8770-14aa-3b0f-aa59-d7d019ad3a85 | -11.42085 | -55.09464 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 10af91de-2866-3d26-b4a2-19c1be954c5e | -17.1111 | -49.1401 | 2025-06-01 04:10:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8faf8ef9-b365-389b-88c4-47541752d264 | -14.69107 | -45.10175 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbf95383-5460-3d85-8c87-6ed421e6c566 | -14.6779 | -45.11861 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e68b745-a94a-3f82-a937-cb69d98604f0 | -13.71606 | -45.25794 | 2025-06-01 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a7ae5a7-85ff-3b20-adaf-94d63e4ec178 | -12.08395 | -54.5801 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 833e2860-62cb-3335-bdda-c97a6e12f246 | -15.56934 | -47.85435 | 2025-06-01 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbe44dae-84b2-359f-90b2-66ad0a6adb80 | -14.65419 | -45.41214 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa437243-f7ca-341b-a8e0-681d718687ba | -14.67392 | -45.12176 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c6bffeb-d7de-3821-91a4-47a7cbf0aa02 | -12.01847 | -49.52236 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b90ca8ea-a4c3-3297-b3cc-b11fac977d4b | -12.01613 | -49.52918 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 526f3575-3a54-3b94-9e4f-530cce3419bf | -12.72235 | -54.96957 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0bfecd56-1980-3f51-8648-d185b382395f | -12.53249 | -57.18049 | 2025-06-01 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e315e14-64be-3da7-8135-04ba7c3d1791 | -11.44555 | -55.00554 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe503b4b-27ed-3d6b-90a7-ae291ca8bece | -11.45087 | -55.01201 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f76dab8-b550-3af0-afcb-da8fb2818931 | -13.37376 | -41.49187 | 2025-06-01 04:10:00 | NOAA-21 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92efec84-8420-3bf0-a406-4248b67d9b36 | -13.63587 | -52.18357 | 2025-06-01 04:10:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78123afd-e504-30a3-8f38-407e785d9c44 | -11.07458 | -54.77124 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccf78afb-ce2f-31f0-a42a-0ca1b2cfe518 | -12.15637 | -48.68584 | 2025-06-01 04:10:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dc67872-fb15-3dc0-b57b-f4285ef01b93 | -11.83374 | -51.27089 | 2025-06-01 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e374b193-15c3-3f71-93ef-515572f63a1f | -18.20634 | -48.15385 | 2025-06-01 04:10:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bfc12c4-72da-33bf-b970-7162a5f83332 | -15.08053 | -48.94546 | 2025-06-01 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 004041e6-d5b8-3ded-9a13-e97fd008a676 | -18.65883 | -47.35277 | 2025-06-01 04:10:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca9eeb84-2de1-31ae-b016-4b851909eee7 | -14.69167 | -45.09802 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c111d26-d03a-315f-84c9-ddc5be60d62e | -12.02139 | -49.52557 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b800444-212b-3996-b08e-90e8634453ed | -16.6802 | -43.88311 | 2025-06-01 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 460e74f2-47dc-368c-96ce-ae42f5e71a1f | -13.10006 | -52.28602 | 2025-06-01 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abb473a4-729c-3b15-a38e-81d94a8a0150 | -18.38821 | -44.33716 | 2025-06-01 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a78a9166-b27c-314c-b28f-e20300df13a8 | -12.52715 | -57.18661 | 2025-06-01 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0fbcfc7-ff38-3dc6-9232-4d85574b4724 | -14.03124 | -55.13353 | 2025-06-01 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb665261-f234-3ec4-ad32-cb03ccba69cc | -11.82816 | -51.27297 | 2025-06-01 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4cc380-4ab0-39ce-9255-9b038b6378e3 | -13.10564 | -45.26971 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eff55228-c32d-3801-b5d4-87d18da6c242 | -14.69625 | -45.09121 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b3e613d-b1bd-31d8-9222-df1879860cd1 | -14.69383 | -45.10606 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 189c4e02-bce9-3355-83af-d9774c7af243 | -14.12053 | -41.67662 | 2025-06-01 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17635e37-4c21-3a6c-9546-e09165ac7295 | -14.69288 | -45.09063 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3b5dfc7c-c68e-38a3-882b-e10dc27aeb40 | -14.08108 | -47.68053 | 2025-06-01 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae86bf65-e6be-33eb-8810-5b658e9dc942 | -11.44448 | -55.01083 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31279c0a-f956-31f0-979b-49cb3597d38e | -13.53584 | -46.73045 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 764ac833-6bed-3e9c-b4eb-751606323eb9 | -13.10971 | -45.26648 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba9a0ec4-d3b1-3dab-a4a9-43cb0ed8525f | -13.105 | -45.27355 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f966c2f6-a8bb-3ddc-a3d8-c14852a4c105 | -14.01995 | -55.12632 | 2025-06-01 04:10:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e1d41ab-10eb-327e-92f7-d0a85a0e027f | -13.95344 | -54.49086 | 2025-06-01 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6db3b56-9181-34a1-ba9f-cefa7c844e87 | -15.06224 | -43.87226 | 2025-06-01 04:10:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed9ed614-92dc-3c75-8fd4-b2d92011a094 | -12.71637 | -54.97689 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f6ebc54f-17d8-37be-95d8-7c01e6ac116d | -13.09471 | -45.27178 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f15a6f0f-a877-3529-840e-5dbfafaba4e8 | -14.68365 | -52.68768 | 2025-06-01 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db64a88b-2371-322d-b3e5-0cf7c196e936 | -11.0799 | -54.7775 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09d42623-0348-33a7-a7ef-99109c854cef | -13.10907 | -45.27032 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2479121-33a3-3a65-8605-cc9a4ceccf3b | -19.55187 | -45.66383 | 2025-06-01 04:10:00 | NOAA-21 | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d11701aa-71bb-305f-8097-eae5bc781d94 | -12.02663 | -49.522 | 2025-06-01 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52cd65b5-74d3-36bb-8688-c48c319ed850 | -14.68365 | -52.68986 | 2025-06-01 04:10:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b96d9d12-c76e-3585-a1b6-c728dfb4f536 | -13.09814 | -45.27237 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ccb24e3b-25e1-356e-ab75-e65eea0e0578 | -13.09878 | -45.26853 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b9c37ae-4db3-3eef-8114-770bacf63f6b | -14.67054 | -45.12117 | 2025-06-01 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 524f95b7-bb31-3f9b-81d7-b45fde9a4bc9 | -12.52567 | -57.19352 | 2025-06-01 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 095ea345-2e04-3762-be00-e6c9fcc67639 | -11.91938 | -54.41846 | 2025-06-01 04:10:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e99a1431-4a26-32c7-8cc1-242861668264 | -16.03114 | -43.67986 | 2025-06-01 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec482af4-cefc-3a12-a191-c3344de77c95 | -13.10157 | -45.27296 | 2025-06-01 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fca9ed7-67c6-36be-a932-353076338bc1 | -14.83006 | -48.09294 | 2025-06-01 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01c69cc3-9ad5-3533-920f-be0703de11a7 | -11.08092 | -54.77238 | 2025-06-01 04:10:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8240d25b-72ed-34c7-863d-8c1cccfdf0cc | -12.72031 | -54.97943 | 2025-06-01 04:10:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9ecdd140-2ae1-335d-b7b3-d8542b182a19 | -11.43169 | -55.00853 | 2025-06-01 04:10:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bce7ae8-9973-37f7-99da-4e5b0d1a4f06 | -19.97091 | -44.21794 | 2025-06-01 04:10:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README6.md)
