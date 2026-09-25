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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dbf768ca-a304-335e-b55d-f05e1601f545 | -10.4422 | -64.498497 | 2026-09-25 01:57:00 | METOP-C | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| aef51b8a-856d-33b5-8b5d-9f182b87b7fd | -7.3827 | -64.361298 | 2026-09-25 01:57:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4112e8be-fccb-3b91-81a6-3942d56394c6 | -8.6606 | -66.586098 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5901afb5-5e38-3710-8967-a15cfcd45080 | -9.1529 | -59.480301 | 2026-09-25 01:57:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 96e226bb-cfc7-3623-aad7-e9a4a0fe36b4 | -7.5164 | -70.387001 | 2026-09-25 01:57:00 | METOP-C | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ea8cc93-afbd-3e73-9320-26d5b20df33a | -9.1625 | -59.477798 | 2026-09-25 01:57:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f0f0c04-8cb3-3626-8c75-3dfc3d6aa5ff | -7.3925 | -64.359001 | 2026-09-25 01:57:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f39c592b-14f0-37c7-a3ad-74d343814396 | -9.0229 | -60.5154 | 2026-09-25 01:57:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dff7e702-4d91-3eb7-8d10-dbf07c7447b6 | -7.3968 | -64.377098 | 2026-09-25 01:57:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74283d3e-3805-31da-a19d-e74b0aa762ed | -7.3849 | -64.370399 | 2026-09-25 01:57:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f091317f-8a53-32c2-a177-e8515dcb4098 | -9.4737 | -67.067497 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20ae79b5-d44e-307b-8be5-a8d75d69725b | -7.5181 | -70.394501 | 2026-09-25 01:57:00 | METOP-C | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6058a4bf-4f9a-3ff3-abeb-d4c0861d4be8 | -6.9838 | -63.001598 | 2026-09-25 01:57:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43b32fc2-26b2-3e8a-aad8-5bd8a1ee8134 | -9.073 | -65.699203 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6417eba4-40ac-3f8a-b74c-1e6ac32c8f1c | -8.9613 | -72.8526 | 2026-09-25 01:57:00 | METOP-C | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| daa200bb-15a7-35ec-9d2b-3dd58ab1871c | -9.0267 | -60.530399 | 2026-09-25 01:57:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66d212d0-9698-37c5-909b-e359464c4ed6 | -12.7065 | -63.077999 | 2026-09-25 01:57:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dff84fbc-5e93-39e4-862c-2391e1d29986 | -9.5519 | -65.980598 | 2026-09-25 01:57:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 141b3bf5-a6dc-3ca8-bdd6-0bf58f527918 | -9.3841 | -66.501297 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6576ade5-44c0-3df3-b80b-762168ac67e2 | -8.7864 | -66.594704 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b6aec18-f10e-3e46-aa9e-190e6fa29f22 | -9.1484 | -59.4627 | 2026-09-25 01:57:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5ae9b85a-512a-3b96-b568-2997a00d951a | -9.158 | -59.460201 | 2026-09-25 01:57:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0e181c8-e642-3e99-a09e-9e9f74015f86 | -9.3857 | -66.5084 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fb0aaf3d-7c79-3af3-9609-2c674d12ac02 | -9.0712 | -65.691597 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 037a5f96-2704-3508-94ec-99ca267b3260 | -8.959 | -72.842201 | 2026-09-25 01:57:00 | METOP-C | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 74d3602e-366b-361c-bdb2-d265db917e07 | -10.4217 | -67.740097 | 2026-09-25 01:57:00 | METOP-C | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 65dda410-9c5a-3df0-806d-374c73f3d273 | -8.6415 | -66.860199 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e940701-4914-3ec0-9b96-ef6b4232129f | -7.6747 | -67.141998 | 2026-09-25 01:57:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ed524a5-9e5f-3ad1-a071-006fe04c7db3 | -7.3946 | -64.368103 | 2026-09-25 01:57:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fc52b2b2-2878-3df9-819e-c5a83b24b51b | -8.6399 | -66.853104 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7ce1fdf-07f2-3057-8d84-849f29e92b35 | -7.673 | -67.135002 | 2026-09-25 01:57:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dffece40-1679-3263-b7de-51ba2c44d279 | -9.5536 | -65.9879 | 2026-09-25 01:57:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5fef3e53-63ad-312f-8c76-ff9f895eb58b | -9.0632 | -65.7015 | 2026-09-25 01:57:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6da4ecc-d563-3121-83e6-f2362b505e35 | -8.0396 | -71.259804 | 2026-09-25 01:57:00 | METOP-C | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 367001e5-0f89-3703-8872-81f20abda72f | -1.1461 | -54.0996 | 2026-09-25 02:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| b0bdb2dc-76c7-36a8-ad87-bb0364f4b660 | -8.5889 | -48.3781 | 2026-09-25 02:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9dbd6a32-f451-3ff5-9633-df7a9553833a | -11.9402 | -50.6987 | 2026-09-25 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| d155c20b-3004-39f4-bfea-22e109f70c1a | -11.9593 | -50.6965 | 2026-09-25 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 7bc9eb61-41ce-3390-b0ad-1b82c1d0dc17 | -7.4037 | -64.3843 | 2026-09-25 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d891ee20-18c8-3e62-a98d-fefe337f95b4 | -4.4099 | -55.5247 | 2026-09-25 02:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 1c4f8ed1-8e93-3b40-8663-1730e72aab79 | -12.0609 | -50.2773 | 2026-09-25 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| f95a800d-d41f-33d0-b296-fc786e2cb8f2 | -8.6077 | -48.3764 | 2026-09-25 02:00:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 111dfd54-e75b-38ed-be85-481bf8f16a04 | -11.9399 | -50.7201 | 2026-09-25 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 174.4 |
| 87966747-5a89-3d20-8b61-fc3c148b47c2 | -3.25 | -46.9369 | 2026-09-25 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| cf46b42d-b9df-3e05-89e3-23cfde1f31c2 | -3.2314 | -46.9376 | 2026-09-25 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| fd003ddb-7785-30db-90a9-09c2d5a0e677 | -11.8227 | -50.9256 | 2026-09-25 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 68d20a32-adec-378e-8fea-854fb1d52770 | -11.3048 | -51.3011 | 2026-09-25 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 2148572b-0de2-3163-acf4-98414e3e12b6 | -7.3853 | -64.3849 | 2026-09-25 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 10c7e986-3c6d-3c7f-aa1f-86078b94942c | -12.0799 | -50.275 | 2026-09-25 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 536f2d8e-b444-314e-a5d1-a3693feeee54 | -4.4098 | -55.5446 | 2026-09-25 02:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 881afb15-bf44-3bdd-ac5a-84c0d9fea18f | -7.4038 | -64.3656 | 2026-09-25 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| af765f98-f43a-3f53-9c6c-028ef106110b | -11.8037 | -50.9277 | 2026-09-25 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.9 |
| f8d8e9ca-9c9b-32d1-978f-5b51fb7601da | -9.1535 | -59.4834 | 2026-09-25 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| e344b262-2682-376c-bec7-90546a4e0e34 | -9.1536 | -59.464 | 2026-09-25 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| c6ce0eca-8271-3ce9-bbf9-297e2d4bea8f | -7.3854 | -64.3662 | 2026-09-25 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 76870c30-911e-397b-ab89-fcb58cbe6ca5 | -11.959 | -50.7179 | 2026-09-25 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 214.6 |
| 998b4bb2-4177-3237-bca2-11b4e1164e73 | -11.2859 | -51.3031 | 2026-09-25 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c94d0839-55d8-38ad-a3f1-a0d0fc4da407 | -11.804 | -50.9064 | 2026-09-25 02:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 8d60f7ff-a296-36be-ba74-50163eab7bfb | -11.9399 | -50.7201 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 221.7 |
| 3b765347-84e2-3ef1-a30b-4ab8cec54277 | -11.9593 | -50.6965 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 48c60912-3d29-3695-9127-dda9dc0f0f27 | -8.34 | -44.1427 | 2026-09-25 02:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 6aeab551-a2ab-3ad0-b61e-56cbb1b057f2 | -9.1535 | -59.4834 | 2026-09-25 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| d2c9f26f-7431-3879-bf9d-461ac08ab868 | -12.1678 | -50.7576 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| d295e980-2bea-3c62-b082-54ac925176c9 | -11.978 | -50.7157 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 9e4f07f6-e80b-3014-ba3c-52c8ccc3f2e2 | -1.1461 | -54.0996 | 2026-09-25 02:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| aa796652-9aa3-39ad-a368-2e936e43e164 | -9.1536 | -59.464 | 2026-09-25 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ffe414ff-caf1-3017-a9de-3940da8e1a0d | -9.4769 | -40.3365 | 2026-09-25 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 75.0 |
| a7b15aaf-6e54-352b-8f78-3935768e5c6f | -11.3048 | -51.3011 | 2026-09-25 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 8641346d-811c-32aa-a592-15b2ebc1788c | -8.6077 | -48.3764 | 2026-09-25 02:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| c819233c-6b84-37a2-b210-86f63a2fee44 | -11.2859 | -51.3031 | 2026-09-25 02:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 1edc4f20-59b4-34a8-9824-e540855c149d | -12.1866 | -50.7767 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e1168d7e-bdc7-3c43-b9b1-c66b6a0e09ab | -3.2314 | -46.9376 | 2026-09-25 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 7c541a0f-9336-3e99-8789-0deca2411ad2 | -11.6754 | -50.601 | 2026-09-25 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| f52636ff-81fc-3c8d-b928-e69e6f097c3e | -11.9586 | -50.7393 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 9149a4bf-ab46-30e4-af4a-8b53c2305273 | -5.7754 | -45.1053 | 2026-09-25 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f93a4073-67a7-31a0-ac7e-9fb2b0c7f001 | -1.531 | -54.2959 | 2026-09-25 02:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| a3ce8058-ba0a-3060-8e96-c77115e436fe | -12.1675 | -50.779 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b4960a12-3b4e-3cf0-b8ee-4ceaec0edee1 | -11.4743 | -44.2053 | 2026-09-25 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| c634fa2d-e897-390b-b365-ebdb468ffb3f | -11.959 | -50.7179 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 349.3 |
| e51c1580-b3e6-3465-a7d1-860b9931d1d9 | -11.9402 | -50.6987 | 2026-09-25 02:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| ce3e9f33-a481-3be0-9881-e9a55af065fb | -3.25 | -46.9369 | 2026-09-25 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| a1c74bcc-ba9b-38ea-8bd3-76101622fd2a | -11.3048 | -51.3011 | 2026-09-25 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 41a86e8b-9f3b-3143-9e43-7a8c96cf473d | -3.25 | -46.9369 | 2026-09-25 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| ccc48c88-a03a-3c25-b126-85e6ef2389d9 | -11.7849 | -50.9086 | 2026-09-25 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 5791624f-e659-3d0d-9972-d26f9174fb75 | -9.4769 | -40.3365 | 2026-09-25 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| 2f162d72-94d9-3bc4-9d01-377c42cc8ad7 | -1.1461 | -54.0996 | 2026-09-25 02:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 51c9b91a-d2a8-3e80-b68d-d3a883fed937 | -3.2047 | -53.4179 | 2026-09-25 02:20:00 | GOES-19 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f80bde62-d2a4-30d1-8e95-edbd05bef018 | -8.7741 | -45.5849 | 2026-09-25 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 2bc4593b-1631-3b86-8eda-c5f73240e7be | -3.2315 | -46.9156 | 2026-09-25 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 0ae83473-7486-3b76-94bd-a9b9e3f57bd3 | -3.2314 | -46.9376 | 2026-09-25 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |
| dfa39612-db73-3fef-8911-e48ff72b86d0 | -8.7738 | -45.6076 | 2026-09-25 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| d1951d37-7f8c-35a0-acaf-bea2105b4fd4 | -1.2189 | -54.5592 | 2026-09-25 02:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.2 |
| a956e29a-a221-3712-978e-c5c839b6214a | -12.1872 | -50.7339 | 2026-09-25 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 23911e5e-1818-3665-97c5-7af3a2438076 | -11.2859 | -51.3031 | 2026-09-25 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 978336d5-b48b-39b1-a052-a8b7be162752 | -11.804 | -50.9064 | 2026-09-25 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| e085de17-e93d-3f11-8307-a919454c43f7 | -9.1535 | -59.4834 | 2026-09-25 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| f7c2c835-f166-3c8d-bb74-a385104f93d2 | -12.1869 | -50.7553 | 2026-09-25 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 0861f22f-4f37-36f7-99c3-68aafdc66141 | -9.1536 | -59.464 | 2026-09-25 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| dfab30cc-98b9-30f1-b22f-bf80c5083b12 | -12.1115 | -50.7001 | 2026-09-25 02:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 75f9e677-ab40-35e3-9350-2fdb210ede43 | -9.4769 | -40.3365 | 2026-09-25 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 159.1 |


[Clique aqui para ver as próximas entradas](README9.md)
