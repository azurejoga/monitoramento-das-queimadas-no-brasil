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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c593db7b-df89-3131-9668-d8cc4a07eb6d | -6.2529 | -52.847 | 2026-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 514335a6-4d09-3555-b23f-f80281929ecd | -10.4147 | -47.2846 | 2026-10-08 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 3971d6bf-f261-3f88-adbb-010847df68bb | -8.2865 | -50.2731 | 2026-10-08 02:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| e010f19a-f886-3170-a428-c9c634ca7236 | -3.11 | -54.1862 | 2026-10-08 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 6075c5a4-391d-3e21-ae88-7af143e9ddec | -3.1879 | -58.6433 | 2026-10-08 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| eb81a7ac-7904-3355-af0f-646235215ba6 | -3.2157 | -50.5586 | 2026-10-08 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 4f680c42-ddbf-3d1e-9099-ea3d60661a88 | -3.1298 | -53.7834 | 2026-10-08 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c7b1e0c0-ed9a-37fa-a921-56e73a2c3c9a | -3.5515 | -59.4807 | 2026-10-08 02:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 357a7477-d373-32d1-a600-ccfc80c248e9 | -5.6931 | -53.5073 | 2026-10-08 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| ad763545-2494-396d-83cc-b0383f831a2b | -3.531 | -54.6757 | 2026-10-08 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c9a1de04-f7fe-3546-8ddd-6b68c43c0ab5 | -8.537 | -66.9764 | 2026-10-08 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 1d2d59f5-9c8a-34ec-ba36-8446836d70d0 | -9.0591 | -65.9396 | 2026-10-08 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ed051f59-24a2-3e09-b8a9-7de8cc04e22e | -6.15 | -39.4409 | 2026-10-08 02:00:00 | GOES-19 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 6ba44b1c-e87b-37f0-8db6-54912c435d44 | -6.2157 | -52.8695 | 2026-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ba7ec7a9-631f-3cd7-a906-797635522c04 | -2.4988 | -56.1266 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| cec0b949-8f09-37f4-b796-b7b2a5fac280 | -5.6932 | -53.487 | 2026-10-08 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 143.6 |
| b03cfe7e-b7c2-3cbc-bfc7-829003bac3a1 | -2.4987 | -56.1659 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4b607805-6f78-3269-8000-896b7d3f7024 | -6.2343 | -52.848 | 2026-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1c9de7f8-4683-3add-bfac-87cc5c5afb93 | -9.4749 | -64.3713 | 2026-10-08 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| a53bd777-c2c7-3fc5-ab2b-aeb335b80b1c | -2.3848 | -57.9044 | 2026-10-08 02:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| bfd49a66-0c3a-301d-9a01-e38ec5a6cfb2 | -3.0373 | -53.9469 | 2026-10-08 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 1769baef-1910-3655-bee4-d8c108e51959 | -9.475 | -64.3525 | 2026-10-08 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6693b1cd-df43-31d2-9c9f-4455afd011b0 | -2.572 | -56.1842 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| d8e149dc-898d-3487-a376-0acf8e3f1305 | -7.0065 | -59.1223 | 2026-10-08 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| fc6953ef-9fcc-332d-8c9d-830532459c3b | -3.0374 | -53.9268 | 2026-10-08 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8b186d24-89fd-3e91-827b-94d691580c58 | -2.517 | -56.1656 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 5bfbe047-b533-3b81-ab56-bc360cfa13a4 | -6.1429 | -47.9432 | 2026-10-08 02:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| a470a85d-7de4-3c34-96a9-cb855b83b040 | -6.2342 | -52.8685 | 2026-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 119e32d2-00de-39a7-b216-618bc0bd3a7b | -2.7797 | -54.0736 | 2026-10-08 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c20cce48-c138-35be-b60d-e14a2947ee06 | -3.1697 | -58.6244 | 2026-10-08 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 572b0634-76b3-382d-952b-b6246f845430 | -3.073 | -54.2874 | 2026-10-08 02:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| b886827e-964c-3d24-a591-d977903c347a | -6.2527 | -52.8675 | 2026-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| a53bc99f-30d4-3508-8663-965f5a0d00c5 | -3.478 | -59.597 | 2026-10-08 02:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 811757e3-510c-38c4-93ef-0129748dc56e | -6.2158 | -52.849 | 2026-10-08 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| fa1a3273-5f9f-3bba-a342-32686144e2b2 | -3.5493 | -54.6752 | 2026-10-08 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 10223bc5-bd0f-3bf3-b5d3-c2ae33658b73 | -2.4988 | -56.1462 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| ece69e97-e6d9-3531-8db4-a8b70314d915 | -9.9018 | -44.7917 | 2026-10-08 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 29de157a-2130-3816-a20e-7c1298bed448 | -2.4805 | -56.1269 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d5e841e8-2b73-3820-bc3d-c1654bee097e | -3.0913 | -54.287 | 2026-10-08 02:00:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 1c73b16d-4696-3555-a824-e299b32106a8 | -3.1114 | -53.7839 | 2026-10-08 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 475a2b7a-4b97-3faa-8980-4336a2fedd8c | -6.6317 | -43.73 | 2026-10-08 02:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 104.7 |
| e15c7d5a-ceff-3565-877a-e85f59e2e215 | -3.1115 | -53.7637 | 2026-10-08 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 606dc48b-06f7-324a-b44d-5d3d21e87884 | -5.9586 | -55.3648 | 2026-10-08 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 54d089ea-e705-326e-a12d-d5d3777321ff | -5.7117 | -53.4862 | 2026-10-08 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 124.0 |
| dea25048-5e6e-3026-9ca8-0099c9e234da | -2.7613 | -54.0941 | 2026-10-08 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e9d3048f-f261-3d1f-821c-2dcc9babb177 | -4.4507 | -47.9112 | 2026-10-08 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 2b95ad74-6973-3837-afdb-ee9866e86e96 | -2.499 | -56.0675 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| bbd75b21-e7ba-3829-ade3-9fcd32389e26 | -2.4031 | -57.9041 | 2026-10-08 02:00:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 6d37c64f-24b4-319c-8db7-a5d9f0c75941 | -2.7796 | -54.0937 | 2026-10-08 02:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ae1d1911-5b5f-380f-a666-22ade9087462 | -5.7116 | -53.5065 | 2026-10-08 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7f0dd244-ca82-3c68-9dbd-6466bbf2f617 | -11.3937 | -46.6922 | 2026-10-08 02:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cfe5e9b4-3dd6-3bfa-9245-b42921ff8c31 | -10.434 | -47.2601 | 2026-10-08 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 932a6795-c0db-3e1b-b592-823291452bfc | -10.4151 | -47.2623 | 2026-10-08 02:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| bca8a6fe-ea6d-3f61-a41d-b490c33a84c6 | -3.478 | -59.5779 | 2026-10-08 02:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 5ab77d01-4c5e-3c94-aa13-919e9badaa41 | -9.0592 | -65.9209 | 2026-10-08 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| f878f83c-dafd-3645-9637-626eeb53c88f | -9.4936 | -64.3518 | 2026-10-08 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.4 |
| cb163e4c-0899-320d-8ad6-cb6dd5987314 | -3.5865 | -54.5742 | 2026-10-08 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b7af8871-b729-34ef-9043-568b8d4fd702 | -4.0628 | -59.8328 | 2026-10-08 02:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bbc6f4e8-7b5c-37c6-b414-b94a446b44b1 | -2.572 | -56.1646 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 39b3c193-94fc-3ed2-a0f9-17c3d5cf3192 | -2.4805 | -56.1072 | 2026-10-08 02:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 89b34c5f-0bce-36fb-aa9a-3ee14da48f78 | -3.1101 | -54.1661 | 2026-10-08 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 08c0bee8-fd50-3266-b6fd-37355f9c83ae | -3.1697 | -58.6437 | 2026-10-08 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 45daa194-756d-34ef-b7db-05c544e9a587 | -6.1431 | -47.9214 | 2026-10-08 02:00:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 62e49181-565c-366a-b24b-4a0acb87f679 | -3.531 | -54.6557 | 2026-10-08 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| c94f7d72-23df-355f-8f95-6e4dbbfdba36 | -3.1972 | -50.5592 | 2026-10-08 02:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 00407191-e5b3-3a83-a780-8e0a243b7b82 | -4.4506 | -47.9329 | 2026-10-08 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| adbbfbeb-27aa-35d6-8742-d161bd87e19a | -3.5494 | -54.6552 | 2026-10-08 02:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| b0fd599d-9e45-3ddd-ae9b-7a8913b5ef03 | -4.3471 | -43.8021 | 2026-10-08 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| dc274ade-13da-38a2-83f7-5ed25531ffc6 | -1.5306 | -54.5558 | 2026-10-08 02:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e6a09456-da7e-39f1-ba61-a4308027f41b | -2.8575 | -59.1107 | 2026-10-08 02:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 09ab5fea-156f-3d4b-ab99-c569421a3aa6 | -3.0741 | -53.946 | 2026-10-08 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| df123445-d33e-3f87-81be-042ae000fb3d | -3.1285 | -54.1657 | 2026-10-08 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| cbd63331-a160-3871-8a53-c2b93ae08c00 | -17.1213 | -41.3421 | 2026-10-08 02:00:00 | GOES-19 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.6 |
| ddec05da-3f48-35ff-9e02-5e455fe25d93 | -11.394 | -46.6697 | 2026-10-08 02:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 0480da4f-bf4b-352e-9570-b1a380cb3cd2 | -3.1697 | -58.6244 | 2026-10-08 02:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 9652ef2a-94a7-3f8b-a895-3875558151d6 | -8.7423 | -45.1334 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| fae954cd-81bf-308b-a3da-41f96e1c8c3f | -3.1115 | -53.7637 | 2026-10-08 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 9b8acecf-4c03-3c36-a3c8-4d3ccce6c04a | -3.8567 | -55.9769 | 2026-10-08 02:10:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 54c33623-5f7d-3d04-9ab5-252f14aa033d | -6.6129 | -43.7317 | 2026-10-08 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c4ba790d-b3a2-32f1-ac1a-ad6db73b92f0 | -8.7228 | -45.1812 | 2026-10-08 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 208.8 |
| efd738dc-5655-315d-8809-6a69eb2e4d1d | -3.478 | -59.597 | 2026-10-08 02:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 6d4e33e6-9a05-308e-8919-052ae7d8e163 | -3.1114 | -53.7839 | 2026-10-08 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| eec76db1-91dd-3dc8-a3eb-c128f9d4754f | -3.0373 | -53.9469 | 2026-10-08 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| b3bd876e-76c1-3b34-afc2-c385f98e29c2 | -9.475 | -64.3525 | 2026-10-08 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c07ef7ae-7c68-3a29-926d-c2982dab83aa | -4.3471 | -43.8021 | 2026-10-08 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9a46f5b4-5982-3fa9-aa97-3a932c0184e6 | -6.1431 | -47.9214 | 2026-10-08 02:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c12f3134-f5b5-32b8-a95e-52d00e821898 | -1.5306 | -54.5558 | 2026-10-08 02:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| b48a71e4-decf-3d36-abc8-b8ff6a922f39 | -5.6931 | -53.5073 | 2026-10-08 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 94abaf1d-5f3c-380b-9035-027f3215593d | -2.4031 | -57.9041 | 2026-10-08 02:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 3d9ad69c-74e7-39f2-95b4-21d19f375a23 | -6.6317 | -43.73 | 2026-10-08 02:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 8dad1818-4333-36b0-82f7-3f50fd1545a5 | -4.0628 | -59.8328 | 2026-10-08 02:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4715f498-e0cd-3465-a408-e4a9ec4b5a79 | -10.4147 | -47.2846 | 2026-10-08 02:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 781c8140-8252-3825-b681-e05615e4b363 | -6.1429 | -47.9432 | 2026-10-08 02:10:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 754a0389-6032-3593-a2e8-7d56fa79fcba | -9.4936 | -64.3518 | 2026-10-08 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 992a0d99-32e4-3886-bd68-783295287754 | -5.3907 | -44.1738 | 2026-10-08 02:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f02084a4-e6bf-361e-82e1-02cf2b6309f9 | -3.0913 | -54.287 | 2026-10-08 02:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| facac8a5-6b8c-3664-afc1-7d9a0594d7ad | -4.3658 | -43.8011 | 2026-10-08 02:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 6da66656-3dd2-3962-bc66-0362cd1d7792 | -3.2499 | -46.9589 | 2026-10-08 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b0b13850-7ab3-364e-a294-388a45f4594d | -4.4506 | -47.9329 | 2026-10-08 02:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5704fcdf-dccc-34b7-9d01-8f344fbfec57 | -2.572 | -56.1842 | 2026-10-08 02:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |


[Clique aqui para ver as próximas entradas](README50.md)
