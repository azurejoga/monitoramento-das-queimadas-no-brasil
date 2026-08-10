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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 680e9652-1034-3c80-83e0-82352c4cc784 | -8.9414 | -60.5367 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 527d8c8f-b153-39a9-97cb-3d3d2dfd75bf | -8.9038 | -60.5962 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 780bf2b9-5ae6-33d3-9f89-4d3b3f0744d2 | -10.9326 | -57.1113 | 2026-08-10 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 633d47c3-95af-3ed7-a8d1-24fc688c1f14 | -8.9415 | -60.5174 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 7fe86e6b-05d4-38b7-9705-be30880f8d53 | -6.1476 | -57.7215 | 2026-08-10 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 4e75a25e-85d2-3ce8-a25e-91683027db8d | -8.8855 | -60.5586 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 291c7258-f30e-3694-a2ff-dc295fd26f8a | -11.0526 | -44.2668 | 2026-08-10 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| c824cdbb-bff9-3186-a0ad-0f548f0366d5 | -6.1477 | -57.702 | 2026-08-10 00:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e4ebeba1-4051-36e5-9b24-442f335529a1 | -8.96 | -60.5358 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| d0d4bf38-bb97-3fbe-97a7-be6bf957fa11 | -11.2123 | -54.0387 | 2026-08-10 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 6e4fa1b0-a96f-373e-a5df-5fedcd780655 | -18.8185 | -49.6365 | 2026-08-10 00:00:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 80.9 |
| ee73e751-614c-33e0-9360-3cec385f71a6 | -8.8854 | -60.5778 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.5 |
| fc452976-4206-322d-94df-9233fe0edf81 | -8.9041 | -60.5577 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 1b00967d-a8b8-34e3-a235-92eecd893a9b | -8.9412 | -60.5559 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 4ca5a5df-0412-38c2-95f9-49bb0eba88c5 | -8.9598 | -60.555 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 95beea63-1e91-3e63-b6cd-9fdfa17110b5 | -10.2655 | -45.8434 | 2026-08-10 00:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 86b7a4b6-ac2c-382b-bcfb-94dc8e3e6175 | -8.9039 | -60.5769 | 2026-08-10 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 5f92c7dc-21b6-3295-8bfe-ec3874c2f963 | -7.5488 | -55.5629 | 2026-08-10 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 67c80496-433f-38d3-82a9-1f0c6600f4f2 | -8.9041 | -60.5577 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 76d1860e-2ec7-3eef-8559-51b2b576d2ee | -8.96 | -60.5358 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 367c6c9a-53e6-3945-8b19-e49a09a7be9f | -11.2123 | -54.0387 | 2026-08-10 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 04c659d4-223f-3338-843b-d36af6430de9 | -19.8221 | -43.3061 | 2026-08-10 00:10:00 | GOES-19 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.9 |
| 59f8e806-9250-35cb-902d-c438977388fb | -10.9326 | -57.1113 | 2026-08-10 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e1092046-a50d-303f-bb1b-b7508da2abdb | -8.8854 | -60.5778 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| a6e3dc7d-217e-3857-8607-5aedd4603598 | -8.9039 | -60.5769 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 179.3 |
| c728237c-2c9e-30d2-aca9-d6fdd008d165 | -7.5488 | -55.5629 | 2026-08-10 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8c8d2ac4-8a4f-373b-bd2c-33d94f3a0b68 | -6.1476 | -57.7215 | 2026-08-10 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 751ec942-0b29-3479-b5e6-a8aedb0ab297 | -8.9598 | -60.555 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 489726c2-3279-34b0-80bc-64658d58fd20 | -8.9415 | -60.5174 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| f7665366-26c3-365e-9a19-0bbaf6ccfa10 | -8.9038 | -60.5962 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 5a77acfa-1c6c-3c10-8e91-1d2bf6eef223 | -8.9414 | -60.5367 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 208.9 |
| 82ceed95-bace-3659-85fe-d3d3fd803c49 | -8.8855 | -60.5586 | 2026-08-10 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1ff7c4f1-d915-34d3-b18a-0d9e658eaed9 | -6.1476 | -57.7215 | 2026-08-10 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b233e12b-db9c-330e-8f9e-dcf9e88b2775 | -8.8854 | -60.5778 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| c482f46f-2ef8-3691-8b01-ad4517464428 | -8.9598 | -60.555 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 91a011bb-9ad9-3f07-8d8f-eccb0ac8677c | -8.96 | -60.5358 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 4e911f75-5f9a-3eb0-93f2-0796f2779bd8 | -8.9041 | -60.5577 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 527f0791-11d6-3563-a423-a22346297452 | -8.9414 | -60.5367 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 5e7cb373-a758-3175-8e0d-91c0cc8c579f | -10.9326 | -57.1113 | 2026-08-10 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 5e0e2a8c-2762-34b2-84ab-46e097f54584 | -8.9415 | -60.5174 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3754349d-5a92-3901-b45a-b2689a606c33 | -8.9038 | -60.5962 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| b8261313-a82f-3d23-9302-60e98f226268 | -7.5488 | -55.5629 | 2026-08-10 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 09447e69-663e-31d5-8004-2bbbc93366d8 | -8.9039 | -60.5769 | 2026-08-10 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 190.2 |
| 93ab64c6-eabb-39a5-96c5-585559c2d9d0 | -8.9038 | -60.5962 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8fa8cdc6-95af-3327-8e3d-92ec96966d56 | -8.9598 | -60.555 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 34b58cfc-e328-399b-b38c-0902c8259f9d | -18.8179 | -49.659 | 2026-08-10 00:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.1 |
| f86c1c63-7fea-3964-888b-19dd1c757463 | -8.9414 | -60.5367 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 02a67b21-2619-3a99-bf3e-9ba7c8af5d41 | -6.1476 | -57.7215 | 2026-08-10 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 58b5bca7-9260-3033-a361-ac77b63ea0d7 | -10.9326 | -57.1113 | 2026-08-10 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| dad53a39-e373-38d1-8d99-f0543ed998c3 | -7.5488 | -55.5629 | 2026-08-10 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fe9e0db7-8428-3e77-8fd9-43c2773193e1 | -18.8185 | -49.6365 | 2026-08-10 00:30:00 | GOES-19 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 91.0 |
| a4849e11-4fbd-3c50-8a53-5afe4141aa91 | -8.96 | -60.5358 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 3302483f-6291-366e-a0f0-5f049f423e68 | -8.9415 | -60.5174 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 5cea1355-ea7f-320b-8316-783d668c22cb | -8.8855 | -60.5586 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 5a719a13-a96b-38f4-9c78-27d448abea89 | -8.8854 | -60.5778 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| b1ddc38b-d6fd-39c5-ae31-9399ccb12753 | -8.9039 | -60.5769 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 145.0 |
| 04a3216b-d387-3cdd-8ca7-fcf919e61f8f | -8.9041 | -60.5577 | 2026-08-10 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 316bc776-6548-379c-91f8-1c0fca5db487 | -8.9041 | -60.5577 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| eff7e569-e8ea-3a4e-b4d2-78654eb548bb | -8.8854 | -60.5778 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| eae156ba-f3bb-38d1-ae83-d4b00a22eb26 | -8.9598 | -60.555 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 469ae3f9-0b3c-3c64-922f-a6cf8270360c | -6.8388 | -56.4146 | 2026-08-10 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 88a45260-905a-3ddf-b022-fd1bb9528e8f | -6.1476 | -57.7215 | 2026-08-10 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2c1b1355-6603-3b38-bf39-2220bcaa024b | -7.5488 | -55.5629 | 2026-08-10 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8f5f504b-3683-3fec-b3a2-396e67b66626 | -10.9326 | -57.1113 | 2026-08-10 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5f9c9ebd-f80c-339b-9911-1ea2adccf3b1 | -9.8107 | -54.8901 | 2026-08-10 00:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e0fa6a0c-b315-3363-a090-6888aa3eea74 | -8.9414 | -60.5367 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| b7d4862c-0d43-31ec-9848-3f0ae45f2266 | -8.9039 | -60.5769 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 172.0 |
| ee84f417-3cf6-3121-9ecf-e49f8c3768fe | -8.9038 | -60.5962 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| c967aa1d-eb08-3b0d-8549-d28ea9532269 | -8.96 | -60.5358 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| 8a8451d9-bb96-3f71-b526-0e80c27e2ce0 | -8.9415 | -60.5174 | 2026-08-10 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ada91d58-922d-3f38-b5c4-db1d91aa4552 | -6.1299 | -47.2884 | 2026-08-10 00:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 44955589-d8fd-32dd-a9bd-b3ee7cb27b57 | -8.8854 | -60.5778 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| d4613125-c7a5-38ce-ade2-1c2001d2a7ed | -8.9039 | -60.5769 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 147.7 |
| edd36dc0-453f-31b2-907c-ffd08394b367 | -8.9414 | -60.5367 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 29b58377-cdb6-359c-9822-1d246b82d83b | -8.96 | -60.5358 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 843700cb-e0e8-3aca-80a9-a20114af59b9 | -7.5488 | -55.5629 | 2026-08-10 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| b3eb1208-81ab-3c21-949d-e2d562c50bee | -8.9041 | -60.5577 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 9ff03e81-e275-336d-b517-5cb7051b61d2 | -6.1476 | -57.7215 | 2026-08-10 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 798dd724-352e-3450-9fb4-fd83dcfce237 | -8.9415 | -60.5174 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| efab9156-9b46-32f5-b6a9-de107cb8d14f | -8.9598 | -60.555 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 2ca7f5d6-4ac1-3505-aaed-910b1f0c1b83 | -6.8388 | -56.4146 | 2026-08-10 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| a24ef920-e830-3fe6-8bee-819e3c29bc2f | -8.9038 | -60.5962 | 2026-08-10 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 467d6f30-7485-33de-8d49-7e76603f8626 | -18.81824 | -49.64822 | 2026-08-10 00:50:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 50dc276a-00aa-381e-b778-a8012c593998 | -13.85255 | -53.6994 | 2026-08-10 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| f5ac8be4-6c66-30d9-829c-4253750ac5d4 | -14.43104 | -58.57671 | 2026-08-10 00:50:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 243ead6a-ca31-3c69-9a39-6f9af6a476ab | -13.77853 | -49.73961 | 2026-08-10 00:50:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 1b3e3a06-8cfa-3b30-a6ec-d04bd50d0a63 | -20.87884 | -57.70547 | 2026-08-10 00:50:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| f1c50313-5cff-373f-981c-3b3260b5271c | -18.82115 | -49.65417 | 2026-08-10 00:50:00 | TERRA_M-M | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.7 |
| 61d90b8f-bcf4-3e82-b22e-8e8db1d73e8a | -13.78349 | -49.73357 | 2026-08-10 00:50:00 | TERRA_M-M | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ea48cdba-8f77-330d-bece-7b3fe61a62d6 | -14.30842 | -54.93507 | 2026-08-10 00:50:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a6a2ea82-6ad0-3f42-b870-230b064f6281 | -15.37708 | -53.76965 | 2026-08-10 00:50:00 | TERRA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 447aa799-ef3b-3431-b569-b6ad49752fec | -13.79683 | -53.92083 | 2026-08-10 00:50:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5925150f-980a-31cc-a6e2-2df5df6fa517 | -17.71863 | -54.1891 | 2026-08-10 00:50:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 23.9 |
| ed3358e7-3aae-3953-9d4f-833f3bce5d9d | -15.06094 | -52.7417 | 2026-08-10 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 670b18b3-202e-3acf-98c7-0420e58b0c25 | -15.06277 | -52.74691 | 2026-08-10 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| f226d041-bac7-354e-8ade-587e8d9e7960 | -11.22294 | -54.04316 | 2026-08-10 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 79fb1742-baa4-3f59-bc98-7c8708629bed | -8.94439 | -60.54295 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 8293fd97-74af-3096-9ae6-c0652d3101f0 | -8.89274 | -60.55942 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a047a63b-1810-34e2-ab1a-186092e01704 | -7.69441 | -55.17252 | 2026-08-10 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 542af6da-9d40-3ff9-aac9-6b71ca7575ac | -8.8952 | -60.57718 | 2026-08-10 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 167.2 |


[Clique aqui para ver as próximas entradas](README2.md)
