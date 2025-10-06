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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aca38e24-efc6-3a49-855f-b75681f0af4a | -13.77181 | -45.73819 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c833eb46-5f23-31c1-9742-478cd94254e4 | -11.71028 | -44.29798 | 2025-10-06 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5252280-0dbd-34ea-b8fd-8095ee11b674 | -12.22385 | -44.23777 | 2025-10-06 04:27:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2992e137-a244-3943-8f83-f1dddb86b442 | -13.36213 | -47.24309 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a3b91f12-d60d-3d23-a180-db05e129a0ad | -11.16373 | -47.16412 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3ba1c4a-7070-307f-a308-40ba1625dcab | -10.61622 | -48.6656 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b32600e8-9727-39e3-8a3d-cbf976561ef6 | -13.27221 | -47.58352 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56a4cb62-f7c7-3b12-baf7-c1ba583a3de1 | -16.34787 | -47.05404 | 2025-10-06 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3594ff6a-b0af-3d5a-bfbb-e9808a344096 | -8.6249 | -54.97727 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ed605df8-8501-3355-afae-9f5409b53188 | -13.37232 | -47.57497 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d23697e0-e2e5-39cc-b9ae-b4616b0e445c | -16.01525 | -50.82475 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d77d9715-1716-3eb9-84ad-d6164bf04898 | -16.02865 | -51.04274 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0ee44efe-dd82-3758-8fd8-f374ce37419f | -13.55627 | -47.2413 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78479b63-cfe3-314d-b0e9-6ee6b936c898 | -16.35671 | -47.05155 | 2025-10-06 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12df2cf3-3a5f-3557-9a1d-c87d4f9f3025 | -10.8066 | -48.81565 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4e8b9dc5-bc58-398d-8464-3b754c5409de | -10.4374 | -50.36036 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db166c2c-425a-3072-ab9a-c10e0efe807e | -12.92557 | -45.06659 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03b107ac-4eb3-3549-afa9-8ead159f9031 | -15.79443 | -46.25231 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a42c4dce-7163-357c-981f-51581d6be910 | -13.37179 | -47.6002 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c0af842-bc7d-3a73-a924-d67f9d97c777 | -14.70625 | -48.37681 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f4f9c0c0-0e5f-370b-9e6d-cc2a55d410a3 | -11.52515 | -47.68076 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a55b93d7-3b44-391f-a488-354c57493542 | -14.55956 | -46.63547 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4823cea1-b911-3653-89e3-94b6168ab0e6 | -9.90869 | -49.95602 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f060c1fc-48e7-3bbb-8d95-5ca9b399168e | -11.01427 | -46.52507 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| c83531d5-653b-3381-9259-80a4af67f00b | -12.78918 | -56.96078 | 2025-10-06 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90343526-a095-3775-a320-0fecb16a7cb7 | -8.15623 | -54.85024 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43a408ac-4aeb-3226-9b56-662ec6947fef | -15.02446 | -55.5542 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02997a41-a320-3790-8509-f63a14be0f5a | -11.01248 | -50.67634 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df3e55f8-5bdf-32e5-9396-902c3da519d7 | -12.90946 | -54.73441 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e77d4ee-82b3-3219-b7b6-96054fef48c9 | -15.24433 | -56.7595 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0335d1b2-14fa-3c84-bed9-f267a871c56a | -14.66009 | -48.36917 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 39d00090-df6e-3db8-bddd-31c8d145d5d0 | -9.33508 | -54.51748 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4abcfe15-690e-333e-a7f9-7714d6caabe3 | -15.23884 | -46.67193 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 945c87dd-7aba-3bf1-ad1e-9986a6b09f41 | -14.615 | -52.50665 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3d318ba-eb26-35b5-89c5-c2807ba1926d | -11.02761 | -46.54893 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1e499593-aec7-3193-85f4-5fee990a5f5b | -10.60906 | -49.14662 | 2025-10-06 04:27:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b561cb89-d11e-3957-9c65-271c18a4ab2d | -8.61791 | -54.98765 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75f7590b-33cf-35ef-a124-a0e768ec758d | -8.61579 | -54.96242 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 59af138f-9c9f-35fd-b9af-de88301d8290 | -15.3117 | -47.96381 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9189112a-e3bd-38a9-82c8-732835fa56ac | -10.41371 | -48.10059 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01e74df7-df6a-3e2c-a342-6b3e6f49fae4 | -9.79275 | -48.27999 | 2025-10-06 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fce8821-7974-3f71-9678-a4df6ce0657e | -15.94544 | -48.61265 | 2025-10-06 04:27:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 387cc52c-8f98-3ff3-8ec9-c0a272e074b1 | -13.28712 | -47.81339 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89fa40dc-2eaf-38bb-8ed7-245a47eb5b85 | -14.55846 | -46.66562 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02c555ef-52e4-3dd5-ab3d-f2c2303a733d | -11.87304 | -57.81936 | 2025-10-06 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2e26cd-d6e8-30a8-b243-f2068ab98c12 | -13.34924 | -48.0476 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 48e08697-37cd-3a77-9aee-2bde2116a33d | -15.31248 | -47.31615 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b28b6d12-bf39-3602-b01c-7320f011cf93 | -11.83833 | -45.10101 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8bc56443-f84f-3abf-8a7f-811f252abfb0 | -10.32509 | -50.26999 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bec9a25d-c0c4-3910-a56e-713f1b084511 | -11.79942 | -45.12374 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fabc2225-7a5a-3a55-b0f1-c81a48cea2f9 | -13.13148 | -48.00444 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4aaa08c-21eb-39e2-8b5c-d2c44b407500 | -12.2471 | -47.85202 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d89a6ad9-9597-304d-ae63-1c0c0572fc29 | -14.3254 | -47.65736 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fc14be14-43bf-3d3a-bda7-87267b246e63 | -15.56995 | -52.45963 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 662e6bfc-164c-39fe-b668-15cecbec9386 | -15.209 | -46.39693 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45cb9313-14ce-3bda-945c-8f4b360a6c47 | -9.07732 | -59.02729 | 2025-10-06 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 611c7031-bc7f-3647-8b70-271a1712487c | -13.37779 | -47.53946 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 195446a2-02bf-3d1f-877d-7047fd14d418 | -13.56814 | -48.14835 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e28e9e74-0ffe-33ee-8f92-99cf2effc622 | -11.26117 | -47.78085 | 2025-10-06 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6f30bb85-2464-3429-b11a-76e0148ef520 | -10.35775 | -51.23182 | 2025-10-06 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b2503f1-50f3-31bc-80ce-072ff237136a | -13.26515 | -47.84583 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2ea79679-5154-3e3f-91a9-d9c907810fb8 | -13.43996 | -43.58559 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fad9c14-52e6-331b-8663-310eaaba4457 | -13.6312 | -48.71856 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7f97bd9-df13-3ef1-a53e-87f9b7a4524e | -11.06726 | -47.90791 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 137e3a07-942a-390c-89df-788fdacd08be | -11.5378 | -47.68639 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d8bab23-87c9-358f-b6cc-586b295f07bc | -14.69595 | -48.2916 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0801e240-83b3-37bf-b821-724e5af91ca5 | -13.36135 | -48.03512 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1ec9ed9-b18d-338e-9c91-f6ec0359906a | -13.32724 | -48.05846 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c56ccd64-5b9a-3577-82ae-a077e43ebf12 | -14.68535 | -48.38062 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d38f8a92-4538-3023-a7b8-73428cdba182 | -11.8046 | -45.08859 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6164d9fe-fb4a-3e20-adae-00d3db660629 | -14.85418 | -48.75519 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af303656-28e1-3b15-962e-1155f2b9ddbc | -9.37075 | -45.91221 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 792b2638-be5e-3829-9185-2a37c590afe4 | -10.62677 | -48.68572 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b64c75-5972-3a18-a772-83dc074393f3 | -8.63245 | -51.08319 | 2025-10-06 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3a0a360-e556-3275-a390-bc1960a30de6 | -15.56105 | -46.836 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ba41b60-a286-3086-b1f0-0f7143a80307 | -15.13846 | -45.74734 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57de5d8e-2660-3497-91be-a77fe058326c | -11.00672 | -50.71045 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0a1c2ed-5e6f-31f2-a396-7dc6fa9c90a9 | -15.57079 | -52.45477 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b76898db-a25f-3848-bd07-eaf67f8d14d9 | -13.62788 | -48.71803 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f60eea0b-e3b5-3bf2-a4ca-7773e12a86c0 | -11.70634 | -45.42121 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72388ded-cf6d-3322-8207-2055449afc96 | -16.01266 | -50.84018 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72f3da89-bf40-3d42-90b1-a25e7f1c738b | -14.63141 | -52.52489 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 853d710c-39e2-33a9-b494-562b64f0fb6b | -9.34267 | -54.52217 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d81f6831-facc-3096-806d-ebd67ff55038 | -12.49195 | -45.55704 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9d54938e-90af-34c5-826a-5c0028ec6206 | -14.69265 | -48.29105 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ade21f8a-bc26-3bda-a239-f458437bdf33 | -14.71289 | -48.3561 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c38dc4c9-b62b-3c09-b1d6-a82957c701fa | -11.48562 | -44.96967 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3e67827-8ea8-33b3-afd5-f9c0bad4a44c | -11.90471 | -46.21749 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95141ab6-5a38-3b5e-8f11-55856180e544 | -8.61813 | -54.95845 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6802413b-9720-3dcb-9813-4e33ff2e096e | -13.37655 | -43.62078 | 2025-10-06 04:27:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 788042a9-0bb1-3d7d-b996-5c688a4084f8 | -14.65353 | -48.34632 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 980d1d0b-f85c-3db1-be25-9d7b99f24901 | -13.68743 | -48.06002 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b81e47f-69e5-3973-af04-c1a9c85ea113 | -14.35022 | -47.71584 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2598e26-9bac-3a1c-8958-fc0ad90d5510 | -10.04737 | -49.20587 | 2025-10-06 04:27:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f351136c-ab98-3a1d-8eb9-83a024ae7b86 | -8.62071 | -54.96336 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2be97083-5c8d-3a2a-8614-b6954efd479b | -13.26785 | -47.63334 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d142937-ec91-3edd-8c62-6e74db809335 | -9.62787 | -50.55124 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e277f7b-d2b3-368b-8c96-429d007109e4 | -13.07661 | -47.92331 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8826d14e-6666-35db-b550-e82fe4d8c9a6 | -11.64133 | -47.74244 | 2025-10-06 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed27ca31-a22a-32e5-b9d3-62092714d630 | -15.57097 | -47.29023 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README35.md)
