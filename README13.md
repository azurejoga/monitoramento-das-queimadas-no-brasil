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
| fd2e207a-e19c-323d-a706-8255f7f3dd89 | -1.6065 | -53.37004 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b4717bb-1e0b-3492-aa34-fb0d0c63f69e | -2.80584 | -47.58994 | 2024-12-27 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 748e33f4-2405-3be2-bdf6-b44c0e15410e | -1.64512 | -45.86588 | 2024-12-27 04:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a40ef976-05bf-30d5-9f06-788d331b470d | -3.41828 | -44.90351 | 2024-12-27 04:55:00 | NPP-375D | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62430a78-8a53-3e1d-a111-83570ec73434 | -3.19099 | -45.98775 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da2e4fb1-967d-36da-a4aa-1c8d953a3e68 | -1.64433 | -45.87098 | 2024-12-27 04:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2545bf09-bf95-3f07-920c-9d93a19c6496 | -3.23285 | -45.97252 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ef70d92d-446e-381a-b16a-9dab2f0f888d | -2.25615 | -46.39323 | 2024-12-27 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0b10e5b4-b32f-3537-a3e4-fa514ab54b63 | -1.81161 | -45.57856 | 2024-12-27 04:55:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 515e09f5-d559-3aa4-adff-a546ed77ab5b | -3.06995 | -41.89429 | 2024-12-27 04:55:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b1b3965-5e6f-30ec-8693-5b2e5f6b7ffa | -3.06656 | -47.7644 | 2024-12-27 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bec82771-1e28-32ff-ba64-f696e287c90d | -3.00166 | -48.05246 | 2024-12-27 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3bc04f49-e7cb-3ac0-9282-cd8899772396 | -1.35508 | -53.6741 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4a918c3-7809-34aa-ad97-f2db77e4b9e1 | -1.87633 | -53.33127 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4d94b16-58f0-3102-b287-e735758fb5c3 | -3.07421 | -41.89668 | 2024-12-27 04:55:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e6c90fd8-77c7-3b74-808b-213427a1a628 | -2.27722 | -45.57837 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0fa3d47-8734-333a-8efe-3064dd5e0b2b | -1.27519 | -52.70301 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba236ae2-be3c-31ec-8593-5b7b5c263c9f | -1.89004 | -53.28749 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37fd92e3-38d1-345c-86b7-b1a1ecb77e5a | -2.63287 | -45.94782 | 2024-12-27 04:55:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aca701a6-0658-36b0-b6be-95787c27c81e | -3.19258 | -45.98659 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdd01e55-c48c-354d-8505-2bd05a84c554 | -2.78814 | -46.72818 | 2024-12-27 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52f9e360-f925-3f2d-b73b-da9302c8f0c8 | -3.69794 | -43.41686 | 2024-12-27 04:55:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e2f9e55a-f340-39bc-b82a-32d32b7e6a7c | -3.19177 | -45.98242 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af77f6a1-68ff-3b9b-9a36-d4352dcd1f3d | -3.41352 | -44.89957 | 2024-12-27 04:55:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96cf79a2-7153-3b44-94bd-20608947de95 | -3.00053 | -48.06 | 2024-12-27 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a14bb662-190f-3b2d-abac-46c26b702417 | -3.23365 | -45.96716 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 557ed2fe-9ba4-395c-8a74-1c1dcb4a3a9d | -1.55485 | -53.50335 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6e6e84ab-de45-3675-8a09-bf6699c0bd52 | -1.32067 | -53.42093 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8113bdb9-a125-3980-8601-7ae3a21d3ad1 | -1.35453 | -53.6776 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe05c7ec-aa8d-3ec0-9309-b9c95953d99a | -1.5554 | -53.4999 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce1f4722-bf3c-3d9e-8aa3-7d1c2d409a24 | -1.87458 | -53.29921 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5094190e-b9b4-3e9d-82b2-425e780e605d | -2.28294 | -45.57362 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ae30cd06-56e5-35ae-8b24-e13c725e3dd8 | -3.19742 | -45.9873 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fbba6a7-bb98-3acb-8ce6-1cadfdfcc570 | -1.60317 | -53.36953 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed1eced0-7b26-32b3-a90e-9ca18cff7fd4 | -1.75271 | -52.61027 | 2024-12-27 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 056f0c04-0afb-3b0b-81e3-7d77695dbe8b | -1.26231 | -53.83381 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e31627f-a257-3c87-84db-587346f772f9 | -3.07022 | -47.76913 | 2024-12-27 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84bd1f5b-6731-3ccc-96bc-730b0543dae0 | -3.13843 | -46.34637 | 2024-12-27 04:55:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eabf0a7e-b184-34ff-b5b7-3e804bfb6d1e | -3.3022 | -45.60925 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0d9317e8-1c41-318d-a28a-c3c48ad953d4 | -2.44115 | -51.7966 | 2024-12-27 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8115564-8efa-3db4-9b0e-e24fdf9a48e8 | -1.55872 | -53.50042 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f267509-87ac-342f-a91a-19d229b16c09 | -3.03288 | -40.12086 | 2024-12-27 04:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d1e1187e-2ae7-35e0-8b8f-be39c872aa7c | -2.09798 | -53.49292 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e556d6a8-db44-3fb5-8513-edb3f2f59042 | -1.02468 | -47.6319 | 2024-12-27 04:55:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a467a4f-b449-3f9f-b855-617e963ad290 | -2.15752 | -53.73558 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5bb38694-4fe6-3621-b879-475ebdddd3c3 | -1.75217 | -52.61377 | 2024-12-27 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed8640e4-5941-340e-93df-ff8bc10fdd43 | -3.19661 | -45.98313 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88549ca4-4124-3388-8123-0cf11ff129e0 | 3.31813 | -60.08131 | 2024-12-27 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3be1a5eb-54e5-35ee-910d-be4ff0c32ef4 | -1.55818 | -53.50387 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c6f57c-477c-3b86-a140-d0d6bed6d261 | -1.19306 | -53.58805 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55ae98de-cbfe-3bbe-a6ce-0f9951c0d870 | -2.2858 | -45.57872 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9adb2d10-77d4-382e-9ea9-e9a6381c70c8 | -1.79786 | -53.2272 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41d95dce-c050-3788-b68b-54ad646c656b | -1.1279 | -54.13105 | 2024-12-27 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d2ccfc2-72ee-3871-91d4-3616e1a3ea19 | -0.06221 | -51.65466 | 2024-12-27 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5ce9708-af9e-3561-80da-050fcdeee3ef | -2.11359 | -53.66851 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66bb0b8f-9f73-3f26-8de4-9694647d06fd | -3.1966 | -45.99263 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fc876d5-870a-3605-b5de-89f0b8ef0078 | -1.5833 | -53.38763 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 028ae9a7-19a0-38e5-be3f-7eaf40fd7c3c | -3.04087 | -40.11546 | 2024-12-27 04:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0dd46a88-9a7b-3f82-b3b8-ba04bbad11ed | -1.35853 | -52.38464 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f716ad8-3484-39b5-a262-e5ddaa0fb7d9 | -3.19505 | -45.9938 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38d2c414-e9cb-3c7c-85ee-e8d64eaeb49f | -1.49176 | -52.39853 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0b8a0c26-93a5-3420-85d6-59d62c670f67 | -3.18555 | -46.12528 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5590d554-a28d-335e-afd3-614f87ed147c | 3.42053 | -60.22187 | 2024-12-27 04:55:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e417839-bfbb-35bc-9d65-2d3254c15135 | -3.0011 | -48.05623 | 2024-12-27 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fa943910-e79f-3682-bd3c-f5197624b63c | -2.63768 | -45.94858 | 2024-12-27 04:55:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 219f7ce6-da8f-3225-8be6-05b0ba0b4ab9 | -3.2377 | -45.97325 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9aab6fe2-3423-3a14-9b69-de1102180e21 | -2.28089 | -45.57799 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 52a087c7-0f80-304f-b32d-976918d2691c | -1.17009 | -53.73356 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9faac29-14d0-37c7-ac09-0c467cbbb875 | -1.80172 | -53.22427 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb8939fd-936c-3669-bf7f-865bd2f2121a | -2.28175 | -45.57252 | 2024-12-27 04:55:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eac3273a-abe9-35b1-b351-a2c2951f0792 | -1.65177 | -45.4522 | 2024-12-27 04:55:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ecbe05a-fa72-3f00-9104-e7457d415051 | -3.19583 | -45.98846 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a9305f59-fab3-3bf8-b3c5-08d865ced6ea | -3.18294 | -45.92011 | 2024-12-27 04:55:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4768bee0-3c01-3a59-bdd5-9f8de9df02d9 | -2.15474 | -53.7316 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 62f7609a-22bb-34af-bcab-9f4ac5415868 | -1.32579 | -53.47476 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| deeac637-a727-38c9-abaf-529c40f03085 | -1.44223 | -53.51064 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d36d761e-217b-304a-8207-2ef2f8ae98b1 | 3.31733 | -60.08279 | 2024-12-27 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5bfe30b-ba20-3ea0-8055-4a49724bcf0b | -1.87771 | -53.23612 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3fe61fd-509c-37d2-831a-80bc97bb3a95 | -3.19176 | -45.99189 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a4b8e78-370f-370f-94fc-b090d7b156e1 | -3.40829 | -44.89879 | 2024-12-27 04:55:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e941cb0-4ad2-3657-8cf9-fb10580bc39e | -1.65309 | -45.45331 | 2024-12-27 04:55:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed8d61c2-8d86-3c9d-9155-67d5c8072265 | -1.55207 | -53.49938 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e8e1be05-6311-35f0-a049-60f3789dc6e7 | -3.03384 | -40.11428 | 2024-12-27 04:55:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 450765fc-40ba-3898-99e0-757369d4b99c | -3.06922 | -41.89936 | 2024-12-27 04:55:00 | NPP-375D | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b04921d3-7ec0-38af-918f-e1694b31989e | -1.16954 | -53.73701 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62f5172c-3ac1-35b8-87e9-13ae92d856a6 | -3.19034 | -46.12603 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d04e00b-02da-3d44-b2d2-4819af7624dc | -1.65228 | -45.45877 | 2024-12-27 04:55:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5919fad-ba3b-3f8f-8991-025afca655cb | -3.18631 | -46.12011 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c752720-8a02-318a-bff2-e51810109da6 | -1.44603 | -53.68127 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 491f960a-d2fd-3494-9f06-79d574f84de3 | -3.13728 | -46.34451 | 2024-12-27 04:55:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9a73f5d-6d1b-34bb-be86-b94ae747e1ae | -1.49231 | -52.39503 | 2024-12-27 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a30fa5d3-fdf2-3117-86ca-001d8e41c5b1 | -3.41305 | -44.90273 | 2024-12-27 04:55:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f24124de-296c-3461-a892-540132865be2 | 3.41981 | -60.22148 | 2024-12-27 04:55:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32ed39e4-0050-3822-93bb-4b3762618ebd | -3.06595 | -47.76844 | 2024-12-27 04:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ea6f610-e28b-3024-b0a9-a4ae858c74e8 | -2.15365 | -53.73851 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f51f5e-7530-334f-9c07-aa94fc44276e | -1.4427 | -53.68075 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 957c2580-7b5f-301a-8881-0c7e00f57cd4 | -3.1934 | -45.98127 | 2024-12-27 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e41b4bf-e8ee-3085-9979-72aa55cf7d5d | -1.89058 | -53.28404 | 2024-12-27 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 180d8be6-8090-35d2-ab63-275be5f3b997 | -1.12455 | -54.13052 | 2024-12-27 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d8851a9-c7f1-32d1-ad4d-4cc285aeb2a8 | -1.64988 | -45.86661 | 2024-12-27 04:55:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README14.md)
