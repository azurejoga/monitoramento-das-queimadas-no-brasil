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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94dc33b5-30af-382d-ad2a-0c55557f8f20 | -9.82568 | -44.78269 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 910548e0-c970-3404-97b5-98e607052f5b | -6.83761 | -39.56221 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6563c869-249c-3668-818e-bce1cafbb6c3 | -6.1385 | -47.93139 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| c52a98b3-3ffb-3801-ab68-9e1b1631efb9 | -6.97928 | -40.03362 | 2026-10-08 04:02:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b80cbfc6-f7e3-39fc-855c-0d801ef3626d | -8.98599 | -45.91982 | 2026-10-08 04:02:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0691b993-b827-32d5-b0b6-f8d85ede683e | -7.73057 | -45.44454 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ec269c4-07c1-35ea-bd8e-fe6da943c79b | -5.97045 | -40.91188 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e62045f6-72b7-31ee-a7d3-a4a6f27f350e | -6.14454 | -47.92877 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| ec250081-2905-39e0-a2a1-7f7acedc4ac9 | -4.29052 | -50.7848 | 2026-10-08 04:02:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 64203d64-2737-3433-b036-8cb0c5dcaed4 | -8.58931 | -44.86577 | 2026-10-08 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4203679c-b1fa-30e8-94a5-e5b94b0e1ba5 | -6.14527 | -47.93216 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| bd62baf3-c090-3a61-bd53-d98148c04d7f | -4.06741 | -51.0459 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1a1636f-435a-341b-b596-cc5f63a2a5f1 | -6.85841 | -39.43244 | 2026-10-08 04:02:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4c275c2c-6332-37e3-8894-7a1e15f716f3 | -8.72544 | -45.18033 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 01c5e1ed-4901-31fa-ae60-e051c617fb48 | -9.8157 | -44.7772 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad9e82c1-5dc0-3706-bd99-63d1fa9aa2a4 | -5.11253 | -47.12723 | 2026-10-08 04:02:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1ae31cfb-a437-39c1-a2d5-6aef624f4d0e | -11.23986 | -44.87531 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4832f2a7-eb86-3d40-b5bc-c570e15f9f27 | -6.89929 | -40.91133 | 2026-10-08 04:02:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 59357477-6184-3202-bf9a-8470337aec96 | -5.73911 | -41.75373 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c265ed8-7580-32ca-af5b-f4f498f8e015 | -10.77373 | -46.58225 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 291aa61e-3c13-309a-a629-bd7f671f940b | -11.84136 | -43.53276 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd0c1703-45f0-311e-a5ad-15f56101e457 | -6.13984 | -47.93125 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b2ff3e2-7d9a-3348-8bed-6bf2ffec73f5 | -4.3399 | -43.80173 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08239a71-fc34-3899-ae53-982d8b3fe59d | -8.21301 | -46.38112 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0ac1816-f964-399d-95e8-df4a0c43dd1e | -3.16892 | -50.45274 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d32f15c2-849b-37f9-a49f-7dd600813b78 | -5.32429 | -40.89618 | 2026-10-08 04:02:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 67df9374-ac39-38ae-9c1f-9022b0cf828c | -6.13439 | -47.93039 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abc87ff6-76cd-3e65-acfe-341b003294ea | -8.59629 | -44.87597 | 2026-10-08 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c3c4d9d-8f45-3848-9d6b-4b4e95f3122b | -7.37681 | -46.23864 | 2026-10-08 04:02:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcca0b5d-6999-357e-a3d5-01a282168e32 | -5.9657 | -40.91903 | 2026-10-08 04:02:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2c0582f6-4d03-312b-b548-b0199e3fe8f9 | -11.74048 | -43.64312 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2cd25c4a-de17-332d-ba96-e137f0109932 | -7.85968 | -45.4044 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0e0bd1b-de8d-3039-bdc8-6291862fc508 | -5.74205 | -41.75864 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 598b9546-7e0f-3828-9a2a-2b0930277d2f | -9.89856 | -44.80377 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c860d01-993d-34fa-8e35-5028f358433d | -9.43925 | -44.60488 | 2026-10-08 04:02:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 795b8099-fbf6-3027-a22c-c6a227bfe548 | -3.19955 | -50.57287 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a69ab2d-d9b9-3b57-b20a-b1e448c887f9 | -6.7922 | -41.2508 | 2026-10-08 04:02:00 | NOAA-20 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 130ff85a-438d-33c2-8871-64af348d5526 | -8.28394 | -50.26877 | 2026-10-08 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 900170f6-7047-3dca-92d9-ff012f8ec851 | -6.83151 | -44.86718 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 10549a59-0be4-32cc-b38a-2ab49dc58ca2 | -9.59116 | -47.78471 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8e96bd2-8fda-3b20-ba58-37ed339927a0 | -5.70449 | -41.69118 | 2026-10-08 04:02:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 59e8934b-427b-30d2-ae34-6eeee85e1582 | -11.83886 | -43.56966 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 690a7542-7062-3653-a087-d002d3108d01 | -5.48692 | -42.87572 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4061b2fc-7bc8-3096-9dcf-b152861e6725 | -6.82873 | -39.55362 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 58e13be2-d8ac-3af8-a5e2-418eeb62dfca | -9.82331 | -44.78243 | 2026-10-08 04:02:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3d3c797-cd37-3fee-831c-86b0a8286222 | -9.0236 | -46.91414 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dc90db9-cdc9-3281-9b37-33fba30e66a5 | -5.67389 | -46.35789 | 2026-10-08 04:02:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d62f02e5-4bce-32be-861c-b813ffcc03a3 | -7.22761 | -44.27716 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4c392de2-378c-3070-a68d-25b3478b878e | -6.82263 | -39.54905 | 2026-10-08 04:02:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 320855f0-19d6-3366-8e1e-a28ea403a727 | -4.34054 | -43.79779 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2fb2f999-64b2-3eb6-8e30-cd447ee42305 | -5.04253 | -49.77373 | 2026-10-08 04:02:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f621d5cc-e838-3d44-a362-c202f310c9e2 | -3.36246 | -50.48687 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3df6f65f-fa33-33ee-b83e-d29226992555 | -3.47889 | -50.08723 | 2026-10-08 04:02:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| adbf21e4-6b23-37ad-ac64-f3253a0ce45f | -4.70992 | -44.35725 | 2026-10-08 04:02:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf41cc41-b773-3eb6-b4a8-ff37d4c41932 | -4.35341 | -43.79859 | 2026-10-08 04:02:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| b6670954-e4a7-3af5-a998-920621e1500d | -8.22368 | -46.34801 | 2026-10-08 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d63b1b7-d93f-32ea-8a4f-a61c2074c891 | -10.99489 | -45.4159 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb5d0fe8-baa3-37d8-84c3-921822a9c0c2 | -4.80435 | -42.74833 | 2026-10-08 04:02:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e48ab07c-4659-3118-913f-b0450b1793ef | -10.77269 | -46.56178 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e042bea-9a55-34e3-920f-5822f81a9a63 | -11.2392 | -44.87902 | 2026-10-08 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 400b48b2-352b-3929-99b4-af2f53fdd83f | -11.64788 | -43.6876 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c8c0f32-1e6c-39e7-b98d-f1af7af61053 | -11.62595 | -43.70023 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49b66047-1c27-3c04-8bd1-018ece7821fc | -6.13503 | -47.92686 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe36def4-179a-3858-9f28-04251701b65b | -8.1878 | -45.7724 | 2026-10-08 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4db33a84-388d-3096-a6ad-287345a3162c | -8.60121 | -44.87271 | 2026-10-08 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8f87c45-5647-3219-af72-5c07eaf9760c | -8.71171 | -45.2079 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 386dbf07-9b7a-36dd-bd34-481eb80a514a | -10.43449 | -47.28536 | 2026-10-08 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a2b824ae-7955-305e-8eb1-173b11ad3263 | -11.23655 | -46.24459 | 2026-10-08 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 024c11d9-6be1-328c-b3c2-204c86afe235 | -8.7384 | -45.15694 | 2026-10-08 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 60c4e8bf-501e-3c31-a61a-0257f06c6bca | -7.64098 | -44.37357 | 2026-10-08 04:02:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97560243-beab-38fe-b98d-c5c6d993c37b | -6.36108 | -42.57462 | 2026-10-08 04:02:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4f5fa45d-bcf9-3aee-8bc3-0ef6e2350ba0 | -9.95906 | -39.39902 | 2026-10-08 04:02:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8d0ddf8f-69fe-3021-9283-8bab0e83ba1b | -4.64823 | -46.33722 | 2026-10-08 04:02:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5df093-8f6f-347d-a08d-403b8c12754c | -6.144 | -47.93927 | 2026-10-08 04:02:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 678c3d10-4598-377a-a4ef-75836a985a23 | -7.88487 | -44.24422 | 2026-10-08 04:02:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22a3f40d-61f9-3c87-b0a5-fbc3aa27c0db | -7.22016 | -44.15987 | 2026-10-08 04:02:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 072230cc-38b4-367c-83dc-515a3ce8bd2b | -9.4002 | -49.01326 | 2026-10-08 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de4d26a5-3db9-3cf3-b163-080c8654d2f0 | -4.93951 | -40.54305 | 2026-10-08 04:02:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8df5f5b2-07df-3bb2-a064-a64964aff19d | -7.83157 | -45.48793 | 2026-10-08 04:02:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 03567001-1575-33ee-b459-15fd53401303 | -5.48607 | -42.88069 | 2026-10-08 04:02:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 99787896-6bf8-39ca-bd58-9712142be407 | -11.64582 | -43.67734 | 2026-10-08 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bdf18fad-5f85-3846-92b4-1d1880c22661 | -10.77457 | -46.57759 | 2026-10-08 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9f8ad47a-027c-302d-a619-cb74d9659b98 | -7.10518 | -42.53372 | 2026-10-08 04:02:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8964eae-6efc-3f14-b0f9-208e7257b4ed | -9.78763 | -47.86502 | 2026-10-08 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49d51030-a15f-3368-b57d-588992faaec5 | -3.26274 | -50.40877 | 2026-10-08 04:02:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 68ffd911-4cc0-3ae2-b6ef-1d583e60cf4c | -16.83193 | -41.0414 | 2026-10-08 04:04:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 77cd2c1d-b157-36dc-bacb-066eb2754f4a | -16.63892 | -45.50949 | 2026-10-08 04:04:00 | NOAA-20 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00b97b76-0c5b-3163-a94d-26c6a75bf319 | -13.80212 | -52.79874 | 2026-10-08 04:04:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c6dd82b-c882-3c32-8818-76c3a6f5b601 | -18.0383 | -43.04718 | 2026-10-08 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e71ef2b5-a726-352c-a441-9ef413a4ede5 | -16.75638 | -53.37793 | 2026-10-08 04:04:00 | NOAA-20 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9c0a8a95-d8ec-3e08-b82a-79576c40e0e7 | -17.4331 | -41.362 | 2026-10-08 04:04:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 84fc1eac-0377-37ab-bd9a-6d5d7d6d849d | -12.23176 | -44.72202 | 2026-10-08 04:04:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48a688e0-6942-37bc-9ea3-3a241199264e | -16.90261 | -40.89462 | 2026-10-08 04:04:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 0d71722e-84f1-3551-bf72-7ae733a6edd4 | -14.97015 | -47.54064 | 2026-10-08 04:04:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59eae56e-296e-3c02-834f-3f962e157888 | -14.93728 | -48.11277 | 2026-10-08 04:04:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0fea37a7-9e56-32b0-a242-e1899fee05e7 | -12.36836 | -41.48341 | 2026-10-08 04:04:00 | NOAA-20 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8f750721-7fd5-3a9d-a191-ee090a31b4ae | -15.92139 | -43.52601 | 2026-10-08 04:04:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f780942c-61e0-311c-a496-98715fe49a37 | -12.15629 | -44.75639 | 2026-10-08 04:04:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce9ef4a0-e8c2-3de8-9d7b-6e5fa3d15d84 | -11.32531 | -46.66314 | 2026-10-08 04:04:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1e93f6ce-620f-3eaf-85dd-f106dd88c2ab | -16.8768 | -40.6061 | 2026-10-08 04:04:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |


[Clique aqui para ver as próximas entradas](README71.md)
