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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22892e60-0012-3515-a3f2-5a0ecc9f3450 | 1.75099 | -55.5572 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93aa15a0-aae7-3e80-a39e-687583a2cf27 | -3.81984 | -59.34149 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 830912f7-baa2-368f-9bd1-e1040c444e6a | -3.43544 | -59.53869 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e7f94e5-a4d1-3e09-953b-67a701ae690e | -3.49044 | -59.38186 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b204fb7e-bc7a-3b61-b58d-257028ab417e | -7.90323 | -54.71469 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9562a2c5-c15d-3dd9-aeb3-3305c6548618 | -7.57227 | -63.34389 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a01c05f9-0ee0-359b-9059-fdd174bc67d7 | -2.94258 | -51.41175 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c031712b-8014-38d9-9d95-4a31b802cbdd | -2.54884 | -57.99491 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 24267578-a62c-30ac-b19c-ea49ac955bb4 | -3.00705 | -54.08804 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 86254f5c-ffe9-3988-bfdf-172f1891d6b7 | -3.17574 | -58.84125 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2d4ee10-8c37-3962-9d62-f1cf2bebe288 | -3.63834 | -60.61853 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287d042e-2581-3e86-a663-8567eb3d871d | -3.10964 | -53.79232 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d63eacdc-d09a-36fd-9ece-d40fa96514e3 | 0.92708 | -50.25743 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 993a87d0-9f00-32cb-89d4-17612f4cf294 | -3.29638 | -53.69613 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 648744f9-cde8-390b-bff7-847dbe527c59 | -3.70239 | -53.66999 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96946d55-643e-38bf-9e7a-b15f646a856d | -6.43116 | -60.05397 | 2026-10-09 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b46323-d2e1-378a-bdf0-b8190197fd79 | -1.29991 | -54.20528 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abab6d5c-3e4a-3b46-9d2e-af783654a624 | -3.79935 | -56.99803 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 277754f1-8693-36cc-ab16-118731852db8 | -3.30764 | -54.04213 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68683583-dc0d-3eb1-bd16-c5b50c48c7cf | -2.93573 | -57.65258 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11e5bf74-d139-3417-9acc-073977c38aa6 | -3.98853 | -59.34971 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e2650ee9-0a11-3be3-bf3d-706a893aed22 | 2.76507 | -60.00227 | 2026-10-09 05:23:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f1fe33f-2d01-3367-8972-dcf0cca57d75 | -3.65343 | -54.06276 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15c59f0c-675a-3e78-a99e-3696c00d841c | -3.17519 | -58.8447 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58445af5-9952-3f81-9fea-09bc0af1c2aa | -2.4978 | -58.08204 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a523ee34-f7a4-3727-bb24-d949c4e7625a | -6.99371 | -59.12574 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db83f29d-cd09-3c5b-bc38-914839108c67 | -3.44769 | -59.54785 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7874ce84-8c21-3b86-be8d-95c02394bdbc | -8.97108 | -45.90869 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7710ba2-030d-3d33-81aa-3e5aa0c6f83c | -1.31974 | -55.44398 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 013a8c0c-e8c5-35ba-8664-99b5a0925a8f | -2.89748 | -56.66756 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10499f55-dddd-39a5-8ef1-681cb1d52aff | -2.86097 | -60.91917 | 2026-10-09 05:23:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b42a5e5-c9f0-317f-8412-e284e9e8ca05 | -3.14874 | -58.5617 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c6ef685-c69d-3bac-9a55-23a756fc5046 | -3.63269 | -59.32237 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1dfcff90-cf90-3e34-89e6-ee407e6e213f | -9.63628 | -61.83298 | 2026-10-09 05:23:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 181ecb38-02ca-3ca5-b562-755828eaa2d3 | -9.25802 | -60.88396 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5f04d14b-49ab-37b6-9cc5-9b4d5dfe9eb2 | -3.08523 | -54.30416 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e3a386b-4938-38bd-a635-f0c839d8dac4 | -2.80239 | -59.18063 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3910a35a-4894-373a-b534-dbd4d6da6854 | -2.88462 | -54.07634 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5058a119-958e-3abf-9d9b-8bcce96893f8 | -3.0063 | -54.09278 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63ea439e-1675-35bc-812c-cba23b4b1305 | -1.3027 | -54.1874 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4272c55b-eefc-3814-b22b-0000081a3d31 | -2.98236 | -54.06963 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| efc8b78a-f3d9-3897-8405-26544eed6bac | -3.04323 | -57.50926 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2409f72e-1565-3040-a5c9-957fc52c0deb | -3.70779 | -58.91504 | 2026-10-09 05:23:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6331ae62-7f3c-3c04-b2d0-2643230653b3 | -3.10724 | -53.78176 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3b85fa9f-185b-391f-980a-226426d63f35 | -2.75339 | -54.09752 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4469350f-6ea7-3554-93b0-729eaeff4a61 | -3.52656 | -59.34816 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8007892-8502-32b3-80af-f2257b22e806 | -9.25625 | -62.30759 | 2026-10-09 05:23:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 612e841c-a9f7-3cd6-b165-e5a0b363742e | -4.3796 | -55.15628 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cdbc9243-5d61-3567-8c53-7b4ede9b39d5 | -3.51909 | -54.47655 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a70821c-c492-37e8-a19b-e98ceddad75f | -4.52434 | -54.86478 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7d467e0-5074-360f-b0b7-6deeb1749ca6 | -8.83785 | -61.45942 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b69c59ff-cfb0-3a72-8d2e-9a58f6d62cca | -3.56494 | -54.68534 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 80d8be1a-62f0-368f-b4a0-0c2802aa29f3 | -3.063 | -54.17157 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b60658b6-a02e-3c98-a35d-3d4d2f50a8ce | -3.07543 | -53.96309 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 506e6972-2d35-3706-811b-05e5452fa535 | -4.34673 | -55.13109 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81958c65-6a29-343b-b81f-69342bbeefb4 | -3.29663 | -54.01069 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 509197a3-dfd2-3cb4-8649-a276d0d995be | -1.25323 | -55.75546 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a613366-4278-3f09-b790-0ea559b9410c | -3.65877 | -59.15898 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9b9f681-7cb5-3f2a-9081-58782d3cd7d5 | -3.89781 | -58.95956 | 2026-10-09 05:23:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0d48149-d953-3715-8745-c9e0a8a56f57 | -3.72791 | -55.96923 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfa199bd-d08a-36ba-96b7-ed15ce6fdd1a | -1.1152 | -54.17014 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0aa5f333-a17d-37e6-8065-ba5dc165f1a8 | -2.50032 | -56.06993 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 52ffd6d3-c81a-39fd-9064-95fa4a3c92eb | -3.79079 | -59.3759 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a38fd1bb-ad38-3a34-8ab4-c0ce0f5b15dc | -2.8455 | -57.47102 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8785962f-7909-3883-9b41-0061844fac1e | -8.84465 | -61.46054 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5b7cb43c-dea6-3e79-81b9-f8ac8766edc6 | -3.97174 | -56.12017 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5520936-cd64-3a8e-8d2a-c3feb38fcb84 | 0.78833 | -59.19835 | 2026-10-09 05:23:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 426e9fef-964e-3e1a-864c-ac07bb749fea | -9.67003 | -57.85495 | 2026-10-09 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ed44b28-ee3b-37c6-a059-a421283314de | -3.02908 | -57.64257 | 2026-10-09 05:23:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d1dd7cc-a051-312e-96b6-5f5fe975620e | -2.9806 | -54.03021 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76d0d2e5-833b-3e94-9f27-ad674ad65439 | -3.10985 | -54.19003 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b243391a-924e-37cc-9efc-87d91b24eb23 | -2.56262 | -57.4126 | 2026-10-09 05:23:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef32b05f-f440-37d9-85f9-4e2e3ef37776 | -3.09567 | -59.19437 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe77093c-5c17-36d0-a41a-a71b9935090f | -2.99775 | -54.07199 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0138dc3-257b-3859-b9ef-3371679845c9 | -3.10873 | -53.95322 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43bb0314-495f-3e09-b738-a91542df6f13 | -2.4737 | -56.06636 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e96233f-f464-3c3b-ac9d-f1fa02321dca | -9.09887 | -59.38995 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d912ae-4a25-3b3c-bc1b-9a747c7dbc93 | -7.57304 | -63.33931 | 2026-10-09 05:23:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b60701c0-dd93-369e-9b7e-42fe3529571f | -2.48861 | -56.16817 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd33e611-0988-3984-9c2f-7d5ef8a488cf | -3.74916 | -59.42302 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c04776b2-0fb9-3c2e-a044-daf010683fb5 | -6.99866 | -59.11589 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97bf4e21-75fb-3d09-8fc3-2842361b75b7 | -3.58858 | -61.6382 | 2026-10-09 05:23:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce4d34a6-3271-3719-9470-361db53532a3 | -3.18435 | -58.65902 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cae4b4a-6e40-354f-bd8c-760b139ee952 | -3.51809 | -58.03131 | 2026-10-09 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d136dc94-6689-3ba9-9dbc-89237ed39563 | 1.74875 | -55.565 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ba05ff1-ab88-3836-8b33-3500d6c9bb5c | -8.23538 | -54.74368 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c3323aa-e072-3cb3-a90d-8542050a9ed4 | -10.28565 | -46.61451 | 2026-10-09 05:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65e09b9a-2e09-364a-afc6-c1a3322c5be7 | -3.28502 | -56.98903 | 2026-10-09 05:23:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76270e95-ea9b-3cae-a409-dfaa03c79ef9 | -3.30603 | -54.02696 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c82c96ab-d8d7-3af8-82d7-c9a1158e7ee3 | -3.2891 | -49.51395 | 2026-10-09 05:23:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69f94784-20fb-3f27-bdb4-cc00f6e1ec60 | -2.90369 | -56.67223 | 2026-10-09 05:23:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba2f0fca-32c3-37d1-8744-ca08cafaf48b | -3.22534 | -54.29627 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a8172ac6-978e-38bf-910c-4108caa75b15 | -2.48459 | -56.17138 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f51205cd-7d69-3459-b050-5fe83bb7598b | -3.74645 | -60.60004 | 2026-10-09 05:23:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16f6bc59-c137-3432-a474-b6daab398097 | -8.98226 | -45.90767 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e60ed557-7986-3b85-9817-2813e5d7db4f | -3.20151 | -53.87379 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 202d8262-3f7d-3116-80c9-5c4a4f058105 | -3.67031 | -56.81182 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3784e30d-1bc4-333b-8241-fa8fd068f1cf | -1.20503 | -55.68731 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b5d56a2-3195-3b13-93c5-8360aabe832d | -3.48631 | -54.6162 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 734ca549-ce9c-3521-89cc-402f6d267454 | -3.56868 | -54.68592 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |


[Clique aqui para ver as próximas entradas](README188.md)
