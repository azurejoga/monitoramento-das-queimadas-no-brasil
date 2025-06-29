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
| f97bdd51-9ea3-3c63-bd86-5013881205d1 | -9.4732 | -57.83919 | 2025-06-29 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e54993e-adbd-3ca7-987b-b00ca701e75a | -9.71065 | -56.18275 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccc536a2-95d7-346e-a0ea-8def67ad4f7f | -9.13613 | -61.44289 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b1047b4-e476-3914-b83d-8e4049fc35b6 | -9.11564 | -59.0502 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55bc3822-8030-3f34-907a-d07b9731a722 | -9.13671 | -61.43872 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa97a3b6-c1e8-381f-b2b2-e84a954fc252 | -7.2992 | -55.31752 | 2025-06-29 05:50:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e2624acd-d107-3796-9705-cc82e8e2d089 | -9.47435 | -57.84036 | 2025-06-29 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 990bdf41-7fc0-37b3-85f8-27c9587e0560 | -9.09249 | -59.49379 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ac8ef57-19c0-36df-91e8-aedb04069ba5 | -9.70382 | -56.1867 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 081c60d8-37a7-348d-9314-f35e05d1c492 | -9.71002 | -56.18764 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 410bf37b-e9db-3183-8a81-7044ab37c74f | -9.10761 | -59.05011 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6be7512-55a9-30b4-baf7-f7ea7939aaf2 | -9.24703 | -63.29327 | 2025-06-29 05:50:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fae1f077-51ef-3b91-a9cc-94cdab9b045a | -9.35056 | -58.83596 | 2025-06-29 05:50:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 293a43b3-07bc-3b55-9434-245a7fa64735 | -9.09056 | -59.47055 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 593a7af9-bd52-3e3c-ab93-70c896423c3b | -9.71512 | -56.18477 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0c1b567-f795-33aa-9cb2-420ce1fc5bba | -9.7021 | -56.18777 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ef40ee6-d726-31ef-8c74-1b8dad32a63c | -9.11092 | -59.04651 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03e3361f-07e0-3cd2-b8a6-c013054e6496 | -10.04144 | -54.33487 | 2025-06-29 05:50:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42c90565-538a-30ff-9e38-b2f251c83b4f | -9.7089 | -56.18389 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6b6392d-98cb-3193-b629-9afff55e5718 | -9.70444 | -56.18184 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f08a66c4-cfb9-3149-b0d4-8e44e6e3c5e6 | -9.47075 | -57.33727 | 2025-06-29 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 820916f3-c1a8-3522-963d-0a80ad0b1c6b | -9.47367 | -57.83547 | 2025-06-29 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e2790fa-32c9-3592-8479-2e357ea3f73c | -9.08333 | -59.48668 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac92599f-05bd-3be7-935c-e18adfc41923 | -10.03444 | -54.33411 | 2025-06-29 05:50:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c530263a-030a-365b-98e6-c39407bc2356 | -9.70831 | -56.18875 | 2025-06-29 05:50:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e99351b5-8ebe-3fec-bc40-391b75100040 | -9.17245 | -61.40532 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 260661de-960e-336a-9907-dff6db11bac4 | -9.08829 | -59.48741 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93dd25ea-d9b2-399b-9172-1eecc41092d3 | -9.08753 | -59.49305 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3a1025ac-be18-330d-b510-fb9d2e0f9ff7 | -9.0856 | -59.46984 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 560bbb38-882a-3a33-b73c-3779336b6fd7 | -10.03726 | -54.3292 | 2025-06-29 05:50:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00048a45-dd9d-3264-a26f-9987e5fb4af3 | -9.11314 | -59.04781 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4159f381-5b35-3f64-b15a-64bd3dcf46d0 | -9.11525 | -59.05319 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5271fab3-cd10-3b96-82e4-f6298e58e245 | -9.25089 | -63.2938 | 2025-06-29 05:50:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea39cb19-bde4-3745-8892-d24dbf112555 | -9.10719 | -59.05313 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b05c4492-1486-393a-8c2b-71f3a8640dee | -9.11013 | -59.0525 | 2025-06-29 05:50:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 347ee741-2cf0-36f7-b914-31751f5957b3 | -9.47127 | -57.33324 | 2025-06-29 05:50:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14cba735-b8df-37c1-9dd3-30956d4d0bf7 | -10.85309 | -53.76321 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2efed476-e85c-3483-806e-99e8b2f6a10b | -12.48088 | -58.47331 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ea8c2b4-c6de-3455-93b3-a543a9e6e327 | -11.04246 | -55.37749 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3b06ad4-cac5-3abd-9f23-efae6f079f71 | -12.48644 | -58.47417 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e18de9a-1447-3003-a179-5bdc6adc7df4 | -12.62053 | -54.21377 | 2025-06-29 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7e8ad9a4-eda6-3ceb-b84d-4e0b2731161b | -12.61903 | -54.20827 | 2025-06-29 05:53:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acf69120-3403-39f0-a461-7866a4004190 | -10.34461 | -57.50148 | 2025-06-29 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7d4096b-2460-3f4e-9224-b685800a13f6 | -12.47163 | -58.47178 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed0040cf-9663-300d-b6b0-5f40ca75479e | -10.83123 | -53.76059 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36d5040e-8313-3a23-bdd5-eb2f1e8d628f | -10.03998 | -59.35426 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b814433-1760-3ed3-8471-12c173cd6f55 | -10.29339 | -57.02783 | 2025-06-29 05:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2d39d4b-55e6-30dc-a99e-521d6cfb0a8d | -12.60934 | -57.87757 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f0ec2f7-adb3-3541-89b7-a3d3ecf2e5cf | -10.03959 | -59.35725 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5fd0a83b-696a-3f75-80b9-3c8445fc4078 | -12.48831 | -58.47412 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c9f56e1-da38-3406-a5c7-0b622740e3c4 | -12.10426 | -54.66874 | 2025-06-29 05:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d64e3ec3-0bbc-37ac-962e-5989696cbff7 | -12.48324 | -58.46944 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d92ddd0-30da-3fa6-81ff-c35234c565a9 | -11.04041 | -55.37202 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d526704-4d01-36ca-b128-edf9aa149393 | -12.99184 | -59.05633 | 2025-06-29 05:53:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccb21491-ad56-3d7c-bfeb-bcef6443aa71 | -11.0306 | -56.26115 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05831552-68c5-3201-8685-5693810b4a91 | -12.47531 | -58.47255 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fbc7736-6e14-394c-ab19-c7c3b68d9c19 | -10.29396 | -57.02332 | 2025-06-29 05:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dff46ef-5c68-3e42-ab01-87e853496818 | -12.99227 | -59.05279 | 2025-06-29 05:53:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecef18ef-e135-391a-a095-42c576ecebbf | -12.5007 | -58.35341 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a3f8a5a-d91f-3132-8454-556da5425ef4 | -11.0212 | -56.26448 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53b80477-914b-3a35-b6b6-4ac95c0d8937 | -11.01228 | -56.23238 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdbe0043-955b-3454-bdc5-ac3e613c3811 | -11.03573 | -56.27209 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6f5bb8d-fec8-31f2-8ff5-13dc1cadc56e | -12.60306 | -57.88089 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167cb03b-2da6-3bf6-80c4-40eb78c6c27e | -12.09725 | -54.66785 | 2025-06-29 05:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d70b4deb-fe40-33fd-af05-fef9f971e8e9 | -10.04465 | -59.35808 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f629e287-5451-3a2c-8efb-7bda69359f72 | -12.47768 | -58.46865 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f19fcfec-7ff9-36d3-8c8c-b2cc38a289d3 | -10.83693 | -53.76318 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e7b3663-19ae-3577-a03c-1924f60766b9 | -11.03515 | -56.27717 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3447463-8879-32b4-91f6-934f28d94b58 | -11.02565 | -56.28038 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e516d2be-0816-36dc-98f9-14fbebf5a8be | -11.03378 | -56.26617 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ce69dae-fef5-39b8-9b95-1647f30a43cc | -11.03254 | -56.27627 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 28fd6114-9741-3bcf-81bd-2dc7df8dd56e | -11.0491 | -55.37835 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 067223e3-1c62-3708-98dd-2d2072a710df | -11.00601 | -56.23125 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 554e95d6-cf8a-3346-acc4-c2f81d2344fb | -11.02944 | -56.27127 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26c5b2ec-6566-36c8-ab9a-bedb07264216 | -10.83771 | -53.76868 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f28f8d6b-8212-35fe-99c9-8f5124dc638e | -10.83609 | -53.77029 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e88bbb33-7894-3f94-842e-d9dd5648a9ed | -11.0344 | -56.26107 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 324086d5-9965-3ce2-aeed-cd64b70684ea | -12.48689 | -58.47033 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee63494e-6da7-3084-b986-b227e3183c95 | -12.60885 | -57.88169 | 2025-06-29 05:53:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca52b5c7-a1c9-3c44-960d-fb72e8bafad0 | -11.0218 | -56.2595 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d830fb41-0b53-32ab-aa51-1e6357c77f2f | -11.01937 | -56.27951 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c459cba-df86-3142-a051-cb600a711455 | -11.03316 | -56.27123 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cae502d8-d68f-3048-84ab-640bf7419604 | -10.35615 | -57.50295 | 2025-06-29 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a68bc861-0f64-31e8-8e9c-fd54b1b5a2d7 | -11.02809 | -56.26036 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e7d3d2a-b868-33fb-8fbe-44b805ed7ae7 | -11.03585 | -55.37636 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9031c7bc-dc01-3049-9a32-1a0f02cf0ceb | -11.01734 | -56.24348 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a91a2408-c1af-30f1-8fff-3aa6ebf8a9b4 | -10.85238 | -53.75747 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0fece2b-255e-322c-a952-81be43da730f | -10.29452 | -57.01888 | 2025-06-29 05:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76512723-0144-3937-bf96-3e87ea8b3c86 | -10.34986 | -57.50623 | 2025-06-29 05:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e49b30b7-e94a-339c-8ff6-e97e8387986c | -9.53239 | -63.57459 | 2025-06-29 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce7573c5-ec5b-37e9-891d-4e9c82dd6cc4 | -11.02687 | -56.2704 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 67eec956-607d-3dc0-b1c0-750a5275c46d | -11.03193 | -56.28125 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efe7db5d-4dcf-3a0b-b99e-478a146b589d | -11.02626 | -56.27539 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96f1cc62-a3ec-39ba-8f0e-d03975aa7134 | -12.48276 | -58.47326 | 2025-06-29 05:53:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a908c65-42c8-3b5a-9dea-3a22d26b3370 | -11.02772 | -56.28623 | 2025-06-29 05:53:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f915ade-118e-358d-a3ef-d61f4892c52a | -9.32059 | -68.32417 | 2025-06-29 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 453fef64-5405-376f-9a10-b394091daff4 | -10.83781 | -53.75572 | 2025-06-29 05:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef5ff617-35ad-38db-be93-b322f51598f4 | -9.92692 | -59.9004 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dfc389cf-18bf-394a-b8bb-15a79e3bb2b4 | -9.92058 | -59.91042 | 2025-06-29 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95874a49-ab6b-375c-a587-5fd9fd7ca42a | -11.04636 | -55.37901 | 2025-06-29 05:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README29.md)
