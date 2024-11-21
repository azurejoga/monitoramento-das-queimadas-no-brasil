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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9906666a-bf45-30fc-8178-1ad8fa53670d | -4.45204 | -50.09816 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb2e0f12-724c-3415-8eba-154e388f0746 | -3.50777 | -53.79794 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2dde26b7-bb89-3a66-998f-18cf2c986bb2 | -4.10481 | -50.74274 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1703ee8-767d-33be-8d47-a76843c3d43f | -3.53969 | -51.60447 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bd13b94-06a1-3ccd-b521-ced562b1a2a2 | -3.64115 | -52.36221 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 175179b6-5bf8-3a42-b529-0ee6a769a22f | -4.57436 | -48.01649 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a3ca5266-128c-3b11-a22d-aaee74d05854 | -3.52128 | -53.80086 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dbc2310-32d9-368b-a866-2371167de85f | -4.09412 | -51.0771 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6eb2a77e-9f2d-3fd2-b646-33355834640c | -4.63826 | -49.54549 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11b2ad18-d1a6-334a-89c4-e17a150cdfc3 | -3.5389 | -51.60944 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c2d5dc3-5a19-36dc-ad3f-152b8faa25b0 | -5.46761 | -46.5337 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38048866-0e23-3e8b-a2bb-0b3f6145e37c | -4.68933 | -48.97983 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16a03944-c9ca-3d40-9587-1bfa44f2d2ca | -4.08984 | -54.04981 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16c7acfe-a3e5-303c-9fa2-887ebb144c29 | -4.63132 | -49.54437 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a3ac643-476b-39ab-9f38-156870862a62 | -3.66413 | -51.57252 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ced186a-2252-311f-97e5-ec13e184698b | -4.09265 | -51.08611 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d4a087a3-f8c5-3130-b215-aa384e60bbf0 | -4.34989 | -45.88589 | 2024-11-21 04:31:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d502b6-bc78-3389-92b9-ea4bec8e65b4 | -3.39087 | -54.55272 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a3338b6-6050-33e2-a26b-b908db6cc632 | -4.49094 | -47.10868 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0663e65-ec85-325f-9e56-e090fd775eb1 | -5.55782 | -46.39556 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 558fb024-99c8-3172-bd3f-3baed9a1a29f | -4.38561 | -47.77589 | 2024-11-21 04:31:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be0f585c-d818-35d4-9f7d-17cd84ba2e38 | -4.95895 | -49.8469 | 2024-11-21 04:31:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e405809b-369c-3dfc-8fda-43888855fd2d | -4.81652 | -45.75353 | 2024-11-21 04:31:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02c6e25d-698a-3d11-8631-19cf39fe9a78 | -3.77256 | -51.81731 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d99e01-e6f7-3def-ad1f-8cc210730b18 | -2.94373 | -54.79775 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad56ee92-623a-32b2-a53b-9acf1f42842f | -5.55534 | -46.19049 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bac05fcc-3857-3014-8503-e49a2cfee60f | -5.81441 | -38.32871 | 2024-11-21 04:31:00 | NPP-375D | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 28276e40-8cec-3729-978e-5f44c88fc940 | -6.07089 | -41.03325 | 2024-11-21 04:31:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d8c6e8db-05ab-378d-aaf3-b9f23cc23725 | -4.63766 | -49.54932 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d2f5fe3-1882-3db9-af1e-d0759ce367b3 | -3.05849 | -54.4032 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45836a93-2935-3720-a6b1-03dbc6e2875a | -10.72856 | -49.51596 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af3521a3-631c-3e44-a418-fa464d52c255 | -3.35649 | -53.40066 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d3904fa-bd82-3b47-bab5-308f60060a5d | -3.29216 | -53.86003 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1023420b-520a-39c3-a4d2-6952d65819b7 | -3.75216 | -52.32767 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dc2ac7c-7b96-32e1-b92f-bff6fb8a9679 | -3.56472 | -51.49739 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50faed1b-b2ec-3a9d-a0cb-d67b778fd4b4 | -3.83104 | -50.2876 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce64772c-0c48-36fc-9f31-3fa09aa2cd1c | -6.20781 | -45.37283 | 2024-11-21 04:31:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7459592-9921-3b46-9af7-e06645b69422 | -3.92236 | -50.11428 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f843c7e-bd7b-3a0e-bc80-e72d0174d91c | -5.34472 | -45.65664 | 2024-11-21 04:31:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dff23f1b-bf3d-3021-a75e-0dfbfd63f7c1 | -5.47096 | -46.53421 | 2024-11-21 04:31:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa644f0-10ab-3a34-9ae8-4c9209a130a4 | -5.19708 | -47.74077 | 2024-11-21 04:31:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be477a32-5006-3349-8884-5b18aa92cdd7 | -9.10142 | -43.19479 | 2024-11-21 04:31:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6276f050-7cb2-3cc1-8cf0-db9f21d52509 | -4.05802 | -50.6106 | 2024-11-21 04:31:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85f813c7-6dab-3504-b544-4e8d48b91f42 | -5.10262 | -43.16713 | 2024-11-21 04:31:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c64fd371-aca3-31f1-ac44-0320df57820f | -4.64007 | -46.35148 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5b59533-2c05-3c1c-bb3b-f47a14b2aca5 | -6.82608 | -46.77575 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cff051db-d726-357b-983f-4cbde654b58c | -3.10528 | -53.74146 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3c7c9d0-a545-3ba6-b0ff-1bcba0d6cb16 | -4.57991 | -48.02452 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 48b20b12-bd9c-3259-91ea-0934a0df9902 | -5.82975 | -44.10844 | 2024-11-21 04:31:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37ccd371-8f88-3742-8536-2b9b50fd216d | -3.90714 | -49.40939 | 2024-11-21 04:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21f62b7d-7ef9-3b8f-8a18-faccf7cf351a | -3.1992 | -54.31973 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 060d88c7-de5a-3e21-ac6b-871d40d92128 | -6.18793 | -43.41188 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7a6ed22c-75a5-3699-b110-61a87f369e99 | -3.6465 | -52.35549 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4af58b99-556a-3937-b6c5-efbb77760942 | -2.94284 | -54.8031 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 466eaa13-0eab-3c25-a161-18d6bb9d9f0d | -4.90282 | -47.41784 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| afa7f7a1-81e3-3ce3-953d-727044ca3c13 | -3.74113 | -51.15393 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 693e3ce4-3e78-3636-8f7f-1e6e7df93995 | -3.67177 | -54.27341 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b8ae277-c223-3d0c-a8e3-4899fc78993e | -3.50699 | -53.80255 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 641e6022-8edd-3d20-ac8d-aae97dae7f65 | -6.81937 | -46.77472 | 2024-11-21 04:31:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d8725d81-bcd7-394e-b6d8-842a52526783 | -4.97586 | -48.45454 | 2024-11-21 04:31:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 45d3ac26-7bdf-3d0e-af0c-ba5420546cba | -3.37827 | -52.45743 | 2024-11-21 04:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| c464156e-3240-367c-a1e4-581d93f00425 | -3.23207 | -53.39097 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2816962c-b1b2-378e-9e0e-0c0870177745 | -3.19295 | -54.32795 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d30098a8-04f1-3653-98f6-47b0471a44d3 | -3.42567 | -54.60338 | 2024-11-21 04:31:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a91cf4a-10eb-3194-9c4d-072ec9eb1575 | -4.47494 | -45.66125 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 719d8b2a-6cbf-327e-a69b-bb4dd6aaf934 | -3.73256 | -50.43757 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cff67ac8-8061-348a-be79-199d8029b759 | -4.05714 | -49.28067 | 2024-11-21 04:31:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1e4fb19-9c96-3a64-aee6-bea188dcdfaa | -3.18428 | -54.32139 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 23f7ad8c-9ccd-3491-9022-3ca280f3dd61 | -3.288 | -53.82277 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e99a1882-295e-390a-b10f-39c8b33fc778 | -3.42359 | -53.28526 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b57d8fc-6f69-3bce-9f6b-316f8b54de05 | -3.28216 | -53.83453 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bdd79804-733a-35d3-9aed-203f11bd26dd | -3.76235 | -52.13371 | 2024-11-21 04:31:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7360f20a-4f1c-3f80-bc72-19a80395ca15 | -7.10081 | -46.70937 | 2024-11-21 04:31:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8def52da-8fd1-30fb-b0b0-6b9bfbba43b0 | -5.84521 | -47.49164 | 2024-11-21 04:31:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73deaeeb-d85f-3c8a-8ef0-21870f8ff723 | -4.57936 | -48.02802 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2f15f3da-bbe7-3263-8af5-778717cf9241 | -3.34021 | -53.30483 | 2024-11-21 04:31:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6a2bcaa-8bd2-35dc-ad41-b8bad0604979 | -3.2944 | -53.84603 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c52fd04-245f-34d1-98c9-42f59e65d173 | -3.51306 | -53.79421 | 2024-11-21 04:31:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 356c3fea-1b51-3e4a-8c60-c28ddbfd30e2 | -5.7609 | -45.78694 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffcc5434-c1c5-3143-ad00-60c91a5d1025 | -4.66222 | -46.53811 | 2024-11-21 04:31:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e99b73fb-a548-3ceb-94f7-82c2efaf26c5 | -4.58436 | -48.01806 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9a4c5223-09f0-3104-9c09-44e55442a1c3 | -10.73239 | -49.53484 | 2024-11-21 04:31:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c12de766-0111-3eea-87c5-b218b6637a69 | -4.39449 | -45.59636 | 2024-11-21 04:31:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1892ad94-13c4-3cd6-9b22-25f76f0a6184 | -4.07003 | -51.03334 | 2024-11-21 04:31:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 973cb39c-2580-3c9b-a4ce-083125d4b63f | -3.19835 | -54.32474 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e8a5fcd-0b80-3bca-ade6-8bc1dd21445a | -4.66304 | -46.40188 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5151b631-592d-372c-a7f7-664768ce589c | -5.10648 | -43.16774 | 2024-11-21 04:31:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 30a59c31-d8ed-3d08-9f13-41811160c0f0 | -3.20225 | -54.33046 | 2024-11-21 04:31:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fdb6e0da-09c3-3eba-aa35-4de7486a5314 | -4.99521 | -47.2198 | 2024-11-21 04:31:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff96ee79-0b90-3e99-9e3e-bb3d307c1c0d | -4.58102 | -48.01754 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 32c32ae1-8e23-34af-bf25-f9fffa3113c7 | -4.61222 | -48.80376 | 2024-11-21 04:31:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad78915c-052e-3d50-8036-9e100e08dc1f | -5.49674 | -43.95403 | 2024-11-21 04:31:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74d3e1dd-2cbb-33da-84aa-c99974d15bb1 | -10.45707 | -40.38128 | 2024-11-21 04:31:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 770a9ea2-82c3-347e-8032-4f8a65781192 | -5.56074 | -49.38346 | 2024-11-21 04:31:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1d5d4c5-cde1-3d2f-9d5f-43388c780bbb | -3.80927 | -51.26538 | 2024-11-21 04:31:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c95702b5-59ec-3a2d-9c9c-82ad0e99922a | -5.23734 | -42.64039 | 2024-11-21 04:31:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a59ddd39-39ae-37a0-a770-2ed910999727 | -4.66638 | -46.40239 | 2024-11-21 04:31:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cfe4d4b-ef08-3a71-b17d-8f34aea9def9 | -6.20612 | -46.224 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65184512-97f6-3b54-b23a-8c670c24913a | -5.6105 | -46.28666 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c0fd679-e46e-3897-ac59-fec45d82b45b | -5.96041 | -45.55416 | 2024-11-21 04:31:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README48.md)
