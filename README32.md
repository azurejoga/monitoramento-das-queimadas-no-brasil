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
| 951913a7-cffe-332b-a3bc-1be9b5ffe974 | -14.17927 | -53.06484 | 2026-08-18 04:40:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40df39e1-7375-3d6b-a918-b13d33a7d6d8 | -11.14471 | -47.28599 | 2026-08-18 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aaad5b7-d354-3de6-8480-927452b0700c | -20.59344 | -45.92276 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3c02c6f-e070-3adc-8bba-d1c8c30a7231 | -20.29638 | -46.47636 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7b8b2297-8652-3a8c-bbe8-a622e26c0cfd | -21.83393 | -45.43935 | 2026-08-18 04:42:00 | NPP-375D | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26117b69-1294-3ead-a4dc-513e1ba5dc2e | -20.59776 | -45.92981 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b3ae494-ec1b-3974-b0ed-f46dc6e73f0c | -23.18963 | -49.15801 | 2026-08-18 04:42:00 | NPP-375D | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73bfa831-5a6c-3c53-b314-1208506fb474 | -23.53818 | -47.30103 | 2026-08-18 04:42:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0a9a905-4f57-34e9-b07b-28d2f4df78fc | -20.58908 | -45.92677 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03520c38-c276-3ef0-a0b7-a0eeb1c5fcdb | -17.33008 | -54.94858 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19071fc7-90b1-3ca5-9f16-08d498134519 | -20.59716 | -45.92327 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4290122-e2db-3538-8aeb-b634d74f46ed | -21.75555 | -48.79661 | 2026-08-18 04:42:00 | NPP-375D | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b94aa80-3aa6-39de-8759-c75ffe528227 | -21.72546 | -49.75972 | 2026-08-18 04:42:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 25417699-7ad9-3df1-9dbe-51b47a0b29cb | -22.83631 | -47.1155 | 2026-08-18 04:42:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| a6a11437-36f0-3d29-944b-bbee703aed10 | -22.0685 | -55.99473 | 2026-08-18 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 70931800-940c-3cb0-886b-50292e8557d0 | -22.575 | -48.5581 | 2026-08-18 04:42:00 | NPP-375D | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c4a19d2d-0e11-3c84-b55b-28b08e72b755 | -20.29275 | -46.47592 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2313f8a8-ff24-34a4-ba9d-19529df4f8af | -19.68885 | -49.03031 | 2026-08-18 04:42:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf482a8d-8daa-387c-b92b-b66aaeb00f33 | -20.61453 | -45.91796 | 2026-08-18 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68879c33-335b-3270-b95f-58c0d384b355 | -20.5903 | -45.9289 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2b3c6d8-014b-387e-96c4-0b738b5c4f44 | -22.07457 | -55.99009 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 15b06114-9894-3c6e-b9b0-0355c6491bd5 | -20.83853 | -57.67229 | 2026-08-18 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2fb26511-6b13-3599-b679-35b1e16cf421 | -20.29337 | -46.47157 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 40fb6871-f46c-351a-925a-b56b6c262bdf | -17.32402 | -54.93425 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cbd3af4-6118-303e-80b6-2b9311203ff2 | -20.61894 | -45.91344 | 2026-08-18 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e25530f1-8ff5-383c-859a-629ccfd41404 | -17.33832 | -54.92808 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56bf556a-11a1-3294-bc3a-0872fbd57ec8 | -20.3006 | -46.47258 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6fe294ee-a38b-356b-9de9-e7320df54bc9 | -20.30802 | -46.4805 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77810abd-4540-3d94-b49e-5d6380997c01 | -17.32822 | -54.93518 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5821130-8d95-3eb6-90eb-956738659789 | -20.30139 | -46.47514 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92702f34-1ec7-3732-8beb-9fd9bd923f65 | -22.06878 | -55.99749 | 2026-08-18 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89790184-a089-31e2-ada6-db2a5ef1c0ab | -20.29778 | -46.47462 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15b42307-140f-3fa7-ac1f-d673a05eeadd | -20.58848 | -45.93114 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e81a382a-095f-3042-84c4-9f9c153fb546 | -22.05878 | -52.18481 | 2026-08-18 04:42:00 | NPP-375D | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0969d33e-6086-338f-a283-ad002abcd808 | -22.07344 | -55.99145 | 2026-08-18 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83fa5b95-82c6-36ab-a7c6-4991357b5400 | -23.68469 | -51.67805 | 2026-08-18 04:42:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| b39e63d3-57d1-337f-8703-1e974dff8485 | -22.37468 | -49.781 | 2026-08-18 04:42:00 | NPP-375D | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b8c1b9b-419c-3bb9-a328-daf4f9c69335 | -20.20897 | -44.74467 | 2026-08-18 04:42:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6be7c0a3-b098-3c26-8154-454b3251c0f0 | -23.68533 | -51.67419 | 2026-08-18 04:42:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| 5a71739e-9d10-3431-9808-f3f1330839c5 | -22.06933 | -55.9904 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1e5a43c1-da88-3e98-bc05-63b361b9792e | -23.81998 | -48.71165 | 2026-08-18 04:42:00 | NPP-375D | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 297b3997-d5a6-3bd1-af04-fb9ceb9aa859 | -18.60353 | -48.20187 | 2026-08-18 04:42:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7675997-a8de-366c-8787-04136b8cd1b5 | -20.3036 | -46.47739 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdde1f48-4f7d-39a5-90a2-0ef92558554b | -21.72604 | -49.756 | 2026-08-18 04:42:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1e16be76-04e8-38a2-9de8-726cf241ab1d | -22.07015 | -55.9861 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 786ab6db-7a44-3d2d-8132-0433a2275464 | -20.59281 | -45.92724 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5959b851-be90-3dc4-8268-0223925cb350 | -23.18775 | -49.81089 | 2026-08-18 04:42:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e039d92c-ad72-3c7b-b4c2-3632e8ff1f7f | -20.29405 | -46.46682 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5e1ea6b-aa24-3ea7-83c5-a8eabc8930d9 | -20.71081 | -49.37098 | 2026-08-18 04:42:00 | NPP-375D | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7b4b1dec-9f9c-36ac-aede-e4cf4b5b378a | -22.06962 | -55.99328 | 2026-08-18 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e589a4a2-62c3-398f-99fb-577582ca2525 | -20.59595 | -45.932 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66287084-96e9-3ab1-92f7-e7624a85f707 | -20.30422 | -46.47308 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29368951-f51e-3a73-b560-b4924a2e020c | -18.84585 | -47.13971 | 2026-08-18 04:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7733a0c-984d-3d00-a077-0787a71943ba | -20.29999 | -46.47688 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 11343662-7e14-3a30-8360-1dfd611b0243 | -22.06186 | -55.9844 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a00ecc-f9ba-3a8c-ac01-e5a95b417a35 | -19.68551 | -49.02974 | 2026-08-18 04:42:00 | NPP-375D | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 707693dc-57d5-310f-8271-b0614bb2a5d8 | -20.5972 | -45.93403 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86c5aa26-9ce4-3c15-b7f1-4a339a84e229 | -20.29699 | -46.47204 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2766135e-134c-325e-93c1-f0c360a52e25 | -21.97825 | -48.16757 | 2026-08-18 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a0d165b-715f-3f51-a0fb-8bada95c21ba | -19.29658 | -46.50943 | 2026-08-18 04:42:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1c06cf9-9090-393f-8ea7-5949b69c4b0c | -20.38535 | -46.53284 | 2026-08-18 04:42:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 990a67bb-3a2c-354d-a9b2-413c732a6f12 | -22.06269 | -55.98004 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5a4d994-c604-3873-b735-df6c98d8359f | -21.72213 | -49.75912 | 2026-08-18 04:42:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 9f5e8992-1812-3423-a2f2-e152b6b46b77 | -20.59524 | -45.92033 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 617639ad-d000-3e76-b4f3-25049da1fb12 | -20.59222 | -45.93157 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0993d3e3-9d63-3e8b-be22-2642156da6a9 | -18.95587 | -47.31891 | 2026-08-18 04:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88be671d-ddd7-3226-bba1-15fc3f4c12ad | -20.3008 | -46.47943 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef246696-f645-338e-bbc3-33853ebcc7e3 | -18.95029 | -48.09755 | 2026-08-18 04:42:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d18f2d5-5be1-336d-be21-b1b7b69c7192 | -20.64018 | -57.91349 | 2026-08-18 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c3adff30-a8bb-38d8-b974-110543c80f61 | -20.59089 | -45.92444 | 2026-08-18 04:42:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ace44a08-df13-3f14-a3c7-a996c81f9300 | -18.81304 | -46.74839 | 2026-08-18 04:42:00 | NPP-375D | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 967697e2-acf4-3eb7-a3e5-51ff3d053000 | -21.61695 | -49.01884 | 2026-08-18 04:42:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b3de08e8-847b-3eb7-a818-fe7495de5ba4 | -23.6183 | -51.78485 | 2026-08-18 04:42:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aecaffb8-e86b-3420-9334-3f68bdf5a879 | -20.29547 | -46.45695 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3b63f7f-3611-3117-a9e7-36f8b46b5cc1 | -17.34584 | -54.93464 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10e853a9-dfa9-3541-b6b8-0f1312d87261 | -20.62204 | -45.91863 | 2026-08-18 04:42:00 | NPP-375D | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e8263ce9-75fc-3053-a0e8-dae2f9145733 | -20.305 | -46.47562 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2ef456a-0262-3f56-b20e-f50614faf340 | -17.34167 | -54.93354 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2cf76958-6a6f-36c8-a80b-efd48ee310c0 | -21.97424 | -48.17096 | 2026-08-18 04:42:00 | NPP-375D | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba982388-0758-3f5c-8e69-99fc9e9d50f9 | -23.53519 | -47.296 | 2026-08-18 04:42:00 | NPP-375D | ALUMÍNIO | SÃO PAULO | Brasil | 3501152 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f1cbb6a-1085-3039-b0a7-2665a0e0c8d8 | -22.07048 | -55.98895 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 876713d8-1837-3242-a863-0bc91a5c4191 | -20.83384 | -57.67117 | 2026-08-18 04:42:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8a26882b-2953-3887-805b-a2bb6fa75a99 | -17.81987 | -52.02303 | 2026-08-18 04:42:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e04d9fe-d388-368c-907b-1914331c9214 | -19.01933 | -47.05695 | 2026-08-18 04:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eaf93030-7d3d-3df8-ba78-7d7a9d9b6c13 | -21.7188 | -49.75852 | 2026-08-18 04:42:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| df8fbd52-56e5-3409-808b-9f37470fd65d | -19.85128 | -46.21122 | 2026-08-18 04:42:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 692da22a-cbe7-3ff7-b204-5cf1884ebf0d | -17.33429 | -54.94948 | 2026-08-18 04:42:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e70fadf8-86c6-316e-8498-fac5ed3fdcaa | -21.33361 | -49.23244 | 2026-08-18 04:42:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a0121812-f656-3259-9116-93d16557252a | -21.72271 | -49.7554 | 2026-08-18 04:42:00 | NPP-375D | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c60d2aca-1124-3b35-a686-6f1ea0e8f2ad | -22.06436 | -55.99382 | 2026-08-18 04:42:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7310d76e-b4de-3fda-a489-381a24bd7d36 | -19.2972 | -46.5051 | 2026-08-18 04:42:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7ae8c8d-a7fd-328d-9ffa-053c3685ee5d | -18.95529 | -47.32282 | 2026-08-18 04:42:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ed5be84-3325-3772-9f71-e464ae2a5b49 | -20.29766 | -46.46734 | 2026-08-18 04:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f346b0a-3553-3105-aef6-7bffa1c00412 | -23.68133 | -51.67739 | 2026-08-18 04:42:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1bc16750-2271-3c3a-80e9-8c779eb7213a | -21.37064 | -46.71243 | 2026-08-18 04:42:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e3c6a6f4-79e6-35a1-a16b-6427c6778695 | -22.06599 | -55.98529 | 2026-08-18 04:42:00 | NPP-375D | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbaab721-4207-343b-8cc2-e9a93c0740b6 | -27.88211 | -53.29899 | 2026-08-18 04:44:00 | NPP-375D | PALMEIRA DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4313706 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc304d51-cf1d-344c-91d4-a544b9a39bb7 | -6.8594 | -59.0125 | 2026-08-18 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 555ca720-1897-32fb-8575-0d77687f7417 | -8.604 | -50.3527 | 2026-08-18 04:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 7f0423a7-5093-3b91-9edb-51632e672d65 | -6.8411 | -58.9939 | 2026-08-18 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 30.8 |


[Clique aqui para ver as próximas entradas](README33.md)
