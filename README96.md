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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc0612e2-ea7b-3c1c-9cae-5518395450f3 | -2.23627 | -55.90285 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f6b04fd-9aa0-3daf-9a2c-ac5a48f1c8b8 | -3.02786 | -54.01788 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0616944-060f-3875-bc14-00bdc41f8a54 | -3.43444 | -54.54308 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ede7b526-04bb-38e5-b66e-054f244fbff9 | -2.59638 | -53.97158 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27d4cd93-97a9-3d75-b5f6-b3e31e9b80fd | -3.81044 | -52.3557 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2a22e149-69a5-3deb-8eee-c9a49644a625 | -1.57547 | -52.2587 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11534284-eba7-30de-bce8-e7687ad9a6f0 | -2.96295 | -51.002 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f17e699b-e9f8-3ca1-bea6-7dc6cc08e70b | -1.36184 | -54.65481 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33eaf97c-04cf-3ae7-8209-412adcb6d3d9 | -1.65749 | -52.71589 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b4a1df0-fb1d-3eb0-a80e-f0e733825211 | -1.6237 | -52.37218 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bcd3f103-fa8b-31de-9659-9128b3bbdfb8 | -1.08872 | -53.37812 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c14fa230-9f5b-328a-879f-6921f7b5da3c | -1.16854 | -53.67818 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3052da3-6599-37a8-a7d5-b9094639e524 | -1.58594 | -52.27637 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ec44b4ba-ca27-3f2d-8f4d-66b643390c90 | -1.57974 | -52.26391 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 43f700a5-c3a0-3d86-9a7d-1cdc40435b84 | -4.08898 | -54.76455 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bacf5df-50ff-3f69-a4da-947620e64042 | -1.32775 | -51.93131 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 733d07ca-5531-3ee6-bbc8-b8bc6b406217 | -3.96223 | -54.61113 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d207e08a-ea6b-3746-9471-2cf4f462e922 | -1.79261 | -52.73806 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f1f2a89-8ec7-3aff-9b88-ba1fbcc6808d | -2.83597 | -54.1126 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7c38ed4c-25d1-3469-8b07-4688623a00cf | -3.23562 | -53.93319 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00bd2fcc-596c-3cc9-8519-e91c16a7cf8e | -2.6938 | -51.68203 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6468b843-a460-3186-97c4-3d451b71112c | -1.65757 | -55.23421 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f257914e-4bac-33d9-8dbb-f656533922d9 | -1.33295 | -51.93254 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2332017-9ccb-38d6-a1c3-93af19ccd668 | -2.59145 | -53.9688 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 605cb887-684e-33fa-80c5-87fd3b47e819 | -2.91678 | -51.7122 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 173db943-2154-30b3-b5fb-f1b5099aa999 | -3.3651 | -50.8262 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cdf82b63-8b6a-356a-b8df-5ec7ca23819b | -1.31603 | -52.86952 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82716cb3-92a4-39c7-a726-c09d5a78991b | -3.32196 | -53.70235 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b0e8adc-a249-39ae-a695-fe76b0daad06 | -3.17614 | -54.32656 | 2024-11-28 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 97e67644-6fb5-3c47-88b0-c58f1d490b27 | -1.15526 | -53.56548 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34748a99-92b3-360b-a408-dd9bcaa12def | -1.32644 | -51.93147 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e579a93d-e697-3f03-a6ad-c0c8266c8090 | -2.83536 | -54.11666 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81b5c5ae-1be8-34e4-9408-532012191f64 | -1.66664 | -52.4726 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e072262-f899-3333-9ed5-1e25340dadba | -2.23044 | -53.69041 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 927e5fa5-cf95-3ede-844f-b82b06fc1281 | -3.09944 | -53.81104 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d1cf405a-43a9-3626-ad8e-e0ca3cceaed4 | -4.08954 | -54.76063 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41f38882-4df8-329f-b0c6-0a21c8f158af | -2.36778 | -56.11902 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55bb159c-e09a-370c-8fd6-132e9937dca4 | -0.97775 | -53.68596 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1be6ca0a-583c-39f3-b22e-61f7fca4a2eb | -1.58056 | -52.2587 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 439ca8ab-0cc7-3815-8eaf-23ffdf50c294 | -3.50662 | -53.80882 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a382bf8-4e88-317f-83a9-f2551a075dec | -2.75758 | -52.09952 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a298b22-694d-30ab-8488-ccb531da523a | -1.71342 | -52.47563 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86fac9ef-d873-378e-abb4-c7a8a24017c9 | -2.93913 | -51.59274 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 45c82c96-75f1-3a4e-8c26-bac6060f6790 | -3.10585 | -54.97649 | 2024-11-28 05:40:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 951000ff-da21-3b6e-b45f-9b35d60d3045 | -2.26053 | -53.47137 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3efa6d66-a101-32fc-b28d-6f5f9c9df657 | -1.72453 | -52.48774 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 701a16fb-5766-3c81-a0f6-8aee6f486117 | -3.09942 | -53.72869 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 758fe108-afba-30aa-b67b-a430616b7ab5 | -3.39531 | -54.28881 | 2024-11-28 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6aa37442-4ba4-3550-b95a-4fd0e979cb64 | -3.69475 | -51.37056 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af3d3402-9db8-3dcd-a88b-8ea90caa3824 | 1.25368 | -55.96623 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8629246f-64cc-32fa-ab7d-c27001734bf5 | -1.10366 | -54.14027 | 2024-11-28 05:40:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a3166f8-8185-30ac-8234-bd3cb3f8da78 | -2.69964 | -51.68904 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d18b28f0-1527-320e-b709-eb2be9a1be6f | -1.38975 | -54.99387 | 2024-11-28 05:40:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4d209c-1e6a-3f2b-a572-e1309e63941f | -3.74186 | -51.8406 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9985bdd0-07c6-3d89-a864-b0df96693121 | -3.11834 | -53.26027 | 2024-11-28 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94972010-c515-3900-b866-0ab98fc20c51 | 1.43293 | -55.89739 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91836d3a-0ca3-3f2d-90bb-dbb872706848 | -3.32257 | -53.69818 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10fa8d06-0026-319e-aaef-e8e62871ba08 | -3.23913 | -54.22517 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b539788-e9fd-3254-a1c5-b693377ab241 | -1.71976 | -52.47662 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e02f686-48cd-30d7-9cbf-c66d7468aee2 | -3.37223 | -50.82737 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 116239e9-88b8-3858-aaeb-a89165fb6ada | -2.90846 | -54.17924 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21446424-d9a3-3647-839d-709b6addb2f1 | -1.67441 | -52.43318 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0cb495e7-04c1-3b81-a04d-b8dc0e697e02 | -1.15571 | -53.57027 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e22b919-dda3-3dfa-a4ae-8170387b16ac | -3.05967 | -51.06358 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb2b3084-144d-3d9d-bb12-c4d8dcfa07bd | -2.37194 | -56.12544 | 2024-11-28 05:40:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06102882-5080-3b56-b6bb-a546495b55d7 | -3.39556 | -54.28457 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e01d0d47-528b-3168-8dfd-f8e11aee2c89 | -1.62882 | -55.70723 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e504be3a-f61a-3b05-8657-393adcb2cd72 | -3.80393 | -52.35437 | 2024-11-28 05:40:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28417cf8-d2be-3705-b9d7-4a7c6f6b9edb | -3.45523 | -54.48183 | 2024-11-28 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 25964263-3de9-37f5-83eb-4cf7f1ffa75f | -3.27512 | -50.61931 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 003503e8-a0dd-3701-93c9-a04bc8bd1a40 | -3.34965 | -50.51183 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 686344d5-9b68-3fa9-b782-4ea9038ffd41 | -2.89605 | -51.36829 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73ec2c62-38b5-3d0e-af23-39d4069e4280 | -2.75722 | -54.12286 | 2024-11-28 05:40:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2e9a2117-7795-3adb-b55d-6dfd61df4ca0 | -2.63185 | -51.77535 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4427d9ad-85fb-30d3-8c4d-ee6858e1a270 | -3.0982 | -53.81936 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0f909d99-bb17-3731-b74d-ef3a02a63bd3 | 1.43442 | -55.89834 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a70d8feb-ece2-3294-bd30-eb2bb1bdf492 | -3.24366 | -53.63501 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40ee86bc-1b7e-3c88-a7a6-ebe6d293dd92 | -2.80696 | -51.58842 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20c20f1b-c13a-3877-82f3-6284e75d2ba2 | 1.24455 | -55.93142 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e42119e-c7a0-31fc-bf43-3afe1c9ca567 | -1.15396 | -53.5742 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 166b3b83-e176-3eec-bc9d-5aa4b8f9b6d4 | -1.15052 | -53.56512 | 2024-11-28 05:40:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a7afece-36ae-3aad-b1c1-24a31d75e2f5 | -2.60186 | -53.97877 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9d04fe9-4e82-3935-b10c-ac721cc802ba | -1.60452 | -55.37799 | 2024-11-28 05:40:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb2c8a04-08b7-3e82-9144-46d00b0b4589 | -3.50122 | -53.80395 | 2024-11-28 05:40:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d19b2e3c-b2d2-3b69-af9d-67e2d629f4c6 | 1.44116 | -55.91728 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2e5f7dc-c4f8-3ea1-8c6a-96514ebb8c45 | -2.75677 | -52.10489 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc2967a3-9d92-38c7-855a-7c693fced535 | -1.78562 | -52.74196 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e4a3255-52b4-3ead-ae83-966bdd9996a3 | -3.3424 | -50.51058 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f972d17-38c3-3dea-b940-71fb4d720170 | -1.65951 | -52.47668 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8968754-60d3-3a23-82e0-07148b6d2d14 | -2.32192 | -51.95922 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e0cee2d-5fe3-39f4-a072-5eef90ab3f21 | 1.23891 | -55.93637 | 2024-11-28 05:40:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cebf89ae-aaf0-3b12-9cf4-96df928c4f19 | -3.27614 | -50.61201 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3f3ba8f7-1ad5-3b27-9e30-d074de0473dc | -1.71898 | -52.48169 | 2024-11-28 05:40:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5405c474-45a8-3e63-969e-fac0282d97dc | -3.25118 | -50.61695 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50eccf8e-04ec-3cf1-871a-d0d66eb95b2e | -2.83076 | -51.84146 | 2024-11-28 05:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73e4f38d-0e2a-376d-977a-709471f11ce8 | -4.22576 | -50.88499 | 2024-11-28 05:40:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87acc187-33af-30af-a3d9-741687c63b57 | -3.34856 | -50.51941 | 2024-11-28 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 97279b39-1648-38c2-8121-15b171b59f0a | -2.94174 | -51.58644 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 73bd5c3d-ef2e-37cd-8d12-1fa67032377a | -3.64997 | -51.39803 | 2024-11-28 05:40:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5dfd55db-2f20-3668-89bf-92384a8fe320 | -1.63055 | -53.86774 | 2024-11-28 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README97.md)
