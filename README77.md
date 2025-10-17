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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f44091c8-d3ae-35de-a77e-9d1d95f8d374 | -5.83471 | -40.81582 | 2025-10-17 04:49:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3d6ed9cf-6d57-3298-90af-00c5ad6416c9 | -3.65968 | -51.75211 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 390e17a6-65d4-394e-91ec-66ab7ada7241 | -7.17612 | -46.93358 | 2025-10-17 04:49:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc780532-72b4-3312-9c37-946d8a92a81f | -5.3109 | -50.72989 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cacad371-61ad-35a7-bdea-108e03afbf27 | -6.9945 | -39.22757 | 2025-10-17 04:49:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 28d32a06-0e16-3518-8716-bed2acdec382 | -5.54309 | -41.3158 | 2025-10-17 04:49:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13b6c168-c68c-35f3-b59d-42480244e711 | -5.03925 | -49.2231 | 2025-10-17 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bca59c0-3a75-3a0e-a8ac-f8887f19a1ee | -7.48483 | -42.75844 | 2025-10-17 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d7bae1a-951e-3087-bd99-97f5f2e05cb5 | -6.37732 | -41.47183 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6561a378-3ac2-39c6-af0c-9240c8b3c2dd | -4.19021 | -50.07435 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85386d0c-aad3-37a8-8458-15cc5204bb06 | -4.11104 | -48.02329 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b1bac5b-7cb5-3700-a124-ce73e24e4536 | -6.35359 | -41.48818 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4ed7e904-ba22-359c-8a72-3de404bdd553 | -2.813 | -54.38198 | 2025-10-17 04:49:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ca8b231-4ad9-3866-9dbe-5abda7ed510e | -7.34816 | -43.85793 | 2025-10-17 04:49:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d1debb57-538c-3b04-966b-330437f9a70c | -4.22485 | -48.36033 | 2025-10-17 04:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e250a874-2668-3c9a-9f91-15d55aa492ad | -5.89149 | -43.89513 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf236aeb-4b75-3bee-8480-1eeeb99be3c4 | -6.76429 | -42.38005 | 2025-10-17 04:49:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3e0d5e12-bce8-3b17-9127-f09f11343e4a | -6.37886 | -41.46944 | 2025-10-17 04:49:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 122eb1a7-9d0d-3031-ab0c-840d93da311e | -7.68236 | -42.56307 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c07b4edd-9fad-3ce9-86c8-2abd96c05d2d | -6.82871 | -41.69166 | 2025-10-17 04:49:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1497ecd9-8940-3bc1-a11e-19008addd845 | -5.69715 | -53.63835 | 2025-10-17 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24189649-dc0e-34b4-bae2-323690a91455 | -3.49594 | -51.55114 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdd87c02-2207-3e35-9b79-5406ae0c1887 | -7.66363 | -45.63274 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a4c130f-bc7c-3483-babc-f3ec8e559e42 | -5.79629 | -42.49839 | 2025-10-17 04:49:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 425aa6a2-3fc6-3688-b950-84f35c4feb99 | -3.50715 | -52.48931 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| a2de1ec6-6391-3692-bf4f-10bc06acacea | -7.9054 | -44.98412 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75df8559-a617-3fa8-aaa0-089b3504d46a | -5.87414 | -44.82932 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2526ad3c-05ab-3a7f-9348-41117ec7e5e7 | -5.83662 | -45.53775 | 2025-10-17 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ff8aaca-8fab-3419-abbf-f27bf07c01e0 | -5.89221 | -43.89023 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb0094ad-e641-3fb2-80ba-6e66ebaba592 | -1.51742 | -51.62627 | 2025-10-17 04:49:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e97f1f1b-8e4d-3d8d-8862-64f80d492d9f | -7.94891 | -44.12117 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b98d115e-f3ac-3d40-97a6-ed2add2d9427 | -4.84877 | -48.76896 | 2025-10-17 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d78a86d-167c-389d-871d-7be64f28d21e | -5.28908 | -47.93114 | 2025-10-17 04:49:00 | NPP-375D | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90de44fb-a5d7-33aa-a845-b908011ab351 | -3.53756 | -49.00932 | 2025-10-17 04:49:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6d22a73-b4f7-361f-b185-354bc275b2a1 | -5.87791 | -43.92284 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d86add8-1b8e-3211-bcf3-ad846949658f | -4.56206 | -46.61649 | 2025-10-17 04:49:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d354bab-acd7-3e22-a2e3-b72d4e9a811a | -7.04454 | -42.73269 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f3e7ce3f-cefc-3f20-94f2-efed86be46af | -4.71944 | -46.44473 | 2025-10-17 04:49:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 813ff33f-c975-3220-9310-25300aa21f19 | -3.51224 | -52.49341 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48365c8d-7251-38eb-8f82-7b8de5c31732 | -2.44545 | -52.24924 | 2025-10-17 04:49:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0db72f53-9e10-356f-9f06-bf12ebdee7b4 | -6.3824 | -47.69888 | 2025-10-17 04:49:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ef0d305-c9c7-343a-9954-183c79920b88 | -4.42344 | -47.75072 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b8df8cff-19a6-3029-a939-7d709d084abd | -4.11344 | -50.43148 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a7e1151-8fbb-3826-b0d1-102d43f30e5c | -3.93256 | -49.42813 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d518b1ff-8eab-3760-9f84-ce2590962ff4 | -6.35272 | -41.48675 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| bac0097d-7d55-3377-84ab-b9a07aa6f15c | -8.18894 | -44.1069 | 2025-10-17 04:49:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dd1d092-d23a-37e1-a4fb-38e376d4267e | -4.41515 | -43.40356 | 2025-10-17 04:49:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dc6e027-6f67-3a0f-85b9-c75e0262897b | -7.19811 | -45.48738 | 2025-10-17 04:49:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0dda2e99-e5e2-32fe-9edb-4e44862a60e6 | -3.84124 | -50.97751 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bb7328e-d8e7-3568-ab3c-3ce126492a20 | -4.72356 | -46.15477 | 2025-10-17 04:49:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9353511-7e85-3bc0-adad-5102ef514850 | -5.03585 | -49.22258 | 2025-10-17 04:49:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80f4a16-bffc-3261-bc3a-dc2497f488ef | -3.73063 | -49.68501 | 2025-10-17 04:49:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3249ff95-cc9c-38b5-b257-ca322be74dd4 | -3.60988 | -48.90217 | 2025-10-17 04:49:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| db1585e1-9196-3640-aa43-edd69ab17a77 | -2.70517 | -49.85984 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27be7a8a-c494-3daf-a468-8966bb0beb65 | -3.52717 | -50.31129 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5cdc15d2-6035-3073-95da-24c991370f78 | -4.30204 | -48.0719 | 2025-10-17 04:49:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb74f19f-8521-3d59-863c-0fee6d1f94da | -5.90458 | -44.74221 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7966ca7-967d-3e75-b80a-1f4ec67ab19b | -5.51918 | -47.04074 | 2025-10-17 04:49:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f689cd9c-1afc-3355-a7bf-d5cb109add9c | -8.10128 | -44.98729 | 2025-10-17 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e263d58f-2792-38ab-9cbe-59926b3a181e | -4.49535 | -49.64175 | 2025-10-17 04:49:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 748adfe4-eaf0-3433-9009-1e7da74a03b3 | -7.07854 | -44.94458 | 2025-10-17 04:49:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3b79be4e-0214-3f23-b9eb-90461bac24fd | -7.73783 | -42.50391 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 11ac3070-3d94-3ce0-973c-c1d69382a761 | -7.11109 | -44.7478 | 2025-10-17 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 575f5f9c-8933-361f-9142-d433d6496958 | -3.68123 | -47.63731 | 2025-10-17 04:49:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffbd7120-aa7f-34c5-838b-ef30243b8978 | -3.47049 | -51.66741 | 2025-10-17 04:49:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c9e3c243-79f1-3731-99ed-795a031244fe | -8.45745 | -41.26775 | 2025-10-17 04:49:00 | NPP-375D | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7b93cae2-9f87-3063-af8e-0a2a7c5321e2 | -5.32497 | -42.89731 | 2025-10-17 04:49:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 61e1c145-e764-3997-8d20-70de72bd14ae | -7.95365 | -44.12176 | 2025-10-17 04:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| aaa01d49-1775-35d6-9168-d020a29873fb | -5.4938 | -48.94485 | 2025-10-17 04:49:00 | NPP-375D | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3cd5a08-9642-32ee-8104-c04854486535 | -5.90777 | -44.75124 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 01290334-f1b2-30c2-9622-f6a115bf67a5 | -3.69809 | -49.56504 | 2025-10-17 04:49:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b0ca7e7-689b-36a9-a0a6-0b1fdbd8656f | -7.47076 | -42.16039 | 2025-10-17 04:49:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37fc49b1-85c0-325c-82da-b07a2740d98e | -3.40902 | -52.88169 | 2025-10-17 04:49:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8a78225-3b5a-3690-862a-2d271590c9e2 | -6.94482 | -47.72281 | 2025-10-17 04:49:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 24ae7fed-05a3-3000-837f-ea8e29c0540f | -3.35474 | -49.79485 | 2025-10-17 04:49:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aef1fc16-ddbd-3b2f-abee-09a2a800b52c | -4.95903 | -44.96054 | 2025-10-17 04:49:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d16553c4-63d1-3852-a1e4-234aa911e1ef | -7.17573 | -42.37241 | 2025-10-17 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 98d53439-36ac-3dc0-9f49-aaf3d28688ad | -5.68347 | -48.96587 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23b131a7-1a00-374c-a798-2c49e17212e5 | -3.51199 | -50.21333 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d10efc7-dbcd-38f4-8251-ec12d852addf | -6.29363 | -45.53005 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cfe51bb5-f540-3a64-b353-78334d7d022b | -6.31852 | -40.94333 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 885b49ea-4175-3ccd-9e93-eb787df82850 | -2.96025 | -52.50645 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a873c535-69c2-305b-858f-3862de5ae4df | -6.22328 | -47.04166 | 2025-10-17 04:49:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5cca381-7703-33f3-9c20-8d053aafe3b7 | -7.2971 | -41.95358 | 2025-10-17 04:49:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f8e76b89-b654-32cd-b6db-9aef1cbc308e | -4.96329 | -44.96124 | 2025-10-17 04:49:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a8fde7a-a644-3f92-8b2d-ae080d5199a6 | -5.89201 | -44.82988 | 2025-10-17 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 205ba0e8-f92a-3643-ab87-2894699df5c8 | -8.30164 | -43.40504 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 26219579-ce3e-3bfc-a376-1c311e247408 | -6.13342 | -41.73713 | 2025-10-17 04:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 086d2b52-84cd-31c6-85b7-376fbe65d2a8 | -6.35967 | -41.48513 | 2025-10-17 04:49:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ba66b5c8-6ca3-3779-9ab6-d182c2b53fd4 | -3.81232 | -51.86389 | 2025-10-17 04:49:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f263da28-bfb7-377f-8ab1-5738f9bbf396 | -3.28847 | -52.54841 | 2025-10-17 04:49:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bacdebd4-6c14-385f-a5d7-30ba74d219c3 | -5.91672 | -44.93542 | 2025-10-17 04:49:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c01a0e91-bef1-35a4-b459-d5c65b7724f5 | -5.87324 | -43.8572 | 2025-10-17 04:49:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 26bff0db-e999-3d57-9b32-dbf723a3b874 | -3.21085 | -54.96627 | 2025-10-17 04:49:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d6f43ae-00f0-30a5-a3cd-fe9b9ab4f821 | -5.73655 | -49.13686 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30935bd2-f3f1-3000-abb1-27bbaf6aba83 | -1.43956 | -55.25084 | 2025-10-17 04:49:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc67622e-e872-36b1-82ed-1f114d305f41 | -3.47383 | -50.02304 | 2025-10-17 04:49:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ac102ad2-5d22-30c0-8465-c57ec8e07cdb | -5.60601 | -49.03397 | 2025-10-17 04:49:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22bbb57b-9b2a-3688-9534-19f6f9e9c39f | -5.79261 | -42.50139 | 2025-10-17 04:49:00 | NPP-375D | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 69606519-ad18-3e9f-a33b-5baefd8324f2 | -8.19785 | -43.31321 | 2025-10-17 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |


[Clique aqui para ver as próximas entradas](README78.md)
