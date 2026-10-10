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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e2950bc-7ef6-3862-b232-90aab494fdee | -4.39994 | -46.53056 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c2e32be-5881-339d-bf63-fa36e10306aa | -3.35665 | -50.4167 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86a1b1f4-efe0-3247-aec2-eabfd3a437ae | -3.22364 | -54.29389 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 98cd7fdf-c23e-392e-8e8c-75097d8830eb | -7.93407 | -49.7459 | 2026-10-10 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5736f2bc-e1ee-34ff-8a55-1ebbe28f08f1 | -6.80979 | -35.20707 | 2026-10-10 04:08:00 | NOAA-21 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c1940682-0c37-38d8-8a37-24f014e82f63 | -3.59626 | -54.60682 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| b5583b99-43bc-378f-87dc-38fba3e23027 | -8.99769 | -47.74299 | 2026-10-10 04:08:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e84c78c3-507b-34a5-a3bd-ce3277dad4a1 | -4.59463 | -50.97543 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2dc0e22-b936-3296-82fe-9532bfb5ebcc | -5.60872 | -47.27401 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa41fa0d-9e6e-324e-9d85-2d1aa418e1e1 | -9.92326 | -44.77863 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb81b43f-cac2-3d74-8d36-c4ac346b1f82 | -7.92416 | -54.72535 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 97b099db-707c-3f17-a439-e3793a48fc29 | -3.75033 | -50.00525 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 053c9ec9-44a9-38ac-8db0-894df182c09b | -6.33923 | -46.03331 | 2026-10-10 04:08:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 904c69cc-23c8-3eee-925d-6bf1e39d7ff5 | -4.29023 | -55.13232 | 2026-10-10 04:08:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fa11295-e7fe-3531-a39a-e629f8238a72 | -3.20235 | -50.8263 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 826c15ac-ea45-32c1-87e5-806a64c79f07 | -3.15648 | -50.59199 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f95e6a5-e6e0-3ec5-88a4-07cdcf51243a | -6.43248 | -55.04438 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ff6b3a7a-a72e-347e-b6a9-c44d076c4f01 | -5.23437 | -50.67854 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ab985b8a-1286-38c5-b744-789770aa509e | -6.64233 | -55.32916 | 2026-10-10 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba23402f-316e-328e-94d3-194ae6de28b6 | -7.59294 | -43.08052 | 2026-10-10 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9514651c-722f-3bba-8034-da8a9b02f9a5 | -8.25404 | -46.4337 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5ab0784-89c9-3739-bc1c-b7b6080424cd | -5.04719 | -49.34794 | 2026-10-10 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 77551b3f-5a31-37c6-923e-b17fa3461b71 | -8.98507 | -47.54376 | 2026-10-10 04:08:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0be480ac-3dc6-3f3f-b87f-f1c529550593 | -6.19961 | -45.43128 | 2026-10-10 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98ee0fd6-9d5e-3c25-92fe-2d01a07b090d | -6.07794 | -44.72128 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fca4ef52-386b-3d7e-99ce-2ed36821e213 | -8.40793 | -46.90425 | 2026-10-10 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11e1872b-0b9c-348d-b7bf-6f11ba34c0ba | -7.55045 | -48.02324 | 2026-10-10 04:08:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f7609d8-9af5-31bb-83e2-f08e2bb7829e | -5.32354 | -45.20741 | 2026-10-10 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 437484de-623c-3683-ae17-7e5a135e3397 | -7.07738 | -41.59952 | 2026-10-10 04:08:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5fa67255-c589-3e48-a156-c8e06dc36670 | -9.15274 | -46.73844 | 2026-10-10 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f949269-8068-311e-b867-951567eefffa | -3.38022 | -44.48455 | 2026-10-10 04:08:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 95603e6b-de93-3477-912e-35d84fcb8e5d | -6.04379 | -46.4161 | 2026-10-10 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe2bfd82-e84d-30ca-b7b7-0065544720fc | -8.25869 | -46.42951 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 527978c2-cb97-335a-962d-5ceb60ff0f13 | -3.50628 | -49.94573 | 2026-10-10 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f252a8e-4a9d-3882-a43b-ddb84f984a78 | -6.93365 | -44.57022 | 2026-10-10 04:08:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b11d76e0-29c1-39d9-9cd5-ef274e8226fb | -5.79929 | -53.7964 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be8d9faf-3a6f-37a0-a3c7-831cd971f652 | -9.35123 | -46.57148 | 2026-10-10 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aea9247d-bf1e-3da5-a28d-b20edad0d8de | -2.99729 | -53.91747 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0342253-e5ea-39ea-bddf-46a7ad86e06e | -2.78528 | -42.59518 | 2026-10-10 04:08:00 | NOAA-21 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c814d2f2-a7e6-3d6d-83dc-1b3777cad818 | -6.08786 | -53.49641 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e594b8c-9d64-3aa3-9163-26e8dc3f6f0e | -3.26817 | -54.68727 | 2026-10-10 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 388d247d-112a-3dd5-892d-0c1b03c455e5 | -6.59211 | -44.30014 | 2026-10-10 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fb474f05-7ae1-35e7-b3e4-971c862e7ed0 | -9.09299 | -45.89166 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3208e783-d76f-3a8d-82dc-282c77850698 | -6.18658 | -44.11273 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0737809f-c6c5-3fe1-8c30-e2a5ef5bdf03 | -9.93843 | -44.78857 | 2026-10-10 04:08:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7856d215-c1f9-3f21-b5fa-baceeb06aa7a | -8.25652 | -46.41908 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01884113-7c42-393e-9aaa-45b883ded4f7 | -6.05078 | -44.03657 | 2026-10-10 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7d4c783-7b79-33d8-b253-892932886339 | -3.18139 | -50.57763 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e10a4d95-e815-3fc1-a679-bb9e2c841dc4 | -4.10554 | -54.02011 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a70d74d1-c260-3098-8930-a80cb12bf449 | -5.23324 | -50.68523 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8c0ed1c6-3390-34f0-b9c1-06da6172a763 | -6.2039 | -40.8913 | 2026-10-10 04:08:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b7342676-f4bd-3825-bb33-d1fae775fa83 | -4.40651 | -49.78667 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8bd3563c-685d-3e4f-b923-3359bacf669f | -7.22051 | -55.06966 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b568b3db-57f3-3260-b58f-01e4e0b56ac4 | -5.7076 | -53.47871 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a49c17e4-2491-3325-b903-c37cfd555822 | -9.28458 | -47.38709 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| edc4466c-531c-3742-9958-e0e27e7ef200 | -4.40702 | -49.7836 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bc35d077-e048-33ad-bf89-1c44c04189e5 | -6.42515 | -55.27122 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e89345df-17a2-3dc4-a502-f249e5502e8e | -5.4596 | -44.78211 | 2026-10-10 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a8dece1-ea84-3a23-92e2-191e3807a17b | -8.36451 | -48.1489 | 2026-10-10 04:08:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 792e9356-bb7e-39ab-8044-bdd49015c84e | -3.01242 | -51.0042 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70b057c7-db42-33d4-a05c-3d4643357140 | -3.10973 | -51.68808 | 2026-10-10 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6bdd7bda-5fa8-3a2d-9934-8860d5b3d59a | -3.18197 | -50.57411 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a7a3914-2e92-34c7-972e-26a9ebc0745e | -6.28838 | -44.69848 | 2026-10-10 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41bfa85e-c077-3a48-b830-3afebba05a2e | -5.1047 | -46.22627 | 2026-10-10 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8aab9db5-ff52-3d03-ac6d-0105c8e92a0f | -6.77213 | -48.66388 | 2026-10-10 04:08:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 84d2e07a-7d00-3935-9577-58129d4d734d | -3.54611 | -54.6888 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb99feab-4efb-387f-9fbf-1d3901904a2c | -6.19683 | -40.80446 | 2026-10-10 04:08:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1cb288d0-98d1-33d9-a719-c3acad44c382 | -3.28067 | -50.39322 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 23796204-5eee-340f-9a27-cdce04e942dd | -6.82143 | -39.55567 | 2026-10-10 04:08:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2629c467-fb8f-3519-9c48-cd0f836a5a0e | -3.58367 | -54.72286 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 173699e5-9434-374e-9e82-b92883550300 | -7.2331 | -44.1786 | 2026-10-10 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a614b52f-f7aa-3126-aa2c-ababf69d6327 | -9.27876 | -47.3969 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1539e48-a063-3485-ad8b-37a4eafd1846 | -3.25683 | -54.18077 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 0ce53d2b-761a-3e89-bc00-6e385bfa2256 | -7.50551 | -54.99246 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 25b822f1-4021-3116-9489-fff49a22e1f1 | -5.23709 | -50.68325 | 2026-10-10 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07401c0a-f398-34b4-8962-4db3676c6010 | -5.59833 | -47.28431 | 2026-10-10 04:08:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b9d00a86-18ff-3119-bffd-33f1874267d2 | -7.17844 | -52.61918 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6ce0968-39ca-31ce-aeae-369b2c29ebaf | -6.43871 | -55.28025 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 200125e5-c674-351d-a515-e46e026ca194 | -3.26454 | -54.06156 | 2026-10-10 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 27df1650-0531-30a0-8c14-65488bcef714 | -6.40733 | -43.74274 | 2026-10-10 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cbb59d3-be5b-3ee6-8b5c-91acf0540d26 | -3.22797 | -49.44606 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f76e066-45ab-3792-b19e-971cd11f7a51 | -8.94185 | -45.12499 | 2026-10-10 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e81b4410-2218-3962-b841-959ab86e3a77 | -5.51721 | -43.99002 | 2026-10-10 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c872fb4-7e83-3727-996a-be112f950ef0 | -8.27014 | -46.43155 | 2026-10-10 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6531a3a4-709f-3090-942d-89c97aa95638 | -9.11944 | -45.82403 | 2026-10-10 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be261e63-c575-3c04-bb4c-03ca94d2d3b7 | -10.27965 | -43.9344 | 2026-10-10 04:08:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1145d25b-4f5a-382a-af17-f9a941c91b53 | -3.22995 | -49.43408 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f60c7e00-7a77-3ae1-ac1f-ed8fc1b9de71 | -3.58124 | -54.69475 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47fd526c-1531-3a4b-9842-d4655958f0f8 | -3.21981 | -49.43239 | 2026-10-10 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5331b3bc-d08a-3db4-bf40-74bfc6b45dae | -5.71096 | -53.47603 | 2026-10-10 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 91bf7127-6bb5-39d3-9f80-dad3fa139f1c | -2.61273 | -51.70308 | 2026-10-10 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 750f0bd9-23f0-34aa-beaf-f0129c9fc476 | -4.41001 | -49.76554 | 2026-10-10 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 0d671925-9fb1-3f3b-b2c4-f44adbff73f5 | -6.42254 | -51.95632 | 2026-10-10 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4cc9fe3e-6f62-3c80-9229-dfb5f87ac46f | -3.56414 | -54.69888 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67bad1a6-9471-334e-a5d8-67d3a2c324d2 | -4.78477 | -42.74071 | 2026-10-10 04:08:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3cf39e8-c6ae-33ff-968d-4d9f1a6fe024 | -6.42769 | -55.258 | 2026-10-10 04:08:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3276128c-3699-3be0-80f3-e7ee99d0d2d8 | -3.59853 | -54.59352 | 2026-10-10 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b0da06c6-b84f-3c3c-9cdb-3bc445078ca6 | -9.27756 | -47.40384 | 2026-10-10 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7201ed37-225a-3108-a534-6008cf558aa8 | -5.97935 | -37.82892 | 2026-10-10 04:08:00 | NOAA-21 | UMARIZAL | RIO GRANDE DO NORTE | Brasil | 2414506 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3df62cea-1fb7-3101-9b0a-0bb990191f84 | -7.01203 | -47.71602 | 2026-10-10 04:08:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README33.md)
