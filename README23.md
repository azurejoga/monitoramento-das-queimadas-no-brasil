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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 600cf96a-260e-33b6-acda-f65e4f1908cd | -3.08604 | -51.21921 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 07875d43-c74a-3259-bffd-8c3dcbac00c8 | -3.08092 | -51.21422 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d239fb01-fed5-3bd6-adad-78eac76fda6e | -3.04792 | -50.98389 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eee78dfc-36f9-349c-8fe7-3066e4067ec4 | -3.04192 | -51.01956 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 79a67636-8078-33e6-b3d7-1600e14953eb | -3.04125 | -51.02357 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 4ae5cc50-743b-3bf9-a065-8de47b264362 | -2.83863 | -51.30354 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf8f31d6-4a11-33cf-9e44-ace89aeab199 | -2.8335 | -51.30427 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e1d2bee-4c9f-36c4-b441-9425d677fcf3 | -2.82068 | -51.3456 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 634cf9fe-7858-3e40-bc45-a76d1a0f7fcc | -2.81964 | -51.34384 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f80307f9-8699-34dc-9b21-6b260de60d80 | -2.81549 | -51.34042 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89e1dfe7-4773-36c8-b3db-908144087f70 | -2.81408 | -51.34893 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0cd2193-8c86-3f6b-9e64-360a433510e4 | -2.80019 | -51.35982 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0000d0b4-a875-3305-9c36-e7a8a0d178e0 | -2.79358 | -51.36316 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 91454030-2dd9-31c7-8d98-ae9b7ea37905 | -2.78769 | -51.36219 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9378fa5c-f623-3f01-b9bb-2fd2027e7788 | -2.76852 | -51.9693 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 85f9b65b-c8e9-372b-8903-6087b8c00109 | -2.76773 | -51.97401 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68e9db9c-334f-3350-8f93-651ab84d56b5 | -3.72113 | -50.71982 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26acb468-915f-3b44-b612-0f22a1a8610b | -3.54861 | -51.5243 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc5a755d-cbd8-3545-af1a-d96c62b11b98 | -3.54738 | -51.17621 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e223dd0-3c04-384e-b65a-27b4a58395e9 | -3.47563 | -51.21426 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d51cb00c-3501-3d6e-afac-a64fb1fbcfaa | -3.43476 | -52.06078 | 2024-10-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2c50f67-313f-375a-970f-35a35b0efc88 | -3.39581 | -50.80061 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77d9a5a4-801a-31ab-a144-de5377bcebab | -3.39517 | -50.80437 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 90d1c13a-8a12-3f84-accf-583b37e92497 | -3.39025 | -50.66398 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 5e2966f3-0fe9-3959-b1bd-069af44991ab | -3.38893 | -50.67166 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 59d6e877-36e0-3ed1-8b85-3d1af8b895ea | -3.38829 | -50.67542 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 82e1a3e7-42cc-3f94-a968-2a45ef2265f8 | -3.38399 | -50.66703 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8e6605e9-a85b-35fd-998a-cc4e3b917951 | -3.27714 | -50.66157 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11aba160-fed2-3d0f-9316-f18f7786659c | -3.27297 | -50.66117 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0d2d15e-e650-3d81-921b-007ab1b45436 | -3.27235 | -50.66496 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 948524f7-0a0a-34a2-86f2-1c9bc50dec13 | -3.24174 | -50.85192 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2be3ebe-befe-3601-95ce-af98efc30126 | -3.23956 | -50.84713 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 490d430b-4dbf-32c3-b7df-593f25da2732 | -3.2389 | -50.851 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4083764-597a-35ea-a745-382b590beba6 | -3.18136 | -51.25537 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f49751ec-d572-3c55-825b-87f212e6594d | -3.17624 | -51.25035 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d4c33ef-2fc2-3c10-977d-6c4b6413ded9 | -3.17559 | -51.25531 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b47dbdef-758f-3e26-bb43-da1c5116f5d0 | -3.17555 | -51.25437 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 70f7e5c5-f8e8-332f-864e-d684482c2f93 | -3.12982 | -51.34541 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 531a1244-a0e0-30d9-b461-962e96b5cc58 | -3.1247 | -51.34551 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ab9dbced-b691-37d3-b0c7-7d7ff0a215d1 | -3.1144 | -51.33514 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 44bab1da-4def-349f-8b31-41756201d7e6 | -3.04858 | -50.97995 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6d28c9a-b849-3109-b2e5-df4ce8f1c828 | -3.04058 | -51.02756 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| a22bc0b6-c0ad-3fb7-82bc-c71257427d77 | -2.9868 | -51.03119 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f21c1d87-34b2-36c0-8d5e-aa99ddbec85c | -2.98612 | -51.03515 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50cb45b4-1fd1-3c87-b190-b5239a902ad9 | -2.98568 | -51.03159 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62d000dd-8a57-3e3f-bc45-b6280f5ae990 | -2.98502 | -51.03556 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b3807b2-6f4b-3f6b-88e3-1430426bf07e | -2.85323 | -51.28862 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 674d3574-e92a-386b-a269-2e70b0fb9554 | -2.83937 | -51.30518 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7df5d16-e153-3f3a-afe9-650f047e8ecc | -2.83791 | -51.30776 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36e3a64f-4b13-365f-9c3e-fdc5b2e1ed78 | -2.83275 | -51.30266 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fcf4558-35bc-358b-bacd-4f961be46ae1 | -2.8259 | -51.27723 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f43bf6d2-4c0c-3e92-a361-27823419a10a | -2.81891 | -51.3481 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f82e1219-a9fb-3b7f-bf4f-bc6b9a46462a | -2.81479 | -51.34466 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48bef64e-fa26-3d92-9bd2-39f5be0f6324 | -2.81375 | -51.34292 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e235aede-83fa-3316-8eea-b07c7354a4ed | -2.81302 | -51.34716 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6023816e-2aaf-3d56-96f5-446969d62309 | -2.80819 | -51.34799 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebe86bc5-6cba-3c17-9466-47c5bef0beb8 | -2.79429 | -51.35889 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 519d4c90-ce1a-305e-9d41-2a86aa988a5c | -2.78697 | -51.36652 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e520991-2ea1-3c79-805d-c9d01133606d | -3.54931 | -51.52008 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 073e1e76-8fc2-3134-bf55-7282cba3ef36 | -3.54808 | -51.17212 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| afb12e2c-fa78-3eb8-8a2b-ad2c4a4d2603 | -3.54119 | -51.38875 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b88163cd-17d9-3cae-801e-f37ef67f52eb | -3.47632 | -51.21027 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8651215-8571-3f60-a89c-ec3fe40b8003 | -3.39644 | -50.79689 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4ba5260-7751-3389-83e8-9be426f9c287 | -3.39018 | -50.79969 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1108cfdb-9ce2-3c72-bcf0-18307e6c305d | -3.38959 | -50.66782 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 35173743-494c-337c-a684-2551398cecd7 | -3.38955 | -50.80344 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4427122d-0f9b-36ec-aa46-2d63d591c05f | -3.38332 | -50.6709 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9da5ec4d-2aea-3a56-abad-4dfcf3798a9b | -3.38269 | -50.67457 | 2024-10-20 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b17d661-c203-3781-a312-c96583c3333d | -4.63626 | -50.93777 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da0a799e-efb3-3a28-b367-e9edf58b27d5 | -3.86564 | -50.98133 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a49587e-c557-345f-9af6-3a989a9815d0 | -3.865 | -50.98523 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f82b3d07-b86d-326d-84e6-13ae29cb0cf4 | -3.86218 | -50.98421 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b420dc79-c01b-320f-af10-b4351fc2a895 | -3.8615 | -50.98811 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 946de8e6-b733-34f2-8b8e-0952d834bbd9 | -3.85935 | -50.98426 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64a313a7-6f2b-3d35-a790-52839b9cef92 | -3.72672 | -50.72062 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 682833e9-5bc8-3e88-b4b5-b8c0393e4909 | -3.86285 | -50.9803 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6b14386-65a8-3e6f-a540-5af6ab217d01 | -3.80211 | -51.60817 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f2ee9ca-b776-347a-a48d-059e43e0d6af | -3.77663 | -51.97409 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d379c16b-4df2-3c61-b23e-ddc232f6c72c | -3.77207 | -51.97572 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3459a360-05fa-3b64-afed-56929e998d2d | -3.70211 | -51.60113 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2cdce88-44f5-3415-ab00-83221f92723f | -3.69548 | -52.01229 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ae2f4bf-7663-3c91-a412-c4a582167de9 | -3.69393 | -52.01406 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1f12dd1-d34c-3fc6-b098-92dccda2ee99 | -3.64162 | -52.02865 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfdb3053-97d5-333e-85ad-01a6e7cc84b0 | -3.64085 | -52.03318 | 2024-10-20 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc7adbf6-b6a0-3caf-8f96-c29977b5bd44 | -4.25317 | -50.99419 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 80be15f5-29f4-3ae8-abf2-e3b631e5d127 | -4.24891 | -50.98526 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a0d23bd8-c35b-3e5e-8307-02378bf3a557 | -4.2476 | -50.99294 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea5ed99d-4458-3e88-8808-e5b7537eb0cf | -4.24694 | -50.99687 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dc98440f-7a2d-303b-9aa5-5787948e60d1 | -4.24134 | -50.99579 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a7321df-171f-3c88-982f-4fac4bf69175 | -4.17148 | -51.23286 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7896056a-200b-3de6-9747-6faa84f2e3c2 | -4.02315 | -51.01267 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01d10641-dbc2-3964-96fa-55d017794be4 | -4.0225 | -51.01649 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74c2328c-c302-322b-b2df-185c90ce3216 | -4.25384 | -50.99028 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 70f87022-5b2a-33c4-befd-c559ba92318f | -4.25252 | -50.99804 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 244ca44a-3242-3a9e-aa9f-2de5055b3e38 | -4.25014 | -50.97802 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9688dd9f-82df-35e2-86ef-f84a60103bcb | -4.24827 | -50.989 | 2024-10-20 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9ae029e-64a1-3711-b7da-fbe45dd18373 | -4.07532 | -51.13182 | 2024-10-20 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f8e09aa-fd01-3e7f-ac1a-2db661e14c8b | -6.08626 | -51.21449 | 2024-10-20 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d7c812b-f320-344e-bb34-6ca132eb90be | -1.99189 | -52.12949 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 804b93f1-8cf2-39db-99f0-356a82830e99 | -1.99107 | -52.13446 | 2024-10-20 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README24.md)
