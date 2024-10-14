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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2cf667e-3429-3a99-9249-57d158b8d338 | -4.05449 | -48.24005 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6789c8a3-a896-3678-8771-15225a53704c | -4.05374 | -48.24475 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9858bfe8-804c-3dc6-91ce-e53cd55e9f59 | -4.05373 | -48.24348 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2776c92a-3a7e-369a-abc7-6a2cb459cba3 | -4.04994 | -48.24421 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6993efd7-cb4f-3cdc-bb29-a980bc073453 | -4.04993 | -48.24295 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4c7266c-3da7-3149-8ecd-3c3a4701861f | -4.04921 | -48.24881 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02870107-2270-3798-b130-7d5bb8510f33 | -4.04916 | -48.24757 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8493e94a-2a6e-358e-92b7-bd7d0e51f04a | -4.90245 | -48.63708 | 2024-10-14 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9dc480a0-4aef-39a2-a6d5-7d3f37d430c8 | -5.06505 | -48.06152 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ad983c8-2444-3b46-ac94-6f3bee3fa2c4 | -5.06435 | -48.06594 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e3cd0909-787f-3a4f-96db-305d810dbfc4 | -5.06401 | -48.06041 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0db1d4e3-1587-3f3e-ac8a-8eb8473c4264 | -5.06328 | -48.06482 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 53a7b0d4-1a28-32a3-89bb-e1dc4866f763 | -5.06136 | -48.06089 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 15d209bd-c827-35ac-b360-fb8a1c33aaec | -5.06065 | -48.06532 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 109f6a16-0bc9-3f25-a7db-f3c7a526ce89 | -5.05994 | -48.06976 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0645f55c-0c49-3aaf-a0e8-9b308f479a20 | -5.05959 | -48.0642 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 291a37a2-05b1-3b3e-999c-68c3a431344f | -5.05885 | -48.06863 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 062ca460-47ae-388b-8f6d-1e1fbf1262a1 | -5.05695 | -48.06469 | 2024-10-14 04:19:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1ba4425-6232-3bde-ad87-f5ff9fe432fc | -3.95936 | -47.96051 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 473e4f4b-beb0-3635-95f5-0e6add62eb87 | -3.95562 | -47.95997 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22d4bb77-1b85-34ba-9b14-3ad7e90599c0 | -3.9549 | -47.96447 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b95445dc-90e3-3a35-8f87-0d865452d101 | -3.92658 | -48.35445 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 76054213-f192-360a-927c-426dfbfeba74 | -3.92413 | -48.35157 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6ac692c8-eeb1-39b7-a692-0ab8a19be40d | -3.92354 | -48.34912 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 166fccca-e5fb-3a56-aaf4-0ebfd71dd1eb | -3.92337 | -48.35635 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d12c78e-f2e6-33e7-9448-4398a40e3d47 | -3.92275 | -48.35387 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d22dc733-7b34-3bee-b235-33b86a911fc8 | -3.92262 | -48.36112 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 31c693fd-bb81-3894-8820-94362ca1a0a5 | -3.92196 | -48.35863 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 12803ca1-1895-338c-a934-ef89aaa4d5db | -3.92181 | -48.34148 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d64348b5-442d-347c-895c-bc423172bae5 | -3.92117 | -48.36339 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed9ff7b2-1b20-3c23-9d11-ec51fccc1a5d | -3.9205 | -48.34381 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed857579-e635-37d5-8d46-781325b718a4 | -3.9203 | -48.351 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 57d11169-df3c-316f-8a6a-32d04adcb0bc | -3.91971 | -48.34856 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 411763ca-82ea-3902-bc7c-24e2b3f317dd | -3.91955 | -48.35574 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7d406dbc-665f-30f8-a17e-6d142ed5ab39 | -3.91892 | -48.35329 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0e0067b3-a766-3041-a7c4-01512b4c984e | -3.91879 | -48.3605 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 082a3969-5776-3532-9387-eee19499b847 | -3.91813 | -48.35803 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 28d0c1be-78fb-339c-8f59-3c8eab1df480 | -3.91799 | -48.34085 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a1ca48f-0139-35ec-9d78-b4f74c8948cf | -3.91735 | -48.36278 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56cf6b01-a9e1-3521-9f8e-3a501b22b749 | -3.91572 | -48.35515 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b3fac103-0420-36f8-a752-7227b2e24386 | -3.91496 | -48.3599 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 80153d7b-6d29-37a8-9f40-a678735c9a61 | -3.91113 | -48.35929 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a4beec6-422c-3b1b-8062-d66cedc2ed93 | -3.90807 | -48.35389 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c8a8c8ae-f016-35e3-9ef1-fe97bc2647e5 | -3.90731 | -48.35865 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ef81e0aa-dcc4-3936-8c6e-d637be00dc43 | -3.90425 | -48.35324 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 76d78287-8e88-34c8-b5f9-b2b0514dfe65 | -3.90349 | -48.35802 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4c3a1386-8b6e-366d-af74-91659427f34a | -3.86978 | -48.37222 | 2024-10-14 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 358f18b1-fd9b-323f-b3d4-509128c91539 | -6.544 | -48.24068 | 2024-10-14 04:19:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 509a78fe-b4dc-3f84-80f8-88b1fcc1084e | -6.54034 | -48.24007 | 2024-10-14 04:19:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a83685e-cecf-36e4-987a-dfc454401af8 | -6.21491 | -48.32005 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7bfc825f-07de-3c29-872b-9ab375938646 | -6.21228 | -48.32128 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a955d8e-13e6-33fe-889b-27face6149c8 | -6.2112 | -48.31948 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e8859fd-9403-3f61-ab4d-bee6797a0c5f | -6.20902 | -48.33255 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cfd94fd5-5c2d-3a68-9aa0-0acac34910b6 | -6.20858 | -48.32069 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b996e569-534f-3448-9987-ca4d5c29a531 | -5.60781 | -48.95396 | 2024-10-14 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55ff124c-4d38-3c98-b640-2325ae65dbd7 | -5.60393 | -48.95334 | 2024-10-14 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 307f4290-ec32-3176-bd57-0468c41a5bf3 | -6.53963 | -48.24443 | 2024-10-14 04:19:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0eb6668-29a4-370a-aff7-8b971a37ca56 | -6.53667 | -48.23946 | 2024-10-14 04:19:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a5749573-d59f-343a-b6d3-e0f0effa2ffd | -6.21599 | -48.32185 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cbeb92b1-6b0e-353e-83c8-15bd73561c9b | -6.21528 | -48.32624 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 94655111-78a3-37e3-9d7e-3b1b98e6fc1e | -6.21418 | -48.32442 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f0b5d2cb-b04e-3dd8-94b0-327d35786ff7 | -6.21345 | -48.32878 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 90e98a4d-db3c-3549-b61f-7c9738cf8556 | -6.21299 | -48.3169 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fb8ee0d4-9bcf-3ee8-90b8-dab9d61d10b9 | -6.21158 | -48.32564 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8aca843-0c31-3c0e-8d20-dde135544a7d | -6.21088 | -48.33 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 25dd4788-afad-3686-8d93-9d1acc56eea8 | -6.21048 | -48.32383 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9471ef54-ea4f-399b-b8d7-3acf3eec2797 | -6.20975 | -48.32817 | 2024-10-14 04:19:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02d92d95-4702-394b-9107-f4c498c411ac | -2.61228 | -49.11734 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 044ba8e5-c46a-37e1-9ea7-4eb43d8bdb7d | -2.60954 | -49.11234 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5b1ac7d0-0843-396a-aa75-7596e5df78f8 | -0.78248 | -48.68293 | 2024-10-14 04:19:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b6a6240-7602-3066-86c6-dc62d3604ba9 | -2.18376 | -48.8486 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c097859f-2ffc-34d7-b501-f0ac064ced5d | -2.17971 | -48.84795 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20100f4c-b951-313c-819e-c6cfe5cf6f00 | -2.17736 | -48.83667 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5ee653c5-035b-386b-be0f-31c090f8ab76 | -2.17679 | -48.84021 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed476e3-4492-38c1-b6e8-376f2139bb19 | -2.17275 | -48.83957 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b54b8f30-9daa-3334-85ce-fffd0e4f9876 | -2.15946 | -48.84482 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 277bdc82-083c-3e4f-b30e-f1ef636d5042 | -2.6403 | -49.52307 | 2024-10-14 04:19:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7a7b6ca-33e6-3052-9b93-c92a00c26fea | -2.63969 | -49.52694 | 2024-10-14 04:19:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6e225330-3995-3359-9eec-d59b6f846562 | -2.62177 | -49.0852 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b131d291-6500-33e0-be9d-a5361c05b2aa | -2.62117 | -49.08883 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7503f72c-f204-34fa-8f45-75fb9efeac03 | -2.62057 | -49.09246 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4f1f87ac-ddfd-3ffc-b3ab-ad5fcdce47f9 | -2.61827 | -49.08096 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| bb87f45a-0950-3a21-bf23-5d6395b78e6a | -2.61768 | -49.08457 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc1b0880-f024-3a92-8b05-1e4911493ac0 | -2.61708 | -49.0882 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4c2dfd50-b275-3761-ad9e-c1cc2fc06560 | -2.61697 | -49.11433 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1db1ae45-e48f-37fb-8e13-f808d6561921 | -2.61648 | -49.09182 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f83ee8f8-93b1-3607-be05-4a2596b56501 | -2.61637 | -49.11799 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1545c1e4-32c3-37b9-8e4d-3727975e50be | -2.61348 | -49.11006 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2c285567-1715-366e-a01c-f829281b60bc | -2.61288 | -49.11369 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d47bfc11-55db-3a35-a1e5-32819f9cadd5 | -2.60938 | -49.10944 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 218e01a1-24eb-3c8a-a6f1-34bb896e1bee | -2.60896 | -49.116 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77a03f7f-6f73-3187-ad26-17ba698a56e4 | -2.60879 | -49.11306 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55b7a3ca-a2c4-3852-a05e-7f83856ae755 | -2.53192 | -49.02201 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 565acc5a-093a-361c-948d-d80292bd69d2 | -2.53133 | -49.02563 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 09b969c3-35c5-3504-875d-4bb5fe1f2b45 | -2.52785 | -49.02135 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eaafd289-74f3-3f85-9162-aaf0845047be | -2.52726 | -49.02497 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7e07a9c-6e61-38be-b74a-39de0586bec3 | -2.4061 | -48.9468 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25403cb6-0669-3730-bb19-90bc2626e7e5 | -2.40319 | -49.75345 | 2024-10-14 04:19:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62ffe5b0-26e7-30b9-a6ae-01650640d87d | -2.4026 | -48.94256 | 2024-10-14 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 350f60c4-2ef5-3f0b-808d-3cf7d04bbf7a | -2.35318 | -49.25506 | 2024-10-14 04:19:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
