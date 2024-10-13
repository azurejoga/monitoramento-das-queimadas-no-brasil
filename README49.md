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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26637917-97fc-3774-9989-e3a04b15da58 | -3.91709 | -51.23349 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e19dda40-5fae-3705-81f2-8d19b2033d05 | -3.83133 | -51.40258 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45e15093-6752-3c57-aa63-f07567586c72 | -3.83071 | -51.40648 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 583baa99-e64f-3c94-961e-8b3b04fd31e7 | -3.83009 | -51.41039 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0f43299-e544-3afd-bf50-26b330a6d16e | -3.82783 | -51.40203 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23dc8fe3-e4e2-3d5a-b606-0117804313c9 | -3.82721 | -51.40593 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf9bd681-d00d-3a9d-ab26-6404e8ad35be | -3.78375 | -51.31944 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69aff2ce-598d-3f15-8c91-bd2f24f3224f | -3.68608 | -51.07289 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba40647b-932f-37f0-be63-b94b6fdd5a50 | -3.68547 | -51.07668 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3127700-b797-3cbf-8dc8-692431e7d5c5 | -3.68485 | -51.08047 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7b79826-9949-3558-b930-e91c7e0f6358 | -3.68226 | -51.08044 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e23aef0d-6f42-305b-a2f7-294ddacc2112 | -3.68201 | -51.07614 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ccb0bc7d-ae0b-3728-b528-ba2231dc2cf3 | -3.67881 | -51.0799 | 2024-10-13 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a098a87-ac4f-3565-919d-83551f1f42e9 | -3.65399 | -51.26022 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 780df61c-a79f-38ca-b98f-3776f5ea5ec4 | -3.65231 | -51.25948 | 2024-10-13 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82c05663-024a-334a-8b3a-9640fdf3e31d | 3.52555 | -51.76852 | 2024-10-13 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b4de150e-12ed-3e54-9c81-84e4666ba7f1 | 3.35251 | -51.34126 | 2024-10-13 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52b07ee7-6a41-3730-91a8-4b1adbaf2e9d | 3.34381 | -51.30938 | 2024-10-13 04:38:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f67252f2-5e6d-38d4-a2b6-f922c91ebe76 | 1.05928 | -52.20571 | 2024-10-13 04:38:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 586633fb-8553-30d0-95d4-20c695d5062c | -0.42741 | -52.03616 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6938012-424e-36fa-ad1d-ccaefef86b23 | -0.42618 | -52.06847 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a78d62f1-18cb-30b3-8696-7939f33b7b5a | -0.42241 | -52.06787 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bc7a9d4-802d-3da4-a666-1c2fa4a38ed2 | -0.12825 | -51.57713 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb23bba5-f625-3cf4-b22f-e24fc320a08a | -0.12493 | -51.57814 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e74fa03-88d3-3c2d-82f5-71aa243c470f | -0.12458 | -51.57655 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3191209-c08a-30a1-acce-c7fa2254ed91 | -0.11557 | -51.63906 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7a8d7ec0-cccc-3d98-8e1a-8fd27e9f7243 | -0.11414 | -51.64172 | 2024-10-13 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f83b13e-05c2-3e9e-8b92-9906ae6792d9 | -0.83822 | -52.36081 | 2024-10-13 04:38:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 169916f2-ad30-3514-b9e5-1ce2dee239b6 | -2.00583 | -53.30054 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be5562f0-6b78-3052-b678-22ec5c667338 | -1.74447 | -52.24764 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cd97093-7ae8-306f-af47-87f69df6532c | -1.66865 | -52.03704 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1b016b0-8c18-35dd-b08d-14c6b45ebfef | -1.66311 | -52.13402 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb093e4c-32bb-3436-a509-44be315cdd1d | -1.66239 | -52.13847 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1b138af-5782-397d-a336-acba69070f89 | -1.66089 | -52.13554 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89df7a33-e917-308e-b2ec-1a90da8bb1c9 | -1.6602 | -52.14 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f30cc407-c820-39ff-a3f1-6de1643b27d9 | -1.65938 | -52.13346 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fcfbbf4-90d8-3af7-862c-45f86ef4d6c1 | -1.65866 | -52.13792 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f4acc0c4-c850-3d4f-865b-4203f25bb400 | -1.65647 | -52.13944 | 2024-10-13 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8db3e303-f736-393c-972d-6cd9ba2fde3e | -1.62335 | -51.94061 | 2024-10-13 04:38:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d49093a-25d8-3f05-8ff3-d89c262234f3 | -1.62036 | -51.93567 | 2024-10-13 04:38:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 540a1501-f67e-31a9-b87c-8a83e210cdc5 | -1.47502 | -52.11699 | 2024-10-13 04:38:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27d7aa83-8006-34e1-ac47-9da22ac7f4fd | -1.43897 | -52.8644 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0caf1a84-99ec-3c1e-939f-838fee8b8138 | -1.43594 | -52.86208 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d0ee47cc-c9d9-358e-b10f-9b3c4a818a58 | -1.43582 | -52.85893 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d7fe44bf-27da-34fb-8418-7bf3c96c9d01 | -1.43514 | -52.86697 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 164a2e28-674d-38ed-b9be-3283c39dedd7 | -1.43506 | -52.8638 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9373e7c9-e4c8-30fb-9524-5f3e9183b7c7 | -1.4343 | -52.86873 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bcdf481d-56c9-3e66-b4eb-54930f1407a7 | -1.43203 | -52.86151 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| da58b4f8-295a-349d-b663-c6049bccdf5a | -1.43116 | -52.86322 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f055850-a6b5-34d6-9671-4f1fb2fd7531 | -2.66532 | -53.35168 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c69840a-fd44-3d7d-9d8e-f9a1c663baf5 | -2.66137 | -53.35106 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62ab2576-3fa3-3637-aeb0-8d21aaa6f5f3 | -2.65742 | -53.35044 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8708957-eb7b-374d-a941-569648ebab88 | -2.65346 | -53.34982 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2bf479f0-221f-3e69-be7b-4690b2c0fdb0 | -2.26255 | -53.47683 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db553ff9-609d-3f41-bd1c-4ee2eb6418b0 | -2.25854 | -53.47619 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6986e11-d3a7-3491-82ea-97f7e8c2dcbb | -2.25798 | -53.47966 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8912a596-5653-37d2-a917-f7b535ccd52b | -2.25743 | -53.4831 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cebe82ea-e92b-3fc8-bc66-1eb70f3e063e | -2.25342 | -53.48246 | 2024-10-13 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a639099d-7a5f-3ad9-bc29-946c7bd4c4c1 | -3.52134 | -52.74948 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fdb322a-e371-3700-9fb2-c8915f7977aa | -3.42774 | -52.77407 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23aa4e52-fe45-37a3-bbf5-f7db64791ea6 | -3.10588 | -53.03674 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 09cc248b-957a-3ccb-9886-60d0e7fd8830 | -3.10435 | -53.04625 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7c68637-8927-34d4-81e6-22f995d40811 | -3.10202 | -53.03616 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f57a3db6-60ca-35f6-b5c8-abfaf6fc08be | -3.10049 | -53.0457 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 9896239b-f989-3d18-ac49-39fb621b619c | -3.09817 | -53.03558 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 5cfb4f2f-82ed-3a68-afa9-f6ea894c441b | -3.09739 | -53.04036 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| b2791e63-8aed-3756-8233-96595904dd25 | -3.09584 | -53.05 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| cf1cb51a-fea3-3134-84af-623d7d579c1b | -3.09431 | -53.035 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0bad0aaf-61de-3324-acdb-1c71f2abf4eb | -3.09354 | -53.03979 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ac13f6a7-c1a5-3868-bd1a-d9441b4713d6 | -3.09276 | -53.04462 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc642e7c-b3d3-391c-8376-8009e15f8975 | -3.52039 | -52.75065 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bac5432c-a19e-35e2-8cc0-b303f02b507a | -3.40639 | -52.49529 | 2024-10-13 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02339de9-6b1a-3504-b289-ebe122e33131 | -3.38828 | -52.4425 | 2024-10-13 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f27f606f-4c1d-3303-add6-2ca1a8ee36c8 | -3.23477 | -52.88612 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| baeaa6d1-c79b-3188-906c-323b3efbb526 | -3.17872 | -53.16037 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afd2b0f5-1f01-3b61-92ec-7c7da2933769 | -3.10126 | -53.04092 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 0920e3ee-f4e9-33ee-bd24-7855f2acc531 | -3.09971 | -53.05054 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 91a6f768-033a-3886-b033-1694162d6648 | -3.09662 | -53.04516 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| aeff4d58-f5ec-3c7a-981d-17f4beb422b9 | -3.09045 | -53.03444 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2c86a2b1-e7ad-3809-b71b-739115afd853 | -3.08968 | -53.03923 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0faa4446-2956-3b76-bca0-3c4e0226a6e4 | -3.08889 | -53.04408 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7a2ee94c-ea8d-301f-bca6-a2e67e7c9038 | -2.98632 | -52.90845 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b29c066-3f26-3f9e-aafa-0ad07f8d0157 | -2.98325 | -52.90317 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b145d58-49c4-37b6-87cd-a74469371609 | -2.98249 | -52.90786 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4db9b0c0-0569-31e6-b105-1e794fcf4100 | -2.9756 | -52.902 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0ba9bdd-e94e-383e-b562-1c863e1e1862 | -2.96719 | -52.90539 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13221bc7-4ab5-3c8b-8daa-8b3a5c3fbc39 | -2.96261 | -52.90938 | 2024-10-13 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dc8fcb9-b577-31a9-8906-58d7643c45c3 | -3.73922 | -52.43111 | 2024-10-13 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc14d431-ae80-3a61-90c3-3e3c427711ab | -3.56307 | -53.5215 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 964a9fac-829c-3d0b-bf4e-8115c3bbd8c3 | -3.56227 | -53.52649 | 2024-10-13 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f81c896e-df9c-3a30-bbfa-07b417c9888c | -1.2652 | -54.67969 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0d00bd9-0c03-3ef1-b1d9-e4cde8f40d3f | -1.26518 | -54.6813 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bfd5980-7ed5-339c-83ad-b3024cd2f6db | -1.26448 | -54.68579 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd00bbbc-3aac-336f-8702-5d561591527a | -1.26447 | -54.68415 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8698bdbe-9ec0-3d12-b401-a53296f3519b | -1.26078 | -54.68051 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43e419d1-6a81-377b-816e-28673b3f2205 | -1.26006 | -54.6834 | 2024-10-13 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7e93dba-69bb-3efd-adbe-339306f1f0c7 | -1.23164 | -54.11586 | 2024-10-13 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 54c98c95-c840-386a-a4ea-83d165bc1044 | -1.2303 | -53.37583 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0597dea7-c157-30c4-9920-b30e090725a5 | -1.22626 | -53.37515 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7378e255-edf7-32a8-b93d-301eb5d6c067 | -1.19917 | -53.38916 | 2024-10-13 04:38:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README50.md)
