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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87dff69d-7373-3bb5-bbb4-51099e781d39 | -2.77873 | -54.0785 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe2e6243-bb16-3515-b2bb-cf4fc4d2d5bd | -6.01595 | -40.9771 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 189.7 |
| 8cbf52dd-e9bf-3515-9e10-378b715e77dc | -5.24321 | -43.98083 | 2026-10-09 04:25:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 271fcb1a-2cac-3d57-9a61-92050048a589 | -2.98681 | -48.91433 | 2026-10-09 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 164f372d-01db-33a4-8728-1398a96aed55 | -3.26499 | -54.05852 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ab65d14-2285-3ed7-96b7-cccfadad9500 | -3.36879 | -50.4766 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3f683c7-5439-3aa1-bfe5-8fa0ae6e3d97 | -5.59434 | -47.28313 | 2026-10-09 04:25:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c432a2c7-cb70-32c9-95d6-36460a13c719 | -4.0691 | -51.04061 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2631082a-4155-3aee-a5c5-41220d0dcf11 | -6.68718 | -41.75965 | 2026-10-09 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac65f4da-115f-31df-ab0d-0d4083d53f08 | -5.68136 | -49.04363 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d4872d6-fc72-37d0-a33f-dc9f4b3a3575 | -3.76855 | -58.84706 | 2026-10-09 04:25:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1aaf1e15-d1b8-3c60-bf46-4db5f227cd47 | -3.10476 | -53.93806 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6a71677b-7d36-3993-911f-41c60e23e72b | 0.97473 | -50.12281 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d25b5fa9-27e2-303c-a921-aaaa6a92546d | -2.18643 | -48.24885 | 2026-10-09 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a23d204-0236-3c74-9d8c-4a45490c31b9 | -5.69869 | -41.73831 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 87da6ed5-1cb2-302a-a1b7-8531c3652286 | -5.70661 | -53.48698 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 953625e4-1fea-3266-bf89-139026eb247f | -3.55413 | -54.68237 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ae55ddb-679e-3339-86d1-6fa240d4353b | -3.20443 | -50.82806 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 48873f8f-02cc-3209-b801-4c308bea8635 | -3.1057 | -53.93235 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bf974b8-498f-3e7c-9e3e-b190c277433f | -1.15424 | -54.2265 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aba7491b-c228-3954-aa01-65cb3bde29dc | -6.95805 | -45.27517 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a333fbc-7360-3c7f-9158-ccc246d41d5b | -5.87902 | -49.87485 | 2026-10-09 04:25:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4640e371-0171-36f4-b873-45f46d5e1a4e | -3.27677 | -50.02421 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94f3b79d-0d34-3826-91f1-d454bd4ffc4f | -3.04342 | -54.15342 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac00e82a-5628-37f1-aeb5-4de7f694ae93 | -3.20675 | -50.55711 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ace2d2ab-fac3-3628-84d6-0c7b18a963d9 | -5.74915 | -43.27288 | 2026-10-09 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fdf9cf59-86f2-3e3c-a031-b12534a027c1 | -7.11675 | -42.53904 | 2026-10-09 04:25:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3f66ae92-9e14-3703-b4b4-9efba81a706a | -3.30792 | -53.71054 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a0dea28b-8717-3468-aec1-03b1e73eb103 | -6.1532 | -47.27829 | 2026-10-09 04:25:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82856fab-02a8-377f-98aa-d9570472e5d8 | -2.49266 | -56.16829 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b5ff23d8-5b48-3cbe-88b4-26cf5e623cf0 | -6.8287 | -39.38725 | 2026-10-09 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| eafbba6c-55ef-31ec-aa9f-8cca0376b7dd | -2.26465 | -48.05592 | 2026-10-09 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0239ccd4-a01c-3f95-9d34-b6f424e00119 | -5.08738 | -46.22054 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d59564f-fe18-35c2-be3a-a3c3ae57c0b5 | -3.76273 | -40.75357 | 2026-10-09 04:25:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1e9944c-94df-3f28-ab20-6bfdd891c03e | -3.05336 | -54.03113 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8152a459-4f1d-3523-bf40-0af829615c32 | -6.88397 | -45.91256 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 06b57189-f5cb-35f0-97a0-f574fc407efc | -4.11025 | -54.62625 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a4ae507e-e08c-3141-ba29-a32e743b9ba7 | -3.08501 | -53.96453 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9523f4f-4230-3c21-938c-73432b306ed1 | -4.5574 | -54.97649 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdd94561-13f0-3031-8f4c-8e958d30a66d | -3.11382 | -53.78973 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| abcf8941-008d-3a35-82bd-b0a8a9810fe5 | -3.01286 | -53.90284 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2947719-42aa-307d-93cd-588a513a4c9d | -5.2704 | -55.95826 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75623758-e718-38ba-97d3-3aa9910b0118 | -3.01974 | -54.04663 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6db846cb-8558-36b7-b747-e1aa20fd3009 | -3.11352 | -54.17083 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5e7c7f3-6ca5-3780-a531-d2d5574e4a6a | -3.58316 | -54.31277 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e5e28bd-0f10-3b13-aca9-6f8286cbba28 | -2.34617 | -57.99268 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| db84eace-c057-3b1c-9e7b-3501fbda8c9a | -2.74045 | -54.12149 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daef4e2c-6551-3328-82e5-66b460f974a2 | -4.57169 | -54.95544 | 2026-10-09 04:25:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dc5c6373-1032-3e8f-aff9-465ddfb373df | -3.174 | -58.62354 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a0fa8adf-63e1-3580-bd80-feacac7a35df | -2.77414 | -54.0747 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96e8785f-3f30-32ed-8e52-77bcc79679c4 | -2.078 | -46.57247 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9d6756e-d91f-37f0-85f4-57aa7881ca79 | -3.03513 | -54.23504 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b9e091db-ccb1-36a7-86d1-81d827658da0 | -2.82551 | -51.28198 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dbfbfaac-6823-3c2c-adf1-7b2cdb3a74e2 | -2.75209 | -54.11417 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f52be35a-7ab9-37e5-81dc-62a55a3fc335 | -5.34471 | -45.17569 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 55cb8b77-554a-3e60-b62b-47cf1b711181 | -5.9996 | -40.94471 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 86922f6e-7796-3a17-a517-4c8c2bfab93c | -3.0356 | -54.10661 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63198adb-0413-301a-9a1a-749f35ca82e3 | -2.98396 | -54.08033 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c18c7c64-7ab7-3466-af49-7bef51169f13 | -3.25229 | -54.04199 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 088446af-b4b2-3e1f-97f4-f63a7f8148c7 | -2.54754 | -57.99247 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adaf22d1-7e66-316c-be4a-207fa5af1dc2 | -3.57627 | -54.68212 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45de9b70-e878-3e4b-b6b2-9ad791754b80 | -6.00711 | -40.97989 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 658c50ab-7c24-338e-bb15-a2497d9db77e | -3.37351 | -50.47223 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1650ea3-ab29-3b5f-b4bb-46416a48b5a3 | -3.59925 | -54.67292 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd5c21a3-ab74-33fb-a687-aa4416fecc9f | -3.17348 | -52.15907 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dfd1850a-254f-3f90-8160-e1b295de33be | -3.10576 | -53.77707 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a2828a55-2c61-3011-b898-f84da1b97d30 | -2.69692 | -49.36974 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d95bcf-9430-3be2-8e41-55791a25b45c | -4.15411 | -43.18808 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29ede1f4-cd6e-33bf-8551-ee6dd51d6cce | -3.00102 | -57.75732 | 2026-10-09 04:25:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91bb6bb3-bbde-3bb2-bc45-b8061a508363 | -4.02838 | -40.64993 | 2026-10-09 04:25:00 | NOAA-21 | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3294e65f-60d9-3a00-ba2b-be2783312e5e | -2.99042 | -48.91489 | 2026-10-09 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e62a3d0d-855e-3c23-bafd-036c44e264f7 | -3.01431 | -54.0851 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d68105fb-1bd8-3583-826c-4e3e10aea566 | -2.98853 | -54.08409 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b693948-439f-35f0-907b-a0e98f0a6ca9 | -3.08047 | -54.29642 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18ddf74d-ad85-3628-a7b3-8a90da8a0f3d | -2.54661 | -57.99808 | 2026-10-09 04:25:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f18cba9e-bf7d-32af-96ee-3a21af10a69b | -6.90098 | -45.89023 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| bb67db58-dff3-3181-8e43-83cfa5f123b1 | -6.96476 | -45.27618 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23e128f8-ef4a-34d0-9da3-d9bff10de032 | -3.57466 | -54.69157 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e025e434-21b2-33b3-ae81-059a9176e638 | -3.0098 | -54.10552 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aed3a4ba-e2ae-3e01-9cee-f802eeabfff5 | -6.06506 | -44.10962 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa2d3771-a7ba-3e4a-a730-ab355a4c254f | -1.3673 | -55.60523 | 2026-10-09 04:25:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c6943473-917a-30b3-ac21-7593cc8a3693 | -3.27825 | -53.81792 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bf58281-0ad1-33f6-acc5-e478a7ea33e6 | -2.47548 | -56.094 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cec40f9e-b384-3421-aabf-6474b441fc18 | -4.82481 | -45.83087 | 2026-10-09 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| de0ecf21-fc9b-3ce4-98cc-ad3b8d433a85 | -3.30501 | -53.71398 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ac9fd8c-a1c7-362b-8a03-5000959cb07e | -2.98444 | -54.07736 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daff820c-52b2-3ac6-b402-57283356ccb1 | -3.58468 | -54.6641 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35078bbf-229b-3f67-bc8b-d42f6d4b1028 | -2.77414 | -54.07469 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f15b495-5068-38d6-b9d9-2d183049245b | -3.43243 | -54.53897 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7fdb86eb-b821-3760-82db-1db9a2fedd39 | -4.29899 | -54.80946 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ade4bc5-dffb-3fec-87a7-60fffb636d76 | -3.46073 | -50.58145 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 201981e9-46ff-38c0-9980-89b55afeaffa | -3.00179 | -54.76411 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b019805d-7cb2-389d-8039-8a11d1ec4dc1 | -3.30558 | -49.12408 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8b77799-07f7-3473-8387-eb8743092280 | -3.12115 | -54.17951 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 630c659a-a78c-3637-a99a-f1b490c028ff | -3.52356 | -50.34269 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6bae6ac-1c83-39a5-b44b-9c1e347c86da | -3.86834 | -55.99028 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08760fbf-6dd4-33a0-b95e-01e7c8ddbdbd | -3.69928 | -53.66968 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28ba5106-52ba-3ec8-9e0c-57e89245a975 | -3.60501 | -54.67048 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9afe44a3-7374-319a-a894-6c746cdaa981 | -5.72229 | -41.76717 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea7ce744-379a-3292-a6b3-0dad5f39874f | -3.5526 | -54.69175 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README95.md)
