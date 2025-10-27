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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8808533b-9629-3fbe-9acb-8d768d28443b | -4.44202 | -45.98584 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 7a373a96-8091-39ba-9703-1298502bf72a | -3.25541 | -44.40353 | 2025-10-27 00:16:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d97fac5b-05a2-349e-bddc-88589a0f4b84 | -3.14789 | -50.4589 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6d846b7d-f305-375b-b8d4-4127b2997794 | -1.35313 | -49.17519 | 2025-10-27 00:16:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6b0036ca-8432-3d57-b84a-256833cb21e0 | -2.63312 | -47.30159 | 2025-10-27 00:16:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 450d74e3-effd-3b43-92ba-c59567a977e9 | -3.47416 | -49.98156 | 2025-10-27 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f9e24663-9ffa-3236-8163-d3aa5760775a | -3.56087 | -49.49702 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c76fece0-59cc-38f1-8024-d0f07f904fa8 | -2.08042 | -48.36876 | 2025-10-27 00:16:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6271d3cf-f964-3d72-887d-61f8efc7fac1 | -4.20488 | -45.7337 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3455edfe-a93b-332f-9240-33d40191fa33 | -4.24315 | -43.29774 | 2025-10-27 00:16:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bfb2db10-87af-3ce2-b933-97681cfd07d2 | -4.86854 | -48.72661 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6ba9ab40-c747-3158-be39-19d3c663279c | -4.18931 | -43.25467 | 2025-10-27 00:16:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2242023e-e3dc-3bfe-abf6-22564f77d416 | -3.2567 | -44.41268 | 2025-10-27 00:16:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 844f127f-983e-33b5-a816-34032a2cd19a | -4.46896 | -50.47531 | 2025-10-27 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 306643d8-478e-375d-bfc3-6d5485567b03 | -3.21533 | -45.77798 | 2025-10-27 00:16:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5a1a9575-401c-3d66-bbbf-48295b851d2f | -3.99382 | -51.03981 | 2025-10-27 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 4057b813-544c-3806-b27b-e2269b300fa9 | -4.30964 | -48.2281 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0665f1c7-82d6-31a8-a990-0163a83fafc8 | -2.37689 | -45.58378 | 2025-10-27 00:16:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f022d57c-bc0f-353e-87b2-64e189e7c687 | -3.87043 | -50.89139 | 2025-10-27 00:16:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 23eebc88-851d-3707-bc03-b7aab9f21f31 | -4.09129 | -42.94213 | 2025-10-27 00:16:00 | TERRA_M-M | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 88f06bc8-68ce-31fb-87e3-833243908248 | -4.56925 | -45.70311 | 2025-10-27 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 812d672d-d1f0-3e92-a506-465dba6c3036 | -4.34284 | -49.88029 | 2025-10-27 00:16:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7d007f07-4210-3dd0-ad9e-8b6da8cbd082 | -3.14671 | -50.44974 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a8142c5a-bf34-3d35-ae65-169982b8b921 | -3.72066 | -47.64415 | 2025-10-27 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 124dd5b6-e886-3b61-b57d-9d42a9c87d73 | -3.21654 | -45.78677 | 2025-10-27 00:16:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 3bb80cee-af9e-347c-8dd0-0d0e7c53886e | -4.42553 | -43.8742 | 2025-10-27 00:16:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 09722a98-8e8b-3467-9a1f-fb1098a42965 | -3.06683 | -49.37082 | 2025-10-27 00:16:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6539705b-ef24-3053-9028-aac1c6829c4b | -2.35561 | -48.29156 | 2025-10-27 00:16:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| eebe3e00-81a0-33f1-ab8a-3e15770ef66b | -3.72222 | -49.45583 | 2025-10-27 00:16:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8e4e0724-9e59-3d07-9e75-d061338837ba | -3.2224 | -44.43277 | 2025-10-27 00:16:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| c2b4b6b5-6188-38f2-a084-e2f59c770327 | -4.31909 | -43.24998 | 2025-10-27 00:16:00 | TERRA_M-M | AFONSO CUNHA | MARANHÃO | Brasil | 2100105 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e08c09e4-c20b-34c5-b252-f075dc975e55 | -4.50678 | -48.84852 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3faa7938-7ee9-33d3-8818-544a0f6a5bf4 | -3.15276 | -50.32375 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 75ddb02e-41aa-3697-9d89-c423246610c7 | -3.71266 | -47.65538 | 2025-10-27 00:16:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 93b9c100-6429-355e-bef9-bb77f08b835a | -3.10838 | -50.17535 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0c16d43d-1f59-3bcd-82a6-7f222fa6f2ff | -4.45326 | -45.46494 | 2025-10-27 00:16:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| aa2eeffe-a249-3d76-850a-a507a5bbbd30 | -3.3993 | -46.03608 | 2025-10-27 00:16:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f5265b43-47a4-34ac-aeff-2a4971676cb6 | -4.22692 | -48.36821 | 2025-10-27 00:16:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a30a47ec-ec1d-368a-8a62-60f109dc28a8 | -3.6179 | -42.78264 | 2025-10-27 00:16:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| a09414ba-1431-38a1-b5bb-89c7548aa129 | -3.57027 | -49.019 | 2025-10-27 00:16:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 14657977-b2fb-3456-8738-6f62aa189b3c | -4.73093 | -46.81318 | 2025-10-27 00:16:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c37a45e1-b907-3057-998b-35f29c23e133 | -2.9735 | -51.04018 | 2025-10-27 00:16:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| cf889d66-2dc9-3e32-9f49-876470438e9f | 0.44258 | -50.81787 | 2025-10-27 00:18:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 548b62f2-1d61-3692-b6ca-6cd52e9a7f30 | 1.14344 | -51.06488 | 2025-10-27 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0f3a86c8-25a2-36cb-9576-57ccab522a77 | 2.35162 | -51.54172 | 2025-10-27 00:18:00 | TERRA_M-M | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 40924179-a79a-3120-a9cd-bc743b1320b7 | 0.16124 | -51.02018 | 2025-10-27 00:18:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 8093f0da-f193-3dfc-b8c7-804e27b0738d | 0.44063 | -50.83175 | 2025-10-27 00:18:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a4bc5808-335c-3f77-92ac-aacb8b7c31e0 | 1.15445 | -51.06644 | 2025-10-27 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 68663160-4c80-3b77-988c-3eb3375897ea | 3.03146 | -51.44817 | 2025-10-27 00:18:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 292382b0-57a0-309d-a581-c190551cf281 | 1.15642 | -51.05236 | 2025-10-27 00:18:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 68efba95-2340-3a73-9f97-dc68eb8f68b7 | 0.80768 | -50.83712 | 2025-10-27 00:18:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 04fb1955-807e-3923-9d6a-dc07ab8e753d | 0.44837 | -50.77647 | 2025-10-27 00:18:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 20157bf2-3776-3237-b79c-807e15186721 | 0.32161 | -51.02525 | 2025-10-27 00:18:00 | TERRA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 82c1fdf1-8471-361d-af8d-72ef0b0c7aa8 | -4.443 | -43.4492 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e8d30be9-960d-3987-b758-b48c0d77bef3 | -4.3879 | -43.3129 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| cb02b8bd-d210-391a-8f48-89247a8bc476 | -12.545 | -47.5651 | 2025-10-27 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f175be59-3a45-36ff-8c26-434e1a8bc021 | -10.7484 | -44.1932 | 2025-10-27 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5e944977-fc99-3538-916e-f730d90b9a6c | -3.7287 | -47.6395 | 2025-10-27 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| ac639e87-4a44-33ca-a1c7-8fec5eb95536 | -7.8411 | -46.4646 | 2025-10-27 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| f69d4663-1e1c-3608-9b6d-976edd7fb6e4 | -7.8596 | -46.4853 | 2025-10-27 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| aef04fc9-d497-39c2-b804-431d05960517 | -4.4992 | -43.4226 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| bcd88642-2f3e-3da7-a2ba-ebfa2b9367b9 | -4.4617 | -43.4481 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 4d53f37a-a5f6-337d-ae77-281492f695d7 | -4.4433 | -43.4027 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d2796ced-72d5-353a-b991-080f09eb413e | -12.5258 | -47.5678 | 2025-10-27 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| f3904316-e0c6-30a7-bab2-3e9ee205d5ae | -10.8401 | -56.959 | 2025-10-27 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| a56ff8c6-32f8-35be-8719-379444b44f96 | -3.1612 | -50.3298 | 2025-10-27 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d17fa41d-7e51-3fa2-a922-efd8c3e47fbc | -4.4805 | -43.4237 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 135.6 |
| aa3a61f6-8229-39f8-811d-1ed6fb89b0b7 | -3.7286 | -47.6613 | 2025-10-27 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 80ee1d50-220a-3cab-9643-cd3352d6bb11 | -4.7578 | -46.4255 | 2025-10-27 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 5ab26428-cb12-3d66-bde2-c7f72dd6845a | -3.71 | -47.6621 | 2025-10-27 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 6502f402-61ac-348d-af94-46557fc3e900 | -11.9221 | -43.8318 | 2025-10-27 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| df19d8b8-d282-3cf6-b09c-2a37bd7afc6f | -4.4804 | -43.447 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 37daccb7-352e-37d3-bdaf-5172f6b36725 | -4.4618 | -43.4248 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 207.1 |
| a1f565cc-f3dc-3bb8-9997-61ac2adea689 | -6.1857 | -47.3065 | 2025-10-27 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| cb615965-fc57-3e2f-8a77-435b45cdba90 | -4.462 | -43.4016 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0e7f75ae-922a-3ae1-8962-b7f9101a014f | -12.2884 | -43.7732 | 2025-10-27 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f7c86f1a-1b99-3a95-8c92-3598d08c4fa4 | 1.1502 | -51.0603 | 2025-10-27 00:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 06611149-268d-37f0-a374-db1cafe8dd94 | -3.1428 | -50.3304 | 2025-10-27 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| e5c21aa8-b842-3793-852c-5d0cb827266a | -12.2695 | -43.7526 | 2025-10-27 00:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 76b0901b-4523-3d4b-8ad0-566d7e9d7801 | -3.7101 | -47.6403 | 2025-10-27 00:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 606ef86d-b184-3846-9f93-11aa30bc2d02 | -7.0692 | -46.7541 | 2025-10-27 00:20:00 | GOES-19 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 45.4 |
| f9408fbd-9486-31b7-8276-9507e0357d95 | -3.5782 | -44.5297 | 2025-10-27 00:20:00 | GOES-19 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 3acb1788-c698-3465-ba98-876695b9e869 | -6.1855 | -47.3284 | 2025-10-27 00:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d5bc3177-561e-32aa-9b99-9b59976fca35 | -4.4245 | -43.4271 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 241682f0-85c2-3192-9253-605b5be76871 | -4.3877 | -43.3362 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 2d66cd83-d2e0-3121-8478-cc4f735a1cf3 | -3.4583 | -49.9625 | 2025-10-27 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 5228a7e6-4951-3436-8547-c3e140d0bf62 | -5.5423 | -43.9558 | 2025-10-27 00:20:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| ed081673-7adb-3d55-9948-aa69cc92aff3 | -4.4665 | -45.4589 | 2025-10-27 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 85f6e749-c51c-32de-a828-74a139701165 | -12.2888 | -43.7495 | 2025-10-27 00:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| ceef0465-56d7-3237-89d4-873a73e676cc | -4.4479 | -45.4599 | 2025-10-27 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 08c3eea7-46a0-3a28-848e-ce57ae7db14d | -4.4807 | -43.4005 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| a1889f3b-bbda-3cba-93e7-ed1e24447601 | -7.8408 | -46.487 | 2025-10-27 00:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| ed03fc9f-fb8f-3b13-8555-3b7dd710ee7b | -11.9028 | -43.8348 | 2025-10-27 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d2f51130-604d-3413-bd04-744be973dfd1 | -4.4431 | -43.4259 | 2025-10-27 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 24729a98-1711-3a6a-ac5e-d21441904be5 | -10.7676 | -44.1905 | 2025-10-27 00:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 1686d8ad-00fd-39dc-ad65-c3c80434eb2d | -3.7943 | -49.2936 | 2025-10-27 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 41ee865f-a1da-350c-87f8-0f50a2648e13 | -3.7101 | -47.6403 | 2025-10-27 00:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 206.6 |
| ac525031-c58e-30a6-a8a9-e699869f4618 | -4.3879 | -43.3129 | 2025-10-27 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| efea9712-a536-3484-a23f-ed87682f9ee6 | -7.8411 | -46.4646 | 2025-10-27 00:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 9ea0becb-91e5-3fd0-9ab9-01222b5daded | -4.4665 | -45.4589 | 2025-10-27 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 157.7 |


[Clique aqui para ver as próximas entradas](README8.md)
