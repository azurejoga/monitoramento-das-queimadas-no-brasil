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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3bc46ec-e435-3eb4-b459-07c3d48a58cc | -15.90509 | -50.15967 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d2544d2-d8a8-382a-87c1-3d211db3dfd8 | -15.90287 | -50.1429 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c0dea4c8-5ee7-3cb2-8921-f729f72adf1b | -15.90221 | -50.14617 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13aad620-ef50-3d8d-8329-858e69de25f2 | -15.90144 | -50.14998 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f43041e1-42e5-31b9-b28e-0839175c65c2 | -16.37628 | -48.85552 | 2024-10-02 03:55:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 267df42a-e0d1-392b-bb08-68a89e26311d | -17.00832 | -49.78201 | 2024-10-02 03:55:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d45a81e3-a336-3062-bf20-428ca53926cc | -19.24863 | -50.89289 | 2024-10-02 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 308be636-1181-3ebc-8fee-68d041531dce | -19.2479 | -50.8964 | 2024-10-02 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be8d830c-de69-31bc-b524-7536c808d8ed | -19.24266 | -50.89507 | 2024-10-02 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f3315600-1485-3992-ac49-fe8db8c762fb | -19.26406 | -50.84528 | 2024-10-02 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f62cab10-7670-3841-84bf-3d08deea74d7 | -19.2636 | -50.84249 | 2024-10-02 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0a935f5d-4153-3fdf-a56d-6ed8eee259e2 | -19.26286 | -50.84592 | 2024-10-02 03:55:00 | NOAA-20 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45b752c1-54ce-3db6-98b4-ef85bfe74c7f | -13.61379 | -51.16433 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b2d2f095-5688-3a2a-89f4-b9ab6a95003f | -13.60877 | -51.15851 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2220e5b-33c0-3561-910e-b2d258491072 | -13.60785 | -51.16302 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2481e30c-41ae-35c0-ba56-dc0e745ed926 | -13.58966 | -51.13071 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e7c055ad-6b97-3928-ba3a-e8dbbf34ab0f | -13.58873 | -51.13522 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 82897070-b4fc-38ea-9f8a-5908b528a063 | -13.5878 | -51.13972 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| d16c6bce-973f-3f73-9eec-9c050e41c37b | -13.58373 | -51.1294 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7e2b984a-190f-31a5-90d5-b10911b50c9e | -13.5828 | -51.13391 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c8f234b1-3cb2-39d5-ac47-6e5914b5286c | -13.55532 | -51.19547 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 013db1d2-46e1-37a3-857a-ca47198a494c | -13.5544 | -51.20002 | 2024-10-02 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8760bf66-1208-34f2-ada5-7df208b17592 | -13.21125 | -51.2099 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 734bd70c-6cfe-3fae-bd94-146ec6acb497 | -13.20995 | -51.20995 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 789130c7-99f6-36f3-9ab6-89fcaca023d8 | -13.20621 | -51.20398 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47262b21-be4e-35c3-ac43-e5322c893907 | -13.20525 | -51.20858 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02424d37-21a8-3378-8b2c-c6170a94e895 | -13.20395 | -51.20862 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e76dfe08-156a-392c-927f-44dfc3894888 | -13.10788 | -51.1876 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8591aab6-6be5-3167-9833-a8b850df8ed8 | -13.10623 | -51.18856 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30aacefb-1a87-35a4-9280-c8f0c0d51bc2 | -13.10187 | -51.18629 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99895c4e-a5eb-3ef3-ab79-f72eff528d14 | -13.02925 | -51.16008 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23b45b10-817e-37f2-bef5-476d0ed4ae3e | -13.025 | -51.15629 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bcbe987-5ec7-3243-9b0f-a21f0968a157 | -13.02404 | -51.1609 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bece119-12bb-3e5e-bc0b-6e477d4e267b | -13.02324 | -51.15876 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2edbadc9-d9e0-32cb-96f9-d08c6be8b9ff | -13.01804 | -51.1596 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bef8f3fd-56d8-3d68-a064-859c3668eb21 | -13.01724 | -51.15743 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4c3c5fb-3dd7-313f-965d-4698bdf34aa6 | -13.01632 | -51.16206 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8784369-bd0f-32ae-9e44-d90897408094 | -13.00294 | -51.13501 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61074314-553d-39b2-bf2d-0997e3fe0927 | -12.99694 | -51.13367 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 856bb57a-a208-3e78-be14-0ed55674e73f | -12.99602 | -51.13828 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f153cffb-c519-34b9-a677-4a6f48c2e00a | -16.10547 | -50.4144 | 2024-10-02 03:55:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3f2ac198-860e-34ae-bf20-315f62a88ac8 | -16.10313 | -50.34427 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50309476-ef81-3ba5-ba43-02717470e628 | -16.10297 | -50.31805 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f78927a-98aa-3506-be55-d25af49b1e1f | -16.10265 | -50.31166 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdcedce4-6218-3c73-9ca1-b12d86f469d6 | -16.10242 | -50.34766 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1b981ad-8e86-33d3-871c-90b6f310c231 | -16.10223 | -50.32157 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c26da5a-ffd6-3d1f-b429-f3253b563aeb | -16.10194 | -50.31517 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b179520b-c5b5-3062-b718-1d748854bbe8 | -16.10158 | -50.34492 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b870996a-1d57-3c78-8ba6-1d8287a39217 | -16.10151 | -50.32505 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd9fddbb-c729-3c7d-8d9f-4d2410267777 | -16.10123 | -50.31873 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2501d1fb-6517-3e1d-a24c-80ffdd2f34b3 | -16.10089 | -50.34829 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7053933d-b919-3837-9ce4-634f0d041186 | -16.10079 | -50.32848 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| da51f1e5-fde8-3683-a1cc-6d9a8079e691 | -16.10052 | -50.32225 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf38e009-3001-3332-810b-9f8aed334508 | -16.09982 | -50.3257 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 494932b4-c658-316b-af75-bedc6919373d | -16.09912 | -50.32912 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66c8f693-2013-35d3-bcaa-777a3bd78d5c | -16.09725 | -50.34536 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da7195fe-8a55-380c-9ab6-c01bd02cb893 | -16.09672 | -50.31312 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f12cebf6-9157-3b45-a39f-56bf69fd1ea2 | -16.096 | -50.31668 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d43dc14-2ec9-31c8-8ee4-dfb204acbd0c | -16.09328 | -50.36428 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a280ff1-b815-3c8d-926f-21a98cc37434 | -16.09237 | -50.36866 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f931fb95-a572-3605-81e2-74518b56e55b | -16.09176 | -50.36554 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7c47d4b-538e-3a13-b1a9-4d4b853b7025 | -16.08645 | -50.36384 | 2024-10-02 03:55:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 901df0e6-cd7a-3e5d-9798-bd264930300c | -16.07863 | -50.34669 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b460f8b-942e-35d2-bd9f-b7b6804caf8c | -16.07802 | -50.3497 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e5989e8f-1d8c-35f8-8179-3808324fda26 | -16.07629 | -50.41405 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5e8feb0-6af9-342d-9b3d-89b4b4f4c69a | -16.07298 | -50.34674 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a87459b-7446-37b6-ae42-2b1a457159fb | -16.07232 | -50.34998 | 2024-10-02 03:55:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bcca2c6-2939-3fde-b172-c68159cff149 | -18.24977 | -50.82767 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad660796-7c5d-33f2-b874-81a326307e63 | -18.24673 | -50.8155 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 27dc350d-82fc-3bed-971e-c73bef60c89c | -18.246 | -50.81895 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5734b5df-8b8c-3097-b7a6-ef96d483447e | -18.24528 | -50.82242 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8834fe72-7a48-357a-967b-1fc687950bb2 | -18.24454 | -50.82591 | 2024-10-02 03:55:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| debf5227-6bcc-3508-ba3f-2d7cbde1c22c | -20.0848 | -51.33676 | 2024-10-02 03:55:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4059ac45-dac0-3e5c-b613-0fa4b567290b | -20.08405 | -51.34023 | 2024-10-02 03:55:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95dd4bde-4fca-3b93-9bae-3289bf12ccb5 | -13.06778 | -51.37984 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58757199-e118-35ed-96d4-18ea7b0bb890 | -13.06741 | -51.38134 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ceceb6d-a45e-3a86-9c17-ca9a04537e92 | -13.06678 | -51.3846 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 87d0b193-8cd9-3bf5-ac90-67819b09966e | -13.06422 | -51.36571 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 02141c69-79f5-3557-8069-aaf47d351d99 | -13.06369 | -51.36902 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f794d4f1-208c-3bc1-886d-b189577ea739 | -13.06325 | -51.37048 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c84ee369-154b-34e2-bd42-fe0e116b52e6 | -13.06269 | -51.37377 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5155ee4f-6720-3235-818b-c12e173f7507 | -13.06229 | -51.37524 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6b08599-5886-3c06-a05c-6ac13fdd74fd | -13.0617 | -51.37852 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| af60ec8b-9cee-35fd-950c-86142e892174 | -13.06133 | -51.38001 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0d630d2d-c28a-32bb-94e4-01e8e9daaa48 | -13.06079 | -51.41327 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 99b0b2b3-a138-33ef-86a1-0034f9b3c7f7 | -13.06064 | -51.41488 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 57ef9dc1-4719-35c9-b1a1-1aa2f5eb355e | -13.06007 | -51.35485 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4720614f-c1a4-3143-8bb7-583c537fa697 | -13.05979 | -51.41806 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7026d8fc-d23e-35b4-bf83-e9b6845664f3 | -13.05967 | -51.41967 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1a74e1d6-fdf6-31d2-b7c2-0c764743af70 | -13.05878 | -51.42285 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| ad2ad28f-d03d-39ee-82d3-a5cf684b06a5 | -13.05649 | -51.40393 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b9c8c8df-a001-3508-924f-9e80ca36a8a7 | -13.0557 | -51.40716 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 879ba063-7b7b-3b14-a957-b5a05961b4b1 | -13.05552 | -51.40872 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c9067a67-e4dd-3243-8a90-5b3d1c224668 | -13.05524 | -51.37868 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b848533-364f-3013-8eca-8caf8bc033c0 | -13.05496 | -51.34876 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73fa13bd-63c1-37c0-90b8-2f7e9005ba33 | -13.0547 | -51.41194 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f4fbf226-b113-3099-91ce-4d2c9bfe9227 | -13.05468 | -51.31894 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65b971ed-3e55-3c59-ac50-e7096aad1ab0 | -13.05455 | -51.41352 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 6d3ff837-b06b-3ba4-ac99-30c1d0b418b8 | -13.05371 | -51.3237 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3ef723c-2d9b-3c74-872d-3769c1c286ae | -13.05369 | -51.41673 | 2024-10-02 03:55:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README75.md)
