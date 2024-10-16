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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fcee6eb3-7ec0-3276-87bc-0ffcc19097f9 | -4.06479 | -54.02303 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d22bd408-8d0b-3b2c-9ae1-1e7faac65782 | -4.06406 | -54.02737 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19e99e30-9a52-3f2b-8a68-e1edeac2c01d | -4.06291 | -54.02491 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91691c06-2f0f-3526-b52f-b53f824bc581 | -3.82693 | -54.2351 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9c4fdaa-9aa3-3984-9c9e-bf9965b733c4 | -3.82688 | -54.23232 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 478e63ac-0eb7-32ab-be1f-b8f2e70f5208 | -3.71931 | -54.20246 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11cb2ee0-9812-3501-8ed3-8f2b9f95659a | -3.71861 | -54.20518 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 02d2e93b-67fb-3e71-9cf1-353757e9f398 | -3.71853 | -54.20729 | 2024-10-16 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f407a373-b65d-3a47-8247-c0623a9dc925 | -3.62539 | -54.67042 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0d43d840-8e42-3a1b-8098-11a3aa6114c3 | -3.62452 | -54.67554 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de69c95f-4f25-3fc1-b687-43b6640f4614 | -3.62418 | -54.67299 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 69252a0b-a4fe-32e4-8451-1f0ee61e635d | -3.62025 | -54.66713 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd184391-2004-344f-bc0b-a8db4f897661 | -3.61942 | -54.67225 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b772341f-0abf-3188-aa67-e666da2d5440 | -3.60462 | -54.73312 | 2024-10-16 04:29:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c8bf233-8c3d-3d63-9791-1bc6c2e14dcf | -4.80745 | -55.85145 | 2024-10-16 04:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a6f487d-02b4-3a3a-abda-416b6f38a463 | -4.80701 | -55.8541 | 2024-10-16 04:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 82a27d37-30cd-3fb6-ab1a-f6c1f4d01c3b | -2.33548 | -49.10906 | 2024-10-16 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa69fd5f-5a2c-3527-9160-5fc18e5bb96c | -10.28464 | -42.38456 | 2024-10-16 04:32:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f9dd247b-e032-310a-a64a-6b3256eab96b | -12.79304 | -44.24057 | 2024-10-16 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c017fc6-c9b3-3f61-b57f-87cef7e163b9 | -13.87816 | -43.79272 | 2024-10-16 04:32:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39964602-1fe3-3bc8-9b6b-421c090f7ed5 | -13.94121 | -45.82748 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e4a3a64-03cd-3529-aca0-6212efaf34e2 | -13.94001 | -45.82474 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5d269f8-6742-3382-9a43-20dcb877e7b4 | -13.9375 | -45.82693 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea1e2623-eb0e-3be4-8c40-c438595ba253 | -13.93379 | -45.82639 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc7c72e5-5061-3081-880b-e4fcd36773df | -13.93314 | -45.83091 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3ddeb04-7956-349b-8c97-c311c2493f12 | -13.93074 | -45.82131 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4b9f4e44-a4a3-3ccf-8b9c-f61c0c5ea1ab | -13.93009 | -45.82584 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a956420-1771-3700-8351-3f13b97dcb20 | -13.92879 | -45.83488 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afdb08b8-d048-330d-8299-cfead0a90c2d | -13.92638 | -45.82529 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65403262-aba9-3bc1-b8a3-29b327ae2036 | -13.92508 | -45.83432 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a741af30-0701-347e-823e-a3b482d4c47d | -13.92267 | -45.82473 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de10f2ee-631f-3401-b5ce-11c648291068 | -13.92202 | -45.82925 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1df02971-b6d7-35db-98de-fe7b95727a81 | -11.10651 | -45.90971 | 2024-10-16 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 991c36d3-7efc-3a6d-b7e1-a1c516c483dc | -11.10293 | -45.90915 | 2024-10-16 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1af3c5b7-3c07-3e65-8102-182dbc9a2b0f | -10.72807 | -45.20954 | 2024-10-16 04:32:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b57be10b-753f-3166-a1b0-99f04e296959 | -11.52451 | -49.07357 | 2024-10-16 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d17b5fc-09ac-3755-b2d6-d2b2a243f4ef | -8.00169 | -40.59279 | 2024-10-16 04:32:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 53f59b04-4d70-30bb-871b-3f20dd6f823e | -8.00127 | -40.59496 | 2024-10-16 04:32:00 | NOAA-20 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 758db821-5e95-3f4b-be70-a2c62607bd3d | -7.60517 | -42.21969 | 2024-10-16 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4365c0e4-4b7e-32d7-a735-453b9a127e06 | -7.60458 | -42.22377 | 2024-10-16 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2c37f7b5-4545-32ab-8654-1290939a8dae | -7.60089 | -42.21918 | 2024-10-16 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c98c6f3-728c-3004-b6ad-92cea4020ac0 | -7.6003 | -42.22327 | 2024-10-16 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ec946b2e-4b85-3b5a-a6a0-5da1d94b1918 | -7.54999 | -42.24076 | 2024-10-16 04:32:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60c73bbe-f65d-3719-83a8-487debc4e92c | -8.18953 | -41.00051 | 2024-10-16 04:32:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 0df71e77-4ddf-3d43-a0c5-a9f130cd48c2 | -8.18886 | -41.00539 | 2024-10-16 04:32:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| b5467938-08e8-3bf9-b680-c8fc387db8df | -8.18486 | -40.99979 | 2024-10-16 04:32:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 5a5940d8-dce7-38d3-b9c0-7a3b19ad383a | -8.18419 | -41.00467 | 2024-10-16 04:32:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 99949b93-af7b-3dd4-9fc1-014fc1d85ca1 | -7.73389 | -43.20028 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a0cfb686-2e64-3761-b078-bb0a54478dff | -7.73339 | -43.20382 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 847b7cb6-ec2a-34d3-8415-3480fa730c1c | -7.73289 | -43.20732 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 756dbf4b-1288-3b4e-bdef-8faa7d89bfaf | -7.73239 | -43.21081 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1c4a4cfd-dc4b-35d1-b2f6-5bad0a1330dc | -7.7309 | -43.19254 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| de48b881-7b56-3bd2-8616-737f1712134a | -7.73039 | -43.19612 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e43a95d9-988c-321e-8d11-8f24f8729305 | -7.72934 | -43.19236 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df740f2a-64b7-3ee7-b7b7-6167c8ae8226 | -7.7288 | -43.19594 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b65c0e9e-70c2-39ed-89b5-d25f1c220818 | -7.7269 | -43.19193 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a851e8b7-c8d8-30db-b957-0f3ac706e5f4 | -7.72608 | -43.28377 | 2024-10-16 04:32:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 491bbbe2-1b93-316e-a528-5aa3468c4c11 | -7.72259 | -43.27975 | 2024-10-16 04:32:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 51f4d8a7-fd92-35ae-9eeb-06b5385b0f06 | -7.72152 | -43.25863 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b0d8676a-cbc3-3436-b768-49759f8bf1a6 | -7.72103 | -43.26212 | 2024-10-16 04:32:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d4c23b92-e093-302c-9dc2-a7055d67aec8 | -7.18751 | -42.63505 | 2024-10-16 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 45655025-9a7f-3d98-9981-1eac4baeb4fd | -7.18179 | -42.64561 | 2024-10-16 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 030d64bc-4596-3ba0-afc1-76bb678b0bbe | -7.18126 | -42.64929 | 2024-10-16 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a6c74d7-4356-3cd8-ab8d-eb83ed632673 | -7.18074 | -42.65295 | 2024-10-16 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8af32a48-edd8-3a7e-916f-aa89878c3ef8 | -7.18021 | -42.65662 | 2024-10-16 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59580081-5fa0-3b04-8551-638c06eb0f5d | -9.33921 | -43.21143 | 2024-10-16 04:32:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 56d03550-84e8-3f8d-9f3c-df8d24cb7f59 | -9.26569 | -43.14002 | 2024-10-16 04:32:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8505a5b9-4174-32ab-b293-003a088b07a9 | -9.11884 | -43.09719 | 2024-10-16 04:32:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 90472f48-92d4-36e3-a0a4-33a52e0de072 | -8.45333 | -42.47353 | 2024-10-16 04:32:00 | NOAA-20 | JOÃO COSTA | PIAUÍ | Brasil | 2205359 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6ee79990-3e93-3d28-96ad-beb521b5fdef | -6.97976 | -44.67379 | 2024-10-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 47e9ddda-40f3-3963-ac1d-6dd436a0c3c2 | -6.97851 | -44.68223 | 2024-10-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3758ab8c-7d50-31c5-8d90-f25d3a7120d4 | -6.9779 | -44.68637 | 2024-10-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72afffc7-4547-3af1-ad61-d8371c9c9dcf | -6.97613 | -44.67317 | 2024-10-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a7744cf5-4303-3ebe-b190-2707d398e598 | -6.97489 | -44.68161 | 2024-10-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c963cf38-66b7-3141-995d-5061109fb09b | -13.92138 | -45.83376 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc721fd3-5791-31db-b2a5-3841f58d525e | -13.83808 | -45.58035 | 2024-10-16 04:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f934338-effe-3828-b3df-1d78dad1a679 | -6.83887 | -46.05814 | 2024-10-16 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 56fb0cf3-4dc5-3e38-a5b8-80b55e385760 | -7.60433 | -46.83892 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 570a5d34-3b85-3bef-8e12-eb1733094c8b | -7.50493 | -46.8602 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e77dc924-634e-35d0-82fe-83010b5494a9 | -7.50439 | -46.86375 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a529235-969e-37cc-b2d2-bb13f6d43b05 | -7.44273 | -46.78093 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1745c2a-57f7-36f5-bc46-5b38cfa6f2bf | -7.38411 | -46.74707 | 2024-10-16 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a844a55-af00-3e11-9def-3163003d13e7 | -7.20726 | -46.26024 | 2024-10-16 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72d5d059-dcb2-385f-a1d0-9bdb0d574fe3 | -7.20329 | -46.26342 | 2024-10-16 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4dc6bc9-48c5-3be4-bbff-ad73dd928772 | -6.80156 | -46.47831 | 2024-10-16 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abfa57be-773f-32e1-a67f-4f4586fc4c2a | -6.79763 | -46.48138 | 2024-10-16 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eec8e7d8-d05d-3f27-9ae7-6151d2757916 | -6.79649 | -46.44432 | 2024-10-16 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3b8c009-3f59-3768-b314-44b1a385856b | -6.58709 | -46.37143 | 2024-10-16 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d78079c1-31c7-350b-9f3a-f2ba6ca43347 | -9.18178 | -46.995 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b8662488-9c76-3207-b6ce-0977b2f47df0 | -9.17678 | -47.02757 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3281db5-ea8c-3bed-afd4-74eea6e1a421 | -9.17107 | -46.97477 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20b76ae4-e8a1-30f9-ac38-7925d7311e74 | -9.17051 | -46.9784 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4831d7d-c2c0-369c-bfe7-3f939f30a51e | -9.16996 | -46.98202 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66f3508a-e8f2-358a-9e59-687d14e26a9c | -9.16769 | -46.97425 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2c459df-9a88-30aa-a7d6-f5a627f62f79 | -9.16714 | -46.97787 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e75f2ca1-51e3-3911-963b-8ae24ddf1ce4 | -9.16658 | -46.98149 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8bf0ab23-12fd-3a0d-8961-d25e95dc060e | -9.16603 | -46.98511 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 71873ac6-0936-3bc2-9d37-38d219e0f5e8 | -9.16376 | -46.97735 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec0799cc-92e0-33a5-9f95-74ba88521d23 | -9.16321 | -46.98097 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a006f47c-901f-3f03-a789-8e6fd195743a | -9.16266 | -46.98458 | 2024-10-16 04:32:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README50.md)
