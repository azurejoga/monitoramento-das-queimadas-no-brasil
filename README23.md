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
| cc8eb45b-d129-3c0b-baf2-4d2309d65b93 | -7.81773 | -44.44665 | 2025-11-04 04:31:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 298416de-b866-3071-b404-161418fcc562 | -4.78494 | -43.18682 | 2025-11-04 04:31:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 403b91db-0e40-3e96-9ddb-48a3ef5ef6db | -3.51806 | -51.58911 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 02c3cf45-5589-3a5d-9aaf-481413088df1 | -2.30804 | -48.59935 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 63c9cdfc-e9e2-3747-80f7-177c01133d53 | -4.42548 | -48.91436 | 2025-11-04 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb05649b-174b-37eb-810d-75794ccf8201 | -3.49226 | -50.4621 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| d7778a60-da10-3c70-81b2-2d1962833973 | -6.36656 | -46.12291 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dae7b061-3d7b-3053-b81b-9c6d90d8ac6e | -3.4316 | -42.54139 | 2025-11-04 04:31:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9e756a9a-889a-32d1-9516-a450b5ae2e2b | -3.45812 | -52.8747 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09d4758f-10a3-33ff-9de2-b825c92b3d4b | -5.51434 | -46.23653 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3304b38-c570-313e-9725-ee98b4c95c29 | -5.57839 | -43.79282 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8028163-f4e5-3b26-a557-9790d102a9bf | -2.62215 | -49.22663 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84da9b4b-4c9d-3374-9b0d-ebaddc25073a | -3.04284 | -50.27267 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 503cd93a-c8f0-3742-bc32-749219ef886a | -6.40331 | -43.06451 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1bf0a2ff-6c8c-3e38-9603-6a7927bfd2a9 | -5.5082 | -41.11192 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b64cc175-800f-34f9-a888-45383f687ae2 | -8.10676 | -43.82209 | 2025-11-04 04:31:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a2d9f5a0-f88e-3825-a167-66859ce92f0a | -2.31374 | -48.58532 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c82ca030-c99d-3a11-aa48-62fe8235e515 | -5.32222 | -45.37855 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2035aa61-73a8-38cf-bed2-eaa73866d493 | -5.23415 | -44.20784 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd5bbf2b-68b3-3c39-a368-e0c69ebd5c69 | -7.85234 | -44.21355 | 2025-11-04 04:31:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1ef7b70-438e-397d-b8c2-cdae8aec570c | -2.87546 | -45.29564 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e724bfa-34e1-33da-9362-b2107fef41c3 | -3.01686 | -48.04814 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de624cff-582c-3a24-9ffa-a1a6af489a6d | -11.11725 | -41.09364 | 2025-11-04 04:31:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d45b40a7-6e17-3af6-908d-3f508b291853 | -5.93029 | -41.29779 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f7f9d0b1-a695-3be6-b46d-bf46235bb4b9 | -2.86811 | -45.29823 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 00cbbf42-9a69-3898-a84f-ad37e101e04a | -4.30878 | -41.45597 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3af6b9db-fe5a-39f0-98d0-afde11fd122e | -4.46832 | -43.23259 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d7c479da-8867-3c76-8816-e55087cd0aac | -3.59172 | -49.4375 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30794f43-95b4-3b4e-9c6d-cb4adf298c5c | -2.37143 | -47.72468 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6312163b-1bb0-3b37-8365-8d27e815dbf6 | -2.9869 | -44.96175 | 2025-11-04 04:31:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b70dbcd9-586e-36e9-b6d3-14b5495e81b9 | -3.44848 | -51.47235 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4be523aa-d44f-32c7-9105-a91ce8634c65 | -5.23714 | -44.21267 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 961ef4d0-d95f-327a-b5dd-c7e4f7a3a326 | -3.04515 | -50.28159 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f170e08-e8a6-3869-8ca2-143b3fe0e19f | -3.52279 | -55.42842 | 2025-11-04 04:31:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8deda5a-ef8b-3d34-9c71-5f618ef24a79 | -2.8402 | -49.83503 | 2025-11-04 04:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aaec120-a6a9-36e0-b852-298edcf683fb | -7.52939 | -47.29396 | 2025-11-04 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62d13245-5246-35a4-bc28-98a9332c892c | -3.40712 | -50.18086 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf39b117-7be9-332e-b6e2-029277aacf52 | -4.6215 | -46.40717 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607ef310-0912-3af6-a2c5-88a151588862 | -3.38758 | -54.28093 | 2025-11-04 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09b7715e-837c-30d4-8eeb-7a7a5bdf95d4 | -3.49296 | -50.45781 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c8475f52-d151-3345-a6d2-1688038a19c1 | -4.59227 | -45.65671 | 2025-11-04 04:31:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76fd6a0e-bcd2-3a50-b05b-09ca567efc77 | -5.50448 | -44.99565 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acb12030-a94c-3dee-b380-4318554ae1f6 | -3.04086 | -50.28518 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae4fbdb8-4d4e-3264-9868-e1049e35c3fc | -2.61808 | -49.22989 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1b44a60f-cffd-36cb-8ec4-b1e303581ead | -3.91656 | -54.52272 | 2025-11-04 04:31:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d08f0f24-d781-3b86-918a-397f739fc23d | -4.96143 | -44.90486 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d56b0ad-51b9-3524-900b-531a001c4a4a | -7.23725 | -45.06764 | 2025-11-04 04:31:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc206357-8157-3e21-99bf-333a8375f80b | -2.31995 | -48.59003 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d4c52bd-7082-3ebd-be32-45cf94542887 | -4.95151 | -44.89937 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de4c5792-744a-3e8d-bc16-06f98216868b | -3.01414 | -51.09069 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5b28650e-6bfc-3186-9449-8cc1fd984982 | -4.64639 | -46.29222 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3607ac07-5391-3710-b68d-30257573c58c | -5.36925 | -45.07563 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bc6253d-3630-3c03-9a0c-f791bc6b3596 | -6.60723 | -43.6132 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5133c54-d6f0-3bd2-9741-0ba3591b69f8 | -5.83019 | -44.6652 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cef9d40e-92a9-3768-8d7f-e33164d4bf65 | -2.72045 | -48.34929 | 2025-11-04 04:31:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6ea9e686-eaa7-32cd-9d97-dde80bc144a5 | -2.25746 | -53.92279 | 2025-11-04 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c95e38d-c943-3491-9f60-dba6e10039c6 | -3.87565 | -51.95676 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0257f0e-917c-3306-b833-2b4b91ae7c97 | -2.84375 | -49.8356 | 2025-11-04 04:31:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c75ba8a6-bc51-365a-bb0a-adb612e6a0a9 | -3.5279 | -51.65091 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43f44f71-ec4e-3d78-bf7a-c82d4c4cf5db | -3.1484 | -49.42448 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4008224-34c1-3e9d-9f76-c785dd0cd7f2 | -3.8378 | -53.40086 | 2025-11-04 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7addc98-4d31-3a10-b1a6-e9d3256e1d76 | -5.98429 | -41.92208 | 2025-11-04 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9f5df10-7d09-3232-93fc-eae8de4aa32b | -3.44142 | -53.25931 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0e13105-7335-3de4-bdaa-c381f10fc8fd | -6.84368 | -46.30369 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 492a34a0-cdac-3806-a6f9-e964b94369c4 | -9.94621 | -44.82495 | 2025-11-04 04:31:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11e177ff-cdc2-35f4-82c6-757d5dc30c80 | -3.60127 | -50.6227 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5dee45c-3537-3f25-9b7f-d4c80f61935a | -3.14405 | -50.20196 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 002b3249-ed83-322b-b94e-0ff91876ab87 | -3.34849 | -50.23579 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b44c7f6-1276-331c-9282-c53435579623 | -3.19081 | -44.37479 | 2025-11-04 04:31:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d431eaa4-2ee4-345e-aba9-05170df0c74a | -2.55926 | -48.93968 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fbae652f-f797-3423-b122-0e17526fcaac | -6.61107 | -43.61372 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 694fbd86-9c4d-3f5d-877f-13ac82bbe531 | -5.1582 | -45.12796 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83163215-59f8-3b8f-b475-1788ebe9ee78 | -5.89262 | -42.91684 | 2025-11-04 04:31:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2c4754d0-ee7e-3852-abe0-e53f6593eda5 | -3.98585 | -47.07821 | 2025-11-04 04:31:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a406be3-45f9-31b6-9ada-6e4c44460f13 | -2.6605 | -51.62173 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fbc540b4-9901-3fa4-9ff4-f5000c5fcc42 | -3.9169 | -47.68779 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 28ee5c66-d242-3c95-82e4-cdea469d34ae | -4.94695 | -48.56489 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 460a1515-fe67-3736-aae8-7e3316f34746 | -3.79072 | -51.76627 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7237c030-5306-3f4c-b4ba-479b6c804395 | -7.06666 | -46.73473 | 2025-11-04 04:31:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ed1b031-e72f-3e8c-8e1b-7a6b5539b82f | -2.9484 | -51.58212 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f0d340a-a110-3caf-abe7-d792b5e196c9 | -2.92562 | -51.76899 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5294f50d-fd93-370c-85d9-8dbbf83a8e85 | -5.83118 | -44.0918 | 2025-11-04 04:31:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a646dde-d149-39ea-9c6b-dcc944976f52 | -3.06724 | -47.77369 | 2025-11-04 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0231940e-6eb9-3482-af1d-7662e26673c1 | -3.4894 | -50.31976 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 983edeee-bf54-3da6-935a-e84b16f450c7 | -5.06145 | -45.90975 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| b408a849-1e2a-39e3-aabf-7681986c2c50 | -6.09928 | -41.70318 | 2025-11-04 04:31:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 62f4576b-017e-3d9b-adf2-254e7471ba60 | -3.91305 | -47.69072 | 2025-11-04 04:31:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f4c214c5-af01-3d01-85e9-88a9e3204d36 | -4.90988 | -48.75536 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2af2223d-a903-3f94-a034-3b91743f0e0d | -3.9179 | -45.21516 | 2025-11-04 04:31:00 | NOAA-20 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c9f19ae-7a32-3b24-9898-bdc98115d371 | -3.78998 | -51.76876 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e1af323-bae4-3b26-aa37-58b78f4c65a6 | -6.84479 | -46.2965 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14fbb317-8b9b-3bbb-bec9-c1e0186f3a76 | -3.17361 | -46.58399 | 2025-11-04 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 684b77e9-1be1-360b-99f7-944003de41be | -5.61868 | -45.97588 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ac02cdb8-989a-3eed-9592-0d24e7f84d9c | -2.67119 | -49.95884 | 2025-11-04 04:31:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5e89924-91dc-34a5-8de8-be1eb74cef19 | -6.13707 | -41.54554 | 2025-11-04 04:31:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e9ac7e75-5772-3280-b89c-b55e5aa3b0ca | -5.57466 | -43.79221 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0614f22-3d21-32b7-893e-f43324942b46 | -4.99885 | -46.05875 | 2025-11-04 04:31:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d42a01b-f851-3225-a3c8-6738c8b19e92 | -4.61713 | -46.10653 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b6b1787-a545-3189-8893-bcc1736ecdf7 | -3.03953 | -50.34366 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5ff3890-07f3-39e3-950d-1bee76156d83 | -4.00216 | -46.99623 | 2025-11-04 04:31:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README24.md)
