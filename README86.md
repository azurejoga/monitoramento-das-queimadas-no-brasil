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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fed2bb7a-e702-3b71-ab9e-8cfd41574d2a | -13.93589 | -44.52573 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 146bcad8-27ab-3916-b4a6-2f70b74c634a | -13.93534 | -44.55102 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0172390d-f8b2-378a-8f5f-c881ce6bf78d | -13.93534 | -44.52927 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fc7391ee-db5f-3cdf-acf5-7ee318615186 | -13.93369 | -44.53988 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ac749d1-ee6c-3bac-9145-6c89e975e679 | -13.93314 | -44.54342 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 14d84938-1fcd-37a1-81ca-ac8b51843d0b | -13.93314 | -44.52166 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e5801d3-1e62-3bf2-8734-ff091f3e1560 | -13.93259 | -44.52519 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 145a70bb-40b0-35f2-9215-60644539ff94 | -13.93258 | -44.54695 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44104dcb-3f26-313b-84e1-dd930a671ebf | -13.93204 | -44.52873 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e357fa7f-85e7-3bae-af67-9f677c7fc331 | -13.92984 | -44.52112 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf5c1881-ece0-3549-9024-281fd443f0ab | -13.92983 | -44.54287 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eeca4165-7e45-371c-acbd-63070455c95f | -13.92929 | -44.52465 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54ac2b40-e82c-39a7-ab85-3e6a1d76a6cc | -13.92928 | -44.54641 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ef18457c-008f-347d-86dd-1f7933fa0a80 | -13.92874 | -44.52819 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1045c782-baf8-3334-be39-517db5035061 | -13.92873 | -44.54994 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1958d87d-6b08-3b5e-ae85-87c8704fe734 | -13.92818 | -44.53173 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 662a76d4-803e-3704-994b-3016701b3d47 | -13.92708 | -44.5388 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 08e5e71d-a2ae-3d91-8b65-42300f6a88b0 | -13.92653 | -44.54234 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06f1803c-755d-3840-8f5a-d3f2e8c5b92d | -13.92598 | -44.54587 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 413437d2-2555-35a4-979a-583ad700dac0 | -13.92598 | -44.52412 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51608e26-2f62-3249-96f0-5ad48629781c | -13.92543 | -44.5494 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d38be52-c7ee-3c03-8388-838c1a6efa45 | -13.92543 | -44.52765 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8888c453-d490-36ec-b65a-d5b982f2fef2 | -13.92488 | -44.53119 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe1cd9c2-475e-3c01-86b0-db18973602dc | -13.92433 | -44.55647 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d60bc98-bf03-39f2-ae10-b0b1cff8d78d | -13.92433 | -44.53473 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 749c6a69-becc-37c8-b51c-5f0a875fdffd | -13.92378 | -44.53827 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c47d94ad-80d4-3f7e-81bf-1a46635a010f | -14.48322 | -44.96405 | 2024-10-09 04:17:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7eff79d-1077-3baf-85c8-8a379b9e0bae | -13.8814 | -44.52773 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddaad64f-ebe8-364f-bf91-b98c832f9798 | -13.8792 | -44.54187 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d5fa4f52-8bc1-36f7-8cf5-45d3ed6c21fa | -13.8726 | -44.54078 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e180e8ac-930b-38b2-864f-106a59090a20 | -13.86985 | -44.53671 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67d339e4-fb12-383c-ba8e-f86af18a66e6 | -13.86654 | -44.53617 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 21469c63-8e75-3732-a4af-ce6a87b5d84b | -13.86544 | -44.54324 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c59b0145-5129-3b76-bcdc-10408575594c | -13.84283 | -44.57605 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d545d224-192d-3e39-afe1-2276097a53d6 | -13.84009 | -44.57198 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3e5048d1-424a-3cd4-b35c-068c259e51ee | -13.83953 | -44.57552 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79579c85-d94d-3cd9-8ca4-f79784c80674 | -13.83623 | -44.57497 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ffb1f030-51a0-35bf-b688-446d542e8af2 | -13.83183 | -44.58149 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5e3ccbd0-e98c-32da-8fdf-b50b32a10183 | -13.83018 | -44.59209 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd6d8e62-f6b4-351a-8158-5326279b7fa5 | -13.82522 | -44.60215 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8a7714a6-4e8e-339c-a9b4-1acfe2253bf1 | -13.82357 | -44.59101 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 08b8699d-b0a1-352f-affe-cc3d83d013f0 | -13.82192 | -44.6016 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 68c11309-4e9d-35a1-aa84-e237f49ccccf | -13.82137 | -44.60513 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dbec9721-fbc2-37d3-849c-f424137dde88 | -13.81917 | -44.59753 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| edd7683d-9ea8-326e-b6ac-e394143b9b18 | -13.81807 | -44.6046 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5d6d9404-02a5-315c-9db7-4c98ecd501ee | -13.81641 | -44.61518 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f5fad98b-9d7a-368c-a5ac-e716dc981006 | -13.88195 | -44.5242 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c9dba44-4c9a-3d7d-a4d3-d4c82c9abb33 | -13.88085 | -44.53127 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bfb294b-0ba8-3a37-af09-ba668fa41f25 | -13.87645 | -44.53779 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f80a14a-f416-3972-a9be-04715675fd00 | -13.8759 | -44.54132 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f6b959f7-80ed-373a-9dbe-56db2d51cb86 | -13.87205 | -44.54432 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4255b589-d72e-39a5-94ec-0100d219c0b6 | -20.65369 | -45.89357 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 573e7f4d-0137-3ec8-96b4-5d5da14dc2cc | -13.8715 | -44.54785 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6769a11-f445-3ac2-8e48-1a24578ebf72 | -13.8693 | -44.54025 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98ac042b-81f7-30b5-ad6f-6ed875c0d682 | -13.86875 | -44.54377 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0be33e8-56cf-39e2-b13c-38d66b204bfe | -13.86765 | -44.55085 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a30d2000-9abc-332d-9577-d812d4426f6b | -13.86489 | -44.54677 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37870cd1-3ec2-3a87-a51d-bfef2c5927c0 | -13.86379 | -44.55384 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e09c68b-643a-3759-a10c-ed023156d12c | -13.86104 | -44.54977 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01308f24-9a82-34e9-9fe5-beec40947d0f | -13.84669 | -44.57306 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84bf831e-bbc4-349a-8464-834e793a161a | -13.83898 | -44.57905 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34d17641-763f-37e9-b2e9-c65e9bdb3618 | -13.83788 | -44.5861 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 87204c20-e9d4-3fd9-a1ab-2f65621e8e6d | -13.83458 | -44.58557 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1b2ebdc5-d897-3bc6-887c-4d3b303cb65f | -13.83128 | -44.58503 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 7781c034-1950-360e-aafa-a6cbf149b5c2 | -13.82798 | -44.58448 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| c609d92c-9fb4-3af0-81e1-510bbcaef0b1 | -13.82467 | -44.60567 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 756aae69-8d9d-3f69-b79f-784e95d2681f | -13.82247 | -44.59807 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ef82b473-b11e-3ccb-9642-e67536e0fabf | -13.81972 | -44.594 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d9cff2f6-edd3-393c-93fd-fd5c2a03f325 | -13.81862 | -44.60106 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0362ef8f-b67c-371a-8620-a9a34630db18 | -13.81476 | -44.60405 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46a0a743-a2c1-303a-8b77-49d5d7907986 | -13.81202 | -44.59998 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 3430c0b8-8ad2-307d-8b35-1a23ccb8764c | -13.87802 | -44.13122 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 983f287b-1bc6-3b4b-8b32-457ce341e064 | -20.81591 | -45.63212 | 2024-10-09 04:17:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ca58c8e3-876b-32f2-ab28-982e15c414b0 | -20.66751 | -45.89207 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e4a9f9-5d43-324b-9277-9e40be24eff7 | -20.65748 | -45.9131 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 066927fa-e073-3c4a-93df-4905c29d9304 | -20.64254 | -45.92183 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5fbde1e9-585e-383c-9e99-d8ed71ae8365 | -20.6381 | -45.92857 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3cd89e2c-3716-3b10-bd5b-7cd8e5d5e475 | -20.36314 | -46.36301 | 2024-10-09 04:17:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaf90d0f-b64f-35d9-8af6-bf263f6c4035 | -20.36257 | -46.36667 | 2024-10-09 04:17:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba334b6a-7d8e-3aeb-b195-69bde9c84270 | -20.32706 | -46.15791 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2f33dbd-e5a7-3531-826b-48397f16eb76 | -20.32376 | -46.15733 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8fab841-b3a2-3902-aa57-b90771c80dba | -20.05526 | -46.37339 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cabd1ce-7dd0-3cf5-b0b2-e280ca539228 | -20.05469 | -46.37703 | 2024-10-09 04:17:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e55469ed-2b74-304e-9d93-dd8569eb2cb6 | -19.86894 | -45.69198 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84f2b49b-32a5-33f8-80e0-633d9f24676a | -19.80507 | -45.62076 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b79871b2-dfa9-377c-bf46-fed90ba2c76f | -19.80176 | -45.62019 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 51c41832-00ae-347d-8cc8-96527dc11e38 | -19.8012 | -45.62387 | 2024-10-09 04:17:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f75d449b-a387-359e-8092-757657ba2d8b | -19.72303 | -46.15076 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d886170f-72c7-30a8-8651-92c68948a2ec | -19.66596 | -46.23111 | 2024-10-09 04:17:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4a1f9aaf-85e0-392e-8382-d64c8e965201 | -20.81648 | -45.6284 | 2024-10-09 04:17:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 31b73e18-d5a6-35d6-9b70-ee518ec09369 | -20.67082 | -45.89262 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4c040fc-2cf5-3e31-82d8-16e95aae3016 | -20.67025 | -45.8963 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7f6304a4-760c-3777-bfa8-b7fdb9d2c673 | -20.66969 | -45.89999 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66b8b1ec-e68c-3a90-a9de-2e5343742ee2 | -20.66581 | -45.90314 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b94fe36-885f-35ab-a1af-65bb0b44bc00 | -20.66411 | -45.91417 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 184e658e-7ac5-3d60-9c0f-6957ebea2295 | -20.65974 | -45.89838 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abca4489-7890-3443-8542-39cd9e91bb85 | -20.65643 | -45.89782 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97ba1d82-cef8-32ef-bd12-2f37b4104cd2 | -20.65425 | -45.88989 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 27b5c94c-a4de-3854-86c5-9c9163a64728 | -20.65037 | -45.89301 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2f58f4f-9958-308e-9745-eca1fbaccfd0 | -20.64085 | -45.93283 | 2024-10-09 04:17:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README87.md)
