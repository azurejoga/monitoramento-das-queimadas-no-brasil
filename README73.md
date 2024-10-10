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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebe5b8e5-b406-308e-b2d0-3ef3381c177e | -11.32682 | -45.82466 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ad5b266-bc01-390e-aa53-28279e2115b5 | -11.13949 | -45.38031 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94a5a6d0-ca24-3a69-8915-e6b5552798b5 | -13.0005 | -46.25195 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f3bd402-480a-3d5e-9fa0-deef14dc593f | -12.99817 | -46.25192 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82019eb7-2876-3ca4-80eb-edb3c17fad6b | -12.99265 | -46.24376 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc408162-729e-3308-8e6c-f981d958824f | -12.98932 | -46.24322 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbf94049-068f-3850-a0a5-69036b8d0b3f | -12.98656 | -46.23914 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3a1ad08-8f5f-3ee7-8c40-cf10f45031c3 | -12.9838 | -46.23506 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbd0002f-9d70-3e44-a106-7e53b0a71416 | -12.98324 | -46.23861 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4091d47-bb97-3ed6-a428-6e55401dd9d5 | -12.98212 | -46.2457 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 30965415-b9ba-3ea2-afad-9015cbe18fd5 | -12.98156 | -46.24924 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 528ee2b4-aa04-3a28-ae15-eb9d9a6cc2be | -12.98103 | -46.23097 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 665867a5-f947-37c6-90df-927abf5ab7d9 | -12.98047 | -46.23452 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fff837b9-137c-30be-ab52-824b837d8106 | -12.97995 | -46.21628 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43865ed2-4b19-3f90-9520-8e2a4323fedd | -12.97991 | -46.23808 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d948e077-2521-3cb8-9462-0a7af3b73307 | -12.97939 | -46.21983 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9467d4c6-657f-3dd0-8c59-1ea86d089d58 | -12.97936 | -46.24162 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6450731c-0f1e-32ad-9a7d-be0312ab1c22 | -12.9788 | -46.24516 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ff90a4b-7829-31bf-995c-2455a53e3868 | -12.97774 | -46.20865 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04d8b1be-67c0-3e23-8f97-ba70369cf9c8 | -12.97771 | -46.23043 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 312e06b1-3ac6-353d-94f7-5b5cf2ff9736 | -12.97718 | -46.2122 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8856ffd1-0801-3f7f-b1ac-fba1a07ff9d6 | -12.97662 | -46.21574 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 46bffb5b-3520-335b-b599-44ba266e0790 | -12.97606 | -46.21928 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a990f0e2-4391-3652-88dd-f1c863f01ffa | -12.97498 | -46.20457 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58b67eee-5f4f-3655-9c9f-774de3721beb | -12.97495 | -46.22636 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2680f0a0-d19e-3edc-8ce1-0b8df6246bf8 | -12.97442 | -46.20811 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21113ec8-1c9f-3ee4-9484-442aece085d4 | -12.97439 | -46.2299 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| ba15d54c-19c6-392d-a0e4-17430cf95856 | -12.9733 | -46.2152 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98de718f-7c04-3df5-8dee-dada64dc4608 | -12.97274 | -46.21874 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7bc748c3-3e5f-3cb2-90a7-1edf40aa7a67 | -12.97218 | -46.22228 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e3ccfe0-bb37-3337-82a6-ef8a6fe4290a | -12.97162 | -46.22582 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| db0b0aec-28f5-3d94-b94c-48c18488beba | -12.96998 | -46.21466 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 384c8b7d-c706-3c88-8037-9903c81aa6c0 | -12.96942 | -46.2182 | 2024-10-10 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f369e4a-29ed-39fc-8e5f-71ee9e28c3ec | -6.76304 | -45.64853 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fb84a425-8973-3f44-b773-7b5ffc43f959 | -6.74288 | -46.29613 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bc39244-1f7d-3866-87b7-b12d41e1776d | -6.74229 | -46.29982 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2df035d8-ae8d-3e4b-b5ae-7f098a206896 | -6.74007 | -46.29191 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 313df180-3b15-3250-ad40-43d2dabc51d4 | -6.73947 | -46.29559 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 708d1927-b1e4-3685-91b4-2d74d2971adf | -6.72638 | -46.1171 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c73ed96f-d82c-3c6e-b4f9-beb2eaefb772 | -6.66404 | -46.33246 | 2024-10-10 04:19:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a1452fe5-7a23-337f-abd6-f99b4ddd2448 | -7.59521 | -45.64703 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2225359f-2be6-3e4d-9261-2cf4569284ac | -7.42796 | -45.61722 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26f013c7-572c-3777-b606-b0c74bb4647f | -7.4274 | -45.62074 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3152d8e-9c18-3af3-947a-b25e38e27442 | -7.42462 | -45.61668 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ab323145-146f-3b92-a77c-b8b34f8a5756 | -7.42406 | -45.6202 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95d165c1-1e8d-314c-8554-94ae0afd9165 | -7.31662 | -45.59235 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c069b6-a75c-3387-aa38-cc1219a41661 | -7.29942 | -45.52818 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 079dbe9e-8f07-35ca-b764-4b423b5506f4 | -7.29885 | -45.5317 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 159f1f3f-feec-3153-b72f-79baee4d5afb | -7.29829 | -45.53522 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e708efcb-539f-3f32-8106-16675718a048 | -7.24779 | -46.45905 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9369baad-b580-346c-ad9f-aaa7b35e3334 | -7.24437 | -46.45852 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1b67b57-53cc-3ac5-80c4-381588ecd0ec | -7.16711 | -46.1799 | 2024-10-10 04:19:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c12243f-f7f9-30a2-8254-6eb1da8dcff8 | -7.11118 | -45.32871 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 243fe443-ae3e-3e0b-9644-22f326c5ba86 | -7.11062 | -45.33222 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08457bfb-a016-35ed-8b56-6149ae178305 | -7.01734 | -45.45426 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e88c454-4594-314a-8087-aee6102e28be | -7.01678 | -45.45778 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81f3ba48-8439-36a3-a96c-ce6e8755372a | -7.014 | -45.45372 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 841dd8e4-5a8e-3fd1-b891-8d3d0fd21896 | -7.01015 | -45.37026 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 62345f4a-52e5-348e-a26f-9011de51d8b0 | -7.00738 | -45.36622 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17c9ccc2-8bc7-3512-a82b-1fdea0991ad7 | -7.00682 | -45.36972 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d211f2e-e998-3184-9836-801d696faaa6 | -7.00404 | -45.36568 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5c81485-c224-3633-9b71-1757a685e1ce | -6.99076 | -45.23438 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a7e6c87-2e6e-36f2-9980-092500ba7632 | -6.98874 | -45.23048 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d54f7d58-5084-37ad-8a60-c23ca0305e43 | -6.98819 | -45.23397 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f0cded8-ad00-38e6-8eef-1200376cc8e9 | -6.98709 | -45.24098 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a7b26dc-4bcb-384e-bf59-40f593468358 | -6.98486 | -45.23345 | 2024-10-10 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f923e27b-0f6b-3bd7-90a4-c6413aa6c50f | -6.98456 | -45.38058 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3baca3d6-1dcd-3528-9576-7ffc5f44413d | -6.984 | -45.38407 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d01b3cea-627f-37aa-a2f9-0a563c5d5530 | -6.97931 | -46.0015 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 81a1e467-589d-3653-ab4f-62df14ed4efe | -6.97342 | -46.25335 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b219877-56f4-3de1-9cc1-2030d403b2a7 | -6.97181 | -45.71869 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3db46530-1a94-35e4-a8a6-b2bd7af2bcda | -6.96718 | -45.79089 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86c8521b-dfcf-33ea-976e-17ae530612aa | -6.96382 | -45.79035 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 937b7e3e-5a3c-3fe3-8b8b-735bc5317bbc | -6.96269 | -45.28723 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 180bee53-29af-330f-9f02-98a00c9649b9 | -6.96245 | -45.64803 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35df6ad7-771c-3f6a-b2eb-a571ec20fe60 | -6.95991 | -45.28318 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b3becb1-e072-3711-91f8-8d3197f651ec | -6.95966 | -45.64396 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 815f0862-3a01-36f3-b9a3-042cf29a9944 | -6.95936 | -45.28666 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f1d49961-f9fe-39ea-9688-5976bfa6b4e0 | -6.95768 | -45.2757 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70e78285-8003-3451-81dd-f465d68dd23b | -6.95713 | -45.27917 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 249625aa-0d1d-3bbb-8477-18091a38fe43 | -6.95658 | -45.28264 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 44ed8807-8d44-3d06-9ad9-315b236808f9 | -6.95324 | -45.2821 | 2024-10-10 04:19:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| bbfc4303-cf3a-39b3-ba2a-d3aed5e2e99f | -6.9411 | -46.4102 | 2024-10-10 04:19:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c102a5be-fc76-30dd-bf27-f01c0ee3b09c | -6.84314 | -46.21784 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc69101b-2c7d-3a3c-9cf9-5dace6c2da45 | -6.84255 | -46.22149 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 603d8929-6ab7-3261-b276-a26aa616925d | -6.83973 | -46.21731 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39444792-7dc2-35b9-a49d-70757e05789d | -6.83914 | -46.22095 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57c92dec-780c-317e-8abc-cc0f5b82bc50 | -6.83574 | -46.22042 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3fce3c68-e0f3-3b7f-a0dd-afe1de594746 | -6.81367 | -45.96426 | 2024-10-10 04:19:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cbb5458-413f-3369-a5b9-0a24c2f63de0 | -6.79772 | -46.12873 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b9ef152-88c1-3803-886f-f685d2c166d1 | -6.79714 | -46.13236 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5efb0f10-e26b-351f-b94c-7a025044cce1 | -6.79433 | -46.12819 | 2024-10-10 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c801e415-b97f-3c6a-ac0c-faaba8ec3c95 | -7.82103 | -46.47798 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a335cf7-30dc-3275-a4eb-a9a595186a08 | -7.74836 | -46.58422 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4a24139-d3f3-335b-8c9e-69fbaf2a06ed | -7.74777 | -46.58792 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 413cc2ca-ff3d-3644-8cf9-0eb8657d1510 | -7.74733 | -46.58718 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9cce1db-d738-3242-a421-2f9384498d32 | -7.58653 | -46.80723 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7c67e6ef-a0a3-3ba7-8c11-1f39dc92845c | -7.58592 | -46.811 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9c8b7340-2b70-33e4-92ce-dc419230d9f7 | -7.58308 | -46.80667 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b1835afb-f2fc-3f24-9acc-b964463daab2 | -7.58248 | -46.81043 | 2024-10-10 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |


[Clique aqui para ver as próximas entradas](README74.md)
