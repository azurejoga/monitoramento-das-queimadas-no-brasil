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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1267325-dfca-3a9b-800e-13cf19f51df1 | -3.84738 | -52.34768 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| aaaa0639-1cf4-312c-afb6-8c30bfc08995 | -3.28331 | -53.85806 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 96f4a542-6f16-35da-a8f9-390c2cb80ae4 | -3.43084 | -54.60443 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ed6f4d2d-47f0-3d51-ae0e-b10b2da5d193 | -1.26178 | -53.36575 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 2908b7bd-2eca-3c9f-9924-f0bfbb600eaf | -4.01353 | -49.91507 | 2024-11-22 01:06:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 41673060-ffca-3a7a-8836-cba2d8c69cdd | -1.22022 | -51.74437 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f1719baa-815e-3113-baa8-24b7592e892b | -4.11753 | -51.04913 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 75bcfbdf-3bfc-310c-8927-3bd64b354bea | -4.25051 | -53.53037 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c95e5234-2c77-39f9-9654-7f9c4ce579d9 | -5.95836 | -48.05044 | 2024-11-22 01:06:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b6b98f3c-3657-3ed3-9995-69cba3d02de3 | -1.29316 | -51.73686 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| e9503ded-abe7-3cff-8fd2-8c603b6f82ee | -4.04531 | -53.92419 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b0f36c71-6153-3097-8aa8-68d1135b74d3 | -1.5018 | -51.9767 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 509b128d-7ee5-3ca2-9f7f-b9a37ecd9799 | -1.62105 | -52.43056 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b45c9a45-9817-35c8-98b7-797b2c3e0f58 | -4.24385 | -49.07667 | 2024-11-22 01:06:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 50da6024-a8c1-3aea-aaed-4f0bdc1549f3 | -1.92241 | -52.09119 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 940de149-1254-3efb-ac30-e79e9302eee0 | -3.52891 | -54.64856 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d0de8725-d147-3f81-813f-92fb53b537d6 | -1.74354 | -52.38904 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ca206b48-3f6c-338a-9e5a-88c98d956caf | -1.12122 | -53.40968 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| ace4f783-8e33-3010-ace5-478de1ad0222 | -3.21497 | -53.83855 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 296326e2-81d2-3f9d-8af6-91109de877c3 | -3.87642 | -52.36158 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8a5e4fa9-77c2-3143-ba4e-dd4474a981a0 | -3.24291 | -54.22783 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 295faabd-ec08-31f6-b8d4-556a887efecd | -3.53789 | -50.53091 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e99c2535-5f1f-3523-97df-772af272d94b | -3.89216 | -46.09349 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 6977c853-d6aa-3207-ad61-dbc05ff78fa9 | -4.25184 | -53.53989 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d5c77172-5041-312f-b01d-2a0785568ba0 | -3.9551 | -51.13951 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0eb4b1c5-a903-3bfd-b1e5-3ecd60bf11c1 | -2.62031 | -54.27047 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c2275472-8433-38bc-8d7a-5c7826f08622 | -1.18528 | -51.94936 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 995787f2-12b0-332f-92b1-b239d7f13936 | -4.40648 | -44.11296 | 2024-11-22 01:06:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 5e2bb464-86c7-3af3-b810-080f7ebdbb2c | -1.42358 | -52.4137 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8606bb73-8930-3fcc-93d6-735cb040d823 | -3.52417 | -53.80653 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0bff3792-f32e-3fec-9769-26c35063a46d | -1.15612 | -53.6622 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 48446f3a-65cd-335f-9dee-ea7c3a65e0db | -3.58354 | -54.51825 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 310f3cb0-fb25-3666-a839-9a7ee0fb17ce | -2.7049 | -46.21974 | 2024-11-22 01:06:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 946c19e7-9e1a-3369-9b8c-b7e4dff20c91 | -3.84861 | -52.35652 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f85690e6-581e-31cf-b3b3-d16feafd200c | -3.56219 | -54.22013 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9345af9b-b0b6-370c-a7b6-3f09404c27e9 | -1.19417 | -51.9481 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.6 |
| beb446d3-7d6a-3d1e-b9e9-1e790fc7ac23 | -3.85322 | -51.40337 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e364066e-74d3-35a2-9205-09f60ac14b43 | -3.31581 | -54.0906 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7c058b58-62aa-3b0c-ab50-08a1f602da8d | -1.96971 | -48.38451 | 2024-11-22 01:06:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2c8a770e-7636-3375-9f0d-cc96df150f1f | -3.04395 | -54.84962 | 2024-11-22 01:06:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a8563374-f31b-3b7d-8366-65da48b3e333 | -3.57181 | -54.675 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 419c934c-f249-3ffd-865b-185fbf3fcbca | -0.30915 | -51.48419 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8cc705de-d877-3d4f-830b-462fca7b5e79 | -2.79164 | -51.71785 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 0a4cea46-5641-34b9-b0b6-4fb7f6b52bbb | -1.39324 | -51.98925 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| adb7df19-95aa-358b-a41e-e6e8cd29fe33 | -3.82626 | -52.26054 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9788a38d-25ea-369d-aa49-0c6275353cc2 | -4.14478 | -54.66178 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 1ba7b14a-4c3e-3596-b0a6-2ac38dce4339 | -3.4649 | -50.01072 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 61d48ac4-c957-3bb7-b9b3-3809ac006269 | -2.44082 | -46.55228 | 2024-11-22 01:06:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 301d2f16-a8fa-3f4b-a9b6-723d35ea58cb | -3.53515 | -50.44472 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 0bb4bb0c-0747-35df-8c47-c11d9b0a36ac | -3.25078 | -54.24072 | 2024-11-22 01:06:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| b3f9f26e-41e2-3c2c-953b-e6917283ee47 | -4.0546 | -53.92284 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bc365430-f615-3702-b7fb-c2b00b9ea339 | -0.89579 | -51.72586 | 2024-11-22 01:06:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a7f05c1f-42fa-310a-925d-365eb009b8dc | -3.68431 | -54.58286 | 2024-11-22 01:06:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 80c3c465-e901-3b04-b722-ac6872beb8d5 | -5.24021 | -42.62313 | 2024-11-22 01:06:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 36.4 |
| f687dcc6-e19d-3a0c-8809-4aaeb304131c | -3.2096 | -54.26316 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 16dbfa30-a35d-347c-84cc-9fcac6a9a83c | -0.80362 | -51.79102 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7f3751d6-c17d-3ffc-9360-466aee8aa38e | -3.59834 | -51.5578 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2a70ffda-1c57-330a-8017-c77e725ff1c5 | -4.09374 | -46.21486 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 723226c7-f2f3-3676-abff-08c240192ec8 | -1.26478 | -52.0647 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8b7d84d7-de0b-3e85-a45a-1dd444560ef0 | -1.20617 | -53.69256 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| ec3f0c99-07aa-3d33-b113-c152f0307ec4 | -3.31071 | -52.86468 | 2024-11-22 01:06:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f62a66e7-5d0e-3631-86a9-f629e2aca98b | -3.75398 | -46.11972 | 2024-11-22 01:06:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 179.3 |
| aea6e994-7edb-3a02-bc35-6db845831bf5 | -3.80655 | -51.26432 | 2024-11-22 01:06:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 96530c23-840f-35c0-a9fe-1af9399d7d40 | -3.55483 | -50.51891 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d2ef1e06-e2ba-3c32-8207-6cadb05a5610 | -3.84519 | -51.14317 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4030ec46-711a-313e-8eeb-ca442846dcda | -3.83634 | -52.26814 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb2ced8a-ab9a-3186-8c7e-f8d1da9999d6 | -3.66618 | -51.57803 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fcc6d89-1546-3acd-b4ec-53a8b0a43e70 | -4.19823 | -53.48948 | 2024-11-22 01:06:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e54d27b9-4a57-3d76-9a0a-dd702d402953 | -3.3393 | -50.49468 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cc39ec5a-62fc-33bc-950c-274b5567e997 | -3.70974 | -53.7491 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0cb0c198-537b-3363-8535-611dba78d14a | -1.79833 | -48.47386 | 2024-11-22 01:06:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c1c36193-2169-37aa-bb00-3f951c123d39 | -1.27263 | -52.97707 | 2024-11-22 01:06:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 25ec5e00-3a95-35be-85d5-d8bacd575298 | -2.70163 | -51.8633 | 2024-11-22 01:06:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| d8d053b5-fdc6-3263-9ca2-1402e66efaaa | -1.46729 | -51.13779 | 2024-11-22 01:06:00 | TERRA_M-M | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3f208537-01c4-343a-af91-f2489f0ddb70 | -0.26465 | -51.56221 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 134dc472-f402-3477-afa4-9db676f5b52a | -3.19883 | -54.25436 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 253f5d16-d8b9-3b77-96ac-38eb646c9cca | -1.77673 | -53.6231 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d86601e4-daa4-3003-9a85-60a51249dbb1 | -3.45719 | -45.90547 | 2024-11-22 01:06:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 1a2604cf-0c71-318a-ada3-9ae4cc8f1817 | -5.5832 | -45.21186 | 2024-11-22 01:06:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9abfd557-2057-3784-a5c3-96096630c875 | -3.17887 | -54.31841 | 2024-11-22 01:06:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 469ffb45-07ad-33ea-8254-07d8b508fbcb | -4.20014 | -48.55997 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 65509fb1-ccfc-3d81-b6b5-69864e43f0c0 | -0.40755 | -51.59488 | 2024-11-22 01:06:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 245e6ce2-c129-32cb-9c31-d69674fcf755 | -3.50572 | -53.80886 | 2024-11-22 01:06:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| c6a441d1-946a-3d85-a20f-14c3fd293268 | -1.1374 | -51.6796 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ac7a34ae-7f99-3c7b-a065-c49956ea8bad | -5.24528 | -42.65475 | 2024-11-22 01:06:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 41.0 |
| f0f36efe-6958-39ce-83fd-8ce506b6f538 | -2.4382 | -46.53475 | 2024-11-22 01:06:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 6bf1aa0f-3c14-30d8-86fc-690f1b7cdef3 | -1.22768 | -51.79804 | 2024-11-22 01:06:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5d7a5e8c-6ae5-3432-8991-ab7a73d2a484 | -1.63693 | -52.62258 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 53e73fdf-3109-344b-8521-be6825ae79ef | -2.01719 | -51.18283 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a7258f72-5d24-389b-83c1-3c3741b136ce | -2.44852 | -53.68697 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ae782daf-800f-36b7-80e7-454d0e3e0064 | -1.92119 | -52.08236 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b3289e56-6176-30fd-ad07-683c20b7550f | -4.21552 | -48.66424 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 48f30752-a8dc-3a3e-b76c-b377406f637b | -0.93708 | -47.55726 | 2024-11-22 01:06:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| bbd8404e-2d54-3cd2-beaa-d7a36ffd0a68 | -2.51088 | -54.14253 | 2024-11-22 01:06:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2d6cc05a-6c74-3aa9-b331-92206aae7ee5 | -3.34977 | -50.50279 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 64142673-6159-3e1a-9e21-194338248419 | -2.31004 | -52.48796 | 2024-11-22 01:06:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 82eae1e0-7825-39da-9064-679d3d027722 | -3.15922 | -50.59038 | 2024-11-22 01:06:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 18e04d37-3883-37e6-bd23-93540c7e947b | -3.58344 | -50.26635 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d051a773-062f-3723-885e-a5b94dcf9663 | -3.72718 | -50.4339 | 2024-11-22 01:06:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a17ad530-7f29-3746-8b4c-ff9dea370bcc | -4.2339 | -48.64983 | 2024-11-22 01:06:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README5.md)
