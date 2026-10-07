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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88e9c58a-a3ca-3140-93f4-46501efa1c0d | -3.5421 | -59.4874 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f30bc313-e3ea-30cf-a842-1c992ba32045 | -3.0229 | -53.914398 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f01c9842-0cd9-3146-96ed-05afac39130d | -11.085 | -45.654301 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 97093ae2-1f02-39dc-a05e-9767c090605b | -2.9465 | -54.115799 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40b5b3ea-82d7-3809-9fce-dee3e61dd926 | -3.7684 | -59.393799 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d1fedfec-82b2-3e38-8437-f2085c5a6b10 | 3.233 | -61.028599 | 2026-10-07 00:47:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a63e232e-9aed-33ee-8331-635cfc800298 | -2.8783 | -54.1315 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c176bbc1-6619-30e5-b26b-45823dc83b8b | -2.7123 | -57.472801 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae42c5c0-dddd-3152-9dd7-f5eb906f9a6c | -3.9809 | -56.2211 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7fb38cc-6c5e-3547-aa39-b94a29f328c3 | -6.7696 | -56.241299 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc2700c8-cbad-3c02-87ef-3614d5a47076 | -3.0807 | -54.161999 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 908d0944-7e7a-3972-9ad2-6af2c3b433f8 | -3.1004 | -53.762001 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3e78c6-2530-3709-94c5-9e28f859bd71 | -3.4986 | -51.706902 | 2026-10-07 00:47:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14bcadf7-13b6-3092-9220-01ebeb74c83b | -3.0781 | -54.238899 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dea5ecba-fef0-3fbc-8dde-d9679474e227 | -3.2822 | -54.012299 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57217133-9114-3179-ad77-c3b86c39b7b3 | -3.0483 | -53.9352 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55e08403-2b22-353b-b9a5-7692a433106b | -3.4923 | -59.267502 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5ffe4a1-5ab1-3f36-a1c7-62b772381213 | -2.7881 | -57.6693 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c61f4584-513a-333b-9873-132182c99a89 | -2.9397 | -54.130199 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 639a4dfc-2750-3ce0-82d4-cae414a494a1 | -2.934 | -54.105701 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3eea6566-a41f-36e5-876b-5332fcfba5a4 | -3.11 | -54.155201 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 812a7420-8c9f-3c2b-bd00-6270ea9b8da7 | -2.1508 | -59.217098 | 2026-10-07 00:47:00 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79936ec2-f1c5-33a1-b7a0-658303052679 | -3.885 | -59.3172 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6e7ce563-898b-3f4e-a44f-997fa458a5ba | -6.2131 | -52.834702 | 2026-10-07 00:47:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 736067c0-af03-3c47-8561-1dd2caed99b7 | -4.3677 | -54.737999 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 933e783a-7cc9-31ea-b0b5-c936c3c0d19b | -7.7459 | -54.944401 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb017f6e-b39a-3737-bf82-141b5e6f65d9 | -2.9695 | -56.616798 | 2026-10-07 00:47:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34427f74-c1eb-3cd3-b6a3-0f22777b341c | -1.4641 | -54.770199 | 2026-10-07 00:47:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f87502a7-191d-3f0b-bc9f-5e665cd9e593 | -3.5275 | -54.622299 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2361007a-583b-367e-81c2-d3bb8b77e1b6 | -2.9811 | -51.037102 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1252d4a-3192-3e9c-8e4a-348db063c812 | -7.7502 | -49.2174 | 2026-10-07 00:47:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 5bf947c1-d242-3dbc-b857-b2adc8a0820c | 1.8026 | -55.5261 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 701e3ab5-4977-3289-837b-fc4ec52f37c8 | -4.3449 | -55.1259 | 2026-10-07 00:47:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 614a8157-ad66-300c-9be6-eddf7ebf3a7d | -2.5742 | -56.151901 | 2026-10-07 00:47:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bae3f43-66c7-3b5a-a2a7-86d328d835c4 | -3.0108 | -54.126801 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c10f1a8-8510-3699-9e13-1f04430d3864 | -3.0485 | -54.156502 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445c1906-6015-3d97-a48a-0506a6f55788 | -2.9144 | -54.110199 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7be29b1d-cf16-3030-a351-e7881b2df478 | -3.3718 | -58.1936 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd39af43-11f2-354b-af03-1ec832eb8c94 | -3.1303 | -53.7141 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a506ee-690a-3258-bec4-2885a739f3d7 | -3.128 | -54.364899 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0780a3a-736a-3f80-80ef-2056f8d5cffa | -3.0836 | -54.262798 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c0b2e88-0b30-3f33-babd-62c86b5f2aaa | -2.0353 | -55.644199 | 2026-10-07 00:47:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bbcdb4c-a069-3e09-8f51-56f34be4a655 | -2.5939 | -57.540901 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf955e7-8592-331d-a8a9-cb2495f74572 | -2.3213 | -60.060699 | 2026-10-07 00:47:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0a8b075-cd16-348f-b798-0251c0ed00ac | -3.5827 | -54.550598 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6576f632-d17f-3c6e-b8c9-7cf0067ad545 | -3.4831 | -54.609001 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 817b3e69-f9dc-3904-b791-4f5085895833 | -1.7958 | -57.1147 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 303c0451-9712-30e3-b822-cf938c568efe | -4.3769 | -59.8964 | 2026-10-07 00:47:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9285cfec-fc1e-3838-9459-7d27e0fb7be1 | -3.9283 | -54.576401 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f4efd46-68f3-3af1-8b1b-6c3906eac33e | -6.7677 | -56.233101 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2380a8b8-90cb-345a-bada-af0f6c774070 | -3.3701 | -58.186298 | 2026-10-07 00:47:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af8ea4a0-de6a-350b-8309-d6f6075442f4 | 4.1513 | -61.254002 | 2026-10-07 00:47:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 502832a0-2021-34ff-ba16-2af63cd83a1b | -11.055 | -45.8078 | 2026-10-07 00:47:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6916b589-472d-3107-9903-8e1999335f89 | -3.4982 | -54.629101 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90d56226-603d-34d4-91e1-2afb340e93e0 | -3.0961 | -54.2724 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79f41de0-5106-302d-8ea2-d7b1473d027b | -3.5669 | -54.4827 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf3add9e-4cf7-3a3f-b71c-e02bd83eea63 | -3.1162 | -53.7855 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b81c38d6-090b-345b-8f3b-4084e47dd587 | 2.7543 | -59.996201 | 2026-10-07 00:47:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d7b620ec-e324-397d-89ab-1e26fd7e9b39 | -3.0429 | -54.132198 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ad38fa2-1a0c-3468-8e23-e16aa6fd5aa8 | -3.0652 | -54.1399 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e36524ca-9f15-3547-b198-bf8df147fc28 | -2.9717 | -54.135799 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0d24fac-b9f8-364b-992d-5553fe7eba77 | -3.5977 | -54.570702 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f49f081f-2e58-3582-bdfc-aa319f61fafd | -10.8309 | -50.653301 | 2026-10-07 00:47:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| edd4e40c-5a22-3610-a5c5-ea74e8a1bf2a | -1.2796 | -54.548599 | 2026-10-07 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26df9a8f-5590-3d6c-ba91-29768a844e08 | -3.3319 | -59.469601 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd2df179-e773-3868-aeb4-fc39a5666e5b | -3.0432 | -54.2215 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcf96d8f-828e-3cc5-b074-54e38d267dc3 | -4.0967 | -52.065701 | 2026-10-07 00:47:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67c71277-0c83-3bc4-a820-61a2c046fb3a | -3.0415 | -53.949902 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1e8a6b0-f3d2-324d-9f08-d3a18002e1eb | -2.9454 | -54.154701 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2d39ec3-4404-3dd8-b716-7851965ac651 | -3.2628 | -50.4184 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f26d6ad-006d-3ef5-b339-307014203e6a | -3.711 | -59.686901 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8f419a23-3a53-3506-bd9f-4aaa9e75a882 | -3.0738 | -54.264999 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 168006ce-699c-357d-9e56-f7e897a079a1 | -3.7745 | -58.512798 | 2026-10-07 00:47:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bc5414ff-fb02-3091-b3b0-eaee888ff9f6 | -6.7658 | -56.2248 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4202e7b9-0397-308b-98e7-1ea9014ba00d | -2.7956 | -54.085499 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08d7d89f-67b8-3890-99bc-e63e6f57538d | -3.0883 | -53.7103 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7116827a-3e48-3632-b515-6780a38d1673 | -3.4425 | -56.926201 | 2026-10-07 00:47:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d6f8d09-93ae-3ca2-a573-17ade8977566 | -3.1071 | -53.746799 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f715ff49-2ff3-3ffd-bd73-11717d7b70c0 | -3.2662 | -50.134102 | 2026-10-07 00:47:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cff8d1d6-119a-3f39-996c-6924389a0aa5 | -2.981 | -54.042801 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eba3fa41-27c4-391b-a7ac-4ce658bf661e | -3.7002 | -59.639099 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c56c7dbc-46a5-3cf5-8ba7-d0b678d3edce | -3.8979 | -59.328701 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dff1623-0649-33ac-b622-c101102159cb | 1.5235 | -55.993099 | 2026-10-07 00:47:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c555ae76-8549-3606-ae22-3602621e0567 | -3.7384 | -59.4436 | 2026-10-07 00:47:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48f34f7a-72b1-3517-a171-270de9eee224 | -3.3479 | -59.494801 | 2026-10-07 00:47:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3ff8071a-194d-3454-b580-c3dc4bb0e32a | -2.6028 | -57.580101 | 2026-10-07 00:47:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5afc661e-fa55-3734-bad8-3dd5a65693a1 | -1.7939 | -57.1063 | 2026-10-07 00:47:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 743bb932-1218-3f16-93a8-e50c8807ee9c | -3.0683 | -54.2411 | 2026-10-07 00:47:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96bf7a3c-d3dd-3d29-a74a-893fd3ee08ef | -4.3784 | -59.903301 | 2026-10-07 00:47:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 59a328d4-75ab-31b4-abc8-cd4223d3e6d1 | 1.5332 | -55.9953 | 2026-10-07 00:47:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93a3563d-1c04-3e53-ba5c-06ecb026ccbf | -1.2921 | -54.558498 | 2026-10-07 00:47:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4590ca1f-8f55-3364-b15a-1ae2a6a5b1d9 | -3.513 | -54.649101 | 2026-10-07 00:47:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fd549a6-ee06-3b93-bb8e-afe0c1ee624f | -3.2713 | -54.053699 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab7c7979-2652-3c92-bdef-74c8be419a8c | -3.277 | -54.078201 | 2026-10-07 00:47:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e0ac4a-eb24-3062-bdf5-7588c0776be5 | -3.9731 | -56.054001 | 2026-10-07 00:47:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0082ac0-b19a-3cfb-bce7-55756281c18a | -2.8346 | -54.076599 | 2026-10-07 00:47:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65fea301-fd6f-37af-b146-dd97bad89fd1 | -3.9789 | -56.212299 | 2026-10-07 00:47:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7422d41-6aad-3a35-8fec-b26d778477e9 | -3.7981 | -51.030399 | 2026-10-07 00:47:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7434db6e-0db5-3cf5-9fa4-d476bcd04a23 | -9.2967 | -63.729 | 2026-10-07 00:47:00 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a4753ca2-37ea-3c32-8b4b-d3cc13b2d10d | -3.1002 | -54.157501 | 2026-10-07 00:47:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
