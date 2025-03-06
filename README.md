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
| 6c88df3b-f084-3e9c-a382-2dd8581f5e1a | 2.9461 | -60.2931 | 2025-03-06 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 376cb0ce-4b8b-3df3-ac32-95f7e9c453d5 | 2.946 | -60.3122 | 2025-03-06 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7e407c8f-dc0f-3735-9db0-5893b677e0f9 | 2.3801 | -60.2255 | 2025-03-06 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| a82c558e-ddf6-3a21-940b-d31bf6a000a4 | 3.3274 | -61.2344 | 2025-03-06 00:00:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 72ded57d-4882-3189-955f-08d5bd1ebf60 | 2.6354 | -60.4119 | 2025-03-06 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a73bc7d9-4b48-38d9-9605-930081307ac1 | 2.7816 | -60.3338 | 2025-03-06 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 569c77e9-b25b-308f-b597-717e7b618c49 | 2.6171 | -60.4122 | 2025-03-06 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.6 |
| d1133fcc-4773-393f-a1ce-9e32cb65911b | 2.7816 | -60.3338 | 2025-03-06 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a9e226f3-a66b-305a-afed-1c726a8bee15 | 3.3274 | -61.2344 | 2025-03-06 00:20:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3de07805-ddc1-3721-b5dd-7035424ab782 | -6.8865 | -34.984 | 2025-03-06 00:30:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 79.5 |
| 524afafe-09cd-3d02-8edd-78228a0c6011 | 2.7816 | -60.3338 | 2025-03-06 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b4fc5600-45f4-3e8e-bc92-67a85749f771 | -6.8671 | -35.014 | 2025-03-06 00:30:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 66.4 |
| 39169559-0970-361a-b811-cdc0f8238ccc | 2.7817 | -60.3148 | 2025-03-06 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8248be25-a03b-3dfb-966a-5fa28da454f2 | -6.8674 | -34.9865 | 2025-03-06 00:30:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 119.7 |
| 3dea493a-ffb2-30f2-be8b-773b2d58c5e9 | 2.3801 | -60.2445 | 2025-03-06 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 026c8828-5692-3bd7-a5f2-870aa528ccc9 | 3.3274 | -61.2344 | 2025-03-06 00:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 74.8 |
| e6d5cddf-29cf-30b2-b801-8d8797c5b70b | 2.7816 | -60.3338 | 2025-03-06 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9acf20e5-eff0-358b-981b-b1f072958f95 | 2.7633 | -60.334 | 2025-03-06 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 46250de0-cb1e-3b4f-97a1-f9d59156a519 | 3.3274 | -61.2344 | 2025-03-06 00:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 3248ea63-a180-3c41-9a3f-8136a3c9fe6e | 2.6354 | -60.4119 | 2025-03-06 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 46.0 |
| bb90e6a2-f380-3e6a-b053-7f1164e88892 | 2.7816 | -60.3338 | 2025-03-06 00:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 83.8 |
| ce2d0661-8869-3fc8-8022-9bf0ab288ad0 | 2.7816 | -60.3338 | 2025-03-06 01:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| deda56e5-b0c0-3304-9cb7-f76b77ffe648 | 1.8504 | -60.5733 | 2025-03-06 01:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 71.3 |
| bf9e7286-9dde-3a0a-bbeb-fb8e9f97ca29 | -29.58664 | -51.9836 | 2025-03-06 01:09:00 | TERRA_M-M | ESTRELA | RIO GRANDE DO SUL | Brasil | 4307807 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 18e3dc32-619d-33bb-b3b7-931578b649f1 | -27.54806 | -51.11155 | 2025-03-06 01:09:00 | TERRA_M-M | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| e4d8bccd-10cd-3021-8364-a2197e867c14 | 1.8504 | -60.5733 | 2025-03-06 01:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 32ef09c9-ca08-3739-840f-cff05e077906 | -21.19555 | -48.63058 | 2025-03-06 01:11:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 578e3e0c-a606-3925-9554-d53677202b2c | -22.87248 | -42.71957 | 2025-03-06 01:11:00 | TERRA_M-M | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 2920e7b8-ed4e-3836-a086-4ca073566c24 | -18.69455 | -48.02014 | 2025-03-06 01:11:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ea5071ee-9fba-3cc3-8c7b-f040dae23186 | -20.72914 | -49.43807 | 2025-03-06 01:11:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 28.0 |
| a3ce15d8-63e1-32ae-8aca-3d59b4b958d2 | -20.71925 | -49.43982 | 2025-03-06 01:11:00 | TERRA_M-M | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7d9decc5-5f26-372b-ac29-7d98fe556bae | -20.72724 | -49.42616 | 2025-03-06 01:11:00 | TERRA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 261db891-0d9f-3beb-87ad-9ed43dc06550 | 3.93013 | -60.59566 | 2025-03-06 01:19:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ae5400eb-a76d-343f-95e2-7b07f5e10be3 | 1.31888 | -60.67613 | 2025-03-06 01:19:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cf0a2f00-3b18-314f-a1f6-295a70877ddc | 1.12624 | -60.51538 | 2025-03-06 01:19:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 8870b24b-0006-3009-ab35-76850150433a | 3.3263 | -61.23838 | 2025-03-06 01:19:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f90dde10-09b3-3852-859b-9adf0c5db964 | 2.72321 | -60.14681 | 2025-03-06 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d6080129-dda2-3fa2-8e1c-a33676b6e780 | 2.7798 | -60.33025 | 2025-03-06 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 8607b0cc-cc8e-39fe-a5c9-1e3086431f8e | 2.15489 | -61.82848 | 2025-03-06 01:19:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 10.0 |
| f93031e6-5e41-3564-9617-12204908a617 | 1.13551 | -60.44836 | 2025-03-06 01:19:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 485e3562-ef4e-358c-9747-081d8d08872c | 2.72176 | -60.15707 | 2025-03-06 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4c425fd6-b715-3156-befd-12b03b9b0d35 | 2.36943 | -60.69748 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 6e468d74-de92-3a1b-8040-7daa4b9f03de | 2.77023 | -60.32888 | 2025-03-06 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c385307d-2a29-33a5-bfc2-22db54b6c499 | 1.85408 | -60.57629 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 70bb82e7-71dc-3003-bc0c-2c22e28614c3 | 2.3757 | -60.23671 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 27aaed18-fe2c-3846-8d6b-89052367b86a | 2.30683 | -60.21005 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 63cfad6b-b53c-3827-91c6-ef5228f6a3ec | 3.73179 | -59.72684 | 2025-03-06 01:19:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1a51e238-f410-32e7-8b7a-72bfd37a7433 | 1.32887 | -60.67753 | 2025-03-06 01:19:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b157148e-ae47-333d-a2c2-ecc9c3a4e06e | 2.36786 | -60.70862 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a115c178-e3d4-3bea-8333-13706baff2ba | 2.37088 | -60.24033 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| e9c85a0e-82d9-3628-a244-d082afb86d78 | 2.77171 | -60.31842 | 2025-03-06 01:19:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9282d8e7-3f81-3421-a608-1f4edcff0216 | 2.37231 | -60.23007 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2218f73d-71bc-344e-8e35-7f424a9a8322 | 2.62573 | -60.41998 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b94bdbff-e198-35e0-b755-07799f358ca0 | 0.95427 | -60.00243 | 2025-03-06 01:19:00 | TERRA_M-M | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c4db133e-6693-3868-ab0d-d16debf02a95 | 1.79424 | -60.27296 | 2025-03-06 01:19:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1b625073-7fd0-3267-b387-09b9916e753a | 3.31623 | -61.23687 | 2025-03-06 01:19:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 55cd004c-0c31-3d9d-aa93-156be4d03829 | 2.11918 | -61.8171 | 2025-03-06 01:19:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4d4068d1-50ed-37ab-afb4-952cfbe73e24 | 1.08619 | -60.44138 | 2025-03-06 01:19:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a8078943-5544-366d-ac29-fc5de0431eef | 1.85254 | -60.58738 | 2025-03-06 01:19:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 10c455ca-7119-30fb-a871-b0fbe1550463 | 2.14949 | -61.83509 | 2025-03-06 01:19:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 615262c8-2634-3b3b-93ea-e461562d5ad0 | 2.84863 | -60.85969 | 2025-03-06 01:19:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d9a19f75-c395-33ab-bab0-3835a63e83c5 | 1.8504 | -60.5733 | 2025-03-06 01:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f135d8d1-4864-3fb0-8049-b3f329f1b675 | 1.8504 | -60.5923 | 2025-03-06 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2020e071-b5d7-32f5-9d98-609ff5592077 | 1.8504 | -60.5733 | 2025-03-06 01:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 458d6989-b367-3da5-95c8-1fea09808cbb | 2.7816 | -60.3338 | 2025-03-06 01:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 8cb7c614-49e5-3a52-9419-7fb96e9bb577 | 1.8504 | -60.5733 | 2025-03-06 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 150.0 |
| c4b7e61f-2bca-35cb-99df-e62baed8006f | 1.8322 | -60.5735 | 2025-03-06 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| bdba6290-99bd-3035-afc4-5256d11fb9f7 | 1.8504 | -60.5923 | 2025-03-06 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 246eb7b7-8866-3a8b-a7eb-2265e228f23a | 1.8686 | -60.5732 | 2025-03-06 01:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 3185dd96-2a73-32bb-8cc4-55006e103e97 | 1.8686 | -60.5732 | 2025-03-06 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 6626cdcb-2510-34ee-b410-123ae419665c | 1.8504 | -60.5733 | 2025-03-06 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 174.1 |
| 264bf3e4-4229-382e-a119-48ae779235f6 | 1.8686 | -60.5921 | 2025-03-06 01:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e4a9c7ac-cf22-3936-bdb5-f57dc5879886 | 1.8504 | -60.5923 | 2025-03-06 01:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 58c97c7a-5160-351a-8b46-ee4046d8c757 | 1.8504 | -60.5923 | 2025-03-06 02:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 163.1 |
| d6fefffe-d04a-3684-9119-6d5443cc5c28 | 1.8686 | -60.5921 | 2025-03-06 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c1eed727-3efa-3bd4-8557-058f230bd01c | 2.8535 | -60.8638 | 2025-03-06 02:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 9c7463fd-782e-3534-845e-20c797ba3242 | 1.8504 | -60.5733 | 2025-03-06 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 185.2 |
| 28602a98-1da3-330f-b7aa-2f9b6448bddf | 1.8686 | -60.5732 | 2025-03-06 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 81.0 |
| e9fee4b0-1b17-3e7b-b8bf-0f270073e5ed | 1.8504 | -60.5733 | 2025-03-06 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 2f759873-1a83-376f-94e1-460de47c5a0e | 1.8504 | -60.5923 | 2025-03-06 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 671edcd7-3240-39b1-85d4-675514dd060c | -21.7013 | -50.3492 | 2025-03-06 02:10:00 | GOES-16 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| c2119c4d-7e06-3635-a057-fe0ad853a066 | 1.8686 | -60.5732 | 2025-03-06 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 87ab8120-abd8-34ce-890e-8d6946d36802 | 1.8686 | -60.5921 | 2025-03-06 02:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 68.2 |
| cc4d5ce1-3d13-3545-950f-54b7b4f847aa | -21.7013 | -50.3492 | 2025-03-06 02:20:00 | GOES-16 | LUIZIÂNIA | SÃO PAULO | Brasil | 3527702 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.0 |
| 9ad0e5c6-1d76-30a3-b7c1-c9901fe2d829 | 1.8686 | -60.5732 | 2025-03-06 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e90a5c0f-3b2a-3040-8c45-bd1adb05f20a | 1.8504 | -60.5923 | 2025-03-06 02:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 20ad5fc2-0439-3372-8b5c-a4f821ca8a64 | 1.8504 | -60.5733 | 2025-03-06 02:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 129.2 |
| c81bb600-59fc-303d-96cc-11e98348e51f | 1.8504 | -60.5923 | 2025-03-06 02:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 77.5 |
| df755697-4ace-3081-879e-f9f7367e799e | 1.8686 | -60.5732 | 2025-03-06 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 878de9c3-cc48-3c2b-89a1-10194dfd4223 | 1.8504 | -60.5733 | 2025-03-06 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 100.4 |
| aa067eb5-4e33-3441-8ab4-0d26eae91490 | 1.8504 | -60.5923 | 2025-03-06 02:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 9675027a-7d6e-38de-8dcc-36786369b576 | 1.8504 | -60.5733 | 2025-03-06 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 02e4209e-f1f9-3d1f-9e4a-33867664ab24 | 2.8535 | -60.8638 | 2025-03-06 03:00:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 9fa3542f-71f1-3946-b449-fa470b2b361c | -22.91052 | -42.61071 | 2025-03-06 03:04:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c4869681-0486-3b15-83b1-a07b2caa60b5 | 1.8504 | -60.5733 | 2025-03-06 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 61ccb80f-5e92-3915-a523-0b88695526f6 | 1.8504 | -60.5923 | 2025-03-06 03:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 81.1 |
| edd2ea98-875f-389c-b782-ad75b57a38c6 | 1.8504 | -60.5733 | 2025-03-06 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 5f6df472-727b-38ce-9c03-d55a7f070185 | 2.8535 | -60.8638 | 2025-03-06 03:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 3403b6d9-90f2-3ee6-9711-4a6c23589906 | 1.8504 | -60.5923 | 2025-03-06 03:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 35cd8196-8093-352b-88ac-795e236cb845 | -5.18679 | -35.83294 | 2025-03-06 03:21:00 | NPP-375D | PEDRA GRANDE | RIO GRANDE DO NORTE | Brasil | 2409506 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |


[Clique aqui para ver as próximas entradas](README2.md)
