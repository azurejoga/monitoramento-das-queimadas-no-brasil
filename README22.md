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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ccbe4d0-d27f-333f-9dcb-5ff93762388c | -3.2503 | -46.8709 | 2024-10-29 03:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 5330be80-aaa0-3f16-8f67-adc03f2d397b | -4.3286 | -43.7801 | 2024-10-29 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6a5ae2b0-4d51-32c2-9413-166f237b4d4e | -4.3473 | -43.779 | 2024-10-29 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| fae00e7e-84af-3196-99c9-98b078ba06aa | -4.3475 | -43.7559 | 2024-10-29 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 8bdcf491-6a6a-3f45-ad22-1f535c5468cd | -4.366 | -43.778 | 2024-10-29 03:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 3e0cc5b4-c018-3a36-883d-1955eb5a9817 | -4.2576 | -46.0965 | 2024-10-29 03:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e7ed9fef-a4e8-3774-a7fc-dfc175a8a00f | -4.2761 | -46.1178 | 2024-10-29 03:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 141.1 |
| c114f923-a59c-394d-9ab1-db5c767d16a7 | -4.2762 | -46.0956 | 2024-10-29 03:15:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 245.6 |
| c8da5a12-4a21-3124-a31f-f388ae3d0179 | -11.138 | -55.5313 | 2024-10-29 03:16:09 | GOES-16 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| eeab1880-7b4b-3ab8-9cc7-81ba909b39b4 | -12.3522 | -49.94 | 2024-10-29 03:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f86c0085-274e-37c2-ab01-0bc3ef795f9d | -12.3526 | -49.9184 | 2024-10-29 03:16:15 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| c9ff74ec-7935-3d29-961b-05a0ac7c0e17 | -13.6028 | -45.587 | 2024-10-29 03:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e9186359-ff66-3bba-ad6d-104b3a6ae61e | -13.6887 | -46.1247 | 2024-10-29 03:16:22 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8f3929f9-9e1b-3af8-b341-2ade16e07f58 | -7.56149 | -38.75251 | 2024-10-29 03:21:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 097d0b32-338a-3070-9980-3095cad421ad | -7.55544 | -38.75771 | 2024-10-29 03:21:00 | NPP-375D | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fc9479fe-2d28-3ca8-b981-c5ed2eb72348 | -7.32395 | -39.36622 | 2024-10-29 03:21:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b27f0a1c-b6dc-30c4-ba50-734a91f6c033 | -7.10681 | -39.59275 | 2024-10-29 03:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| becf40b5-cf91-32d1-a612-939fe94d714a | -7.10204 | -39.58873 | 2024-10-29 03:21:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf7c0875-ad22-3c53-9e7d-00f39dd747a0 | -4.38648 | -43.03974 | 2024-10-29 03:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 41496ba1-ca6d-32bd-aa52-212bbe73403c | -4.38634 | -43.04002 | 2024-10-29 03:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 043c6cd5-9a9e-3bd1-ab6a-5c2cc3bddba7 | -6.3591 | -35.13825 | 2024-10-29 03:21:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a2a7930e-0660-3103-9912-03900adbff3f | -6.82821 | -35.32193 | 2024-10-29 03:21:00 | NPP-375D | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 946fb978-1fb7-3f05-a59b-cc44836296d7 | -6.82763 | -35.32539 | 2024-10-29 03:21:00 | NPP-375D | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 398d8d28-2caf-3cf3-98e0-20f94214ac4c | -7.20803 | -35.23409 | 2024-10-29 03:21:00 | NPP-375D | PILAR | PARAÍBA | Brasil | 2511509 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c232f84a-6f4c-3ac2-9058-977c0fb0c9a5 | -7.20407 | -35.23343 | 2024-10-29 03:21:00 | NPP-375D | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2636b27e-9c46-3872-8c4d-981717f3799d | -7.02984 | -35.2262 | 2024-10-29 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2f17df01-310b-3ea3-8d99-57ede86b7e8d | -7.02857 | -35.22267 | 2024-10-29 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| aaf2c1b0-e8e2-3529-ad91-b499a5933a70 | -7.02586 | -35.22556 | 2024-10-29 03:21:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff52d470-78ad-394f-941d-410254c1e3c9 | -8.51538 | -35.03671 | 2024-10-29 03:21:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3ecb7551-89ba-30d5-800d-35b1ac74edb0 | -8.16109 | -35.38194 | 2024-10-29 03:21:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 934f769d-2678-358f-bf79-15fb80dd1bea | -8.15716 | -35.38126 | 2024-10-29 03:21:00 | NPP-375D | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7caa1964-92b3-34ec-b75a-448e0eeeee41 | -4.18205 | -38.36192 | 2024-10-29 03:21:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bea46f7d-fdef-3c78-bcb3-bd2ed74adc88 | -4.18155 | -38.36493 | 2024-10-29 03:21:00 | NPP-375D | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f43b23a2-2289-3c97-ad47-135bf7fc5b73 | -7.08643 | -40.59055 | 2024-10-29 03:21:00 | NPP-375D | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e48a51d6-a174-3cd8-a8bd-b1bf98ccc48c | -9.09574 | -40.366 | 2024-10-29 03:21:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7ce858eb-f0d3-3cfb-9acd-55b5676e0c8f | -8.80557 | -40.96435 | 2024-10-29 03:21:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a8f56559-f557-32b1-8e09-3b0165ae3d76 | -8.80487 | -40.96818 | 2024-10-29 03:21:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5f03fdb0-8911-3bb9-944d-012078029288 | -8.80219 | -40.96473 | 2024-10-29 03:21:00 | NPP-375D | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8493e0a7-7e56-31a2-8602-697938643e00 | -3.59244 | -40.33218 | 2024-10-29 03:21:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 63f67c6a-969d-39c6-8489-a2020911bf0f | -3.59173 | -40.33627 | 2024-10-29 03:21:00 | NPP-375D | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 56c7d0d0-879a-3335-ade3-428e7c5da6ee | -3.16207 | -40.20775 | 2024-10-29 03:21:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 15882e79-0b2f-3ac4-a25d-a40806d29019 | -4.40896 | -40.69524 | 2024-10-29 03:21:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 351e2e0b-8060-3485-b93e-27d6d558d9fd | -4.403 | -40.69413 | 2024-10-29 03:21:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 68a82a38-d6bd-3aa9-8d7d-364d2a5bd852 | -3.8972 | -41.04148 | 2024-10-29 03:21:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af200881-b492-3a6e-94d7-a2c35887f13f | -3.89185 | -41.03566 | 2024-10-29 03:21:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd9ec334-b71f-3565-9e67-f4f8775f8548 | -3.80382 | -40.96456 | 2024-10-29 03:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ca5b6167-8bf9-3d69-9018-22da5f91bebf | -3.80352 | -40.96101 | 2024-10-29 03:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f16323e2-86a9-3879-9907-1f8a8d681711 | -3.80275 | -40.96544 | 2024-10-29 03:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 5ec8e9af-fc97-362d-a4c2-f39161e3380f | -3.79774 | -40.96322 | 2024-10-29 03:21:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 42e76c6f-1780-372f-8fcb-c5de7943f5d4 | -6.35846 | -41.5771 | 2024-10-29 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9b674e97-299b-31e7-a740-e5e431adf7c7 | -6.35843 | -41.5769 | 2024-10-29 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 516e64e3-23cd-3b32-8b21-96022d3ed424 | -6.35766 | -41.58169 | 2024-10-29 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 621170f7-dcf1-3550-b1a4-9c499413afcb | -6.35759 | -41.58149 | 2024-10-29 03:21:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b841f251-66ca-3981-b69e-54b4417ca98d | -6.3552 | -41.59451 | 2024-10-29 03:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7fd5de33-ea6b-3b64-9fea-483c509ae9fc | -6.35148 | -41.58088 | 2024-10-29 03:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7e4e537b-c847-3714-aec8-8eb855dd8f44 | -6.35142 | -41.58071 | 2024-10-29 03:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44f54f47-bc85-3808-9186-b95597a60b84 | -6.15662 | -41.86217 | 2024-10-29 03:21:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9d0ecb39-8a23-3ab4-9c51-c2a8c18bc0e1 | -6.15579 | -41.86682 | 2024-10-29 03:21:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3150bb68-ea4a-3482-af34-79ffb3ff8a5f | -6.14954 | -41.86571 | 2024-10-29 03:21:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 02505941-8c56-3c21-a370-21dc8a828e8c | -6.99839 | -41.34096 | 2024-10-29 03:21:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9c898482-2e24-3be9-819b-2d0269b06d4e | -6.99326 | -41.33527 | 2024-10-29 03:21:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 89d33405-bab3-3757-bdad-b4d72bcf8d34 | -6.99243 | -41.33988 | 2024-10-29 03:21:00 | NPP-375D | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e36e31c1-37b9-3fbf-905d-cb504fd88934 | -6.98728 | -41.33427 | 2024-10-29 03:21:00 | NPP-375D | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 14407ce3-15fc-35ee-9369-55a3affa0fc1 | -4.3796 | -43.03851 | 2024-10-29 03:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12791510-d816-399f-973b-e6c42bfec12d | -4.37946 | -43.03883 | 2024-10-29 03:21:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77ddd575-efcd-36ba-b7cd-3256f18c8d23 | -7.34177 | -43.57928 | 2024-10-29 03:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| fb705e71-6aef-30b8-acf0-1ec7058d9da2 | -7.34164 | -43.57618 | 2024-10-29 03:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 22a75666-c9c8-3f7b-bc4f-4238ab8542e2 | -7.34041 | -43.58273 | 2024-10-29 03:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8ba69461-ed9a-3969-af47-84795d47466c | -7.3257 | -43.58622 | 2024-10-29 03:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8d1b0094-3fc2-3dc9-b379-a571e1757816 | -7.31889 | -43.5851 | 2024-10-29 03:21:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 840911fb-27a6-33e3-a666-45a3a050393e | -6.6339 | -42.79618 | 2024-10-29 03:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ac376a4b-fa14-3eec-adf8-f59d0d2fe333 | -6.63289 | -42.8017 | 2024-10-29 03:21:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 6e2b89a3-03b5-3645-a269-8cafc784e274 | -4.35189 | -43.77254 | 2024-10-29 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24aab956-61ae-3906-8779-e50c836d615e | -4.35057 | -43.7798 | 2024-10-29 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| ee3ffd5e-53e2-301c-8f76-13a0872a8c0d | -4.3497 | -43.77431 | 2024-10-29 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| d2d10898-1780-391a-911e-e4c023b80c49 | -4.34842 | -43.78162 | 2024-10-29 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 4b9a5148-cec4-3cc9-8c42-7193b4c9a617 | -4.34336 | -43.77866 | 2024-10-29 03:21:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 531947d7-f2bf-3d61-9cae-f8b65bce05c7 | -5.28792 | -43.41277 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 812abea1-a93f-3e90-b495-34dda02983bf | -5.28353 | -43.40662 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 485d3053-3aa8-3040-ae3d-55123032ba45 | -5.28237 | -43.41316 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a8ef7789-0800-3032-9765-0ebd87111440 | -5.28214 | -43.40527 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2b6d49fe-d11d-34d7-b88a-9f222a1dac35 | -5.28094 | -43.4118 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0817f4b6-d52a-31b6-a95f-8cdd2ff6a10d | -5.27975 | -43.41822 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cdae4baa-5e3a-346b-bc0c-37384b57b6eb | -5.27538 | -43.4122 | 2024-10-29 03:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b396f88f-d4d8-393b-8f66-f69deccf237c | -5.06337 | -44.2212 | 2024-10-29 03:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bac6480-0ca0-3827-942d-5cd2330d97ba | -5.05614 | -44.21954 | 2024-10-29 03:21:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4113eec5-db8c-38a9-9f55-ae8c753c324b | -7.42055 | -44.80025 | 2024-10-29 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83d4656a-5533-37cf-96bf-d2c66018dcc3 | -7.41427 | -44.79895 | 2024-10-29 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba874133-ee73-3936-a040-d32b0cc99814 | -7.41323 | -44.79921 | 2024-10-29 03:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ca8751f-1997-3e27-9c5b-736cbbbdc879 | -10.92872 | -37.66484 | 2024-10-29 03:23:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e26853e-33d5-341c-8da8-4612b1771079 | -10.92826 | -37.66761 | 2024-10-29 03:23:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cf656551-b232-3702-aff5-795e5455bc43 | -11.23666 | -39.41051 | 2024-10-29 03:23:00 | NPP-375D | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| df431555-0d15-351c-b20c-c90d45d4784d | -9.38498 | -40.79618 | 2024-10-29 03:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b838a84c-fb21-3b6c-bd52-7c2939ba87b4 | -9.38434 | -40.79972 | 2024-10-29 03:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8d9250b9-e3a0-3ae4-988d-206f3d5a8e88 | -9.38373 | -40.7949 | 2024-10-29 03:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c243da69-35b0-38fa-bc91-9c06035fe05d | -9.38305 | -40.79847 | 2024-10-29 03:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ce95807d-534d-30ce-b1c0-58266e579457 | -9.37946 | -40.79512 | 2024-10-29 03:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fbf1e45b-261e-3bbd-8c63-6bc87e474e8b | -9.37879 | -40.79874 | 2024-10-29 03:23:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0e8091a6-a97c-30b7-b188-ac7003cdcbf2 | -14.00761 | -41.01539 | 2024-10-29 03:23:00 | NPP-375D | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 26a188be-9740-3468-a28a-115fca0aed1f | -14.007 | -41.01847 | 2024-10-29 03:23:00 | NPP-375D | CONTENDAS DO SINCORÁ | BAHIA | Brasil | 2908804 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README23.md)
