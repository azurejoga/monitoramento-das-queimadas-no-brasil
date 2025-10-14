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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fb62be3-f3fb-31e4-878d-84fb1aea6476 | -5.88764 | -42.91051 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 443af413-1df0-3a9f-84b2-9fca06a250bf | -6.28958 | -42.98736 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a40c3f0-f282-3bec-9cc4-73b9d66e66f7 | -7.94017 | -44.12006 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2cf259d2-c695-33b0-afec-6e74ac1a102b | -6.15151 | -41.72689 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a23a45c-8518-3ba5-b0bb-cea2648422ee | -7.9409 | -44.11557 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| db37c9c4-6815-3c87-83d1-bf37cf7b328c | -6.15138 | -41.7497 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d63bec6d-67db-3212-8ce0-d4df01b08386 | -4.00358 | -44.66681 | 2025-10-14 04:04:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4952d49c-4155-36b9-befb-39a9011a5ada | -5.87509 | -42.87453 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 20cd57cb-7953-3f27-9de9-fd51541e32e0 | -4.40471 | -50.62601 | 2025-10-14 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c75877c7-1996-304c-b8ef-81a9a9003406 | -7.93443 | -44.11238 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e9309c76-e437-3c1d-9d57-f44ec0694615 | -4.23604 | -48.68795 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28b140b3-524f-356e-abf1-f41e4de18fd3 | -6.30455 | -43.14399 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8611b602-40f7-37a7-87ce-6c554272d76c | -7.1446 | -41.71786 | 2025-10-14 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cbc5e4ea-c922-338e-bd8e-da45e5781ee1 | -5.84653 | -42.32518 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 69d16383-6fa6-3032-8747-54c778b072c5 | -7.50228 | -42.14595 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3ce52e9c-d768-313f-9cc4-477f6ed83112 | -7.94864 | -44.11941 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9f9d4491-5753-3dcf-94c7-86100a90224a | -7.02616 | -38.37631 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0cdd556a-6548-31ff-86f6-60a76086364a | -7.9207 | -44.12141 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 6fa977fc-b97c-3ff0-a215-9c5536907188 | -6.98785 | -38.44667 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30256c90-67a5-3778-ad64-551ea3d24011 | -4.30068 | -50.39804 | 2025-10-14 04:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e621aa32-a319-36a8-bcb5-eab183116255 | -7.083 | -41.95017 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7868480c-8d95-333c-8828-f660648ba6fd | -3.13814 | -50.21548 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e77a8280-a28f-3fa7-bd54-50f3a889d11a | -7.93569 | -44.12393 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 853d3e47-a06a-3617-8572-2426916822ba | -8.25432 | -43.36166 | 2025-10-14 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 146feb99-7e58-3019-9589-cc1032315a20 | -3.09729 | -50.38617 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 97ea7b11-92f3-34cf-acf7-e394abc5b3ce | -6.46459 | -44.18715 | 2025-10-14 04:04:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce4732cb-762f-3135-a8d2-52e6220ac257 | -6.96536 | -41.6813 | 2025-10-14 04:04:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6989202-e5d2-304c-886a-7c4b2e860e3d | -5.85461 | -46.45171 | 2025-10-14 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2632589-d18d-3ca1-9073-035e89636ecf | -5.33241 | -45.1965 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93295f5f-7c0d-3c5b-b458-38b7132d5171 | -7.94712 | -44.12839 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| e5da2ccb-c47a-3514-b5c6-934b81265fec | -7.74825 | -42.43634 | 2025-10-14 04:04:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd9f2a6c-ae77-3ebf-8110-e372a791f04c | -7.43195 | -45.41183 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bb4d080-a20e-3442-be78-1ffe7ecaf8b4 | -7.92745 | -44.12717 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dda6177f-6609-31bf-a7c3-c6b17a447864 | -5.63615 | -50.03297 | 2025-10-14 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 304324b6-ac7e-3c71-957f-5406710923a3 | -6.459 | -44.57777 | 2025-10-14 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93ee1962-9608-3bb6-86d1-fea5ae1a692b | -7.93716 | -44.11493 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5a498e21-2610-3e26-8b06-7bef94531325 | -7.45618 | -40.64823 | 2025-10-14 04:04:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e4f218f2-8ed4-325c-a663-fd04519eb2bb | -5.50059 | -43.0635 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b3804417-0aad-3d71-adf2-f1a865734ed9 | -7.93268 | -44.1188 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 54248a75-e43c-3943-8eed-39537672e14f | -4.84296 | -42.77062 | 2025-10-14 04:04:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8866fd4f-a5c5-31b8-ab7c-741be648950a | -2.8448 | -45.45931 | 2025-10-14 04:04:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eae5ec88-818b-3978-9ae6-7237b936baca | -6.33571 | -43.38399 | 2025-10-14 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c262be7b-1111-3892-adad-32c5bc7d9b97 | -4.8044 | -45.33702 | 2025-10-14 04:04:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e446de38-e8b9-3d47-bbf6-2e9236e7d9d4 | -7.91769 | -44.11628 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47ec521c-d664-32d5-9d78-96082f7b05b3 | -5.69849 | -49.30797 | 2025-10-14 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16859e46-e16b-34b5-b8ad-dc97f3ff82e0 | -6.21621 | -41.56321 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 45be0b2f-2452-3c73-b058-7f89e8223220 | -3.93348 | -42.80857 | 2025-10-14 04:04:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3ba3a94b-38bc-36ac-bf4c-497243acfc11 | -6.15527 | -41.76939 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 692d8af5-17a5-33b3-839b-ae9e87d7950d | -8.53325 | -44.59427 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 13e6a541-0c6b-3ffd-9dc2-ddf5871e12d0 | -3.07033 | -49.40755 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e047bb72-a6a9-3b1b-aaf8-b32d7987cacd | -7.14918 | -41.71115 | 2025-10-14 04:04:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d88e551b-9495-3b3c-91b1-8b539f8ed353 | -3.69078 | -40.32439 | 2025-10-14 04:04:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd3596bd-0861-3fde-a402-1e77e51ebe48 | -3.06457 | -49.40666 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea5c5782-b9b7-3254-a09a-30bc694a29a4 | -7.91996 | -44.12591 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 59dcd35e-5bfa-3e4c-bda1-1bdfd5e29bd6 | -7.14902 | -39.4247 | 2025-10-14 04:04:00 | NPP-375D | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e4fe822-9bec-37f4-83ca-6933b53283c5 | -6.45507 | -44.57711 | 2025-10-14 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a165ed55-7599-34a5-a3a5-c54796d06d92 | -5.59711 | -42.57003 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b80c3d4b-700e-3627-83fa-8abd60a3b0b3 | -4.66809 | -43.1334 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d886d87d-f67c-3479-ad62-290f9ccd41e6 | -6.29109 | -43.90562 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9edd5d46-a590-34cf-a2ec-8cc299f06465 | -6.44612 | -41.80701 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 47bad8a1-9650-3679-919e-51c10edea547 | -7.90295 | -44.99601 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be8cc72d-2d3c-3a2e-b8dc-6136fba14249 | -7.93341 | -44.1143 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eaea80ff-e46d-3691-9785-178ad3dcc940 | -5.94076 | -43.73452 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77cf28e4-c10d-3441-89cb-4ea41c443cb2 | -7.50477 | -43.06602 | 2025-10-14 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d41da81a-04cc-399a-9d8e-16c39516897d | -6.15895 | -41.7243 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 707de7b6-67c6-3e08-a8bd-f17f167564d0 | -2.53271 | -47.80619 | 2025-10-14 04:04:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eee17d7-27fa-37fd-bb75-73edae0c3d46 | -3.04568 | -40.11189 | 2025-10-14 04:04:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 11f8422c-9839-3d14-aa25-c708175a358a | -2.83572 | -48.83521 | 2025-10-14 04:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 354bc577-840f-36b1-ad30-3d9ac22b3be2 | -0.90251 | -47.55043 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 59917ef9-adb5-3596-8d9f-90806a0602da | -5.40264 | -40.8838 | 2025-10-14 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f16ba29d-562e-3705-ae3e-6c05d1f3847b | -6.6681 | -46.13654 | 2025-10-14 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 101cedd9-2fdd-37d9-81a6-010007e92d43 | -7.23087 | -45.32203 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54dc5451-c20b-3f84-8532-8691e59163ad | -6.18696 | -41.74362 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9e62ad05-5ad5-3a77-a896-fb524a70ae56 | -7.62506 | -47.8351 | 2025-10-14 04:04:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4e3ed0c-c65f-3a76-939b-d97f3d75a6f4 | -6.58148 | -43.92263 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e0146137-f67b-37b3-87c7-febe0be17ba1 | -4.56293 | -38.24762 | 2025-10-14 04:04:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50d09da4-e96c-31f9-bc2c-44a286b25053 | -5.89347 | -36.60738 | 2025-10-14 04:04:00 | NPP-375D | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2ee793d-3209-3785-9090-1f58c147e7d4 | -5.74223 | -40.77066 | 2025-10-14 04:04:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 31917b18-5b56-3a2e-b442-5a7541dab0a2 | -6.56637 | -43.92025 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b65613c3-4d0c-3245-a398-26298c9e1d44 | -3.6723 | -48.31007 | 2025-10-14 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ae6748d-0bf2-331b-bbc5-daa3a9927ccd | -5.49261 | -43.06657 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3e4cfd8-a85d-35fd-85d7-35f32fbcc333 | -5.63638 | -42.68809 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af250704-3927-3deb-846f-e4ee5a594d78 | -7.1642 | -46.52707 | 2025-10-14 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 127a291f-17a0-3d7d-9d90-888385036ed6 | -3.09647 | -50.39107 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f956c45d-b008-372e-b8dc-ca56ebc27ed1 | -7.40307 | -39.78769 | 2025-10-14 04:04:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 93049f16-7808-3999-8fbf-e51ee570c9e7 | -7.9329 | -44.12136 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ca080a47-6c7c-3084-aa4e-e07152adb53c | -7.6946 | -42.37303 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c4bd94e2-73cd-3043-b4b4-ac6c6fa79e1f | -7.92144 | -44.11691 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 183737b5-441b-3932-8448-c9dac6acef11 | -6.45569 | -44.58071 | 2025-10-14 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8dfafeab-7ca5-3681-8b35-27940c54e8e2 | -5.59777 | -42.56606 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fce56cf6-7b7e-3af4-855c-8efbfb602eac | -5.10484 | -43.20207 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7fe12026-d765-3672-abf0-15fb5963d2f1 | -6.16259 | -41.72067 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0ab7b6f7-d379-3946-9c5e-f7ab601c6f99 | -4.91689 | -41.54064 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99a9801f-9c72-38f2-a974-13cb43cd5f43 | -5.85862 | -43.85681 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae66effd-d067-3ae9-87ba-45f68d58c4cd | -5.9807 | -43.60939 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0a9c28e-07f5-3bd0-8f48-3274a3c40aed | -7.92685 | -44.13423 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eeebf388-ffed-3aaf-aeb4-5d732292abd8 | -3.12239 | -49.10316 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b94cbc51-7199-30b5-bc4b-ad1b7001f319 | -5.86721 | -42.87745 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 512f315c-2a4c-33ad-8eb9-a334e41dfc36 | -6.38173 | -47.26065 | 2025-10-14 04:04:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 315533ee-7691-307f-baef-6867adeb5f7a | -7.93817 | -44.11301 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |


[Clique aqui para ver as próximas entradas](README13.md)
