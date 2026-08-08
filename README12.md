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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6247ba3e-a8ce-3b0b-94dd-43559f940dc1 | -12.542 | -46.91656 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71f48f97-62f3-3508-be9d-75a7ff348eeb | -11.03781 | -44.28012 | 2026-08-08 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5138a95a-f406-3ed4-8f00-07d85b394f49 | -12.55025 | -46.97389 | 2026-08-08 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4daa7ff3-cd83-3426-a094-b54ec7ec34c0 | -11.19756 | -54.84372 | 2026-08-08 04:25:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4f34350-2296-3dce-a30d-29052bc4072a | -6.90605 | -41.96358 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d2fb1139-2938-3a55-ad2b-e7798da60b96 | -6.72352 | -48.11647 | 2026-08-08 04:25:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16dc76ed-65da-3624-aba6-cc368a06339d | -6.91336 | -41.96108 | 2026-08-08 04:25:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e3183147-cdcf-3c33-86c1-68c6044ad077 | -11.271 | -55.86791 | 2026-08-08 04:25:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cfd241c8-6f0a-3482-bdff-254ab2505340 | -12.82059 | -41.95842 | 2026-08-08 04:25:00 | NPP-375D | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dca2aa06-fa6e-326e-a34d-c50609039f4a | -6.89085 | -42.44263 | 2026-08-08 04:25:00 | NPP-375D | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b0fe2a2b-cfb7-3260-ad8f-1de397f2621b | -15.16308 | -52.73804 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fa7a732-003c-34df-b5a9-5255cc863209 | -14.41906 | -45.66026 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a3e33d6-5967-32f1-8668-7065684b9728 | -14.35697 | -54.89054 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9fb22d6-1046-3118-b0e0-d8f1a0d7042c | -19.89512 | -40.66238 | 2026-08-08 04:27:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2f8ecb14-3384-3032-b33a-804783295827 | -14.41516 | -45.66327 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83aece7e-6b73-361d-9a9a-3b3f302d74cf | -15.10144 | -52.73109 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f7d8aea-8a02-3b83-af2e-6fdc7b22137e | -14.32976 | -54.94087 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 748f5700-1abf-3873-95c7-d11fd4fc40ba | -18.33171 | -43.91562 | 2026-08-08 04:27:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fea5e0a2-b904-3b44-8e21-4aafc577ac02 | -17.30918 | -47.48783 | 2026-08-08 04:27:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8c96723-ccb8-3d92-8302-1beac5b01cfa | -15.1667 | -52.74458 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4ea04847-0ecd-36da-9b9d-e079789d1f1e | -18.36571 | -50.69986 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e97f1808-f216-3cb7-8a70-e408997e55df | -20.36662 | -41.16401 | 2026-08-08 04:27:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 309651c0-3905-3886-a14a-eae19d2693fe | -14.16553 | -54.00578 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 193bba80-56f7-3bbd-b0e5-232666bd2b0d | -15.3969 | -53.80858 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5e8e204a-b285-378d-af65-821bc11f5d65 | -14.93381 | -48.24607 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b794337b-78cb-3cc0-8734-f5e80291ad52 | -14.37437 | -54.97392 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5ba0fa2-a075-305a-ac0c-21fdc64e5425 | -14.27669 | -45.28174 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12671595-b1cc-3915-8f1c-a94155f6b1cf | -19.85643 | -43.46748 | 2026-08-08 04:27:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e457c383-f33c-33d4-b071-f89d587dd90e | -15.1537 | -52.73646 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe882258-5503-372f-bbdf-bb08f33e5d7c | -17.30971 | -42.67761 | 2026-08-08 04:27:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 5d2fffac-32a4-3406-a537-4ba03cb5205c | -17.89215 | -44.43795 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 520ed018-7048-3b15-8b77-c8293bf7a304 | -17.83829 | -44.49117 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2ce0dd41-eeb6-3be3-8609-defee72781dd | -14.92526 | -48.25289 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2e92383-e10c-37b0-944e-a86bf5c84508 | -14.27944 | -45.28585 | 2026-08-08 04:27:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acbb4f4a-c80f-3d52-94a1-793604e6fd9a | -16.9107 | -48.99292 | 2026-08-08 04:27:00 | NPP-375D | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a531086-8549-32af-8857-477a15fa8758 | -17.30492 | -42.65937 | 2026-08-08 04:27:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 18.2 |
| e35f8b71-da8c-332c-938f-916a87cb1e33 | -15.38434 | -53.79368 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c2328ea-eae7-30af-8e26-584863cc2066 | -16.4517 | -43.14427 | 2026-08-08 04:27:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1bb9f36-6abf-3c34-a3ff-06b396548ade | -16.68398 | -51.36193 | 2026-08-08 04:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27fddc6f-c217-389f-b115-5098cd824b58 | -14.41631 | -45.65612 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 623da890-3f8c-3520-a52e-f8c279e4a979 | -17.98229 | -44.25399 | 2026-08-08 04:27:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f109750-f874-3e19-9556-16bd6a77ad9f | -15.83761 | -48.22927 | 2026-08-08 04:27:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef0036d2-db9b-3460-b7b5-7e54a718954e | -15.14592 | -52.73735 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d57367c-f999-3e8e-92c6-24312cccb0b7 | -14.9388 | -48.25995 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3be2b283-49fd-31c8-9e3e-bc8e997c830a | -15.15745 | -52.74224 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26b917f3-7ee7-3741-922d-6df7fabd7c44 | -16.18388 | -46.22497 | 2026-08-08 04:27:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c27c272-bdca-3093-9482-74c0e62e2ac3 | -20.61793 | -48.95481 | 2026-08-08 04:27:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cc87dd38-06a7-3226-82ad-7a47c99a8921 | -17.84167 | -44.49178 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05a005cf-dc89-3bb0-ae5b-64416a14d316 | -18.35027 | -50.71972 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7781eb03-aca6-36fb-8f72-d7aba7005b4c | -14.15999 | -54.00439 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 61fd9ff6-36b1-3da0-8550-a865c71956cc | -20.24161 | -46.90218 | 2026-08-08 04:27:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cebc002d-4e4e-3168-a8d9-f3cd720589e3 | -19.96251 | -40.60769 | 2026-08-08 04:27:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b33b4c8-1662-3b84-bbe7-b2e263b4f54d | -16.6798 | -51.36129 | 2026-08-08 04:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccf0a4e3-11e0-383b-9605-bf880029193b | -18.34466 | -50.72739 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 53.4 |
| ef99cca0-f80e-3659-bfe1-2cf38227f7d1 | -14.92599 | -48.24871 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aba3738e-96ae-3718-84de-7ddb02f8603d | -14.32634 | -54.98589 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c8a50d69-7a08-3cc1-82b0-852d3f99ca2c | -14.15979 | -54.00765 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51f991bd-4387-381d-8edb-b10cf870cca0 | -20.20955 | -42.14658 | 2026-08-08 04:27:00 | NPP-375D | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7b53babd-23b1-3c12-97b3-a4803f98d6ce | -18.50925 | -48.34053 | 2026-08-08 04:27:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adca1925-956b-3d67-b2c3-ea92b77c9a0b | -18.35338 | -50.7237 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 3e0d9176-7116-3762-87f0-c0c21390d503 | -19.85287 | -43.46689 | 2026-08-08 04:27:00 | NPP-375D | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5cae6b3f-7e24-3c97-9955-48ad1a42d17b | -17.89159 | -44.44173 | 2026-08-08 04:27:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f9c2d977-427a-35fd-ac3d-0cb1224bf749 | -14.31314 | -54.99462 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f91b660-1918-3a03-a88a-269093195a6e | -15.37936 | -53.79269 | 2026-08-08 04:27:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84048a3c-a599-351c-ae13-466ad6d6b231 | -20.04746 | -44.05936 | 2026-08-08 04:27:00 | NPP-375D | IBIRITÉ | MINAS GERAIS | Brasil | 3129806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bee0c7ed-9da5-3aaf-81c9-48abaf49574b | -17.88111 | -43.77866 | 2026-08-08 04:27:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9801d8bf-b82e-3c22-ba3e-c56c50342805 | -20.05941 | -40.8883 | 2026-08-08 04:27:00 | NPP-375D | SANTA MARIA DE JETIBÁ | ESPÍRITO SANTO | Brasil | 3204559 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 234f7e9f-f26b-34f6-8572-2be9d7008c39 | -13.83401 | -53.68279 | 2026-08-08 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6b0215d-4509-3e32-98f0-f66e8837e16f | -20.32373 | -43.66082 | 2026-08-08 04:27:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4f980ac8-065e-3a36-8a27-1a79a321f062 | -14.3186 | -54.99589 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 299f1f08-2355-3fbd-b207-4019048a74a1 | -18.21444 | -44.35635 | 2026-08-08 04:27:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0e10d80c-525e-3b2c-b7bb-58f2a0a04557 | -15.15536 | -52.73866 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 54efdc78-15a0-3d00-a926-354f011654ac | -14.32428 | -54.93984 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0430229f-da8a-3e3e-9641-be947d33fdbd | -15.52413 | -47.34716 | 2026-08-08 04:27:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05ca38da-54ca-3737-955c-09bcaadf97c2 | -16.68325 | -51.36588 | 2026-08-08 04:27:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 825e1888-b500-3d3b-a5fb-c11928fff5fc | -14.93095 | -48.2627 | 2026-08-08 04:27:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3c96049e-98b0-3691-9524-5e168ee169e3 | -18.21785 | -44.35691 | 2026-08-08 04:27:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 762b4e91-70c0-392b-a40c-f091583d13e6 | -15.70213 | -54.85956 | 2026-08-08 04:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f903247e-fd6a-36ac-8b0d-f46ad41ce4a3 | -15.70283 | -54.85617 | 2026-08-08 04:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 038cdac4-ae69-3062-b068-0d3ec6d1d344 | -20.39082 | -49.30745 | 2026-08-08 04:27:00 | NPP-375D | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a4c04baa-77fc-31d0-a6f7-4e67eedc9784 | -18.36481 | -50.70487 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27e10bc6-5a98-3547-a431-8b20bec7c911 | -14.32558 | -54.98964 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa3c29a8-3ce2-3432-b17a-976e65b3c00c | -19.95709 | -44.13678 | 2026-08-08 04:27:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ea0cdaad-6999-38c5-bd67-b249ac3abf2c | -16.40498 | -49.9347 | 2026-08-08 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a735c01-5711-3d75-bcea-8d20e1795e54 | -17.59837 | -46.68888 | 2026-08-08 04:27:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f94a0863-3577-305e-b5ac-c4b05e718772 | -18.95456 | -50.62803 | 2026-08-08 04:27:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 382c42d9-81fe-3f4f-8252-1228e5386331 | -20.17223 | -43.69004 | 2026-08-08 04:27:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f431cbf5-b570-3764-8463-862a8f6cad51 | -14.41964 | -45.65668 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cecceaf-edbd-3997-a7a8-385a130a0b4c | -18.36093 | -50.70409 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1ffe9e21-86c5-3dea-96f6-a7e34c7ef665 | -15.16212 | -52.74319 | 2026-08-08 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7045c3da-d297-336f-ab50-e514d895d2e9 | -15.70523 | -54.85711 | 2026-08-08 04:27:00 | NPP-375D | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f057057f-dcf8-3007-8064-7da74f458b4f | -17.57685 | -49.66912 | 2026-08-08 04:27:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efc6189d-182c-3fc5-adaf-de2fca7fad5c | -18.35993 | -50.71107 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 11c8fb06-1637-3ea7-9f8e-0bd18f6b9661 | -14.42239 | -45.66082 | 2026-08-08 04:27:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec9f850d-5b02-38e0-b3dd-232e2eb8a674 | -18.34173 | -50.72134 | 2026-08-08 04:27:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c64408c3-8111-3424-b7b6-ec5b60031679 | -20.17934 | -43.69102 | 2026-08-08 04:27:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b431437-e08b-3431-9e4f-a85c40c26630 | -14.22652 | -48.50721 | 2026-08-08 04:27:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f4b7810-8f20-3838-bf36-59a2a7b6f776 | -14.33102 | -54.99094 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 530883e0-8e5f-347f-a04f-400d065a100c | -19.36103 | -40.68638 | 2026-08-08 04:27:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6404a59e-03cf-3c83-befc-354440b797b4 | -14.36893 | -54.91573 | 2026-08-08 04:27:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README13.md)
