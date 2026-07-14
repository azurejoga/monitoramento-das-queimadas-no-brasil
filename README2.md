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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00bf276b-e00b-3a3a-aa59-035a78b4e107 | -8.5175 | -48.0577 | 2026-07-14 00:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| b3f0b4ae-d6fd-3248-9925-eacbeb89709d | -8.4987 | -48.0594 | 2026-07-14 00:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 11288037-baa7-334e-a4fd-d37cbc5d8ba6 | -10.092 | -50.1085 | 2026-07-14 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 7b5a80e6-acf8-3b56-a089-b10993a7b79b | -18.7743 | -52.4061 | 2026-07-14 00:20:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 4c443392-69c0-3614-9c93-50d51c4f7fc7 | -10.0728 | -50.1318 | 2026-07-14 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| e4ad3d83-c970-3aeb-862b-5be1ca7be94c | -10.0917 | -50.1299 | 2026-07-14 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 6ae91838-0d45-3148-a337-d230999e7bda | -8.4985 | -48.0813 | 2026-07-14 00:20:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 34eba3f7-d146-34d3-9ab3-09665c5b09b6 | -10.0731 | -50.1104 | 2026-07-14 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 04b6127f-b1d4-339f-8992-dadeddaef3e7 | -18.7943 | -52.4027 | 2026-07-14 00:20:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 50.0 |
| d62090bd-f1f7-3701-bc8e-a09f11bbab02 | -6.493 | -42.232498 | 2026-07-14 00:29:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c38ce62b-7f41-3f27-a890-91ec8a9e8741 | -8.7259 | -48.324299 | 2026-07-14 00:29:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3a86cc2-cb11-3ea5-8cee-20547051ff9c | -6.491 | -42.2239 | 2026-07-14 00:29:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 879891ee-ae0f-35ed-a56e-6d122b7ff66b | -5.2422 | -44.9263 | 2026-07-14 00:29:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de11894d-bc7b-3170-9a03-394b369703f1 | -5.8267 | -43.484798 | 2026-07-14 00:29:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7089873-3727-38e6-9c31-c47a2d20b7d8 | -8.5053 | -48.068001 | 2026-07-14 00:29:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4a48aac-853f-309c-9722-762565910c7a | -18.1759 | -46.914799 | 2026-07-14 00:29:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6cfb5191-650a-3d50-976c-e225c888fc89 | -18.778601 | -52.418499 | 2026-07-14 00:29:00 | METOP-C | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7eb1c924-4d89-33a6-86c3-eb5165d4abcf | -18.166201 | -46.917 | 2026-07-14 00:29:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1be6c3c8-55ed-35b4-b0f9-b1a74c6ff948 | -4.0175 | -48.0546 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0372e603-da17-3839-8372-3a493dac2118 | -8.8311 | -48.335899 | 2026-07-14 00:29:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24911a28-3469-3ded-a1ac-b95cba8cede5 | -7.7783 | -45.509899 | 2026-07-14 00:29:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6d3b8b95-28ce-3ad4-9e97-151781651899 | -7.0236 | -42.777599 | 2026-07-14 00:29:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eed8802c-e347-3cc1-9a50-c376696d5d31 | -18.765301 | -52.399502 | 2026-07-14 00:29:00 | METOP-C | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 83ecfa6a-1294-3237-91f7-37fc69ed3940 | -18.775 | -52.397701 | 2026-07-14 00:29:00 | METOP-C | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6b96af1a-e24b-38e0-98c4-213dd7644b8e | -18.164301 | -46.907799 | 2026-07-14 00:29:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2fde269-1132-3ffd-82a5-2e588bc73b7a | -12.4425 | -49.576401 | 2026-07-14 00:29:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6bba2ad9-d8d6-3b6b-a46d-121417a6c919 | -5.8365 | -43.482601 | 2026-07-14 00:29:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a786e310-72a4-33fb-bd4a-3b6c959c2ef3 | -9.0284 | -44.257 | 2026-07-14 00:29:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2acc6c21-ce42-3d42-8ead-ccf819463759 | -4.3725 | -47.757401 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd4ee9ac-0c1a-3965-96c7-c0a4649d8a49 | -18.174101 | -46.905602 | 2026-07-14 00:29:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a28d4067-073a-35e2-9536-e50abc76b644 | -5.3074 | -47.2458 | 2026-07-14 00:29:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12037bc6-d38a-3058-befd-c5cfa167d66b | -5.8347 | -43.474899 | 2026-07-14 00:29:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92e0eef1-f8ee-301d-ab0e-ad70b8e3a77f | -18.167999 | -46.926201 | 2026-07-14 00:29:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e2ffdd9c-2ca0-3f37-aee7-3abcb1fc7874 | -5.9384 | -46.3479 | 2026-07-14 00:29:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a04368f9-6d39-3878-af2b-5caf10f69149 | -10.757 | -42.102402 | 2026-07-14 00:29:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b48dce72-246d-3db8-87a4-b4e06f5a3e27 | -4.0191 | -48.061798 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aeddec1-b83d-394c-861f-fd767625a439 | -10.0651 | -50.119801 | 2026-07-14 00:29:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de679f09-0328-3b0e-9abc-6e08333b1066 | -11.8899 | -43.826 | 2026-07-14 00:29:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b48e0dfb-db32-3e18-8ec5-6ba2fef2a9e3 | -8.4955 | -48.070099 | 2026-07-14 00:29:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9edca4e-e58a-3f4b-a09a-a6eccc314e54 | -4.3742 | -47.764599 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30db4ce5-8877-3fbe-b1f5-712929accaeb | -5.8329 | -43.467098 | 2026-07-14 00:29:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b32967e1-cc29-3c07-ae0d-054e58e31efd | -4.0077 | -48.056702 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62161883-18c4-3b41-8956-34d7c8b31410 | -10.0748 | -50.117699 | 2026-07-14 00:29:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc875e3-5b2b-3736-b279-df1ded61fcbf | -10.7589 | -42.110401 | 2026-07-14 00:29:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9b4ed294-5e2c-30b7-86e0-76a042cf6df5 | -6.4889 | -42.215199 | 2026-07-14 00:29:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 15cab389-e490-32c7-822a-ae766002683b | -8.5071 | -48.076 | 2026-07-14 00:29:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f6f71a6b-3361-37b2-829d-61e19f27f267 | -5.8249 | -43.4771 | 2026-07-14 00:29:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4587d056-19c2-3ef5-90b7-4cb5b003dd2c | -5.2555 | -42.673 | 2026-07-14 00:29:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 81119c16-8ba6-38a5-9ac1-f3aa65f2d118 | -5.3058 | -47.2388 | 2026-07-14 00:29:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d4aae6f1-709e-393a-bdff-6f49e792ad5d | -7.7501 | -45.0242 | 2026-07-14 00:29:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c2a54e08-506f-31c0-b779-55ada3cf6f43 | -10.0628 | -50.109001 | 2026-07-14 00:29:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11212d57-6290-364e-bbe9-df7471783fd3 | -5.9095 | -43.618801 | 2026-07-14 00:29:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5512ee24-66b9-324a-9c3f-d1e9e1ca0b36 | -9.9115 | -44.510201 | 2026-07-14 00:29:00 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8a06d7e0-4353-352c-bda4-31927cc22a68 | -18.177799 | -46.924 | 2026-07-14 00:29:00 | METOP-C | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6fcae2e8-2a23-307b-9957-3d22cb7842a8 | -11.8915 | -43.833099 | 2026-07-14 00:29:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 280231cd-c885-388f-ad2d-caaec9a294be | -6.4812 | -42.2262 | 2026-07-14 00:29:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ec93177-5a6f-345a-a5ad-3e9c10a2994a | -3.9231 | -47.819401 | 2026-07-14 00:29:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84b08cc-92d8-38c9-83d0-809529c46ea2 | -10.8277 | -49.376301 | 2026-07-14 00:29:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5eff3c28-6a53-3b1a-a48d-30f280e69cb0 | -5.94 | -46.354698 | 2026-07-14 00:29:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b269b9f3-cbf5-3221-9470-d319cd5a0eae | -5.2535 | -42.664501 | 2026-07-14 00:29:00 | METOP-C | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f3325e7-8f94-318a-80e1-61fa7646284f | -4.0093 | -48.0639 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| debaa828-4fc1-3ff8-896d-3f8b971601d9 | -10.0575 | -50.132599 | 2026-07-14 00:29:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38a1a78c-897b-3458-a265-f480f5803bb3 | -11.8931 | -43.840099 | 2026-07-14 00:29:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d54bacf-4b54-37e5-a28d-20de2874e4cc | -8.7277 | -48.3325 | 2026-07-14 00:29:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9bab749-bd69-353c-bca6-ef2b17b8c64f | -4.3758 | -47.771702 | 2026-07-14 00:29:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a94d77-54cf-328d-a356-dada20920ef9 | -9.0268 | -44.25 | 2026-07-14 00:29:00 | METOP-C | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c459f4a-745a-380c-bb0b-c37e586db67b | -12.4447 | -49.587101 | 2026-07-14 00:29:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ae7f21c0-5cc8-3291-b4d7-53dba33d0f65 | -7.7768 | -45.502998 | 2026-07-14 00:29:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d837c21-7ee3-35fe-bf6b-bb7210c21e34 | -12.4454 | -49.442101 | 2026-07-14 00:29:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4e6bb01-79ec-3f58-8575-ffd46452cf50 | -10.0673 | -50.130501 | 2026-07-14 00:29:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 486c1b12-e959-3478-b60c-44f9cec5d150 | -5.9113 | -43.6264 | 2026-07-14 00:29:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0e478e0-9ff9-3975-a859-b8471bb3ab7a | -7.7517 | -45.031101 | 2026-07-14 00:29:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 128075ef-b430-32c7-b966-819df275f76e | -8.5036 | -48.060101 | 2026-07-14 00:29:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3c29c606-99df-38a0-bec0-3a3a3f878ccd | -10.0553 | -50.121799 | 2026-07-14 00:29:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6dda4798-9b7f-3869-8c36-9a0860f1e66c | -18.7743 | -52.4061 | 2026-07-14 00:30:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 40.2 |
| b333eee0-e975-3428-a17a-be17fcae2154 | -18.7943 | -52.4027 | 2026-07-14 00:30:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 2be59f1a-ca12-383c-9316-08e44820d6be | -10.0728 | -50.1318 | 2026-07-14 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 805da5e8-4001-30a6-9d10-ec33cb9149d8 | -8.4985 | -48.0813 | 2026-07-14 00:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 8c565b20-13ef-3d0b-a1ab-92033dbc8fc0 | -8.4987 | -48.0594 | 2026-07-14 00:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cc19de29-d9e4-301b-87bc-2c6239bbc0cd | -10.0731 | -50.1104 | 2026-07-14 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 57480c47-abc1-3a25-b82d-bace48e7ffbb | -10.0728 | -50.1318 | 2026-07-14 00:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 65c29994-acd5-3ed1-bc93-77450640e16c | -18.7743 | -52.4061 | 2026-07-14 00:40:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 38.8 |
| b21f4646-cc90-3e21-92fe-971808ec405a | -18.7943 | -52.4027 | 2026-07-14 00:40:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 16ba2001-2f69-3b08-85a8-bf4cc6718af4 | -18.7743 | -52.4061 | 2026-07-14 00:50:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 46.4 |
| af1bd62a-bfa4-3d92-a6c7-e0545afe307f | -18.7943 | -52.4027 | 2026-07-14 00:50:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 54308b71-9381-33cd-b5cf-482ab81fefe5 | -8.4987 | -48.0594 | 2026-07-14 00:50:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 02a01dd9-9c49-3a29-b8b2-325d3cdba83d | -10.0728 | -50.1318 | 2026-07-14 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 2f9767cf-f804-3d6b-b423-03ecd1447732 | -18.7743 | -52.4061 | 2026-07-14 01:10:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 69e502a8-1c08-321a-a9fa-b6a948c30f27 | -12.88027 | -58.28545 | 2026-07-14 01:17:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6a56af52-0502-32fe-8a9e-3e214ba532f8 | -11.2753 | -55.79482 | 2026-07-14 01:17:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| dcece58f-cba0-3977-8d59-c89153abac60 | -18.7743 | -52.4061 | 2026-07-14 01:20:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 38.1 |
| cf2ba2e3-b9d6-3c28-acd2-6f94ebb3bfcb | -9.67216 | -67.22424 | 2026-07-14 01:20:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2bc92eb-e61d-3732-a45a-f67f395239e7 | -18.7943 | -52.4027 | 2026-07-14 01:30:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 39.8 |
| c4a77002-66f4-306a-abc0-5b5419608382 | -18.7943 | -52.4027 | 2026-07-14 01:50:00 | GOES-19 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 37.7 |
| ebfb8e88-4fe6-39b9-804d-cf702b880fc5 | -4.15067 | -38.17215 | 2026-07-14 03:15:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6748d651-69ae-323f-9a05-9d7c36a63473 | -4.14678 | -38.16993 | 2026-07-14 03:15:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 64103135-670a-3747-bc29-2253cf637f73 | -4.15236 | -38.17093 | 2026-07-14 03:15:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c9390b94-eeeb-3db0-96f5-cf3c04c82aa0 | -4.15131 | -38.16846 | 2026-07-14 03:15:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| d3675fbb-7581-3dd9-89a9-8a69c6a29a0c | -4.15297 | -38.16726 | 2026-07-14 03:15:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6593b3d8-fbce-3fb1-a5d3-d78808fea109 | -6.4924 | -42.22089 | 2026-07-14 03:17:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |


[Clique aqui para ver as próximas entradas](README3.md)
