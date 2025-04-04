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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 239064b2-d0d8-349b-ad25-3fd836a45a15 | -6.53504 | -43.09822 | 2025-04-04 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d7d6601-69c8-3104-b6ab-062ca2ee6a08 | -6.29575 | -45.26598 | 2025-04-04 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f987df4a-83bb-3e7b-9ab5-c269b0eb317e | -6.53957 | -43.09145 | 2025-04-04 04:19:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa2276b3-8577-349e-b5f3-759ddc14108b | -6.87632 | -45.22918 | 2025-04-04 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1024a68-20c9-3f24-ba3d-fa4483da36f9 | -10.34941 | -38.47617 | 2025-04-04 04:19:00 | NPP-375D | NOVO TRIUNFO | BAHIA | Brasil | 2923050 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8c1e2587-7bd7-3133-bb08-ddf25b8f18d3 | -6.2142 | -48.05468 | 2025-04-04 04:19:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 093f80ee-e7c8-3c16-9e8c-2ffb93d1c628 | -8.11512 | -43.12651 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 01b0efce-bc68-3c82-a4cf-51507a6bffe3 | -8.10085 | -43.12811 | 2025-04-04 04:19:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eff03044-eba1-3569-8548-0639fb94952f | -6.96648 | -43.01766 | 2025-04-04 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f7177d69-6517-3b71-9f15-71d75539e45c | -7.23001 | -44.77207 | 2025-04-04 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c32defa3-1bc2-3d30-8168-b1d150ad4697 | -7.38085 | -43.54471 | 2025-04-04 04:19:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee20a903-0a0d-3025-9305-f4a09364dcc0 | -12.28197 | -43.52898 | 2025-04-04 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| be6dab33-6af1-3568-80cb-9ade0d72b95c | -12.56038 | -45.33628 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 086cfe18-3a69-33f2-8b3d-29ff9e39468f | -12.50328 | -45.5055 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6bd77cf5-f2fa-334d-8714-745843d8bcdf | -16.63515 | -43.3589 | 2025-04-04 04:21:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffdd1c1b-b262-3ad3-b2ac-8c65e32fe1d5 | -12.55704 | -45.33574 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b0c8f72-c72c-32f3-9e94-5b267dec48a0 | -13.48488 | -44.03148 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 366e5f44-5d4a-3d70-b7c2-f48242b7bd89 | -12.28138 | -43.53291 | 2025-04-04 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e96e1db3-aec7-38a6-9e4d-1ae1e7592f70 | -10.66743 | -44.3974 | 2025-04-04 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9bf9f71-617c-37dc-bc6a-06cf7792d855 | -11.26813 | -52.47228 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e720e0b6-6c08-3acb-a089-9c667d3dc4da | -12.27847 | -43.52844 | 2025-04-04 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b7955d3-0978-3707-a735-cf177bbceabd | -16.4548 | -47.55567 | 2025-04-04 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 970c2f7e-90da-3429-95a2-20b5f3b3f339 | -16.34953 | -43.69466 | 2025-04-04 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c0bf45d-3cfd-318a-9719-9d3235011da3 | -17.83292 | -42.6247 | 2025-04-04 04:21:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ec63c7e9-e472-3962-a108-6f42c86ab197 | -11.26858 | -52.47649 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0143eccc-3f91-3397-a59e-58c51cbd9af0 | -17.15718 | -44.79426 | 2025-04-04 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7241937-8163-3dc5-89e7-c829b308f60b | -11.26581 | -52.46634 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c829102-48fe-356d-8019-5304b01addde | -11.27778 | -40.98123 | 2025-04-04 04:21:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4fae82a1-b4e1-3188-a52b-ef3691c61591 | -16.6799 | -43.88324 | 2025-04-04 04:21:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31b498f4-257a-3a93-bd0d-c69311d2458a | -11.26945 | -52.47181 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f37c9b5f-1c00-39f8-ad84-02fbffb75928 | -17.83223 | -42.62971 | 2025-04-04 04:21:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a4a7fdae-6e4a-3659-ab2e-fb58527aae90 | -16.29696 | -45.09752 | 2025-04-04 04:21:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b4ddf9-3b99-3f0a-bb3d-57e5655a5b78 | -11.26409 | -52.47562 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4360c10d-3d6c-3657-bb42-1b78131d2bef | -13.04434 | -53.71023 | 2025-04-04 04:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e55a9b-9559-37a9-9ad4-a097ba6551b5 | -13.61839 | -40.95251 | 2025-04-04 04:21:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 597afe18-180a-3337-9f00-dc48f46e75ab | -16.45813 | -47.55624 | 2025-04-04 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61172da7-6c62-392c-b2de-250b81271cc9 | -11.26445 | -52.46679 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cca68e6e-9897-3613-8542-4d67f3999cfe | -15.76158 | -43.9355 | 2025-04-04 04:21:00 | NPP-375D | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8085ab5-c672-3c26-8659-239a2c7f56f3 | -16.68234 | -43.88571 | 2025-04-04 04:21:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3394760-2a84-3b7c-b885-587153c0616c | -11.03087 | -44.42325 | 2025-04-04 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 51115d58-5a8c-3595-a863-3b5a141469ec | -16.29354 | -45.09696 | 2025-04-04 04:21:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f43dc2b-2761-3684-825f-84c236e1be7c | -17.15371 | -44.79372 | 2025-04-04 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6931af48-f97b-3cf2-83a6-1b9bdd677efd | -13.03637 | -45.08101 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 460ab670-cbb3-3d08-af02-26a81ea15e03 | -13.03302 | -45.08048 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ff80afd-6995-3f06-ab13-c705a2e20392 | -16.63451 | -43.36341 | 2025-04-04 04:21:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7f45a9c-ceea-38ff-9e79-ed4304b9f44f | -17.59575 | -43.19957 | 2025-04-04 04:21:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f4eb8f4-2c24-3220-a86e-95d2d1a852d4 | -11.27597 | -40.98217 | 2025-04-04 04:21:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f91a6855-89da-3d8d-ac8e-9d0535aa6255 | -17.83289 | -42.62622 | 2025-04-04 04:21:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6360a237-d267-3caf-9b3d-a1c996b4401c | -13.0375 | -45.09598 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f33a3e8c-3150-35a8-88b3-a0a0941b525d | -13.02855 | -45.08716 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dc5ce513-c0f3-3c2c-8d92-08ff3a918e5d | -11.2673 | -52.47697 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 55882274-7e2c-3a27-a2c7-93e991dbb590 | -11.02921 | -44.4341 | 2025-04-04 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67fc1f69-9dd5-3ca6-b964-7e74da621ab7 | -11.03257 | -44.43463 | 2025-04-04 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90c214fb-a08d-3c13-947f-6917279ea470 | -13.62678 | -47.81018 | 2025-04-04 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23ca527a-87d5-3b73-9b1c-0170d7fee080 | -13.03526 | -45.08823 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9bf45416-84d1-3338-a383-89ce243d0388 | -13.03246 | -45.08409 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70d8e979-0000-323d-8c61-94eacf50f0f5 | -11.03255 | -48.81526 | 2025-04-04 04:21:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 161cbc6f-5104-3b6d-988f-385976a5aa80 | -17.82833 | -42.6291 | 2025-04-04 04:21:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5061a3d1-06b7-3c28-b1cd-a899b23de8fa | -16.45755 | -47.55985 | 2025-04-04 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9845fa5e-8210-3d77-847b-3db687c7f3b1 | -17.83678 | -42.62686 | 2025-04-04 04:21:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5d56ab1c-4916-3698-97a3-b858e96d32de | -14.72971 | -46.83006 | 2025-04-04 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df70a9f4-01b9-32ee-af5d-9937afcc486b | -13.48141 | -44.03093 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a923d0f2-2707-35a4-8b7f-b93f6af2485f | -13.028 | -45.09076 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2fef8aa0-b76b-3619-a644-b79caa700681 | -14.12678 | -47.65838 | 2025-04-04 04:21:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41b79764-6e02-3238-81ca-1c9d664a48f5 | -17.82899 | -42.62559 | 2025-04-04 04:21:00 | NPP-375D | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| feb1c7cf-424c-305a-8f83-74579632f8fa | -13.02464 | -45.09023 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 389b8094-5d0b-3041-ac01-3ba8e58450dd | -16.21689 | -43.74184 | 2025-04-04 04:21:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02a36089-01b9-3586-8750-fafb7642261e | -13.0481 | -53.71635 | 2025-04-04 04:21:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42c439a7-f23b-3e20-8a62-8124bae9df60 | -13.03191 | -45.0877 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddc5699f-34dc-32ca-bead-9efee6bd35c5 | -13.64084 | -41.35861 | 2025-04-04 04:21:00 | NPP-375D | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7143211-1b35-3fa5-9ffd-b2d370cc53ee | -12.50661 | -45.50604 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1dd1405f-f41a-36ed-9746-485aa3148891 | -10.66463 | -44.39327 | 2025-04-04 04:21:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52e65877-0001-33d1-8772-ac3b5e44858d | -13.02409 | -45.09384 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a52a603-7e2f-3b14-bb4e-ba302351700d | -13.0252 | -45.08662 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ed1c4207-a5df-3a5a-85fe-845f137c9062 | -15.60329 | -42.31724 | 2025-04-04 04:21:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87866e47-3737-330a-836f-d17f5239f521 | -16.67875 | -43.88512 | 2025-04-04 04:21:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0edb7b3e-0257-3e58-8596-f88e445e1623 | -12.49995 | -45.50496 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b756e49b-d650-3135-9f56-63740f6e2089 | -12.27906 | -43.52451 | 2025-04-04 04:21:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fa3776-9442-316b-ba2b-7ff3356435d3 | -13.03861 | -45.08876 | 2025-04-04 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26138a86-e664-3da1-a9ef-440142d5cd60 | -11.27991 | -40.98281 | 2025-04-04 04:21:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71a02bc2-235b-3aff-b4e4-3e41eb6a242e | -17.1566 | -44.79822 | 2025-04-04 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 064f740c-451f-32ab-9a59-8204a4b4c537 | -17.16066 | -44.79481 | 2025-04-04 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ce926af-08cf-32a8-8367-f0c0528b7623 | -13.66826 | -44.05893 | 2025-04-04 04:21:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dae4fb73-39af-3f83-870b-9b0446a56961 | -20.4791 | -53.67555 | 2025-04-04 04:23:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aca5aeda-c22f-32d8-8974-fdfee0aac514 | -19.44419 | -54.78839 | 2025-04-04 04:23:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0866e372-dff2-33c9-a13e-4f2ac86e581f | -21.66584 | -48.7718 | 2025-04-04 04:23:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2144372d-a3a3-3369-817f-8e3300158328 | -20.31048 | -45.58141 | 2025-04-04 04:23:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 534d4b25-de5c-3272-b375-27ac43c83477 | -19.44068 | -54.78237 | 2025-04-04 04:23:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8048b479-6cc6-3035-bce7-66c7a611c619 | -18.76665 | -45.42362 | 2025-04-04 04:23:00 | NPP-375D | BIQUINHAS | MINAS GERAIS | Brasil | 3107000 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55782b56-0dd8-33bc-9e9a-252b86c79cfe | -20.57563 | -56.03392 | 2025-04-04 04:23:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| acf5037d-e6fa-355d-a3dc-f04274889b86 | -19.15048 | -50.59095 | 2025-04-04 04:23:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc4c48e0-e19b-38f5-b017-a0465050575b | -23.40445 | -46.55791 | 2025-04-04 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 439b9418-71db-3122-a2b7-083ab32a2585 | -21.19557 | -44.93742 | 2025-04-04 04:23:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15276f5b-9606-3c1b-8c64-e64ed042967d | -19.44516 | -54.78348 | 2025-04-04 04:23:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2af632d8-0053-31e8-af4d-390c38b1ca21 | -22.678 | -42.85349 | 2025-04-04 04:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a8dcdfc8-e473-3c70-8626-3c58a5f280ee | -20.57926 | -56.04051 | 2025-04-04 04:23:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 93bd197d-7c1c-37e0-b723-3c27cd77b9ca | -22.67389 | -42.85293 | 2025-04-04 04:23:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| cdf79889-57ea-37e1-9326-70cab6340be0 | -20.478 | -53.67667 | 2025-04-04 04:23:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9f556d5-b6e3-3e83-8b9b-8a389f20859c | -19.4397 | -54.78729 | 2025-04-04 04:23:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 62e8a4c8-50b5-3302-8957-1c802fc394bb | -20.58039 | -56.03507 | 2025-04-04 04:23:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README4.md)
