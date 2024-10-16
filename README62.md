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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19311941-db11-3585-b413-2d0c8d268d49 | -11.76771 | -64.08746 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a40915ae-faa9-3c1d-8d95-affdce3ce43d | -11.76528 | -64.08778 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5d1bce0-f347-332e-b32d-b8ffea09a9ba | -11.76077 | -64.15012 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d903cee-d296-33bb-8ade-462eca67d022 | -11.75861 | -64.14178 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1067beb1-b740-36e3-9281-84be73e7af12 | -11.75795 | -64.14567 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6aef4302-6c57-35a6-ba5b-4a0a27a45e2b | -11.75703 | -64.1383 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80598252-43d3-3516-92c6-c3f1e1ec37e4 | -11.7564 | -64.14218 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 648f9fa7-e7d9-3898-817b-16d9eb78eb6a | -11.75449 | -64.15387 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b2be0d1-f0de-3209-ac2e-2bf8bd46daea | -11.74614 | -64.0527 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3815d13-fd0a-380c-b0de-b2aeb51af1eb | -11.74408 | -64.15211 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf600eb5-4489-3ece-88df-94c83c93959d | -11.73577 | -64.05096 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a62c953e-83da-371a-845b-9c73f5a6036c | -11.73487 | -64.03489 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb737673-abe8-3221-809f-2b65fce37cce | -11.73423 | -64.03875 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d7c6a99-dadf-3651-8ae0-30da4e113412 | -11.72951 | -64.04588 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2581a705-c8f8-3873-88b3-671e8942203c | -11.71222 | -64.15069 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0eeea84-70fc-3a31-a231-118099b2c6b3 | -11.66838 | -64.26411 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| afb3c59a-1d73-3e6d-b70a-c5c664f230f1 | -11.66718 | -64.04341 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44e5398a-d4aa-3a2a-ae17-5a5f946c331b | -11.66612 | -64.0426 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f97a0f8f-339e-32ca-baf3-b64811899e9f | -11.66489 | -64.26353 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 441047a4-4a3b-3ca5-b67a-712776f32e7c | -11.66091 | -64.03833 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a5c2d39-9a63-3d0d-a8ba-a73999c35f50 | -12.11721 | -63.76164 | 2024-10-16 05:25:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2692f846-8323-3f4f-b35f-f137e0906c05 | -11.79763 | -64.16436 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 462f5b49-13c6-3e01-a327-55fd0d1a9e77 | -11.79698 | -64.16826 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b02ee938-b5f7-3b75-93d1-41ea21e153ff | -11.7681 | -64.09226 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e59f6149-1def-343b-89cf-d292a4443137 | -11.76706 | -64.09134 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 009dd949-45fb-343f-a9c6-5eb99e515263 | -11.76591 | -64.08392 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33aaf73b-a1e4-38be-b69e-cc3acde9e0a0 | -11.76401 | -64.09556 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4bf231ee-2af0-3d48-81cb-041f8a1df314 | -11.75933 | -64.05893 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78127fd3-f98d-3920-84e9-2b52d606f031 | -11.7586 | -64.15055 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44adb8f5-0323-33ed-a647-a54006fb2fff | -11.73586 | -64.15873 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5799432-3e91-3565-a76b-1b72faad04d9 | -11.73359 | -64.04261 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21c05d7d-a470-37ca-8b07-f88eae060c18 | -11.72987 | -64.02211 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cdf059c7-44d1-353d-acc4-69cbbf7cb943 | -11.72643 | -64.0215 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5039e0c0-1904-3848-a222-0238c41a504f | -12.50841 | -63.97019 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fadf8b1c-e6c2-30e7-bd21-17d675d32354 | -12.50562 | -63.96581 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22caeb78-6e6b-39e1-96a5-313b2b7a4a4c | -12.49568 | -63.94073 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77ccc619-2803-31db-95c6-833ae7614027 | -12.4941 | -63.97165 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 926f90b9-62b2-3dea-9eb6-c2161a3d6982 | -12.49163 | -63.94394 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 00fdef1a-5c0c-3ffc-a033-beff430a289f | -12.48812 | -64.02934 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 955cb38f-3fc9-3753-aea5-f7e26fed9c6f | -12.48696 | -63.95095 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30fd0a31-b29f-30e8-98b7-84e2a7bfb6da | -12.48532 | -64.02494 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb36cfb-9d34-3d7c-92b8-98cba7480178 | -12.48406 | -64.03257 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3247931a-bd4f-3120-a4bb-1f21d3fb2cd1 | -12.48354 | -63.95036 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| e8b942ac-3867-3180-802f-e500cf027429 | -12.48126 | -64.02818 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b935b76c-4faf-33aa-80b9-6df1c79d5fee | -12.48104 | -63.96553 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d94eab0-5193-3d46-a567-083b4110740d | -12.47972 | -64.01615 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3eb6f89-2d61-3882-9b5a-94e974d3de8d | -12.47629 | -64.01557 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1e4166d-2069-3894-8986-ad36a5ba5d25 | -12.39539 | -63.73861 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddc37d4e-85f4-374e-92ec-c153617b50b6 | -12.39229 | -63.71502 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef3b2bc7-f6cb-39f0-8a64-cd15feffdedd | -12.39168 | -63.71875 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f7f0858-c07a-3070-85ff-9a38425d1430 | -12.3889 | -63.71445 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e382eff-e762-30c9-9f75-6489752756da | -12.38704 | -63.72566 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23438c60-ea77-3806-bc30-886019d0c092 | -12.38611 | -63.71015 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd0c35fd-36bd-39a9-a410-1d78ec47a7de | -12.3855 | -63.71387 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35c1772f-717b-3980-b99d-06f79aeb3727 | -12.36399 | -64.49628 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e0367b7c-ca41-38c8-bd7e-d110cd4885cc | -12.51184 | -63.97077 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f913d3b4-dd16-35d0-b3a3-0633950511f7 | -12.50499 | -63.96961 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d54bd61-ad1f-322a-9477-6eb48a092a65 | -12.50437 | -63.97341 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8a16ffe-342f-38e1-8632-17e331161674 | -12.50314 | -63.93811 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 454d748f-f948-3f9a-82a1-5d6567f2106c | -12.49505 | -63.94453 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da390358-9b04-3f1b-bf7c-5a47d9d2b50f | -12.49101 | -63.94773 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c70abc98-5d02-33d1-beb7-1a8b1448717e | -12.49068 | -63.97107 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4919d5-ae11-3f38-8aca-5d8c700fe6cd | -12.48788 | -63.96669 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ea091e-cc7f-388d-a9fc-8e7efb2f2b3f | -12.48725 | -63.97049 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a7b2b6c-71b5-3d0f-97ae-a3070098ebc3 | -12.48469 | -64.02876 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b160286-9195-3ba7-83a5-d239a6198b77 | -12.48446 | -63.96611 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc593bc0-d846-31e9-b432-34d2f61ab35e | -12.48291 | -63.95415 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 054095ad-b40b-37e9-b0bd-ce54d3d44099 | -12.48252 | -64.02055 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1645e17d-8eb5-3532-a6fd-aaee8e6dcbb6 | -12.48229 | -63.95795 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c28c4901-6366-3bb5-be29-cb080e39f116 | -12.48166 | -63.96174 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02cfb3c6-d6c8-3799-b516-dd4b834c3e1c | -12.47566 | -64.01939 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82026fa8-3c43-39f3-a633-d5fedb346cd2 | -12.39507 | -63.71933 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74b6d6c8-7d47-32b5-829d-26e850c94b69 | -12.39199 | -63.73803 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fefb97d0-19b1-3949-8b70-98a6aa2c3d24 | -12.38951 | -63.71072 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe74a6b5-1c13-32fd-8d84-744697181a12 | -12.38828 | -63.71818 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52e086fd-f2cd-3cfd-b68b-c43f950923a1 | -12.38766 | -63.72192 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04ac95a3-12c6-3d86-9ba0-f8d53e13f50a | -12.38673 | -63.70641 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2329cb0-2987-39fc-84cd-a1a659572a6a | -12.38643 | -63.72939 | 2024-10-16 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99f21123-7bcb-3edc-9129-0df7958d8b27 | -9.26895 | -65.56525 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 528cb62f-b1f4-329c-bace-985b2398bfc7 | -9.17756 | -65.39375 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28372f29-5e48-3e6e-8e2a-75d65ec1f07d | -9.17675 | -65.3985 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b837f35f-5df9-3106-94c8-fb825e8be296 | -9.17593 | -65.40326 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d5a409e-b587-3455-a10f-b116ff651b1e | -9.17512 | -65.40802 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b02ae9b5-1b1a-38ba-b13b-1c20d66cac8d | -9.17375 | -65.39309 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb374843-f111-3f2e-a6fb-d9d753f05288 | -9.17293 | -65.39786 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8498a1b5-19c7-3d15-a303-d28df1eae1ac | -9.17212 | -65.40263 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04e2dd74-2bdd-3817-ae6d-0777bd6f7dab | -9.17131 | -65.40739 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d80b202-8805-3a2d-b46d-e74968dccc65 | -9.16912 | -65.39722 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5e9dd01-7f75-325b-bdf1-4a999cff731f | -9.16831 | -65.40198 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a22c1890-d4c6-3ac4-b5f8-52614032f4c2 | -9.1072 | -65.56192 | 2024-10-16 05:25:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55d3c2f4-4fc5-3f20-9286-a8372b1eb76d | -10.17139 | -64.78552 | 2024-10-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c1d87e8-ae27-3cb0-8467-3390c62d0ea7 | -10.11751 | -65.1504 | 2024-10-16 05:25:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d07ffe2b-cb58-3810-baee-5c8d24537ca3 | -9.92882 | -65.20486 | 2024-10-16 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcfde37d-afc5-3f34-a8cd-7960baa911d2 | -9.92509 | -65.20425 | 2024-10-16 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c1b06bc-875f-329f-93ce-c6f28441c0ad | -9.56757 | -64.62084 | 2024-10-16 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ede6981-61f3-3ccd-ae4b-c969b20919ee | -9.56686 | -64.6251 | 2024-10-16 05:25:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b686f0a0-676c-3518-8b5c-dc1888c4be9b | -11.96007 | -64.84757 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 444f2541-c99e-39b2-a295-09f394b00639 | -11.95294 | -64.84634 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b7dfccf-17d3-3d5b-9640-cc361443cb7c | -11.94937 | -64.84574 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdf6ccda-b222-3a49-84d0-b015beac8824 | -11.9481 | -64.87547 | 2024-10-16 05:25:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README63.md)
