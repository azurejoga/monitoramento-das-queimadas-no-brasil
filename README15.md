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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 715cf0d9-feee-37d7-b797-5ea0923255f5 | -21.87709 | -57.09896 | 2025-06-03 05:14:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a29b93c-cd94-3edb-98bd-8f4b4fce9332 | -16.39926 | -58.17695 | 2025-06-03 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cc99e0e8-6f34-37fd-979a-22bdec62d8f7 | -18.83942 | -47.6856 | 2025-06-03 05:14:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 629df21d-faca-38e3-8d45-fd12ea4e4485 | -18.8875 | -53.6402 | 2025-06-03 05:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9824a2b3-43c5-3889-92e7-566318e5adb1 | -11.9027 | -54.7931 | 2025-06-03 05:20:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| f24080c8-68b5-35c6-96e2-002738e40770 | -18.8679 | -53.6218 | 2025-06-03 05:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d2288ebf-f592-37a1-b63f-90d9c5671e2c | -18.8675 | -53.6434 | 2025-06-03 05:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 132.5 |
| fee7da74-c9a0-37a9-8529-8c2761df349f | -18.888 | -53.6186 | 2025-06-03 05:20:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 73.5 |
| ed56c7f8-75d6-339b-92e9-a8603dbd74f1 | -18.888 | -53.6186 | 2025-06-03 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 613908de-d821-330c-8c36-e02a6c22eb82 | -18.8875 | -53.6402 | 2025-06-03 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 0d26230a-ad62-3cec-8dae-1a0722f94324 | -11.9027 | -54.7931 | 2025-06-03 05:30:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 983a486a-da56-34cc-97e1-155429c3be2c | -18.8675 | -53.6434 | 2025-06-03 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 133.6 |
| ceba5789-4f69-323f-8ba0-108fac6abbbb | -18.8679 | -53.6218 | 2025-06-03 05:30:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6dc29af7-7e05-3596-b1aa-1cf4e0da2b6b | -13.09529 | -52.04136 | 2025-06-03 05:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8a61578-490a-3854-ba3f-0078db730b66 | -12.36189 | -54.17267 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60cdb198-c5a0-3a81-b5bc-0dedf9f71c8f | -9.23909 | -63.28755 | 2025-06-03 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c8e8516-f38d-3ba6-a0d1-de90a6ef3022 | -11.5526 | -56.42536 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41f002f8-fa38-3657-8741-0778f7dfe7bf | -11.64387 | -55.36929 | 2025-06-03 05:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 822e3214-0cea-3263-85b0-69350c4d342a | -12.37357 | -54.16354 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81d3b66c-6ce9-39bb-a3c8-6487c0cfda2d | -11.92344 | -54.81716 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8821af7f-00d1-3ade-a90a-61b35197273e | -11.90959 | -54.78724 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c71c4736-2992-3e82-b98f-0041f702bc8d | -11.89559 | -56.40837 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce917cb4-3529-3c5d-ba9d-a0388afa73fb | -12.37493 | -54.16504 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3c6b106-661f-31bd-956f-b97f53d81de7 | -9.61899 | -67.29192 | 2025-06-03 05:38:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eb56795-1449-35ac-84d1-2fdcbb93cc76 | -9.61652 | -62.06105 | 2025-06-03 05:38:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d3d89f0-ae47-3e36-9c42-349e9f2aaef3 | -12.09419 | -54.66678 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d62d329c-3be6-37e0-8013-5e337d421edf | -11.55772 | -56.42602 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5043e674-0872-3eb9-b4d1-704d0440d466 | -9.23854 | -63.29114 | 2025-06-03 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b03c01fd-e43e-3123-b8e7-6eafb31d027f | -10.69132 | -57.651 | 2025-06-03 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b83d04a7-89e2-3404-8923-a76cf713d844 | -11.89682 | -56.40874 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a52c9ebe-b539-3f4b-89ee-22bc1b53c69e | -12.0882 | -54.57619 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e2d0444-3b70-34eb-90eb-4a4ad58541fc | -11.64981 | -55.36646 | 2025-06-03 05:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d9ca856-93c7-324f-854d-cd186010aa35 | -9.63535 | -65.40914 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42456ecb-c7b3-320b-8f8e-1069e33a9606 | -11.89667 | -54.79185 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff708c4b-f7ca-32ee-8129-1323d8899e78 | -11.43423 | -55.0034 | 2025-06-03 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d4625e4-20e8-30f9-a385-3813f23af160 | -11.89717 | -54.79372 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd45ef6c-753b-3f93-af26-becbadc7b126 | -12.1712 | -54.25994 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7eaa5fba-2b99-3776-b252-ca14b8a03e08 | -10.30269 | -57.14354 | 2025-06-03 05:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d064291-797e-3b16-b2f7-67514f513f91 | -9.63592 | -65.40558 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecabab75-4996-3b8a-930c-11f3e370afa9 | -10.2979 | -57.1429 | 2025-06-03 05:38:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c101d1a0-6c5a-3733-bfc4-50831c819e31 | -9.43453 | -62.46351 | 2025-06-03 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf15dbdb-1b81-36d8-9e6b-2b7ae1f5f2f4 | -10.69195 | -57.64622 | 2025-06-03 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ad19c42-128f-37fd-96a2-d14dece0be2e | -11.91743 | -54.42097 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a9bc40a-a9da-314a-b0d1-c0d61284dc5e | -9.43556 | -62.46433 | 2025-06-03 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6e540e4-ef3f-31d1-a6d4-a81a47d0a9c8 | -13.09671 | -52.02818 | 2025-06-03 05:38:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a1a0324f-fdbc-3c4e-b76f-5a8c51304ad7 | -11.90074 | -56.40903 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64cf843a-8429-3652-9522-4c82dbe59684 | -9.24135 | -63.29525 | 2025-06-03 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8201eae-85ea-3dba-b241-03ec158c4866 | -11.92297 | -54.82106 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a264dd6-9c24-300e-9ad1-5bc34a6f8a36 | -11.65576 | -55.36359 | 2025-06-03 05:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aad3a105-9b92-38ee-a006-5f2b10898ee7 | -11.43935 | -55.00803 | 2025-06-03 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba278a1f-5eb5-30d4-8899-2e0c3841d9ce | -9.96118 | -64.96197 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78052149-32c1-3f0d-b22f-b9eb6984bd65 | -11.92391 | -54.81325 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abdafc89-f2cc-3f6f-891e-4493317926c8 | -12.10033 | -54.66975 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eeb61256-68d5-372f-9d76-074bc1cc53a9 | -9.33532 | -63.52194 | 2025-06-03 05:38:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91ce2ff2-199a-3388-adf9-e3bae39c7a17 | -9.65232 | -65.75377 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 204c05a0-777f-3e40-a75e-51c0cb09a511 | -11.65025 | -55.3629 | 2025-06-03 05:38:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3cb3425a-0e9d-3557-baf8-374c176f28a6 | -12.09998 | -54.6676 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c5f0078-6f74-33b2-93f9-e97cfcb5f3d9 | -7.89109 | -61.47506 | 2025-06-03 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d692f7b6-00dc-3115-974f-a06ca7e72819 | -12.09951 | -54.67165 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d12d873-fabf-3ae0-8c95-794e7707e747 | -10.69661 | -57.64677 | 2025-06-03 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1718d6c-6e68-392e-91cd-361ed7eca90c | -11.91677 | -54.8242 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8c15482-40e8-37db-9248-767b7631ed94 | -12.3684 | -54.16892 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96a6362f-27b5-3f09-8789-1d5a8c1e32f2 | -12.08189 | -54.57949 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4aeb2ad1-d4e3-37b5-9440-ad3c66be00fb | -11.91007 | -54.78319 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3d0bf489-dc12-3b22-92ee-1ad168860a8e | -12.37302 | -54.16806 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39cf69a8-4fca-37ba-8915-04b5dedee1d1 | -12.36647 | -54.17188 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 422110f8-0883-3105-af4d-9c463869f577 | -9.23798 | -63.29473 | 2025-06-03 05:38:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc51961a-14b2-3f58-9427-a3520247c00c | -11.90433 | -54.78253 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 46c127ea-1858-37ae-a452-ae4440bca95f | -9.6387 | -65.40969 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ddaa209-7160-327e-97ec-07e63ac0c3ac | -9.96062 | -64.96548 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3aa2b45-203c-31b7-9815-5cdd4a5a3e47 | -11.90197 | -56.4094 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 247a77ee-a346-3251-88a2-290e07c4190e | -12.36891 | -54.16439 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b6a4eb-2d29-32c9-8fa1-140d8c564a60 | -11.9225 | -54.82494 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15c9ec5e-41d9-3e65-8b58-809a3565ad6a | -11.9029 | -54.79446 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 051a993a-dd95-3413-954a-f5248a62283e | -12.36701 | -54.1674 | 2025-06-03 05:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 74f4fc6f-0da7-3974-9c7b-a2d756fbcbe9 | -12.10083 | -54.66571 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccb0897a-20ae-3950-911a-8b2de7999f98 | -10.01671 | -67.00356 | 2025-06-03 05:38:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d3d9b72-eab5-3d16-bc74-967a8a45eb46 | -11.43375 | -55.00719 | 2025-06-03 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52fdd340-3829-3ccc-abff-4da113b552a9 | -12.67112 | -58.21746 | 2025-06-03 05:38:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b45c1244-b6fd-3e1c-9c08-523c02999e59 | -11.5522 | -56.4284 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5d0f6d7-de0c-3e65-9519-ed2023ba2a3c | -11.91958 | -54.41971 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ded72477-8f36-3454-815d-d239fa4c2b26 | -12.17069 | -54.26431 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 444f1a2f-2355-358b-b5c3-4c31165504e6 | -11.55693 | -56.43208 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38a6c530-d3dc-3ff4-af2d-eb9eeaf8ebba | -10.01321 | -67.00298 | 2025-06-03 05:38:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 956f49bd-b461-3258-a95c-fd0b4972a26d | -12.16851 | -54.26222 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1a0f5cc5-dc69-3370-a0f3-a3a2b9202fcc | -12.0814 | -54.58354 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bee4a40-d02e-319b-9a76-6b61cb57a531 | -11.89617 | -54.79578 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7bdceb9-ea5d-3fc6-8369-48ab0f0c1a02 | -11.55732 | -56.42906 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9657b821-2a13-3a8c-b27b-f2f2c0f70ab9 | -11.90384 | -54.78656 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6180e96b-bc63-3507-9a95-e28c2991294b | -11.92332 | -54.4216 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e62ae68-c476-3c82-80d8-5e7525a1b7da | -11.43672 | -55.00607 | 2025-06-03 05:38:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| beee10f0-7d56-31a7-b28f-efc310bd2db3 | -9.67837 | -67.40926 | 2025-06-03 05:38:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c4a5de30-26d3-3e3f-8a40-65e12cf6efea | -9.96451 | -64.96251 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6cafa552-1afa-3e18-b07e-66f573892d3a | -10.69598 | -57.65156 | 2025-06-03 05:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c2d851fd-81e9-3956-a726-bee023736def | -9.96395 | -64.96602 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0788c364-283b-3f0e-8489-786386ab286e | -8.73274 | -63.8503 | 2025-06-03 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d6256bbf-a104-33ba-aa96-fcd7edc43803 | -9.75635 | -67.32926 | 2025-06-03 05:38:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9256a029-c875-3398-b0bb-c953ec28676d | -11.55181 | -56.43143 | 2025-06-03 05:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14cabfd5-c547-3e40-bec1-828922f71eed | -12.09454 | -54.66897 | 2025-06-03 05:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 853f9c9e-c0a4-3ce4-b67f-6970beaab7bf | -11.90337 | -54.79052 | 2025-06-03 05:38:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README16.md)
