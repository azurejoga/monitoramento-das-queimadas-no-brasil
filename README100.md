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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b97c430-02d3-3c24-8fb9-82dfdb0abd6f | -3.03791 | -53.04254 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7054ba80-bfe4-3b5f-a586-cf12ea9bdbc1 | -3.03725 | -53.04687 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4b7561d5-9ccf-3473-8a6e-f0d4a1b369b1 | -3.03489 | -53.03761 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bbcf7a0e-736c-3112-959c-8e3bd578f82d | -3.03423 | -53.04195 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ac5ae5ac-5573-350d-9ba6-8cafe9492baa | -3.03358 | -53.04628 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 338caf9f-f616-34ce-b84e-fbb8b521bcd9 | -2.95328 | -52.78368 | 2024-10-06 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1628e08c-eab1-3df6-9a77-d21dfce7f0fa | -2.94955 | -52.78312 | 2024-10-06 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a428b8a-d1cb-3eb5-af70-a878382d5c43 | -2.94887 | -52.78766 | 2024-10-06 05:10:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b8e899c-4f1b-338d-9b07-50313ec76e5a | -4.15985 | -53.61967 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bb37d06-d36f-3b8c-852e-19e71257c086 | -3.53519 | -53.75131 | 2024-10-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 286a229d-fd40-3e0b-b4d0-0d8f2461b309 | -6.22742 | -53.32902 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| edfb903f-1c51-3d23-92d6-f8ff9e8114a4 | -6.22675 | -53.33358 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a627bcf-6526-3e48-8ea3-e827e77641b5 | -6.14805 | -53.41793 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8fbe1588-df6a-32a7-927b-8952c7bc2773 | -6.21763 | -53.29027 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71db60d6-5b90-3cb3-a1d0-e529de71e16a | -6.21687 | -53.29293 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3a069f46-a447-343c-8389-b0f3dad93719 | -6.15181 | -53.41841 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d65d95f-6917-39b4-a5a7-dd1c6cbe6ad0 | -6.07791 | -53.36733 | 2024-10-06 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e848c7f-47b7-356a-8a40-beaa017b664e | -6.07416 | -53.36677 | 2024-10-06 05:10:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1758f8c2-7fdd-375c-a317-ba19df07b86a | -5.9299 | -53.42569 | 2024-10-06 05:10:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea0e57ca-392f-3807-8e19-495122136870 | -2.15361 | -53.66156 | 2024-10-06 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2680ab96-d947-33d9-9b1b-10ce0099f16c | -1.75086 | -54.00727 | 2024-10-06 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aaea57ae-3661-379c-baaf-4778bb78b3ef | -1.56148 | -54.77383 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bea396d8-f01f-3f8f-9123-37f68af1c9f7 | -1.55811 | -54.7733 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 279a8667-0683-350e-a6d1-fbf48b931f1c | -1.55474 | -54.77277 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0cc7a4b-15c4-3da2-977f-3bd82e0284ae | -1.55419 | -54.77636 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a263a0cc-b3d8-3040-8c9d-12a52a67ffab | -1.55138 | -54.77224 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 237f3b96-fc14-3acb-a513-d7804330e766 | -1.55083 | -54.77582 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3720f802-99cd-3a8f-b2e9-98ff346aa658 | -1.22586 | -54.22091 | 2024-10-06 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 386e3bda-c145-3ef8-8ef3-ec708cfea4e4 | -1.22529 | -54.2246 | 2024-10-06 05:10:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 311a338e-a7e1-33c6-ba7e-1f82762063f5 | -1.16357 | -53.78387 | 2024-10-06 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 754f5d96-c850-3aca-847f-15ac6f3f2171 | -1.12617 | -53.64495 | 2024-10-06 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 41993d25-3c8d-359f-9c08-bec788430696 | -1.04101 | -53.54011 | 2024-10-06 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fa90838-c87b-356a-bd8b-0fe3e8221f74 | -1.0375 | -53.53957 | 2024-10-06 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2592d932-7dc8-3dbc-a75e-6e654fd4a9f5 | -1.03195 | -53.73427 | 2024-10-06 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2b2e87b-f47f-3988-891b-9359d2347802 | -1.02913 | -53.72963 | 2024-10-06 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3c42920-acfc-3be1-b09b-73a3ddb192f7 | -1.02849 | -53.73367 | 2024-10-06 05:10:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0337fe12-18f0-3e28-81fc-84bfa145f527 | -3.13903 | -53.68533 | 2024-10-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d1562f10-1cda-3297-98d7-ee651a0c180c | -3.07255 | -54.78589 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f25fceb-9ef7-3f3e-a260-ad4d3fa0a890 | -3.06915 | -54.78536 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 16bc0b40-d3cb-3c90-b9c1-3a6668df6f75 | -3.06744 | -54.7738 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fdfffe86-71d3-3986-ba36-c5a15993f6b4 | -3.06688 | -54.77748 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c926bf3-8f73-3583-8560-c9c6951cb910 | -2.96268 | -53.72618 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7b0752a6-55b1-3c1d-a2b4-bc0ed5a47bfc | -2.96037 | -53.71761 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a29ab652-272c-3e81-b5e4-b7c8c2681417 | -2.95975 | -53.72163 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adbbcb05-449c-3ffe-9b2f-09be184e37e3 | -2.95914 | -53.72563 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8830e568-c70c-3cc3-8c2b-a5966e240389 | -2.95559 | -53.72508 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a5e60d3-6d97-3dde-9250-82d463ae6437 | -2.94803 | -53.70337 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 54165103-c3bb-350c-b14a-44d118c65c7a | -2.94741 | -53.70739 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0edeb1f0-9e8b-373e-befa-560396a34f1c | -2.938 | -53.69769 | 2024-10-06 05:10:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77e121f3-2c12-376e-8d2f-3f0f4e6cd62b | -2.91381 | -54.76529 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 565fcfa7-d5f1-3891-a065-650ad229a960 | -2.90184 | -53.86308 | 2024-10-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11954d3d-4aba-37f0-bf20-f2a88b00ce55 | -2.8122 | -54.58453 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58b6581c-c0a0-3959-a6b7-dceefa489aab | -2.81163 | -54.58824 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca3b2afc-efa6-38c7-ace7-c293ff3a9126 | -2.80879 | -54.58401 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45842b70-2f2c-3593-ad81-de1a53b1f7a1 | -2.80195 | -54.58294 | 2024-10-06 05:10:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4d1c4c7-7db2-3a19-a0ba-9c4edbe55be9 | -2.74716 | -54.93736 | 2024-10-06 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8734690f-99ff-3d7f-b16b-f92c0b4db20f | -2.66831 | -54.96619 | 2024-10-06 05:10:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aab9b39b-1c82-3b5b-ad0c-dd7436f3e6d6 | -2.60759 | -54.54583 | 2024-10-06 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 552e3359-d8ad-3403-b4fb-dac039e589a1 | -2.60418 | -54.54528 | 2024-10-06 05:10:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7edab40d-4700-3c3b-966f-aa211eebfdb1 | -3.53258 | -54.48955 | 2024-10-06 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bda2518-fc3d-38f9-9dde-f20c049a8122 | -3.52913 | -54.48902 | 2024-10-06 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dc4494e-8d55-3ffe-a491-e1ea28ba24b2 | -3.87028 | -54.233 | 2024-10-06 05:10:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa9f3cac-8582-3301-8320-2ee7eb2db093 | -3.85647 | -54.01767 | 2024-10-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f631075-87b0-3dd3-a463-c4e4f34e350f | -3.85294 | -54.01714 | 2024-10-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3f94d93a-b842-3bae-805b-68ff75940111 | -3.79585 | -53.94038 | 2024-10-06 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43d36929-757b-30f1-b0c2-dddfbb5b7dc0 | -2.19077 | -55.12594 | 2024-10-06 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c06f9ecc-430a-3699-b7f4-23c588500cd2 | -1.79395 | -55.2702 | 2024-10-06 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 066b7eee-69dc-35c3-8fce-0cd93bff73a6 | -1.77026 | -55.64045 | 2024-10-06 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44cc82ad-50d7-3c68-b47f-e4813142b0e5 | -1.46722 | -54.96733 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20f842f8-c48e-34c1-bf51-cad9fd62006d | -1.46442 | -54.96326 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 53e3b1d2-9b5d-3965-bce9-9964b8837892 | -1.46387 | -54.96682 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1eadb0db-cd8b-3163-b8bf-33946ec8462b | -1.46331 | -54.97037 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27162897-5a48-35b1-acc9-7ab116ac715f | -1.46052 | -54.96632 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dda06ad1-1cc7-3bb2-89b4-156db4c309f1 | -1.45996 | -54.96987 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 142ec2db-6549-3c23-884d-9700a022743d | -1.36709 | -55.3896 | 2024-10-06 05:10:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dfbec770-2919-3c0d-aebc-02ad9433d57a | -1.32059 | -55.51365 | 2024-10-06 05:10:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d881442-f0fc-3608-9e99-b830c09b75a2 | -1.20773 | -56.21337 | 2024-10-06 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 207e4962-5959-3938-a4d4-66ff908490ed | -3.54009 | -55.46156 | 2024-10-06 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49b7da23-9ac5-3b66-81ca-f95e169e77cf | -3.53675 | -55.46105 | 2024-10-06 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d714b15-af07-3270-ae6d-050f3e1483a6 | -4.86725 | -56.20282 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c82227-6bf8-3f98-8e70-7d8c2e97db02 | -5.09181 | -56.18083 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f68494b9-47ed-33cd-87c9-fc2adbcfd7cc | -4.77552 | -55.85149 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 43aa17da-cbc7-358d-879c-211e24d571e1 | -4.23449 | -56.28848 | 2024-10-06 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 249156d1-94f8-3dc9-aa5b-d1d4c7bcfcf1 | -4.13335 | -56.10954 | 2024-10-06 05:10:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e0438d3-2715-37cd-b2af-9b01f7eb9762 | -4.06121 | -56.31102 | 2024-10-06 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2634a7b-7cb6-3977-965f-704fe52ff81d | -4.0556 | -56.28187 | 2024-10-06 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e81243d9-af83-3ba5-a07d-ec8deb6caed7 | -3.94111 | -55.83698 | 2024-10-06 05:10:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4f94f81f-220a-3062-b547-43f9b02bcda4 | -5.12211 | -56.11748 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34e4505f-0b13-3d9e-b1da-94c1b92a821e | -5.11689 | -56.25975 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37143d69-48a0-3257-aa21-17e0c8361a82 | -5.11635 | -56.26324 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 426462fb-4dee-3262-a700-248a84e5b2e4 | -5.11357 | -56.25924 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4a6ad67-a5cf-3eba-89f5-043c2791cb10 | -5.23662 | -56.05968 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81d89346-e0d1-3aa8-8ea6-357a3551e9b8 | -5.23608 | -56.0632 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95fe1580-0a41-3c56-a2f1-a68b6b35d618 | -5.11303 | -56.26272 | 2024-10-06 05:10:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8443a741-0793-33b2-9b5c-3d4db8a26622 | 1.34516 | -56.14463 | 2024-10-06 05:10:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe67ac09-83cf-3ad7-84ad-00d367f937b7 | -5.97044 | -57.67444 | 2024-10-06 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbf0f111-adc4-3d74-9f99-d4d48429d7f0 | -5.73913 | -57.54549 | 2024-10-06 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67fb5510-e321-320d-b7dc-be2160a625b7 | -5.94297 | -57.69843 | 2024-10-06 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd144987-e336-368d-be45-444c21168d91 | -5.84187 | -57.75676 | 2024-10-06 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1fea141a-5440-335c-a8f5-59eacd6dc8cb | -5.82146 | -57.73584 | 2024-10-06 05:10:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README101.md)
