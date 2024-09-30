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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07aedd73-06fc-3bf8-90c8-cfdc15230173 | -21.86121 | -48.3777 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 08ccca7b-0c73-3714-86c4-cb8a442d2b24 | -21.85673 | -48.37328 | 2024-09-30 03:47:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d3550a7-445b-397c-ac40-b373c76f641e | -21.62831 | -47.78339 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0b48cbcb-f7ef-3d15-b755-dc379e1cd628 | -21.62764 | -47.78653 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4b8e6a8d-6f83-305d-b468-c4759292b5e6 | -21.62698 | -47.78966 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 46ff5930-c361-31ac-a890-5402170bfa40 | -21.62631 | -47.79279 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87d0dcda-9960-37ec-ae18-61af0dc0ef62 | -21.62564 | -47.79593 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d28814a-54f7-343f-bb25-4f631b5d4a22 | -21.62335 | -47.78202 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c343ad0-e59f-3608-b48e-7cd13c396de8 | -21.62268 | -47.78511 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ab59643-a658-3b8c-aae8-7f61de684509 | -21.62202 | -47.78821 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ea3293f-68d9-3725-a7b6-d6bf56e72d00 | -21.62135 | -47.79137 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ddae413-7a29-397b-87d3-dc6b4879b123 | -21.62068 | -47.79453 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34963174-e708-3184-bdc6-f3debfe083ee | -21.62 | -47.79771 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f137bc6f-29da-332b-a8bc-aedd95f53d33 | -21.61932 | -47.8009 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3beb41d9-b72e-316e-97bd-576c09f4c26c | -21.61863 | -47.8041 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b950f3f-19c5-347d-9a55-efe020b2d786 | -21.61837 | -47.78069 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a0f3675-6c13-32a6-93bb-f0e77c9f4d70 | -21.61795 | -47.80729 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b772146-fb69-37df-baee-99fa11766f83 | -21.61771 | -47.7838 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b27dd58a-370f-3b81-9fc7-ad56846e5b7b | -21.61727 | -47.81049 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7f9c7b88-9c3a-344a-8255-d0cb8b7c29c3 | -21.61659 | -47.81365 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1783eeba-215f-3537-a249-b5a3a8a02066 | -21.61568 | -47.79327 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2a2b47e-4491-36f6-a970-c98b38e1cd12 | -21.61525 | -45.58825 | 2024-09-30 03:47:00 | NOAA-21 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 13cd69dc-3c2d-3139-95a0-66b881e32878 | -21.615 | -47.79645 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5903a41e-ab35-31ad-8c47-379d2814ea26 | -21.61432 | -47.79966 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fddbb99e-fed8-3854-b200-2305abfeff37 | -21.61363 | -47.80285 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fd58502-e84c-3eef-9043-242a7f715c17 | -21.61295 | -47.80603 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 694bc303-d56d-3863-a60a-2b88c329e384 | -21.61227 | -47.8092 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e69f2c4d-b721-3b26-a08e-0f0e8b549af3 | -21.61215 | -47.73618 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 021d4975-9128-3e91-b70c-afc874938111 | -21.6116 | -47.81233 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 7.8 |
| db28ca28-fe16-32bb-85bb-71f953d38c69 | -21.61136 | -47.78887 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25631b03-23fb-3065-8079-b8269665bfcb | -21.61068 | -47.79205 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e6487ff-70d9-35dd-afd6-11617c93e744 | -21.60999 | -47.79524 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6cf821e-0a50-323f-8670-f31408894b3c | -21.60931 | -47.79842 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5925a146-6840-3abc-81cd-f2e7817dc3f6 | -21.60864 | -47.80156 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e33237b8-62f1-31a3-8ae0-73e8354767e4 | -21.6072 | -47.73478 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee15b378-c722-3bd7-ac48-afd16f80950e | -21.59663 | -47.73513 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8daba785-88c5-3e0d-8ed9-fd5f895e1699 | -21.59315 | -47.75124 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d94da234-86fc-3a9b-bc5d-db1aeb5d8562 | -21.59098 | -47.73697 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 469b572e-2e12-3e82-be8a-d9fe4a7996cb | -21.59028 | -47.7402 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ac7765b-70dc-3ed7-82f6-d786e65c40d3 | -21.58959 | -47.74342 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d459ef44-6454-3fa3-945c-1d74ad041652 | -21.58818 | -47.74992 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35e2edad-708e-3dae-a34e-880ef9489d89 | -21.58748 | -47.75319 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36622af7-f053-3994-9c57-38ec4e23fd02 | -21.58678 | -47.7564 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01043a6e-ef4d-3d70-a227-bb3be48276ed | -21.58428 | -47.79234 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6e2522c-9e0c-3968-92df-94d40e404a34 | -21.58362 | -47.79538 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 173b48e6-085b-33f2-8d7a-243094e94051 | -21.57063 | -47.78239 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6af8507b-0017-35db-bc69-8540cd3881b0 | -21.56996 | -47.78545 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be6b8b66-e7cf-37b0-96d5-f7bae2249f83 | -21.56433 | -47.78712 | 2024-09-30 03:47:00 | NOAA-21 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e17bbd8b-6821-3069-be1a-5854a2d5aefc | -21.47175 | -44.67514 | 2024-09-30 03:47:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 28a66ff4-c065-3831-90e0-a0d363a93c3d | -21.47095 | -44.67926 | 2024-09-30 03:47:00 | NOAA-21 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 641687b5-fe07-3a2c-894f-c1e66ad34ce7 | -21.37279 | -48.48749 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9887d100-d9bf-3a77-a08c-d40a859ae290 | -21.372 | -48.4911 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bc555273-dc6e-329d-8bd8-c10dce62180c | -21.37121 | -48.49474 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 71d12a3e-6999-3fa6-878b-62b8dca3d95b | -21.37043 | -48.49834 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5abe1fa6-f9f1-3894-a4ee-220f47d2873b | -21.36965 | -48.50193 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8333d2cf-f30d-3cde-90bb-74781b5a4719 | -21.36603 | -48.49312 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9ae71310-8388-34aa-8c69-153ef8ed9b0d | -21.36527 | -48.49661 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cd14b56c-7bef-3700-8543-d1314600e7b2 | -21.36451 | -48.50014 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 54f04326-ff16-3c9b-b99c-8672bdd6a4ac | -21.36374 | -48.50365 | 2024-09-30 03:47:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 16a5ecee-984a-3391-910a-450e866ac7cf | -21.32049 | -49.42376 | 2024-09-30 03:47:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| af17412f-fee2-30a3-aa3f-8f36bb243d34 | -21.31696 | -49.42365 | 2024-09-30 03:47:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| b626e7d5-138a-3f97-b707-9d3edb6dd70d | -21.31013 | -41.73267 | 2024-09-30 03:47:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a8195bd6-cdee-3536-8c36-0c432385ee08 | -21.29131 | -42.943 | 2024-09-30 03:47:00 | NOAA-21 | PIRAÚBA | MINAS GERAIS | Brasil | 3151305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0663cb6e-1768-37a7-b25c-68c5732d95e1 | -21.25549 | -47.65191 | 2024-09-30 03:47:00 | NOAA-21 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fcdfcc5f-7444-35d1-b747-2810ce824746 | -21.25432 | -47.65269 | 2024-09-30 03:47:00 | NOAA-21 | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80287062-8ad3-3ccd-9bfa-15a2903a3a3d | -21.18032 | -43.97954 | 2024-09-30 03:47:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f46123cb-8a0f-36e6-9ea8-ded20eeb8406 | -21.09089 | -45.85508 | 2024-09-30 03:47:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85d07c91-e549-34a7-9847-d2f8b92c19d0 | -21.08542 | -45.85891 | 2024-09-30 03:47:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 48a16d65-ebfd-3bdf-8477-f40d3227f34f | -20.84668 | -42.6428 | 2024-09-30 03:47:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 885ec69e-2198-347e-bd0a-79dde1d8091d | -20.84473 | -50.4181 | 2024-09-30 03:47:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e93cff97-8aa0-3eb9-a99b-de5a49ffe659 | -20.84295 | -42.64207 | 2024-09-30 03:47:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 58a4f3c7-0a6c-3a83-90c4-16220357ce3b | -20.66361 | -42.2856 | 2024-09-30 03:47:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50b03db8-7317-339a-bc03-276718d21eb8 | -20.65994 | -42.28489 | 2024-09-30 03:47:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| da2b5ef0-b068-3e86-be0f-729889c720f7 | -20.63794 | -48.74655 | 2024-09-30 03:47:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 12732364-cdb5-35dd-86ed-0a5a59aa84a9 | -20.63714 | -48.75016 | 2024-09-30 03:47:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 41a5ff7b-a051-393d-bb57-bba622563b84 | -20.63635 | -48.75376 | 2024-09-30 03:47:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 3bc82a0c-3fbe-35fd-a0de-cdf3b0fea96a | -20.6325 | -48.74535 | 2024-09-30 03:47:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| bb966b8c-08cc-3927-bb03-725826ad3e8c | -20.63169 | -48.74904 | 2024-09-30 03:47:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 56e41b6b-2189-3869-9229-7c8c1a1cbe25 | -20.63089 | -48.75268 | 2024-09-30 03:47:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.2 |
| 33d75e8b-058a-34ac-8d19-e1785e2dd464 | -20.60666 | -46.24471 | 2024-09-30 03:47:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d08a555a-d2ec-305f-9cca-64eed328adc8 | -20.60577 | -46.24908 | 2024-09-30 03:47:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7a20af73-cb1d-3cd8-91fb-cd4509d0f46a | -20.59625 | -46.24815 | 2024-09-30 03:47:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bc6ede7-cad8-3826-85a5-5b886dbc9aec | -20.49824 | -43.78055 | 2024-09-30 03:47:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8ca178d2-60b8-3794-896d-c8359d5076df | -20.46957 | -47.00506 | 2024-09-30 03:47:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 023e9415-ff2e-3c7a-b1d0-c2cb2622a52d | -20.43891 | -42.00167 | 2024-09-30 03:47:00 | NOAA-21 | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2af113da-1bef-30aa-ad7a-5cc18193765f | -20.4328 | -42.33397 | 2024-09-30 03:47:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d75fdf82-3d34-34e4-86e1-910fdeed5afe | -20.41826 | -43.55518 | 2024-09-30 03:47:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ce9f504a-2d9c-3b3d-b5c1-771766311411 | -20.34424 | -43.86367 | 2024-09-30 03:47:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 68b2a349-ea9b-3285-9771-f1539ffb4f09 | -20.3402 | -43.8629 | 2024-09-30 03:47:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b3d9bdf8-aa51-379f-bc0b-e0bf490f029e | -20.32478 | -46.64841 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a741c96e-a9c4-35b4-983e-844be4bb5d1c | -20.32348 | -46.65474 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d412ac3-6021-3e54-9f7e-19b26f08bff5 | -20.32264 | -46.63449 | 2024-09-30 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d014ed4-5d53-3cff-8f32-52d4cb7f2673 | -20.32208 | -46.6615 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 22f43637-3aca-3c38-a3ca-256b3601817d | -20.31771 | -46.65843 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6c390dbd-32d5-3654-8359-2b2c97a87290 | -20.31663 | -46.6394 | 2024-09-30 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a49de950-31f8-3c55-a518-5ed8161a8188 | -20.31637 | -46.66491 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ed7aed96-4b46-37af-bb78-d8a3f0766412 | -20.31553 | -46.6447 | 2024-09-30 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8ffad4f-a2d7-3145-8377-803ffcee196f | -20.31325 | -46.65574 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d6557700-04df-34db-b089-ec7eaae659d2 | -20.31199 | -46.66183 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dc5c0907-febe-3529-869b-16dd851d24ae | -20.31061 | -46.6685 | 2024-09-30 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |


[Clique aqui para ver as próximas entradas](README24.md)
