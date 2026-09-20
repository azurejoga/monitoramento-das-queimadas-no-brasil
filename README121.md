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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d57d5182-cd38-33ca-8996-05476bb63710 | -10.2787 | -50.2605 | 2026-09-20 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| a1efc6d6-de3f-3c05-a22f-e1ea27ec4a26 | -7.0098 | -45.257 | 2026-09-20 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 93a36ab4-dd8d-31e2-bf1f-7defbb518ab5 | -7.3708 | -44.8606 | 2026-09-20 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 4256ca03-e524-3421-8bc7-629ad6e3a596 | -11.1369 | -54.0251 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 8f1f7164-5b35-3586-b6dc-f5d0c14495ce | -3.3 | -57.8681 | 2026-09-20 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 079a48d5-5a4f-3cdd-bab8-ef57a01310a5 | -12.0072 | -50.047 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 95678874-0104-317d-a74a-271d43cea57a | -9.2865 | -48.2453 | 2026-09-20 13:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d9241928-cf6c-3a7f-a131-d43a1063cd92 | -12.1711 | -47.0356 | 2026-09-20 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 77be646e-c0c5-3d87-b810-58ed24500ca1 | -2.9143 | -58.3401 | 2026-09-20 13:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 7a9cedc5-929a-3e31-995a-028bf1999a97 | -8.0892 | -55.3511 | 2026-09-20 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 617f85d4-c618-338b-a195-d02cab49153e | -11.6621 | -50.2169 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 19d76b1a-d924-3a90-9c9c-23f28f9bd591 | -8.4376 | -46.8757 | 2026-09-20 13:50:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1b160c62-e7ff-3b27-9282-28bde1b0b62e | -5.9795 | -52.2046 | 2026-09-20 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 163.7 |
| 9bf9e739-ff21-3105-a1af-507f103e465b | -10.6703 | -50.6465 | 2026-09-20 13:50:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c48dec06-f407-32fa-bbf3-4471a2b8a2ad | -7.9637 | -44.0667 | 2026-09-20 13:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| ece7afe5-fa1a-380c-bb50-32bb520e5e83 | -7.2691 | -45.5737 | 2026-09-20 13:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0a1164ce-b2c9-3a8b-a232-6618bafe78e8 | -6.4486 | -59.9717 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.0 |
| e144d1a7-7067-32d4-b9a0-e6b774538579 | -8.0706 | -55.3522 | 2026-09-20 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2c5d365b-177e-3a15-9e97-6c7bfbacace3 | -9.8397 | -46.4361 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 472.3 |
| 4f1189d5-049c-3a45-9064-a564b9419998 | -8.754 | -44.2589 | 2026-09-20 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 9911ee60-2ac9-3eae-928e-9a3e3853eb67 | -9.0087 | -44.9897 | 2026-09-20 13:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ffc3e26a-447c-3732-97b8-a3fb130030f1 | -11.1545 | -42.8124 | 2026-09-20 13:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 315.7 |
| 87383a5e-f14d-3f2c-a0a5-0db2fb25608c | -11.1183 | -54.0062 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.8 |
| e80c9f9a-aef6-30f9-99d2-ea7a61cd42f0 | -12.027 | -50.0015 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4bbf3c73-52a2-379b-818e-52593a875340 | -9.2606 | -45.9164 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 322.1 |
| 55f26f2b-8769-3616-8859-11a356a3b3d4 | -9.2756 | -46.2077 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 690771ff-f410-314f-b19a-85ec4b10b032 | -3.3492 | -59.8861 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 23aec129-761e-3e04-9ff6-241de958b053 | -8.7003 | -45.4567 | 2026-09-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 943e787b-9b5d-3164-a48b-2f374630fef1 | -13.2602 | -51.7548 | 2026-09-20 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 8602ea86-e7c5-3035-94f7-1906b2afa652 | -7.2519 | -55.5994 | 2026-09-20 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 98a8b028-50a4-3faf-844c-dc7b3a29c472 | -9.3609 | -48.3251 | 2026-09-20 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 92873f0f-3794-3ca7-a9fc-4998a3ba2f02 | -12.2344 | -50.1488 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| b7550fa4-2a0c-3f20-a32a-17d155b031df | -11.155 | -42.7885 | 2026-09-20 13:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 257.8 |
| dd73e18d-cd4b-3fe4-b4f3-c39839a5ed41 | -13.2219 | -51.7595 | 2026-09-20 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| cfe0a886-6dc2-3ba9-98f7-15b51b96870e | -6.7406 | -44.0909 | 2026-09-20 13:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 48d5fc10-8005-3b1e-b881-f301b2aa08a2 | -2.8974 | -57.7987 | 2026-09-20 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 157dd6a1-3ca3-3663-a889-98f28fdd07e3 | -12.5415 | -50.046 | 2026-09-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f16b73bc-f905-34f3-a72a-988941ca7289 | -3.3675 | -59.8857 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| d05f3fb6-406d-36cb-ae0c-67eff3a5707f | -12.2341 | -50.1703 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 3271af01-97ea-3685-a168-1c1b7ac71979 | -12.8893 | -51.0124 | 2026-09-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1c8901b8-6df7-3acc-b19d-a9c3c55a2f51 | -9.8313 | -48.4073 | 2026-09-20 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 210.6 |
| 3c9871d0-b163-314f-b111-6726a77f2e16 | -11.041 | -54.1567 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| d61caf19-4a4c-3c0c-90d9-e4a9e64aa53f | -5.8411 | -53.5002 | 2026-09-20 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 4fecc88b-4657-345e-b84e-a14512bd71f3 | -11.0065 | -48.3187 | 2026-09-20 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| d3f0068d-3100-33e2-8b41-355dda056856 | -12.8701 | -51.0148 | 2026-09-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 0dc12066-d7e5-3972-9fdc-adb0d8afed62 | -12.9088 | -50.9886 | 2026-09-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e9c57419-c0b5-3d38-80c1-a9887627cc64 | -8.8827 | -45.935 | 2026-09-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| febe3153-cd79-35c3-b96c-078164551167 | -12.7621 | -46.18 | 2026-09-20 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 9f1b0a7e-91f8-38ac-819c-202457141d9f | -2.7826 | -59.896 | 2026-09-20 13:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 0b469834-f17b-3bc6-92b1-944af5fd2e07 | -2.8009 | -59.8957 | 2026-09-20 13:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| e0e7a37e-e7e2-3a62-889d-5284bdecb191 | -3.3454 | -42.7597 | 2026-09-20 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 2dc29ec8-5244-34f0-a401-574532b6d57e | -9.2603 | -45.939 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 666.5 |
| 070f362c-90de-3b00-8f1f-88f323917fec | -12.0263 | -50.0447 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 2aab315c-fd80-3731-be21-934b4badd347 | -3.3675 | -59.8666 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| d2d1917b-9130-3dc7-a1b6-e73162cac876 | -8.7733 | -44.2336 | 2026-09-20 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 1e1dead1-1ed1-3c22-81fc-6b5b77aa7da9 | -11.0994 | -54.008 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| dbee9e35-6698-3d17-8609-c48d0acffab1 | -12.152 | -47.0383 | 2026-09-20 13:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 5ce53da8-cfc0-3fd1-800b-20abbb03241b | -13.5907 | -51.4794 | 2026-09-20 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| b90fdc37-1c97-3e40-bbb9-4aa83a0b9d41 | -13.9641 | -47.8464 | 2026-09-20 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 02746f2a-cd87-392f-88a5-7497c9cc5cd9 | -8.1688 | -54.7432 | 2026-09-20 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 278354dc-741c-3a25-b05e-060a30fd83d1 | -12.5081 | -50.952 | 2026-09-20 13:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b795312b-1d08-3b0c-95c0-0db5be12adc2 | -8.845 | -45.9391 | 2026-09-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 125470fb-3390-3fa3-81b7-72a34316fc83 | -6.3198 | -59.9572 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 6eaa4374-74b7-34c9-a7be-428b2108a3c5 | -14.1458 | -45.5638 | 2026-09-20 13:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 335.2 |
| 358d7a88-a6a0-3dc6-9a2b-9726a8977017 | -10.6889 | -50.6658 | 2026-09-20 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 454af371-9a4a-3645-9a35-588eb4ab7683 | -10.9301 | -53.9618 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1331a5a5-9f4f-38a5-817e-cd47527b8a05 | -13.2606 | -51.7335 | 2026-09-20 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.3 |
| fb88b988-c022-340f-91f8-1e12cbbe5dbe | -6.4485 | -59.9909 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 307c0ce5-b4a6-3d8d-b7a4-abb476905fca | -11.4714 | -47.776 | 2026-09-20 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 3005dc31-e49f-3c1b-ab3c-cc5dde621a6a | -13.241 | -51.7571 | 2026-09-20 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1da026c4-dab8-3da1-b45c-7efe12a3e6f3 | -2.9326 | -58.3397 | 2026-09-20 13:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| c0d28e76-f579-3e3e-b987-c48a8f2f55de | -9.3577 | -50.0943 | 2026-09-20 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 65dfe83d-010b-3c0d-8ce5-8f51f109a105 | -8.8636 | -45.9596 | 2026-09-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 173.1 |
| c83b1afa-6769-3241-8526-d1e2a9a21783 | -6.1359 | -59.9446 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 8dd9379d-728c-3696-bf12-269f3b911d95 | -12.0652 | -49.9969 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b6a6d141-d647-3505-bdb4-750fa03b62fb | -9.8502 | -48.4053 | 2026-09-20 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 262.9 |
| c12f2c44-d474-35e8-9f71-3df7de55b2a9 | -10.8757 | -57.1554 | 2026-09-20 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 838435fc-a6f6-3112-b56b-516ce494fc2e | -8.8825 | -45.9576 | 2026-09-20 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 4603d2fd-bff4-3f0f-bf23-2e0fc5cef20c | -12.5224 | -50.0484 | 2026-09-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| eb29ade4-8f6a-381c-bdfb-a644a34416ae | -11.118 | -54.0268 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 202.7 |
| cd0646a4-4d71-3b99-8b3d-4a6677b043a6 | -11.8744 | -50.0199 | 2026-09-20 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.4 |
| ee6c9b20-46f2-3021-b171-ff8fcec0c22d | -5.8088 | -55.7095 | 2026-09-20 13:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 40eaf5f3-2f6c-344b-a992-b78b4f898ebc | -11.0506 | -54.9309 | 2026-09-20 13:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 251.9 |
| e8d15ecc-ef74-3688-9128-2331cc8b92ba | -3.3492 | -59.867 | 2026-09-20 13:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 18d4eba4-d5fa-3372-8768-d5ca6c58614b | -10.9665 | -49.7583 | 2026-09-20 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 924b4c41-7de8-3d6c-9cf9-57e002ceb708 | -3.3183 | -57.8677 | 2026-09-20 13:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 37c9cd45-bc86-31c0-b6e1-904ead475eaf | -13.5911 | -51.458 | 2026-09-20 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| d7e3f2d5-afb5-37e0-b7d2-6657c6c30fc0 | -9.2567 | -46.2098 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.0 |
| adcf85a3-4d38-3d05-95bd-eed27ceeac78 | -11.0259 | -48.2944 | 2026-09-20 13:50:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b327ccde-6b1b-3c62-8b8a-8444e8cb7ae1 | -10.8553 | -50.9459 | 2026-09-20 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 95432d6e-e095-3831-903c-644c5643c16c | -6.3199 | -59.9381 | 2026-09-20 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5d9c886a-6538-31c0-b425-2443fec4d0b4 | -10.4673 | -45.0873 | 2026-09-20 13:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| c701027c-3995-30ee-b0c0-54a17ad597a2 | -10.3917 | -48.8915 | 2026-09-20 13:50:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 15fc72d5-61d4-3f60-abb4-18269ddfda19 | -3.364 | -42.7824 | 2026-09-20 13:50:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e2d5a8f2-db22-30f0-ac84-28d2b8d14710 | -2.8974 | -57.8181 | 2026-09-20 13:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ee6d7aac-1506-3f8f-9847-af22baa693f8 | -10.8921 | -53.9857 | 2026-09-20 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e4d73997-e437-318e-a6fd-f86c9b5ccd57 | -12.5039 | -50.0075 | 2026-09-20 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 76c8dfa9-0d97-365f-8e60-28632ba8626e | -9.2414 | -45.9411 | 2026-09-20 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 2d4b5f17-933b-3039-910b-6c756bf19536 | -15.866 | -49.9177 | 2026-09-20 13:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 3ade0ff2-6b52-3145-880a-1ad1e7e09cd9 | -10.7899 | -46.3429 | 2026-09-20 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |


[Clique aqui para ver as próximas entradas](README122.md)
