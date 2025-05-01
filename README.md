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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51beddd0-09e5-38b5-89ec-ea34d4fb60cd | -23.60774 | -49.0111 | 2025-05-01 00:28:00 | TERRA_M-M | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 41.1 |
| c8b99c5e-e260-3a84-a966-4af3a7806ee9 | -6.96605 | -42.7854 | 2025-05-01 00:33:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| f6e234af-549b-36ce-967c-5dee12eeae22 | -10.67481 | -44.41443 | 2025-05-01 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 718fd92a-dc26-36b0-be24-3d7ffe3c7e84 | -10.67353 | -44.40541 | 2025-05-01 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 2b14724a-5841-3e3e-8681-44b4b37538b2 | -6.95782 | -42.79816 | 2025-05-01 00:33:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 43.2 |
| c4613bec-89bd-38e4-a94c-fd8987d46b60 | -6.63104 | -48.01946 | 2025-05-01 00:33:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0814d716-a3f9-3fd3-a773-458af24ec1ef | -9.61929 | -37.03783 | 2025-05-01 00:33:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 41.9 |
| 5bceff7b-d655-3dd1-9599-c79c88d5db19 | -6.9677 | -42.79672 | 2025-05-01 00:33:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 5033950f-adac-3ea6-bbe9-d1e57ca561d6 | -8.86224 | -49.89563 | 2025-05-01 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| c853cd65-36d0-3317-be29-386b6bb17c64 | -7.9983 | -44.38852 | 2025-05-01 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| fb842927-b1de-359e-bd10-b04147c9012b | -7.99698 | -44.37926 | 2025-05-01 00:33:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 21a820dc-6a9f-3d4f-b4c7-3af314a45698 | -6.95617 | -42.78689 | 2025-05-01 00:33:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 17a83503-a88f-3ebe-9965-5f162e22b312 | -7.07588 | -44.38445 | 2025-05-01 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b295bbf4-f260-3944-b17f-a65e4ee0188f | -10.67225 | -44.39637 | 2025-05-01 00:33:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf198477-8d60-31ed-b0fa-631c5e741563 | -8.86044 | -49.8817 | 2025-05-01 00:33:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 834e397b-6633-3d52-bb38-623f844948e1 | -6.19962 | -48.04273 | 2025-05-01 00:33:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 00622b1e-3af0-3f1e-8625-a59346345428 | -12.03853 | -37.97311 | 2025-05-01 00:33:00 | TERRA_M-M | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.7 |
| ef7a38ac-4c99-3269-8198-0171b5c4e78a | -7.08495 | -44.38308 | 2025-05-01 00:33:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0acd5c1-052e-33da-89e0-f0c563bd4762 | -9.61938 | -37.04448 | 2025-05-01 00:33:00 | TERRA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 9f42ea64-93c5-3b18-9505-00919035f96a | -4.86172 | -47.40916 | 2025-05-01 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9c377ea0-e06b-358d-b9d0-1773d58de056 | -8.853 | -49.8843 | 2025-05-01 00:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| f7f6d9c3-6b27-3e9f-a947-8c9fd7b9f258 | -9.61594 | -37.02988 | 2025-05-01 02:56:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b338228a-7edc-309e-bb35-dca03e056c06 | -9.61382 | -37.04055 | 2025-05-01 02:56:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| efbbdd8c-411a-3c7b-8d63-5d5480ef1e1d | -9.60849 | -37.03377 | 2025-05-01 02:56:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c603f945-d9f5-3eb8-83fe-31f2d48769eb | -9.62218 | -37.02851 | 2025-05-01 02:56:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1fe2368e-83e9-3ad6-a721-1e357b295918 | -9.62232 | -37.03135 | 2025-05-01 02:56:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6712a19e-0b8a-3156-9792-b4a95e3698c0 | -9.62116 | -37.03386 | 2025-05-01 02:56:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 317cba19-ac52-3e9d-a5cf-5dce71df9e5e | -12.03303 | -37.96592 | 2025-05-01 02:58:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 907931d8-a4de-3882-ad8f-269894d0fd57 | -7.07055 | -44.38163 | 2025-05-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f65456c-1a8d-3e33-940a-7d477bfc507e | -6.6972 | -42.12323 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7952198a-2eba-38fe-a6d0-47439cbfdae6 | -6.95841 | -42.7905 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 60d5cb4b-4901-3ba4-924e-8fc0dc559992 | -5.78567 | -47.5209 | 2025-05-01 04:14:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3909e72-8e9f-3d63-8b1c-49aa7ac362ce | -4.8631 | -47.4102 | 2025-05-01 04:14:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b130da70-6def-3f55-8fff-764eac720fcf | -7.06941 | -44.38874 | 2025-05-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9cbd306-9904-3c8e-9a9a-f31b1dd43171 | -6.95677 | -42.80097 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7032587d-2d1e-3a66-9bf5-e017fe6141ab | -6.70056 | -42.12375 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3b4f5503-ca66-39e0-bbd5-8f02c4747c1b | -6.96174 | -42.79103 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| fc502814-b605-3016-89d0-dff01e385943 | -6.69329 | -42.12626 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e33425fd-2878-3dff-b5c9-4ddae33448ac | -6.48644 | -43.78894 | 2025-05-01 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1428ba0-1282-3d5c-b6e8-e02f769ef1b7 | -7.462 | -43.26214 | 2025-05-01 04:14:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed37c146-51d8-3e91-b5e2-9ceb016c1182 | -6.63253 | -48.01734 | 2025-05-01 04:14:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c4cf11e-31cf-30d2-b060-30384ee28dfb | -6.70392 | -42.12427 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 910ce781-d993-336c-ae1a-a9c2d7de9a87 | -7.08456 | -44.38028 | 2025-05-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12182743-e592-373a-9cb6-4ea4e65242ac | -7.08063 | -44.38327 | 2025-05-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60d09938-197f-3ee3-812c-81ddcd5eff85 | -6.19588 | -48.04245 | 2025-05-01 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa034d71-3e43-3715-85a2-0a91dced3d87 | -6.19647 | -48.03889 | 2025-05-01 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05f41b29-944b-32a6-bde0-44463ffd610d | -6.95787 | -42.79399 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0b011aa5-dbe1-3d07-b3d7-64234ce168b3 | -6.487 | -43.78543 | 2025-05-01 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e274b7f-38d9-38eb-9d77-373630813135 | -6.70001 | -42.12731 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 995f75ef-b11e-3d7a-8139-bbad0a0f4c2f | -7.07112 | -44.37809 | 2025-05-01 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd9ecc5d-40fb-3a22-a023-117f9148ba89 | -6.96562 | -42.78806 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 65a8c8d6-249f-3402-8d9e-ba3756f4eebc | -5.78656 | -47.51908 | 2025-05-01 04:14:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e037ada5-e90f-3092-9867-69387af2feb4 | -6.19184 | -48.04184 | 2025-05-01 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f574a86c-6db9-3742-b001-950df9d653fc | -6.62854 | -48.01666 | 2025-05-01 04:14:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c802cf1c-400e-35fc-8717-ea3f23548863 | -6.95399 | -42.79696 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 197dbd54-7473-3bef-b60a-3edc3224aece | -6.9512 | -42.79295 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4344fc04-8c0a-3942-8642-7692138afb81 | -6.20049 | -48.0396 | 2025-05-01 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfc36f83-bf4a-380f-90c4-45482ba22b7c | -6.70337 | -42.12783 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| df3a9b63-8524-34cc-a4a1-3059f78a5f03 | -6.62582 | -44.77675 | 2025-05-01 04:14:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ea70b1a-ad20-3619-af9e-b7dacb8f3134 | -6.96453 | -42.79504 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 88fdb7ed-77a9-32c0-b146-41360b95da90 | -6.96229 | -42.78753 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| dc91d2d5-fff6-351f-adc9-8e00fa255347 | -6.95732 | -42.79749 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| cff742a2-7231-3f6b-a861-23bc29b8289a | -6.96065 | -42.79801 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2ee8f6ba-e910-3e0e-801b-0193956bf7d2 | -6.96119 | -42.79452 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c6aebcf0-486d-38b0-917f-70bafcd5181e | -6.69665 | -42.12679 | 2025-05-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 7c6646bb-0de2-351d-aeb1-f11de686ff0b | -6.88477 | -43.96405 | 2025-05-01 04:14:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3f1afdf-bd03-3635-9b3f-f236e0408808 | -6.96507 | -42.79155 | 2025-05-01 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c8c55a4a-00f3-31f2-8598-3cb40065e908 | -6.55168 | -44.47886 | 2025-05-01 04:14:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59dbb2c8-7a2a-3120-8074-903b5b05f451 | -9.61857 | -37.04111 | 2025-05-01 04:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f95082b9-10aa-33df-b502-55cccaf2f838 | -19.45541 | -45.3068 | 2025-05-01 04:17:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97fd5af8-8a33-3773-99ef-4013bf22d271 | -20.9939 | -51.79337 | 2025-05-01 04:17:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e382921-370e-3d58-9a15-27cb96313d0c | -10.67144 | -44.40265 | 2025-05-01 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 609e7b7b-26bb-333d-becf-b503162d5a04 | -19.41606 | -44.34037 | 2025-05-01 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 856453e5-cd41-3533-9e06-9cd3350e52fd | -19.36083 | -53.21159 | 2025-05-01 04:17:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ab64ae8-aa9f-3de8-8fc5-0527ff74e10c | -19.77607 | -49.74517 | 2025-05-01 04:17:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bd92d29-845e-3ccc-ae20-7d4ac1926616 | -12.03554 | -37.96392 | 2025-05-01 04:17:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 3301fa43-cd5e-34bf-8a98-1a70ddfa5c9a | -8.41389 | -49.85272 | 2025-05-01 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fd9e091-4585-33d1-9a5f-6854edf7a295 | -17.91004 | -54.653 | 2025-05-01 04:17:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6e771d9-8a42-3055-9662-36a598e959df | -11.61636 | -37.89542 | 2025-05-01 04:17:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8ff56ef0-ac6c-3e60-b50d-24424d51993b | -19.9699 | -44.21751 | 2025-05-01 04:17:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e8432750-e841-3c57-9331-725bd76eb8bc | -15.07715 | -48.94488 | 2025-05-01 04:17:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab7976fe-13ec-3caa-ae44-41a11f01965f | -19.76878 | -49.74371 | 2025-05-01 04:17:00 | NPP-375D | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a297fe45-391c-321b-97f3-d18993467b23 | -11.40319 | -52.95578 | 2025-05-01 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b1d7527-7bf9-31f3-820a-8e847b23c32c | -9.74455 | -37.00342 | 2025-05-01 04:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 898df32d-3096-38b0-9829-ac13034b544c | -20.76337 | -46.76921 | 2025-05-01 04:17:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 683fe79d-4ce2-34d4-bddc-1d373debfa0c | -8.41373 | -49.85409 | 2025-05-01 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb9aa255-894b-3dc6-b450-ccaca949d500 | -19.43719 | -44.33979 | 2025-05-01 04:17:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e724b6a9-0619-3656-ba05-a1c7c27f9607 | -9.61985 | -37.03179 | 2025-05-01 04:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.4 |
| bcf5af42-d988-3364-9314-489d942062f0 | -18.67508 | -47.38179 | 2025-05-01 04:17:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4eb87433-bd75-3ae7-8d11-cb39e59f4fb3 | -9.6205 | -37.02711 | 2025-05-01 04:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9c7f3fc6-5382-3a61-8876-034c6d2b4b37 | -20.04329 | -51.53872 | 2025-05-01 04:17:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dc95e88-5997-3824-9494-de6b5648eec4 | -10.66756 | -44.40562 | 2025-05-01 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 33f46161-dcfb-3fdc-81f1-fbdd1a8c5d4c | -9.62507 | -37.02774 | 2025-05-01 04:17:00 | NPP-375D | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c9fe53ad-426f-3677-9270-1af2fb95a108 | -10.66812 | -44.40211 | 2025-05-01 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6f9c4b5c-68fb-343c-9aed-ac6f9d7b9549 | -18.95524 | -52.38316 | 2025-05-01 04:17:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bab9c85-f3dc-3bf3-9a07-8eeca7d6f7b1 | -21.17781 | -43.97947 | 2025-05-01 04:17:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0acca07d-9ca8-3738-8241-adff390d37ef | -10.25379 | -36.26295 | 2025-05-01 04:17:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 70076fc6-76ed-3f61-8021-ca272201459e | -10.67088 | -44.40617 | 2025-05-01 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 40429d68-689d-3bac-9c15-3ba02208c171 | -12.17393 | -37.79312 | 2025-05-01 04:17:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4033af50-2583-3ae0-81b8-0ed235fe3c40 | -9.60614 | -37.02997 | 2025-05-01 04:17:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
