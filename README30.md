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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc674f60-33cb-3a77-81b5-8ba99d4088b2 | -5.08573 | -46.21804 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d192853b-f8aa-30e1-94eb-5225b5cbba1b | -6.42602 | -55.27109 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 373f0240-6f07-36d8-9a3f-51e6e85e0559 | -5.83779 | -44.92937 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6ec3a591-5c46-36b5-ae1a-38fc55157b70 | -7.07132 | -41.59501 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d4343108-4887-3641-b400-0610786a6e77 | -3.25612 | -54.18994 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 30226d3a-4a4d-34cf-b830-86af3126dbc9 | -3.40482 | -54.19057 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ac4a11e4-923b-3a59-b68e-de3d81013979 | -4.4112 | -49.77928 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 722ab507-17a5-39d4-ad71-b33f8fb99662 | -4.12041 | -54.03456 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7a1c5547-fde8-3b5b-abe9-a76344610159 | -3.20322 | -53.86523 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a3f207b7-d24e-3911-b3b8-e620c29f0b91 | -7.03394 | -47.66285 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d3f8fb4d-b007-35dd-9f6c-75bb7540a080 | -6.9487 | -46.12849 | 2026-10-10 04:08:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6b2cc4e8-01f0-37be-bd11-738e724b0e04 | -4.61021 | -49.20798 | 2026-10-10 04:08:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a32f4895-daa7-3f38-a85f-54ef824908f3 | -3.0083 | -51.01163 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6519d22c-a84f-3e58-a52c-022ef2ee4476 | -6.07836 | -43.99784 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03f5268f-58c4-3480-8f45-305db8963942 | -7.02154 | -47.68516 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6a8c90be-c50c-386e-96c4-64dfdbf77d64 | -8.24258 | -46.43169 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7674349-ce80-3008-9039-bfc3e29e2cad | -3.11135 | -51.68948 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fea18506-29e6-3e36-a202-b5a2d5ae1284 | -3.26984 | -50.39156 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38d24e8e-e727-3926-8ea8-15970def4695 | -7.18769 | -52.63475 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 985a8c13-a2f4-3ef5-a657-fcda9135211f | -5.99341 | -41.36822 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 35e08540-4082-360b-aa90-f761dc4a24fa | -5.75569 | -41.76107 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e74db701-87ac-3216-9c26-867fc2bdbc7e | -3.01334 | -51.01637 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e3d0884-5681-33c7-a2f7-03c5b49e9e41 | -3.35124 | -50.41583 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e85be93-6dc1-3cf8-b58d-783244694e0d | -5.76092 | -41.68438 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| cb300d7b-3543-3521-bcd9-bcdd4c4b051d | -9.90192 | -44.77919 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20608514-da8e-38bc-b8ab-cbece5ec0692 | -6.13121 | -44.12408 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd18a03e-fa8d-3b64-9890-ed27ef7c4cda | -6.99807 | -47.72136 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14ca3ca2-fa52-39ba-b506-5f277740807f | -7.48655 | -42.85082 | 2026-10-10 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 54dac7d0-0444-3bae-9cb4-bb7ba143e636 | -3.50106 | -49.94483 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 495b392b-de8b-33be-9702-74f4be07c280 | -4.67375 | -50.44766 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbb91431-a0b4-3380-9eb1-e8a11d1987d0 | -5.7078 | -41.65137 | 2026-10-10 04:08:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| be1cf47b-6f73-3b51-ae19-85afe631fe00 | -7.00008 | -47.70937 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c91d18cd-e58e-3735-ad3a-a6238d40906c | -7.91313 | -54.72153 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c52b68ce-b004-3778-96bd-ee1a9e23594f | -7.45778 | -42.83907 | 2026-10-10 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1432fda-99b8-3662-9dc9-1ad89969d04a | -5.71799 | -53.49393 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d3b9aff1-aa20-3c05-9310-cfbf38006d73 | -6.07777 | -44.00153 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9f4487b-37c3-3ad7-b0ce-8b3e807caf4f | -4.40243 | -49.77969 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62f3a7f0-db3c-32a1-a05e-ce12b8fec10f | -7.87976 | -49.80414 | 2026-10-10 04:08:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 485ae7ba-310d-3ce7-831e-085d9ea64b70 | -4.40951 | -49.76853 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0ee5be0f-869b-3d03-a77f-1d929842367a | -3.17381 | -44.29774 | 2026-10-10 04:08:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d665348-4358-3bb3-93e7-0351bb39ec2f | -3.04046 | -50.34145 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b530083-634e-35fb-b0da-e08c32ad632e | -4.05758 | -50.96576 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7da4e92d-e1df-3b67-bb40-1e2d79af93b7 | -9.32136 | -47.63249 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb1bcf68-6999-35e5-84b8-f12757cf7e6a | -8.98569 | -47.54016 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 448ed20e-b507-35be-968b-ad4df2534f97 | -9.76843 | -44.77718 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 593efc9b-52ba-389f-95f9-7a39dd8df7cc | -3.58915 | -54.59909 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 70e1c9aa-c133-3323-b03d-ecc1732e7578 | -3.26502 | -50.38719 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f2e0282-8376-3e1d-b5c0-f5b45fca6517 | -5.86707 | -37.27875 | 2026-10-10 04:08:00 | NOAA-21 | AUGUSTO SEVERO | RIO GRANDE DO NORTE | Brasil | 2401305 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5eff894d-ea15-38bd-9188-2487f8b37fa1 | -4.40853 | -49.77451 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d3dd5516-d981-33f8-af3a-e262d493b2bc | -9.88625 | -44.78842 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e79da483-9072-3f2d-b4f4-1a977437b33c | -4.63748 | -50.95605 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8b6146f-bd50-3054-a930-de4fef9476d4 | -6.92148 | -47.65967 | 2026-10-10 04:08:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a04c4b47-473b-3344-99bb-b9ec697734ff | -7.00651 | -47.72295 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f5196569-f1da-305a-9e06-7341b7846a69 | -3.59732 | -54.59362 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7c436343-398d-3ff4-83ee-04c56906e891 | -3.11866 | -54.16393 | 2026-10-10 04:08:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 6599daf7-a9df-3efa-9f74-0d4a71c973dc | -8.99199 | -45.88963 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c64c53a7-c380-308b-b9f5-b7c31d9f0524 | -2.612 | -51.70741 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a003574c-7af9-36a8-a7af-4b1ba9eb1d3d | -3.01177 | -51.008 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46d4b2b6-09a1-3967-af5b-263a18784e22 | -6.12792 | -43.53558 | 2026-10-10 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24544b9d-385c-35b3-906f-4dc17be9d36e | -10.05252 | -44.34755 | 2026-10-10 04:08:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3254481-6e0f-3937-b8a7-9e386e486c86 | -3.1086 | -53.79273 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4013b809-c018-3d30-b142-6c6a414f1822 | -2.89297 | -54.06864 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c07e9f45-d2e2-38f3-9916-9a26d36f173f | -2.73066 | -54.14577 | 2026-10-10 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df055a5a-baba-3ba6-9284-ec77af796a54 | -4.68526 | -48.51931 | 2026-10-10 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 02a83fb2-86a1-3e8a-a58d-043a3e372184 | -4.63688 | -50.95967 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bf9950d-7be8-3d2b-87bd-906187bf8f9d | -5.53692 | -43.05782 | 2026-10-10 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e8103aa8-5778-35cf-8f61-cf1c433e3a1d | -3.28197 | -53.86602 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c099b229-ab9e-3938-9c99-f412e4e1498f | -5.95931 | -48.91832 | 2026-10-10 04:08:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6c8a34ec-0155-31ad-b601-a9663a8ec315 | -3.01112 | -51.01178 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55bc283e-faa8-3f80-a261-d2cc3a939b43 | -6.14419 | -44.15423 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d2edc07-c45b-3bdd-9cc7-f016d4f938a3 | -1.10295 | -54.17823 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9bf7c38-63ff-36c0-a019-91b4c5213366 | -3.46335 | -50.58899 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16f995fa-655b-37df-8e0b-8d2a126ab4ae | -7.57822 | -45.65364 | 2026-10-10 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c05fdef2-9a62-3ffc-9331-feef43869612 | -3.56655 | -54.68538 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 49cd5921-05ae-3bf2-b5a5-979abfcaf220 | -7.07025 | -41.60194 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1e4b60a3-e7f9-3d9f-a8f1-f5cfc86a4a4e | -4.12407 | -46.86998 | 2026-10-10 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7eee082a-38b1-32e5-a336-db0e49594b10 | -3.18806 | -49.25162 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2d9642f-7e08-315c-bff7-f2f26aebe560 | -3.2574 | -50.43237 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0918caa4-59d4-384d-8bde-5b469dd3362f | -9.94182 | -44.8759 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf1fd821-5ef1-3c75-9caf-afc362148958 | -7.17917 | -52.61523 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0344c60b-87e2-350a-aba7-4fa8da67d330 | -3.20171 | -50.83007 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d02005f7-1644-3024-944f-8be35f2b9deb | -2.99943 | -53.90506 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69baf22a-985f-382c-8835-616fb36132f5 | -3.26344 | -54.058 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fc1d8e8-380f-31c5-beaa-ea712f7a9b8e | -4.91882 | -45.78349 | 2026-10-10 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b39e9a80-6dbf-3906-abac-d213d9b73c5e | -6.8013 | -52.77753 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0d6e504-8025-3590-9ce4-9018549962ca | -5.41432 | -45.01984 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19c57416-5b4c-34fc-8b4d-7fab4d81bc49 | -6.32597 | -55.34306 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 747720b9-8843-3920-a606-0b776d4368bd | -7.92959 | -54.73249 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 26a74119-1216-3b31-891e-d45d65fa4278 | -7.22965 | -44.17808 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f7bf43a7-6c3c-3aca-91f7-ac5fe6b6ace7 | -5.94834 | -40.93686 | 2026-10-10 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55873e8e-8372-3fab-8a6a-e569f9a06251 | -3.21932 | -49.43537 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca04b386-9da9-30fe-be4e-e4f42c9a0da6 | -3.7487 | -50.01487 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a58744b2-dc00-339f-bcec-1994018dfebb | -9.01197 | -44.37111 | 2026-10-10 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2cc46886-2036-3599-a4a7-09f164aee7ee | -5.87535 | -50.10001 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c5196c59-cefc-3c01-ab91-bfbd5e5b5358 | -1.18894 | -54.21352 | 2026-10-10 04:08:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b282c517-955c-3b35-a94d-fdd03c1bad46 | -3.34604 | -50.47922 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bb347ff-9fee-3506-9cbc-e47a7817a0f9 | -9.12018 | -45.81964 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e7b463f-2a73-3048-a97a-36239f12bbef | -6.42642 | -55.26461 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1e28d085-96c9-39e8-a210-5648e9911e4c | -4.61262 | -49.21027 | 2026-10-10 04:08:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f09862d2-cfb5-354d-8995-907792d98b3b | -7.52401 | -45.31749 | 2026-10-10 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |


[Clique aqui para ver as próximas entradas](README31.md)
