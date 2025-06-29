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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ff06318-16b3-3287-9fec-18162b21c30b | -10.9808 | -45.1335 | 2025-06-29 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 5c9b77a3-a680-359d-87ff-79b21117ac0e | -11.0356 | -56.2644 | 2025-06-29 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1856c088-f072-30ca-af5d-0cfa2139bb9f | -10.5579 | -52.0289 | 2025-06-29 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 162.0 |
| 46414ceb-7498-3d4d-a94d-68d618c8a515 | -10.9811 | -45.1104 | 2025-06-29 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 234.3 |
| e69b2b37-3498-3a13-a7ad-7db365993ccc | -11.0354 | -56.2844 | 2025-06-29 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 1c84217e-653c-3f20-9afe-6e1f44481160 | -11.2666 | -52.7318 | 2025-06-29 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ce19491f-6154-30f5-b689-11a346fd9389 | -11.017 | -56.2458 | 2025-06-29 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 47.3 |
| e00c3903-6042-3b41-adec-e8073c6f48c0 | -22.4056 | -46.8205 | 2025-06-29 01:20:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 66.4 |
| e926011e-a57f-345c-b013-a9939f7047e0 | -11.2664 | -52.7527 | 2025-06-29 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 12d398d8-d496-3613-9307-47fc9b0eb40d | -10.962 | -45.113 | 2025-06-29 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 4193c849-0407-340d-b000-089aef25ccff | -10.5576 | -52.0499 | 2025-06-29 01:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 215.3 |
| 2fa7eff1-d110-3b69-a1f8-68b498716ee4 | -17.4045 | -42.6186 | 2025-06-29 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 114.2 |
| fd6dcdaf-5530-3408-bc57-84565e56e384 | -10.9815 | -45.0874 | 2025-06-29 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 11ecf611-93c2-37c7-9d14-016f35ceb3ce | -10.5387 | -52.0517 | 2025-06-29 01:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 35cee772-da98-324d-bd21-e2aceff03a9d | -11.0168 | -56.2659 | 2025-06-29 01:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 31a2740a-d95e-3ef1-894e-0dacc5aaca30 | -6.634 | -47.274 | 2025-06-29 01:20:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 5cdab7d4-337b-3f24-aa4a-fc73bdf7550c | -10.962 | -45.113 | 2025-06-29 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 10cc3a60-00ad-301a-b773-87aff1bf1145 | -11.0166 | -56.2859 | 2025-06-29 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| b3e98107-1127-3f15-b09a-e754c9dcf2a3 | -10.5576 | -52.0499 | 2025-06-29 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 182.0 |
| 36a4a388-235a-32b5-af0b-a5c5baace340 | -10.9808 | -45.1335 | 2025-06-29 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6c7d4556-6765-3752-a723-e3089226295d | -11.0356 | -56.2644 | 2025-06-29 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 3b90bb29-7327-361c-940d-1d3bed07b19f | -11.0168 | -56.2659 | 2025-06-29 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f9e5aa3d-6c84-3d52-98d2-d146246dfbf7 | -10.9811 | -45.1104 | 2025-06-29 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.4 |
| c0fc4e69-055b-3766-891c-db0daad2345b | -11.2664 | -52.7527 | 2025-06-29 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| cca952be-6aa0-31b8-bc5b-d8f101097d56 | -11.0354 | -56.2844 | 2025-06-29 01:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 2e85dcfc-7b2e-3396-98a9-81deb2f366c9 | -10.9815 | -45.0874 | 2025-06-29 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 394c00fb-ff50-3337-aecc-57a7ec9931eb | -10.5579 | -52.0289 | 2025-06-29 01:30:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 537d9dc2-3600-3528-a5bd-ce87c58cbacb | -17.4045 | -42.6186 | 2025-06-29 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| d3509894-22f3-328b-92c2-8f87b3bfd280 | -17.3844 | -42.6235 | 2025-06-29 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 49c44772-a48c-3bf7-89fa-b25b23175ef9 | -9.7182 | -56.184898 | 2025-06-29 01:30:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b55c32b3-2eee-3128-8fc2-33a35198709c | -10.3072 | -57.127998 | 2025-06-29 01:30:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad9b333-1d5d-32c6-ad42-39330e2f7deb | -11.0229 | -56.2379 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 432efb24-6bfb-3928-9de8-19ffa6e494c9 | -11.0206 | -56.228298 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a892bef9-3ec9-350b-bb57-3d1fbc4b67a6 | -11.2648 | -52.730202 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba024c4b-dabd-3ce0-a902-92971c17a06c | -12.6117 | -57.868301 | 2025-06-29 01:30:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e36ff78f-c67e-3360-a451-2db414a1f9ac | -10.5483 | -52.032398 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1943e587-0d72-3c95-b252-5a7bb7575282 | -11.5601 | -52.753399 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51af1204-e9f9-3d74-b810-0c4f5ceb3954 | -11.02 | -56.268902 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a8505162-ca03-313d-a63c-383043ce0ede | -9.0935 | -59.471298 | 2025-06-29 01:30:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7fb7eaa-6a39-3998-a658-3f18bdf7fa5a | -11.5408 | -52.7584 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| daa932a4-5b4a-36d9-b095-12e2b01bd46b | -13.1454 | -56.807598 | 2025-06-29 01:30:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b016aa28-c079-34a2-ae64-948d10b0ea84 | -11.0344 | -56.285599 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 29793849-f500-34ce-aa91-a94cbe8d653b | -11.0177 | -56.259399 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a2474eaa-799d-32b4-86a0-b1a961eb0195 | -9.087 | -59.487999 | 2025-06-29 01:30:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0c989a6e-f4e4-3374-98cf-d458c4512486 | -10.3093 | -57.1367 | 2025-06-29 01:30:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf7a73f1-ddf5-34bc-8730-48cb8154753e | -10.8361 | -53.767502 | 2025-06-29 01:30:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 01618f33-60e2-318b-9ec5-17b451a816f1 | -9.25 | -63.297199 | 2025-06-29 01:30:00 | METOP-C | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5b32c553-906d-3153-82c6-3f30900f6e57 | -11.0372 | -56.254601 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9e56e26-b84e-325a-949e-8a7a61da0d75 | -10.5724 | -52.045399 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6938be0-52a8-3677-a2a2-c08c63222a03 | -11.5527 | -52.805099 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c026c6d9-8c49-3e5e-bfa2-2db7e59e335d | -11.0395 | -56.264099 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac5f499a-665c-30b6-ab80-3d6c9947dc50 | -11.5641 | -52.769001 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f341ab60-7c43-3652-836d-f65778166b8f | -11.0275 | -56.257 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2366e9fe-5e30-3a3b-ba5f-69065fe5e56c | -11.5504 | -52.755901 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0f6200ee-d156-3d72-8123-19cd176bd3ed | -11.5254 | -52.779099 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b984c489-5795-36a5-b4fb-47b0bc0c1c31 | -12.4848 | -58.473202 | 2025-06-29 01:30:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4e18280c-01d6-38a5-b3e0-5923fb9a24e4 | -12.5077 | -58.350101 | 2025-06-29 01:30:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 45dd11e2-bfd9-399e-b9eb-ee0b677f4c56 | -10.3051 | -57.119202 | 2025-06-29 01:30:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c9dd421-299e-3f37-8b68-75fe4cb867ad | -11.5311 | -52.761002 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66eb7f48-0221-37fb-8394-93db64de2ee0 | -10.5627 | -52.047901 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11c0ba5c-befe-3ba2-a17f-152ade42e18c | -10.3558 | -57.504799 | 2025-06-29 01:30:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 325cfcd9-e482-34df-9e85-3d29e919ec51 | -11.0252 | -56.247398 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb4c49fe-6ba8-35ef-b13f-fdfc57eacecd | -11.5623 | -52.802601 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83415fba-b2a2-3734-8c2e-b8455e46e27f | -11.0442 | -56.283199 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19240256-e295-3eae-af9d-ddc9e0bf6226 | -11.5448 | -52.773998 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4604627-4af7-39ec-ad59-3ea6acfa00f1 | -9.0887 | -59.495201 | 2025-06-29 01:30:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9e88f2a-5af7-3031-b6ce-9097f98ff653 | -10.5677 | -52.027302 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3af53ae-3a76-3781-92fc-aea184a82951 | -12.1121 | -54.568699 | 2025-06-29 01:30:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 823d19c2-9854-3422-befd-8a25c95189ba | -9.7085 | -56.187302 | 2025-06-29 01:30:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2463259-9128-3a57-99c0-497962f778d5 | -10.5674 | -52.066002 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fd94b526-ce51-3d2d-bc51-ca4a52a2b7a9 | -7.2996 | -55.323898 | 2025-06-29 01:30:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b93d243c-6060-3cd3-b25a-a9f3d85b528e | -10.558 | -52.0298 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba0f016-a979-3e9f-ae5b-2b522732231d | -10.2995 | -57.139099 | 2025-06-29 01:30:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bc00b22b-ff39-36db-9038-5730522b96ff | -11.0108 | -56.230701 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d82a5af1-0e83-3504-b87c-10efd0db751c | -10.553 | -52.050499 | 2025-06-29 01:30:00 | METOP-C | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1a311c0-83e0-353e-947c-10d572b8a5d9 | -11.0223 | -56.2785 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f7033fe-8004-3248-b1d1-3d5948369b94 | -12.6323 | -54.207901 | 2025-06-29 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2aacfd2e-8920-352f-b4cf-65dcb2342c4e | -10.8715 | -53.743801 | 2025-06-29 01:30:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 834311cd-979f-34d0-b647-fa9b845c1b9f | -6.5797 | -51.1166 | 2025-06-29 01:30:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdb20e43-6d60-35ad-84bc-afac113d4c5c | -11.0298 | -56.266499 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e31aadda-2c3b-3be3-865b-d80f6ea8514a | -11.539 | -52.792099 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74c487f4-0aca-3802-8caf-4554bb09d7a6 | -22.4027 | -46.805099 | 2025-06-29 01:30:00 | METOP-C | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4f8c819b-9590-3fbb-9b62-b30753edb231 | -12.6135 | -57.875999 | 2025-06-29 01:30:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8cfa71cd-9574-32a3-b472-0316881e2cbc | -11.0321 | -56.2761 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4488f6b1-3920-3172-bb52-85f849d43b40 | -10.8458 | -53.764999 | 2025-06-29 01:30:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9c01235-c352-3fad-b3b2-f4ca3943733e | -12.4946 | -58.470798 | 2025-06-29 01:30:00 | METOP-C | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0ae70be1-289c-3636-9446-5e6780cf13ae | -11.2786 | -52.7435 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 78f339d3-9b81-3dd2-be98-375212bf5f83 | -11.5544 | -52.7715 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1474c3ce-63f9-35e6-8050-e0e45892f5c8 | -9.7157 | -56.1749 | 2025-06-29 01:30:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4b237da-0b17-398f-a8c5-55c65592946f | -10.2974 | -57.130402 | 2025-06-29 01:30:00 | METOP-C | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce3f8762-0ba3-304d-8be6-e2fd1cb8f9bb | -11.2592 | -52.7486 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eed73de4-f5c1-33c7-ae98-923bfa24bfef | -11.5487 | -52.7896 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 622e31a8-642b-3ee9-a382-7b6da76ebc55 | -11.0247 | -56.287998 | 2025-06-29 01:30:00 | METOP-C | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0b1ab1-03ca-33a0-b78d-d6b244f55b7d | -11.5584 | -52.787102 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e19f979e-049c-354f-9530-dc501e49498b | -9.1189 | -59.048698 | 2025-06-29 01:30:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe9c0977-03f2-3e00-ab53-c1665ed24a62 | -12.6153 | -57.883801 | 2025-06-29 01:30:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 865f6c35-3daa-3819-9bb1-2a2372c269ed | -10.3577 | -57.513199 | 2025-06-29 01:30:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b15493ab-481d-3a5d-9c35-9f17765a0329 | -11.5351 | -52.7766 | 2025-06-29 01:30:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 655cea4b-2d63-340b-bcb7-fca3bf182f41 | -12.6256 | -54.2225 | 2025-06-29 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2d04d836-0fe7-3a3c-8456-7b42544fcbc6 | -13.9559 | -54.492199 | 2025-06-29 01:30:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
