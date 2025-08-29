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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d56e5be5-7a92-36c7-a391-85fb5fc36e95 | -7.41271 | -42.06155 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 964ec37b-b63f-3601-b8e6-5317cb49e43e | -7.96552 | -46.3625 | 2025-08-29 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 286a7969-cefd-3357-84a5-99a617d38330 | -7.22897 | -45.43097 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 924ed70a-8423-3e61-8bda-974fc7ceeb4f | -9.93642 | -44.02302 | 2025-08-29 03:47:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fd77362-784c-3466-a8da-104ce62e5417 | -7.43057 | -42.05992 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5eb0cb3d-4039-331e-8bfe-5b383ef5e978 | -5.27387 | -36.08348 | 2025-08-29 03:47:00 | NOAA-20 | CAIÇARA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2401859 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 52e3ae1f-2254-3e38-8f5f-d5592ac3b7d6 | -7.62381 | -42.72141 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a4599231-ef60-3e28-b9c2-4b6066df46b1 | -6.8118 | -44.99585 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e92de20c-940c-3354-8955-2a259e6140a6 | -9.50443 | -45.38012 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82e4af25-7ba3-3981-85f5-f4bd6e4189b9 | -7.03807 | -44.38708 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a34982d-e441-3479-8eb9-2eec17581ae8 | -4.14923 | -38.4796 | 2025-08-29 03:47:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 28952e16-e9f5-32b3-aa9e-060317ab08a6 | -7.0454 | -44.37313 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa2bc035-b85f-3a32-8806-f088e5fa9fec | -8.45284 | -43.71798 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5d7b49a4-8b76-30ec-9c3e-6c0f1f59cf25 | -7.61963 | -42.72066 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7fb2c560-aa56-3f8b-8ca3-b0e4558210ef | -6.48513 | -44.39743 | 2025-08-29 03:47:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8e72777-45fc-38b3-b9aa-c395c698d8f2 | -7.00104 | -44.36998 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11d41e6a-bc47-36be-85e7-2f89e0e67374 | -9.42927 | -47.64802 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 639426e4-4cda-38ed-97e0-dffbf16747ed | -3.27548 | -43.53012 | 2025-08-29 03:47:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8333a325-d757-3cd7-b365-d4da83d4a078 | -7.05007 | -44.37425 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ceeaa76-d321-3c59-8028-ba1e35f49862 | -7.63279 | -42.6678 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 661bf625-464c-3479-9bfc-f5718030f419 | -7.10478 | -44.59603 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2c400e78-f699-30bd-83d3-e87bcc9c3439 | -7.06869 | -44.83795 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bf076973-97b5-398b-b975-4a098b558656 | -7.63321 | -42.72279 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 78cdd4f6-7ecf-340f-be15-83f7e9df06ea | -7.42419 | -42.04209 | 2025-08-29 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 569f5a7a-d48b-3490-b5bc-fba0a4c0f2ca | -6.45582 | -44.56334 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68cf65b3-8854-3a45-aaa0-1a2e6f4498a1 | -2.97827 | -48.60749 | 2025-08-29 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e13101c-d497-3167-ab21-829ff105dfaa | -4.17249 | -42.87446 | 2025-08-29 03:47:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c78d030d-6de6-3e7a-8a98-ed9f197b8ed3 | -9.42852 | -47.65202 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eceecc9f-2ea2-325f-8e19-6fa318924fe6 | -9.5479 | -45.85248 | 2025-08-29 03:47:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d300a1c-31ba-3ff8-ac18-8bd44e9666f6 | -6.53065 | -44.11174 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 920b1c12-a3a8-3f11-a1ae-db546cc3d4c4 | -7.22018 | -45.45125 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 40a78743-800d-373e-bd98-67dad4d5edf0 | -6.88457 | -43.62156 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5259f62b-7b1b-3e4f-b0f3-0bf467f25c2e | -9.86485 | -44.68534 | 2025-08-29 03:47:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83c58a8e-0b62-3071-9dc0-e44c95a43fd7 | -8.70515 | -47.87218 | 2025-08-29 03:47:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 36487bca-306c-3393-8b29-61a774d65c8b | -9.04076 | -47.01384 | 2025-08-29 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 711d3b2a-a2ae-33bb-b61f-915fbc617584 | -7.01952 | -42.01964 | 2025-08-29 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d7da1be-b84c-3876-901c-ad5ad211490a | -6.88007 | -43.62077 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f215ae86-4149-34cd-b58e-1a6545af282f | -6.81279 | -44.34826 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b9f8fc2c-0d5d-3b86-b89b-cd79fd6c685d | -7.0492 | -44.3792 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d89a42c5-41f6-3bea-b294-3e649404fd81 | -6.70042 | -49.47506 | 2025-08-29 03:47:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2d99c17-0332-34c4-baa0-9a063f736f1e | -7.22187 | -45.44166 | 2025-08-29 03:47:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55f6778a-c885-34ca-93c3-5cf6dac19e72 | -8.46155 | -43.64332 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 64e1ce96-4e6e-305d-8cb1-5471358982d1 | -7.05303 | -44.38511 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ec6922e-e6b8-31a8-b5cd-afc09616cfc6 | -7.05273 | -44.35915 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cf0117ec-8fa5-3183-a9f4-2c6d37b858ee | -7.62863 | -42.66707 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fdc8f2e2-5234-3d8d-8fce-5faf7cc95175 | -7.6132 | -42.70775 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0ad2c47-7ee1-3601-810d-862181878e3f | -7.62219 | -42.70543 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 122be7b3-b282-39c7-bb5f-1021c1e5e323 | -9.43069 | -47.64039 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bbb7ab1f-6195-3ea0-8727-b652d83f7893 | -6.83512 | -42.82183 | 2025-08-29 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27624165-c480-3d61-8922-691e128d2ee4 | -9.69693 | -47.06812 | 2025-08-29 03:47:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fca6655-30d0-358f-9a63-3510be028c46 | -4.4028 | -40.48671 | 2025-08-29 03:47:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1b5956cb-c006-3077-a3aa-4bc4134a60f4 | -6.38544 | -45.22399 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95061a28-95ff-38c7-bde5-643eb65385d5 | -8.4755 | -43.64109 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d0a36ed-1e22-34e3-ba60-bb9a5884d49f | -7.03984 | -44.3771 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 891faae5-05d2-3eb7-a165-c0a33470632d | -7.72321 | -50.28619 | 2025-08-29 03:47:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| db135f13-76f2-39e2-bdc8-101eda2805f8 | -6.78596 | -43.56429 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8232ebce-efc0-37d6-bdbf-843ecbf722c8 | -4.15267 | -38.48018 | 2025-08-29 03:47:00 | NOAA-20 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 80fda55b-e6b5-387a-b2cf-c30bc1351e36 | -7.02353 | -42.02045 | 2025-08-29 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1683d756-ffbb-3bc7-9534-60adb84c9b12 | -7.07202 | -44.83513 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1af18a42-e321-362d-af7b-0bae698c5c0a | -7.15888 | -44.16364 | 2025-08-29 03:47:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d58f095-eaa1-3b33-aaee-074ed7835d29 | -7.96717 | -46.37313 | 2025-08-29 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 207f4a06-7438-3434-8a4e-8b258e6bcc66 | -7.67522 | -40.14886 | 2025-08-29 03:47:00 | NOAA-20 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 31516ae7-b995-3bd4-b07d-1624f13cf6b3 | -9.48697 | -45.39359 | 2025-08-29 03:47:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4b5f4b1-d1e0-3341-abb7-725a02f7c60e | -6.72158 | -43.57848 | 2025-08-29 03:47:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dbd55c5-c326-364c-9bb6-e91ecab07cc7 | -6.70359 | -49.458 | 2025-08-29 03:47:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fad68f00-0273-300a-adb1-fae7e163e6f0 | -7.03883 | -44.37646 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f5e2ce85-3a73-3984-aeca-cc3db4620a9d | -6.51589 | -44.85439 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48f3ac32-2433-3374-b6f4-0ec393045e80 | -7.04807 | -44.35802 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aeedf84b-16dd-373f-9e07-3a62d8f6ec7b | -7.04338 | -44.35707 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c172859e-bb2e-3f94-b5ec-04d733038fdd | -7.63217 | -42.72286 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3e92d9ac-e881-32d7-9d89-2fab9b8824a7 | -8.90331 | -47.32743 | 2025-08-29 03:47:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4884562b-830e-37b7-b54e-81f52fa5b733 | -9.42999 | -47.64414 | 2025-08-29 03:47:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 16b44872-2618-39a2-9082-4807243b5902 | -7.04249 | -44.3621 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8b36e3f7-9587-36f7-ae5d-2fc51db74948 | -8.46135 | -43.64505 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f61eb5d0-404a-3a7a-a2cd-0a2bf282c6e5 | -4.08975 | -42.85867 | 2025-08-29 03:47:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3eac3d5-c6bf-3872-9e68-2c171f2c0eb7 | -8.47988 | -43.64187 | 2025-08-29 03:47:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9dce9be-c162-307c-88fe-c133447149ca | -6.70147 | -49.46937 | 2025-08-29 03:47:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e44f713c-4615-3fc1-a426-49709ee4e9ce | -3.61783 | -43.5435 | 2025-08-29 03:47:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85338352-2639-3048-be80-9a0a56ce9224 | -9.31779 | -40.21091 | 2025-08-29 03:47:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| be34dfce-349b-3f82-99b5-6e9a08f7b33b | -7.0782 | -44.29682 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a444f0f4-36f4-36ff-bd02-3d178d829cd7 | -6.39003 | -45.22754 | 2025-08-29 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84893c03-4029-359b-98dd-b451a86be3a0 | -6.88086 | -43.61621 | 2025-08-29 03:47:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02455d94-8057-3e13-8025-b02ac24603c6 | -2.98108 | -48.60559 | 2025-08-29 03:47:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eae21ec1-4168-3596-a589-9c86c7600646 | -7.10508 | -44.59298 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2a56b81-fb6e-32cc-bae4-c9b9acc86dc9 | -6.81176 | -44.35922 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe256a40-956b-322c-95f7-5cfe5e011e84 | -7.21327 | -45.31435 | 2025-08-29 03:47:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aaa66539-3ea5-3e38-b897-651a8e0fc851 | -6.88928 | -44.44745 | 2025-08-29 03:47:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 661439e1-d6e0-3a12-a2cd-cfd30b2f8a7f | -7.40443 | -43.3819 | 2025-08-29 03:47:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 794f39c0-a5e8-3f94-bdac-4ac384a6f411 | -6.70253 | -49.46367 | 2025-08-29 03:47:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9c99d9c6-d755-3622-9fc0-b05181203636 | -7.42085 | -44.27804 | 2025-08-29 03:47:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 175175c3-ed06-3881-98cb-6c12b05daa30 | -7.6206 | -42.68933 | 2025-08-29 03:47:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 43d20b0f-726e-382f-b39f-742d2f4ee93f | -7.96374 | -46.36198 | 2025-08-29 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b08c2e99-61d2-3cf2-9120-57fe6588393f | -6.70804 | -49.4707 | 2025-08-29 03:47:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 98c787d6-0d30-3229-9409-ca9f4e4c83be | -7.64653 | -42.66254 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5567beb8-5a03-3a90-a8a5-682101277804 | -6.70699 | -49.47637 | 2025-08-29 03:47:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| db266651-f130-341f-a2f0-b688f9455a20 | -7.20814 | -44.06467 | 2025-08-29 03:47:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e07529bc-e0bc-3e96-9975-5160050f1326 | -8.44879 | -43.71914 | 2025-08-29 03:47:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4de95c9d-46c7-39f5-8fdf-b2481e26b0c4 | -6.81122 | -44.35753 | 2025-08-29 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a530f3ce-c54c-3934-9b9e-b31e1800f9a7 | -9.93902 | -46.70307 | 2025-08-29 03:47:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a8b1387-408e-3f7c-9c1f-034a2d1736f1 | -7.64237 | -42.66176 | 2025-08-29 03:47:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README26.md)
