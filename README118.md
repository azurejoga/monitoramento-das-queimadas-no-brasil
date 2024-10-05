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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3126a4b0-924e-390b-8c89-0dc3076a485f | -16.13082 | -50.43851 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44d1ffd2-2f27-35a8-bf50-86c85465815d | -16.13026 | -50.44218 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd338348-d1e7-346e-b02f-ea16dd2d8cd8 | -16.1297 | -50.44585 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f70ff3f8-0286-3ac1-a0db-563d35d9e63e | -16.12915 | -50.44949 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54f43dd3-f410-36d6-a83c-255c51a89a85 | -16.12803 | -50.43431 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66718e5a-9407-3ed3-b951-534a0ff84b68 | -16.12746 | -50.43801 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a684507-1f74-3f39-bbcd-ba5f6c4a7a21 | -16.12579 | -50.44899 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ddaf09b8-5578-3b43-aea0-d65db0248265 | -16.12467 | -50.43382 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40816183-e093-3cb3-a3e7-f9433295069a | -16.1241 | -50.43753 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ee2369f-632f-34e5-aa6f-e0ca583431f4 | -16.12188 | -50.45213 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6983d586-19df-38eb-aca9-5b3da1199a51 | -16.11852 | -50.45164 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9cfd6fd-e5e0-319d-bb8b-a8a4a27fbb85 | -16.11797 | -50.45526 | 2024-10-05 04:40:00 | NOAA-20 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131a3105-e6b7-39a8-ab25-869c64bfa9c2 | -16.11351 | -50.462 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc07a5ce-6949-31fb-b718-7ba8715eb83a | -16.11016 | -50.46148 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93286c07-d5d5-330b-be30-7094ba0e13e4 | -16.10961 | -50.4651 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21e88d45-ed1b-307e-81ec-117b26a42118 | -16.10681 | -50.46096 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab83903b-56c5-3166-8a65-1bd5d9504f80 | -16.10626 | -50.46457 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 540078a0-41c4-37c7-9eec-65f38de565ff | -16.10571 | -50.46819 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cbeaf345-3508-33b6-b9d2-22e98864eb36 | -16.10291 | -50.46403 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1a6e76cf-1995-36f8-9aae-ed92b05248aa | -16.10237 | -50.46765 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51f6e43b-6c8d-3775-a08c-eb3b79aa3ae4 | -16.09957 | -50.46349 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 077a7efd-e6d1-31a5-8b7b-096a0a2aff74 | -16.09902 | -50.4671 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acce7d8c-850d-3bce-920d-d7220c3d241b | -16.09847 | -50.47073 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0cc7f7e-89d8-3dc1-aec2-ae3c1bbc4633 | -16.09622 | -50.46293 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 75f5ed73-61aa-359f-ab35-7e6df3f50237 | -16.09288 | -50.46237 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c9e923d-b0f2-33ee-91d5-bdf75c33ceb7 | -16.09233 | -50.466 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0106f6d0-494a-3ed1-a267-d071d12d2c7c | -16.09009 | -50.45817 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a4c9ed70-1b9c-3279-9be8-53269ef33dfd | -16.08954 | -50.4618 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e76f4e6f-9c54-3a4a-b83e-186a7800a403 | -16.08948 | -50.43955 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b1ef276-7c15-339e-9fd1-3cd11d244df7 | -16.08898 | -50.46544 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b362becf-3cf1-3eec-a693-2723b03833e6 | -16.08893 | -50.44313 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b56ce28c-64ad-34ed-b3c8-77f98000756c | -16.08839 | -50.44673 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e43623c1-c433-330d-9643-2b710e5a6c53 | -16.08784 | -50.45034 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 80c96c2f-dab5-35c1-bad5-f8bd01f48ceb | -16.0873 | -50.45396 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 375823c2-371f-3656-b5a8-f89265d00eed | -16.08615 | -50.43892 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f56fdade-47b5-3315-8215-0ea6141bed0c | -16.0856 | -50.44253 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 184fd338-8fc2-3b7e-8132-7a31f5461d4c | -16.08505 | -50.44614 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3bec5f90-9d95-36d2-8d5e-d5380fff018a | -16.08395 | -50.4534 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2269ed34-6d3a-3dce-bc3d-6f41013f523a | -16.08226 | -50.44194 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3f2a03d-dd15-324d-83c8-47020df540a8 | -16.08171 | -50.44557 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab3c8c67-fa24-3ccd-9d17-806d67fd2adc | -16.07892 | -50.44135 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8222beb3-8761-3a66-a709-69539eccc054 | -16.07836 | -50.44499 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f61adb80-4f52-37a0-93ce-b9ec38817a5e | -16.07781 | -50.44865 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49dbdb97-782e-3791-9d5a-07166d3d3280 | -16.07502 | -50.44444 | 2024-10-05 04:40:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 401ac429-3694-392e-8596-610c756608e5 | -17.13369 | -51.72301 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48726d18-45b5-3dce-8e67-a5623749f2bc | -17.13313 | -51.72661 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9883913-01b1-3702-b416-2eb8f2bcae3a | -17.13257 | -51.7302 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80a8c733-8894-33b9-a84a-c575a5c6abc4 | -17.13044 | -51.72274 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| bf5d82b3-6e8d-3844-9c97-261b669bdce4 | -17.12987 | -51.72634 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 71a0c78f-7bca-399c-bf07-dfd42261c5bd | -17.12931 | -51.72993 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4dcce1c4-cb95-3222-b7c8-912de037089c | -17.12818 | -51.73712 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a22ade8-7ab3-3ba9-b3d6-78aec06712e5 | -17.12769 | -51.71859 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9b8d669-ad90-3a91-8ae6-bec5e66ecebf | -17.12712 | -51.72218 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| e90a290a-4a48-3145-a02f-cac21e3c9174 | -17.12656 | -51.72578 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 19845c89-5d87-3982-beef-35b3d23b1bc2 | -17.126 | -51.72937 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c18a55d-c726-3a8b-a413-1955237c757a | -17.12488 | -51.73656 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c4bf2d4-7fc2-3f99-b7bc-de296bd56d7e | -17.12431 | -51.74016 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce941e7-aa74-38dd-8db5-44e854ccbea3 | -17.12382 | -51.72163 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5854c18c-ab23-3160-a108-29e7a8a6de3f | -17.12325 | -51.72522 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22121eb5-1966-3e89-ab06-258432f8d14c | -17.12269 | -51.72881 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a4b4f658-e200-340e-83b3-59c173a73bc2 | -17.12213 | -51.73241 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| df524f4c-566d-36ae-8ea6-27228f854758 | -17.12157 | -51.736 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf55fd69-41e5-3386-92fb-944a51cc8dfa | -17.11939 | -51.72825 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0ac1af39-cece-380a-bef9-e1ba85221725 | -17.11882 | -51.73185 | 2024-10-05 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dbcec450-f2c1-3f6b-8ec6-b7ae1f359a80 | -20.14724 | -51.76957 | 2024-10-05 04:40:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c3238ba4-9add-3dc0-8c41-bacc639ce6fd | -20.63184 | -51.48207 | 2024-10-05 04:40:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.1 |
| b19b943b-2fe6-3aea-a6ee-c8b93e472345 | -20.63127 | -51.48585 | 2024-10-05 04:40:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 42.1 |
| 06c2e1df-24f0-3f51-a348-eb0b53339334 | -20.62849 | -51.48152 | 2024-10-05 04:40:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f8e82d32-cb70-381b-a95b-6cb001594e11 | -20.57996 | -51.39198 | 2024-10-05 04:40:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dac6bc85-0eb1-379a-b701-4840c1401fbd | -20.5794 | -51.39576 | 2024-10-05 04:40:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 89caa70d-27b1-3087-92b6-3e781f368c56 | -20.57604 | -51.3952 | 2024-10-05 04:40:00 | NOAA-20 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3fe42002-a202-348a-b25d-207d195315cc | -20.57548 | -51.39898 | 2024-10-05 04:40:00 | NOAA-20 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c3d426fa-96bd-38f7-8771-7edd09e81d53 | -18.80935 | -53.77175 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f75f81e-894f-38c0-9b64-3d07ecbb4041 | -13.74211 | -51.8802 | 2024-10-05 04:40:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 086f6f89-00fe-3796-9134-8b5cf561e983 | -17.70792 | -53.06379 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcc0ee9d-5c1c-3496-8f63-6710a1faa0d3 | -13.32948 | -51.35861 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c5355bf-8c0f-3f86-811e-d27200c3010f | -13.28621 | -51.24633 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df1f2cec-5e05-32e4-8621-2b8270e5898a | -13.28234 | -51.24932 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c7a4dce-ce77-3521-9384-b887001816f9 | -13.28178 | -51.25285 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc258af1-0a8b-3041-b60c-89fb39dec4f7 | -13.27847 | -51.25231 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61aaa8bc-96f6-3d30-a77a-443e8d6cc250 | -13.27791 | -51.25584 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0d1b8a6-87fd-3a1f-9fa3-efc3784dd3e4 | -13.25362 | -51.25909 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca0809cf-0702-3c96-9532-e7b1e58fcaab | -13.25087 | -51.25501 | 2024-10-05 04:40:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21b3c702-36f4-3ec5-829f-7234b7cb18a8 | -13.19621 | -51.25687 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 38aacedc-2c14-3ee4-bbf2-9c8af40dac3f | -13.18012 | -51.22922 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cd4bad7-5151-318f-9ba2-4f589e7319b5 | -13.16249 | -51.21181 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a33b533b-a6bd-3a4f-8c01-f4bfd47de602 | -13.13603 | -51.42168 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f89ea22-5ce1-3591-ab01-8c87ab065a48 | -13.13547 | -51.42522 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c245f8d6-2017-30c6-9252-2ba2eacb0767 | -13.13491 | -51.42877 | 2024-10-05 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6993d349-383a-3816-8e71-c0ae07f0b28a | -13.81125 | -52.44228 | 2024-10-05 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dfa8fc8-1cb6-3296-bd5d-43cf45e225ef | -17.33031 | -53.19663 | 2024-10-05 04:40:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2caf3f9-2321-3fe6-9a7d-b791d7323596 | -17.73436 | -53.0913 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de1f8ed1-b7ab-32f9-a039-b4a32a065531 | -17.6955 | -53.07675 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05df2268-0e9e-3cce-a6e4-bca5c0d625b1 | -17.70732 | -53.06747 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9311e6b-bf79-3a12-98ed-b88dab9f89f9 | -17.68544 | -52.63558 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75c898b4-c71b-3d47-8654-1843b5f60af0 | -17.33208 | -53.19639 | 2024-10-05 04:40:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3988f3e-5728-3e7c-b362-a2d3cb796682 | -17.71459 | -53.06497 | 2024-10-05 04:40:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0cc2b1c-2db4-3e38-ab7a-7b363c02e38e | -18.82535 | -53.75898 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65a2a618-bd8f-37fd-a805-ee2b574818dd | -18.82135 | -53.76217 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb94e0ed-1982-3bf6-a87c-e03a188261ee | -18.81798 | -53.76156 | 2024-10-05 04:40:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README119.md)
