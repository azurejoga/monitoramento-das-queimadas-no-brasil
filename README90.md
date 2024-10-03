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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f29a95bb-6321-3bdd-b4fd-4b7889185fc3 | -10.94345 | -46.59209 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 5cfd795a-0477-3436-892d-009d0cad33c2 | -10.94068 | -46.58804 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3ae9c0a1-d9ec-36fd-ad92-f4878b1256de | -10.94013 | -46.59156 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f07ca54b-d98a-3aa9-ba4c-471c73f97976 | -10.9379 | -46.58399 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1a5a67de-9f04-3a6a-ad0a-b04e9b7ee9c5 | -10.93736 | -46.58751 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1239fe58-bafe-3d38-99ec-330e9f1eb04a | -10.93682 | -46.59104 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 79fc58ef-8a46-3197-bef2-e60fbc731764 | -10.9353 | -46.48992 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5eed1568-68dc-3b79-8509-8f99c15ff19f | -10.93405 | -46.58699 | 2024-10-03 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00a24f1b-b407-3958-a6b5-405dbcd3ef9c | -12.19957 | -46.7585 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8de13385-eb4d-335a-819a-a8b41ff0e0b2 | -12.19625 | -46.75797 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45778422-aa1c-365f-8322-c744701cfbfb | -12.1957 | -46.76152 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8009f401-1b94-3a2b-b176-74f53ff3c559 | -12.19486 | -47.27175 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52e81a33-9095-3942-bcb7-580b7d22f3a2 | -12.19293 | -46.75745 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| afbf106d-0563-3463-9804-15ffea068525 | -12.19238 | -46.76099 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a4c509f8-86b5-3824-858d-b597066f9909 | -12.19015 | -46.75337 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0087650b-5351-3ba3-9fc9-53f2841700c1 | -12.18683 | -46.75284 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79ff7fa1-b4b2-3276-95df-118e44c7dd8d | -12.18351 | -46.75231 | 2024-10-03 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89f9586d-ce45-3b97-8fdf-7fabf235d634 | -12.00238 | -47.35174 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12eb2213-88cf-3f68-8640-e46515e7dcab | -11.97329 | -47.38301 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 558b5602-e069-3839-bfaf-ac44a78e4bdf | -11.96559 | -47.38895 | 2024-10-03 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 938fcec5-1b0c-39b8-9f79-61f9d3415452 | -11.81864 | -47.58799 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c29e820f-f803-31b7-a6fb-54febbae2deb | -11.81699 | -47.5985 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfd00255-2336-33d1-a570-d824608df72d | -11.80324 | -47.57832 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b8a8323c-91fe-3fd9-8d08-7dff7bc00e3c | -11.8005 | -47.57428 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a2795f2-5225-3bb3-95ff-f8d459e2fbb0 | -11.79992 | -47.55629 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60e21dde-3da0-3766-9ffa-0e68ee8190ce | -11.79882 | -47.56329 | 2024-10-03 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c76570e-6509-3887-89aa-1f99f8879033 | -13.65391 | -47.24981 | 2024-10-03 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0029b91d-a16e-3c3c-98a4-a9ad2f0d122d | -13.06168 | -46.74571 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9769464-275a-322e-8d67-188e4b966ece | -13.05834 | -46.74519 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e74c5c74-7b44-3155-83a1-dfc891a0faf5 | -13.05779 | -46.74878 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a75f1a10-a53a-3cf4-afdf-ca7ae13d85e8 | -12.49196 | -47.50348 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aacb004b-0713-31ef-84a9-f3529d63afc3 | -12.48866 | -47.50294 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6ffb29c-479a-3296-a8f4-847bdb8cb793 | -12.476 | -47.4973 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 444c8ebc-0ac0-3e6f-b121-f5f2fd9ab8c5 | -12.28853 | -47.65347 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3747216-05fa-3d4c-ae32-94fc93f648d5 | -12.47655 | -47.49378 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 899da827-5d97-35d3-9f52-713a399c4e3f | -12.28798 | -47.65697 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb5ad1c5-941a-3cdb-91be-2538ec3ed15e | -12.28468 | -47.65644 | 2024-10-03 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de373859-6f02-3707-a3f0-4109243e5327 | -14.81251 | -48.08678 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9af315bb-8886-390e-8614-957250260d66 | -14.81196 | -48.09032 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24db6fee-c6f4-3709-9cac-3dc5c89e7a1d | -14.79 | -48.05762 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f74e02b6-d19f-34be-b582-627f0bd7d795 | -14.78615 | -48.06062 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f550a1b-4c6b-37ad-b568-4f207c860a9b | -14.78285 | -48.06007 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 200c563d-c53d-32ac-ade8-0cbe759d23c2 | -14.78172 | -48.08895 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 20a16a88-ad02-3013-bc85-9f6205147f64 | -14.76469 | -48.36971 | 2024-10-03 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdf5dce5-fe11-3684-a652-96ffe0983b2e | -15.02156 | -47.55182 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb968796-4a79-3679-81c4-269f71aab73d | -15.02101 | -47.55542 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9198579-8a9e-3ba7-82de-d864157700b7 | -15.08475 | -47.18122 | 2024-10-03 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf6e2db0-f0f3-3a5a-8ce1-454dbd4794e9 | -13.74 | -48.15959 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7603bfb8-7b3d-31fa-87cb-9963dbb21396 | -13.73944 | -48.16313 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ea26f76-e86c-3d77-8288-5b38e38fd797 | -13.73837 | -48.14847 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16cf1d21-d67c-364c-b4ad-ad2b7fb8caec | -13.73781 | -48.152 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 45477ee0-273b-35e5-951d-df0a2a931f1a | -13.73506 | -48.14794 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04710b31-3c8f-37c6-81be-11c8b00fc930 | -7.51321 | -47.5653 | 2024-10-03 04:27:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5012bf7d-c3a9-395d-b9fe-2fa502d9f4d1 | -7.41756 | -47.8676 | 2024-10-03 04:27:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0465d5f-bf91-32a2-bb68-e25428415b09 | -7.76137 | -47.50409 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc00719c-23b0-35ab-a89c-3b677b4b288e | -7.80742 | -47.47175 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f260704-abe5-3ee7-bacc-4363615c8819 | -7.80354 | -47.47474 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c62c601-f2d6-3a20-bd00-bac7e362a359 | -7.51654 | -47.56583 | 2024-10-03 04:27:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 651b4bb4-b378-32a7-8e52-4b56c8a7c2c4 | -7.41813 | -47.86402 | 2024-10-03 04:27:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e636c65-1c30-3c37-b0d9-8484f3e16834 | -9.17407 | -48.74857 | 2024-10-03 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 95293535-96ca-328f-961d-f8be68257bbf | -8.57693 | -47.44831 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f563190b-a7d0-3871-8493-238996b54eda | -8.53618 | -47.32009 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fc26d90-7dce-37cc-bd29-59dd3b36a328 | -8.53287 | -47.31956 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d94ee611-94ea-31dd-ab01-2592bd7effe4 | -8.51879 | -47.32079 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07e61c90-2578-341d-88b5-8885047ea364 | -8.51548 | -47.32026 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41fb2e12-a2e5-3389-a3bf-f8241baec4a2 | -8.51217 | -47.31974 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e61b6dc6-4326-3817-9dbb-9e9e73f42062 | -8.50886 | -47.31921 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d689cfa-e966-3f77-b98f-133fc5c08ac8 | -8.50831 | -47.3227 | 2024-10-03 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f94ec4e4-c870-308f-ac4f-e03eae6fb864 | -8.43835 | -47.1184 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9c4ae38-f8ec-3ec0-84d5-f4f32c7d2015 | -8.4378 | -47.12188 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef623303-5eeb-35c7-b788-0aea457fc611 | -8.43725 | -47.12536 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0285f755-8d86-3750-8961-77f880129ed1 | -8.39776 | -48.48331 | 2024-10-03 04:27:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61e484a6-450a-301d-8e25-66f8d5a58774 | -8.35781 | -47.54205 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c1c76c3-06f2-3812-a84a-66289d2d585b | -8.35505 | -47.53801 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 890f8ca8-9e47-3508-a392-c495d550120b | -8.35449 | -47.54152 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9369cbfc-6a45-3612-8549-f7d583d6613e | -8.35393 | -47.54503 | 2024-10-03 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 667e1c51-6249-303d-b0c9-2d32d8be8696 | -9.89548 | -47.7627 | 2024-10-03 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 78e9284a-56ed-33b5-8c23-f7a54def7264 | -10.75302 | -47.97819 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3e06dc0b-cb19-3c00-ba80-6aeaab7afd37 | -10.7497 | -47.9777 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2dcf8690-59c6-3386-a8ab-9a6711282422 | -10.74858 | -47.98471 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c74741a-5917-3aec-8a02-decbf91d2fa3 | -10.74638 | -47.97718 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9cbf5f46-10bf-330a-87f8-02604a4b2b1b | -10.74582 | -47.98069 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 29dc12e3-b50f-3096-9eb9-6adab78d22d2 | -10.74527 | -47.98418 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cff9ac44-163d-34ec-a985-43d9e27573c4 | -10.74471 | -47.98769 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| efd00dd9-a40a-3cb5-b1ce-81d44379341c | -10.60535 | -48.09236 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6d35036-a1ad-31af-aad8-8e2a751a380b | -10.6026 | -48.08826 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aad7816b-f4b6-3bf4-afc9-9828b2a6b7a3 | -10.60203 | -48.09181 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5cad4649-a5f6-331c-8105-c7ac363731b1 | -10.46452 | -48.18503 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bdddc412-bbaa-31e5-8e91-4dcd7b3c5ad6 | -10.46393 | -48.18866 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c7d7a1b-6ca2-3615-9872-ceeb6136917c | -10.45846 | -48.18026 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1dcda1b7-a272-30f2-9937-fd5864a3bfa7 | -10.4573 | -48.18744 | 2024-10-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02dc9040-3da4-3a74-ad3d-0f97468d74e2 | -10.45629 | -48.17258 | 2024-10-03 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7d202a93-ab4c-3aff-a81e-914a5ca8cfd9 | -10.45457 | -48.18326 | 2024-10-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1dc8539f-5825-3cd0-a21d-fd4ed4e1d7d7 | -10.4526 | -48.17572 | 2024-10-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9cb9d2a-2215-3103-91e8-a06784459734 | -10.45204 | -48.17928 | 2024-10-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e670d73-76f4-3896-85a0-b962c8ff3aa6 | -10.44871 | -48.17873 | 2024-10-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 514e7792-a8f4-37c0-b4cd-dbc53b3b3ac0 | -10.42824 | -48.15729 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8609e1a3-9000-33a5-8194-9c801dd62c4d | -10.42652 | -48.16805 | 2024-10-03 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af15b1aa-ff87-3862-8715-4ca22093323e | -10.42491 | -48.15673 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b29bc30c-336e-30c3-b741-4c718db795b9 | -10.42434 | -48.16031 | 2024-10-03 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README91.md)
