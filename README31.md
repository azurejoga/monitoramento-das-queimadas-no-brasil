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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7eef7d08-a3aa-3194-a4b1-62d5e36f1e2c | -6.9605 | -42.8816 | 2025-06-27 07:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.0 |
| 3b14f12d-806f-3bfd-8102-b43546065e79 | -6.9605 | -42.8816 | 2025-06-27 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 210.6 |
| c0b3ddf4-0f03-307e-b3d2-14d5f4321eae | -6.9791 | -42.9034 | 2025-06-27 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 139.2 |
| 2b30787d-aaca-3b76-a406-9094211d6c3a | -6.9793 | -42.8798 | 2025-06-27 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.9 |
| 37ff39a7-6412-306f-8649-2317a7d81637 | -6.9602 | -42.9052 | 2025-06-27 07:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.5 |
| 8bf66049-479e-3a02-b2ce-818d70384f34 | -11.5779 | -52.115 | 2025-06-27 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| a6837f03-a823-30bf-a714-81a497d63ed9 | -11.5779 | -52.115 | 2025-06-27 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| d3b596de-b3ef-3aa7-bf34-521c12946426 | -6.9602 | -42.9052 | 2025-06-27 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 213.6 |
| 4ef8faeb-ad9d-3815-8f5a-17b322681b37 | -6.9793 | -42.8798 | 2025-06-27 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 8d900dd0-8709-330a-8190-a7939d4d4eae | -6.9791 | -42.9034 | 2025-06-27 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 175.3 |
| 0e239c14-fb2b-39a9-be38-f29a1ce3153c | -6.9605 | -42.8816 | 2025-06-27 07:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 157.8 |
| 057ca269-7352-3e94-aeac-2dd4462601e3 | -6.9791 | -42.9034 | 2025-06-27 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| 8c2728a1-94bc-39ec-9a1d-cd5ca929e945 | -6.9602 | -42.9052 | 2025-06-27 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 189.4 |
| 2fe957b6-490a-3d95-b936-13fdd9796ef2 | -6.9793 | -42.8798 | 2025-06-27 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 111.8 |
| 09a0cfaf-6330-3718-8dd6-11763ecdf8ee | -6.9605 | -42.8816 | 2025-06-27 07:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.3 |
| 862c5645-febf-390e-8377-0c125ddb590f | -11.5779 | -52.115 | 2025-06-27 07:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 62338308-9611-3861-8215-49be14ba09d7 | -6.9793 | -42.8798 | 2025-06-27 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| df83088a-cfd6-38a5-984b-24731d6123e3 | -6.9791 | -42.9034 | 2025-06-27 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.1 |
| 72deb59b-d2f6-3283-af35-49fedefe11fb | -6.9602 | -42.9052 | 2025-06-27 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 222.6 |
| 9f1441e4-d264-365e-b2a4-ce65fc7b1b0f | -6.9605 | -42.8816 | 2025-06-27 07:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.4 |
| e20458ca-2e1a-329d-a8b9-1cd02fd3426f | -11.5779 | -52.115 | 2025-06-27 07:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| d36223b4-6431-3979-a2b1-66e667b8d0c1 | -6.9602 | -42.9052 | 2025-06-27 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.7 |
| a8636e02-5b73-3ab6-8f47-f8c546fdf3ef | -11.5779 | -52.115 | 2025-06-27 08:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 122b0919-a4b3-31bf-8c2f-31dd2318ac8e | -6.9605 | -42.8816 | 2025-06-27 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 155.9 |
| 578cd4c6-a0f8-3447-aa81-bc0a69c95b7f | -6.9793 | -42.8798 | 2025-06-27 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| 6f853a5d-9133-3ae0-98d3-385747b008c8 | -6.9791 | -42.9034 | 2025-06-27 08:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| 302181d0-9bb2-3da4-a43f-07d25d997859 | -6.9605 | -42.8816 | 2025-06-27 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| b01dfde9-cecc-3b6f-9b95-b0ba26a4ece6 | -6.9791 | -42.9034 | 2025-06-27 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| f8dfa152-7d72-35a5-8534-9a8c7a541fc2 | -6.9793 | -42.8798 | 2025-06-27 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.2 |
| c6ab7c69-0234-36b2-943e-b3df7e089f3a | -6.9602 | -42.9052 | 2025-06-27 08:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 200.6 |
| c83e27aa-2372-3d39-86dc-090424e7f6e2 | -11.5779 | -52.115 | 2025-06-27 08:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 249180f0-4594-37b5-8020-4a2bdeabed6f | -6.9602 | -42.9052 | 2025-06-27 08:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 170.7 |
| 5a37ffd0-b849-32ff-9913-0a8fac5f01f8 | -6.9791 | -42.9034 | 2025-06-27 08:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| d04decb0-310d-32ad-815c-475be53dd7e2 | -6.9793 | -42.8798 | 2025-06-27 08:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| c7c85fbe-f0e5-3c4b-aac2-58db35285502 | -11.5779 | -52.115 | 2025-06-27 08:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 42c0600d-0f05-3603-9e25-d7719de64cfe | -6.9605 | -42.8816 | 2025-06-27 08:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 160.7 |
| 74294532-0d82-30fb-95e1-eb8ef1b7d453 | -11.5779 | -52.115 | 2025-06-27 08:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 0f6fbb9e-302a-334b-bfe0-49cdb3c048c4 | -11.5779 | -52.115 | 2025-06-27 08:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 04d3cd4b-a099-3525-a22e-2502c3d0c28b | -11.5779 | -52.115 | 2025-06-27 08:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ff157f49-4e55-395a-a089-98ed21abe380 | -11.5779 | -52.115 | 2025-06-27 09:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 73b9bac4-d223-33d9-a7c6-ff5c6a6647fd | -6.9605 | -42.8816 | 2025-06-27 09:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 127.1 |
| 03976b34-c846-3a91-9a0b-6123f9472216 | -6.9602 | -42.9052 | 2025-06-27 09:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 138.2 |
| c548ecae-8227-379a-9d61-eb07d2f40e7f | -6.9602 | -42.9052 | 2025-06-27 09:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 143.5 |
| 75fbec85-281c-3d25-8595-3ed238e704fe | -6.9605 | -42.8816 | 2025-06-27 09:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.1 |
| 5e54da4d-2538-3cf1-870a-00fdb9c39676 | -6.9602 | -42.9052 | 2025-06-27 09:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 9773a7a3-5605-3a45-aca5-05d2492ef4f7 | -6.9605 | -42.8816 | 2025-06-27 09:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.9 |
| 69d12531-ce97-3fb7-a43d-d76b84c7920b | -6.9602 | -42.9052 | 2025-06-27 09:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.7 |
| 7cd255bd-cd43-3e1e-b011-6ba3a35f4701 | -6.9605 | -42.8816 | 2025-06-27 10:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 106.8 |
| b54e8782-49da-3380-a941-521d94343bc8 | -6.9602 | -42.9052 | 2025-06-27 10:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 4dbad9d8-aa93-34d0-b0bb-0b469a8904b9 | -6.9605 | -42.8816 | 2025-06-27 10:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.1 |
| f6264f15-c865-3f58-bf53-802d30a80738 | -6.9602 | -42.9052 | 2025-06-27 10:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 0cdcb608-5139-3f85-b319-ae393f4a814b | -6.9605 | -42.8816 | 2025-06-27 10:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 105.9 |
| a87e3619-3555-3290-bfec-d520a75c3cfb | -6.9602 | -42.9052 | 2025-06-27 10:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| cef6dfa6-6f86-3626-bbe5-f2a886772e69 | -6.9605 | -42.8816 | 2025-06-27 10:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| e57e6be4-5252-36a5-a399-60f098844444 | -6.9602 | -42.9052 | 2025-06-27 10:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.3 |
| 9b870da5-22f7-3440-b919-25ef993d0ba5 | -14.2442 | -45.5002 | 2025-06-27 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 5064218d-b1a9-350f-bcdc-4c882a341a81 | -14.2442 | -45.5002 | 2025-06-27 10:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 190.6 |
| be7cafc9-5a91-334a-9301-6d536100657c | -14.2442 | -45.5002 | 2025-06-27 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 48c58bf9-a467-3804-8937-0dac52ea217d | -14.2442 | -45.5002 | 2025-06-27 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 340.9 |
| 949e4887-b4d2-3865-8f50-07d0b22a4ea2 | -6.9602 | -42.9052 | 2025-06-27 11:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.8 |
| 9aaea6bd-ba46-334d-945e-42128f8c931b | -14.2442 | -45.5002 | 2025-06-27 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 395.2 |
| 99516f05-9f7a-3310-a326-49211a9293be | -14.2442 | -45.5002 | 2025-06-27 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 413.9 |
| a11ba4c0-6157-31b6-81ec-c985df302ebe | -14.2442 | -45.5002 | 2025-06-27 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 303.5 |
| 2d004dae-6009-3923-841a-23302467d355 | -14.2442 | -45.5002 | 2025-06-27 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 9622aa49-0665-3021-b96a-8f7b448f6b28 | -11.5779 | -52.115 | 2025-06-27 11:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e9e0ce4e-24a7-35d8-a78e-1acfad0fc5b1 | -14.2442 | -45.5002 | 2025-06-27 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 177.2 |
| c934c2b6-e246-35d2-a150-e22304e47fc0 | -14.2442 | -45.5002 | 2025-06-27 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 167.7 |
| 486d4ba7-5205-36b9-af2f-787ac32121c4 | -8.5722 | -51.5761 | 2025-06-27 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 108aa8d8-7b9d-3d94-8728-49bbfaa30317 | -11.5779 | -52.115 | 2025-06-27 12:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 2c16fc99-0a2e-3c54-90c0-d24be408841a | -14.2442 | -45.5002 | 2025-06-27 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 141.0 |
| 659dbc3b-08f7-377a-9cf5-77914ca53b81 | -6.5631 | -51.1126 | 2025-06-27 12:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| af37dea6-9570-3213-86af-5a45d9548c55 | -14.2442 | -45.5002 | 2025-06-27 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 81399677-5f30-308c-a104-f50e8841767b | -8.5722 | -51.5761 | 2025-06-27 12:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| af6d766e-05a4-34d1-835f-b60092fd5113 | -4.59372 | -47.72356 | 2025-06-27 12:44:00 | TERRA_M-T | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f49bd535-ce55-3559-9076-c8a0c1886a24 | -6.96438 | -42.88287 | 2025-06-27 12:46:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 62.7 |
| b4e6b474-9981-38cc-97fe-b6fd4fe6f0d2 | -7.55164 | -45.84411 | 2025-06-27 12:46:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7614fc6e-48bf-323f-9c73-feeace4f49a6 | -10.62382 | -46.73172 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1fecb233-e2f4-328c-a9a1-b6123b0d3680 | -7.86061 | -50.67194 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f5a5acd2-cb73-3ca4-b140-52912e1afdbc | -11.72461 | -49.67017 | 2025-06-27 12:46:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fc25e008-293c-33ac-ae96-5b49b2906bd8 | -11.14008 | -53.93394 | 2025-06-27 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e6439d1d-05b0-33eb-a74d-40e9dfe8ee99 | -10.38199 | -46.79002 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 314fdb61-6328-37d2-90fa-e995460ba003 | -8.14659 | -47.12398 | 2025-06-27 12:46:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 1b674142-da47-38bb-8965-ead9fce4168d | -9.07299 | -49.41653 | 2025-06-27 12:46:00 | TERRA_M-T | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d7075f82-06a6-3ad8-a5bd-30b1aee7c3c4 | -8.37379 | -49.22563 | 2025-06-27 12:46:00 | TERRA_M-T | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 265eba02-7477-32c3-8b9b-b97e010c192f | -11.44015 | -54.46888 | 2025-06-27 12:46:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 36996d4e-e748-3c6e-a8b5-67a1ef0d12a1 | -7.10528 | -44.37345 | 2025-06-27 12:46:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e58f03c2-151d-3823-9463-fb30886f2b0b | -8.57397 | -51.57073 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| a49cab01-f289-3378-9c56-c0baa4986795 | -7.54126 | -45.82112 | 2025-06-27 12:46:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 651a4c23-7a85-3594-a8ab-a1c9eac8219c | -7.74188 | -47.60423 | 2025-06-27 12:46:00 | TERRA_M-T | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 468645bd-f3be-363e-a596-b676239f70fc | -10.37934 | -46.80421 | 2025-06-27 12:46:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 14112250-8aec-36fc-b2b0-d1e7880d6065 | -6.74915 | -44.93403 | 2025-06-27 12:46:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| d657a4ba-6d38-37cb-a91f-18e27c9467b3 | -8.61761 | -51.58624 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| fad1383e-5cd7-3552-b37a-0093a1584f05 | -9.26098 | -47.90514 | 2025-06-27 12:46:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 972011ac-eefc-3f46-8e9c-26a49b07e4aa | -10.81914 | -53.73993 | 2025-06-27 12:46:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c7e35b77-4ea6-30e4-ab17-ee3aa2c58968 | -8.58296 | -51.57199 | 2025-06-27 12:46:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c8c0d67d-2ed8-38fe-9c6c-f61986e89242 | -10.03582 | -48.66246 | 2025-06-27 12:46:00 | TERRA_M-T | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 4e50b393-6975-340f-afc5-d01a04c5e2aa | -10.15561 | -53.9215 | 2025-06-27 12:46:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7aa5f671-e958-3f90-8d01-84bbe9c4c67d | -11.06438 | -55.37777 | 2025-06-27 12:46:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0d7081d5-16e9-34bd-bb36-e791298dfd13 | -5.87388 | -43.66882 | 2025-06-27 12:46:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 3e6a24d4-a937-3afd-b65d-87ef904b98e9 | -8.13855 | -47.13395 | 2025-06-27 12:46:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |


[Clique aqui para ver as próximas entradas](README32.md)
