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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c392238f-9bf8-3eb4-a82b-67bca6ef535e | -12.7126 | -48.47966 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32b57e97-a348-3914-8a87-49d175dd72a7 | -8.52262 | -54.90048 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1051c2c-f7f6-3fb3-93e3-a5150cabf4fa | -8.0666 | -48.53802 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eed51cb5-6bfb-3c99-b063-beb56fb84656 | -15.03014 | -47.03906 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 185b9737-73b8-3409-b9b4-135b651adc9d | -12.55998 | -47.84462 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e8ce4e6-2a8c-3df4-904f-7eced4d038f0 | -13.52322 | -46.23857 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1106b188-190c-3cdf-b9c3-8a086b5ae589 | -6.87435 | -56.42317 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7dcd5fc-3f9e-3e31-8bb5-a2711620c28d | -11.90903 | -47.34932 | 2026-08-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e469b763-2fa8-369c-95b3-88aba75f0404 | -8.07095 | -48.53437 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fdde922b-1df3-3df7-a4b5-418712f5e19e | -11.50406 | -46.6031 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdcf5ff6-8996-3d4e-9252-2b3f51190e0c | -6.10189 | -57.73766 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c7ff7a61-cafc-3258-bfab-6360d1cbbf1a | -11.97508 | -46.4412 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e95e5659-6f43-3b79-a32a-419576307e7a | -12.75606 | -48.43074 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 55e1e084-3416-30ae-9356-88a13bb47e9e | -11.28159 | -45.81089 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9573e379-832e-3a29-a036-37e2f059f046 | -7.38519 | -55.48078 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 46a7e80d-eda2-3e00-90de-f8fc39bc008d | -13.44417 | -43.8404 | 2026-08-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 29911ff6-096b-3be2-863d-7d5172160b69 | -11.50349 | -46.60667 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfb382b9-11eb-3bc0-a941-642aa82e6328 | -14.48362 | -45.67302 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb64c32b-f493-3b18-9188-bea64bb89b04 | -12.70897 | -48.52342 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c9e5ddd8-8b10-397b-a96c-ed8c723e0e22 | -11.23404 | -54.01919 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 200b2df4-91f2-32d1-9aaf-dd5037ef72d1 | -10.94021 | -57.15455 | 2026-08-17 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d3c8da69-6d0b-3a8a-b806-f8f1ed8e78dc | -14.44522 | -51.83422 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 047aaac4-562e-3856-ae1c-180d67dbbcef | -10.38004 | -48.26948 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e9eb76e0-28bb-3e11-9356-5697d8e75adc | -11.71123 | -54.61422 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b73d0ddd-79a3-3385-85ac-df34f89ecf3f | -8.58302 | -54.69181 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 840b2a10-7afc-3e29-b02f-632bd8d0cd0a | -13.65606 | -46.23803 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3113fbd4-ff39-359d-b5dc-be0a3447779f | -15.11186 | -48.7196 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02fe6bff-1994-37d9-903a-4828735cb817 | -11.72249 | -54.61013 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47c8101c-ba24-3b68-b5f3-047f30fe9dba | -14.18797 | -53.0705 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 13ad76de-7dad-39c2-8a56-447fe585f6cb | -11.71008 | -54.62033 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0efd951c-ae4c-3ecc-aada-53fbbc3f18e3 | -13.5183 | -46.29205 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eee93e2-ff09-38be-a681-80e3bb40a6cd | -12.53113 | -47.89324 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d9a7062-1225-35fb-81c4-b6501faf645b | -12.04865 | -46.44984 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9079cc2-1737-3169-a155-af05eae17b0b | -10.47076 | -45.1427 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9fc4889-1d39-35b1-8724-ef48d75b8898 | -9.47108 | -51.61653 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19382fb7-dbee-33e1-b4c9-ae7da7b159cc | -7.39596 | -55.48977 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ba967968-cbd1-3cee-90b6-685fbe23517f | -11.32684 | -47.01268 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5046950d-62f3-3497-930f-f2994e3ca50d | -13.51609 | -46.28445 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b4fe208c-bad6-3a70-b1f7-bce0dbca37f1 | -14.87763 | -46.64488 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 24e23dc0-9bbf-3f22-9947-1820846e1c7d | -8.71986 | -45.29736 | 2026-08-17 04:21:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a439c089-7945-3b21-b8fc-e92550e9ecc6 | -8.61422 | -54.71729 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7239a989-ad30-346f-b9ef-a213ecc59e9d | -12.02493 | -46.428 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c884dd04-8f30-39c4-acd3-431a7d0c886f | -9.75742 | -47.23055 | 2026-08-17 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e4d086-fb5a-3701-8658-53cadc41254b | -7.36272 | -55.50623 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| edead2ea-e121-3ec4-9fb6-9b0bc3699adb | -15.16074 | -48.61502 | 2026-08-17 04:21:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df1f0742-38fb-39a5-8888-4c56ee4f20e6 | -11.50681 | -46.60718 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bc1f9d2-6964-38c9-97ea-f0910944c544 | -11.8306 | -51.77538 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db55c958-7c94-3b40-9d26-df965e009946 | -11.39484 | -46.41188 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54ecfc44-42d8-3152-8ded-f4c15726f9f8 | -9.49237 | -51.60807 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0e27d2a-f3f1-344e-a07f-ccc02afb4daa | -11.13721 | -46.49252 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a5d76f9-7d40-39ab-95a7-1a49ae51198e | -7.0706 | -56.65384 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23f0d8cc-c899-3911-9238-986ecb8d666d | -11.72472 | -54.59827 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7344088c-71ff-38e1-8398-eba25c87fa4f | -13.77309 | -50.24138 | 2026-08-17 04:21:00 | NOAA-21 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfa460f0-552e-3758-80bd-53000fe61046 | -11.31641 | -45.87032 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 591d1a8e-0a42-3679-b3d8-b22e47b69568 | -12.00167 | -46.46772 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dfda8ec1-0a1c-347d-a7b1-4cfd89e887dd | -14.49919 | -45.6829 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ffc60919-b9aa-382c-822f-af2c07562446 | -11.21204 | -54.01871 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ba00ce0-ccbf-3973-8bce-56a33d0ec5df | -10.5126 | -50.01498 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d75237bc-b6f7-3c6f-88c3-21bb05b82003 | -12.71027 | -48.51556 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 976399a7-454e-388c-8014-366e4c2a644d | -11.32407 | -46.21265 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60c0475c-1ac9-3da1-a7f0-3acaf5ef3831 | -12.68372 | -48.43935 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f3f520f-cf0a-3cc1-9411-1757abe1cdf9 | -14.49974 | -45.67929 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bb8d8d0-df58-32a6-aae7-5e293c7901e6 | -12.66811 | -48.51224 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e372a962-41fc-3325-9889-790c716e65d8 | -11.99393 | -46.4737 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3491eec1-0db2-38aa-85ce-fca7c437e1d1 | -15.60555 | -47.869 | 2026-08-17 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd014306-d140-3cee-a224-ffd8994c9236 | -11.83897 | -51.77691 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dd4aa89b-6a82-3f6c-9d91-254e6f7da99d | -12.69705 | -48.50939 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9873d4e7-521e-3b96-8755-cfb5b96bac33 | -14.47918 | -45.6797 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f1d18d59-7ca8-32e6-b281-ab5e98076727 | -13.50394 | -46.25351 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8420bc67-467d-3fb0-a2a0-76c0f39b8a00 | -7.3917 | -55.48059 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 162555dd-1856-3b4c-9b27-2747e85b38dc | -11.13722 | -49.04296 | 2026-08-17 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd704a35-43b4-3528-92ed-a5caa6ddf31c | -9.30201 | -56.80869 | 2026-08-17 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 916de0e5-4399-391b-90e6-b8d0c3b182fe | -11.73429 | -54.57514 | 2026-08-17 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 212d5749-b45d-3eb2-8b97-628eca82e827 | -14.73557 | -47.96836 | 2026-08-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de659d73-f03e-3864-8bbb-13af0005361a | -10.50319 | -50.40592 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e67734ef-283b-3215-8ee8-7f3fb6240d96 | -14.44118 | -51.83355 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b37338d1-795a-37f2-bd42-012f17032348 | -14.47639 | -45.67556 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 6ab0d071-45fc-3fb4-9fec-1159b9f66a88 | -8.52134 | -54.90747 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16bf162a-99f8-32e0-b304-910abf3e9879 | -14.89361 | -46.62934 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d333753e-bd5e-3198-a5d7-a41f90d861c9 | -8.06334 | -48.53371 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7b3dcce0-b50d-309b-85bc-a86d18695113 | -12.18316 | -45.14443 | 2026-08-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f964a925-b0a0-39e3-8c40-71fe692a803e | -12.70051 | -48.50998 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| bf0bbb1a-19f0-37f6-af15-8c9c0c03d56d | -12.70833 | -48.52736 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 75c34726-8d7e-3493-8af9-1a1688325994 | -6.10865 | -57.73888 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 119d4acb-8612-377c-91fc-e87044e526e2 | -14.30858 | -47.19341 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7941e674-6961-3c87-8279-e7647e5f103b | -12.23309 | -47.04414 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f1cefce-10ad-344c-ae43-5443eef447df | -14.93125 | -46.60619 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d11fa349-e9d3-3478-9d39-6fee61409563 | -12.54738 | -47.85782 | 2026-08-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86a8a6ed-df60-3ec5-a42d-a0de622c2c29 | -15.72537 | -45.97039 | 2026-08-17 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41eded43-467e-3fa6-80ef-cad24d07e31d | -11.72923 | -54.57423 | 2026-08-17 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaa6190b-b8bc-3b59-ab21-48f83673ddfd | -10.38355 | -48.27007 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e220f909-c601-3d26-8288-37afc8c4ce2c | -12.01268 | -46.50562 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 30ffc547-303b-30af-a0f2-2a2414701444 | -14.49362 | -45.67461 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de0701c4-fe8f-3a46-9c22-06a812dba7d4 | -11.9124 | -47.34986 | 2026-08-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c4020c3-e918-3b6f-b3b7-fdb9d4f4dd36 | -14.27878 | -53.11919 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3609cd91-6f82-34d8-bcd3-a84aa493ff88 | -7.39018 | -55.48875 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3e9227fc-9429-3885-9b66-eb8c142db700 | -11.83478 | -51.77614 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e84c6b97-1d62-3e57-8bd0-e02935d9bcbd | -14.46056 | -51.84571 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35065023-6f9b-3e8c-8c08-ec08905ad44e | -8.63649 | -54.71722 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 10974a47-f1c2-3b34-a70c-c1a227ae2d12 | -11.13383 | -46.51376 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README21.md)
