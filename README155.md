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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52a90569-833e-30ce-a109-03a1ac5424bc | -11.12069 | -45.95277 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 44dd2610-e50f-3ab3-9fe4-ecdfcb2b791b | -11.63207 | -43.60351 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3fff7929-fc4f-37b9-a79b-fd7354bfacaa | -11.51486 | -41.70242 | 2026-10-07 16:01:00 | NOAA-21 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 7d8736eb-371d-30ab-90a0-c8fe01505832 | -10.49634 | -47.29281 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0a01d58f-aaab-3e05-aac4-6384860748bc | -9.86107 | -46.3085 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 08a44c7d-c28c-3e56-93d0-7268ae5003e8 | -8.74196 | -47.87728 | 2026-10-07 16:01:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 498d9276-abe4-359d-b8f2-f261af731f08 | -11.05607 | -45.86649 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e3e09f92-7105-3f9e-b221-50efc1af34c7 | -10.78443 | -46.55188 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 129d0d95-a710-36df-8f6c-a9a503a074d6 | -10.99344 | -45.42216 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5a82d260-4274-3593-a02a-2624494ec4ea | -13.38968 | -43.87242 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| dfa0cce5-4cf6-3c74-9820-26dadc2f3f77 | -12.21764 | -44.70869 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 3cd23754-014f-3236-b0c5-69475701bc21 | -12.98866 | -47.06779 | 2026-10-07 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 21c6412b-2506-3bc3-9eae-c007f991bf31 | -10.38103 | -46.23476 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 17b53c80-5532-3470-bc43-bd9c07556926 | -7.26742 | -35.80865 | 2026-10-07 16:01:00 | NOAA-21 | CAMPINA GRANDE | PARAÍBA | Brasil | 2504009 | 25 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 602930c1-0e36-343f-b08d-2d81bbba7df7 | -11.83506 | -47.35088 | 2026-10-07 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3ebaf6b7-6f17-305b-9acd-4a3ce7f19189 | -9.77737 | -45.91444 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6e8bc249-6de6-36c3-bfd9-8963ea4a6cb5 | -9.39557 | -45.81258 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 06ed8bc8-6810-3151-8738-06e23756a128 | -9.3799 | -45.93174 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 145099d2-eb00-3959-be9a-aba2136980bd | -11.00017 | -45.47403 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7dd16abd-0bad-3108-bee9-5070f45db1ab | -10.99589 | -45.48079 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 26d0d69c-1b7d-3508-89c9-94fd6a536611 | -11.76219 | -47.73684 | 2026-10-07 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| fff84846-5474-303e-8d61-a1e33bbb5bb5 | -10.63387 | -47.3371 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 59678334-51ab-3779-80ed-76ca47666a9e | -10.61457 | -47.56968 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| a4bd6987-6cfa-307d-aeaf-d73263b1a37b | -10.98147 | -45.40899 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| da273f78-9d67-370b-a3d0-c388759afb08 | -13.68376 | -49.09618 | 2026-10-07 16:01:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| c3563771-1bb6-3bf8-b1f9-0a98aab857c3 | -10.46117 | -46.83974 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 6e64a636-e896-31a3-b2d9-b4ed2b603a00 | -12.17706 | -44.74162 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 743ffe25-f9dd-3ea0-8e7a-eec25493c0a4 | -11.73805 | -43.6609 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c6539d31-b75a-3f86-bcc6-5a887f377627 | -11.64167 | -43.67523 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| af561f67-19b5-3615-9b3c-b8e583109ed9 | -11.36682 | -46.71938 | 2026-10-07 16:01:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3dac449f-1ab6-3c2f-97f5-df4b26b69a8f | -10.35994 | -48.23803 | 2026-10-07 16:01:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b9dcd959-9800-330f-86f7-448fc32782e2 | -13.69038 | -49.09546 | 2026-10-07 16:01:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 54f01570-2a74-39d7-88a3-c63725117350 | -11.22698 | -45.25563 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 16307682-57e8-356f-9d9b-d326fc8b2d14 | -10.94781 | -45.38621 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8169b11b-4a06-361c-83b9-cb4aab8b729a | -12.30879 | -40.78456 | 2026-10-07 16:01:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5b531a04-32f4-3f63-b0c7-5f894db6bd21 | -9.97433 | -37.97123 | 2026-10-07 16:01:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7226f09f-5d13-3ca6-b2c4-e33be9e8c64d | -8.95134 | -45.10746 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2dbb4519-b225-3fd8-8de8-fa47bd0e1442 | -8.8346 | -45.81638 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a9f97159-9015-3ddf-adcd-263a5537f121 | -10.95286 | -45.38566 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8a48ae8a-96a7-32e8-ab92-0a36663362f3 | -11.80265 | -46.7029 | 2026-10-07 16:01:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ae12c75f-b9ba-3b14-9046-ba8045d5afdc | -10.46027 | -46.83583 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 84a0b26f-69a9-31d1-9733-4885ee88757b | -8.79526 | -47.21467 | 2026-10-07 16:01:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f899407-a6ff-36c0-8f87-6af0b85c11b7 | -9.80622 | -44.77934 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| cec1a0a2-1c2b-3a99-98e6-7d41ee00537e | -12.26427 | -44.4318 | 2026-10-07 16:01:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 29768151-d4be-3948-8524-26abd5078867 | -10.78205 | -46.57714 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 07f56883-ab2f-3fd2-bec8-207f6b4b6215 | -10.80092 | -46.55127 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 56f06840-c670-3cbe-89b6-df6d9e6e74e8 | -11.8022 | -46.69922 | 2026-10-07 16:01:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9d966c42-56b1-333f-b0df-62140e77f357 | -11.7323 | -43.65229 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| af1fa091-fea7-3246-9f64-7d45bf5619b1 | -10.64672 | -46.70403 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e4b6c93e-5d9b-3cfe-b385-fe0c5ed63ac5 | -11.08465 | -45.66425 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.5 |
| bbf635e4-7e8a-347f-8ec6-3d8562ebb17e | -13.93914 | -46.48769 | 2026-10-07 16:01:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 725ce352-0d5e-3355-9361-5f0a4c52b927 | -11.0935 | -47.62296 | 2026-10-07 16:01:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 57364c76-ad53-3480-8472-33bf255d7c94 | -11.78857 | -43.54034 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| cb58dc4b-8f9e-3e2e-bf7d-799b083bf171 | -9.81641 | -44.78322 | 2026-10-07 16:01:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fd766cef-3152-3023-b0c1-3bbf39e74d3c | -12.22703 | -44.72331 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 199.3 |
| b78a4860-265a-3bab-9da9-b0f88c06d032 | -9.14093 | -45.10057 | 2026-10-07 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 28.4 |
| a6f4b2cd-b9eb-3707-bd5d-7dda37b76c9c | -11.71027 | -43.65973 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 23067b49-b2b1-3ef1-bc10-31faa8ae77ff | -11.23126 | -45.29001 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 316d5fa1-b572-3ab5-9477-4be1afcaa1c9 | -10.79458 | -46.54471 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| d5982e50-96ee-30b8-9757-d6b13ebb88e7 | -12.21116 | -44.65899 | 2026-10-07 16:01:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 6e9c3032-9a82-3004-a377-af76ce5bab58 | -11.27827 | -45.21867 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 4588c042-fa8a-3545-a86e-1b3051ab1412 | -13.69206 | -49.09578 | 2026-10-07 16:01:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 05ed5ece-9e40-3bf2-95f0-bf027e71ba5a | -12.21723 | -44.72458 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 25.6 |
| b1e7fb5d-19d3-3adf-890c-7918b497c6af | -12.16389 | -41.65128 | 2026-10-07 16:01:00 | NOAA-21 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0d2f93fe-bfdc-380b-81d1-23ffadd99c01 | -10.99921 | -45.42704 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d3188129-0c90-39d2-9f02-d617d7dd62b6 | -11.83734 | -43.52906 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 7ef6af4b-9c05-3449-9521-25d446afd8ca | -12.19788 | -48.42834 | 2026-10-07 16:01:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 8c9dd0f5-f566-3041-a71f-88835ea8f50d | -11.6384 | -43.68515 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 210.4 |
| 99689f7f-19ab-38fe-90c5-fab7a4512ee8 | -9.14808 | -45.82714 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 636da703-1a7c-35a0-9ae0-81edf9a910d8 | -13.8919 | -49.11913 | 2026-10-07 16:01:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| efa4aff5-8ced-3f8b-ba23-100cbbb3d0b1 | -8.95154 | -45.10913 | 2026-10-07 16:01:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| c0644f6d-5156-3c0e-97d0-023fea8eccbe | -10.87959 | -47.60846 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 37bb5619-e425-3e1b-ad10-c5c0f6ee6f88 | -10.98731 | -45.49426 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad726b61-d33b-3fd9-b29b-d60dd2524602 | -9.3773 | -50.65607 | 2026-10-07 16:01:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 6b9e215f-f771-300b-9479-eebe32539133 | -11.3919 | -47.54626 | 2026-10-07 16:01:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eced6e11-0c28-3240-9cb6-f1a4f938498f | -9.39974 | -45.88428 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cdead665-d93b-3640-980b-a4984548e1f0 | -13.57321 | -42.43396 | 2026-10-07 16:01:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 42.3 |
| 800b2197-b8ad-38cb-9b7b-d0abbc1a5a02 | -9.25585 | -45.64126 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dba40e1c-84a1-3bac-a106-7ede3f406d66 | -10.3565 | -46.24915 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5d2c75de-d7e2-3e0b-be08-f8187f09ed5c | -11.04433 | -45.81633 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e4caf8c-b30d-351a-8a45-00ed1577b699 | -13.10786 | -49.00052 | 2026-10-07 16:01:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 431786d5-d774-3f43-8349-851884d44183 | -9.77777 | -45.91743 | 2026-10-07 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d28fec52-3cd4-39b5-b1bc-2a88724eda99 | -13.42241 | -40.83192 | 2026-10-07 16:01:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 592116ff-6a28-3925-a4e1-40ccd79acbbe | -13.3903 | -43.87751 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ee9a2ec4-e9e2-35c6-866a-b0ef71f7a9c7 | -12.21982 | -44.72545 | 2026-10-07 16:01:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 8e170903-b081-3311-8cc9-5e51591c9140 | -10.37784 | -46.25238 | 2026-10-07 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ef4f64ea-fb31-38f4-a2a8-dac389e71bf5 | -8.07423 | -38.23318 | 2026-10-07 16:01:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 30.2 |
| 377bfcb7-865d-3044-8d71-0dda5911f4bd | -10.47511 | -39.42932 | 2026-10-07 16:01:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 305d9fd2-4c54-30ea-9fda-d1485247d8f5 | -9.97139 | -43.57022 | 2026-10-07 16:01:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.0 |
| ccef5bef-cdc8-34c2-9325-71600a1d3e51 | -10.95324 | -45.38862 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2bd00a28-a7fe-3a68-bf08-65388c05d051 | -13.39725 | -43.87312 | 2026-10-07 16:01:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c580f279-cd39-3abf-be42-ad0f4c9107f3 | -11.23098 | -46.24365 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 35f09f11-44db-3170-8f38-70e96fc75faf | -10.60823 | -47.56604 | 2026-10-07 16:01:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 62b814ea-59ae-3392-b365-5df2bfc72749 | -11.35669 | -39.99863 | 2026-10-07 16:01:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| a99a1269-c73b-337a-85ef-80faeb0249ae | -13.68545 | -49.09654 | 2026-10-07 16:01:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 0b0e55ed-e033-3dfd-b0e5-3a0256e17c38 | -8.3084 | -44.1498 | 2026-10-07 16:01:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c6bc1a19-cd46-3ab2-959c-3889d7c76bfa | -8.59654 | -45.67478 | 2026-10-07 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8ccd59d6-f75e-3594-a5bb-b3509a338c68 | -9.45618 | -44.60886 | 2026-10-07 16:01:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 564e8618-fc6d-34dd-a836-3ad6f39c580c | -11.62191 | -43.66495 | 2026-10-07 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 2def525d-f077-3777-942e-1e485034368a | -11.22409 | -45.27333 | 2026-10-07 16:01:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |


[Clique aqui para ver as próximas entradas](README156.md)
