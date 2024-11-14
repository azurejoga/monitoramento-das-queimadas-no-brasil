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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 093ac3eb-c261-33f7-b931-90ddb38474b6 | -4.42835 | -47.23572 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc3b2c78-530c-3b04-b89a-3e0379584099 | -4.35214 | -49.68274 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 907a9a15-5731-39f9-b702-181688129042 | -3.04593 | -50.32853 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3f379e1-b9be-3132-ab0e-9601efa82cc5 | -0.41408 | -51.58188 | 2024-11-14 04:40:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 83533cb4-ad21-3218-9b87-3cb0eb0186eb | -2.42008 | -46.26857 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eec998ac-195b-3ead-85c5-f5c633570e56 | -2.64724 | -46.18231 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 56adde5f-8e9c-3875-8679-4e041f366bd7 | -3.90061 | -50.08843 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ec7a79a3-3ae0-3652-bbab-f789ef54a0dd | -3.30426 | -43.5136 | 2024-11-14 04:40:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fdfef703-7bc2-397c-8ffc-c06a05d1b068 | -2.65544 | -46.83407 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdbbdf56-7cd5-3044-9d8c-94f22d95618d | -2.17379 | -48.75208 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf549f2b-d178-34d7-b448-0405f7fe800e | -1.68827 | -53.75245 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37e54977-4066-39f9-9cd2-41b39f5db2af | -1.48011 | -52.09866 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0cfcc7c-9a79-39ee-8bfb-314e2df61b2e | -1.8587 | -47.8281 | 2024-11-14 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65ce8420-4baf-36f6-95b7-902b6499169e | -3.86946 | -41.03643 | 2024-11-14 04:40:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 84c9396b-3164-30bc-8c6a-caac505119d3 | -2.65602 | -46.83036 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bba1f471-d132-3a03-8d13-b10a9c78212d | -2.64312 | -46.18571 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b6cdf37-55e7-3388-81f9-c76dd35ac588 | -2.08451 | -45.60113 | 2024-11-14 04:40:00 | NOAA-21 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d38bcc7b-aadb-38fd-a867-5d7b228ecc5d | -2.6367 | -46.18072 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0fd1ba2-d4de-359e-a579-5331d5ea403e | -2.17234 | -48.54471 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ed3f464-9a91-39b2-8742-5fa6351ec3ee | -2.40702 | -48.47912 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 571f9ec3-4ff0-371d-b5b9-4ad1d0d4b97d | -2.65074 | -45.80186 | 2024-11-14 04:40:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b0d5556-5203-37ff-879e-85aed9a8feba | -2.1784 | -48.54916 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38edda05-f6b2-31b3-9400-5a8c1683d54d | -4.81807 | -45.79992 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 574c8e70-4f4c-3ffe-b3c0-f6e7c674e197 | -2.65947 | -46.78525 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d6492a4-8960-38d4-99d2-13b2b05a2e05 | -3.89011 | -46.08653 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 78856d38-b62a-3801-a610-44d4f96828d2 | -3.49552 | -50.83284 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cf953c7-2063-3855-a30e-ede936d2f392 | -1.66687 | -52.53399 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d4fbf7e-b84c-32d6-a7ca-cd6c7c6ba457 | -4.5885 | -47.06003 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 919711ab-41fd-36d2-be08-9e4099056e27 | -1.35017 | -51.43112 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8872e04d-d74b-3cca-ae90-7563c8bf842d | -3.49437 | -50.8402 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90112df5-a905-315a-bb57-c165e238ba78 | -2.67028 | -46.82878 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 138628e4-cef4-3509-8eaf-d8b52ecf9208 | -5.04153 | -45.88066 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 500fa9d6-b4fa-37b3-af6c-e41ef9b2abaf | -7.22549 | -48.80883 | 2024-11-14 04:40:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2d3b1d9-1ef2-363f-8611-032816099d4b | -2.02427 | -46.94218 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f7cc16b-036f-3725-b76c-403fe380d64c | -3.40668 | -50.30798 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 384e2862-479c-37d3-a656-bd0b6961140e | -3.03018 | -48.0598 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33146e1f-dc36-399e-9428-9030ede63a6a | -3.57829 | -50.36049 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1766fb0a-acd7-3b3e-bb3a-d5fcd38ae476 | -3.4145 | -50.36759 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3d04f38-50a5-3976-bcff-9a513dc74a6e | -2.58069 | -51.92467 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0acd2973-7716-374a-b951-af593dafea9d | -3.40724 | -50.30444 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e41513d8-d97a-3269-877c-bd0c4e18c165 | -1.66378 | -48.25047 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9cadbb4-2db1-3392-86b1-ddcd2e411661 | -3.35843 | -46.08162 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8189ec2b-b7fa-356a-93d9-4649c2837e9e | -2.25205 | -48.38475 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed7cd003-5bd2-3374-a053-6a0a2d97e382 | -6.26646 | -46.9115 | 2024-11-14 04:40:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 17c9c3b4-f9d0-32ca-9b7a-3286f4569fa6 | -1.52728 | -47.2926 | 2024-11-14 04:40:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6130fdf-e6bc-3c27-a607-863239f12c2b | -4.32838 | -48.61322 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d20fc7cc-847e-3972-bb33-4f4b6d7d250d | -4.26497 | -48.53961 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b0b7c32-98fb-3f4b-a42d-6335dabcc091 | -2.82341 | -46.65673 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 46a47a26-281f-34ff-a0e5-4ef57b51fad2 | -0.83488 | -53.04432 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbe32716-17b2-36b2-ad4a-a29d47a9ebc8 | -4.64969 | -44.14918 | 2024-11-14 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 772a4503-292f-3b8a-b7ad-60aaac31b95d | -2.0237 | -46.94582 | 2024-11-14 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a13db7bf-a24f-338e-a6f5-7acd0dbd6b6b | -5.48035 | -47.00712 | 2024-11-14 04:40:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04e7fa8d-5fc9-3eb7-bed4-fa95f79e62f0 | -4.59137 | -47.06431 | 2024-11-14 04:40:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7739b92e-75e5-3dd3-8032-e1775955108e | -0.93892 | -51.72528 | 2024-11-14 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e82b566-2d57-317a-a6be-108fa1e32819 | -2.40649 | -48.48256 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5ca76c7-54eb-3a49-9d46-5bbcc490ad7c | -4.94412 | -44.96265 | 2024-11-14 04:40:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3c339f1-0243-30d6-a9a8-cf838aed1524 | -2.12767 | -48.896 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fff6062d-5329-3de0-a7e3-12a34c6495b6 | -2.18532 | -49.11602 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8efe6cc-1ff3-3b3f-a446-1110f6dbbccf | -3.79705 | -47.45943 | 2024-11-14 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3493d818-48bd-3870-b23a-2dbcefe01815 | -2.65829 | -46.83831 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2052811-6b49-39de-bd0e-dac50023a8ba | -2.30305 | -49.12379 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4999afd3-e5b5-3bca-aba5-74829942b6b7 | -1.79859 | -52.17052 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8847e909-eff2-35ca-85c3-06ba22f848a4 | -1.22416 | -51.74876 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21173864-8eb0-3c79-bcb7-1b7f5a54bd2a | -2.9244 | -47.02521 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adb2fdaa-5e29-3c80-879a-6bd3792b57c8 | -4.18698 | -48.40631 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acf5a092-603a-3f22-b3a6-a7f3c22b080c | -4.40559 | -47.27017 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97a8b245-411a-32af-8720-9baa3edaf4a5 | -2.63864 | -49.52349 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 255caa64-93ca-37ac-83af-efb8fadb480c | -1.98754 | -51.11437 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa28d254-86de-3517-83e6-1594bfed7d7d | -2.70471 | -51.87534 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| afb66d73-ed3a-3f9e-a105-f87ef76d9cc8 | -2.05667 | -49.02571 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fd4b127-45f2-390e-a5a0-abe051c1e1f5 | -5.38247 | -42.77507 | 2024-11-14 04:40:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 870e4ad2-9a66-3238-9675-59e5e1c13546 | -3.73666 | -50.43973 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a93cb5c4-4c6e-31ff-b8bb-661eab96995e | -5.1569 | -46.08425 | 2024-11-14 04:40:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c17b986-9cc9-3e37-ae35-8355359dfa20 | -2.63478 | -49.52644 | 2024-11-14 04:40:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72ee7426-e3a8-3d20-b1f6-6c18634b0eae | -1.39524 | -51.12513 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ac8995dc-b7eb-31a0-9b39-81a57954940e | -4.37648 | -48.08121 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bca40fca-5cc9-33f1-a8cf-613ab6346296 | -2.18868 | -46.6316 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3764c54c-772d-3874-997c-1ca9e52695c3 | -3.39997 | -50.30694 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47d50f75-ad58-32f7-81d2-670ea2a99498 | -0.79507 | -49.49964 | 2024-11-14 04:40:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d4e553de-b4ef-3c78-a604-b985b2ca5e69 | -2.21806 | -48.90646 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9e1d0db-0444-353e-9a60-d7345ed6757d | -3.04424 | -50.33923 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4791ab1e-45ad-3cbb-ae4f-5d2512ee1f5c | -3.11252 | -45.56873 | 2024-11-14 04:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab407e6d-b681-3a2b-bc82-38ebad0d0efa | -2.15281 | -50.91311 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 771c8359-43aa-3747-b0d2-bc7bb66551da | -2.64785 | -46.17838 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddac4a44-e483-3510-8f31-1c18c0f7ab5d | -4.39367 | -45.80967 | 2024-11-14 04:40:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d60095c5-71b9-3b9c-bbcd-d0980be2a187 | -2.93898 | -48.31902 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4184f038-0740-33ec-b953-1e2d7f9eeeaf | -2.03907 | -49.03004 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bba2cdf8-9d40-3659-9d5f-4446e008d027 | -1.49881 | -51.6195 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff100656-8423-33f9-affb-55be6ae54552 | -2.25473 | -48.73651 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29a8ecca-5690-37a9-8a2a-cd8454c8ab9c | -4.0248 | -46.96171 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69a12567-059d-3332-9ebe-27d62a96db08 | -3.77675 | -41.59686 | 2024-11-14 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 815b991b-4829-3171-bcee-b05972f45488 | -2.61879 | -48.34334 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e089fb16-02c6-39ef-a6c0-740e59b56fba | -4.52163 | -46.47967 | 2024-11-14 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6f0ebe4-563c-318a-b9a9-691c1e154c5e | -2.9006 | -46.85958 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00f27a05-5c7d-3e57-8a6e-eaf984ae13d3 | -2.82686 | -46.65726 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aed1548b-9e49-3ef2-9878-1313c85226db | -2.16866 | -48.45982 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 02b4061c-639c-361e-8529-9b7fe75b2a86 | -1.35018 | -49.14731 | 2024-11-14 04:40:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cde2e0ea-0fd6-37fe-8c95-281f2fb3c2e9 | -2.07963 | -46.56519 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb2675b-cf87-3849-b0d1-9ed88970d7bd | -3.6348 | -48.91756 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec9221bf-261c-3467-8789-fad78cd7aab8 | -3.85396 | -48.97321 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README37.md)
