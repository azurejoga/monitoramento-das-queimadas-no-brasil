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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 491dc786-103c-3397-bd61-d79e28788d0f | -7.33442 | -55.22447 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7a368c92-7942-3b0d-a6b3-52db0494ccbf | -6.39942 | -56.40512 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1c6da27-6b06-33e5-811e-eeff707cf85c | -2.89839 | -54.15369 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e77c0d7c-2b0b-3364-8eac-c469d1e9ca98 | -4.25801 | -50.74492 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75b4ceef-41f5-3d35-aedb-f3840dc3d192 | -6.09577 | -47.6717 | 2026-10-02 04:57:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 746a8a14-1bee-3d1e-8a6e-2e9af0de9655 | -7.46221 | -54.99587 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1abe19c1-f16c-3a6f-b816-8ad9f56a3a0d | -3.28622 | -53.84862 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 118f5c8b-2db0-3bd5-a9b1-b22fe29d2e18 | -4.06984 | -51.10548 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 093945e5-7cf9-3492-a842-513a819c5023 | -5.87055 | -50.162 | 2026-10-02 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6b3b78fa-8f3a-3487-a91e-8298a2382051 | -4.68763 | -55.79624 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8dbaff72-85e4-3f73-bdf0-0551aa3121c7 | -4.25677 | -50.75324 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 759046c3-f96f-3665-a7a1-f333c51374e1 | -6.33817 | -55.32717 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a5dddad-396a-3d5a-84b8-a0ea65eb0d4c | -6.51841 | -55.39224 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c05378d-7169-38d3-b243-575a601fc9c6 | -6.40508 | -56.41367 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 73651a00-a4b5-3e33-a0d0-c09f8fbc6ff3 | -6.09767 | -47.67457 | 2026-10-02 04:57:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b0e4896-5eb2-3875-a26c-ae370ba4c36e | -3.02542 | -53.97258 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4e738b29-2f93-31f5-a28a-0ee8c564882e | -3.27445 | -50.08858 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d521b4a1-6199-3452-8616-0030ea9205be | -3.02234 | -53.88428 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5d6b7d7-b985-39af-9685-83dcaf6c3282 | -4.45962 | -47.92304 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0e5aa0e4-a2e8-3985-9f13-bee6e7522bd9 | -6.19341 | -53.17785 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0141636-b12b-3ce4-93e8-934c24ca6e34 | -3.1181 | -50.27955 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4883ef68-baaf-3c7b-a1f0-a9bce1444d6e | -6.33068 | -43.35741 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 099dfcc7-5787-359b-b77c-357fd6b536cb | -2.93267 | -54.19432 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8333999-72d9-3706-b7a3-956b2ad586f1 | -5.90026 | -53.49207 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33fa77c8-5c1d-3bc8-9440-f3f285dd7207 | -3.11446 | -50.28149 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bfcfdd00-de7c-393f-afe9-007b49b58866 | -8.17642 | -54.80117 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4af2243d-5c80-3654-9f09-2a4e4acdf4c1 | -1.0464 | -53.57054 | 2026-10-02 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1246b37c-47aa-3712-8a84-cae29a3e2fef | -6.14814 | -52.80854 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50154503-b1e7-3b5d-a036-05f6084b019e | -2.86142 | -54.13034 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d451c29-2726-36be-bce6-c649bcf9bcb7 | -6.41028 | -56.40299 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debda374-e548-38f1-8297-b47f1ec12060 | -7.836 | -55.13071 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db40f685-31ee-3f3a-9bb7-0ba7843dfa4f | -7.83379 | -55.12325 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 700c7898-8d37-3dff-9b7f-cd2368cab459 | -6.25075 | -43.7707 | 2026-10-02 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53053a42-ef8a-36f2-ac4e-dfc89e012fb4 | -4.29622 | -50.78474 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9170ffdf-dcf7-371d-be19-f3801b9ace6d | -2.10669 | -49.2458 | 2026-10-02 04:57:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbb2ac45-437a-318c-81ab-454f0b75025a | -5.84711 | -53.48388 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f30ea19-a96b-3614-8c6f-c6519ee1f2aa | -4.25317 | -50.75266 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f5afc23-845e-347a-8811-dd48c8936bee | -9.52394 | -45.3288 | 2026-10-02 04:57:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf01f4cb-4c8c-3f13-ac11-ba0599ccc9f4 | -7.54191 | -55.61292 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6db511b-6840-3d16-9342-0b83dfbe362e | -4.25739 | -50.74909 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf159641-1aac-3f4a-9c23-7da2fd89900a | -3.00968 | -53.87881 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac8071ba-9aeb-3d0f-b5f0-50545fc22f15 | -5.14303 | -49.86848 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 27a7a3c3-aaa8-3ee3-a93d-09dccab7723e | -6.36014 | -55.14433 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97dca448-fc1c-36ab-9b1b-1b1bd0f71e84 | -6.34372 | -55.33524 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca501f56-46f2-34da-9925-f3ef9d8c15ee | -6.24286 | -53.14563 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aaedae01-a863-32ad-8f0a-fe881b461f03 | -7.19397 | -46.5531 | 2026-10-02 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0b7bb1c-44f9-320b-8311-441653d7521a | -7.82939 | -55.12967 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e66dd53f-ba84-3c6f-b122-fe2a6a7f8a8e | -6.1511 | -47.47343 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 561b67a4-e481-3bf3-b7c4-bbda404f39e1 | -3.29174 | -53.85649 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aff4bcbe-c143-3a98-a047-3bb997cfaf72 | -7.74744 | -49.20499 | 2026-10-02 04:57:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0ba6ceb0-3a64-32b3-904e-dff7822fe51d | -3.11874 | -50.27782 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac44f131-5894-305e-938b-3fc81b6f16df | -4.27353 | -50.76435 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce7f5c5a-6c09-3d3e-a058-37af1c4e10d6 | -4.26224 | -50.74128 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 915184f3-4743-3d66-8412-ce3af523d048 | -6.34205 | -55.3242 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20503638-07f5-3a2d-83b1-982de27245f5 | -4.38899 | -54.82521 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cad1fb5a-b829-33eb-aacf-badeacd1da64 | -7.49849 | -54.98029 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f501806d-ca36-3d12-8078-1eed82ca5134 | -7.45946 | -54.99189 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 257c6d02-f164-382b-8413-4a69c72f1919 | -3.17223 | -54.098 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99e97b74-c9d0-3382-a75d-bf33db385d59 | -5.7517 | -55.74723 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74357693-97cc-36be-99b6-cbd0e96df334 | -3.11014 | -53.95469 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a5b187bd-2de3-324d-963a-2fa8d10289d9 | -3.11319 | -50.29 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bf9baf2-2b80-3468-9eff-a1078cc13a60 | -4.04392 | -54.22839 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d042aef-0c44-3b94-834e-9292970cac6f | -6.00181 | -53.53984 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e6ca1eea-7eec-3410-8881-db0c217fd8ca | -3.01859 | -54.23242 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cf24c5d-14e5-344d-bbde-a6c289a1fb9a | -4.30045 | -54.80408 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc13db9f-067d-3ca9-b087-aee2b872b359 | -2.9349 | -54.20173 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 95294465-3a49-3ac0-affb-9c892cdb4f42 | -6.49937 | -55.89515 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62197842-316c-34e6-ba85-c31f3d0ae210 | -7.52763 | -50.531 | 2026-10-02 04:57:00 | NOAA-21 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 835e8724-3e46-3dab-a710-3dad9cb1a292 | -6.45192 | -55.01628 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 583403c4-0f5b-3618-b988-c92967a87339 | -3.29228 | -53.85307 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fd1fe8ae-1fcc-3ae6-afd8-9577d0b66620 | -4.292 | -50.78833 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 23574d85-0f96-3fda-b3f0-02c1c1ee81f3 | -6.58596 | -53.01543 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a5dad9d-bdc9-37e1-84c3-b97b061af422 | -2.62288 | -51.70251 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72c9c73c-7082-3ff4-996b-0a73cef738fa | -6.15152 | -52.80905 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79fa9b1d-6659-3842-9157-1c2750ba3b6d | -4.27416 | -50.76016 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f3a46a2-0e29-3233-82ed-38dd7d36c5c0 | -8.16652 | -54.79961 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e424c577-7586-3fbe-a7b4-b67ef2455190 | -3.07169 | -54.37241 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbff9bd7-f845-3317-8dbe-1b972d9e6cb6 | -2.85919 | -54.12295 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0285da3e-5075-351a-8b77-f534e8a239e9 | -3.17162 | -54.0803 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e0b54a0d-578d-349c-9bbf-8d32c339802f | -4.27525 | -50.77734 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13197b16-c135-382a-acd7-0f0b76f94a73 | -7.55253 | -55.02847 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c84bf08a-c905-39d9-aef8-31a6e2389d38 | -4.25615 | -50.75736 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9172192f-dd7b-3f12-b20a-f927e2a022d7 | -3.95182 | -47.63676 | 2026-10-02 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 443d232e-b165-3e9c-bb38-6a25c610aff2 | -8.23126 | -54.73602 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77370523-f09b-34af-89f8-63a62c801ed0 | -2.95159 | -54.09487 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee09f299-b0a9-3094-be91-f2ad27fc963a | -7.41971 | -55.5468 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a0c02b-d4e9-3942-a299-ec029bdb3029 | -3.17492 | -54.08082 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| daf07ced-b7bf-31ca-9fd4-a8460c54b104 | -5.62117 | -57.23387 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be2c6726-1b5d-302c-a283-a89c80e015e4 | -5.23293 | -49.57996 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9ed4d75-a78c-3b36-ac01-9ebb2031db18 | -2.05684 | -56.87206 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26194749-4840-35e4-938b-2ec9a902c74d | -6.18972 | -52.8075 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d2ec5c9-e765-35e2-9f42-0bc1803a25ef | -6.39481 | -56.41205 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ffccf9f-5fe4-3a70-a0e2-9118ce385374 | -5.85865 | -53.47514 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5975e153-7f70-3737-bbbc-b717ce691da9 | -3.28791 | -53.85942 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8b42450-5b75-365a-88b3-ae1e504e7a2c | -4.28121 | -50.78666 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7fb99c4-eb9c-3bfd-8eab-9b562df6730b | -4.89076 | -48.37766 | 2026-10-02 04:57:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e08a7f50-f329-3caa-824b-fe9f089269bd | -4.36306 | -47.77162 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e04fe4a-d01c-329e-8856-90a1915bd950 | -5.85543 | -57.56311 | 2026-10-02 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 133caea4-4f98-38f5-a9f3-efbfe7ec590a | -2.97432 | -54.16909 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a2dee8e-1ad4-37cf-98de-e78fb835fd5e | -1.26558 | -54.55994 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README61.md)
