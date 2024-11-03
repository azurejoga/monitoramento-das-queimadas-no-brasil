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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57fdbd6a-5547-3456-b641-8754f4f6a959 | -2.57597 | -50.06406 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26643884-13d9-3d1d-a862-a703c5dc94da | -2.57428 | -50.05327 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4783231b-0b93-3d08-bd1e-e0a29ec8cb24 | -2.57374 | -50.0567 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf356d22-140a-33df-87d2-9f6b55a8af91 | -2.54514 | -50.30505 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35c3bdb9-761c-3bdb-8ec3-7426a0b9f31b | -2.54086 | -50.33249 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ceb16162-58fc-395b-b172-be20b1b56e5a | -2.52285 | -50.16117 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28764168-2928-3775-bb80-36459e2035ea | -2.47212 | -50.24815 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0591622a-fe0d-3c06-be5c-209c79b84def | -2.47122 | -50.42713 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ce4bc15-260c-3ad1-b2ca-b466b94bbc70 | -2.46069 | -50.40793 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b3b1240-a8a4-3ebf-809c-a29cac189b3e | -2.45793 | -50.40399 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 012a545c-6bf4-3f65-873c-47bdc2aa0b3f | -2.45739 | -50.40742 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b315f494-8b89-320a-a3f4-4f685fb4be8e | -2.45516 | -50.40005 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbd187f0-6972-3bda-82a5-4f45f89045f2 | -2.45463 | -50.40348 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e8db990-9b94-3b47-89e4-832a4094c5a7 | -2.4524 | -50.39611 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da8b8d41-dd64-3583-96b8-ac6b9c049755 | -2.45186 | -50.39954 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6349fb3a-288a-36c2-b9c7-296a583de2c6 | -2.44582 | -50.26515 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba4ec45-fa40-3f4c-8889-6058bbf826ae | -2.44187 | -50.37692 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 554c77b7-d8f9-3f10-9b0b-fd9f5de6652c | -2.42384 | -50.40577 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25409e9e-a77d-3dea-ae97-4e8ac1ce4905 | -2.42331 | -50.40921 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 936310e8-9865-3734-922a-beacef792b8a | -2.42161 | -50.3984 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6364880-eccc-3f5b-b081-234ebe188d6c | -2.41778 | -50.40133 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e32772d-ad1a-3177-bc6b-b490258265c4 | -2.41732 | -50.42587 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 883e2715-6610-3110-95d7-b525697293ea | -2.41678 | -50.4293 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16393c9f-ca57-3dfd-b39d-ff9aa69bf533 | -2.40039 | -50.31361 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e34c021b-9245-3096-9833-9292e14d3ca8 | -2.39985 | -50.31703 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4703087e-9fa5-323e-b1c9-5d2b24c63d6d | -2.39709 | -50.3131 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63f1206e-e6cd-312f-816f-a32274cf855d | -2.39655 | -50.31652 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 653229bd-c98b-36b3-9af5-1aa4afbfdbda | -2.39325 | -50.31602 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80218134-1ad9-376a-a2aa-ec66391997a8 | -2.39272 | -50.31945 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f0e983a1-a516-36f8-b110-d2fbe3d46cf3 | -2.38862 | -50.38908 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 357ff569-4208-3190-a42a-3630f622a711 | -2.38371 | -50.39886 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5a3dae9-a4c2-39a6-9967-f525f64ebebb | -2.34071 | -50.37116 | 2024-11-03 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 193882a6-ca89-3436-af74-eb98170ad4c4 | -2.31064 | -49.55795 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37e1c08a-b708-32d4-aa0b-b0245c68b151 | -2.31003 | -49.5402 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a2349b6-1ffd-38b9-a82b-d88c4f0a4d39 | -2.30687 | -49.84634 | 2024-11-03 04:46:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa20e73c-e020-3dfd-bbc1-203cd53567bb | -2.2331 | -50.31944 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aa4be17-d96b-31c8-8aff-957317ef2460 | -2.2298 | -50.31893 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 51213c3b-442e-39f8-b096-08c6289ace27 | -2.22266 | -50.32135 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c837c39-6a21-34e0-bbcf-34fef1f07d66 | -2.22212 | -50.32478 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad0d7525-433c-3f5e-8e78-c86c2b0f1ed6 | -2.22087 | -49.56887 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c95dd4f7-d71c-3282-a64e-269a1aa0e771 | -2.22033 | -49.57232 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 574baa5b-deff-3396-bce5-84c4637fac69 | -2.21936 | -50.32084 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2084983c-6cd6-3d14-941d-7b86c3c9c76e | -2.21882 | -50.32427 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 886b1ba6-c98e-349b-98fb-34fdb8e6ac7e | -2.21756 | -49.56836 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7980469-8c64-39c9-8d84-6a0f89535a13 | -2.21222 | -50.32326 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c37af3fb-a698-3f88-97d7-657d093f06de | -2.21169 | -50.32668 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db087c0a-6753-3fcf-9aab-a13c841d852a | -2.20455 | -50.3291 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 35b93a98-4b5d-38f0-b8da-8017201f7de9 | -2.20401 | -50.33253 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 756e220b-e160-3272-a629-8a0969d3258f | -2.19052 | -49.52124 | 2024-11-03 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef2e8df5-883c-3fed-bc8a-f9b61258bd0c | -2.16573 | -50.14038 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85773192-faf1-3d19-bd30-1d6514dab149 | -2.16519 | -50.14381 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30dae850-b75b-3f4b-b60f-dd26e1f968f7 | -2.16324 | -50.19965 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cea5b674-20d4-3554-976f-a126c8f3a338 | -2.16243 | -50.13988 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f7feef1-f14c-399b-a7c9-da31b9754b6d | -2.16189 | -50.1433 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13cd7f71-eb25-3c36-b8f2-64998ad851f3 | -2.15966 | -50.13594 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af610e7d-e5d3-3293-b839-27b647fa8eaa | -2.15913 | -50.13937 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d6268d7-8930-3ea6-b80a-29b6b348b86b | -2.15859 | -50.1428 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fc4e699-e6d0-37c9-9f34-075b6bc29756 | -2.15583 | -50.13886 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40fd09cb-012e-3c58-ab56-02f8ef95be60 | -2.1553 | -50.14229 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0c7b69c-d838-3a67-b23d-00f7b8653be9 | -2.15253 | -50.13835 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 691a289e-c1a7-3afe-bf9b-af9b9dc17b01 | -2.152 | -50.14178 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 196a0878-0119-3447-9605-c470295fe25c | -2.14816 | -50.1447 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c31f9fb-0c4f-3dba-831d-641a4c63f127 | -2.12676 | -50.15194 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a4d37e4-ba15-3718-be65-cb9e9d76236a | -2.12453 | -50.14457 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9826389-ab3d-34b6-86e0-99de94d72b35 | -2.12444 | -50.25335 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4abb5161-b0c8-3fac-9b13-3e7860bac89b | -2.12346 | -50.15143 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc679325-0557-387f-827d-a28478a733ea | -2.12177 | -50.14064 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d91b739-c55e-3222-8279-d01e131c5d9f | -2.12123 | -50.14407 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a1ef80e-1de0-3abc-bbf8-9d151625b1d3 | -2.12017 | -50.15092 | 2024-11-03 04:46:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53bd5870-6678-3fdb-a8f4-899beadf712c | -3.54699 | -50.29353 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 56fc7556-c745-3d08-a0f4-00bef55313d4 | -3.54592 | -50.3004 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e7eb74d-2dac-3f2d-b12f-ec962a1d7f47 | -3.54423 | -50.28959 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f558c4f6-96c7-341a-a869-e312563790ac | -3.54369 | -50.29302 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f572247b-e7ac-38f4-8cd3-e974bde65d28 | -3.54316 | -50.29646 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 956ad841-31c4-3a78-9874-8bddb3be7d74 | -3.54093 | -50.28908 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5c00b051-b634-38d7-a9d5-c83ed470546c | -3.51006 | -50.28779 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4acd6d44-7380-3aa6-8eae-e7d8f18ee231 | -3.48437 | -50.32248 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54bba191-dad3-39ce-a27a-13722d8a7c38 | -3.47528 | -50.38082 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d1268716-df68-3591-9949-b42a0ea1dc30 | -3.47474 | -50.38425 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2093a728-d84a-3346-a960-59b9fc80ec42 | -3.47305 | -50.37344 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b6e3647-c5f3-30c0-bd1c-777781f8eaaa | -3.47198 | -50.38031 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c8cfda32-3f48-35ca-8050-f6191cb6e05b | -3.47144 | -50.38374 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db570def-abd1-3f68-a7a3-867a830a1623 | -3.46939 | -50.28856 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54998f2f-b206-35ee-a022-0902488c0ac6 | -3.46921 | -50.37637 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f23534bf-9d73-37a4-8a6f-42023e930133 | -3.46912 | -50.48528 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dca5b2e6-51d1-304b-ab72-7d1eaab46ba3 | -3.46868 | -50.3798 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 464d64eb-f705-3587-bc92-becaaa951f2b | -3.46858 | -50.48871 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 186ad9d0-414a-392a-8483-cb3629a0e229 | -3.46609 | -50.28805 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f529ca7-e417-37b4-885d-a38b75d9e8ac | -3.46591 | -50.37586 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b5ac9d91-1674-3805-ac0a-70067ff9c335 | -3.46582 | -50.48477 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6058e7e4-642c-3e0b-b1f0-a238182d5aa1 | -3.44913 | -50.17998 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 712e7879-81ed-327c-8f54-8ccf8b4b7c43 | -3.44859 | -50.18342 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 531fe6c8-ebff-3160-9d03-5e649453db83 | -3.44529 | -50.18291 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4eec538-59ca-34d2-850c-617c1a1cc7d8 | -3.44504 | -50.37967 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a728d91-2ecd-3c09-834b-61b72dd88a5c | -3.43657 | -50.32565 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d9bd597-2760-3d1b-aef0-6ccd9bf8b1c4 | -3.43327 | -50.32515 | 2024-11-03 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc1551db-5074-3afc-ba94-68ddddacf19e | -2.36732 | -48.93148 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2e9d614-bca0-3c1b-b5a9-23fd345a0415 | -2.36445 | -49.10386 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b572fe78-60e9-3b78-84a2-17ebc95971df | -2.36002 | -48.91228 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a941153d-30b8-3bdd-bcec-3be9d1dc7e15 | -2.35667 | -48.91176 | 2024-11-03 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README44.md)
