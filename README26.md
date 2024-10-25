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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcb9ddb5-b1f0-3cee-ba94-0b91374438ca | -7.04964 | -43.97265 | 2024-10-25 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6149362e-d860-3e6d-a60c-0336bd7c60c5 | -6.5943 | -44.18328 | 2024-10-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f67b236-4a5d-3f47-85de-8777ecf071b9 | -6.59375 | -44.18679 | 2024-10-25 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff686cf8-0a91-3ba1-97ad-fbe0faccadb9 | -6.58456 | -44.41159 | 2024-10-25 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57095d32-1ee7-34dd-95fe-7c74e00181b0 | -6.4654 | -44.66816 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d08cc1d7-4a49-3ae8-be00-1ae23529ff62 | -6.46482 | -44.67179 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fff0fc34-1da7-31a7-bb49-e7da29f6f45f | -6.46424 | -44.67541 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4f89deb-bbab-3413-99c2-834fa8e8a962 | -6.46366 | -44.67903 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb09abf7-3767-3ae6-8a0b-1e4fdfcac839 | -6.46202 | -44.66766 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb2cc01a-ebd8-3688-8bb0-f08083ac6f59 | -6.46144 | -44.67128 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f8eb00fc-9d7c-38c8-927f-c220cb0c9782 | -6.46086 | -44.67489 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 346fcb1b-f750-356b-a4bc-9e52aa81f7f9 | -6.46028 | -44.6785 | 2024-10-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 992a1d16-d447-3c0a-a03b-419e1f359ee3 | -8.79632 | -44.719 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c2610d0-b2ea-31a7-84ed-8b8b0d901895 | -8.79576 | -44.72256 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34949d34-6aae-3eda-8a7a-797dc92d6044 | -8.79519 | -44.72611 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f98e1df7-df43-3ea9-9d26-f8bc125c7f5f | -8.79242 | -44.72202 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7ee88ed-7046-3384-8054-49f92107f13d | -8.79128 | -44.72914 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a6e118d-726a-32a8-896b-ebbb063a3ae7 | -8.79072 | -44.7327 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec6ed60c-2633-3991-b496-dc3a6a7c0d52 | -8.79015 | -44.73625 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1657b892-e2d9-36e6-87b8-3ef8588eea41 | -8.78959 | -44.73981 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707c1263-85f5-3c0d-9bbf-4d6082adaee0 | -8.78354 | -44.7133 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78854dc6-5078-37e3-963e-86b87250308e | -8.78298 | -44.71685 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 053e988b-7a97-3156-a313-552b20ef57f3 | -8.78241 | -44.72041 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c7ea69bf-d204-35fc-a6a3-c7410d7f9ece | -8.78184 | -44.72396 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ed76d6b-49d3-33ea-a4e0-5190b86ce187 | -8.78128 | -44.72752 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9af0c5d7-0a2c-3d5c-865c-3da817214fc3 | -8.77801 | -44.70511 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d147297-8d1f-3f59-945d-d84cfda092d8 | -8.77794 | -44.72699 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25775a30-2473-34d6-befb-c14dde645e4c | -8.77737 | -44.73054 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e32819a5-0517-3036-a453-c1c4b60344c8 | -8.77467 | -44.70457 | 2024-10-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c40a92d-601f-39e5-a06e-926036c26b19 | -8.38917 | -44.47551 | 2024-10-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21750bc6-e4ad-3e6b-8429-454dba9587ec | -8.06701 | -44.51081 | 2024-10-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c91ec8b2-89f4-3cfc-943e-6099c68aba80 | -3.47445 | -45.65628 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 036351f2-def1-3622-8336-4968f0bda768 | -3.47378 | -45.66047 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 580c793f-c4c6-338d-9e12-f781492ab8cb | -3.47083 | -45.65573 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5de3c62e-6ff6-3725-8074-16de772f55f1 | -3.47016 | -45.6599 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eea53288-9c50-39b0-bce9-459eac4c8232 | -3.46948 | -45.66409 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52ab6471-aaad-38e7-bdd0-5a9d39d4e197 | -3.25079 | -45.8095 | 2024-10-25 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c596dcd2-3f89-3017-90ee-dea3007903d2 | -3.11739 | -45.70698 | 2024-10-25 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 105973ff-6079-377e-9ec3-2f06a2ed1a38 | -3.11375 | -45.70642 | 2024-10-25 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9212a4fd-fcf1-31d2-a62e-66e05abca654 | -3.08826 | -45.90934 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3928f404-b808-3d0a-b2ec-598314ee0d28 | -2.92937 | -45.45575 | 2024-10-25 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 286d46ff-6dc8-33c6-8d8e-146da0ff5aed | -2.10397 | -45.45064 | 2024-10-25 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60fb292c-d244-36d6-a2a8-411e82f5adf3 | -4.71434 | -45.7346 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3a701ea-4a41-3376-af00-c38a954e8655 | -4.69619 | -45.87159 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75e58af-7505-3b90-8484-d96f6c02039d | -4.68037 | -45.80895 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5aa6977-83b6-3eaa-8e78-d42fadd704d6 | -4.5464 | -46.03503 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cc72219-d7b9-3ff6-8c39-46903820fbed | -4.54276 | -46.03444 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| faf5275d-431a-3e89-bb83-57fd482e63ba | -4.54208 | -46.03865 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed06546-1cdc-307f-85a1-b1c565192a98 | -4.41587 | -45.98481 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50c0c88f-ae5a-3f7d-8e68-134a384d0fb9 | -4.39079 | -45.80944 | 2024-10-25 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1336a1e8-1486-36bd-a47e-ae27ac57dafd | -4.35029 | -45.97079 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42353a2b-ad9c-390a-9e02-2ea5f1d26cd8 | -4.34963 | -45.9749 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c8e9b75-1da2-3de8-a1c8-86b7b47c740e | -4.318 | -46.00907 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a3c8e114-8c03-3bca-881a-048f4d48de50 | -4.06576 | -45.52447 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dbac9312-3023-3b87-8fff-77f862413d25 | -3.92934 | -45.83553 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a121f27b-1f67-3470-86da-7ed15d49d7ad | -3.77581 | -45.74351 | 2024-10-25 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 686d93ec-dc65-3cdf-b223-d0fa941f6438 | -3.77219 | -45.74294 | 2024-10-25 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ee740a61-4262-326a-b8dd-e081479da700 | -3.75898 | -45.80121 | 2024-10-25 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1eec5708-b66d-3c53-a647-7331127e7049 | -3.71409 | -44.64602 | 2024-10-25 04:14:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d555fc6-ff00-33ba-8720-fe81d82f0a35 | -4.99578 | -44.89102 | 2024-10-25 04:14:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b20351a-6661-362f-bff2-2ecd74e3b805 | -4.94837 | -45.73997 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 055a2e70-8ae8-33e7-96a7-610d74b47854 | -4.94748 | -45.54639 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de1d4f2a-c3e2-33d5-ac3b-af51b1557512 | -4.94683 | -45.55045 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6e08385-5826-3e87-ade8-c4230e8c210c | -4.94569 | -45.74047 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b0367245-a4ca-3039-8e10-77e22597d1e3 | -4.94503 | -45.74459 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cdf8fcc-89a2-3586-aca7-bd4fb784bfbe | -4.94412 | -45.74352 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 786d3b69-ebb6-3afc-ac1e-febf065d7544 | -4.94329 | -45.54992 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 157810d1-fd3e-3841-ad87-15ee711a4691 | -4.86546 | -45.82839 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 574aff4b-daca-342a-ae50-9ea714fbb691 | -4.85336 | -45.83483 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fe41ad5-8ae5-329a-86af-a6b73b4852fd | -4.85269 | -45.83895 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc153fab-26f3-31e5-a7b7-959025892244 | -4.75311 | -45.66912 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f73bd26-89cd-3785-8c3c-81805538ba10 | -4.74889 | -45.67254 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 636c5d7b-a065-3dbb-a61c-654fc37c657c | -4.74025 | -45.79268 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abfa5e99-bb64-3753-be2a-9e9d99c6e81b | -4.7101 | -45.73816 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72ec5434-6af9-3a01-850e-74b8e4426dbf | -4.68103 | -45.80485 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 721db68a-15ce-3ac2-94b8-ab970e09bbc1 | -4.39244 | -45.80928 | 2024-10-25 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e9f5ff8a-7619-394f-b159-4571ff7c0aa5 | -4.36975 | -45.84863 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05442545-490d-3c0c-b185-fd312c9fc8fa | -4.06641 | -45.5204 | 2024-10-25 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b1d65ad-3ad1-3169-83d3-6b16d86564b4 | -5.02944 | -44.98937 | 2024-10-25 04:14:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9e139c92-49b1-3cc7-9524-91726a662263 | -4.84865 | -45.03901 | 2024-10-25 04:14:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d428b7c-9416-3516-8f00-acb501aa8492 | -4.84803 | -45.04284 | 2024-10-25 04:14:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b568fb06-59c7-3aac-9dc3-a86bd70866fb | -4.55004 | -46.03564 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c852c9be-a211-30f8-a1fd-6cd08f76b93e | -4.54572 | -46.03926 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd06db69-b711-36ef-95c4-b2321f4df820 | -4.53911 | -46.03386 | 2024-10-25 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e08e30aa-7300-3f8f-98ca-151884256483 | -5.05719 | -45.47321 | 2024-10-25 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3e197c15-c5c0-3778-9db5-1772e6f6d4e1 | -4.94811 | -45.54245 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ede0a13-5501-3ed6-b5c0-7f0a9638e6f8 | -4.9448 | -45.7394 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7233462f-9fbc-3eab-8aa6-1ccc8c0041be | -4.94393 | -45.54589 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d3122091-e401-3a31-9b69-9449f3c47dcc | -4.94264 | -45.55393 | 2024-10-25 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8acfa25c-8a88-3d24-aca7-2c8d1677167b | -4.87907 | -45.6097 | 2024-10-25 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c72616f2-ebf9-3223-8ee8-6de53e98bf3e | -4.87125 | -45.77008 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c12fe433-d95f-37e6-979c-5e7af1495d18 | -4.86766 | -45.76957 | 2024-10-25 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d26ec3f-df40-38fb-90aa-ed496783b937 | -6.4464 | -46.06048 | 2024-10-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bf8f202-dea6-362d-bed5-398f5235b412 | -6.44282 | -46.05994 | 2024-10-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 450167a1-bad4-3824-b445-e41cbdb78907 | -6.44215 | -46.06404 | 2024-10-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d518b9ba-cf88-3997-aebd-75ee0c0b3a97 | -6.08211 | -46.3116 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 605239b6-dbec-3952-877e-dce16d1fd559 | -6.07917 | -46.30685 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91ef358e-96eb-38b6-968f-219263cd4dfe | -6.00728 | -45.9476 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 478b8530-044a-396c-a86b-d9ad1f32ea48 | -6.00662 | -45.95161 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29745f66-3364-30e8-8deb-8269d5a58435 | -6.00595 | -45.95564 | 2024-10-25 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README27.md)
