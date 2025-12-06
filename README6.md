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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6edba789-6a07-3076-8208-7caa4b97f1f3 | 3.41819 | -51.26166 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60a5fe5c-3d99-3dc4-9885-682f1ffd7af8 | 3.50956 | -51.26338 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 334fa88f-66c8-3936-ac08-40305c61a5ac | 3.49368 | -51.24251 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a5819d89-4081-37ce-9504-48cc6e7fc67a | 3.46226 | -51.24329 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b830818-4a32-3671-be93-d72c4b322790 | 3.98414 | -51.68439 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23aa2a4d-f4ad-3278-a545-44bab4c6106c | 2.90886 | -51.02738 | 2025-12-06 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4968267a-53b0-393f-821a-8943e29edda6 | 3.50257 | -51.24502 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 51339bc3-83ed-3ff0-acfe-4ff3500040bd | 2.115 | -50.9049 | 2025-12-06 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c46e53b3-95c1-3185-9922-8cbc8f1506b4 | 3.49198 | -51.24261 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 59ce8cb1-2779-345f-b239-91895a1f0225 | 3.5037 | -51.25262 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 765a6152-8b96-3f99-a8fb-ab8f3571a87f | 3.48781 | -51.24326 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f35cc2-8826-338b-9828-72bfb7735f13 | 3.41043 | -51.26674 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2cedcf5a-eb41-3359-8239-fb8d0f4f2cc1 | 3.47474 | -51.24138 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c096a7d-5234-32c1-ae43-9b70fc4382dd | 3.50596 | -51.26782 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3aec4eb-1a41-3676-bbb5-57ca24de42a1 | 3.50314 | -51.24882 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 09de2be4-6c9e-344e-afeb-b109e2e95437 | 3.46584 | -51.23886 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55d128b5-dcd1-34ab-9c0f-e3d88122b65f | 3.47523 | -51.4978 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c94bc8-0ba2-31b5-867d-12f11aaf5f9d | 3.41099 | -51.27053 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e43963bb-9bf9-3d47-95a9-a11250820b82 | 3.49424 | -51.24631 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1570db69-9956-34fe-9117-1b62088f6f8e | 2.90957 | -51.00525 | 2025-12-06 04:29:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0986b4cf-227b-3f53-88e3-f44b4e38e08f | 3.45509 | -51.25213 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fce5c3f-ae51-3735-9b8b-363339893261 | 3.42178 | -51.25723 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fb68653c-560c-3413-a923-830519984f3f | 3.45451 | -51.24834 | 2025-12-06 04:29:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5db3c3f1-d5df-37e0-bf21-922bdf13695b | 2.11554 | -50.90834 | 2025-12-06 04:29:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 098267c5-a2da-3e53-ae04-6d047e79738a | 0.79206 | -51.96979 | 2025-12-06 04:31:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7b7908c-e67c-3566-b01a-2e026acb36a8 | -3.54871 | -43.38063 | 2025-12-06 04:31:00 | NOAA-20 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ebc1f4c-8852-3793-955a-03a9b5ca6e8d | -5.98764 | -41.89297 | 2025-12-06 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| fe24f477-ad10-352f-a342-452b38d1b01c | -2.10596 | -53.45467 | 2025-12-06 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c3773bb-b934-36c3-8509-04cd8e3f1e90 | -1.20913 | -53.72915 | 2025-12-06 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf63bc4c-bf35-3c20-a839-f8cc72d7ea19 | -0.64444 | -52.38366 | 2025-12-06 04:31:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f75f43b3-aeb0-327f-89fd-d1c0efc9c1eb | -2.30754 | -47.73436 | 2025-12-06 04:31:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53150406-3808-3872-ae4d-5b93ca4175c8 | -2.12965 | -45.32411 | 2025-12-06 04:31:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cf5eaf20-65eb-3a82-a29f-89ed6c6e4f04 | -1.48383 | -45.76538 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 753a0393-8af5-3e32-8c3b-2d152501dfd5 | -2.02039 | -46.49721 | 2025-12-06 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfc31f92-bc5f-3a20-94f6-76844643e627 | 0.12304 | -49.91821 | 2025-12-06 04:31:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8234909-506e-3310-8b1e-01443374c016 | -4.7347 | -44.42791 | 2025-12-06 04:31:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fb6610b-75a1-34e6-b6ea-d30340608ea6 | -2.77253 | -45.51494 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f22e995b-23b2-30cd-b118-d5c01bb7e53c | -3.33233 | -45.90604 | 2025-12-06 04:31:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7180ae7c-e9a9-352d-87fd-cfc78f44a3c9 | -2.06647 | -45.36663 | 2025-12-06 04:31:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be74d7cc-ba92-335f-8d70-e51e504d5b92 | -2.6803 | -45.97255 | 2025-12-06 04:31:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f14e7dab-6b7f-3744-a145-28a4cf4f3384 | -2.59185 | -45.54637 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01e6420d-426b-367d-9d5c-491d37ce9238 | 1.98207 | -55.70918 | 2025-12-06 04:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 40b557bf-cb09-3022-b3c1-8e73bcf560c6 | -3.752 | -45.18583 | 2025-12-06 04:31:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fc55e58-2b7c-3b0a-ac5d-78b8542b6c40 | -5.98913 | -41.89391 | 2025-12-06 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a7c08ef8-2a6f-36e1-bbcc-0c2090c24626 | -2.27732 | -45.68187 | 2025-12-06 04:31:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76151008-085f-3f3b-a0df-03a6a0dc6afc | -1.32861 | -46.61754 | 2025-12-06 04:31:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b04f3c7b-db32-35c7-a389-52e91ca7c073 | -1.47881 | -45.58032 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b136ac5a-8c87-35f9-a538-7a64e29d1c97 | -2.34145 | -47.47763 | 2025-12-06 04:31:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b75deae6-33a7-3c7d-9b18-26b4f877dc5d | -0.76115 | -48.52728 | 2025-12-06 04:31:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbdfa512-48a8-3266-8769-159199aab755 | 0.84871 | -50.18708 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa87a25-a942-380c-b1b8-3395428cab2e | 0.3265 | -50.99263 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3fa0463-83f0-32e1-80db-f557b8e90aae | -1.48216 | -45.58084 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccef75c3-cfd9-35ed-a4cd-6320ceec9015 | -3.22279 | -46.86615 | 2025-12-06 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae727fe3-012f-31d1-a289-05e239c23067 | -2.10857 | -53.5774 | 2025-12-06 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a317e0fa-5f14-3671-a4d9-750f1d5dd4fb | 0.32259 | -50.99325 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea89db38-165b-303a-930e-3980a85dd0e2 | -2.22758 | -53.5403 | 2025-12-06 04:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9f9afc-c646-36ee-9645-1a67fa207ec4 | -4.57605 | -45.83789 | 2025-12-06 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34362838-9388-369a-a592-5a57fd784f4f | -4.38633 | -45.90576 | 2025-12-06 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa99e053-ae27-31ab-af62-f741e4fc2429 | -0.96165 | -47.32771 | 2025-12-06 04:31:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5f5be674-cbef-3244-ace3-74ccd6a6ed2b | -2.7731 | -45.51132 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8508479f-35fb-3cf5-ba25-351549de00f4 | -1.91567 | -46.51621 | 2025-12-06 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1a54ecf-452e-34aa-a080-61465428e505 | 0.32278 | -50.99514 | 2025-12-06 04:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9287c43b-d9f7-3388-84b1-79a3ac76eb74 | -1.85468 | -47.48206 | 2025-12-06 04:31:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef30aa27-73fb-321e-a2b3-a3ae1a631d03 | -5.98706 | -41.89701 | 2025-12-06 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d1fee482-c008-3939-a358-1d2a72240530 | -2.23066 | -45.59447 | 2025-12-06 04:31:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3c02c35-da79-3783-a829-69ad13c6b662 | -3.07818 | -44.31968 | 2025-12-06 04:31:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3630d8e0-964a-3b60-b48e-066339a7ced0 | -3.2165 | -46.06279 | 2025-12-06 04:31:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 758eb785-cd7c-35fc-9716-8791e8ddcf8c | -3.60517 | -46.01331 | 2025-12-06 04:31:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d4ee04a8-0516-378a-8acd-f6b647b1d40c | 1.98151 | -55.70552 | 2025-12-06 04:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 186ab35e-658c-3af1-96ee-e701745ee110 | -3.66502 | -43.55345 | 2025-12-06 04:31:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91ab1c3f-f889-3060-8e46-7697f748271d | 1.69682 | -50.84724 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a83d9c6-6658-32d7-8187-022cc699297b | -4.57944 | -45.83843 | 2025-12-06 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 320653b2-eea0-3b1c-9980-45579209993d | -4.31619 | -48.62797 | 2025-12-06 04:31:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7efa7c40-d9bd-3191-a5d1-f613dc2b01b8 | -1.71973 | -45.77368 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6941c15-1a88-307d-8a0c-e928ea744507 | -2.2379 | -46.13034 | 2025-12-06 04:31:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d3f24bd-7fdd-3731-9379-b0055a81531d | -4.16244 | -39.25128 | 2025-12-06 04:31:00 | NOAA-20 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 610c082e-9655-38fa-bae7-1484f0eca569 | -2.30422 | -47.73384 | 2025-12-06 04:31:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6596bd28-16a5-380e-ba3a-9c5220b4a1cc | -4.73768 | -44.43267 | 2025-12-06 04:31:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e90da47c-a136-33fd-9e06-38caa42b8253 | -4.73408 | -44.43208 | 2025-12-06 04:31:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21ffca78-39d4-392e-bce2-ed586cc82fa5 | -4.5419 | -45.35757 | 2025-12-06 04:31:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35ebb7aa-8305-3026-b68b-5e7c057b70a6 | -2.34199 | -47.47419 | 2025-12-06 04:31:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12060050-e20c-31ee-b2a5-b34e1028b27c | -4.4086 | -45.76385 | 2025-12-06 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37855457-bb41-391f-abd0-774aded305cd | -4.73605 | -44.4334 | 2025-12-06 04:31:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42ad1371-ccd8-3769-bc9c-6d8331171716 | -2.06704 | -45.36301 | 2025-12-06 04:31:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cea80d1-a37e-359d-95b7-ecd1995cbe34 | -2.70056 | -45.68822 | 2025-12-06 04:31:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c5ba28b-bb3b-3a30-ae3d-e11cb781a09e | -1.80546 | -45.94152 | 2025-12-06 04:31:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3cc2572-fd27-34e6-96f2-1157d77c8448 | -2.5879 | -45.54945 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e593995b-b38e-3281-9e05-99e21aa68555 | -4.40408 | -45.74824 | 2025-12-06 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df51c43b-97f6-3d59-8e5c-eebeded4c420 | -1.7684 | -46.45813 | 2025-12-06 04:31:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e6ae83ec-5ba3-3d13-bab4-daa61be5376c | -1.95757 | -48.45958 | 2025-12-06 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67a222c0-8a8e-31ce-a4a2-8501c8c1afd2 | -2.76915 | -45.51442 | 2025-12-06 04:31:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 455f2c3b-ebe1-30f0-8e2e-25d0e11713fc | -3.3592 | -46.8631 | 2025-12-06 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0f5c87-cbb0-3c5e-bf61-27ba1d4cbb7b | -3.66111 | -43.60297 | 2025-12-06 04:31:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad3df379-7d1d-3dc2-a5b2-ca68da0f7cef | -1.02067 | -47.06167 | 2025-12-06 04:31:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd2e7b66-64e9-3db0-b93d-62e9f2a14a70 | -2.42104 | -46.86702 | 2025-12-06 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09379f3f-4f9b-3872-93f2-7bbbd2fb5303 | 0.79286 | -51.96997 | 2025-12-06 04:31:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8171e80c-721e-35bb-a3a9-508d47b14fba | 1.69961 | -50.84449 | 2025-12-06 04:31:00 | NOAA-20 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a68aae36-5bd7-3d30-8bf3-910dab2db641 | 1.9969 | -55.69526 | 2025-12-06 04:31:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a232348-5df8-3431-80cb-d87dfef0f576 | -1.72252 | -45.77773 | 2025-12-06 04:31:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e8b79497-bd60-3138-9c05-12bdb325c2ab | -5.98484 | -41.89327 | 2025-12-06 04:31:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README7.md)
