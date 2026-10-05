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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90958d78-a010-38da-8fc0-8043ac44787e | -3.10237 | -53.72377 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| f3b84a88-06b5-376b-bb01-8a948e2bc9ed | -3.1272 | -53.72302 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c614af85-4235-33ec-a841-eecbf9509039 | -2.15082 | -59.22671 | 2026-10-05 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3f31e4b-43a6-3593-bd58-88339b8716b6 | -1.63732 | -55.53313 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| f1535d82-847b-35db-bc5a-49eb434cea67 | -3.06621 | -54.15837 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 941cc098-f8a1-339a-a421-1bff501dd086 | -3.48795 | -59.72561 | 2026-10-05 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cbf01d22-79a0-3865-9753-63ef7f1e60ca | -3.11377 | -53.73015 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd853377-a1b5-3c25-b484-1475c24e89f9 | -3.10567 | -53.71154 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3f80c416-8285-3f38-9726-a4c6bf4fcb02 | -3.10975 | -53.71566 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ce34e53-15b6-3142-a388-5feb5c27993e | -3.50399 | -54.61925 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b815c25d-33ae-3a96-8e2d-67f4736e7dd6 | -6.22188 | -52.68457 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0c24102-205f-32a6-ae5b-735f1c8e7cf7 | -2.91193 | -54.1214 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da5249f7-1225-30e8-9d64-215a8bbc90c4 | -2.8235 | -54.11871 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6eb80796-ed8a-3beb-aa07-ba7c092cf425 | -6.25981 | -52.83529 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8b343773-9e99-3638-8b6b-e2f3552ca6c3 | -6.2124 | -52.83466 | 2026-10-05 05:42:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76c00d80-ed49-3bf3-abc2-fb471a34c482 | -3.78882 | -59.3782 | 2026-10-05 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2826895a-1fb1-3f84-933c-65c178c93232 | -3.05931 | -54.17302 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 03cdcf98-cf47-3913-9662-7aed7c177657 | -7.32725 | -55.02961 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d22bd75-8527-3e6b-aa2c-cbf3283696fe | -2.94227 | -54.19901 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 827a17e7-6295-3a63-9cfa-082c41149b77 | -2.91047 | -54.09059 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| e48f6eb0-f2e6-3c1c-a7cd-4065a592bae0 | -3.86157 | -55.8261 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7f0c711-2f09-38ff-b973-dd621ad6a468 | -3.05002 | -54.22935 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3986870-515b-3f5e-996f-f6d87544dc32 | -3.01178 | -57.74478 | 2026-10-05 05:42:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3d75f1f-f087-38f2-9810-848a10ba6630 | -2.80527 | -54.12024 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b30ef3b4-d881-39b4-84b2-37660a8dd893 | -1.61527 | -55.13707 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f51ca6c1-06f2-3ffa-9dca-ca84ffec318d | -2.94593 | -54.13501 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d37335ec-8085-3760-a70c-3088100a88c8 | -3.12789 | -53.72902 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3e2e9c1a-b4cd-366f-ab75-ae2919aafa27 | -2.82675 | -54.12936 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b69a18f7-51c2-3019-8d25-70932eb951c0 | -3.10034 | -53.73737 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ca41fac3-8034-3a7a-b146-0a3a2cb9a447 | -3.10438 | -53.72062 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 806053fc-3887-3e6f-9233-b0359bcfb7ff | -1.61936 | -55.10938 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e827f10-c273-3ff8-b68f-59f3873f761d | -1.55269 | -54.79654 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2cbec730-24ba-3ee9-a5f1-30ae1c4c1b5b | -3.3238 | -53.85136 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6903eaf0-3ed5-37f9-a5c3-bdf9cfe3dab5 | -3.37682 | -54.11465 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f1d5a02-97c7-38f1-b42f-9408ac100c67 | -2.94448 | -54.13764 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c06f192e-bb38-3ffc-8d00-69e6543c0a76 | -2.82149 | -54.12423 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc9b269-9132-3a1f-b148-67aa1b8c8330 | -1.61808 | -55.13832 | 2026-10-05 05:42:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf0fb206-502c-3854-97b0-3cb98af632ea | -3.30577 | -53.84851 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bb0612b-f44f-3d96-8950-e503aae9ae1f | -2.15493 | -59.22732 | 2026-10-05 05:42:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5ca3307-4e41-31a1-bff3-3e6f33f9c76f | -3.46737 | -54.58883 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| f8f384af-c651-36ac-ae38-0b0e45a4fb76 | -1.52035 | -54.82142 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85a906e7-dace-31d4-b7df-2721bd7ab254 | -3.3774 | -54.09771 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bcf9a14-db15-3fb3-abad-06c627046cfc | -2.8281 | -54.12802 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58c035ac-0be5-3a6a-82a6-bd2d5e2e0285 | -1.21152 | -55.86229 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a04c7b79-df9e-3419-86fa-b24883b54744 | -3.57666 | -54.65421 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f69a93ce-d670-3ccf-af2b-292f9b000a8d | -3.11731 | -53.75982 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| bbf504a6-0aaf-3994-a60c-1cc4b2677307 | -2.9457 | -54.12913 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0db36b41-22c0-3a0e-944b-9df37d85fc78 | -3.18437 | -54.08079 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c773ee90-0454-3131-a6e3-82c62fe5d429 | -7.22251 | -55.19617 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3039bdfe-e193-33f4-ad96-e4c336291ec9 | -1.55232 | -54.79671 | 2026-10-05 05:42:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29311782-3c8c-3a05-b636-bb23d81b33ab | -3.07023 | -54.17209 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 99e338c2-38d0-30c3-9852-6e3cf954bbde | -3.04583 | -54.22263 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 449f1db4-03bf-3fda-b96e-e00bafbe2489 | -3.46679 | -54.59284 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| f1063b38-30ef-3013-86c7-05c015c89926 | -2.90583 | -54.08121 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| affd7ec2-dcbf-387a-84fc-16ba60e9caf3 | -3.19371 | -54.09988 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f40d8d9b-767d-308d-8d6f-aa71b41e6336 | -3.04773 | -54.21001 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d0376ffd-2b68-3f27-8081-6c54526b4dca | -3.12788 | -53.71848 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d43b7037-65f1-390d-a4be-d8976dfbdbaf | -2.44655 | -56.3794 | 2026-10-05 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c5ba1c2f-fc0d-3ad4-933f-9f4a28053c20 | -7.22137 | -55.20478 | 2026-10-05 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95f1ca14-3503-38b3-8c72-3105841add4b | -2.59455 | -51.85555 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25f6ad46-c3e0-329d-a992-2a3537f3981b | -3.30641 | -53.84401 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc0ba1d7-8483-3c28-bfc6-ea25719df3ba | -3.00668 | -53.87343 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f4dc662-85bd-340b-943b-4842d1e27167 | -3.10773 | -53.72923 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 14e277e6-083e-394b-b74c-cbd741196448 | -2.80464 | -54.12444 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b351f132-d71d-3a93-bfae-90b1a2c7c841 | -2.78894 | -54.10893 | 2026-10-05 05:42:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e556e2cc-a839-3157-abe4-3e5ede9cbf85 | -3.12249 | -53.72355 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7b08e2e-6c3b-3412-a94c-54a5e49dba8d | -2.95037 | -54.13845 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7a846bfa-4757-310b-b69d-52943beda439 | -2.94509 | -54.13338 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c895aec-7a95-36c5-8767-26ce4fb736b0 | -3.10632 | -53.70692 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d5c65602-0de1-316d-9157-77db880fc3ec | -3.31553 | -53.85133 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 548f2a9f-6564-3432-9236-2ee97d0bf6ff | -3.0656 | -54.16263 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2b7e0bed-2649-3275-a557-6ce385e765a6 | -3.12515 | -53.73659 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e49c1728-9506-32e8-9c4e-68664f52686e | -3.51031 | -54.61619 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f3ec8a5-4a61-33eb-ac18-8051f8e0f270 | -2.96093 | -54.14847 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d979f08-dd7f-3f3a-bf6b-cad0448953dd | -1.20124 | -55.86128 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20226ae5-5808-3863-8b29-8ca25e13a474 | -3.1212 | -53.73264 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d64d435f-1596-3a01-b1ee-4f9df9345435 | -3.88641 | -55.80552 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eea2554c-5006-39d5-85c9-3210ada94b63 | -3.513 | -54.60769 | 2026-10-05 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d805294-fe66-3e4a-97b3-020c8c475c2e | -3.06962 | -54.17638 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef67e686-d5c3-3638-b40e-ea0ab3abe4f6 | -3.04599 | -54.21578 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38a2128e-81db-33b0-ba47-25e2fd7bebd9 | -3.78711 | -59.37803 | 2026-10-05 05:42:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2e80559-eef0-3ddd-9f58-59940f3564f5 | -3.10719 | -53.74431 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d38fc44a-a1f0-3bc1-b210-67b121f4fa36 | -3.11309 | -53.7347 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04f73d36-945a-38e6-a9fd-2ef9bae5a00f | -2.57928 | -51.86586 | 2026-10-05 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9e98b9d-4d13-39bc-8640-7bed46ec2148 | -3.04418 | -54.22841 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79baac44-0b76-3eae-8fa7-72f73757cb6c | -3.93172 | -55.85682 | 2026-10-05 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee609022-8a89-3581-b181-58e292b6a675 | -3.87944 | -55.80399 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7973db95-13cd-3f9e-af24-eed939a1a2e2 | -3.29913 | -53.85202 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaa46daf-c911-3014-8ab6-19df81e68b51 | -1.74587 | -55.2407 | 2026-10-05 05:42:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71ecc587-e52f-3ac1-9059-2b9231de4d66 | -3.30819 | -53.85933 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 253ee9d3-90a1-3041-aca3-fa44b9236792 | -3.87848 | -55.8108 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc491e95-1076-3f47-97c5-c0c117ba2f9a | -2.85297 | -51.29662 | 2026-10-05 05:42:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b22c55d-bd23-362c-8f13-c97ca9835e10 | -3.31715 | -53.8549 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8adaff5c-9dc2-3f34-a237-155bf89e8a77 | -3.29976 | -53.84753 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 001ba5bd-d7c8-3063-9bfb-6927c282340d | -3.099 | -53.74633 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23c26f17-1430-338b-82d1-56baf7d52edd | -3.31178 | -53.84946 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb841775-2ebb-36c4-b43b-f41f30e7d22f | -3.84215 | -55.84724 | 2026-10-05 05:42:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ee47131-a4e0-3f7c-ba40-233c334f2e8f | -2.48333 | -56.09776 | 2026-10-05 05:42:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4732d465-ea71-374c-97d2-19ac945390af | -3.06498 | -54.16693 | 2026-10-05 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 595c538e-1a95-3123-8f3e-8c4245ce5571 | -3.12116 | -53.72209 | 2026-10-05 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README51.md)
