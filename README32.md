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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| feb1d429-acba-37a9-91d7-1dca66fb8706 | -13.91233 | -53.78092 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62c04d89-4aa3-36ba-8ee8-5e05cbe65a91 | -14.0446 | -53.58155 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 92720063-32e5-3dcb-b058-67e860646345 | -11.65534 | -60.11684 | 2026-08-14 05:21:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 394cd810-eba7-3f2f-8478-cf811a189dcf | -13.28415 | -54.23052 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 96f87f6c-57a3-370d-a212-fd3b83dae3bb | -13.90778 | -53.78028 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4228d89a-c4f6-3972-9206-d665ef70f850 | -14.29113 | -51.97199 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4838a80-ea8e-3e4a-9a1f-72f9c9046c51 | -13.28035 | -54.22549 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e33685f6-0871-3ccf-bc27-3afcdf4640ad | -14.05868 | -53.6586 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 774d650b-b668-3272-a636-97a8e678c19b | -16.91282 | -54.15269 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fd847df9-7689-3229-a959-2dc50c3d2e0e | -16.24914 | -53.7076 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 74c6130e-0c36-39a6-b2a2-8cddef88867b | -14.44849 | -51.85785 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 015e6873-0355-33ee-bc39-7af5a83b036d | -14.08944 | -53.63739 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b11b9e25-c59b-3376-bbb5-e7d4515d030a | -15.1222 | -48.65817 | 2026-08-14 05:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 383377f6-b444-39ff-b01c-29ff20a7d529 | -14.31496 | -53.07139 | 2026-08-14 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 541e94eb-0869-3ec7-a1c3-4ec6e4278a8f | -15.16156 | -50.05492 | 2026-08-14 05:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc9a3377-470c-344b-9e98-5b66d31c1bda | -15.20447 | -56.03534 | 2026-08-14 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f78ead65-4135-3a38-bb66-73b23ee125d2 | -13.42405 | -57.04925 | 2026-08-14 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdc832d8-ad2e-3602-a947-3051b26cc673 | -16.25198 | -53.72387 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec46c8cb-8b83-31f7-affa-56c978b0c9a3 | -13.90848 | -53.78164 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e9a7d57d-a045-33d1-a2b7-936f146d2f73 | -14.06014 | -53.60846 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb2c7673-4680-36bd-8d1e-7facda79b89a | -13.2414 | -54.25074 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e7f1e70-e15d-3927-969a-ae2d5689b33b | -16.91397 | -54.143 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e97d98b3-ecfb-3275-85e9-6d9a71f0f201 | -14.29187 | -51.9656 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 39d65327-0e63-324c-8a62-a2a9b1dde0fc | -13.88174 | -53.76623 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df3a17e5-806e-38eb-a495-c85a0b8c2bfd | -14.30735 | -51.96824 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9879c76e-3ebc-3d9f-b1f2-3df11d8d4cb4 | -13.81549 | -53.81433 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8ac0453-0f18-37e8-8e84-055c8a64f789 | -16.35486 | -55.38206 | 2026-08-14 05:21:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6bb01e26-3ef6-3669-a495-320c6d334da4 | -16.8779 | -54.1291 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7920665c-bae4-3e28-9f0b-75d178d2876b | -14.44811 | -51.86109 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40d4e62a-1334-3509-8c8c-dc019d7fac26 | -14.05928 | -53.65376 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d0deff8-876b-352e-9ded-cfdf9260719d | -14.2978 | -51.95993 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 93e24526-b0a5-3b9d-b896-3a29db1ac152 | -15.51244 | -53.00015 | 2026-08-14 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 537a7908-93ac-3b69-be0e-6bf0e8a29f01 | -13.22556 | -54.27017 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd881aad-f365-3bcb-b7f0-d19d0dbc026e | -14.09005 | -53.63246 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 56bcc640-93b1-3942-ae33-44aa9a7f6847 | -16.25324 | -53.71346 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0cc2a45-2005-3d2b-a07a-ff2f8de87c65 | -18.55526 | -48.18432 | 2026-08-14 05:21:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0e5b871-30c3-3f3d-9634-62b9f7696c05 | -18.88748 | -47.62796 | 2026-08-14 05:21:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 738bc7c2-0bb5-3c4b-9074-460939e8b3b7 | -14.08081 | -53.63128 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| aafc1199-998f-33e0-9014-e5694bd4d402 | -13.75678 | -53.4205 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d309732-b065-3798-96b8-aa809d37ea0a | -16.88324 | -54.13349 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fc91c726-872a-3db4-92d6-0b3b028d3119 | -18.47794 | -51.7518 | 2026-08-14 05:21:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce754ab2-b859-3e3a-9b90-2e4d319b60d7 | -13.75395 | -53.41805 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f4e4bc6-7cd2-305a-abb6-c7c80a7057f6 | -14.29743 | -51.96314 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e73f79f4-7384-35f9-b8ad-c87b7c9382a7 | -16.88202 | -54.1342 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c16c75fa-ff3c-3954-8f0d-ac3749ff0ec1 | -10.06656 | -67.55504 | 2026-08-14 05:21:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ad9c5134-8586-3f09-a7e9-5cc07c49ec03 | -13.82683 | -53.79758 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cb2518db-31f2-3584-80c8-15cfff9e2bf9 | -13.28472 | -54.22615 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c58a3a35-9579-3ca4-a212-55ac18283058 | -14.29263 | -51.9592 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 44d11959-1eac-3e1a-a92f-0e5078303505 | -12.51894 | -55.78423 | 2026-08-14 05:21:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 360e4ca4-38e6-332b-8335-30a29a897acf | -13.42467 | -57.04483 | 2026-08-14 05:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d33fbf5b-c6cc-3726-aaac-9cf6bbe4d2da | -14.05986 | -53.64904 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a34f2c39-3313-3804-b079-8c25a179d3f0 | -12.35878 | -50.89341 | 2026-08-14 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d97d5660-b605-3256-a82d-87cb16c579c5 | -16.24315 | -53.71744 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbe043b5-a0e3-3e8b-bb7f-ec852c0e4ecb | -14.03547 | -53.58802 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 383cfe0a-af60-3ecd-a449-2fa7dec76264 | -16.90928 | -54.14281 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b8afeb4-5da4-3d93-8e84-2a7b42a9e3b0 | -14.28632 | -51.96808 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d3ef793f-3da8-3df1-889a-2e3a57f33836 | -14.3022 | -51.96728 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 173deed9-410e-3fbf-b88c-8913940456b3 | -13.92841 | -53.95561 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 930fa631-50b5-388a-a9f3-6010ec6dbad9 | -14.07156 | -53.63014 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbd600c9-f2be-3ede-a8e1-e36beeeb0d3f | -15.87599 | -59.63499 | 2026-08-14 05:21:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87d39f54-96c7-3f97-a462-6e7d9cb8d18b | -13.27483 | -54.23359 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e26eddb-e58d-3d15-9259-4d2db1c36a1c | -15.12315 | -48.65747 | 2026-08-14 05:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f10de8f-9066-3178-a3ba-08effccf3bd0 | -13.27539 | -54.22926 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebf5dc8e-093f-3c02-9175-1c2a2a09f5c4 | -12.35336 | -50.89267 | 2026-08-14 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e4eef0ca-cd8b-33a7-b431-79c72f388b02 | -14.45296 | -51.86496 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e358dbd8-80b6-38a9-8b97-1b6bd79791f5 | -16.9035 | -54.15193 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 869acdd5-3e61-322f-982d-c2bc74f1d98e | -12.52216 | -55.78988 | 2026-08-14 05:21:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5e87cb7-7823-360e-9ed9-7e4afcbe225d | -14.05269 | -53.59241 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 64b3dac7-9311-3a46-a07e-c9484adc60cc | -13.25016 | -54.25187 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a769049e-74ba-3bce-ac3e-37d6904ce27d | -13.75273 | -53.41478 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d16a169c-5b84-3c79-a4a2-0485a0849916 | -14.04536 | -53.58427 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c806dc27-235f-3f52-84e8-a3b3838686d9 | -13.75739 | -53.41552 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdfc2911-024d-37a3-b7be-d2667a800488 | -14.06476 | -53.60909 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ce10c554-5cb8-31b4-87bb-63043ab68c08 | -13.8141 | -53.8173 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa914e98-4789-3cb6-ab79-5ada2fcb88de | -12.35699 | -50.89117 | 2026-08-14 05:21:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17db310c-fd04-36bf-836b-8a9f73883e40 | -13.2792 | -54.23423 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b4518f65-9fe9-3ff6-90d1-baec2a945077 | -13.90333 | -53.85008 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e190858d-969a-3d10-b602-2b045ea4ac8d | -16.90815 | -54.1524 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d6df4153-4e7c-3495-9716-cede4e6cdffa | -14.03517 | -53.62072 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21fe84bd-9fa9-37d2-8be6-000628ed262d | -13.8223 | -53.79671 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b63b42a-694f-394e-9e91-8bb5ec8908bc | -10.06561 | -67.56025 | 2026-08-14 05:21:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a7222351-d606-3eef-8b97-31feb4426208 | -16.87861 | -54.13285 | 2026-08-14 05:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 89d4fb2d-a6eb-34bd-8727-0518b46b96a2 | -13.9051 | -53.84692 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aeed01f6-ed2c-36b6-aa8b-fff784ee1f1d | -16.25261 | -53.71869 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5cd29287-46cb-3240-9ad1-dd290280e42c | -13.27711 | -54.2161 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ebcfdd-758e-33c0-ba83-caf78dc4bc32 | -14.05403 | -53.59012 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 53e16564-a9da-3ab0-97fa-79c12c789ecb | -14.31565 | -53.07061 | 2026-08-14 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf91bee8-3c8a-3cfd-9d37-134a6e48a3df | -14.07837 | -53.65095 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6412ed5e-6349-3de2-8b22-e716492983b8 | -15.63294 | -48.89699 | 2026-08-14 05:21:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 32b5da53-5160-3d55-8cd6-6a6496c9bf01 | -14.4636 | -51.91512 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bb52528-0288-36a2-8d53-52ca88880ca4 | -14.07743 | -53.62069 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d801f4da-d67e-3da3-bf99-280003c3b038 | -10.22171 | -68.08887 | 2026-08-14 05:21:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f30a395-84bc-3df3-8e7e-2e5010f9323e | -16.24787 | -53.71813 | 2026-08-14 05:21:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a041771a-2c58-3b97-8179-921bfb819143 | -15.70082 | -48.31955 | 2026-08-14 05:21:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37dc8996-4e34-3ed2-861e-7024eae975fe | -12.65456 | -54.75356 | 2026-08-14 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9115bc2c-8196-3933-8321-98d12569a2d3 | -13.7586 | -53.41878 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c916a972-0ece-3dd2-84c5-fcc394c50acf | -14.04937 | -53.58973 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e310fd0a-93c0-3813-8935-fcf231570701 | -13.2551 | -54.24815 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b557891-f40c-3342-9c41-3ea24f720c52 | -13.75153 | -53.42464 | 2026-08-14 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbd7d25b-fb47-3ad8-b046-369e116b6237 | -14.46324 | -51.91835 | 2026-08-14 05:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README33.md)
