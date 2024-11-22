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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9918855c-6902-337a-b223-524ba95fbd86 | -1.79642 | -53.63778 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 19e35f78-2087-3b91-827b-8579435f3e55 | -1.74884 | -52.3913 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af5de643-68d4-3d73-8ffb-12bd384566a7 | -1.2006 | -51.95992 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ceea5b98-2265-38a3-9541-b3f6ef5e91b6 | -1.77839 | -53.60159 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b09888d9-af79-3b9c-89bc-c109c5dfd16e | -1.63247 | -52.41335 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bc61d8b-f666-398f-96f8-0c3babed4710 | -1.46016 | -52.66385 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5914e1c3-78cd-3499-b12c-3af3f0a97f5f | -2.49898 | -48.99601 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6706a946-d97a-30c4-b2bb-38044a7b0d57 | -2.00405 | -54.51866 | 2024-11-22 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ed10ab2-50c6-3ac1-a34c-c9fa2a0e0755 | -1.74308 | -52.3937 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 378643ef-a38c-3357-9da1-0bbc2cca8756 | -1.15185 | -53.65708 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c10b368d-ad3b-39e0-b73d-674d1a8df753 | -1.8142 | -52.16528 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 3880e1d0-2bd0-3796-980b-49bb62087f8a | -2.2255 | -53.72544 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f071b643-8118-3142-846f-bb4a9832568c | -1.71317 | -52.4842 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e6896b1-7d37-3c17-b0a9-bc1ab57dd51d | -1.19729 | -53.67989 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 210a64a4-6cc7-3aa1-9445-0218e557c338 | -1.44192 | -53.39216 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cff07bb8-3f2e-3ab9-b614-a65335bbb639 | -1.36727 | -55.70034 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab295891-e260-37c6-962a-66143b6a0b41 | -0.26911 | -51.57035 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3cb6bb73-8b09-3750-922b-c792149aba16 | -0.8141 | -53.06032 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16606f81-ecc7-38fa-ae44-8d4b0f8381b9 | -1.58997 | -53.80706 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 259eabd1-cf38-35ac-97b2-bd410d86fd9a | -2.3553 | -48.55529 | 2024-11-22 05:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8c057b1-27d4-3881-94e2-2273311c39c2 | -1.33369 | -52.43139 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1629a21-4623-3a39-81ae-3960800c02a9 | -1.8152 | -52.15852 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 274dd70e-fbd3-3af9-9f62-5302e75bbb84 | -1.79766 | -53.6372 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73facd2e-f651-3447-a7e4-bb7578bccc5b | -1.39587 | -52.34271 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f6b1362-5dc3-3508-9f55-55e889b9b9a6 | -2.31385 | -52.49225 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b94d5ea9-bd41-3573-ab86-2ea1744936fd | -0.26318 | -51.53725 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61ff02e7-65fc-3122-9dd0-b8dde24938d8 | -1.65835 | -52.67105 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9c4cb73-50b2-303c-98ae-b54848fbf204 | -1.19869 | -54.03449 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cf6c56d-7e96-39cc-bb0c-db74d4e97f60 | -1.74785 | -52.39774 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c8090a82-32e9-30b7-b8e7-d5c20683dd48 | -1.98817 | -53.1364 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3f40cb3-df67-3381-bbd3-ea2f07e9f157 | -2.23461 | -53.66669 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e70c7ac-04f6-3186-ba9b-64e01b2db516 | -1.91544 | -53.34453 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 64025de5-0657-3082-8efd-ca05b5331dcb | -1.24354 | -51.74723 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a934a60-7256-3c38-9f0e-3b80f4a65e51 | -0.93119 | -51.72099 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d933d33-a160-3eef-a7ca-5e1e2529533a | -1.09612 | -53.16307 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 701905ae-d8b7-307e-aa43-2c27638b6c35 | -1.21096 | -53.68628 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 39fa1828-6f2c-3a9b-9cd5-e2bece8433d0 | -1.21628 | -51.74289 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2850cfe2-5da1-37c0-887f-4c1d8918d442 | -1.96441 | -52.98923 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2473e086-d0ad-38fe-ba99-63d5d01f07e6 | -1.09747 | -53.16483 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2ecf2924-099b-3478-aaf2-d7abf620c1ea | -1.64326 | -52.63066 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac59097-4102-3525-8c37-9e24cc487659 | -1.61663 | -52.58566 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f466df0b-5957-3033-badd-1d0a92b28399 | -1.27044 | -54.21309 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5af60752-eb8a-3d26-8e25-f79a17d2460f | -0.81284 | -51.79239 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea51490f-27e7-328c-ba88-9524617762b1 | -0.80848 | -51.78461 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f3501cc1-d628-3b5c-b588-01f12e5c3d88 | -0.14301 | -60.86692 | 2024-11-22 05:31:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc83e610-8028-3bc7-a2c7-9b0e42d9435a | -1.20162 | -51.95311 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3ebb49e0-12e0-3c45-82ed-0e4f286f3655 | -0.26807 | -51.54169 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26380b3b-ea83-38cf-bb75-473058c002fa | -1.61844 | -52.60823 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1f13a11d-7c56-38dd-a799-d34c0b70cd0a | -1.27806 | -52.98281 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cac4ac34-1deb-37b4-9687-0580ec3f0624 | -1.87701 | -54.36444 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d786c47-eb7a-3e7d-b6ab-a3ea872d42fc | -1.71791 | -52.48821 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d12e9759-51e1-388d-b807-0408c9d19f4e | -1.57896 | -52.93024 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ada71088-e6d6-32e2-ad2d-c23c13c7644e | -1.79158 | -53.63703 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 81d0f6aa-2e5b-345c-86e9-b20e4163e999 | -0.92245 | -52.6936 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 175e44e9-ce70-31cc-b244-ad1764662c6d | -1.21021 | -53.6912 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2352c35-4961-390d-a70c-090b5bb46393 | -1.65366 | -52.66714 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| be2f587c-0a8f-360b-bdab-8599e0c44215 | -1.58918 | -53.81226 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| daa3f5f1-9453-3744-aeaf-89485afa312f | -1.13118 | -53.4076 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d35b3606-a329-3c84-83fd-95da15c06d40 | -1.15507 | -53.66821 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8293ec12-6b11-385b-baff-878105c6df77 | -1.50655 | -53.13315 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d5077e9-68bb-3e4a-9f41-5b7088dc8885 | -0.93607 | -47.55696 | 2024-11-22 05:31:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 60b3b701-3efe-3e29-b7ea-c680aa3bedaf | -1.44763 | -53.3875 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d8a4199-f70f-36c7-b8c8-b640547149bb | -1.62181 | -52.58646 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8241bc70-ce6d-34e7-a138-b06245f442bf | -1.91973 | -52.08484 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c50a104-af83-333d-801c-e3db90610d0f | -1.65276 | -53.77945 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e5372cb-4c26-39d4-85bb-f461c1e020d1 | -1.74358 | -52.39048 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2fa54b79-9609-3afc-9bdc-0cca6d59b1c9 | -6.22018 | -55.64615 | 2024-11-22 05:31:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a802f220-0285-3335-b44a-efc2f0152a13 | -1.73298 | -52.71416 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e243e056-0984-3630-80bb-82eed8058651 | -1.7236 | -52.70638 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fde74d0e-359c-3d7c-b78c-50ce49f5a22c | -1.71269 | -52.48738 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1da43905-7679-300f-a5da-5d856b4896a1 | -1.14251 | -53.39867 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1710a913-e247-3653-b071-affcb05e8973 | -1.21031 | -51.74552 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8a0a815d-6eea-3a57-ac94-01f43c30fd05 | -0.81231 | -51.79583 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce8d1300-fba9-3b02-b5c7-0062df68d521 | -1.63947 | -52.62054 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f6cc4d7-75f7-32f4-910d-71b3ebf5d9f1 | -1.1946 | -54.02997 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 548d0e50-3990-3f8b-998a-74a3d196b885 | -1.19972 | -51.77021 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e39b03c-f13e-3466-a9b4-cadc63388820 | -1.41257 | -54.51275 | 2024-11-22 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f8fa866-b330-3831-b164-a5f32d935e9e | -1.12311 | -53.39527 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98e7d12e-8150-3843-aaa4-5ed3d0d91d7f | -1.96111 | -48.38886 | 2024-11-22 05:31:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82e0078b-8ff8-3e94-aa3e-232077f8fe33 | -1.7674 | -55.32064 | 2024-11-22 05:31:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f1b4f3e-4829-3149-8b21-d1eba268c8b5 | -1.19726 | -51.94543 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ae76a463-4c5e-37bd-ab4c-53da368e7633 | -0.271 | -51.56909 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b21c2e1-d32e-342f-a866-fd726362b595 | -1.64086 | -52.61123 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ab65618-6885-3a9b-8535-96b44876867d | -1.94677 | -49.52641 | 2024-11-22 05:31:00 | NOAA-21 | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| aeb1374d-6199-344a-a367-884c20817d9f | -0.8921 | -51.72188 | 2024-11-22 05:31:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b499ce4-46ef-37c7-9516-3fb3bfeeb6c1 | -1.21033 | -51.96842 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29a52c75-07b2-3659-b045-4db01bd1fe9d | -2.19659 | -53.65529 | 2024-11-22 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f92f4b1c-9863-3fef-b0de-fca971936cb8 | -1.39013 | -52.34509 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| afe242a6-4320-3bc5-8e93-4b57fa6eb123 | -1.09522 | -53.1689 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8f5360f-a6cf-3a18-9c86-d3ac14a8b78b | -1.81469 | -52.16193 | 2024-11-22 05:31:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 45461976-c4c1-389c-b4dc-6949bed14250 | -1.67637 | -54.99373 | 2024-11-22 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13f2fc27-0243-32fb-9f7f-340f4d67f4f1 | -0.14631 | -60.86743 | 2024-11-22 05:31:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a26426be-3233-32ab-86e3-fe5fc36fea78 | -0.80901 | -51.78115 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 59986307-194a-3f96-a4b4-4254b2132da0 | -1.18807 | -51.95183 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d831a692-fd4f-3a00-8d93-b08383ca7432 | -1.23263 | -51.74552 | 2024-11-22 05:31:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1211aca3-8350-3f8a-9909-25e36c56cfee | -1.19397 | -51.94926 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9c7bafe0-9196-3542-b08a-a92cd81b2995 | -0.8675 | -51.88724 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4968175f-f7cb-3c0b-96f4-10de3037bbaf | -1.20213 | -51.9497 | 2024-11-22 05:31:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8b645f0e-2112-3663-9946-64637335de25 | -0.80691 | -51.79498 | 2024-11-22 05:31:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7b6cb55-3529-3578-bba2-97e42c5aef57 | -2.49697 | -48.99504 | 2024-11-22 05:31:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README62.md)
