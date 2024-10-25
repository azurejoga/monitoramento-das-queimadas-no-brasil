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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 497beeaa-153b-3e2b-ab92-96e5bd268cd8 | -1.57522 | -53.31374 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd37eb34-1107-33ae-b48f-4960bb27fc61 | -1.57466 | -53.3173 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b6a536c0-c787-3dcf-85f7-bad54b5be0ae | -1.53342 | -51.9196 | 2024-10-25 05:01:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5899076e-58b5-30ca-b225-686bb7c1a1e5 | -1.52988 | -51.91905 | 2024-10-25 05:01:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea9d15f1-07eb-3acb-9354-dc8d1becfb07 | -1.44027 | -52.23497 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d45dfdaa-503c-3e64-ac7e-4b551fcb1873 | -1.43678 | -52.23443 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b36b939-ad29-35e0-9503-5ff6cd3dd213 | -1.43617 | -52.23828 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2cd23fd0-576e-3dea-9ee3-03bff1cfd810 | -1.43496 | -52.24598 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d13e35b-93fd-358a-9b5a-a650d1a4ac1b | -1.43244 | -52.72759 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 89853b5b-7e63-3e6a-85f5-14b5fff29135 | -1.27518 | -52.61312 | 2024-10-25 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0903326e-0d3d-3118-a1a4-4f442f79afda | -1.97289 | -52.07281 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e23c94f7-8ba3-315c-a426-f04c03cde497 | -1.94939 | -52.94154 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0aa7bea-fa89-3567-b546-df17d5615d43 | -1.94656 | -52.93733 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fde8739-008e-3302-931a-de4e48058550 | -1.94598 | -52.94099 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 495d286e-b335-317b-ad4a-8b8bab29fab2 | -1.92589 | -52.51007 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db61137e-3d76-358a-b30a-2d3c1ddce2d4 | -1.89794 | -52.57542 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285a8288-7cfb-3b0b-a995-b0ada1f37d4e | -1.89712 | -53.0085 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 681f4a45-e5eb-32ff-aac1-866599f1c32d | -1.87741 | -52.3182 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1c905f9-5087-3162-b5bb-dc8b5bf669bc | -1.87392 | -52.31766 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89bd6615-9e49-3911-9567-76a1e1540e7a | -1.83845 | -52.16989 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ffa94296-5aa1-3016-9d36-18446de16d40 | -1.83494 | -52.16933 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17cb9acc-2a47-3735-9628-7fba044225a9 | -1.83434 | -52.17323 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3faf740f-4362-39b7-91c5-5cc22add2c43 | -1.8338 | -52.47302 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a0ba2d9-774c-388b-85ae-82c2ce9196ff | -1.10498 | -52.24782 | 2024-10-25 05:01:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad5b5d5-1d65-3385-8faf-e3a91608144c | -3.22473 | -53.36962 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb9b4102-ad73-3d2d-9928-63753daf4ed3 | -3.2219 | -53.36548 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1859bff8-b074-3321-8b74-ca615ab58461 | -3.22133 | -53.36911 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae979c66-678c-3458-8a35-925d811d6b93 | -3.2185 | -53.36497 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cae8fe8b-3465-39e1-a0a7-2b11a67b5bac | -3.21793 | -53.36861 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 526481fc-3db4-3dd7-b3a4-a867ec566e89 | -3.21454 | -53.36812 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e35b922-af91-389f-85e3-5d844dc7045e | -2.62185 | -52.44292 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7a8b49e0-5374-3174-a2db-f0065da627db | -2.62125 | -52.44683 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| bf89b90d-6623-396e-904f-febea307c7aa | -2.62066 | -52.45072 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| fa79b3e3-eda8-3e96-b875-db3b609dfb1f | -2.61835 | -52.44238 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8dcb83cc-9baa-330f-b1dd-a425eb48346d | -2.61776 | -52.44629 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| bbd1607f-e4e0-3a3c-b259-367c555e9bd7 | -2.19127 | -52.80707 | 2024-10-25 05:01:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2028b42-323f-3b0b-91a2-68400db4df8a | -3.07957 | -53.22378 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de6e5000-a587-3061-8c35-a97f84bd965f | -3.079 | -53.22744 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8e57795-5b55-364e-b73d-fca424fcb8d7 | -3.07728 | -53.23852 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bd8db8b-3c11-3c30-9d3a-5102ddf0f56f | -3.07388 | -53.23798 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49ecf64c-00c8-3042-bbba-308389ecc086 | -3.07274 | -53.24534 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0f328792-ba6c-3d60-9cc9-5b7006b39e85 | -3.07048 | -53.23744 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca7304b-8fea-32a2-921d-a7dbbc9086e9 | -3.06253 | -53.24375 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b13706-afc1-30e7-902b-82c4e1cdc365 | -3.00056 | -53.44271 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 871af1cb-c53b-3781-840a-5710f714cd97 | -2.85242 | -53.33198 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6151ef0-2b4c-35cd-8f7c-59d73a4105f6 | -2.84903 | -53.33146 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 318e0e38-0327-3ed8-8159-e03445571e6e | -2.82003 | -53.00025 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3c31b13-e306-377a-a24d-729fe90df68f | -2.73959 | -53.20293 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 68a93b08-e835-3c20-abc2-46428f08897f | -2.73619 | -53.20238 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bf53beea-835c-30eb-8884-a430c2029f24 | -2.73279 | -53.20183 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b1d53f4-31fe-305a-94bc-897d1e710783 | -3.02636 | -52.35069 | 2024-10-25 05:01:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c6003b1-4381-34e6-8a17-745b9c374291 | -2.99512 | -52.36609 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81ac58d4-37e4-3248-93b7-8f36655ea313 | -2.95948 | -52.48086 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86409feb-0e99-3e41-9f63-402ec47f0235 | -2.75491 | -52.04964 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc9d1df9-2a75-3f38-b188-b1edafbf15c2 | -2.75135 | -52.0491 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fac87b02-45f4-3d7f-8967-4ab435d869fa | -2.75072 | -52.05314 | 2024-10-25 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71fd4dfd-4bcb-3cb5-990f-41b6f33958e9 | -3.54495 | -53.02441 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebdb44f7-86f7-3be0-9f64-1bd315ff7dc6 | -3.53979 | -53.01214 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3699d1cf-d4b1-3572-95d3-36d5ce2a878c | -3.53642 | -53.51286 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f67cc7d-7119-3095-a91e-e26920bc8355 | -3.53248 | -53.51598 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20a8f923-d6e9-30ff-81b9-bb801a8cc0f4 | -3.53202 | -53.26602 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b4e5c3a-77af-3fdd-b3ee-26e6fcde7a83 | -3.47584 | -53.44829 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e63aad5-7d6b-310b-9c6c-5075b2a40b46 | -3.46495 | -53.29335 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9381931a-c2da-34fe-9845-121f87f3fa1f | -3.45582 | -52.62059 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c10b5d94-63b9-39af-8d9f-92d5d3a5f5d4 | -3.45232 | -52.62002 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03f5b6aa-f2db-39ec-b9af-db4ccaca077f | -3.45173 | -52.62392 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a472360-a8b2-37ff-84ff-f6b10b5462dc | -3.451 | -52.62029 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37bc1db1-7a31-3f2b-895b-537b26493c2d | -3.22076 | -53.37275 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78c8ee43-8948-3821-bd94-d0a7fabfb8bf | -3.21736 | -53.37225 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2309422b-af8c-34f7-915f-97cc8b56374c | -3.21511 | -53.36447 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 55e9c030-37fb-3f8a-b3e2-7a4e51aa498d | -3.20832 | -53.36345 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9fd4c274-e516-3286-a19b-ce86f563bc92 | -3.16818 | -53.6416 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c01d61b1-bb58-3784-a507-8eee984ef290 | -3.10749 | -53.13402 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f955aae-3170-3c82-bcc9-c03ef497b87d | -3.07786 | -53.23482 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a4b129d-a097-35a9-ad24-7681ae431f7b | -3.07671 | -53.2422 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb2678ec-abc9-3aab-9f7f-904201d7d3dd | -3.07614 | -53.24588 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 021aa490-6bf4-38b2-adab-e42f50e18ad9 | -3.07557 | -53.24956 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2f180f3-6b59-30f6-a7fe-c3e129d5f961 | -3.07331 | -53.24166 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5584161a-5adb-361a-8f81-54dba7997dd3 | -3.07217 | -53.24903 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3a3a551-d31b-3077-8de1-50d40b5894e1 | -3.07105 | -53.23375 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29f28a26-7153-337a-a8ca-32395a393a78 | -3.06991 | -53.24112 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 166b6489-3de6-3676-97e5-c1ea77d60368 | -3.06877 | -53.24849 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f3a2a6e-fc90-3d7f-ab2f-bc04b9b9c938 | -3.06708 | -53.2369 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c8549e-4b34-3c15-b2a0-da7347604d40 | -2.99718 | -53.44221 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92fc92ae-f484-324d-98c9-3ffacedd25bc | -2.99594 | -52.85817 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f829187-cbe4-357b-b098-b0b35f0bf11d | -2.99537 | -52.86191 | 2024-10-25 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf76458a-d47e-36a8-aef2-8f86e6151ead | -2.84338 | -53.32315 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f5ed0c7-88cb-34d9-a287-f4ffbc8879a4 | -2.84282 | -53.32678 | 2024-10-25 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f866ba04-3357-3cd0-883a-e33e3f32681a | -4.16439 | -53.48083 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2797c7f2-f530-3261-8777-459a52d9be60 | -4.16381 | -53.48451 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91675175-29a4-3ad7-863a-db49b4282d8e | -4.16098 | -53.48031 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3913576-41a4-3e32-bb87-8ca4fad76efc | -4.16041 | -53.48399 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 065cb5ac-24d2-3ac2-b8a5-ac0c58cb513c | -4.14391 | -53.5452 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f648650-3e14-3db8-9712-419c6f187714 | -4.119 | -53.83783 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 070bb298-89a9-3964-89c5-71bb375ff8f5 | -3.99361 | -53.43253 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbf9bf34-88a3-370a-9802-cd87ebed62ed | -3.99021 | -53.432 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15cbb49a-87c6-3a5a-ae3e-9e9843260ae5 | -3.98964 | -53.43567 | 2024-10-25 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7ba5d12-8c7d-31cd-a682-1a1b0cd50631 | -3.93781 | -53.47332 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f9bb3384-6a33-380e-b08f-5d592e6347c4 | -3.92809 | -53.66893 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ddc33e0-c0e9-37f9-a0df-9b40036d158e | -3.9242 | -53.51606 | 2024-10-25 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README90.md)
