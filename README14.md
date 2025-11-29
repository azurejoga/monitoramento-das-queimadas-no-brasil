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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07de90a7-67f8-3ab3-bc94-71ebe625d537 | -2.55125 | -48.39596 | 2025-11-29 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd6bb06e-cf7a-3d0d-8f3b-135a355681b8 | -2.68733 | -47.36191 | 2025-11-29 04:12:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91cb08a0-c344-33e5-812b-db5a9a21f767 | -2.63686 | -48.48146 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d9cc58aa-8f9e-3d56-84e7-c3edecc13eee | -2.46496 | -48.22982 | 2025-11-29 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4b333e9-110c-3c0b-9791-650136609cf1 | -2.3529 | -47.46804 | 2025-11-29 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3008936e-778d-36e1-a61d-5b53b8337469 | -3.43485 | -41.49787 | 2025-11-29 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df49a8a5-59a0-3b97-84bc-b1b12b0928a4 | -2.94097 | -40.43369 | 2025-11-29 04:12:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8804b07f-0f7a-372b-9925-779bcdfa613b | -0.97485 | -47.56704 | 2025-11-29 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0054753a-e38b-3f59-a4ba-9b972e9aa663 | -3.42857 | -45.3656 | 2025-11-29 04:12:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89a01ceb-7339-3ada-a8c3-0fc0b9004bb3 | -2.36542 | -46.27606 | 2025-11-29 04:12:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54c758ff-b525-3acc-a8f0-43a48c9633cc | -1.48555 | -45.7839 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 465b3787-3412-326b-9a7c-af51f07cf703 | -3.89614 | -40.766 | 2025-11-29 04:12:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 30609aa4-0f63-382f-87ce-da8da6dff2fa | -1.48784 | -45.79345 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dd2dec6b-baa5-37d5-8ae6-169d2318475a | -3.1446 | -40.18243 | 2025-11-29 04:12:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| aee5d8ad-32c5-33ca-b2e2-e7fef8c5e42b | -3.78859 | -41.93345 | 2025-11-29 04:12:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 979b9d25-7fc6-39a2-9582-067225b48ace | -3.38146 | -44.4549 | 2025-11-29 04:12:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac1cb723-1cdd-3a5b-82cb-4c20867185f7 | -3.00175 | -45.4281 | 2025-11-29 04:12:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aade8de7-c4af-3ede-a928-d3d7d7fcf76c | -3.59314 | -43.2236 | 2025-11-29 04:12:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 524866df-4126-3146-8864-40e03c821de0 | -2.42439 | -47.22864 | 2025-11-29 04:12:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e549ea0d-6f22-3b16-b033-95f07e843afb | -2.13441 | -46.2151 | 2025-11-29 04:12:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62009ccc-32e6-34f7-a3b8-4a3d18b318de | -0.77362 | -52.33282 | 2025-11-29 04:12:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34933d43-5b0e-3bb6-b346-ae14db9b8bce | -2.6434 | -48.03492 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a4f0fa63-c699-30ec-8588-8980d511b8bd | -3.59441 | -40.86108 | 2025-11-29 04:12:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bf1ad36b-8a18-3565-96b6-21ef472a29ae | -3.34874 | -43.37156 | 2025-11-29 04:12:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8affaf13-550a-31df-8612-5d73db50d3d7 | -1.48393 | -45.78543 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7dacf644-24cc-3aa4-972c-7ed8f9c95a0b | -2.41979 | -47.23157 | 2025-11-29 04:12:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a312f6c7-848a-3d55-a734-09959202424d | -2.25103 | -46.52501 | 2025-11-29 04:12:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 248fd89a-9999-3256-ae03-303bfe0bc1a5 | -4.11908 | -38.65807 | 2025-11-29 04:12:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 22d2da45-368b-3d85-b1e8-4337b8b07c61 | -2.62964 | -48.55431 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a444fab8-6f37-309e-aa0c-985825f17699 | -1.49605 | -47.80649 | 2025-11-29 04:12:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a250d438-ada7-32c3-a54d-b63d59b0fd3d | -3.25616 | -46.92891 | 2025-11-29 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bbdb977b-12dd-3bb5-afbd-5d8320af7019 | -2.60083 | -45.1217 | 2025-11-29 04:12:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d07c13e0-2fc6-37c5-ad5d-96bbee19eee8 | -3.6492 | -42.23669 | 2025-11-29 04:12:00 | NOAA-21 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d89d8208-34bf-36f1-82ad-b63eda4412d7 | -2.78614 | -47.42182 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| db5d60e3-7c1a-3bd7-ad05-3b6e6b95dee1 | -1.48856 | -45.78897 | 2025-11-29 04:12:00 | NOAA-21 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd12352c-0b07-392a-a369-a80271fe2ae0 | -2.79079 | -47.41887 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 022c1b85-608b-31cb-a479-20a64d092abd | -1.49669 | -47.80253 | 2025-11-29 04:12:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4605ad62-8d43-3ac3-bd1f-3cc0206a1b71 | -2.7873 | -47.41465 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0feef7e8-45a7-32b6-bc64-5730b018f39a | -2.74859 | -47.1344 | 2025-11-29 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 18fc89d7-3aa6-3e64-9014-98f0ef22476e | -3.58499 | -44.54404 | 2025-11-29 04:12:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b25d65b-1102-31eb-85cc-39cdefb6cd2b | -2.79021 | -47.42246 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ed957d14-a9cb-32fa-97d0-44cc435193c7 | -2.6354 | -48.54655 | 2025-11-29 04:12:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 11e70f8e-3dec-3595-8d0f-f5cf86a8d3ad | -2.23397 | -51.5686 | 2025-11-29 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 809e03bd-da92-369b-a737-2b5721c79b6b | -2.17271 | -48.42103 | 2025-11-29 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f5331cf8-d7a2-3a58-bfac-c430f23e41f1 | -3.50345 | -44.61675 | 2025-11-29 04:12:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 601103af-e6e4-3ddd-94c7-b633993d317a | -2.61395 | -47.34952 | 2025-11-29 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfcbc813-f082-32d0-9aac-ea386816a858 | -8.16942 | -43.19436 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4d2f3e0-d3c2-3257-94be-4520b20480f6 | -4.0422 | -50.69993 | 2025-11-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfa254c1-a9bb-33fc-ad8b-69c36e5a19c0 | -3.22605 | -50.3218 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| df14e0a6-87e4-38a9-bceb-307ecea1555d | -6.71174 | -40.81941 | 2025-11-29 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 798166ad-7015-3c04-a5fc-b7ea9daa385a | -8.17549 | -43.19887 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 968d603c-24d7-39c7-a82f-1f26b2765024 | -4.42677 | -43.30932 | 2025-11-29 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ed90716-4d7b-3530-9802-a627e4b11073 | -7.23119 | -40.28192 | 2025-11-29 04:14:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ee987af4-a9bd-3b14-bffb-ebaa8e6eaa4d | -5.42076 | -44.85631 | 2025-11-29 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 26c64b59-9729-3451-97db-bdfa2f71341a | -8.17273 | -43.19488 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f547bb13-4348-3076-a22e-be3fca9d0f0a | -4.42622 | -43.31279 | 2025-11-29 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56f2d2df-9ffe-393c-87a5-f23d43fd3dc8 | -3.90064 | -46.34084 | 2025-11-29 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c7b1b66-9733-3b45-972f-54489c7575b7 | -4.52525 | -44.90209 | 2025-11-29 04:14:00 | NOAA-21 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b638e70-9609-3860-9270-a5145ce752e1 | -4.11841 | -44.9023 | 2025-11-29 04:14:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16e22caa-4aff-390f-96d3-c26d057eb099 | -7.24282 | -43.87511 | 2025-11-29 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e4952421-9cb4-3872-8baf-9c914dab4b41 | -5.23541 | -41.24805 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2d21355b-5ca4-3231-85e5-aef582e9d855 | -6.98117 | -42.46146 | 2025-11-29 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fbe25917-92a2-3da9-8651-12505aa028b3 | -9.80476 | -42.0549 | 2025-11-29 04:14:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 28c44e09-8c15-3ff7-9eff-50abbc19b6e1 | -4.73844 | -45.68214 | 2025-11-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d74257b2-2d39-3f4d-afee-891daeef1759 | -4.41596 | -41.98908 | 2025-11-29 04:14:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 73b5a03f-07fe-33ee-9690-9b704315173e | -7.56853 | -42.86081 | 2025-11-29 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d99868b6-3a3b-32be-acd5-79fbead57d9d | -3.46644 | -47.63033 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0e1d9dbb-ea5f-3f6a-9012-07018a6b2e0b | -2.9163 | -53.06747 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67b790e1-0601-3520-876a-8405112c6298 | -5.9449 | -45.39672 | 2025-11-29 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cae309db-f75a-3c00-b763-d08be85af57d | -5.07004 | -40.82212 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| fc9fdcbc-747e-3479-bee6-824e52121333 | -3.03284 | -50.97578 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69204625-a235-3ec9-993d-e6d18fc0f6ed | -4.63252 | -43.98627 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 17573fc5-b9bd-37ab-ad37-b73a12cb610d | -8.17056 | -43.20876 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 468be7f9-75c7-3645-998c-2af3221d829f | -8.16395 | -43.20772 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 466d09de-b3c7-3f0a-a9b7-c844c5f1ece9 | -9.96178 | -42.33118 | 2025-11-29 04:14:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 96cfb60e-633c-38fb-aa42-473760248deb | -3.55299 | -50.3081 | 2025-11-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1f3fc868-9113-3525-9dc0-18195c7748be | -5.61686 | -45.25121 | 2025-11-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41638705-6f4d-366a-8bfa-19eb3255b2d2 | -4.93723 | -41.18779 | 2025-11-29 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 98a3f2b0-7486-36d3-aad9-cb5723ce68f3 | -4.51834 | -44.28153 | 2025-11-29 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f24654df-72ed-37b9-8ca9-24e95521384a | -3.46579 | -47.6339 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9eb77f6e-fee2-3619-a914-597bd7761b7f | -3.32635 | -53.32516 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ce53bba-16f9-313a-88b1-2815e23b777d | -5.36212 | -43.02908 | 2025-11-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9bcbfca0-029a-3024-a4d0-42561b7e3a57 | -2.93613 | -53.27767 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d89a7ca-f575-3746-8176-f59d9abe1c83 | -4.72414 | -45.49828 | 2025-11-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41e44f04-bb3f-39e2-9876-04f90c121050 | -5.46139 | -44.68807 | 2025-11-29 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6453a22-8b86-3459-974d-02f36f6ad874 | -2.96437 | -50.99372 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7663cca9-e64e-3bcc-b58c-e0a6aa958017 | -6.56371 | -44.25235 | 2025-11-29 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e584718f-58fa-3f6d-a4eb-0a66746ee99b | -8.76618 | -40.98323 | 2025-11-29 04:14:00 | NOAA-21 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 763712ed-f1fa-358f-89f9-a0b6d887ac50 | -3.55555 | -50.30661 | 2025-11-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 65dcacd8-f175-31d3-ae58-90ca32df0e26 | -4.17261 | -43.75698 | 2025-11-29 04:14:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fe792e36-a83b-31fb-b35e-4c1fc41adce9 | -6.69763 | -41.45896 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 27de2205-90db-3df7-9afa-0b9a5a992447 | -3.03232 | -50.97881 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11480337-13b4-395c-a231-8437094774da | -4.38891 | -43.83125 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52f68e87-f942-3333-9255-9e34caa7ae85 | -3.038 | -50.97656 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc631c3a-5965-3911-9fff-aac38273e628 | -4.8914 | -43.96532 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3a31d3c-8759-398a-823e-54301c11c373 | -4.37552 | -43.74217 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11c109bc-5a61-3d8d-82f0-2f6e76be443f | -3.97189 | -44.01075 | 2025-11-29 04:14:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e08d4aec-909d-3799-9a73-8ddbe67dc166 | -5.23935 | -41.24496 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dbe556b0-22cd-31df-9aa9-7544c293c7bf | -8.18102 | -43.20684 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 17d6a4e7-bc2e-3c24-96cd-fcc75babf0da | -3.4664 | -47.63021 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README15.md)
