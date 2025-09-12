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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c03cec89-6bfc-33e6-abed-6865d3fa03e8 | -11.31612 | -50.78257 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5faa9497-808d-3db2-89c4-dd42d527dc31 | -15.15703 | -52.40703 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dbd72682-0894-3bd1-a8c2-4a1b1a7d2fc1 | -15.79046 | -52.23351 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4788b4c3-42f4-3640-92d2-f94aadfee833 | -13.3127 | -40.5661 | 2025-09-12 04:06:00 | NPP-375D | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7a65544d-6076-3e47-91ec-3fe4426816eb | -15.49461 | -47.34663 | 2025-09-12 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf5061d3-96f2-33c2-853e-af3aa04d156e | -16.25027 | -52.65699 | 2025-09-12 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02c28033-1ad1-3cce-884f-dc3070186e16 | -15.52722 | -48.55814 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00a00a1d-553c-38aa-896c-b433d363bc1e | -16.41047 | -45.68758 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdc5d762-726d-3545-b4ed-466f7acc95d5 | -15.22301 | -44.05432 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1678a060-5196-33e1-9a0b-60fe9b6e1827 | -15.17715 | -53.81901 | 2025-09-12 04:06:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 107bbade-8aca-3a3f-98af-2d75150c34fc | -11.92737 | -50.70103 | 2025-09-12 04:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68bbdb4f-c094-3733-b44a-f534a3bee040 | -15.57867 | -54.76019 | 2025-09-12 04:06:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ddf8cb38-3125-374a-be95-e718396e6612 | -11.53273 | -50.39621 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 92b52e64-e7b2-3357-a7c4-a8d52c4488f8 | -15.10908 | -52.46643 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf68d7fa-79ec-3b89-ac90-c48876bfd02f | -14.32493 | -54.12329 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4777d1c-182c-3f85-a86c-6fd0a8ceede6 | -17.81815 | -46.73197 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53dd18ab-9826-329d-b913-cdad0d3e1a38 | -17.58514 | -42.16688 | 2025-09-12 04:06:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cce3e88e-3288-3e6b-afd6-d9b2baeaafc1 | -15.60904 | -52.74145 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 980b0757-f778-3979-bead-c7c8958b6e9d | -13.90063 | -48.25515 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e0f04a66-5238-3e4a-b7b4-4bbe45f6ff3b | -11.86109 | -46.75886 | 2025-09-12 04:06:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f3c5051-1df2-3d63-a06d-80807565e3ae | -15.48708 | -47.34166 | 2025-09-12 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fa6f7c7-9350-3e22-bdf1-0aaf9ca16cb9 | -15.08374 | -52.44541 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a09d801-1c98-3b33-b5d7-8df32b580e46 | -11.50163 | -50.37298 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 407d4a74-ef51-3581-a72b-bc3220c2f007 | -11.79475 | -50.57085 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79b7b20f-ae59-3eef-bec6-21c00394ec09 | -17.73215 | -46.14762 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa72a434-7a36-3e07-8694-6cfb8f5bea22 | -16.08237 | -49.31955 | 2025-09-12 04:06:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b72bcc5-452f-3494-a581-68c9e0b38ecb | -15.14896 | -52.47495 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ee2fa743-22f2-32b7-a283-dcc61768db32 | -16.43689 | -49.02727 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b76ffb5d-505a-346b-a665-b963f951b889 | -13.25203 | -43.77006 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb806736-9b67-3591-8ff8-c38afe0fc86d | -15.52481 | -48.55413 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cfd7bf8-34d4-3b30-9e60-9eb8c78af9c3 | -12.14551 | -44.86745 | 2025-09-12 04:06:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d820adb1-fa0f-3a22-8ab3-4f17a99b1f01 | -11.48508 | -49.27561 | 2025-09-12 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 49dbd2a6-5883-3874-9593-0cf10bcc9b18 | -16.65734 | -47.62473 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae92d82a-adfd-3063-b592-ec70202701cd | -14.12055 | -44.32023 | 2025-09-12 04:06:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e09db1b-296e-35d4-92a7-5a98947a2aa7 | -18.01814 | -46.85691 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e51e11e0-3415-37b4-b158-91ed1930ba77 | -14.38954 | -52.96 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e63fbef-6aa2-3b88-9bcb-46d18151f7db | -14.45138 | -47.31104 | 2025-09-12 04:06:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12227f20-81d1-3dbf-8c71-3eab2ac56735 | -12.82367 | -52.96876 | 2025-09-12 04:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d58c2ca-7964-332c-8e5b-c1a414d2d9b6 | -15.10988 | -48.02075 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 223d83c6-664e-3098-89e4-575bdbcd9efd | -14.18596 | -46.20262 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c137419f-a7e7-38b8-8014-c6e59ea3b23d | -11.09014 | -51.97943 | 2025-09-12 04:06:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d3fef2-8bf5-3616-83b8-eca52a4199b5 | -11.70309 | -50.60078 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a0a53d5-6474-3fd0-a96e-fadbeb507a1a | -16.66141 | -47.62551 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1f123b7-6c93-3f1c-8c0e-e8d833fe4a55 | -13.17197 | -50.0912 | 2025-09-12 04:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d72f2c40-4b9b-3323-b235-cfb981741a50 | -12.84229 | -52.97528 | 2025-09-12 04:06:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f56e93c0-b1fd-3619-af55-0067587da613 | -15.09566 | -48.01366 | 2025-09-12 04:06:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 870b3cff-7bc7-3776-a144-b35925941e56 | -11.78293 | -50.56304 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60e5c748-6bab-30ea-80d4-868b4c3b8834 | -17.35029 | -46.68129 | 2025-09-12 04:06:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6f388cab-f737-3c40-9d44-e6cf65f3f518 | -16.66478 | -47.6301 | 2025-09-12 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a965de29-4f7b-3b0f-b161-2ec31270ddbd | -15.68821 | -47.01151 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e1875940-e2a3-381d-9ac6-0f4fdecfe32e | -15.11736 | -50.08792 | 2025-09-12 04:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2360819f-c81e-317f-838d-7850600f1c9a | -17.54772 | -44.53956 | 2025-09-12 04:06:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1639a1cb-2b89-3b24-ab92-05fd16d14d23 | -12.91389 | -54.75578 | 2025-09-12 04:06:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ae3003d7-c9d1-3f15-b8d4-0253510d2533 | -15.15271 | -52.39928 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3bb8086c-b512-3eac-bce1-a12786463cd2 | -11.9417 | -51.18235 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 73c2a581-06f0-3714-b211-4621a7f49a50 | -15.92521 | -51.79921 | 2025-09-12 04:06:00 | NPP-375D | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61aad1d2-b598-3ff3-a784-0e401f825e6f | -15.16765 | -52.41298 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45438879-4dc3-3107-91fd-281748638980 | -13.24855 | -43.76945 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68dd624d-3828-3db0-80c6-6e811139e5ee | -13.26772 | -43.74065 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee1bf749-2f0a-3364-8af5-8d704624579a | -15.68167 | -47.04804 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f54df43a-ca51-34ca-afa1-16fca7bc5217 | -14.17824 | -46.20094 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4eebd683-7fd4-31a3-8256-50f713ac0bc7 | -11.49113 | -49.27063 | 2025-09-12 04:06:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3acb66ba-7559-34dd-bd7e-ff87a0e1ab83 | -16.43318 | -49.04645 | 2025-09-12 04:06:00 | NPP-375D | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3be636d0-a05b-31b3-b690-c9108373da79 | -12.08958 | -47.58164 | 2025-09-12 04:06:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd9611c7-9865-32cf-a47e-da2e89c75f2f | -11.98446 | -51.14066 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 455147de-d78e-37b3-8ad2-5bb8bf2fbc21 | -12.93238 | -48.00026 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 20d7d25e-bd36-34ac-b93c-e249afebf402 | -14.53543 | -42.47654 | 2025-09-12 04:06:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ead08ee-647a-3ae1-bd10-d866843e217d | -15.6943 | -47.02352 | 2025-09-12 04:06:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6e419fed-aa67-3302-8444-2dd085718e95 | -11.94096 | -51.18609 | 2025-09-12 04:06:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ca4706cc-f50a-395c-81e0-9a789e814f36 | -15.87863 | -48.17999 | 2025-09-12 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 757ab30c-2a61-392f-ad1d-1c5f5d22589d | -12.24702 | -47.33449 | 2025-09-12 04:06:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd15c60f-08c4-3a4a-ae0e-9d9361c9342d | -17.91827 | -45.71003 | 2025-09-12 04:06:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64222851-8794-33c0-839b-660408dfdddc | -11.18179 | -55.07383 | 2025-09-12 04:06:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0560e538-ba70-303e-b017-501c1b919ba7 | -14.41405 | -52.93159 | 2025-09-12 04:06:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8692f798-6788-39f3-b0b9-5ff71448485c | -13.00136 | -47.99977 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12e66bd0-135e-3a00-88b7-7a7baec049ec | -14.1646 | -46.18747 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fddea7d-8af4-301f-aa4a-0fe9649d153e | -15.08241 | -52.44621 | 2025-09-12 04:06:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0606309a-c74d-3790-9d5e-4e137ba40e8a | -13.27677 | -51.71854 | 2025-09-12 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a94036e8-6527-30b4-bf9e-d8570681ea31 | -17.8165 | -46.73361 | 2025-09-12 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5f4204a-b4ae-3b7e-ab25-c3ce88fc4af9 | -11.52229 | -50.38068 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6c88202d-7e95-3157-8607-1164f5581f79 | -12.981 | -48.01069 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a727d02f-fada-34a9-9437-11116b206c6a | -13.9851 | -48.21167 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d14612e-87ea-3e66-9cfa-cd86bcbf61d1 | -11.52166 | -50.38406 | 2025-09-12 04:06:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3bb77633-f807-3a33-9dca-80e4712397d6 | -11.64853 | -50.58698 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52917df6-32cc-32ee-99b5-6d15753dee31 | -18.05294 | -45.44268 | 2025-09-12 04:06:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e63eb303-7425-3983-b42d-334b09563097 | -16.25875 | -46.78464 | 2025-09-12 04:06:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbc54e27-c835-377a-96d2-f6411f06af36 | -12.92798 | -47.99921 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 883bd06d-afe1-3d9d-921b-14d1f0159d92 | -16.43684 | -45.68795 | 2025-09-12 04:06:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2dcbb7b-a6fa-3719-8fad-d6a5e39a16c3 | -15.24093 | -44.0535 | 2025-09-12 04:06:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d4ff44b5-2ab5-392a-8c92-2fe7eb12b776 | -13.27184 | -43.73736 | 2025-09-12 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c127179a-783d-32f2-9104-c324e53f6fe4 | -14.17738 | -46.2058 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 73bf6597-a5d2-37db-8b37-186c83bc731a | -15.15414 | -51.25177 | 2025-09-12 04:06:00 | NPP-375D | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40a7347f-5550-391c-8209-169af37f4f0f | -13.92177 | -47.97134 | 2025-09-12 04:06:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40f8c87e-aba0-3618-abf7-b9d353aaf8c0 | -12.89201 | -47.95481 | 2025-09-12 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3de1c44-c946-3c46-b71c-17ea5d08fd16 | -15.12155 | -48.60381 | 2025-09-12 04:06:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e57c4ad7-dba2-3bd4-b265-0e779ac1b546 | -13.27117 | -51.71727 | 2025-09-12 04:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e372b44-38d7-3266-8228-7cca794cb5d8 | -15.53358 | -48.556 | 2025-09-12 04:06:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 10d8f037-b298-37e6-b56b-57ca93dc5b24 | -14.1727 | -46.20956 | 2025-09-12 04:06:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7fb61922-0c88-36b8-b7a1-ff93395dde9f | -11.72732 | -50.62013 | 2025-09-12 04:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68e032e6-b6af-3c90-84c8-8329751154b3 | -14.50209 | -53.92531 | 2025-09-12 04:06:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README48.md)
