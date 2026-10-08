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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfb6d6d4-b85b-3672-9048-0a4fbada20de | -3.96724 | -56.12744 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b5e8e71-db32-32cd-8320-df9fa682fd7f | -2.98246 | -52.96692 | 2026-10-08 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7db23bc5-1c65-329b-8af2-623d01ee3628 | -3.04346 | -53.95869 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 727ff163-07d9-39d0-8441-8d12694c495b | -3.58532 | -54.65522 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 508d1871-bc7c-39ea-bf18-842f7d81c938 | -7.46666 | -42.85838 | 2026-10-08 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 534f4e9c-57dd-33c3-b556-aa7ce88864ee | -3.81176 | -60.47466 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6d084e3-76b1-3702-bc6b-cc8738c7c840 | -3.26258 | -54.04352 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2e17ef6d-efbc-3013-95e0-614a60986e7f | -3.65022 | -54.05889 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b039be7-0499-3a2b-b990-9741890fe435 | -3.00144 | -54.08086 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 3645c44f-4285-3787-a1c5-05a1b1e1e66e | -4.7738 | -55.72229 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64541d03-3be8-3dfd-a956-8dda3dcc317b | -3.23191 | -57.87445 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad8426cc-2f21-392d-aa4c-fe7184490c55 | -3.83079 | -50.98874 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fce4a679-8f1b-304b-8ecb-36062b5f2e3d | -2.58202 | -56.15403 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a89f3fe5-430a-3b09-9539-8e9509697eca | -7.38194 | -46.22824 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f43c589-00c6-3e5b-8fd4-b887fad7bd53 | -9.14725 | -45.82172 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f880e81d-7a7f-331c-ad2d-cd2d9627308c | -11.86211 | -43.55717 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4502e9bf-d837-3e59-8911-a277ac8bcd9f | -3.54302 | -54.67682 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2368f3a1-ee00-3fb2-b5c2-9c88aff6ae77 | -3.0539 | -53.91634 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7d635e8c-8666-3996-a5bf-192845dd9a0b | -3.38264 | -59.431 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9567aa9a-7e38-35b4-9619-dcd84c7ea48c | -4.06427 | -51.03976 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8677ba63-6e24-3749-9713-c549fbfa2cac | -3.28432 | -54.02475 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07ebef14-9a6d-3aaf-bd27-bf37928654ae | -5.73499 | -45.15208 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 048be195-8623-3520-a3f4-6afe82f35fda | -9.3699 | -55.97084 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d41d850-c0ff-38da-905f-e1cce853975b | -5.29622 | -60.08307 | 2026-10-08 04:46:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a889164-4942-3f05-b420-66b9430972a0 | -4.30492 | -50.78543 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c50d083a-6ada-3ebe-8376-00a2de9f897e | -4.07488 | -59.8427 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4c135f3-61e4-386c-8bb0-2d24035c3e49 | -4.05775 | -55.32653 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7efae5e-6f2f-3ca3-839e-74809b916c2c | -6.82732 | -39.55304 | 2026-10-08 04:46:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a9d3b39a-7c13-31a2-9e77-32fa21bc8587 | -2.58014 | -56.16581 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03759bb5-ccc5-37c5-92d8-a05e06014faf | -3.07869 | -54.25385 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f3f1168-e2f8-31f5-908a-a7ae513a45aa | -2.50622 | -56.16631 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2fa51a96-0748-3ad9-94a4-c8fa72f739a3 | -3.30109 | -54.01277 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7126465-bc87-3897-ade8-60b63eaef878 | -2.48853 | -56.11496 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d86cf7c-0bdc-3df6-a84d-2f85156126d5 | -2.7691 | -54.07864 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 06407ef5-1a1a-30a6-a253-f12a29ed97fc | -3.31431 | -53.86207 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e24ef4ad-d1ba-303f-acce-579df464c6ce | -2.73825 | -57.61413 | 2026-10-08 04:46:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f00b24f4-8d0f-329c-b932-66bb1846a45d | -2.94435 | -54.15294 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9cf79d16-292a-3fd8-be77-f2f58fcc4e26 | -3.05088 | -54.15147 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e3e1269-4f9a-30bf-847e-60ebd306b408 | -9.80069 | -47.8173 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd75d717-b9a1-3be4-bb08-c564520f1256 | -3.14819 | -53.72638 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08fad131-c281-3f04-a125-c58d859fff98 | -2.99915 | -54.07156 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 7a4e06ac-104c-368a-b10d-7016de364f18 | -2.94802 | -54.06535 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6d0a81e-c16f-38c9-896b-9de97c3a57e3 | -10.4984 | -51.93755 | 2026-10-08 04:46:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f0c768f-6c35-384f-b960-62952d5d6797 | -4.06746 | -59.84537 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 45bdac0a-577e-3612-8ce9-97cadfb00c24 | -6.68452 | -55.09103 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ef551baf-9327-3521-98d5-e9d0dfe91e99 | -3.02289 | -54.08866 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18167d47-de93-33fc-87d6-c627b64e6a36 | -3.21181 | -53.86916 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a8356c5d-42b7-308b-9592-20b7a1528f12 | -3.29062 | -54.0774 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4bec82e7-ebfa-3d73-9aeb-0e82d9566d64 | -6.23217 | -52.85214 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53827acb-355b-389a-9bc2-ee41f164c212 | -7.37132 | -44.03438 | 2026-10-08 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bba3fbf9-cc89-3231-8661-a5d374bc55b3 | -7.87333 | -44.15552 | 2026-10-08 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| acafc8f4-cf8b-363d-a05f-294edc2cd535 | -3.16349 | -54.72137 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7cd0c03-0768-3d1c-87b0-a07bc9a4863d | -3.14164 | -53.72109 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25ac995f-cf0c-33b0-bc60-6247cc058592 | -4.77889 | -55.74083 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 004e6b8d-649d-3abd-b90b-364144b865e0 | -3.28646 | -54.01043 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95124b5e-2e7b-3b6c-bfcb-5d39b69fd69c | -8.17564 | -54.72536 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab90ddb-a2e9-3874-927c-8e42db9c14d8 | -3.84904 | -55.97961 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ecc0aa31-1dba-3308-8498-41b8a3d532d9 | -7.46438 | -47.59825 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d6445004-3360-3b22-9f8c-70c522494bac | -3.55208 | -54.66885 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b68fdfca-23cc-3f77-8264-cc1e56d1a97d | -2.9865 | -54.0562 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c7efda7-54c0-3591-b23a-583b83bfd28f | -9.53163 | -59.37968 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 703011c4-7c02-3788-9bc8-48fab32991dc | -3.58543 | -54.67887 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3e935678-7357-39e6-895e-2c029e3d7543 | -6.14967 | -52.64302 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b1156cc-f131-372f-b62f-9c9e243c634a | -3.18043 | -54.61374 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 200279a2-7210-3481-b7e0-1051bca231e5 | -2.39024 | -56.133 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b27b1cce-3382-375b-a4d6-9d3f5a671007 | -5.11655 | -47.12069 | 2026-10-08 04:46:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ab11761c-00fb-32cf-ac9d-b6373cffe82a | -6.23275 | -52.84851 | 2026-10-08 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5625fbf0-714a-3880-905c-025e0665e553 | -5.95867 | -46.39033 | 2026-10-08 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 047022ba-d6ef-3a68-aed9-daefd233ed8a | -3.08186 | -54.28177 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42206e81-2097-3114-883d-429e960dfed2 | -3.10121 | -54.2802 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| dd3ab898-d9f8-3959-bc82-7b5ac8931c80 | -3.15402 | -54.08985 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58705503-0395-311e-abf9-f3a667ad714f | -5.97155 | -40.91098 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 50c19e65-89ad-33d0-af20-2482f5db5f46 | -5.73045 | -45.14536 | 2026-10-08 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 17757f9a-a1cb-34a6-8986-bb66152f9e8c | -3.0116 | -54.06454 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 703750e4-e4f3-3341-ba3d-8ce967b00ab0 | -2.58374 | -56.17042 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b4d3323c-a3d4-3db7-a765-85b6e45f3382 | -3.06306 | -54.25615 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c94821d8-ec2f-315b-acfa-3201847c3b60 | -3.56535 | -59.49761 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76e6053a-9057-3226-b3bd-0d1da2900876 | -3.27631 | -51.05289 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bab4ed03-8fc3-3398-a3c1-9eb701240b34 | -3.16901 | -54.0867 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1c920dd2-eb3d-3510-9ffa-252d8baa6af4 | -3.38215 | -59.43016 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a21f8a0f-573c-3b40-b541-489fbdb7f21d | -5.68805 | -53.48322 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23e19f36-1886-321e-9fde-8af0e922d7c2 | -4.14398 | -54.89865 | 2026-10-08 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b3d8d88-15a0-3f06-a283-90ccd8519356 | -3.66136 | -60.62644 | 2026-10-08 04:46:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b0be85d-90a3-3070-a044-a2005030692b | -2.85148 | -59.11697 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d76d5ed7-ecb8-37fd-b401-b642460a4c1d | -3.44622 | -56.93373 | 2026-10-08 04:46:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73a354de-8cc5-3bbc-9d28-bc0a6a187400 | -3.28499 | -54.02044 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96d91b89-fb23-32e1-b220-00ff1f15012d | -2.47364 | -56.07267 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4fc121a7-238e-34ca-aba1-94a753debe02 | -3.14525 | -53.72165 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d85b18a-1015-3857-a2b4-5d35b302d56f | -3.0275 | -54.10736 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| da661f2e-bc5e-3806-a156-34dabe3f93f3 | -6.93981 | -46.59469 | 2026-10-08 04:46:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5c8e908-d4f2-31db-be53-39681d0ebfa2 | -3.11134 | -54.16835 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b40a1d4d-23f2-36b9-b278-4f1d6985a00f | -3.04417 | -54.14589 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f1f2792-c48a-3532-8382-f427eda3b679 | -3.47938 | -59.46316 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0157d9de-fc73-359c-8136-e61462d7dc36 | -3.12921 | -53.70633 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 108c9454-cccc-37bc-afaf-b83635047a69 | -4.29147 | -49.09054 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 124fed77-ed68-3af3-a200-793e9c965842 | -8.08853 | -55.31231 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15250b4a-9ef4-3999-8aca-58b9c891bcbb | -3.48027 | -59.58675 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c2b0ecae-8c2c-3e8d-86e5-7499a5903a0b | -7.38395 | -55.21629 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1bd348f-9560-3a1d-a063-04f00bdc4018 | -8.08289 | -55.30856 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2246b8f-60f2-3a42-865e-ee80b001424b | -2.75887 | -54.09513 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README117.md)
