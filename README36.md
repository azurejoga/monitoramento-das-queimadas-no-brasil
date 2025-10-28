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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dff65611-a6d9-3b0a-ae76-b07c43b48442 | -12.12494 | -45.22343 | 2025-10-28 04:14:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1035bc09-d280-3dce-bf4b-1595497c8bf9 | -10.60442 | -46.61473 | 2025-10-28 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 734623e3-2abd-37c2-b414-fa60e13ba49f | -7.05688 | -44.81029 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1835a6ef-032d-36e0-8e5b-da427678b81a | -11.14538 | -44.94196 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68d52068-0f0b-36c9-b474-3dab58766e09 | -11.19509 | -44.62805 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf826a7a-0c4b-3105-95e2-2c610db1fd35 | -7.93404 | -49.73969 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 02e18e58-9399-3336-8ceb-1c2749897442 | -11.00807 | -44.79946 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b8cb659-6a63-3e29-9d8e-caeb27fc7db9 | -9.24796 | -45.60406 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 208155f2-f4a9-31c5-9081-0be333a53cb4 | -7.51546 | -46.27625 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00d07c17-2fb6-3adc-a61c-7b9c78a56143 | -12.39447 | -49.95976 | 2025-10-28 04:14:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a98ff4ec-1853-3847-a429-282a3860fd8d | -10.09197 | -45.33647 | 2025-10-28 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb45f0fc-f2a8-3a7d-bbf3-2ea8985f8ae7 | -6.23764 | -42.56693 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d922c16b-56a5-315a-a73e-fe6fb4cc6435 | -10.56589 | -49.80469 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5db3040f-2c28-36eb-89ce-35d015b3c55f | -9.96221 | -47.08999 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 80ab8583-98d6-3b21-8b80-2ca7ab9d79f4 | -7.22053 | -46.86447 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ecf2198-2d04-36fb-b463-0e64589a24cf | -10.68109 | -44.58697 | 2025-10-28 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7378489-d5fb-33c9-b5f2-02d74bc007dd | -6.24335 | -41.82828 | 2025-10-28 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2e0970cf-71a8-3ac2-8265-e4c1421b7ae4 | -9.0688 | -45.10719 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fee40d4f-3052-3145-aed7-18fa764b8d6f | -7.78574 | -46.4404 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 85da66fd-ded5-3e12-a2a0-6ac696d73d64 | -12.48567 | -44.21261 | 2025-10-28 04:14:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e31d76e6-06cb-3100-8f89-67fc9a2faed1 | -12.32819 | -47.45553 | 2025-10-28 04:14:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3598a244-60e9-3b79-83b7-5eb3fba2e7d3 | -5.82851 | -53.44835 | 2025-10-28 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22528e37-d800-3117-aebd-dd76a1264c63 | -10.77371 | -45.05254 | 2025-10-28 04:14:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ab4103f-a200-3104-8a5e-598bc24bd354 | -8.64299 | -45.25924 | 2025-10-28 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a072a0f-1fb7-36aa-865a-1e11ff0fff3a | -6.7038 | -42.04095 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7da6e2a2-9a59-3bf2-a40c-a89084c1a1dc | -13.44392 | -44.48031 | 2025-10-28 04:14:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5bcc483d-ab96-3294-a624-560b8342618c | -8.57461 | -47.02909 | 2025-10-28 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b7978bd-e8f4-3da9-8960-a2d2755a8370 | -6.89068 | -44.90045 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a993e71b-ec00-3ad3-9207-3cf9e4c0bd4d | -8.12095 | -45.48969 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26ae1605-0805-37bc-a0c6-8cfee1a7c043 | -7.2349 | -44.9929 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fd66f22-269c-3ec9-9b9f-a260addf2731 | -6.58195 | -41.40102 | 2025-10-28 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a799022-ae8a-3f10-be84-7abae10a8ca8 | -10.95236 | -50.27692 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed9b888d-ee4b-35f5-98fd-a6889400e457 | -9.52042 | -46.1137 | 2025-10-28 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a4d188f-12fe-3941-a450-67a3bf32e517 | -9.18614 | -44.61189 | 2025-10-28 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 225a6e5c-5fa3-33ea-a639-bb1312a307cc | -8.0641 | -46.93803 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d12004f-d462-3849-abec-0434187e86e8 | -12.08996 | -45.67551 | 2025-10-28 04:14:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e19f11c8-617d-3efd-a0a4-447836524712 | -10.41827 | -45.16717 | 2025-10-28 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d1cfb66-823c-38c6-9000-8cbbdda9bbd7 | -7.4566 | -49.40609 | 2025-10-28 04:14:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0676387a-b01c-326c-9387-0c189ecbd35d | -7.26312 | -45.01257 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76749106-06e7-37c6-841e-b77c2091dea9 | -9.54071 | -46.93725 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0d75a91f-c3cf-3530-8829-cca7930bc376 | -7.60253 | -43.58612 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 87368daa-9f77-3917-94c5-b7cfab1f968c | -10.93223 | -50.26464 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d2cd70b-9c14-3bfd-a7d0-4bfa56cd9160 | -7.47163 | -47.1604 | 2025-10-28 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a89803d5-2a0b-36cc-b62f-c19dd036e00b | -8.50532 | -44.0337 | 2025-10-28 04:14:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5504c431-b975-3940-85f5-75a99249dd98 | -5.8415 | -47.56292 | 2025-10-28 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c7107f74-7ec9-35dc-a84e-b47f0eb7c458 | -9.59282 | -44.94415 | 2025-10-28 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ebec425-37fe-351c-a8bb-7011012a48e4 | -10.77194 | -44.76466 | 2025-10-28 04:14:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad278854-9a6d-339f-8d0d-ab8b07e9085f | -12.46868 | -44.49401 | 2025-10-28 04:14:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61e04374-2343-308f-aded-82fbb2da86e9 | -9.24515 | -45.59979 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fb63f2cb-ac84-3f6e-b2e6-4b65aa9f1348 | -10.95668 | -50.2777 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f45d9eb7-e071-38b5-92a1-a70268c6c617 | -10.96269 | -48.05092 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 132f7d93-eceb-3613-be2a-c33dd4105b63 | -10.654 | -44.11296 | 2025-10-28 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b354651-f12f-337f-b52d-4b7326210953 | -12.53548 | -47.54161 | 2025-10-28 04:14:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3c9f3682-20ce-3932-b63a-db7409d3b571 | -10.2179 | -49.89938 | 2025-10-28 04:14:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 522c1be0-90fd-347d-a43d-eaca1fcacbab | -6.10338 | -44.68514 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afcb5e42-34e1-3c0e-a289-1c58cc99efb6 | -7.61402 | -46.47514 | 2025-10-28 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ca662fc7-1bf9-30d7-8521-aaff12512565 | -6.03763 | -46.56669 | 2025-10-28 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c925749-971f-3f82-92ca-7ff9412f72ed | -6.2064 | -43.26796 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 49ecf80c-2fe0-3816-b424-7ce69526230a | -12.61724 | -45.08231 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d176895c-9e5d-3b33-a3ee-5503dc0925c0 | -6.64693 | -43.38739 | 2025-10-28 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 63e946cf-f765-31b5-be3c-615215f66a8b | -10.64659 | -48.01345 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86bdb53b-d149-3a4d-bc67-4612134c6bb7 | -7.97658 | -46.71656 | 2025-10-28 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 889f4b56-b020-3420-b73e-93d9a80f96a8 | -10.92791 | -50.26387 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc5feb69-07bc-3efd-a079-b1d9016a242e | -10.30167 | -47.16977 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ce942c0-c364-3782-b6ed-11984356f755 | -12.38698 | -44.96799 | 2025-10-28 04:14:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e87d3e8c-3dce-3cd8-8231-fc8e0d747487 | -6.10115 | -44.67735 | 2025-10-28 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 79d2160f-b97d-34aa-95e6-678b889d0319 | -6.22597 | -42.53334 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0409a146-b914-3aa3-b17d-26f59700a4e3 | -9.24173 | -45.59923 | 2025-10-28 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5c60b31-72a4-37f4-b561-47f046221b8b | -10.31465 | -47.15878 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b56e654-b83b-3b7f-b241-dc404c7b260d | -9.54162 | -46.97616 | 2025-10-28 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 97c805cb-4179-3c0e-a2e0-ccb3eb16df58 | -8.63213 | -44.79941 | 2025-10-28 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e201d97d-d328-3e3b-a072-3ca90827896c | -10.28664 | -47.23752 | 2025-10-28 04:14:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cb46a51d-0a13-36ba-a763-c197d10abedf | -7.86628 | -46.39816 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 265e2460-ac6a-3335-ad4d-4cfacf0fdb29 | -12.2047 | -46.5031 | 2025-10-28 04:14:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a7589c7-471c-3d69-85ac-f8d829cdb11b | -6.42082 | -42.32927 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c4a27d1-7b60-3127-b244-b47a1ee0536f | -11.21061 | -41.63559 | 2025-10-28 04:14:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6aaa2e1d-4e5e-3bb7-8f31-f7cfe3f43467 | -6.42028 | -42.33274 | 2025-10-28 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 68aca94c-5549-3de5-b96a-fed264efbefb | -6.70047 | -42.04044 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ea32c092-0105-32a8-933d-bc896c1b8d22 | -7.06026 | -44.81083 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8d5abaab-62b9-3379-a151-afa45d7ac861 | -7.08044 | -44.94512 | 2025-10-28 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 677dc085-f0ca-3661-9254-2baa94c1a8ce | -7.59869 | -43.58906 | 2025-10-28 04:14:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd9023d4-90e9-305d-825a-bc663f9a504f | -6.69604 | -42.04699 | 2025-10-28 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9bc65f27-9903-31ef-8c6f-e71b57717be7 | -7.03286 | -47.62225 | 2025-10-28 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db811e5c-5dd1-3aba-bd2a-54678f230c70 | -7.85911 | -46.39702 | 2025-10-28 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bab0ef7b-8461-339a-8243-74812a3d57bd | -10.76597 | -47.90173 | 2025-10-28 04:14:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da2a9be8-7593-3fd9-9cfb-0d3b61adfa1f | -7.94832 | -45.51251 | 2025-10-28 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4be24348-6440-318b-855d-38990f2e4727 | -10.9917 | -50.3583 | 2025-10-28 04:14:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 10659296-d49f-39b8-a54a-20dca4f159c0 | -13.74153 | -48.40501 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2fa93de5-32e6-3073-8f51-9aefc0079669 | -13.73341 | -43.9945 | 2025-10-28 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08d5040c-8ac2-36d3-9623-9b92e76b4149 | -14.76597 | -44.96654 | 2025-10-28 04:17:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9af245e6-7a04-36da-9ee9-4c2106cc2006 | -15.2005 | -47.20742 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f66a8ce7-0662-388a-a46b-3b260e71baed | -13.6275 | -46.46732 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 06a6a6e5-2b0e-32c6-8c6c-e6a5f81bff6d | -14.55102 | -47.98061 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 75b4f22a-55d5-3a18-a3a3-17c1f0e45783 | -15.2015 | -47.39378 | 2025-10-28 04:17:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0335b916-e39a-35f1-a69e-e8cf6476d969 | -14.54384 | -47.97955 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f311bfce-aa14-3b41-bcdd-d0936a9527d8 | -13.62825 | -46.46708 | 2025-10-28 04:17:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13478bd4-4c06-3437-b932-ea1eb3033931 | -13.73786 | -48.43455 | 2025-10-28 04:17:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95317269-fe44-3dfb-abf8-f503f6564773 | -14.24654 | -48.11852 | 2025-10-28 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78cbfb18-d0cf-3a86-8921-297ab8f69f5e | -16.51806 | -43.54497 | 2025-10-28 04:17:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c75f8f8-21a7-3b18-84b1-55e22aa86391 | -13.56139 | -47.16553 | 2025-10-28 04:17:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README37.md)
