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
| d86705ca-bed7-3cdc-a3c1-871fe0972cf8 | -6.5849 | -44.6327 | 2025-10-07 00:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 17391dd8-bf91-3c11-a6e9-fd53f788ba90 | -18.1176 | -53.3548 | 2025-10-07 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 635613fa-5f92-3240-b570-7f9d7c6dfecb | -16.6373 | -40.93224 | 2025-10-07 00:11:00 | TERRA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 877f087e-99ee-3207-ba4a-c34f24e5ad28 | -13.36192 | -43.67092 | 2025-10-07 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f52dc640-0c48-3ee4-808f-2ae137df8cab | -10.39812 | -45.38015 | 2025-10-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df7d20ea-b114-39f1-bf90-5f0eae096d4b | -11.72134 | -45.44843 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 61f91fec-4587-3729-8f7b-11e10a2e2d70 | -13.77628 | -43.94334 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a57cb29a-654e-3bdd-9a5b-a3f86a7daac4 | -17.08771 | -43.38066 | 2025-10-07 00:11:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 12d3653f-e6e4-374d-96f6-5ecc67f3ac5c | -14.9126 | -46.83759 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8d59fd23-f858-3660-8885-28b3a589bfb8 | -17.24239 | -46.92163 | 2025-10-07 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e5a5f637-5d14-375a-acfb-5923d2a71f21 | -16.63594 | -40.92291 | 2025-10-07 00:11:00 | TERRA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9b1909a8-bcbe-3f87-a28d-65d6aaef1274 | -15.58966 | -44.50516 | 2025-10-07 00:11:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 28a0bc99-d294-3cb7-add7-0fab6de3a27b | -13.35305 | -43.67221 | 2025-10-07 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cf92fcac-0610-32ad-a205-fa3e390d1997 | -10.26976 | -44.35893 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c628b908-6c92-3037-ba22-d14ec11bbc13 | -14.89748 | -51.42498 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f10c3e0a-b75e-3cac-8bbe-8ab50ac7c2d0 | -14.49893 | -46.93677 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 2819c0af-5e35-3832-9e3a-8b88ba6d1089 | -11.57215 | -44.66599 | 2025-10-07 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| faf9825c-b731-3b51-83bb-f6f30aed972c | -11.7171 | -44.44363 | 2025-10-07 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a1b325a4-bbe2-3571-bd82-51a7b17d6e15 | -14.92901 | -46.79412 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 94cdc979-b4f8-3e03-a9e4-a5914033baf6 | -17.97914 | -45.00515 | 2025-10-07 00:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3a5aac09-a774-3f37-846d-c6589828d438 | -11.71068 | -45.43939 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 50956336-aa01-397e-b5c5-24b629a5bd0a | -17.02386 | -43.45475 | 2025-10-07 00:11:00 | TERRA_M-M | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 26adb896-6ef0-3b1a-bb39-21eb62e16d06 | -13.39504 | -42.7043 | 2025-10-07 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 13a2feb2-1a71-3144-a97c-bde0afcf7f31 | -14.54412 | -46.64203 | 2025-10-07 00:11:00 | TERRA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d554501c-5a0f-35a9-a1df-a253099e36f7 | -13.85912 | -44.42278 | 2025-10-07 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4e891d40-2e7b-3273-b0a5-dfb24bd4d486 | -13.24075 | -48.45611 | 2025-10-07 00:11:00 | TERRA_M-M | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 2feb2168-aedf-3b28-861e-a746fed7cfd1 | -12.0164 | -47.79403 | 2025-10-07 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 7a9fffcf-7a13-3f4d-a352-3a99b5495bce | -13.08773 | -47.85662 | 2025-10-07 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| be60e359-f0fc-340a-affa-1e946db9859a | -17.34535 | -46.82742 | 2025-10-07 00:11:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5fd2e36e-b8a3-3868-92df-6302547ecdb8 | -14.7624 | -46.01368 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 0ad417b4-dce6-3b03-b219-60a291b1a549 | -15.11962 | -43.86952 | 2025-10-07 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9cd1019a-4f94-3e7b-868a-144eaf555531 | -15.08287 | -46.63876 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 94e41bdf-8c06-369a-a802-33ad965619fc | -15.27196 | -46.33968 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2ecfd653-1a1b-3f4a-93de-735906f34162 | -15.50021 | -47.93842 | 2025-10-07 00:11:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 89157b27-d695-3bbb-a03d-94ed825384e8 | -11.79032 | -45.12941 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 283a6c14-f258-301b-b3ff-d40de8aa640c | -15.12088 | -43.87901 | 2025-10-07 00:11:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a7ff80ce-930a-3644-b2c9-3a203d101f66 | -11.56314 | -44.66726 | 2025-10-07 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2e264460-f2a6-31fa-9a0a-30b26d84d06b | -12.4354 | -45.62093 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 216c28f6-23da-3401-8072-fd5d4fc14ccf | -15.31817 | -43.09197 | 2025-10-07 00:11:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a95548e4-4163-355a-b54c-add14ecfa088 | -13.6971 | -44.3831 | 2025-10-07 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 57e1974e-57ea-361b-9430-93a65c4bfc25 | -14.89779 | -46.84685 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 81f787b4-d7cd-3b41-aca0-a72973f00276 | -11.8245 | -45.10497 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e18800ae-7a4f-32de-9208-c993c3178fb7 | -11.15305 | -47.95213 | 2025-10-07 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 403b730b-1cb0-3fc1-ab82-af8f81f433fa | -13.51535 | -42.24816 | 2025-10-07 00:11:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3e9019fa-7649-30c3-9f68-7dfed98e6ac4 | -14.75389 | -46.02709 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 182eaa59-ce7a-300e-8799-a3ed32caa113 | -13.5359 | -42.98972 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 19be2e16-bac1-384c-ab6d-1b6c70ef258f | -14.93047 | -46.80631 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 39.2 |
| c9d4a28f-4561-3612-ab83-8fb3d064e1e8 | -13.30619 | -48.04964 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 889094b1-a78d-394a-a59c-8cffdc0cb69e | -10.26255 | -44.38412 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 20a88062-857e-3c88-80b0-9844098d6803 | -15.90539 | -47.61819 | 2025-10-07 00:11:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 21.3 |
| be443257-a3e0-3949-ba43-02ee0fa872ca | -14.93471 | -51.50716 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 95bc1e8f-2071-367d-b8e7-d735a4e14236 | -12.21614 | -44.25061 | 2025-10-07 00:11:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 004a7bd4-a916-3ed6-8403-d92ad03a07ce | -14.92003 | -46.80922 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| a20224c2-aab6-3ee4-917e-df681ef6747b | -14.70995 | -46.00239 | 2025-10-07 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| e4158044-ebb8-365f-9913-8c3a028215ef | -15.49817 | -47.92142 | 2025-10-07 00:11:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 84b625b3-bf56-34e3-902f-dd4c437a5743 | -13.85783 | -44.41318 | 2025-10-07 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1412c613-5a19-3186-89f3-af1121e10ccc | -11.9396 | -43.03582 | 2025-10-07 00:11:00 | TERRA_M-M | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| dc729fab-df34-3817-abf2-e64374ffa329 | -11.73079 | -45.37578 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| efe5d219-83e9-39cc-893d-cdabd5599e9c | -17.61438 | -46.68715 | 2025-10-07 00:11:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 060a041d-4de7-359d-92c3-799b20d6c13e | -13.38154 | -47.54065 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1cb4b6a5-a684-37f4-9de2-ec767015ce75 | -16.20471 | -43.65874 | 2025-10-07 00:11:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 89fc2b53-8228-3ecc-85b5-ec5760b4c23f | -15.96784 | -50.83584 | 2025-10-07 00:11:00 | TERRA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 867382fa-aee2-3ad3-a248-c5cde57ca02b | -14.2714 | -45.83789 | 2025-10-07 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6c137d42-bc8d-3845-8a8e-553355c68d1a | -10.36264 | -44.98233 | 2025-10-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| ce680233-cd8f-3952-bc11-9068eae8e502 | -13.68285 | -47.95519 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fe21f521-a8b8-3951-8318-1b6a6b819739 | -14.94349 | -51.47001 | 2025-10-07 00:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 4a4d2db2-d79f-3332-ade8-92072735bdb4 | -12.0147 | -47.78001 | 2025-10-07 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| bba5bb4a-3ce9-332e-aaea-b7dc6887d502 | -10.41685 | -45.39144 | 2025-10-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5af7c9d0-ecfa-3714-b92d-9f9c58d815d3 | -13.2853 | -48.06838 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 583cb3ed-e95a-3e7e-8d7f-0c1186556f64 | -13.3062 | -48.06011 | 2025-10-07 00:11:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9f19b2c7-5658-33a9-9811-985e87b7dc04 | -10.36139 | -44.97295 | 2025-10-07 00:11:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f5a0ec71-93b2-353c-90d0-5501cbe9dd5c | -14.70817 | -43.95935 | 2025-10-07 00:11:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f8975697-0b30-3fc6-b2c5-0a3796f1e777 | -17.97769 | -44.99366 | 2025-10-07 00:11:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f071cf28-2c27-3ad3-8da2-8dfe81ef040b | -15.20309 | -48.25361 | 2025-10-07 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| bc98ec04-9a2c-3095-8fd4-6ef94e6de160 | -14.90364 | -46.85344 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 238f917b-fe65-3739-8b8e-79147db21e17 | -14.51859 | -46.92049 | 2025-10-07 00:11:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a371aaba-6c2a-3ba5-93cb-ae0f7e88ef02 | -10.27221 | -44.377 | 2025-10-07 00:11:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| a6511876-38c5-3452-ae8e-6a2ccb266e47 | -15.49601 | -47.93298 | 2025-10-07 00:11:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 446022d0-15a3-367c-b578-b167c3ea77ca | -15.27287 | -48.06459 | 2025-10-07 00:11:00 | TERRA_M-M | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| a34adb90-ec46-35bd-ad7e-b293c0e43cf2 | -13.51664 | -42.25734 | 2025-10-07 00:11:00 | TERRA_M-M | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 18.4 |
| f10af7ef-21fc-34a8-b7f9-881c7e103bdb | -15.65528 | -43.67814 | 2025-10-07 00:11:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 8e9b3295-2cb2-3527-b58d-1314ae175f13 | -13.6724 | -44.05896 | 2025-10-07 00:11:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 091bf666-4b3b-374e-b8cd-c37cd3610795 | -15.63927 | -43.01057 | 2025-10-07 00:11:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d36d6068-902e-3e65-8b46-482076dd0939 | -14.7524 | -46.01514 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 025b2766-b68f-3276-958a-607d9e1af201 | -15.35771 | -46.05089 | 2025-10-07 00:11:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 939dd82e-03cd-34bd-adbd-922acca9aeed | -13.72411 | -48.20758 | 2025-10-07 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 998e3963-7936-39ac-a97a-062fe7a99efe | -16.19568 | -43.65998 | 2025-10-07 00:11:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 327245e1-d9c3-31cb-90e6-24d7f7255b5e | -14.99417 | -42.01872 | 2025-10-07 00:11:00 | TERRA_M-M | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 087c8d8a-5b12-3c2f-873b-261bc209e0ce | -13.02318 | -43.54349 | 2025-10-07 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 163f584b-0f32-30d7-852c-d44211a57e2d | -14.70669 | -48.38483 | 2025-10-07 00:11:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a5abf807-68ba-313c-81f4-6de26ebc72c8 | -15.60139 | -52.58134 | 2025-10-07 00:11:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 88.2 |
| f71998c4-261b-3460-b0a3-2b72ab5e4f86 | -17.52728 | -42.47683 | 2025-10-07 00:11:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df792dfd-cb66-36b3-b551-1b7df02c2138 | -16.68703 | -41.02169 | 2025-10-07 00:11:00 | TERRA_M-M | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| beed9b7b-7a6c-324d-8d11-e64ed8fa0913 | -13.72226 | -48.19179 | 2025-10-07 00:11:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| fcaadf3f-9f39-329c-b503-faaa9e184d4d | -12.16038 | -50.90268 | 2025-10-07 00:11:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 24ba97cc-215f-3aa1-a114-4a5e551427e5 | -11.84503 | -44.91817 | 2025-10-07 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 5da4588e-8463-3e50-ac2a-f22d1db2f513 | -13.85672 | -43.99226 | 2025-10-07 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 2945cb4c-045a-3c5d-8832-aaa973c710f7 | -10.81063 | -48.59905 | 2025-10-07 00:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8b7a267c-13f2-376e-9139-78cb4ba715ec | -12.34554 | -47.05647 | 2025-10-07 00:11:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 48236c64-ed08-30a0-86cf-7f6ad8d25b61 | -15.63802 | -43.0014 | 2025-10-07 00:11:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README4.md)
