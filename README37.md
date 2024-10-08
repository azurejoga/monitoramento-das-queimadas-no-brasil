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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78940f52-2b5d-3141-b9cf-694ebf8aed46 | -12.1608 | -47.76684 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 14efa033-7b4f-368e-84a9-3319d050d824 | -12.15656 | -47.76504 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b80afde3-c519-3610-843a-d7abe1bc7f47 | -12.03855 | -46.8583 | 2024-10-08 03:42:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf953482-0657-327e-bf7d-15f71c9116a4 | -12.03287 | -46.85712 | 2024-10-08 03:42:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 522fdeaf-2d18-3610-b048-bee60be8677c | -13.17717 | -47.99654 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51e52240-1d80-36c2-923a-e022257d36e3 | -13.17587 | -47.99266 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32903ddb-e22b-3af6-9c36-224dbd4418dd | -13.1749 | -47.99754 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eca57fae-97a9-31a8-8b75-e4a73008322e | -13.17113 | -47.99556 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af5dc5f2-d418-3e01-9247-1e667f0d85aa | -13.17005 | -48.00074 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92f5e651-641f-3385-84d7-6bd47aac5d80 | -13.16886 | -47.99654 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a84d7fe5-123f-3546-81b3-9036f89513ca | -12.46523 | -47.31262 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4ab93ae-6057-3f9e-b533-e863892056e1 | -12.46461 | -47.31193 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ad68936-d03d-3ffa-adbc-143016f529d2 | -12.46441 | -47.31686 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8742c21b-a738-310d-a95c-76f7b6f889e6 | -12.46375 | -47.31617 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f287266-7a09-31ae-a92d-887bd8d678b4 | -12.45858 | -47.31572 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9c90aae-da47-344b-981e-efebd0ff21d5 | -12.45793 | -47.31504 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1413ee74-c88e-3b67-84b0-7799b2034d33 | -12.36225 | -47.10305 | 2024-10-08 03:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37f9dda0-f560-32f3-8b59-3b0f2b55611f | -12.35813 | -47.09355 | 2024-10-08 03:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f0e197b4-811c-30e5-ab21-270d2c0b983d | -12.35732 | -47.09768 | 2024-10-08 03:42:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 15b4addc-7862-3cba-a613-19b05fedeb09 | -12.35652 | -47.10178 | 2024-10-08 03:42:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| aadc4d97-6277-3b7e-9b98-12313ab1ed59 | -12.35159 | -47.09642 | 2024-10-08 03:42:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c4144026-ce8b-328d-bb05-3be8c4f3b621 | -12.2825 | -47.64587 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d609672d-f3fa-336e-8bb5-6e4909b439af | -12.28008 | -47.64557 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3dd23542-afd9-3c7d-8f46-732883fd816c | -12.2775 | -47.64 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd4d5194-5147-30ea-821c-1e9790cdb767 | -12.27659 | -47.64446 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea3b662e-9e12-3882-8a17-d1443f26c158 | -12.27505 | -47.63965 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed28d090-e463-396a-87ce-396927358659 | -12.27418 | -47.64407 | 2024-10-08 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97a6dc1a-a1a8-3fd7-afb7-eb47bd3d3f45 | -20.37242 | -48.86224 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 319.0 |
| 86585d69-374f-3e8e-9933-c9b4e99bda2d | -20.36956 | -48.84872 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 74f25cfe-21ec-3ab2-a37a-138d7415f002 | -20.36685 | -48.85674 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 233.5 |
| 26d500b8-3875-304d-bc95-62e447ccee09 | -20.3569 | -48.85367 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 05ff1d64-0ff7-37d1-ab3d-ff76943ff728 | -20.35145 | -48.8521 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 25ed866f-96ec-3457-9adb-d6c22c120eae | -20.34792 | -48.86833 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3dc9c7b-09ad-30aa-b9f6-0e864bd9bfa7 | -20.37296 | -48.90728 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24b2b7bd-ae33-3159-9295-0d1897ffb18b | -20.37179 | -48.88652 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 3ce4aaa0-ec70-3bbb-87ba-4b8ba0593f44 | -20.36956 | -48.90223 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd163c68-c900-3a02-8322-1dfec8c85423 | -20.36921 | -48.89806 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4def1c7e-876e-3f4e-920a-b3de709d5ba4 | -20.36745 | -48.90588 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca7945e5-81b0-3a9c-b229-6d491aae8e8f | -20.36704 | -48.91389 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 30b892cc-39ec-3dd0-a594-d3b8187b0b60 | -20.36544 | -48.88894 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5304e617-ce53-3feb-ba91-e4fb5d99fe4c | -20.36493 | -48.89681 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0f31119-702c-3b1b-9da9-43779f1f73ef | -20.36323 | -48.90468 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe50be7-d119-3ba7-97a9-068804782322 | -20.36238 | -48.9086 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8ffd0c4-b8a2-3c99-acdc-ba835a235fde | -20.36196 | -48.90444 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e97f9e9-ecca-3c25-8dde-4dca65e9146f | -20.36191 | -48.88399 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7a2fcbb-29e8-3169-9bc3-0bb7461fcd9f | -20.3616 | -48.88013 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c09d4246-02b8-346e-94f4-4dcf687296f1 | -20.3611 | -48.88773 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d14dc673-532d-3c18-989c-64454322292c | -20.35934 | -48.91615 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd178da3-65c0-301e-9a61-67e0cdfe9e3c | -20.35735 | -48.8991 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 207ba6aa-c6f6-3fd0-933d-2bdd077cc752 | -20.35393 | -48.89399 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f61a1700-35e2-32a2-bf01-fcd95412e61f | -20.35309 | -48.89787 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ecc6174-c4d5-3175-92bf-94dfa3dea85c | -20.3891 | -48.88698 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c8eb2e3-2a3e-30f0-b41d-31f148d04eaa | -20.38826 | -48.89075 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15550d26-9c1a-34a3-9a74-8c0909898d47 | -20.38742 | -48.89453 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00bb8950-7095-38aa-a143-d8873ab0bd21 | -20.38656 | -48.8984 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06e65997-2e58-3d6a-af83-7913c8ff27b2 | -20.38568 | -48.90234 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7dac9f2-7a4b-3bdc-9795-ce7282175c58 | -20.38472 | -48.88577 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e927062b-0534-37b7-9837-5e48db50b3c5 | -20.38391 | -48.88953 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2cd2b28-cf3b-3b60-9fbb-c6fa2cb6b076 | -20.38362 | -48.88555 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f7ceaef-82d8-372e-8666-378a287adec2 | -20.38309 | -48.89331 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| def0e0ea-06af-3288-bcc1-8a719608881c | -20.38278 | -48.8893 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8313a8fd-1830-396a-8421-55200df54f7b | -20.38226 | -48.89718 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a9899d9-6832-3bd5-8968-b0c8286d01b4 | -20.38194 | -48.89307 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6888b7fe-5cd5-39b9-a27a-550fc5b7ea31 | -20.3814 | -48.90115 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5026a737-9d20-31ca-a86a-f00d103bb80c | -20.38108 | -48.89692 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 024e4ce4-2e93-3b6e-96f1-c3bd316fa53b | -20.3802 | -48.90088 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ab04e42-e455-35ae-bad4-136342541e1f | -20.38004 | -48.88059 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 83c8493b-8ae3-3acb-b326-924b6a630863 | -20.37924 | -48.88432 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df0738ba-a953-3812-9139-a003d563d32c | -20.37843 | -48.88807 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2925dd9-62c2-3c62-8ebb-1942244c12d0 | -20.37813 | -48.88413 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0439f6eb-ad89-3b8e-9670-b77901d8fd59 | -20.3776 | -48.89188 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79103084-4663-3dac-a380-6181106bd604 | -20.37729 | -48.88787 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 8e581e23-b259-3f35-8d2d-e75d8cf2b76c | -20.37677 | -48.89574 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d17c96ce-d15d-3ea7-b237-06efeba8f6b0 | -20.37644 | -48.89167 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1380fd7a-ce5f-36e9-90d4-d8c2f9603cde | -20.37591 | -48.8997 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e7396ec-8d4d-3bd2-9b59-ee4b2127a676 | -20.37558 | -48.89553 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a558fcac-4bfd-34ab-b978-e01701b2c3f0 | -20.37506 | -48.90367 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9982053-d237-325d-86fd-f00f13a64690 | -20.3747 | -48.89946 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c916bbe-1909-30eb-bff5-50bffa942fed | -20.37422 | -48.90754 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7955c042-75f9-3b29-a91b-049ba1aea972 | -20.37382 | -48.90341 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aace4e2-0167-3f77-b5a9-fc65e8c87887 | -20.37126 | -48.89438 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f638ed2d-5e79-3bf8-b94d-66596dbe1842 | -20.36833 | -48.90198 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99ae8868-4f09-3d82-910f-cc1813faad8b | -20.36742 | -48.88535 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 4fbe2d10-144b-3162-9f69-71e523db0167 | -20.36628 | -48.88519 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 70d79b0a-b721-3e59-be23-a81b22b5c756 | -20.36572 | -48.91364 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fd54823-bb52-3fef-908f-a150d175b3af | -20.36458 | -48.89275 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6dea034-eed5-333a-9901-16abaa85290a | -20.36068 | -48.91644 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 298e914a-3f09-3f2a-a8ce-cf3d2fe4cb50 | -20.36027 | -48.89153 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7122d689-3c16-3ac7-ad00-284b1a4fa017 | -20.35944 | -48.89537 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 267abdfd-c10e-3bea-9cd0-1d5225e9022d | -20.35858 | -48.8993 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be810c44-19d8-384c-9ee6-a4669b9fcdec | -20.35773 | -48.90325 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 016d602a-4f77-3b74-9c91-e9be2131993a | -20.35688 | -48.90715 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7313baf7-1590-3031-9f07-2ad9a2772b30 | -20.35559 | -48.88638 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d0936c2-e56f-34f1-84da-3572f4628b98 | -20.35518 | -48.91497 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23f122ec-9770-32cd-9acd-4dc62574948d | -20.35223 | -48.90181 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 415e77e0-732e-3548-9b8c-e17ace227565 | -20.34621 | -48.87616 | 2024-10-08 03:45:00 | NOAA-20 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3e6b4667-0ce8-3764-a17f-330040096606 | -20.02312 | -48.91353 | 2024-10-08 03:45:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5bc11f4-3f16-363c-bc67-b8ab86f521ba | -16.10176 | -50.22984 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 14c54839-04f0-36cf-9d3a-7e9a64257b35 | -16.09572 | -50.19591 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a5163122-31b8-310b-b0f6-713c1131c1b1 | -16.09455 | -50.20117 | 2024-10-08 03:45:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README38.md)
