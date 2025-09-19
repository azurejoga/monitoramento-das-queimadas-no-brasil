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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2de64cb3-995c-3282-9de2-943370caf004 | -8.9911 | -46.3059 | 2025-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 0bb3afdd-9d22-3974-a42e-94363c81540e | -8.9347 | -46.2894 | 2025-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| dad6b5d0-c561-39a9-9e67-20442dcebb55 | -8.0281 | -44.957 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 71c11f12-24a2-3927-b355-f67338e2d2cc | -7.6949 | -44.486 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 179a97d1-3b69-37d0-9d6a-3332e0f1d944 | -8.6076 | -45.3302 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| cee6ad80-74b6-34d3-b19f-b9c4c8005c6c | -7.7148 | -44.392 | 2025-09-19 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 8dadddaa-7bbb-300a-8e18-8b2b4fdadc42 | -9.1937 | -45.2886 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 293.2 |
| f170e73f-d7f8-3458-b611-0981020b8ffd | -7.9282 | -43.8848 | 2025-09-19 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 47ec67cd-3079-336c-8970-1a8017fa93f3 | -9.1744 | -45.3135 | 2025-09-19 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 127.5 |
| b596d5c4-a2da-3ad9-8e14-10c4b270b4f9 | -8.0188 | -45.7298 | 2025-09-19 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| a07eab42-7079-3685-b34b-2a0c047ffe04 | -6.9024 | -44.7656 | 2025-09-19 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4f919a4c-03e2-3edc-b091-c3a1b5c459e2 | -6.9212 | -44.764 | 2025-09-19 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| bc382f4e-7771-394d-87c0-c0087ca92b4d | -8.8801 | -46.138 | 2025-09-19 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 0c055114-24b3-3332-887e-7b5584bbd5dd | -7.9471 | -43.8828 | 2025-09-19 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| d794b7b9-99d0-37e2-96ae-323700f6d029 | -9.1429 | -44.8598 | 2025-09-19 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 8d121e8a-5bab-305c-9a29-6972da0f945a | -9.7334 | -45.9302 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 133.1 |
| e9e85ed9-9b56-3192-9098-0182ad11be5f | -6.6319 | -45.56 | 2025-09-19 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1e84c7ed-6375-35b9-beeb-19d50f5fc044 | -8.9344 | -46.3119 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 215.4 |
| b921c050-061f-3d6f-8da1-eef0df6b525f | -7.6949 | -44.486 | 2025-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 13772f13-c135-3262-bf4d-64512fa2ef5e | -8.6265 | -45.3282 | 2025-09-19 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 515917ae-8d15-3c67-9584-8ada134aecb5 | -7.5818 | -44.4971 | 2025-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.3 |
| f6352bbb-effe-3344-9653-0f84f4525d42 | -9.1747 | -45.2907 | 2025-09-19 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 12dd0113-d431-3603-a55e-b5382a8c0e60 | -8.9347 | -46.2894 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| d07ce616-03a3-3593-8cde-686fad4a6ad2 | -7.6386 | -44.4686 | 2025-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 1b7dfee9-84b5-3ab6-9a93-85de1d9f5c21 | -8.6076 | -45.3302 | 2025-09-19 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 12f982c4-8f15-30f3-8033-f2b1c2ef2e2f | -8.9341 | -46.3344 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 4dce80a6-7505-34ed-aba8-cac3ec148835 | -8.9536 | -46.2874 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 511612c6-b291-325c-b817-ef7ac809bc96 | -6.9024 | -44.7656 | 2025-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1b612a54-6a4e-3497-93a5-ab265aff2c01 | -7.1878 | -44.4193 | 2025-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 799a45c5-3a64-3b3d-849e-28e7211fd7e6 | -7.7148 | -44.392 | 2025-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 3859d415-4dea-35ec-95a6-bd1997442f51 | -8.8801 | -46.138 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 7a4c0f14-df79-35a7-b808-160818093e81 | -6.6321 | -45.5374 | 2025-09-19 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| bc0833db-bd84-3de7-a4dc-a2d8f500fb6d | -7.3366 | -44.5663 | 2025-09-19 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 3ce544cf-96ed-3c03-b014-795bc707ee38 | -7.2607 | -46.36 | 2025-09-19 13:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| ac39a064-1b12-303b-85f6-9ee444a4f785 | -8.9533 | -46.3099 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 4826f728-4bd6-325e-888b-03ef7b81e19e | -8.3709 | -44.6697 | 2025-09-19 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| f19386d6-b1a1-388a-b594-d75508ca0fd3 | -9.1937 | -45.2886 | 2025-09-19 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 61c5730f-f8b9-3d24-a36e-2981a6b26ff5 | -8.9911 | -46.3059 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| bcd00403-a700-3d4b-80f8-f7e8c5f93a4f | -8.899 | -46.136 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1ce58ae0-c1a1-3c8b-8edf-7c25a21d8fd1 | -6.9022 | -44.7885 | 2025-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 6c402f78-6693-3160-8e52-31089ecf0195 | -9.165 | -44.6273 | 2025-09-19 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 93.3 |
| fc4d2139-4637-3a1f-a7df-2d8460e5b1c7 | -9.1744 | -45.3135 | 2025-09-19 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.6 |
| f2a637d3-4479-381a-b8d1-7d6f0c5d5662 | -6.1878 | -41.2097 | 2025-09-19 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 179.2 |
| 7c36132f-f616-31eb-bb11-29461be95735 | -7.4531 | -42.644 | 2025-09-19 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 183.1 |
| 4b847659-f9d8-3f2d-bece-b9948afd2a84 | -9.1615 | -44.8806 | 2025-09-19 13:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 6794c1a8-3c70-36ff-b301-56cdf8ff24d1 | -6.9212 | -44.764 | 2025-09-19 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| cc66499a-8481-367e-b756-5fa0b52f54fd | -8.9179 | -46.134 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 2b15778e-0ba6-3054-99af-21e7933cf9f7 | -6.6762 | -44.8762 | 2025-09-19 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| fe0bf64c-dc57-344d-8478-694b7198331d | -5.8073 | -43.6352 | 2025-09-19 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 4bc7a6e4-f36d-3afc-a99d-364ec4af09b7 | -9.01 | -46.3039 | 2025-09-19 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| e8113942-1744-35dc-926e-c13bb79ceda1 | -8.9796 | -45.7439 | 2025-09-19 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 4ea88751-7cfa-3070-929a-7e99370ec1b4 | -6.6538 | -45.2417 | 2025-09-19 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| bd6cb594-8fa4-3d00-bd39-4256ce7e9043 | -7.6386 | -44.4686 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 232f16a8-29d6-30f0-9050-d59c6e705921 | -8.6076 | -45.3302 | 2025-09-19 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.4 |
| bc1af624-dcc0-39a7-b672-54080576f889 | -9.01 | -46.3039 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.4 |
| b30efd56-15a3-3277-9afd-1a6f1daad678 | -7.5818 | -44.4971 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 68351533-fee0-35d0-a819-c245ab9e8714 | -9.2087 | -46.9752 | 2025-09-19 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 6850924b-caf8-3389-b490-6e8cf4cf0e7d | -8.9179 | -46.134 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 75a83cf1-3950-3215-af85-8c983f536569 | -8.6885 | -46.3823 | 2025-09-19 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.0 |
| cdf04547-7aa3-3de1-888b-5b25a2cc721b | -9.028 | -44.9646 | 2025-09-19 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 10f3709f-4390-3a95-961e-72f3c4a95b3c | -7.4531 | -42.644 | 2025-09-19 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 140.5 |
| 4ba388cc-f5a1-3871-be3f-167053e58b6d | -7.6497 | -45.1308 | 2025-09-19 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 137.7 |
| d0fe1145-0de8-3f5e-8163-34c233f4f916 | -8.9911 | -46.3059 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 163.2 |
| adbf8404-ab65-3b1d-acaf-4b56604d0a46 | -7.5598 | -44.7743 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 22ef5d57-2a95-3e68-98c9-66c0d23d110a | -7.3366 | -44.5663 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 591d8eb1-37cc-351b-b7d0-d8bf21250a62 | -6.1881 | -41.1855 | 2025-09-19 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 157.3 |
| a26eb450-498b-3b97-9d6c-cbee96c854a4 | -7.3111 | -45.1622 | 2025-09-19 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| dc64b34b-8f58-3ed7-9638-0d7a20e3c0c7 | -8.9892 | -45.0376 | 2025-09-19 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 6d8ee48f-60c8-328c-92ad-3543ede5039b | -6.9024 | -44.7656 | 2025-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 88fe268a-fe3a-36cd-bb47-98ec76e5852f | -8.9347 | -46.2894 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| e26eece5-c253-3489-a01f-46f0c36cfd82 | -9.7334 | -45.9302 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.6 |
| b4a817f2-588c-33dd-8894-b5233ccd5b76 | -9.1744 | -45.3135 | 2025-09-19 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| fbec33c7-3626-3b90-b021-d2959fc16356 | -8.8801 | -46.138 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 7a5c491f-ae72-3c8a-9bd9-9a657d11c63e | -8.0281 | -44.957 | 2025-09-19 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| 9bad1d3b-591d-36ee-b4e4-e0d1bfdce7ee | -4.6762 | -37.6106 | 2025-09-19 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 120.9 |
| 16782578-faa5-3d6c-83f3-1704d5c2b12b | -4.676 | -37.6366 | 2025-09-19 14:00:00 | GOES-19 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 104.1 |
| 2ce1e626-bcb9-30a4-8c89-c85f8dc45f87 | -7.1878 | -44.4193 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 25b5be49-860e-3985-aeb9-6bb080c38b8b | -8.9536 | -46.2874 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.5 |
| b105dd12-4958-31e3-be82-3fb2efea2a38 | -5.5393 | -42.176 | 2025-09-19 14:00:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| ff83090c-b960-3dcc-84da-119293a0902f | -9.1747 | -45.2907 | 2025-09-19 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 142.8 |
| ccedc331-a3b2-39d0-a5c5-3ae9f8d3563b | -7.6685 | -45.129 | 2025-09-19 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3bd28d06-91c4-3c08-beed-330ff55cf837 | -8.9725 | -46.2854 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 103.6 |
| af1abaa5-9216-3129-bc3f-de54cb10e0a3 | -7.8509 | -45.6105 | 2025-09-19 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 022b56c7-f32c-3077-a840-b3a05dde47e0 | -7.2208 | -46.5861 | 2025-09-19 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| e406bd95-ea33-3db2-8eb1-9ad8b819cb0f | -9.0661 | -44.9374 | 2025-09-19 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 21859375-155b-396d-9ef8-4a91167db295 | -8.6265 | -45.3282 | 2025-09-19 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.9 |
| c1c54b13-434a-3b1a-a0b7-3d5719f1af9b | -9.1615 | -44.8806 | 2025-09-19 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 694bb6e2-3226-32a9-9db3-e2aef002afa4 | -9.1461 | -44.6295 | 2025-09-19 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 043369ea-0d01-3466-b850-25017f3670e3 | -9.165 | -44.6273 | 2025-09-19 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3035bfa8-8de3-375f-be4e-fb00fd7753bd | -6.1878 | -41.2097 | 2025-09-19 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 264.6 |
| 07ae440d-7924-381f-85b8-bdfbe4a2f36d | -8.899 | -46.136 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 90ecafea-cdde-39f8-a2cd-beba05c16afb | -9.1429 | -44.8598 | 2025-09-19 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| ea8ea3b0-be51-3e2a-a831-f8073d12c8b9 | -8.9895 | -45.0147 | 2025-09-19 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 40e2fbe8-f1d8-3b60-aa3f-08636785c137 | -8.4834 | -44.7266 | 2025-09-19 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 98.1 |
| b0e84fec-685d-3f2e-bb5a-4546bc743920 | -7.6949 | -44.486 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8d5ea2b5-178a-3866-863a-37f036bc8ea8 | -7.1886 | -44.3503 | 2025-09-19 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 23c5d2d4-754b-3f53-b584-5f5fcc0cd732 | -6.9022 | -44.7885 | 2025-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 23204dd9-4714-3304-94e8-479b04e19f84 | -9.1647 | -44.6504 | 2025-09-19 14:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 48e822b9-edf8-30ec-9970-0ccf1632f884 | -8.9341 | -46.3344 | 2025-09-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d6766fa4-5dfb-3765-ad46-29f98a61b58e | -6.9212 | -44.764 | 2025-09-19 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |


[Clique aqui para ver as próximas entradas](README43.md)
