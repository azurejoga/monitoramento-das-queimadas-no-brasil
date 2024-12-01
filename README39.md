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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 817e1146-5bcf-369c-b02a-a21b9431eab7 | -12.9322 | -48.62543 | 2024-12-01 04:25:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42557aa3-0b73-36ef-8146-fe94c684d277 | -21.09183 | -51.58704 | 2024-12-01 04:25:00 | NOAA-21 | NOVA INDEPENDÊNCIA | SÃO PAULO | Brasil | 3533205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 26034e87-a989-3730-85cc-810d7a4f422e | -29.87465 | -51.15756 | 2024-12-01 04:27:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 1ebc6451-8224-3b13-94d0-71b5118c07d3 | -30.06307 | -51.08421 | 2024-12-01 04:27:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| bd271347-885a-35b6-9584-84b58c0ad442 | -30.15215 | -52.02596 | 2024-12-01 04:27:00 | NOAA-21 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| c340a9f5-65d2-3ac9-9a19-3b1b4712e568 | -6.9344 | -43.5401 | 2024-12-01 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 097e8b02-9261-3045-9ff3-9e30f5141b06 | -4.5562 | -43.3028 | 2024-12-01 04:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 8927765c-822c-3ae6-aa9f-7c2a36ff124d | -4.0052 | -44.7596 | 2024-12-01 04:30:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 92f77a50-d3c9-3b19-9133-f934a0d2b162 | -4.5563 | -43.2795 | 2024-12-01 04:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| dafcfe82-1f95-3cd4-9efd-c4fb0b4ba692 | 1.1439 | -55.9871 | 2024-12-01 04:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 249c7913-24b0-354a-8ad9-03e49d34028c | -10.6674 | -44.4835 | 2024-12-01 04:30:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.5 |
| cf5e78f0-b792-3cbd-bc16-57e54c72a079 | 1.1622 | -55.9869 | 2024-12-01 04:30:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| cf597506-ff43-3391-8b79-5790e6bbbd5b | -3.2591 | -53.6186 | 2024-12-01 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 88a9787f-bc8e-3ccb-ba9e-8ea2cd143463 | -3.259 | -53.6388 | 2024-12-01 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| fee1d584-bfa4-337d-a4a0-0de199fd6e82 | -2.9778 | -45.5713 | 2024-12-01 04:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0b2e26da-4818-3a10-8f85-d254adb1ce66 | -2.9963 | -45.5706 | 2024-12-01 04:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 67bbaba2-75dc-3f42-aab9-38b3b057afa4 | -3.4974 | -53.8339 | 2024-12-01 04:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 307cc564-f060-35d6-b26d-5e0b52aaba55 | -4.5578 | -45.7232 | 2024-12-01 04:30:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.4 |
| af642214-aa1f-393b-b886-525510e30357 | -4.5578 | -45.7232 | 2024-12-01 04:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 59ac89bb-c381-3931-b863-2f9eae1730d6 | -3.2774 | -53.6383 | 2024-12-01 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9d6b0046-cb4a-3b3f-af6a-3c9932f5ff6c | -4.0052 | -44.7596 | 2024-12-01 04:40:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 1734bc60-9a09-32a0-af9b-c2cc81fce44f | 1.1622 | -55.9869 | 2024-12-01 04:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ba7b48aa-aa5c-3c94-afa7-571f1b28d3b1 | -4.5562 | -43.3028 | 2024-12-01 04:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 7ce024d5-f24d-3085-bcca-e54e45dd9165 | -3.259 | -53.6388 | 2024-12-01 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5cb07cab-e0bd-38e6-ae88-d465d7329646 | -4.5563 | -43.2795 | 2024-12-01 04:40:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| acf47171-cfb9-39a3-84b6-8272807ab97e | -4.0054 | -44.7369 | 2024-12-01 04:40:00 | GOES-16 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 5b698126-7858-318e-b5a8-eafda47dc57b | -3.1273 | -54.5264 | 2024-12-01 04:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| d7edc5b9-433c-3baf-9a4a-297d4b86a88c | -2.9963 | -45.5706 | 2024-12-01 04:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 0ec2c306-c3bf-3ee3-bc66-ad461082a29c | 1.1439 | -55.9871 | 2024-12-01 04:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| ec21cbf0-b60b-3d90-9117-4e8db30dccea | -3.2591 | -53.6186 | 2024-12-01 04:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 504b7d72-2d33-3dfc-843c-cb57dd70d9a8 | 1.14076 | -51.14739 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ccfa274-a938-3ac4-84a7-e3e1eaf3658f | 1.17 | -55.96416 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3c38f23-2314-3f82-aac5-8af872ee7f0e | 1.64098 | -50.95113 | 2024-12-01 04:42:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d1052cd-f01e-3cf1-a464-04f06293f3de | 1.15094 | -55.99353 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 1cb34170-9317-3f6a-ba98-7e34899d7e64 | 2.73592 | -60.39718 | 2024-12-01 04:42:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 387b1f82-6861-35c5-ba6b-44df777d9fac | 1.24916 | -50.6808 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8db3eaf6-c7d5-3094-ae4a-ec3eb7574c57 | 0.34877 | -51.0846 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fab99c4-64f2-3c73-8e5d-fe67d392ac6c | 0.8367 | -51.85121 | 2024-12-01 04:42:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bcc27ed-aa9d-3d5e-b699-7d8351fe6234 | 1.16615 | -55.96944 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 672367da-08ad-3510-9918-ea4e639e7ac5 | 0.98485 | -50.07061 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e68ddf73-d6fd-34b3-88a1-6b44f631ad43 | 3.27595 | -60.07411 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f93a49ae-bce5-38a8-b08d-d2cbab54730f | 1.15787 | -55.97847 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4df7676a-6dff-3099-8b14-ced768dc85ef | 2.15924 | -55.76963 | 2024-12-01 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7709f11-b185-39e7-8593-7590eec37807 | 1.17769 | -55.95363 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0eda336-bb0f-3ce8-aeff-0f04e6b01a87 | 0.97764 | -50.06816 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a54fac7-cedb-3212-a167-efd80d76f21b | 1.15236 | -56.0026 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a192ed55-9c19-396f-b59e-27447d599ef6 | 3.26948 | -60.0838 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 144ec26b-299e-34ad-b412-065166e40388 | 0.32883 | -50.78177 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a07384a-b4c1-3877-8847-1021828b4263 | 0.63014 | -50.56773 | 2024-12-01 04:42:00 | NPP-375D | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1c68479-f1dd-3b56-8d7e-945abd15f313 | 1.17724 | -56.0126 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00b09179-0568-3faa-8f14-48203c2129b0 | 0.97696 | -50.12896 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84067761-f5cc-325f-ac40-a2a5626023e8 | 3.27047 | -60.07968 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91764afb-fcb2-3723-9753-927d5532ccfd | 1.17755 | -56.01421 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f30cb08-22cf-34a0-9641-27782b59b197 | 1.16932 | -55.96267 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f3ca6c2-02d8-3a02-9803-00078aadb4d6 | 1.25422 | -50.69104 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82860841-de12-3aec-8b0b-5b85d7fcbace | 1.17342 | -56.01789 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f448e22-abdf-35ff-9289-397f978aaea9 | 3.26881 | -60.07909 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b5a91d72-2950-3432-b127-5e8586efdd2d | 1.17652 | -56.00804 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 352da7a6-5f8f-3867-8561-f04b96b68792 | 1.15762 | -56.00642 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77d9e6d4-4587-3a55-9fcb-526e7630b370 | 1.14711 | -55.99881 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66fd387e-c748-3a03-987c-2f6a446c524f | 1.17686 | -56.00965 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3cba14f4-cb24-3947-b4af-19648fb5dbb1 | 1.16169 | -55.97318 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 002a3e63-2884-383f-92da-111962684507 | 1.15405 | -55.98374 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ccf8b96d-b9ca-398a-b41e-af75cd911114 | 1.17766 | -55.95671 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03aaec4c-e461-311f-924a-8d8c12828e0f | 0.98309 | -50.12443 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eedf6370-caa7-3e01-9660-87e9ec0d3cf4 | 0.97975 | -50.12495 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c68edba-e29b-35f6-afae-4ada434e2dd1 | 1.15023 | -55.98899 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5eda9806-e35c-3b0a-a64c-027c9121f27a | 1.19373 | -55.9371 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c22f7964-f438-3531-b1c8-f498008bc50b | 1.67941 | -50.66257 | 2024-12-01 04:42:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c12b4f4-2ae7-3af0-9580-0e5abdb30f9b | 1.67207 | -50.66002 | 2024-12-01 04:42:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 188ace1e-b99b-3047-9001-9202427ba5df | 2.20201 | -55.80534 | 2024-12-01 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 774acbb6-16f5-3e79-9425-da3b72bc2a08 | 0.9803 | -50.12843 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d854654f-8ba2-304b-bafe-a828b8f1ed0f | 0.97641 | -50.12547 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8edb4af7-d2d3-31ca-a4cf-283d9828a188 | 0.18224 | -51.4025 | 2024-12-01 04:42:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ac2f4a6-2eca-30c7-9889-2701403f7ec6 | 1.67659 | -50.66671 | 2024-12-01 04:42:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9ca0a2b-7cf1-3e5a-88cb-312a428f7993 | 1.25254 | -50.68027 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2045ed9-4e59-3a83-bacd-4d0b0f4d0706 | 1.16001 | -55.99203 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25892903-1d4b-394b-8020-8b354cf2dfdf | 1.94465 | -50.81883 | 2024-12-01 04:42:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 662811fc-7a95-3444-96f9-0732df3152ef | 3.27566 | -60.08282 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f41620fe-1afd-3a70-85bb-02968412f907 | 1.15715 | -55.97392 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 491f58bd-dbc5-3d5d-8f96-7da716de06af | 1.14782 | -56.00333 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4fb85a95-e865-3208-a181-bf0db4ff7a5d | 3.27187 | -60.08907 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13a6e64b-8965-3a1e-ba7c-630157d662e6 | 1.14419 | -51.14685 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e37c4170-a8a3-3bdc-911d-b219a100f6a2 | 1.1464 | -55.99427 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 01b6e041-15db-3585-8a92-2930e62302cb | 3.26431 | -60.08069 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0777e0cf-f276-3896-833f-fd8ff4d8a8cb | 1.67602 | -50.6631 | 2024-12-01 04:42:00 | NPP-375D | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 944d5813-a313-36e0-8492-fd7af6cda2e9 | 1.18542 | -50.87495 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcb0023c-9a4d-3dea-aeae-791fe220c845 | 3.27015 | -60.08852 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9736cc20-4086-3770-aefd-edbb71315151 | 1.25704 | -50.68693 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 01382307-17b8-3fa9-a869-099b0ce21e80 | 1.14257 | -55.99951 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70cfab10-1c33-3c45-9270-eff025079aa6 | 0.98097 | -50.06765 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 845ac45e-669b-3a46-91b2-029667596bf9 | 1.1593 | -55.98753 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91a8a1f6-ab17-3e7e-81cf-2106c709ee59 | 3.27117 | -60.08436 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 479343a6-b803-3c3c-996a-a89cf84a9c06 | 0.98431 | -50.06713 | 2024-12-01 04:42:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6298e05e-5d58-30f3-ad91-55157d410247 | 1.15477 | -55.98828 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 7f8c2266-066e-3aa0-a621-ad0406014089 | 1.18202 | -50.87548 | 2024-12-01 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1495d399-eb13-3e34-874a-acec05b42ad1 | 3.26501 | -60.08545 | 2024-12-01 04:42:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7317e4a0-3de9-3982-8abc-b4c6dbd04b1c | 1.173 | -56.01497 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bd38a2a-8b3f-3e01-b64a-dd07b966cde1 | 1.14569 | -55.98971 | 2024-12-01 04:42:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e290b045-2942-356d-802e-34ded6155dc4 | 2.74145 | -60.39128 | 2024-12-01 04:42:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README40.md)
