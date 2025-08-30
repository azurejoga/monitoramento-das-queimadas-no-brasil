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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 311e1c33-0e72-3bc5-bf07-5a09a3dac18e | -11.85024 | -46.43784 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47144317-c901-3bd7-aa46-8442ff72a49c | -13.51117 | -46.94952 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a1b920a-dc64-325e-a3aa-dfb6f60f81de | -13.51777 | -46.95066 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d85c8da9-6cc0-3bea-8db8-fd7f815bb16b | -10.7951 | -49.58573 | 2025-08-30 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0321fb9f-6dfd-3db2-9c81-624eb2ebf02e | -13.5918 | -46.89039 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7bbf4378-5fc7-33b7-a140-94dc2083c9c6 | -9.17606 | -59.57655 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d0c27e08-bc22-3aac-8b76-20d57f51c45b | -11.87288 | -46.38027 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3fbf91f4-dfa5-3e04-9c59-aae0a9424971 | -14.00708 | -44.59835 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45cfb593-1ac7-353b-a949-422d5c835e5e | -11.72338 | -51.75664 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d77e8b69-b890-3cac-8a8d-4a4c92768436 | -13.40697 | -46.83461 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d22caca-c165-3e5a-9dbf-3cf243e8fdf8 | -10.73159 | -47.01095 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6c83a6d-41b0-3b03-acc1-b76657035c2a | -14.56371 | -51.99866 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92f1ee39-c36b-3281-bdb5-b2ebe550b05f | -14.02125 | -44.54991 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 62fdcbcf-f9dc-399e-bfec-51755f5cc3ea | -12.70967 | -48.14542 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1299092a-708f-37c3-ab28-029b16a24a00 | -11.83697 | -46.45736 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bfe9fc70-9ce8-3f60-8f01-e14e865c254a | -10.94131 | -46.84728 | 2025-08-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4cb5306-14a1-3004-82d5-c01368c3601d | -11.33929 | -43.28307 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32bdc883-a07b-3a43-a644-80f75571a7f8 | -12.92337 | -46.36075 | 2025-08-30 04:21:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49a68cda-3c58-3386-b885-6db27dcbbbcb | -12.40515 | -46.47829 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb8a996-a233-36cc-8490-1b08f1488793 | -16.08039 | -43.61969 | 2025-08-30 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9d913b5-72cf-3c2e-ad3d-bba22ca4439e | -13.62417 | -48.25128 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ac70838d-253a-3971-9947-00bb5878450c | -9.70949 | -49.47268 | 2025-08-30 04:21:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 241f42fb-7e92-3b02-a465-ea88ab286147 | -11.30441 | -43.64432 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 771be0bd-f67d-391c-83f9-f993bc060463 | -10.38422 | -57.83218 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3cedb2f7-ffe2-3338-aec8-90c5363b1a3d | -14.50687 | -52.99181 | 2025-08-30 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 720aab5e-9319-3d36-a653-5c5b56ccb395 | -11.8773 | -46.37377 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3887cd5-5cb4-3b35-b8fa-9bb4a7760c40 | -13.63242 | -48.17994 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34b96c97-b876-3ae7-8323-c8907c3ad6aa | -13.36766 | -46.99546 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| be119090-3146-3f06-a1ce-1a42a747411c | -13.73457 | -45.53153 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7d56c59-7261-3114-a222-e0a834f94c43 | -14.25941 | -48.05799 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf8df536-bf94-3a8e-bf84-1e7cbe3be4bb | -13.57191 | -46.90887 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d9155e3-8a7b-3594-8fc6-6d3e418ed505 | -13.5608 | -46.93617 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1add4422-40da-36ce-be0e-70a25d3be2ff | -12.69543 | -48.14694 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b587b502-d8cd-3759-92bc-38a9063ca72d | -15.17935 | -48.02901 | 2025-08-30 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00f2ac70-31e7-35d6-b0ee-e4a9ef387010 | -9.95831 | -46.35295 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f9254df-26a1-35f3-b435-1f1ace0717dc | -13.3921 | -47.01392 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c33144ee-e657-3a23-bb4c-ad08423feab4 | -11.34018 | -43.52213 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 04e78c36-ce51-31ba-af13-31a490275065 | -13.5147 | -46.84134 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 736b435c-6e7b-3f9c-a347-e9692f5db90a | -11.85634 | -46.3992 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4d261d3b-84b1-3c37-b02f-9dd3f16c5ca7 | -11.86847 | -46.38676 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67c9d2a4-01d3-3722-a0a1-24e3eb70ed98 | -14.02412 | -44.55424 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fa376989-bfe3-338e-b5dd-e83ef4328f19 | -12.9442 | -46.1404 | 2025-08-30 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1c862ac-9dcb-3e18-9466-70ed177f02b5 | -9.50005 | -45.39645 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34af16a5-0bd6-3431-b2dc-5bec7de17af5 | -11.34367 | -43.59487 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eea6a011-ab3c-3ac9-b0a2-1ebe176d7a8f | -14.8378 | -46.77664 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2228cb1b-b345-3183-ae75-97b26671f021 | -13.37047 | -46.97771 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 671c63fe-4cd7-357c-8f55-5356ed295c9a | -11.84805 | -46.43024 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be5c0832-bca7-3c62-b54f-aa5c966442c9 | -13.38386 | -47.00161 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96b7c3d0-263c-3401-92c2-99ba6551a09d | -9.59139 | -45.74588 | 2025-08-30 04:21:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84bc7cbc-62ad-3ecc-bc13-f3905d56feb2 | -13.50513 | -46.83616 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0758ae5-a3d8-3ddb-9eb3-493d6db3fb1d | -13.40972 | -46.83867 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2dc5aadd-1967-38ba-abab-3d14c74f8bfe | -13.6787 | -46.87946 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffebe66b-1427-3921-b098-473ba58708ff | -11.31248 | -43.63773 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fb97e6b-6ac8-3b01-bd83-f32072cd9efe | -15.16196 | -52.33302 | 2025-08-30 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 518d2710-70bd-366f-9274-19961f3e25cc | -13.36929 | -47.00669 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 93d3081c-b54c-39d3-acca-e2a39154bbe7 | -13.68414 | -46.90945 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8cdf8940-00e6-386f-a144-16235e6807d9 | -13.5802 | -46.89938 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42229a70-8162-3147-8b1b-fa130f7a4ed3 | -9.44706 | -47.63939 | 2025-08-30 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ad4f184a-a904-301f-adaa-6e4c2084ac25 | -13.57022 | -46.91952 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dcd4978-5ed7-3fe5-b1f9-5d28884c7000 | -11.06742 | -52.04337 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c95bd5-c3f1-33d5-9f03-7bcef15468ff | -10.99572 | -46.8489 | 2025-08-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c0e5a92-db69-38d3-9df8-8b39809392c4 | -11.32862 | -43.60049 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 062c7c44-6cea-3786-b9ae-e31dc8f17905 | -12.82742 | -48.09157 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa513fb1-0cbb-36ff-9971-b09327889b5c | -9.69436 | -48.31211 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d488f6c-deda-35ea-9c3d-f8094f5dcb55 | -9.11508 | -46.04823 | 2025-08-30 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb67aaf7-0c4b-3f06-8d3c-4c970e219602 | -11.29861 | -43.63553 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20478a49-15d4-3886-b311-7c5e4241cd50 | -10.53582 | -56.38603 | 2025-08-30 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cc58ec53-856d-3817-a30c-be5f24d98abf | -13.66656 | -46.8704 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3ef292c-a824-34d5-996d-1cfca25ae56c | -13.66536 | -46.92096 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6752c423-4eb2-3900-b9f3-f40dd2962f82 | -13.4064 | -47.03086 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6151567b-e0b3-352b-9fe2-c2d94c50d5de | -8.51733 | -54.71723 | 2025-08-30 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a63ae26f-500f-3d01-993f-8d73f5a29a0c | -12.8268 | -48.09536 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db0a6d1d-5698-3a55-80ba-c533193f9bad | -14.23352 | -48.06861 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32dac943-690a-38fb-b484-c6aad9f74f96 | -12.05169 | -45.58149 | 2025-08-30 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f44d9ab7-79c1-38b4-bc1d-91a924609acc | -11.15307 | -47.14232 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4b9408e1-1d17-39ce-924a-480093ffee83 | -11.83809 | -46.45032 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2106bca1-9f3e-328a-a840-89cadb8efbc3 | -11.84424 | -46.39 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 41501341-536b-32ec-9d8c-edf0938d536c | -13.49465 | -46.83805 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a631e61-8ef6-3d1d-85ad-704e502f0d01 | -11.83136 | -46.79274 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e46a58eb-3419-32bf-9973-b6e2044bc829 | -15.11641 | -47.1255 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 400e11a8-b95b-3247-8853-f3c29d846061 | -14.00871 | -44.56358 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b48e1605-c457-3126-a7f4-3f51856bac4c | -9.75365 | -48.69789 | 2025-08-30 04:21:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15ad432d-3d58-36ab-b5e6-c131c37ddc4e | -13.40779 | -46.95804 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| abc6a547-ee16-3c64-ab34-dfc0f36379d6 | -14.33972 | -51.89214 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7ce75f1-d07b-3214-9e6b-75136995e19a | -11.89068 | -46.71896 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c70039c8-e5a2-3651-80d3-da123d183300 | -11.84132 | -46.79435 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e708f51-5bc7-3109-b6b9-a1674a195f11 | -14.31884 | -51.86958 | 2025-08-30 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c366c2c-2d9b-3f07-a35a-302e3710c571 | -9.17749 | -59.56945 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 320cdad3-c4c5-37a2-91a4-59f6385936c7 | -15.02402 | -49.24557 | 2025-08-30 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 332133a3-98c3-3eeb-8fbc-0448455319ca | -13.46019 | -46.97034 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43af141e-522e-3e42-b037-dc637ed42ad9 | -11.29907 | -43.58396 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7a4dd89-5aad-380b-9387-96e4a8bbb7e9 | -14.83676 | -46.76191 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51d559f2-0d78-3329-8aaa-e53dc9848f2f | -11.41194 | -46.90593 | 2025-08-30 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37a6a8bd-720a-3446-ae5c-944cee6e42b1 | -11.93668 | -46.68708 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 426e5003-ef23-3eed-bd05-a0d11bce2140 | -11.31362 | -43.62995 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9dd8f842-3d06-382f-a1d6-2c179c94c2aa | -11.90568 | -46.71104 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01c5c84e-ef7c-307e-8502-0afd90cdb7ee | -14.37817 | -47.84856 | 2025-08-30 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0026d01-3a77-343d-be48-dbf5709bff9f | -11.32633 | -43.61596 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74fff078-d021-3dba-9aeb-1cf55fa26e50 | -12.82282 | -48.18414 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aea46f60-2e77-3f2b-a21d-5b16a237af86 | -10.46287 | -57.94474 | 2025-08-30 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README30.md)
