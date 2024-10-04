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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc749cdc-17d2-3fee-ae1b-a985e76c69ec | -8.1951 | -43.6703 | 2024-10-04 12:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 11a3748e-f66d-3569-87f3-8112c5eaf090 | -8.1759 | -43.6957 | 2024-10-04 12:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| eba9cae5-78c8-3ca3-9f7e-e348e5b2c29e | -8.1762 | -43.6723 | 2024-10-04 12:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 83.3 |
| fc6e3947-d172-3434-8c68-86c5a7f45b56 | -8.1948 | -43.6936 | 2024-10-04 12:55:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 209.7 |
| f803fac7-5843-3b3d-bc8a-1aa08bdaa924 | -8.1241 | -44.8101 | 2024-10-04 12:55:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| bf48ca37-7e5e-388b-8256-cbf25b3800cb | -8.3194 | -42.8343 | 2024-10-04 12:55:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 60.3 |
| 7ed7e345-ee67-3919-b253-87a3db139306 | -8.4535 | -47.1181 | 2024-10-04 12:55:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 18925778-a457-34f9-834c-bf605733a7d8 | -9.1041 | -50.902 | 2024-10-04 12:55:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 419.0 |
| e9ea25a0-d299-3ca9-9edc-ec26b3258313 | -9.0853 | -50.9036 | 2024-10-04 12:55:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d98a7d92-8d26-3636-9f66-aeb2f45e9670 | -9.1039 | -50.9231 | 2024-10-04 12:55:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 183.1 |
| ef7074a7-4d4f-3ea8-ac68-10c556821cd2 | -9.9822 | -42.0976 | 2024-10-04 12:56:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 111.3 |
| d8dfbebf-dc2e-3bd7-b3b1-cacca5eb6126 | -9.8855 | -47.2124 | 2024-10-04 12:56:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 002a6396-ccc1-3e34-8248-c45187984cb1 | -10.2761 | -47.6995 | 2024-10-04 12:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 47249cff-d700-3669-908f-d5e59424b874 | -10.2571 | -47.7017 | 2024-10-04 12:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 165.5 |
| ca9a2527-04c3-3b6b-ae53-2c97266a45cd | -10.2378 | -47.726 | 2024-10-04 12:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 6adb914b-8b7c-316d-8b79-5645ff76c1bb | -10.2381 | -47.7038 | 2024-10-04 12:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 3f0139fc-3b94-3073-9342-4b07d650fc2c | -10.7352 | -46.1918 | 2024-10-04 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| e4d68c21-ecb2-31a9-a176-aba054f9b9f3 | -10.8661 | -46.3331 | 2024-10-04 12:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 5cf82328-a094-31c5-9a08-ec6479326ce9 | -10.8018 | -45.5927 | 2024-10-04 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| e2d5b989-8045-3f88-8eb8-70391e827ac0 | -10.7309 | -47.7126 | 2024-10-04 12:56:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 2f6d884d-b4f6-330b-8304-6b5203e62dfc | -10.8021 | -45.5698 | 2024-10-04 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 61518f58-f8bf-3dd4-aaf1-04145748c771 | -10.847 | -46.3356 | 2024-10-04 12:56:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 152.9 |
| e97423a0-9c7d-3fd3-8bc7-34b476f59ce0 | -10.7355 | -46.1692 | 2024-10-04 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 329.8 |
| 896cc1bc-e163-3ba3-8480-7a7ac044c7c5 | -10.7115 | -47.737 | 2024-10-04 12:56:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 3f62887c-3290-3d88-8a0a-f6a5b86d1a33 | -10.7359 | -46.1465 | 2024-10-04 12:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 281.4 |
| be313ef0-eaa5-3500-a975-2f6a6249e1a5 | -10.7118 | -47.7149 | 2024-10-04 12:56:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 451e5455-f85d-3fdf-adc4-16dbc10c3172 | -11.0345 | -46.5143 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 264.9 |
| a781fcb1-1a6a-3184-b3d9-444c4159d97e | -11.0349 | -46.4917 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 282.3 |
| a3b3f688-1f75-392a-910a-ace2478eb000 | -10.8992 | -46.6442 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| b3e2b636-85b9-3653-93d0-7beaa204da90 | -11.0536 | -46.5118 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 436.9 |
| 04061c13-6309-3ddc-b524-d1eab6ed9f49 | -10.8996 | -46.6216 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 32f38ac2-935d-3213-8205-18ca6c212c3c | -10.9374 | -46.6393 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 42d138cd-e187-36d0-a814-3b6739794526 | -10.9187 | -46.6192 | 2024-10-04 12:56:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| ceee72ed-9993-3a45-8256-12a79e314cde | -11.2779 | -43.4118 | 2024-10-04 12:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.1 |
| e85d4552-2f59-3eab-bf21-1fbe054a2f44 | -11.2971 | -43.4088 | 2024-10-04 12:56:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 193.2 |
| 1d87c7b1-8045-3199-9017-4139dcf2fc08 | -11.1108 | -46.5044 | 2024-10-04 12:56:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.9 |
| 5bf50889-3c11-3644-a234-167f62422105 | -11.1384 | -45.9804 | 2024-10-04 12:56:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 9df38986-d42d-3263-b69e-f627d79af8ab | -11.9296 | -50.1425 | 2024-10-04 12:56:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| d1f06dcb-56a2-3a48-b0ec-900f25d15649 | -12.7815 | -50.5758 | 2024-10-04 12:56:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 6386bb1b-6ae7-3776-9407-216239c82c3c | -13.1595 | -48.6322 | 2024-10-04 12:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| ff38098f-a7d6-3ab1-864a-696cb0e2af74 | -13.0786 | -51.1385 | 2024-10-04 12:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 1f794e03-bfa3-3334-9098-c54cee381cda | -13.1163 | -51.1765 | 2024-10-04 12:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.3 |
| cc8e1867-7827-32f8-b5ed-14e3b947b0d2 | -13.1779 | -48.6737 | 2024-10-04 12:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 959e8cd2-8d90-3874-8ebd-961a464fc4cc | -13.0594 | -51.1409 | 2024-10-04 12:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 12ad7ad7-0a9d-3a9b-aaf8-fb5c17d69144 | -13.1791 | -48.6073 | 2024-10-04 12:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 6b06c140-0653-3e7b-967a-ecf914c8d81f | -13.1787 | -48.6295 | 2024-10-04 12:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 33ee2c4a-6937-3fb1-969c-01446013c6f3 | -13.1447 | -46.3033 | 2024-10-04 12:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 5955aaaa-d97b-30f0-986a-893648c40990 | -13.1443 | -46.3261 | 2024-10-04 12:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 155.6 |
| 04e11b76-93a8-3f19-be23-96f7d1836866 | -14.0382 | -45.1414 | 2024-10-04 12:56:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 2d00c1f5-961d-3bf0-9749-5f8b77315cd3 | -15.6304 | -47.2063 | 2024-10-04 12:56:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 86234b81-5801-304b-b9fa-2e998721ca0c | -16.6133 | -57.176 | 2024-10-04 12:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.6 |
| eeb32979-95d2-3f38-9640-8be5e03084bb | -16.9296 | -47.1455 | 2024-10-04 12:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4cf35a8d-fbfe-315f-b062-2950d52e82eb | -16.9302 | -47.1224 | 2024-10-04 12:56:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 69.6 |
| bfe890de-39c6-30e0-8274-52b078d74626 | -16.6127 | -57.217 | 2024-10-04 12:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.0 |
| b0337fb9-5dc6-3919-8a86-90a18ddc7b8b | -19.1134 | -48.2833 | 2024-10-04 12:56:52 | GOES-16 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 4a375567-f775-31bd-9f10-6e6c674ddd8c | -19.6122 | -46.2632 | 2024-10-04 12:56:54 | GOES-16 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 74859356-c5b9-3e24-8dd9-e49f2b25d150 | -10.75 | -46.17 | 2024-10-04 13:04:22 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7b04d27-99a8-3e92-bef8-d702c801b61f | -10.25 | -47.73 | 2024-10-04 13:04:28 | MSG-03 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07cedac6-df70-3ce5-970a-c19ec0746dce | -9.11 | -50.89 | 2024-10-04 13:04:33 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179a48ca-5b4f-3bd2-a891-c06503596711 | -9.09 | -50.88 | 2024-10-04 13:04:33 | MSG-03 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f06e453d-48b5-352a-8a98-f433bfd2b32c | -5.71 | -43.81 | 2024-10-04 13:04:54 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b32792e7-dece-3e62-bc58-0abe84605f6b | -3.29 | -50.43 | 2024-10-04 13:05:10 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9255308-f7a7-3d10-88f3-9a2b363e59f2 | -7.3136 | -44.9343 | 2024-10-04 13:05:47 | GOES-16 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8079bf19-92c8-39eb-93e6-59586db6e838 | -7.6675 | -45.2201 | 2024-10-04 13:05:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 4e7adeee-1714-322c-85ed-1c0004d9d961 | -7.6484 | -45.2446 | 2024-10-04 13:05:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 1bcfac4b-3096-3229-8115-b92c1215995d | -8.1951 | -43.6703 | 2024-10-04 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 16ea751c-5759-3493-825b-604b64f382be | -8.1948 | -43.6936 | 2024-10-04 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 3d3c426d-c065-39c4-ada4-e73f5f39081a | -8.1759 | -43.6957 | 2024-10-04 13:05:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| d017a740-e0a7-3d5a-952a-598e024b366b | -8.3194 | -42.8343 | 2024-10-04 13:05:53 | GOES-16 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 77.6 |
| 5114cfd8-b805-3910-a8d0-18c5c0eca1d2 | -8.4535 | -47.1181 | 2024-10-04 13:05:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| a18af9fc-47c6-3888-93ac-63b255be9051 | -8.4347 | -47.1199 | 2024-10-04 13:05:54 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 55c80148-5c4d-3308-a072-9f0d010a375b | -8.8362 | -45.1688 | 2024-10-04 13:05:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a7d069b6-57b4-361b-869f-87c416ec7458 | -9.1041 | -50.902 | 2024-10-04 13:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 976.7 |
| 23ec9a80-57ed-3add-a847-e1ee5e11fd4f | -9.1039 | -50.9231 | 2024-10-04 13:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 330.0 |
| 06ce8ff0-3759-32e0-a3aa-50a0b41ad4c2 | -9.0853 | -50.9036 | 2024-10-04 13:05:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| defd7fdd-dcd0-3a00-879c-8fd571644a88 | -9.8855 | -47.2124 | 2024-10-04 13:06:02 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 5f3659b2-bcf2-3eda-94b9-085bbe161eb3 | -9.9822 | -42.0976 | 2024-10-04 13:06:02 | GOES-16 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 112.0 |
| ab09071a-8340-3d26-853a-721b9d0caa81 | -10.2381 | -47.7038 | 2024-10-04 13:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| cee94340-ac7a-31e4-9a9b-01f2757eef76 | -10.2378 | -47.726 | 2024-10-04 13:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 91e107a1-5fba-3350-a91e-db86050fd2ce | -10.2571 | -47.7017 | 2024-10-04 13:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 343.7 |
| 9be9097f-0ffe-339a-906e-f6ed4052120e | -10.2761 | -47.6995 | 2024-10-04 13:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 257.6 |
| 246adfbe-d54f-337a-bf7a-333e03680368 | -10.7118 | -47.7149 | 2024-10-04 13:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 12e80a90-9787-39f4-addf-1a88e27a2c16 | -10.7115 | -47.737 | 2024-10-04 13:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 775b5c92-ee5d-32fb-bf64-1de4e3f3a737 | -10.8021 | -45.5698 | 2024-10-04 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 270.1 |
| 708148b1-5acf-346c-b33d-6c812f0dee84 | -10.7309 | -47.7126 | 2024-10-04 13:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 94737744-22ee-3852-b9b3-eab76e8799e6 | -10.8018 | -45.5927 | 2024-10-04 13:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 8cd84c12-0cef-3a12-895e-040ad76b3416 | -10.8661 | -46.3331 | 2024-10-04 13:06:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 0e14fc88-fabe-33c7-a5b7-59e28a6c1eb2 | -11.0349 | -46.4917 | 2024-10-04 13:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| b392056a-4148-3cfc-99c6-b858e525f47d | -11.0345 | -46.5143 | 2024-10-04 13:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 141.2 |
| f82d88a4-f659-38aa-8a63-41220a35104a | -11.0536 | -46.5118 | 2024-10-04 13:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 253.4 |
| 0d284574-4acb-3dd7-845c-10e6293f6609 | -11.2369 | -46.9597 | 2024-10-04 13:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 276.8 |
| ac6ce4e1-2573-36cf-8f04-6b8b7d6b5b96 | -11.1384 | -45.9804 | 2024-10-04 13:06:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 347.5 |
| 19221fab-7524-3c5a-9b2d-7cf3307b9b87 | -11.1108 | -46.5044 | 2024-10-04 13:06:09 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 873831b6-ed1d-3cca-a5f3-fd1f070f6f2f | -11.2971 | -43.4088 | 2024-10-04 13:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 165f107f-e012-3f95-8f43-51f62396fd9f | -11.275 | -46.9548 | 2024-10-04 13:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| d3a95567-5623-3536-8159-d65017d236bc | -11.3536 | -50.5304 | 2024-10-04 13:06:10 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| cb84e41c-4b36-3ecf-af1d-751353074ccf | -11.9296 | -50.1425 | 2024-10-04 13:06:14 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1ecf2a6e-28ac-380c-8664-a407c210ebaa | -12.7966 | -47.4398 | 2024-10-04 13:06:18 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 53e9dfb7-b093-3723-a1ab-467d3079f1b6 | -12.7815 | -50.5758 | 2024-10-04 13:06:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 8458c262-537d-344c-af67-878a676e4d18 | -13.1779 | -48.6737 | 2024-10-04 13:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 109.9 |


[Clique aqui para ver as próximas entradas](README191.md)
