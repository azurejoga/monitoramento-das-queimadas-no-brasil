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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19c6a784-74bb-35a1-9f6a-941b26eed74e | -3.09792 | -49.25185 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e22388b-a004-3728-a239-623ec9bf1b7d | -3.55639 | -45.01512 | 2025-11-09 04:38:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1b2713bf-40ca-306e-a84d-833b3f7e94df | -3.80768 | -46.00108 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df128045-4d86-30d4-9eb1-70f12228a413 | -6.02956 | -46.56083 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8e78dff-09db-3029-8f34-11ae182313de | -6.68607 | -46.6672 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bd56631-beca-38c8-9650-42bed9d8b58a | -6.12885 | -52.64154 | 2025-11-09 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 622e33f3-9ea2-3ef0-89ae-aadc60de5053 | -4.5984 | -45.99054 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 388a69ae-c33d-3fd2-8bbd-c358873a3ce0 | -3.59542 | -41.65436 | 2025-11-09 04:38:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0072bc9e-adfc-3017-9f35-f80fe47b4c7f | -4.7558 | -47.52328 | 2025-11-09 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31fa676e-9ab5-3384-be69-183b70d52118 | -3.34793 | -50.17989 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d8119ec-7272-3396-ae0c-3a545f45325f | -3.43257 | -50.24482 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5bc1fa0-5942-3fd2-971d-187cae5c2dcc | -3.15791 | -49.53901 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6bb58649-72aa-348d-9893-f1cf092ed1b8 | -3.07102 | -49.37891 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 14a2f3e6-0675-385a-a405-601c576f02a6 | -4.78164 | -46.9054 | 2025-11-09 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5da343ca-7642-302a-a35c-7929194bca68 | -3.9192 | -51.01713 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fcf53ac-b69d-3162-ba6d-06e6e90c0737 | -2.85093 | -48.72943 | 2025-11-09 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9bfb33e2-4ba3-3d5a-b364-51185ecf1b29 | -6.08029 | -42.6993 | 2025-11-09 04:38:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 487c2672-574d-3926-b2b1-1f1c0e4ed44f | -4.39026 | -45.95658 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c7836cf-1947-3267-8776-520fec834e40 | -4.83792 | -42.84461 | 2025-11-09 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6b1ab8b8-2c0b-3d0d-9665-d4ec20e3dec2 | -2.63929 | -49.20804 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a65e7fb1-c1bf-37e3-8ef3-ffe66aa00701 | -4.46179 | -44.64252 | 2025-11-09 04:38:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e586f291-833b-357e-a38f-5274c1097041 | -3.06162 | -49.37388 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 957314cf-ecb8-363e-a77a-b814a2f985b2 | -5.32276 | -44.83416 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cb3673e-2c6a-36cd-91f9-d2865cc78158 | -3.44333 | -50.22077 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c6ac859-791f-3708-bc91-a8589e339596 | -3.83816 | -51.12492 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05e4ed3a-8f59-3830-9553-09bee7bce8d4 | -6.02772 | -46.57275 | 2025-11-09 04:38:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 978b9c41-07db-3419-809f-2227ccd555ab | -3.09399 | -50.32097 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 48ab0f5d-e057-3d36-8e46-caf0b4feb552 | -4.71431 | -46.45667 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3a76a4f-5470-3c0b-acbb-50eada105c3d | -3.31709 | -50.30781 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c612ba-02ca-3cda-95dd-35015711887f | -2.84518 | -49.51783 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b40f396b-2439-3976-a22d-676c185b4e27 | -3.3048 | -50.15857 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 371efd7f-3dff-3f20-8d0d-72247d5abf5f | -3.84839 | -51.08355 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 285d7b80-fa6c-3ce1-81c8-8b17b4070de0 | -4.39345 | -49.65529 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6717ebf-538a-3475-aeb6-39dfa892e93a | -4.96154 | -44.94323 | 2025-11-09 04:38:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d538b55f-53cb-374c-ac77-edf603fcc061 | -3.08911 | -49.26464 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94ccd96d-faec-39d2-9d55-ff060c29054d | -3.33142 | -49.1292 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84031f47-5b30-317d-b1bd-fad0dd961088 | -4.46044 | -45.57696 | 2025-11-09 04:38:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba06574a-e379-3af0-a5ea-54f7fbb583b7 | -3.32096 | -49.1311 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aab26859-a93f-3395-9461-1d62bd23de0f | -3.3172 | -50.10189 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 37bb9cda-e1f8-353a-ad09-82c4125b9733 | -4.39843 | -49.66675 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a81ec65-da50-34a6-bcb3-c2d5c00b8ab7 | -6.71687 | -39.99683 | 2025-11-09 04:38:00 | NOAA-20 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f77e9123-2786-321c-a517-e05dd15aef98 | -7.4934 | -46.60884 | 2025-11-09 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a292bf28-35b5-31c5-8fa5-8b99372156ec | -3.94945 | -49.02599 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8d44d1a-0582-3ea8-ae5f-8a7dd3809581 | -2.92251 | -40.0037 | 2025-11-09 04:38:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9549d6ad-eaab-3556-9bdf-bdf21a518b8c | -3.75401 | -52.10273 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bc2cc2b-81d7-3fb7-a77c-60d0565f7df7 | -4.63291 | -46.39666 | 2025-11-09 04:38:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 360a7a3a-8dd4-3cc1-acca-7783d7a2f227 | -2.8758 | -53.15615 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a57268c8-50d4-3828-b4b8-0b1bb7e357e9 | -4.20889 | -49.76918 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 670d8d2b-4db5-3481-83b7-8497ff94e91b | -6.4935 | -47.22424 | 2025-11-09 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55efa5ee-297d-3025-beae-6ca675db885a | -4.83355 | -42.84401 | 2025-11-09 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f6233ed6-1538-3d94-b9d9-13b51e93b103 | -3.79756 | -48.91072 | 2025-11-09 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 221c8c1d-78c1-3097-9221-1e483c98e666 | -4.21998 | -49.78524 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 685bb206-8be5-3b4a-8bcf-6d9c54552277 | -1.23958 | -46.0271 | 2025-11-09 04:38:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bdbf572-e518-3f94-96b9-6eb1b01b39f9 | -3.86566 | -51.21955 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9117b70b-69ed-3dce-b52e-e9d1bb5c6e41 | -4.14818 | -46.25748 | 2025-11-09 04:38:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f30f32e8-6623-351e-a6fd-78abf2130e12 | -4.20384 | -44.75883 | 2025-11-09 04:38:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23fc3822-fdd8-3c0e-92ea-72ce5f2f0d4b | -6.17727 | -49.8712 | 2025-11-09 04:38:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 296ef648-06d4-35c8-a4dc-ca9c6145558c | -4.3987 | -45.9495 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2b94bb6-a0c1-372c-8a4a-499f5a09c081 | -3.86226 | -49.38295 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca04c3f9-d039-32e1-b71b-7131762c9e94 | -2.61279 | -49.22517 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 21535f1f-af7b-3e35-9204-279efaac54f3 | -4.02898 | -49.2752 | 2025-11-09 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 14c098ad-0f08-3544-bae2-f2f62836413e | -3.25264 | -50.13932 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e94d10dc-c606-36fb-9085-958854bb3040 | -2.83195 | -53.00251 | 2025-11-09 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd64d716-ae6c-3963-a5fd-c6e14d4491a2 | -7.94937 | -46.84854 | 2025-11-09 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5c7b3cf-3c0d-39a5-85d2-02fe96f1a620 | -4.28225 | -49.90555 | 2025-11-09 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 215429ca-5dde-3875-86b8-7c87e9ad46fb | -3.03585 | -50.30904 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d72b640-9ea5-3dfe-a820-4ec1fc333e14 | -7.56008 | -45.87984 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b172db14-fde0-3f48-96d1-6511a6253b52 | -3.30423 | -50.16216 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee5053dd-3365-37fa-bc33-02e4f10c7547 | -2.51136 | -49.45858 | 2025-11-09 04:38:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a447846d-1dd5-3837-b422-55339872453f | -7.55963 | -45.85664 | 2025-11-09 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 03d0fb45-c9cc-3c4e-a03f-4a90c6ee3f3f | -5.20581 | -44.41576 | 2025-11-09 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ba00e2e-4c23-38f5-ba8a-6143337be339 | -3.64785 | -49.87794 | 2025-11-09 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82c2e301-34a5-32a4-a690-6fb06bc5717e | -4.91325 | -45.98786 | 2025-11-09 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68eeeab7-cef0-3903-8682-4e3096e26cd9 | -2.77503 | -50.40649 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4380731-cd46-31a2-8571-ac6e703d5af2 | -3.13461 | -49.10554 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0a8dcd7-e8d9-3905-a166-cd22c6bd5b1a | -4.24921 | -48.63303 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ea21ae1-c5e5-3be7-8efb-6ce5e84436bd | -4.18502 | -45.73814 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50881532-3823-326f-8c71-0194ce1fafcc | -3.65107 | -50.26029 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b23b6425-98fd-3fb2-aefe-fb25b8eaccf4 | -4.05602 | -46.43213 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 117c655f-d04f-3ddd-b766-4d3d814c9cd6 | -5.36804 | -44.6191 | 2025-11-09 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89329c45-3ea1-3135-8349-020be4091b6b | -5.39892 | -47.26141 | 2025-11-09 04:38:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b17a5db0-b625-3f0f-8519-383fdd3d260f | -1.59186 | -54.30949 | 2025-11-09 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85f8de87-656e-3324-9507-3ab2567485ab | -3.52648 | -47.54281 | 2025-11-09 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d89c152b-fbbd-3ce3-9c36-cc1d4cacd381 | -4.5853 | -45.61715 | 2025-11-09 04:38:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd65d04a-b7cb-3e65-8845-afbeaed2221b | -3.39764 | -49.99765 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49c485a0-2dd0-31cf-90d7-f479fec438e6 | -4.18389 | -48.59452 | 2025-11-09 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af82e2ee-f6be-3965-9b49-4535b1afd32b | -4.97596 | -47.81393 | 2025-11-09 04:38:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c08c6163-d816-3a60-b644-6487e5f1f1d4 | -5.72608 | -46.46413 | 2025-11-09 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcc12e45-1620-305b-aa9f-ede40d7e9fbe | -3.5037 | -50.05832 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74c09d73-4db1-3129-8a67-6199b5231b9d | -4.28643 | -46.84308 | 2025-11-09 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8fa85af-af9e-3f78-93c8-01ad6d1fe96a | -7.09656 | -45.226 | 2025-11-09 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3728f856-ac2b-3ce4-bb5f-9d83d36b144d | -1.72565 | -54.68076 | 2025-11-09 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a24f3d9-7683-34bb-a34d-4d511566598c | -6.99846 | -42.78628 | 2025-11-09 04:38:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3365600-549f-3b91-93b3-bbc85e57c65a | -3.45344 | -50.02853 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98a21108-2250-38c9-b0cf-42502ff0d5e5 | -3.42833 | -50.04255 | 2025-11-09 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ea01805-f6c9-33a5-957d-36dae52c03ff | -2.64104 | -47.30141 | 2025-11-09 04:38:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7a9fbb15-241b-3b28-9422-2e3afd5d5f5a | -3.1273 | -50.15615 | 2025-11-09 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c466a4-4dbd-3b04-88cd-f123a564b2ea | -3.21955 | -51.34017 | 2025-11-09 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 867add5a-4314-3ca9-8d3b-f8bd735ee6da | -4.39969 | -45.96656 | 2025-11-09 04:38:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d184d345-fe7f-349e-a056-671ad2f20e7d | -3.07766 | -49.37996 | 2025-11-09 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README25.md)
