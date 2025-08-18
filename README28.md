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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75ab1aff-a9f4-3740-bc20-077360c08c8e | -12.98434 | -56.84453 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2902229b-71cb-3ac6-8954-2d2cb2f3317c | -15.11565 | -48.73282 | 2025-08-18 05:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3428fa78-0359-369c-8d23-b5d5d9524d28 | -8.9739 | -60.49922 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e49c405-8e8c-33f8-8582-aedc5f760ef3 | -13.58869 | -47.75578 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1713793-39a5-3406-928d-0a0cf27d38e1 | -12.98663 | -56.85265 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12854273-9c51-3ab1-a237-06fe0cfc5db6 | -8.97407 | -60.49474 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 418b6cd2-51f8-3ddd-a2b3-c055cab5bacb | -13.86555 | -45.54297 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fddb459f-d00c-3193-92b9-9735d705f6cd | -13.14099 | -54.89477 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd2f9b6d-0766-3ad3-97b9-57429babb8fd | -13.1364 | -57.15159 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a75979e-3566-334d-ae5c-f7a8988cfa65 | -13.22511 | -50.75652 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b42a1988-9de5-36ec-8350-7b7eac43aab0 | -9.51535 | -60.51934 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18371146-4817-3ab7-9cc8-d53ec75c70b5 | -13.22451 | -50.77441 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 23307ace-130a-3823-a07a-759f000e704d | -9.51507 | -60.5239 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93be5c66-3857-30fa-b65b-5d8ac48f71ef | -16.16021 | -50.02904 | 2025-08-18 05:14:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26dfbdc7-19a4-3140-b6e3-ef7d1bdde6dd | -13.20886 | -50.76578 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 28b8edce-ad18-3c9f-9af4-ae97404d5dfb | -13.21945 | -50.76147 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee08f022-babf-3dc4-b20f-213a5412e3dc | -12.63363 | -46.90257 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de8ebaaa-e88c-3bc6-8b4e-1819a9aa5eba | -12.99522 | -56.84234 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9713479d-33b8-361a-8a7e-86893ab6f03b | -13.58817 | -47.76043 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d15f4c6f-52e4-3456-afd2-8afbedc9f50c | -13.21597 | -50.7496 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a4f4a82d-57f3-3521-abdb-052414c8f4ad | -10.99585 | -45.65385 | 2025-08-18 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8a5167e-7331-3d27-b2f6-7a97a3d9785c | -12.9872 | -56.84887 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e35d863b-e829-3e24-9c4c-56e2a8a24087 | -12.63705 | -46.90352 | 2025-08-18 05:14:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b413a033-6e95-386c-9426-56425550237a | -12.99923 | -56.83906 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20d472fe-6b03-3685-938f-3bcb0e117d93 | -12.12455 | -47.90112 | 2025-08-18 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 062a3ad4-a98c-3634-8091-ec6dcd7d9747 | -13.13751 | -57.12125 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5fafa18d-1bdd-3a78-b65e-43488a967dfa | -13.17591 | -54.91891 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d329894-7232-3ed5-bdfd-be70e0447aa2 | -16.79012 | -50.09449 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 18b79eb5-c269-3a26-924f-ef5902ef7459 | -13.22438 | -50.76213 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 5b20886f-7d1d-3838-8049-9213f0647187 | -14.99318 | -54.78165 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 325d9d0a-259d-317c-b72a-711044fb23c3 | -13.61123 | -47.77316 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3d3186a-63d8-32d9-a72b-0864d04b674c | -13.01749 | -56.85283 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dc5f1d7-80e2-3338-a160-1b46181f4874 | -14.58878 | -47.96476 | 2025-08-18 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a772b4-a39b-3fe4-9350-9ac0defd3708 | -13.21109 | -50.76118 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| fb000ea8-cdc9-3b1c-9c92-b27f9aac628d | -15.76687 | -56.2978 | 2025-08-18 05:14:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42260353-e07e-33d3-ba0a-078ad569ddde | -14.70105 | -59.65447 | 2025-08-18 05:14:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00444410-e53a-3149-bb83-f6fb84fc82f9 | -12.94209 | -46.11938 | 2025-08-18 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a974a8b8-7a3a-3362-829b-89319038d062 | -13.59344 | -46.98105 | 2025-08-18 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| afd5e44e-3487-3c9b-8496-d56c5e0d7e1b | -12.99293 | -56.85749 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04320ef2-d886-3af6-bde7-eaf09cfe24cb | -12.93613 | -46.11282 | 2025-08-18 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b44a8616-e79d-3ce0-9c59-25bb3fa0dacf | -9.51313 | -60.53582 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9076469d-7b17-332c-8c91-192be4ee4cc3 | -8.97761 | -60.49533 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 024ca59a-549d-3d5d-a136-f53244c41c17 | -13.22291 | -50.77333 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| f2c96de0-c742-35dc-9ad8-b4936ee05745 | -16.7951 | -50.09919 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 756a75af-d415-3be6-a7de-81bdd6bae352 | -13.13016 | -57.14681 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16b8b598-39eb-3c6c-98f2-bce44a29c1e5 | -9.51025 | -60.53125 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c97e5b2-6bbd-35d1-b4e1-5763145addf6 | -15.11518 | -48.73701 | 2025-08-18 05:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1cec2f94-3551-31c4-8eb2-f914767afb49 | -16.16208 | -50.02816 | 2025-08-18 05:14:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fc2af08-d677-3a9f-9712-bc8c71132077 | -13.22796 | -50.7463 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3bad438a-e72c-369a-9246-c48aee2310a3 | -14.18223 | -45.32373 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5321b966-d538-32ce-87ee-39dd27b71511 | -9.5105 | -60.52667 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afb6fe4c-e6a7-38ac-8c6f-7552deeaa67c | -13.21104 | -50.74895 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d2dc52cb-61e2-352e-9814-4717d1aa8096 | -13.13356 | -57.14734 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81c01aec-97a7-3202-a259-cab0f7c9d1b2 | -15.00731 | -54.79374 | 2025-08-18 05:14:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62f5bde2-9044-3a90-9185-06a15cd4bdad | -13.22313 | -50.78561 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3eca29c-9895-3c8e-9509-3b4ad36c1089 | -13.22365 | -50.76774 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.0 |
| c140d232-a1be-3ae4-8ded-1268500ae2de | -11.85071 | -51.5834 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d77b3011-24bd-3b96-bcc4-9a0ae70d7b16 | -14.28902 | -53.1963 | 2025-08-18 05:14:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35c4e40d-6f92-3f6d-8e1b-5214fcae1fa5 | -9.51469 | -60.5233 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7912488-d59a-303d-8580-089c8c8aeedf | -12.98606 | -56.85643 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ffc8b669-9c95-35cf-81ba-11b1dd321143 | -8.97694 | -60.49932 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9b80f98-057d-32e0-8828-5bc93263771c | -13.22658 | -50.7453 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 385ee535-5b13-31ad-9b16-5a70156d5929 | -12.9935 | -56.85371 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 984ca016-5734-3711-9ef3-7f437e2c8372 | -13.22731 | -50.73968 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a76a7e55-4861-33dd-af3f-bd412214b4dd | -16.16245 | -50.02473 | 2025-08-18 05:14:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 76851fe2-a271-358f-a750-2233c2252381 | -11.85528 | -51.58404 | 2025-08-18 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27c6e754-dba0-3269-bbcf-d297ca511215 | -9.51602 | -60.51537 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2090c5b9-78f1-3994-9832-f7e22e72a4dd | -13.01862 | -56.84523 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dee8a9a-4e83-3d83-8216-fb7813bc5512 | -13.2252 | -50.7688 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| bc8f9284-58b9-37d6-b9d8-e78bc9e01253 | -12.92295 | -46.11061 | 2025-08-18 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3b9cb550-687b-38f6-bef4-94dd5657aae2 | -9.51636 | -60.51595 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 599054d4-4564-369b-9418-b1a63ed67aa8 | -13.2182 | -50.78495 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e8390be-1742-3f32-8252-03c98f475909 | -13.58711 | -47.75394 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7a6ef8b-fac3-3cee-86af-bc9f50c6593d | -13.22164 | -50.74464 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 65f0689c-b105-39bb-8d64-411f8d52a76f | -13.21603 | -50.76184 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 57e3bae9-cce8-3534-b8cc-fec7f8314d72 | -16.79398 | -50.09655 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb90edfd-c2f3-3753-afe1-9e705b3890ec | -15.61617 | -54.30426 | 2025-08-18 05:14:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 745d6024-830c-3f49-8002-b3b879007283 | -11.31459 | -55.21901 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d4f5eeb-4ea0-362d-b084-fbc6a30d7fde | -15.01246 | -54.7851 | 2025-08-18 05:14:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8c8c3fa3-1973-3742-b088-3f97ae350642 | -13.13983 | -57.17494 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b04109-fe4e-3343-ad46-58f420e31b05 | -12.99865 | -56.84286 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a73acd1-5d21-34f8-b747-57332c107732 | -13.16774 | -54.92234 | 2025-08-18 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 74d110e7-58a2-3c84-ad27-17bcddb4a367 | -13.2329 | -50.74696 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87b2b489-dbea-34da-87cb-0df22cadd694 | -13.23854 | -50.74199 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43f95345-e3bf-3413-8102-3dbd33d4b464 | -13.00553 | -56.84391 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 63fff492-1bf8-3590-95a9-6eede931eff1 | -13.21958 | -50.77374 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| bb03581a-c5ea-3f34-960c-613f27c0a450 | -9.51688 | -60.53183 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ae179442-4851-3624-8115-c151e08c3e93 | -14.17738 | -45.30246 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 513de7dc-a631-360a-8008-8fbfffbe3eed | -8.97809 | -60.4958 | 2025-08-18 05:14:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e02a3716-a37b-3152-ab73-7f8ff273b168 | -13.21799 | -50.77268 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 80dfa7ec-5dfa-3fc1-a927-36f1ad9604fd | -13.20616 | -50.76052 | 2025-08-18 05:14:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| ec0a70ff-993c-3c31-be6c-b2f6df791c5f | -12.93553 | -46.11808 | 2025-08-18 05:14:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c37acfd-f6bb-3a6b-b3c0-eb268a5e8864 | -13.43595 | -56.94306 | 2025-08-18 05:14:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 875f0a89-f248-32cd-bbc8-c051f0339f4e | -13.59458 | -47.74251 | 2025-08-18 05:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b10b1157-abbb-33eb-bf75-4bd0c6476b66 | -9.51378 | -60.53186 | 2025-08-18 05:14:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61f564e5-1980-34df-b9b1-4f72756d6962 | -11.36388 | -55.43497 | 2025-08-18 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f89977ca-cf90-3de6-964e-48015a127fc3 | -16.79547 | -50.09569 | 2025-08-18 05:14:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59900bf9-200f-3ea6-9570-a01430358526 | -14.18022 | -45.31445 | 2025-08-18 05:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a67c108-e9ab-3ce4-a4dd-9cc0372f3b08 | -15.72909 | -48.42068 | 2025-08-18 05:14:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2681c35-1910-3573-9aad-d9128959985c | -12.99864 | -56.8661 | 2025-08-18 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README29.md)
