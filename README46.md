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
| 1c8fad4d-c51f-30f6-8ee2-7cc5b2fc63de | -2.82838 | -52.90913 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 066ed48f-1af0-3531-878d-1c04635dae6a | -1.2197 | -51.76999 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 883cb084-d661-359e-ba81-bb4668fe889f | -2.60688 | -51.75563 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6b42ba5-5776-3501-81c4-4a0561768468 | -5.04647 | -46.85162 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c665aea2-63d0-3d5d-a241-d65956fdb51a | -2.78098 | -52.87004 | 2024-11-07 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98016b4d-354f-360b-a350-773fe23d07a5 | -1.34501 | -51.41758 | 2024-11-07 05:10:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c2d9e0b-fbbf-3c55-ba4c-249d825bed61 | -2.91797 | -51.05273 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f009cff-ea0e-3454-a50c-486870a51fa5 | -2.88907 | -54.11563 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60f983a0-937f-309f-8148-d7e181abef79 | -1.46221 | -53.49331 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5f44b69a-04ea-3744-a81f-6b68ed40c117 | -2.82528 | -52.95389 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b98417a4-bde0-3f0c-b6ff-3ae16210645e | -3.01432 | -53.23347 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ece86ec4-2fd2-3152-8c34-4240f3caad22 | -1.73186 | -53.4368 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab62833f-9f38-34cb-ac2a-55e368dbe107 | -2.88551 | -51.30902 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4887d514-8aed-30d6-9931-b845e02d420e | -1.62364 | -52.24768 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e1f7c770-0648-32f8-82bd-2c2a6890c766 | -1.51664 | -54.51191 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98178495-9323-3fa5-9e30-af11501b8c56 | -1.22859 | -54.53917 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c18fdc67-7057-398e-9704-396e68dd125c | -1.68748 | -52.13029 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b44637cc-c694-3191-9dc8-8502fd442253 | -2.77492 | -51.91977 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad070b82-41bd-311e-b0e9-c3848ead8a81 | -3.11345 | -53.71214 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67a50954-0367-37c3-92ea-7c8b4b773cf2 | -3.22453 | -50.38066 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 70e48e98-9695-3101-bba6-a66e91c19ea5 | -2.60749 | -51.30602 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4edc3f3e-fa70-3158-b1bb-fb9eb0725e7e | -2.91556 | -51.04051 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a615182-78d6-353e-ba7f-8b1385dabbb2 | -1.40798 | -54.196 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05732d19-15e6-305d-a34d-461e9cf802ef | -3.45491 | -50.37676 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| faa0276a-90c2-3435-ac65-73f465b857a8 | -2.92008 | -49.59669 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c65be61-13b9-38d7-8d61-a558696cba62 | -3.22725 | -50.45105 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea8ba64a-70f5-35e4-adc9-522886591004 | -3.03247 | -54.07631 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba2485f7-21fd-3bc5-ad55-fa7411454845 | -2.99123 | -53.84769 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca9cdc8a-926a-3e09-b167-e3297b26c9c8 | -3.87382 | -52.38276 | 2024-11-07 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d7b056c-b4aa-351d-9c0c-b0a5ae6d30e1 | -2.76539 | -53.22031 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d984b53c-fbbe-3405-87e0-befdc752ab7e | -2.82263 | -52.92178 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed18eacc-395e-37a7-9499-5474f11caedf | -2.92078 | -49.60024 | 2024-11-07 05:10:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 347f877d-c1f4-3027-b4a9-ee6205f65fff | -3.2283 | -50.38335 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| aff86b9b-1b17-3888-91f4-02740b0a723d | -2.84923 | -51.77527 | 2024-11-07 05:10:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 170b51e9-1cba-3eb9-be16-5f21e13fd6da | -3.08255 | -54.03149 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e1a057b-f24e-3dbc-ab94-9b66d69470ff | -4.37674 | -48.58661 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 713ecac0-3bdc-3078-910e-8f05600d055a | -2.21318 | -53.72395 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 433fb79c-787a-3a5f-8dd6-5195ee93e2e9 | -2.61844 | -51.73275 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb592889-79c2-30d5-aa82-d4d155fd7e0b | -2.08214 | -52.03973 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1eaeba0-1894-35c7-8526-f4d07a118177 | -2.66819 | -49.87635 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8bb6fffd-56d3-3561-b0f4-779034668534 | -3.01552 | -53.42322 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb7f08ae-ccd6-3ab1-bbe0-e4148fd92cc5 | -2.91664 | -51.0394 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e58532e4-437d-3d4e-b3f3-c0a2a7eb7aa2 | -2.25691 | -53.72249 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 880d415f-c488-3238-ac00-55ec4eceebac | -2.73165 | -54.14461 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46e4df83-c07c-313b-97e8-07ca55417ce3 | -4.04994 | -49.27162 | 2024-11-07 05:10:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1deab000-da57-3ddf-9c75-628a90155018 | -0.83051 | -53.05842 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49f83089-7828-3916-84fc-03703d2471d5 | -1.21808 | -54.22146 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ed2fed49-390c-3c40-89b3-95c838955d39 | -2.6168 | -51.29993 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2d323b2e-7214-3459-87bf-144a11cfa4ff | -2.95393 | -53.28541 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8fe33b4d-11d7-3165-bfed-9887ea5ba1b7 | -3.7127 | -48.99781 | 2024-11-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 83c13f32-922b-374c-9f0b-b0696331f432 | -2.99997 | -51.05617 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cd334ad-372a-3be2-a214-c120c4e99245 | -3.18788 | -50.59161 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b5099ae-f9a4-3f7a-999f-5b73065dc1b1 | -1.39403 | -55.4238 | 2024-11-07 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cde899b-05e9-387e-8a41-ad2b23e25147 | 0.52938 | -50.79892 | 2024-11-07 05:10:00 | NOAA-21 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee8b3460-b91f-385c-bd9f-6c90d9e093d7 | -5.0424 | -46.8445 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3806bd8-59fc-35db-a0eb-2f268793b01d | -3.11622 | -54.16887 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e4924b8-112b-3bfc-a79f-4054a3961086 | -4.35093 | -48.63109 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fa0f194-84c9-3913-9211-22ddb7a825fa | -2.40201 | -53.62819 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6429efbb-4f02-3f79-ab06-0e74f54581ed | -3.3284 | -53.18796 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f6be638-845a-36b8-927c-bdd94606cfa6 | -2.81959 | -52.91675 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78482699-831f-3dba-896d-1901ce7a455a | -4.25339 | -49.6535 | 2024-11-07 05:10:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0607acf1-3ead-3247-b390-029962e2081f | -1.10609 | -54.19713 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9977b3f0-cfd2-33e3-b479-c374070a148c | -1.48297 | -47.21539 | 2024-11-07 05:10:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| db8cd144-157c-3a7c-a068-2e5b8e49d6a7 | -5.55432 | -43.70214 | 2024-11-07 05:10:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 186a77e7-8b66-3e3e-8b83-3bffcdd73994 | -2.60394 | -51.30174 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7df5f482-cf01-346c-9a10-c617016de4ee | -3.77509 | -51.40489 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c91c7b26-bc38-31c8-8561-8f0fae240d97 | -3.00141 | -54.09159 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dac1e790-a198-39fb-96c7-7d1e30108737 | -1.34939 | -54.61839 | 2024-11-07 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a252d9ff-0ca0-3b40-b200-e039aa338734 | -1.41536 | -55.15812 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31c89c7f-b093-313e-8d64-cc90bb454c31 | -3.01599 | -53.44459 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e39a628-1458-3df5-a186-54217aff11d9 | -3.71351 | -48.99231 | 2024-11-07 05:10:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f41e9dd2-d924-341d-92f9-3ba2bfb59bb3 | -0.67325 | -51.66521 | 2024-11-07 05:10:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b03f29c-d2eb-34eb-9561-3e40bab3e48e | -1.52014 | -54.51568 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fafce457-9967-381c-91da-e62b8f7fa7e5 | -5.04707 | -46.85333 | 2024-11-07 05:10:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6410bae-72e0-326a-8f38-8a851891a97e | -2.90357 | -51.46904 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd4c925c-0fd4-3a1b-b2b0-14b6e2a03a64 | -1.32574 | -52.24263 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a25728d4-fcec-321f-b410-af5db35efff8 | -1.67359 | -53.81539 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a17ac729-ea5d-3fc6-b033-2b3db9201d63 | -2.23224 | -48.02466 | 2024-11-07 05:10:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00e9cf57-a283-33da-aa7f-78f468d19232 | -1.51044 | -54.8042 | 2024-11-07 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed353306-d39a-38b3-a1df-65ea04c5374c | -3.10925 | -53.71566 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d4130af-31a1-3736-a0a5-b9cf4a9fa7cd | -2.8321 | -52.90971 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3ebeb89-1079-3fc7-9a67-319dac738db5 | -2.94162 | -54.12365 | 2024-11-07 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0806a4f-8935-3c34-8f05-24bb23a0d2f0 | -2.55799 | -54.00061 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4a042f4-ff36-3074-a347-4a0ec6cc2b56 | -3.15934 | -50.20977 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b77d0b1-d74f-3929-873b-b8ff4daad976 | -2.66657 | -49.87781 | 2024-11-07 05:10:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b481100-b9e0-3df3-90e1-29eb4e04bcb1 | -3.7784 | -51.29625 | 2024-11-07 05:10:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74ae6efa-23dc-333e-8a81-0560a158ecca | -2.91437 | -51.04824 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4975a332-ca9a-3d3e-b0fc-1741b7c385b4 | 4.34325 | -59.83427 | 2024-11-07 05:10:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 214588ac-5931-3ac9-aa46-a18db636ec9a | -3.24783 | -50.46506 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 10b1628e-ed96-394c-91e3-e348f9e33a65 | -2.58025 | -54.00284 | 2024-11-07 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 691109f7-6ba1-3a58-8b91-511486b702a9 | -3.28968 | -53.24414 | 2024-11-07 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0492446-f820-3ad6-921e-24bf027d4714 | -3.22894 | -50.38131 | 2024-11-07 05:10:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 745c9218-89f8-3ce0-85c7-5324df416749 | -1.4639 | -52.57626 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f7859d95-ccce-32b9-aa24-719bbf71148e | -2.84953 | -48.66716 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 639df62e-a08f-33f6-a311-566f85e31876 | -0.8658 | -52.83141 | 2024-11-07 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fae8776-62b8-3758-8e9c-3138d6f7596a | -2.07751 | -52.04399 | 2024-11-07 05:10:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5cac04ee-e412-3678-a91a-5420170bee6e | -4.21937 | -48.68754 | 2024-11-07 05:10:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1afa4ce-bf0b-3dd4-ad61-b3e4caecef44 | -3.09915 | -53.70991 | 2024-11-07 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 114b87df-0034-3cbb-9e2f-76f09893d2f1 | -2.85859 | -48.67426 | 2024-11-07 05:10:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 46229eb7-8b20-3a6a-852e-a044fdbbe53c | -3.65724 | -50.25831 | 2024-11-07 05:10:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README47.md)
