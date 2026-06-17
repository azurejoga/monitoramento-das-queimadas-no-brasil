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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7c8c221-7df5-32ed-84c7-55463eed7b2a | -3.50729 | -48.03569 | 2026-06-17 05:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21da3d62-3ee2-31dd-b0ce-993aa562e4df | -4.35497 | -47.7648 | 2026-06-17 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8aea6cf0-9668-3952-9d9e-d90e04f6aa9f | -4.35386 | -47.77239 | 2026-06-17 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2549733a-cc48-380f-8a9b-065592d69579 | -4.35471 | -47.77132 | 2026-06-17 05:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 01a33941-fd51-39f8-8523-ff1fa86f5b57 | -3.51439 | -48.03693 | 2026-06-17 05:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f511e883-429a-3d6e-93f2-9a83ebb20ce4 | -12.8548 | -44.3625 | 2026-06-17 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 1fde6581-de7a-344a-87a8-913758efb1ac | -12.8354 | -44.3657 | 2026-06-17 05:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.8 |
| 06fd610c-7dc2-32c9-8b1e-032ebb274a53 | -12.07713 | -54.60976 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 321e6420-1119-3e67-88c8-58565c2a671d | -10.7681 | -54.1078 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eff689cc-6413-3e03-9c21-72faefb083d1 | -11.35499 | -55.82521 | 2026-06-17 05:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 80d263f5-d7d8-38ac-bb34-f5d2c1381047 | -12.21343 | -52.79678 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 0847f92b-b58d-3fd4-81e2-108bcbc0b17e | -9.37592 | -50.54057 | 2026-06-17 05:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8c045c2-740c-3725-8199-0455e016b640 | -12.17044 | -52.78471 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 83bf8472-44b2-3d51-bc02-293cd0d3c620 | -12.19602 | -52.79 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| bdd0a7fb-3dbf-3ed5-85f9-8807fbae849b | -12.21713 | -52.79973 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7a9a535c-8a1e-3506-b36e-89c72a2b15da | -10.12015 | -52.1786 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54f02dc6-1f43-38d9-98cb-734db3fe70c5 | -10.15637 | -56.61045 | 2026-06-17 05:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f668e08e-b74d-3a1d-906c-be5971d63096 | -10.77347 | -54.10863 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba1b6c74-96ad-3a13-8fff-4dae1d36fc7e | -12.19159 | -52.77576 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 40208b4a-521a-383b-9a23-c928ef0f4734 | -10.1213 | -52.1695 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 59fcc7d9-eeba-3a3e-a195-b283e6249efc | -12.17749 | -52.77657 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5a367084-81e5-3f38-9ec3-6bfa9b501ccd | -12.0811 | -54.61308 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 332814a4-ca46-3fc7-9358-a6b73334aa4a | -12.20354 | -52.77738 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f3aa2bdc-88fc-3fe6-ad92-fe0e20be618e | -12.17098 | -52.78025 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 54bfcfcf-4864-3487-80b0-0b7110a73f01 | -9.36929 | -50.5397 | 2026-06-17 05:40:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c97bb9e7-2469-3ce1-9afd-63a68c2456fe | -11.54297 | -52.78164 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bae1e100-a7d3-36ab-9fd2-27e6ac2604e4 | -9.18626 | -58.05155 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc67d93b-c025-3ae7-b91d-8073c20843c8 | -12.67565 | -54.57688 | 2026-06-17 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a012a5a-b602-325f-9c0a-7eec8c4b0f7b | -11.58566 | -55.34496 | 2026-06-17 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05e66c04-cfe1-34e5-b773-d29e5261a438 | -12.08031 | -54.61953 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0db55133-4a4a-3cfc-a138-8710af761924 | -12.19487 | -52.78337 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 140680fc-c45a-3292-bfdb-0cba0d5be469 | -9.72839 | -57.67339 | 2026-06-17 05:40:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e437a30e-56d4-333b-ae32-e2f8f870d169 | -9.46087 | -57.83606 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85c2f0a1-3e9c-30f7-86ea-49e4e216c74d | -12.202 | -52.79079 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 4bd2eb05-c00d-37df-b4b8-19a1b978a8b1 | -12.22146 | -52.77986 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 95f570db-de9d-390b-994e-bccfb7371451 | -12.20251 | -52.78635 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 600dc56b-c2f7-30a6-aa23-ff08090b7107 | -12.08241 | -54.61051 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 43d1263e-0314-3a34-8de0-4a79af44f8a5 | -10.76581 | -54.11094 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2536a3c-bda9-3b73-8520-82e1f01beee2 | -10.54282 | -53.72345 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e40ebdf-9d0d-3d64-b669-bf311b08858c | -10.77206 | -54.105 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 516aeda3-4920-3d73-8ac0-d43bc9e84974 | -12.08284 | -54.6072 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15ffcfdf-b6ac-3bfc-8f73-87032d2f908f | -12.19108 | -52.78027 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3df364f5-8347-373a-b627-135cdd81d2a4 | -10.90414 | -54.13422 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb63df0d-bca9-3017-8e4b-e367736d197b | -12.19542 | -52.77888 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c49fff79-06dd-30ff-bb2e-26a7fa6e65d9 | -10.63931 | -51.80392 | 2026-06-17 05:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d2a22bc-ba6d-3941-98e3-058645559f7a | -9.44228 | -59.20712 | 2026-06-17 05:40:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| cb27361a-00b3-322e-8f8b-8c8573ba9d3f | -10.12622 | -52.17925 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 994b694f-ff6e-3715-80ea-61812d4fb500 | -11.58609 | -55.34144 | 2026-06-17 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 268f0dbb-defa-3ecb-ae56-8ab170f798b5 | -12.20682 | -52.78495 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 72be0e35-63f7-3498-8ed2-2994f0fd80de | -11.47935 | -57.11426 | 2026-06-17 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 768b0043-1a9b-3ab4-bc5d-f1de3e44c5fa | -12.18238 | -52.78629 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a4937c3f-601b-3a81-a533-3783a0d43e2c | -11.48053 | -57.10556 | 2026-06-17 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf65964a-5d54-3716-87b2-2ee36c1b3e1f | -12.21333 | -52.7813 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a5bbb465-4739-3df5-afb9-ecad392c93aa | -11.79352 | -56.99787 | 2026-06-17 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b495a3f-5e6d-39db-9632-8a44e6c84f72 | -12.68058 | -54.58101 | 2026-06-17 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5253c84-debb-3870-917e-21c0f741889d | -10.15309 | -56.60092 | 2026-06-17 05:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21890ab7-1922-3358-88fb-2f7952bea66a | -12.17641 | -52.78549 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b3d17c14-37cc-34d3-bf2c-5fe782b731bc | -10.54326 | -53.71992 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68661209-a596-3d07-9256-4f83196df625 | -12.20149 | -52.79522 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 23d022c9-e7b3-3e75-b32d-43339762e535 | -12.22693 | -52.78507 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26b40551-d669-36f9-855c-0149b8c0ad32 | -11.54996 | -52.77379 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0908097a-5795-38c0-891a-89d4d81aee84 | -12.22419 | -52.79168 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 752cbde6-df54-398e-8e97-0317a53d99d3 | -10.1196 | -52.183 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4ad6316-2e4f-390d-86c4-cdf5ac061487 | -12.58146 | -54.16583 | 2026-06-17 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 075c2397-8947-3f78-8e6d-0f8f8d540a3e | -12.18292 | -52.78183 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf5a032c-64ef-3e7b-99fb-db037caa50f4 | -11.91595 | -55.91376 | 2026-06-17 05:40:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 597131de-843b-3f70-91ea-e9d81968d291 | -12.0767 | -54.61303 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6dd7c36-0a8f-38a4-8e2a-c534dd1e475f | -12.18835 | -52.78706 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2195eae1-51b2-3f79-88f6-f3c3726f78f4 | -10.77744 | -54.10575 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5946bda2-efcb-30f7-9774-3ff9a8c7b8bb | -12.21992 | -52.79314 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b30d70fb-6da5-3e6b-b465-e41cd082767f | -11.53759 | -52.77644 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6a2e2123-dfbf-3cdf-82b1-b9618fe04296 | -9.20837 | -58.06925 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2529eb55-d485-3104-85b7-7a26abdd019f | -10.90371 | -54.13758 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03950ccb-9877-3a10-8080-6be685a401dd | -12.17206 | -52.77124 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8dd98b0d-fb31-3f18-9be1-7b5646bb2f42 | -12.19056 | -52.78475 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e5609ec3-7a9a-330b-b3dc-5983704a33a1 | -12.19654 | -52.78554 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cda2317a-6add-3ffc-8b64-f09a357ca1f7 | -10.76852 | -54.10441 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56c3d516-bb03-3a58-9e5e-381bd07cec05 | -12.18944 | -52.77812 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9c011f99-0ea5-31f2-8486-7f7daa770bbd | -12.2003 | -52.78862 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 355ac333-4c3f-34af-915c-bc8f720537cc | -9.21239 | -58.06986 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9f89a42c-57b5-3dcd-8287-6781a085b567 | -12.19809 | -52.77205 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dc90137d-e927-37df-9cb7-9c05dbf68488 | -12.22529 | -52.78285 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 7bbed497-93e2-3b59-9f88-2b37c1228cff | -10.78329 | -54.10295 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab2d4144-8d5d-3fb6-a3e6-258b34cf7372 | -10.63992 | -51.79906 | 2026-06-17 05:40:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e361c733-5d8c-3f4e-b21a-db91f45cf280 | -9.18978 | -58.05571 | 2026-06-17 05:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44500a46-c2c1-3e13-b1d4-3ec5db9ee9e5 | -12.21876 | -52.78651 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76056b1e-a18a-3816-a25b-05e088798837 | -10.77389 | -54.10523 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd17047a-ab0d-3185-a04e-49755808e927 | -9.88774 | -52.43971 | 2026-06-17 05:40:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f2abac7-b4c3-325a-b322-0a0a7a8b93f5 | -12.22538 | -52.79832 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| defe0220-e65c-31ec-81b7-92b5ad8b6f5c | -12.58696 | -54.16648 | 2026-06-17 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a64cde1a-73f3-3c5c-9027-4cf342621270 | -11.55589 | -52.7746 | 2026-06-17 05:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ba28eeb-e4ab-32ef-abd7-e8403c8b5951 | -10.27846 | -60.5444 | 2026-06-17 05:40:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f9fc211-441e-33f9-96ed-23ac14266302 | -12.20695 | -52.80038 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 7438b7a2-2d43-36f2-9763-c535a79dceb5 | -12.209 | -52.7827 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 21b9cac7-bdec-3dd7-8827-2717151128da | -10.76768 | -54.1112 | 2026-06-17 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e3cf4f4-bf07-38b7-a0e1-72c924f0b9eb | -12.22641 | -52.7895 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 12311ccd-a6cd-3988-9063-1270a494495b | -12.2194 | -52.79755 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 7e70dc3a-9325-3272-b21e-68e9ad7eb6cc | -12.1889 | -52.7826 | 2026-06-17 05:40:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eebec97b-735b-373f-9380-0a0280cf3e20 | -12.08158 | -54.617 | 2026-06-17 05:40:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b9385bdc-dbd5-3d69-a0e3-a85f3d08fa85 | -11.47877 | -57.11856 | 2026-06-17 05:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
