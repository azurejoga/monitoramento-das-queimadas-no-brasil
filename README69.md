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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f732c7b-f9d9-340c-94cc-619b92257481 | -3.6638 | -54.26613 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3d49b03c-216f-3fa7-a84a-0fb37676fc22 | -3.66317 | -54.27007 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81f43a91-13ec-31d2-9075-d70e7173981e | -3.66255 | -54.27398 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ba8c61-eeb2-35ed-add1-c35283babfe3 | -3.65097 | -54.79761 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7e774e87-d63c-392a-9fb5-d82d530c0b15 | -3.64734 | -54.79253 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 507ec51b-9498-396f-a836-c6b04ffb4227 | -3.64665 | -54.79674 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a7542d9-a808-3537-955f-17b12efd985e | -3.63892 | -54.68175 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a10904a0-692b-3413-9ece-6d125ab1ad27 | -3.63826 | -54.68576 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ee15277-6b51-3335-a03f-4ac1612139d0 | -3.6346 | -54.68111 | 2024-10-25 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0534ce8b-19da-36c7-b27e-e83415d98d5f | -4.42335 | -55.43064 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 423be407-30d3-3c2f-99c5-a6514162cf4b | -4.42263 | -55.43507 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0eae870-6b90-35d0-8236-9c2b836483c5 | -4.39349 | -55.09252 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7dea90-0698-3a68-828c-4bc6344c418d | -4.38814 | -55.04143 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd213e3a-0b34-369c-87a1-fdce42b36a91 | -4.29541 | -55.08836 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d71d1df1-4195-3f50-9a6e-57ddf48117a4 | -4.29538 | -55.08625 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 022e3518-72ec-37a2-9011-f97530c1e718 | -4.29465 | -55.0906 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57c1b72f-7c30-3e95-998b-719ea0adf6e0 | -4.28677 | -54.97593 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 042cef0e-8d4c-31ad-bf10-2aa98bb112ba | -4.28312 | -54.97092 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8ac05f7b-98a1-3e65-9d6e-483202c71622 | -4.28243 | -54.97514 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1f6f00fe-f71f-3b63-b498-3ca265fb78cb | -4.19635 | -54.98184 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7edd6ae2-fa7e-328c-802d-19167a4be1ab | -4.19543 | -54.98325 | 2024-10-25 04:38:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb6124ca-01be-3512-beb0-72d61aa3f1c1 | -8.36224 | -55.13979 | 2024-10-25 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00be9305-57fb-3b36-b7ff-34ee4e7cb1d5 | -2.13346 | -55.85548 | 2024-10-25 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c7587df-d03f-3aee-a5cd-613e9b0c0df5 | -1.97679 | -56.42801 | 2024-10-25 04:38:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| febe8f32-fdfb-305f-b472-2b1e1d658ab2 | -1.96906 | -56.44402 | 2024-10-25 04:38:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d4a4af78-961a-399e-9be4-9d2a2c16c2be | -1.96407 | -56.4432 | 2024-10-25 04:38:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9be0353e-5e6a-3e5b-b071-90e2e0861a6c | -1.96315 | -56.44881 | 2024-10-25 04:38:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58f92ed8-fb20-3ec1-8188-5a0528a45c3f | -1.77251 | -55.08776 | 2024-10-25 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cd1c234-454a-3aac-9a62-7c3c60310e13 | -1.70939 | -55.04441 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b907c1c0-06e3-364c-bbab-2616aa29889b | -1.70919 | -55.04605 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 165d58f8-5978-3da9-bd43-ec580f65ef32 | -1.68256 | -55.30634 | 2024-10-25 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb1190c9-b699-3152-93b2-fa387aa39959 | -1.62437 | -55.1657 | 2024-10-25 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 31c44650-d031-3e13-b196-6a39be28dbea | -1.61902 | -55.16961 | 2024-10-25 04:38:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38b63ee0-77a4-398e-b4d9-1c32880332a2 | -1.53005 | -55.40882 | 2024-10-25 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0375d339-a49d-31e0-8276-bd9e0a321c06 | -1.52536 | -55.40812 | 2024-10-25 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b7651f-6af8-302b-bba9-c8d902026b40 | -1.48642 | -55.12487 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 952fa9f4-d25a-39a6-acb2-b991736b4994 | -1.48591 | -55.12173 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e383d05-21fb-3674-8fb3-709aa0348cfa | -1.48514 | -55.1264 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5446cbb-9b82-36fe-90ba-5f4a4162858a | -1.45725 | -54.95395 | 2024-10-25 04:38:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 179928fa-95d9-3546-8e07-1be1a30174e4 | -1.285 | -55.72001 | 2024-10-25 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9ec3430d-641d-3436-981c-348bd375d0bf | -3.68796 | -55.46154 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2a91aa-3dc7-3d28-9103-4ee52b9c4012 | -3.6733 | -55.46108 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69e4a472-b392-3816-b704-885671fcb24f | -3.66875 | -55.46038 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 079f83b6-a651-30f2-8985-11c8a847605a | -3.62412 | -55.50462 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b599f093-1e84-3b11-a4bc-fa4c4c267ead | -3.50316 | -55.47256 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29f4e3c3-c163-3f6b-8bb9-82bfabcb8fd6 | -3.49864 | -55.47162 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed4fedba-813b-32dc-b128-898d0aff04f9 | -3.49786 | -55.4763 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01ff0c23-4611-322f-a727-f085a4eebaa3 | -4.9968 | -56.06219 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca819474-7c79-3e2c-b36e-7e357ec8c889 | -4.3545 | -56.05333 | 2024-10-25 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83207135-26fb-3407-aad6-e479e7ebc12d | -4.35185 | -56.05066 | 2024-10-25 04:38:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a9d65a05-c1e9-3a3c-93d3-f9cea3ab17b7 | -3.99054 | -55.44184 | 2024-10-25 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 056b94e2-9acb-3697-8acc-e55bf8b502b8 | -4.99823 | -56.06561 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba42cc15-2575-3f22-bbdb-7e35f585f403 | -5.24834 | -55.96357 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 56fd3234-086b-3107-9202-2930709f899e | -5.24754 | -55.96828 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2398862a-be15-3d80-b927-aae24a153019 | -5.24376 | -55.96278 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dfa1853d-f715-3538-95f9-bf80560adf11 | -5.24296 | -55.96748 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93ee396a-9bba-384b-be4d-2aabfd41e031 | -5.23838 | -55.96668 | 2024-10-25 04:38:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc2e5ed5-d72e-3c08-80ee-2696bb602f63 | -7.25755 | -57.63137 | 2024-10-25 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19acb60b-de21-3bf2-b237-6fe4c5188eec | -1.9892 | -56.91592 | 2024-10-25 04:38:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79780383-f867-302e-b06d-84302bd13048 | -1.98873 | -56.91878 | 2024-10-25 04:38:00 | NPP-375D | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25da7001-2ce8-32ce-a425-f2afef53c6d4 | -6.16395 | -57.79195 | 2024-10-25 04:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd844c76-e7a1-3843-9129-16464ee73de7 | -6.54443 | -58.47221 | 2024-10-25 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68c9da7f-2159-3a95-941b-d847ff356130 | -6.54384 | -58.47556 | 2024-10-25 04:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b372247e-87d9-36ba-923b-74fd87985e77 | -6.76261 | -59.11849 | 2024-10-25 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 359bbe28-b048-3d00-8d25-edbb05842214 | -6.76196 | -59.12212 | 2024-10-25 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3081ff80-3ef0-36c6-81a4-bbfda1506551 | -6.75711 | -59.11737 | 2024-10-25 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b51aa4d1-8437-3c9c-a3e6-b6b6c1d81b11 | -6.75645 | -59.12102 | 2024-10-25 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b9455d0-6a55-3195-aa5c-3df7c47c8b1a | -6.75159 | -59.11633 | 2024-10-25 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 954a3c3c-87e0-3770-9988-382d65e26280 | -6.75093 | -59.12001 | 2024-10-25 04:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f621404e-ee7c-30c4-a33b-b73449057e32 | -6.53176 | -60.03965 | 2024-10-25 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3379596c-fe59-36b7-99f5-a329155a6eb7 | -6.52659 | -60.03462 | 2024-10-25 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 089ad1c2-30c7-37bf-b196-f1cbdc4bfa42 | -6.52584 | -60.03878 | 2024-10-25 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9d862baa-3151-3e1d-bd26-92f650f9f385 | -6.52068 | -60.03368 | 2024-10-25 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2ac245c7-7ea4-3c8b-a94b-97ced986d5f7 | -6.51992 | -60.03791 | 2024-10-25 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6eb2d1b3-19f8-3c8a-a70b-f87da5d2ecc2 | -6.51918 | -60.04209 | 2024-10-25 04:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4812537c-de04-3104-90d1-5f1d32b3a9aa | -4.51771 | -61.1384 | 2024-10-25 04:38:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3dfe627c-27d1-304c-9b8d-cc6a6a61226b | -4.51676 | -61.14383 | 2024-10-25 04:38:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6026d170-3aae-36d9-ad93-753d2684cd90 | -2.4381 | -48.62371 | 2024-10-25 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73b64af9-e28f-3a46-9c75-24e42abecb62 | -15.31787 | -41.74524 | 2024-10-25 04:40:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f70f1f5-a2fe-32ac-a988-616547da6ea5 | -15.31767 | -41.74799 | 2024-10-25 04:40:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0b4c39da-d3dd-3066-92b1-da0cbc8b3960 | -15.31741 | -41.74914 | 2024-10-25 04:40:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 08185e71-a69c-3fff-b7f0-fdcf8d81fb13 | -13.5699 | -43.43097 | 2024-10-25 04:40:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bb3535d-ddee-3b55-bde7-45d13e3436f1 | -13.75301 | -43.59465 | 2024-10-25 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0947cdf8-5c3b-31ba-81e1-83c10e2e3980 | -13.74828 | -43.59402 | 2024-10-25 04:40:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9aa4cc63-3a6f-3f97-93ea-e3b42c9631c0 | -15.26123 | -43.62972 | 2024-10-25 04:40:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 0bb11f29-2c56-3ab9-8a59-b4b99723bb3f | -15.25642 | -43.62907 | 2024-10-25 04:40:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 058b40bc-e1e1-36bf-b090-71586a159471 | -16.68239 | -43.88556 | 2024-10-25 04:40:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b41faa48-5127-3bc2-b898-893fcf67746c | -12.30866 | -43.56734 | 2024-10-25 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45a0c010-1a4e-3785-b70a-cab5749ef686 | -12.30402 | -43.56672 | 2024-10-25 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ac7fffc-be83-3005-9745-719b2ced996e | -12.29937 | -43.56613 | 2024-10-25 04:40:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa2ff2fd-2bc3-3125-8427-669d9ec35698 | -11.90988 | -44.17223 | 2024-10-25 04:40:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a3a687e-4d47-3310-84ea-5efde2ae4e36 | -11.90485 | -43.8376 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1117bfe5-78ae-30f5-99fa-806755293339 | -11.90093 | -43.83236 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3b6a5c0-8c7b-373a-ab0b-9f3d51d8088a | -11.90032 | -43.83696 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdb23ce7-cd1c-3184-aa11-870f33813fba | -11.48317 | -43.23792 | 2024-10-25 04:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6b85089-f0b2-38f4-9a67-20abcc0ac6af | -11.4825 | -43.2429 | 2024-10-25 04:40:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 73eb0cd7-ae6d-3059-bf8d-d64e9acd112e | -11.78566 | -43.7579 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4db49a4b-9b15-3cae-8e4f-1800c0869d03 | -11.78504 | -43.76257 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a128859-e32f-3182-ac72-82d26069265b | -11.7805 | -43.7619 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6be38721-af68-37a4-af17-2fdeb9ce89b0 | -11.71714 | -43.91466 | 2024-10-25 04:40:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README70.md)
