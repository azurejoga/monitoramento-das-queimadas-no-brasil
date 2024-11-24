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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b0420b6-d0f8-3e5a-b891-ec3bfd596437 | -3.9497 | -45.9908 | 2024-11-24 04:53:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 754391b1-640c-3a53-ac22-f7e30b2dc843 | -1.08464 | -53.64113 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8e3c2ba-b0f8-3055-9245-a584f2329915 | -3.50095 | -51.05679 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 854e6eba-f414-3077-ab74-56fa3e3c4d22 | -1.06623 | -51.75474 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a808cf45-ffac-3043-b181-4f1a03098eba | -3.33755 | -54.62714 | 2024-11-24 04:53:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36ef6e11-9f26-33b7-82c2-8123f0f7b42a | -0.8536 | -52.24646 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3d195a0-3d3c-3a6c-8e76-d2b143317c53 | -3.76036 | -49.9369 | 2024-11-24 04:53:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a49ee57-6a35-3cd1-a4ad-629a9d18535d | -1.04972 | -51.7522 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4015f45-9131-352d-9eb5-88dc50617617 | -4.25432 | -53.53294 | 2024-11-24 04:53:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 058a9ce0-2d5b-3807-93dd-1ed58185541a | 0.87702 | -54.6343 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6393d420-e3ea-3d22-8f9e-011c98e50da3 | -0.92441 | -51.64149 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56f3f604-ccbc-3974-a7ea-fad1ca44f547 | -2.27946 | -50.57911 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 59af7872-62a4-3eeb-bd0f-eccbd81027ec | -3.19086 | -51.61235 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cf8275e5-f514-33c7-8af3-9d41f232b23a | -1.41896 | -51.13086 | 2024-11-24 04:53:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed893846-02ad-31c1-8e61-fea463f3837e | -2.10021 | -50.70805 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 825927ab-70dc-3c14-88c4-fc011ac040dc | -3.2383 | -54.23027 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 69e4f7db-7591-34b9-bfa0-2a1c74a0c53d | -2.28465 | -47.30909 | 2024-11-24 04:53:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6c943c22-9a74-38fe-b550-5fc46c732c4d | -3.24578 | -54.22758 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4f2f589b-56ba-34c5-beb8-8c23e5bc8f77 | -1.13011 | -48.34015 | 2024-11-24 04:53:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f0cb2ef-104b-3edc-ae25-ad3a27276172 | -2.46236 | -53.69839 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9d32dac-4a3a-3a0a-8e46-68dd12eb236a | -1.06464 | -53.18309 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41d07c6b-2a17-329b-9f84-633f859b55ee | -0.92825 | -51.63857 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b67a3de3-3d84-363e-9028-d68da0d1e6ec | -1.2759 | -52.9816 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4fa0821-aec4-37dd-9ef4-29e66d49e50e | -2.2453 | -50.47543 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcffca78-da28-3746-8175-8e1e9027a024 | -2.99764 | -51.45465 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f28e109-4b9c-315f-a362-358e367344bf | -2.06292 | -48.96568 | 2024-11-24 04:53:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c76b510-812a-35d7-891b-bfb96d3ba9c6 | -1.24776 | -51.74836 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f966bee0-6756-3be1-803a-b3d11be9a424 | -2.54788 | -53.97944 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63905a1c-c2ce-3da3-9422-190650153539 | -3.49393 | -49.90947 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5db0f21c-0096-3857-ba55-3761acecfc2b | -1.75422 | -52.6645 | 2024-11-24 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e575bca8-5705-32b5-a00b-003094f91e45 | -2.17473 | -50.50848 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c593c41d-1102-3476-9f24-d00fb9f5dec8 | -2.73643 | -46.10011 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dc2ac229-a062-31d7-af5a-c96e64f98ab5 | -2.00728 | -46.28761 | 2024-11-24 04:53:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 603b8e62-8656-3916-b7b2-6a1f978b3623 | -2.20745 | -53.75725 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0696fa37-b873-31cd-b092-4b881782fefe | -2.57765 | -54.23337 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4e9febf-f774-3995-91af-d68e8bbf5993 | -2.84441 | -54.01353 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8889d3e6-664b-347b-a910-d0529d64bf39 | -1.11287 | -53.39384 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 074fca1e-d4f7-385a-ab9e-983f389b2225 | -1.29058 | -51.73388 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e437206-0e7b-38bc-b3fe-e3e41dca03c1 | -2.43356 | -50.41977 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e79060b-f25c-3c95-95fa-8545b07d88a6 | -0.34471 | -51.97597 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcdc1544-874c-373c-b887-8024f49af609 | -3.23148 | -53.63191 | 2024-11-24 04:53:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a70f369c-b58f-3ac0-8702-df2dbfa0a343 | -2.8617 | -53.97072 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 02244cd4-109c-3c40-aa86-f141b4755a91 | -2.10141 | -50.13554 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 313e4388-c771-3f57-8e2f-631688ce9bad | -2.44722 | -49.22085 | 2024-11-24 04:53:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 08267a64-6fa6-3fe9-a88b-9ecc68d45c9f | -2.81124 | -54.02357 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a338f02f-eaae-39fa-86f3-eb5bf36a390a | -3.59272 | -49.35645 | 2024-11-24 04:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5af33f14-1798-3f91-bb7d-3435c16517b2 | -2.32003 | -51.30664 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 57ab345b-463d-34bf-bed3-c2ac3533a257 | -4.31316 | -48.07798 | 2024-11-24 04:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9837eb7e-3ffb-31ff-831d-88b23e49a1ca | -2.70353 | -51.99017 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dc57e415-0d60-3735-a412-639717db889a | -2.15986 | -50.91483 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88092758-92f3-3670-90af-89c54d573957 | -4.51442 | -45.71941 | 2024-11-24 04:53:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19a3514c-ece2-3859-b5aa-2688fa687340 | -1.22983 | -51.79825 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a0998a96-20af-3238-b1e0-076825da978b | -2.81407 | -54.02782 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a808e0f9-978f-3521-9398-697f061bae7f | -0.446 | -52.11166 | 2024-11-24 04:53:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5027488-b118-3ee2-b4c4-812acdb45edd | -3.78226 | -51.41621 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 575d7aed-9d43-3be6-8134-9a6a572492c5 | -2.57979 | -51.88659 | 2024-11-24 04:53:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 07ff9918-49b4-398b-9fdb-a2f775a281ad | -0.25587 | -51.63169 | 2024-11-24 04:53:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97a7bc20-ad49-3aea-b1cc-2bcf82d635f0 | -2.69558 | -51.799 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d15ea80-0f22-37f2-b49c-b68ae7687cb0 | -1.14627 | -53.4026 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c42e3e81-f7b9-31d1-bbde-b464a42ad37d | -1.28007 | -52.23878 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b59f792-8f66-3fa4-81b3-2ba3de88d6a3 | -1.42709 | -53.38284 | 2024-11-24 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0285ec13-93b8-35ba-bccb-7fceb87bca44 | -3.11609 | -53.11322 | 2024-11-24 04:53:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb6939f4-b042-3faf-b646-086099c55c00 | -5.10393 | -43.15049 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 340232fc-753f-31f1-9cda-5e086863c8f0 | -3.70188 | -47.60134 | 2024-11-24 04:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d609290-e917-3151-a7f7-1a858442abbe | -2.32026 | -53.86482 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 64b213c7-b8cd-3316-bd96-1525e657381e | -1.89825 | -50.95647 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ea652a2-5411-3213-9b3f-d34c10e75b69 | -2.35195 | -49.03976 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 641d3737-6d4c-3e74-b153-3bbd82fb084a | -0.95412 | -51.64606 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82446293-da94-329d-8c70-b34b5ccf2e57 | -0.8175 | -51.6069 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 220e8d66-5fe6-3b94-b830-295306571f00 | -1.55151 | -54.33916 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e529320-0db2-3a13-b064-b6ffa752cd59 | -2.41134 | -50.31653 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e77360b-12bf-3071-83fb-7d8bb15fdc9b | -0.94812 | -52.40299 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef02e4ff-03f0-3f6f-a19d-ee4f9133bf20 | -2.71565 | -46.10176 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d7b7d8d1-e77e-3afb-8a39-f56649350714 | -4.52361 | -49.16779 | 2024-11-24 04:53:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d81e7a7b-3261-3239-af70-a8c6535aa0b5 | -2.66223 | -46.60322 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73d67837-406d-3528-a07f-93c61124bf82 | -2.70005 | -48.82507 | 2024-11-24 04:53:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a030208c-a608-3895-b862-9793cad04596 | -2.80386 | -54.02586 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d75fb04-73d0-33d8-bbd3-fc6e9bb56761 | -4.85532 | -50.82349 | 2024-11-24 04:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e37c96dc-ccd8-36e6-97de-f6ec774f93e7 | -3.02057 | -51.24129 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 091385fe-7129-3952-a4d1-d837eb352d14 | -4.2154 | -50.69697 | 2024-11-24 04:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7f67baa-9977-35b9-a9ab-a14c132fbb8b | -1.1458 | -51.6828 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8e22483-9533-349c-9750-27a896951a64 | -2.04529 | -49.72993 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69641143-322b-3edd-a24e-b1e590e56ba3 | -2.45051 | -49.08229 | 2024-11-24 04:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6cb8b9f9-5d84-3902-8129-23d916ce433f | -4.52923 | -42.90486 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9642747a-792d-39b4-b47b-1adab6edc10e | -4.54514 | -42.91105 | 2024-11-24 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0bbbb3e-f54c-30b2-955c-85cb0dd829da | -2.23278 | -53.66362 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f858115-e172-3cb2-b624-72b398f85a2e | -1.88947 | -53.32139 | 2024-11-24 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7438c3a-c728-3c33-a07b-f96ddda5bc05 | -1.63696 | -55.14095 | 2024-11-24 04:53:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c595e78-51d7-396c-aaa5-573d229c19e8 | -1.92909 | -54.43129 | 2024-11-24 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6753c67-187c-3942-b127-42af19493002 | -5.35633 | -44.06913 | 2024-11-24 04:53:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8bdd3fd1-7095-377e-8e13-3b77969db037 | -1.04802 | -51.74141 | 2024-11-24 04:53:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68453dee-37f6-3b45-abd4-81bf82d2b68e | -3.58917 | -49.35589 | 2024-11-24 04:53:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f03d1ea-949b-3663-9cf7-cac986c73137 | -2.2034 | -50.54574 | 2024-11-24 04:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20641319-9772-3dfe-87fd-604b1e8180bc | -2.32382 | -46.34167 | 2024-11-24 04:53:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1b22548c-b4b7-3030-93e4-e1f10ce7ce0c | -2.38558 | -49.84131 | 2024-11-24 04:53:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7640f490-3657-3088-a460-5bf4fb5ba1b5 | -1.21911 | -51.73694 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf6a8386-d55a-319c-be30-5acc60899ef7 | -1.26647 | -51.6284 | 2024-11-24 04:53:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2d4366e-58e8-361a-b20f-63944935036a | -3.24174 | -54.23079 | 2024-11-24 04:53:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7382e22f-1398-32cf-b7c9-d0e4434943e6 | -3.04322 | -51.26973 | 2024-11-24 04:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f82d468b-873f-30c7-8132-d464fe6da391 | -2.10477 | -50.1808 | 2024-11-24 04:53:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
