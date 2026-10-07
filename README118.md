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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ca3d6ea-87ce-3ed9-b354-a0f1bec6646f | -2.15644 | -59.22903 | 2026-10-07 05:59:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e7a3101-ec54-327b-b88f-e4522d4d8d96 | -3.53947 | -54.65519 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| af6aa2a9-6775-38d8-ac90-07d69a4c5b39 | -3.66381 | -60.62526 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d582a9e-f359-3a3b-ae42-08b71ec04080 | -2.78815 | -57.66136 | 2026-10-07 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e039c4df-89ce-3672-8891-e0b9fc338739 | -4.159 | -55.1537 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e0efbdd9-5e55-3f4f-ae12-f56ed81ffe3a | 0.45029 | -60.53659 | 2026-10-07 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a07b8bf3-1bed-3730-a8f6-b3414b8c87c1 | -3.1008 | -54.15831 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1bc8877b-7187-3319-8889-ef7bc379e34a | -2.48833 | -58.07051 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 245cf336-bccb-3b14-9f68-8c55f06ebf94 | -3.05571 | -54.21673 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2d4d9909-217f-3b53-9123-0d6f4dd43f88 | -3.23952 | -56.8064 | 2026-10-07 05:59:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d72c7e75-02f1-3676-a201-5089a443b961 | -3.55893 | -54.48375 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58ec3423-a12c-3c33-b0d3-b50d6ad98eab | -3.99523 | -56.25299 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa5bd282-5b11-3487-9907-671893799643 | -1.28981 | -54.55803 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 79f7fbca-525c-3ea1-bbdb-7b9a85dee935 | -3.43943 | -56.94009 | 2026-10-07 05:59:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 13982b00-6dab-3b48-8963-d7f59eace1fb | -2.77615 | -54.08841 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 83550103-8433-3595-baa2-bfebb8c43aa5 | -3.51912 | -58.75891 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6985b953-6b71-38b6-a0e9-aa7a001b5a15 | -3.77831 | -58.52754 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69035420-2144-39b2-aab2-a5ac1ee6a0d7 | -3.07961 | -54.28122 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0af2dee5-514c-3c59-8ba9-99fc5a8a0ec5 | -3.99449 | -56.2581 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 620356a6-cdd9-370c-a27c-58eb8cf40751 | 0.44277 | -60.53524 | 2026-10-07 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9956ce40-ddf3-399b-a2c3-004311ff10d8 | -2.52433 | -58.09466 | 2026-10-07 05:59:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ef3d6dd-647d-3709-a736-6f7fc4dbe823 | -3.58907 | -54.57076 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8bf15148-336b-3ea5-a263-4197ac256b36 | -3.06179 | -54.22471 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ea397dbf-69c3-374a-b338-a5d8914b8902 | -3.56502 | -54.49125 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5d2b69f-8319-3a5f-8a1a-c88f2ee82c63 | -3.51933 | -54.65606 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7efa320d-f670-327f-b061-33ee5405a3ea | -3.67428 | -55.95024 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b74ea146-e6f6-3a21-a2f6-6b6fe981571d | 1.03494 | -59.45575 | 2026-10-07 05:59:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 930590b0-bd4d-350c-a665-0487cc52bf0f | -3.54029 | -54.65871 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7b91cc0-5a6d-3c5a-b601-783c854904a8 | -2.79266 | -57.67013 | 2026-10-07 05:59:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28723588-d63d-39fa-bcf3-15f625d662f1 | -3.68044 | -55.94859 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efe3a8b2-0b8c-35e2-853e-225ac165e4a3 | -3.76742 | -59.40167 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b88bf9a7-f118-3be3-8745-667598e917b6 | -3.59005 | -54.56417 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92efd70d-004e-3ffd-9fae-ff4b814b6a3c | -3.53525 | -54.64458 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2a32d7d7-b3fd-3a1f-aa45-b063e87eb70e | -3.0039 | -54.12348 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 864356f1-149d-37bd-b1e0-29082c788a7f | -2.15689 | -59.22605 | 2026-10-07 05:59:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46513e3b-3112-3628-9236-beafc486cf9f | -2.93743 | -54.15673 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 021905b3-4fdf-31dd-8184-9bc6db078d6c | -3.10567 | -54.17432 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7c3e32d8-575b-36cf-bb72-701714bdbc82 | -3.38647 | -58.2039 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f49c808-dbe2-36de-8f7c-03c50f5dbf3e | -2.85572 | -59.11034 | 2026-10-07 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4175539-7607-312a-96c3-21e18b5785be | -3.09983 | -54.29139 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9523d368-7b82-3c23-b564-0576d1c11a51 | -3.65685 | -60.63201 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cfde18e-2234-3683-963e-6bad427cc489 | -4.1531 | -55.14619 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3dcd8d17-7d1b-350c-b1de-7ecfb1fc837c | -3.34965 | -59.49866 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f1b2787c-1156-3f32-92bb-1f4486be8220 | -3.68646 | -55.95745 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff45c912-3223-368e-b778-106ffd1a93bd | -3.59462 | -54.56848 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9afb7fff-303d-3676-9fbb-82e3a5ff8e17 | -3.48359 | -59.46303 | 2026-10-07 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eeb2882-dcf1-390d-a1d9-62b71fe0c5ef | -3.08161 | -54.26735 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c5788b79-27b5-3c3c-9a0e-5bfca81eea93 | -3.79067 | -58.29496 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82fc50b8-869c-320c-bd30-58ca611acc84 | -3.73948 | -59.44798 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13202017-bfc3-359d-8546-6e1c004ea831 | -4.38334 | -59.90686 | 2026-10-07 05:59:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f51073b-99bd-3384-baae-c20a69cf1512 | -3.5292 | -54.63729 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fce55b5-96ad-3290-872d-857c09a54cdd | -3.60158 | -54.56981 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1042dd2e-ce4f-3f36-9af1-e37c01e93552 | -3.00567 | -54.13848 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 134d0fb4-9883-328f-b259-9fd3480a81a4 | -3.54373 | -59.49762 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e345e82-8c7d-34ee-ba17-e37a33d171c5 | -3.08605 | -54.25636 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9afc997-fe8e-3e55-90c8-e387e5f844b7 | -3.0966 | -54.16294 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51ce35e1-8566-34ef-a8dd-3373802c481a | -3.77282 | -58.52674 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68350e68-87e6-3d87-b427-4d6ead0717c1 | -3.07594 | -54.27544 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb158fa7-4d11-39fa-b67f-1cf64adec79c | -2.01479 | -56.89265 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed954bf2-f2c1-36c5-b29a-e7675ac42f34 | -3.53861 | -59.49685 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 553a2ff1-c38e-387d-aa39-6de36a2b7828 | -3.04362 | -54.1509 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6b9ad43-87ed-3762-b927-856bb4308c00 | -3.50357 | -54.66653 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6c5ce178-8069-31dc-b0d2-dc7d860e5fa2 | -3.99128 | -56.26632 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| caad8cdb-a81f-39f3-bfa6-9fa93b07cf5e | -2.7768 | -54.11016 | 2026-10-07 05:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 11d14aba-0025-3845-be9f-58a77afac172 | -1.28789 | -54.57047 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0e08b57a-363b-35b0-8976-a13a97dd41b9 | -3.08899 | -54.28487 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ae0d2f75-2a36-3dea-8428-16036ba2cfc5 | -3.08062 | -54.27423 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 12b39db5-dec0-398f-8fd9-bfcc10ad7de0 | -2.93543 | -54.12085 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54762428-1f0a-3125-a5eb-040fdd1fc3ee | -3.07489 | -54.28242 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8bd7542e-e4ea-3560-acfb-b415a7264be5 | -3.67663 | -60.5383 | 2026-10-07 05:59:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5f4e295-26a8-3cb3-995a-86c6936c7a4f | -3.85372 | -55.98987 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ff783445-ff20-3129-a593-c5c194dde2eb | 0.44582 | -60.53732 | 2026-10-07 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1783de38-3f6d-3e0f-a291-d582f7d793dd | -3.05685 | -54.15997 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 308a8afe-1d22-3d0e-ae5c-c29f1c3dbb13 | -3.57574 | -54.32017 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e50510d5-2bb9-38f1-871b-7cc5186bac38 | 0.44793 | -60.53894 | 2026-10-07 05:59:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5a14e9f-a723-3ff2-a4af-a09ceda7b021 | -3.54086 | -59.48168 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b1a9051-f7bd-3d76-9177-8b40e85fc823 | -3.05674 | -54.2098 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 964175ea-3c7a-38d8-a335-e9be6290e2bc | -1.79702 | -57.11408 | 2026-10-07 05:59:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1817c323-e617-3795-9bc1-c6f1ac143777 | -3.59365 | -54.57522 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e58b6c9-dd34-3faa-ab68-09ac423477d8 | -4.13751 | -54.91093 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a9e21cb-af8c-3d77-90f7-f8604b9e1d1c | -4.15886 | -55.1472 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa911d83-d862-3ed5-8d89-211f8cda6346 | -4.14246 | -54.92538 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f40a1fdf-cc1b-3ffd-bdfc-12e855fe8960 | -4.15984 | -55.14783 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 086d3934-4318-3a8d-8582-22b9ec746ef4 | -3.52725 | -54.65052 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 885d15c5-aaf5-3307-8444-467f2f2940cd | -3.00777 | -54.1246 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 95cc631d-21e1-3e30-8666-1ea226c909af | -3.51835 | -54.66269 | 2026-10-07 05:59:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab150b0a-9763-3bef-9e73-24d3d0ecc377 | -3.68535 | -55.95997 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d186009-501a-3294-bcba-b08b61114b40 | -2.99678 | -54.12233 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46ec3c8d-b820-3da3-9a52-5e7fb95d7540 | -1.10483 | -54.15426 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8694ff73-e5de-3fa6-8c60-5ee1a3ac8286 | -3.77334 | -58.52319 | 2026-10-07 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e62c523-4845-3b0a-bc07-93a0555afcf0 | -3.84881 | -55.97826 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| aa56a149-e475-3d4e-985d-205c920b5e08 | -4.44485 | -54.97557 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e23b1a40-aedd-396f-bfe2-28b499d160b0 | -3.99303 | -56.26835 | 2026-10-07 05:59:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0901e59-1761-3c5d-be54-fe08732ee0ce | -3.10264 | -54.17157 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4e67742c-063a-30e8-995b-080b7146cf71 | -2.97021 | -54.13204 | 2026-10-07 05:59:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01862e12-40cb-3bf5-8b79-d58313688449 | -3.10418 | -54.28014 | 2026-10-07 05:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b80f29a4-cb9b-38a9-aadb-9dda020f80d3 | -4.15735 | -55.16533 | 2026-10-07 05:59:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9c606fc-1a40-3d52-9f73-93cb8869b571 | -2.70448 | -59.80695 | 2026-10-07 05:59:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d18453d-dadc-300b-96c1-f564c772042f | -3.55716 | -59.47789 | 2026-10-07 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05bf14b0-f378-3605-b5ee-d1582c9524f8 | -1.282 | -54.56353 | 2026-10-07 05:59:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README119.md)
