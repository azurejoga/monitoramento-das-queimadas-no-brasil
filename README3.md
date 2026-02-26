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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6dd4dc76-a4b1-3b2a-a449-18dcc5d9853f | 3.80624 | -61.7508 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62715ba0-9ab2-3175-bcd9-e071c0f9c580 | 3.12944 | -59.9741 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dc4f35c-d7f2-3f96-966a-fbd0a3f9f58d | 3.06195 | -60.0361 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 887a2ced-e89c-361a-aae6-4dd37c50d16d | 4.14543 | -61.09886 | 2026-02-26 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d732fa-6827-3743-8e1a-729a55508203 | 3.51564 | -60.30415 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e030a8e0-e42b-39d6-9917-182f58ec2e76 | 4.07155 | -59.89426 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2cb6d46-b7eb-346e-8261-5a60fc83d9ec | 3.04443 | -60.03514 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57a21994-9b2c-3769-aa8c-eaf9a226e4c6 | 3.05972 | -60.04389 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed6384c7-32b0-3e5a-abff-47e13d7bddcf | 3.72026 | -61.3564 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91211fba-4095-3940-a1b1-8b77490038f2 | 4.22313 | -60.11756 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6b6e9a9-a5de-3bcf-b8a0-6691b000efd4 | 3.11329 | -60.27193 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2cc8ab08-cb30-38cd-9e1f-064d996f9ec4 | 4.1308 | -61.07304 | 2026-02-26 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b377ae1-fd10-35d6-8c3f-af04f3559505 | 3.12224 | -60.26318 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 101f722f-a6ba-35f2-b248-6ecc91b11874 | 4.27649 | -61.32843 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18fe6871-bed4-3913-a986-8d0cd658f941 | 4.07611 | -59.90105 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e4380f0-baaa-38ed-9912-5f93fef8e07c | 3.51394 | -60.29349 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f852a6-cfd4-3161-a83f-22c46ee27e3f | 3.05914 | -60.04026 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45973c9c-cbde-3308-a88b-cc06aafb7f98 | 4.07553 | -59.89745 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aa1f5141-060e-35da-9069-624ca7c04e86 | 4.12749 | -61.07355 | 2026-02-26 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d7d80b8-8fc1-31bf-804d-76c338f95f97 | 3.04782 | -60.0346 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8a52d76-cd75-3f08-83dd-0f80b85c0a6d | 3.80954 | -61.75029 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 922c7af4-4960-3012-9c82-879de8e134b6 | 3.50888 | -60.28334 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97b375e2-ea5d-3988-ac66-b23e99a355c4 | 4.27979 | -61.32791 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89301d2d-da80-3f0e-8407-a454d2ec67bf | 4.10487 | -61.12302 | 2026-02-26 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c9a711f6-363f-30e1-9abe-2b74a4cba961 | 4.27595 | -61.32499 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d568349c-2022-3a82-8984-0713b1e9e74d | 3.13962 | -59.9725 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d9ac15d4-81eb-3c26-8b26-f6333e8d6319 | 5.04947 | -60.49875 | 2026-02-26 05:33:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47639fb7-5172-39aa-b6d8-d96f2f5d472c | 3.51507 | -60.30059 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b15887f-06ce-3363-b455-57b99dab73f1 | 3.1723 | -60.43487 | 2026-02-26 05:33:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1d1e5a8-cc6a-3c68-b9f1-1c3c78c1b0a1 | 3.64267 | -60.90931 | 2026-02-26 05:33:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f250951c-6cda-34c9-932a-6141a51fc2ef | 4.14989 | -61.02045 | 2026-02-26 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b45ff904-12b2-3d20-8569-7c5aec2dced6 | 3.48425 | -60.27993 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ca48128-8a44-3787-90ca-0d5a5b6d37c8 | 3.13622 | -59.97304 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57df6aa8-d27f-32c4-9d5d-9f4fe0a19ce2 | 3.11608 | -60.26782 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 863cbc35-d76f-3f45-b026-41ac7a97b15d | 4.28932 | -60.7646 | 2026-02-26 05:33:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c2f8ce8-c1bb-31c5-acff-f292490bd9a4 | 3.51899 | -60.30362 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07498705-b127-35e4-8ce0-9eb8cccb8790 | 3.13283 | -59.97357 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa7ca995-60fe-33d4-87bc-c90b55ee78c8 | 3.51286 | -60.30822 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd7ae8c3-39cc-3fa4-a737-cc470b5da895 | 3.11272 | -60.26835 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e55e979-c583-3856-a179-5229d5f09fbb | 3.51843 | -60.30006 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dcd0ee4-6621-3e86-81f9-2988a1d2c4d5 | 3.11945 | -60.26729 | 2026-02-26 05:33:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c48fa9ed-5b4b-3b63-ad00-899238568593 | 3.51337 | -60.28993 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94138b5e-cf8e-35f0-8602-0096af6beceb | 4.1532 | -60.29504 | 2026-02-26 05:33:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 077de885-9541-33ce-ae25-96c2e2579023 | 1.49633 | -59.94062 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd74fa9a-22f7-378e-bf95-1caee3927ac2 | 1.48705 | -59.92671 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4e28c2f2-8706-314c-96e9-882559dc9044 | 1.49453 | -59.92939 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b4f781-0989-3288-ae76-9b30dfa90066 | 1.94232 | -60.36588 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 757bfe96-ffe4-33aa-bd65-2936dfbb25c6 | 1.48928 | -59.91861 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc96a7a4-1244-339b-8dd9-a4f888fc4832 | 1.49169 | -59.93369 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a49e358-63ac-3c8c-8422-f853490866ee | 1.49348 | -59.9449 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40fce1ec-2679-3d03-a1e9-f139bf906c39 | 3.03214 | -60.06684 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bd23aa4-1ec3-3ee8-b69d-89f6d0243c6c | 1.47447 | -59.93634 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db74a0d3-51e0-3cac-ad17-bd92c26f4cb0 | 1.48885 | -59.938 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5364a9c3-ba61-311e-a09b-00d8880974c7 | 3.00456 | -60.14176 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34644d45-7452-3974-9638-2f9d28aa05c3 | 1.48825 | -59.93425 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6905d094-f2ff-3ca7-a302-62a678564489 | 1.94456 | -60.35814 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f32842dc-9264-3c4e-9d71-3ccc5a4d4980 | 2.07236 | -60.20888 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29423a5a-43fd-3e41-8afd-53901d8db42c | 1.83443 | -60.61056 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 606686ce-b615-32c1-90a1-fd80ff8a6b33 | 1.49752 | -59.94809 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beba186c-716e-3c13-84bc-31dc993c8ce8 | 1.48136 | -59.93531 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 539d83c8-6d48-3f8c-9275-9d6fb8971ce0 | 2.91007 | -61.22017 | 2026-02-26 05:35:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed12dc44-c673-35df-915a-2f7c79c67388 | 1.47792 | -59.93583 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecbded67-5d68-3193-bdca-8c8430350bed | 1.48765 | -59.93048 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 27b62438-1b8d-39c9-99dc-8b74a7f81ca1 | 1.93837 | -60.36281 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e808e25-daa8-3025-aec1-b2e7e4a4f6e5 | 1.49109 | -59.92993 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1440962-1412-3fea-8428-33eedc92eca7 | 1.48196 | -59.93905 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d6e6f87-3393-3f67-9a32-44b780410516 | 1.94175 | -60.36227 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4d7e56f-13fe-3931-ba84-31da3a9383a3 | 1.49049 | -59.92616 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0898b22-0d3b-35d8-aad6-ab5aafd614cf | 1.48016 | -59.92781 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1c35512-150f-3ea6-9ba6-d0305de14015 | 1.486 | -59.94225 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 673f9187-cab8-381e-aa8d-f0a9b1af61bd | 1.48541 | -59.93853 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ce13f974-4918-3874-b2e9-d5d1760af823 | 1.94118 | -60.35867 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d685ad37-f164-335b-92fb-18f7277be978 | 1.48644 | -59.92293 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 38021c32-1da4-3bac-b8ff-404164b33a51 | 1.83164 | -60.61465 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8df92eed-2db7-3590-9a75-ea2bcb02d5ba | 2.07294 | -60.21254 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e4f8697-2224-3609-923e-3d7a5f3677ed | 1.83107 | -60.61108 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3028d1f-468e-3980-82bc-95db093325db | 2.51614 | -60.02363 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fc17a46-f03f-3372-993b-34332350f1a6 | 1.48481 | -59.93478 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 853169c6-a13c-3bd3-8928-06dca72bf02d | 1.8083 | -60.46788 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebc0d10f-4a39-3d72-972e-ec4998d65160 | 3.03156 | -60.06321 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 848e4ea4-ef66-3349-bf3c-fd343ccd6361 | 3.03098 | -60.05959 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b17571d-7b8a-3ed1-a990-64a1dd957455 | 2.57233 | -60.55011 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8a25476-604f-3ff3-8ed0-ef8fe8ed43e0 | 1.49229 | -59.93745 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c7a1ac0-aeaa-3ae1-a6c0-16e1ecc400f3 | 1.4866 | -59.94598 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a9993fd-b08c-3fc7-ba84-da6d3e8b7c2c | 2.57289 | -60.55366 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5161933-7835-3fd4-8419-4809187af97b | 1.48945 | -59.94171 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ddcc680-2aa5-3c53-8db7-1212463b7f0c | 2.23417 | -60.71192 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc011de1-622f-354b-a45d-73a60026df4c | 3.02934 | -60.071 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 29184cf3-b59f-39b5-b452-f1d1c8ec7899 | 1.49289 | -59.94117 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e239bc04-e05d-3637-97ab-0567280db6bc | 1.96739 | -60.61181 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b548849b-3ccf-3065-a8f4-3c7f97b5e639 | 1.48868 | -59.91484 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70496f39-6029-3d90-b1c5-e21ad7c61e0d | 1.80773 | -60.46428 | 2026-02-26 05:35:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca21680b-c7e6-382f-a5a3-2bb66cc5aa08 | 2.576 | -59.93567 | 2026-02-26 05:35:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16204853-fd94-33b7-95e1-0a3b0ed2ec13 | 1.49513 | -59.93314 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70865729-3777-3785-9c10-370809004d63 | 1.48076 | -59.93156 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9861a1ff-c239-34ce-be95-9fb5ac63b7aa | 1.49064 | -59.94918 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ccbc01f-10ea-38bb-9bfe-7fe28baddd99 | 1.49004 | -59.94543 | 2026-02-26 05:35:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68d74432-e9df-36a8-890f-18f8ebf99dbe | -10.3622 | -58.59302 | 2026-02-26 05:37:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 333d337b-88a0-3207-9bc8-50794aaa517a | -10.68562 | -59.37389 | 2026-02-26 05:37:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ede4355e-7ad2-3090-bf87-d619e05f8ee1 | 1.4864 | -59.9308 | 2026-02-26 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.4 |


[Clique aqui para ver as próximas entradas](README4.md)
