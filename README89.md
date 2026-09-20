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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fa8b71c0-51d5-3f32-a0cb-35cec7322ca1 | -9.17858 | -59.42411 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81109c4e-9a2e-3926-9a6a-1ce059692a5a | -7.32146 | -55.61347 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8249b5d-87a1-3083-9d88-6152a627a274 | -6.45531 | -59.97928 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e91a7549-903e-3c48-a61a-3f0b679a234d | -2.6854 | -57.62547 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef7a4254-50ea-398b-9967-db1238796ccd | -3.34359 | -57.85769 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d291255-bc74-3430-850c-58c05fd8cea4 | -8.24251 | -61.36944 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 174e6f2d-ce8b-3e6c-8baf-f416430a9f56 | -9.70815 | -54.83311 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc842447-d022-327d-9905-f01b7b1815c5 | -10.31079 | -50.23946 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 07446877-3488-3076-9b37-eca880bbef7d | -3.34822 | -59.86205 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94ac95cb-eeec-3a25-93fa-a8a9a9c69dc9 | -6.44643 | -59.97076 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa6c27f1-2fd7-30b3-aa9e-0790fc8f9f27 | -10.30857 | -50.2585 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cf42dcbf-de43-363f-b502-bbd90b7a4773 | -8.63946 | -47.61271 | 2026-09-20 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5d43b323-ddd0-34a5-85af-0ea4d7508f01 | -2.91494 | -57.79434 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f3d48d8e-03a3-3a77-94ba-6cd07ee125c9 | -7.59814 | -55.71206 | 2026-09-20 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 181fbb41-289b-31c0-9dde-796b339165ef | -8.16882 | -54.75716 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba7baa82-43ad-3652-8431-f362a6ca5d50 | -2.89021 | -57.82128 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b97c9155-9b19-36fd-ac8f-9ef3fba24881 | -2.50317 | -56.59978 | 2026-09-20 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 41dfd83a-1421-398a-ae7a-dab9cf7cc4bb | -3.11512 | -61.4092 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83dcd6cd-4e3e-3b76-bb4b-b4a8ec2c7278 | -2.88338 | -57.79719 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6f59f152-03d4-3f1a-88b5-ff3dc2bb3e4b | 0.00717 | -60.6042 | 2026-09-20 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 513a77d6-e85c-3d73-91c8-f3c7606f3bd7 | -3.14966 | -58.6408 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8af437ef-e866-32c0-9ad5-8f651a167787 | -10.31112 | -50.23475 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 64c2a0ed-b4f1-337d-ab66-e1b98d6f50aa | -3.44849 | -59.259 | 2026-09-20 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c024615c-2607-33e8-86eb-17e7c57e59ee | -3.343 | -59.84724 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa1d3eb-0c1c-3448-ab0f-e4acfaf42d5d | -8.74011 | -52.35999 | 2026-09-20 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3162c86-2772-36c2-8277-2a5ea36e4970 | -9.19105 | -60.75811 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 079516de-69f1-3155-9548-b42104656cc1 | -3.33515 | -59.81087 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aee70827-8e08-3f95-828e-2fe82888f4bd | -10.31963 | -50.21649 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4d217154-38c0-3474-95a3-cf68ab837def | -6.34393 | -58.30135 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53d512aa-f653-3fd2-a021-c782a23cd23e | -8.76484 | -48.6651 | 2026-09-20 05:23:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 839dae69-8006-3186-bd68-1c2f66a813c0 | -3.34684 | -59.84432 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc275e49-4470-3c06-82b0-ce2b98b9b4b2 | -3.363 | -50.44482 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7912ffbc-b380-3f6c-8fe7-a908f890fb51 | -8.61808 | -54.59306 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5a224e0a-2191-30e1-b914-4e5c2589dac6 | -2.615 | -54.75509 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 04be342c-7bc9-3071-b1ff-ed09e2c6483c | -11.09131 | -48.29727 | 2026-09-20 05:23:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0e96ec5c-d115-3bc1-a718-a93ca7821c45 | -3.08211 | -61.18943 | 2026-09-20 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc7306a8-750a-3969-9954-2346aaf2f691 | -2.65927 | -59.7613 | 2026-09-20 05:23:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 124d70d7-9eda-3d80-b373-98b6b5461b2d | -4.29644 | -48.62918 | 2026-09-20 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1a79fe31-9007-3b5b-9951-75b86d6114b2 | -2.9827 | -54.77364 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c8e5b39-1f97-33cd-b164-b4d93aafcc87 | -3.36685 | -50.4566 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f90c823-b4c0-38ff-a368-0ccedb5591a6 | -8.61683 | -54.60215 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eea9b3c0-5b44-3cf8-9ac0-24c20502a742 | -5.91144 | -59.93365 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eaf1f637-5cc7-3be9-8122-1eb0f3bd8fc1 | 0.68986 | -59.55241 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 04b7cfed-3cc1-3ac4-84ab-8d6c96305446 | -3.44796 | -50.60224 | 2026-09-20 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 620ecf5a-ad62-30aa-abab-c3664683ea31 | -3.11119 | -61.41224 | 2026-09-20 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f3bb579-2494-3b3c-98f0-7c226592e6cb | -6.924 | -63.07119 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6847027a-a81a-3bea-8b4b-fe852927f9bb | -2.74439 | -57.64923 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06a8780b-7968-34ec-a7a9-1b94fb5ecc79 | -4.18683 | -49.4086 | 2026-09-20 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa1aae28-f458-3ceb-bbcd-faedf1fcc374 | -10.7157 | -50.244 | 2026-09-20 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fdd6e850-20b1-3961-b68a-f0935c8831d5 | -3.29362 | -57.86619 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b859bb5-5228-3223-a3fa-bb02c1512f4f | -9.03074 | -60.36562 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 57785bad-db8d-357d-a15e-4352e737530a | -9.08925 | -60.99944 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d98073f-0f47-325d-96ac-91c29c6805dc | -2.97973 | -54.76574 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8f9ebde-c357-3b86-9092-7a677fb2d828 | -3.74455 | -51.82143 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| d59522f2-ae09-3c2b-b9bc-9df5fa866a7f | -2.89365 | -57.82181 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75f852ac-2d9d-33b6-8914-617858c8cadd | -7.55433 | -61.33079 | 2026-09-20 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c66c951-4df9-37fd-b1f9-978c26a0dcdb | -8.16943 | -54.75283 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9dfe27a-abc6-36f2-b846-7034f2d41199 | 0.68932 | -59.54898 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fbccaab9-982b-3c65-b6d9-718bc6049b59 | -9.66612 | -54.32281 | 2026-09-20 05:23:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b93c185d-56bb-3385-af8d-abaa98f1e47a | -3.33287 | -58.13469 | 2026-09-20 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 447275b9-737e-32a4-8ad8-e257e8fbd2ed | -9.26484 | -48.20457 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7cebb30-0be4-3b4e-a677-63177a1acdac | -3.00731 | -54.1784 | 2026-09-20 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| def85b77-ab7c-3c3d-ac47-272b4d708d28 | -3.29707 | -57.86671 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e875867b-3ec2-3d1a-a2a3-fcd9dd663981 | -2.88121 | -51.73447 | 2026-09-20 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0f1639c-0a6e-354d-acd6-bf116523affa | -9.0248 | -60.42618 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 307f2e5d-465f-3ad5-af0e-45077527e4f7 | -9.03129 | -60.36207 | 2026-09-20 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a20aca3-83e1-315a-8938-a81950a376df | -10.31581 | -50.24982 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 07d070ee-3404-3d56-8d54-144d5fc4ed87 | -6.45145 | -59.98226 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d1d5ee-e0a1-3b29-b2e1-540f040c2fa3 | -9.03765 | -48.713 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7baa0c2-2aba-3b55-b83e-1e27dc1c076b | -8.79757 | -60.79639 | 2026-09-20 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7cb98c71-7129-347f-9677-a379c378bae4 | -8.17504 | -54.74477 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f71e134e-61ac-35b2-a3c5-7e9e2f2c8d2b | -7.04814 | -62.95473 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e6e799a-ab26-3966-8a15-c88ad7842dc9 | -2.68194 | -57.62494 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f29c2e73-16cf-3346-b9a7-de6c8ed3ecde | -7.41173 | -49.84208 | 2026-09-20 05:23:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2e14bced-3733-3b8b-89f0-49707da7bb48 | -2.97621 | -54.7614 | 2026-09-20 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df0782da-c23b-3387-99fe-dd5aa1597f10 | -8.17262 | -54.76213 | 2026-09-20 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7077b27-3313-31f9-a62f-f074d1e671ba | -6.34465 | -57.86308 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1cc52355-79eb-372e-a6ce-9539dcfe2158 | -2.91094 | -57.82064 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59c42d5d-45d5-3cb6-b2e9-316e7fbb733d | -3.85158 | -51.34256 | 2026-09-20 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a8ecc96-6a9a-3a41-b20b-feb35c0bbe91 | -8.63306 | -47.6245 | 2026-09-20 05:23:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7374f2e5-11a4-3873-9b46-7dba8aadd601 | -8.23671 | -62.83916 | 2026-09-20 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e044b538-799d-3a9c-9302-ced464385d57 | -6.20179 | -57.77628 | 2026-09-20 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 932e0ce0-94d0-3a67-8e9a-75d00280eac0 | -6.94485 | -62.91944 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70a50320-a5de-345b-b284-6eb2e956ae7e | -2.88449 | -57.81274 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 23dc4216-d3f6-3687-a91d-c20a85ab065d | 0.78776 | -59.2003 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a300725-4041-3fbb-b0c0-a590a47c9362 | -9.2809 | -48.24623 | 2026-09-20 05:23:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9c8fbf65-1e41-382d-a424-a36f048ffc44 | -9.1784 | -51.51403 | 2026-09-20 05:23:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 545820ce-781b-38f0-b46b-4e35c9718c15 | -10.71629 | -50.23917 | 2026-09-20 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 74d82b94-ef53-3010-84ae-908b0fd4e3ce | -3.40359 | -54.07389 | 2026-09-20 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 481b918b-91aa-3f62-908d-a8405fffd146 | -9.05432 | -48.7254 | 2026-09-20 05:23:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e43785b2-1cef-39f8-bd5b-f2a499622d83 | -3.339 | -57.8647 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d918aa3b-36a6-319f-9487-51910772c7b4 | -3.35536 | -59.85963 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de8bda4-8b20-3dd0-ade3-e96125d101ca | 0.69209 | -59.54504 | 2026-09-20 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebb34bc4-1305-3b20-bcb6-2e28a16c69fe | -3.33953 | -59.80452 | 2026-09-20 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e36acf5d-5690-3b7a-a8f8-15b9209ca434 | -10.3041 | -50.24339 | 2026-09-20 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2cb7a66d-77d1-3209-a5b8-54ff84498c77 | -6.34683 | -58.30575 | 2026-09-20 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d34270f-c844-3b7f-a753-7f6cb87a702e | -7.04531 | -62.95042 | 2026-09-20 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ae9e297d-f6be-3ea8-9844-26c9c5e3f81c | -4.26515 | -48.64137 | 2026-09-20 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1bc56a84-c58e-325a-8b98-3fdf4702789c | -3.94088 | -54.85546 | 2026-09-20 05:23:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d6ea217-6184-3a2a-8aef-23f56ca8f627 | -2.88397 | -57.79343 | 2026-09-20 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README90.md)
