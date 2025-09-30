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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d2d787c-2874-34c1-b334-36f076750965 | -12.83432 | -46.97761 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5719546b-c908-3773-8873-6bdd4f14345e | -13.72841 | -48.66956 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93b2e3cf-8518-3f07-a4a6-0398fcf3c00c | -7.10881 | -45.54656 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f33d496-6c00-357a-92d2-713cf2deae90 | -13.71279 | -48.64556 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 493423f9-a90f-364e-ac43-db0a2963586c | -14.54824 | -48.48088 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7bebeae6-ed56-391d-b5ee-23f84538cbca | -13.61105 | -48.03597 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e52d1b5-960e-319c-8c25-424f15ac45d3 | -14.68841 | -48.23906 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37be8369-79c6-379a-a676-4a21c38b9257 | -11.10659 | -49.7733 | 2025-09-30 03:49:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 822984c0-86f4-38cb-a2bc-e3352d1c9bf4 | -6.89876 | -44.53077 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4824410a-3363-30bb-9140-d4e1dbc60507 | -17.09244 | -48.56725 | 2025-09-30 03:49:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da9f7c64-eadd-3109-adbc-5bf6880256e6 | -13.22305 | -50.94034 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 939b88ce-2da8-3c53-8ef6-5f667f1257e9 | -12.83771 | -46.97655 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51cf5183-1e71-34ed-94ed-ddf2aaf57993 | -19.76385 | -42.15194 | 2025-09-30 03:49:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b34f1ea6-c695-34a9-a393-8650455b9689 | -5.90759 | -43.71385 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 199b4238-a1fc-349a-bd0e-8562e6885296 | -14.50359 | -46.19619 | 2025-09-30 03:49:00 | NOAA-20 | DAMIANÓPOLIS | GOIÁS | Brasil | 5206701 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24c44240-cd15-39ef-aba4-482f00aff129 | -15.52264 | -39.88023 | 2025-09-30 03:49:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f589fb66-0cfa-3961-849b-441ee1424cab | -15.03047 | -42.3316 | 2025-09-30 03:49:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94694ece-1c6c-3164-abe9-4fc2cb2edc35 | -16.40636 | -47.03875 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 056bc92a-4a35-3e34-8bb3-a89aee150c3d | -15.23537 | -50.09899 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53218647-9109-35c0-a869-f098947286c7 | -15.66252 | -45.24562 | 2025-09-30 03:49:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02640e3e-a031-3d16-9cd5-9f13eb1a0c97 | -13.83652 | -47.47988 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72d1a221-5d5d-3e0e-9da6-5a9acd5eb41c | -13.38743 | -48.06637 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0768c86e-5be3-3d28-8daa-753e947f9f1e | -11.69644 | -44.31732 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6621451b-a1b9-3ba8-9b98-77d863818984 | -17.4206 | -45.05579 | 2025-09-30 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a392d6e0-3256-3a40-87a0-dea07b070111 | -17.73429 | -46.67355 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a70c502c-b807-3290-97f5-55b1cb1f0f42 | -12.77479 | -46.86195 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16e47288-e90d-3952-a7d8-b21329fefc0e | -15.68356 | -46.25948 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e5b4b77-73fa-3155-bfc6-be26cac30d62 | -7.04481 | -46.42083 | 2025-09-30 03:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a34a2d28-3ca3-3127-b263-f21275b2195d | -14.72349 | -45.22172 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d803f14-dec9-39ae-bd33-5eb09cb4fa54 | -15.5383 | -47.87354 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 068edf00-9828-3736-9597-2938e6096a1a | -13.82207 | -47.49812 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54f06b24-b787-358c-b213-cfc7631c0f9e | -7.28534 | -42.85307 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6146390c-40cd-3a3e-9b48-ab1d69d1ef33 | -11.22533 | -47.20204 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f03f662-2653-3f84-992d-a0b5f3fa5f46 | -16.40834 | -47.0458 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 192b446c-d66d-3f54-826f-182eff5a22f0 | -13.67379 | -44.21729 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 336d3d49-19ca-3fa6-a550-9b63fdb6937b | -7.05709 | -45.1959 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| c89d43f2-cddb-3b4d-bcea-5d71682a8719 | -15.26544 | -49.50579 | 2025-09-30 03:49:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21f849dc-0fa3-31fb-8d0e-a1f8ac56d1ad | -7.0167 | -45.21829 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 076ab260-b6db-3daa-8676-24aa4c7464a0 | -17.23366 | -44.11193 | 2025-09-30 03:49:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 945b916a-c9cc-3cb1-a32c-b781063bc3f9 | -13.79727 | -47.87094 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00e1938a-ea52-3975-9835-b1737ef19865 | -11.72319 | -44.44454 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8652f78c-2730-3385-bbf5-65024b596e71 | -5.74595 | -42.66824 | 2025-09-30 03:49:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| ac96e820-f675-3db2-bc8c-1438009b8067 | -11.70361 | -44.32763 | 2025-09-30 03:49:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d10dc81f-9ea4-378e-9759-c97d91ff16d0 | -13.39745 | -48.0761 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e27cf8e-ffa5-3c34-b1e6-83552d164e3f | -15.30053 | -46.41688 | 2025-09-30 03:49:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 856d2370-4720-3d92-af0c-14c76f5b1d0f | -12.75317 | -46.85063 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26a0b157-b181-3a62-a04c-9d55c0e5ea7c | -14.69655 | -48.14359 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bcc4e450-9534-3804-8cd5-64608c6c69c2 | -12.74406 | -46.85688 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 001881cf-87fe-3909-8291-2243ac6c63ca | -15.38566 | -47.07554 | 2025-09-30 03:49:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2c9d49cd-f581-367e-baee-286ded929fe0 | -13.38896 | -48.06197 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 86bf2b37-1e1c-3fe2-8e52-5a0dc5040e2a | -6.25565 | -43.63136 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5b9e4e0-740e-3fcc-b5d7-11aa3279dc62 | -15.85982 | -46.23502 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cc5a5a5e-32c9-3811-ac0c-c7c730bdc3ac | -6.27934 | -43.65916 | 2025-09-30 03:49:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 478ff6c0-0497-3d8a-a47a-101fed2a383f | -18.19271 | -45.21984 | 2025-09-30 03:49:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7cd600b-ee7a-38fc-8279-8f6fe40dc9cf | -12.82368 | -47.0046 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2227b37a-1b0e-39d8-a644-66741402f95e | -14.50533 | -48.46658 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a704b4e-98bd-37c9-93ba-22f33eeb3b50 | -12.81742 | -46.99944 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3987ccb3-a24d-3b68-bdc6-bd24e9e6a467 | -14.53672 | -48.24986 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 286151e1-2511-3559-90b3-fe3bf15c8f79 | -17.08726 | -48.56586 | 2025-09-30 03:49:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c1f607-ba8e-34bd-af79-184e7d01d374 | -11.90792 | -48.05935 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 751c3aea-3bd3-3e39-b3d6-af6b1842b4d1 | -19.52242 | -43.90117 | 2025-09-30 03:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db12117a-e8db-3d69-b0dc-de6d1c96c53b | -7.30171 | -42.85086 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b7dec7ac-9c00-3051-99b1-efde4bcb6ae5 | -13.23325 | -43.37452 | 2025-09-30 03:49:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 29e7a0d2-ef4a-37c0-815f-cddfd904c5fb | -12.75392 | -46.87474 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a317a00-23e5-30ae-955d-8bf7c702798e | -14.71036 | -48.24117 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a7d56de-8e11-3c67-bcaa-c17b4811b508 | -12.84403 | -46.9712 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33f96b5c-f4a0-37e2-8db8-98887b7f0647 | -12.93961 | -46.76091 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68fd3bb5-a8cb-3c80-a1fa-29c4f2395beb | -7.05103 | -45.20076 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13318092-7d37-376b-9304-340e67997b89 | -16.36813 | -49.12915 | 2025-09-30 03:49:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| feb48f25-ecac-30f9-a296-136958788436 | -14.52833 | -48.38293 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfe216c0-63ae-3c7d-ad41-a12235ad68b2 | -15.46983 | -47.94299 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1742485d-9edd-3ee8-86e8-561295e1fe4e | -12.84528 | -46.88004 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e166b5c-4fcc-3bb4-9934-81b5dd3461a0 | -6.36995 | -45.63694 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 689fc453-0a68-3531-b110-e9905b0c021a | -13.38584 | -48.07748 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14c27604-d17f-370c-b682-9cefe23e7a3d | -15.24581 | -48.75473 | 2025-09-30 03:49:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c5ed9b4-1eb9-3948-b720-41fcb4f04a3b | -11.25837 | -47.23286 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 898545fd-52b7-3f64-97a1-7f5fcda6b03c | -6.39325 | -42.89777 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 99c7ec7a-34d7-3e96-86f0-21a3dec15e48 | -7.29884 | -42.84205 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 78d6c3b7-c52f-3b24-9185-a561ac68da6e | -19.50663 | -41.7016 | 2025-09-30 03:49:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00dfc2bd-a446-3d16-8f32-ee59533628fd | -15.1957 | -50.18787 | 2025-09-30 03:49:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bce8d2f6-539e-3018-97a1-33638d390514 | -12.8965 | -46.76723 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 334ffea7-daf3-3101-b769-0605a81ac6da | -15.92158 | -46.20566 | 2025-09-30 03:49:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea99ea86-fe91-3993-a96a-9081c6d39583 | -13.03137 | -42.80637 | 2025-09-30 03:49:00 | NOAA-20 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ef6191d6-6f5a-3bad-8eb4-27a14de7bc67 | -6.43061 | -43.07779 | 2025-09-30 03:49:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a3ca151a-cf8d-3d78-9270-ad2dfa6320ee | -13.36285 | -47.81891 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a22a0c4-85eb-3f9c-bebd-a04668becee4 | -5.81707 | -42.86245 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d4a00629-6e8e-3d0e-970c-e820d122ff4e | -13.57053 | -48.06385 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6156d90f-9efa-38e8-84dd-48730217b37a | -4.95512 | -47.60903 | 2025-09-30 03:49:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b9ba0a8-4d69-3e67-b9ae-e0ab5210fafd | -6.21124 | -44.20953 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5fe7452-b572-385e-87ef-0e6a117d4df2 | -7.01012 | -44.48177 | 2025-09-30 03:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 83ba5001-a071-31ab-b19c-e9fc02329729 | -12.8631 | -46.91188 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73239ffa-3df4-3d8a-a668-1de0799e01b9 | -7.1277 | -45.49947 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92e92531-f3ac-3e9a-9651-cd99139abfc8 | -14.18845 | -46.60489 | 2025-09-30 03:49:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0557848f-e642-3f87-989d-05a36bca71ce | -15.2459 | -49.7136 | 2025-09-30 03:49:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1cdd60bb-d32d-34f4-b2fa-d6cd832d9c95 | -13.66567 | -44.30733 | 2025-09-30 03:49:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 4c4b576b-be23-38da-93bb-0a198f0aa53c | -15.72015 | -47.58514 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7852ea12-cd48-3a00-9100-f05d9452a087 | -17.39238 | -47.12729 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7214a82a-5516-3fbe-bd77-da4a04d33b67 | -14.51098 | -48.46793 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88c1f55b-00ec-3c25-b848-3ae4ba87f15f | -12.83064 | -46.99633 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1db9289f-563e-3c72-a977-c9af51653404 | -14.69468 | -48.23573 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README38.md)
