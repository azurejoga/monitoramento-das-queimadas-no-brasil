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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2dcf0f8-8383-3247-8c85-441669d6050e | -0.70039 | -51.67173 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f455e9a1-2cff-35d9-b35d-30c02f1ca489 | -0.69356 | -51.67068 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 386078bc-920c-362d-b9d1-821b4c81cbbb | -0.68216 | -51.67649 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d91f478a-fad0-3383-b99a-3eab0ce17574 | -0.68173 | -51.67667 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0edda220-c597-374d-a9e3-a138be210cd9 | -0.67923 | -51.69496 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4f25fbc3-c7ca-3db7-b19a-6cb23ee197bb | -0.67888 | -51.69513 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28a9bbd1-e395-38c3-be14-90cd61e21c4d | -0.67831 | -51.67615 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9413ec46-00d6-36b9-9e47-7fa02c04707b | -0.67774 | -51.67983 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84ca49a9-136e-3d94-9c7b-a38ea45caff5 | -0.6766 | -51.68721 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 05e988d2-bb1c-3449-a34c-65ad3f3dfb68 | -0.67603 | -51.69091 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59e57c01-4d52-3a1d-a24d-56c12148a1be | -0.67546 | -51.6946 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf08f0ac-8071-3e5a-8395-c1228ac9a7f7 | -0.67433 | -51.6793 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0182875d-6de7-3ede-9195-2ad22fe4ef02 | -0.67376 | -51.68299 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea9ba4ef-ea4e-34b8-aca9-b37494f448ed | -0.67319 | -51.68668 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1af82edc-13ea-394c-b2b6-41c6035f8b2b | -0.16403 | -51.68853 | 2024-11-03 04:44:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35bfbb8a-5187-3f11-aaef-87b8d07b11f2 | -1.63179 | -52.04518 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6fa936ce-88c7-37af-b49f-eade527af35c | -1.63079 | -52.25329 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7ab0122-66f6-364d-a82b-f55327d00245 | -1.61101 | -52.37934 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f19df642-1061-3a70-9322-70c54ab53a31 | -1.6104 | -52.38318 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a0d808-6195-3854-adff-69ec351f3ca8 | -1.60848 | -51.96964 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e67ac41-b776-3822-b05c-bfc11ab13459 | -1.60791 | -51.97335 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85817c35-18f2-3232-a417-45c7f4b97ade | -1.60448 | -51.97282 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ccbd5ae-ed68-3b5e-bfec-333a25f36d21 | -1.58635 | -52.15784 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff6f645f-afce-3f1a-8873-5fa1ce9ba0ba | -1.58581 | -52.15719 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cb74d8d-8db6-35ac-8393-3149ab07ff45 | -1.58577 | -52.16161 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 394005fc-0084-311d-868c-b36e988375a2 | -1.58521 | -52.16096 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edea4f18-a5dc-335b-a0a4-5a30631402a3 | -1.576 | -52.15624 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 26846329-9452-3408-be4c-6f8c88a57adf | -1.57541 | -52.16002 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79946f5d-b14b-3795-9a19-bf4ae2de3174 | -1.57483 | -52.16379 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b34b6389-4a86-3921-9f92-2c6a4106765d | -1.57456 | -52.05218 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02eddf25-e70b-3b3d-951a-adef3cf34bc6 | -1.57313 | -52.15194 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 61a77431-9cf4-3d8c-accd-9708d8c096bc | -1.57255 | -52.15571 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0eedfd9c-4859-32fb-895e-a53bba99be88 | -1.57196 | -52.15948 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 84c0a37a-36c8-33b8-a0c6-0570f5456648 | -1.57144 | -52.1401 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d93434f5-85b8-3b0f-9bfb-988bade5e865 | -1.57086 | -52.14387 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28e32e70-9b65-3039-928d-bfa2e2f0b8f0 | -1.56826 | -52.04744 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0735a339-2859-37e2-a40a-926b40fd6def | -1.566 | -52.03943 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92b06625-0aa0-3698-8614-339a066c738c | -1.56483 | -52.04691 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a91f523-cdb5-35f4-bc20-21c4d95988ed | -1.56349 | -52.28256 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6349732e-fbaa-3089-95c3-11312f65590d | -1.56198 | -52.04264 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41009be4-4f97-3ac6-915c-df7b778e8929 | -1.56184 | -52.08858 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 90617e79-4bce-33c3-b9fe-afaf1398d82a | -1.56139 | -52.04638 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24e3c855-8310-3ba3-b350-4fffbaaed225 | -1.56125 | -52.09233 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 56d335d2-7ac7-377e-8692-7bc8be1ad7ea | -1.55898 | -52.0843 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c5a6ee2-4fae-388e-8eef-c4772fdbafd4 | -1.5584 | -52.08805 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f0d3aff-4b8e-312f-8cf9-00489c620b8b | -1.54715 | -52.02506 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d930e5c4-f668-3c95-8f46-e43ea4596399 | -1.53518 | -52.01175 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90a349ef-d83a-3474-af4a-bcf5f6a3c781 | -1.53233 | -52.0075 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbf9825d-068d-3cf1-abd1-a5ecd285c2b6 | -1.53174 | -52.01123 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8e86812-eb79-3390-bef0-899fa77f2db3 | -1.53067 | -51.9958 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4e8f73c-1bc4-3905-adf9-48638cd849bf | -1.53008 | -51.99952 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c93bb15-6710-3cee-9495-cb064de80749 | -1.52949 | -52.00324 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b921429c-0d8e-363b-82c7-0f94d0740ce7 | -1.5289 | -52.00697 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e82d6fd-7c69-33c4-8fde-b2afe0b59670 | -1.52724 | -51.99527 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53b6eac0-b8ee-375a-b11e-d2efa83d8882 | -1.52665 | -51.99899 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4166accf-d1b7-3ddb-8178-8ad532868fe8 | -1.52364 | -51.90723 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 075bf91e-2e80-32f4-818d-8f4d85a9d6cc | -1.52209 | -52.11709 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fa7fb89a-b511-3cff-a63e-da03a2defb8b | -1.5215 | -52.12085 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 86a3b353-c476-39b7-b9e7-b0d04b0e55d8 | -1.52022 | -51.9067 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cc728d3-425b-37d3-89af-559aef3a059f | -1.51873 | -52.54852 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6302d8ee-d769-3e74-8a91-79fe94de0146 | -1.51864 | -52.11656 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f1a50d2-8b22-38d2-9064-aa9d69bf2840 | -1.51805 | -52.12032 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 468a129b-0011-37e3-adae-97e7c47e805f | -1.51582 | -52.54406 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5b9ba1b-d8a6-3e88-87bd-d8ae5c2801ba | -1.50996 | -52.12683 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9d0e236-45c1-312e-9848-11c2bf18d141 | -1.50605 | -52.10692 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a191860-e0a7-377e-a0f2-442fd00f815e | -1.50545 | -52.11068 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6dd0311-5939-311c-8460-895b417b6988 | -1.50478 | -52.43084 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 926bb13a-a288-39da-ba80-2b4d41f378cb | -1.50418 | -52.43471 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4fdc7f5d-49c8-39f3-b9ca-0076c0fe737b | -1.48848 | -52.01963 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c1514db2-712f-3169-a465-964fc38d6608 | -1.48268 | -52.05702 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2c6119a-9898-346d-a455-887551f7724c | -1.47918 | -52.07952 | 2024-11-03 04:44:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b81b993-6e04-3d3f-b16c-c9ff619eb40a | -1.47739 | -52.51415 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f478b98c-61c7-39d5-8ed7-f59d34b68943 | -1.67358 | -52.04779 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1140b2e-5d3f-39f5-afff-1071ad2d5a89 | -1.66473 | -52.1269 | 2024-11-03 04:44:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3aaf4058-aab8-3317-8ee8-1b2ee0203cc7 | -1.05105 | -52.36631 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 770b6a39-cf89-3d5c-a7f3-adb892f41fc2 | -1.00279 | -52.29994 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70291a73-e859-3103-ab20-075c0e2620da | -0.9703 | -51.78511 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27442c37-87d0-35e7-ab0a-95690bad4207 | -0.95045 | -52.38305 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 603f7d04-5b7e-391d-9f1a-c2486e748552 | -0.94985 | -52.38692 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e71479d3-b62b-3228-bbf1-e5cfdc6baf0f | -0.87518 | -51.98838 | 2024-11-03 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28e44a34-067d-3223-b703-bb1af49fad12 | -0.83586 | -52.19238 | 2024-11-03 04:44:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 841c2880-c01e-32c8-ad91-090d9e4e97d1 | -0.77595 | -52.33713 | 2024-11-03 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0bc0c974-e14a-3ba3-ac50-8f1d3f592d10 | -0.77245 | -52.3366 | 2024-11-03 04:44:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9fdbf7e7-8d77-3f54-b2ac-4632ef52b205 | -1.2412 | -53.06683 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1aa27fca-6577-3761-b0dc-b0005a861ccd | -1.08546 | -53.16938 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 920d3a99-e1e1-3361-84d5-f2a06098eb03 | -1.41891 | -52.19399 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97f44aa5-647f-388c-a2ee-a13164447f45 | -1.41604 | -52.18966 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9448896-b10b-3216-8d63-59d91342db18 | -1.40853 | -52.19239 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a69a7868-3f24-377f-9704-a4e47ea0c993 | -1.40507 | -52.19186 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 78a37420-b1cc-34e8-ab09-fa8c0ee3fde5 | -1.40504 | -52.30508 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ceb8759b-889b-3c33-bc9a-f39de070e0d0 | -1.40447 | -52.19565 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7516dce3-c372-367d-aa5f-3c4e6dd41ded | -1.40443 | -52.30891 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed3283ac-2001-392a-a7e6-17e7cb4a7a05 | -1.40101 | -52.19512 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbb7e1f4-fc1e-39d0-9171-a3425e56e119 | -1.40058 | -52.06363 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fbcca18-c80c-3b04-9ca5-29e03e63ced5 | -1.40045 | -52.08671 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9c6a2165-8957-3bba-ba79-496b1017ea93 | -1.39713 | -52.0631 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4d77434-2008-39ce-ae6a-ac65bba04bb4 | -1.38554 | -52.2707 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88f906cc-b0ed-3a6a-a358-9eed5354cbcd | -1.38552 | -52.00418 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff53b980-5a8f-35e2-b7c7-fa2ad38987c5 | -1.38206 | -52.27018 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0e5d46f-e59b-3d23-8f93-baac2435ebf8 | -1.37985 | -51.97272 | 2024-11-03 04:44:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README33.md)
