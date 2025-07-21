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
| 14715ea2-b91e-31fc-825d-bfe42ceec1c2 | -6.65079 | -44.16119 | 2025-07-21 03:55:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c994d7d-0fb3-314c-b592-e9fde313706a | -5.88919 | -45.21692 | 2025-07-21 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c1956c19-8f44-3920-9ae1-7a0ccd22d882 | -6.20255 | -44.38657 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dab87c81-1a0a-350b-b5d8-45c00b942aa7 | -7.93594 | -43.94467 | 2025-07-21 03:55:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c09645f-2e37-34f6-8221-d037d0ec25b7 | -6.19686 | -44.39383 | 2025-07-21 03:55:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57450670-1cf5-37b9-afe3-2ea7467fc372 | -8.87458 | -39.74679 | 2025-07-21 03:55:00 | NPP-375D | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| eec2c590-c4a1-3661-8542-46698ada86fe | -7.19555 | -43.02449 | 2025-07-21 03:55:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0e39fb93-ea06-3450-8ed4-937bef2a929b | -5.04194 | -37.77312 | 2025-07-21 03:55:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49896be5-c1be-38fa-af1e-315f05de443c | -6.50138 | -43.51936 | 2025-07-21 03:55:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4adda53-9568-35c8-aeb6-434732d45789 | -6.78677 | -47.16348 | 2025-07-21 03:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b24deb04-351b-3ec0-a278-883346ba8274 | -7.27234 | -44.2677 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb8b9d4e-7b43-3fa0-8375-0b0acafb6590 | -6.68173 | -43.00946 | 2025-07-21 03:55:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0faeef6e-cb07-3d8c-9951-278827a61edf | -7.25622 | -44.28534 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1724b38-47df-3ab8-9cf2-06018fd07b61 | -3.03765 | -47.86117 | 2025-07-21 03:55:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c90a0970-2dc1-38bc-92cb-e8fe1f02dffe | -7.94541 | -43.98001 | 2025-07-21 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a5f7ffb-2b41-399f-821a-c77159357b6c | -7.75667 | -42.15923 | 2025-07-21 03:55:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 75dfa209-dc0b-34fa-aaac-3d9618be0c9d | -7.05965 | -43.51507 | 2025-07-21 03:55:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef52d06f-d269-3032-b981-6fc8964a78c8 | -11.50007 | -48.07958 | 2025-07-21 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b50297c9-bb1d-3e4c-ba20-b541d972a856 | -8.26833 | -46.0694 | 2025-07-21 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cda3e2c-a332-3cb9-a6e4-cbce9fda5f71 | -12.36732 | -46.43293 | 2025-07-21 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc849555-157a-3d6a-97c9-f20aec616c6d | -10.68906 | -46.77361 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6110be60-0928-38fa-8f1c-7fa95ecd529c | -11.77753 | -46.46409 | 2025-07-21 03:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b52a8cfa-07a2-3b56-a65c-d0c08b68b662 | -15.61409 | -45.90198 | 2025-07-21 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c76e489-1795-3c78-9eac-c12b61faf676 | -10.15588 | -49.66336 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a28e73ba-c40c-388b-83cc-6981eecdb80f | -15.61478 | -45.89813 | 2025-07-21 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f890818a-4669-3ad6-9a0a-027957c32d14 | -12.15593 | -44.79328 | 2025-07-21 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d080229-9bf5-3018-b10e-dcbcdfee1bee | -10.13367 | -49.65448 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4121d9c6-1eb1-3b57-867a-65bfbad56d14 | -10.68935 | -46.77552 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0dad978f-deca-3cbb-ae47-5fd4844c19ca | -10.13206 | -49.6627 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d928621d-d67e-3674-aea4-c2a77505e429 | -10.69028 | -46.77055 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd0edb22-0cc3-35fc-81f9-a7302ee2555b | -14.77806 | -47.99074 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1a542063-7b00-3a9f-a9dd-b103482e3a0d | -10.67961 | -46.77182 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37a5a332-1610-336a-a9e3-17f4bb240311 | -8.92045 | -47.36252 | 2025-07-21 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7cf6d77-808e-31cd-a677-a01296c789f2 | -14.77394 | -47.98777 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 994e314b-ab46-3c63-89de-ef29f5470440 | -14.74337 | -48.28179 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2da766b4-d9b5-38ad-8d00-93cf3cec8d32 | -10.64846 | -44.48203 | 2025-07-21 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6bf99c93-242d-361f-b9ed-6bd8fae6ded4 | -10.13923 | -49.65689 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a2f4fa3-1891-31e2-942b-f40123803995 | -14.77706 | -47.99586 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 71cdaeb9-d561-3cd5-8257-fe7f07a3b845 | -10.13192 | -49.66391 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4395f2fa-2106-3776-9df2-f8747a62d324 | -10.1327 | -49.65979 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f757513-bac6-3104-8ad3-e8f50030072d | -10.15572 | -49.66462 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c478db4-3dcc-3990-bf4e-fbb402ca5e3b | -12.46524 | -46.92223 | 2025-07-21 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88f16c35-d459-31a0-878e-b6821f0f799a | -15.1141 | -43.86031 | 2025-07-21 03:57:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8f838a8-92d1-306e-9161-8459ece164f8 | -10.68433 | -46.77271 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 95f9e37a-1f24-3d5f-9196-fa53f0d970e0 | -10.14517 | -49.65687 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25a72658-e975-3a66-85b5-2b62ca6c3bbc | -11.77837 | -46.45947 | 2025-07-21 03:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58e3bd34-c186-3d2c-99c9-0bcd5e78e7ca | -12.37641 | -46.42696 | 2025-07-21 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70a952af-5056-3862-bb84-0d6c4418fac8 | -12.37198 | -46.42583 | 2025-07-21 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c9c7d76-a113-3f58-a007-8ae0270bcc47 | -12.48337 | -45.88118 | 2025-07-21 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b45e863-569f-370b-a24d-1618c862c541 | -12.46986 | -46.92315 | 2025-07-21 03:57:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a84766be-9f35-31ff-a218-9162bb6797e5 | -10.1442 | -49.66225 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 19e9f2dd-699e-3b87-b08a-79952119595f | -10.37969 | -49.92962 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc4f5e18-d2ac-36e6-8fe0-867cbe696dca | -14.20843 | -43.95829 | 2025-07-21 03:57:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92839b6e-2126-3cb5-9ba6-bbb0fce31080 | -10.69378 | -46.77455 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eda0c49b-3dd0-33cb-adcc-ba3e31331f66 | -11.96456 | -47.02927 | 2025-07-21 03:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eee54942-7ee5-3c2e-aa41-789801015104 | -11.7887 | -47.55065 | 2025-07-21 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ae07abe2-0523-3f23-968e-1bd961347abd | -10.15012 | -49.6622 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eab3ff6e-4f63-3af1-9fe8-e417581f842f | -15.61269 | -45.9011 | 2025-07-21 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2ee9db5-7c0e-3bca-b03f-e1ecfd18798e | -14.67766 | -42.48418 | 2025-07-21 03:57:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4e600ee1-91a7-3434-aacb-a9b80d78c775 | -10.66359 | -46.77935 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80777ba5-9304-3e0f-9173-115777d4fd7d | -13.09223 | -50.57286 | 2025-07-21 03:57:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1018e5a9-2d6b-3d6b-8111-2c0d2b30c557 | -14.77292 | -47.99316 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03500c0f-c2be-3f98-9f05-37ed655c0eee | -11.78279 | -47.55523 | 2025-07-21 03:57:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bce1ed75-bc3b-3331-9f9a-d082899b0000 | -11.38566 | -47.97528 | 2025-07-21 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a6dde68-68b9-38f4-9b85-bfcf6d8b571f | -12.47929 | -45.87365 | 2025-07-21 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19c3ca0d-01cb-369b-84a1-2642a4977a93 | -10.13942 | -49.65569 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c2dd2aad-bc8b-3871-a48c-5052e07af535 | -10.68555 | -46.76967 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 416a9fc0-a27b-34e6-93cc-0f61a75a578d | -14.76441 | -47.98587 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cd730e1-d75d-3e4e-bab4-26dbefca0365 | -9.63409 | -40.60304 | 2025-07-21 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a9d99891-3988-31ac-bddd-8af24e379d77 | -16.08035 | -42.01755 | 2025-07-21 03:57:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 318d8ffe-4979-3869-942e-19a3caf7f868 | -9.59388 | -48.54401 | 2025-07-21 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b089a9b-9b9c-357f-bce6-408f03b7c356 | -10.37887 | -49.93386 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 65998cd3-0df9-3e38-a6d2-16ba38c1a2e6 | -8.91537 | -47.3616 | 2025-07-21 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 713842c6-ae67-3246-99b9-0ce76cc1b6db | -10.84451 | -47.15631 | 2025-07-21 03:57:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f05e3518-54e2-3ba2-a926-640982a2b2ba | -14.78079 | -48.28379 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 724ff4d7-c4ef-3003-96d2-298c3c049903 | -12.38407 | -45.88193 | 2025-07-21 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e550e481-2c36-3751-9cc0-ffde2d02ec54 | -10.66924 | -46.77512 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 25eecc59-18af-3e2e-be5e-ed282c15e5e0 | -11.96081 | -47.02328 | 2025-07-21 03:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 36f718d6-f57d-31bb-9a1c-f7ebb3bdcbea | -9.63808 | -40.59993 | 2025-07-21 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4a363381-751c-3e71-9f9d-cacb37a08546 | -10.13348 | -49.65566 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fc2fb8a-d636-3b8b-a043-18507bf2a355 | -12.47982 | -45.87621 | 2025-07-21 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 876c1c23-cac0-335f-9018-05d9d021ce1c | -10.09028 | -46.58671 | 2025-07-21 03:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a8a378f1-b8c5-329a-90e5-30227098a54e | -13.63589 | -45.5319 | 2025-07-21 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a683eaa4-1a9b-3acc-8a1f-01e192f77149 | -10.67517 | -46.7729 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1aa146f-8bf6-3fe5-95d8-bb5200cc153c | -9.59473 | -48.54372 | 2025-07-21 03:57:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa846f94-7f5d-36d4-84a2-841ca73e9a1f | -10.15073 | -49.6593 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df45d688-9b89-3013-b271-944ee3874e18 | -11.60826 | -44.23544 | 2025-07-21 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c4cc7a35-fa79-3d77-8446-0cd595832e96 | -15.61751 | -45.89801 | 2025-07-21 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44a6115d-1dd8-3c39-9b09-aa8878a3cb71 | -10.14436 | -49.66103 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0f9b838-5135-3ad1-a439-0c5d5d86ced1 | -14.78578 | -48.28405 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7589799-32fb-3a0c-a965-01522b8b4b2e | -10.14498 | -49.6581 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fce421ee-edeb-36c5-906b-0a94f6234df5 | -14.77768 | -47.99409 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a5a9910-4848-34d4-be01-dbc202cb198a | -12.36555 | -46.43591 | 2025-07-21 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f24ae34-4e8a-35b6-98be-786e0b98343b | -13.48799 | -45.50583 | 2025-07-21 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c93f1cf6-d829-3a93-b31c-d676c3d0ec05 | -12.96148 | -40.66981 | 2025-07-21 03:57:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| bdfd0cf1-fc74-327a-b416-4ef08c613e4f | -13.0914 | -50.57706 | 2025-07-21 03:57:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c5e0cb2-8a5b-32ec-8d42-81736448ad6e | -10.64784 | -44.48564 | 2025-07-21 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ebb6e977-1b32-379d-aaf9-d815aac013ef | -14.76921 | -47.98663 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba143b07-eddd-3528-baa0-72b0d72df117 | -9.55706 | -40.60207 | 2025-07-21 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3f454009-6cfa-3d44-a707-970a967d2af1 | -14.7654 | -47.98067 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README5.md)
