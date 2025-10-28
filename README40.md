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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea4ccdda-f9d9-3ac1-b7f5-1dec9cc05788 | -15.16569 | -47.22519 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1de6d31e-c55c-3c67-bf0a-d774d149a079 | -13.23184 | -47.07332 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5f7740b-9ddd-35c7-9a94-af3a19be4689 | -13.39868 | -47.35643 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a971b65-dbf2-3263-828a-bab1876a6b07 | -18.81718 | -43.22583 | 2025-10-28 04:17:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 83c7de86-811e-31c1-8163-2d4f84441d12 | -15.0277 | -47.39663 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6f4fbc2-85e6-384c-819e-14fe7d6f8657 | -15.19423 | -43.47433 | 2025-10-28 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ea6074d2-bd06-34a2-a22c-950d8e35c000 | -16.15301 | -45.10188 | 2025-10-28 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 893037cd-37c2-3da5-90a5-a0b5d024b34c | -15.11398 | -43.25939 | 2025-10-28 04:17:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d4da5e7b-134f-3c64-9334-524bda4eb51e | -13.35237 | -46.34753 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c0fc215-aeb7-38c2-952f-83d7ae0eb2ad | -14.78953 | -42.96325 | 2025-10-28 04:17:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b1fb6e1f-5a91-3735-abb3-08fdd607978a | -18.1455 | -44.17334 | 2025-10-28 04:17:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d818bdf8-29d2-3df0-95b8-66df2121b383 | -13.3643 | -47.66739 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0e8f3e3-b47d-3de3-8d0c-be816f8050f0 | -13.23249 | -47.0694 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4dbc7abe-9e25-3caf-9627-e98d0fa8321d | -14.62568 | -48.42694 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22e3dfd4-ed8c-3099-a149-fc16c8d9acb2 | -17.3719 | -45.35376 | 2025-10-28 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b6abb50-87b8-3be8-8100-f9583c8ee443 | -14.42626 | -49.42092 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8a6b68e-5be4-3719-9531-39ac372f593d | -13.55611 | -49.58624 | 2025-10-28 04:17:00 | NOAA-21 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a902a4b-5247-3c7a-90f3-cfc58673c190 | -14.4277 | -49.42931 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c2af305-ff5a-3dd1-a367-8b0355453c94 | -14.35132 | -44.57101 | 2025-10-28 04:17:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44ad4ebe-6b92-32a0-baa9-bc98fc4456e2 | -14.4333 | -49.42002 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50eb0e2a-9b9a-39d2-ad28-2c710b10a8f6 | -14.61395 | -48.40835 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fb0d149f-233a-3178-b1cb-f5084877de8b | -13.24753 | -47.04375 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707ab9ac-7e41-3cb5-b5e0-bc062a48a424 | -16.1497 | -45.10133 | 2025-10-28 04:17:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6d8de66-ea3a-3bff-addd-46067f534854 | -13.22646 | -47.10536 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6628782e-8c1a-3406-965f-c5120f482783 | -13.2443 | -47.0631 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37642eb0-300b-3194-9f52-77954ccd6287 | -13.91657 | -48.48639 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b86255bb-5e1c-3606-a6da-253a44937aac | -13.36787 | -47.40973 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 76150618-bf2d-3d92-bc1d-06db62a92c7e | -13.31268 | -47.68945 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41396a45-d505-33b8-bdad-8cd2a540b646 | -14.44229 | -44.79679 | 2025-10-28 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 572ffba6-d51f-3c73-8b91-ee204bcdc292 | -15.16981 | -47.22176 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87a2fe1a-580d-3539-b359-a2a3c93360bc | -14.13052 | -46.97949 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39bced8f-f547-30ff-88b9-9ee6c1bff4de | -13.67111 | -46.52493 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 71d9f4ff-a870-3f46-b865-420de7909880 | -16.74821 | -41.68869 | 2025-10-28 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 245936e1-e899-3c45-9b47-f0eb2c48415e | -13.91184 | -43.89474 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfcb4211-c4d0-3678-b22f-42794a8fa7c1 | -13.62382 | -47.02634 | 2025-10-28 04:17:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6247c17c-5238-3319-9b1c-26bf3b22378c | -16.74513 | -41.6906 | 2025-10-28 04:17:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 55e8a03f-ae92-3ac7-85b5-985c50da8882 | -17.32531 | -43.60376 | 2025-10-28 04:17:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a767ae09-4d1e-3294-96e5-f48ff8cec24b | -18.09768 | -42.40568 | 2025-10-28 04:17:00 | NOAA-21 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 247962e0-f9be-3f20-a627-0208063b177b | -13.73727 | -48.41549 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58df10ab-9b56-3a5f-b9fe-5b55bf64bc26 | -19.02557 | -42.03102 | 2025-10-28 04:17:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 313020de-085e-3e04-b4e4-8d61a4acfc8c | -13.86017 | -43.78733 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f58c60a-13b3-3cb2-af4d-787c463baaab | -16.14696 | -45.09721 | 2025-10-28 04:17:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 378532ab-8ec9-30a2-b9b0-c2c527265f6f | -13.26621 | -47.73316 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d20fc200-53e3-3beb-b010-113543b97640 | -14.70315 | -43.78864 | 2025-10-28 04:17:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f9ae94e-ab25-3a80-8371-d7fec20e877d | -13.73915 | -48.41864 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae844388-85ae-3d4f-ad66-96955b0e984d | -14.76152 | -44.95132 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba9b4e74-491f-35e9-8bf2-399a38c9b1ea | -15.11343 | -43.26315 | 2025-10-28 04:17:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f73df060-843f-3ea4-9237-7f4aebacb28c | -13.62888 | -46.46329 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 83a5d71d-71d7-3e38-ab91-f4e34cd36227 | -13.63843 | -46.46886 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d86534e2-4769-30d3-be61-8edc27ebc487 | -13.73942 | -48.42525 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e374dbc3-ab71-3da0-a251-7dca31599af1 | -13.22283 | -47.08424 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ec52cd48-c538-356d-bc7d-341712da9161 | -12.65749 | -52.61737 | 2025-10-28 04:17:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79c5dc77-8ec4-370e-bad4-daecbee3c379 | -17.31395 | -43.60979 | 2025-10-28 04:17:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a20caae-a77c-3e2b-95c6-253a3f1b21e2 | -13.42355 | -47.38094 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf51740f-cb2e-309f-be1f-50f1316c5509 | -12.97358 | -47.93099 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5c70777-7613-30a5-b7c0-3bbcfffe4db0 | -18.14606 | -44.16956 | 2025-10-28 04:17:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c07da0f2-d8d7-30fb-b915-327456269882 | -14.42469 | -49.42363 | 2025-10-28 04:17:00 | NOAA-21 | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b8dce895-772c-338d-ac6e-658a9bc941e5 | -15.43332 | -44.19009 | 2025-10-28 04:17:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c36fcf6-3320-382e-bed7-4b7c6782b423 | -13.89148 | -48.49929 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77f49eb4-6e4c-38af-9d2b-6f18fc3d6931 | -15.15346 | -46.62129 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e5cf666d-ca76-33e6-a21c-588904b226da | -13.26141 | -47.96043 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 924bc9f2-4d28-3c3f-ba09-ed51a86d1b85 | -19.02928 | -42.03162 | 2025-10-28 04:17:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 0ad37361-9f5a-3f51-9090-1d187847eba1 | -15.76921 | -43.85997 | 2025-10-28 04:17:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c5b9c16-5eb5-33f6-afc6-5fe8974030ca | -13.77919 | -48.49548 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64b8e69c-4132-38b9-bd8b-0496e6e6bd3b | -13.63407 | -47.62167 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e15a26a2-42af-350f-bbac-bf68a04fdc07 | -13.15447 | -47.09821 | 2025-10-28 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eb1cfaf-099d-3a47-ac9d-d83aa39d9ba8 | -15.23266 | -47.94533 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48c7a625-2abc-3053-9091-c83673b44e84 | -13.26337 | -47.7281 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edba3d49-c206-3dcd-9d83-50de3891afc4 | -13.9147 | -43.16317 | 2025-10-28 04:17:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a37ba6d2-4314-3a89-930b-db4f5506fe6d | -14.61338 | -48.41118 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3efba05d-78a6-3819-ba3f-55f856ec2907 | -15.15287 | -46.58282 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51fe13c6-6929-30b0-859a-b0d2679503d9 | -15.15226 | -46.58654 | 2025-10-28 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 06fa9138-e8bc-3e4b-b1d9-90c5ed2f8c0f | -15.19992 | -43.781 | 2025-10-28 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 332a5b72-bc76-3320-8f54-04f2b7e0e9c8 | -12.97724 | -47.9315 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| beec5681-6dea-3015-baad-05f1d1295ff3 | -18.25069 | -51.27412 | 2025-10-28 04:17:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31c6d424-fb87-39ab-aa86-ee106a5e8d2c | -14.89455 | -46.76281 | 2025-10-28 04:17:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5b6f24e5-1a16-3e7a-943f-371ac5b7f277 | -13.78808 | -44.34476 | 2025-10-28 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9eb03453-2d82-3ff2-9b5b-15b75832ecac | -14.66444 | -48.42038 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0b99141-3a49-3caa-822c-9aa484d8ce8e | -14.50739 | -47.89132 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| aaf6fc94-83ac-3d33-be54-057f11aafa98 | -13.42283 | -47.38522 | 2025-10-28 04:17:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f8ff959-2e63-3e8e-99f0-d52f9fb8935c | -19.01814 | -42.02981 | 2025-10-28 04:17:00 | NOAA-21 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f1c8583-f770-303b-8e36-7b5506d42c19 | -15.1976 | -43.47488 | 2025-10-28 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4920805a-e612-30ec-aa64-4672047204a3 | -14.61319 | -48.41282 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33da1fc5-8a33-33b8-b409-91a43a8dab99 | -14.02662 | -48.73365 | 2025-10-28 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33233c4d-9c72-3d20-8a57-2d90178922e7 | -13.31987 | -47.69051 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b75a3fa-ed03-3e87-99c9-21cc2d5a3bd2 | -14.6652 | -48.41594 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe6f7cd6-d9fd-3c5b-9d2b-3fdda9ad6fd3 | -13.73755 | -48.42773 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdf37298-9569-300f-82ab-e337565041ab | -13.74327 | -48.40246 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd8db224-b797-3a35-b850-ef104d81e22d | -13.92204 | -48.43206 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b8d9af12-7cdc-3e37-afe0-c8b7d478b9d0 | -14.03037 | -48.7343 | 2025-10-28 04:17:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6dff4bfc-03b4-324e-babf-eeb6c168a462 | -17.39877 | -45.53137 | 2025-10-28 04:17:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d468f3d2-fe6d-3aab-a781-ec35dd56d339 | -13.3126 | -47.69839 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5abfd16d-8a5d-3a86-be04-c04579da3fba | -15.22858 | -47.94946 | 2025-10-28 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdc77f8f-c7a0-3918-b967-a16470796d63 | -13.91447 | -48.47636 | 2025-10-28 04:17:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 030ef8ed-8c52-3cf4-ab11-b71c28d44761 | -13.22714 | -47.10128 | 2025-10-28 04:17:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0401d49f-6a04-351c-be01-ac8a97e39e9d | -13.25548 | -47.7311 | 2025-10-28 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7ad37dcf-4772-3e22-9729-d582c4fc67cd | -14.28737 | -43.7708 | 2025-10-28 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1d6bea9-463d-3a18-97d0-6e444f80c63b | -17.53627 | -44.61594 | 2025-10-28 04:17:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6acdb17c-c41f-323a-8ac8-ca95f11b3cd8 | -14.63277 | -48.45118 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 394e5d08-62b6-3d06-a71c-289c34596fbd | -15.578 | -43.19875 | 2025-10-28 04:17:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README41.md)
