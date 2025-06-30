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
| 11f568fc-ba82-30e1-8bab-2c2fd5500718 | -9.35467 | -58.85373 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2debdd9-269e-35c9-a5ef-1b74bc210f52 | -10.29962 | -57.12817 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5946b624-0817-3395-afc8-4e19ff327e06 | -10.86779 | -53.7409 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a9afa093-4a46-355a-9cf4-fecdda5f5aaf | -9.23249 | -58.74313 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d620a45-4c7d-31d4-8e73-e45a3e271c06 | -9.11113 | -59.0472 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9d72e8d-e1ad-318d-b213-a9fd5dbac96f | -10.34984 | -57.50501 | 2025-06-30 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1edef840-e884-30c3-92d9-cd67f4aa1739 | -9.11049 | -59.05166 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd441944-3ac9-3fc4-a9ba-6ae80c8aa399 | -9.23872 | -58.75357 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40deea82-d5d5-3e88-a27d-92000bbafc28 | -9.2318 | -58.7478 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8acf8b5-a312-3662-8d0e-09fe2bba3bff | -9.24321 | -58.74952 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 420f4a58-7bdc-304f-ac07-6e511a8e0645 | -10.87508 | -53.77026 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afcd9e2f-0627-31a3-8acd-a2a5132acbae | -9.25012 | -58.75531 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12a45efb-bac6-314d-b652-c54a2e418466 | -10.29761 | -57.04773 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b27b61e-171b-34f5-bc62-66aef175ade6 | -12.10108 | -54.57953 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f623c5f1-1c4e-35f3-bf3d-32f8f6bc2dcc | -10.29273 | -57.05128 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63b4b393-3f13-31ed-8b16-9f0a0a717fc8 | -8.72592 | -64.1611 | 2025-06-30 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66faf02a-e27c-35b8-87f3-7ea9004891d2 | -9.08795 | -59.48992 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c50c2fe-a332-3bf3-8c9d-a1261398c0a4 | -10.87052 | -53.76271 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6ce2573-63e6-3980-bc61-e7884cf4ab43 | -12.60858 | -57.87326 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4346fb9-2044-3765-a6b2-7d5c5aee6740 | -12.50421 | -58.35269 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0505452-fac2-37e2-afcc-3c5a24f3eb84 | -9.25618 | -58.75811 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d82952-a9bc-368f-a7bf-2d41df9b5c9a | -12.62362 | -54.22749 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9522364c-4c2a-3529-84e2-2062642f767b | -9.23629 | -58.74371 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b614856-5d62-3fde-aff9-d3449de51bb9 | -9.08732 | -59.49417 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 30cff8ad-3841-3f12-8a4e-39ff2327595f | -12.50064 | -58.3485 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab004a6b-7925-366b-a26f-9226a178b83c | -12.19806 | -49.63905 | 2025-06-30 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d0ddc83-5553-3da4-b1b2-2c8ea5effc3a | -11.20865 | -55.91844 | 2025-06-30 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b723eaf3-3c84-3ed6-82ef-96c75c55119e | -9.25392 | -58.75587 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd7fe90d-61f0-3660-85d3-eab546ddc1d6 | -9.24114 | -58.76342 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d40df958-1ed2-381f-aa0b-cbba33fd2bd8 | -9.24494 | -58.76402 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c73623bb-de96-3085-bd66-09f3c79a3293 | -9.86387 | -60.32 | 2025-06-30 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65a08df2-35e4-3f70-9f9a-e9c74ba41b66 | -9.94961 | -52.17448 | 2025-06-30 05:31:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1536311-6fc1-346f-a469-12d213efb9d8 | -12.61279 | -57.87388 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 430fc79b-1ce4-3294-bc01-d8fc672d08d8 | -10.2273 | -54.29681 | 2025-06-30 05:31:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 037cdcc0-9925-31f6-9e48-88a8d2ac0425 | -10.87552 | -53.76681 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57c565b9-691b-3fce-b523-bafc78b3d07d | -9.23767 | -58.73435 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50c3c391-70d2-365b-98b9-38383cec7806 | -10.85507 | -53.75386 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 64f64d83-b5de-3e1a-8473-7feeca10ab60 | -10.86188 | -53.74379 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5fc5f792-0622-3a1c-b325-dbd0188c3021 | -10.29705 | -57.05184 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e19bba4-7f82-36ce-a47c-2df3c160fe3b | -10.8628 | -53.73659 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f792a8b-afa2-3f18-91ef-b46db39dfa4b | -10.8742 | -53.77715 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5efef097-e13e-3d60-8a1c-e1265c2d7721 | -12.62404 | -54.22412 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| dcd4465a-37ff-37c3-bbfe-2b5fe69ce121 | -9.11267 | -59.05354 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 112ff34b-f531-3d0a-b31d-11400af56835 | -9.35845 | -58.8543 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 143eca32-6b6a-3db0-adf4-8e1ab8a5f042 | -10.85553 | -53.75027 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7588fb9-7674-3e8a-8ed3-11078a0c7f20 | -10.21607 | -54.30189 | 2025-06-30 05:31:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8b1d931-1494-34be-8427-4051985dcbf9 | -9.2394 | -58.74894 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5cb2f0d-478e-33cf-af78-40330dab5b09 | -10.85736 | -53.73588 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddb902c7-e014-38e5-b6dc-4c4cd7afca47 | -9.70241 | -56.18695 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90104a10-83b3-3d49-8bc2-7f1077442c85 | -9.35781 | -58.85645 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd01c4c5-386c-3fb8-bf46-9ebc8a54b180 | -12.62859 | -54.23163 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a2a5348-7a2f-3d12-bd38-87ec0887cba2 | -12.09566 | -54.66624 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51907db2-84d0-3808-b54b-acbc29125e07 | -9.2439 | -58.74485 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 67645685-87bf-394e-807d-0ac97ad602bb | -9.24943 | -58.75996 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 554c0aba-a1aa-33ca-ac2a-2294fb54badc | -10.1259 | -57.77772 | 2025-06-30 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43079a2b-cc39-3d44-922a-d8f42b6c7432 | -9.70693 | -56.18765 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e080320-c278-38ca-8f21-1936fb107ad6 | -10.87686 | -53.75642 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae181142-e75e-324d-b9d5-d97e26b6992b | -10.87731 | -53.75294 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e259ce73-06d9-3149-93f3-7a435694d87d | -13.08804 | -54.84755 | 2025-06-30 05:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 73f216d6-5686-39d6-a7c7-30cf6d1a3692 | -9.1096 | -59.04854 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e9928ba-9253-3f61-81af-40dc4c907c88 | -12.62488 | -54.21735 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2d34b67a-14d0-32e3-9782-0ad6a1b2fce5 | -12.61949 | -54.21661 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9108739c-70d6-38e8-967a-36abe19eff17 | -9.24701 | -58.75009 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 892a1420-084f-3178-a0d5-51a3ecbafeff | -9.24183 | -58.75879 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a4b48a21-1b2f-3cd2-926a-14ebfdecc029 | -12.63526 | -54.22214 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5fdb5f82-05ad-3df7-822e-0dd942fbe647 | -10.30134 | -57.05251 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a11bc225-309b-31f3-9678-516073e115b0 | -9.22937 | -58.73788 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aba1f832-275e-30c4-9d99-1c77a6653023 | -10.87964 | -53.77778 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8377e18a-aac9-3d5d-a526-b589a09eee48 | -10.86825 | -53.7373 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614714b0-8d5d-301f-8a89-bdf8cadcc6ff | -10.86733 | -53.7445 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dccfc634-5110-3a70-833a-f604f134d785 | -10.88008 | -53.77433 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cf0fc5d-df20-3d38-be3d-0e56a503355d | -10.86964 | -53.76964 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 208bb70b-df85-32eb-9c19-df5c2756e071 | -9.11422 | -59.05222 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27c6c53e-a1cc-33d7-ab67-6f2cbf54c5ed | -10.13052 | -57.77467 | 2025-06-30 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 156482d8-0475-33ee-bf68-c2fa10bae2d1 | -10.85146 | -53.73871 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ce62e7e-7157-3378-b2d4-7acc059c2bfb | -10.86097 | -53.75096 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c88c215c-d521-37c2-9f07-1c104f12eb55 | -12.6232 | -54.23088 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0d62678-62b5-3a4a-86f7-b6b9d18f941b | -9.23318 | -58.73846 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6deed457-7e50-3697-8e4c-86a51442b082 | -13.08285 | -54.84678 | 2025-06-30 05:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d77ed16-0afd-3a35-b58e-b97c60f21017 | -12.62901 | -54.22824 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d45da28a-2f8c-33e6-97cc-a454f7c2b5f7 | -9.53346 | -63.57578 | 2025-06-30 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7eeb528b-533a-3b69-bb5c-5163a6c28396 | -11.02712 | -56.27015 | 2025-06-30 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ad0781a8-1e62-385c-bbe3-81682f3e97f6 | -10.87142 | -53.75577 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6d14324-3c3f-3fd4-a5b5-5607d3aec4c1 | -10.86052 | -53.75451 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 812788eb-a467-3be4-a0fe-9e90d028bc10 | -12.60943 | -57.86978 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1174934f-cec1-3653-bba0-2fb545061b16 | -9.71662 | -56.18439 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd4f08e9-f5d6-384f-9264-312c188c96ac | -10.35455 | -57.50178 | 2025-06-30 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5254ee4f-5a35-3541-91ce-9fe6f6bcad42 | -12.09527 | -54.66939 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f47cd17-43f7-324a-bef9-9f6ea6c93990 | -9.24252 | -58.75416 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 877cf02f-46f2-3809-bb14-185b745a1e2e | -12.09488 | -54.67252 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 263b0573-f3b6-3e14-9ab2-82964112644c | -11.19452 | -55.91637 | 2025-06-30 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c963e67-d7ed-3c7b-a82f-f73e80b5bb29 | -12.62943 | -54.22488 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4254c521-97d3-3704-a226-286366b26735 | -9.23803 | -58.75821 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fe39970-a697-3c07-8e9f-5c5f29b1d663 | -9.10893 | -59.05301 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6403343-11e3-3579-a435-0b1df067f6cd | -9.70757 | -56.18307 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c9b6fd-e8a5-3ed8-9831-1287c1ce2914 | -9.89008 | -56.10936 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 80df92c8-dfdb-38bc-a897-80aeb475e33c | -9.70305 | -56.18238 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5bab9be-28fc-3c67-96f0-da1a58dd8db1 | -12.63568 | -54.21875 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd8e9e26-7581-326a-9348-44f845330fb4 | -9.24563 | -58.75938 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a7b324e-4f4e-35f6-8ee6-0e53e1fc07b3 | -10.30192 | -57.04834 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README16.md)
