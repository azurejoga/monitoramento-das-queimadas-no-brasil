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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ac36135-c4d0-3989-b8bb-dc7b9f61c6ef | -8.52908 | -54.82802 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| b733aa4d-8375-3488-8fbf-b83b177d2e7b | -12.10324 | -56.31719 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4a553d11-6e9a-3059-a9ff-df33b5d0f9be | -6.56036 | -58.51129 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e27a99b-2fdd-33fc-bf42-eae01f2bde86 | -7.02456 | -59.55135 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8007a8ae-f449-3cee-8a74-0afe580d3b40 | -6.80927 | -59.6659 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 099825c6-e4fc-3817-95f6-35c209cd1394 | -6.43693 | -56.18142 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05937ff8-859e-3b07-96d4-f0822e1eb2de | -7.3746 | -59.95625 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b59d4ee9-470d-3a19-bcee-616e4e3a8197 | -13.25699 | -51.61075 | 2026-08-22 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0ea5fa82-3324-321a-b666-017aa2335767 | -6.79926 | -59.45123 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d01a6636-7fbf-3692-b12e-a6a687dbbe1b | -6.90459 | -58.99979 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fa6b7d59-84cb-3f37-a854-2fd03df896c7 | -7.05384 | -59.83645 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2aa6d1e1-90e4-33f2-9074-e423f0788921 | -6.15944 | -55.44694 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f88fdbf-e086-3ae6-b91c-70b78d0699dd | -4.47064 | -55.39281 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cf5608c6-38eb-3ee2-9736-9714835e58dd | -6.20832 | -55.63951 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddaf125a-5cb8-35fd-b44b-b5eb723ef5a2 | -6.81645 | -59.66348 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f1a30033-8911-3dbd-a413-a46fccf35255 | -6.79896 | -58.63414 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 671ec1d3-24c3-36a6-924d-d3f96f1bd116 | -6.02451 | -57.6828 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02fad8fd-84b3-3a7f-9c82-99c72d983bf1 | -6.26605 | -62.52514 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 08574fc2-4ebb-3918-832e-9ebc6affd0b8 | -6.90569 | -58.99286 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecee09df-7b9d-3af0-bd84-3e80ea00c823 | -6.77774 | -59.41588 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 297f019d-f0c6-3717-94be-3d2f549c9864 | -10.83913 | -57.51808 | 2026-08-22 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a8624c4-1a1c-3c3a-bf3b-d84df78762b5 | -7.41712 | -60.03105 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48ff3e7b-7a77-34ae-b6ed-2b605fd999cd | -6.37833 | -54.9502 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dd72f6b-7d12-3da1-bb11-79cc304e0eb0 | -6.57939 | -56.52993 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98906c4e-c60a-3aac-a2ca-99fe58433eb7 | -6.79649 | -59.42595 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| f4e47855-24d9-3218-b31f-54fa4feae9ab | -6.37434 | -54.94262 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0735707-aa43-329b-bd00-0034629201fc | -5.91318 | -61.29867 | 2026-08-22 05:23:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ab50f9a-8294-3447-acc8-c868a908df03 | -6.77446 | -55.70308 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4b0177c-445e-3f1a-a1c4-139fc74e29dc | -6.76716 | -58.66484 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 34e6dc48-e20e-3cb4-8793-734070eb72ea | -6.79484 | -59.43634 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3f61aad-ce8f-3ed8-a72f-c080137a386e | -6.86763 | -59.4479 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea01f076-8a7f-349e-912b-b076a9768640 | -8.5878 | -54.7195 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 796a4c7d-b16f-352a-b46a-4e2f4f38444a | -5.7943 | -57.54414 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fae51c04-1970-3515-ad67-622114daa0c5 | -8.53111 | -55.33342 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a49de61-7127-3dad-9a3a-1a568fc749fe | -6.70685 | -58.9398 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47cdaa1d-5c56-3ce2-a109-06ed0f544f9f | -6.56985 | -58.96811 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c1e7adf-93ba-30f2-bf46-f116c110269c | -6.08322 | -59.95724 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 339bf13d-1055-30b1-9e32-3c7a944bcffd | -7.01355 | -59.59926 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c920e0-324f-3018-bb7e-26c0442484de | -6.37905 | -54.9455 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59a20b1d-e2fd-3f63-8cc3-54dc4eb56d95 | -7.59709 | -60.94476 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8755a108-9c2c-37af-ab09-ec632bd48839 | -8.02472 | -51.80268 | 2026-08-22 05:23:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c52184f-a0a5-364c-9bb2-dc7ffcf9bcb8 | -6.79842 | -58.63762 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84819ed3-8897-3d33-a739-af99c0ddeb90 | -6.79601 | -59.59979 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 588d53c2-fb41-3ff0-87a7-6ff26d9bd82f | -6.78932 | -59.42836 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e371d455-1da5-3e8c-a461-1b46fe9c8556 | -6.93099 | -59.3055 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca003912-8d32-3819-9816-2a0fa1567246 | -5.79993 | -57.55241 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bdda5b76-1ba6-350f-ba21-fb95d11b9fc4 | -6.86494 | -59.03612 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 496a40d2-f084-37b0-a1eb-1b182e53dd5c | -6.41736 | -52.73233 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29221864-fe4e-3a14-89ec-9b4de67117d5 | -6.89361 | -59.43435 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e717e46-d4b9-3427-9df1-adb97ceb50a0 | -8.15854 | -55.37597 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d82b2452-e2eb-3a47-92b4-69bce335d1c8 | -8.55749 | -54.7183 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3ff4e214-26c9-331f-9b31-61959f1dbb40 | -6.63427 | -59.0773 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a94f4f54-778f-3fb0-a074-28e2f56b6a6e | -13.25657 | -51.61414 | 2026-08-22 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| de3392c6-568b-33b6-8939-e8b2de923256 | -6.85216 | -59.41705 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33037c5c-3c3f-367a-a755-0f4767ba6fae | -6.38827 | -54.95428 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d7dd97ef-0573-3633-809d-3abd2b23bd32 | -11.16968 | -54.00394 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0936da50-9d23-3e83-ab66-beea9ad4905c | -6.76771 | -58.66135 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8edea8dc-a0b0-3397-a919-044c2711ef2b | -8.52028 | -55.32684 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f61f8d2c-928f-3413-b6cf-cb3d4a1f0b90 | -6.43218 | -60.07082 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42c91b6a-dccc-3a0c-928d-7adc1ceffe32 | -13.69173 | -51.84645 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 282b6a6b-01d1-3292-89e5-4fccb8c10153 | -6.84942 | -59.43436 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed0a4033-4fd8-3af6-9361-03fab77bf59e | -6.71574 | -58.99088 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39bf03b1-dc3b-3a8a-a2f7-667c9a47759a | -13.99185 | -53.69373 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4de4303b-ae5f-3b6b-ae17-41e697d47326 | -6.81258 | -59.66642 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ec2589c-51f8-3db2-b897-667dd4859124 | -8.53855 | -54.81884 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c09a9d34-1124-3753-8970-a25817084646 | -6.86156 | -59.44339 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 533f6ad1-7d7e-36d4-a403-8aefdeb02efd | -6.7109 | -59.08586 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df4d7e2b-a4ac-3349-98ab-901e90815b53 | -6.81302 | -59.40729 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7cbc62a-dd10-3f8c-99de-2bac532b8f61 | -6.80956 | -58.9986 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4dac7b2-6628-3651-9e1c-93addae30419 | -6.94974 | -59.31557 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0a12341-b3f8-3057-b5a4-c2223bb89974 | -14.31329 | -51.86757 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85c301c4-4cd9-33b2-b105-252e651ca0f2 | -11.20511 | -55.05201 | 2026-08-22 05:23:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 776b4c1b-fe6b-36df-bbfd-0ab0b1541269 | -6.08932 | -59.96179 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ef55241-6f6a-3b11-912e-ddd966e42033 | -6.79796 | -58.98612 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92648dd3-5d6c-3a7c-8b71-3bd6ea16d13a | -14.97329 | -52.65818 | 2026-08-22 05:23:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95dc95b0-c226-35a6-bbe2-9e888868b293 | -1.74592 | -55.24817 | 2026-08-22 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49f5611d-48f1-35e4-b08b-4dd815097d7d | -6.78766 | -59.41745 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| f4b830b7-b30d-38a4-b25a-9ad27c3eb731 | -6.0139 | -57.79478 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83ec84b8-44da-32ef-b0fc-3cd31fc59f86 | -6.76722 | -58.70761 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7ec99c2-cf73-3b8b-88d8-f88b71f9dcbd | -9.17502 | -59.44231 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 167af3fb-8f9c-33fe-9bb0-af3bb367bd44 | -8.89884 | -60.60119 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4015fce-0ab1-3940-86db-fd01b6baa66a | -8.68392 | -54.74438 | 2026-08-22 05:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02055211-c4da-31e6-9daa-198d5c39602e | -9.1811 | -59.44686 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09a239a0-8b6a-3b53-afdb-4ef2637f9e4f | -9.44516 | -51.59909 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4862445c-6e9b-3e00-a827-576fb3ed4485 | -9.4398 | -51.60105 | 2026-08-22 05:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cab45137-a51c-3537-8565-1caea07ec1a9 | -7.75081 | -61.08167 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7822dfb9-d1ef-3d98-8237-c21f4d633fd9 | -10.52066 | -50.77549 | 2026-08-22 05:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5cdde6e8-9e6b-30ee-9885-d4370d6bdd88 | -7.67112 | -61.11776 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1884801-620a-3b18-ada6-84908e44c365 | -7.67393 | -61.12198 | 2026-08-22 05:25:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 717e2d76-8cb9-33b7-9846-4292d1512d09 | -7.87334 | -63.74794 | 2026-08-22 05:25:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13a60f4b-f3c1-3b24-9acb-e628f4ea1a53 | -8.89941 | -60.59767 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 724de0e3-bac1-3aac-b1c2-7c339e96f9dd | -10.51197 | -57.60092 | 2026-08-22 05:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 577199d4-2b6f-369d-9c74-deecc48a8993 | -8.38993 | -62.69075 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52b63528-acf2-333f-a0d4-d81ee8ff95e0 | -14.50137 | -59.8301 | 2026-08-22 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3f2242e-ed01-31e7-83a9-4c2a30456c67 | -16.49982 | -55.18945 | 2026-08-22 05:25:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| abc38924-dc73-3d27-93de-229fe7d0d0ec | -15.34189 | -52.92789 | 2026-08-22 05:25:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30d2a378-f467-35db-9536-691c755a5d0b | -7.88705 | -61.71127 | 2026-08-22 05:25:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df9ff8f1-6b71-35a2-b54b-6aeef364e928 | -9.24582 | -59.63931 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c05554e-1ca9-3d2e-b934-f5e38bb99caf | -9.21055 | -59.77644 | 2026-08-22 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00d64e2b-08a4-3c57-8a4e-d807620d6345 | -8.40856 | -62.68959 | 2026-08-22 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README71.md)
