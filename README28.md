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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc21dfa4-515d-3ef8-9c17-a1d982c2a8a2 | -0.76737 | -48.6448 | 2024-10-20 04:29:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3955aa27-9584-3de3-8d9e-c3adec56ac0c | -0.7654 | -48.64366 | 2024-10-20 04:29:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70c5beb7-3556-3c85-b8e3-90229dd5ec64 | -0.76449 | -48.64048 | 2024-10-20 04:29:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eff373c-3c06-355c-a43c-f2e17e8841ea | -0.7639 | -48.64426 | 2024-10-20 04:29:00 | NPP-375D | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92d68149-fa68-3ea4-a0a0-d8744ce6367c | -2.1204 | -49.5384 | 2024-10-20 04:29:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee40130e-213f-3ed4-a864-fcb9f04d1f60 | -2.05854 | -48.88202 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e6ddcbd-754e-36ec-99df-a73b68c52be6 | -1.53897 | -48.70327 | 2024-10-20 04:29:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba0caf6-7c67-3198-922b-7e71a673caf5 | -1.49298 | -48.9915 | 2024-10-20 04:29:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98507da8-ac80-3574-b71b-b47426ab8498 | -1.48949 | -48.99096 | 2024-10-20 04:29:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5bd5608-79e4-38b2-a07a-894ec40ae66d | -1.471 | -48.97233 | 2024-10-20 04:29:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d7a735c-4513-33f8-936e-b7b15a65c84c | -1.46979 | -48.97285 | 2024-10-20 04:29:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c197345f-a72d-3e09-b8e7-127f2b11678c | -1.46341 | -48.96791 | 2024-10-20 04:29:00 | NPP-375D | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4dee3d8-6978-3f88-9618-36a9db00ba74 | -1.017 | -48.84955 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6272953c-0596-3fc5-82b9-ba058259970a | -1.0164 | -48.85338 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 262d4421-9bce-3f68-b575-1c7847ea94a4 | -1.01412 | -48.84517 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fa7dc0a-3cc7-32cf-920e-336fe598a19e | -1.01352 | -48.849 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94857e33-76ae-31cd-a9b0-423e4fb46aa9 | -1.01063 | -48.84463 | 2024-10-20 04:29:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e69be7-20be-3f0d-acf9-ecadc2e42034 | -3.27723 | -49.08719 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f56620e-8085-3caa-ab53-0c00d24285d4 | -3.27185 | -50.23045 | 2024-10-20 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fee6de9d-bccc-3f0a-9df2-e8ab2418975c | -3.2554 | -50.12523 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c862a5eb-049a-38f4-b861-8d677c789bb5 | -3.22095 | -50.3605 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 696b4e0a-7f38-30df-8dce-e0a2cf680e76 | -3.21799 | -50.35564 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42fc9fa0-a7e5-31c4-8337-a92b4541f9d6 | -3.21729 | -50.35992 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd34b947-d0e8-36c2-893f-0e155c509b55 | -3.19491 | -50.31444 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3cde2f8a-cd51-37ac-82da-89b3082a10ff | -3.19126 | -50.31386 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4111ed82-b620-3b06-aa16-2f4f1756e91b | -3.15851 | -50.37834 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2b7d6d8-9216-3eeb-9376-cd659eb4f56e | -3.15485 | -50.37774 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc3a7571-9765-3af9-80b2-f9053fde57c2 | -3.11988 | -50.17748 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efcb0dee-8e74-300f-b34b-5d6218bbac4e | -3.11967 | -50.17838 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 893b4b0b-b666-3b11-85b1-9ed6034e3911 | -3.11625 | -50.17692 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be74c644-9bfd-323d-90ba-3e4029600d8d | -3.11603 | -50.17783 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e693464f-e447-3098-a6b4-32a7aa0a2ebe | -3.0721 | -50.36128 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49a38f9f-da97-3efa-8ecf-fffed58552fb | -3.06844 | -50.36071 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1960d7e-ee25-3fc8-9323-5f225b616d37 | -3.05854 | -49.37675 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1a7c36b7-a897-3075-a5ab-53929eb0087c | -3.05504 | -49.3762 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5f778931-d52d-35ea-8af6-3101b92d23b3 | -3.05155 | -49.37564 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a03bc3fb-caa6-367a-a34b-109805d5190e | -2.97383 | -49.09845 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91e7f8fe-1e20-316e-bcad-78b030a2b658 | -2.97097 | -49.09417 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddf4c919-3f5f-3a2f-9b6d-191131b1412c | -2.97037 | -49.09792 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d0a75a5-b361-3ce7-96cf-9654ddce982a | -2.88079 | -50.47838 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44a7634a-70e0-39a4-b5d5-334db5b39ae2 | -2.41654 | -50.28466 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7175427-52ed-3834-bad6-3300f4cba27f | -2.41208 | -50.40842 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cc10bbf-f43d-33fe-82a5-86f96eea303e | -2.40838 | -50.40785 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20ed0292-ca84-3ec3-998d-6488047ebd8f | -2.573 | -48.94106 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8cb4edee-700e-3829-8ae4-01aee2ae7c2c | -2.5724 | -48.9448 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05f743db-ec7d-3122-a64c-0ae2b056a154 | -2.57119 | -48.95231 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfb99070-f9df-3c8d-a617-51543a5e6e14 | -2.56955 | -48.94051 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 790005da-ebbc-3114-8b61-0c6baefe33d4 | -2.56895 | -48.94426 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aec24c4-594c-36dc-8445-8afbf932b250 | -2.56774 | -48.95177 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c77e332f-0b3b-300e-b5bf-043e9c88b656 | -2.56609 | -48.93998 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 467c4118-7a78-391a-bafe-b7fadf4016a1 | -2.56428 | -48.95123 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5c04b62-e789-304a-bb28-489e54579f75 | -2.45696 | -48.96575 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26252144-9b32-3182-ac98-7aa4968223e3 | -2.35337 | -48.91559 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2f805d3-1671-3dd0-b65a-8ced707ec4d4 | -3.07244 | -50.5026 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa4b39ac-5d74-3a66-8af6-4032528ffa28 | -3.07079 | -50.50105 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c245e9bc-6d58-3aea-9f62-76d50651fe77 | -3.06875 | -50.50201 | 2024-10-20 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf6f8032-68de-34f2-baef-1b14a5378849 | -2.86212 | -49.36338 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 692932d6-c274-3d1d-a4e1-623d876d9159 | -2.84496 | -49.62971 | 2024-10-20 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4254ca07-f646-3179-8aec-eedba5951f34 | -2.83668 | -49.13574 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ab3de3c-0e32-3e8e-bdfe-d78ad2c22d2f | -2.80598 | -49.62353 | 2024-10-20 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e05e11a8-643d-365c-85d8-bc90ce076de1 | -2.80244 | -49.62297 | 2024-10-20 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60d7a895-3d92-3223-ad8d-4cd8a20fce2f | -2.78857 | -49.30456 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 57b9c3d9-758c-317b-9ff8-937e052a6984 | -2.78795 | -49.30843 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 0bbd77c9-3312-37ff-a76b-4947f3bf83f5 | -2.78568 | -49.30016 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9a30fc93-c836-3b80-8e8c-4b8ad3fc3d94 | -2.78507 | -49.30401 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 04dd234f-6b92-38d4-8fd6-3041a60aa15b | -2.78446 | -49.30787 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f308b32a-1f58-3846-878f-89f24466ba35 | -2.78219 | -49.2996 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 633d5262-c270-3d37-87fd-4b1aec3685c9 | -2.78157 | -49.30346 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4af658da-386d-3a40-b818-c76f71f0c2c9 | -2.78096 | -49.30731 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| fee01ec8-eb11-3ed1-9518-01d608abaea5 | -2.77808 | -49.30291 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3237c895-23ec-3445-845e-3349d1033d30 | -2.77746 | -49.30676 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 462cc063-b4f8-3f6c-94ae-9158c5d4cb86 | -2.77136 | -49.41304 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18209741-c6b4-326c-9cb5-77cf5e9741fa | -2.76846 | -49.40859 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af35621e-940c-335c-a9e4-5dd4b6f5e269 | -2.76785 | -49.41248 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 07cdae7a-de4f-3c25-a8d9-c436d04e183a | -2.76723 | -49.41639 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6035d33e-9c6c-3870-a4c1-19fd94fcf64e | -2.76534 | -49.36038 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e5f09ae2-6711-3d7b-9e68-a7b7375c85ad | -2.76433 | -49.41193 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 96034769-f948-371a-941a-6d935ff05bd4 | -2.76371 | -49.41584 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f5014a8-abec-3d22-a873-26fab2042b84 | -2.72357 | -49.16539 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28dabd19-4d71-3b18-9105-6b8df7eafa98 | -2.7193 | -49.51311 | 2024-10-20 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 527c68f7-c39c-3749-9d72-d25b03bab149 | -2.7164 | -49.50863 | 2024-10-20 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 843a8b55-0f22-3b2b-90e1-e9f4d1d1fac4 | -2.71577 | -49.51257 | 2024-10-20 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7218c650-dc72-37f6-953d-aaab3e241aec | -2.68536 | -49.31676 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55142fa9-af61-34b9-99b6-551812ced64f | -2.68186 | -49.31622 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ea91639f-850c-322f-a7f7-f1c2cc316e1d | -2.664 | -49.13651 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f36d9899-48bb-3432-861a-e3f506fba3be | -2.66339 | -49.14033 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 792b7244-e376-3297-b537-d289a4e41c42 | -2.66247 | -49.79862 | 2024-10-20 04:29:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35b20596-be81-3d64-9a17-f55cce20aa1e | -2.66053 | -49.13596 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c7094435-d3bd-3023-ba2b-d7e9a9de12c8 | -2.65992 | -49.13978 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 0ada9dae-0a5f-3f5e-8702-446870f5c9ce | -2.64083 | -49.09489 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5199843-c7ff-36ed-a957-b49faf81fd18 | -2.63736 | -49.09435 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a8e486ae-aeca-387e-bc0b-ce702ca9dd92 | -2.63628 | -49.07859 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28407881-3576-36d7-bca0-81367f1bc80b | -2.6321 | -49.98688 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ede64b7b-8c80-33b3-8162-8ba05f37ca7e | -2.62916 | -49.98217 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa773b4-3619-30bc-9a06-2ae0c0434a90 | -2.62707 | -49.06935 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 79cc8179-d08d-33a1-94f3-ba3d8a305292 | -2.62421 | -49.98988 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15a0bc7b-a183-3493-9e6c-527988efe552 | -2.62059 | -49.9893 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5044795-eef5-316d-af41-e596cafe33ea | -2.60084 | -49.10025 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e51d57ee-9658-33d3-9d5c-9c6c01da57ca | -2.60023 | -49.10407 | 2024-10-20 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f48dec0e-88cd-392f-9866-35978b67c800 | -2.5955 | -50.02505 | 2024-10-20 04:29:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README29.md)
