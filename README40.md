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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04617c77-2eab-3426-8bd0-e3bec230f2c8 | 1.30008 | -50.88588 | 2024-11-13 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 903cf4d9-34b9-33a8-9887-7098d2a962fa | -3.35442 | -48.95958 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 2eb50c17-1125-35f6-9fa8-4325cf6720ad | -3.22799 | -50.44469 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 58ab9fa7-c726-3ed7-a88c-320f2951dc5c | -1.23275 | -52.52749 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce3fd734-d1bf-388b-a8dd-d35dcbbf8063 | -3.84819 | -51.05267 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5d4d77ed-999f-3514-bf61-fba35e02d88a | -1.35084 | -51.40021 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f65e816-17f0-39f8-8ce7-fdfb866c8830 | -2.24999 | -53.74973 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b27f753-b43e-3c48-8a35-b318564f2ae5 | -1.61287 | -52.5331 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 387c33f7-dc9b-396b-ae90-0b709dd9ca4c | -4.81894 | -48.75611 | 2024-11-13 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa872440-bfe2-3f1d-9224-036fd50286de | -1.57019 | -52.02061 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a0a1a12-bff0-3160-963d-53ad069b228e | -2.56405 | -54.00315 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc6bbe85-01e7-31ce-84c3-c01c53cdc0b2 | -3.39547 | -52.40172 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11b6b164-4a0d-3d07-9efa-48c55a153189 | -0.3718 | -51.74181 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20fb73e9-1787-3b26-9b4a-94e657559c36 | -2.62327 | -54.27771 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 766ec7df-99e0-34a3-bbde-a823b149d7e4 | -2.9352 | -54.45839 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 982a2ba9-1fdc-3e36-baeb-a4c12a41b08b | -3.05746 | -50.3387 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43100c0c-c4fa-3015-bb40-32aa6b09af72 | -1.63663 | -52.53322 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 255b6860-021e-3650-92be-2d3ca85729aa | -1.21512 | -51.78375 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ddee7d8-34b9-3949-8801-edae363bd467 | -1.13275 | -51.94578 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d208ec98-16b8-3877-9df7-0884bbbcf578 | -2.6831 | -57.37634 | 2024-11-13 04:57:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7f5a12f-3efd-3450-a188-769139cceb53 | -3.25381 | -43.26267 | 2024-11-13 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5485d00e-f083-3a2f-8868-39c5943d2161 | -2.60818 | -54.02765 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82885df5-4877-3228-8017-578a2c8ac399 | -2.83978 | -53.3497 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79a7a109-e577-3c1f-9e2d-4ef8f9c0cb6d | -3.0799 | -50.33783 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1645c56e-fa82-3a13-9b87-a529104af915 | -3.07026 | -50.32768 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1047e4c-ba83-377a-a13d-6f4eb96788c5 | -3.25737 | -54.53022 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ebb78043-3311-32a7-b337-0f02d72c73c7 | -1.46904 | -52.27557 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57846281-b48b-3f9e-8815-ef28b2c32fd9 | -3.57897 | -54.64859 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4dc134d0-b02f-32df-937a-cbd246ce73f8 | -1.25276 | -55.69118 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6896df18-01eb-349f-a290-6b59d9a99a0d | -4.3332 | -46.54264 | 2024-11-13 04:57:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c7e9e205-4952-3cb7-8b52-04192ec7b602 | -1.83022 | -55.34959 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4ce7f56-cd6f-3af1-a00d-763cacaa65c6 | -1.35142 | -51.39654 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 775e3738-cd84-39d6-b928-5394ca4e8fe5 | -2.03043 | -54.47791 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24e72a14-f64d-32a9-8178-6bf98fe3e270 | -2.36467 | -48.56916 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab36c393-f0bd-3a2e-bfb0-ab0ab9c6c067 | -2.54859 | -53.99372 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07ddbbbc-f92c-32ed-b6a6-ab2fc462d2d4 | -2.36227 | -48.5189 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c73d2ff5-aeb2-3a62-bdcd-0c1a37f39f71 | -2.66892 | -46.82196 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8b08043-0be5-3276-9468-d0fb46898651 | -1.64381 | -52.53077 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 243698f8-955f-3ed7-a22e-c433416781b0 | -3.01525 | -54.11959 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48dcdb99-4143-3b70-bb3e-12fdfe04f2d8 | -3.81084 | -52.35224 | 2024-11-13 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2680d709-234f-3ab4-9f39-a9620c19c791 | -2.69245 | -51.80108 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 689b8c93-3a9a-3f94-83ed-dd104689d21f | -2.9834 | -53.71695 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d03ec4ed-4033-3035-97d5-8df90865a419 | -4.29894 | -48.09878 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c13e223f-6bda-3ba5-a4b9-4052b7fe29aa | -2.60542 | -54.0237 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 321f890b-ac59-3745-8555-597f188dad52 | -1.40701 | -51.1082 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6e99a34-4ce6-3b4a-9b9b-3d23c4412955 | -2.72707 | -51.7352 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a74bcc94-c36f-3852-bd9c-55988f315191 | -2.99868 | -51.45645 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 625de7a3-d652-3954-8e5a-1ce5822e3aa6 | -3.25301 | -50.30597 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 809eaf83-bd63-3693-ad28-cc845a0f92c4 | -3.29594 | -53.85036 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0721674-f17b-3082-97d2-4a8d90ab2bd6 | -2.60846 | -46.17116 | 2024-11-13 04:57:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 73cd8a46-8fc7-377b-b61c-674083cc19d3 | -1.21451 | -51.76533 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc5c77e2-9b1e-310c-9616-9ea39393f6cf | -2.73642 | -49.35093 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9918b708-f8d6-3829-bb60-43e3e69203bf | -4.50027 | -48.7977 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 95c2367f-8b03-3bb7-8d4a-b5664359a44e | -1.41104 | -51.10497 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c689b529-384e-342d-b6c8-8332a4da4c75 | -2.71687 | -51.71104 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6d77aa1f-c660-33ce-b983-c836befd308e | -2.46391 | -53.96942 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bb886e44-2215-3327-b5c8-75d6dda2ecad | -2.73164 | -45.29636 | 2024-11-13 04:57:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 75da0a79-b0e5-3db4-a254-464bf62def3e | -3.0881 | -53.26193 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7eeecac-6172-3342-881d-7be8bac6d221 | -3.25274 | -50.58306 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e99014d-af63-38e6-9142-7bc614ff7a1b | -1.82672 | -50.97951 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed860afc-7847-34ed-a0e1-36b4057046ad | -3.16132 | -50.5916 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5bf148d7-4fb6-3809-b85e-3943e481fbc6 | -3.5486 | -51.59524 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 550dd88a-f733-38e5-a5b7-407299954d2d | -2.55851 | -53.99524 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b1a7ad-b91d-3410-8a1a-eaa70d2aa34f | -4.95387 | -50.03359 | 2024-11-13 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8efc1d15-ce49-3815-bd75-147739560765 | -2.44999 | -53.9285 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62c7d9bc-3ab8-33bf-b432-1e457314f176 | -2.47252 | -50.1199 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5b1b8655-b4c7-34b5-8e5a-fbd8091440c4 | -2.86637 | -54.20255 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79dd4606-a0c6-3860-86bc-551b1e6b55a5 | -2.98187 | -45.16005 | 2024-11-13 04:57:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 594c1472-c0bf-3f2a-843c-b457f81c2c96 | -2.21755 | -50.77034 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73eb7263-9453-3c6d-ac99-dd5611ba18c8 | -2.27276 | -50.67196 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92ee272e-b580-3372-a0c7-66820622a18b | -0.38466 | -51.74743 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a1c260d9-a0b7-3b42-bf1c-7bf56c7cc608 | -3.6642 | -51.40969 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b81f93e-bd48-3f96-83c0-86504ba54c3c | -1.5781 | -53.73936 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8520d37f-9230-3480-a5d1-433e51c25879 | -2.90845 | -49.23031 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0b1c5776-1191-34d3-84c3-45b44f23dcab | -2.72876 | -51.74673 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d9a0b8ed-a22d-38fd-99d1-2c4e33c799dd | -2.80647 | -46.65485 | 2024-11-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26e26da8-1d03-3d3d-a26e-3df4834e2bcf | -3.34651 | -48.95837 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| dcbdb094-5705-38c0-8d93-66af9c65d321 | 1.05346 | -60.59247 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 668109ca-6d6a-33a0-b30f-926bc29bebde | -2.32274 | -49.0886 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7fd370d-d2a7-389c-ba96-7118057b4e66 | -3.02674 | -50.97591 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4842b7c1-9acf-35b4-ada6-11b6c74b8d4d | 1.5944 | -55.77244 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d737dc0d-47b4-360a-b52a-d6d5c6b64bd5 | -4.56652 | -49.38645 | 2024-11-13 04:57:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| cab51208-3017-3968-9412-6353be3625fb | -2.24892 | -53.7566 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ec6c87e-051a-3cb3-b171-0da37f02e232 | -2.30089 | -50.39011 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bfc3556c-c907-3948-ac65-f2fba167e29f | -0.89339 | -51.73088 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bd419719-df92-34da-9c36-12c38d6e6840 | -2.39517 | -53.73354 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcdf4c28-919e-3cf7-87c5-a1027a7ce456 | -2.1497 | -52.09487 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 885b928c-53ae-36a0-973c-53ef9d040c62 | -2.62882 | -54.28567 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c32fa915-dd52-3c31-bb95-5375de3f8e62 | -3.72645 | -51.32844 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1a45605-8178-3151-85ab-a8e756addc3f | -1.5347 | -51.11858 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fd3634a-ade3-352b-b6ec-d7c43f6918c3 | -2.37203 | -53.86015 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29ded8cb-7856-3e22-8f5f-ccd3fa707eb8 | -3.27882 | -51.05992 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2abdaf0-314e-3c03-b974-6ba8c47a0389 | -3.53544 | -54.49218 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ca65592f-92d8-3710-acbb-6afef65cc8d9 | -1.98643 | -51.10069 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92ef4ec2-cbce-30cf-92ae-edd341047d02 | -3.03975 | -50.32839 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcbaabd8-1aac-380e-a4a8-a5c545e04cb6 | -1.30763 | -55.75121 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d8c69a5-5280-34ab-a2a5-e18828e66d33 | 1.05836 | -60.59173 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b911bea9-1b1b-36ae-bdbc-01816d4a7c25 | -1.95485 | -53.3312 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e0c8399-439a-3155-b39a-8aa9bd3884bf | -2.77236 | -54.73798 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abfcaa85-bd0e-3641-99e9-c1974706ee4b | -1.82808 | -51.08528 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README41.md)
