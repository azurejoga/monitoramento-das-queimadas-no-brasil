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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 021b915c-fcaa-33a6-8d0b-ce491fc39de7 | -8.43854 | -48.69495 | 2025-10-24 04:38:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c73a4a1e-516b-32ba-9130-2aa45ef657a0 | -6.28637 | -47.01257 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5c27ac4-e698-3ffd-b6a2-61001799dd50 | -6.88608 | -43.6143 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6dda36d5-6ccc-37af-8a78-ea348789324d | -10.40826 | -47.1128 | 2025-10-24 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92de5267-9c70-320c-8fd2-8eba4bfa470b | -9.60369 | -46.9169 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bf6e86dc-5c3d-33ba-b92a-2d67daea1acd | -7.49245 | -42.57688 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 01538c9b-b6f1-32a6-b5fc-8096550fe7ff | -4.8136 | -50.93823 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6445302-a27e-39d4-8c22-a5f32f8c2f17 | -4.84318 | -47.80145 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5a972af-0540-395c-8146-c1e0b3c60c15 | -4.34647 | -50.59295 | 2025-10-24 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ad760b8-34da-3b54-986b-0f3c6dfbf903 | -4.28226 | -48.25821 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 408185c0-9bd1-3dba-a364-64c7a3b0f489 | -7.9077 | -48.94364 | 2025-10-24 04:38:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 67c9e061-3729-3699-b8e3-b0374d6210b2 | -10.87015 | -44.41279 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 513f7cba-ac10-3c47-8b64-2ccccabfea88 | -9.30487 | -45.2019 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 409e7329-2eed-38be-ac1b-78890bd4a2af | -2.86128 | -50.73747 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| accf0dd5-245f-3687-bc12-d9a0241b5b72 | -3.60099 | -49.90119 | 2025-10-24 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2bc856b-a14e-3dd1-9d6f-a7a8cd2c49fc | -6.84476 | -41.55068 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| be3237b6-7429-31ee-a2bc-6d859b354552 | -6.09428 | -47.05818 | 2025-10-24 04:38:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37a00624-98d3-33ef-8325-5cf70ec9c8d5 | -3.40768 | -46.89885 | 2025-10-24 04:38:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cae0d6b-22db-325f-8000-27f9c30d9dae | -6.08291 | -49.37962 | 2025-10-24 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a9b882f-ef01-3e5c-8bdb-ea759dbe44f9 | -3.69517 | -49.56638 | 2025-10-24 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 544f9d6f-d3fa-34d0-b22c-9124322e0712 | -4.92053 | -55.86282 | 2025-10-24 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a773221-5614-31b4-8ff3-55d1e245f2bb | -5.25468 | -50.8109 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d406bc5f-e96b-3d85-bf5d-038b90dbc9fe | -4.85936 | -46.7325 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 538d7c7e-c591-3ea7-a942-0506a44ca872 | -4.24226 | -48.55593 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70f71b72-858b-3713-be32-07139695d92c | -4.73998 | -50.93797 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa00532d-a827-381b-9ef4-1bb013991a18 | -9.9783 | -47.06607 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cbcfdac-9cb0-3a22-affe-5e9be5b5f5cc | -10.95831 | -45.07794 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8243a34d-9d80-36b4-8b75-3afbacebeb2a | -9.57854 | -46.88784 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54bccdf6-743d-3a30-8a0d-b3f4b2f8cfb5 | -7.97572 | -47.23646 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b923a3b-20d6-3787-a194-5f3c50875ede | -9.6417 | -46.8842 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| db85778d-02f0-3c89-84d8-f902b7822e0e | -2.85662 | -50.7445 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d238b1ea-2154-3933-b873-a70de9f758db | -9.32272 | -48.48159 | 2025-10-24 04:38:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94c0a60e-86fa-3e64-a5cb-a3daccd518b1 | -10.01355 | -47.07558 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 53405812-837c-3839-809c-9c10d7d51c1f | -6.66603 | -47.71356 | 2025-10-24 04:38:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f789d09-07f7-3584-ba2d-3ce70572eb1e | -2.87869 | -50.71693 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf6f3be-ad7d-3575-bf29-e2da8db8b27c | -10.01049 | -47.09627 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4acdeb46-5999-3d8c-9ed5-aef2f40cd87d | -2.86487 | -50.71474 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 181880b1-b8c3-3df5-8a27-ba45581c7c6f | -7.29562 | -46.95824 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3030db65-1f51-3ce0-860a-ea61a1b6ad79 | -3.79988 | -51.75331 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b4f469b-7ac8-3dac-ac94-286100be94c9 | -7.00587 | -45.21042 | 2025-10-24 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 30492017-a73b-32f7-bffe-3a61f91092c7 | -2.92622 | -48.30355 | 2025-10-24 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3e4b040-bb0a-3da4-a65a-432bf891c125 | -3.86925 | -48.33504 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c494869-892d-3c72-ba9e-84920732d623 | -7.48853 | -42.57414 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88ae165f-c6a7-3710-9b12-0c6c570cdf9f | -7.29797 | -46.94261 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa8a8ad6-617d-3722-87d9-0944ddebc6ee | -8.6668 | -44.78079 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5125e01-7b8a-3f50-945f-29f26cb4eac8 | -10.17736 | -49.67529 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0be715c2-85d6-35ce-800c-73c41acc0ec6 | -7.49403 | -49.50171 | 2025-10-24 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd9cd478-f491-3aa5-8cca-4e442d7af68f | -4.15689 | -46.78967 | 2025-10-24 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2164aeb4-ddd8-3591-9e3c-d978f6d0d811 | -5.40779 | -46.41274 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| eea31ed6-eb9b-36e8-a2bc-ee60f8e49469 | -4.20191 | -48.35894 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c9a499a-863a-3479-b1c4-d3ef7775d1ae | -3.1325 | -50.61687 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d3232c-e616-34ce-bdd0-ebee95d5c528 | -6.01176 | -45.87238 | 2025-10-24 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d97bfcde-7211-33cd-b036-b89fcb051480 | -5.58528 | -49.08892 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e93f5cc6-ead1-3857-8b50-1cb76ba2aea0 | -3.03037 | -49.4938 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e21a3bc0-463b-3c08-b437-e4bf3268b517 | -8.56806 | -48.51386 | 2025-10-24 04:38:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc56d11e-fae9-3c0e-9a3c-71e62e4cd492 | -7.6399 | -42.17312 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 342afe70-5df6-3f4b-abcf-f08ab73546ca | -3.82712 | -47.47456 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f1b2ed0f-3876-3008-b530-08d8140e4e1f | -4.84901 | -46.73077 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34980eed-1ddc-3c82-800e-b3cc9d6141e5 | -4.695 | -47.90123 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3db1a4ac-bd6e-399a-aad1-0958ebc74bd6 | -7.62181 | -41.85178 | 2025-10-24 04:38:00 | NOAA-20 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e96bc875-235f-3296-ac10-16fee409c629 | -7.77837 | -45.39896 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7e3c521-e406-384b-ae4b-20e9402b399c | -3.1478 | -50.16796 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b5f2d10-30b6-3520-88bf-a646d874f7ec | -3.51208 | -53.03086 | 2025-10-24 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73578f6c-16d4-325e-bfc9-64216a0f1aa6 | -9.28484 | -47.85508 | 2025-10-24 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6fd991-68e3-3e11-9e60-4e7f278de52a | -9.26429 | -45.34537 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3178b3f6-1e45-338c-b64b-fef97f50ef32 | -9.78237 | -43.8558 | 2025-10-24 04:38:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d8a8c87-7442-3b14-b57e-99d793b99bf9 | -8.31909 | -46.78602 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 593e1895-a2e0-3705-a5a4-a35423c5207a | -8.65157 | -44.80051 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7f2a38c-1ab3-35d9-b95d-aa7fdf63bb18 | -6.77744 | -45.47596 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ea259a7-23e6-3b61-b28d-5d10baa5fac0 | -7.55248 | -47.36583 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2b88b0cd-d628-3adc-8269-274be318a692 | -3.80212 | -51.76213 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92007839-6de1-3f4d-8f70-5366e90a2883 | -5.97732 | -48.92823 | 2025-10-24 04:38:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62b6f40f-e1f5-32b3-9413-e87100f28f41 | -3.48172 | -50.07613 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84cfce4f-f563-3afe-8b26-e15a956a26aa | -4.00117 | -43.28225 | 2025-10-24 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f18dab3-5029-3a41-bab4-c8351ee1bcc2 | -10.61534 | -45.18444 | 2025-10-24 04:38:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7964847b-4eea-3583-afd9-11eec926f5d2 | -6.79929 | -45.43265 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50efc1e7-ba5c-3b69-ba1e-9b621c27aa9a | -10.61383 | -42.30331 | 2025-10-24 04:38:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2bc2c7fe-3e41-3416-bb6f-a38eec0d01cf | -6.83912 | -41.55527 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 94df9d99-6f84-3231-8df4-a3c62e3a06d9 | -3.21532 | -46.80595 | 2025-10-24 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98168875-e01c-3746-a944-d3d977e442af | -9.19114 | -44.54324 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9c595a8-d7b9-31b8-be90-4cf7482b1239 | -6.78257 | -45.4673 | 2025-10-24 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b487f5f-f96b-3006-813a-bef0e1bdd510 | -7.48783 | -42.57897 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3db00127-8bba-3c55-9ddc-8aeed0fc419c | -10.37895 | -47.53345 | 2025-10-24 04:38:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfdd78b9-1c4c-34de-9773-f5cf90bc9ebe | -3.60014 | -48.98711 | 2025-10-24 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 668ce5da-a6b8-34c9-85ae-04330658198d | -3.23821 | -48.76085 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5f685cab-56ce-377c-a235-4f77121562cf | -9.64468 | -46.8889 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f7408e7-1212-3ae2-8a10-7a7345429f97 | -4.818 | -48.67495 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce189eb3-6baa-3b0d-bd38-91871c98a6a8 | -6.94618 | -44.02166 | 2025-10-24 04:38:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f90513ff-3166-39a6-b7ae-8db93d9155dd | -9.60747 | -46.86653 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d9842ee-7d47-3538-a9ab-f67cfe6ee9c1 | -7.18533 | -43.86724 | 2025-10-24 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c3550ce-d6b9-3eb4-879f-10ae98c0e9c5 | -8.33944 | -46.19904 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d99577ff-5520-3210-9b90-c7d989d06778 | -9.85843 | -48.27114 | 2025-10-24 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cee2ba6c-e4fb-3802-a0a9-e97299eb9b86 | -10.46568 | -49.10815 | 2025-10-24 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83f43326-c7f9-37d9-9974-2406fe21ef8f | -9.25932 | -46.46788 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 242a2a26-cd3b-368f-b8c6-272ab6d30316 | -6.88974 | -43.61881 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea306c12-d113-34d8-9a9d-16f3b99b8571 | -7.33851 | -49.04357 | 2025-10-24 04:38:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59155470-8010-37c4-963d-bbd665ccabb2 | -4.83431 | -45.35554 | 2025-10-24 04:38:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1bf064f3-023b-3374-8b2e-be07f7c287db | -6.60008 | -48.0064 | 2025-10-24 04:38:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4370e9f9-5c4f-39b2-80f4-eb30ec215c9c | -4.64376 | -42.51612 | 2025-10-24 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 74daf4a0-9884-3582-a915-87663f6eda76 | -3.14499 | -50.16381 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
