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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0458ed9d-bee7-317e-94fc-ca992578fc51 | 0.8843 | -60.087 | 2025-01-20 00:00:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 53.1 |
| bdb24588-95fc-37ee-9276-3926377abd63 | 0.9026 | -60.0869 | 2025-01-20 00:00:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| fdca07e9-4840-3fd3-892b-a143c6326340 | -5.2173 | -43.298401 | 2025-01-20 00:00:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c063148-b694-337f-8a93-cd664c333ec0 | -8.5748 | -35.647598 | 2025-01-20 00:05:00 | METOP-C | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6d53eac7-8136-3b7e-87c9-b9a2532d835e | -7.9781 | -35.218899 | 2025-01-20 00:05:00 | METOP-C | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c2f6c424-75d2-3211-9c03-2048d48b179e | -6.9826 | -34.893902 | 2025-01-20 00:05:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 75a5aee8-93fa-318e-b3f9-99a120d17206 | -10.1194 | -38.269699 | 2025-01-20 00:05:00 | METOP-C | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5103e3d3-68b3-3fa2-8b64-9f5debdff3b0 | -10.262 | -36.417801 | 2025-01-20 00:05:00 | METOP-C | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 824775c6-6799-380d-ab6c-fe3fb0b6ba78 | -9.0139 | -35.451698 | 2025-01-20 00:05:00 | METOP-C | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d35b7c22-6770-3ffa-916b-0a55b6512920 | -9.3523 | -36.0131 | 2025-01-20 00:05:00 | METOP-C | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 040ec4fb-be9d-34b5-87be-d343039c7a1b | -10.1178 | -38.262699 | 2025-01-20 00:05:00 | METOP-C | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 59913ba3-2b22-3eb5-8d1f-ffb545608ec5 | -6.9804 | -34.884998 | 2025-01-20 00:05:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e8a8d475-7ead-3f49-a126-9ac2b9f9f6a8 | -9.012 | -35.4436 | 2025-01-20 00:05:00 | METOP-C | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 46746a8e-f534-3bf6-877c-a1a72a8f8767 | -7.9801 | -35.227299 | 2025-01-20 00:05:00 | METOP-C | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 06cd2ebc-b47d-3371-b729-4c7428393319 | -6.9783 | -34.875999 | 2025-01-20 00:05:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 27687bf8-0767-3373-97f1-f5a15232cb2c | -9.3394 | -36.0108 | 2025-01-20 00:10:00 | GOES-16 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 102.9 |
| 83d07e34-d1c2-3e51-aff5-30ba84bc0c47 | 0.9026 | -60.0869 | 2025-01-20 00:10:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 99192ef0-1970-32fe-ba5e-5ed55c3e5f46 | 0.9026 | -60.1059 | 2025-01-20 00:20:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 5dcc54e3-69c0-38b0-88be-aa9b22e5cd92 | 0.9026 | -60.0869 | 2025-01-20 00:20:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 6e4fba0a-905d-31a4-a5f2-5d806215a42d | -9.3587 | -36.0076 | 2025-01-20 00:20:00 | GOES-16 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| 8b03195e-9ef6-3d30-bde1-13cc79ec6aa7 | 0.9026 | -60.0869 | 2025-01-20 00:30:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 66.0 |
| e347ec1d-2bd6-3cf9-ad74-4d935b2d9765 | 0.9026 | -60.0869 | 2025-01-20 00:40:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| f6af16a3-0fe1-3db0-a7b3-e930a33221e7 | 3.1623 | -60.490398 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4ac060ad-cde4-30f7-bc03-2c19e04afc73 | 4.3927 | -60.472099 | 2025-01-20 00:46:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 18c71e79-1766-3670-b3e5-94d4712e3fea | 1.3531 | -59.981998 | 2025-01-20 00:46:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 489adb0c-370e-3b9b-baae-138c0fa45579 | 1.3511 | -59.990799 | 2025-01-20 00:46:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c8040e46-898f-3794-adfd-b2e459ae2ae1 | 0.8024 | -59.8689 | 2025-01-20 00:46:00 | METOP-B | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ae21524a-344a-3d35-820f-5f6c7a64336a | 0.8953 | -60.049301 | 2025-01-20 00:46:00 | METOP-B | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 05deb8d6-820e-3f77-afba-a2f4b448bfc2 | 3.4162 | -60.416599 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 46773074-386a-3d4f-9520-86f77e21f289 | 4.3947 | -60.463402 | 2025-01-20 00:46:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 00ae7ca9-299a-3e84-8d33-7aca76822b59 | 2.9059 | -60.575401 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e83fa5b8-3997-370e-8d1b-d85fd70e7f3c | 0.6972 | -59.652302 | 2025-01-20 00:46:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a3199d0b-a05e-3e44-b1de-226e643ebebe | 0.8044 | -59.860001 | 2025-01-20 00:46:00 | METOP-B | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 307705d7-1789-361e-bb7d-f76f54165b58 | 1.3491 | -59.999699 | 2025-01-20 00:46:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 97daeba2-4dd2-337c-ac42-0a6f2da31561 | 2.8682 | -60.605499 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b9ba20a3-43fd-3de5-b1bb-b45755006b0a | 2.908 | -60.566299 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0c599877-3199-38ad-86ee-a362def4dae3 | 2.8898 | -60.6007 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3396093e-3933-39a0-a3ba-51e8d10c4bfb | 2.8996 | -60.602901 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e3bce941-bee7-3281-a195-78fe480ce1c3 | 2.8703 | -60.596298 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fb67f4bc-08a0-32ac-854f-3cd10ec52e1e | 2.8877 | -60.609901 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ac5ad292-8bdd-37b6-9f2b-0357a0d9ac77 | 2.9038 | -60.584599 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 44ef135b-8884-3362-87c5-51605160aedd | 3.4142 | -60.4254 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f1accbbc-ad0e-352a-9672-2e2433a71519 | 4.7719 | -60.705399 | 2025-01-20 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb774cf-359a-39a5-848a-cae3be565b9b | 4.6519 | -60.733898 | 2025-01-20 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9fc7d555-7ef7-3314-95a3-fa4b16b56af7 | 2.9409 | -60.153301 | 2025-01-20 00:46:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| deffb619-3da8-3970-8aed-78a0733886f1 | 0.8912 | -60.067501 | 2025-01-20 00:46:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0fb9be-9007-3ca3-a820-65d05419c77f | 0.8835 | -60.056301 | 2025-01-20 00:46:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6d38b3f4-8fd2-3c51-8365-33e55634fde6 | 3.4121 | -60.434299 | 2025-01-20 00:46:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ce0b97cf-bb72-3725-8e63-0ab58df94593 | 4.129 | -59.960098 | 2025-01-20 00:46:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5122c907-2040-3428-835b-260c0a32addc | 0.8933 | -60.058399 | 2025-01-20 00:46:00 | METOP-B | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e13df678-2cef-31a9-97c9-954b80f40d27 | 0.6952 | -59.660999 | 2025-01-20 00:46:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 82715702-79d1-33b1-9ce0-c3099c19d456 | -22.899099 | -43.705101 | 2025-01-20 00:46:00 | METOP-B | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8305645-4bfc-3bc7-9f8c-0767182b41ea | 4.1835 | -60.932201 | 2025-01-20 00:46:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 763ccbbe-6dbb-3809-8420-e764ac518732 | 0.9026 | -60.0869 | 2025-01-20 00:50:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 2ace8627-6fc0-3030-832a-73d03237eeea | -9.61361 | -47.63312 | 2025-01-20 00:56:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4783efe1-30cd-3cd1-941f-5819280957ab | -11.02732 | -45.04841 | 2025-01-20 00:56:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ca170fb4-09ab-3ca0-9ff6-0120d14fbd70 | -11.58911 | -44.8697 | 2025-01-20 00:56:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5f8a7015-e056-3ed9-b8d0-fd1d3ab6035a | 0.9026 | -60.0869 | 2025-01-20 01:00:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b0bbf63d-a6d8-38d4-aa59-62e1d0cac2dd | 1.35268 | -60.03102 | 2025-01-20 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 50cfa929-50b9-3bf0-8c98-e4e92fc9ba53 | 1.35428 | -60.03795 | 2025-01-20 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 317750bc-3b3f-33d4-bf7c-6d2772456dae | 0.88668 | -60.10339 | 2025-01-20 01:00:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 44.1 |
| fdde2db3-8a3f-3772-a2ce-d30ae24af359 | 0.88629 | -60.09775 | 2025-01-20 01:00:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 392f80d0-090e-3bf2-b90b-8fce5fa608b9 | 0.9014 | -60.10541 | 2025-01-20 01:00:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 8ba49dba-1ae8-3b7b-910e-a60e56365b00 | 0.90101 | -60.09978 | 2025-01-20 01:00:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8a2b9bba-d19e-3024-a592-94f5d66470fe | 1.3582 | -60.01185 | 2025-01-20 01:00:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 434a7d44-a826-3306-b795-17203cade975 | 0.89069 | -60.07646 | 2025-01-20 01:00:00 | TERRA_M-M | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 19.1 |
| bd1b1036-bd26-3607-8b0b-f6ea46020f81 | 2.91421 | -60.61623 | 2025-01-20 01:02:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 4a13512b-9240-38eb-a875-8e2966637894 | 0.9026 | -60.0869 | 2025-01-20 01:10:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 57.9 |
| f876a82e-057c-3edc-a625-dd23895d2a9a | 0.9026 | -60.1059 | 2025-01-20 01:20:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 89ff38a1-69f7-34af-a0be-d77aee4de175 | 0.9026 | -60.0869 | 2025-01-20 01:20:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 5b378300-3c4a-3084-bc0d-6ee1cbfdea3d | 0.9026 | -60.0869 | 2025-01-20 01:30:00 | GOES-16 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 4cf1ce5b-c618-311b-a64d-65d8d4ba0df0 | 3.4118 | -60.450901 | 2025-01-20 01:42:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 724d247b-57b0-3a18-a214-b2ecc0b26c6f | 2.9428 | -60.167599 | 2025-01-20 01:42:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aebb5e73-211f-36af-89e4-f8acfb0d2f9c | 0.889 | -60.092499 | 2025-01-20 01:42:00 | METOP-C | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 897fbe8b-1fca-3fb0-a6e8-d16d9cebaeca | 1.3467 | -60.019901 | 2025-01-20 01:42:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8dff6e07-12c2-39ed-ab35-0da466f8e9a8 | 0.8818 | -60.078602 | 2025-01-20 01:42:00 | METOP-C | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 843c5c36-fab0-31ed-be53-62b74eaeffc1 | 2.94 | -60.180099 | 2025-01-20 01:42:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 381fb9b9-ee6c-3a6c-8466-36a7d8bcf1d8 | 0.8792 | -60.090302 | 2025-01-20 01:42:00 | METOP-C | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 68731186-8ebe-33f2-9d23-c1a3448d0089 | 3.7391 | -60.635899 | 2025-01-20 01:42:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 71e53712-f5ea-3cfb-9ee9-e15803425320 | 2.9066 | -60.601299 | 2025-01-20 01:42:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d10ff99c-d24b-38d8-81d1-a36793ee1b01 | 0.8916 | -60.080799 | 2025-01-20 01:42:00 | METOP-C | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 60277c4f-86d6-3287-ae5a-e4d07d3fbf1b | 1.3494 | -60.007801 | 2025-01-20 01:42:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 57836f4e-eca2-3486-87a1-b458742d2fe1 | -7.3495 | -72.55753 | 2025-01-20 02:36:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 97e0df00-284a-3a5e-bc60-e0ef8a059dd8 | -7.35098 | -72.56782 | 2025-01-20 02:36:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d703dd27-0689-34bc-b9a3-1e6de1a65e0f | -7.34596 | -72.59999 | 2025-01-20 02:36:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 778ed4a2-c102-3486-89a9-5f55e8716f40 | -11.75177 | -37.993 | 2025-01-20 02:51:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 97d0df05-d8d9-38c6-b22b-7c954414e6d1 | -11.74465 | -37.99151 | 2025-01-20 02:51:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0edcea6a-4b42-3a6c-8d64-4d3c29b1bcf0 | -5.4401 | -35.66901 | 2025-01-20 03:42:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 734372f1-83ad-3d7d-8028-3053198b556d | -9.0104 | -35.44916 | 2025-01-20 03:42:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d2aae5c1-efc8-3cce-8de1-98c007a9d656 | -8.06972 | -34.97655 | 2025-01-20 03:42:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| a790b526-edbd-3589-89eb-061a042a7e61 | -7.37649 | -34.88547 | 2025-01-20 03:42:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| dc1f2dee-bf1a-3826-886d-4130e258e705 | -7.93622 | -35.26496 | 2025-01-20 03:42:00 | NOAA-21 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d794ffce-80be-3b38-a323-024600045a46 | -5.9745 | -35.62598 | 2025-01-20 03:42:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5cebd90-87d7-354e-85a3-8537d9d2d39c | -7.93292 | -35.26444 | 2025-01-20 03:42:00 | NOAA-21 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2aa61974-d3bc-35a5-b527-ea2b3ae60447 | -11.05161 | -45.37758 | 2025-01-20 03:44:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ced7382-be54-3762-8cca-4af5647eadd2 | -11.05098 | -45.38092 | 2025-01-20 03:44:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e44c9865-ff49-380e-b187-4588373ca7aa | -11.03171 | -45.04783 | 2025-01-20 03:44:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 610f33f0-1999-3fa8-8309-396282311f77 | -11.74965 | -37.99152 | 2025-01-20 03:44:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bddc2e7b-32d4-3558-b341-d2b7c1a57e6d | -16.03996 | -38.99941 | 2025-01-20 03:44:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 38560647-21d1-3a1b-82b0-19700d99d990 | -11.75024 | -37.98785 | 2025-01-20 03:44:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |


[Clique aqui para ver as próximas entradas](README2.md)
