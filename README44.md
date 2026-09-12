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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b1ec7e3-64f5-35a2-8be1-e4a2aaee0741 | -14.9534 | -47.52721 | 2026-09-12 05:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03717198-1dd7-37de-9ab2-e85c02476a0c | -9.17416 | -68.21603 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1d28eb01-6306-3419-af29-5d1ae14512fd | -9.90569 | -67.83152 | 2026-09-12 05:12:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0e4306-678f-3396-8ac4-a3bf9e0e9e7b | -12.14931 | -64.13615 | 2026-09-12 05:12:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c05b8720-bdf8-3628-ad70-e5caab4e78d0 | -10.51285 | -57.45223 | 2026-09-12 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c1baa1e-48ad-3df8-961b-98b170d2a8cc | -9.17304 | -68.21788 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ce050182-cfe3-3f1f-8a2e-6a6177284151 | -12.20555 | -49.39443 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7462c8f-2f04-325e-b881-83e779c2aa44 | -12.13179 | -48.95183 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8fa1a633-1a80-38a7-b3e4-10f44f450760 | -14.59129 | -48.83228 | 2026-09-12 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58e42ef9-f0ae-311d-bfda-c2974992b8ba | -12.20119 | -49.39388 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 322a6b43-5cb5-3337-bb97-87bc43cebd15 | -9.71066 | -64.96637 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b16bd2d-3dba-3e1b-9ac7-1378b3776270 | -9.33988 | -68.27216 | 2026-09-12 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ddbe67c-75d8-3671-8919-b50faf39a606 | -9.74214 | -64.95298 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e148d1e-e638-3def-aec4-0e0397521c89 | -14.95858 | -47.52756 | 2026-09-12 05:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 683a6b69-b22a-3c4b-89ca-c983a8b10ef8 | -10.96696 | -54.0995 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e62de86-2bd8-31d6-9b3a-e08e4d0e4e01 | -12.42879 | -54.50191 | 2026-09-12 05:12:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a889e100-2114-344f-8366-ec68dde17a57 | -11.23405 | -54.13366 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e24ee334-e4d4-30d7-af0f-ac5e6981a737 | -13.45888 | -48.5045 | 2026-09-12 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9db5b61-05d3-36b4-852f-0aad7ee2192e | -13.37114 | -48.02131 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85ee9580-64da-3990-ab24-476525680f85 | -13.72489 | -51.83448 | 2026-09-12 05:12:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62833a55-6fb1-33f4-b9b4-8181531e6f06 | -12.13775 | -48.97543 | 2026-09-12 05:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65474e2d-b46a-3cb5-b5ad-91761cfbeb09 | -12.6442 | -51.4286 | 2026-09-12 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15a549d3-53c5-33cb-a787-8e299f9ae1a5 | -16.02821 | -47.9026 | 2026-09-12 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 305d8fa5-21c3-3ff5-b71d-059e07222dcd | -15.01628 | -48.50138 | 2026-09-12 05:12:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e842249e-fcf9-31fc-99e4-188e1f75aa9d | -11.43195 | -51.43661 | 2026-09-12 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 211c24c6-556f-3ad1-9add-3b8e5f2af719 | -12.64155 | -47.09068 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f422ead2-a5a3-3991-be97-f381b4f210b1 | -15.25114 | -53.88892 | 2026-09-12 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0eca6566-1506-3f17-9689-50d2c89c1273 | -11.81065 | -60.45519 | 2026-09-12 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97391ed3-baf7-3b34-b60c-8108f4a2ef6a | -16.0151 | -52.70008 | 2026-09-12 05:12:00 | NPP-375D | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c44424fd-733d-357f-ac06-4bb92a089c7a | -14.5853 | -48.84208 | 2026-09-12 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a53d23f-22eb-3900-9363-35532e844f52 | -14.95379 | -47.52385 | 2026-09-12 05:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cddfe5ab-fe30-3773-ad61-23e021b479a5 | -11.80986 | -60.4596 | 2026-09-12 05:12:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1efaf2eb-cbae-33ed-b9f3-a7aea700bd84 | -9.73729 | -64.94803 | 2026-09-12 05:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4236843d-ac7c-3c9a-8a5a-b2c7b78e5281 | -8.95204 | -67.39005 | 2026-09-12 05:12:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10bd3858-8e2e-366d-9690-f06391ffa5b7 | -16.0321 | -47.91309 | 2026-09-12 05:12:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 313241bc-b16d-3eea-a8d8-9960e8710312 | -13.48308 | -48.50267 | 2026-09-12 05:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5782a798-911b-3e00-a631-b560951a5c83 | -16.63141 | -52.82611 | 2026-09-12 05:12:00 | NPP-375D | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb33d4b4-7250-35b0-8ad9-46c44b522098 | -12.64104 | -51.42318 | 2026-09-12 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6a946b3-4308-31e3-a297-47d4746a379e | -13.37179 | -48.01632 | 2026-09-12 05:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d0ad638c-32e7-3357-ba6f-4f22a10ac9d3 | -12.64118 | -47.09372 | 2026-09-12 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8e4331d1-9ee4-3e30-a1cc-e045039a4ce5 | -9.3386 | -68.27846 | 2026-09-12 05:12:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| be308e91-4aaf-39ac-9eb3-513224dbba1b | -11.25202 | -54.12909 | 2026-09-12 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9a88b5a-a75b-3492-af67-d516bf86926b | -11.42817 | -51.43601 | 2026-09-12 05:12:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90c95869-34e9-397a-befb-f2279ef2f4d1 | -14.98268 | -53.95386 | 2026-09-12 05:12:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0669115-0605-3d91-84fd-3e275cb290a2 | -16.29191 | -53.85335 | 2026-09-12 05:12:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58c550bf-b1f4-3d5a-807c-53072eb7b934 | -15.24705 | -53.89234 | 2026-09-12 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abef2d3d-3b0d-3b12-8c62-22eb77d37673 | -18.93516 | -46.82318 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 69e43365-2c40-3692-b9b9-a0f09b8a204f | -18.48152 | -51.71087 | 2026-09-12 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b08c4187-0c9d-3cc6-89fe-cee63768291c | -19.74399 | -46.05056 | 2026-09-12 05:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbd53181-d26b-336f-a2e2-416b28ad9bc7 | -18.87578 | -46.98079 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d493cca9-cddc-394c-980c-31af04dec66b | -18.40905 | -46.05461 | 2026-09-12 05:14:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87ddaccc-8b82-3747-8816-05e4bce2063f | -18.93744 | -46.82925 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 246edde2-74d3-3d4c-9f06-95feb77a19df | -18.93702 | -46.83319 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 78c4cc32-2324-3874-9a8c-513a374ffeb3 | -17.17192 | -55.92752 | 2026-09-12 05:14:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| da2317dc-635d-391f-8984-1679e9d33c29 | -18.94001 | -46.83195 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1009ebef-1cb7-31de-838b-9a13dadc7b07 | -18.93786 | -46.8253 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 147cdc35-7dd9-3a55-8097-faf5e8798a25 | -18.93477 | -46.82715 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ec4a696-c0a2-3f65-b27a-a5f548ad0b1a | -19.74436 | -46.0468 | 2026-09-12 05:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2009c1d-2fb3-39d3-9273-b5e1de054789 | -18.94041 | -46.82799 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a648a63-1d83-30ba-82a0-053d6a90f7ac | -19.73962 | -46.0475 | 2026-09-12 05:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eaa71fe6-45a6-344b-b15f-775e0e0d5476 | -18.87617 | -46.97707 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95691c9d-751d-3208-b480-73dd1880f68b | -17.6968 | -52.34087 | 2026-09-12 05:14:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55afeec6-d587-3460-9661-38c728229037 | -18.48608 | -51.70773 | 2026-09-12 05:14:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94dc70e4-3270-3284-b4a8-313abde8632e | -18.41451 | -46.05973 | 2026-09-12 05:14:00 | NPP-375D | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c678e0c9-a096-36b5-bbcd-58b546ac8dca | -18.93437 | -46.83111 | 2026-09-12 05:14:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6733cb93-e219-3b1a-b1c7-966d5bc922df | -18.23877 | -55.39888 | 2026-09-12 05:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6d78e58d-206b-37c2-9efc-f490cf922781 | -17.16857 | -55.92696 | 2026-09-12 05:14:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 704fb87b-01b9-3772-a4c3-90d39d8f20f7 | -17.17135 | -55.93118 | 2026-09-12 05:14:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| af575fa0-a5e8-3792-ad36-bf1ca1ef2d6e | -17.17527 | -55.92807 | 2026-09-12 05:14:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 72212765-a7fa-339d-be05-b0890e1435f7 | -19.74561 | -46.0482 | 2026-09-12 05:14:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72c1f77f-2f5f-3f22-b655-30fc716a44f8 | -2.94 | -50.4 | 2026-09-12 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bfdd440-9275-3944-bc96-b664b1817f23 | -2.94 | -50.46 | 2026-09-12 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d63e6471-e16f-3b47-89c5-9fcf486dc794 | -2.97 | -50.4 | 2026-09-12 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e3642c-8ee9-32f9-9066-8b4b9bdf1128 | -2.97 | -50.46 | 2026-09-12 05:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3299c0b-ca70-3c29-8e59-89db60f88e06 | 2.51508 | -50.85492 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5dfee358-7406-3206-a656-3a2afad41a78 | 2.51309 | -50.85934 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56c404df-bef7-399a-8b06-1bb7fece4177 | 2.51217 | -50.85392 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d926a483-3586-3340-8b70-4ed282a02d40 | 4.32138 | -61.09813 | 2026-09-12 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c13149e-a141-3b86-9d49-bd247274166a | 4.32076 | -61.09413 | 2026-09-12 05:25:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f64fd9da-fb25-3296-ab64-c906cc3ae73c | 2.51707 | -50.85315 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84806062-dcb3-3432-8115-6489b9fda3eb | 2.51614 | -50.84768 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6617a98f-47da-3096-aaa3-9b6b5fb852a4 | 2.51124 | -50.84843 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c50203da-d914-328a-9e9b-62853cb92e05 | 2.5142 | -50.84945 | 2026-09-12 05:25:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 01d67e39-4b13-3482-b245-b3fc9b2a365e | 4.23938 | -60.07148 | 2026-09-12 05:25:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5353c22b-c7c0-37f0-b226-32e5503df59d | -4.35552 | -54.7697 | 2026-09-12 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4656a225-471e-3bd8-a946-97c73a34ebdd | -2.72173 | -57.61706 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee3db358-571a-3ede-a224-464f4ba1868e | -1.02756 | -53.74114 | 2026-09-12 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32ce93de-ef0a-3d1d-8b26-7b3157c1d18b | -3.22689 | -46.94782 | 2026-09-12 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cadb7309-ff68-32d4-ab0e-bede399285bd | -3.80679 | -59.32196 | 2026-09-12 05:27:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5b5c7863-9dfb-38a5-9ca7-e04a80bdb288 | -2.95707 | -50.3857 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aecd59ad-d1e8-3674-8d19-248cf87556dd | -4.91105 | -55.8183 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8bc1a234-1582-36c5-85e1-b13c7cfceffc | -2.72511 | -57.64098 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4d8593e2-0a7e-31b5-9325-2403e4d3587e | -6.22699 | -51.68898 | 2026-09-12 05:27:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9960b6f0-df8e-3cfa-8c03-f82f35b64005 | -3.36942 | -57.70929 | 2026-09-12 05:27:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 734e9840-89cd-3d91-a850-9c381b92b784 | -4.85878 | -56.00428 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8e55664-05c9-3fdf-818b-916770b34d18 | 1.03848 | -51.05721 | 2026-09-12 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 832a145c-c843-37e3-8160-b2b5a59463cd | -2.73908 | -57.61974 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 298c8c40-d4a0-3cdc-9416-32893361b1da | -2.73145 | -57.64586 | 2026-09-12 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7e9266b3-42ce-3ddf-824a-e76023f0da05 | -5.10176 | -56.12573 | 2026-09-12 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d4886c26-fe40-3d94-b41c-17da9cd13403 | -2.96646 | -50.39827 | 2026-09-12 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |


[Clique aqui para ver as próximas entradas](README45.md)
