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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e46e281-e5bb-3cc8-9c4e-76cf3fbfe846 | -14.48905 | -46.6281 | 2025-11-16 03:49:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9fa50f3-106a-34c5-b758-5c128a11e323 | -15.46012 | -39.23865 | 2025-11-16 03:49:00 | NPP-375D | SANTA LUZIA | BAHIA | Brasil | 2928059 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 91881ec0-ffcf-3c60-91cb-87d308719587 | -12.85335 | -46.45486 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77a73b84-8b1b-3a4a-9121-e240ee473840 | -10.70079 | -44.52195 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c50f5099-a305-306a-b5ae-dde67e8c6df8 | -12.39793 | -47.56419 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e2dc4e70-c4e5-377f-af6c-8df5cde651f1 | -12.20839 | -49.55148 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4a03ab2-12b5-300f-9dfc-9717f72e757d | -11.99988 | -49.27696 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 88456dd3-75d7-3c39-8ed3-0c968c0aabd4 | -14.49055 | -46.62765 | 2025-11-16 03:49:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b167c6b8-2969-302d-9bb4-173cbdfb2c8b | -12.85368 | -46.42439 | 2025-11-16 03:49:00 | NPP-375D | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5a5e8ef-c054-357b-9ac6-2439c10af169 | -13.97876 | -47.0541 | 2025-11-16 03:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4951dc28-8502-3e98-a881-88135c4ce4c8 | -10.70159 | -44.52248 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35fffa2a-99f3-3c66-8a9b-9b1c57233cab | -13.55862 | -44.27781 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63350d5b-94b7-3bf5-97c7-68f7405368e9 | -12.68174 | -47.16685 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cf943be-f1c9-32da-a1d5-cfb4a2d625c4 | -11.41759 | -43.33348 | 2025-11-16 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec749226-3c3d-3391-ad06-3d95a8d305a7 | -13.75689 | -43.14425 | 2025-11-16 03:49:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad9436d7-eb59-3d07-b948-8298f6eefda3 | -11.80574 | -45.55136 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f5aaf00-b405-3179-a321-2e3886d929af | -12.65507 | -46.74948 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff9f1817-5ba9-3bdd-87d6-b6b4af1dd5b7 | -12.66452 | -47.16328 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ea80092-e923-3c33-88a5-3ced1bf8ca6a | -12.39704 | -47.56859 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8526158-9084-3977-8bf6-444fa70e82d3 | -12.20175 | -49.5499 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f47364a-534b-3cab-bf50-650d86203368 | -12.66205 | -47.17541 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7338adf3-1a7f-3da3-84cf-8edd00ed11f2 | -12.6627 | -47.17348 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac65e832-3146-3cab-a96e-fad7d441ab8e | -12.8037 | -46.44675 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38cd93ce-d945-331a-a109-521ba287a7fb | -14.58331 | -45.22002 | 2025-11-16 03:49:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f2f2c8a0-77d5-3607-a78d-84157b266bd3 | -9.71832 | -48.90122 | 2025-11-16 03:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a9d6fcb1-7e9b-3668-a359-0f991c972b1e | -13.55308 | -47.3881 | 2025-11-16 03:49:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5f206423-0570-313f-b6bc-5500d2a0cdef | -12.06159 | -46.97636 | 2025-11-16 03:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c396d3b4-6a2a-3e2c-a940-0c017285ce66 | -10.70522 | -44.52604 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 738d983c-8e7a-392f-abdf-466f59363903 | -13.97405 | -47.04861 | 2025-11-16 03:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eeb6a9e-6c73-3211-a892-b51c5f297077 | -10.52791 | -44.83478 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7da71e59-4481-378b-bbca-4bf4c122f433 | -12.06415 | -48.20943 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d65acc99-942b-3a51-a4f2-c2d620dabcc4 | -13.82073 | -43.18758 | 2025-11-16 03:49:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 56f40e14-b137-3121-8cfe-66ee07ef8695 | -10.66486 | -49.35833 | 2025-11-16 03:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0662c026-3990-32bf-9ad5-52ef7bc01cd6 | -14.64131 | -46.58467 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0811291d-e94b-3a70-9c11-3c4e0660a204 | -12.00105 | -49.27123 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 6ac0f038-45aa-3146-af0e-f8c57ff27e30 | -12.65693 | -47.17239 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a864a860-39bf-3ac1-9841-4f29e390869c | -12.66781 | -47.17652 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa0635dc-360c-30f4-ae99-96c1f4568f35 | -10.66233 | -49.37077 | 2025-11-16 03:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7847b804-4631-37f6-b652-78f62e6664bc | -13.81691 | -44.45089 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a29ad712-686b-3c4d-8c84-90c45f0148f0 | -10.44855 | -45.08396 | 2025-11-16 03:49:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2e4118e-2294-3753-aa0c-cffc5fcb344b | -14.66264 | -46.58925 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f8769d3-e7b7-30a7-9e7b-57d148322f0d | -13.71017 | -43.66132 | 2025-11-16 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9f48ecd-9054-3de1-bd4b-12827ce032d0 | -13.9762 | -47.0536 | 2025-11-16 03:49:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f598c25-69f7-3702-b2fe-71bd990d9799 | -11.16526 | -47.46262 | 2025-11-16 03:49:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 88c4f5f7-0120-3d4d-962e-c5571c8b4799 | -14.05771 | -43.12525 | 2025-11-16 03:49:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f0ad4b97-c4f8-3ba4-acc6-ad7cac24483c | -12.6752 | -47.16961 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35d8b0c9-254e-3202-a969-e08f5dd97af8 | -12.01303 | -49.27988 | 2025-11-16 03:49:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bc867039-83b9-3105-b800-87009aa391ee | -12.06836 | -48.22042 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b75f8649-5320-375e-a8e9-2b42d6f61111 | -15.37589 | -45.64758 | 2025-11-16 03:49:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 00ff69c9-ac00-3c21-baff-a13df1af4ee4 | -13.38385 | -44.37445 | 2025-11-16 03:49:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ede532b8-cda6-3071-bb79-bde4c6549234 | -10.54452 | -47.92252 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cfff1d96-cf4b-3204-b7f7-5631e49f9d52 | -10.80286 | -47.99653 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 116420d2-d796-384c-b9cc-b41ffcfc946f | -12.66765 | -47.17874 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b41dbf04-d8c9-34b2-a526-959ed5d7dff7 | -11.96289 | -44.95015 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1f56913-11ce-3465-8403-aa9f538ca4db | -13.82164 | -44.45177 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa971ebb-fff4-3469-b83a-430dc6512720 | -15.47679 | -43.18828 | 2025-11-16 03:49:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5055d39b-6b19-3d90-bc68-ac4b562fc041 | -12.002 | -49.2841 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| c4ff31d8-b4bb-3851-a321-529c79747385 | -13.75598 | -43.14457 | 2025-11-16 03:49:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1ae8fc40-2435-30a0-ba9a-7959eb3508e4 | -12.00524 | -49.28436 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d3088339-5d66-3545-8e2e-502dce7acea3 | -12.06216 | -48.21919 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 33057abe-aa1b-377f-ac46-73fd4c239299 | -12.68071 | -47.17307 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0bdc6f4a-2ea4-3163-9559-38b0c5f66d3a | -13.71466 | -43.6622 | 2025-11-16 03:49:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30bb3a4b-4eb9-3d58-bbad-cd08cfa7d344 | -14.65087 | -46.59245 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85b8756f-61cd-3b0b-8598-55ef731ebbad | -10.66361 | -49.36448 | 2025-11-16 03:49:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 318c699a-cf0c-3b0e-84b4-a2d06f67b083 | -13.81169 | -42.54604 | 2025-11-16 03:49:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| a79f46f9-2494-3690-bcc9-e9f19b736fae | -10.54883 | -47.99993 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b71fec5a-3350-308d-ba17-7f3d3b1923f3 | -10.63004 | -44.60021 | 2025-11-16 03:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 813d6e7a-d890-34ec-8fc9-a277a30444b2 | -10.71078 | -44.52407 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8132023-5d15-3df7-bb77-88565b60f709 | -12.84885 | -46.42012 | 2025-11-16 03:49:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f803a0f-f446-3eff-88b7-c3e116fbc80c | -11.97199 | -44.95739 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44e96a8a-0b6d-3930-8749-60ce28937002 | -12.66925 | -47.17056 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd1e177a-e253-38aa-8b92-e404287bc485 | -14.68119 | -46.55219 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d1356b77-14a3-37d5-9ef0-caaaa285e9be | -11.15996 | -49.44598 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d10c4da0-9c67-3adb-946a-4a517adebb04 | -10.53188 | -44.83545 | 2025-11-16 03:49:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0df10b61-3ff3-3805-bfd2-6f452145bfef | -10.53748 | -47.92527 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 18c6629d-53d4-384e-ac14-ec8feb61df26 | -13.75261 | -48.67458 | 2025-11-16 03:49:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 790b4e76-eb06-3ccb-be74-405e848b0b65 | -15.52934 | -44.38236 | 2025-11-16 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5bdb7b4f-7e4c-3d51-9195-170e65ab67ec | -11.84638 | -47.60126 | 2025-11-16 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| baf76941-f34b-3e44-a9dd-9ecdddfae72b | -12.65269 | -43.25012 | 2025-11-16 03:49:00 | NPP-375D | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8059557e-e893-3543-abc7-f3bbb5960580 | -12.79762 | -46.44865 | 2025-11-16 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80ba01e8-dc42-376c-9ad2-c9454a53ea09 | -12.69026 | -46.79388 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 116bc9ee-13ba-3b5e-b2db-3076bdb0037f | -11.82944 | -45.53604 | 2025-11-16 03:49:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 629a06da-87d7-33de-ac3f-693d0748d95c | -12.40476 | -47.56089 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b5a50ff-2022-3080-9821-27555ef224b5 | -12.00449 | -49.27239 | 2025-11-16 03:49:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 26e77fcb-3ac8-334a-89fa-f0a09793015e | -12.20613 | -49.55158 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cdb67cb-7673-3b4d-86d4-1b62890c03eb | -12.00328 | -49.27808 | 2025-11-16 03:49:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9776a133-622e-3445-abec-ce38d390bff1 | -12.6558 | -46.74569 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0183b1ca-8d61-32b8-8ca7-5cd2e53ad4c6 | -14.6798 | -46.55918 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7143e00-22ab-3617-b012-2b3a743c1324 | -13.81787 | -44.44582 | 2025-11-16 03:49:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4fc40064-7572-3e72-ac66-4262ce0f9647 | -10.70579 | -44.52298 | 2025-11-16 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 377ca5ec-16a4-3b98-90ee-225af768513d | -9.71639 | -48.90108 | 2025-11-16 03:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b4e4144-e7c3-3202-8f66-fd78fdafacad | -12.40652 | -47.55219 | 2025-11-16 03:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06e82d43-2a4f-39ac-9218-d2b547688a84 | -10.79947 | -47.99692 | 2025-11-16 03:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc63f5c6-dc99-3f22-9b7f-fd16c371b756 | -12.69664 | -46.79112 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7f756db-f8b2-3d1e-89a2-74f259e71066 | -13.37115 | -44.05761 | 2025-11-16 03:49:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21ee0358-f37b-335b-84d9-1cdf135c00c4 | -12.66845 | -47.17462 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e98975c5-6f9e-38fd-bbec-84267e527614 | -12.06934 | -48.2156 | 2025-11-16 03:49:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff93324f-dd20-3ecd-956c-25003d3f254d | -12.67655 | -47.16381 | 2025-11-16 03:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 77ffd06f-8954-3028-9ded-436835e99f9f | -14.64746 | -46.58175 | 2025-11-16 03:49:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96139832-bb66-3389-afbc-f75d2d9c3582 | -11.96232 | -44.95319 | 2025-11-16 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
