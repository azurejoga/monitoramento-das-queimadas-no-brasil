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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39608a8c-f647-319a-bdac-6626d21b8991 | -7.94755 | -49.7561 | 2024-11-28 05:18:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1a9426ea-663a-3fd4-ac56-f8fb2939919b | -2.46038 | -55.27675 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34fb7aaa-87b0-3e1c-99b0-c16fbe8152d2 | -2.50091 | -54.53783 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b310afa4-17fe-337b-9584-730d05e69f9d | -3.18214 | -50.27851 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64578e95-daf1-3a51-9fa4-c0495532febb | -3.18367 | -48.43699 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3b96493-46df-3610-abc3-e3b44c535284 | -2.80857 | -53.02136 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5af6b8c9-d504-3ead-a82c-96155d912adf | -4.15649 | -54.80992 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26583ec7-8d5e-384a-a522-a0be7eee0ac0 | -2.2454 | -53.62663 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7777ab64-ee20-3e3e-9ae1-05c8601e4218 | -3.46872 | -53.70943 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c0adcec-0da1-3579-9fea-eb2ac1679980 | -2.97751 | -51.57741 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db1458ea-d96e-3069-b2d2-9241222e1528 | -3.87019 | -52.10823 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0204e361-d83f-37e9-960b-3cad105b3eb6 | -3.3518 | -50.51654 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0eca3303-e4f7-310c-b5d6-73be297692ce | -1.6308 | -55.70883 | 2024-11-28 05:18:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4f36c51-d4ba-38f6-a3c3-088e2d0c5ad0 | -4.00866 | -54.33461 | 2024-11-28 05:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b8aa433-010f-39fb-97f2-72e31c9d63af | -2.59291 | -54.08633 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5557cc0e-cf47-34a9-8697-ece9d79eba8b | -2.60502 | -53.98116 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74d5ed39-22c1-3945-a9bf-7c961b72d3f2 | -3.24441 | -50.61611 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 81bee211-5927-30bb-87c9-74c64e0d3264 | -3.57283 | -50.23311 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b31c070-cba0-3ea0-adf5-dddd25ed937e | -3.29517 | -50.27752 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24aacd4a-57e2-348f-9c8c-3986d742a669 | -3.1042 | -54.97788 | 2024-11-28 05:18:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b25b61d-e7e1-3fa5-885d-cc9fe861bbd8 | -2.95035 | -53.71699 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c61c6dfb-99dc-3f64-9d61-259e5e6f84d7 | -2.35432 | -54.68915 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 257f7dd7-793c-3c26-8064-f090bce0c894 | -2.89607 | -51.37032 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 88d06389-7e31-3559-9230-6cb3e96fea9d | -2.80245 | -51.59109 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 47de3dcf-8cd6-3cb0-aba6-e24fadfe7b68 | -2.62555 | -54.30423 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7494ac4b-1491-345f-ae19-9cc3be95e12c | -3.41453 | -50.16357 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f614e11d-d88f-33a3-a27f-2641cdfb340f | -3.29039 | -51.15533 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c0f8d8c-a13f-3fd7-94e4-8de2eda37af4 | -3.50194 | -50.47651 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bbaeafe-4e39-3ee1-ac62-77a00d06646b | -3.08997 | -53.25819 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e40c7732-286c-3f36-95bb-f63f197fe669 | -2.8697 | -54.03102 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 888584cf-1827-3f1c-a1d5-a4927a34d313 | -2.87693 | -53.99421 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9cfd3abd-b2c2-3a8a-b533-54e9b75633d4 | -2.77868 | -54.03181 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 02d72660-b41c-329b-85c1-4fe2863c7b23 | -2.84298 | -54.07603 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e94ff0dc-d17e-3fa2-a54f-8b5f9a893097 | -2.78478 | -52.99212 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03b74367-9ead-3729-8aaa-28c604f678b9 | -3.75171 | -52.39418 | 2024-11-28 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1b45d83-5a70-3214-87a6-7caef6b6f4d3 | -3.05708 | -53.28258 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45e17750-3345-3b48-8771-267d33c4321e | -2.65732 | -49.51052 | 2024-11-28 05:18:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8c7c53b-1a95-3cd3-82be-4efd88c385c2 | -3.39068 | -50.11444 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3405c4cf-aa3b-36ec-a5f8-439ca20d6ef3 | -2.87794 | -50.73801 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ede1e383-e301-387a-b338-96319e76d74b | -2.35385 | -55.87454 | 2024-11-28 05:18:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6658a096-a111-3d74-a520-33c4eb404801 | -2.62674 | -53.99414 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e3ce2251-96c5-37de-9117-693c4937c54f | -3.96956 | -50.1885 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f8c503a9-adfb-3567-af1e-50efa9da5b08 | -3.44835 | -50.00672 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741a4a5c-6b75-3208-8790-50509cb1cdc1 | -2.9678 | -53.89304 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0726cab3-8e58-39fb-8129-949e7e04e956 | -4.04782 | -48.3343 | 2024-11-28 05:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c39f8adc-5e66-3bf4-9a23-da85cc656e5d | -3.71226 | -51.81164 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9178f3d-ea55-3935-8d13-4d5fdb63486d | -2.75924 | -52.10073 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee84e334-baf7-3e34-9402-69201637ac10 | -3.51277 | -50.50703 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee8feea-96be-33e3-8341-3d5b9c8be2d8 | -2.62933 | -54.30482 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 82e8cb94-f05f-3c9f-9baa-863df6672b88 | -2.83251 | -54.11837 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 901fad7b-26b7-37e1-95ee-60d83486eaca | -2.99252 | -53.35322 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2e2afe8-81b2-39e4-8ac5-837b3fc8d08f | -3.33909 | -50.07585 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65e19ff0-3479-334d-8519-f0deb843b999 | -3.15033 | -50.14577 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da73db1-beff-3f56-ad04-98a961690304 | -3.03466 | -48.50464 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a69aa9d1-343d-3fca-b5fa-b52ed54953aa | -3.28948 | -50.31549 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1959884d-7d0f-333c-9c83-bb0eccb82691 | -2.81728 | -54.03772 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b764350-2e25-321d-95cb-49d3134e9f9f | -3.11844 | -53.26197 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c083c7ce-4812-3889-bef5-d8fe07935cf3 | -3.09917 | -54.03735 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 421d22bd-141b-3c49-92e1-fc8c0051a472 | -2.73887 | -54.16677 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58839215-a67e-3d02-be11-97560ce1dd56 | -2.58323 | -51.92301 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 53d30170-471c-3776-bd35-a0ec02d413a8 | -2.5995 | -53.96548 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42a8e894-dd8c-3c4b-863d-e687a1471dd9 | -3.24462 | -53.63461 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5586a6f4-71aa-3157-b7a3-0e9434cbe094 | -4.66269 | -49.5232 | 2024-11-28 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0dd1601-d472-3aff-a34f-09454eb6dc30 | -3.50351 | -50.32377 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e19a2d4-984a-3c50-8b78-1d7be0a86f29 | -1.84689 | -55.57006 | 2024-11-28 05:18:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 501848d1-40cc-3132-9652-798df36e95b6 | -3.0504 | -48.51484 | 2024-11-28 05:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffa7fc81-7ed3-3483-8cbe-b6c05ab23006 | -3.46842 | -51.59087 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d120f5aa-4b4e-345a-b9e9-4c7bf2dd1ff4 | -2.17082 | -51.96897 | 2024-11-28 05:18:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4c2ff88-be00-3161-afc0-40a85dbeedda | -4.66318 | -49.51979 | 2024-11-28 05:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4bb82b8d-9df5-327d-8b11-522c324cf33e | -2.8285 | -54.60057 | 2024-11-28 05:18:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9550d2ab-cc42-3408-ad14-80be88bed6f2 | -2.18219 | -53.77847 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76e65ac3-10a6-30ab-8249-fbe19cd8b459 | -2.98436 | -53.89234 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee1eaf57-d4ef-36ee-8ce7-ed8cd4e5f560 | -1.62732 | -55.70827 | 2024-11-28 05:18:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45a25379-46e0-33b3-b8ee-0ef51347c34d | -2.43871 | -53.97268 | 2024-11-28 05:18:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91dc62e8-22d9-3e87-aed2-b734ed1afb9e | -3.03293 | -54.01995 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 667ac6d7-e38d-32c3-b27d-2cc5f0ff552e | -8.12628 | -47.98803 | 2024-11-28 05:18:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 95519dc7-6fb2-3ec8-a75d-fbb8415bdbca | -3.32675 | -52.76277 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d85c131-9d06-3ea1-9eb0-95924eb0e7f6 | -3.43963 | -50.12485 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 83e2dcfb-ac1c-3535-93c5-3e7bce92e004 | -6.08889 | -48.04316 | 2024-11-28 05:18:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95ae66e2-8ae3-36ff-90f8-782595ee16b8 | -2.7574 | -54.12135 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 6b5944c9-6707-316e-b4ac-dfa4f97beb3e | -7.83831 | -48.19609 | 2024-11-28 05:18:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1195aa6-c09e-366f-b722-ab0c835f5e05 | -2.80697 | -51.58443 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| beea6142-5c78-3358-a1e9-ac1c43f467e3 | -3.1767 | -50.28062 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78bb5ccf-4e08-37e3-95bf-c76c7eb51e9e | -3.59073 | -50.69471 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 41c1582e-3d39-3491-b34c-a831007b268c | -3.22532 | -54.18177 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88b7c26c-f32b-38c9-9268-c27db5098727 | -3.08384 | -53.29786 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e44eeb22-adf5-3657-bb0d-3a1a5d648897 | -2.86968 | -59.93106 | 2024-11-28 05:18:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3f9e06a-fe9e-3f95-9ebf-a410be65396c | -3.29845 | -50.35781 | 2024-11-28 05:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b73a22a7-75a6-33de-91b2-b2120844c98b | -3.56148 | -51.56598 | 2024-11-28 05:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1880a612-a8a8-38c3-9723-c639253e7ee5 | -4.73985 | -46.50962 | 2024-11-28 05:18:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c0cd4a1-3781-3cb2-a096-310c68271a20 | -4.21501 | -50.89672 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 03b5d4bb-3c72-3bfe-b9d5-840bb477a060 | -3.09862 | -53.25506 | 2024-11-28 05:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9c6e5ac-69af-3903-a229-c30c8cacea83 | -3.9649 | -50.18476 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a885795b-f4b1-3e24-9e83-661605093eb1 | -3.49765 | -53.81455 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18899c30-67e6-377d-8522-f0fdd5f3e8c6 | -3.08308 | -49.2077 | 2024-11-28 05:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d6aef466-f0a6-3f74-92b4-7f7f6f3376f8 | -2.14737 | -54.81979 | 2024-11-28 05:18:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71ceecec-2ddf-3038-84af-eaee6ca0703f | -3.29059 | -50.27384 | 2024-11-28 05:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11a98c4c-62af-384c-9af5-418e15823bdd | -3.0999 | -54.03248 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 467d768e-a629-391d-ae51-217ec4a451cb | -3.68207 | -51.85878 | 2024-11-28 05:18:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12d2853-ddfe-30d7-94d8-cb79580eb226 | -3.334 | -53.54449 | 2024-11-28 05:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README88.md)
