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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0cc0044-7595-38ee-afbb-50496a7a9622 | -13.02762 | -42.80993 | 2025-09-30 03:28:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 3bf43d42-7972-38ca-b527-36fa8d69ec6c | -11.67494 | -44.29616 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99c44612-9dac-3928-bc4f-47643b81f494 | -11.94779 | -43.91838 | 2025-09-30 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8c905ab-ef45-306f-a681-854d0aad55ef | -11.69754 | -44.31875 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5924d7a9-8e1f-3612-aafd-dca3a2e33343 | -10.20271 | -44.89864 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 53d54962-7b64-3168-897a-3ec36f321807 | -11.68147 | -44.29757 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93f44b15-3c26-3b7f-a4ad-0ea2a4b44255 | -10.18241 | -44.90192 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 0ee0b7f9-a55a-3e77-9f41-c0480ae89925 | -13.62641 | -42.53671 | 2025-09-30 03:28:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 25fd372e-93dc-38f2-91df-7cbea7771fe3 | -15.05406 | -46.97186 | 2025-09-30 03:28:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 336508df-3ede-3db3-82ca-c50075df836c | -15.77163 | -43.67448 | 2025-09-30 03:28:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdca4f1f-a478-30ca-87af-e53ef178845c | -14.50377 | -46.19441 | 2025-09-30 03:28:00 | NPP-375D | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| edb63f8f-4c53-307d-92bc-d820707a89d2 | -12.58299 | -41.28709 | 2025-09-30 03:28:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6e6bb2a-2222-315b-b949-114b5566143f | -16.83162 | -39.33609 | 2025-09-30 03:28:00 | NPP-375D | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3040e8a4-ad87-3c88-b691-b1ad07674e3a | -13.02851 | -42.80546 | 2025-09-30 03:28:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 7b017ec4-3cc5-31c2-b654-01aa724553b5 | -13.23213 | -43.37102 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 2162b370-84bb-302e-a667-3dacca795122 | -10.18067 | -44.90049 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| a2f32527-7dab-3159-8cc0-5d1fd1cdbc98 | -13.02662 | -42.80742 | 2025-09-30 03:28:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 70494eec-d3ce-37ef-89e1-5649666fee7b | -15.29056 | -46.41563 | 2025-09-30 03:28:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4e7e1a8-309c-396b-9246-b289fd831212 | -14.64827 | -46.97108 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d66ad9b1-da00-38d1-9964-90be5b5d3712 | -15.05221 | -46.97359 | 2025-09-30 03:28:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cd3d6c30-9760-35c0-92e0-7c09261fa6d8 | -14.08756 | -44.09158 | 2025-09-30 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 997cb89f-996d-36cd-b01a-02a8ec7094ac | -14.65712 | -46.96542 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc464725-b44a-3bee-b27b-9929cfa29e7d | -12.88132 | -44.68707 | 2025-09-30 03:28:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 495bc8bc-49cd-34cd-bc64-9f0deed77671 | -11.46078 | -45.01065 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9d9cc675-59b4-3255-a038-6884933a7889 | -13.16108 | -42.35481 | 2025-09-30 03:28:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8d5fc161-a779-32e8-a2e2-579e12dffaab | -11.4356 | -43.50274 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d29be30d-f9d4-3d0a-8ac5-e7320d2759e1 | -11.4346 | -43.50766 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5fda32ab-daf9-3407-836b-975c9b06ae8f | -12.88482 | -44.69425 | 2025-09-30 03:28:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d787e325-cd4c-371f-ac5c-6373f9228037 | -11.72343 | -44.4437 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 04e1a7f0-9917-378e-86d1-6260bad07126 | -10.75854 | -45.37859 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a5e5668-92bf-322c-94c9-a649c2b27b6d | -14.74889 | -45.66232 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 39a2639c-d3a0-3c3b-978b-cf67fa038d3a | -16.22595 | -41.73215 | 2025-09-30 03:28:00 | NPP-375D | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bc5d9c06-ec60-358f-839e-732c72e0d019 | -14.72825 | -45.23575 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5cc7c51b-a8bf-3b03-9c10-b74e24425b74 | -11.94588 | -43.9213 | 2025-09-30 03:28:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a044d74-9dfc-35a5-a773-41ac32ae1c98 | -15.05381 | -46.96644 | 2025-09-30 03:28:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bec19a73-a8d8-354e-9fad-8f1482a09396 | -14.73425 | -45.66496 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7351fb05-4797-3bb5-bca2-429c597dbe85 | -11.67133 | -44.28835 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67e87727-a13d-324a-bdfa-15788d8efc8a | -14.08277 | -44.09373 | 2025-09-30 03:28:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b75f973-11fd-30f6-b89f-501a09e00196 | -10.53652 | -43.63964 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e79c3af8-446c-3427-b3fd-1bbb5bc23738 | -15.17113 | -46.407 | 2025-09-30 03:28:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aec6d0a1-9c06-3441-9bb3-cd7c000f89b3 | -12.87949 | -44.68716 | 2025-09-30 03:28:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f07b0d7-de1e-3b1e-bba2-6d7a542f25a4 | -13.23116 | -43.37561 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c9b88672-13c1-323d-a4df-7828cf620d89 | -12.88603 | -44.68858 | 2025-09-30 03:28:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc3de766-2f09-3c2a-b081-2e8561610d93 | -15.0684 | -45.06401 | 2025-09-30 03:28:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee8480c3-c4c6-3bfd-b6e6-f0b5c8d64a6b | -11.44086 | -43.50898 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30e0a685-4752-3b63-9ad5-291918cd941c | -11.45669 | -44.99607 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 73544833-a56d-386e-967c-302bd5497e31 | -10.18501 | -44.88876 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4ba4324f-b48f-3c39-b278-6a35b6f0e979 | -13.03239 | -42.80895 | 2025-09-30 03:28:00 | NPP-375D | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| b1ab78fc-f1fa-38c3-9f86-d2addb4c8668 | -11.6803 | -44.3032 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c215910c-6f38-3f2f-9436-cedffbf53caf | -11.71685 | -44.4423 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3ef4b93b-7db9-3d04-b364-203eb9cfcd8f | -13.23753 | -43.3733 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e92eb640-6bac-372b-bb76-55aaff1c1b2b | -16.1632 | -40.6846 | 2025-09-30 03:28:00 | NPP-375D | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0a228ae1-14bf-3fed-ad11-ec97f056acc7 | -11.49401 | -43.51691 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4770deec-ad13-3977-8836-7da05c518d26 | -9.57549 | -40.34914 | 2025-09-30 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1ee19b28-574b-35ea-ae35-4fe3863036a9 | -13.62753 | -42.5353 | 2025-09-30 03:28:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d39b96ee-5662-3040-bc15-6a78323ecca7 | -10.53683 | -43.64122 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aab352d2-3d79-31d0-8e4b-36748c7527ab | -13.63211 | -42.53778 | 2025-09-30 03:28:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af856051-7324-3209-9bcc-5c98aa584c8b | -15.93005 | -43.31348 | 2025-09-30 03:28:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9208a1ef-31ae-39b2-bece-6b52ad5c30bb | -12.9558 | -46.41063 | 2025-09-30 03:28:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3b4db47b-3110-3b5b-b5e6-f838eff26fe1 | -11.42575 | -44.90636 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5f7aa94-e107-3f0c-ab00-090d41c89840 | -11.72464 | -44.43796 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 083bcc13-662f-3df3-859f-93f3737e5f6f | -11.48551 | -43.51398 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39b8de2f-fa69-3cdf-9847-fba2910531f6 | -11.49802 | -43.51668 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3550f1c8-3c9a-3cf0-9765-ffeaf45348da | -11.66959 | -44.28912 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3987f529-d704-3ad9-9468-1481ae75a153 | -14.71831 | -45.67348 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e45205b4-efdf-3747-a299-a729f42830a4 | -15.16812 | -46.4105 | 2025-09-30 03:28:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ee834267-a6e6-3f42-b111-7944d68e0364 | -13.00703 | -44.11634 | 2025-09-30 03:28:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd0d1260-51de-362b-a177-f90e855c8198 | -11.6821 | -44.30252 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0c02a5c-e7da-33f8-912b-4ca35b882691 | -14.44304 | -46.36148 | 2025-09-30 03:28:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fdc8780f-89a0-3c36-bf6b-0ee878d16728 | -10.18372 | -44.89531 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 49c7cfb0-fe94-3593-8e95-2ebf3c679861 | -9.57486 | -40.35247 | 2025-09-30 03:28:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 7c37be5d-de04-3735-814a-4610bd416d90 | -13.23059 | -43.37654 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4e8c36dd-10c4-310c-a077-c5f9f798c209 | -11.72537 | -44.45007 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| af374ed5-c39d-35af-95cc-dfe087ae4aa7 | -11.75076 | -44.74469 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa5a0dbb-034e-331c-a02b-580b26efdba3 | -11.42477 | -44.90976 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3fa6ee8-da02-372c-b83c-1df0b3e75681 | -10.81166 | -45.3704 | 2025-09-30 03:28:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4cdb793-1703-3cfa-8cf3-04ed3a8024a1 | -13.66238 | -44.31469 | 2025-09-30 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b2f88504-76b1-3aea-b823-0841115e0090 | -11.42834 | -43.50639 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac201d13-1b90-357c-bb49-1b1bf165990a | -10.18628 | -44.88237 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 726e6fc8-37e5-3edd-82e5-55160e9c0410 | -11.44611 | -43.5153 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bbc0298c-f073-3c6b-a90f-51880369a52c | -15.32896 | -46.27195 | 2025-09-30 03:28:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57321f09-30e7-3794-a90f-f2b5e08ca0f2 | -11.72114 | -44.43712 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3542bbff-8183-349d-a40a-8e64525a996b | -14.64717 | -46.97278 | 2025-09-30 03:28:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 638dbfc8-c5c5-392e-9bca-a30f7e44e8aa | -15.77457 | -43.6767 | 2025-09-30 03:28:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5fc58b0-e5b8-3877-b6c2-2a4ca59ad6f0 | -15.06885 | -45.05865 | 2025-09-30 03:28:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9f7b9c4-7768-3342-825d-2c3bf7858032 | -11.71997 | -44.44287 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 613d5613-766e-3573-810d-905e58bff41e | -15.07403 | -45.06584 | 2025-09-30 03:28:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cec59c97-e163-34f1-8cb0-20c05615a66d | -10.18764 | -44.90171 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1e287148-4ed7-3e0d-b559-39a713c2042e | -11.43048 | -44.95138 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a73ac802-54f7-3327-b5e6-e93c133fc5ca | -15.77748 | -43.67583 | 2025-09-30 03:28:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 311f55ee-e630-3f0d-975a-10305b772d79 | -11.48979 | -43.52529 | 2025-09-30 03:28:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 527ead9c-6faa-3a49-aa74-92fffce9d109 | -13.66339 | -44.30986 | 2025-09-30 03:28:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 71a250d6-a2e1-3102-b522-0bba28a1bf10 | -10.53034 | -43.64032 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f9c34a1-0170-3363-9199-05c9f47be17d | -13.2366 | -43.37789 | 2025-09-30 03:28:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e32347bd-07cc-3448-b8e6-2be84cf47999 | -10.19582 | -44.89701 | 2025-09-30 03:28:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0422bdaf-3c28-3b85-b28d-3b8a4190d61c | -11.41941 | -44.9013 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 41f5c655-62ab-31e5-9529-855b26b0d8b3 | -11.43672 | -44.95549 | 2025-09-30 03:28:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c93c783d-5c9d-391c-a698-ac05ab6da813 | -10.54434 | -43.63706 | 2025-09-30 03:28:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cad90dc7-f850-366d-a5dd-d12f670f9107 | -14.76373 | -45.75518 | 2025-09-30 03:28:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b75bf51d-6f8b-3c59-8c50-14e8b481fd47 | -11.72655 | -44.4443 | 2025-09-30 03:28:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README18.md)
