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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98b3a677-735c-35e1-ae41-d796aa4e828a | -7.0435 | -45.5439 | 2026-07-23 00:42:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f3e217a9-0b07-3d54-a22e-a4d47f56640f | -11.9075 | -50.374699 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ada9b39-7096-3297-b9f3-2abc953f0787 | -11.6981 | -50.3564 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b05bdfe-3559-3b18-8ac6-364cba0fd09d | -11.585 | -48.404999 | 2026-07-23 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9409f284-bd8d-33f8-be64-8f8937060d09 | -11.6883 | -50.358601 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37bfbff1-4c39-3b10-aee4-5d914fe8d18c | -6.0574 | -43.870602 | 2026-07-23 00:42:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4e3fe0ef-0bcd-32a7-828a-5b16e0158292 | -9.1051 | -49.6535 | 2026-07-23 00:42:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aadd8ac0-32f6-36f1-92a4-c6f2c3d8aa94 | -11.8159 | -47.3316 | 2026-07-23 00:42:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cba11a9f-403e-3ad7-b664-6ea27cc5f8e1 | -11.9134 | -43.835701 | 2026-07-23 00:42:00 | METOP-C | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 675f9ec6-74b5-3d71-a4e7-f14cb8b1acd4 | -11.9663 | -50.361801 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 820e0af8-96ca-3332-b3a0-e5e80f3d6284 | -12.8489 | -44.371601 | 2026-07-23 00:42:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44f2d6fa-afce-306e-bb97-0f83dc006974 | -18.798401 | -51.2519 | 2026-07-23 00:42:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bab5aa92-0411-3f43-8401-1d30a41db103 | -7.8343 | -47.113201 | 2026-07-23 00:42:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7dcd89c2-a731-3482-a08b-8c6ca26192f1 | -12.0203 | -50.374199 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cdb9b55d-9b9b-30df-90b2-2b5658f3d949 | -11.3962 | -47.480701 | 2026-07-23 00:42:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 31299a6b-3eb4-3c1f-9894-97086dbb2dba | -12.4458 | -49.592999 | 2026-07-23 00:42:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5314723b-e6ab-397c-b682-9195409283ec | -12.4442 | -49.585602 | 2026-07-23 00:42:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a39956af-2448-3b57-b6b1-7f22413e9e5b | -5.3853 | -49.291199 | 2026-07-23 00:42:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ed04ea3-4bba-3823-8735-9a20fcadf310 | -7.7373 | -44.554298 | 2026-07-23 00:42:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ab30ee26-e1f8-3d96-9cfc-d2aa910cfdc0 | -11.6866 | -50.350899 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8f22c9f-3fbe-3306-84da-8fc6568d8a28 | -11.896 | -50.369202 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| de88bfcd-1b1e-3c54-8b55-9bf456c7683b | -5.7624 | -49.0914 | 2026-07-23 00:42:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d723ab0-a5f4-3c2b-93e8-f2914be8be8c | -7.8326 | -47.1059 | 2026-07-23 00:42:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 787c8e83-8611-3ef7-8308-acc30c873319 | -11.7751 | -50.3797 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06ee3079-6c10-3e00-a3c6-22a81bf6ef98 | -11.9352 | -50.3605 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30dbd3b4-e9a2-3c89-892a-75d390af86be | -11.7919 | -47.091599 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f222e85-293c-3a39-81f1-89f684996c86 | -11.919 | -50.380299 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02d624ca-e34b-3e33-9f88-f7e97625bc3a | -11.7325 | -50.372898 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66147462-27f5-3992-ab8e-03bab86a7453 | -11.8862 | -50.371399 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c60e83f-b6c3-3c14-98b2-5957492651ea | -10.8025 | -50.441898 | 2026-07-23 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0358ef30-a1f8-39fb-8f11-e492285016f8 | -6.4128 | -51.235901 | 2026-07-23 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4bb31b3-afe3-30d5-b1c3-e50c18d6b4d5 | -20.712601 | -42.849602 | 2026-07-23 00:42:00 | METOP-C | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c268a19b-4b3e-3ed0-acdb-5ab9157bc307 | -21.0504 | -47.775501 | 2026-07-23 00:42:00 | METOP-C | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4a341f9c-f9f2-3d19-a8c9-f0d1c01f13dc | -6.0477 | -43.872898 | 2026-07-23 00:42:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0b2975bb-5149-34e6-9d30-42fbf03eb689 | -11.7342 | -50.3806 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b77809f6-1234-37bc-82c0-b1deba79bea5 | -12.0251 | -50.348801 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 999d32f9-acc4-3f43-a538-2555c763850e | -11.7079 | -50.354301 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d351b73-3584-391b-b469-a79f97b32e01 | -11.9335 | -50.352798 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6339c50-2702-3eaf-b5d4-d03800d0b4ca | -11.7837 | -47.101002 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5fecd4d-e326-347e-9286-732470577297 | -11.945 | -50.358398 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f63c9b9-f0b7-3524-a92d-dba60f5ff030 | -5.7609 | -49.084499 | 2026-07-23 00:42:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 013485dc-139a-398c-be89-3c45baeb109a | -6.2347 | -48.992401 | 2026-07-23 00:42:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0e40562-e9be-395c-891b-293ba01e731b | -11.8175 | -47.3386 | 2026-07-23 00:42:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5643a94b-d42b-3007-9708-1cc8d03522cd | -12.6657 | -48.2169 | 2026-07-23 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5a575557-9bc3-39c0-8ca9-e27e1e3c3c9f | -11.9859 | -50.357498 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dfcf0930-83c5-3133-bd28-a1cee5ce62db | -11.7129 | -50.3773 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 368d9a4c-3f0b-3833-96f6-ccfa4165fdc6 | -11.7947 | -50.375401 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 150f861c-4976-3d48-8b48-075911b31009 | -10.6327 | -47.479698 | 2026-07-23 00:42:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c703372-6dbe-3c2a-8fe4-ca9096ff5c26 | -11.8896 | -50.386799 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f023de6-5e88-3a92-a2c0-c7e894e2e7e4 | -11.9761 | -50.3596 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63596270-d47f-3830-83be-15df853d600c | -11.7717 | -50.3643 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d59ce884-0cac-37cf-a69c-3d5062bab7a4 | -11.6539 | -50.341999 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89c94645-22b7-37ac-8c64-376c83bd4883 | -11.6097 | -50.327702 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68617b4a-8582-3642-ae25-2e18dfaf7b56 | -11.7653 | -50.381802 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b459504-e130-3dea-92a5-be67c1e9b19d | -11.7014 | -50.3717 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c55569be-2f96-3786-beee-9518ff4d41a7 | -11.6654 | -50.3475 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c378525-cd4b-37b2-aad2-d0a783d6f4a5 | -7.0144 | -45.420601 | 2026-07-23 00:42:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c4cd9f7-82d8-37a4-a8c8-cc74ee8937c6 | -12.6641 | -48.2099 | 2026-07-23 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22dad3ab-392c-3abd-8ade-ff709ec5f231 | -6.0449 | -43.861599 | 2026-07-23 00:42:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eba484f8-a232-3011-a64e-0982bd77bf30 | -11.7739 | -47.103298 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a778918c-79a1-303e-9623-09236ca04e34 | -11.6752 | -50.345402 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c9e4c35-0c7f-3148-8a11-bab3342576c8 | -11.7504 | -50.360901 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f22782f0-6cda-3156-bb7f-6047a0e9f7b7 | -11.9744 | -50.351898 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3909619-8d8f-377d-9d0e-4996812362fa | -11.7849 | -50.377499 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 99cee859-cb6e-31ce-a30b-1380a8a083dd | -18.7866 | -51.243401 | 2026-07-23 00:42:00 | METOP-C | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c2db98e3-1383-3471-a4f8-33a249460494 | -11.9058 | -50.367001 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a6caedae-a119-352d-b5ce-439d2eec2cde | -11.626 | -50.308201 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aedb9a9a-3f13-3829-9ff7-9f57025e1cc7 | -22.287701 | -47.266102 | 2026-07-23 00:42:00 | METOP-C | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c8ef54f7-7d2b-3bd2-ab83-f84d2a430aab | -6.0546 | -43.859299 | 2026-07-23 00:42:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 649a6d75-c65e-3e4b-a644-9a21f113bdcd | -11.8403 | -50.349201 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c0170dbd-b038-3e2d-b815-85703cd7c52a | -11.9842 | -50.3498 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ba6fecb-06f8-3603-b1de-d36a9ec2613a | -11.9957 | -50.355301 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fcd13a68-f61c-3aa0-84a4-f093fd58bcba | -6.2331 | -48.9855 | 2026-07-23 00:42:00 | METOP-C | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e9a6ef0-700e-3bcb-899e-394b737e21f9 | -11.662 | -50.332199 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cff98134-8805-3aca-af6c-d11022579ea9 | -11.8066 | -47.1106 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 411731fd-91f3-367e-b460-771b04867d92 | -11.9646 | -50.354099 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a41b762b-4075-3a94-8bb1-8565500ba773 | -11.9369 | -50.368198 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 22ac50d9-5786-3bc8-ba90-f8251ea808dd | -11.5835 | -48.398102 | 2026-07-23 00:42:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26e8348b-56ff-35d7-88b0-85d10e4ff305 | -11.7952 | -47.105801 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 983ab7d1-8951-3945-96ca-0ef99fed3834 | -11.842 | -50.356899 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46003188-b115-3691-a8a5-a1f968766ad8 | -11.805 | -47.1035 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8d3a82f-4340-3dd8-8a3b-ec978c181a56 | -11.7521 | -50.368599 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| addbac97-96e5-3da5-ba8b-4bd25a10d12a | -5.3673 | -43.141899 | 2026-07-23 00:42:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d4617922-9d6d-395e-9436-059873118654 | -11.7935 | -47.098701 | 2026-07-23 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1f743a3-2ac5-35b3-ab94-0364ce758b3f | -10.6343 | -47.486801 | 2026-07-23 00:42:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 45a237c3-e728-34cc-ae09-0e2553410db0 | -11.7734 | -50.372002 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb86516a-5d41-3ccf-b1d1-18f0ed170c63 | -12.0105 | -50.376301 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47934047-cff5-3f6a-bf02-177ca20b1fcb | -11.999 | -50.370701 | 2026-07-23 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd9527a9-727e-3497-acf8-5a6672c73011 | -11.698 | -50.3629 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| f6384e4d-9165-3812-8a75-dc8690e3dfdc | -11.6983 | -50.3415 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| b9ef9de3-5bd0-3823-a7b9-81d6c1cc196e | -11.6792 | -50.3437 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 85b7ebf6-3c78-3cb5-ab8e-d9808b392ef6 | -11.7738 | -50.3756 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 8bb0f949-8edc-37b8-a8fa-a9a86f9d2112 | -11.7875 | -47.1108 | 2026-07-23 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 215.6 |
| 8994ebc0-105c-32fe-bb19-ed5928f4f9ba | -18.7804 | -51.2453 | 2026-07-23 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 2b4abea7-e588-3395-807a-23aa5f290eb3 | -11.8066 | -47.1082 | 2026-07-23 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ad0362f5-7d3c-3020-98a8-329568c378c0 | -11.807 | -47.0858 | 2026-07-23 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 9d1953f8-8a2a-39c7-aa3f-73777b19f6ef | -11.6602 | -50.3459 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bc782f09-ecfd-3b79-9c39-60246d11c5ff | -11.7879 | -47.0884 | 2026-07-23 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 8a56ca90-fa04-347e-a140-baeb36c6026c | -18.8004 | -51.2417 | 2026-07-23 00:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 0930ae01-8548-3110-95da-821433bd5be6 | -11.8879 | -50.3837 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |


[Clique aqui para ver as próximas entradas](README6.md)
