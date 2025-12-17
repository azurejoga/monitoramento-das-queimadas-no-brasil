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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b7b0004-4ab2-3c4e-9be4-8e26629a76ca | -8.72197 | -50.24582 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acf40131-7f2f-374f-9140-64bd8c396b51 | -11.71419 | -44.53508 | 2025-12-17 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 847ba947-7347-3ad7-b335-1d6f7c3f4f20 | -11.96683 | -44.48829 | 2025-12-17 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a0af8eb-5e2b-3eab-931e-0d9707408e83 | -9.00999 | -45.92318 | 2025-12-17 04:27:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7dfd939f-9a9a-3ad6-851a-10850b326870 | -9.81539 | -43.93319 | 2025-12-17 04:27:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a80cb72-a144-36e9-b852-4a1b05812e46 | -12.09994 | -43.77496 | 2025-12-17 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dfb46c54-5622-3971-b4ee-96da947b37f1 | -9.00944 | -45.92673 | 2025-12-17 04:27:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b6a1fbb-c83b-392c-a817-d565893fb2c8 | -8.73146 | -50.25617 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 338f1ef3-7fe6-3f49-9ba6-e42b2438c228 | -10.07294 | -39.43607 | 2025-12-17 04:27:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 17e97a35-82ed-3484-807d-3447e400d169 | -14.43737 | -44.86805 | 2025-12-17 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d80a80d5-d220-33c7-b943-3e4911b71ca9 | -8.73216 | -50.25191 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f86be4c-295b-3e0f-b33b-a369372efa84 | -7.88619 | -46.74948 | 2025-12-17 04:27:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb8062be-0155-3009-b71d-69e939b9b8cf | -9.00712 | -45.92654 | 2025-12-17 04:27:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffae9bc5-40d2-3a04-9384-f45370cb664b | -11.81833 | -43.79543 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11c0409a-c6b9-3d58-8610-20836cfdb916 | -8.72419 | -50.25496 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6deccd69-70df-3d81-b26e-45988247861d | -13.18248 | -42.96131 | 2025-12-17 04:27:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 738608e1-3e73-3b65-8b02-b877d21b4478 | -9.81901 | -43.93371 | 2025-12-17 04:27:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8091102a-d622-38fb-a3a0-e710add260bd | -10.58589 | -44.96769 | 2025-12-17 04:27:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e773b0e-b0dc-384c-944c-a463bb6cadf9 | -11.82358 | -43.79436 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 813d0518-7baf-366d-b630-00e81329d39d | -8.72572 | -50.26836 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c85ceb8a-e6e6-33cd-bd7d-033857fe8bf4 | -9.15655 | -40.97604 | 2025-12-17 04:27:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e1ddd0f9-ac78-391a-9973-ef45d1811bf2 | -8.36857 | -35.57811 | 2025-12-17 04:27:00 | NOAA-20 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 756e8289-8bd3-390f-8948-07e147346611 | -12.39359 | -43.66302 | 2025-12-17 04:27:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5d0717e-d853-3ab4-948a-b984e45fd07f | -11.71676 | -43.91866 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81bf5401-ba8c-3bd3-a551-851744cd431d | -8.58937 | -39.44665 | 2025-12-17 04:27:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| da4686c9-d521-3fad-a7ef-800af4e57cd8 | -14.43798 | -44.86375 | 2025-12-17 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50dc25a9-faba-3c9a-b941-3ab2ec47ea1a | -6.60596 | -47.61954 | 2025-12-17 04:27:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af83b294-9ddb-3802-8185-03e33df29731 | -10.06959 | -39.43483 | 2025-12-17 04:27:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2ddafcd4-53a2-3720-af65-58db1993b980 | -11.81984 | -43.7938 | 2025-12-17 04:27:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b1dcbf9-7221-3875-ad33-ab34b5809fbf | -10.363 | -39.12697 | 2025-12-17 04:27:00 | NOAA-20 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f60892e5-51e0-35fb-b701-723e5d2ca826 | -9.26341 | -44.31341 | 2025-12-17 04:27:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fd96c02-2cda-3ec0-bf66-ddda55d9d39c | -11.75016 | -43.30868 | 2025-12-17 04:27:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 75fb6be6-4cfc-3a84-bc7c-1a33392632e7 | -9.87786 | -40.56977 | 2025-12-17 04:27:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 25dcb4a5-d306-388e-b40a-7aa1d81c91a6 | -8.72126 | -50.25008 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e27437e5-5a23-360f-b484-21a06a6b9db3 | -11.27896 | -49.47662 | 2025-12-17 04:27:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e06d5c4c-6a7a-310b-8e85-0022d8a4716a | -8.7351 | -50.25677 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 671fc1eb-72f3-30ce-9867-3efd12290e2e | -11.96621 | -44.49252 | 2025-12-17 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa4a9f55-736f-3130-b4c7-58a75bd9ff0d | -8.72642 | -50.26409 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d438744-c366-3578-8553-a852724e3033 | -11.01532 | -45.25625 | 2025-12-17 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87db3933-d88e-31b1-9ba4-03d935b2630f | -8.72056 | -50.25434 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a38a3f82-33a0-3f12-bf87-26d9dd93a088 | -11.01878 | -45.25676 | 2025-12-17 04:27:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3501d3e-3b60-3b0f-9d4d-4f6200971404 | -8.72783 | -50.25556 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7062d48-1728-3b82-9ccf-0693b8e93cd5 | -11.96982 | -44.49307 | 2025-12-17 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aca28d8-1083-38e5-83e2-2f7a5c94c3b0 | -8.72936 | -50.26897 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61b1eb02-677c-3b64-ae8e-2090a1da0ad6 | -10.63598 | -45.15357 | 2025-12-17 04:27:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bb0841f-969e-34cc-a5b8-48567a807047 | -8.72349 | -50.25921 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae861ae3-2f4c-315d-9cac-a944a104ca80 | -6.69022 | -46.66534 | 2025-12-17 04:27:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6dd8ccce-8e0e-3d22-b762-fdf96873efc3 | -8.72713 | -50.25982 | 2025-12-17 04:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f13916f-7123-379f-9193-6d4c101b730a | -31.33817 | -54.07886 | 2025-12-17 04:33:00 | NOAA-20 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| c032f03f-3c68-3a0c-90a4-b7161a943e9a | -31.10527 | -53.43544 | 2025-12-17 04:33:00 | NOAA-20 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 0ca35efe-86e7-3f13-8bd2-3b401d522a62 | 3.44747 | -60.14453 | 2025-12-17 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bc02ab2-ecb7-3dfc-9724-6ed74cd4d7ee | 3.89625 | -60.54142 | 2025-12-17 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4055e97d-d2bb-3896-bae0-38da18d2c280 | 3.89536 | -60.54495 | 2025-12-17 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61afd70f-ccd4-398e-8890-5dd3d6fd0a68 | 3.89467 | -60.54046 | 2025-12-17 05:14:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca9bda17-fa9c-358c-b797-b150f8c83a89 | -3.14591 | -48.15494 | 2025-12-17 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21c9cc9b-b255-3dfa-8a39-91290b1d6cf7 | -2.93793 | -48.23264 | 2025-12-17 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a12fe5c-40e8-3ea8-b294-7722818c0750 | -4.14233 | -54.02656 | 2025-12-17 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a7ba0b0-c478-3ab9-8b19-8c6357f50d48 | -2.22915 | -51.94366 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1264a346-7a1c-363e-87b7-0a8222add5ec | -2.2298 | -51.93952 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd9be982-4c89-3660-89b8-549aa7b47f05 | -3.14021 | -48.154 | 2025-12-17 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d0ce84b-87d8-3fcf-8842-6edec40635a3 | -1.42041 | -46.06439 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e71a0dbe-32b5-3174-9c16-5a26603927bb | -2.58107 | -54.66633 | 2025-12-17 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b34207cf-616f-3d60-bd23-5a112c5ccd7d | -1.42676 | -46.06543 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c4511b4-7e44-3c93-9894-c3a8dee17611 | -1.28472 | -53.17572 | 2025-12-17 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9debae36-0433-3b55-9251-b3295565166a | -1.30589 | -47.25308 | 2025-12-17 05:16:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6b52e76-699a-3dcd-8c1a-d03e395184c6 | -0.91761 | -52.10287 | 2025-12-17 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f754d0a-89b7-3517-a488-5631b61f858e | -2.23223 | -45.65587 | 2025-12-17 05:16:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb59b999-4030-39b7-a529-3edc438bc25d | -2.6995 | -51.6441 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 035015b9-ef8e-3469-a012-ddea2f3d979e | -0.70572 | -51.98743 | 2025-12-17 05:16:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aa74bd5-5d7b-3685-8071-13bce979211e | -3.52662 | -52.56867 | 2025-12-17 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 781c0364-d483-38c8-9220-53bbc959d63d | -2.69838 | -51.64104 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| abd4fef9-df7a-3a0b-a8b7-c75ec9831d65 | -3.16644 | -50.21632 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2028e5c0-8fe9-3190-bf50-86743141a7b4 | -1.6637 | -52.0615 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da716027-969c-3fcd-8d2b-eb199ca815e7 | -2.70285 | -51.64172 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 636622a4-a4d2-3bd6-a2b5-c00c2ea73a45 | -2.4372 | -47.19703 | 2025-12-17 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9c39d57-a02f-36a6-96a4-2e8f355a44f1 | -1.42118 | -46.05925 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3f6ba9fd-570e-3f36-9d78-c5c6d20dfd89 | -2.69767 | -45.70094 | 2025-12-17 05:16:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 908b21a4-7151-3060-977e-620a96d8105d | -1.41745 | -46.06678 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b40db019-e70f-36f4-9e5a-6d30ffcac3cd | 2.70964 | -60.7503 | 2025-12-17 05:16:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9f1265f6-5f0b-3f8a-bf39-7494cfea611b | -1.41826 | -46.06162 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b777a6f-d722-3648-8ffa-860ca8de02b5 | -1.70866 | -52.62626 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e3df552-a837-3c71-bcc0-39ae897fdb75 | -2.77554 | -54.52519 | 2025-12-17 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2dce3e77-171e-3f9a-81c1-e3e86439e1f5 | -2.91176 | -51.78228 | 2025-12-17 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 370d0e69-b3bb-39de-b185-a623c426fe7d | -1.30527 | -47.25732 | 2025-12-17 05:16:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2c67dc-c555-31ff-9e11-62b5ef5273bd | -2.22729 | -51.93693 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c4db242-ec41-3a9d-9108-f10ea8693de4 | -2.77927 | -54.52569 | 2025-12-17 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d053284f-b7bd-351b-82fa-083c891b7d44 | -2.23163 | -51.93761 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5978e1c2-6bee-3a4e-8147-af34c5be80fc | -2.37857 | -51.91563 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7d102e29-6cf7-3535-bb17-168aed6a0bf1 | -3.03387 | -45.34747 | 2025-12-17 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 280b41ad-116f-3821-ad94-eaef347ee3ca | -2.37358 | -51.91912 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cb468757-00d8-3519-a2eb-03d2a846d207 | -2.36557 | -47.68114 | 2025-12-17 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 866a4238-96a8-33f8-8f50-4ac1c4070e6a | -1.41907 | -46.0565 | 2025-12-17 05:16:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30f5b555-f3b2-3768-8f49-bc9025537d38 | -2.2304 | -51.94593 | 2025-12-17 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29612f04-6a8e-320f-b67b-c8d5acb42b6d | -2.79325 | -51.40584 | 2025-12-17 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25a18af0-9f58-3004-b30a-2ae5d7e471bd | -2.16619 | -53.69057 | 2025-12-17 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4643f12-403f-3946-adb6-329a11bb7ea2 | -2.92662 | -48.23081 | 2025-12-17 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d44cc84-6421-37c8-b4d5-deac325b39e6 | -3.32745 | -53.24067 | 2025-12-17 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 933c8b05-4b64-30a3-a36c-e415ad67c252 | -3.32829 | -53.24 | 2025-12-17 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 528f4ea4-a0ea-353a-872f-d7277846d8e7 | -2.93283 | -48.22793 | 2025-12-17 05:16:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ff3f81d-7a0b-37b9-900e-b34c6be488af | -1.41716 | -52.572 | 2025-12-17 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README11.md)
