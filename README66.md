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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e5dc4da-d57e-3f6f-8378-17d92ae95625 | -8.4899 | -48.821 | 2026-08-18 13:00:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 6e4ca092-b98c-33b0-bf1e-0e203c88f586 | -14.1628 | -52.9323 | 2026-08-18 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 95bc5939-6e1b-3708-8b45-297407906b94 | -11.3606 | -46.381 | 2026-08-18 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5db606f0-1364-38cd-a99b-737112fa7010 | -12.7597 | -48.4453 | 2026-08-18 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 77d7b29f-df07-343a-ae36-cec70857e543 | -14.2566 | -51.9259 | 2026-08-18 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 9549c942-525f-3176-99da-9b156fd15596 | -17.4667 | -47.864 | 2026-08-18 13:00:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 79.9 |
| a0dee328-56a7-3be6-bff2-ca2e42815b67 | -14.1817 | -52.951 | 2026-08-18 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 270.6 |
| 84680a1a-4ae4-384a-9891-24c031c1d83b | -14.1824 | -52.9089 | 2026-08-18 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 524781e6-dbcf-34cf-acad-846e09fc67ac | -13.2808 | -51.6673 | 2026-08-18 13:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 05128ea0-5741-375e-bc7a-dbbe0a335a8b | -14.1821 | -52.93 | 2026-08-18 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 7cf248b7-cbbc-32e6-b9d0-4f3e1415e39e | -12.7793 | -48.4205 | 2026-08-18 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ed3d0808-6f07-3ac8-938a-3c383a59f1d9 | -7.2007 | -43.2814 | 2026-08-18 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| b8ab1f28-e0a9-334a-b560-4e976c88c0c2 | -9.7709 | -47.2917 | 2026-08-18 13:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| faef17e4-642e-30fd-a1f2-c516054f3cc6 | -12.7789 | -48.4426 | 2026-08-18 13:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| af4a16b3-809e-3581-949b-f4788c43a6a4 | -14.2373 | -51.9284 | 2026-08-18 13:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.7 |
| df4b808c-b817-3c3e-8d7d-1e43719b30e9 | -14.1631 | -52.9113 | 2026-08-18 13:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| eaa383e8-283b-3751-a8a1-5488c5f2aff0 | -13.568 | -51.6953 | 2026-08-18 13:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 24e9618e-6899-37fa-8a24-58b38421251b | -12.7793 | -48.4205 | 2026-08-18 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| d8966421-4e4f-319a-bec9-4937a1cac9f9 | -14.1628 | -52.9323 | 2026-08-18 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 090b2a8c-8eb2-3c72-b487-79370a8c4ea1 | -14.3715 | -51.9747 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d7615d96-f0d4-323d-ba37-aeebf3791ed4 | -12.7597 | -48.4453 | 2026-08-18 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 75565b88-eef3-37fd-8b73-7286d933ac48 | -12.7789 | -48.4426 | 2026-08-18 13:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 351d0386-05dc-3f05-9fb9-36988d6c505b | -14.3529 | -51.9345 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 6377453c-2cc6-3299-a3ac-e321d4b8c2aa | -17.4667 | -47.864 | 2026-08-18 13:10:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 93.0 |
| dd72f0df-197b-3c8c-a2c7-48d9069d2931 | -14.3521 | -51.9772 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 1fcc1737-2663-37d4-9fa2-3a8dc7947ccf | -14.2566 | -51.9259 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 0dd8e876-f782-3b60-a17b-d9054b147df4 | -14.1631 | -52.9113 | 2026-08-18 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c3262071-16d6-3968-9c2a-953f0c8d2583 | -14.1824 | -52.9089 | 2026-08-18 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 97a90aa0-8b96-396c-adce-75e1f9c8a1f9 | -14.1817 | -52.951 | 2026-08-18 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 186.9 |
| 5bb96d72-98dc-3dd1-9985-8d29d3a06354 | -11.3491 | -45.9292 | 2026-08-18 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 42e4d130-9fc4-311e-92d9-ba0c45f74dc9 | -14.3525 | -51.9559 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 0128bb1a-7972-36f8-b064-45e53a8a287e | -11.3606 | -46.381 | 2026-08-18 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| eb9462f1-ca0d-32a8-b6f3-306ca1559ce1 | -8.604 | -50.3527 | 2026-08-18 13:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f06c94e5-a3be-303f-b68c-93a0b753dde6 | -6.7478 | -59.1716 | 2026-08-18 13:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e5a7d9a1-6901-3df0-9336-0ef209cbdb27 | -14.2373 | -51.9284 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| b8213284-5b09-3a50-bf32-1e6f683f3a8c | -14.2759 | -51.9234 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| c92c55ce-ebfd-3ae5-b006-4dd0247517b2 | -14.1821 | -52.93 | 2026-08-18 13:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 938a5ef0-a987-322e-b046-9de96c14c86c | -8.4899 | -48.821 | 2026-08-18 13:10:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 139.9 |
| ccb95a5f-59a4-3a89-b510-b17cc7584c03 | -14.3718 | -51.9533 | 2026-08-18 13:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.9 |
| aca12be8-b533-3ea5-8662-25ac5b0b8d12 | -12.77 | -48.46 | 2026-08-18 13:15:00 | MSG-03 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3348d4ec-99a8-3778-a8bf-ffd31fa94f9a | -8.57 | -54.73 | 2026-08-18 13:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406b9aa6-b9c7-36d3-bcc4-8ed1d9881754 | -14.2759 | -51.9234 | 2026-08-18 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 26a42f91-6a23-362d-81ef-80601a49a5b2 | -9.0349 | -45.8509 | 2026-08-18 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| b31fab30-88e2-3bf4-924a-b611080bb718 | -17.4667 | -47.864 | 2026-08-18 13:20:00 | GOES-19 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 384855f0-4f2a-3c4e-9273-648c9054ae0f | -11.3606 | -46.381 | 2026-08-18 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| a71c697e-7b55-306c-8f82-eb52885b08d6 | -14.1628 | -52.9323 | 2026-08-18 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 1a19c1b2-3d2a-32c7-91dc-5c959f5755c5 | -6.7478 | -59.1716 | 2026-08-18 13:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8db2c915-0812-379d-b652-9d62d0cef825 | -8.4899 | -48.821 | 2026-08-18 13:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 282be9ff-48db-307c-a6a4-6691b70660e6 | -12.7789 | -48.4426 | 2026-08-18 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 187.6 |
| a0c42abb-40ee-3911-954d-d9b0f8b6e9d2 | -14.2566 | -51.9259 | 2026-08-18 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 133.6 |
| d2ab2b6a-2264-338f-9672-1cdca2294950 | -13.568 | -51.6953 | 2026-08-18 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| baa24150-73f1-31c7-a9a6-992678e45b70 | -14.1817 | -52.951 | 2026-08-18 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 232.5 |
| e55a8ca0-effe-3458-ae06-9dc0410fe451 | -10.2767 | -50.41 | 2026-08-18 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| b9cc1327-28e1-3eb0-bfc4-7bcdcb87a172 | -13.5676 | -51.7166 | 2026-08-18 13:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 26f2fd4c-ac0e-3759-aa24-3d5b599b7349 | -8.5087 | -48.8193 | 2026-08-18 13:20:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 85.1 |
| d75cf66e-b03e-379a-b4da-14dfe16db615 | -14.1824 | -52.9089 | 2026-08-18 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4d6ac335-6b76-3966-b5dd-e42c23a9b9d4 | -7.2195 | -43.2796 | 2026-08-18 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 9cb0254c-c009-3ad3-8616-30cbb0b130ea | -14.2373 | -51.9284 | 2026-08-18 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 0400b907-abf1-370a-a4bd-7ec78d687b33 | -14.1821 | -52.93 | 2026-08-18 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 177.8 |
| 0402c60d-05af-3164-b45f-5f3f33f93f6a | -12.7793 | -48.4205 | 2026-08-18 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| a6c26b6f-d32b-3e2f-9091-1bd98e2c0e99 | -7.2007 | -43.2814 | 2026-08-18 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.5 |
| bd5abf4d-aaba-3774-85de-649d921b72e2 | -12.7597 | -48.4453 | 2026-08-18 13:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4793442c-3f7a-3f9a-a904-fda1ca500fa0 | -6.1813 | -47.8099 | 2026-08-18 13:20:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 90e33d1b-4270-3b25-8c20-47e0b26207a3 | -10.2765 | -50.4313 | 2026-08-18 13:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 78e0cc7d-53ae-3f76-8a0e-7326d9a305ab | -14.1631 | -52.9113 | 2026-08-18 13:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| b2ebc1c7-1365-3e54-8c14-c08e2b4b6168 | -6.841 | -59.0132 | 2026-08-18 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 1573b2ed-a6b2-3957-ba94-fe341ebb5293 | -6.8594 | -59.0125 | 2026-08-18 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b5b53bda-fba5-3e8b-9906-b1bd074c94ad | -14.2949 | -51.9422 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| b568d891-cd3b-30a6-ad80-b461b37ac327 | -8.4899 | -48.821 | 2026-08-18 13:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 164.9 |
| b0d0b069-2fb5-3a54-b6bd-5b4295f0bfb8 | -8.5087 | -48.8193 | 2026-08-18 13:30:00 | GOES-19 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 0366cca1-157f-314b-bd2f-9df353c8710a | -14.3525 | -51.9559 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| e2cae230-a1e7-3d33-a9e5-aa7e1b4732a0 | -14.257 | -51.9046 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 475df16b-839b-32ac-84e1-f976db512966 | -11.3606 | -46.381 | 2026-08-18 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| abcbe2d6-0d69-3b57-8b66-ef4006e447f5 | -8.997 | -45.855 | 2026-08-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.0 |
| ab89622f-80a8-36ef-b7b2-70b2f312b2f2 | -6.7123 | -58.9412 | 2026-08-18 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1dd254bf-cd4c-320e-be33-8ce5d5e78285 | -9.0349 | -45.8509 | 2026-08-18 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 03f63b2b-cf41-3b16-8b53-ced850ede29b | -6.7478 | -59.1716 | 2026-08-18 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| fc83ad28-f6d3-36e6-a144-f408bd126ae7 | -14.3529 | -51.9345 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 372be80d-966a-3b61-a4d3-596ba896f451 | -12.7789 | -48.4426 | 2026-08-18 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 204.3 |
| 5961e68c-84a7-3181-b140-235076f3b457 | -12.7793 | -48.4205 | 2026-08-18 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| efea7919-2046-3956-8712-7cb15411455a | -12.7597 | -48.4453 | 2026-08-18 13:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 3e24df00-0467-37d6-b1e8-761667d9fac1 | -7.2009 | -43.258 | 2026-08-18 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 16538728-47a3-31f6-a3dc-814ab1efa6da | -14.2566 | -51.9259 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 178.4 |
| cdb6061b-4fda-397c-9144-6ba5b37821f4 | -10.2765 | -50.4313 | 2026-08-18 13:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| de94bce5-100a-3472-88ff-8a0db273a462 | -14.2759 | -51.9234 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 4107e4eb-6c3e-3b6e-92c4-66a1028d3826 | -7.2007 | -43.2814 | 2026-08-18 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| 4dc3384e-b27e-38a5-a1a3-5f3febcfaf0f | -14.2373 | -51.9284 | 2026-08-18 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 536dc9ca-d4ec-3ac8-be59-a8d7c7c86a1a | -13.4117 | -54.3737 | 2026-08-18 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 726bd64a-915e-3812-b96d-62622ef76991 | -7.7881 | -47.8607 | 2026-08-18 13:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4bb3c598-5b1a-3fa0-aadb-2fa5f409ecfa | -11.3491 | -45.9292 | 2026-08-18 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 6213d464-2634-3740-bf7d-5ceb0fab627f | -14.4656 | -52.1112 | 2026-08-18 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 3f8aff20-023a-36de-84d7-85bdac7c3110 | -14.3525 | -51.9559 | 2026-08-18 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 1a0cfa89-0bc4-39f7-a3c1-1aff8d8f5e87 | -6.7478 | -59.1716 | 2026-08-18 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 1871cd3a-7ec0-364a-ac20-374d3b3b0076 | -7.2007 | -43.2814 | 2026-08-18 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 103a00a6-e5a1-36ff-bab9-690eb608d7b9 | -6.7814 | -59.7672 | 2026-08-18 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 1f1a1c30-b410-3504-a1db-41d7dfa0b2dc | -12.5207 | -47.8581 | 2026-08-18 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| e58210e9-b6c3-366c-b070-3bcbed7d6c49 | -13.568 | -51.6953 | 2026-08-18 13:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 186b3b63-a41f-3acc-bb20-7685b0a55632 | -14.18 | -53.0564 | 2026-08-18 13:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 248a9f20-5873-3008-9aa6-fae5858258d0 | -6.8411 | -58.9939 | 2026-08-18 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 648f9203-2b1f-3133-af62-68a5b94832fc | -6.7123 | -58.9412 | 2026-08-18 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |


[Clique aqui para ver as próximas entradas](README67.md)
