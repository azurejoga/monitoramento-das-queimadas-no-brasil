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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b01d6567-30fc-388d-b936-88923e4f0869 | -8.9598 | -60.555 | 2026-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0c2fe586-1297-301f-8f90-2ab35f1cfaac | -8.96 | -60.5358 | 2026-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 66054aca-f7ee-3ad2-b7c0-cc08941c079c | -6.1476 | -57.7215 | 2026-08-10 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 18a01ed1-9f0f-3968-ac1d-61d9ff92cb68 | -11.2123 | -54.0387 | 2026-08-10 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| be000b2d-7042-3f1e-ac4b-1089780bbdd7 | -8.9414 | -60.5367 | 2026-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| ecb394b4-1f69-3d37-afdd-877f41ada62c | -8.9039 | -60.5769 | 2026-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 4633cbf6-5b22-3621-a8b7-73a23a24009d | -8.8854 | -60.5778 | 2026-08-10 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| d30eb852-a0b2-3f15-bcb6-91f12b7c17fa | -11.2123 | -54.0387 | 2026-08-10 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 1d702aec-4469-33b0-8ec0-cb99f0e9da85 | -11.2125 | -54.0181 | 2026-08-10 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 0cde80d2-705d-3ac6-95c1-74910f60c320 | -8.8854 | -60.5778 | 2026-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| b06b3974-b75c-3794-89ee-f2bf27ff8426 | -8.9039 | -60.5769 | 2026-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 618f14cd-519c-3dd8-9faf-e9250f965f38 | -8.96 | -60.5358 | 2026-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 241ce2d0-c245-3326-8a0f-eb91058cf558 | -8.9414 | -60.5367 | 2026-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6b783390-a670-3490-8721-ccf20336c553 | -8.9598 | -60.555 | 2026-08-10 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 1a2bdc8b-c6a1-39ac-b82e-863bca9a77a2 | -8.8854 | -60.5778 | 2026-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 2318fe95-ed25-357c-8b6c-cf02d76726ff | -8.9039 | -60.5769 | 2026-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 8c98dffd-11ff-34e1-9f9b-201f4a94a6be | -8.9414 | -60.5367 | 2026-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 4317884c-abce-38b5-bfe3-ec0f265eb298 | -8.9598 | -60.555 | 2026-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7ddd8dd5-f463-3e58-8074-d81e2dda2703 | -8.96 | -60.5358 | 2026-08-10 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| cfda32b7-b141-39d1-bb0f-b5d90ea829e3 | -8.9598 | -60.555 | 2026-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 034e106a-9207-3480-b548-88ddcf22350c | -8.9039 | -60.5769 | 2026-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 76022e6f-f606-3370-8feb-81a7ffc358b7 | -8.96 | -60.5358 | 2026-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| b6e66949-f027-38d3-85ca-ea941b2023ed | -8.9414 | -60.5367 | 2026-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 0f4cfe76-9425-3281-8627-5d693064db6f | -8.8854 | -60.5778 | 2026-08-10 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 6a745c05-c4c2-3524-8bb3-aba37b2dee5f | -8.9414 | -60.5367 | 2026-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5820fac9-c004-35c3-a691-19083a659b48 | -8.9039 | -60.5769 | 2026-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 880f2b29-7829-3d5e-a094-9d87dbf31268 | -8.9598 | -60.555 | 2026-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 65cc0d23-32e7-3c98-903c-f9c89035c3bf | -8.8854 | -60.5778 | 2026-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| d593be9d-483d-3441-9b52-d751646a8f2c | -8.96 | -60.5358 | 2026-08-10 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| b65329a1-1594-336c-a27a-e2beb5ad080b | -8.8854 | -60.5778 | 2026-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 38ef2a5e-bda7-3988-bf0e-3a28a0c865b0 | -8.96 | -60.5358 | 2026-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 070c680e-57e2-321c-ae64-539205dd4eb7 | -8.9414 | -60.5367 | 2026-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c865b5c8-2a52-3b92-9380-0e831175c4a3 | -8.9598 | -60.555 | 2026-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3cd4f879-d2d4-310a-a256-7b9374412dad | -6.1476 | -57.7215 | 2026-08-10 02:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d980dbc5-5a4b-383e-9a1f-97d5593084ce | -8.9039 | -60.5769 | 2026-08-10 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 2cff4094-b84a-32fb-bd62-1fd5a1d9477c | -8.96 | -60.5358 | 2026-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| be27db9d-27fa-3120-86d1-e8a394c7f536 | -8.9414 | -60.5367 | 2026-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b0de0b1d-7748-32cb-a7ec-b559ed388ee2 | -9.3817 | -40.3252 | 2026-08-10 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 92a7c407-48c5-3fb8-ba82-c01fbcb34d54 | -8.9598 | -60.555 | 2026-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| da646d9b-ae2f-3c87-a665-c71f0d7ba624 | -8.8854 | -60.5778 | 2026-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ee553a9c-2f0c-3e05-926e-a5a1bfff6f10 | -8.9039 | -60.5769 | 2026-08-10 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d95c92e6-4bb4-33a9-9108-705d775c6fcf | -8.9598 | -60.555 | 2026-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8cb0cd02-44d4-3252-b4e6-785643e439aa | -8.9414 | -60.5367 | 2026-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| cc75482b-eb05-3c20-8d8a-c37bdf2f9ffc | -8.96 | -60.5358 | 2026-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e000aabf-ba4b-334e-8381-a9982e655620 | -8.8854 | -60.5778 | 2026-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| de1022b3-18b4-3bdd-aeed-4f3fff880ba8 | -8.9039 | -60.5769 | 2026-08-10 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.2 |
| ea93d8a8-02b4-3396-9b81-26bac3e19469 | -8.9039 | -60.5769 | 2026-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 152fd10b-7695-3a43-9769-6f296634c1e8 | -8.96 | -60.5358 | 2026-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ee09dfbc-b366-38cb-a81f-c64088d931e1 | -8.9598 | -60.555 | 2026-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| b7368306-3fcd-3b9d-8131-e1b8927c030e | -8.9414 | -60.5367 | 2026-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 13a745d0-30b5-3490-87f3-964c27c39202 | -8.8854 | -60.5778 | 2026-08-10 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 73d283fe-b7a3-3944-a26b-5a1af635bb73 | -8.8854 | -60.5778 | 2026-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 9343ef0d-b11e-3b92-9f01-370c9fd6177f | -8.9598 | -60.555 | 2026-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| d092e7f6-dfb7-33b2-b41f-ab72c1cee0b4 | -8.96 | -60.5358 | 2026-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1b46e43e-3b90-3079-b801-5739028e16b2 | -8.9039 | -60.5769 | 2026-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 22a24484-872a-3807-a8e8-10ec40e1478a | -8.9414 | -60.5367 | 2026-08-10 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 3e3c07e2-ee02-330a-8aa6-73cc7003f7cf | -4.92978 | -37.42697 | 2026-08-10 03:10:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 425ed935-7b40-371c-9147-0bafb2ec289e | -9.38832 | -40.3156 | 2026-08-10 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ed0e8f0c-3f35-3a77-a508-e4f2d5ca542c | -9.38688 | -40.31928 | 2026-08-10 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c44ce07-312d-3dee-9637-23bd5c8b085b | -9.38044 | -40.31806 | 2026-08-10 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 38811e4f-05e6-31eb-b618-c25de423f0d5 | -9.38188 | -40.31441 | 2026-08-10 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ca9f1b7c-df7a-322b-86b8-ea316d7d8f45 | -9.38789 | -40.31393 | 2026-08-10 03:13:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 83d9d0c9-cdc6-3b4a-a27c-d370a33ae084 | -6.9846 | -39.50812 | 2026-08-10 03:13:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 23751ee1-3c7d-38f9-a15b-5450c91e5756 | -19.86058 | -40.24313 | 2026-08-10 03:15:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8078a60e-a413-3e49-b431-eb56edb575c5 | -15.16519 | -41.84534 | 2026-08-10 03:15:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 384cd892-9072-379c-b1bd-c0c1d396fe7b | -15.16407 | -41.85053 | 2026-08-10 03:15:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7fe77b46-b4e4-3f94-b3cb-627a44a1870d | -17.69153 | -40.14281 | 2026-08-10 03:15:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| aaf37a05-c8c4-3c69-89e2-6a574dd8c34b | -17.82954 | -41.96219 | 2026-08-10 03:15:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2e3d2723-cb63-3418-bf3e-b2c908bb25af | -17.69229 | -40.13919 | 2026-08-10 03:15:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 84932b76-9037-3cf9-88a3-bb648f9d0328 | -19.86133 | -40.23962 | 2026-08-10 03:15:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48c4cd79-de6b-3899-92a4-314e011bb132 | -17.69076 | -40.14647 | 2026-08-10 03:15:00 | NOAA-21 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| edad8208-b404-316c-b27e-a5819e1b50db | -22.22166 | -43.0238 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 193cb91e-34f4-3564-a00e-9e6aa4cdbfad | -20.50274 | -43.64223 | 2026-08-10 03:17:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 100b2a12-7ed9-3658-b2d3-2385fb8662ad | -19.82824 | -43.29929 | 2026-08-10 03:17:00 | NOAA-21 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 96791daa-1f4c-3dc0-b932-3a705445ddd6 | -20.50396 | -43.63708 | 2026-08-10 03:17:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9136c1cc-029a-3111-9511-c81f88b23165 | -20.49865 | -43.63104 | 2026-08-10 03:17:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dfe3f078-aa8c-3303-aa75-2be38efc1a75 | -20.37679 | -41.60803 | 2026-08-10 03:17:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 395a02c5-1b21-34fc-a0af-9fc53bb3677e | -22.22576 | -43.03307 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 21691752-f08f-386b-b00b-ca76c5e9c339 | -22.21973 | -43.02201 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| d443daa6-11f5-3b49-9703-af664f547e98 | -20.37562 | -41.6073 | 2026-08-10 03:17:00 | NOAA-21 | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| def3bfa9-4b11-3c9c-804e-00d98c65150e | -22.2258 | -43.02297 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 93e74ba9-5ba9-3540-9939-945fe1b032c0 | -22.22251 | -43.02022 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b572b918-98e7-3cdc-99b5-2aa7f7e0177d | -19.82673 | -43.30576 | 2026-08-10 03:17:00 | NOAA-21 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| f0caa403-9dc9-3f62-a16f-f6a35883c1d2 | -22.22495 | -43.02667 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 80682aff-cf9d-386f-acd9-4208dd44ce86 | -22.22674 | -43.02895 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 60be4707-8630-348f-b1a5-840ae4081ab6 | -22.22405 | -43.03053 | 2026-08-10 03:17:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| fd27ad6f-08c3-3ec8-9903-00045c2c5386 | -20.5228 | -42.30751 | 2026-08-10 03:17:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6b8c6cfb-f065-3dbe-b29f-87f6d5787027 | -20.51968 | -42.30732 | 2026-08-10 03:17:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| e514a1b7-845b-3ec6-8415-ee85396cab26 | -8.9598 | -60.555 | 2026-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| a814c988-cd34-3fef-ba34-ec74d264110c | -8.96 | -60.5358 | 2026-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 439869d3-1b4d-3676-91f9-90fd4acd72a1 | -8.9414 | -60.5367 | 2026-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 51bf9745-6993-3a74-bffe-7f4d7c112fcd | -8.8854 | -60.5778 | 2026-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 7d61a0c9-720e-33d9-bf94-5eab76e52d7d | -8.9039 | -60.5769 | 2026-08-10 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9bf85c95-6b7e-31ba-a693-a62b11840a94 | -8.8854 | -60.5778 | 2026-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| bfd2f18f-e8d5-39fe-b1e3-55ae77b310f1 | -8.96 | -60.5358 | 2026-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 0ab67f80-6e57-3781-afc9-a65759a46410 | -8.9414 | -60.5367 | 2026-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 6dbd1185-a944-3508-9d50-3987df628ed6 | -8.9598 | -60.555 | 2026-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0917403c-554a-3002-8543-ac285b7ddb3a | -8.9039 | -60.5769 | 2026-08-10 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| d69650e3-deab-3d01-a6a2-ce956b181844 | -8.9598 | -60.555 | 2026-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cea00a78-5675-3f5b-b441-11c12ddf2702 | -8.96 | -60.5358 | 2026-08-10 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |


[Clique aqui para ver as próximas entradas](README4.md)
