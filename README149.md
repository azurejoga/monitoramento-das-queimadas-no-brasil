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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20656a5-d1b1-3e1c-bcf3-0d8826ae3810 | -8.90222 | -46.02787 | 2024-10-10 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 49d25a5f-c0da-3020-99ff-fbebad4a1bca | -8.90093 | -46.03688 | 2024-10-10 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 3cbcfb34-aa85-3cb3-a4d1-ff83ffea8de5 | -9.83181 | -46.61288 | 2024-10-10 12:42:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 184f5088-8c56-3c4d-9b70-a1586f72d748 | -10.14149 | -46.31847 | 2024-10-10 12:42:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9fc44a3c-3564-3ca8-a07b-3c6723641354 | -13.65698 | -47.11337 | 2024-10-10 12:42:00 | TERRA_M-T | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fe0c9195-1a51-3cc7-b8bd-a61cfaa246f6 | -13.40981 | -46.90936 | 2024-10-10 12:42:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 936a80c9-0601-3c24-ba92-745797e79cdc | -13.40091 | -46.90794 | 2024-10-10 12:42:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| 00a220ca-d0f1-3d8b-b47e-7741fae85414 | -13.3996 | -46.91711 | 2024-10-10 12:42:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3551e554-80c4-372d-8727-a72f9ba3173a | -13.39199 | -46.90663 | 2024-10-10 12:42:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 6cbb1942-30f6-3128-8c27-d93893dcf551 | -13.39069 | -46.91576 | 2024-10-10 12:42:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 8bf6dbf8-9965-33e0-9417-400dce5edb3a | -13.38939 | -46.92492 | 2024-10-10 12:42:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 543d01e1-693b-364b-85b8-c8ed4891210d | -12.38343 | -47.06339 | 2024-10-10 12:42:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| ada03796-2e24-3799-9792-6025c930b8a7 | -15.26105 | -48.13052 | 2024-10-10 12:42:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 14f41649-10bf-34c7-aa44-096fa79f4140 | -9.27277 | -48.22771 | 2024-10-10 12:42:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 29341772-0019-353c-bdaf-f906348e5454 | -9.26362 | -48.22641 | 2024-10-10 12:42:00 | TERRA_M-T | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 31633d36-398a-3f64-be25-34fe0e67cd7d | -8.49982 | -48.63808 | 2024-10-10 12:42:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 78.3 |
| a6334c01-fdc7-30a3-90ef-f10b566e4932 | -8.77328 | -47.79957 | 2024-10-10 12:42:00 | TERRA_M-T | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| aaf96e2a-90f6-313e-a921-a0ea5dced959 | -10.62028 | -48.28003 | 2024-10-10 12:42:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 80fe9dc8-28dd-3bb1-82fd-0d3ae845c204 | -10.61889 | -48.28941 | 2024-10-10 12:42:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| af58a01b-a79c-3f9c-9146-5fd34e0107ca | -9.87716 | -48.25357 | 2024-10-10 12:42:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 419779e2-f766-3af4-b8fb-4f60871c0275 | -9.87576 | -48.26303 | 2024-10-10 12:42:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| be6e3342-df21-39b1-8b3b-f5ab220150f7 | -9.86663 | -48.26179 | 2024-10-10 12:42:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8afd0ede-ff1c-3901-b9cd-4aa6a830cc4c | -9.84637 | -48.21059 | 2024-10-10 12:42:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 20d9ab83-99b5-37d6-a31e-d8e77089e041 | -9.33219 | -48.68639 | 2024-10-10 12:42:00 | TERRA_M-T | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 2ffbb812-d8c9-3d1e-ac73-ecec9f4370f3 | -10.05061 | -48.75299 | 2024-10-10 12:42:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d1aa862-78f4-3e4f-9276-29665545b2ef | -10.01028 | -48.85179 | 2024-10-10 12:42:00 | TERRA_M-T | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| ab6df949-e7ff-318a-afec-f919920e0ed7 | -14.8678 | -48.61558 | 2024-10-10 12:42:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 01c3773c-d96a-3134-9709-6d726780aaab | -8.49832 | -48.64801 | 2024-10-10 12:42:00 | TERRA_M-T | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 6ccafedd-6e51-313e-b961-4c6abf102f0f | -9.90946 | -50.07105 | 2024-10-10 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c8fa3b38-b5be-3c49-bb4e-e21198e807af | -9.85386 | -49.3102 | 2024-10-10 12:42:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5d575179-9f2a-39ee-beaf-dc2d981141cf | -9.90769 | -50.0827 | 2024-10-10 12:42:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4a2ff050-d68f-3a16-bcdd-611336b7b3f8 | -9.84909 | -49.31414 | 2024-10-10 12:42:00 | TERRA_M-T | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8661b3bc-f625-3f40-afde-a3dc71fd9cac | -12.19567 | -50.5935 | 2024-10-10 12:42:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 73b2c9a3-545a-343b-b267-30d996f6592e | -12.19384 | -50.60523 | 2024-10-10 12:42:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| be973a25-5226-36fa-82ee-e715c1f13e1d | -9.65497 | -51.79257 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 6b0d3ee2-cb37-3804-b92f-1b9d20914d36 | -9.65737 | -51.78699 | 2024-10-10 12:42:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 6cde1500-0057-3e72-90b3-ac84e20ae90c | -10.32134 | -52.0252 | 2024-10-10 12:42:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 59c39bb9-1aed-33ae-801a-0e85de03c77c | -8.19767 | -50.73825 | 2024-10-10 12:42:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| a5fbb5ea-90ff-3206-967e-2b7258c3f9b2 | -11.09632 | -50.61229 | 2024-10-10 12:42:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a2470036-8e9f-3f29-a1cb-0be183d4e468 | -22.06052 | -46.69256 | 2024-10-10 12:44:00 | TERRA_M-T | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.7 |
| 0a9d546c-a8e9-30bd-ab1c-f76c34ed6c05 | -17.66036 | -56.29692 | 2024-10-10 12:44:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.0 |
| 0e06bca7-82fe-34db-a2bc-11bd0b190472 | -17.68811 | -56.30247 | 2024-10-10 12:44:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.4 |
| d3ceaf24-113d-3f07-bf4c-2cd1672926b1 | -9.5659 | -44.4178 | 2024-10-10 12:46:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 9a0c73c4-cec9-3827-8e0a-fff5e003063d | -9.5655 | -44.441 | 2024-10-10 12:46:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 8d25afdc-df56-3f1e-a10d-6a13d787a4f8 | -10.2052 | -42.4504 | 2024-10-10 12:46:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 127.0 |
| b7a287ec-6c91-3a61-889f-cfd5349ed447 | -10.3116 | -53.7085 | 2024-10-10 12:46:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 198.5 |
| faefe9e9-c0bb-36e3-94d8-f50237a14248 | -10.6084 | -48.2995 | 2024-10-10 12:46:06 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 138.2 |
| c83fd0cd-7097-3ae3-a006-7895fade99df | -11.309 | -51.0038 | 2024-10-10 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 48f8bc36-f297-34b5-bfd3-266ba44eadd4 | -11.3087 | -51.0251 | 2024-10-10 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 243.9 |
| 0b04297d-1a0f-31e2-bf22-dacb3bcddd76 | -11.3084 | -51.0464 | 2024-10-10 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 8b237b02-a925-3f20-9772-bbfaf08ff4a8 | -11.2894 | -51.0484 | 2024-10-10 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 3d7c796f-159b-3d20-b20e-2c8a1d299337 | -11.29 | -51.0059 | 2024-10-10 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 57295197-7844-3d13-bdef-5813f64f4eaf | -11.3286 | -50.9592 | 2024-10-10 12:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8bf41ca2-d654-3064-852d-f9e421986573 | -12.2086 | -50.5815 | 2024-10-10 12:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| e92c8e5a-50c1-3788-881e-020af7f5ce3d | -12.1895 | -50.5838 | 2024-10-10 12:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 7daceb6a-e9b1-36a4-9523-bd4d81f1b49b | -12.2978 | -45.3112 | 2024-10-10 12:46:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 154.3 |
| d819beb3-febc-363d-8fa5-3ebdd15709b3 | -12.2083 | -50.603 | 2024-10-10 12:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| fcfd9339-3c55-3a1f-8e8f-b7bf6627740d | -12.1892 | -50.6053 | 2024-10-10 12:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 4ef3c6ae-4e2c-3dac-a884-0660bf45db0e | -13.4027 | -46.9214 | 2024-10-10 12:46:22 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 114.6 |
| acfc7f1b-5844-33d5-8fa0-4fb161965c56 | -13.8579 | -44.4949 | 2024-10-10 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 025929aa-132c-3628-936f-fc92496bdff2 | -8.6671 | -46.5857 | 2024-10-10 12:55:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 42172eb6-cda4-3f90-b305-c553810c3c3d | -9.235 | -46.4142 | 2024-10-10 12:55:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 71206060-b385-3e91-966e-d665951edfcf | -9.3064 | -45.3441 | 2024-10-10 12:55:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 68.2 |
| abd5ec2e-018b-346c-ada9-9c9b5863ae01 | -9.3067 | -45.3212 | 2024-10-10 12:55:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 76.1 |
| e65e22b3-dcda-3420-aea5-67751e8beb68 | -9.5655 | -44.441 | 2024-10-10 12:56:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 75be8620-15e2-3515-8534-96fe6628162a | -9.5659 | -44.4178 | 2024-10-10 12:56:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 17bde0d7-29d9-31df-9836-2751137ffa14 | -9.657 | -51.7984 | 2024-10-10 12:56:01 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6858ea18-bc7e-39c0-8ffa-1ddf1ca55fac | -10.2052 | -42.4504 | 2024-10-10 12:56:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 133.8 |
| 7dcf0edf-f293-3bb7-b2a0-b32eb0a020fa | -10.2243 | -42.4476 | 2024-10-10 12:56:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 114.2 |
| cf12e561-756a-3f5a-8187-f2036204a2fa | -10.3116 | -53.7085 | 2024-10-10 12:56:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 214.4 |
| 2eb07aaf-c880-399b-830f-684425adeaf1 | -10.6084 | -48.2995 | 2024-10-10 12:56:06 | GOES-16 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 147.9 |
| d1afd6c9-2954-3a09-a2d8-32f1c46ffcf2 | -11.3084 | -51.0464 | 2024-10-10 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| a823e8c5-c28a-39b4-b764-4aaf9a8913a6 | -11.3087 | -51.0251 | 2024-10-10 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.7 |
| c22aec8b-3902-3b95-84dd-27f9df97317c | -11.309 | -51.0038 | 2024-10-10 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 3cd340ba-1969-3595-89ed-0cb00a877deb | -11.29 | -51.0059 | 2024-10-10 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 155.3 |
| f27981c3-0b7c-3c4b-bb13-b313e17ad93e | -11.2894 | -51.0484 | 2024-10-10 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 144.0 |
| 48d08352-a238-3f44-9ba0-74acbe5b401f | -11.7749 | -44.5335 | 2024-10-10 12:56:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 4ce41fca-9c8b-32d2-8c53-5fe2d4ac2caa | -12.2083 | -50.603 | 2024-10-10 12:56:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 1dbae847-7919-37f3-b387-41383c6df84e | -12.1892 | -50.6053 | 2024-10-10 12:56:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| bd56d4b5-f808-31ca-a2c9-0b5faf3b1a95 | -12.2978 | -45.3112 | 2024-10-10 12:56:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 66347439-82c8-37c5-9d97-5e393ece8dcf | -12.1895 | -50.5838 | 2024-10-10 12:56:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| d72a5e6a-9bf0-375e-8aa7-e1dc10aebb7a | -13.1276 | -51.6649 | 2024-10-10 12:56:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 8532186b-e46e-3339-a420-ffc9f119660b | -13.8579 | -44.4949 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ba3be126-03fb-3773-b5c0-7179ca41bb0e | -13.8574 | -44.5185 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| a884568e-ac42-37f2-ad41-fcfe859c5d82 | -13.8369 | -44.5691 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 150.6 |
| adc35219-7fa3-3c68-b11f-5f37a9b0cef8 | -13.8379 | -44.522 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| f3af5782-f963-3e76-9f7d-d6670ce3ea42 | -13.8564 | -44.5657 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 2e1ed41c-35e6-3731-b116-22bdd4fd67b3 | -13.8774 | -44.4914 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 87610069-9dff-39a2-bea8-d3142dd95cba | -13.8769 | -44.515 | 2024-10-10 12:56:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| b2fba658-adc2-3a7d-a349-cad9be89ff8d | -13.79 | -44.54 | 2024-10-10 13:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f66b9a0-c577-3314-aed6-0fa68996c908 | -13.82 | -44.54 | 2024-10-10 13:04:04 | MSG-03 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9aa3af7a-6172-3fe5-b87b-3ab631d3378d | -8.6305 | -46.5001 | 2024-10-10 13:05:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 9b7a34fb-d3e1-3a71-bb27-45e31d2ef085 | -9.3067 | -45.3212 | 2024-10-10 13:05:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| d61e4244-f2ee-3e40-89b8-8cad30cb8514 | -9.3064 | -45.3441 | 2024-10-10 13:05:59 | GOES-16 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| aa223d45-7078-3866-8aba-89aa77566940 | -9.5659 | -44.4178 | 2024-10-10 13:06:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| f5b841f5-2780-30eb-971e-7310f6f526a3 | -9.5655 | -44.441 | 2024-10-10 13:06:00 | GOES-16 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.0 |
| ae0f1684-5d40-3a06-b4ed-5858f08af96f | -10.2243 | -42.4476 | 2024-10-10 13:06:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 115.8 |
| 1ff80e19-1575-385b-8177-a5e605860466 | -10.3099 | -45.4281 | 2024-10-10 13:06:04 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 3f6de0c3-3b39-3b88-86e1-d102e40bd88f | -10.3116 | -53.7085 | 2024-10-10 13:06:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 195.0 |
| 7cfe7d68-bd1f-3f4d-836b-70b624f8ea63 | -11.3084 | -51.0464 | 2024-10-10 13:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |


[Clique aqui para ver as próximas entradas](README150.md)
