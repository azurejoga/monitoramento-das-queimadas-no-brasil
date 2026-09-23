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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d345d57f-267c-313a-bc55-aca063bd7a35 | -8.2671 | -45.4337 | 2026-09-23 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 6c577794-521a-31bd-bf45-a22cdceb5cd8 | -7.5704 | -57.6766 | 2026-09-23 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a2b78407-284d-3286-8e38-d4e73ba674fa | -5.7615 | -57.5807 | 2026-09-23 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a6ef8e87-c5ac-3075-8946-325e8b744df9 | -6.6148 | -59.908 | 2026-09-23 14:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 32c4c506-58c1-36b3-a32f-5603ea8c851c | -6.5953 | -45.4727 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| c27fe1fc-0e21-39ab-b62c-19c4cc2316d0 | -6.001 | -51.7903 | 2026-09-23 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 5f272cdd-0815-3abc-a6f0-0c3399493b5e | -6.2394 | -41.6875 | 2026-09-23 14:20:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| cb271a96-d5a7-34d2-b501-ed715ebe659e | -8.1289 | -44.4191 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 34ff10f5-23b7-34c3-897a-b6c2cae96189 | -7.4288 | -44.718 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 2347a42b-8949-3c76-91e8-f74ad3c9be03 | -6.5763 | -45.4968 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 27fb23c5-0123-3cb5-823a-7348b3783ba5 | -6.221 | -41.641 | 2026-09-23 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 72.9 |
| 13e9bdfa-8991-34c3-a74c-8bbdbade284b | -6.8985 | -41.6976 | 2026-09-23 14:20:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 5c6f3693-d033-359f-ad90-3024262d0bf0 | -6.922 | -42.9559 | 2026-09-23 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| dd12e228-f1bc-3cab-a737-ae041f779f67 | -11.6605 | -43.4476 | 2026-09-23 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| aa58d854-f6eb-3544-8b75-b1a36eadf9fa | -6.9841 | -49.7777 | 2026-09-23 14:20:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| dca5ce78-ebd0-3e0c-b42a-d025b271fe29 | -6.4485 | -59.9909 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 4ff27f1e-8ccb-3c5c-89df-b8c13035bdf1 | -6.3015 | -59.9387 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| ed264131-480f-3398-ac65-6423127217f9 | -7.1274 | -43.1009 | 2026-09-23 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 61f9f3e6-6102-3395-a6da-dff1ff8fe743 | -11.0237 | -49.7304 | 2026-09-23 14:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 257f33fd-2725-3acd-acb1-f5658d35305a | -8.1287 | -44.4422 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fc177098-a61b-3a20-82a8-52b71493a06a | -8.7924 | -45.6282 | 2026-09-23 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 086e3418-54a1-3b9d-947e-ec903f3428aa | -6.7123 | -58.9412 | 2026-09-23 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 98beb575-9e57-3afa-bb5e-742efdb0da41 | -8.754 | -44.2589 | 2026-09-23 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 138.3 |
| fb01406c-4164-3f96-9442-927eaeeb9a2e | -11.3551 | -43.3764 | 2026-09-23 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 379.1 |
| 43f8c851-2296-3cab-b06c-377fedda1aac | -6.5948 | -45.5179 | 2026-09-23 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 5a96d89b-dcf2-325b-af8d-d877780efa9a | -9.8307 | -48.451 | 2026-09-23 14:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 8e57b2b0-2c62-3ab9-9d47-35270e4a537b | -7.1203 | -42.083 | 2026-09-23 14:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| a3450ded-9eb2-3291-8f89-0f5c4755992f | -7.4495 | -44.5557 | 2026-09-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 2b4089ae-ec42-3cbe-8800-92a1b152411a | -6.136 | -59.9254 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 61eaf746-fe47-35cb-a8af-f789129fbadb | -9.9163 | -45.0885 | 2026-09-23 14:20:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 990d1ae9-2b35-3b78-aea3-64dbfebec96b | -6.1317 | -45.0109 | 2026-09-23 14:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 25643b23-310c-38cf-9974-3a774878db11 | -7.4153 | -42.6479 | 2026-09-23 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 694eedc5-9683-30a6-9091-14e50971bc9b | -8.7735 | -45.6303 | 2026-09-23 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 41f9b9a3-75db-3f99-8017-535af9acee4d | -6.2399 | -41.6394 | 2026-09-23 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 69.7 |
| 58ce4ece-d6b3-3780-8c00-7f67a4da7877 | -11.4782 | -47.3529 | 2026-09-23 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| a6a89eef-f6c6-335f-a590-f6880355fc8f | -6.4301 | -59.9916 | 2026-09-23 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 49c3bdc0-3a52-3317-a801-de49608e68c4 | -11.4209 | -47.3603 | 2026-09-23 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| a1e42f74-4042-3231-a4d5-873199823a78 | -11.4209 | -47.3603 | 2026-09-23 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 156.4 |
| fe64ad0f-9dc1-3890-9fca-66dc4be7aae6 | -6.001 | -51.7903 | 2026-09-23 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 152399eb-f5d6-3813-bc96-344b75336a24 | -6.0172 | -45.2462 | 2026-09-23 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| b81d156a-4152-35b7-bc14-8179fea7557e | -11.3551 | -43.3764 | 2026-09-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 268.4 |
| 72715ec5-9b3d-3731-8a51-476a035f8d11 | -11.6624 | -50.1954 | 2026-09-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d3e0d145-c9e6-3df5-b3a6-f9c46768e919 | -7.0352 | -44.6396 | 2026-09-23 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 30fdc421-4d24-3e3a-b5f3-77c8e8cf4fca | -11.6426 | -47.7984 | 2026-09-23 14:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 56d16c74-8873-324e-b059-f1ff2864ca20 | -6.4301 | -59.9916 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 084f4d0d-c2c4-31e9-bf17-9cdfca3cb835 | -9.0242 | -48.1403 | 2026-09-23 14:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 44b93962-71d6-327c-b111-371d8b620dda | -6.1317 | -45.0109 | 2026-09-23 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 35262007-4b2c-3221-ac0c-2bf5fa53b71d | -11.6802 | -43.4209 | 2026-09-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 452bc6c2-a6d4-319a-a60c-89d808421342 | -7.1033 | -43.571 | 2026-09-23 14:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| ca8d3d48-19dd-3038-b1a8-57f77196e686 | -7.1088 | -43.0792 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 068d9b17-224f-375e-a0f2-e86206ae9221 | -6.467 | -59.9902 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3ab657d0-af44-32ba-91e8-ce50275fa823 | -3.4635 | -58.3096 | 2026-09-23 14:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 40e7c589-2aec-31b1-bf8b-67b1814791b5 | -9.406 | -47.7507 | 2026-09-23 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 111.0 |
| b4214b79-9da7-336c-a204-1240139972b7 | -11.6621 | -50.2169 | 2026-09-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 32ba3ab7-38a3-323e-8e84-376022fa010f | -7.1277 | -43.0774 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 829a4bbf-0c9b-3767-aef8-aed0559e1f2d | -11.1204 | -48.327 | 2026-09-23 14:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 7aca250b-4099-3bdc-9eff-0a3dad0a065b | -6.5962 | -59.9279 | 2026-09-23 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 077e594a-4f7e-339d-91d5-8ccfb6025254 | -10.5561 | -46.7095 | 2026-09-23 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 292e7ae3-ec3f-3ef6-85f2-681f96d6ffbc | -6.2394 | -41.6875 | 2026-09-23 14:30:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 99.2 |
| f9186841-a7c2-3fbf-b1e7-24185c292e32 | -3.3138 | -59.4281 | 2026-09-23 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 6857ec1c-929e-3dd8-a047-a4ca1b5906ae | -11.3547 | -43.4001 | 2026-09-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| e653ccab-db6b-3350-99fa-14ef92d5a69b | -6.4671 | -59.9711 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ea09ba21-fd90-35fe-be4e-6600bacdc746 | -11.4782 | -47.3529 | 2026-09-23 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 162e6657-a32a-3410-a464-ea843fec2ebc | -6.2026 | -47.5026 | 2026-09-23 14:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 16fab016-5b4d-3db0-8667-045895f59ba2 | -6.5963 | -59.9087 | 2026-09-23 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| b5b88fd2-b8bd-308b-a143-db7ebc13d9a3 | -9.5854 | -48.4549 | 2026-09-23 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 293.7 |
| 2c0a05dc-4536-3854-b160-48c657bbd50c | -7.5434 | -46.2235 | 2026-09-23 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 09bfbec9-baa6-3be4-ad0c-d62770c7f071 | -7.4286 | -44.7409 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 5c909579-e97c-3fbd-aa2a-64906c01f79c | -7.4495 | -44.5557 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3aa0cb1b-6457-3874-99dc-bd25026de5f0 | -3.3138 | -59.4472 | 2026-09-23 14:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 3592eb38-f4ca-3a55-b994-5fe6068f956a | -6.202 | -41.6668 | 2026-09-23 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 32cc6be3-2696-3161-aca7-a0483dfebaa2 | -6.2399 | -41.6394 | 2026-09-23 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 619c425d-2e83-364a-883d-c4114ec8902b | -6.6129 | -43.7317 | 2026-09-23 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 294.8 |
| 7cc19db0-2687-3a07-85e9-95ecf36b3ee9 | -6.6127 | -43.7549 | 2026-09-23 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d57d6c66-3cfc-3355-a3fb-9883bbdfc0e2 | -11.7002 | -50.2125 | 2026-09-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| c4306e6e-c8fd-317e-a330-116cac798dda | -7.4288 | -44.718 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 3964cf57-4790-3638-9e5f-1311dc1de5ca | -8.3591 | -45.6056 | 2026-09-23 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 095c019d-6f2a-3137-88ca-7f291375e05e | -11.6431 | -50.2191 | 2026-09-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b573ba7f-6b18-3fad-a2ae-0f10cde25189 | -6.2205 | -41.6891 | 2026-09-23 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| fb7cd52f-69b6-3835-8792-734c078a71d9 | -6.5941 | -43.7333 | 2026-09-23 14:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| dd503ab4-411a-3e0c-a9d5-e3716f69e4d4 | -9.8499 | -48.4272 | 2026-09-23 14:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 8593d9fe-751c-3c88-94df-005b51e84144 | -3.7167 | -54.1896 | 2026-09-23 14:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 261.4 |
| c89fa331-5671-338f-ba12-36ceebc0143d | -7.5519 | -57.6775 | 2026-09-23 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 326ffb57-e4b9-30eb-94a0-ed575be5048d | -8.5803 | -44.5322 | 2026-09-23 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 141.6 |
| e738c167-fcc8-3021-95c7-73a9fba9cc03 | -6.3382 | -59.9566 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.8 |
| ae2934fc-92ca-3e0b-8c1a-8289aa309e3b | -11.7784 | -50.0743 | 2026-09-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 30b57d7f-d0f0-373f-98ab-3f2facc4155d | -6.3198 | -59.9572 | 2026-09-23 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 7254308a-80f0-3707-bc2f-f4447d6cf713 | -11.8014 | -49.8129 | 2026-09-23 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 66745c7b-54bf-3f9d-bef2-466a3b6d8b73 | -7.4097 | -44.7427 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3aa8be4f-41bc-3efb-9d43-f515f70452f2 | -6.221 | -41.641 | 2026-09-23 14:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 84.4 |
| 2fbc0c5c-25b6-3d7e-988f-3e81ee099c2b | -6.922 | -42.9559 | 2026-09-23 14:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.2 |
| 78e5062c-f124-3eae-9771-abd0d4989855 | -8.754 | -44.2589 | 2026-09-23 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 117.4 |
| b9de04e9-993c-37cd-b17a-5b08b283f906 | -8.0921 | -44.3538 | 2026-09-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 100.0 |
| fa9f44b1-e107-328f-82ff-2ab262a7645a | -6.5636 | -44.8856 | 2026-09-23 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ec296852-27be-3290-84ad-dfa47166f2c8 | -6.6332 | -59.9073 | 2026-09-23 14:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| df860b8a-47bb-34b6-9936-c2747731f0b8 | -7.9904 | -44.9608 | 2026-09-23 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 200dc3a6-0852-3d80-9f9a-671de60ae6e8 | -7.6834 | -45.468 | 2026-09-23 14:30:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 4f2a0915-351a-3d42-b75b-440889bac78d | -6.9841 | -49.7777 | 2026-09-23 14:30:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 71f18d2a-4ecb-3a55-8e5c-7823a318d54e | -11.6596 | -43.4951 | 2026-09-23 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e70e65f9-1187-31ca-b34e-eafaea7d19dc | -8.9205 | -45.931 | 2026-09-23 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |


[Clique aqui para ver as próximas entradas](README142.md)
