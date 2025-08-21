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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8118610-ecc2-34ec-a416-c3f76a7c433e | -13.01373 | -45.1782 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d365a3de-c489-3d0a-840d-33cac0368871 | -5.53806 | -45.5466 | 2025-08-21 04:17:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3319adfb-f56b-37da-a1db-f72942c7e7f6 | -5.87477 | -50.14678 | 2025-08-21 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d31dd20-4175-3f75-890c-b248aa97be33 | -6.01731 | -44.44881 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5e0eb1e-ba99-370e-a923-3c7a79789f4a | -5.46348 | -46.47158 | 2025-08-21 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 605a4220-0bb9-35eb-af31-6bed852637fe | -7.95183 | -42.63997 | 2025-08-21 04:17:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1e8e5975-f98c-338a-852c-fd99b9e75805 | -7.64826 | -46.25734 | 2025-08-21 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a183e2f9-a23a-34e6-9140-905722673597 | -6.02381 | -44.38638 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fb1d403-7edd-3ebc-b1b2-8c8087b80bf7 | -7.48881 | -44.94139 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b161854-8d7b-38eb-a0b8-2f72c85d7f19 | -10.72482 | -48.24193 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f8a7500-c3c1-31aa-a60e-016590baa795 | -13.02546 | -45.16915 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| dec490a0-2102-3afd-ada5-51b3ba0c57de | -6.0733 | -44.38272 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a2cc070-d035-3e54-99fc-081c6e04a052 | -11.02511 | -44.59654 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4b8751e-037a-3697-93fa-d7e8403edcf0 | -12.97909 | -45.20177 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9040cd3b-3610-345b-bc2f-6d03940441c3 | -6.21871 | -44.13277 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 904513a6-3a43-3dbd-8404-ba1991bf6574 | -6.95165 | -42.86503 | 2025-08-21 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9da3fd0b-d203-3e69-b22a-2cfb846c805f | -12.9807 | -45.21307 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3b853b91-4a37-3aee-8ff4-638816b75f35 | -6.49478 | -43.10212 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a364aa0-6e06-364a-8741-fe45ecfee661 | -6.55218 | -42.99743 | 2025-08-21 04:17:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a4933d0-a17d-3840-9cbd-1b6c254174dc | -6.02407 | -42.82877 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 319f166d-aa38-3f5d-92d4-cf9eaae55eb2 | -11.81719 | -50.65223 | 2025-08-21 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ae29b52-bffb-3de4-8023-50850d250bbb | -6.27295 | -43.70963 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cec15931-35cd-328b-aab5-0f2f98e8b2f5 | -9.48922 | -47.32777 | 2025-08-21 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6cd4275-56f0-38cb-bd6d-0b6027519564 | -11.30012 | -44.92911 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e64661e-92a2-31e3-b159-de19c7720ce4 | -12.66678 | -44.95999 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 969518b2-bac7-3c7a-aa4f-1c1148786d6b | -7.02593 | -44.60807 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a935f79-6160-37f0-9c45-ffa9f71d5d17 | -12.22198 | -45.40539 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d58d382-6108-32fd-923e-bf4926c37130 | -10.99439 | -45.62701 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 298061bf-efcc-34ed-a8ed-936650983d64 | -6.38918 | -44.72148 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92c10daa-c4c5-38e2-a05a-877ec6270263 | -5.68131 | -43.86168 | 2025-08-21 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2dc297f-3efb-3500-9080-f47e5dee5114 | -6.96829 | -44.1642 | 2025-08-21 04:17:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc5d5de-374b-3b6e-9255-9c2626f32ff0 | -11.29563 | -44.93568 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cf27b0d-635e-377f-8929-2d2866b4dcfa | -5.87352 | -48.11669 | 2025-08-21 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a3f4b56-1dcc-3439-9066-aaa6266808f8 | -12.21803 | -45.40845 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c0ff7ec-4994-330b-a0e9-b9268e15b0b6 | -12.0819 | -47.91201 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af92b391-f445-36a3-b41c-8d38006960b0 | -12.67011 | -44.96054 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 968b0121-da5e-39dd-8d86-3045315da4a5 | -5.96555 | -44.13686 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53d8ef53-d0a4-3205-87f9-061a7775a4c0 | -11.28782 | -46.28317 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 96ac47af-3eee-3359-9f29-272488addb00 | -8.84426 | -52.0407 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d98ae921-b6b4-33cc-ab77-2c140be79250 | -12.63792 | -46.87126 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf016d48-036a-3d36-91ef-1e731c3ee2f4 | -6.28993 | -43.88206 | 2025-08-21 04:17:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 32e658bc-8cdb-3422-93f6-44df0ae11f86 | -11.81055 | -44.25773 | 2025-08-21 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0d41501-57c0-3e88-a636-33cb8bedbcf3 | -5.40684 | -46.22352 | 2025-08-21 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e6c0d6a-8f25-35f0-9713-c8e89a07e705 | -6.27737 | -43.72479 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb4396c5-11ad-3743-9290-2da9975f1954 | -12.64209 | -46.86789 | 2025-08-21 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ba4c7279-0253-344a-b7ae-278d01caabd6 | -8.82602 | -47.47339 | 2025-08-21 04:17:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 718bdbe3-7f6c-3f9b-91a3-2a9c907db0ed | -5.99637 | -42.81021 | 2025-08-21 04:17:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7eede1a-776a-3055-94de-73263aaf352e | -12.2072 | -45.43265 | 2025-08-21 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2420d78-7bbf-3174-921f-3aaf1ad3f7ba | -6.02671 | -44.36822 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 095caf8b-43aa-310c-b7b6-73945232e864 | -9.55433 | -48.11753 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| efbbc053-602f-3aee-86e9-7b182f3d534d | -6.20348 | -43.57246 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0fe140f-5356-356d-b02d-ecf31687d914 | -6.10898 | -44.37725 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70a5315c-7427-3a51-bced-e33660884969 | -5.78837 | -45.06668 | 2025-08-21 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60971b0b-ea60-3fc6-b70e-4d34148bd028 | -6.1084 | -44.38086 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 403b8ccc-350a-36d7-a634-2a3b8a32cc57 | -6.93188 | -41.73345 | 2025-08-21 04:17:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d5d5f6c7-e30c-3a75-ba25-7977d12a9070 | -6.42594 | -44.6671 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d9f9913-0a52-3123-b1ae-d2b540d23eaa | -9.47732 | -47.33027 | 2025-08-21 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 925b44f7-aeb2-3dfe-ac57-bfd72944491f | -6.72396 | -43.98422 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38adbcf1-8121-36cf-832e-29818b46e45b | -5.98586 | -42.81211 | 2025-08-21 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd1f0458-19d9-3fda-b990-311d249700ce | -7.02581 | -44.63032 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 8da35e77-7e5f-3d34-8bf0-9c443cefdd77 | -10.97533 | -45.65804 | 2025-08-21 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8267b9e5-f3ad-358c-880b-0dd06ade0d53 | -5.77813 | -43.60925 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 067087ae-16f2-3e9c-896c-68210aab3b4d | -11.17878 | -44.52748 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b91e78ee-3135-3b02-b5e1-9e2f16baf83d | -5.9588 | -44.13577 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f2a86d74-8292-3827-8830-423935fc3bc9 | -6.58387 | -44.46372 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2470676-0933-3fd3-bcec-c4dcb2fc1377 | -9.91447 | -49.24633 | 2025-08-21 04:17:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db7f0dc2-c467-39aa-a073-becb888ba7ea | -5.81961 | -51.68877 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fc5a1ee-e496-3de1-bf62-cb1226249e1d | -8.84329 | -52.04607 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ef20c08-c450-38c6-8d19-a3bb55dbd075 | -10.71821 | -48.24895 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ce69b2f-4f74-3dec-9340-958a2918acbc | -5.78481 | -43.61031 | 2025-08-21 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab1935c0-73b2-3ea7-afb5-10e22f697591 | -10.59501 | -52.2855 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba59fcd9-41de-3db6-a300-9fc9b2f94462 | -10.70309 | -48.2212 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bfc3e55e-072d-3012-ae75-964c7ba67b55 | -10.72778 | -48.24768 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27db139f-d6ff-36b8-9924-a8caf3d581d1 | -7.86111 | -46.72797 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 67157100-1f70-3f1d-b3b4-2a8b9885922b | -6.72787 | -43.98123 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f54c8dc9-24e2-3ba4-999e-38dec296b032 | -6.5629 | -44.48614 | 2025-08-21 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e96c2412-8281-308a-8344-ba6a7e949cc8 | -8.16525 | -47.33183 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4721c09d-eab4-385b-a554-8d8e3ce1573b | -6.08782 | -44.42222 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5dd41a7-2a2c-3393-affe-2fce90e708cc | -7.09673 | -43.51101 | 2025-08-21 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94279e31-318a-348e-89c8-35e3a5105bff | -12.97575 | -45.20122 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61280ccf-2be0-3a22-86fe-c362e49827f3 | -10.71001 | -48.22709 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a6ed0d96-02c9-3023-b256-88ab6b40f0f8 | -8.02888 | -47.68162 | 2025-08-21 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03d65aea-e145-3950-aa42-087d371ebb66 | -10.72007 | -48.24638 | 2025-08-21 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77906cf9-fcc3-3c17-99fb-d08771b5cf67 | -7.26187 | -43.6842 | 2025-08-21 04:17:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c4bb089-b284-321e-a6a2-fef02d655326 | -6.02779 | -44.38327 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b30deec-da54-3d0e-9a68-d1c6656d9a82 | -6.63173 | -43.90364 | 2025-08-21 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b286074-ee35-3e82-b31c-55f12d23f48d | -6.07373 | -44.1171 | 2025-08-21 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c0050ad-7c38-3ba8-9414-e31c0705d688 | -6.26182 | -43.72183 | 2025-08-21 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56bd7504-7b8f-3061-9755-bf3545302f59 | -7.86478 | -46.72859 | 2025-08-21 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdddf048-cee1-3e6f-bde9-508d4475b522 | -6.25878 | -52.81824 | 2025-08-21 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 210ca4d3-2199-3288-a90d-3c2a7b8cd3eb | -13.01936 | -45.16446 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 7934d612-1817-321b-b7f1-c2ab1a1f5545 | -6.08383 | -44.42534 | 2025-08-21 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4384236d-0506-3c58-a2f5-941f147d4e6c | -12.08485 | -47.91716 | 2025-08-21 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9805a9b2-7086-37cd-b6d2-8311b130dcc4 | -11.29449 | -44.94276 | 2025-08-21 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e3bca79-ebee-3d3a-acf8-15018cfcd8a6 | -7.49162 | -44.94566 | 2025-08-21 04:17:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f444fa61-71b6-3686-a80b-670a62260df3 | -12.98127 | -45.20949 | 2025-08-21 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4c515b2b-5597-38f3-ac77-4b8226760855 | -6.32134 | -43.74973 | 2025-08-21 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 043d1bfd-f75a-3f41-81bd-caedbc7d1362 | -9.7236 | -45.62004 | 2025-08-21 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37e21cb9-bf85-3d2a-9bf5-3a138006c6bf | -9.55457 | -48.1157 | 2025-08-21 04:17:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12a3d194-b654-3d1b-98d7-57587b4cdf6e | -7.0174 | -44.61776 | 2025-08-21 04:17:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |


[Clique aqui para ver as próximas entradas](README27.md)
