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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2f3f5e7-0e05-34a1-aca2-b2d81baf63dd | -11.23645 | -45.26005 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a0de1238-deed-37f5-8971-ee8651c77dee | -11.27732 | -45.51922 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ca024a98-d94e-34a5-a78b-5ff72bbf8877 | -5.11183 | -45.4458 | 2026-10-06 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c3f0f30-2c5f-3087-b971-6f1ce1587abd | -11.2974 | -45.51705 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4bccfdd-578a-345c-bf9f-5e3597283b4e | -5.23107 | -48.39849 | 2026-10-06 04:19:00 | NPP-375D | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1d2270e-7aa1-3579-95a9-55ef203db78c | -3.09864 | -53.72925 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bdadbdc2-7725-316b-8f07-8158c23b86f5 | -4.35605 | -47.77977 | 2026-10-06 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66fd4882-d8c8-3ce7-9865-d5cd0802a3c8 | -2.77416 | -54.10152 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f2dab95-2b73-338d-a795-a6fa7fc2b7db | -3.09076 | -53.73423 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c10f2a43-20e1-3073-b815-29135c6ad45d | -8.70123 | -45.20681 | 2026-10-06 04:19:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5547010-e0ac-37e0-9b6e-b94c271d55a6 | -11.28597 | -45.51916 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 800c561a-9a76-39b5-91ae-d83298b0f270 | -4.19157 | -44.26429 | 2026-10-06 04:19:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d51d7e-9e78-3d0d-9446-c24de89bf262 | -6.31682 | -43.34586 | 2026-10-06 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ada123e6-d25d-31eb-9301-6a7f720ac196 | -5.96682 | -41.36352 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7f7375b-1f8f-3080-a1a5-b60ba81a59df | -3.15733 | -50.43608 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7150f168-766b-31b8-afd8-0506e0268d25 | -3.11009 | -53.7067 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72e33bf3-29cc-3959-b9c7-2f7e89c4bb14 | -4.45843 | -54.96158 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 523ee527-e1dc-3213-a4fa-a08b0fdfbb0d | -2.99984 | -54.13076 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 28a10111-0fb4-3bb4-a3c2-18fd1b993cb6 | -3.23569 | -53.87659 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fe707d5-09f8-3919-8e7d-f687869a03d2 | -3.0939 | -53.71557 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d987c0ae-3820-31ac-a763-4d8198e83709 | -5.02952 | -43.56701 | 2026-10-06 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74ee941d-5f96-3fc0-98f1-ebc89eb3674c | -2.77676 | -54.11282 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 327cea21-1d39-3d5b-b546-fc74af52a578 | 2.45983 | -50.83313 | 2026-10-06 04:19:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 10a32c53-9640-316a-a00f-6e7132b29caf | -10.70512 | -48.54567 | 2026-10-06 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67da2600-afbd-37f9-8625-57cfe4ddc46e | -3.22771 | -53.88173 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04681c97-d9d7-3c9c-b1ee-0cf2ddd146e0 | -11.26864 | -45.50494 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 178e067a-2207-3f54-8ae4-0cf3f48ad1bb | -7.34055 | -44.37853 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3702c90d-c2e0-36cb-b900-8603706f579e | -5.75281 | -46.68121 | 2026-10-06 04:19:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 07518502-719e-3cad-93f9-47d961058e15 | -7.89828 | -44.18599 | 2026-10-06 04:19:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec91f090-4826-37b5-95cc-49443bc1f59d | -3.2761 | -50.4025 | 2026-10-06 04:19:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26930857-ed62-3fd6-b0a2-48a4856fd293 | -6.18982 | -44.85884 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 961448a3-4e35-3154-b3b5-4cb6f0a978da | -3.46708 | -50.10183 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19082a0c-e876-371c-849b-856ed60da28a | -4.2686 | -48.62643 | 2026-10-06 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e312084c-9391-3442-912c-a3c81c7f6e8d | -5.84616 | -45.01933 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 9a55ae73-3cfb-3156-a1ee-bbe26c9d0a0b | -7.01571 | -43.4492 | 2026-10-06 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10403682-28f7-325b-8a54-3b3ac9f391fd | -3.2278 | -53.87879 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f0c7859-6c05-3008-bccf-4ab9973b1d19 | -7.28974 | -39.3184 | 2026-10-06 04:19:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eb4aad7c-1118-3c39-973a-db4c847b7c55 | -7.2144 | -39.64299 | 2026-10-06 04:19:00 | NPP-375D | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e9812c42-ae7f-3606-8791-88c0724e2a8f | -2.8887 | -54.15882 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f798d245-5ce1-34d1-b277-6eb06c01e1cb | -5.97785 | -41.31546 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15579e60-9a20-3841-90fc-5b1ebd4111dc | -3.32393 | -53.85664 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea25ac6e-9241-3f54-b84f-e50e0d534f2e | -5.97675 | -41.32241 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 13a6942c-29f0-377e-bd4a-c46bb46080f8 | -2.78118 | -54.10278 | 2026-10-06 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4a20e7ac-3bcb-37b6-8a32-20f44a682d16 | -5.67333 | -42.59061 | 2026-10-06 04:19:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 116b6f2b-6b0e-3a34-b381-2941bb4433f7 | -3.58133 | -54.3111 | 2026-10-06 04:19:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 74f0b6d6-a6df-3938-9a4a-742df9de1765 | -6.85468 | -41.80036 | 2026-10-06 04:19:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81484a2a-5ff2-3010-8253-064336dc66b4 | -5.19099 | -48.31309 | 2026-10-06 04:19:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e471a94-7026-33b8-ba08-040495bb7deb | -7.25539 | -48.06718 | 2026-10-06 04:19:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2091fec-fcce-372a-aaee-cc308918fdfb | -6.92267 | -43.681 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8982993f-99b8-31dd-aadf-a5734addafd3 | -6.44839 | -43.82645 | 2026-10-06 04:19:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0e512695-0cb0-3e00-aae3-9e6b066e3da4 | -2.95543 | -54.15013 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1e367015-7eb2-35c7-93e6-3691353f8cc0 | -11.26946 | -45.52212 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 7fc48f80-3d13-38b0-96a6-eb3639f16a4e | -9.88259 | -44.80392 | 2026-10-06 04:19:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b9087f8-1943-3b49-a8bb-58732f2572f7 | -6.87985 | -43.68177 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94bc179d-a696-38ef-bc1f-a5f73bd2499b | -11.27015 | -45.51798 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 36645d23-9c2d-35bb-82b9-5f661338c64e | -5.94681 | -41.31767 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e1aae3d7-bdba-37f4-9526-c1a2af611103 | -6.58454 | -41.58591 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ae96ec46-a489-3661-aa25-11958ee4a0a6 | -6.00189 | -53.51006 | 2026-10-06 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6cf931f3-2e05-38d4-b71f-a490a68e2196 | -6.88331 | -43.68233 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b1127e2-7839-34cb-b695-6ac77bf7f1c5 | -6.91921 | -44.56244 | 2026-10-06 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fc3f7e5f-5d08-3cc6-babc-00c12ad0b2a8 | -2.97993 | -54.1339 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46a90c65-72fe-37fe-8f3a-e4484eac18ce | 3.31645 | -51.33898 | 2026-10-06 04:19:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dee466fe-d3aa-384c-8702-35c5fdd8d98d | -6.60447 | -41.54642 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 24487419-7b5d-3c3e-b42f-c8a5b201df06 | -5.88939 | -43.4557 | 2026-10-06 04:19:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6ceb6bac-6b70-3652-8727-a2737a06e724 | -10.97316 | -45.41547 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcdea1d1-482a-31d1-bea1-4a59e0834151 | -2.80138 | -54.13765 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24f359dd-d564-37ed-8f09-cd892827d9d8 | -6.88678 | -43.68288 | 2026-10-06 04:19:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d507f15a-fb53-3d4b-a5ea-7288156474c4 | -5.02888 | -43.57092 | 2026-10-06 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90a4d34b-ce5f-31f1-aa2d-62c93f26bad7 | -5.97014 | -41.36404 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85e4f1c3-e6c1-3beb-ab42-e72713c608cd | -6.60544 | -37.88929 | 2026-10-06 04:19:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83eb764a-4d13-3ba8-b270-3665d8991166 | -10.97492 | -45.41507 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5eb2c043-1802-372e-9e3e-196842b92392 | -11.65853 | -43.66117 | 2026-10-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b271345f-5017-3961-bbfb-87cbda75a05d | -11.26506 | -45.50432 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| af46c166-53dc-3c51-ad54-1aa299f45e74 | -7.73128 | -45.46421 | 2026-10-06 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee7f3517-5660-3b58-92d7-0255a95b7e25 | -5.95186 | -41.37182 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b55235e6-c199-3b1c-ac09-65da3c17c76a | -7.47654 | -42.80115 | 2026-10-06 04:19:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ea9b43d7-b483-3bdd-a4e0-9588e2c2b657 | -5.84194 | -45.01616 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4933f87f-f602-3737-890c-db9057c1e85a | -7.33635 | -44.38194 | 2026-10-06 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4dc9ef2d-07ed-3d81-a994-1da12aa3d9d1 | -11.27291 | -45.50143 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| e85834d7-434c-31cd-98a7-28486f8a2582 | -2.87525 | -54.17181 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4479b5e2-250e-3d30-b798-e63e10d868ce | -4.46396 | -54.97847 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8360ceca-0e16-373e-bc23-b9b934f197a9 | -8.58707 | -45.66231 | 2026-10-06 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a63da640-722f-3f1b-b8fd-860f263bf46e | -5.47102 | -41.22816 | 2026-10-06 04:19:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 084d8ddf-c321-333a-b9ea-4194066d8b46 | -5.42748 | -43.44645 | 2026-10-06 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf9688e5-7a64-3eb9-919e-0f3ee0e401e8 | -6.19278 | -44.86376 | 2026-10-06 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23a3e472-15f2-3332-885d-d066d74a3bdb | -6.6209 | -41.56679 | 2026-10-06 04:19:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2dcf6ec1-cb1f-33ba-a40b-621b896ca2f2 | -5.84989 | -45.01997 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6db1698e-833e-37a6-9808-363e7aaa6bd5 | -3.64956 | -54.05645 | 2026-10-06 04:19:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77486d5a-879d-3dd5-9699-fcbb752e7ad7 | -5.0666 | -46.10906 | 2026-10-06 04:19:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b8ee23-46c0-3c10-a5d6-023ce322572e | -11.27305 | -45.52274 | 2026-10-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 62cefe2b-2c62-3487-a196-38e126aa61ee | -5.84242 | -45.01873 | 2026-10-06 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 02ede4f1-b42f-30ea-95ba-ee8c495844ae | -3.71553 | -48.88047 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36aa8797-a56b-354f-82c6-f538fe055bb8 | -2.9403 | -54.15387 | 2026-10-06 04:19:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e0d75c34-46c0-32fc-a89d-204179d06ef1 | -6.13331 | -43.50577 | 2026-10-06 04:19:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2bf955e-381b-39b8-9e29-8081a173c152 | -3.05945 | -54.24594 | 2026-10-06 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fe348d09-a863-3418-bec5-a8c2188ab354 | -4.11491 | -49.39834 | 2026-10-06 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 175d55a9-7e94-3e13-851a-8f319a6067ba | -6.80393 | -41.2435 | 2026-10-06 04:19:00 | NPP-375D | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fa59e1b-b39c-33e0-bca6-98ae048cd7ad | -4.45811 | -54.96975 | 2026-10-06 04:19:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9fef13a-97c6-33db-a2bc-f81a60936a4f | -3.83799 | -50.30973 | 2026-10-06 04:19:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57a846aa-261a-35f3-909f-8b9547a43c4c | -6.82324 | -38.53522 | 2026-10-06 04:19:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README26.md)
