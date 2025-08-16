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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34c96a76-36cc-354a-8fcc-9f27236f97ac | -2.82406 | -49.1448 | 2025-08-16 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cf56a5e-7f81-3812-bf46-eaed5fc2e3e9 | -8.31596 | -47.58846 | 2025-08-16 04:32:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d984f794-b548-3a49-ab20-caefa1b8fc8a | -8.16902 | -45.02156 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bed3709f-cfa0-387d-ae4d-c74315aeba1b | -8.42995 | -49.61762 | 2025-08-16 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5288f719-023b-3751-aab0-9ca8596b6281 | -3.82236 | -47.739 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e77eb364-46be-352c-9733-ef3005eea0d9 | -6.54151 | -44.53999 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 160e3b8b-e69f-33da-9f8b-d3ea28e0a6b1 | -7.59915 | -55.19445 | 2025-08-16 04:32:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6415173b-08a4-399a-89c8-6135cf9bef90 | -7.53262 | -50.52641 | 2025-08-16 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 10dfd3b4-c9e4-3b5a-8a73-28379d4260d8 | -7.40795 | -44.89107 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b31c1e20-8df5-3ae3-a365-7223dfc88a05 | -4.14666 | -46.45499 | 2025-08-16 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8962f04e-49fc-3f56-bb4e-81dc0f88ab47 | -7.69112 | -48.00079 | 2025-08-16 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7f9010c-c554-398f-b9ea-8525829f0165 | -8.19149 | -45.02065 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 024be052-cb75-365d-9a03-e5a0e680925b | -7.50408 | -49.75017 | 2025-08-16 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66e86b74-753f-3346-b1ca-957c9b328d0b | -3.59335 | -51.06515 | 2025-08-16 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8de82db-6d8c-3f1a-bab5-6ebb48f9a0dc | -10.92514 | -43.74447 | 2025-08-16 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dca2ebb2-93b2-3da3-8118-269edf9a860b | -9.36517 | -47.97976 | 2025-08-16 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| cb6af7c4-832e-33ea-b9cd-d921a915fcf2 | -9.81081 | -48.53758 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c326898f-199c-3e39-94d7-acdc19fdd981 | -6.93713 | -59.54537 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7588e139-6ba0-30d3-a724-bb656b323310 | -7.07555 | -59.23818 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 22a0b85a-6f6c-3022-a109-9caa125f93ce | -7.92358 | -61.74423 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b13d95ee-a163-3c50-8e1f-7afb1fff8f21 | -5.9333 | -53.65123 | 2025-08-16 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4425bd91-f568-32fc-a8a2-a6de608d7f3b | -6.69728 | -58.82295 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eb4d5976-6d70-3f3a-93a3-f985b1029fe3 | -7.38475 | -44.92222 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 647699db-0fce-3caa-b3c5-7de08db2f943 | -8.18594 | -45.03279 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 754a6b47-5411-3bf6-874e-085a2c47d340 | -8.34378 | -44.95137 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2d353ba-8619-3df2-bde9-cfea3e7eae42 | -7.14669 | -44.38685 | 2025-08-16 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1ec86f6-403f-34a6-a082-2d6991efca87 | -7.40197 | -44.88132 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d55d527b-a5bd-3a46-b8ae-af1c9e33697e | -4.92079 | -43.26158 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b7816203-7099-3747-97a7-d2c9dc4b63b4 | -6.94063 | -59.52621 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf6516a3-8245-3e5c-9c13-d96471cd1624 | -7.41823 | -44.89676 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c801cc64-10c9-3905-b2eb-e37cacf4900a | -6.93797 | -44.56169 | 2025-08-16 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8696a415-2df4-3dd5-bf9f-5eafcba025e0 | -7.70568 | -46.18797 | 2025-08-16 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 895598ef-6750-36c0-abb0-a092d2d74480 | -6.57925 | -42.23365 | 2025-08-16 04:32:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 55549489-b540-3bac-900f-7642df82df45 | -6.22095 | -44.46155 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f691e499-d84c-315f-aec3-15722f906899 | -6.55917 | -43.02749 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 025ab70c-d99e-32b9-ae33-29402bda766c | -7.41394 | -44.90061 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51fcdb17-80cb-39d5-9f3d-f13b3223096e | -8.74638 | -44.04744 | 2025-08-16 04:32:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbdcac7b-6127-32da-8e6a-8d43dcfbb376 | -7.66238 | -42.22765 | 2025-08-16 04:32:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9eff6b9-5b4e-3d82-8253-748738f090a3 | -7.91794 | -61.73636 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| f5678fca-6ba2-3d4b-849b-478c656d7bc6 | -7.90853 | -61.74807 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| aecbbdce-840b-3cc6-ae50-21ee7b99fa29 | -7.01689 | -44.31607 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 214a7403-1bd1-3096-9e79-3c2dd0573417 | -3.73437 | -53.98029 | 2025-08-16 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cb6228b-1a80-38c1-8a94-553407158fa7 | -4.91692 | -43.261 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 75607771-a0aa-3c5b-b958-ac66ef3b2847 | -4.08779 | -48.80668 | 2025-08-16 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faa39163-395b-307f-9d45-32cc3cdcb31d | -7.23971 | -44.79137 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bfdff5e-36d3-3dd4-b26d-64155b99680a | -7.40516 | -44.85988 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0913e94-3847-3bf5-9616-8164d808d540 | -7.53097 | -61.34122 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a85510e-2ffb-3d3d-b4b4-ef9123565345 | -9.96517 | -48.33339 | 2025-08-16 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0580a367-2d52-39b7-a18a-240a1c7aa342 | -3.74206 | -48.92989 | 2025-08-16 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bdc9356-98ff-38ac-9cc4-1c435705515f | -4.22416 | -47.21684 | 2025-08-16 04:32:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21560c75-af9b-39d5-993c-5cc9a8d62d22 | -6.60783 | -42.75784 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 21632ae1-7ba3-37eb-b296-004df8c96826 | -6.56013 | -43.03185 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 8a36bc60-0d84-332f-866f-49ee4f3533cc | -8.17994 | -45.02324 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c6a12a3-3966-3222-badb-04952be4db2f | -3.48759 | -51.18885 | 2025-08-16 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ba2a03f-2656-36a6-98c1-b2657d3159f2 | -7.97414 | -43.96372 | 2025-08-16 04:32:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1640178d-5ed9-3c18-a8e4-cf7f7050a110 | -6.60836 | -42.75419 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fdf15f2f-a2a6-3073-b523-582b0824e82d | -9.85454 | -44.68412 | 2025-08-16 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4e51bf6-d97b-3262-9df6-a850e54ac959 | -7.01056 | -44.31813 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 564e4390-1c67-39a2-9c19-05318b2a1e77 | -7.53325 | -50.52256 | 2025-08-16 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9988e5d0-568c-3d11-bcac-6b7a18ae0bef | -7.532 | -50.53026 | 2025-08-16 04:32:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0db0cce-da3a-3d9e-ab23-b720f100f706 | -7.0635 | -59.23596 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f063038c-1db0-3444-adda-600dc22be62a | -9.34802 | -50.25211 | 2025-08-16 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c4f05083-f0e0-30e9-b0fe-1f4c65cc347e | -6.66469 | -58.81442 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60acf059-1f77-323b-9507-ccf5d4850b9e | -6.85848 | -42.80619 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9eaca9ea-b2cf-3963-8bf9-8fa31853da14 | -7.91414 | -61.75608 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3d576fd9-8abe-368d-b3f5-bdcc006d0ec1 | -9.7014 | -46.26937 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fdcf21e1-8a61-3c6c-884c-129a1fedd01d | -6.95207 | -59.53323 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52219220-b29a-3d0c-990f-f3b8f707c0f6 | -7.12527 | -59.65472 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae7e44c-aa8c-3578-b9b2-db007c53bf44 | -9.26849 | -44.54243 | 2025-08-16 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e26d7648-4e5b-38ab-8b11-7d14cf5bb7d5 | -8.1763 | -45.02269 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26cf1d5a-824e-313c-a4f7-6da6dff21fb0 | -6.60428 | -42.7535 | 2025-08-16 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 7075ea73-5e54-36be-a636-54d3ad14d788 | -9.85207 | -47.81399 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d61880bc-0c21-3c58-934d-92fe70c09492 | -3.10877 | -47.50353 | 2025-08-16 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa7f634e-cfe5-3b9b-a803-2fcaaf503a8f | -6.55612 | -43.03125 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4c0bf95f-f3fe-3bba-9a49-c3f51ac4b0ad | -7.51965 | -61.31974 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0a1cc628-e0b8-3288-8725-2921de6e26ec | -7.58812 | -45.15965 | 2025-08-16 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eaa4005-42b3-384c-8f5f-fab5cdc663e4 | -7.07641 | -59.23356 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6b372792-9f94-3fab-8f9f-00bc22744764 | -5.76036 | -46.66766 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7036b478-00e0-3452-992d-0172cf205a10 | -9.70429 | -46.27383 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdcb73b5-cacf-3ed9-a1b5-4b0a1efa5611 | -9.86098 | -47.82262 | 2025-08-16 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f09de02b-acd2-3d53-91f6-0a4d0ca19d7c | -8.29711 | -44.96523 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 508b8698-7b8b-3fec-ad2b-80e8936a7169 | -6.93009 | -59.54903 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a2dbd52d-18ea-3223-b423-0661fabd7a46 | -7.37674 | -43.82756 | 2025-08-16 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4194f3f-88f1-30b2-bc44-3e50b7a4bd08 | -7.07539 | -44.94043 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc61b577-7f51-37b3-8f5a-8e264579e6ea | -7.66667 | -42.22833 | 2025-08-16 04:32:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d17e0d0-ad52-39ed-9cbc-4be8f6a66b7d | -13.02693 | -56.86958 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff6a3289-91c6-394d-84cd-47f2ba5075c3 | -11.93013 | -44.1249 | 2025-08-16 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bbe4f59-a2c6-3579-84b7-cf368818a1a2 | -14.94187 | -54.69468 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 7b9f5d8f-fd13-3fb1-8096-61591b9a17d9 | -11.2087 | -49.32179 | 2025-08-16 04:34:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4db5afb-6f9d-35cd-9456-403543aa2557 | -17.61538 | -46.70572 | 2025-08-16 04:34:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c2cafe4-ce23-326c-9a52-af3e60a1b8c8 | -8.9685 | -61.68717 | 2025-08-16 04:34:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 759ddf32-1a8f-3962-9e95-27a78590ec42 | -15.90293 | -48.32069 | 2025-08-16 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3237c002-daba-3c1d-80fe-bf817c8dfd01 | -16.23714 | -51.12819 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37c09a27-b975-34cf-951c-e049b5fa0072 | -11.36054 | -55.42031 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a4664eb-095f-3a99-b7d4-3a3a8b44f265 | -12.60457 | -46.91293 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bb4ce964-abc0-3b61-99c9-972f49470b8f | -12.55893 | -46.94752 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 5c672beb-11b5-3161-901f-b5a76a01ca35 | -16.23891 | -51.11724 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adc61778-3075-3c24-b3bd-d91dd7e5b34e | -8.9873 | -60.52708 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 91a5f37b-0913-391e-a725-4bfc818f2548 | -10.04022 | -59.12247 | 2025-08-16 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 417c3fff-5405-3cd0-8cd5-03b5ecc26baf | -12.23224 | -41.3899 | 2025-08-16 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README41.md)
