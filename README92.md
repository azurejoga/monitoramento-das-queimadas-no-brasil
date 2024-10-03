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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fef47ff-aa86-3263-a598-ab4898fcd808 | -13.20308 | -48.64495 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eba3145b-ec4c-39fe-b833-22ef029625e3 | -13.20308 | -48.51686 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 918f9f06-6d5b-3da2-8602-5673198029be | -13.20252 | -48.52038 | 2024-10-03 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d022fe8e-a723-3fa0-8c3c-db56799e4b9d | -13.20214 | -48.60813 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3d075a0c-6739-3510-8528-ef7a5db26ce9 | -13.20158 | -48.61166 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7004c9e6-afc8-3cc9-9886-3f5df6a21fc9 | -13.19976 | -48.64439 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2922308f-3f79-3cb3-a7db-577ffbd847c2 | -13.19882 | -48.60759 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6c3e75c9-620c-3092-bad4-1200453f4ee6 | -13.19826 | -48.61112 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e66d5c86-7d9c-332f-ad02-85591b3e1d57 | -13.19804 | -48.65517 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b542ecc0-8e41-3c8f-a113-5a4fda2d6983 | -13.19644 | -48.64383 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ab35c66-b067-337d-9ce2-ad9a57f36a1b | -13.1955 | -48.60705 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5a12b4b-8fe9-3c08-9471-504752732556 | -13.1953 | -48.65102 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0f4ba1eb-808c-369e-86e5-b9ac92b9902e | -13.19494 | -48.61058 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c41643f0-3a54-30b9-9375-2d77fa2c2aa7 | -13.19472 | -48.65461 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a4094317-2e0d-35aa-84f4-8f9845685dfc | -13.19437 | -48.61414 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7ab2718-362f-3be0-9b9f-3b03c2972bbf | -13.19427 | -48.63612 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa6d8f7d-bdd5-3512-a3c6-7635d841f4b6 | -13.1938 | -48.6177 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 822c3e47-3e34-3389-86ab-75f8bd6148ca | -13.19369 | -48.6397 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 480a746e-bce6-3e5f-9548-6205c5420425 | -13.19323 | -48.62128 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4d0b6073-c07d-3ed5-bb9c-441c4350630b | -13.19312 | -48.64328 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 70436bb6-dd19-3205-8838-188acb009036 | -13.19266 | -48.62484 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 27fc77a6-513f-3f5c-88ec-5dd8921f57b0 | -13.19209 | -48.62842 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31a09958-dfbc-3115-a023-0324dd12b0e5 | -13.19198 | -48.65046 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 312821c8-7c4e-371b-a87f-536ddc58c39c | -13.19162 | -48.61005 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc337d5b-e005-33ab-817d-7dc09a3573a3 | -13.19152 | -48.63198 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c3bc1e2-9fa7-3f2b-a6f2-2d90dbf1c770 | -13.1914 | -48.65406 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 48997f58-2556-311b-beae-f306a9ad23f4 | -13.18886 | -48.60598 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b869cb6-1250-3b0c-8d4a-7a1896dd9968 | -13.18866 | -48.6499 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a26e12d3-bf01-30f6-a6c8-1a281b56e454 | -13.18829 | -48.60952 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 154796b7-60a1-3a20-8f87-54271f922948 | -13.18808 | -48.6535 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f67cd24b-4605-39c8-9aa1-89fb9051f0c0 | -13.18554 | -48.60543 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 605e84b0-58fa-3f93-b90c-072ef68d00a8 | -13.18497 | -48.60898 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeb57e96-8706-3ebd-b352-9bb6fc8e2735 | -13.18476 | -48.65294 | 2024-10-03 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a98789e-09ef-3946-b322-17b54c0a166a | -13.26754 | -48.58273 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 61bbe412-6da7-3584-af37-e23129062349 | -13.26697 | -48.5863 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f876b12f-33f5-39b0-ae56-b265688e8c4f | -13.26423 | -48.58218 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0cc54568-a221-34f3-b7a1-a633806a2dcb | -13.26365 | -48.58575 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 51c507b7-5bb5-3eca-9880-6e10d2751426 | -13.26308 | -48.58932 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00759508-fa14-3d6a-9aaa-6be7c88cb189 | -13.26091 | -48.58163 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45590361-0459-3110-b379-4c96018465ae | -13.26034 | -48.58521 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f07e42f-9311-36f5-896f-4e71131731f9 | -13.25976 | -48.58878 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72117556-97e3-3225-8bac-0f720cf1a13a | -13.25645 | -48.58824 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb041ed8-f378-3b6b-8a61-ce2506140730 | -13.24924 | -48.59071 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49817552-d06d-36f3-8300-3ebb4ae7d756 | -13.24867 | -48.59428 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 346632d3-2383-3959-9b17-00e095034fae | -13.24478 | -48.5973 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5281e2f0-f9f1-3705-896d-51125f250098 | -13.04506 | -48.61148 | 2024-10-03 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db3f7d9d-12e5-3aca-929f-4eac69e2591a | -13.32513 | -49.31858 | 2024-10-03 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d367e5b8-ff79-3f1a-bfe6-ee1f181c1fcc | -13.32042 | -49.31434 | 2024-10-03 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5f953c1-2b40-36f9-bd6d-bed3df24bf86 | -13.31706 | -49.31371 | 2024-10-03 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d41a9fd-f178-307f-be77-fb6ef1a76d31 | -13.31429 | -49.30951 | 2024-10-03 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7faa0faa-164f-3cde-a217-44cba93dac2b | -13.31371 | -49.31308 | 2024-10-03 04:27:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 114c1318-99b4-331c-ae07-9719b6da7940 | -12.49403 | -48.6077 | 2024-10-03 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb404f93-b2dc-376a-9dc1-ec4e0e671d73 | -14.49581 | -49.28732 | 2024-10-03 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 92f1f624-fede-358e-982a-be443bc3f89a | -14.49523 | -49.29092 | 2024-10-03 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c4d647a7-6501-3269-aac7-ffc9a19e305a | -14.49247 | -49.2868 | 2024-10-03 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| b8baae4d-e48f-3a12-8964-edeea39060e5 | -14.49189 | -49.2904 | 2024-10-03 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9ca37497-67e5-3b4f-bfdb-50fccc05b63c | -14.48912 | -49.28627 | 2024-10-03 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd1ce408-75d0-33cd-b360-fd85d64d6698 | -14.48854 | -49.28986 | 2024-10-03 04:27:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd1f6afc-f5cd-3168-909b-9bcaace9e0d1 | -14.27021 | -49.66389 | 2024-10-03 04:27:00 | NOAA-21 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b82443cf-bd26-35a8-b9d2-e0ab24daabee | -14.8267 | -48.7521 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aff76587-1d2a-31d9-a708-852519677850 | -14.82666 | -48.77445 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c379e3c-9026-3736-ac4c-8eea354fc77f | -14.82609 | -48.778 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84878435-f909-3f4b-a453-c6c8b61ede29 | -14.82444 | -48.76627 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 097023a0-c572-3f4a-9447-a3522eb162d9 | -14.82388 | -48.76982 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fd42579-c063-37dd-8116-b7170e0c6b85 | -14.82339 | -48.75153 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 163c1018-8676-3add-b4ee-de978d39b6f1 | -14.82331 | -48.77338 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69e13b66-2b15-3e55-b523-82504555d138 | -14.82275 | -48.77693 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| feb746ae-dbdf-3291-b8d0-697f254d277e | -14.82218 | -48.78048 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8f4a5c2-84b7-3f0d-82ec-3f54cf5c131d | -14.82114 | -48.7657 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 056404cb-687a-3f5d-8e08-5177fec846d1 | -14.81783 | -48.76516 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dc1cd80c-2a69-305b-ac63-4d29e3e19eae | -14.81678 | -48.75042 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5625ed04-884f-3a45-bedb-aece0fee91fd | -14.81387 | -48.78997 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2133f9e2-91b2-30ca-a220-4861d260f81e | -14.81346 | -48.74988 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae6cab2a-98f8-3ea2-bf35-9ce91be65495 | -14.81331 | -48.79352 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3efbb23-d4b4-358e-8a88-08857dffcfd9 | -14.81274 | -48.79709 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6c02bef-453d-316d-8c71-ae506db05ea6 | -14.80943 | -48.79655 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edb4e4ca-362c-3312-b204-4e213c078dc2 | -14.80612 | -48.79602 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 72236666-91d0-36a1-8f85-ed5919db2dd4 | -14.80281 | -48.79548 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8e5180f4-f8e6-3da9-a94d-17dcc2351db0 | -14.80223 | -48.79909 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f79bd8ab-36ba-36b4-b607-f75d1c67a53e | -14.7995 | -48.79493 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1417e68a-a795-3335-b930-5f62e08bc243 | -14.79892 | -48.79853 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d32efacc-3a40-3838-8594-945b93369500 | -14.79504 | -48.80158 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 4691625b-a18f-3b51-a775-9429f52df257 | -14.79173 | -48.80104 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ceae4c5d-bac7-3828-afb0-12244ad072c7 | -14.78842 | -48.80049 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 26c62f3f-dcfb-3046-abac-9f8442665de9 | -14.7851 | -48.79995 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1f64055-04f6-3385-9d07-34365d66a2a0 | -14.78179 | -48.79942 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25f2153d-7024-318c-8656-39f6c092ce36 | -14.77847 | -48.79888 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ae1e72-1749-3f75-bdc4-b21703c906ad | -14.76797 | -48.80081 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb78b3fe-e6d6-3107-932b-59159f1d056e | -14.76739 | -48.80442 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79da8165-c84e-3489-b546-09fdd46f5da8 | -14.71487 | -48.77003 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 128cf2eb-ed61-3223-8eb8-cf54a57f4415 | -14.71157 | -48.76945 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08b27a9c-211e-3834-9b54-cd2b6f47f6b1 | -14.70826 | -48.76886 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8a763072-722b-31a6-92f3-30b33c6427da | -14.70777 | -48.75058 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c149775-5e22-3944-8701-181190351fa1 | -14.70722 | -48.75409 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8d2418b-58f0-3f34-9a24-36b0ae365cbe | -14.70665 | -48.7576 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 191602b0-23fd-34c8-a2cd-f33cce6f4161 | -14.70496 | -48.76827 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7fb74a5f-899b-3f52-b0c7-09d59bd0fbeb | -14.70447 | -48.75 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8f43aea8-4d37-329e-b5e1-c99a969a7b98 | -14.70391 | -48.75349 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 29cdbbd5-def4-30cf-9ad5-0b3668c2596e | -14.70165 | -48.7677 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03cd8cad-0166-3fdc-83c6-e9cce814c60f | -14.70108 | -48.7713 | 2024-10-03 04:27:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README93.md)
