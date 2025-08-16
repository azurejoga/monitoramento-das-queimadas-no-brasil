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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fd95f63-f072-37bc-a590-bcc48d738d79 | -11.35106 | -55.42294 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e7db282-4656-3d9c-8bb4-ee178a03ac8c | -13.47356 | -61.00043 | 2025-08-16 04:34:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4ecb174-52d4-36b4-b679-861a91d727ca | -9.20908 | -59.66137 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d48ef61-9cda-3a84-8a9a-69749787ca7a | -9.16391 | -59.63847 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 12c5ba72-ebb7-33f8-8736-4d37cb6e4ae2 | -14.53135 | -48.58026 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aeb5dc0a-6192-3cee-8332-661304823174 | -14.8701 | -60.08087 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b9db22bd-2f5e-3213-913f-9f0cd7a84613 | -9.20334 | -59.6403 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc8fb56d-1410-31a4-a210-9fe965ee8a4c | -13.10121 | -46.84772 | 2025-08-16 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 57f7ce7e-feaa-3db5-adcf-ca39d7f95ebb | -14.86781 | -60.09197 | 2025-08-16 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9fef713-b734-3ffa-9b64-65bccb52184c | -12.8446 | -46.0531 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93086cc9-d62c-365b-a02a-75e1a29b61ed | -11.51376 | -47.24291 | 2025-08-16 04:34:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5e6580a-f890-348b-97d5-88c127126a03 | -12.82649 | -45.99703 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c317cd6-54d1-38e3-bf3e-e331daeb8d43 | -12.60749 | -46.94165 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a1354714-d8cf-392f-af52-5c35018f30c9 | -17.21299 | -49.58833 | 2025-08-16 04:34:00 | NOAA-20 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d068935c-fdc4-3394-ac51-4ac8788aa983 | -10.96212 | -49.56981 | 2025-08-16 04:34:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f9f7279b-521e-39ff-a5f9-6bbb05661338 | -13.14371 | -57.16478 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6d75dc52-80a2-3cfd-bc28-9de99ce8d0ba | -11.31198 | -42.07262 | 2025-08-16 04:34:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2711a694-cc1d-33a9-a27d-d30c3d13c681 | -12.53348 | -46.95101 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 903d30bc-b21a-322c-b42d-25beeb7dd643 | -14.58565 | -47.91541 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 27dad1f8-da55-31b0-b83d-bf32b222d617 | -13.43631 | -56.67682 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e4dcdc4-5147-33bb-9146-fc2233b481fc | -13.60784 | -46.91467 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20e8f4f4-6ba5-3fee-a13e-1d0d1c8e3985 | -13.00179 | -56.87485 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 693f42a1-2b1e-370b-a149-fec42ece08a5 | -12.82251 | -45.99796 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03d2493e-3b35-35cb-81b0-42a624e2664e | -14.93934 | -54.75389 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c6ab2fed-06b1-3f26-8777-64c37521ef9f | -13.57029 | -46.97485 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7f2c9d42-d571-33e5-a43f-bcecc319a3de | -10.17646 | -49.51111 | 2025-08-16 04:34:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 786dad95-1bbf-32c0-8f72-2766bca32ed8 | -13.10977 | -57.13609 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ed1eda38-744a-3cfe-9f47-8102ed582a91 | -14.52463 | -48.57917 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 707c80b7-a380-383b-85ba-9d8111375879 | -13.43911 | -56.68732 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33d55344-6594-38e9-99e5-3795d7a95d90 | -14.48138 | -47.72299 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f973167e-5f75-3fb9-aad4-ec07eddbe88f | -11.35337 | -55.4101 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc0d10de-ca0f-3bac-8e96-bb76fe882416 | -12.61616 | -46.93121 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8dfebd24-965b-3fe9-b474-5503be8c7461 | -12.82168 | -46.02896 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0de7ba5-b5b8-3513-b358-ce818b3638d7 | -12.53462 | -46.96724 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3011559-bdb1-3e50-afde-ce4224db9591 | -8.98662 | -60.56461 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 356839a5-01a3-3cbb-aed7-13014e4edd4e | -13.12496 | -57.13354 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37afb14a-5c16-3577-bdb2-07c30a1714e0 | -14.52409 | -48.58282 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b285b16-4e5b-3559-bfbf-fc084466e968 | -12.60109 | -46.91232 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 36aacc66-76ed-3177-91f0-209accd4398d | -8.8924 | -60.74285 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48d8899a-8aa0-3f8f-ae42-60c53b94d1f0 | -9.2194 | -59.65314 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| aa050ce4-f205-3aaa-8043-39a5451b52cf | -13.33311 | -45.21703 | 2025-08-16 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ca2f8b2-6c48-385a-b5ef-8f50a5a17f76 | -9.16482 | -59.66626 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e80410e-0725-3646-80d9-9a494316e0ed | -12.54448 | -46.94888 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23cfb9d5-47c8-3292-8068-04069e2b1d7d | -13.00644 | -56.87584 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46211045-a417-3193-b649-38cf772b0aaa | -12.82278 | -46.0233 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 35e3403e-d04c-35f9-b0d1-11b1a47f2c4b | -12.56592 | -46.94846 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c7053c4-6d58-37be-965c-f622da6ede46 | -10.85009 | -45.2212 | 2025-08-16 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| feab2e1a-f001-30ab-8461-c80d5e7bfa48 | -13.12024 | -57.13255 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7f3e1ecb-54e1-34d1-8d16-075e05813443 | -12.57348 | -46.94557 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e3ed59d-2f49-3da6-aa3d-1842e0548aad | -14.94718 | -54.7555 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 112b018e-3115-36ea-a844-aa33ae76a590 | -14.58677 | -47.90792 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 70fef3d5-686b-3a44-a24d-b8d64724f1fa | -17.73456 | -43.52287 | 2025-08-16 04:34:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9b617f0-f305-31ba-8f62-abb70a61a6f2 | -14.95777 | -56.24014 | 2025-08-16 04:34:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f5ab69d-72d2-35ef-995c-a48783072abc | -14.59758 | -47.92904 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 53af260f-b488-3c23-b766-944048257a97 | -12.81885 | -45.99745 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 65003d29-4f75-3941-bf20-75bf69ac6cda | -9.2042 | -59.63588 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1bcbddeb-d5ce-3769-b0af-bbe2de18d1d5 | -9.16734 | -59.65298 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0b772ab2-e287-3edc-9c9d-2ce54a9e8f38 | -14.601 | -47.92957 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e69ad71-6851-3356-8f0d-a50b5a6a741e | -15.90009 | -48.31635 | 2025-08-16 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dcd1827e-2ca9-35ad-ad9c-a4374857743e | -12.54274 | -46.96053 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| fcdb61c9-9098-35de-a098-8f083bb418a9 | -12.59123 | -46.95527 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 832a5ab2-7e72-32fc-919a-45e253f61670 | -11.35465 | -55.42808 | 2025-08-16 04:34:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fa047bf-106f-3dcb-9c11-d0950612d309 | -8.98396 | -60.51047 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 43ecd361-13ed-37b1-9d90-3878a94dd13d | -12.58597 | -46.94252 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 295897aa-7028-3502-812a-3f56162c80a3 | -13.61654 | -46.90444 | 2025-08-16 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 276845cf-18f0-3276-83c4-9739585977c3 | -12.92628 | -46.96006 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ec612da-a1fa-39eb-90a7-6ff4558fb33b | -12.46267 | -46.98455 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3d615682-64a8-3af5-8a9c-ba155b8f498f | -9.17068 | -59.63537 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69e9a265-17e9-32ef-aded-58cd350e3216 | -14.57938 | -47.91053 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62ee1d66-c961-3df9-8740-b3dd50a36c03 | -12.56827 | -46.95658 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ef3f4d5-04c8-3c5c-9810-1eaa1d664cf9 | -9.15714 | -59.64153 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0e3bbed2-f618-3f80-ba2c-ac529735501a | -14.93204 | -54.70427 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 195a839b-2c4a-30ab-aec9-bf3f8b37ed22 | -12.6005 | -46.91632 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d02ecd07-d71f-35a9-a3b5-0aa0a117430f | -13.11707 | -57.17588 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3fab691-755b-3949-81ac-68f96bca04ec | -13.64798 | -44.20021 | 2025-08-16 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7422295d-cce0-3fb1-926b-bee4d4ed2964 | -14.96379 | -54.73072 | 2025-08-16 04:34:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| f0177d73-8c19-366f-bd95-5fc21f0332c2 | -12.60056 | -46.96452 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a347949-9191-3787-83b3-3213287a28b9 | -12.81155 | -45.99638 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84948088-31cf-3ecd-bd4e-036cccaa0597 | -12.5439 | -46.9528 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 37defd41-6c08-3a74-8e6c-d8a9061bd927 | -12.60343 | -46.94499 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| cc7fa1f5-5638-3495-bd28-b2605d113253 | -8.98098 | -60.52591 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ea16fd34-5319-3479-8e7a-74397e0b5507 | -11.73957 | -44.94538 | 2025-08-16 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5f37e8cf-8f0f-36fc-b4bd-c97452dfc833 | -13.43085 | -56.68083 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 667099b8-65d7-39c3-8cf3-a4fd5fa7cc50 | -17.33794 | -46.56211 | 2025-08-16 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52de46a5-d752-317a-a376-7b0643476bb8 | -9.15541 | -59.68316 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9846d12-4dba-3206-a122-4b7d2c72dd62 | -12.04673 | -45.76512 | 2025-08-16 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a95f96e-99d4-3428-a749-047fbd690035 | -13.43454 | -56.68647 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7e701e1-3445-340d-b06e-f136af4d2627 | -12.782 | -45.94269 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 712ddb56-fc2b-3363-ae27-4ca173a1ca15 | -14.97263 | -54.72662 | 2025-08-16 04:34:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e849d6b-8930-39cb-bbff-60813963f508 | -16.23107 | -51.12339 | 2025-08-16 04:34:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 581e16c0-71c4-3286-b9aa-c08008d35ded | -13.13799 | -57.1691 | 2025-08-16 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c23aa1a8-7bd3-3497-ac01-d0668d84443c | -12.61504 | -46.93881 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 40b68833-108f-3929-9f15-114342d6aa9e | -13.8718 | -45.55645 | 2025-08-16 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32076a49-fdb3-3189-b6a3-1072d348d5b5 | -14.52799 | -48.57971 | 2025-08-16 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bf4abba-6115-378e-b92e-37c34097c977 | -14.48197 | -47.71907 | 2025-08-16 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 153d7e1f-941e-39a5-a61a-fa5a6b8fffd3 | -8.99563 | -60.51787 | 2025-08-16 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a4956b88-48f4-3aff-a085-8c146f2cc655 | -12.77467 | -45.94168 | 2025-08-16 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a50dfac0-b53e-3c50-a19a-15ba624cf8fd | -17.21188 | -49.5956 | 2025-08-16 04:34:00 | NOAA-20 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9495d222-0845-32e5-b975-654b07d6ff79 | -12.45861 | -46.98791 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 824c13c3-e7e3-3856-b835-a2e03d69a1fb | -12.5918 | -46.92705 | 2025-08-16 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |


[Clique aqui para ver as próximas entradas](README46.md)
