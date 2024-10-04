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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac94b373-f4af-3dbe-9a95-318e10447200 | -4.44869 | -45.16004 | 2024-10-04 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4772a88c-a153-3a6d-b1de-769944e76bec | -6.35752 | -46.51163 | 2024-10-04 04:08:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8f5635a6-c401-3d29-ba5a-56dc07c29f65 | -6.33277 | -45.68592 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d812ac8e-4ac8-3932-a7eb-f2490d1764f2 | -5.1109 | -46.13677 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9600950f-3477-3373-84fc-e402c5c7abdc | -5.10632 | -46.13963 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca188576-f1d1-3790-b2e5-3e44a38f1555 | -5.10572 | -46.14322 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6f66a760-8de0-304c-8398-b61f7336744f | -5.08982 | -46.11583 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 48986854-6c2c-3b14-9566-993c830952d0 | -5.08922 | -46.11934 | 2024-10-04 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42b333c3-59ad-3a9a-b686-c4b1e90c8360 | -6.09314 | -45.95098 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1818b396-5fc8-32f3-b8ae-753e6fbb2ee5 | -6.09184 | -45.95278 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27cf33f2-70d4-3297-98f5-70124e2f5b69 | -6.08925 | -45.95041 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32f0f79d-dcf9-3f8b-a2bb-f4f2716d4f77 | -6.08619 | -45.94488 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fc87f21-9c0b-3cf3-9e94-aac5db001a00 | -5.97496 | -45.38147 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43643b33-b28f-3f08-b213-fc08f72c3f1e | -5.97196 | -45.37631 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0e11acb-65f5-3e8d-b91b-fafcc9144aa3 | -5.97119 | -45.38088 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3163587c-0662-31ec-b43e-8417e76171e5 | -5.97087 | -45.37831 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 84bc1d42-da9e-39cc-9676-9f6656c239c2 | -5.97043 | -45.38546 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9c27e665-b9d7-3d4d-9140-67d27757da85 | -5.97013 | -45.3829 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| df7350fb-8259-3a13-b7d2-ea2322d57b93 | -5.9694 | -45.38748 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c4a28d0e-c3ae-30b8-837b-0b73e6fdbe72 | -5.96819 | -45.37576 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c6c8d98-8f58-3d65-992e-23001abb87a0 | -5.96743 | -45.38031 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7491afad-afb1-31a3-b3ac-9504bd765f7c | -5.9671 | -45.37775 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 12a06d8a-aafd-3f88-a052-591db40abc7e | -5.96666 | -45.38487 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6a76ff76-30f8-3289-9cf8-5aee9c76194a | -5.96636 | -45.38231 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fdd74454-d4fd-30e0-beec-956485049e38 | -5.96563 | -45.38688 | 2024-10-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e1f9c981-fbd7-356d-821c-e91d84b7a470 | -5.90111 | -46.23373 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba7309f2-bee2-38eb-bde4-f67d69f460ea | -5.89375 | -46.2785 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a834e4c-97ad-3ec4-8c3a-1a21668a8246 | -5.89318 | -46.28197 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7eb95eb6-c63c-3649-bf9c-796b7140bb11 | -5.79471 | -45.08749 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4f8e4b8-fac2-3be3-a25e-4356f438ab8c | -5.79288 | -45.08445 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 89a6b066-2966-3b69-8362-c0a980b1ff47 | -5.79216 | -45.08891 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6d7a889d-3d52-3d35-8e5a-3e7bc884989c | -5.79101 | -45.08688 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b68d0b8b-65eb-391d-8735-455ebd554c92 | -5.79026 | -45.09133 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a9798d2-8a06-3a55-a5cb-ddf460f53900 | -5.78845 | -45.0883 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8e145481-8b65-3479-ad0c-14ff83a7da14 | -5.71875 | -46.40484 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c780f3-c68b-3fc1-a717-5f54839c739d | -5.71816 | -46.40838 | 2024-10-04 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b2e40c4-37c8-3ec6-b4aa-e1f851b12887 | -5.59893 | -46.37264 | 2024-10-04 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14ea95f3-d218-3f40-8a73-d86259a0330f | -5.57797 | -46.31557 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bfe144c-8f06-36a3-8fd5-db2c55802885 | -5.53977 | -46.19883 | 2024-10-04 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 611cbc63-b3ce-3751-a37b-4455a1670091 | -5.40507 | -45.08662 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bde081a-c910-3371-9fa0-9b43bcc58ebb | -5.40133 | -45.08608 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d6ce21a-ff25-35d4-9993-e7eed17a66d9 | -5.30117 | -45.1734 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22e2f1e5-6f4c-3635-91d9-bfe30b065c06 | -5.29741 | -45.17282 | 2024-10-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e0723489-b756-3e54-b209-e32b18c4cf60 | -7.91137 | -46.42673 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2bc8b2cc-254a-34ca-b13a-fd9ee0fb3a0e | -7.76296 | -46.15504 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| eab9c482-874c-3c83-a801-c039c39d1675 | -7.76214 | -46.15998 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 694b4636-136f-328d-bcbc-b3c3e32099d0 | -7.75912 | -46.15439 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e6dba113-9793-3bda-91af-aa1002628005 | -7.75832 | -46.15925 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 47df004e-6fbd-3ead-9f1b-ab8ea053137a | -7.75528 | -46.15377 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5096bea-c603-3242-94be-7338564a1bc4 | -7.75143 | -46.15318 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87ec40f3-45aa-3fb5-bbe3-1d850b294162 | -7.74836 | -46.14795 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 38853624-4a01-393f-ac85-9b9ae7049e49 | -7.74758 | -46.1526 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcf31a6d-b131-31ee-8a9e-aa0c888e381d | -7.74374 | -46.15197 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef527390-a48e-31f6-a42b-18da414526a2 | -7.73456 | -46.13609 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a228660-e869-3f22-a0fb-92f4d6665170 | -7.70826 | -46.15152 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bde029e1-1494-3d8f-9eec-f7ce2500edea | -7.70441 | -46.15094 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45e3a126-63eb-384f-93d2-90b4f2f3cce9 | -7.69975 | -46.1551 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14bf6ea4-86b2-3de0-bb00-9fffa3695081 | -7.69726 | -46.16973 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f467099a-3eba-3c23-8bf8-5356c1fb894b | -7.6959 | -46.15451 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2befb763-f807-30df-83c8-16e862d53e14 | -7.69508 | -46.15933 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6713ee5a-7400-39a4-9114-266400771f02 | -7.69348 | -46.15665 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f43e05c3-b8f1-30b7-b6f1-aabf333516fb | -7.69341 | -46.16911 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 427f6efa-1068-34b4-80f0-c77fde683984 | -7.69204 | -46.15395 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fbf608bc-82be-31b1-b53e-f892719814a6 | -7.69189 | -46.16639 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f528ac48-0e04-3426-b802-80b0e440b989 | -7.69041 | -46.15129 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e627c40d-8519-3bdc-9432-9306300171c1 | -7.6904 | -46.16359 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b93f2af3-246b-3ecc-9067-d89ee9842fa4 | -7.68956 | -46.16851 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9177090-92ee-3b29-8fe2-c4c1a6563a1f | -7.68804 | -46.16578 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1d4c7404-000c-305f-ba8a-cb948d458448 | -7.68654 | -46.163 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a8bcb33-68e1-3664-90e4-d91d647a4c88 | -7.68498 | -46.16032 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 096a4be0-f755-3088-85b6-9cb011736437 | -7.68419 | -46.16517 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 530d7890-683a-3d6e-81cd-66c02e2cc012 | -7.68268 | -46.16242 | 2024-10-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 723b4d2b-9bcb-3969-b469-5734b545a7bc | -7.33226 | -46.70859 | 2024-10-04 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8f0164b-ab87-3966-8d27-e864ef90f6d7 | -7.21404 | -46.66627 | 2024-10-04 04:08:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b2a006d-76a9-3f32-b91d-eb93925fd7f2 | -7.8162 | -45.46615 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90e17a53-910f-3b0e-84aa-f2fc5c36ead7 | -7.79122 | -45.46328 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06e6a7c8-426c-3ebf-8371-12aab0daac37 | -7.73802 | -45.41856 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9162bafc-ac47-307d-a9a3-48ca9764f5a9 | -7.73728 | -45.42303 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4db560b9-cb8a-3620-9fc6-2943d46e00cf | -7.73361 | -45.42231 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c4d35dd-7d3c-3557-87a9-dd32c4e69a25 | -7.71147 | -45.41891 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4c21358c-3956-3a5c-af82-8f7f38929d1b | -7.70777 | -45.41837 | 2024-10-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b83b2704-1574-38ad-8c4a-4934e3c4d178 | -7.6274 | -45.54292 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 546358d2-baa2-3334-8d24-ff0dac304884 | -7.62667 | -45.54731 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| df860075-18f7-34ff-91c2-6e23ed7ae577 | -7.62594 | -45.55174 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b9f143be-0ba1-3782-81e1-a7b4aa75eba5 | -7.62441 | -45.53797 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 283e95e2-e500-30da-a3de-4adadda325d7 | -7.62368 | -45.54234 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 7723dce6-1123-3987-88ae-c31eb4b7f589 | -7.62295 | -45.54674 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 8f3a0a47-a367-302f-ab94-8cf669bd675c | -7.62222 | -45.55118 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4e8d71b1-2ec0-307d-8bc5-07de81c0ca3f | -7.62069 | -45.53737 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| ef1d09da-6104-33c5-9524-80911ba2d367 | -7.61996 | -45.54177 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| c8be2b53-9f0c-36cf-946f-39dd5062f367 | -7.61923 | -45.54618 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 36d2a1cd-e43d-34f3-8cfa-d44b1361e177 | -7.61849 | -45.55063 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3b14d2a7-ff12-3cf4-8e5e-3fc6e35960eb | -7.61697 | -45.5368 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a4e3ac2c-393a-30f2-84b8-54f2aa12e0c8 | -7.61624 | -45.54121 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a9f76fcb-60ab-37c6-888f-43aa86e7c47e | -7.61471 | -45.52747 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 49c433b6-6c99-3fd2-b173-ec10a4e9b5b2 | -7.61252 | -45.54065 | 2024-10-04 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 04f7f295-ed73-3dc0-a69f-4207205e7e60 | -7.22481 | -45.59948 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 645a5d66-7c99-38d3-ad95-4c526de757c6 | -7.2218 | -45.59433 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 987a873c-8ee6-3135-9916-d77b9a2eb10b | -7.22106 | -45.59891 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7e3b0d37-fefd-3324-a211-d0fa6b884cfa | -7.16647 | -45.48813 | 2024-10-04 04:08:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README62.md)
