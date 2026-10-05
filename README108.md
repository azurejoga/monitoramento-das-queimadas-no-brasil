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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43d1bbeb-23a4-3bb1-b706-aa6f3dbd1049 | -9.54452 | -64.81554 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1da32461-5728-343c-b858-01494ee8b3f4 | -5.55077 | -44.08108 | 2026-10-05 17:15:00 | NPP-375 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| af96bf7f-efae-3000-9d61-e0580a71480f | -6.38254 | -45.79696 | 2026-10-05 17:15:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 747c9136-8d33-3d6e-9123-36ef6f281e07 | -3.27587 | -50.40188 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 339a081c-683c-377a-bc19-f82d0167496d | -8.52833 | -54.59837 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| dac74219-9d03-315a-ad02-b45a53420102 | -4.32744 | -43.82645 | 2026-10-05 17:15:00 | NPP-375 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c723a471-5869-38f9-a474-a3efc9e86cc1 | -6.80485 | -39.29833 | 2026-10-05 17:15:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 5fe1c2c0-3553-39b2-a516-d06d3113c154 | -3.04941 | -54.22407 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ba0b74e7-2f5e-3afd-bbb5-f6d0adf93340 | -8.04672 | -46.83182 | 2026-10-05 17:15:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7f31da97-1ec6-3c8c-b787-6c8220c33513 | -8.52977 | -54.60214 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c4c63f0f-c87b-379b-b17c-2267a82dfcfc | -5.9992 | -55.68198 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 317f2394-383b-36ff-91e9-9348071c0f7d | -3.6295 | -55.27726 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| c93dad67-4941-3359-9691-0ccb00164dc3 | -2.45104 | -50.2528 | 2026-10-05 17:15:00 | NPP-375 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| fab43f5e-6815-3061-a5cb-01b4a40a65b2 | -9.10313 | -64.37014 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 785fa341-1970-3c17-ac47-6a7110b814a3 | -6.34079 | -42.54636 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| f13fac68-e4b2-3915-b9c6-c41895ac9240 | -4.46691 | -54.95972 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 006d425c-0207-31fc-bfca-a1cd31a02095 | -2.99511 | -51.00591 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 9048cbd1-5e47-378d-857c-016e92fe91c9 | -3.67198 | -55.94584 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 3260bff2-4094-3285-8ec2-0cc11abf0b21 | -8.60095 | -66.80917 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 2fb64c61-d248-3f5a-bd73-d9617ad2fef0 | -8.53208 | -54.59435 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 333fc768-8ec5-3eff-9260-2f84bc1239be | -6.79206 | -66.67278 | 2026-10-05 17:15:00 | NPP-375 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4f38d72b-17e9-34ed-ba9c-5df1c504e444 | -3.87827 | -45.77568 | 2026-10-05 17:15:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1bf362c4-399d-319a-bf42-5728afdc7aa0 | -3.36757 | -43.07122 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b742b80f-7d3b-302e-91ec-22209d1c8de0 | -9.82645 | -65.02131 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 59500335-4b1f-32d2-bf1b-63135c929eb1 | -8.78078 | -47.55606 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 333a5cec-b9ec-3d4a-b242-59093ac8b1e4 | -3.51022 | -54.60709 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 23c5a956-d725-3a4b-a95c-c50846e2f6c4 | -8.85884 | -47.14565 | 2026-10-05 17:15:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 361cf7eb-8065-3c45-a283-01a32dfae5e5 | -5.11852 | -43.99487 | 2026-10-05 17:15:00 | NPP-375 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 878851f2-6be6-3294-81b1-a8cede6aecd7 | -9.16111 | -45.13088 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 37977006-a04e-304f-8760-0c7813d28f87 | -3.55106 | -54.69646 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d3073e3-ef99-33ab-81ae-1ac3d2a29b0c | -3.61154 | -54.60517 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aaef237d-4db9-3f2e-aea8-e4ad60834da9 | -4.20779 | -53.46631 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0870330-bda4-3f41-bcbf-d503fab7fe0a | -7.61816 | -45.29449 | 2026-10-05 17:15:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6825acec-3aba-33f1-b7c4-3e2b901f663b | -4.80782 | -42.15185 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| cf676554-5fe7-349f-a057-cf7c690a54e1 | -3.67936 | -55.94847 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 8f4af8d4-e9b1-3789-bd19-52538f5b7de3 | -4.20726 | -53.46283 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2e565f20-3e2d-3c53-87b2-33fc305d2a2f | -6.92992 | -44.55928 | 2026-10-05 17:15:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9ef9d9cb-3478-3664-9028-cce4774fb366 | -4.45742 | -54.96473 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d5277cd0-68ef-3502-905a-2f4044052ea7 | -7.89897 | -44.19934 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8174cdc0-e604-3048-b062-ec1e6bc94674 | -3.63393 | -55.28382 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 13a92184-9083-35db-8b76-35c86bb08b82 | -2.99055 | -54.10588 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 00886492-f7f3-370f-bac5-318bcbcbdbf0 | -7.55205 | -46.72936 | 2026-10-05 17:15:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 01682576-b365-362a-a7c1-b8a7040b1990 | -3.03862 | -54.26452 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aa7772e1-3d6f-3857-8050-1011ddfebf2c | -2.88906 | -42.36871 | 2026-10-05 17:15:00 | NPP-375 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0003dc1-de95-3afb-acfe-b1b621c81657 | -3.55994 | -44.56972 | 2026-10-05 17:15:00 | NPP-375 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a9314e49-d8c7-3ae8-ac5b-8a0c005d9d09 | -4.52895 | -60.22911 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9e2a7f1e-bc0c-3d68-92c0-f9a83771668c | -8.43377 | -54.98891 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 459d2477-8a05-3357-9990-6e58516e0718 | -2.78405 | -49.44894 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fbf6d9ee-b124-3338-a887-78caa43e947b | -4.11706 | -54.41913 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 768bcfc7-cc8c-31c3-aab1-c82d37c4724b | -9.47334 | -64.34092 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 75260da9-17dc-3b07-9313-c9f7219d80b4 | -6.0662 | -59.93458 | 2026-10-05 17:15:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d00aa5a6-ad89-388f-acc5-cdf1e2244ef3 | -3.28205 | -54.1765 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8072f8d1-f6db-3d32-a3ec-1cd73b38b163 | -8.41953 | -54.98728 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e1dd32b9-79d3-3985-a448-d98a786b6274 | -8.51959 | -47.44233 | 2026-10-05 17:15:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b7216566-704a-3198-9748-fb9aae235054 | -3.71877 | -54.22408 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2665f8f1-d096-38a0-8c2a-8cbfb82663ae | -6.36116 | -45.02497 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d02d3b08-9742-34ad-aa83-235ec168c5a4 | -4.66984 | -54.47397 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| d69f8b6b-b28d-399b-bdd6-fe35be99ffe0 | -2.99378 | -54.03831 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe71b999-023f-38f6-8d92-c8587baabdaa | -3.98457 | -55.82 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 48a289f3-a4b0-3642-a198-49b1af745457 | -3.36385 | -43.38444 | 2026-10-05 17:15:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4fc2d820-284e-3493-9f7d-436de1e8cb6e | -4.15577 | -60.7847 | 2026-10-05 17:15:00 | NPP-375 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0286a516-4d61-35d6-9879-dcd98cc3c1f5 | -7.23276 | -55.18871 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| baa2bbc9-c1c2-3ee8-a1cf-2d02d341c351 | -3.52793 | -54.32464 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 29e55c1a-1486-3a99-801a-6bac0b409ce0 | -3.85667 | -51.34179 | 2026-10-05 17:15:00 | NPP-375 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| f0b63597-1c9a-3e27-9399-c2b60863f3ca | -4.05513 | -54.03639 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 631963f2-237d-398b-8814-de06c6d665cb | -8.86075 | -66.78362 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bd003490-209b-3d3e-83c9-4ce427f904e0 | -8.00587 | -42.91827 | 2026-10-05 17:15:00 | NPP-375 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 39.9 |
| a4caeeb7-ad81-38ef-a42c-b4d601835c97 | -4.26869 | -59.20178 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| eca6da66-c5c1-3d41-80f0-85199844e396 | -6.33832 | -42.56038 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 1a20d532-ee5d-3576-b567-bb0aa1b44692 | -7.48201 | -44.42862 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 71cf088f-8e28-3662-93b9-3ad886eeb06a | -9.80293 | -64.99104 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8471bb5-8f2b-3431-ac90-1e3d58a61e05 | -5.95763 | -41.35653 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 175.7 |
| 2f0092e7-5f8d-35cb-b213-11b009aae72d | -3.03915 | -54.26797 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1a41844e-9a2c-3f40-9073-0fb258cf8a55 | -8.53439 | -54.58655 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7da602e9-fef3-32f0-a5b8-fb87ed3de0ff | -9.38426 | -47.06811 | 2026-10-05 17:15:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1acb8fd3-80a4-3162-a995-8664648e4ddb | -6.90759 | -43.67215 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10f82ba2-9e04-3d1e-a529-336e052c7d4f | -6.34739 | -42.54168 | 2026-10-05 17:15:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b89bd92a-627b-345d-b81a-02f6cd928344 | -3.05099 | -54.23442 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e43c2f6-3c63-3275-951b-5023639a15fc | -3.4672 | -54.59238 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3f01b049-e662-30f3-a69a-a880e156d23b | -3.18305 | -49.44845 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 93e39793-0d5b-3a82-a704-80242663de8a | -7.22648 | -55.19341 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| abd33997-d50f-3ec6-9b73-4c2ac5ef6f72 | -5.13349 | -60.31963 | 2026-10-05 17:15:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b144238e-bc8f-3dd5-a765-fd390f1d8532 | -8.5232 | -54.61028 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed468a52-b31f-3ec1-b527-122cc7da8424 | -3.42259 | -42.56413 | 2026-10-05 17:15:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc2ec412-cb5e-38fa-aca7-56f047a3ed7b | -6.59805 | -41.57878 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 5ef077d0-b8ae-34e9-961e-7ca29f24c51c | -3.2694 | -54.00542 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a59eb5c5-474a-34f5-9318-ec0dc49e44e7 | -9.81871 | -65.01901 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81a50f2c-41cb-3e43-aa47-fdfdd678105e | -7.22306 | -55.19393 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5e8653a0-d36e-3055-b814-1c4acbbb5790 | -3.03877 | -54.24333 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7986f076-a893-3fa4-b611-679d0f1e312c | -8.6665 | -54.54019 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| eef363e4-8858-3853-8a70-16997e6c6e6c | -3.84605 | -50.32069 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9078654d-41aa-3f1b-9421-4ddd24cbfe96 | -5.82006 | -53.83802 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 712b7a01-2171-3e4a-bcf5-84a6e24a8c88 | -7.45216 | -47.64906 | 2026-10-05 17:15:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db1e3d83-0ed0-39d7-a094-4ac47794d1c0 | -3.67093 | -54.53167 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 47ca0035-34c6-378c-8df8-85f0cb7e31f6 | -8.66121 | -54.57445 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e9a1aac3-4fca-3d6d-b224-8e4a7e440c67 | -6.59708 | -41.57354 | 2026-10-05 17:15:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 40.9 |
| 8030952d-bb36-3cd6-8d8c-6f4353cba626 | -6.73307 | -55.06273 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 94eb64b9-937b-3f5d-a9e5-e497b97fbf6b | -3.08443 | -49.53276 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 20415766-c9f4-3347-b2dc-e97d3fba4a8c | -8.74568 | -64.19108 | 2026-10-05 17:15:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 620b8e0c-73ba-34f3-bda0-ebd2c738f2b3 | -7.32635 | -55.13688 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README109.md)
