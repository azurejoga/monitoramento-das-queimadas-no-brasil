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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 891ce0b0-06bf-3534-95aa-acb4aad0262d | -11.78733 | -50.39727 | 2026-07-24 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f38fd24c-fa04-3ee4-87df-fbea28f77b42 | -12.16699 | -59.76088 | 2026-07-24 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c85af5c2-e452-34ff-a827-c2f330e6c05e | -11.59816 | -58.51298 | 2026-07-24 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a130666-a548-3106-9344-78500128fdb9 | -9.17181 | -58.32662 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae626301-16c7-388d-a015-0f08b586cd11 | -12.66729 | -48.20103 | 2026-07-24 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d81d1266-da0d-34f7-89a9-25bf3b3cd475 | -11.62038 | -50.14669 | 2026-07-24 05:12:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9d303b-d263-374b-b676-303bf854340e | -9.15858 | -58.32453 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 662b5397-b757-36c3-87b5-9d45a7237334 | -9.16795 | -58.32958 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9078575-939d-360a-a167-8d02870d85e5 | -13.43583 | -51.53182 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3d5449e4-5c6e-3c4e-a1ef-d439910ce833 | -11.849 | -60.71199 | 2026-07-24 05:12:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 526a2a72-bc11-3b2f-be26-e71f75218d42 | -11.01838 | -54.31189 | 2026-07-24 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5fa36e2-5cc8-35d0-8cae-0f76fcfa80cc | -13.4185 | -51.55537 | 2026-07-24 05:12:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e314af6a-1838-3863-a422-a8a09e780207 | -8.71609 | -54.54312 | 2026-07-24 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45fee334-dac6-3315-9193-63398785c655 | -11.36769 | -55.43959 | 2026-07-24 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 544f02ee-7d6b-386e-8798-cfb1acd0f287 | -12.45189 | -49.59021 | 2026-07-24 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cd26903-17ea-324f-ab81-6c393085045d | -9.16134 | -58.32854 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1af64c5-06b2-374c-8bed-dccf774832d8 | -9.01405 | -64.14647 | 2026-07-24 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 300162c4-9ee0-3c64-af63-fa0c618b2fae | -9.00972 | -64.14571 | 2026-07-24 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b21ad7aa-2329-3df9-a771-0e52ce0fd8aa | -8.71546 | -54.5474 | 2026-07-24 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 564db80c-8b0a-30c6-a357-b9ab24aea076 | -12.66149 | -48.20011 | 2026-07-24 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 093e8a4b-b78c-3584-b6ec-d37d269bf4d0 | -9.13566 | -61.06425 | 2026-07-24 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 224c7e8f-17ca-311d-8940-09f6c5a8bed5 | -9.16465 | -58.32906 | 2026-07-24 05:12:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdd14f26-877c-3b8c-a54f-86a97c82c042 | -10.02364 | -65.05106 | 2026-07-24 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1c72ba2b-3a6c-33aa-85de-602994f68ebe | -10.02814 | -65.05191 | 2026-07-24 05:12:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 21e3a745-ffb5-3b90-b9d7-c220fb01e0e1 | -17.77617 | -49.13262 | 2026-07-24 05:14:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 57565239-82e4-3770-825d-b4cdebcd0bb5 | -13.31529 | -54.33399 | 2026-07-24 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a19fce9-2a10-3ec2-b6d5-4d790b4a837f | -13.72848 | -52.0213 | 2026-07-24 05:14:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be0920da-5856-3c38-b2da-f74b61cbafe3 | -19.07056 | -46.78053 | 2026-07-24 05:14:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58dfc2a6-e936-399a-a25d-cec8100a4760 | -18.79878 | -53.13766 | 2026-07-24 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 178b257e-6135-311e-8e22-0eeec86f7476 | -18.80278 | -53.14298 | 2026-07-24 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec39a30e-1998-3a38-a2ec-c69117265f05 | -15.56942 | -53.87784 | 2026-07-24 05:14:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4dd5989-0ee0-3593-bc20-d7ec13c7735d | -18.5482 | -56.82601 | 2026-07-24 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9e2cd3b4-11a7-302e-ab7b-a9b425542702 | -18.54518 | -56.82106 | 2026-07-24 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| deb629a0-8ea4-38bc-9dcb-160a8afd00e0 | -17.77591 | -49.12958 | 2026-07-24 05:14:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3bdd71e7-3b60-3a50-8682-dfa1630d9202 | -13.7279 | -52.02598 | 2026-07-24 05:14:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cf61907-35df-3006-b84a-536068b5b894 | -14.38232 | -50.33334 | 2026-07-24 05:14:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 236cfae6-f032-3f40-89fe-0fccd181a17e | -17.63227 | -51.85825 | 2026-07-24 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 810dbcd5-9f75-3e6f-bf83-b33323a7e466 | -12.72151 | -59.9931 | 2026-07-24 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db2ef4d1-4bd8-3712-a2e0-1e5c714fc718 | -12.71816 | -59.99253 | 2026-07-24 05:14:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41b90bad-19cd-39c2-aafa-8bff10ad6826 | -17.77661 | -49.12834 | 2026-07-24 05:14:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 072f5965-9611-3c04-bc5f-2a444b3b24b2 | -18.54458 | -56.82545 | 2026-07-24 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a028289a-9bb7-3413-aad1-e04a56a818ad | -18.8079 | -53.13869 | 2026-07-24 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f331e881-2d5e-3b2a-9f7c-db3872e4f3b4 | -18.79822 | -53.14241 | 2026-07-24 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df7ec72b-c530-372a-ab8b-ec3b6ad9ba16 | -13.3312 | -54.30767 | 2026-07-24 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5912370b-2733-30d8-8d2e-412fa9d43719 | -18.80334 | -53.13815 | 2026-07-24 05:14:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ba7fb145-491a-37ef-81d3-8aa4391f7922 | -13.34753 | -54.30489 | 2026-07-24 05:14:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6dba8ce-ac91-3a26-83dc-a386b57bbedb | -17.62739 | -51.85762 | 2026-07-24 05:14:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c8f4f038-3e7e-30e5-a0af-efd51fc19f8b | 1.64243 | -60.14079 | 2026-07-24 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66494f53-ebd2-35fc-ac57-dda22574a8de | 1.65858 | -60.13838 | 2026-07-24 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 57196dc6-3e63-371b-abbf-0e1b7c650e99 | 1.13698 | -59.38572 | 2026-07-24 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 550e34f6-1b7f-30c7-a4c9-e5fc577f4759 | 0.89384 | -59.69262 | 2026-07-24 05:44:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7c8b2fa-818e-3a05-8707-ece1ee512355 | 1.64142 | -60.14107 | 2026-07-24 05:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d618655-dea6-37a6-ae9a-4abc802d2ad6 | -6.56528 | -55.14873 | 2026-07-24 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06916a88-6d42-3a9d-bc9a-af387e458bae | -2.71533 | -59.76928 | 2026-07-24 05:46:00 | NPP-375D | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38dddcc-86b9-3e31-a4ce-6899c89b4ac8 | -6.56571 | -55.14561 | 2026-07-24 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 595f10b7-12b4-381e-bfef-e5b31e06663d | -6.56484 | -55.15187 | 2026-07-24 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab9c1301-b2b3-3734-9210-8d7624b323ce | -1.78168 | -55.52872 | 2026-07-24 05:46:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b41575-1ee1-3f98-981a-67dd5d390143 | -6.57051 | -55.14954 | 2026-07-24 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9198567c-5580-3720-af05-0596e6709686 | -6.57094 | -55.14639 | 2026-07-24 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b0d99ec-5ef6-32ef-9412-649eae18819d | -6.56614 | -55.14252 | 2026-07-24 05:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a3400d3-eebd-3aa7-9470-d56398280dab | -9.1356 | -61.06512 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f6a2454-113f-365b-be19-fe9bdc70340a | -9.16647 | -58.32603 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7be9b5d7-c67c-3b3d-82b4-a29fa72d9753 | -10.26015 | -59.03196 | 2026-07-24 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26119536-406c-348d-bfe9-50610ce46866 | -11.59781 | -58.5082 | 2026-07-24 05:48:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 696e752b-b367-3a17-8605-ea2450aa3d85 | -9.17203 | -58.31829 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef346d4d-21ff-323b-93d0-f7c58cabb032 | -9.01283 | -64.14573 | 2026-07-24 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78a3a485-9ab7-3345-8e77-5de7bee49c4c | -9.13186 | -61.05816 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43720e27-a367-3315-9ba1-1e625670ef0a | -9.13626 | -61.06079 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2b30b0a-ef02-3502-a5d2-9f707b5c6ee1 | -9.16587 | -58.33022 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80a796c0-a866-3434-bb04-e81a69f0e9c9 | -13.43387 | -51.52797 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2742e121-a91a-3f33-ac6c-ec1b8e3117bd | -7.32077 | -64.70073 | 2026-07-24 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01c10a59-cc7f-3452-83c8-b296c62d9a13 | -9.16449 | -58.30845 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c71e0d3-ddb4-37eb-b144-64fd7af1b683 | -9.13258 | -61.06022 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ed1a3fa6-bc05-33d3-a792-2018042aaeca | -13.44398 | -51.51979 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3261616d-80f0-3de6-924b-5fe9959ca867 | -13.43536 | -51.53338 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4c15bcd2-2862-3a75-906f-80ec2a606934 | -7.86434 | -61.48991 | 2026-07-24 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188e969e-a2fb-3401-b6d6-167176e2836c | -13.449 | -51.52234 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| aa754f79-6e9a-3074-bacd-5a54e5b56097 | -10.47407 | -62.44707 | 2026-07-24 05:48:00 | NPP-375D | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59c47969-e2e7-3a6c-b8a5-26571a039762 | -10.0241 | -65.04958 | 2026-07-24 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b60115f7-27bc-3796-838d-458ec457166b | -9.00896 | -64.14869 | 2026-07-24 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c85e15c-859f-362d-8048-d52feff35a59 | -13.44182 | -51.52155 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5f7c6d17-ba4c-3682-a1f6-4e431615d243 | -9.1615 | -58.32956 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4ad7a2f-9926-399c-8052-63dc9e7ad1f4 | -10.02354 | -65.05309 | 2026-07-24 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0d8c1a15-91d1-328e-9e25-d70485902fce | -11.5972 | -58.51271 | 2026-07-24 05:48:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f06b514e-8081-36bc-b094-379cea268db4 | -9.00951 | -64.1452 | 2026-07-24 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9bae7dc-29a7-3ee9-b533-78a57d0e7876 | -9.1621 | -58.32536 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4977927f-619c-37f3-bba9-0fddb4d30cc5 | -13.45116 | -51.52062 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f0287da-ebe9-3645-af90-abf2f52b777e | -9.17264 | -58.31403 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d327aeff-e6a8-3f67-b51d-4a8ffdc746f5 | -11.359 | -55.43772 | 2026-07-24 05:48:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e88f24ca-0f20-354d-878d-056b2cc35773 | -13.44105 | -51.52875 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e70c9389-c4ed-3830-985a-e3cd0c556520 | -9.13193 | -61.06455 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ddf7b9a-a6a0-37d5-8ec6-5e5c37c13198 | -10.02742 | -65.05013 | 2026-07-24 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6697667d-e815-38a9-8d6a-714c88248ae3 | -9.16886 | -58.30911 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1055ee16-0c01-3c90-be1b-5adf4a53b22b | -11.3645 | -55.43841 | 2026-07-24 05:48:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87a90f41-8aa4-3b83-8d8b-6c04abbf2307 | -12.16437 | -59.76356 | 2026-07-24 05:48:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42dee29c-83aa-3538-9cce-149d5be39172 | -9.01228 | -64.14922 | 2026-07-24 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58d8d017-8839-339d-b4a2-50f06712cf2f | -9.15773 | -58.32469 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed04caed-c74e-34db-90d8-ce03e8e3f2cd | -11.84868 | -60.71182 | 2026-07-24 05:48:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15436ae6-094b-305d-9bbc-59b0fdf2026d | -9.13554 | -61.05873 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b30bb1a-1b66-324f-824a-814ef02b852e | -8.82729 | -63.90473 | 2026-07-24 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README8.md)
