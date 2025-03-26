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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd2090dd-8ca9-338b-8760-451e5d6c8a5e | 1.52477 | -60.71045 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928ec7c9-8eec-32d4-af24-7a2485f6182c | 2.11006 | -61.82766 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d428f2d-6ec8-3860-a51a-93ac33e5da6b | 2.19552 | -61.81495 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee0e4c0a-629c-3136-a24c-d4943ae30860 | 1.33237 | -60.71541 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14a2fb80-63e9-39e1-936e-9c238418f4b9 | 1.83604 | -60.88194 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1667a710-e0ac-3b67-be22-e8b92e922ed3 | 2.11347 | -61.82712 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2140d04d-e056-3611-8988-ba733931bc7f | 1.73636 | -60.29205 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 35dd1723-6f6d-3a96-bfd0-55c344923910 | 1.82605 | -60.88349 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30a27533-1cc2-352c-90cf-a04410cd2532 | 2.19381 | -61.80397 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 234ccc76-2431-3444-9e78-3a1825fba8c2 | 1.38415 | -60.80658 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f29c4aa1-ef47-3aea-95a2-a4e409658a93 | 1.82495 | -60.87653 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d75e0ce7-d81d-3a7a-9fb7-de55054c33f6 | 1.83271 | -60.88245 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 02d2809a-0b0a-324b-8a0d-e221600fb18c | 1.11225 | -60.5418 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91307b01-3b69-3faf-b9f6-9c0fcc536baf | 2.11289 | -61.82346 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0054eff-e30a-31ca-823e-5111d3662eeb | 1.38748 | -60.80606 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b123f00a-ba98-3c77-a173-6a337b955fe7 | 2.19495 | -61.81128 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e3eee03-1f2a-3565-ad50-9680aba2aab1 | 2.19722 | -61.80344 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae33685f-2c86-397c-a6ad-e57d234aa1aa | 1.81884 | -60.88104 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f02d55b2-82ed-3c9e-a587-763974dedeb6 | 1.10639 | -59.34959 | 2025-03-26 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baa58bf4-8ed4-34d9-80da-fd0ffa51825e | 1.8355 | -60.87845 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b1c40e0-848c-36ee-b7b7-b376bb1db029 | 1.82326 | -60.88748 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| dd2819ac-405d-390a-ace7-3935b9f10aec | 2.19837 | -61.81077 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75fa906d-2349-34a0-9e6a-260b90720e11 | 1.82217 | -60.88052 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 16003d25-8f91-3e84-9deb-8716c9f3cc87 | 1.82441 | -60.87305 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1077d051-2146-35aa-8698-0674a2fff7be | 2.08637 | -60.83607 | 2025-03-26 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e0f726d6-dc90-3005-8ad7-a8dc338cc7de | 1.52809 | -60.70993 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c29a908d-45e1-3994-a68b-30fdc94087ed | 1.82107 | -60.87357 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b59087d5-e2b9-326b-84cd-10437336db26 | 2.10949 | -61.82401 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e2787d4-a313-3507-911f-41e9ffaed583 | 1.94919 | -61.19814 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94303b4f-c144-38a4-a9fb-b6e0b60c81e4 | 1.33292 | -60.71886 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d736ed6-60ef-3d94-9b78-a92268df015a | 2.19894 | -61.81443 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d6c285e-2e60-3d06-ab22-6447ee1db950 | -7.05848 | -44.37448 | 2025-03-26 05:40:00 | AQUA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 2be30e84-a0e7-3f02-854b-07a2b39d9a48 | -17.86003 | -39.85431 | 2025-03-26 05:44:00 | AQUA_M-M | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| f3073545-ea07-3d70-a0d4-c35a7dc5a01b | 4.65771 | -60.90967 | 2025-03-26 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d43f771-9da8-3690-8647-e12bae162788 | 2.31819 | -60.14246 | 2025-03-26 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2700335c-070c-3299-a4c6-450ae93a7059 | 4.09378 | -61.58916 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9366fd2-92e5-320d-b734-d2a22f7397d8 | 1.821 | -60.88591 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| dd0813a1-ea31-3b7f-a81c-3a63e61b4c99 | 1.83354 | -60.88394 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2905e533-5a69-3c62-b4f0-94fafc7e6da3 | 1.69142 | -60.99141 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8eda9e0a-78f5-3d05-b1b4-c843e914be87 | 2.61146 | -61.49775 | 2025-03-26 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 869d5c2a-94dc-3644-bb2f-9a0220d3c497 | 2.61201 | -61.50119 | 2025-03-26 05:50:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 53b573f2-9a0b-33d5-bd65-b6781d09c55b | 2.11364 | -61.82699 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76003aa7-81b6-39eb-87b6-c138777c12d3 | 2.17289 | -61.82061 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b7ee0abc-93b3-3eba-9526-71cd64b91d5a | 2.04594 | -60.75012 | 2025-03-26 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 20239eee-1cd1-3c67-a105-56df209acb6e | 4.07755 | -61.5868 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ea637d8-1d5d-3ce7-86b5-c98519b91e83 | 1.82518 | -60.88525 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f2af46bf-8dee-370e-8a44-5479f42882da | 2.10892 | -61.82257 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 710e2349-d513-309b-bb02-f8ee9b7dfa5c | 1.81915 | -60.87444 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 89f887d1-832c-3a1a-88d6-0d250625bdb8 | 1.32982 | -60.71705 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e91e3d3-e0e3-3e7c-b5ea-5364692668b8 | 2.19943 | -61.81117 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5286dd6e-98f1-3ecd-87e6-8adc523522f3 | 1.82038 | -60.88209 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 8a0d2204-fb75-3cfd-9b1d-ac62b7e4f555 | 2.56163 | -60.69437 | 2025-03-26 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 58ad8665-7734-37d4-814d-f046eaa40c9e | 4.09457 | -61.59395 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 39726ef8-95c4-3442-b84f-54cc573b24fe | 1.83231 | -60.87629 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5b1cf4aa-6323-3a4c-a20a-0f5d45d12d76 | 3.9755 | -61.50565 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ef37951-f72c-3872-bef8-cf8a2c148dfd | 3.98658 | -61.54887 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e0ace34-b8dc-394b-868e-d1f27750918f | 1.82456 | -60.88144 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0b76d7b1-3779-3cb0-8ca1-59cf3edf2207 | 1.38759 | -60.8051 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdce8b3a-4507-3459-927d-bec671aa5d15 | 4.65483 | -60.91706 | 2025-03-26 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 756aaf0e-5762-3f9f-ba74-2fc917f00b18 | 1.81977 | -60.87827 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c08ac890-7b46-3e1a-93d5-d7f6ed51c19a | 1.68957 | -60.99161 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e123c65-1dfc-36b7-ab86-b137a9718613 | 2.31383 | -60.14314 | 2025-03-26 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf6111de-0986-3193-8c79-abfb3fe9aff4 | 2.31502 | -60.14572 | 2025-03-26 05:50:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16b8720e-dd6b-3ae8-857d-31e00203b159 | 3.96303 | -61.50259 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5b6be88-d254-312b-9acd-b855995193ff | 2.05019 | -60.7498 | 2025-03-26 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c6859d5-2b17-3646-a390-14f402de177c | 4.65422 | -60.91338 | 2025-03-26 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f977b48f-6541-3cd8-95d1-884c90c5eac0 | 4.09219 | -61.57953 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36e39c25-5eb7-3aca-b2dd-4539a306bb48 | 4.65832 | -60.91341 | 2025-03-26 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d9e8aac-3b3a-3c5b-88c7-33d87a141d71 | 1.82395 | -60.87762 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 331a2337-3d2c-3c8e-8108-f66e7153143e | 2.16898 | -61.82124 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 987c8507-c9b7-3d31-9d31-941e77235587 | 3.99125 | -61.55313 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da6fb006-cdb1-3375-b7b5-051dfa902560 | 4.09299 | -61.58435 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26eb3f32-9d3f-37dd-9d46-2b06303c59a0 | 3.9827 | -61.54947 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b42f843-bfac-3218-a8db-bc012d62ff99 | 1.83293 | -60.88012 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 67904c3b-a143-352c-b7d3-e18a21dc647d | 2.19473 | -61.80688 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb6be8cf-8fdb-375d-9fec-10be6c8f839a | 1.83772 | -60.88327 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 916c9146-8336-37d4-82d0-876bac9e401b | 2.11284 | -61.82199 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 669c97be-7e28-3cc0-829f-9789afac938a | 2.19553 | -61.81185 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9284b40a-e67b-30e4-a5e5-ac79382bf08b | 1.82875 | -60.88079 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 91686f92-cc81-3d38-9248-705b08f675f6 | 1.82936 | -60.88459 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0cadc800-eacb-315b-bfd0-9ccd52f09db6 | 2.19864 | -61.80622 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a86215a-72bf-3523-97eb-1ebded72b38a | 2.10972 | -61.82755 | 2025-03-26 05:50:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4af5bf60-5a36-3c93-9984-5f67f02e2feb | 2.56101 | -60.69056 | 2025-03-26 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4375b06f-5b06-3a6d-9545-15d820c6e23a | 1.82813 | -60.87696 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 448dac9d-a619-3a48-8ffb-c3595f8d5b0f | 4.65546 | -60.92085 | 2025-03-26 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a53272dd-ed43-3289-9c5c-ebb7daa5762d | 1.82333 | -60.87378 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be0cb2f0-4ef6-3620-b6e9-2ae88d747f65 | 1.95073 | -61.19846 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fdcb797-9ba9-33e9-a178-eab611210a27 | 3.99045 | -61.54823 | 2025-03-26 05:50:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14af6e83-a7d8-331f-b09e-ab4a2ed9b718 | 1.83711 | -60.87945 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf03a8fb-f10a-3f39-bb2f-4396e9997be3 | 1.33407 | -60.71637 | 2025-03-26 05:50:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5c14e03-15bf-3458-8a14-ecc42664ec99 | 4.65894 | -60.91713 | 2025-03-26 05:50:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3a39bdba-5143-300a-968a-89d2236f9f77 | 2.57062 | -60.69688 | 2025-03-26 05:50:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b6eb198-4c6c-3659-8d36-8b253e4b628b | -2.63901 | -68.13892 | 2025-03-26 06:44:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d0c6709d-babb-3f15-80eb-48f5f3e6a332 | -8.97787 | -72.92107 | 2025-03-26 06:46:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6694dd51-a7b7-3a6d-b678-9e70c328dbc6 | -10.26478 | -70.51796 | 2025-03-26 06:46:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81a39bd8-d620-3c50-beaf-9e46fbbfe374 | -3.49787 | -39.57941 | 2025-03-26 12:06:00 | TERRA_M-T | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| dd9a943c-eb09-3e7b-9960-43c3b3cb9306 | -7.14664 | -37.62885 | 2025-03-26 12:06:00 | TERRA_M-T | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 10.4 |
| beb27d3d-4baf-340a-aaa9-743e95554957 | -4.80789 | -37.68337 | 2025-03-26 12:06:00 | TERRA_M-T | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 17.1 |
| d16f65fa-0031-31c4-b834-fc227e1a4ead | -6.04971 | -37.50148 | 2025-03-26 12:06:00 | TERRA_M-T | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| c1b7e4e9-9801-347c-a616-0c2d57ef2812 | -4.80938 | -37.67257 | 2025-03-26 12:06:00 | TERRA_M-T | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 28.5 |


[Clique aqui para ver as próximas entradas](README9.md)
