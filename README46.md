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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5694fc3b-42a8-381a-a4ca-48a56855a5e9 | -15.68393 | -59.74272 | 2024-10-25 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39487ba1-7da0-3176-b302-8ea06601202e | -15.67687 | -59.74103 | 2024-10-25 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de7d4c9c-9b3c-378e-b342-920d3f09a0db | -15.6752 | -59.74828 | 2024-10-25 04:19:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cad59ecc-ca53-3615-93bb-eeb336f16bd6 | -29.81555 | -51.17794 | 2024-10-25 04:21:00 | NOAA-21 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 7e79ef4b-9428-3068-87e9-04288a12e588 | -29.77972 | -51.17868 | 2024-10-25 04:21:00 | NOAA-21 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 1a038893-66ff-3831-9345-eed3c6485b51 | -1.1834 | -53.6771 | 2024-10-25 04:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 00710f48-eaf2-304c-a935-05afbc1a58a5 | -1.1834 | -53.6569 | 2024-10-25 04:25:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a2655348-9b52-38d4-bcb7-7bd1cfa4d377 | -1.5878 | -53.3089 | 2024-10-25 04:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 211991f3-c83d-3fa1-b7ed-f4be3cbfa7ed | -1.6062 | -53.3087 | 2024-10-25 04:25:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 216b5eee-08cd-3e1b-a5d9-e3f4de2edf14 | -2.9578 | -50.4198 | 2024-10-25 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 86e0933f-004d-337e-aa5b-8b7cc1886386 | -3.2135 | -46.8063 | 2024-10-25 04:25:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 109.8 |
| c870878b-5e9b-31b3-a0ee-588f709bedac | -3.7761 | -45.7402 | 2024-10-25 04:25:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 08b44111-4fec-301f-ad10-5bbcec4e8d53 | -4.2429 | -48.5474 | 2024-10-25 04:25:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| acdaa264-ed5e-3e88-a154-ef2eae5632ab | -4.3351 | -48.6292 | 2024-10-25 04:25:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| c379a19e-e867-3c62-8bbb-2e0cdeea7ae7 | -5.9788 | -45.3621 | 2024-10-25 04:25:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8dbca4f9-c990-3019-ab21-cfacde2d0405 | -12.3783 | -63.863 | 2024-10-25 04:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 9fcf0a48-45b5-3364-bc54-a49b416a4e37 | -12.5356 | -63.051 | 2024-10-25 04:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.8 |
| ac8de587-80a6-3c59-88c6-7e10e3c71d9f | -13.4959 | -61.6203 | 2024-10-25 04:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 15890ae7-9ba3-3a54-af0a-e8d5d76afb1c | -15.6594 | -55.9742 | 2024-10-25 04:26:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| e8b4ba6a-7588-3817-b5bc-5866537c8753 | -15.6788 | -55.972 | 2024-10-25 04:26:34 | GOES-16 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| e881867a-e098-3310-b34c-706d6994cb4d | -17.0381 | -57.5155 | 2024-10-25 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 9bebee09-2b94-3808-b7c9-2b813f1d4e78 | -16.94 | -57.5268 | 2024-10-25 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.1 |
| c83b77b3-60e6-3380-8cf1-6017ffebb013 | -16.9596 | -57.5245 | 2024-10-25 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.9 |
| b1e6aa0c-e6e4-33aa-95dc-617a05e7c031 | -16.9792 | -57.5223 | 2024-10-25 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 119.4 |
| 81f53b9d-dd17-37dd-9ce1-e11d3cfaef1a | -17.0586 | -57.4517 | 2024-10-25 04:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.2 |
| c8011341-f1d4-39d2-a267-9456d5384a02 | -17.2537 | -57.5108 | 2024-10-25 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.2 |
| 81bd5d3d-0e78-36bb-b591-afce95502fac | -18.3004 | -56.2222 | 2024-10-25 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| f1c2ad70-8820-37eb-b283-ae3d6ff45c4c | -18.3199 | -56.2404 | 2024-10-25 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.1 |
| a287a4b4-5ebd-35de-86ab-c52035c1f405 | -18.3398 | -56.2377 | 2024-10-25 04:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| e8d5897d-302e-390e-b490-16288821e78f | -1.1834 | -53.6771 | 2024-10-25 04:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 74efb544-5c6d-314f-9097-7a562b6e8a08 | -1.1834 | -53.6569 | 2024-10-25 04:35:12 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 905493f1-ca4d-3ff4-a243-3248d9c72e0f | -1.5878 | -53.3089 | 2024-10-25 04:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 8aac6fcf-f17a-37aa-953a-daca259e9944 | -1.6062 | -53.3087 | 2024-10-25 04:35:14 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5cd36bd5-b43c-3b30-8137-a172b4a45e6b | -3.2136 | -46.7843 | 2024-10-25 04:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0a40bec3-ff13-3dd6-b4f2-b68283a17b82 | -3.2135 | -46.8063 | 2024-10-25 04:35:23 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 3c1e97ef-c264-3e2d-9ebc-ed0f38e9293c | -3.7575 | -45.741 | 2024-10-25 04:35:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| dd93733d-acca-33e4-887d-0b863e1e86f9 | -3.776 | -45.7626 | 2024-10-25 04:35:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 109.8 |
| ad4163aa-e411-3237-bd47-f4752c909aa4 | -3.7761 | -45.7402 | 2024-10-25 04:35:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 527.6 |
| bdae65f5-a9b5-384d-b9fd-342240d685fa | -3.7763 | -45.7178 | 2024-10-25 04:35:26 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 89.2 |
| bb08ccf0-fe04-30d9-ab90-0cc4e6ec78ed | -4.2429 | -48.5474 | 2024-10-25 04:35:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 163c1701-c58d-3eae-969f-c1a89c145f8d | -4.3349 | -48.6506 | 2024-10-25 04:35:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| e4215f10-55b4-33eb-b749-ba2989c1761b | -4.3351 | -48.6292 | 2024-10-25 04:35:30 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 112cf3a2-4735-3280-befc-f3b07dcf630e | -5.9788 | -45.3621 | 2024-10-25 04:35:39 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9545ca23-6024-3582-ba98-8c2c7df86536 | -3.06 | -40.04097 | 2024-10-25 04:36:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 02666594-3099-37fb-8bc1-178c4cd0601b | -2.97395 | -42.71579 | 2024-10-25 04:36:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71f0750b-39b0-32d4-a222-18ea5d372c8d | -2.95377 | -42.7045 | 2024-10-25 04:36:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ec2ec4c-a9da-311e-aea8-c1a60e07d8e9 | -2.9501 | -42.6998 | 2024-10-25 04:36:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1e7ee60-82d9-31de-be36-fc54115ae544 | -2.94949 | -42.7038 | 2024-10-25 04:36:00 | NPP-375D | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 963a2e76-08cb-3011-9cca-0450b24d58c6 | -2.94107 | -42.78796 | 2024-10-25 04:36:00 | NPP-375D | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5af54c90-20f9-325e-9432-400dfb21bb7e | -1.96073 | -46.63173 | 2024-10-25 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 983ead62-607f-33ab-824f-4f5d1c7e757c | -1.95732 | -46.63121 | 2024-10-25 04:36:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9402825-a816-347d-b22c-3aaa1b287d5a | -1.49615 | -46.78726 | 2024-10-25 04:36:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 721a83f7-71e7-341b-a8eb-6be9982a2781 | -2.68636 | -46.72258 | 2024-10-25 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0aaa340a-f9b2-3165-90e7-8e4632fa3c40 | -2.57218 | -47.25212 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e95893a-e2b9-334b-9537-114d70ec35d9 | -2.57162 | -47.25567 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 380f8467-dd0c-3d53-b966-f4a0d607336e | -2.54939 | -47.35386 | 2024-10-25 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bdd0ae72-44b1-3dd8-8bb3-339e70229185 | -2.54184 | -47.22555 | 2024-10-25 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 43ce9f31-a08b-318a-be21-65e44fcc3f07 | -2.53847 | -47.22504 | 2024-10-25 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51035351-99fa-30ab-9a9d-2f181ef12e5b | -2.48467 | -47.2752 | 2024-10-25 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8999704-dfc7-3d2e-a695-eccf00cec2a5 | -2.31536 | -46.61738 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 475957e2-45df-30a7-a6b8-6873beff8e56 | -2.31251 | -46.61317 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b593b60-9615-3705-aa0c-17ef00e6bb97 | -2.31194 | -46.61686 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f372d8ca-133a-32c0-b14b-c9416d33adff | -2.31137 | -46.62054 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 691abf40-a0e3-3421-9270-b23bbf50a688 | -2.3108 | -46.64682 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39f12878-1301-3315-9606-a588d2bd3963 | -2.30739 | -46.64629 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 937f265d-9ab9-37d1-a63b-4d0feb17f6eb | -2.26268 | -46.7968 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12176371-5881-362f-9559-85d47910932c | -2.25871 | -46.7999 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f54e6f25-af3c-38e0-9270-2b3298d0cf57 | -2.25646 | -46.7921 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7cb24f9d-ba53-37ec-876f-184afe11279d | -2.21677 | -46.86753 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88f693a5-ef21-3720-823d-cb05191c2b93 | -2.21337 | -46.86701 | 2024-10-25 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b3ddb77-b80b-35cb-8c4b-dbb0f9052895 | -2.73558 | -45.99489 | 2024-10-25 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e17137b-a597-3523-a4be-aa8b5584f06f | -2.73498 | -45.9988 | 2024-10-25 04:36:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97a9c0b2-e74d-39f7-9d7a-0d6f4d2a81fe | -2.6109 | -46.12739 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4f433273-babd-3948-9fa8-5b599357b4a9 | -2.61031 | -46.13125 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1ef5f30b-f912-3286-8e66-1dffedd7de14 | -2.60972 | -46.13511 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aedd493d-2b03-3023-a81c-272a6d70d89e | -2.46889 | -46.08682 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54900291-a583-354c-aa92-625b61422218 | -2.466 | -46.08244 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08623f0a-e855-3dc1-8498-9624b76d8d19 | -2.46539 | -46.08629 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32cee643-9d6c-3b97-9019-da4665322685 | -2.32457 | -46.04174 | 2024-10-25 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cfaa2c9-f864-338e-a243-e6cf086e2ac3 | -0.61509 | -47.34892 | 2024-10-25 04:36:00 | NPP-375D | SALINÓPOLIS | PARÁ | Brasil | 1506203 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91268303-0ba3-3ad6-9a42-c9ab88ee8f54 | -2.01535 | -48.51497 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 516dbc61-0f5e-336a-b1f4-6227abed3123 | -2.00932 | -48.53168 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 11443b1f-530b-320c-aabf-4e0864e28c22 | -2.006 | -48.53117 | 2024-10-25 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 11fc2166-e5b1-330e-bdc7-1a1e575e4a78 | -2.00209 | -48.72849 | 2024-10-25 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 954bb3cb-76be-35ff-87c7-80905f50eadf | -1.99877 | -48.72798 | 2024-10-25 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d2ba412-3a59-3621-8a76-20085cd24af5 | -1.60769 | -48.69865 | 2024-10-25 04:36:00 | NPP-375D | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3fc231c4-f181-3265-9a36-6f464b644798 | -1.41366 | -48.38231 | 2024-10-25 04:36:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9728fc04-a263-3faa-9662-1397009664d5 | -1.63996 | -47.73912 | 2024-10-25 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2f7d65c2-8d5e-3940-84ee-43bad191f6bf | -1.63941 | -47.74258 | 2024-10-25 04:36:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2529fcde-8010-30b7-8dd8-a42b902d5a1c | -1.53494 | -47.20434 | 2024-10-25 04:36:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56a32a37-4ed0-340b-a978-3f202b9f0f2c | -1.53214 | -47.20032 | 2024-10-25 04:36:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35763096-6bcb-35ad-b181-2133bc4296af | -1.53159 | -47.20383 | 2024-10-25 04:36:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2bc1bca-93d5-38c8-8217-d6057ca3beee | -1.50212 | -47.28203 | 2024-10-25 04:36:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7bce1f6-adf7-3684-b2e7-cdfb75f78d7e | -1.34767 | -47.75014 | 2024-10-25 04:36:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ecab7a2-4353-3284-adef-faab522bc1b1 | -1.20203 | -47.59634 | 2024-10-25 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a7b2438-d587-31a4-8ed4-e8ffdccfbe08 | -1.20148 | -47.59981 | 2024-10-25 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0dfaff7e-fa7f-3d1f-bdb3-292f31d087bc | -1.20094 | -47.60328 | 2024-10-25 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3b96bb02-4c3d-3b37-b6b3-803ce02fc5e0 | -1.19815 | -47.59929 | 2024-10-25 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8731085-4090-3d5c-a89d-a3698ae6f219 | -1.19761 | -47.60276 | 2024-10-25 04:36:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e06202ff-c0e7-3d70-ad44-f6eaf508eefb | -1.04674 | -47.61855 | 2024-10-25 04:36:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |


[Clique aqui para ver as próximas entradas](README47.md)
