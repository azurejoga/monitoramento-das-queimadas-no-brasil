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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6640ea5e-630a-319c-9be9-70a196c2a2c9 | -7.87619 | -54.98626 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41a16b35-9dbf-38ed-8d50-8047c6d8f3b1 | -2.96498 | -54.1428 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fabe0607-58e4-3e4c-a39b-d8c46c3ca8c0 | -4.49856 | -55.48699 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96a8620a-735a-3117-9ac5-dfdae0cc3fac | -3.1106 | -53.76891 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10d8b512-86bd-3d0e-8a05-946aa9575044 | -3.59215 | -54.66104 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2f6edd78-3267-3605-a08c-ecf26c129940 | -3.02651 | -53.94725 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a3c1801e-0431-38c4-8cca-7e93fa7d357b | -3.48105 | -54.62681 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5f063b1-79f7-3646-8e64-339a3ef63615 | -6.12832 | -55.69105 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c79354c8-1bdb-3f30-ac2a-e9d9d301f202 | -3.99329 | -56.25557 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc53b914-62bc-3c6c-84da-c84985b65221 | -3.12768 | -53.76174 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b381eb1-45b0-3d75-a98f-75d0a0f827e0 | -6.01193 | -53.54499 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6343469d-af98-3bc1-afa5-13466f14068a | -7.87997 | -55.0089 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49f531b6-f4e0-32c8-9bbf-e44fa48e297b | -3.74111 | -59.44783 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36f00247-343f-3c1a-8490-ba726d7a8801 | -3.99037 | -59.21922 | 2026-10-08 04:46:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dfe7d3e-26f4-36ea-9794-003ba690d36b | -3.13113 | -54.36647 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4fbff341-accd-39a1-92ab-47ae4bce27f6 | -3.64612 | -54.51481 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a138951-0288-3472-8b97-81f83b2d1589 | -8.29334 | -50.2673 | 2026-10-08 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00d44e56-0356-32c3-9b7d-d6ab0d72bb34 | -11.63297 | -43.69349 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b642c610-0c57-39cf-928f-913a06a13c8f | -3.61849 | -55.50083 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6bd00d3a-4df4-3ad1-ad58-f8a22d37383b | -2.48493 | -56.11034 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 297da248-093d-3086-8586-eb1e6674a0f7 | -5.72835 | -45.16736 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| adcf18ca-29cd-3f8d-8176-560baaf5fd8f | -3.03384 | -53.94837 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f9fc5be-18d8-34ac-b388-649417e3657f | -4.07377 | -59.8495 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9989a380-0494-37a8-ae5c-c30d85677ef6 | -3.12628 | -53.70161 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 64683c7e-e242-3e20-9e10-88c978606e08 | -3.54462 | -50.0965 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de6c508c-0095-37e7-9d65-2fc6ca813a34 | -2.5095 | -56.17456 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 27cdf093-6ee0-3507-8311-9a44dd9978ad | -5.29817 | -60.10374 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ff81e96-4b38-3219-807b-ef188d0087ab | -7.37982 | -46.24289 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acff0d2c-c013-3b8d-bb0b-fa9625690284 | -3.60984 | -49.50157 | 2026-10-08 04:46:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72d116cf-2bfb-3756-bbe0-0716998380b6 | -3.30678 | -54.6958 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ba81ad7-cbd6-31a4-88b8-9dbe35239a18 | -3.36264 | -50.4791 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 34b362c1-a7fc-38f8-9f1b-0248b73b8c34 | -3.30176 | -53.86573 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c1f8f90-9136-3674-b3bc-25557ac1e1f9 | -2.50455 | -56.15004 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d9651251-14b8-3bdb-9c9e-02fed4d78106 | -3.06075 | -54.24676 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fc16601-98cc-3e2f-ae6c-aae7439b41fa | -2.61147 | -57.58157 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb66ce91-f632-3144-83a7-04d420df011d | -7.88362 | -55.00948 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1ef3bbe-3c57-3603-8676-ed14735338ba | -6.12234 | -51.69727 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d149044-bf85-366a-b90c-941cdaae0a24 | -7.22313 | -55.12449 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a0d8b163-0501-339f-8044-6187e1dd8fb2 | -3.01481 | -54.09189 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4546983c-c1e2-3b76-988f-a8d0e236b2ce | -2.57888 | -56.17366 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e85b5827-cfb8-33d1-85ec-a6949c6e45f1 | -9.81844 | -44.78079 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80260db2-dd8d-3dce-a2a9-70d1abddf241 | -3.25353 | -54.66587 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81205fe9-79a1-37c2-833c-7c2da485166d | -3.02634 | -54.06684 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94f67e35-cc2a-3fd2-a1ea-90ccf168c587 | -3.14886 | -53.72221 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 42097b80-4ed7-32be-9d8e-1d237e0b34e7 | -8.08433 | -55.29967 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c37cbac8-aaab-3efd-828f-bf10edea8ae9 | -7.88208 | -54.996 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7abff909-713a-39d5-8ca0-6348f23f24f1 | -3.07596 | -54.29473 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ddeb95c4-047b-3504-9076-5185cbbb0f1b | -3.22223 | -53.96681 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f142b70-7a95-3dbf-b6a2-9b31a97a188a | -4.11096 | -54.41028 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0cb81483-e0bb-397f-8075-150bee0bdeda | -3.58459 | -54.65981 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74e77401-0872-38c0-be2d-ab02ccbcf13b | -5.73438 | -45.15612 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 35d62c5a-72af-368b-a062-8c5c6edf6cd9 | -6.12246 | -51.95757 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 277141ad-5072-3580-a8b2-3251c6a244bb | -4.5697 | -54.95662 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ee68c3fa-3d52-35b2-a3f4-656b95fe4785 | -3.03563 | -53.91353 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f2f3dcb2-cf5c-3c80-ba7b-8d0c8c2e7dfb | -3.59442 | -54.24126 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f5e0ba25-84d3-3703-afa6-ac248063642c | -8.73076 | -45.16502 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3facca32-a044-322c-8176-8db2c0d568ff | -5.89839 | -52.03971 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e26e9476-7494-3924-a4eb-a576d8b1997f | -3.35711 | -50.47123 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4f4ffda-92e9-305a-b21c-0bf416a1f8d1 | -4.11669 | -59.87744 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b6c0f030-fd80-3232-b9f6-27ba85e75d69 | -6.16022 | -39.43818 | 2026-10-08 04:46:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d0ae4417-a54d-3cb7-bcea-304d4517d5f1 | -5.76182 | -42.06581 | 2026-10-08 04:46:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 44093d6b-5fb1-3943-ad7c-c2ee8b38b5e4 | -2.89728 | -54.07534 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fa1c087-1f6f-3dff-b1ed-0389ddecb001 | -2.76486 | -54.10512 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e03456f-03f2-3fc9-861f-bb2906c5bd61 | -2.93936 | -54.14497 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 635ad437-121a-3c66-b58a-ab8b8eafd7bd | -3.5428 | -59.50381 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 361fe80f-5694-3212-ae04-fa32c93db3f0 | -3.06066 | -54.22372 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16d306df-dc76-3bc2-9aa4-7118a64aa4b2 | -5.25404 | -55.91956 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b086448-7fdb-3d33-a8c5-6f39183f9ac2 | -2.51376 | -56.25323 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| de9a30d1-0ec7-3040-9003-6cabac635352 | -2.48965 | -56.13519 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 416746b7-d5a0-38a7-aae8-6f97caf7ba44 | -9.82776 | -44.78206 | 2026-10-08 04:46:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d77efda7-8d97-3237-a567-5823be2f719a | -2.93993 | -54.15676 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f3228e58-08a3-3f1c-a30a-adcc6a75970a | -2.99725 | -54.10712 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b372bc63-9bf9-3a5d-9980-2187cfd39087 | -3.58849 | -54.6841 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| ce582277-a38a-3797-ab09-2f2cd1d49251 | -4.28131 | -50.78529 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16ee6a20-e3e4-3023-b119-ada0077916f5 | -3.32557 | -58.22961 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53716386-93db-3037-b645-7b7ffa36f0da | -3.22296 | -53.89253 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a36aaaf-0386-3c60-92f3-95bd76b0a59c | -7.08041 | -52.68075 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90be044f-ae72-33e1-adec-ed8e656280b0 | -5.11214 | -47.12454 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e650c579-579d-310d-819b-12c146319919 | -5.11282 | -47.12009 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf4af856-ce1c-301e-af9b-c19781ca3e6a | -5.84039 | -50.14447 | 2026-10-08 04:46:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e1bc0bca-5b16-3741-b660-0914c252b6b1 | -7.46707 | -42.85536 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 28e37eaf-45b3-357f-91e5-8724243c434c | -3.0352 | -53.93977 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 094edba8-3e0f-3e38-8550-0e7ccd7f0462 | -3.10269 | -53.77203 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9dff177e-5f93-3798-a53a-e4c1caa76f34 | -7.18786 | -44.33674 | 2026-10-08 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f289e02-b117-3b5e-b202-1b75a3a98643 | -2.89825 | -54.02185 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe365f0a-941f-3325-9a29-430586026c2b | -2.97381 | -54.13516 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 09613d0e-80c7-3522-9d5d-1fe4377a11c4 | -2.48666 | -56.12671 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2ea9972-71e6-3627-a517-2b212ba3ac08 | -3.01824 | -54.14194 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c9a60c1-4ef6-3bfa-80c9-c2bd35434dc2 | -4.60967 | -55.72097 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c26a88a1-9442-3e3f-95f9-3036a079d429 | -4.06902 | -59.84513 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 990cf811-e366-311d-ae89-0945f38e32e2 | -2.48915 | -56.11104 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4602058-fe8b-36a9-9e5a-557444969736 | -3.35934 | -50.4786 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfac7577-51b0-326c-bbb8-c342798e1104 | -9.59317 | -47.78136 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2bcea412-3b35-3547-9c39-0b564b785aa6 | -2.99885 | -54.12083 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa6c125c-18be-35a4-907e-bfbac9ac7a58 | -7.46869 | -42.84315 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40bc548f-b44a-30ef-a88b-42ab5f96edb1 | -3.12224 | -53.79543 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ca323b90-682b-343d-81f6-a7cb00486714 | -3.84966 | -55.97588 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd86b80f-0703-3806-92dc-38b48b1ac000 | -3.17202 | -54.73477 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaa31814-f010-3591-b632-f889cc23132d | -10.32894 | -46.61405 | 2026-10-08 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2480283b-419e-3d77-8ca6-fbc38b8b3ada | -10.96604 | -45.39837 | 2026-10-08 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README105.md)
