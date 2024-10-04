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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc2c4b6d-6d22-3ee2-a535-1c05bd06d251 | -19.187 | -43.4997 | 2024-10-04 00:26:52 | GOES-16 | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 3fb2db0a-e6b7-33a3-86bc-ae5bd24b9d86 | -19.3167 | -42.5724 | 2024-10-04 00:26:52 | GOES-16 | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.1 |
| b6c1a680-ab14-3f08-9d45-86d469d2eb51 | -20.1036 | -43.4276 | 2024-10-04 00:26:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.9 |
| 6196eb05-e028-3ef6-9045-54d1e437c4cd | -20.1044 | -43.4026 | 2024-10-04 00:26:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.6 |
| f3c32517-1b0a-35b7-8fab-d9e097997167 | -21.3328 | -48.8277 | 2024-10-04 00:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| 58b948f7-a438-31cb-9499-13b37915e716 | -21.3334 | -48.8044 | 2024-10-04 00:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 107.8 |
| a4c15fd8-794a-31e1-b184-2fa555ed2525 | -21.3534 | -48.8229 | 2024-10-04 00:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.8 |
| 1407accf-3281-3fc4-a0fa-42091a2815bc | -21.3541 | -48.7996 | 2024-10-04 00:27:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.3 |
| 5f598761-dafd-3865-9408-ee2dbd2af483 | -21.7988 | -48.3691 | 2024-10-04 00:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 589e97c8-ea17-3ada-b4f9-b3244b5e0005 | -21.8079 | -48.7626 | 2024-10-04 00:27:06 | GOES-16 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 4af8e32c-b50a-3197-aee6-c3d3d942586c | -21.8175 | -48.4346 | 2024-10-04 00:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 2bc270c8-af81-3b6f-ab7d-81bff5ebfd52 | -21.8189 | -48.3876 | 2024-10-04 00:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1fad1cb1-9599-306b-80dd-5549f8a67b6e | -21.8196 | -48.3641 | 2024-10-04 00:27:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 151c21b3-9c66-3f04-b810-58333156a22e | -21.8376 | -48.4531 | 2024-10-04 00:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 115.6 |
| c811c276-b552-3d22-ab17-1a0a97254ff7 | -21.8383 | -48.4296 | 2024-10-04 00:27:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 2cf4ce83-4642-3cc4-80b9-f266d4535fff | -21.8584 | -48.448 | 2024-10-04 00:27:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 7b7e4dab-1ba3-3212-87de-b86102a374d3 | -21.8591 | -48.4245 | 2024-10-04 00:27:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 92be5101-9b71-33c1-a41b-79a0f7fe09d7 | -2.9494 | -52.7748 | 2024-10-04 00:35:23 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 85ece65d-eb3c-3530-9e8b-3e15b9385cca | -3.2349 | -50.3695 | 2024-10-04 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 2300bf5a-44f2-3877-a389-9c5669cf9f5e | -3.2534 | -50.3689 | 2024-10-04 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| aede6d8f-a8a2-32fd-83e1-5d5d1d1ca270 | -3.404 | -42.2858 | 2024-10-04 00:35:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 2dca98a8-120f-3506-aafc-9e8738554183 | -3.2899 | -50.4725 | 2024-10-04 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 03df8989-a6be-347d-a9ed-5e93072b3990 | -3.2899 | -50.4516 | 2024-10-04 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 263.9 |
| 19f18a08-3617-34f7-a069-d5e95d3282f0 | -3.29 | -50.4306 | 2024-10-04 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| c6f89275-0a39-30d7-9f13-491da9510594 | -3.3083 | -50.4719 | 2024-10-04 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 0312d76f-5ae8-3780-9586-55ca1fdadfcf | -3.3084 | -50.451 | 2024-10-04 00:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| 653a1748-755a-303a-9332-d19835739649 | -3.4915 | -50.8004 | 2024-10-04 00:35:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| df72140b-4e05-376b-9aad-848ae4f43ce1 | -4.0949 | -48.4894 | 2024-10-04 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 9cac3642-d3ec-314f-8b28-cd9cb1bbed87 | -4.095 | -48.4679 | 2024-10-04 00:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 8841c65b-2631-3d25-a6c5-ab0f401f999c | -4.4657 | -42.8877 | 2024-10-04 00:35:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 228cf309-575f-36fa-93b8-14d5d453d44f | -4.5188 | -43.3051 | 2024-10-04 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 45eaea33-9465-3be0-ab8c-fcf3a6f47499 | -4.5375 | -43.304 | 2024-10-04 00:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 0deae9c2-937f-3c97-a10a-04625c94b763 | -4.6684 | -45.8961 | 2024-10-04 00:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 43068e48-ca2e-3eeb-bef6-1d911f977b88 | -4.6686 | -45.8738 | 2024-10-04 00:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| bef7d387-6c57-3d65-ba9b-66c944454d0c | -4.687 | -45.8951 | 2024-10-04 00:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 252d9714-8089-3fce-8fce-384515e02c47 | -4.6872 | -45.8727 | 2024-10-04 00:35:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 173.8 |
| bba84265-0dbb-38d8-b90b-29899ac11a95 | -5.5033 | -48.8046 | 2024-10-04 00:35:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c614db51-8555-3927-9390-109d4a3e4099 | -5.5218 | -48.8035 | 2024-10-04 00:35:37 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 11189f19-846f-344b-810a-a480f3158832 | -5.8214 | -44.1426 | 2024-10-04 00:35:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6504b56d-033f-38e2-884d-3f158770b796 | -5.8216 | -44.1196 | 2024-10-04 00:35:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| c08166a3-8bba-3b4c-8e3d-9cc5a3f593eb | -6.2524 | -44.132 | 2024-10-04 00:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a47fc30a-8ced-3f10-80f5-e6df3dee4ca6 | -7.4557 | -72.6984 | 2024-10-04 00:35:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6d852867-b7bb-3ecf-9ffe-85cebbe2ac73 | -7.8539 | -45.3611 | 2024-10-04 00:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4828a7b9-2c78-3900-8804-536cc0181f04 | -7.8541 | -45.3384 | 2024-10-04 00:35:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 01580263-2807-3c18-9fd0-ee6d1e60bfa8 | -7.8164 | -50.543 | 2024-10-04 00:35:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c38c7ccb-138c-346c-bf3d-04aeac259b28 | -7.8166 | -50.5219 | 2024-10-04 00:35:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| bbd5115a-9b13-33f3-bba4-fabc31054356 | -8.2986 | -50.9059 | 2024-10-04 00:35:53 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bce38c5b-10e3-3dc6-9610-32a3781d5217 | -8.3128 | -49.5679 | 2024-10-04 00:35:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| fb200aaa-2d10-3c5f-9e16-91496aed46e8 | -8.6448 | -50.0518 | 2024-10-04 00:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| ce449a0a-02a9-37da-bdf3-11229b9c6a2a | -8.6451 | -50.0304 | 2024-10-04 00:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| badd8dc1-8887-38d4-b073-888e4646e2e5 | -8.6636 | -50.0501 | 2024-10-04 00:35:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 03a51a09-5623-3128-96f6-0bfb795d993d | -8.6491 | -66.6396 | 2024-10-04 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ba6a8ce5-1171-3b2b-abeb-6f2d225da87a | -8.6492 | -66.621 | 2024-10-04 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e1a1db37-4cd1-3e3b-9a60-27c2d71338a1 | -8.6676 | -66.6391 | 2024-10-04 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f3804024-aca4-3876-b0b5-c862f66c3b30 | -8.6677 | -66.6205 | 2024-10-04 00:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 4cf9c836-5f3d-3397-853d-3f63df080b72 | -9.1481 | -43.1611 | 2024-10-04 00:35:57 | GOES-16 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| 25014b32-4cba-3e71-bd59-2d13a7f9d426 | -9.1671 | -43.1588 | 2024-10-04 00:35:57 | GOES-16 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 0c86258c-3e5a-3918-90c3-6d88d14c637e | -9.1041 | -50.902 | 2024-10-04 00:35:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| ff9e0068-638d-3c43-93a5-4c846cb3fb1b | -9.1158 | -51.5315 | 2024-10-04 00:35:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 731cbfd0-ce6d-3c60-83d9-510bc15d217d | -9.5686 | -64.2171 | 2024-10-04 00:36:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 768bccab-7386-3eed-a5a5-a4eb923acdcf | -9.8353 | -46.7502 | 2024-10-04 00:36:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 1d2e1890-bfe4-3dc2-a572-8104701a10ff | -10.4424 | -50.7336 | 2024-10-04 00:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| b7446c5e-c695-3a7a-bbef-6088366aa46c | -10.4613 | -50.7317 | 2024-10-04 00:36:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8f4e7928-c3f0-3ba5-b22e-e022594e0a53 | -11.0536 | -46.5118 | 2024-10-04 00:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b1923dd6-f6fe-3fd5-a1a2-01038c253921 | -11.5238 | -65.0615 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| bad4d6bf-fde5-3517-9145-d6d9d456b4f5 | -11.5425 | -65.0607 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b549698e-3dae-32ec-8636-6455bae92be8 | -11.5803 | -65.0212 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1acbe82e-2942-3bb0-bc6c-a3ba2b708311 | -11.5991 | -65.0204 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 1028f962-c64e-3baf-b4c1-6479546172ec | -11.5992 | -65.0015 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 31cb636a-07a4-3335-8dad-30e38040f29c | -11.618 | -65.0007 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| f7de3b60-b50d-3e9d-9e87-349b21bf1548 | -11.6181 | -64.9818 | 2024-10-04 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 2b3a4dd0-09c0-3b62-88fb-7dd368c308da | -11.6369 | -64.981 | 2024-10-04 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.7 |
| bf4d5043-f72b-33eb-a6c1-4dd6eb83b5f8 | -11.6932 | -64.9785 | 2024-10-04 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 789b7451-8eeb-365b-a3ee-bfe326cafa2f | -11.712 | -64.9777 | 2024-10-04 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b59f36b9-d765-3c89-9b02-d939a70f9a25 | -11.8052 | -56.6024 | 2024-10-04 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 5f8bdb83-6c4f-3504-9c3a-1626bf4408e9 | -11.8242 | -56.6009 | 2024-10-04 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5c782b92-8055-3642-a5b2-3ac58ce03069 | -11.8244 | -56.5808 | 2024-10-04 00:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d7d3b108-d9fa-37fb-8528-057c589af4e0 | -11.8957 | -56.9554 | 2024-10-04 00:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| aaabf5ee-95cd-3151-be72-89f7c9bea477 | -11.9147 | -56.9539 | 2024-10-04 00:36:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 12235aad-667e-33ba-92a1-d78747a4aa1a | -12.4225 | -63.019 | 2024-10-04 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 65de1c5e-2817-3531-9f7a-e4d0f8f4b07f | -12.4227 | -62.9999 | 2024-10-04 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 0538ccd3-503c-3651-87cc-4200ab3e4992 | -12.4416 | -62.9988 | 2024-10-04 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fcd27af6-60e3-3954-8af2-8d8e17627462 | -12.5898 | -53.1359 | 2024-10-04 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| b41b38d9-eced-313e-a8fb-a80b8c40c29a | -12.5901 | -53.115 | 2024-10-04 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 4d6f2458-d52b-3e29-956a-dcfe9bda2294 | -12.824 | -62.4766 | 2024-10-04 00:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 611d6721-8d87-390d-b9c7-413ee7a7c318 | -12.9831 | -51.129 | 2024-10-04 00:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 3722ce82-b9fb-3c9d-b33e-4fbc5300312e | -13.0598 | -51.1195 | 2024-10-04 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| d7a8f19c-d33b-36d8-bb0b-d0e3aebdbb37 | -13.0786 | -51.1385 | 2024-10-04 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 0453f4a6-e758-3944-9ebe-fe35e816c991 | -13.0971 | -51.1789 | 2024-10-04 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 03ef1d39-dd03-3c12-ab60-239e3e0c07dd | -13.0975 | -51.1575 | 2024-10-04 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 144.4 |
| d67cc68a-a359-3d50-a476-1165cc7016e6 | -13.1163 | -51.1765 | 2024-10-04 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 79dbb8c8-30a5-36a7-b864-8033a04770be | -13.1166 | -51.1551 | 2024-10-04 00:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 66a7aa6b-cf82-3f63-948d-7f733d17e1b0 | -13.3976 | -61.957 | 2024-10-04 00:36:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1e917a73-de9e-30d8-8e65-4b55af68d921 | -13.6143 | -51.22 | 2024-10-04 00:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 383509fb-4516-3f1d-85cb-675364e717a6 | -13.6146 | -51.1986 | 2024-10-04 00:36:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5ab792c4-d29b-3037-ab30-3825a56e733b | -13.9845 | -44.0236 | 2024-10-04 00:36:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 6eabcc4f-07f6-3461-adec-ae0f1af1dd3d | -14.0035 | -44.0438 | 2024-10-04 00:36:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 2add42be-287a-35d9-ae71-c6dbad7db0b1 | -14.004 | -44.0201 | 2024-10-04 00:36:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f2b6b0b2-8896-3a90-b7b1-b6adb94613f5 | -14.7939 | -48.0275 | 2024-10-04 00:36:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 009fe115-c3df-3f40-ab33-c16aa22ef3fc | -14.7944 | -48.005 | 2024-10-04 00:36:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |


[Clique aqui para ver as próximas entradas](README6.md)
