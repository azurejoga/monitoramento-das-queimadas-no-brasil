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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f4bad21-deaa-3c9e-bb3c-9c0ebb4557b0 | -1.59085 | -53.81147 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 61127672-a134-382c-bb93-c36530e729d3 | -3.29065 | -53.8605 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 83d933d2-62cd-3a25-9ebd-407b9c3a4736 | -0.81219 | -51.78515 | 2024-11-22 05:59:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c44dfda9-ccb7-3c7a-9d36-558aaad044de | -3.19683 | -54.24656 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 81a536b5-a3bf-3cb1-bf99-1e2fa57cd7ff | -1.13478 | -53.39918 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| fba5322b-96fd-3142-9585-d0c61c51a677 | -2.77104 | -54.06377 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 477b205e-8afc-3ac2-a075-b01c29eaf577 | -1.74655 | -52.38731 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7146d998-5759-3fb6-9826-895999a65082 | -2.30524 | -53.59462 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3df2f8bd-2009-3263-98d3-826f9af40450 | -3.17878 | -54.307 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9bcd5a6c-288f-307f-9d28-26293bf2c6cb | -1.44901 | -53.39029 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2654474e-9bdd-34d3-a146-018ca667faf2 | -1.11562 | -53.40553 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| b7b5a221-2bd4-3d4a-ad8e-4182c6dc6a5b | -1.73726 | -52.38596 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b8afe895-8136-3f79-a341-3c5067f0a12d | -3.5209 | -53.8024 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ff1765c9-7cbf-3c55-a350-49572af86fbe | -3.0967 | -53.98415 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 271f16bb-d6d2-30f0-b4c5-2b382b19ebc4 | -1.2598 | -52.06748 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 87cf5398-dd7b-39a3-b821-b09bf72afc63 | -1.64019 | -52.6119 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9369fb1c-ba1c-3c92-a3fc-337777691c86 | -3.10559 | -53.98544 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 19f8f418-eb5d-39b2-918f-10daad893b89 | -2.19539 | -53.6546 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d5c5255e-4d62-3415-ae46-e8cede395549 | -4.1127 | -51.04615 | 2024-11-22 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 152cc3c1-3a59-3061-83bc-9be56db3a88d | -3.3487 | -50.4904 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 17a2cce8-cd33-3a3d-aa77-3f438ca57f47 | -3.25128 | -54.24545 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| a1a12460-7f97-3b3a-b7b6-239b7945839d | -1.59626 | -53.21161 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b2b812b5-4383-328d-806b-2653a7d58a65 | -1.12587 | -53.39787 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 47ecb009-cc04-3564-8faa-a3bad721b44a | -0.05494 | -51.22376 | 2024-11-22 05:59:00 | AQUA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 450d67be-4ef1-3792-b064-370d7c1900c1 | -3.24375 | -54.23533 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 62dd4e9c-0535-303d-be7f-ee3046855556 | -2.55911 | -53.99588 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 52418dd8-67b8-3c6c-94c6-fa83eb059129 | -3.33311 | -53.32658 | 2024-11-22 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 30f9e107-5a59-33d9-a04c-e4d988bbbabf | -3.27682 | -53.83097 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5c75e94c-83f6-3dee-bc43-5a76182850bf | -3.23094 | -54.26051 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 16fc7c4a-3bbe-3fc2-9546-464f813a7220 | -1.61501 | -53.27048 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5751ca25-5f4d-3fcc-a07f-834b8f71461c | -3.85459 | -52.34903 | 2024-11-22 05:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a352f7f8-1f64-3ba5-a8af-0e504887a175 | -3.51114 | -53.80377 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0b5a4220-67a1-37c3-9835-897523eb8305 | -3.50965 | -54.68563 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 302a8c2f-58af-3c30-b9b0-63d961a6bcf2 | -3.58014 | -54.51622 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 05dd79df-a718-38dd-bda6-19409d8d03c2 | -3.10641 | -54.29082 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 54978f24-07f8-317c-9d5d-8748912aaa80 | -1.61686 | -52.57923 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 44bac140-15a6-3a46-8d11-4c2595e154c0 | -3.18631 | -54.31712 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e59f742e-3908-32b1-a874-780d9535438b | -3.10773 | -54.28201 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9715d7d1-a1a6-326d-a622-fcb2539cdb98 | -2.00121 | -54.51324 | 2024-11-22 05:59:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f7a4f638-44d2-37af-865f-27580fd10078 | -3.20437 | -54.25665 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2e13d9e7-2e2a-301c-b019-7729caaa03d1 | -1.1183 | -53.38759 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d7db8831-c474-3d7a-90fe-2dbf0c7e6680 | -2.80558 | -54.01448 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| bae81f19-2979-3981-a6c5-46896b0f5179 | -2.57535 | -54.07705 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df2d8030-1678-3025-85cf-4275f1f94a2c | -0.04363 | -51.23306 | 2024-11-22 05:59:00 | AQUA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f502613e-ed38-35dc-a646-9a8c75d9c259 | -2.59607 | -53.99879 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1b7e914d-56a0-3618-aa8f-935ad56c1fd3 | -2.31401 | -52.48608 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d2b03235-7bc6-312a-8019-55e3790db2a1 | -3.29199 | -53.85154 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 71c74587-820b-38de-9663-3120ad6b602a | -1.25844 | -53.36878 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e430a7e4-ba39-3c7b-be32-aee4f24a9011 | -1.19308 | -51.77025 | 2024-11-22 05:59:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 381385d2-ec64-32ff-a372-74956dc395d2 | -3.8343 | -52.25526 | 2024-11-22 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| efb23082-dd6d-3b17-a8ca-239adadfb1dd | -1.59217 | -53.80262 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 7a12e2a4-9689-3ed0-bc64-1c07d3e1d2dc | -1.84693 | -53.6978 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 031f6534-0f01-37c4-ba2a-ab173160b98c | -2.78838 | -51.71454 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4551c321-3f37-3cf6-8b52-98124d554246 | -2.15767 | -53.78578 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 488b3ee9-84a6-3619-a16f-9660de5819b8 | -3.24111 | -54.25297 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 817d9ae8-8bfb-3dad-bd6c-4d6e12cf328b | -1.20499 | -51.94982 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 3c55fdf4-01d1-309a-ba78-2d85cf6f23ab | -3.33793 | -50.48886 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a31613bb-e28d-330c-a473-689025ae824b | -3.27816 | -53.82196 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 66b17368-1577-3ff3-b762-18fce9517614 | -2.45695 | -53.69328 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 044b851e-f078-397f-92ef-c3b2e76defb9 | 0.46645 | -51.33856 | 2024-11-22 05:59:00 | AQUA_M-M | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fa1aa087-73a4-33b8-8191-30d86cf81a66 | -2.82157 | -54.08919 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3ca28830-d5a6-37fd-8d8d-701d77ec2385 | -2.76217 | -54.06248 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 27411a63-b95e-3f41-99b1-9e303c663117 | -3.84504 | -52.34764 | 2024-11-22 05:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2cd73d24-81f8-3a90-a75e-222a39e5ef05 | -4.13243 | -54.65852 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cd871520-d8c7-324e-be54-3155e0c17952 | -0.97759 | -51.71615 | 2024-11-22 05:59:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5765767d-367b-35f1-902b-2b0175fc69ad | -3.85307 | -52.35949 | 2024-11-22 05:59:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| d2d8724b-d9c9-385b-b0b5-50323c833641 | -2.15635 | -53.79467 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 44bbecee-2e2b-3280-991b-c4de9b1b0821 | -3.21586 | -54.2403 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1efe4b73-8d3e-3679-a267-afe846fd5245 | -1.94081 | -49.51686 | 2024-11-22 05:59:00 | AQUA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| a5500e15-1fd7-312d-9965-65eb9c1463a9 | -1.90966 | -53.34002 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 73e6d517-8ce5-3b9b-bc42-a96f0f3d96dc | -3.15694 | -50.57833 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d595382e-0169-3b9e-99d9-813a7451e6ea | -1.81015 | -52.15341 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| dbcaae1b-8991-3bec-95c2-e78370fde21f | -3.07054 | -53.28951 | 2024-11-22 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fcd79860-b87d-377a-96e0-4ef6ace6cae7 | -1.19401 | -51.95859 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4651537b-8870-3b0c-ba9e-2c4ba07916f9 | -3.23289 | -53.62522 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 80ee66fd-84ab-3460-a35e-02173f0769d6 | -1.71213 | -52.49172 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| df9eeedf-eb8d-3b60-9c41-74d4d0304dc0 | -1.22642 | -51.74323 | 2024-11-22 05:59:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 7d109ba6-3090-386e-8406-3477e72513e5 | -3.27549 | -53.83995 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1ff7163c-a20c-3e05-929e-c7a6474535a9 | -3.34673 | -50.50377 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 17f7fba8-9315-3124-a9af-a8b8cfdad0c9 | -1.1876 | -51.93698 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1c05401f-c0db-3b39-8961-b9f8f8019bd9 | -1.22973 | -51.78606 | 2024-11-22 05:59:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5dfa9e0d-ce5c-3c2c-ab54-b30e9eed9f91 | -2.76349 | -54.05363 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b3583204-3460-389f-93f1-462469b26412 | -3.32094 | -54.09016 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 72c150be-6259-31ea-b8dc-c9beb4446a21 | -3.12346 | -45.06931 | 2024-11-22 05:59:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| b4125185-af22-301c-838c-ee37ffab8a2b | -2.83353 | -54.00946 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9ea896c0-2e78-3597-99f5-03cc42ca5311 | -1.62266 | -52.41238 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b7c14d0b-51d0-39f6-9acb-ac8eca6f9102 | -3.23489 | -54.23404 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4d3207c6-a18e-334a-a484-e761548e6c40 | -2.86052 | -53.9647 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 108d63e5-d5a4-3aef-af05-fadcf6a2f079 | -3.23357 | -54.24287 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 3d2a87a0-e98c-3de3-a5f6-38e4d287dbf0 | -2.50875 | -54.15094 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d6562095-8476-35d5-aa95-21b4ee5066d5 | -3.63865 | -54.31498 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 616e6831-782f-3f13-ab5d-11b5bab79302 | -3.2679 | -53.82966 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 348a1ef1-0a6b-3448-af14-d7d533edf4f4 | -1.63194 | -52.41372 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ada885bc-5240-3aa9-90d5-0c402186e2a3 | -0.80269 | -51.78378 | 2024-11-22 05:59:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c1063b96-ab40-345a-bdf4-b9a37b731227 | -0.34465 | -51.56051 | 2024-11-22 05:59:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0659d9c9-84f8-3599-a691-f207021611a0 | -3.2526 | -54.23662 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c2b280e0-ef87-340e-bbbf-0315a0dcdbd7 | -3.28307 | -53.85024 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 867f77d5-64d9-3906-a012-d2ce71c707c5 | -1.63305 | -52.65954 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 15d18282-8f18-34f7-a65a-f54701f85360 | -3.82313 | -52.26449 | 2024-11-22 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 782fec18-ce5e-3f2f-81fe-85f4a6215870 | -1.301 | -52.22112 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README66.md)
