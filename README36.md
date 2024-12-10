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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44c8f91c-c99b-3cab-bc3b-7946ff046273 | -10.02425 | -53.75337 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ec6bf02b-5c22-357e-8431-b3f2c000c6bc | -12.71285 | -54.97299 | 2024-12-10 05:18:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a360ed3e-83f6-3090-8c42-863812b54530 | -12.56522 | -57.76662 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d54e6b1c-eba6-30d2-926c-e0cf3a50b511 | -12.54031 | -58.34261 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e72caa5-79d0-3c2b-b4de-10a687403759 | -12.91783 | -55.72906 | 2024-12-10 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 30eb2459-840c-34df-a629-52d097df16a4 | -12.53587 | -57.72091 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e69b030f-4d53-3f1c-9b3e-856252bab9d8 | -11.82667 | -57.82241 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fa42c50-2df5-3c1e-b85d-29ab4405d701 | -12.55354 | -58.34855 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d30bd8e1-d0bf-32f3-8636-b9761a15b785 | -11.41606 | -54.32225 | 2024-12-10 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6b44693-b530-3081-8741-5d36af2f9b53 | -12.85743 | -51.93788 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86fcfd17-9a9c-366c-b31a-ad894194e4f7 | -12.85706 | -51.94091 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa63258d-f161-34f2-9ff9-df2267990328 | -12.24607 | -52.44758 | 2024-12-10 05:18:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f24184d-93db-3631-85e9-91da57358d0d | -11.4203 | -54.32291 | 2024-12-10 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51532427-18ca-3ce2-a854-14fe1e5dc1e7 | -7.89992 | -61.52246 | 2024-12-10 05:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7b127a0-4fff-3251-9093-d22a4e93d5db | -12.5589 | -57.71205 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 87659f47-c026-3f4d-9fb0-0057a1acddae | -12.14778 | -58.15107 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fb46d6c-45ea-3719-8bb2-ba8edc31a416 | -12.55758 | -58.34523 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7f741c67-1d6b-3645-abf8-72298fd2beb7 | -12.3726 | -54.16009 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 680bd632-328e-3ce5-a83f-de22d2515ca8 | -12.53821 | -57.72953 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfad8392-eb69-321f-955c-b086367aa333 | -12.54548 | -58.35518 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44d78f1f-9aba-3e88-a1ad-e9d5a4dfa7bc | -12.53526 | -57.72495 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e233159-dd75-379d-aa4f-e10a6655d541 | -10.02857 | -53.754 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 82cf6658-5bf5-3d09-9daa-34f594e7132b | -12.36654 | -54.17225 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f56f5676-1e6e-3c11-8afe-4d4fe7dff9b6 | -12.57177 | -57.76626 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84721c6a-cb68-3d64-bdf1-0396bfcbcee1 | -13.75075 | -53.28305 | 2024-12-10 05:18:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7840fe7f-0184-375b-b019-12af82f7c5b2 | -12.56159 | -58.36548 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3b6dc4a9-f4d9-385c-9265-56e0df03fc24 | -12.16054 | -55.17251 | 2024-12-10 05:18:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5555084-4fb3-31b6-a830-7a2db98564b2 | -12.91711 | -55.73425 | 2024-12-10 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55fe3b39-873f-3d7a-a12c-1e81e3144675 | -12.86189 | -58.21661 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1775e91a-8d21-3918-9df9-3a3200d7a833 | -12.56217 | -58.36165 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 54ab913e-407c-39b5-998c-f3362df572fa | -9.20557 | -62.43409 | 2024-12-10 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2344824b-fd48-3bad-b82b-3cc4e7144812 | -11.72146 | -57.44069 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c32f1e-42b8-37a3-b225-0f5caa50f435 | -12.56875 | -57.76716 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3148c6b3-a63f-323e-a68b-4ee2dfe68d7d | -12.5376 | -57.73358 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0e8bc76-b9d9-3d5f-ba4e-6ef788489af4 | -12.54318 | -58.34698 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4223c230-cd7a-38a0-8c31-577644488c84 | -12.54721 | -58.36717 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 04b6150c-006f-32d1-afba-8a018d0bc7f5 | -11.65862 | -58.2733 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aec75f1f-01cc-3703-9d1a-4622056d2295 | -11.78293 | -55.12699 | 2024-12-10 05:18:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a345546-a5e7-363f-9d58-fea959f9e6a9 | -12.37696 | -54.16068 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 732a30c0-53c7-32c8-a684-e36058a07096 | -12.8527 | -51.93413 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37845428-186d-3f43-a7a4-419d8d0fee38 | -12.37203 | -54.16436 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f0a1a2e-69a6-3b98-8225-cb12c0cae2ef | -10.02601 | -53.75301 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| cbb4ba20-f11d-32aa-83de-78c9d8fc383b | -12.55067 | -58.34419 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 2179523d-c0eb-379f-8529-ba2c3b7f5292 | -12.04549 | -62.79113 | 2024-12-10 05:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf51486c-03be-35c4-b790-9f0c56669606 | -12.16409 | -55.1767 | 2024-12-10 05:18:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ae3ec6-0fdf-3e4e-87e4-60be9d5a2ed4 | -9.71626 | -54.88819 | 2024-12-10 05:18:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30fb21df-9fd0-3100-99f7-a15afc159a83 | -12.8567 | -58.22768 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 338c16c5-5020-34fd-a56f-918cf71df4f7 | -10.35718 | -57.25216 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21e8f781-7146-306b-87ce-29bd0e4a30b6 | -12.37146 | -54.16861 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7473cb33-53a4-38b5-b024-ed980e9d82da | -10.03033 | -53.75363 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 92ca0e1c-d152-3627-a925-d5070748ee77 | -10.38333 | -52.00414 | 2024-12-10 05:18:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bfee0b85-947a-36ae-a347-9e2a9d6c52e3 | -12.86132 | -58.22049 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3bdf3cf-8b69-32eb-9448-18a474302939 | -12.15182 | -58.14778 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c02553f7-8fa2-34ff-adb6-5b06c8208d8b | -12.55066 | -58.36771 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c28d50d-6cac-3413-aca4-49ce32abd85d | -12.14836 | -58.14724 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53fe144b-f497-35c0-b570-3606f0ac941e | -12.85308 | -51.93105 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b4e80c3-b2b8-3469-a6f8-6b72f9090595 | -7.93026 | -61.55497 | 2024-12-10 05:18:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ceb28d1-b024-30df-aefe-4e761571f18d | -13.48247 | -60.35049 | 2024-12-10 05:18:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d345eb0b-be34-3985-8b00-e9b5c63f6215 | -12.90382 | -55.05338 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1083686a-bfd5-3ec6-a987-a2092a2f2d77 | -12.55411 | -58.36824 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 599cfaa6-ab19-36a0-a43c-140cffb4c66a | -9.82968 | -54.37185 | 2024-12-10 05:18:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2242d3f4-904d-3bad-9a65-e509e0756189 | -11.41551 | -54.32622 | 2024-12-10 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fafcbafa-a92a-3c69-aaf2-f403a6f5a980 | -12.56936 | -57.76311 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 560a678a-2293-3ae7-87c8-07b79a3bc5b9 | -12.53347 | -57.73711 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e76cbed2-e3cd-3303-ae82-1a3c73105bf5 | -10.38191 | -52.0033 | 2024-12-10 05:18:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b45c909-227b-39b1-aba8-1ad56096e083 | -13.32039 | -52.41391 | 2024-12-10 05:18:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c99baa78-38a0-3225-b86a-f2ca86492571 | -12.56446 | -58.36983 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fbc18ce3-4838-356b-965c-96f4d53db77a | -12.53283 | -58.34533 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 67e2635f-d52b-3240-b4db-ccf4f2992f97 | -12.54491 | -58.35901 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8ed08fac-180d-375c-86bc-34cbd75c616e | -9.14731 | -62.72041 | 2024-12-10 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88c5f3b2-8831-3e52-80b0-4f88b0be1184 | -12.54434 | -58.36282 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ded60943-186e-3f2d-9380-acdd759b8218 | -11.66262 | -58.27005 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76280979-b95c-354a-9979-b298fca4b9de | -12.55929 | -58.35729 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f7517a0d-ca3e-3a3e-8fed-f3408e094199 | -10.67813 | -55.92308 | 2024-12-10 05:18:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98d8fc2a-95fa-33c6-b4be-8bc29fb91407 | -12.53701 | -57.73763 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 901007fc-e016-3dc2-90d6-90da3073a589 | -11.69183 | -57.44454 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19dca75e-08ca-38f7-8a1f-6ffc0933f5d0 | -12.85781 | -51.93481 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2b20e09-ab32-38f9-b20b-fd408179ae88 | -12.90795 | -55.05402 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d021aa15-2cc4-3de4-9b27-6c8c1bfd19a9 | -10.02917 | -53.74985 | 2024-12-10 05:18:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9afc9786-b054-3c1a-836e-5af06aabaf1e | -12.16003 | -55.17612 | 2024-12-10 05:18:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29c0458f-eb73-341f-91be-5c9eb29427ad | -12.56101 | -58.36929 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34e30943-46ce-33ee-8186-bbba3e753d4c | -12.91259 | -55.0509 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fafc8316-50c5-3c20-8923-a633629d2444 | -12.85784 | -58.21997 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 480b6e09-4661-32ed-98c2-4da41cd24569 | -12.54261 | -58.3508 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 607c339b-ddd9-3a07-9f56-1bfc4ee570df | -11.14925 | -54.22911 | 2024-12-10 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aab192c2-3063-31a6-83db-bf51796b2644 | -12.55987 | -58.35344 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb8ce539-0bfa-3e8b-9e2f-e4fd57415f71 | -11.82144 | -57.83364 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1fb4a9af-17e3-3dc5-8d04-52acfcb0bca8 | -9.39562 | -62.57324 | 2024-12-10 05:18:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fa92bd3-6390-3fbd-afcc-620ce6a04f84 | -11.20412 | -53.81943 | 2024-12-10 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7055c066-e77f-37fe-a649-7da4fa8af282 | -13.02639 | -57.21544 | 2024-12-10 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d83f3588-d229-3ded-a91a-bcec5dc07a91 | -12.85727 | -58.22383 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3de964b-c86e-36ed-bf72-9bd33b563fa3 | -12.85819 | -51.9317 | 2024-12-10 05:18:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d986ec4d-6945-3328-bc8a-820ea2b2a73d | -12.53881 | -57.72548 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1efddc80-48a3-32c6-b0d6-71a32e6bc60e | -11.81852 | -57.82918 | 2024-12-10 05:18:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71f902c0-72cf-3f11-8aec-08ac0f89929b | -12.04616 | -62.78716 | 2024-12-10 05:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 039f5ffe-058f-33fc-a16a-e3f9d3fd9ce0 | -12.16105 | -55.16889 | 2024-12-10 05:18:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbfc365f-404b-3d38-8b3b-95e6f1db8c46 | -12.91208 | -55.05466 | 2024-12-10 05:18:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa2e1d2-34f6-362b-a4ab-ed076085d280 | -12.04265 | -62.78656 | 2024-12-10 05:18:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42a06f72-9351-319e-a3db-f1393be1c2db | -12.54376 | -58.34315 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1e95ef30-0e2d-359f-94b4-2bf1a53184aa | -12.54054 | -57.73814 | 2024-12-10 05:18:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README37.md)
