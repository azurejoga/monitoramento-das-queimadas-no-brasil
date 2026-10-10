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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f6e641a-cfe9-3fcf-8971-95cc05661657 | -3.30241 | -54.68019 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| caed6d37-2194-3a76-bb0a-202c4fb5a5a9 | -2.997 | -53.91011 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a972e28-f536-3e44-83aa-5d67a9bb1b51 | -3.16372 | -54.72299 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8cc4e0b-edfe-3653-95d0-0f7c92b06ad4 | -2.94648 | -54.18501 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97937f37-6fcb-3678-800c-fbd3b3644cb6 | -3.18695 | -58.64717 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd1b5bf9-cc75-3eb4-a205-bfe717c34ca1 | -2.50255 | -56.20353 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 812d9f2d-ac05-3f2a-bc46-95d009fb83db | -3.0845 | -56.79349 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2951e4fb-5a0d-3872-8d72-2f1724ec29fb | -3.02476 | -54.05571 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91d090c6-2134-3e00-ad6d-bb21fb00b37e | -6.7714 | -48.66572 | 2026-10-10 05:04:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 9.3 |
| bbeac621-d06b-38b3-aed0-03966781b4a2 | -5.88864 | -57.72528 | 2026-10-10 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cd6d92f-d60e-3282-88b2-4d79a44c0e12 | -4.94209 | -55.0986 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d7544eb0-aeb1-3355-ba88-3bd2b5bbb435 | -3.789 | -59.376 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dc44468-760c-3778-a4e3-689a8a9019bb | -4.15766 | -55.13715 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63af0c59-270a-39f8-8c0b-50227fde0bc5 | -6.36777 | -55.27523 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 577461fb-1ff1-304f-a8ac-571a57d61d10 | -7.20939 | -55.15557 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 935b4dba-27ff-3e96-ba02-d929d0dde090 | -3.164 | -58.62865 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ec7b3de-0ba4-3e3d-b1a0-a1279664fefe | -3.57528 | -54.35502 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09d5906b-3a7d-39c3-b460-a3a5e41ab9bf | -7.24417 | -55.21441 | 2026-10-10 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5dbb111-2c6c-3610-9a32-3655ca3372a1 | -4.57017 | -54.9557 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7a4ba77-f0e4-3649-8bd1-edccd713a9f6 | -2.99315 | -53.91304 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 540e1e07-4cfc-3032-820b-4842c4847db8 | -3.43037 | -54.53939 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22f1f6a0-e609-3152-bda7-1bcdf811fe88 | -2.99424 | -53.90614 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07a83603-6f7f-3d05-8dca-c13b08f3cc63 | -8.25078 | -46.41839 | 2026-10-10 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc16c725-68c4-3ea5-ab55-7d5176517c43 | -2.88195 | -54.18543 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dac750ba-67d9-3748-896f-de8ce358b0e0 | -2.82014 | -51.95749 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98d689ba-d094-3b32-b0ec-6d53ac3f2cda | -3.43758 | -54.53696 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cad34331-b742-34d7-881a-c3f064aa18b6 | -3.37779 | -44.48297 | 2026-10-10 05:04:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7e65af3-18b0-3fd0-a7ea-c8870b73e109 | -4.11491 | -54.01649 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb46a5b2-e15a-3dc8-9d3e-4b56150af56b | -7.18922 | -52.63382 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b5d470d3-7ce8-3777-8aa3-ab69352dd800 | -3.27521 | -53.86911 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c53d010-e971-3bd0-945e-a5ba0c3e1868 | -4.34189 | -55.12996 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e09e4381-e7e6-387e-9f8d-681d7d645395 | -3.74276 | -55.95329 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 72dc7309-bc67-35e0-981d-dcdd277a4ff8 | -3.29893 | -54.0849 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 068285c9-5b91-3729-a546-6c555cd70898 | -3.30114 | -54.09231 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1507adb-899e-3226-9d72-02a79c71a0d4 | -5.59733 | -47.27918 | 2026-10-10 05:04:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdb4fff7-8108-34b0-90d8-e118a638f0bf | -6.23385 | -60.0348 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d2ddab5-65c3-36fa-b99d-76d3ecb06855 | -3.35492 | -50.41782 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc7dffa5-9f34-34c6-8d13-ac0bb25e95dc | -4.96114 | -55.12326 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bb5a158-926d-337a-8d69-ecf6b59ae98c | -2.84688 | -59.12013 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dfb2e5f-ffe7-3025-b7d6-14cc20e6ad80 | -3.11132 | -51.03267 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5d2f1eb-0374-3404-aae1-077e0aab4193 | -3.26596 | -50.38844 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5aee609-110e-3360-a2c6-3c679255a0c1 | -5.70442 | -53.48139 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4613d0d-0866-3821-a603-b2f3b10f731c | -1.37687 | -55.18258 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11459a19-74df-3aba-aa3d-0f0203c0cb9f | -4.28448 | -55.13194 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4ce6297d-22e8-3aa3-8c65-a09a793d359b | -4.4021 | -49.77639 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c73d8f3-a93a-3e4e-acd5-2c93969ee147 | -3.58912 | -54.52452 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e4c9c92-4986-3d38-937e-43fb8eb2bf83 | -6.50181 | -44.36544 | 2026-10-10 05:04:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1693f83e-b115-3989-bdeb-4ca0c1dca1a5 | -3.7164 | -55.46672 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09369860-669f-3205-819b-bb4272d781f8 | -5.8419 | -44.93205 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 61edaac3-d132-36d4-b35d-d797d62f220c | -4.56772 | -55.05641 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 43667128-bda8-343c-8cb4-0a6ff56e44a8 | -7.03483 | -47.66349 | 2026-10-10 05:04:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd88a9aa-5fa5-3ff2-b7e7-1bb87b8595ef | -7.66562 | -49.78849 | 2026-10-10 05:04:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfd12999-45aa-3f19-b914-1c09c6c20321 | -6.25566 | -55.4448 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b02a9581-c15b-3e82-bd27-f0bd39d51ad8 | -2.86649 | -54.19719 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ef2614b-dbbc-3c56-9c81-c878e044da68 | -1.62907 | -54.43497 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbd618ac-a43a-3fe1-9ea8-52426703eb5d | -3.90505 | -59.5924 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1ce83b7-4e23-30d9-94fb-768e1cf950e9 | -3.40167 | -54.18605 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2951d638-129c-34be-8828-90c263ff5ace | -6.11901 | -55.70466 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b074aa87-431e-3dd4-9de7-f68c7c7883ac | -2.84214 | -54.13661 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9362705-ddca-3411-b73f-6e80806ac5b5 | -5.9317 | -52.18266 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 92125a9a-7a71-3205-9e6c-204976c4f518 | -3.53539 | -59.57576 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6a2d695-b019-32fc-aa8a-cc9ab4affefd | -2.84272 | -59.1194 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38f178ad-520c-38ca-883e-49f9e2fb287d | -6.79949 | -52.77554 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d7f9872-d58a-3bb4-af22-3bb37028da5c | -2.84876 | -54.11641 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff9a5d78-9049-39ab-b7ac-eca9138aa6ba | -5.88817 | -43.41061 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f5077dc6-6f63-3dda-ba05-e286fe023c04 | -3.25871 | -54.18826 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c44d10e1-8976-39d4-8902-a25e18c9588d | -1.62349 | -54.42689 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 015ff0c5-4708-3125-9112-b9b042bba5d3 | -3.44332 | -56.91081 | 2026-10-10 05:04:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ef1bba2-a43e-3d8e-9149-647910713931 | -2.97455 | -54.05135 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 46ecf70d-4e23-3cce-bb2e-295a8d13fcaa | -7.52235 | -45.32495 | 2026-10-10 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b48ab84-afb8-3e3d-88f2-142631a7ef15 | -3.52469 | -54.67181 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d76da916-fa25-32cc-98e0-75ab2657d9d4 | -4.98937 | -56.95258 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2133a2e-dd85-3f6a-bb89-36fd6d3560bf | -3.72163 | -54.22599 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7b2cc77-124b-36a6-95b0-ddc4a7c7cb20 | -3.46904 | -50.59614 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5826d5b-7054-3a1e-afb9-98ee04ff3e9f | -3.57133 | -54.70077 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3091b0d5-b7ca-3e21-9acd-afbc58387515 | -2.51055 | -56.13202 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a23335b-1984-3ebf-ac98-438f38f22d16 | -3.72965 | -54.64347 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b49c4164-824f-31d3-a654-00e4d9ed102e | -7.19391 | -55.14595 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3317fec8-8c70-35fe-bd1b-7f485c6e632a | -3.56967 | -54.68972 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1061090-01b3-38cc-b68e-a547b6b0ca80 | -1.38029 | -55.18313 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29b1809d-89a2-338e-a91e-804577cedd9d | -6.22478 | -60.03723 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6158fa6e-c659-3228-95cc-15a98ece90e5 | -6.41995 | -55.29079 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59707c66-875f-3717-bd55-f34f770d45d8 | -7.56466 | -45.64745 | 2026-10-10 05:04:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c4b3f41-9daf-370b-9303-736153e9cd73 | -5.21673 | -60.05048 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| edc455cc-d3c6-33a0-98cb-7b712a36b7c2 | -6.37779 | -56.23171 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195b6445-b8b1-3b53-ae42-f491ee920c51 | -2.97788 | -54.07309 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e80deb51-5982-3762-8ae6-f81b927ca2e2 | -3.01994 | -54.17174 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d839a96-6474-3f39-8566-a635fe8618c1 | -6.4402 | -55.03579 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c9bc6c7-5281-3482-b425-fa27cc1048b6 | -2.99132 | -54.77907 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 237e01ba-8494-3a2e-bd78-9542c97a2bb6 | -3.11619 | -54.16539 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0fdc4b3-362d-3149-84f4-2f4dece79bd8 | -3.85391 | -58.90152 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 830ef804-d46d-3e7c-a7bc-4f491dd45393 | -6.20896 | -45.42746 | 2026-10-10 05:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 890ea8cc-4623-3a03-be0b-76290d57e753 | -6.43082 | -43.51246 | 2026-10-10 05:04:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e145713d-ce9a-3709-9604-e4c9d54dfde4 | -3.84494 | -55.97248 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b740bc5d-e210-3038-8873-a0af2f452f59 | -1.48555 | -54.52459 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6ae63db-6b8d-383d-82af-45e85990050c | -3.04551 | -54.16135 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72e07c94-bbf5-3fc1-93b8-3ceacadc63b4 | -5.31688 | -50.06933 | 2026-10-10 05:04:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1a528e8-996b-3868-a416-7faf0436d8a0 | -2.21884 | -53.69505 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 903a7b67-c6c4-345e-8a20-3d3cdedff4e6 | -6.34511 | -55.14194 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a1ade1a-01b5-3326-b8e6-dc950148f8e6 | -3.49123 | -54.20053 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README115.md)
