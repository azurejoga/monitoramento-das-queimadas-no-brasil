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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b09e4d0-e3fe-333b-9a52-df1d7652b20d | -17.25585 | -57.45619 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 12016daf-fa86-3ac6-91fa-15ceca244c98 | -17.28802 | -57.47223 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 0ac75670-18dd-3302-9f42-fb31f6022acd | -17.56252 | -57.54269 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| d3e3984d-e50a-351c-b2ea-ab0c7f1d2a58 | -17.58841 | -57.57232 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.6 |
| f09ffdc6-1be5-329a-8a10-e735f328caae | -18.03525 | -57.3499 | 2024-11-15 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4ada310b-be7a-3fc7-8c68-948c36a69f08 | -17.25124 | -57.4602 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 5a75ed65-d00e-34b3-8f6a-63bb18095d58 | -15.85009 | -59.29712 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cf354bc-4c43-3f5c-ba39-9480c6b7e350 | -21.57836 | -55.81364 | 2024-11-15 04:48:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1145a8a-27ae-32b1-8e8d-952a26f7b551 | -16.95507 | -57.63705 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d68491a7-f7e7-33d9-b916-70919ebb343f | -16.94571 | -57.63715 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 3943bae2-6b79-3865-bced-0bd1bd84e925 | -17.26085 | -57.47186 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| c4dc45e7-7699-3d1f-b4dc-cf63015abb57 | -17.56835 | -57.55365 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a1c26502-8031-3ea8-9b41-f0e517dbf9f6 | -16.94953 | -57.6379 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 1f90347b-9286-33f9-89a9-6525d632e470 | -17.59092 | -57.47018 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| bfd672da-84dc-38c5-a271-5f2d522e7e4a | -17.57295 | -57.54964 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 27d40284-a04d-3260-8f3d-86715bebd3ba | -21.90749 | -56.4606 | 2024-11-15 04:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3bd8cff-ff60-3578-af4d-4ebbc91cfb3c | -16.10503 | -60.09656 | 2024-11-15 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3eacf9e4-9d65-33b7-8be5-bc0a7724943e | -17.57637 | -57.4431 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| a116a3a2-f818-38e8-8a35-8eb22b9e91bd | -17.61474 | -57.55043 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 39e2416d-a33b-306f-8471-699747b3a19c | -17.62268 | -57.55445 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| f3c8aae6-2225-3cc0-9c51-b59a3bf41329 | -18.74825 | -57.30206 | 2024-11-15 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 38046484-3a49-3d4b-bc7e-f382c9545275 | -17.70785 | -57.52949 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 55c6e25f-5512-3835-9980-f592095c28c2 | -17.58632 | -57.56208 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 50376e7e-366c-3b18-a3f4-14829a52e51d | -17.84134 | -57.38872 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 08047149-d7d3-395f-8aa9-df787ad45ac6 | -15.23297 | -60.22608 | 2024-11-15 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d32d3f8d-61b2-37c6-b989-d6ba311902f2 | -17.63439 | -57.54936 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.7 |
| 8d09fdda-edd2-3d5f-9458-c2894d60a810 | -18.43979 | -51.69897 | 2024-11-15 04:48:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5e6f424-64d3-339b-a3d8-b657a87d5c6f | -17.70868 | -57.52478 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 97264c22-045f-3f3f-90af-35643d061088 | -22.05297 | -56.00748 | 2024-11-15 04:48:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9943a1d8-c99e-3446-ba1f-881d7fb1f6a8 | -17.57424 | -57.52051 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| c97a13a9-f03f-320f-a59f-e6f3382767ca | -17.69867 | -57.49363 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4a15f55d-d944-389a-8ef4-da6f247af161 | -17.57335 | -57.56937 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| e92fab05-20ef-36d8-b0df-485edede2331 | -17.58551 | -57.4352 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f40df477-a25b-3531-9f8f-9426492b7631 | -16.95123 | -57.62816 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 910c1968-d9d2-38d9-8997-4eab523e24ae | -16.93636 | -57.64542 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e2c292ec-adbc-3236-8a27-e7b321ea2b1b | -17.60006 | -57.46225 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 73420abd-f54a-3c23-8a22-666db0557676 | -17.60926 | -57.55917 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c97a611c-629c-3c3d-9ff5-093954daa6b6 | -17.21068 | -57.22846 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| d984b6f8-d8f4-3b0f-8378-d02806dd4df4 | -17.56964 | -57.5245 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| 98223582-9704-332e-b9ff-47ba0fdb9136 | -17.5747 | -57.45246 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 27f88428-2a18-36af-bad0-6cb8453ea341 | -20.86348 | -54.92731 | 2024-11-15 04:48:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d53a41-2e0e-33e8-b18b-deb2ee0e1750 | -17.65421 | -57.46072 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d1db6860-58ff-326d-ac83-ef8f849f7a60 | -17.29732 | -57.30921 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9f7eb81-b5c0-36c2-9c83-2c4390f93cf9 | -17.61388 | -57.55516 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| f1e37fb8-4894-370a-960d-49339ea3e317 | -17.59008 | -57.56282 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| a507bd0e-e144-39ae-acca-d11a2ff8f241 | -16.95038 | -57.63303 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| e79bd0b9-5637-3eea-85ce-0a05f021b574 | -17.59217 | -57.48501 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5adeabb7-b89f-32de-8eef-650e16665bdb | -17.7257 | -57.49404 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| c366f022-826b-31d8-b579-ec325304ad92 | -17.5596 | -57.53723 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| 4afc7965-c93d-3a3c-8a67-9daada288d2e | -17.56504 | -57.5285 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 8d6be6e6-0b07-34fa-96a0-362afc189285 | -15.85522 | -59.29345 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a45e66-772a-3d96-a9bc-d7ffb25ab68b | -16.94275 | -57.63155 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b29cf290-f608-3689-8304-a59e58af4882 | -17.69368 | -57.52185 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 7c73b597-922b-36a1-9a37-fa7f6fcf551a | -17.59841 | -57.47165 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 69183d4a-bd34-39bd-a182-f634f7689149 | -15.89437 | -59.27404 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c3fdc7-5085-33c4-ae76-cfc629f58f09 | -17.79999 | -57.31875 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1624b67e-3da6-377f-afbb-e7cc3f4895e6 | -16.94656 | -57.64043 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fdf88f16-3178-3d84-b13f-ea6eaa07d207 | -15.89613 | -59.27335 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 249e21f2-af01-374e-a67a-467c8b1092c6 | -17.24081 | -57.45329 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| bb93969f-ea21-3715-bb18-dc1cdbb2be18 | -17.64094 | -57.44847 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6e0f1ab7-0601-302a-925c-c4eed4987e3a | -16.95214 | -57.63144 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4a91d91c-ed54-3e1d-b605-4f925f2d262c | -16.94363 | -57.63483 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3b9e50a6-754d-3566-93cc-7091ceba6d37 | -16.01476 | -59.38242 | 2024-11-15 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a310e46a-d575-389f-96cc-951eee596779 | -17.64468 | -57.4492 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8af340be-ca46-3505-ab55-aaf175893c6c | -17.25709 | -57.47112 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 1d9e29f9-53f3-3665-a379-8d6edf5e8dc7 | -16.94275 | -57.63969 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 79e22a77-4c84-3f13-91ce-a1b76ee5e5e2 | -17.61599 | -57.54824 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 7c568457-c095-3942-a5e0-3b80367c5071 | -17.58176 | -57.47812 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c721e13a-91c1-3046-ab44-cdc68e0eef91 | -17.23658 | -57.47695 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b5f3be61-2626-3355-8b13-b4dec36ad4f8 | -17.58717 | -57.46945 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 07bcccdb-3142-334b-8a3f-d785546dc593 | -17.80369 | -57.31947 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5119be14-4bda-3fc0-a51e-6c4e6e8551b0 | -17.72196 | -57.49331 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fdabe8c3-6cc7-35db-8698-2b955bad99e8 | -17.64275 | -57.5461 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3c9f8579-f8bd-301b-bd7d-58a8064e425b | -17.58177 | -57.43447 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 839c33d1-2fbd-33d3-a06e-8f13a06090ff | -17.56336 | -57.53796 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.1 |
| a22efa34-75f7-31b3-848d-de17c02cb5dd | -17.55875 | -57.54197 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 72b21129-eb97-31b6-8306-d7e9385c258c | -17.72488 | -57.49874 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e1852e8f-6d18-3982-9c21-eece90a2f6ce | -17.6501 | -57.44057 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f0004dda-f608-33ee-8e1e-688a8850c554 | -17.57553 | -57.44777 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 64e93aa3-fa44-337d-bd7d-6910ad99571c | -17.70077 | -57.54763 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 785f1cfe-384b-3a6a-b6f3-a082fc08a4de | -17.70662 | -57.55856 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 7da4b6ad-db57-391d-82bb-510ecae95d63 | -17.59924 | -57.46695 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| abd956cf-0427-394b-a9ee-9708df514bfa | -16.93808 | -57.63567 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| bac4cff7-82ee-3c56-9f4d-9b4bcf8f5876 | -17.58088 | -57.57083 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.3 |
| 1cb46f45-a05c-33d7-97be-ae72150e5ecf | -17.57048 | -57.51978 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.1 |
| 7b4553a6-793c-3c35-af04-bdc81269e2bc | -15.53256 | -59.50294 | 2024-11-15 04:48:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6070e48a-174f-3520-b95e-5056f8926b54 | -17.57419 | -57.56461 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| e1eeb689-d849-3f01-ad8f-585ce4f03654 | -17.66407 | -57.53559 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 30e1c74f-4dfa-3647-9f59-f356eaeb1b9b | -17.84053 | -57.39334 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e83cef95-e49c-33ef-9735-50d6067f4ade | -17.57756 | -57.54563 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 6cc65301-ec30-3ed6-9e49-09a104106b08 | -17.24288 | -57.46347 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.6 |
| 6dc6c6bc-35ea-3a8f-a1ee-f64ab2fb78bf | -17.67158 | -57.53706 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f411a7d7-4bf6-3d8a-89e2-115674bc94ac | -17.26461 | -57.47259 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| b0c9bc35-8a1f-359d-9a65-643b16d033d1 | -17.59301 | -57.5683 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1756010d-d392-3b2a-9877-5e2c63878038 | -17.58301 | -57.40574 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 77136faf-ae53-3861-bfe8-1803aecf8954 | -17.57924 | -57.53616 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e88a81a2-c344-389a-846e-fd830d815026 | -17.59385 | -57.56355 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| e9130bca-dcbc-3c92-b816-3400b1664822 | -17.5725 | -57.57412 | 2024-11-15 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d2a49e31-ff19-3506-9d4e-262a676b4e75 | -17.59175 | -57.46549 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fe6e281b-c758-3b90-b901-5c2e93f04f12 | -17.70286 | -57.55783 | 2024-11-15 04:48:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |


[Clique aqui para ver as próximas entradas](README25.md)
