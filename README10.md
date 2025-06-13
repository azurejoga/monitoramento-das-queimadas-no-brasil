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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46e628f8-f4c2-3c13-b485-5d026776528a | -11.57476 | -47.43795 | 2025-06-13 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea65c0c4-96fd-3646-a262-b91c267d4cbb | -11.56942 | -54.57841 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a8fba878-beea-368a-88c9-6c66c86fadc3 | -11.57083 | -47.43719 | 2025-06-13 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99b6af05-f78e-3d81-a68d-0ba612420559 | -13.0312 | -49.99083 | 2025-06-13 04:10:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eb3c8c4-d81f-3264-8879-dd1a9e0c1e37 | -10.63694 | -49.42996 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 30daacdb-17ae-3e9e-9868-bdbd129b71a2 | -7.96279 | -47.63618 | 2025-06-13 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75705c46-a538-3bda-a599-520eb07a589d | -9.41556 | -48.42724 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 918eb2ba-4687-39bb-9667-e2023b4614be | -11.81169 | -54.50175 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a4468b8-cdc2-3310-bfaf-2d19abd36c54 | -10.69571 | -49.49266 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a627d994-559e-3e6e-9512-b354d5bf7212 | -9.40614 | -48.42981 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de221436-d08e-3a39-ae80-ff5636757f3d | -12.00451 | -45.13668 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1b1c2185-c824-3027-a64a-3afd5bbf04a2 | -12.00316 | -45.13743 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2d8f4dde-1cde-3a9a-a94e-4d62a262d7d3 | -10.23742 | -52.23802 | 2025-06-13 04:10:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e822ba54-9815-3c1c-9114-6233e5580a09 | -10.64921 | -44.48288 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 535d34d3-692c-3a4a-af9e-b32f29e4f599 | -9.87794 | -46.27831 | 2025-06-13 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a450503e-0c42-3d54-a79e-19d741e1a1c5 | -8.07932 | -43.11563 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 6ca1ada8-c705-372d-9bde-b05428459c31 | -9.88628 | -46.27493 | 2025-06-13 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5eb4bb88-73bd-305e-aa16-71293328372e | -10.65145 | -49.42773 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aaefc242-a1f8-33e8-bec2-e99b06a4d3a4 | -7.44602 | -45.51811 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c8fe3ba0-cf70-3809-8605-f1cbd7c958de | -12.0038 | -45.13354 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8b3d0a7f-6f35-311b-985d-4f806e97bd68 | -10.18183 | -49.5021 | 2025-06-13 04:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfacbc05-2fd4-38d5-9109-65bf6aa4326a | -10.91744 | -56.84077 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85be7012-b0de-33ac-835c-bcdf8683beca | -9.41123 | -48.42643 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59bfec16-f8d3-3b0f-8a08-20baece58e99 | -10.91536 | -56.84058 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 7f1531dd-a0e7-305d-8b57-099f52363e69 | -8.87809 | -48.51411 | 2025-06-13 04:10:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4fff8929-c829-3b22-96e1-62ebab9333bd | -7.45498 | -45.51035 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 749be7b1-303d-3d19-91f0-19ee939ba99c | -13.11647 | -44.07354 | 2025-06-13 04:10:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59f3e526-8b28-3145-a139-26b6f8e3d14b | -10.92617 | -56.83483 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2954f8c6-c1fc-3147-aa83-5adeaa824e29 | -7.45722 | -45.51994 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 909fe226-69be-3973-86b7-1af47e16f1d6 | -10.64773 | -49.42233 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6f2df0f5-25ad-39cb-b326-2935bd14f489 | -8.07374 | -43.10738 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| cdeb165f-728f-3fad-9b25-030f85bd2084 | -11.80054 | -43.78938 | 2025-06-13 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c31e5d1-fbee-3341-ac08-589c445f284f | -10.35244 | -51.99356 | 2025-06-13 04:10:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d30bc0fc-9ab1-3b62-803e-2f3872d50d2d | -10.696 | -49.49448 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4a0f0739-8e11-3e95-8a8c-0aaaafe08241 | -10.64606 | -49.43152 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a542b786-4be3-375c-8c83-d8697b51b3c1 | -8.96438 | -47.96944 | 2025-06-13 04:10:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d58fe18-a852-37e8-ac51-2b650469dbcb | -10.80995 | -54.04182 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4653a60a-7c21-3f60-8720-3972cae0c2fe | -11.5673 | -54.57478 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 98a816d8-a80c-33c1-9acb-501fa07bd25e | -10.65228 | -49.42314 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fb8a7fd0-ebb3-3812-b643-c8fafa772692 | -12.05419 | -48.07874 | 2025-06-13 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34ec48fd-cd30-3e40-b13f-12d11fb56d62 | -12.43048 | -54.87115 | 2025-06-13 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25802af0-6162-39f2-9883-64ce4fbeb311 | -8.06923 | -43.11398 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 0051a03b-f5cf-3944-b938-241ef4785f7b | -8.95142 | -47.27449 | 2025-06-13 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07b5ab51-d41e-3594-af2b-ec5ebd8fec1b | -7.80313 | -40.55157 | 2025-06-13 04:10:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 64962d73-c1cd-31c1-a7b5-0ee64daffd29 | -9.36172 | -40.41678 | 2025-06-13 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9dc62c10-6b2f-3394-8a1e-596fa973bbe9 | -9.36515 | -40.41731 | 2025-06-13 04:10:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e6a5f7b6-5f1b-30f9-aefe-0dc229410fc8 | -12.28608 | -50.10696 | 2025-06-13 04:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e73ed06-f2fc-3259-b91d-21db868c5f8f | -9.66967 | -48.77272 | 2025-06-13 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3fee0cc-af8f-3569-a499-052e41238d51 | -8.09364 | -47.5774 | 2025-06-13 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e8c377a-2a2b-3087-a843-763f075cc19a | -11.13203 | -53.94738 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb62dc8e-cc78-3ced-b2c3-fa6eeb76a3e7 | -11.74864 | -54.72186 | 2025-06-13 04:10:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e7ca441-c725-3aa4-8d93-dcd19b946a04 | -12.13046 | -54.66651 | 2025-06-13 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fedd5f30-ffe5-341a-baaf-d6cbeaaefb32 | -9.60671 | -49.01279 | 2025-06-13 04:10:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0574535-1114-3787-9ee4-fdf815fee944 | -9.83968 | -44.7065 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ceb41d25-f8cf-37e6-9a0b-4a38abf5d89e | -9.84317 | -44.70709 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8abf7b3c-79ca-36c8-aa4b-94709914e062 | -12.00517 | -45.1328 | 2025-06-13 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f9da78d1-751a-3505-821c-ca2772d542dd | -13.22792 | -47.20764 | 2025-06-13 04:10:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c971cba-d31b-3677-bf8c-6b05c7c73228 | -10.69484 | -49.49736 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0fbc04dc-88f2-3937-87a0-1fe75b257f19 | -10.91901 | -56.8333 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d23d58c2-0b41-3ad9-9752-67de2fc2293f | -11.56518 | -54.56706 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 001e817f-d5ae-315e-bcf1-558c6d5bad1c | -8.81224 | -46.68823 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0afb6c2-e64f-37a8-9b8b-ad6efdb9da9f | -11.57042 | -54.57335 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 728fbe95-f8fb-3c91-9683-74b4e1ce8ea7 | -11.56209 | -54.56851 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e72578f9-49c5-3d32-ab8d-f7e034272bd3 | -8.95548 | -47.27518 | 2025-06-13 04:10:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a46b9385-f9bb-3fd2-8354-b9647069e7fc | -7.79974 | -40.5511 | 2025-06-13 04:10:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8289fdb1-0df4-3569-9945-7c21571eb355 | -7.45871 | -45.51096 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e712f0f9-6012-3529-9a32-86fae290822a | -8.07259 | -43.11453 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 116a6bbc-1f91-3245-bd68-32a954797765 | -7.44527 | -45.52263 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ee9e071-5007-392c-be32-691dd8f204c6 | -9.87716 | -46.2829 | 2025-06-13 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8db294-5437-34f2-851f-c691748c5397 | -10.63778 | -49.42535 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 04a1b612-d21a-3a4c-ac09-b4094b547ab1 | -11.17389 | -46.88313 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| de9fb7d2-78bd-34f6-91fb-ee547c0f4b8b | -13.09011 | -52.2835 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ae9a502-46ee-3ee2-9da7-83d436642974 | -11.17283 | -46.88013 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d3406935-1ed8-3fa6-9a7a-519c23b971cb | -9.84509 | -44.69544 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bb3d982-69b4-3bc5-8580-3156df653e36 | -11.13891 | -53.94535 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80447229-7271-35af-9dae-4a166d1c676f | -8.0799 | -43.11205 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8091dd94-e559-3732-bbc3-4721437fee10 | -11.17006 | -46.88248 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 332a51f1-dc7b-3752-bcf7-ac966e7ad5d5 | -11.81576 | -54.50454 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b1f31c76-462a-394a-8347-e11ffc101d2b | -10.86491 | -54.30022 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2bd6a765-bcc8-3b14-939b-ddbcb29be9ac | -9.10998 | -46.92509 | 2025-06-13 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 298fc62f-593c-388f-9685-89bbb94deac8 | -10.65683 | -49.424 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f58e766d-dab9-31c2-b6e8-96827ab16f05 | -11.81675 | -54.49968 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a594ab6-d7ac-39aa-9d4d-c00cd14b1b02 | -12.10682 | -48.87685 | 2025-06-13 04:10:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5d32d68-0c50-3c30-904e-938a749e1507 | -10.64317 | -49.42154 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83568915-2fbc-3e7a-b788-3403751abd45 | -8.31132 | -47.91848 | 2025-06-13 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7aab9d21-08b9-332a-82f2-45c2d8d5a7c3 | -8.0771 | -43.10793 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e3004b4-0388-31bf-b135-d7df9afae4b0 | -7.45124 | -45.50975 | 2025-06-13 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f4077a46-4460-34a4-9027-483e288b011b | -13.09037 | -52.2884 | 2025-06-13 04:10:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16bc2cef-1ed7-3807-ba06-92050a4abd54 | -8.07653 | -43.1115 | 2025-06-13 04:10:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e3a00a97-3e3a-3775-b50e-07a6a7fa5854 | -11.17857 | -46.87895 | 2025-06-13 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5d9550e4-05e3-36f2-a47e-732ae1a5b3c5 | -10.6469 | -49.42692 | 2025-06-13 04:10:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d5b49695-6fe0-3219-94ee-c5d008299346 | -10.70028 | -49.49349 | 2025-06-13 04:10:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c249358f-1d79-32a7-817e-3d4eb5dba862 | -10.65203 | -44.48722 | 2025-06-13 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.8 |
| acd3798d-3157-3e96-a1ba-ee0a67ef1ce8 | -11.57141 | -54.56834 | 2025-06-13 04:10:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9284e553-a891-38c7-9862-082d08d4b6f0 | -9.84289 | -44.68706 | 2025-06-13 04:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ded4cef-3ebc-3ea6-9f96-30155d619baf | -10.86679 | -54.3046 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3140fd14-03e8-39c0-ae88-f263d2281d93 | -7.74889 | -42.91246 | 2025-06-13 04:10:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c701cd87-16d1-3613-8f16-1574ca6d20ba | -11.13115 | -53.95189 | 2025-06-13 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c02e468a-c6c1-3612-b3cf-a944b9d672f6 | -10.92405 | -56.83464 | 2025-06-13 04:10:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 339249a7-c931-3d41-84f3-cf2a8de3887e | -7.20038 | -45.34942 | 2025-06-13 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
