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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9aa6c684-4b99-37e5-a5d8-94367dcac881 | -7.31543 | -47.41895 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7dec57d4-0943-305f-9752-b126176982be | -7.68487 | -47.25894 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77358f46-1162-3ab6-9f76-519d18e7a512 | -7.49266 | -47.08556 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1ccaa2fa-5a8b-3e07-944c-0ca2693ce9ac | -7.49204 | -47.08931 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a454a890-e707-357b-975b-0bbc74da94ed | -7.49141 | -47.09307 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 15039030-9a7c-33d2-b9b1-93cd3dc527ff | -7.48789 | -47.08862 | 2024-09-26 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e868eb2e-1f96-3a39-ba7a-4184ade4ef21 | -7.27421 | -46.8675 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d27a8bc1-60d6-311a-af55-d3a30224ec0a | -7.27358 | -46.87125 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a118583d-53cb-3c5f-8fa3-e8056c81a9b4 | -7.26951 | -46.87042 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b182be62-6daf-383f-9e2d-cb35a46d6fdb | -7.2661 | -46.86569 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 352ddf72-2a23-35ab-b218-de35fe669f7b | -7.26267 | -46.86104 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11528e28-f78f-3364-9f08-b9151ae197b6 | -7.26204 | -46.86476 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b0ac12e-0117-38ad-a9bf-30a41f359b8e | -7.03109 | -46.8965 | 2024-09-26 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1fb5ed35-a0e7-3a36-b07e-183ceea4e813 | -6.75329 | -46.99347 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51db47ae-0526-3330-9e0e-44a538afb340 | -6.73349 | -47.21764 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e23fbd8d-be42-37fa-ba5f-ac6a334ca592 | -6.73336 | -47.2165 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 81400e45-67f7-3b2d-9c16-4004a2b4d3de | -6.73283 | -47.22162 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f603890f-d414-302a-af54-70817e33889a | -6.73267 | -47.22049 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cfb6aa80-a551-33bd-ab00-0ceaae95a588 | -6.7286 | -47.22092 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63eb9289-558e-3d5b-a8fc-2ca955729fb2 | -6.72844 | -47.2198 | 2024-09-26 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bf6e6459-1ae3-336b-bc63-43d94eb42c3e | -10.69142 | -47.95853 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ab89267-5fa7-3cb4-acf7-d9d76f97e0ef | -10.69006 | -47.96635 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68aaaa8f-95aa-39cb-a224-d859fb57bc44 | -10.68937 | -47.97029 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e96b0af9-fccf-3b62-b878-407585b284f1 | -10.68722 | -47.958 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0bfa81f0-784d-3990-bca9-ed83ad54625c | -10.68518 | -47.96972 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de128ff0-049b-3e96-abe2-9831c3700c6d | -10.68356 | -47.92986 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 803e7500-e6ce-3856-81f1-565c1f6728ca | -10.52847 | -48.07111 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fd366dd-6346-32d3-b2b5-ab29f4bd19ca | -10.52514 | -48.06538 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ab13815-0046-3d8a-9f2c-7c8d94ec9bc1 | -10.52008 | -48.06948 | 2024-09-26 04:06:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c03a5acb-cf51-3659-85bb-ab37154b70c0 | -10.32816 | -47.8287 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffb68b62-9fc1-32da-88c2-60a48248af0e | -10.324 | -47.82807 | 2024-09-26 04:06:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9a00ca3-10e7-38d8-b852-0b1229b2f366 | -11.72056 | -47.85638 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c7da955-a875-3c9c-87c5-6d20de30ab18 | -11.71993 | -47.86007 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d9805375-bbdc-3695-8277-8c4db569c3a7 | -11.71777 | -47.84829 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48513c54-7f85-3951-88ed-9a2fadaefe5f | -11.71714 | -47.85194 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d826317-d8ff-3df4-b89c-2c08423bbef3 | -11.71587 | -47.85928 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 98c7b352-8bff-3400-a557-906d00b3e5bf | -11.71523 | -47.86296 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0db6894b-13b3-32d7-b601-e6966f67345b | -11.71371 | -47.84752 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3b80e10-7535-3f6c-8670-6764338e360e | -11.71245 | -47.85483 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3bc3f55-d6ea-3bcc-8b80-3dfa0b0c649e | -11.71181 | -47.85851 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 46cc14d6-22b2-34be-9c47-248dc7e3e62d | -11.71117 | -47.86219 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89ca9a2e-3f9f-3046-b398-85a24cb1614c | -11.70965 | -47.84676 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e64d2668-1208-3296-b532-cbf05565e5e1 | -11.70902 | -47.85042 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3a905de-803b-3344-a2c4-623ddeff53c5 | -11.70838 | -47.85409 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 924f053c-219c-313b-81e6-7f9c0a647b08 | -11.70775 | -47.85777 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a7b1defc-c021-3f5c-be2a-1498d0ab4ec3 | -11.70711 | -47.86144 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3effa537-4e40-33ec-90f4-535337639dbb | -11.70495 | -47.84968 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1c3fd357-b380-3b02-bb01-4fd602a7cb9f | -11.70368 | -47.85704 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 851d0552-5cab-3bc7-9266-f7efc1cb2749 | -11.70304 | -47.86071 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7df3ab1-b8eb-397e-a491-9d55d071b161 | -11.70089 | -47.84895 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33476321-fd86-301b-ae27-323b03f27d28 | -11.69897 | -47.85999 | 2024-09-26 04:06:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd3b7e76-1391-3ce7-8394-c4b55316cad0 | -11.22294 | -48.07372 | 2024-09-26 04:06:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df8746d7-a538-301c-aa2e-9ed0b0f8666b | -5.87888 | -48.0922 | 2024-09-26 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 05ee4f46-73f7-3773-9eca-8c435c3c9f21 | -5.87811 | -48.09674 | 2024-09-26 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1db336f6-97c1-3c8d-9ac2-55df8bddb7d7 | -5.87734 | -48.10126 | 2024-09-26 04:06:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 5f4755bc-ff3d-3c2c-8ba8-78501712d96f | -7.27195 | -49.48608 | 2024-09-26 04:06:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a459e9a5-6066-362e-981a-af1744b740c9 | -8.78877 | -49.644 | 2024-09-26 04:06:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5ab5e57-4df5-32cb-9573-0836a0da7fd9 | -8.55865 | -49.60864 | 2024-09-26 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a5bdbfa2-1bd2-38fe-a4fe-58aa4d021ae7 | -8.55382 | -49.60785 | 2024-09-26 04:06:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c7971644-f1a6-3cb7-9b10-df674faec321 | -10.79646 | -50.11378 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16548a1a-a2f8-3906-ba79-3dbd2b7386a7 | -10.79548 | -50.11905 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f92e8d5-3541-3209-a95b-69a272bff005 | -10.79069 | -50.11815 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3f522dc-2a48-3c31-bdf7-91c1179dedf6 | -10.47443 | -50.25954 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 837b0b55-c777-3260-93e9-ee7f6e45efa2 | -9.96962 | -50.16729 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8f99c0ec-13ae-30e7-8e50-c9c017b1ab33 | -9.95036 | -50.10687 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1da84146-1e3a-3d91-a9a1-a6c00a66cbed | -9.89625 | -50.14208 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4751d84f-a14c-3282-b25f-52add7b29526 | -9.89359 | -50.14155 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 036123e0-3ee7-358c-b870-cc84ed1a8fbf | -9.88055 | -50.17344 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2652b5fc-b742-3254-8b84-92e3088497b9 | -9.5474 | -50.1919 | 2024-09-26 04:06:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 47794eeb-9dd6-39f3-83b4-821d39e4e05b | -9.40139 | -50.03661 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75f80c68-7aff-30ea-959e-65b950170c48 | -9.39926 | -50.03564 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a4b9ad76-9949-31a8-be3c-b5605a46dc36 | -9.39651 | -50.03569 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 795c6148-b006-3a85-ad8d-3c2b71d54131 | -9.39437 | -50.03471 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1ba17096-4e5c-383c-8be6-5d9167cf8c7f | -9.39162 | -50.03479 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 42619045-24b0-34a6-91cd-09f47e1d5219 | -10.15358 | -49.9967 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3630377-e77b-3068-b993-b0b89ba9f027 | -10.15264 | -50.00203 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae2c5588-ffdd-3d77-a86c-4d2b9db88dc3 | -10.15219 | -49.99797 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ec7a6f9-77e3-323b-a0c3-1fd1df3d2b89 | -10.15169 | -50.00738 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d132f6fb-918a-36c0-98ae-f6b3a308710e | -10.15121 | -50.00328 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00a0b2a9-89cd-3a40-b20d-47dde30e3fac | -10.15022 | -50.00862 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da32ff95-b478-37e4-be0e-7f3b199950b5 | -10.12571 | -50.01352 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1960dcd1-7470-34bd-b37b-e3f6cd8e1168 | -10.12185 | -50.00725 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e90b115-973c-3026-b071-c82b49a89cfe | -10.1209 | -50.01259 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6415c06a-436a-3e45-bcc5-6689568b2ffe | -10.64221 | -49.90709 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9adbe54a-a443-3201-9434-e87ef6478019 | -10.64127 | -49.91226 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b2ef8ad-e24d-35a8-a9f0-c6e2864c2001 | -10.63747 | -49.9062 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0dac2564-1bcf-3a0c-ae1c-95fd08407005 | -10.51313 | -49.7803 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fe6abcc5-a00b-3b32-aea0-7e8c93f11b28 | -10.51219 | -49.7854 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 408a5746-f208-37fe-acff-24ef4e00c9e8 | -10.51199 | -49.77895 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1066afd6-f85f-3043-8766-5ea66e0e1801 | -10.51108 | -49.78407 | 2024-09-26 04:06:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02191478-459b-3514-b2f8-263da3c2e8fb | -11.21872 | -50.28406 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 85a01c13-2ae7-39d6-8076-13c2c14f3101 | -11.17216 | -50.21829 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50598136-81cf-3bd0-9491-84f4e90f60d3 | -10.93729 | -50.15404 | 2024-09-26 04:06:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f2354d45-7ae8-3202-a0db-75c5468065ee | -11.15182 | -49.7293 | 2024-09-26 04:06:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 005ebc10-9761-375b-92e1-0bdc112a8af1 | -11.15093 | -49.73426 | 2024-09-26 04:06:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c2400e6-8bdf-3386-bbf6-fd868a339214 | -11.02251 | -49.63291 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6022f87d-3ed1-3f68-8d53-2bce15d67549 | -11.01789 | -49.63203 | 2024-09-26 04:06:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8366967f-e925-3b85-9208-c9d36fddd3ad | -9.13636 | -51.52897 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0be0355e-721f-3c51-b509-f649816eff45 | -9.13571 | -51.53244 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e237c00a-706a-3170-a46c-9b109a221bf7 | -9.13507 | -51.5359 | 2024-09-26 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README64.md)
