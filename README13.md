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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9bbdd40-f036-305c-b992-62607b9c7233 | -8.00841 | -43.15823 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.4 |
| 5643b74e-dea8-35e8-b2c5-b4a9953ff517 | -2.58874 | -51.92004 | 2025-08-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f46b68a6-6d9f-32ce-9ab4-1a39d33d37db | -8.00884 | -43.18076 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7b72caf6-c079-387d-a2b8-d676a1fffe8f | -8.00276 | -43.17082 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| ffb21a34-1999-393b-b149-73f9e6820d88 | -6.96088 | -44.50631 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1438430-9bf3-329c-9f9c-3d2fb45fc714 | -3.37985 | -46.93027 | 2025-08-03 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a23008a-88ee-3cbc-8e0b-16e4c1496e36 | -8.01451 | -43.1681 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 83857d1c-e0f2-3e23-bf2b-0b2b2d3e3a4e | -8.00711 | -43.16699 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7690fa21-34fd-34a4-bd1b-701ad28d62e7 | -6.20616 | -46.34768 | 2025-08-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d39ce344-10e3-3adb-b134-5835219516e9 | -7.13733 | -44.38112 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17ad8002-427c-3be4-80d7-698ce1a1f13e | -2.66414 | -42.72251 | 2025-08-03 04:25:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0eabdb46-bf12-32a2-a86f-cad63c11253d | -7.4341 | -43.82695 | 2025-08-03 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 16864a78-8e09-3d72-89dd-d6c02a44b47c | -4.0256 | -48.06224 | 2025-08-03 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77fd668-18fc-382d-9d22-00d8e88da2c0 | -8.00318 | -43.19337 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 4e9082f5-0343-3d74-be00-d3423f9e8cce | -6.76639 | -44.03121 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1df994b-64ef-315c-afab-21c80ef53c3d | -7.12001 | -43.47709 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5a0f215a-814d-32dc-9170-4d0948e0f144 | -3.43488 | -48.95538 | 2025-08-03 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6255ac1b-61d2-3b58-821e-97c71ade28e9 | -7.12539 | -44.07196 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 596d9733-031d-32b7-98d4-12812a7af7b8 | -6.6841 | -44.36473 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec3aec98-f2c6-3ca8-8cef-cb9708a92a3e | -8.01408 | -43.14558 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 7ad57250-f1ea-3b8a-96eb-97f3ae4f9e06 | -7.57172 | -44.79929 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5777d93-8e0f-3953-80f2-295d9ad6c02b | -8.01211 | -43.15881 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 199.4 |
| 5130bb04-983f-3641-88c1-d208c4aae854 | -8.02083 | -43.15112 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2b9a7ff7-b33a-3562-ac7d-f3d865d79a10 | -6.52403 | -42.80351 | 2025-08-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3c5a9b70-1732-3fc3-9968-18b74e33ac46 | -8.02017 | -43.15552 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4dc2e720-5be9-38b1-b026-1149662d8453 | -7.56809 | -44.79923 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 327a3e5f-d177-365e-a91e-132cf94aeb84 | -8.04163 | -43.1135 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 09ebd0ee-0726-3f28-98d2-641b74eff81a | -6.96043 | -43.13652 | 2025-08-03 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac205dd1-d174-374c-8039-a83ed881321b | -7.12711 | -44.08415 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71bf1698-dcda-3d9b-b3e5-a83401c5d889 | -6.67891 | -44.35237 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 78206e78-674d-3cdb-8572-671d541531d7 | -4.77513 | -45.33971 | 2025-08-03 04:25:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b5005796-6bd4-3958-8e82-ae57d84b1684 | -7.30939 | -46.14212 | 2025-08-03 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb249806-d211-3e65-95df-c5c44438d5b4 | -6.35788 | -46.1592 | 2025-08-03 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 86c183f6-31af-36bb-b56d-781e213d30ef | -2.90702 | -48.29397 | 2025-08-03 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b351ede-dbc0-3038-bcd9-4a86c94d3bda | -6.68325 | -44.62476 | 2025-08-03 04:25:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0ec2d6c-2ac8-363d-8af3-910ba8f117cf | -8.00383 | -43.189 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 262747e6-b30a-3bcd-aeba-5839f50da0d7 | -7.6057 | -43.96197 | 2025-08-03 04:25:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f52e73b5-6a02-3347-9792-059eeb3ea770 | -7.11822 | -43.47828 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0f2576c5-3ea2-3a6d-a8d4-2eeae68b3c9e | -6.95026 | -44.22829 | 2025-08-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 289a0e6b-0536-35c5-a40c-0d41d235bf3b | -8.01516 | -43.16373 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| bea0de84-e6e9-37eb-993b-ecb5643e72d7 | -5.94964 | -50.08204 | 2025-08-03 04:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b432632-7a90-35c5-bcdf-bc4065b5b936 | -6.96094 | -43.15861 | 2025-08-03 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3b869807-6507-379d-b698-2554012ab3c0 | -6.94201 | -43.33801 | 2025-08-03 04:25:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f1cc3151-adbb-31c7-9e04-01b14eda30ff | -8.00645 | -43.17139 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 48fd27b7-6e78-334c-8a91-c75970dc1313 | -6.8611 | -44.28645 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a7781b53-6044-37df-b5ad-b54d40d776db | -8.00753 | -43.18955 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6aa1692f-8824-3313-b99e-510227d069cc | -3.43342 | -48.95606 | 2025-08-03 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 951d2929-0371-3323-af83-deadf81694cd | -7.53454 | -44.88126 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e5fb2cf-9783-3219-8c00-13b05ced26a6 | -8.02414 | -43.12899 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8a3d3108-12bd-3d8b-a52f-9b04464ecb1c | -6.8075 | -41.36405 | 2025-08-03 04:25:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af16b1dd-6853-334c-ba39-cd3f895e2bf9 | -7.68391 | -45.12164 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c05e2cb-7091-3f33-bc03-0aec17ce6e39 | -8.00536 | -43.15329 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.0 |
| c3055fc1-7447-367c-9eae-a0c574a445f1 | -8.00341 | -43.16642 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.1 |
| f08550d4-6b11-3c54-a4d5-b52614b287c7 | -6.56317 | -43.91494 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8af0e3f5-3652-3339-9f4c-557e50986c47 | -4.30752 | -48.10229 | 2025-08-03 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 11917599-746c-3a35-bacb-19cd92b6f8eb | -7.52377 | -44.88328 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| afefba48-2750-3760-8f93-c7674fe2893d | -8.02917 | -43.12068 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f8234786-4545-3b39-80b3-d59d09e7615d | -5.88981 | -46.52385 | 2025-08-03 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5129ee6e-78d2-3fbd-a18d-659ccbb11051 | -7.5641 | -44.80243 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 077350b5-dba3-3571-bbca-0af5ebaf36b2 | -7.53114 | -44.88071 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6040c021-5a2e-3a4c-a33e-cb84250f9892 | -3.58263 | -47.51619 | 2025-08-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa9b1e9d-51bc-383b-bb0b-1e071d486f1e | -3.51035 | -44.0244 | 2025-08-03 04:25:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab86f27a-c7cc-3b7c-948b-ef361c01d9b2 | -7.33396 | -44.67986 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96c9644c-29f8-3106-b29d-650d885aeb5b | -6.96053 | -44.50566 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d653d6d5-6ee0-335d-b7b7-6b957fbc4b72 | -4.06608 | -46.93681 | 2025-08-03 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f0b8b48-0315-3a16-8bf6-21ca68e62436 | -5.92039 | -50.0043 | 2025-08-03 04:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38947e99-5fee-3fff-9656-29df752abe74 | -8.01342 | -43.15 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| a6999c35-8274-379a-8a6b-4e55e9d3909f | -2.66121 | -42.71795 | 2025-08-03 04:25:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2f1582dd-8c96-3262-8c42-3217dfdf8be9 | -7.13529 | -44.07751 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c894392-7ff9-3eca-aa9b-c55f2e9ec9ef | -6.49988 | -42.81299 | 2025-08-03 04:25:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4a7d08dc-110a-3d11-ab1b-7f417a9aaa85 | -8.04027 | -43.11112 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 8eaa2a2b-ed7b-3d44-972f-1d1f07ccb181 | -7.12307 | -44.06366 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44305d9b-6c16-3563-a85f-0ac95910e93e | -8.02043 | -43.12843 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| deb320da-1775-30bb-b9b3-b503f2abc9ee | -6.53229 | -44.53416 | 2025-08-03 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2a8698f-14af-3956-98f8-513b6f220958 | -7.11399 | -43.48185 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b394f7bc-7c26-3595-8a87-a59ad78768d6 | -7.09755 | -44.36313 | 2025-08-03 04:25:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 722249ad-470f-39cb-a0ff-15ea165676c1 | -6.95779 | -44.22552 | 2025-08-03 04:25:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acf57089-356c-317e-a2de-50a30cc8073a | -6.75861 | -43.03386 | 2025-08-03 04:25:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6eb1113f-4f46-3188-ba42-afc7b5d52285 | -8.01385 | -43.17249 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| af5f7c0f-4e36-3694-ac59-36c9c1431941 | -7.41284 | -47.00348 | 2025-08-03 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6618e633-c6e4-3aa1-81a8-f3ccb2200b80 | -7.75669 | -45.10645 | 2025-08-03 04:25:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fd50cba-5359-302c-b893-a8c8f102d744 | -7.5683 | -44.79879 | 2025-08-03 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1b22b42-621f-387b-88c5-e292aa0f2b04 | -6.68523 | -44.35722 | 2025-08-03 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b04a9a7-8c22-3424-8f2a-f12f42703b4c | -7.12301 | -43.48177 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5eac0f2d-9f96-3f4d-8917-133758ac00bd | -4.55948 | -44.2049 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| ed8441ac-8f87-301f-8e24-2b8603442dc6 | -8.02956 | -43.14341 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| ddb1ef2a-f3cb-301b-a034-ed8e7a087ee0 | -7.11759 | -43.4824 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c7ab436a-88ea-3ee3-842f-be0fa54cfba6 | -4.55551 | -44.20803 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| d0dd642c-c5b9-3ec7-8337-1f2ebfe0cc30 | -7.12361 | -44.0836 | 2025-08-03 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e4ff619-a2db-300c-8ccf-2f4b74624052 | -7.11337 | -43.48596 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 95053354-dd16-3523-99d3-289545ca9dc7 | -7.11641 | -43.47654 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 88ab4774-45a2-3d3f-a79b-0dce04791bc3 | -8.04833 | -43.10779 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 614bdeb7-c320-373f-8b08-df784758df69 | -7.99645 | -43.18779 | 2025-08-03 04:25:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 4933411f-03bc-30ad-adef-8782757d333d | -8.04462 | -43.10723 | 2025-08-03 04:25:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| a499a94a-b1b2-39a7-a45d-2329ec69da91 | -7.12362 | -43.47763 | 2025-08-03 04:25:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c6169e6-5a84-3508-89d7-818c359b1f76 | -6.09124 | -46.36465 | 2025-08-03 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 771e10ab-e4ee-3072-91a6-6c16f61c8c77 | -4.56345 | -44.20176 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f883f28f-6148-3244-bee0-2210f8eac695 | -4.56288 | -44.20543 | 2025-08-03 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3329674c-991c-3607-b397-5ca0ed5e49b1 | -2.88211 | -40.29915 | 2025-08-03 04:25:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 36d2e745-d62c-3895-953e-e7dce86be1e1 | -3.58321 | -47.51255 | 2025-08-03 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README14.md)
