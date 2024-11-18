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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed114db1-e40a-34de-a488-9db0e3845913 | -2.78436 | -51.75405 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d759fe5-a30d-3767-a077-6a575764796b | -4.7808 | -46.48351 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 106763c5-8262-3edc-92ff-f39c18183d43 | 0.11053 | -51.45937 | 2024-11-18 05:03:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56228f22-671a-32f2-9167-d7544dbefbf3 | -2.36522 | -53.67796 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cc14c2e-833e-3a85-a2a0-d86fefc71c4b | -2.60213 | -51.79456 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd679d11-9405-3967-9cbc-f096b081a933 | -2.46822 | -45.6148 | 2024-11-18 05:03:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 253a75af-d8f3-3ce7-b762-2d0270834f43 | -3.31117 | -53.36366 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abc99247-c094-33fd-b12d-dd19dbaeac62 | -2.65945 | -51.71393 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73a22b4f-7e64-3bff-a7f8-9cfc6421c820 | -0.89484 | -52.72037 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59692ba7-9b20-3f3c-9c53-c83da67fc195 | -1.69432 | -54.12642 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2595d2fa-b8af-3d5a-bf15-01be3a6954b0 | -2.29788 | -49.13313 | 2024-11-18 05:03:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad55d975-333a-35cc-a3cd-8aca21da2839 | -1.63864 | -52.58802 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97358ffd-b028-305d-bf03-435d7fb6f9bc | -1.40095 | -52.41953 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d422afb2-c45b-3ae7-a6c3-0c0ae664306f | -1.41229 | -52.06318 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb9dc636-0af5-3270-bb72-837c73f4c692 | -3.83288 | -52.02413 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb7d6ec1-147a-3e1e-b5a9-c544ffe3b8a4 | -3.399 | -53.26998 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa86dd8b-fe06-3f28-8f92-29d6932e41e5 | -1.30287 | -51.74089 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2d4fd509-a19f-3b45-b916-3fa0cc26970e | -2.94322 | -48.05457 | 2024-11-18 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fd69e19-3cd7-3276-9b1d-95d0989597e2 | -2.76269 | -52.61443 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcf022bf-3ae9-38d0-8caa-037bd6794e9e | -3.52617 | -50.2445 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7fef683-e92b-345b-9434-c50df3f3d69d | -3.66593 | -50.2027 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ebad7b1-0d19-39c3-b459-05d699c7728b | -3.54967 | -54.57445 | 2024-11-18 05:03:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 928d53ec-dc87-310a-bfdd-a2a88d5b3425 | -3.11883 | -53.70523 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf87db2e-010f-3876-94ed-1f89eb01fa5c | -3.87924 | -52.26658 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2b0ae81-62b3-31f1-9266-9d468231fa9b | -2.34013 | -54.58883 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 972d823a-ad77-3865-bad3-740d3565819d | -1.60618 | -52.24113 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 631db1c2-6be3-3e69-a5ec-8c449e5e0ade | -3.52805 | -50.25926 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d2ea077-6b00-3dde-ab62-c4c9c0df48b5 | -3.18936 | -46.28313 | 2024-11-18 05:03:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6d5f8578-7713-3718-88e5-dfe69cd724ad | -2.06026 | -46.54565 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff6c531a-0de8-3b47-acbf-e2f499488788 | 0.23345 | -51.11293 | 2024-11-18 05:03:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c77f459-16b8-3f6a-a8f0-c4fa5877186d | -3.11545 | -53.70471 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 363cc498-16cb-3079-9e76-d213091b72ec | -3.3374 | -53.30692 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5503d936-b166-399c-ad18-278d397af9ee | -1.70914 | -45.83138 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 78f2a068-aef7-3af6-a5c6-41c3389ea074 | -0.05088 | -53.25449 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b4b8dd7-8e12-391e-810c-f846848b942b | -0.18145 | -60.68325 | 2024-11-18 05:03:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f767f04f-bc52-3b3a-b3da-673e38d9ea13 | -1.62576 | -53.30087 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbd4c144-0286-3be1-a768-62e665324e9b | -1.5518 | -53.09927 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fad785c9-0067-3c16-b896-0ef03b9d34b9 | -3.04832 | -54.408 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26a9f0ce-eb8e-3c5b-a0f2-ac85364f73ad | -1.2075 | -51.77398 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a327369f-0ccf-3c61-a532-9d77bfeb78aa | -2.24058 | -53.61182 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 183177e7-1320-3c0a-9472-60c79a6fc669 | -3.83882 | -52.27916 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7e7198d-1997-342c-a8fe-47595054dbab | 0.61605 | -51.77322 | 2024-11-18 05:03:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 252e4eca-eb56-3255-a026-384988fdabd5 | -2.97407 | -53.85921 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b138c6d-1660-394c-bf3c-99e5b7e46624 | -1.56124 | -52.85838 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8045286f-6c06-3f12-92e1-a14d8f4d048b | -3.33817 | -50.49868 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3145af2e-13a5-3a23-bb1f-862adf85fa0c | -2.8323 | -46.66378 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68b0b167-546c-326c-93db-1d61e7edaf8f | -2.68181 | -52.98748 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76f539ae-b524-33be-ae4e-c516d245c8f9 | -1.43029 | -55.25141 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1570da86-83be-317e-8aef-6d7c8a9e5fa1 | -0.95669 | -51.72911 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79723ed3-6d77-38a8-b31e-ecc4cba9e77e | -3.52509 | -50.25151 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf133fc4-cf08-31ac-a876-de213fb78119 | -2.6818 | -52.98281 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b298dfef-b380-351e-95e8-8a679124630c | -3.3342 | -50.49804 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 45065ac3-a8a6-3555-8260-190ff8c224d4 | -3.06808 | -53.27837 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| fdf8940d-f851-3ba1-a716-c23703b94264 | -3.34089 | -44.06268 | 2024-11-18 05:03:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f25de804-a5bf-346c-843f-e0ce9aa8bf4a | -3.29742 | -53.85738 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 778a26d2-316f-38e4-8e29-a69c1e332fdf | -3.18467 | -53.24999 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b809b442-1947-3624-a91b-be0cf7da5aeb | -1.92035 | -53.34914 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ec2211c-6225-3a42-9311-24d1e4ca439b | -1.62288 | -52.62074 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 544fd02e-895f-365a-a882-8eaa7082977a | -2.67894 | -52.98322 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c14eb88f-06fa-3765-82fb-bcb9eaf9991b | -1.20942 | -51.76165 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f0e65160-3bf1-33ef-b3e8-68d5e43d7034 | -3.18924 | -53.243 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 679a6e0a-a7ad-3c44-90e6-420994b8e982 | -2.68438 | -52.43829 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d92393fc-558d-3f01-92a5-3a571eea7c09 | -2.90304 | -53.05065 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16c41414-6ad9-3695-bc93-51ab98da2b95 | -3.74364 | -50.18501 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a17763-c5c7-3ab8-b393-e2fced58bba2 | -4.10827 | -51.06403 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe70e4c3-96ca-36a8-b094-468501941e42 | -2.60592 | -54.0168 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 814c4450-90cf-32f1-b611-9c694ab6c8f9 | -0.96871 | -51.72257 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c9138b6-1612-3249-9db8-2e14a3e09a62 | -2.86035 | -51.84654 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fc8cadc8-635d-3092-a09d-c7fdd0186695 | -3.39577 | -53.27014 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac6cb00d-00ec-30b7-a48d-2d5300c5b3ca | -3.33051 | -53.19118 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f579f80-3826-35cf-b53e-fd2189e53bf3 | -3.06407 | -53.28157 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b978b36-f47c-3d52-a6e5-6efd9e3eb9fd | -1.3696 | -54.15796 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe082ff0-f2f4-3947-80f7-4474a99fd830 | -3.62907 | -50.22641 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bdd7f27-128b-367e-bf82-e588e2d3f1e7 | -3.28604 | -52.9559 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b601efd-8e9e-3db6-a458-5433d8dd21fb | -0.95732 | -51.72502 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aca9f54-19fc-39bd-b009-c8ca58d672b8 | -1.62077 | -55.14443 | 2024-11-18 05:03:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ca69321f-1d57-39c1-acba-5b16575c1992 | -1.27645 | -54.66878 | 2024-11-18 05:03:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6db9e7f0-cbad-37dc-81d1-c734bb2b1380 | -2.87231 | -51.79165 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4741a8ec-b1d4-3d9a-865d-1ff63119b5f1 | -2.92654 | -54.12023 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5417528-e72e-3b8f-b6ad-b202f51ded07 | -3.18486 | -53.24998 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 554d957d-8f04-3646-ade5-b2074e249b1d | -0.83849 | -52.42653 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecdd683a-bf07-3e87-ae20-0e106191779e | -1.1702 | -49.14049 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37d707cd-bc1b-3ddc-a3b5-48b189a4f7e0 | -1.70332 | -45.83387 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9d50859-9644-397c-ad51-516ea48216c8 | -1.19367 | -51.97945 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc72bb42-4e10-332d-be8e-66ed5476778b | -3.07718 | -48.07238 | 2024-11-18 05:03:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d217ba50-9121-37f6-ad47-cf3afddc8fbc | -1.54306 | -51.11251 | 2024-11-18 05:03:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08d76b12-b1c7-3761-9e02-d6242a3b862b | -3.10785 | -53.74378 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 795f9750-e6d0-3dee-83c5-ddd9cb112d0e | -3.57095 | -50.25398 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 077695f1-1864-3fa5-8aea-7026edfdfc9b | -1.70478 | -45.83649 | 2024-11-18 05:03:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d772a0e0-011a-3439-b044-89e31adb3deb | -3.34266 | -50.49587 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1c219425-bb8d-3cf2-acb8-685d11c8df04 | -2.60726 | -46.2622 | 2024-11-18 05:03:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58b464d2-0cb9-3e6c-b6ca-b88db94a0122 | -2.85702 | -46.67376 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc006ffd-caf2-3986-b419-6daeb54394d6 | -2.61936 | -54.3234 | 2024-11-18 05:03:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f092322-fcca-3dd2-a9ea-e0e4c4ca4562 | -3.51045 | -49.93234 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a3cb61-081f-3b45-8fde-07961ba6d40e | -4.79439 | -46.50302 | 2024-11-18 05:03:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf301d6-7e40-3258-a88c-4fa31eb54dd6 | -2.3714 | -53.68258 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d1c858d-f460-3452-b864-9e078d239c9b | -2.3634 | -48.56443 | 2024-11-18 05:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e7d15c4-e33d-32f7-a67a-5b95e3c1b3c1 | -3.08334 | -54.66551 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23b8f784-cb22-3121-91d8-cf5408d14b42 | -1.62293 | -53.29674 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2a748a5-d190-34d0-8e22-05748b061f66 | -2.19747 | -53.66746 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README29.md)
