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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f45b3fb0-8af6-32de-9fe7-a95a8e386f6f | -5.6732 | -44.309101 | 2026-07-08 00:53:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 47a6cf87-b01a-3e2e-8563-584873379dbf | -6.9134 | -43.709099 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c2e37b06-9728-36ed-b3bf-823d0719cd1f | -19.621799 | -47.584202 | 2026-07-08 00:53:00 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e3b68b8f-dcfe-3778-9101-f3e77d4c046a | -18.085699 | -54.032299 | 2026-07-08 00:53:00 | METOP-C | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2ce35e00-6156-325d-a6b7-0e1e1f910670 | -13.953 | -45.2393 | 2026-07-08 00:53:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 14c15df3-aa6e-3472-9927-76032380906e | -8.1214 | -47.8792 | 2026-07-08 00:53:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 148ca195-de32-3e71-aa08-e96aa4c6839f | -21.3641 | -49.169601 | 2026-07-08 00:53:00 | METOP-C | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a0ffb6f0-687a-394b-87c6-98a802ee7272 | -6.9467 | -43.7187 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| dbf9a944-e75b-38de-8b3e-640ea615af7f | -5.7955 | -43.8022 | 2026-07-08 00:53:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d19ad3c4-8f1d-38e0-a41d-a892943ad416 | -21.7966 | -56.263901 | 2026-07-08 00:53:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 91d57bd7-8261-3ac6-8285-108ec2011f49 | -9.2144 | -48.572899 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ebdf0bf-d9bc-38c1-b79d-268cca51fe6f | -14.1503 | -52.8825 | 2026-07-08 00:53:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef7e8bdb-c85c-3501-b30b-8d2721221eb9 | -10.8734 | -46.348301 | 2026-07-08 00:53:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6449f0d6-cf8f-3fb3-abf6-a49d31fbf646 | -6.4333 | -55.796799 | 2026-07-08 00:53:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f3a6c25-88c0-381e-b4c0-b093ee50d8de | -13.5435 | -49.300499 | 2026-07-08 00:53:00 | METOP-C | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b1ac43c0-fea4-3114-83ac-2060d4f1dde0 | -12.5058 | -48.253101 | 2026-07-08 00:53:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 702293cd-259d-3a10-8ada-5e7f8cc3c469 | -8.1974 | -49.476398 | 2026-07-08 00:53:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd40e66d-8f53-32f9-b9d6-ef2b2e85d5fe | -13.9478 | -45.2183 | 2026-07-08 00:53:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f638d212-e941-3e91-beda-20d06c8cd543 | -6.9425 | -43.701801 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4c744724-50b0-35e1-b9c8-4d31fcf5a34b | -6.9231 | -43.706699 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 316f712c-3f3a-3691-9183-694c5c78b669 | -9.7347 | -49.031101 | 2026-07-08 00:53:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 211b70c7-d8de-3248-b7a0-16edfda5eaa9 | -13.5357 | -52.933498 | 2026-07-08 00:53:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85100fdb-daf0-34c6-9b8f-b850eebf2796 | -5.6635 | -44.311401 | 2026-07-08 00:53:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0ed4aa-b30e-3391-bae8-023252e52e41 | -5.3416 | -44.7202 | 2026-07-08 00:53:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd181eb1-8c59-3df9-b6f3-eeac496f2b74 | -17.2815 | -50.023602 | 2026-07-08 00:53:00 | METOP-C | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b28d7fba-7313-3c06-a210-dcfed8c7ee09 | -21.3724 | -49.159801 | 2026-07-08 00:53:00 | METOP-C | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 92cd6852-c2dd-3441-b7c3-a41c82df6fb7 | -14.1422 | -52.8927 | 2026-07-08 00:53:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b00d69d1-7d48-3aa0-9dfd-066d5c63b9a9 | -21.808901 | -52.712399 | 2026-07-08 00:53:00 | METOP-C | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9abd8622-ed39-3af8-a72b-e7bd3ea8951f | -9.2382 | -50.138901 | 2026-07-08 00:53:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c6a860-348e-3179-8f85-430efea96e09 | -16.736401 | -49.422298 | 2026-07-08 00:53:00 | METOP-C | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a3d66b74-ec2f-3885-8323-749b9ba09fc1 | -6.4983 | -42.2103 | 2026-07-08 00:53:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e83def1a-75fb-3dda-948b-dff915f7bad2 | -8.5933 | -47.997002 | 2026-07-08 00:53:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f80dd71-32e3-3c3f-be52-552a241839f7 | -22.285601 | -46.857101 | 2026-07-08 00:53:00 | METOP-C | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1c537835-4da3-3ab3-b498-a979e42c6d32 | -8.5993 | -48.022598 | 2026-07-08 00:53:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea89134-3877-382e-a469-3dfecd64b6be | -17.541 | -54.0079 | 2026-07-08 00:53:00 | METOP-C | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5940c5a7-7c09-314d-b2d3-892750c4c5ce | -5.6692 | -44.292999 | 2026-07-08 00:53:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 16cfc88c-716e-3d2b-a251-48dd712ff66c | -13.2847 | -45.172901 | 2026-07-08 00:53:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9b162593-ecd8-39ee-bfef-475f9de14682 | -8.0736 | -45.577801 | 2026-07-08 00:53:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c956e0d6-6b69-3fac-bbea-df3d817cbbea | -9.3712 | -48.801201 | 2026-07-08 00:53:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| abee7086-b8fa-3dd6-aff7-6118c5f1ea3d | -21.7994 | -56.2803 | 2026-07-08 00:53:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 747b26a7-5689-3988-b0b2-a2b7373665a4 | -12.1375 | -48.267899 | 2026-07-08 00:53:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afefdcb1-c712-3c06-b52d-98d1aa1d7aba | -14.152 | -52.890499 | 2026-07-08 00:53:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 65373521-9629-3a6f-9734-cb9b17d4df72 | -6.8489 | -50.648399 | 2026-07-08 00:53:00 | METOP-C | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0befebf6-8cf6-34ae-b072-7fd8c236ea1a | -12.8522 | -44.3913 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f92a54b-2032-3b35-9b1e-f77a10785de1 | -6.9328 | -43.704201 | 2026-07-08 00:53:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98076da8-658f-35df-9c7e-ca8bba49b90f | -12.1357 | -48.260201 | 2026-07-08 00:53:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc968e59-15d5-37c7-aff8-0726d7d7242a | -12.3518 | -47.425701 | 2026-07-08 00:53:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d8589f4-9b84-38c0-a51e-c69d1df0ec57 | -9.226 | -48.578499 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 066f7d9a-f205-3df7-80d0-2ca550fcc918 | -9.3796 | -44.720299 | 2026-07-08 00:53:00 | METOP-C | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e60a9f08-a560-32e7-b8e2-aac70639972b | -9.7445 | -49.028801 | 2026-07-08 00:53:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da642dee-0adf-3ac6-a2f4-1ba3b0aedebe | -12.7545 | -44.4557 | 2026-07-08 00:53:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f77849a6-8915-3db8-955b-2a08c44c6d8a | -8.1309 | -47.0961 | 2026-07-08 00:53:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6eb99788-f5a8-33ef-987b-9e3df2382647 | -9.2181 | -48.588799 | 2026-07-08 00:53:00 | METOP-C | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d90a3f1f-96bf-3b7c-9d90-2ce5e1a19371 | -5.3092 | -47.243599 | 2026-07-08 00:53:00 | METOP-C | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f1433421-ef98-3ae8-ae79-64722ad9f691 | -20.1099 | -53.348 | 2026-07-08 00:53:00 | METOP-C | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| dc3ab5d2-03d6-338a-a37b-bd26224c89f3 | -13.4753 | -49.9063 | 2026-07-08 00:53:00 | METOP-C | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| afb28323-837a-3402-98a2-c1fe804318a7 | -9.2398 | -50.146 | 2026-07-08 00:53:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73972fdc-48b3-38b5-8dc5-1a2285c22e6e | -1.828 | -54.481602 | 2026-07-08 00:53:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3fe1e3-65ca-365d-b9fa-a76e2a1125be | -13.5391 | -52.949501 | 2026-07-08 00:53:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 085dc3d3-c6a8-38f6-9e8a-d6454f1726bf | -12.7566 | -44.449 | 2026-07-08 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.7 |
| f8a5eb61-0c8d-3b19-bca4-48bf9f91033f | -21.0705 | -47.2568 | 2026-07-08 01:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 2904c064-6af4-36ae-a29c-2a4feb488e8f | -13.9589 | -45.2251 | 2026-07-08 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 5503876a-8daf-3540-b23f-6aa74cbde7a0 | -12.7373 | -44.4521 | 2026-07-08 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 6fb3c006-f531-3e6e-a80b-2576000863d5 | -9.2258 | -48.5782 | 2026-07-08 01:00:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bb311646-17ac-3ffc-9c38-998dd81e77a6 | -12.7562 | -44.4724 | 2026-07-08 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 9a775623-d9cc-3e00-b689-5070db694dd0 | -21.7827 | -56.2762 | 2026-07-08 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 57.0 |
| aefb9e53-a404-3c67-aa45-9c4aa29b6afd | -21.8033 | -56.2729 | 2026-07-08 01:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 964ce1db-0781-3ed5-a52c-89a094fb98ac | -5.6701 | -44.3147 | 2026-07-08 01:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 1cb944ca-9175-3827-b48a-1cec6fa470f7 | -21.3642 | -49.1664 | 2026-07-08 01:00:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.5 |
| 64a13c95-7419-354b-bafc-e4a27231609e | -5.6701 | -44.3147 | 2026-07-08 01:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9f6d2d5c-989f-3385-8319-cbecbe2d6cab | -21.8037 | -56.2514 | 2026-07-08 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 43.0 |
| cee003eb-4262-3eea-aa5f-2642731eef76 | -12.7566 | -44.449 | 2026-07-08 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 929e6289-276c-3490-864e-a09ea367f599 | -21.0705 | -47.2568 | 2026-07-08 01:10:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 975c7019-48da-38bb-9b6c-704628326d1f | -21.3642 | -49.1664 | 2026-07-08 01:10:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.7 |
| 1e674640-fb10-30e6-a0e5-31aa7bdeb2f2 | -9.2258 | -48.5782 | 2026-07-08 01:10:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| dcbe9383-9dcb-317f-97b7-0b9d798af769 | -12.7373 | -44.4521 | 2026-07-08 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 66c846a8-ef52-3e2b-bbb7-ceb882eaaa08 | -21.8033 | -56.2729 | 2026-07-08 01:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 801f7b44-81ed-3475-a29c-6f76fa40c6e5 | -12.7566 | -44.449 | 2026-07-08 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 14d24f07-2262-3b6e-b215-8baa3b87c405 | -12.7373 | -44.4521 | 2026-07-08 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| fae9ef53-d311-3c06-bf2f-5ae7b66d405d | -9.2258 | -48.5782 | 2026-07-08 01:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e01e47d3-7013-302d-8d6a-f44f4fbf9ff0 | -21.8037 | -56.2514 | 2026-07-08 01:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 5026947b-90b2-3ec5-bd3f-51e964fe4f5b | -5.6701 | -44.3147 | 2026-07-08 01:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 90.0 |
| bcbb9223-4c6a-3fac-883c-eb3868ce8e5e | -21.8033 | -56.2729 | 2026-07-08 01:20:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 3ddf1770-60dd-376f-8bfa-7f6104364de6 | -8.7267 | -49.446 | 2026-07-08 01:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 6fc798d9-eac6-34ba-ade4-b9ba3e051dc8 | -21.3642 | -49.1664 | 2026-07-08 01:20:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.5 |
| dc1fb40d-1f24-3648-9f25-05bd72df2b52 | -21.8033 | -56.2729 | 2026-07-08 01:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6374ece6-11b1-37af-8a3d-de1c96924d8d | -8.7267 | -49.446 | 2026-07-08 01:30:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 648b6183-023f-357c-a133-3ad47c604362 | -9.2258 | -48.5782 | 2026-07-08 01:30:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 4af95623-f309-3dd6-8726-88548f719390 | -12.7373 | -44.4521 | 2026-07-08 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 828b4402-2cb3-3562-8fb4-f8e784c1c599 | -5.6701 | -44.3147 | 2026-07-08 01:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| bdf09126-81bb-3f97-909b-bd6a100c4ac8 | -21.3642 | -49.1664 | 2026-07-08 01:30:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| 9d227737-bf3f-3589-8f61-453902857a68 | -9.553 | -40.3503 | 2026-07-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.5 |
| 4409f46f-0c8a-3e51-919d-138ca033dc2c | -9.5534 | -40.3254 | 2026-07-08 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 126.7 |
| d8cab34b-e98f-34bf-ac8f-fc404d38ea47 | -21.8037 | -56.2514 | 2026-07-08 01:30:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 4fd151fa-03f4-33d6-b56e-d180c42cb757 | -11.3955 | -46.5794 | 2026-07-08 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 91de6aaf-9300-3701-bc50-1e4068592e52 | -12.7566 | -44.449 | 2026-07-08 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| f51b0b5d-3484-35d8-a17a-d6410b6b1fde | -5.6701 | -44.3147 | 2026-07-08 01:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 872b830f-9d7e-379b-a3d8-8f9321eba567 | -21.3642 | -49.1664 | 2026-07-08 01:40:00 | GOES-19 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| 155e4da2-716f-3cf2-a1e7-f491215c5c81 | -9.2258 | -48.5782 | 2026-07-08 01:40:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c35c24f0-d234-37a6-b91d-0c262a8bf2c6 | -21.8033 | -56.2729 | 2026-07-08 01:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 103.2 |


[Clique aqui para ver as próximas entradas](README6.md)
