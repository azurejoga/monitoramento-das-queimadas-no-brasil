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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a08ced6c-fe58-3319-8dc2-7087e6b27c01 | -2.1419 | -45.6644 | 2025-12-12 00:40:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 105.4 |
| d0f89dc8-c9bb-3b07-8500-1d44e3e89eb5 | -12.4135 | -58.0292 | 2025-12-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 325.0 |
| 758a3b6d-3a7d-3bbe-bfcf-93f560da3ecd | -3.0511 | -45.7924 | 2025-12-12 00:40:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 789de10c-8622-39f2-a425-79e0de42e528 | -12.3946 | -58.0307 | 2025-12-12 00:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 137.6 |
| bc749d22-cfdc-38a0-a46d-99ef2abc8f26 | -6.1306 | -41.2875 | 2025-12-12 00:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| 9852b459-9785-3b4f-a354-296574178eac | -3.2371 | -42.0565 | 2025-12-12 00:40:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 49.7 |
| f2af5067-e5f4-3efd-857f-e1516c635ca0 | -2.4183 | -51.9278 | 2025-12-12 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 241.8 |
| cce7325e-6af2-38b5-ac2f-95f11a5c59e7 | -4.745 | -43.0576 | 2025-12-12 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 8200db11-e28b-3144-b780-dd3242f670e4 | -2.4367 | -51.9274 | 2025-12-12 00:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 302.6 |
| e155695e-f3bd-352a-8b29-1e16b241e197 | -2.2169 | -45.4159 | 2025-12-12 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 49f9034b-03a1-30be-b655-2e5a4a080718 | -2.2356 | -45.3929 | 2025-12-12 00:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 92.0 |
| bcbe34ac-24f0-3713-bfd3-74cce166f3c8 | -4.334 | -45.78 | 2025-12-12 00:40:00 | GOES-19 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 27bd9d52-038c-393f-8c93-80bd7fbdfcef | -2.5108 | -51.7817 | 2025-12-12 00:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| ddf6911c-3aa5-3aa5-bdc8-cd7198272cfb | -27.82456 | -49.74667 | 2025-12-12 00:47:00 | TERRA_M-M | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| fc18d732-736d-364b-869f-de559d953fbc | -23.30776 | -45.65166 | 2025-12-12 00:47:00 | TERRA_M-M | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.1 |
| 0f6815dc-2e3f-3088-993a-82e95756415a | -20.63789 | -51.67304 | 2025-12-12 00:49:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 02d51e09-8dd9-3535-a4c3-d95caedf487b | -20.47381 | -55.59248 | 2025-12-12 00:49:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c5e34c0f-5bcb-3ec8-a714-2396c2c903c1 | -20.47524 | -55.60432 | 2025-12-12 00:49:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b280c2b6-2b84-374a-ba52-bd50dc8ad044 | -18.83463 | -51.6259 | 2025-12-12 00:49:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1a0483d-17f6-313a-8a2e-aed736b8c9d4 | -20.63924 | -51.68256 | 2025-12-12 00:49:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80a9a9c0-d41e-3352-8700-d26472ecd0a5 | -18.83602 | -51.63552 | 2025-12-12 00:49:00 | TERRA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f7d101d0-3ded-3c18-a487-6c86355c052f | -12.43388 | -58.02677 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 5188aaf9-e5ac-3d9f-a0c9-a4003a64b952 | -12.50699 | -58.35097 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 31a6f4bc-e76e-3003-b0c7-b365840a15d0 | -12.39217 | -58.03235 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 123326e8-fdeb-3c1b-8007-8243c96d537a | -12.20288 | -49.55423 | 2025-12-12 00:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 53a75974-89c0-38bc-8f6a-1b8a5338c042 | -12.4026 | -58.03096 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 009016cf-2936-3348-977a-ca060269e2ab | -12.4162 | -58.0552 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f4e87667-9597-3e93-999b-c0aa2993d82d | -12.38623 | -58.03897 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| d1506ccf-5f07-323f-bf20-cb585055902c | -11.87633 | -57.02121 | 2025-12-12 00:49:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 502db5e5-1566-3771-b2e4-40cf0ed1bdd3 | -12.51091 | -58.34406 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 398fd56b-138b-3478-b813-87c9aa22dd61 | -12.51254 | -58.35768 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 5172d130-780c-3dad-ae76-b21d8be1efca | -12.41462 | -58.04241 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 316.6 |
| c7616170-b50e-3570-976d-5db82449ffdc | -12.62558 | -58.09381 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 2f124b83-6226-3ec8-80c5-1bf22d5b69d7 | -12.42345 | -58.02816 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 76.4 |
| add3ea65-e11d-3bcd-bf2d-729eb804c955 | -12.51768 | -58.34956 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 811e1417-ffd9-3170-a665-a90539c74618 | -12.39375 | -58.04519 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0631f805-5b44-32bb-a503-d6ef12d801cf | -12.63444 | -58.07931 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 86f8b984-ea9e-365f-876e-07fd2e6e0e43 | -12.50872 | -58.36457 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 923f8cb1-6a2d-31b0-870b-5ad37b75316e | -12.41303 | -58.02958 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 166.4 |
| 88a69f78-9bf8-3589-ae10-3525f2256997 | -12.62394 | -58.08065 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 21bd1874-d670-3d88-bdfc-9a941aef6482 | -12.40418 | -58.04379 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| c739f51a-cf63-345e-b252-efeaeb251aa4 | -12.42505 | -58.04097 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 14eefa8c-045b-3684-9f0d-756e676079b3 | -12.38332 | -58.04665 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c88e19f0-09de-3899-8d46-7788e3ab6575 | -12.43548 | -58.03952 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 2f3cddb5-4245-3283-b6a8-74cb0ce6506a | -12.20058 | -49.53988 | 2025-12-12 00:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2dd6e628-a1f5-31b6-b035-7c79339d88e3 | -12.38176 | -58.03381 | 2025-12-12 00:49:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a4c91e7c-ab29-3921-a540-05af857514ed | -12.19979 | -49.54652 | 2025-12-12 00:49:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 043eb5e4-91e6-3f5b-9688-187ad43e62f7 | -13.88142 | -56.19669 | 2025-12-12 00:49:00 | TERRA_M-M | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 334a672d-8b90-3f74-8fba-63c8922f7f15 | -13.57454 | -49.77968 | 2025-12-12 00:49:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c86b268f-f962-3666-b92c-56b03df8c982 | -11.81001 | -56.96418 | 2025-12-12 00:49:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a1bbf07-b9e9-3412-a8d4-7c05d497247e | -12.3943 | -58.0506 | 2025-12-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 104.5 |
| e3da6860-e18a-3d09-80fe-da7f9f1ae9d5 | -4.3856 | -43.6381 | 2025-12-12 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| c0107c86-a527-378c-a87b-759f52671ba7 | -6.1117 | -41.2892 | 2025-12-12 00:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.7 |
| f010ed44-1493-3e20-bdeb-9658ee87fb78 | -2.2355 | -45.4154 | 2025-12-12 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 8739cc97-1555-35c0-9735-62f0115490c1 | -2.4367 | -51.9274 | 2025-12-12 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 254.6 |
| 2291f5a6-40f9-325b-aafe-338c5fa9d44b | -12.3946 | -58.0307 | 2025-12-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 528dc427-6d0b-316f-aa4b-e036a67d3a0c | -8.0513 | -43.1001 | 2025-12-12 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 146.5 |
| 185faa00-b4da-3d34-af0d-cc3af434062e | -4.7448 | -43.081 | 2025-12-12 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| fec1d15f-ed2e-304d-835a-0b1c4396fb65 | -3.2371 | -42.0565 | 2025-12-12 00:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| cd7d97f3-12af-3419-9f56-10e832478c69 | -1.5337 | -52.7414 | 2025-12-12 00:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 9f27d9ab-d652-3c21-9c55-87c53c41632d | -2.4923 | -51.8027 | 2025-12-12 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c8005fd0-f45b-3b93-b6ee-4fbaca6b5082 | -3.0695 | -45.814 | 2025-12-12 00:50:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 5997be23-45ba-30ae-a532-17dc77ed0e07 | -2.4183 | -51.9278 | 2025-12-12 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 223.1 |
| a36d5ed5-4bcd-381b-80d3-6ffb7809ccce | -4.745 | -43.0576 | 2025-12-12 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| f464a725-c7d8-3044-a0d9-cb6bddfc245b | -4.4043 | -43.637 | 2025-12-12 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 28612356-8163-3361-9886-a704e87a2e66 | -4.7263 | -43.0588 | 2025-12-12 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 8019e385-e673-3ce6-9d7d-bc6211ab8f97 | -12.4325 | -58.0276 | 2025-12-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 193.0 |
| b3a2a138-e56d-30e3-b225-9283e8a4f29d | -8.0324 | -43.1022 | 2025-12-12 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 227.5 |
| fca848a1-750f-3e1f-8552-1c6174807cb9 | -6.1306 | -41.2875 | 2025-12-12 00:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| be0a6d59-3872-391f-974e-f6f0f6bdf657 | -2.1419 | -45.6644 | 2025-12-12 00:50:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7b8cf298-96cf-3315-8cdc-5cf955f796b5 | -8.0327 | -43.0786 | 2025-12-12 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| ff35d26a-646d-3e26-ab69-c22641264a49 | -2.4183 | -51.9484 | 2025-12-12 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 3dcc82be-e921-35ee-95ff-d20c70b6f5cc | -6.0315 | -43.7105 | 2025-12-12 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 4a44bd65-9767-3798-b125-49f340482d6a | -2.2356 | -45.3929 | 2025-12-12 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 982e4072-328c-3a29-9dba-5604f1a8d1d8 | -2.4184 | -51.9072 | 2025-12-12 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 67fd90db-26ad-3d05-b3e7-04985348ff95 | -3.0511 | -45.7924 | 2025-12-12 00:50:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 53a84412-3cbe-34cc-9a38-ce10ec53edc6 | -8.0135 | -43.1042 | 2025-12-12 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| a34107f9-6b37-39ef-a343-6ca79eee21f0 | -12.4133 | -58.049 | 2025-12-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 207.9 |
| 0d7e900d-35cd-337b-9723-0cacfcacd285 | -3.0696 | -45.7917 | 2025-12-12 00:50:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 128.2 |
| 8efb30e8-8352-3ff2-abb4-f9947f7eecf1 | -2.4368 | -51.9068 | 2025-12-12 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 27111e75-3be7-3d65-8277-af18b8d57b68 | -4.3858 | -43.6149 | 2025-12-12 00:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 8d54c573-b499-36a0-b5c3-2cea62ee68b2 | -3.9511 | -41.5186 | 2025-12-12 00:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 33a3eebf-61ea-30ab-9b12-439d30c80b1e | -12.4135 | -58.0292 | 2025-12-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 304.4 |
| 67389434-da62-3687-8593-c150dc859767 | -4.7261 | -43.0822 | 2025-12-12 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 49de04c0-1ded-3d75-948d-64a9dfa07a6c | -3.237 | -42.0802 | 2025-12-12 00:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e61d54d6-ef99-31a4-9e05-fad7134f9963 | -2.217 | -45.3935 | 2025-12-12 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 0caab115-388b-3ace-85fd-37d6e79f3124 | -2.2169 | -45.4159 | 2025-12-12 00:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 73c4c355-2685-375e-850f-2b5d812f8b47 | -8.0516 | -43.0765 | 2025-12-12 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| da499944-6762-3efd-af77-8e5acb22fb73 | -12.4323 | -58.0475 | 2025-12-12 00:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| bf58f63c-1631-3632-81c4-acee7219fe0d | -2.4367 | -51.948 | 2025-12-12 00:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| c1a9d346-2fd4-3a26-ba56-94c5e86761a5 | -2.5108 | -51.8023 | 2025-12-12 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a843b735-5d7c-3a97-b49b-4f98ce254eba | -3.07176 | -45.80019 | 2025-12-12 00:52:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 4520b2ae-983d-39e7-8d2b-2e47269d7188 | -3.79709 | -51.37729 | 2025-12-12 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 52b066df-ad84-3b6d-9dbf-fbdfb473b9d5 | -3.81566 | -50.61688 | 2025-12-12 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 095db337-095b-3b01-9694-0f451f620d8f | -3.33995 | -53.34339 | 2025-12-12 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 439e5643-171e-3124-9c08-4c5da274fa0c | -3.86506 | -50.96648 | 2025-12-12 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 4f8d4ffe-4baa-3681-a5b8-20bb2c69aad1 | -3.48756 | -52.35786 | 2025-12-12 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 78158123-b5b4-39ab-ad95-9ebccbe833a1 | -3.24804 | -52.83599 | 2025-12-12 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f7b2210c-f124-3441-888e-0ecdcc6d23cf | -10.66015 | -54.2878 | 2025-12-12 00:52:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b4b374d-24ab-37d9-9ac5-c6a6e8537e37 | -6.51692 | -55.0383 | 2025-12-12 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |


[Clique aqui para ver as próximas entradas](README5.md)
