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
| 24959816-35a3-39a6-af1f-a18481cadd57 | -1.39037 | -54.64429 | 2024-11-10 04:36:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa1c4d7d-e1e7-3cef-bc35-e370e3ecb306 | -1.87589 | -48.55081 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18f26c8f-8e2a-307b-86b6-a7a0b998f562 | -1.38657 | -51.43583 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 926d05b5-d615-3d18-b143-50c99092cabf | -1.23475 | -51.77855 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc97ed3a-cc5a-3002-9054-d6c9bb2e1ccb | -1.18421 | -51.99857 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71e4ec0e-a90b-3d66-8df2-9a8176407684 | -0.89462 | -51.78117 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212a4d8d-4670-3135-b1f0-1636e45bd210 | -2.20066 | -46.79365 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 880c01fc-d63d-3358-a94e-981b59c568cd | -2.09396 | -46.53809 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 138825c5-78ea-3571-98cb-b35ef7337825 | -2.25892 | -47.0643 | 2024-11-10 04:36:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 69ad7dbb-137a-3052-bd2b-4f32e36b01b8 | -2.18033 | -48.37646 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f96728f2-00dc-3406-bf8b-007276ef5712 | -1.31173 | -52.19426 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56011197-54ae-389d-abd7-6f3530ebf5e8 | 0.81775 | -51.86998 | 2024-11-10 04:36:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd542796-dd5b-3c10-a4ed-9f84ba156a87 | -1.50541 | -52.18809 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 83e97f29-1f86-3db8-bb2c-3c58bf0b1471 | -1.49491 | -51.7405 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 354cf6ea-3776-35fa-bdc1-5da8ebb25dec | -1.17267 | -52.09457 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 905e8199-88e8-31c4-b1ed-afd6387b5cb5 | -2.09281 | -50.37896 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 349f9524-411a-36f1-b8c5-87f429472dab | -1.0571 | -51.7502 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba77cabd-54c0-3318-8977-b503be4e6aec | -1.79623 | -48.06562 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3edc9a1e-9994-3ee6-9045-133282f1914d | -1.82967 | -51.34738 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 141c9a2d-826e-3f2d-8c11-aafb30428c06 | -1.62862 | -50.48565 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5efede04-2949-308f-86fd-202ea6e7023c | -1.28406 | -48.26814 | 2024-11-10 04:36:00 | NPP-375D | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c56dc95-c523-3386-8b4e-62539b26b2b8 | -2.16811 | -48.54037 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a47c6af1-2cfb-3126-83fa-f19df7f90263 | -2.15912 | -48.27802 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cf6e496-f2ec-39ad-81a1-caf4db447d78 | -2.11578 | -50.14726 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 502bf11f-8518-37af-9e8c-b0505e7172e1 | -2.16156 | -46.68691 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e64f51d-a1df-3e2e-ac62-df58d1d84ac6 | -2.3699 | -48.56878 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ffd4ad7-9849-3dbd-9c33-4f4ce8a7aaeb | -0.91243 | -52.56818 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3740bd51-7f6f-3603-ba9d-0e8f4737ae00 | -2.36654 | -46.82652 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c24f4df-8e42-3555-88c7-3ccc0b95f763 | -2.35349 | -46.66396 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 670405ec-3da3-36e5-80b6-9abc04e265c9 | -1.54 | -54.30182 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6737eb0b-804d-3bb3-ad07-e4e8ebddd421 | -1.73311 | -47.82254 | 2024-11-10 04:36:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 539926fd-c25f-3c6d-a4f0-dadf46163fa3 | -2.62614 | -46.16029 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7e9f0a72-c687-3d30-b6b3-3de1bb2c7a7e | -2.04796 | -46.32269 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6abb46c7-80c8-3628-aa9b-64308ebaa65c | -2.27424 | -46.85695 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22e918f1-b7fa-3baf-93f1-210534745618 | -1.4222 | -52.27641 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 048c9ffc-5c9e-36e9-aa79-fed3b9e38e66 | -1.27939 | -53.71238 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 42c3fa03-3671-332f-9ba0-4e8bb680bc7f | -2.20676 | -47.7368 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23f96442-ab48-3e4b-bb37-9b66f047d736 | -1.12039 | -53.5978 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dc590a3-f54c-37d0-8bef-7d0de9186386 | -2.16033 | -48.52504 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d9a55ac-2400-3b75-b5e2-c26e6acb1f36 | -2.3101 | -47.4274 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7acde98c-ab90-3423-b650-d9b86b0cdecd | -1.23846 | -51.77914 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3b7f389-c777-32fc-b8f8-d8fdafde4dba | 2.849 | -60.08562 | 2024-11-10 04:36:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9b2c74f-69dd-325f-999b-d34d2f52f85d | -2.36202 | -46.7439 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98df1d76-a427-31f5-821f-c81e2efec731 | -2.31697 | -48.54245 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24ef5237-d16a-31c8-886e-6bb8eb459fc9 | -2.37338 | -46.73817 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72967afa-b1f1-34df-a66a-82b7a57175fe | -2.44154 | -46.32398 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 854ce65e-9275-3086-b08d-b7a3f2f978fd | -1.17845 | -53.69494 | 2024-11-10 04:36:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b7a9907-aed6-3177-be78-77d4c69c2ebf | -1.71313 | -47.97154 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 838a27a6-79f6-39aa-aeb7-eb8fa7c5d184 | -1.64284 | -50.44126 | 2024-11-10 04:36:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e7d4228-87d6-32d9-a643-ec5a698ffd53 | -2.50265 | -47.22897 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7c31b16-4272-36a3-b4be-16c72e163901 | -2.20791 | -47.7512 | 2024-11-10 04:36:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6059cbeb-b12c-3249-b667-dfe535cbc3fa | -2.12681 | -48.3753 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f56e8c41-cee2-3b70-a971-668caddfd0ba | 2.61002 | -50.86708 | 2024-11-10 04:36:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8be4401-771b-30c5-b129-1e7c7d7ffc0b | -2.30955 | -46.08636 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa9adab1-9a4a-35a7-8ccb-42dcb833a6fd | -2.57078 | -47.35224 | 2024-11-10 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ecc2200b-9d33-3690-ba7f-9dc3e5b91271 | -2.2851 | -48.42104 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3df4bcf-fe18-3d6c-82ee-33c08cba8266 | -2.16243 | -48.27853 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b7f1465-ecb2-32a1-aca5-e72e0234af30 | -2.11367 | -46.41233 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0834ead7-7f2c-3c69-9e5c-a6e17804f2a3 | -2.50387 | -46.298 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22c9bec0-0a6f-3e01-a8ac-30b6f52649e9 | -1.94971 | -46.41042 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2529c891-b764-3d94-a1f4-b473d5296a33 | -2.23611 | -48.3675 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f4492bf-5cfa-3f7a-8238-863cd710e39a | -2.27654 | -48.71275 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 015e33ed-8366-3bb6-81ff-f8ffc6700041 | -2.39575 | -46.17401 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 01023233-6521-361b-a9f2-e641c9a2445c | -2.56423 | -46.5405 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8482eff-decc-32fe-901d-b3da2607ba25 | -2.66689 | -46.77877 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2dc73a9-1be9-3e70-980c-5ac677262e3d | -1.24148 | -51.7841 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53808d84-5dcc-39c8-8d5b-4e1839a2dd90 | -1.58188 | -48.02899 | 2024-11-10 04:36:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35e845cb-d875-343a-ac00-87532c196572 | -1.32211 | -54.17716 | 2024-11-10 04:36:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdb01148-14ab-3a42-b065-2fcb4a140200 | -2.56742 | -47.35172 | 2024-11-10 04:36:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a064e485-9395-3f44-8520-32d222403fa3 | -2.6385 | -46.8043 | 2024-11-10 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93739512-3e1b-33cc-8c12-7ae528a7f620 | -2.28837 | -46.85546 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aadb37cb-b10a-36ba-8fbf-b52cde5ec20a | -2.17647 | -48.37939 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f375c60-b0ee-3076-97e5-435ff224a7f0 | -2.0951 | -50.21574 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a7676314-31db-3ba0-9fcb-bad19fee081e | -0.97705 | -53.71437 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbe6ff45-81fb-3e7c-893e-2a9da4978f08 | -1.65757 | -51.91036 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2d48de76-7d2a-30be-b80c-5611ef1cc478 | -2.26402 | -48.27657 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 825d0cf6-6ee6-38bb-b1f8-f1331b5ef3b7 | -0.03974 | -50.77071 | 2024-11-10 04:36:00 | NPP-375D | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70191e65-9fa8-330b-9159-f142a07e218b | -1.38159 | -51.44365 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f7178b8-aad1-3b43-bf1e-aec40fd74bd3 | -2.29174 | -48.81064 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a7a55e1-df59-3cae-a45c-667942ccd25b | -2.32245 | -48.52918 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ba092a-ce06-37dc-b22b-dda978589274 | -2.00224 | -48.99276 | 2024-11-10 04:36:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64133cc1-9577-3344-a893-6891711b2dbb | -2.03967 | -51.16725 | 2024-11-10 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f389c65e-1e66-39f7-a7b7-c5042e9f35a7 | -2.35919 | -46.67233 | 2024-11-10 04:36:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41cf2282-f39b-3925-8681-7390f4a5f2a4 | -2.17701 | -48.37595 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6a452c5-3093-32f4-b9dc-61c2b2168479 | -1.58675 | -52.18436 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60ddcab9-de49-3eb5-8f9d-5d111dfe703f | -2.62364 | -46.16853 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1db25459-f1e1-3ebc-b6dc-8cc909702127 | -2.15471 | -48.28439 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13ed046c-6cb5-33a0-8cbf-9039d8d1c14d | -2.23022 | -48.42655 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a849095d-1765-307c-9e84-cb5671701fe4 | -2.08757 | -50.38963 | 2024-11-10 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57bc52d1-47b9-3063-ad67-741a3b0aaf08 | -1.24195 | -51.75722 | 2024-11-10 04:36:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1d78dc22-3942-3450-85de-00acd11bd375 | -2.16059 | -48.39819 | 2024-11-10 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0beff66c-f1bb-3bd1-b978-45115fc78262 | -2.41307 | -48.40257 | 2024-11-10 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25509ef1-8ff1-335a-b30d-b64df4662dfd | -2.33431 | -48.94529 | 2024-11-10 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28ec7dc2-f149-3087-b16d-37b6aa2aadea | -1.45877 | -52.55543 | 2024-11-10 04:36:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7ddab66-c22a-3e2c-912d-3c47a882a608 | -1.75874 | -52.68013 | 2024-11-10 04:36:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b88e60-dfae-3423-aec6-66c4b74d594f | -2.51878 | -46.36199 | 2024-11-10 04:36:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 667a8ab7-fb6c-3f85-83e5-967dfb51b2cf | -2.39922 | -46.17454 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ababe26-7ef2-35ea-a333-5ac6622d46a2 | -1.16281 | -52.08355 | 2024-11-10 04:36:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 471772ba-a274-32b4-9b56-8a79eb190876 | -2.62618 | -46.13668 | 2024-11-10 04:36:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3694ac0d-49b9-3e20-a0e1-ef28dae9f264 | -1.99617 | -46.36057 | 2024-11-10 04:36:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README62.md)
