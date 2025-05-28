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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| baf88c6c-cfff-37ff-bb60-c89ab5d1df06 | -9.04424 | -47.01552 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 989ad54b-a5b4-3b14-839e-2887f781a08a | -11.76537 | -47.26247 | 2025-05-28 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac040292-349a-3f3e-be79-c7084cf41204 | -7.66876 | -46.10294 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 49c2ee11-0f05-3c88-868c-9c62188dc29f | -9.89778 | -44.80494 | 2025-05-28 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb599428-c883-3ad4-b2aa-b30adb8d83d9 | -10.22873 | -47.42574 | 2025-05-28 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c3c9b4f-1547-38e3-ade4-33ff9122614e | -11.81574 | -46.1383 | 2025-05-28 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53038197-d591-3aed-9695-28676361af86 | -9.54006 | -44.07402 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f7b7f44-38ba-30d6-956c-53060d83cac1 | -8.14538 | -46.48595 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74030336-a5ba-37e6-90ad-5fbceabaa256 | -10.22482 | -47.42883 | 2025-05-28 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9be4d556-5969-3dd1-8bf7-b2effab22ffa | -11.132 | -54.21867 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e2ef8c1-cc44-34ea-a03b-79968377ea64 | -9.39124 | -48.42519 | 2025-05-28 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6f472f8-19d1-3fc1-ad72-d565420b77fd | -7.46949 | -47.0573 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7621e9d1-8a9c-3c64-852d-3fe95e83d6e1 | -9.67877 | -49.71466 | 2025-05-28 04:32:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce4a8a98-87a1-37f9-ad5c-1dcf5a8a2def | -11.13433 | -53.91829 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90776cb8-fdb3-3e05-8392-3d71367570b3 | -9.51213 | -47.69407 | 2025-05-28 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15cfb3a9-22b3-3c9f-96ef-f3d03f94c9b6 | -7.67277 | -46.0997 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 07c04bca-8f0b-30b1-91e2-a6a10d3191e8 | -6.834 | -43.41254 | 2025-05-28 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5fdac61a-466f-37b3-ad4a-b42aef609162 | -8.00691 | -46.15786 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24c3d858-3e19-3c3a-a4fb-46346a0bf223 | -9.22583 | -50.62639 | 2025-05-28 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c473940-5c0d-38c0-82ed-447b14fd747e | -7.56413 | -43.34555 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9c33c41-3718-360d-b6f2-983c32d7443a | -11.81248 | -55.07143 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c82dbd3f-2503-3efe-b7a2-c3ad9b8b1c33 | -7.08155 | -46.04995 | 2025-05-28 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8164ca73-ba2b-3f36-a73a-c2d8bbac045e | -10.45417 | -47.94388 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fef5eae6-f31a-3840-829f-31557505ec52 | -11.81986 | -44.27157 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| a0a5464c-f4ab-3591-b99f-d8e0044fa22d | -11.56938 | -47.44566 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d446e14-5d97-39b4-a981-7f6e2a3d115c | -13.08149 | -45.27327 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbb24b55-7135-304a-8342-47e9e414b3ef | -10.66629 | -49.44526 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f49bff03-454c-3cbb-b385-79dd5cb939f3 | -7.20382 | -43.54136 | 2025-05-28 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5b28e7d2-33e4-399f-8b0e-d3bfa735df0c | -7.60887 | -43.39904 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eb5e3e29-3b45-3195-9cd0-b99943050318 | -11.97375 | -52.46735 | 2025-05-28 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed0ae35a-ac81-38bb-8a59-c1d8eed285dd | -7.95951 | -45.9367 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56419fc7-1722-3776-aaac-7c5be1f4854e | -9.15602 | -49.64815 | 2025-05-28 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f524a6e-8305-3f3b-918d-8ef154db6a2e | -10.24024 | -52.22798 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 670bb6ca-aa34-3058-ab54-e2bde6080537 | -8.09517 | -46.28834 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 826cc731-7361-3c30-a0fd-24e754ca42e5 | -11.81174 | -55.07552 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 010eafaf-85cf-393a-810a-dbde2fe18916 | -11.91241 | -54.41497 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 360a23c9-c53b-3537-93fe-76f58800aea8 | -9.97391 | -48.67183 | 2025-05-28 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cee9e56-e125-3e8a-a2f9-89638078734f | -7.62664 | -45.76316 | 2025-05-28 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7cf8e8ca-41e7-3a0f-98eb-7cdb6b756693 | -7.55943 | -43.35014 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fa169bf-e43b-3e91-893e-22677b9d85e8 | -8.72711 | -47.98378 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06786b95-e068-3687-b47e-f1394a938eff | -10.65633 | -49.44363 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 925d94c4-96e0-362c-a1be-8ca5bc4bee71 | -8.01851 | -43.18725 | 2025-05-28 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 681e5551-7b0a-3d2e-aae1-b54f78c4cf0f | -9.03322 | -47.74148 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ede5fe7-73b1-33cb-a670-12b97fbe6e51 | -8.84631 | -49.83433 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c5a0359-aecc-3016-a611-2e16e4acb275 | -6.2146 | -48.47426 | 2025-05-28 04:32:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83e7dbff-91b3-385d-a482-bdeaad9c3b49 | -12.26894 | -44.60186 | 2025-05-28 04:32:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84487709-79cd-3a57-a350-bde9e3970e35 | -9.609 | -49.02522 | 2025-05-28 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 152a5ab8-e3fa-306a-8dc3-676d817c3b7c | -11.97447 | -52.46307 | 2025-05-28 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb6cbe1c-7627-365c-996c-8ade7bd93798 | -10.45696 | -47.94795 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4ac58af-8d7e-36bf-aab5-bbcf2e942b30 | -10.5406 | -59.22412 | 2025-05-28 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a2fe869-5710-33f2-902c-194aa423726a | -11.81517 | -44.27614 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 6ba8d9fc-0ebe-3010-8e8d-11e8b6bc85df | -9.02767 | -47.7334 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c83bd2ba-d509-3500-b621-119caf99b41c | -7.67219 | -46.10346 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| f40dfb7d-ce31-361f-9dbf-9b865e77def9 | -11.40003 | -52.94665 | 2025-05-28 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713a653c-29fd-3a6f-a31d-f397af789e1d | -9.03822 | -47.75307 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b0533df0-8f95-3752-8211-a8ade5f3930d | -10.72075 | -45.0439 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 607f2d67-f770-331a-8588-f419db652186 | -8.0071 | -46.15376 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef16abd3-430b-38b5-bf8a-c73163effd0c | -8.74321 | -49.74715 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da807520-8287-3bdf-9397-bd7db6b48fde | -8.00653 | -46.15758 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74781629-af5c-397c-9a58-d63b8cc102d0 | -12.40978 | -49.99259 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b84d4d7-8f94-35f0-8383-9b06966003e8 | -10.23951 | -52.23232 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cb702752-1770-318a-baa2-4f9cacb84569 | -11.97666 | -52.47229 | 2025-05-28 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5016c13d-572e-3441-94af-922b4d19a235 | -12.11458 | -54.66806 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c369da9-48b2-3eb3-b5ec-8443df90ee84 | -9.04154 | -47.7536 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4979a29a-dc06-3ab4-b03f-769b632c53a7 | -6.75013 | -44.63162 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2ced6bf-aad4-3e78-b454-b8a22590eb71 | -11.10905 | -44.62851 | 2025-05-28 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c859f907-c023-30df-80fd-982877e0145e | -10.06571 | -48.28204 | 2025-05-28 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63bba39e-44fe-3f1c-94f1-97a6de2fa373 | -8.01771 | -43.18409 | 2025-05-28 04:32:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7b7576f9-4890-3c65-a00f-b09eabf66f4f | -12.41196 | -50.00027 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59624f07-9ee8-3636-abc5-87f9a9c9fecb | -11.81444 | -44.28128 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c16308ed-3789-3940-9fcb-40c7252691a2 | -10.66961 | -49.44581 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b6328f2-3c8f-331f-b8c5-ad81335badeb | -8.78832 | -47.93987 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fc2c8fd-c3b6-3aaf-83b6-751bbba0a76e | -10.73582 | -49.2869 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b74e73d2-e039-3773-b5c9-44f996c60128 | -11.80748 | -55.07479 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 696563ab-a046-31e0-926d-7cefa39ea69d | -9.03599 | -47.74552 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0e6c5df-0161-3c0b-9703-6d39295eeb4d | -11.29623 | -54.01586 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf25402b-cae9-3059-83c5-15b5e28b36d3 | -10.1468 | -52.13762 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d40dd246-071c-32d8-9e92-45d60de6e3cc | -8.0952 | -46.28951 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aae34da-bb0a-34d4-a1ea-b7026dc8f2f7 | -7.6808 | -46.09325 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 81f6eba9-cdb6-33ac-929e-cf3a5f27f7a7 | -8.00063 | -46.15296 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| af274896-4075-3a66-9892-53a30adb2aae | -10.95277 | -48.14548 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d95ae525-97e3-320c-8e5b-3c3903a065ea | -13.09285 | -45.27494 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55f5bc57-0614-30a9-8795-f8a5341078b1 | -10.54097 | -59.22818 | 2025-05-28 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00df8d9e-0f43-36c5-b88b-d7c5c3837715 | -9.39807 | -48.426 | 2025-05-28 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91ea52f2-e1e8-345f-8d69-17f30882e954 | -10.73526 | -49.29041 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2fe9c15-5d2c-31ff-96cf-a920baffa4b4 | -11.1411 | -53.9267 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d35a937-79f8-3121-83ec-a8b18d04f030 | -7.60541 | -46.64672 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 93711222-b1bd-39ed-ab35-1dffe548f1be | -13.08082 | -45.27797 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f932504-6bff-397f-805b-c7aec91c1757 | -12.11113 | -54.6635 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4cb257f3-6adb-308c-8dc1-e57a92d66e8e | -10.54177 | -59.22415 | 2025-05-28 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c538754-58d5-37ad-be80-d59096ac85ce | -11.13648 | -53.92955 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 121c2c5c-0390-3cac-88a7-6aafb6fedaf5 | -12.28867 | -43.54606 | 2025-05-28 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4386614a-1da5-3422-b845-ed601d67a8f1 | -7.21413 | -43.11517 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 415de615-7645-3c5b-a1db-5edbbccc6ead | -8.35954 | -48.0325 | 2025-05-28 04:32:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5b66d2a-8069-387f-a5b3-78b22fdc3327 | -11.13137 | -54.22232 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54efd670-76f0-39f1-84de-0f5ca873fc51 | -10.4575 | -47.94441 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 15838b47-bd26-39d1-b71a-d917f4d931cc | -11.29797 | -54.01283 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38eb866f-8f16-3607-a280-fb5a3bae2b17 | -9.18226 | -40.31146 | 2025-05-28 04:32:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f8f2ca17-dbd8-3750-b705-8d73c44064b5 | -12.27215 | -44.60736 | 2025-05-28 04:32:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7aae3a46-5f9a-3329-8e95-dfd08eeb9cb5 | -7.56469 | -43.34851 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
