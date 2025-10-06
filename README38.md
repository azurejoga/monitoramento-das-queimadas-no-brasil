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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78e86749-90ae-3b4e-bf30-65228b7ad65e | -11.02815 | -46.54539 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c46f33b4-eebd-3702-bf1f-57f2c1ce6f48 | -13.72714 | -48.06994 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a83f2b14-8064-3557-b3ef-11931c717398 | -13.37286 | -47.57144 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c7e7b653-39b6-3eaa-8b0c-3d58fbf5c4d7 | -10.23653 | -52.69796 | 2025-10-06 04:27:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cfe27f9-be51-387f-89b4-30e32d445797 | -10.37241 | -47.99653 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85b08f66-51ea-3e3b-8e3b-4a5f37d7bdef | -12.91937 | -47.29154 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 20fa392a-f393-38e9-a92b-6da335436007 | -13.32835 | -48.05141 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a0c5940-ba2d-3e36-af79-3c4c321b599a | -9.15184 | -58.31184 | 2025-10-06 04:27:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84fd135f-2cff-3c1b-9888-92130ee053cb | -11.83659 | -44.9197 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a06c97ef-9240-38e6-ba8c-d583b64d2ab2 | -11.81511 | -45.04136 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a54edf6-d003-3d54-b791-b3a2e5cd2095 | -13.08155 | -47.82685 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 087164e4-ec9c-36b7-a371-de2738dd8ff6 | -12.56739 | -48.14988 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c75c03f-ff11-3d45-8b2c-471ec52817be | -14.56181 | -46.64341 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1656eeb-860f-38e5-9af6-5dda4a5f235d | -12.44167 | -50.17056 | 2025-10-06 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7de33ae6-6221-3c28-88a8-18bed4581bfd | -9.25317 | -51.81379 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08680f0d-d9c2-3d66-a3ac-97d7835ee5ee | -11.00815 | -50.67999 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd721205-65c6-38b9-8c97-8b1de69242be | -13.49428 | -47.24626 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0751574a-aaf5-38b5-8625-12c234fd338a | -15.577 | -52.44115 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 14327451-0b67-3189-b90d-0743b2653cf1 | -10.47583 | -55.59136 | 2025-10-06 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a71f626e-0653-3799-a3e3-28bb2e58215b | -17.08955 | -43.3812 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a266da7c-9a01-37e9-add4-450544103989 | -16.0159 | -50.82087 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 609754e1-f3a9-34fc-9ffc-5121535fa550 | -15.33979 | -47.31343 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec0f6950-5a26-34a6-9aaa-cefc29717a1e | -11.46371 | -51.52328 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c76d74a6-9dce-3598-8846-52b43b2a51c8 | -13.1095 | -47.99363 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81eab25c-c9bc-3af4-b7ed-2a998d4aa8f3 | -13.27064 | -47.81071 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93cbc003-9ce2-3f1d-824f-bb7854dfc4b9 | -12.31765 | -55.11832 | 2025-10-06 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a8ee7e7-f73e-3785-8ce6-751ae1d465b9 | -9.68224 | -48.20369 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c44c8e47-e7a6-30a5-a6fd-927051aee44a | -14.99142 | -49.97639 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 279f9cac-fe6e-3a22-9168-d22a562455e2 | -14.55284 | -46.65716 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ac08c803-148a-3ffb-8668-b4af20c58878 | -13.08812 | -47.87117 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f3b1c738-66b3-3672-a9e0-b6a60c9592ca | -13.0854 | -47.88873 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 872b149e-def1-39f1-8c91-194d55bddc58 | -13.63841 | -48.71601 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9fd32a2-5728-31e2-838b-ac2e971f2b08 | -13.25086 | -47.80749 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2237e39a-24e9-381e-82be-19e24a62e6dd | -16.03716 | -50.9703 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0a8f330f-47a6-31ed-beea-fa52a2ffa204 | -12.44735 | -45.5736 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8de733f8-cbeb-3448-96f5-43b12fa532b1 | -15.23443 | -56.77808 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b0337222-b2c5-3459-b35a-ee2fb6ea7d2b | -8.61972 | -54.96909 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e2c7d0c6-c4bb-3d56-a1a2-de918b599fb1 | -11.48446 | -45.05008 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c7d3ac9-bcf3-365d-a298-51c713c78d18 | -13.10187 | -47.93463 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef9db161-1107-300f-b876-66d921a9e696 | -14.64911 | -48.35286 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0f6dfa47-dfbd-3ef4-b073-3ebb0bee48d4 | -13.06264 | -47.92111 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27ad44b3-82ed-3ab6-bb4a-a3860d1bb212 | -8.6148 | -54.9681 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 237be427-fd64-38d1-a7e0-5c66ab95c0b0 | -13.05605 | -47.89841 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e54f7f27-6f51-3746-b26e-7570aa575de8 | -11.94698 | -51.47819 | 2025-10-06 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cf41eb1-4b5e-30ba-b7a2-e6c88874c2a3 | -11.07276 | -47.91597 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4e1e7d7e-f2d6-3871-9960-dbb64d5765b2 | -14.559 | -46.63918 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 679eb5c0-a5b5-34ba-8227-ad4b56c7ceff | -11.70739 | -45.41332 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 872391a0-70e3-33d3-b63f-3f71f3bef1fe | -15.37741 | -46.27757 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0f92601e-6751-35d5-8fa1-37e6209029d3 | -15.99959 | -50.93906 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61cb79a0-1e29-3957-83c5-073113b17a6e | -13.73043 | -48.07048 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 92d2e9a5-85a9-35ab-bac6-62325e323713 | -14.5579 | -46.66932 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22e8a4d7-5a6f-3ff2-8e24-d16ca31a66ee | -15.29648 | -46.32723 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 54fe759f-b0ea-3d8a-b5c2-58dcb90ecf31 | -13.63177 | -48.71497 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d04f4aa-57db-3128-9ddd-2b75fac496de | -15.55823 | -46.83173 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa5bad21-96cf-30a7-bdf2-846b36f8f574 | -13.26955 | -47.83932 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba18259f-3769-34a2-baf5-525ef3532304 | -14.74624 | -54.67096 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d82db7f-e96a-3e9e-9445-754ab426cc11 | -14.05766 | -49.13947 | 2025-10-06 04:27:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5201b18-4bc9-3921-b74a-83f53123aa94 | -14.91057 | -46.84862 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 866e6f25-6b83-320c-be54-41c075a4a816 | -15.74833 | -47.68998 | 2025-10-06 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82003d57-3f5f-3cb5-b1d7-ca16bb30e1fe | -13.61807 | -48.69437 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bf25f45-f6f0-3ebd-b194-13e547d0cfc8 | -13.32838 | -47.17556 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0201b319-8768-35a6-85ad-bf8e3d70d065 | -10.61507 | -48.67279 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59095e42-b9f6-3bb3-8725-70b54ef75eee | -14.32618 | -45.85246 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3acdacb-82dd-3f96-9c4a-02c3ade59a25 | -11.64593 | -47.01513 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d6fc86c-b905-37e9-a9fc-51e57c16e15f | -14.67555 | -48.3354 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6ec196c3-07ec-30df-95a4-09208b37bf99 | -13.73483 | -48.06398 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1056ce9b-1a2c-3d38-baf4-6a7b26d340a5 | -13.13588 | -47.99795 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 744717a4-06b2-3e00-afc7-d1f518d4fb7f | -13.35271 | -47.19408 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fae581c8-cf9d-3e41-a4ec-4f93f99b7402 | -13.62628 | -48.70677 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3c69ca3-3caa-351c-9abd-3ef1c90653b1 | -14.68717 | -48.28288 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15cf0c6b-5051-39ba-8b6e-44c5a8cbe24d | -15.19672 | -52.80611 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92b8a0cc-8aa3-354c-bf08-e07d4e78de1d | -10.27536 | -44.3652 | 2025-10-06 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1dd1c84-7dbc-343e-9333-d8a995e96d09 | -9.53697 | -51.707 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dba60f58-48cb-3595-bc17-46deed9a3c39 | -15.2925 | -46.33052 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c90d0942-7d2d-3fa7-bc4d-7db09234e257 | -11.15648 | -47.9258 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98dbc80b-0feb-3023-8528-404ffe8ac518 | -9.24589 | -48.20662 | 2025-10-06 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27d22d45-9f70-3f90-9a06-0a9191f9121a | -15.43871 | -45.87289 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6a933bb-4018-36aa-abc9-d0b99341a8ff | -13.35773 | -47.24961 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1bee290-be13-3613-a3a4-7a59a52e477e | -12.2566 | -49.1977 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb1422d4-dab1-358f-8376-62e9c856f9e0 | -13.6858 | -47.34958 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e944d432-f7ca-3e1f-a388-392e2ab887a7 | -11.40497 | -43.48549 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d3b25a7-0017-33d7-bfa4-ff6c5800624b | -8.51047 | -54.60157 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e749423-162f-3001-bc42-90983ef219fd | -10.42226 | -50.34069 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2a757454-462f-3198-8db1-5371815a48f9 | -17.07732 | -43.37956 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68c87af3-7b95-3213-b5e1-f246cc328461 | -13.34924 | -47.59283 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bfb7ec6-8f26-3ed3-b74d-dad73bc63f9e | -12.91115 | -46.81344 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39c07506-5359-3933-bdc1-5dcca04602f0 | -13.26972 | -47.18115 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ca018fe-7a4c-3268-97d6-c04806dc38a5 | -15.58595 | -52.52786 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b954d34c-4870-33a7-94a9-3e81bd675f49 | -12.32232 | -55.1192 | 2025-10-06 04:27:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2569da00-3cef-3619-a66f-18eecc50867b | -11.48968 | -45.03876 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3cd305dc-d1c9-3b9b-9a2e-05d208046b49 | -15.26715 | -47.14125 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0a47d66-5a01-3cb0-ab8e-c38e17582071 | -13.27027 | -47.1776 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f4c9d90-9d92-3cfb-b5ba-9ea084b03354 | -15.57538 | -52.45054 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8834e90-8607-31c7-bcc4-3df610e169f2 | -11.04867 | -47.76836 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37c76a58-1482-36e1-8759-b4fdaeaaf7b1 | -13.24658 | -51.68609 | 2025-10-06 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 882f4417-edd6-34d4-9710-87737dcfb362 | -10.45044 | -48.36194 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 505d158a-6271-3a56-a4cf-0c796bad53cf | -16.03847 | -50.96244 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 156617b2-2a52-359f-ade3-b193a512511b | -14.54389 | -46.95947 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4dbd4872-569f-3d59-b90e-81c4e90ad85d | -10.58686 | -51.60188 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4be62ff6-3f5a-3ee6-80c6-e2c4b61ca81a | -15.20056 | -52.8068 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README39.md)
