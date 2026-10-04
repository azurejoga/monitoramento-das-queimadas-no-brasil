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
| 4a836e3f-fa6a-3458-b250-357a4470a24b | -3.77204 | -51.85679 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 106b60c8-0fdd-3f7d-921a-c5dc1c3b5205 | -5.22824 | -48.40884 | 2026-10-04 04:19:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6624c67-e5dd-3016-aff1-6035ed3ac8fb | -2.80277 | -54.10324 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c2cf3064-535a-3b13-8a01-c6cf8d87951a | -5.96078 | -41.30989 | 2026-10-04 04:19:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0a94528-1aa2-3428-b222-5f718b7fa299 | -3.35685 | -43.3828 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b84926a6-e74d-3e4f-8621-c55c4e26ab08 | -3.89652 | -49.69278 | 2026-10-04 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1bdac0b0-2a68-3a3e-9838-7fa633ca8996 | -2.56073 | -54.72369 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ca47fc2-f233-33fc-812f-63f437390d68 | -2.97156 | -54.1039 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9a0b4558-5a97-34e7-af56-34087e2ecc45 | -2.97368 | -54.10487 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd2418f6-0669-337e-8c3f-345268a177ab | -4.8193 | -49.28339 | 2026-10-04 04:19:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f98c59a8-a740-36c1-a04d-879677f553fb | -4.16904 | -44.2867 | 2026-10-04 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a99c16e4-528e-387c-a14e-299875a8f4ed | -1.40964 | -49.26548 | 2026-10-04 04:19:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c4b833c5-f563-3c80-baa7-4593ad64ebab | -2.21783 | -53.70479 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 754af3ad-15c0-393f-82b8-83bfa4e5946b | -2.23954 | -51.91632 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b843b6f7-3a8a-38fb-8284-ffed27d03886 | -3.11541 | -53.7246 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 9ee28933-3548-349c-9db7-3f3d9e144ef8 | -4.27563 | -50.27243 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebabe48c-2749-3647-b7e4-0fbf04263d8d | -3.07483 | -51.27976 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c0e2299e-fc89-3c0b-9c59-b7178b4b6864 | -0.49268 | -49.10592 | 2026-10-04 04:19:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e902d7-2e11-36bf-9880-304491ea1e27 | -3.29494 | -49.12626 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4ddc4240-ee64-3d0e-8563-4d374f403881 | -2.89959 | -54.13223 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7dddb973-4b78-3298-94f5-dbaac0788e43 | -3.08677 | -49.53097 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afb47c48-2ad9-3f7d-95ef-dd9dfa836fe0 | -2.25332 | -51.93728 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9a031dec-1126-3280-bc70-cbecc8a3640b | -3.18393 | -54.09915 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 811534f0-6c50-3927-ad2f-8ee099f1477d | -2.47674 | -50.87634 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 97457472-9968-3962-a9c1-bbc8793dcf26 | -6.0763 | -53.47334 | 2026-10-04 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27b61682-044d-3f07-adac-48cdd96d3ee1 | -4.27497 | -50.27639 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6253ea4-4d43-3a3d-9e43-cdf16328ae49 | -3.46956 | -50.10631 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d2882da5-ded9-3c48-b7ab-264567e61af2 | -3.51164 | -54.60897 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 32cff3a2-7fcd-36c5-acee-64d43bd30c26 | -1.62062 | -55.01981 | 2026-10-04 04:19:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b30bea93-1f0a-3427-954f-94df51748d30 | -4.13089 | -54.15936 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de8321f4-e0ad-3e59-8db0-9a906c785a0d | -5.8605 | -55.70343 | 2026-10-04 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aba950e8-636c-3879-90f3-d03034963746 | -2.81457 | -54.13693 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f8486db-edfb-3dc4-9dc5-7fcc95c65297 | -3.07676 | -49.54866 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe1d995c-85aa-37b0-aa3f-daeb9e308afa | -3.11912 | -53.73621 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c6c7ded0-a6d6-32ac-a5af-725e683f7eb6 | -5.74381 | -43.27319 | 2026-10-04 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 469c1acf-e1da-3cec-921d-4f1df0516f83 | -3.07911 | -49.53378 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acc3d098-c363-33fe-8ba5-12f671af84a2 | -2.97287 | -54.09625 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e41f685e-84b2-3ef6-b2c6-9053e54723c8 | -4.27171 | -50.27269 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fab12d80-0cdb-3c32-b9c6-b905ec1dc268 | -2.81522 | -54.13301 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a6ca78cb-0d40-3046-b0fa-48072108b36a | -3.35021 | -43.38178 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67879333-4e6d-3a5f-9fb8-655e6e931171 | -3.47087 | -50.09831 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8ed6d279-e045-32b3-8bcf-c9512c9cc8d8 | -4.48575 | -45.54109 | 2026-10-04 04:19:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f3a6c61-a86f-315a-ba87-05f76cd70268 | -3.08372 | -49.54943 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43925e33-cea8-302a-9979-c00665fe3e5d | -4.93184 | -45.69094 | 2026-10-04 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae7f3b0d-c170-3efe-939e-a37e308b0a81 | -4.26483 | -50.74006 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4404d9eb-9eed-3d17-83e1-86194835da52 | -4.46163 | -50.97427 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| adef1184-4e0c-3982-8af7-0a90db95270f | -3.12756 | -53.71918 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d0da49d9-aad1-3f1d-9edb-5610b401133a | -3.47512 | -50.09901 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 69352e4f-520b-36cb-95d6-3bbf6cd26dee | -2.44737 | -50.25114 | 2026-10-04 04:19:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| afc8561a-2362-3e25-b896-65bf0c60939c | -2.69461 | -49.03707 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 16fedc80-59e3-3a59-8034-bb614005028b | -3.08089 | -49.54931 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4129feae-1787-3a4b-a704-4468684b9cca | -3.08793 | -49.53147 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 424d3c10-e0ac-330b-8c0d-74cc34417a0d | -5.73873 | -45.14742 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d34ffef9-41c3-301d-a6cd-055c0c1579a3 | -3.26942 | -43.37646 | 2026-10-04 04:19:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac834204-d96b-33b0-b280-dfe87722de69 | -3.80886 | -50.85009 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3206a6b1-4f69-34ff-80c4-e55f5869eed6 | -5.55416 | -45.26319 | 2026-10-04 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 70b55ea0-d39f-3e49-b709-baec26ffba99 | -2.8002 | -54.11861 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 58cf5df6-5e62-32ee-b495-927124cb9a68 | -4.4602 | -50.98308 | 2026-10-04 04:19:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d109154f-511b-3571-9137-fdeb8e223736 | -3.12579 | -53.72993 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4f147219-ce1c-38bb-8b0c-d60191dadbf2 | -4.39189 | -45.98941 | 2026-10-04 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf52df88-f9c9-30ab-a0f2-1a8726b7b385 | -4.26421 | -46.37774 | 2026-10-04 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 45bc58a2-7c61-3d09-9bdb-6b2ab55a0ae6 | -2.81716 | -54.12136 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a45e3905-cc1e-3743-b81a-1887a4c3dbea | -4.44264 | -43.42206 | 2026-10-04 04:19:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43f1e255-558b-3d48-a93a-334d6e6184f9 | -4.36141 | -47.77693 | 2026-10-04 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac4266ae-e0a2-3543-9b2a-b94a821ab0f8 | -3.08204 | -49.53398 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e0eccb3-2f1f-3511-94b8-f9fc1da13e34 | -3.57561 | -54.6561 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 074091fc-5e7d-3eda-932b-33b8d2ddbaa2 | -3.12461 | -53.73711 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d00882bf-aac6-3465-93ec-6fd156510761 | -2.5755 | -51.87339 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0ce77bfb-8552-3227-91c9-e18659cf3dd6 | -3.0421 | -54.20195 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1730c29e-93b4-3de8-8105-047f396f1f9f | -3.5174 | -54.61002 | 2026-10-04 04:19:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7fee8c71-6617-3352-9bc5-95e0a2d640f9 | -3.28056 | -53.82328 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5971f785-69a4-327b-b0d2-e3df1ecabf11 | -3.04265 | -54.2338 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 910fbfea-6d47-3cd7-b580-043e77c74771 | -2.58628 | -51.85637 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| f1b5f08e-64e9-3dda-bd9f-f23990954dc0 | -2.88441 | -54.13609 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1470c60e-3027-3681-846e-9abbfb1ef6bd | -3.05979 | -54.16521 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c8fb9db2-ca95-3ff8-b490-37ab15412eac | -4.15014 | -49.69681 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db41a004-b0b9-3e24-9615-f80debcfc683 | -4.29101 | -50.25869 | 2026-10-04 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| aa3b3621-3272-39a4-9fca-01f4bd812843 | -2.96993 | -54.09246 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e502b722-f827-3a1b-8c77-16a3fb7909f5 | -3.13675 | -53.73176 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0766e806-9cc7-3d60-841c-ff221eed61ea | -3.06969 | -49.53991 | 2026-10-04 04:19:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4f8a52a6-e788-3f10-b0b3-0ffeb866cf06 | -3.28983 | -53.83541 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02f567c4-05ac-34b1-925a-1aef156e7964 | -3.90003 | -49.69718 | 2026-10-04 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10eb8862-53b5-30b9-a6b0-fca89ac63949 | -3.5689 | -51.98394 | 2026-10-04 04:19:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b1aa0c2-1afb-3167-91e0-41b6042f92c3 | -3.0118 | -50.47381 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 542cda1a-6b7b-3e16-87f8-a9376add78bf | -2.97618 | -54.08961 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f428f748-0cd7-3039-a469-15e09eab13e4 | -3.10814 | -53.73446 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ed67cd86-4eca-3c11-90f0-12c06920aa82 | -5.56164 | -49.88276 | 2026-10-04 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15e33b62-6756-3ad9-b904-f4620956ec59 | -4.8381 | -46.08556 | 2026-10-04 04:19:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5697344e-1348-3209-88cd-27b9e7900253 | -3.13734 | -53.72816 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f7ac5771-fd65-3eb2-b73b-4c1441073509 | -3.8126 | -50.85521 | 2026-10-04 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec49cfe8-3eca-365c-bc34-6e31ec428b4b | -2.97483 | -54.08485 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 68fff505-d3ca-3f63-8da1-4df86a1b687e | -3.20272 | -50.748 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9839feb-e323-39a9-837e-f12857b8c4bc | -2.97001 | -53.26711 | 2026-10-04 04:19:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea0a281a-fe96-3930-8151-38e26f339468 | -2.97056 | -54.08865 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8f8ae12d-712d-3174-a9f2-d4cefef2950d | -3.04394 | -54.22602 | 2026-10-04 04:19:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e1362624-fb1e-34fd-98f8-8ff51cfb4116 | -2.82101 | -54.09822 | 2026-10-04 04:19:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2cfb4b7-b535-320b-ae50-55d234007f39 | -3.01374 | -53.89101 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3d622d2-9c3e-3ab1-af8a-fe8c4215fd1b | -2.58719 | -51.85097 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| bd62e903-ea09-351a-9d26-6e3de11213d1 | -2.59781 | -51.84726 | 2026-10-04 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 80bf6021-0400-38a0-9ef5-ae9854d6200f | -3.01436 | -53.88736 | 2026-10-04 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README24.md)
