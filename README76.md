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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d70bf3d-1e03-3dbf-b84f-4f244ac0d83e | -1.6649 | -52.47141 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0013f63-b8d0-372d-8552-f225f98fa6ad | -1.38628 | -55.01357 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2218f80c-5cbf-3bfa-8f55-b3aa23052fe9 | -1.60763 | -52.27797 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aad2c035-ddd9-3143-b895-3fbe68f11e0a | -1.6601 | -52.47462 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c076f826-f9b0-3767-8260-44dee107591d | -0.9555 | -51.63478 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12570d3e-39a2-3c3a-8014-9ced4b4374d5 | -2.00081 | -51.17659 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 08dc9806-defb-36b5-84d9-7ca96e544884 | -1.21116 | -54.19477 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb962c96-9e6b-3f12-bfad-d352cf030250 | -1.69069 | -52.4991 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 134745f5-a6ac-3e90-84aa-f192d2281eb0 | -0.7761 | -52.39338 | 2024-11-28 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1216c1e-3057-3c46-86e8-5284692ca6e9 | -1.08702 | -53.64011 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e68e4e5-6846-3607-9cf3-fb0d6ebc576a | -1.18756 | -51.76807 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9fbafe68-ace6-3a95-ae3d-dd1c1498e770 | -1.31965 | -52.87056 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa117479-2232-3ce7-a9c4-bc6591bb3be6 | -1.69017 | -52.47896 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 713b5594-21cc-3540-a2a8-141d1050f2b3 | -1.43069 | -52.66669 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 275d75dd-8d5d-3e50-b652-129775894822 | -1.06635 | -53.37859 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f537b8bd-06ec-3bfa-86f4-269005935428 | -1.44729 | -47.11451 | 2024-11-28 05:16:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3924894b-34da-34b5-b5bf-c3f0db4069c2 | -1.66474 | -52.73503 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8be364e6-1027-364d-8d80-5233e775ffbf | -1.49922 | -54.4594 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a9e08db2-4f00-3358-ac80-f78e4b115714 | -1.60041 | -52.52833 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4504ca1e-6f25-33b8-bcb1-99c0afd67b1e | -1.04707 | -51.74072 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 28810890-56fc-3bbf-bf7f-c4fe90e267ed | -1.09011 | -53.64582 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 659f5948-73e2-3705-86ef-c9f3f8c8a2e7 | -1.3058 | -51.7318 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4f644e4-7b62-317b-9144-46c01737400e | -1.35603 | -52.54378 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff560fdb-b591-378d-a541-7d64eff5fd88 | -1.27153 | -51.6294 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9c2f9bd-9ca3-376a-a4a6-f4e52d4d7eb6 | -1.397 | -53.55184 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7c5fd8c2-1ada-399d-a69f-5c42969a320f | -1.16038 | -53.6769 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 397d90a6-b172-344d-b97e-c22fb235e9ae | -1.04376 | -51.73786 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9ec509b5-18bd-3ef2-8fb1-32d1e6eff901 | 4.26011 | -59.9871 | 2024-11-28 05:16:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b012e07-aa80-31bd-b241-7b6fbc986069 | -1.72263 | -52.49194 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6b2be7f0-faa6-3802-a235-edacc0c3acc3 | 0.97628 | -50.12804 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9011ae25-9129-3246-ba3d-c66da64e909f | -1.6829 | -52.49395 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 783cb695-ecfc-3234-824b-b90f0d3f77e1 | -2.84587 | -46.85852 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98b0ac9f-f436-3eab-a1d1-a498632271a7 | -1.33207 | -51.93827 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 591a6616-f05d-3e84-a68b-0086994dfd36 | -2.39322 | -47.16599 | 2024-11-28 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0790fb3b-91c4-3d0f-af51-db58fcfb3631 | -1.33576 | -51.94307 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10e20b4e-2114-3705-add6-87b099510645 | -1.7115 | -53.2547 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87d48b87-683a-3e58-ac93-9136b8355930 | -1.06946 | -53.64032 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9ca1a6f3-5255-30d1-bdc4-67a3480e54d6 | -1.10436 | -54.14155 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 701ded78-74eb-3aa1-bb7e-029cb15667d7 | -2.86524 | -46.85694 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1afea86f-2085-3ed4-809d-99cc81c680d2 | -0.24027 | -51.59679 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 71b3e6cc-8b21-3a63-a85f-24aa762d0243 | -1.57104 | -52.00446 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3057fe77-8007-318f-aac0-713644e6c964 | -2.87847 | -46.85373 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 182feab3-6b1a-39b1-bc43-389882312997 | -2.60618 | -46.83392 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4848d9da-a7d3-3f0e-8a7e-bc036846ed34 | -1.38946 | -53.62571 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0dce5dcb-cab1-3c63-8d6c-5dea5528d74b | -0.26647 | -51.5142 | 2024-11-28 05:16:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3fae0d3c-add4-334c-969b-e5f1cf464ced | -1.64804 | -52.71725 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| de8ed096-bfe6-3b15-8478-93eb89e59c44 | -2.43738 | -48.23997 | 2024-11-28 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36328454-6f70-3ea9-b0fb-9049bf26d4a4 | -1.33142 | -51.95313 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2c4671e2-ecf6-364d-b865-6791ddfb9782 | -1.68712 | -52.47057 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 894a0b8f-6c71-3982-badd-f959f2a2b7ca | -1.47542 | -54.44197 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04ec39e6-19e8-3974-a26c-28b057d5281d | -2.27003 | -46.36112 | 2024-11-28 05:16:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11fe0b09-5312-3ef8-96d6-addaa5d7e544 | -1.76867 | -52.70789 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20b6e772-bfcb-3a19-b512-d67ef38c56fc | -0.95228 | -51.65627 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e25c8b6-d8ea-3e5c-b98a-040927c26541 | -1.62798 | -52.37407 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2653a868-d4fa-3094-a1bc-2a23d555d51f | -1.80557 | -52.74424 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f09f0bc3-2f69-3598-88d1-c88a1585dc86 | -1.20817 | -53.55635 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5e09124-a801-351c-8736-9aa77eda9cc0 | -2.38636 | -47.17016 | 2024-11-28 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 48719548-6fd2-3ed6-b112-ef1acc21cbf9 | -1.30141 | -51.73111 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 283e5f50-d626-35f9-905d-0cc04f0202e8 | -1.32903 | -51.92932 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b29a8823-3723-36ab-a538-1c4f34a3b707 | -1.65099 | -52.71385 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a7f5fe7-b5ea-3b28-a187-3b10fd184916 | -2.00243 | -51.04339 | 2024-11-28 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ce7bea2-754d-37bb-9152-7e830c81edd6 | -1.06021 | -53.20756 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 292dfeff-0268-35eb-826a-a3dc339f27f2 | -1.44423 | -55.19957 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b566a485-0747-3b62-a61e-3c90b47ed8ca | -2.84648 | -46.86628 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 235a6af9-c6d5-3407-bad5-784f817a25fd | 4.36958 | -60.8202 | 2024-11-28 05:16:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c20cc525-db1b-3ded-8037-88d1fb4f2b90 | -1.78846 | -52.7454 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7bfff58e-744b-3430-958d-db41e1cc5db4 | 1.72333 | -55.80084 | 2024-11-28 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c54d67a-a533-3e80-af43-ef0b8b46744e | -1.57575 | -52.26254 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15e406da-3cf5-3490-8b66-032880e18111 | -2.86388 | -46.86642 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 158c9824-7627-3dfa-b1d6-c5f969239a42 | -1.68353 | -52.43462 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10f5de4d-ef59-34b5-8c6c-f848f0aa77ac | -1.68367 | -52.49376 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5bf803a-558e-3057-a619-f313f976c8f5 | -1.47629 | -52.66118 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dae4abae-cc8b-3f2f-a28a-af3aee345f28 | -1.44219 | -55.2362 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d115e5bf-0ec5-3be6-bc86-f57e4be99f12 | -2.86517 | -46.86929 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| febc9468-a60a-3dfd-8d29-1a128e1b228f | -2.87011 | -46.86746 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c9358be5-7d82-30b3-8559-8f34947388ad | 1.44337 | -55.8993 | 2024-11-28 05:16:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bac216e1-ed31-3d27-919b-2bd845e0e49a | -1.68877 | -52.71589 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2cfe9a6-3c9c-37ac-ba74-a4dc85f83fe1 | -2.85272 | -46.86723 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a420020-85e4-3bdb-a538-de766af8fb27 | -0.9511 | -51.63409 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9b8e5d5-b98c-3659-8b0b-0edbfd9837c0 | 0.9827 | -50.13107 | 2024-11-28 05:16:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bca2b1e1-af76-3667-8832-f7ea737c98f6 | -1.15611 | -53.57703 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83945ce2-25c8-3dea-8773-1efe29e195b5 | -1.35929 | -54.63442 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec1af62d-736a-3405-9a0f-40abb2540cec | -1.1913 | -51.77301 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e2765484-9090-3531-b97a-0273e704afc3 | -1.3605 | -51.96616 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 75cc97e0-eb4e-3915-beb1-65d6d39339ea | -0.87933 | -51.72084 | 2024-11-28 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11bd24f3-3951-34ce-8fa0-633ad39cadc5 | -1.65229 | -52.46946 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe17c20f-36a3-3e45-bed6-3d0c125efd49 | 1.31347 | -60.40814 | 2024-11-28 05:16:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e8382b42-c2e1-33e0-bacc-aef99bc2cc5b | -2.84796 | -46.84386 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c7899d0-6d80-301a-af92-bda2d733e12a | -1.35912 | -54.63554 | 2024-11-28 05:16:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a21bb3dc-4f2f-3fbf-81d7-d8160854952b | -1.23326 | -53.36499 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f99f7d45-5108-372d-8a98-b0674e10d69c | -1.75301 | -52.65675 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 705e892d-1a50-3099-9497-ba77673198fe | -2.87511 | -46.8458 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55c1dd18-f84c-32be-8d75-4f20fdfb54b0 | -1.19085 | -53.87769 | 2024-11-28 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c9d5fef-28f8-3b6b-a61c-3be2bf60467d | 0.69743 | -51.44739 | 2024-11-28 05:16:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 90e9b596-e85b-3c3e-89e7-c241da6f0fa2 | -0.95761 | -51.65059 | 2024-11-28 05:16:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8d100be-441c-3451-8d0b-97cc83af5e04 | -1.32469 | -51.92864 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a1f378c6-c724-33ba-83f9-da1329778579 | -1.08125 | -53.36022 | 2024-11-28 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e93e79a-5ace-37ef-8455-cc9df7d08bcf | -1.64159 | -52.73147 | 2024-11-28 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aec90b4a-1d16-39ae-bac6-0bd943a91676 | -1.25747 | -53.99895 | 2024-11-28 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38f6c4f7-ca40-3411-a9cb-9236290a40e8 | -2.87083 | -46.86246 | 2024-11-28 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |


[Clique aqui para ver as próximas entradas](README77.md)
