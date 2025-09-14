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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f38cc7a3-26bb-3fe3-ad0c-1ab1cc2bd7fd | -20.59714 | -45.22553 | 2025-09-14 03:51:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 09b12ca2-71e0-3170-8e6f-81c343f128bb | -18.37293 | -48.34025 | 2025-09-14 03:51:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3762c1a2-99df-367a-83fc-7ab30babeccd | -21.41776 | -46.60571 | 2025-09-14 03:51:00 | NOAA-20 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1aba4a2-8a41-312e-94d7-26a9ef88bebc | -20.08903 | -46.89902 | 2025-09-14 03:51:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8509bda-737a-3318-9eb2-fdeb8ae64563 | -22.72633 | -49.90801 | 2025-09-14 03:51:00 | NOAA-20 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 309ae180-893c-3c37-bec5-1394c43fc5bc | -23.79266 | -49.94279 | 2025-09-14 03:51:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 84088057-0da4-3a3b-8e2e-d3bb78a2d703 | -22.27604 | -46.03019 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 646c727e-239f-36a2-9564-85eba517e74a | -17.3615 | -52.89982 | 2025-09-14 03:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7655dcb-a37c-36ed-a4c1-08ef29d75032 | -21.91722 | -46.55725 | 2025-09-14 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e2ce7669-3e21-3840-8314-11b2b7e315e2 | -18.16026 | -49.207 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a01a97a3-52d8-3d02-bdef-73e9818ff41d | -25.08365 | -50.9187 | 2025-09-14 03:51:00 | NOAA-20 | GUAMIRANGA | PARANÁ | Brasil | 4108957 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a7833815-fbe5-3470-a707-4f9d39e49fbf | -19.45408 | -43.68672 | 2025-09-14 03:51:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 61484b82-68a7-35e9-803c-c446bb6e5785 | -18.14753 | -49.18793 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c9dff9dc-b682-3ba6-9e76-de35c3eb8210 | -17.6078 | -51.83128 | 2025-09-14 03:51:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e77e69ec-058c-3003-9f9e-8908d5401acf | -18.14667 | -49.1921 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 061a1460-2e9b-3898-8570-55478bb4b7c4 | -18.145 | -49.20012 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 37ef2a2c-5664-32ba-8f86-20638a1e532e | -22.99436 | -46.46202 | 2025-09-14 03:51:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c2448cfe-878b-38f6-994b-112b8e222f42 | -17.60459 | -51.83453 | 2025-09-14 03:51:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4585c360-9c33-350b-9712-14b3398f8de1 | -19.43082 | -47.41128 | 2025-09-14 03:51:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab556e75-71d6-3bcf-80ca-46d7e82b9d8e | -18.14045 | -49.19526 | 2025-09-14 03:51:00 | NOAA-20 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3bf4bf1d-00e8-36b6-9be2-dc04e75447cf | -24.47638 | -50.82072 | 2025-09-14 03:51:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 94a288a3-7033-318a-b4bc-2e21f0ad3860 | -19.70289 | -45.43287 | 2025-09-14 03:51:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a31e2e60-f531-3234-8a8d-24e638b3bb02 | -19.41749 | -42.32881 | 2025-09-14 03:51:00 | NOAA-20 | IPABA | MINAS GERAIS | Brasil | 3131158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 41b30c5c-39be-31f7-b750-267114a0cc15 | -20.14128 | -45.64553 | 2025-09-14 03:51:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5b29d38-1e7b-315d-a013-77b4b99914b2 | -22.29239 | -45.96619 | 2025-09-14 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 63169c7f-3560-3463-9d11-5d1ba418f4d2 | -18.19928 | -47.92013 | 2025-09-14 03:51:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 662da5d0-0ff7-3ac7-bae9-bd0fd8af5ae1 | -27.25232 | -52.0601 | 2025-09-14 03:53:00 | NOAA-20 | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0da58347-d9e2-327b-8f39-7d86da006388 | -26.62848 | -51.81384 | 2025-09-14 03:53:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 693aba02-eca0-321e-a132-bbd7909ca169 | -27.25148 | -52.06374 | 2025-09-14 03:53:00 | NOAA-20 | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f28172d8-93cc-3285-be57-47583b2e20c0 | -27.25611 | -52.06179 | 2025-09-14 03:53:00 | NOAA-20 | CONCÓRDIA | SANTA CATARINA | Brasil | 4204301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6181a67d-7d96-3546-8da1-4f17ab859451 | -12.9294 | -54.7333 | 2025-09-14 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4a879aec-8ed3-34b4-95a7-5c0bbdd71e40 | -22.7492 | -49.8817 | 2025-09-14 04:00:00 | GOES-19 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 589fdada-e944-3dbf-8493-ab37c86f0843 | -12.9294 | -54.7333 | 2025-09-14 04:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 875fe419-6cbf-316c-9b47-e58f8e6f1a9c | 3.00222 | -51.44375 | 2025-09-14 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3a97817-bbd5-35db-93e0-fa9cde7b89e6 | -2.82433 | -47.7254 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbfb6b81-51aa-355f-893b-cdfcfeb6fe18 | -5.97983 | -43.77502 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 861d0b8d-3118-35de-ade0-54c2c1e22a93 | -6.17961 | -41.15129 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4150068f-e54f-36ca-a102-c63785589a3e | -6.44 | -44.08363 | 2025-09-14 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64c46d81-e4da-32ba-bad0-c98be95d254c | -5.08878 | -43.01762 | 2025-09-14 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07720983-3e6f-34d8-ae18-c5576e239ec9 | -5.22052 | -45.45163 | 2025-09-14 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9507226-ec7b-3efa-bba1-45939965efd2 | -6.30538 | -44.57582 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ed9abae-e6eb-3628-b789-086d43dda81e | -3.21982 | -47.12525 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4afd0a47-033b-32e1-93a5-4fd7a1db7477 | -6.17919 | -41.15427 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9a338553-bf78-3945-9c6c-9a5830dcff01 | -6.43287 | -42.62988 | 2025-09-14 04:38:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2c4f152e-5d8a-3861-9ecf-f888c39e4960 | -6.17627 | -41.17495 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd8fdd6a-90eb-3b16-b2b6-dc6f38972885 | -5.73348 | -43.20026 | 2025-09-14 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c43da462-6930-3a14-971b-fcf8a4cc95cc | -4.48811 | -48.11576 | 2025-09-14 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d46c73d1-72bc-3892-9a95-5cf6f9431baa | -5.26367 | -48.57595 | 2025-09-14 04:38:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2070787e-c454-3d40-9060-f92e32709244 | -5.95591 | -44.11664 | 2025-09-14 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0eb560ca-b31d-32a6-ae4b-cd9f561ebb0b | -5.21238 | -45.45489 | 2025-09-14 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81ceebe8-970f-3fd1-be33-feabf01a2e33 | -3.17737 | -49.12312 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfff5c28-a1b9-360d-aad1-a28c73c826db | -6.20589 | -44.5148 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abb435a1-c3ca-3894-9407-b4b6041ffc08 | -5.25021 | -49.86049 | 2025-09-14 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0d47ab7-8029-3807-803c-6e7a20050b8f | -6.10843 | -45.94414 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1d8b8c8-4b23-38e9-b89d-c35203940115 | -5.75616 | -43.91547 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 225f6e4c-b2fd-325c-aa5a-bdbb503bdb4c | -2.95089 | -48.59564 | 2025-09-14 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32a895f2-6079-3905-a797-b7385bec1012 | -6.43908 | -43.3258 | 2025-09-14 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7920f4b3-e792-3843-b374-43c08a08bfb8 | -5.96519 | -43.21428 | 2025-09-14 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3d85680a-4e9f-3ba0-8c65-974e0b7e6c7c | -3.30536 | -51.59663 | 2025-09-14 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 13e52c33-067d-3488-99ca-aa3ab0ff6b5d | -2.32067 | -49.16479 | 2025-09-14 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45e8807b-4c81-3cef-a509-1d53893d8edf | -5.64652 | -43.89602 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c2cbaa3-56b0-3c71-91d8-900aca0391de | -6.77771 | -41.59119 | 2025-09-14 04:38:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cb47640e-898f-39ff-aa28-28121774d85d | -5.76862 | -43.91736 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0529276-6bd1-33c6-8ce7-010e6fd10063 | -5.99262 | -43.98117 | 2025-09-14 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 491121e1-841e-3637-a9f7-56db6e768c98 | -4.27078 | -47.56621 | 2025-09-14 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fff7372-96bd-31fe-a465-971911b9b63f | -5.08815 | -43.02181 | 2025-09-14 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db649b70-c64b-3814-9d0e-9d48613f54ec | -3.79522 | -47.58174 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31b74f23-fd04-32ee-8f10-0d51a4097913 | -6.28293 | -39.68445 | 2025-09-14 04:38:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ca7a7226-bf2e-3b43-8905-828004d1816d | -5.98347 | -43.7796 | 2025-09-14 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6732efa1-c30b-3ee9-b7e0-d9c6cf01790e | -3.83428 | -48.94889 | 2025-09-14 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edf5510c-f5bc-38be-a2cc-8c508d6bde12 | -1.97807 | -47.98198 | 2025-09-14 04:38:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85207f41-e91f-3e17-aba2-7b670fa4decc | -3.79914 | -47.57866 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1524d8d8-22e0-3931-97e3-5dda7a00a65d | -6.11708 | -45.93659 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c74e35e7-d2cd-385d-984e-a301beea1727 | -6.28244 | -39.688 | 2025-09-14 04:38:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b9c3c204-7c65-3e6f-a9a5-008362359be5 | -3.08706 | -49.46191 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edd84e05-a8bb-3653-8db4-55f31259f59b | -5.06286 | -40.47075 | 2025-09-14 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00669d66-d869-3d69-a23d-50a5243bb4af | -6.25634 | -43.47489 | 2025-09-14 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49192334-7e76-3c0e-9882-f81308b4997b | -6.20989 | -44.5155 | 2025-09-14 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4cb4346-dfa6-3f30-aaba-b726138c9911 | -6.17793 | -41.16321 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8f67c7b5-3814-3a14-9a82-e220d9347066 | -5.9968 | -43.98161 | 2025-09-14 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6befb277-478d-3679-8d46-cd4e68c88818 | -5.38108 | -43.42967 | 2025-09-14 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e8ee86f5-dce6-3093-9689-bbcb7f3572e3 | -5.96459 | -43.21848 | 2025-09-14 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ccaba265-63a2-3ca4-88ab-0360bf99b509 | -6.33277 | -43.87333 | 2025-09-14 04:38:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 609989c2-6a32-3a0d-bd37-3a3ae9fd41e4 | -4.63884 | -46.40289 | 2025-09-14 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d8b7ed8-9b09-3c1c-9112-e44a23da3608 | -6.53804 | -39.51087 | 2025-09-14 04:38:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4443b501-8719-3be8-8d16-682e6fe76a5d | -4.05938 | -46.93768 | 2025-09-14 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9944a02-f20a-3b33-a3d1-845d75de2511 | -3.0876 | -49.45846 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac1e71c0-eb1d-3048-82de-653502491937 | -5.06808 | -40.47152 | 2025-09-14 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a6c91fdc-6496-3fe7-9f08-7476dd55b289 | -3.80752 | -47.56895 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7913efb-8228-34b4-a349-98f50b122b51 | -1.41786 | -48.3862 | 2025-09-14 04:38:00 | NOAA-21 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9bc5e521-fbae-3a96-a9b2-b52b952f36c2 | -6.19103 | -43.48322 | 2025-09-14 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5341fa59-436c-3179-8c42-eecbd86cb67e | -3.59547 | -47.51081 | 2025-09-14 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 392ac2da-3c58-3ad3-a475-c90586ac3006 | -6.18217 | -41.1697 | 2025-09-14 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cc00fffc-81e1-39aa-a80e-cd9323e981eb | -4.27133 | -47.56263 | 2025-09-14 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c76eb1ed-85f8-3564-98e5-b8ecc18f0763 | -5.96001 | -44.11729 | 2025-09-14 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9bc4ad5-572d-3c0b-988b-cb25f820f681 | -3.08814 | -49.455 | 2025-09-14 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63849409-36e7-3e73-a55d-4b31d3b7878e | -5.39691 | -40.34633 | 2025-09-14 04:38:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2af7dce7-736d-3af9-ba18-97d046ac2f2f | -3.22241 | -47.63538 | 2025-09-14 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f70f42f6-7792-3e98-a599-e87c8dd45d89 | -3.31703 | -50.07744 | 2025-09-14 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be7a5cc6-cdb8-31b5-9083-4da10d6862ca | -6.1041 | -45.94796 | 2025-09-14 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README27.md)
