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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 796495e5-5e27-3761-a682-3f9542bacca1 | -8.45934 | -47.80321 | 2024-10-15 05:16:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6fa2f10c-7e4f-3551-9821-1a54bc780177 | -7.87581 | -47.74714 | 2024-10-15 05:16:00 | AQUA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a7bec472-0dc3-327e-b766-5d5ec3cd7113 | -7.46448 | -47.67275 | 2024-10-15 05:16:00 | AQUA_M-M | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2e2420be-d43f-3f87-9b48-1e1d7b34d9bb | -6.941 | -44.59635 | 2024-10-15 05:16:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa4feffc-2d2a-3ec7-adbb-04fa407a91c4 | -6.67274 | -49.4543 | 2024-10-15 05:16:00 | AQUA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 6d095607-d3ea-3329-95d1-c3b17bb0c41f | -6.67065 | -49.46731 | 2024-10-15 05:16:00 | AQUA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 7ee1bc3e-d225-32b8-8bf0-63589b22f579 | -2.50208 | -49.06948 | 2024-10-15 05:16:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| a99f278e-f7b4-3f69-9672-e0bb1c829976 | -6.66214 | -49.45267 | 2024-10-15 05:16:00 | AQUA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8d9b6e3f-d4ed-3238-87c4-827738e045fd | -6.66006 | -49.46563 | 2024-10-15 05:16:00 | AQUA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 3d9f94d7-1879-3141-81b3-401cc9b49921 | -6.58635 | -44.1792 | 2024-10-15 05:16:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4709fbda-96c6-3252-bbd1-89d38f81f3df | -6.57067 | -48.23013 | 2024-10-15 05:16:00 | AQUA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 0249da5d-9a86-3521-a026-f5050807be18 | -6.56894 | -48.24103 | 2024-10-15 05:16:00 | AQUA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 43.9 |
| b44bae82-584a-3724-bcc3-0bcfb74ff9a0 | -6.56675 | -48.23499 | 2024-10-15 05:16:00 | AQUA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 66524b5f-93a9-3a4f-b485-53fe7fb73d57 | -6.56508 | -48.24594 | 2024-10-15 05:16:00 | AQUA_M-M | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 9c839280-f6c6-3b10-a01a-1b66626e3b90 | -6.41791 | -49.5975 | 2024-10-15 05:16:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| f8b32196-4f02-341e-8fc6-030b353e8660 | -6.40931 | -49.58212 | 2024-10-15 05:16:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cb2e2b0b-bcb1-32a7-a5c8-8333b0d941ca | -6.41235 | -44.35614 | 2024-10-15 05:16:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ddd64fbb-ed1a-37ac-adf7-7cc96e449a4b | -6.40723 | -49.59533 | 2024-10-15 05:16:00 | AQUA_M-M | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d2019a65-9b17-3286-af74-7673008cb5d0 | -1.86297 | -47.83386 | 2024-10-15 05:16:00 | AQUA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1d96e65d-2ed7-3b13-9ed5-f9984fc3ee09 | -6.403 | -44.73768 | 2024-10-15 05:16:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 02fbaf50-8aca-39be-97da-95ca4c7fc46e | -5.60662 | -47.95937 | 2024-10-15 05:16:00 | AQUA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4b19e849-1ecf-314c-ab1a-deb9994891b1 | -5.38147 | -45.6382 | 2024-10-15 05:16:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1aca6036-3dca-31a0-95fe-d38561a62b95 | -4.57311 | -48.01334 | 2024-10-15 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| ccfc2ab3-3015-39d0-8a09-54d84c111c2d | -4.572 | -48.00748 | 2024-10-15 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 770b7bfe-1a8d-3d24-8002-f2f69d69f3b0 | -4.57031 | -48.01868 | 2024-10-15 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 6906fda0-99a3-3dd4-b3c0-2471c0582185 | -4.53693 | -46.57964 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e4ef0594-d082-345b-bb89-5bb8e1ccbe80 | -4.38603 | -47.75297 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 65bd32ec-2123-3505-a7ad-97dd35fb6fe4 | -4.38436 | -47.76384 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ee51615f-950c-31dd-b44d-bd79fb78c099 | -4.32396 | -48.62414 | 2024-10-15 05:16:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d1b09fbf-f582-38fc-9467-62c93e49270c | -4.22666 | -47.85143 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 35f7efb9-e75c-31c8-9acd-09769a595d06 | -3.95146 | -46.42951 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 40eb6897-8554-33ee-8eb6-92252e6c78cb | -3.95004 | -46.4389 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| f8ae8710-58f6-33b1-ad16-d0a0df332cab | -3.93602 | -46.40805 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 236dbcf0-e9fc-36e3-b428-a880713da687 | -3.9346 | -46.41742 | 2024-10-15 05:16:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0a8a7858-1828-386a-8775-58519c374b18 | -3.92591 | -48.34674 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| e4749832-64b3-3daf-bede-c184a5be008c | -3.92405 | -48.35887 | 2024-10-15 05:16:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| dc4b4b98-35e0-3dd0-aa53-5784277cbcb5 | -2.51247 | -48.55095 | 2024-10-15 05:16:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5c5e4144-d3f6-3e20-86bd-a496d5d2831b | -16.18263 | -43.85411 | 2024-10-15 05:18:00 | AQUA_M-M | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| acef871f-9407-3b77-bb32-ebc0553a018c | -13.92628 | -45.81801 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 376e950a-0f92-32dc-aa24-582abbff8dd6 | -13.92491 | -45.82741 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b80a684e-0318-3fde-8e5e-2664ca4c0e27 | -13.91727 | -45.81667 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 398.6 |
| 39eb3c3d-9204-397e-800a-56b6a12f659a | -13.9159 | -45.82607 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 822.5 |
| 2cce481f-5e6a-3715-84e6-d3623ead8a2c | -13.91454 | -45.83547 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 5c903cf8-45ea-3a68-a572-1edfc1e7f835 | -13.9069 | -45.82473 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 672a11c5-e136-3f0a-b9b5-e8634198ff84 | -13.90553 | -45.83413 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 11f225d6-ae42-3848-88bb-9064fb7c6f1e | -13.90417 | -45.84352 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 95c6a98b-82b0-3156-8b07-ccce35056ddd | -13.89653 | -45.83279 | 2024-10-15 05:18:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e913bf3c-ef30-3bc1-af94-bb708761521d | -12.87428 | -44.60819 | 2024-10-15 05:18:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| b0b25fd3-4857-373f-ad5e-53d1ce556eb6 | -11.92422 | -45.76223 | 2024-10-15 05:18:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6994ab44-3b51-3630-8824-7c5be2f9148b | -11.92287 | -45.77136 | 2024-10-15 05:18:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d341589-0779-334e-8351-645456a5c4b7 | -11.91395 | -45.77004 | 2024-10-15 05:18:00 | AQUA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 112c2977-734e-30f2-bb5b-bdc6a545ac3a | -11.89088 | -43.815 | 2024-10-15 05:18:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 171d7876-229e-3f42-af1b-3dba2da746d0 | -11.8812 | -43.81363 | 2024-10-15 05:18:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 80d41b3d-ba1e-31db-8942-eaaa3df42b01 | -11.44071 | -45.28669 | 2024-10-15 05:18:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b36a611e-a65a-3939-bb25-c5e49271b8e4 | -10.48673 | -42.43426 | 2024-10-15 05:18:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 72e99ecb-3037-39c1-9206-d3af26961ffc | -10.48501 | -42.44697 | 2024-10-15 05:18:00 | AQUA_M-M | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 83fb38c3-455a-36e7-a1f9-05f1abdac9a4 | -10.39341 | -44.81965 | 2024-10-15 05:18:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bba4a472-e633-3a5e-a8e0-dd87d0e7dd7e | -10.09436 | -44.21116 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a4cfcaf2-02b0-3675-b03b-c33cb21e20eb | -10.09294 | -44.22097 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5ad25b70-05cc-3f15-8e9a-d7f297844a2c | -10.09153 | -44.23079 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 26.3 |
| dac606cf-aaae-38d7-bf50-6d8e64a68fad | -10.07862 | -44.18872 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9a3bf29b-403c-3716-8e8b-567d6c950722 | -10.05949 | -44.25636 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 052f6fcf-c2e7-313d-8dc1-3ee558780ecc | -10.05075 | -44.18473 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 618928ca-e2c8-372f-83ef-d86d8cee07f7 | -10.04935 | -44.19459 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cd9eb0df-51a6-35ad-8a1a-7f6d2e22fc2b | -10.04006 | -44.19329 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 97708005-bb72-3d7f-a362-25cd99cf1714 | -10.03866 | -44.20321 | 2024-10-15 05:18:00 | AQUA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ba75a335-d0c2-367f-aa05-4abbcb12311c | -9.96654 | -47.2478 | 2024-10-15 05:18:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e0c1861e-f0e0-3b76-98b2-2d3664629be6 | -9.91443 | -47.28994 | 2024-10-15 05:18:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c3fc2bf2-d435-3787-a701-cf2003080bc9 | -9.52202 | -47.79191 | 2024-10-15 05:18:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1539ee65-ac00-3f46-85be-407737301310 | -9.49906 | -47.81815 | 2024-10-15 05:18:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 843eb91c-38e3-3899-98d2-edbf41c71412 | -10.94937 | -54.0924 | 2024-10-15 05:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ac8940a8-b52f-3ea6-9416-dd4d4fb779d0 | -10.94442 | -54.08616 | 2024-10-15 05:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 5cede8af-b942-33a4-b2bd-e901df25db98 | -10.83139 | -49.23897 | 2024-10-15 05:18:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b74865fb-febe-3c1d-8ebe-5da95ac85c7d | -10.82965 | -49.25006 | 2024-10-15 05:18:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| de9378f9-4a23-3466-b9bb-5b970a509b43 | -10.25875 | -47.27329 | 2024-10-15 05:18:00 | AQUA_M-M | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eacca680-40a2-3b19-9d8f-76417a06ce5f | -21.88366 | -50.49866 | 2024-10-15 05:23:00 | AQUA_M-M | TUPÃ | SÃO PAULO | Brasil | 3555000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| b9cc67ab-1a3e-395b-8eca-b2fb01eec564 | 1.0016 | -52.2164 | 2024-10-15 05:25:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 673ff77b-64ff-3472-a251-199b36a6a054 | -3.1099 | -54.2263 | 2024-10-15 05:25:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 7cf3515d-9d47-3d8d-9c8f-75ff4c4d87a2 | -3.1283 | -54.2259 | 2024-10-15 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| bb8d7a8c-fa13-3f37-85df-429858713d7f | 1.0016 | -52.2164 | 2024-10-15 05:35:00 | GOES-16 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5f42a7ff-9304-34f1-84c8-4016b8c4d55f | 1.00834 | -52.22305 | 2024-10-15 05:40:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 690160db-3f11-36c3-8330-5337473eacc5 | 1.00756 | -52.21825 | 2024-10-15 05:40:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5c8a4491-cf88-333a-b1ba-6aaf6e72e6d7 | -1.20159 | -54.52155 | 2024-10-15 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e5c76e2-d3ee-3283-bfb9-2e2cabbbdcab | -1.19612 | -54.5205 | 2024-10-15 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70151339-f270-3da4-ba6a-65376ee0426d | -1.12855 | -54.11135 | 2024-10-15 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20f36adf-d300-3994-a223-eb7540a23b1c | -1.12795 | -54.11524 | 2024-10-15 05:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bdb76a5c-7246-397c-a51d-6836232cc066 | 4.81404 | -60.3243 | 2024-10-15 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43ace865-4c67-3da4-85fb-4eae88d89a1c | 2.90745 | -60.27412 | 2024-10-15 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02403346-b1bd-3c63-9cd2-c20f3e487f2d | 2.13945 | -60.8505 | 2024-10-15 05:40:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40756fb6-0417-39d2-8eef-be9002d1fe55 | 1.4755 | -60.85766 | 2024-10-15 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a23f1a15-c929-3c7f-9846-bb4e21094c9b | 1.11692 | -60.51709 | 2024-10-15 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fcae85a-2c38-37ca-ba40-254e4f3b8cde | 1.11333 | -60.51765 | 2024-10-15 05:40:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2fb4513-3519-3102-a91d-d9ad2b3558f7 | -4.07375 | -51.07573 | 2024-10-15 05:42:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c6900d3-a8d0-32cf-8a7a-280c250328c7 | -4.07277 | -51.08257 | 2024-10-15 05:42:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90d60ab1-bbd3-3d3b-9bc0-9ade380aa33c | -3.82759 | -51.41449 | 2024-10-15 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43c8ed8f-b389-343b-899b-9672c4811974 | -3.82053 | -51.85869 | 2024-10-15 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 14c82f10-a013-3b2a-be06-3ba79c8457d6 | -3.81966 | -51.86479 | 2024-10-15 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9ded6c64-082a-3636-a7b7-4085da436c13 | -3.8129 | -51.86383 | 2024-10-15 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 75b1049a-d2c5-3d3a-85e3-fdf480ba940a | -3.75135 | -51.93788 | 2024-10-15 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 88ebf801-f415-3508-8b82-5fb52dd60452 | -3.09973 | -53.03925 | 2024-10-15 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README72.md)
