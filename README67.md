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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e054b80b-1b60-3aed-83cd-467a725c1992 | -4.87237 | -50.73884 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54748381-e757-34e2-bbde-4bb71efb99c0 | -2.80241 | -54.04953 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1a5d49a4-7b8b-34ac-b598-0b0bab438d9d | -2.61206 | -54.07793 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a5ede22-9796-3613-abf1-c1c3e40c91b5 | -2.20198 | -50.5503 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e1218c7-5f27-3a10-95a9-be587b02921f | -3.89104 | -46.4045 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19d6c5d7-6fad-3d91-8b96-4c24c991c3f7 | -2.59007 | -46.93718 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa7adcd1-ff96-367a-983a-10a0fbf6bb81 | -1.2834 | -47.90404 | 2024-12-01 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3e5aa1b3-c0e3-3f0d-8c3b-d7c7771251cd | -1.37488 | -52.8665 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a88891e-351b-3d86-89a4-1eb55c137d53 | -2.32661 | -50.68329 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 095f1420-5c91-3d71-a90e-31ce894c88af | -5.53915 | -45.42966 | 2024-12-01 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d9648d1-db38-3ba8-a971-30a4de8e443f | -2.88177 | -53.33206 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a1cabdac-3915-3795-b975-600590f78b0b | -1.8187 | -54.87215 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caded065-6203-387d-90b0-8fd9bc6d38fc | -1.31518 | -51.67203 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc6c2b0b-4aa0-3716-a994-2b02fd5b8560 | -1.49398 | -52.41758 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4709706-bdba-36a4-a9ad-25e6fb22211f | -3.26571 | -50.04849 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a5b2254-c033-3e32-985f-c18a31c0d66d | -3.49638 | -53.79723 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42718690-5569-322d-a206-3dddf95f754f | -1.92059 | -52.66273 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5504c271-e64e-356d-b190-96cffc511c34 | -2.58846 | -53.98492 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60f92ff5-553c-33ba-99bb-75d99eac1680 | -3.1086 | -53.10521 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56360e6e-9abf-3348-aa3c-d762b105161b | -3.7844 | -46.70103 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a2f0d6f-e393-333a-8df8-a069a6e0b389 | -3.70953 | -51.67812 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0ad6f0d-53fe-3476-8f0a-490df0164469 | -2.33213 | -50.66992 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9858b086-6eb0-38b1-b567-0f3a1ce4ea16 | -2.93137 | -51.93919 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49443866-c2e7-397f-8761-03fcf3dda9cd | -3.09822 | -54.29526 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3166b1c6-2bca-37fb-b581-65b0bb9ae7f4 | -2.12422 | -46.57856 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4aa90e73-b2b6-3de3-853c-477f6a23ddff | -2.47828 | -50.3666 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d90b1c6-2559-35ef-a3c2-819c12e3fd4c | -3.81716 | -50.95255 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea60c714-039a-321d-aea2-f31e6a044d99 | -3.86354 | -49.95056 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d4e3224-fc96-3218-8cfe-f64fb892c08e | -2.46614 | -50.37885 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 037e7565-f43a-3eda-8472-422c214fe77f | -3.23942 | -53.63779 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e42852b-5c0a-34f4-a54f-30b4eafd5574 | -3.179 | -54.32794 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e97001f8-ab92-36dc-8e1c-4913ae56c6e0 | -3.053 | -51.05814 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5005fe5-de4f-3bc9-b20c-05b6c2e6ad77 | -3.73999 | -51.69003 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5a64879-b208-393c-875c-60bf56f8276d | -3.79319 | -46.69344 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf864ea6-177f-3399-b117-743dc9cf8c96 | -2.00239 | -52.09764 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b8440e1a-b4f5-3944-9cf5-d7e8e546a7fe | -3.06048 | -54.05206 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 202909ca-eb84-3216-b7b0-58543be4f607 | -2.78306 | -49.82808 | 2024-12-01 04:44:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7b10a84-e2e5-35a1-b530-3c9fd9a6d93e | -4.55051 | -43.30777 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| cef72db5-0fe1-329b-b0ee-b01f0b5bf5d7 | -2.97854 | -53.2862 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 33c20a51-9533-30b4-bbc0-4bcfbcc5af5d | -4.25435 | -50.8402 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d1885c5-2b16-31f1-bdbb-408f0c755d24 | -3.70531 | -51.79849 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 155ffb49-a1fe-3dd6-a61d-741a7b2ea8c2 | -2.80776 | -54.06189 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 12a105d4-1684-360b-b855-4a045b850d33 | -2.98905 | -45.57607 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 33dfc178-b7ab-327a-b1d7-6b712d93b2eb | -4.00526 | -46.94124 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 785e9f54-4bb2-3b09-bf29-ad0b082fa713 | -3.28629 | -50.62802 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a6e7890-90ee-3a4a-95b6-984afc39a387 | -4.02683 | -48.88775 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c25bf1a-38ca-3da8-b26f-3221644d3b61 | -2.68233 | -46.14454 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0a8b617c-e8fd-318e-a7f3-219961afc926 | -4.53254 | -45.70052 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb43fca6-4722-3416-98d6-5e9100755962 | -2.32606 | -50.68676 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d536583-f5c0-3b5c-8bc8-d6c6eb3ce697 | -3.13877 | -45.98318 | 2024-12-01 04:44:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 257e1258-5b5a-3972-a1c1-a44264332f41 | -3.28553 | -44.90511 | 2024-12-01 04:44:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16885d6f-8bbf-3bd7-a0b5-4be00e68af2b | -1.7847 | -52.74477 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50966ed5-7c85-3360-a9d7-a64e7af5596e | -0.9794 | -52.40953 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ca707cc4-1c98-3709-8d72-1aec44096afa | -3.85099 | -40.98486 | 2024-12-01 04:44:00 | NPP-375D | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 672e4d50-f4ab-3497-9f4a-3b8e6d22dc2d | -3.48905 | -53.80635 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc48b962-d64c-3283-91bc-3df9aa46177f | -3.28433 | -54.1486 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 225a4f9e-c151-30f5-b4f5-b621c5fc69f6 | -4.0179 | -46.99937 | 2024-12-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b87fd700-444c-31ea-9ac4-ec0aabc6f0bc | -3.50007 | -53.79781 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e2b6481-a096-300d-835c-ad679b3c7975 | -2.47978 | -54.01255 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09bbcf6a-9a08-3b5e-baae-148f105d1cdf | -4.05207 | -46.82208 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 676bd373-2a92-368c-8417-2e75fc166ed3 | -2.5773 | -49.99709 | 2024-12-01 04:44:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4319fdd8-3e34-367b-8246-a544962a7863 | -1.5752 | -52.27028 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ed263722-5817-3799-b284-f8f9bb5afc8e | -2.88419 | -54.21536 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7733608-5478-38fb-8afd-1814ab73fc5c | -5.80123 | -47.07624 | 2024-12-01 04:44:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa4c8bb2-cb95-3e48-96fe-f29eab37a7c6 | -4.56911 | -46.2994 | 2024-12-01 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| db171afe-1c31-3fed-b1c2-e6168da6839e | -4.54166 | -45.70057 | 2024-12-01 04:44:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| fb9129c4-a2a1-3395-b744-b943176dfa17 | -1.99893 | -52.0971 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e86dc65-20eb-3137-b870-a06eda1174b8 | -4.49649 | -49.64149 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 590af046-9028-30c3-9786-f2e64285f359 | -2.69627 | -52.90803 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ec46244-d413-3061-b02d-406c88e27ca9 | -3.26529 | -50.09439 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e9642d1-2eb3-345f-9e09-6dd2c8805078 | -2.35433 | -54.58309 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e999a1e1-4b17-33f2-a4bb-ac4598f32cc7 | -2.85169 | -54.10165 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8eed40fd-c318-390a-96eb-72e36ca7a653 | -4.99694 | -50.7448 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3eb0a496-25d3-3ad3-93a0-af6c6152e9b9 | -3.38791 | -50.35033 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 449993d5-facc-3835-ba5b-1f9d2cc834d9 | -1.23429 | -51.61092 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6643f4c5-6239-3010-baf9-90a7d795be1b | -3.74213 | -49.92459 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94ace0d8-0021-3658-9f8f-42ace8c9fbe5 | -3.11129 | -53.2727 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0f22cc4-44e0-3578-b4fb-2b7b2e4753ff | -3.10245 | -53.25864 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 571cd03b-cb0a-38ee-be2a-c569f00198c8 | -3.26643 | -53.63337 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0970681b-ffb9-3b73-8b33-454cb5f3de54 | -3.55682 | -51.65444 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 66a09738-66ac-3b07-a006-b06f90bc8343 | -3.27008 | -53.63399 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 494301d0-9c43-3222-8cec-7d16b1306529 | -2.46436 | -53.96476 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c6026f5-da65-392c-8073-f1db3959975a | -2.44379 | -50.52051 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a495140c-c170-360c-a304-e6f391efb65a | -3.24239 | -53.64267 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 143d0694-fc0a-3814-b5e8-d7d77aaf10d7 | -3.02287 | -53.4075 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7263782f-9f58-364a-ac57-3257b01c9694 | -3.21831 | -54.17762 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 67c20f15-0656-3725-a4aa-6006d304128e | -2.84234 | -54.03954 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fc058c5-f464-3a02-9bcf-14c08bb7e62c | -3.28817 | -50.16511 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cfcfb99-c894-3acf-9416-0713733390eb | -4.20534 | -50.69791 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 374fd50e-f05c-3926-b7fa-336c32686544 | -3.99001 | -49.94166 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36790076-c809-35e0-b702-fafb6c79357c | -3.26903 | -50.04901 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3933ba1b-f101-3d74-bd66-20bc6b05c247 | -2.71156 | -52.00306 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 11bc2067-b181-3296-a9df-f2f33911e1cf | -1.55933 | -53.51374 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26863cd5-1c07-371d-902c-66729b51f9b2 | -2.12731 | -46.53491 | 2024-12-01 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d6693cac-b9cb-3c75-8508-4c9d73690169 | -3.58557 | -50.50876 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf3f176c-c9a0-38c3-a92c-e648393c26a1 | -2.44317 | -53.61992 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d507e30e-e6df-3a7e-9ffd-f257893fe1a4 | -3.09325 | -54.01589 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4eeded86-8d43-3f1b-ac80-0d426403b8a4 | -3.86021 | -49.95005 | 2024-12-01 04:44:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a9eddfa-b146-3eff-aa12-da67f90d8734 | -3.58689 | -51.20613 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f281984-0128-31c2-aa2a-fe54f5b8fda7 | -3.57305 | -52.01181 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README68.md)
