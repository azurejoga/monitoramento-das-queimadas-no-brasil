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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db248ea7-3a82-362c-b612-3141610c338e | -6.33395 | -55.85323 | 2026-09-12 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d8a3b63-f33d-3d6a-b201-3b69281ec424 | -6.40419 | -54.9779 | 2026-09-12 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5e7e231-6a7f-3479-8596-661f6ff81099 | -6.8377 | -55.28909 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85fe43f8-ed04-3d37-9684-1f9d96d1acb0 | -6.50913 | -58.28725 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dfc2b50-1d80-36b5-9c36-941bb0a64787 | -6.26543 | -50.83752 | 2026-09-12 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb024a9-572b-3262-ad50-03f10a6ea5fc | -5.71192 | -51.74832 | 2026-09-12 05:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2739152-a03c-322c-a4a0-11f8d0c54c07 | -3.89842 | -55.81848 | 2026-09-12 05:10:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fa261518-27df-3637-a672-9362cf0b1790 | -6.10631 | -57.63311 | 2026-09-12 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fdcdfe73-5b03-3fbc-b86f-c00eda7f2a9c | -6.3312 | -43.36377 | 2026-09-12 05:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a069ebe-e843-3f56-b32c-6103494440f5 | -6.87609 | -55.63466 | 2026-09-12 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a7caf032-17fe-3219-9357-1e2c50521ad8 | -9.70138 | -54.34267 | 2026-09-12 05:10:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96f7623f-de55-3ee9-ad73-90abf2d68851 | -15.0195 | -48.50251 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1dd3a53c-de44-3774-9f7f-a319e9032367 | -16.63514 | -52.82671 | 2026-09-12 05:12:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cd124b8-f758-355c-b5ab-989339751c65 | -12.46473 | -54.42585 | 2026-09-12 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fa4dc81-f776-380d-b711-2a10509a31f0 | -14.91453 | -44.6665 | 2026-09-12 05:12:00 | NPP-375D | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e893d28f-b780-3808-b288-7059d5b29adf | -13.37523 | -48.00785 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 316f3fc3-3d55-37f0-957f-6befdb49f1a4 | -13.37462 | -48.01274 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5cfdf594-d7e2-3f35-a183-a351eb036210 | -13.43892 | -43.81488 | 2026-09-12 05:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a78d1671-9132-3b88-a64d-c43785f21166 | -11.24416 | -54.13526 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f44c1add-7cff-3ddf-8273-f2248667a87b | -12.64192 | -47.08765 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 811d2914-79d6-318d-ad60-f508bc3eb59e | -11.24698 | -54.1394 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50668302-f059-3c6c-a69c-1b5101a9c4d1 | -9.50248 | -68.49448 | 2026-09-12 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69c9cebd-e05c-3e73-8a18-ef04918e91e0 | -16.04393 | -52.65799 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ca096c56-31f8-3292-bb16-a75821ca386c | -14.58733 | -52.66469 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e8a23eb-4840-3002-9069-2b0ff1a0fed3 | -12.12435 | -48.97333 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bc84c677-74a2-3857-9ead-cf4ed5272c48 | -15.55539 | -54.24313 | 2026-09-12 05:12:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22e169ff-6296-30f0-b446-b4dad3baa579 | -11.23739 | -54.11189 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ecc6dc9-ce9f-3e0c-bc3b-9e4c297a50ea | -11.24361 | -54.13888 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da7934d2-73c8-3c6c-916b-e498dcadfd49 | -16.03644 | -52.6569 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0b624e5f-7548-388a-bd30-bd279436ebad | -15.04695 | -48.51827 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9845c15-aae7-34a6-9a9c-23c1c303c946 | -9.73515 | -64.95934 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c78ed086-046f-35ce-845a-47e953310df1 | -12.64004 | -47.08915 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ff6f975-e975-3374-a090-74a6fe6406ea | -13.3734 | -48.02258 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ff41ac0-0b1e-3770-89e9-c4d6314c810b | -14.59101 | -52.66523 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8b25d2de-acbc-312a-a877-9f6a662a3f56 | -12.85169 | -44.39108 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 155b4d86-8369-397b-9ec1-0e705386a25b | -17.1081 | -51.25314 | 2026-09-12 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b0a0693-6795-3efd-baa9-56b6226e4d5b | -14.57629 | -52.66309 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f086bef-cae0-3122-a3c0-c39719e1da19 | -9.73658 | -64.95179 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd8cd491-6a46-3f06-b53a-749b753aa4d4 | -9.46523 | -67.09338 | 2026-09-12 05:12:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f504efd3-e3bc-3cf7-a45b-fec793cf87e8 | -15.0559 | -48.5251 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0d764fc3-399d-38b4-8f4c-13f956629c71 | -12.15438 | -64.13717 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 65c4befc-5fb2-3486-ba47-09ffa9e327d5 | -13.46422 | -48.50016 | 2026-09-12 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a3a49fa-1867-3d28-804c-6d7f391e3186 | -9.17981 | -68.22359 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| ab70973e-6060-3b0e-a80b-65bd3dca3863 | -16.63204 | -52.82156 | 2026-09-12 05:12:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1dfb38ae-0ccf-3bb5-b439-2c8d1cd06578 | -11.23798 | -54.13058 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14444e9d-d07a-397f-a4cd-5c2de778ca2c | -11.24528 | -54.12803 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2210bc8-3414-3d81-b904-4ff088953630 | -12.85782 | -44.39189 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 959ffadb-6aa7-339c-ba56-3d4815e64009 | -11.24583 | -54.12439 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 069c789e-9e09-325b-b0f1-ae33f4c94357 | -12.6368 | -47.08692 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ea406cc-edfe-363a-ba8a-3a589276bd01 | -14.58596 | -48.83681 | 2026-09-12 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e017cb89-0144-3002-a4bc-ba183069f231 | -15.02044 | -48.50711 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c72a6cce-3db7-3284-9206-af1e66232ca2 | -9.74284 | -64.94923 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 459a7af7-4324-309e-a596-ed32ca9cd30b | -16.03333 | -52.65184 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fa33995-4fe9-3499-bf3d-f6f11df5bf29 | -14.58428 | -52.65969 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5ab39d1-6465-3319-bff5-6a6fe26922ff | -9.74071 | -64.96054 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea121d5-df45-3bd2-862c-f514114cd9b6 | -11.23687 | -54.13781 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99aeffd2-7a97-33fd-ae3c-dbfa81b6e6d2 | -12.1304 | -48.96223 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff514b9b-3bdc-33a7-bdd4-70acd4ae31b0 | -12.13435 | -48.96678 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23646578-86f7-33ae-ac4f-fe42493ba924 | -13.69683 | -49.8952 | 2026-09-12 05:12:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61814dd4-185d-3aba-9a34-c42c92c3e9aa | -15.25404 | -53.89344 | 2026-09-12 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 37dac183-4683-3f2c-afb8-887af83bb512 | -11.24079 | -54.13473 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfe61d7f-eb36-33bb-83ea-dbf6c313f1b1 | -12.85745 | -44.3951 | 2026-09-12 05:12:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1cdfa28-4897-3b45-ba55-cf073c92e212 | -12.11718 | -48.95865 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04bdc2c2-019a-3e60-b5fe-000fabfc2591 | -12.63643 | -47.08995 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2712941-1b0e-3a41-abab-4e65ff018ba0 | -12.15263 | -64.14631 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 51f9a997-8641-319d-86c7-13a948a4a1f6 | -11.24472 | -54.13165 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 139ce68c-fc9a-3b86-bea4-f0549e0df6c9 | -16.03144 | -52.66532 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ed40936-1e47-307c-9df7-a0ab0f2ee735 | -12.63965 | -47.09218 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fa3cbf9f-9614-3807-b581-1b36a430c127 | -14.57694 | -52.66528 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ba16079-2ccb-3de3-9581-ac3529b14652 | -11.24754 | -54.13579 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d0144a-eaf2-3e9a-b881-df6ffcaf59d3 | -12.20498 | -49.3986 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 66ee2733-55da-36fb-b68b-a56c08395d81 | -12.126 | -48.96101 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6257f4a1-093d-379a-ac4b-f99e97c02f34 | -9.1881 | -68.21393 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ba05789-e0c9-3cde-8316-f2f4b80d8ab4 | -11.24642 | -54.14302 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4eec2524-435b-3599-86b6-c035b593d2be | -13.37402 | -48.01762 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c6a6a1b-a79c-378e-8d14-6e8c72af224c | -11.24024 | -54.13834 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4f7bc5c-e0e6-39e7-a2f8-f47f4fcb60cb | -12.12258 | -48.98653 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf2b463e-1f0b-3e7a-ae7c-1cbdeb0de554 | -15.06072 | -48.52568 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bd1c162f-bc36-3a85-baaf-41134b7ddb61 | -9.4956 | -68.49281 | 2026-09-12 05:12:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47f8bae7-b80c-35b3-b84d-30e1c87ec116 | -11.25147 | -54.1327 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c95acc7f-54f4-3f03-a572-b8e1ef00becb | -12.64517 | -47.08987 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 109b4cbb-1015-3d6a-a92e-b92ffb9e04cd | -12.14815 | -64.14223 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 775650ec-5294-3b88-99df-15d1daa57ab2 | -12.65179 | -47.09218 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22206601-04e1-3084-91c8-55996698b87c | -11.23968 | -54.14195 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6316def6-5015-3d34-b86a-19831c1eab70 | -15.23516 | -55.46719 | 2026-09-12 05:12:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 041dad17-0508-3a08-a092-9eba4b9d2c39 | -14.5867 | -52.66913 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18517462-1e58-374c-a42d-9556bdf7ff5d | -9.18793 | -68.21846 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e0112c26-bf7b-3f6a-ace6-7b8dbc083e6b | -11.23742 | -54.13419 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb85db6c-d667-38ea-a0b8-0b6bc7d50c5b | -17.03019 | -47.1742 | 2026-09-12 05:12:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ddcd550f-cfe3-3ce0-988f-0961c9b1e60e | -13.32953 | -51.65736 | 2026-09-12 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1dca5d77-1b13-30e3-975a-e06888e9a98f | -13.38006 | -48.00882 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f491dbf4-c57d-3329-aa69-5f587e6ed593 | -11.24809 | -54.13217 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9bbe875-ea07-3b3c-a728-520fbcef403f | -12.13382 | -48.97071 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8dca7f27-b7ea-3fd1-bbed-490206291b00 | -15.69041 | -52.76922 | 2026-09-12 05:12:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b257e29-8ba2-3c80-893c-9616d2e54f4e | -14.57997 | -52.66364 | 2026-09-12 05:12:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba3f08b3-ed21-3820-b379-d28693481a0f | -11.25091 | -54.13631 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d2de557-2d2b-3e94-9583-45c4df81d032 | -13.47838 | -48.5019 | 2026-09-12 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d66e554-7997-3e11-b7da-8692131fe0e4 | -13.23104 | -61.6092 | 2026-09-12 05:12:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86913e64-904f-3fbe-b4c6-b74c6bfc11f8 | -12.12047 | -48.96821 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b7d7ff5-c89b-33ec-96ec-55447b663d8b | -13.37663 | -48.01712 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |


[Clique aqui para ver as próximas entradas](README43.md)
