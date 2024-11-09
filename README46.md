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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e78ca5f-25a2-345a-9267-b098b983a2b9 | -3.12267 | -50.15496 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8af07810-4932-38ac-a1f5-65417b653e75 | -2.77578 | -52.87032 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f22aa2e8-212f-3b7b-b3c5-8ff50dda7c2d | -4.59809 | -48.47867 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6670c6d1-80a6-3799-92b6-ddd5c4552c18 | -5.58992 | -42.8052 | 2024-11-09 04:33:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f4135a9f-c57b-34c9-8a9b-374390e6bb28 | -3.6515 | -50.75869 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f64a433a-da18-3973-b1f5-4629f6086318 | -6.27287 | -44.53724 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 940ab727-fc95-3f18-8aee-9f2e5b567eb7 | -3.68535 | -50.19766 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e662a1a-fe1f-350d-a383-dd43973642c8 | -2.23378 | -53.77728 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| af9d23bf-ac78-342c-874a-1991ccd0f5f7 | -4.20565 | -45.8673 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| efd02331-a0fe-3a06-9239-8495efb1c18e | -3.48319 | -50.80373 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 693097e9-f2ba-3919-99d8-2cdbe91cba20 | -2.90622 | -49.71407 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bacec488-a85b-386a-84b2-35d7a3e4c2a0 | -3.08164 | -50.57135 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| f7e0c27a-ac26-35ca-a1f7-fcb9f0ff5afc | -2.78 | -52.87096 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a702aef-baad-3fe7-b1f5-eca2d8d62677 | -2.82131 | -52.9655 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 634ffa36-59f0-32e5-bac4-47516f53120f | -4.22418 | -50.6454 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a65b95fa-c163-34d8-bf4a-010dea61f2eb | -4.56679 | -48.05054 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61bcb015-84c1-365b-a096-e47cb147d55a | -3.03949 | -48.04803 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3327dafa-e37d-37bf-bd30-0dc7edf5e0e2 | -2.66385 | -49.86997 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 900ea483-a351-3dea-8591-2250de48e144 | -2.67068 | -49.89541 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdf883ed-8f3e-3d73-9006-ba68ca261092 | -2.85625 | -48.45459 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b98744a-353d-3b34-9886-68dc705d1c73 | -4.87063 | -45.67469 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71e72eac-a9a4-3dc9-a1e9-7d7486029ff2 | -3.58435 | -47.34985 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ef61b0e-d0bf-3898-be4b-4702b8004ecd | -3.30813 | -50.08434 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2a4eb47-5a6c-31db-8740-a89ca041dac9 | -3.9723 | -46.47202 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40fd6cac-6801-3390-9670-a7e57562c124 | -3.81823 | -50.79565 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84e8623c-62a4-3594-b0cd-fda440544589 | -4.06668 | -50.01263 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4dc46cd5-0935-3752-9b2c-55e577755ba6 | -3.34146 | -50.08041 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6b52b55-23b0-30b5-82d0-0eacfe73f38a | -5.18218 | -46.18531 | 2024-11-09 04:33:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d36766ce-f349-3949-8e29-73afa1d70e6b | -4.20621 | -45.86368 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b845df11-66ab-35b1-adaa-e2de471bf685 | -4.11166 | -46.88929 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2acef7cc-5d68-396b-a355-2a2fcc5c5cb5 | -2.19024 | -53.63302 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd0e39c-2404-3ddf-9859-29333ab73ee2 | -4.24696 | -46.01368 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26ff59d3-899c-3a18-bab3-3447bac7dfd9 | -5.24481 | -46.66487 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 46beb777-2565-3438-8d3d-e5ee8034357a | -3.03615 | -51.53093 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4acf027c-9c5b-364a-9f6a-d3439dfeb238 | -3.24139 | -46.49123 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 638b53ab-e7d6-3d5b-9e09-200c69f48195 | -5.20278 | -47.46312 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2b7205c-1685-3acd-a45a-03c39f0e2fe7 | -4.06148 | -47.38576 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06a12744-4b94-38be-98bf-db7904ce98f2 | -7.5953 | -40.0537 | 2024-11-09 04:33:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| c57df26e-e3eb-3bf1-9156-df9c0ceb4b3c | -3.57143 | -53.52429 | 2024-11-09 04:33:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e65f70a-1df7-35ea-a619-2710b89c1613 | -3.2441 | -46.47387 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38229383-2348-3d86-b259-7ffe3b537e3d | -2.71366 | -52.96113 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dcfd0ac-9d8d-36f9-a48d-881feae9213d | -7.63071 | -43.5479 | 2024-11-09 04:33:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35da6e30-e8b4-3abb-bddc-d0061124c937 | -4.7609 | -48.00715 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f443deb9-caca-30e2-a488-15a99fe86b34 | -3.96183 | -48.1324 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f76d000-70cc-3a82-9933-13cd704eafab | -4.07451 | -48.3251 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb0e0b92-1e38-3177-8c8f-ff1c9d2bc63b | -4.62538 | -46.53693 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 03989c9a-88e7-3e39-9360-e08456d0d302 | -3.08508 | -49.58703 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97ba4696-c82e-3e78-bb74-eb91b67a8025 | -8.85091 | -47.68466 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| affd6b7f-af2b-389d-863b-95d686c475f7 | -4.60905 | -49.58177 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fa31e44-c933-305d-b615-644c97083af3 | -5.19948 | -47.46262 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce3027ec-c7bb-34a4-bb84-616952ac7a7b | -3.85715 | -46.64388 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 754ccd62-96be-341a-a46a-def3f77390f2 | -2.67855 | -51.8282 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c8392396-5f67-3be8-ab53-ff1cf19f428c | -3.97053 | -46.98779 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e9e7e76-f12f-3b1a-9d55-2fdc87591baf | -3.43197 | -46.40328 | 2024-11-09 04:33:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c17b80c3-619a-3db1-8cb7-24541ac6aea8 | -4.41212 | -45.93898 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeaea5a7-3674-39f7-8f8b-cd40531b47c0 | -2.91664 | -51.67287 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23a735a4-1da3-3665-a451-66802e3da02d | -4.20226 | -45.86678 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15a27f34-c00d-3223-b723-8a2197eea2d4 | -2.76766 | -54.05401 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a6a1ea83-8895-39f1-9deb-1417191ac787 | -4.41247 | -48.77435 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c93b6cf-414f-3ff8-8fe6-7a6dbdc402c2 | -3.02009 | -51.196 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1b249c2-3c16-3efe-8bc2-c2705216ab57 | -2.94166 | -52.70761 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a17d50c-c9b9-3b11-b858-f3a10b223a04 | -2.73596 | -51.71972 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8133a1c4-1047-3d27-9b9f-8ceee7ba3c20 | -11.08579 | -43.34187 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 41316099-5225-3c4e-a206-8f1ad1a33685 | -4.07728 | -48.3291 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 547a4f33-f3b0-33d5-bdf9-1b25ca1e7998 | -2.93562 | -49.50586 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afadccdf-de75-3fde-a1eb-60599a5bbdd3 | -4.25358 | -50.98175 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecca59cf-c145-307a-9b9c-51a9e6f62ca2 | -3.03786 | -50.37225 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ff6f52e-0ad0-3b1a-9d56-973a8210fb53 | -4.2493 | -47.57737 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c4b537e9-f4ae-3983-88d4-30fb18d7a984 | -2.66236 | -49.90225 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9d8fd40-b1d2-358d-808d-52b61d0f508e | -3.11329 | -50.14523 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aaa80847-f735-3942-b0b0-c5eac0f83d14 | -11.08059 | -43.34172 | 2024-11-09 04:33:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 04787970-8835-35e9-93b4-b25ed182452c | -3.68583 | -51.30362 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d85fd29-f4e8-3b51-9796-1672e5341618 | -3.54006 | -51.10246 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c2ae472-3af4-3886-aabd-195086647cc6 | -4.88714 | -44.59385 | 2024-11-09 04:33:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e373015-60c4-3856-be62-598d8b55074c | -4.05158 | -47.38422 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 285ac09f-75f4-3843-8369-2e9711ce3d5d | -3.85769 | -46.64039 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60476537-b713-337e-bc45-61d30dd07a3a | -3.05109 | -48.03914 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1bcf638-cb55-36ca-ad50-49b60b4ec675 | -3.66152 | -50.25548 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711844d4-3f1f-33c5-b162-4d5e717dc9a1 | -4.13331 | -43.59321 | 2024-11-09 04:33:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 12c0d6ba-4fda-3b04-bf79-ab7d0feb0901 | -4.66862 | -46.65184 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a193451f-1d69-31ff-8955-805f3ce807bb | -5.44602 | -43.26442 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0272be5d-6978-386d-b4c2-7dbdbba51aee | -3.12646 | -51.11302 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3419638-20b7-31f8-b8b4-a7a779df7a83 | -4.21424 | -48.54058 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 806df013-b61e-35ea-bad4-9dd36dd9c763 | -3.48332 | -52.87025 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7a48895-3aa0-3f33-9a2f-ee418495f817 | -3.97635 | -48.1703 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4f6f64a-29c4-3ecd-814d-900670f61270 | -5.44062 | -47.6164 | 2024-11-09 04:33:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c934f94e-a9e3-300f-9c87-72c7de5fdb74 | -4.37406 | -48.17226 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46bbadc9-39da-3437-bf92-af07e57ac035 | -3.47011 | -50.81497 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1521b4d-4b1b-36a3-a8de-814d83b81b89 | -3.76287 | -51.76694 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4019b327-915c-3800-9793-c85783286f0a | -3.63926 | -51.78486 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c3ca9cb-ae1a-32e1-a4ce-969cd3a4c219 | -3.74878 | -52.10325 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ca7532c6-1574-3ad1-aeac-1ed847508850 | -2.86016 | -48.45156 | 2024-11-09 04:33:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f3f32f1-1102-318d-a21f-8e69e46df9c9 | -5.44364 | -44.81889 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e0159667-a2bc-3401-b44f-106ba4d184f0 | -4.13384 | -46.92109 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b4cce3f-387c-353f-8f5e-3cd257fa4da6 | -3.07436 | -50.57023 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c38ebc8-fd4d-3f02-a3f9-5988722f5119 | -3.24474 | -53.39741 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eee4711-247d-3665-8abc-544b15c60739 | -3.25594 | -52.23845 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d95ef6b4-3aa5-384e-9a17-9452cd5a3044 | -3.24511 | -46.44553 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f43e3b4e-a5db-3ef1-a072-4cc182cc1a07 | -3.14333 | -48.57564 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fd446e6-1be6-3d68-967f-7ce7dcc045f5 | -3.45685 | -54.53384 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README47.md)
