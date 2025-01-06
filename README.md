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
| 05440674-2fef-3ad3-a01a-31dde2ec700a | -9.3986 | -35.9196 | 2025-01-06 00:10:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 104.2 |
| ef1ad02c-d48f-3066-88ff-fb1f38dd3fb8 | -9.3982 | -35.9468 | 2025-01-06 00:10:00 | GOES-16 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| 7f9be4bb-eef2-3220-bf84-b1bec58846f5 | -9.4179 | -35.9163 | 2025-01-06 00:10:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| 90dc533d-e341-3b40-81de-dc151c7f253b | -10.2381 | -36.3127 | 2025-01-06 00:20:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 131.2 |
| d495c196-4072-3ed3-81e5-9015320e3820 | -10.0255 | -36.351 | 2025-01-06 01:10:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 81.9 |
| 31e9185b-37c6-3eb5-934b-84f4dd9fd368 | -10.0062 | -36.3544 | 2025-01-06 01:10:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 219.6 |
| 9c3e91b6-5f7a-331f-b7ca-b6749bf1df4f | -10.026 | -36.324 | 2025-01-06 01:10:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 94.3 |
| af05bfa1-3033-38ea-8221-ed9d0a322ec4 | -10.0067 | -36.3274 | 2025-01-06 01:10:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 257.2 |
| b18e916c-6427-319c-a9a3-c3b528d60d9e | -10.0067 | -36.3274 | 2025-01-06 01:20:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 117.1 |
| df77550e-3792-3dc9-8398-2ea04bb2fb19 | -10.0062 | -36.3544 | 2025-01-06 01:20:00 | GOES-16 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 20d2eea5-c55c-3fec-965f-ca6dcccdcd6f | -30.32607 | -53.41975 | 2025-01-06 01:24:00 | TERRA_M-M | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 8.8 |
| 79cfa006-5481-3a4b-936b-b75faf97026f | -29.85268 | -54.92746 | 2025-01-06 01:24:00 | TERRA_M-M | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| d294fb86-7efc-3d17-8109-356979dd4d38 | -30.32466 | -53.40944 | 2025-01-06 01:24:00 | TERRA_M-M | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 5.1 |
| 092360b7-4145-3d85-961e-73b812989823 | -21.56312 | -54.20778 | 2025-01-06 01:26:00 | TERRA_M-M | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 0b1e7fbd-190d-3514-81d2-c2afab931005 | -18.5946 | -53.16496 | 2025-01-06 01:26:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6719293a-2d78-3619-a8c5-c80929a6cab6 | -18.51027 | -53.40664 | 2025-01-06 01:26:00 | TERRA_M-M | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5ad7dd45-e3ba-35f1-98ce-240315707a9a | 1.349 | -60.04198 | 2025-01-06 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 485c36a8-3bde-352d-a6f6-84e420dca88c | 3.50256 | -60.80276 | 2025-01-06 01:34:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 819ae397-e87e-3905-90c3-9ca07332189b | 3.66179 | -60.32057 | 2025-01-06 01:34:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 298eb61c-1c5d-3a26-a706-b5c7a4a9d800 | 3.66301 | -60.31177 | 2025-01-06 01:34:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 33c74c39-f51d-38d7-a6cc-b05e08b3955a | 2.02519 | -60.88365 | 2025-01-06 01:34:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4c1b89f5-69bf-3c10-85e9-2e4a13140007 | 1.35022 | -60.03321 | 2025-01-06 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.0 |
| eccd1424-d02a-338d-add0-a620889a8b29 | -10.6288 | -37.0442 | 2025-01-06 02:00:00 | GOES-16 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 567d6843-d6de-3ac5-ab8a-59c6264c6e96 | -5.16371 | -35.54029 | 2025-01-06 03:04:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 08920d90-3d90-3a5d-9124-c07c76981705 | -10.59855 | -37.02321 | 2025-01-06 03:06:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6b266bc-25b7-3fce-b5ff-0d5c475beb52 | -7.80583 | -35.1683 | 2025-01-06 03:06:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c782f32e-1ac6-36ee-9a76-bb1f428a42a5 | -10.6011 | -37.02288 | 2025-01-06 03:06:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9fb0b57f-649e-3d2e-92d3-8c0077c5c57b | -7.07822 | -35.27904 | 2025-01-06 03:06:00 | NOAA-21 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1bb4a268-b8a1-35ca-9289-54e950a85efe | -7.80639 | -35.16793 | 2025-01-06 03:06:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 41f92d22-350a-3505-b5fe-dd6a25d710f1 | -10.59927 | -37.01936 | 2025-01-06 03:06:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 27604faf-c404-32ac-bc14-449396700125 | -10.60186 | -37.019 | 2025-01-06 03:06:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0218df2e-8144-3014-8e7b-62a94bfd96d3 | -22.67555 | -42.86113 | 2025-01-06 03:10:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 083ab450-9e22-3de6-833d-8a1b30391973 | -22.67693 | -42.85545 | 2025-01-06 03:10:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 46f7e901-e83d-380a-b4f0-e9033fc50ec5 | -2.91628 | -40.44937 | 2025-01-06 03:27:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 836cb0b0-8301-3a63-b117-b8756873897c | -2.91833 | -40.45096 | 2025-01-06 03:27:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d6167d64-0fc3-36c0-bd22-63e007961e5a | -5.16092 | -35.53767 | 2025-01-06 03:29:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3688303a-700e-3d9c-9856-f93a95437a35 | -5.85479 | -35.47395 | 2025-01-06 03:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6a26fc75-6587-3475-97f4-9f5780fc597a | -7.99304 | -35.23324 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d260e79-89d0-36e2-9b01-5eb4ff00382a | -7.98934 | -35.24152 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| cd6246e1-2e7a-339c-9cfa-b810d45f1fb9 | -9.71041 | -36.69909 | 2025-01-06 03:29:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4ace5830-0254-35de-90eb-0a4c44380cc2 | -8.97443 | -35.77105 | 2025-01-06 03:29:00 | NPP-375D | COLÔNIA LEOPOLDINA | ALAGOAS | Brasil | 2702108 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9aa4f2a-9804-355a-a099-74395db65333 | -7.9917 | -35.24127 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| ebfdb6f9-c0db-38a7-b65c-3142d70d82bd | -5.18824 | -37.63667 | 2025-01-06 03:29:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 625d2582-e7b4-39c2-9ca8-fe4d60be757f | -5.16465 | -35.53827 | 2025-01-06 03:29:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1f73a1c0-8b15-3281-80e4-815a62878fc4 | -6.94138 | -35.78362 | 2025-01-06 03:29:00 | NPP-375D | AREIA | PARAÍBA | Brasil | 2501104 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 701d83ed-0148-317f-bb77-55d4c0130fca | -7.99419 | -35.23404 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0ae4aabc-a44e-3234-857f-985a12d44aa7 | -7.99289 | -35.24208 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 0f53faf9-3244-33f2-9596-059e1c0d278a | -7.99064 | -35.23346 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6c5a6d90-a288-320b-aed8-5cd1459e2d2e | -6.56229 | -35.27643 | 2025-01-06 03:29:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3b1e09ce-50f2-37ca-8529-84f43170d770 | -7.80849 | -35.17143 | 2025-01-06 03:29:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6a4fea1d-a928-3393-8ab7-6572ec5d942a | -8.50758 | -35.02661 | 2025-01-06 03:29:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8b67d800-68cb-3d15-9111-48fd46dad886 | -7.99237 | -35.23726 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| ac50a46b-2bc2-38fc-a119-fccfe589435d | -7.08075 | -35.27939 | 2025-01-06 03:29:00 | NPP-375D | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 016576d7-662f-36ae-8a10-48cbb5d97419 | -5.8511 | -35.47338 | 2025-01-06 03:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| d33c796f-7d49-3716-be70-dbae133e9f9e | -8.54217 | -37.72564 | 2025-01-06 03:29:00 | NPP-375D | IBIMIRIM | PERNAMBUCO | Brasil | 2606606 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 46d53c25-4a2a-3c1e-a52f-6d96b0bfacf6 | -7.99103 | -35.24529 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4827a4b6-a692-3f40-9eab-3afabf4208f3 | -5.84671 | -35.47716 | 2025-01-06 03:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 9028063f-c83a-3709-b227-b2b3caeafaff | -7.98579 | -35.24094 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9e18fce9-1a11-3cde-9003-ce8222542352 | -7.99354 | -35.23807 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| b60d9cb5-266a-39d1-92f4-6b3628693c51 | -7.98999 | -35.2375 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 5cf44a7a-7e9d-3898-a503-f467b6ecbca6 | -7.07716 | -35.27877 | 2025-01-06 03:29:00 | NPP-375D | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 52eb6e66-b896-3e8e-9604-ae22ab3ee447 | -9.70963 | -36.70364 | 2025-01-06 03:29:00 | NPP-375D | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 42fa121c-3deb-3903-a6b6-b61f2cdd7734 | -7.99458 | -35.24585 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a1e8015f-ea5a-3e55-8266-7b7307a0421d | -5.84742 | -35.47282 | 2025-01-06 03:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| f3292821-744c-3dcf-9a4a-f245988d471c | -8.48594 | -35.027 | 2025-01-06 03:29:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2a113004-fb0f-3529-ad41-8df4b7a19204 | -7.81275 | -35.23393 | 2025-01-06 03:29:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7ed00379-d806-3766-b9d5-fe3fd86fb427 | -10.1933 | -36.30315 | 2025-01-06 03:29:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 135e89d1-86f5-3412-a166-dc5d4ce8717d | -5.8504 | -35.47771 | 2025-01-06 03:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 7.4 |
| b706b0bf-32e2-3277-bae7-f38ab1fd122e | -8.4888 | -35.03147 | 2025-01-06 03:29:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cc0885af-e36f-39f7-8d81-dc2b9fc4d758 | -5.85408 | -35.47828 | 2025-01-06 03:29:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bbee45b4-d98a-33ad-aaea-007bb20408ff | -7.99525 | -35.24184 | 2025-01-06 03:29:00 | NPP-375D | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| c91cf1ef-7633-3ac0-8572-7f7dfb137812 | -7.80915 | -35.16742 | 2025-01-06 03:29:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 0588f477-d3f7-30e8-b33d-530d927fae3e | -10.86531 | -40.42501 | 2025-01-06 03:32:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 419344c0-0193-3829-9552-8aa33de40440 | -10.73584 | -36.85539 | 2025-01-06 03:32:00 | NPP-375D | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b5138746-d267-3f43-a0c4-3033d5ea51a4 | -10.86993 | -40.42606 | 2025-01-06 03:32:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 218207cd-92e6-3f32-b4e0-8eb3b6d606f1 | -10.86905 | -40.43099 | 2025-01-06 03:32:00 | NPP-375D | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ab91f0f5-9012-31a6-8a43-b35cc0e8a74c | -12.76982 | -38.46107 | 2025-01-06 03:32:00 | NPP-375D | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9b58d085-1f28-3a1b-9e51-e6d829b8e0b9 | -22.67419 | -42.85765 | 2025-01-06 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e802c3df-d698-3f1c-96c8-14f19da15c40 | -22.67603 | -42.85611 | 2025-01-06 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 523860ac-82ac-35cc-af05-cf359e39162a | -22.54052 | -48.8119 | 2025-01-06 03:34:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 652ba55c-b3c6-36f4-9b48-94a9c10f60a3 | -22.67513 | -42.85307 | 2025-01-06 03:34:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f89aa260-9d1e-38c8-ae3c-c1c2e7b91aa6 | -25.57359 | -49.36135 | 2025-01-06 03:36:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 694ccef2-3975-3e6a-bd4a-4a44d43dbeac | -25.57361 | -49.3564 | 2025-01-06 03:36:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fc952c08-aea0-3cb1-b15b-4ffc7a376cf9 | -25.56881 | -49.35449 | 2025-01-06 03:36:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3891565c-f426-377c-9a9e-607dd834c85f | -25.56758 | -49.35947 | 2025-01-06 03:36:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3738a5f4-69c8-3f53-9908-ad74db34b76e | -25.57234 | -49.3614 | 2025-01-06 03:36:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 49636cb5-931b-335d-ba3f-97384acfbf95 | -25.57482 | -49.35632 | 2025-01-06 03:36:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 08b9b3cf-d09e-367d-8b15-673400e35fb7 | -30.32471 | -53.41854 | 2025-01-06 03:38:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| a39387a9-d476-3c49-bc24-9c4f01ee8f17 | -30.31822 | -53.41563 | 2025-01-06 03:38:00 | NPP-375D | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| b1573139-b689-3f64-bc25-db81f6afe5ee | -6.04591 | -39.44351 | 2025-01-06 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 238318b9-ae47-3004-9bb0-6ade15ec0caf | -7.56806 | -39.01001 | 2025-01-06 03:53:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18b0e4a7-b12f-3ec5-9515-0001e63d6868 | -10.49446 | -40.1325 | 2025-01-06 03:53:00 | NOAA-20 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1412f8d0-0a32-35bb-9bf7-2c237722acfc | -2.91764 | -40.45124 | 2025-01-06 03:53:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 138334ce-f926-39ac-b5f1-1c6aa845331b | -6.55951 | -35.27718 | 2025-01-06 03:53:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 20d5f04f-7166-33f6-afb0-92bca7f8cafa | -5.95119 | -39.67048 | 2025-01-06 03:53:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 86e7225d-e30c-3f78-8298-9b99cceaa599 | -12.35253 | -40.27981 | 2025-01-06 03:53:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6f7688ce-661a-3929-8437-636f09ad93a8 | -5.74398 | -39.34873 | 2025-01-06 03:53:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| afb5ec96-f299-3812-b4a2-aed7d2baed3c | -7.81569 | -35.22314 | 2025-01-06 03:53:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 333c1b4c-1964-382a-a323-6e8a1bd183a9 | -10.8691 | -40.42338 | 2025-01-06 03:53:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 437864ed-f63c-3fa3-b181-ebb1294b5870 | -6.04256 | -39.44298 | 2025-01-06 03:53:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README2.md)
