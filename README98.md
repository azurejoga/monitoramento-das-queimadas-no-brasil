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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c45d2ab-6f93-358b-b3f6-bbb21a21a8d6 | -13.59405 | -51.14889 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c28afb0-d2c5-3ad2-b5a0-e21ca5f9cd3c | -13.59349 | -51.12992 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57c9d4d1-aec4-3f41-b7f3-6013e6d5ad2e | -13.59237 | -51.1373 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abac52da-8071-36be-8fb6-5a48787421b6 | -13.59124 | -51.14467 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44c04afe-b870-3a93-9291-1aa80cb9b327 | -13.59068 | -51.14836 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dc30efb-cfda-3510-ad1e-76760a28ab18 | -13.59011 | -51.12939 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0c6746a9-9f9f-3a4a-8e8d-c8397cfd8ebd | -13.58955 | -51.13308 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a6c18a99-9cf2-3cc7-9d3a-57bc7c9f0358 | -13.58674 | -51.12886 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e52f7fca-61a0-3673-89a8-5d9b8d809d7a | -13.58618 | -51.13255 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0bfc1d33-0223-37a7-a3e8-131690c7c20c | -13.24414 | -51.21457 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 608012ef-85b9-3087-bb1c-6b4ceca3b3de | -13.23798 | -51.20985 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483baaa2-945f-3114-b819-e7b33df3c1d0 | -13.23742 | -51.2135 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6417e7c4-0a77-3a4f-98e5-c968e0733713 | -13.23687 | -51.21716 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acc09249-edd6-33b4-aec6-ff1f93c11e53 | -13.23462 | -51.20933 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a341772-2c11-3923-b185-1a5b5511acb9 | -13.23293 | -51.19783 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0dd99c9-33f8-3202-829b-946978b2fefb | -13.23126 | -51.20879 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d01440e6-d7e8-37d9-8419-5581e02fcb9b | -13.22004 | -51.19205 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 83f9a00d-39c0-3d30-b826-b43543f3de90 | -13.21391 | -51.20979 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8ddc212-d154-354a-bb31-dc561a3d3bb8 | -13.21111 | -51.2056 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 380fc957-531e-3359-aa8d-1b1bcea2190c | -13.21055 | -51.20926 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4400d0df-8fa6-39c9-8d75-c60bb87c82ff | -13.20885 | -51.19777 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca94cfc0-35a3-3d5c-84f4-4bc2744ae79e | -13.20775 | -51.20507 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5bf55117-d4d6-3f2a-af38-f993d9b0e3dc | -13.20605 | -51.19358 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1b1b3c2-b41c-3c0e-b4b1-31197eea3e2e | -13.20439 | -51.20454 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 905ff2dd-98f0-3eac-9923-076c84509648 | -13.20384 | -51.20819 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 77dad545-faa9-3e67-b885-9315e8315332 | -13.20214 | -51.19671 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1e2287d-6daa-3132-93e1-a75be662657e | -13.20158 | -51.20036 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45207444-b82c-3b6a-ad5c-932f0ca54794 | -13.20048 | -51.20766 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8423c62-de7d-30ea-8dd2-6b332b2b46d9 | -13.19712 | -51.20713 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 189c2ed7-b84c-35ed-9433-e49b8ea7c962 | -13.11209 | -51.18668 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59e6ad69-bab8-39a1-805e-187c0abb90d4 | -13.10537 | -51.18561 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f01fa8e-9c73-3a2b-9c43-0b482ce98cd2 | -13.10482 | -51.18926 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 65a4dc4c-9590-32a6-ba36-7a7c3d746d38 | -13.10146 | -51.18872 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da751675-9480-35ad-9024-1a9d7d01e323 | -16.0892 | -50.36516 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| c1dfbf27-eb4d-3d9e-9c92-8d8f7906e7b5 | -13.0981 | -51.1882 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 36ffc430-6ca5-3eef-85c1-c5b25e4fd58e | -13.05719 | -51.16304 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| caddfbfd-b1a6-340e-9808-474c70404ce8 | -13.03495 | -51.16007 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8791b60-45ae-3f51-a7e0-48f11099cc51 | -13.03215 | -51.15589 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3ff93fe-f7de-3589-a779-c44e2ac820eb | -13.02879 | -51.15535 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb2eee67-aeb4-3047-a3a2-73b7857ddc9e | -13.02543 | -51.15482 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f34e83e5-d029-3e83-b281-87800b5d47d7 | -13.02207 | -51.15429 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 886de4cc-44c6-3d80-82ec-b76f1cc8e055 | -13.02152 | -51.15794 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f14f7e8-e330-3b27-a166-c0d8872398d9 | -13.01816 | -51.15741 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db0d4c11-c361-3aae-a680-06f3274537a0 | -13.00469 | -51.13285 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b8a630b3-8ad3-3a53-8ee9-12972220c39f | -13.00413 | -51.1365 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 820d2064-e7a4-3b34-9b83-95940922fd34 | -13.00188 | -51.12866 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c434d4d1-d4a6-3212-9ae1-827eeeaed196 | -13.00132 | -51.13232 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c9495c18-61c3-340e-9559-8dcdbfe3e86f | -13.00081 | -51.15841 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b91ff76-5c70-332d-9c1c-8234e7094cef | -13.00077 | -51.13597 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6580bbc7-ea8f-30b4-b63b-93e50fb1e622 | -12.99796 | -51.13179 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62347ed8-80df-3535-9adc-b0c3698e0004 | -12.99129 | -51.15317 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15b79ffc-41de-37c9-a87c-b714f74ba613 | -12.78795 | -50.59191 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6669c7c4-2029-3d11-8a2a-3c5743865808 | -12.78738 | -50.59567 | 2024-10-02 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e1a696d-3037-37a3-9ae9-8f5eb41479ca | -13.93583 | -50.88469 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2519f865-7be0-330f-b3f7-0836447e76e6 | -13.93242 | -50.88415 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65c92072-d235-3ef9-b7c4-65cf30c1e90e | -13.93241 | -50.86097 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 461302ad-a5af-381a-b253-38b807367954 | -13.93071 | -50.8723 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d94e1db8-62f9-323f-ad33-0a59d68a86d5 | -13.92958 | -50.87985 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f507332e-54ef-3e9e-bdec-82ab08837802 | -13.92787 | -50.86799 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c540e06-ce43-3d8f-acfb-ef50cf0b1c15 | -13.9273 | -50.87176 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd78a525-0ce0-3a0b-99a0-327e73084129 | -13.92674 | -50.87554 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca53c8e5-ae7f-33e6-acbe-d2f18083bdaa | -13.76145 | -51.13704 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f690c89a-ea11-33f2-95af-27b7a470c39a | -13.75863 | -51.1328 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9224e233-9934-38ed-a0a5-b7999973044d | -13.75807 | -51.1365 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c503c474-5a68-3d12-b7ca-8e3e2c423ecd | -13.75636 | -51.12486 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74efa8cd-3da9-359c-92be-6e21bcbde01c | -13.75581 | -51.12857 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b73443fc-5ae9-3a21-a3b3-6e16f723b96b | -13.73088 | -51.06389 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9df122f5-95d0-3e7a-a53a-a247219e1abb | -16.08565 | -50.3647 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6aaa7530-9610-3898-bd2a-096a1ee71a82 | -13.71423 | -50.86675 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74d90a48-887e-352a-a6a9-e776328f554b | -13.69332 | -50.91341 | 2024-10-02 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d0abc56-76f4-34bc-b6c6-f6f9a8ef7aea | -16.1063 | -50.34544 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62919de3-bc4b-39b7-a32a-c9f009745e1e | -16.10582 | -50.42585 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 489290a6-f727-3b56-a0ac-6a6df15ed8c2 | -16.10571 | -50.34966 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa8c58b3-d143-31ed-a2f1-fda30231fe65 | -16.10415 | -50.31213 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 020131c5-8692-3b83-898e-55810138cc3a | -16.10407 | -50.41262 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c33faa4-2d0c-33d3-aa56-a51db563408a | -16.10355 | -50.3163 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4ecacb01-6068-351b-96a5-f08b4e8b75fa | -16.10328 | -50.31527 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe4d1e6f-4988-373d-9a7f-9894c1cc0a22 | -16.10294 | -50.32047 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ca9f90b-7ef2-3bdd-8d6d-d5e331851aa7 | -16.10286 | -50.34602 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 521b12e6-4b3d-36bf-9bc6-d357ffd1ab8e | -16.10273 | -50.34504 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd7b90cb-4911-36f9-b489-381ddc9291b7 | -16.10233 | -50.32466 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fabd098-703b-36c9-ba03-5d0a5ea4702d | -16.10214 | -50.34927 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e2bbe03-2a89-35a5-8345-9a2ef649eabf | -16.10211 | -50.32363 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d8b65f33-fe0b-3379-bba7-1da7896e5d39 | -16.10152 | -50.32783 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 701138a2-8c1b-3367-9f0f-704427fbc860 | -16.10058 | -50.31173 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9ac41485-4284-37a9-bc69-7bef08642033 | -16.09998 | -50.31589 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b4f6acb-b8fa-31d8-b49a-8d36ca4af2af | -16.09687 | -50.36223 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5c9b92a3-921e-3a81-864f-df3684a8090d | -16.09629 | -50.36621 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e5221a06-c894-39ef-9b46-7325e791c2fa | -16.09627 | -50.3653 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9d44fffa-662c-3188-948e-03770b776248 | -16.09332 | -50.38668 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f41f8df-60aa-375f-9403-a928510e5dd7 | -16.09281 | -50.38993 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cbbae902-83c7-3709-9435-f65e80f26d70 | -16.09275 | -50.36569 | 2024-10-02 04:49:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 07c2f44d-0af9-3efb-b4f7-e2d30c312762 | -16.09098 | -50.37783 | 2024-10-02 04:49:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 534aa217-f23c-3272-80b1-329bb0bec8ac | -16.08931 | -50.41486 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 346bc043-b281-389d-bd07-1e20c12ada8b | -16.08908 | -50.41576 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0e5579e-74f1-30e3-a6f8-cb6b06adb42c | -16.08685 | -50.33136 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 06bdd3a7-4d38-36f3-aab9-2f2faaba6d2c | -16.08511 | -50.31837 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b83daada-5e85-3bac-9bb6-9ea708a6b0aa | -16.08452 | -50.32244 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 544f7af5-0b3f-38ff-92cb-801266d15720 | -16.08444 | -50.34807 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b98c423e-8259-3335-8f2b-d714b8a6ff29 | -16.08335 | -50.33052 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README99.md)
