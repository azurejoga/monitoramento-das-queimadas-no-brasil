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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b92ea2a-f8a1-3c89-b429-4111591b076a | -14.68223 | -45.11317 | 2025-05-21 05:04:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5ef0c197-6fdd-359a-9a55-5fed043ceb91 | -12.28922 | -52.47445 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73df3421-f25c-3d0a-ac65-000f08159856 | -14.04696 | -56.06561 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28ed850e-7ad8-34ce-8bfe-4d42899284e1 | -12.47857 | -57.18298 | 2025-05-21 05:04:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eabdc262-2682-30fa-8284-44b70c213cde | -12.33819 | -49.95673 | 2025-05-21 05:04:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d1ff99b-316a-35e9-9bd5-fd1170b08e36 | -14.01848 | -55.13609 | 2025-05-21 05:04:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cf4dc33-7036-3616-ab68-1e3ea0f632a0 | -12.40665 | -52.15033 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51f067fc-ee01-3f2d-9106-07f8e36df90a | -12.41017 | -52.15442 | 2025-05-21 05:04:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2534d4a5-cf7c-3977-8475-67189350fe4f | -17.70868 | -47.49463 | 2025-05-21 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9405fae-7932-3866-ab52-43a548b55249 | -19.05467 | -53.45644 | 2025-05-21 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d169b66f-3b64-3765-9174-fad7280db557 | -16.28411 | -58.66723 | 2025-05-21 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f478b892-a04d-3c1a-9b2e-55f655ad02c2 | -17.76284 | -56.31207 | 2025-05-21 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| e8759c01-1a93-319b-ba96-33325890f418 | -19.06063 | -53.44235 | 2025-05-21 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8c2767a-3482-32aa-9721-b75a417d8f6f | -19.11025 | -52.69323 | 2025-05-21 05:06:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdf7c2a9-9070-371a-838d-8d0f317d3268 | -17.15122 | -54.01165 | 2025-05-21 05:06:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86dd9c45-b111-3015-bcd6-42e50552fab8 | -20.95287 | -56.61112 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 992b0dd4-c2b5-3714-bd46-c8d86901ea96 | -17.6953 | -54.09156 | 2025-05-21 05:06:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbaa4b46-086c-3e8d-b4ca-8213072169cb | -15.2751 | -60.20905 | 2025-05-21 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f5c389c-40d0-384c-bf9b-541fd77f40dd | -19.82751 | -54.58371 | 2025-05-21 05:06:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b022f8c-ca0c-3235-92b0-ddd4b20a279f | -19.11346 | -52.70201 | 2025-05-21 05:06:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03782ee6-1888-3438-a39b-1aca7380dabc | -20.47879 | -53.67519 | 2025-05-21 05:06:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 623f0701-e579-3bbe-b439-5cd917eca8d5 | -19.16141 | -47.82234 | 2025-05-21 05:06:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6c198b9-a338-39df-9ae6-c747bd1638f9 | -21.67514 | -57.65398 | 2025-05-21 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5294592f-b9d9-3a5e-8169-617b0396784b | -21.05363 | -55.99676 | 2025-05-21 05:06:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 47e3c987-1d76-3b87-866d-4fb42d8c9319 | -20.95405 | -56.60281 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e2df89a4-ba9e-3b89-b0b9-65c99fb48966 | -20.95636 | -56.61169 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68e86e43-a9b5-3699-be9c-84963d056901 | -19.74119 | -54.5091 | 2025-05-21 05:06:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61af2a56-4aef-3f91-9e79-10e1bca6eae1 | -19.73672 | -54.51344 | 2025-05-21 05:06:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe2d89c1-f3ac-349e-bce6-de343f6506d7 | -19.16095 | -47.82044 | 2025-05-21 05:06:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2478a700-029b-3061-9618-d3d6f8b24e57 | -20.96045 | -56.6081 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f26fa10c-d5e7-3788-9a14-03138049e60b | -20.62269 | -55.03204 | 2025-05-21 05:06:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| deb78e87-ae11-3083-9ac9-7d0191951d2d | -17.7594 | -56.31152 | 2025-05-21 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| a51bbf15-b096-3f8e-8209-36ac544b28d9 | -19.73736 | -54.50858 | 2025-05-21 05:06:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba876831-65f4-39b6-86dd-320107d4a4d7 | -19.0587 | -53.45704 | 2025-05-21 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a1585c5-4db0-391c-a2ea-91c4a2c3d866 | -19.11398 | -52.69793 | 2025-05-21 05:06:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c5b88cd-35b6-3530-9d9a-4ab25663340c | -16.28353 | -58.67084 | 2025-05-21 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 2ffecfb0-c6d7-341e-909d-cd26f6037dc6 | -16.28078 | -58.66665 | 2025-05-21 05:06:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2f4f737c-1666-302c-bf6d-a03cefa4f7ba | -19.05918 | -53.4534 | 2025-05-21 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0f159252-53c7-3ac0-a9f5-c4aaed77fc0e | -17.69459 | -54.08901 | 2025-05-21 05:06:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 619bc0c9-0ffa-3432-aa08-acb9297df867 | -17.70823 | -47.49894 | 2025-05-21 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9cc6fd2-48f1-31b5-974a-2b7cc6608c11 | -20.94996 | -56.60638 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51a53792-97eb-3d7b-86ac-a8e4dcc8757c | -19.73289 | -54.51289 | 2025-05-21 05:06:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2348239d-ad1c-3b50-b597-6fed2203a610 | -19.1618 | -47.81849 | 2025-05-21 05:06:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caa6c6d4-f383-3370-83a4-978b3720c43a | -19.06015 | -53.44604 | 2025-05-21 05:06:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09c97bbe-d5aa-31d7-9779-f1ec558dc52e | -17.70746 | -47.4967 | 2025-05-21 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66fdc20e-d568-3c32-8d7e-c2ab682534c7 | -20.95463 | -56.59866 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6726aab-1dcf-3664-9028-78d8ea9a2078 | -17.70237 | -47.49837 | 2025-05-21 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15412127-95e5-31ba-91af-a55c0ddd9b3f | -19.70276 | -54.56416 | 2025-05-21 05:06:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c32ba9f7-ad61-3709-9a65-8cbcdecbb0fb | -21.441 | -57.12916 | 2025-05-21 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b772ebe-d95f-3752-a0af-d9c06be64ccf | -21.67456 | -57.65788 | 2025-05-21 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1367c1b5-eba2-3065-b89f-b242481e2035 | -17.11977 | -53.18535 | 2025-05-21 05:06:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46b8d093-f3f2-373c-ae96-b2b31997729f | -20.62205 | -55.03689 | 2025-05-21 05:06:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 453f2db3-49f4-3568-aa3a-f6f1aed863f7 | -20.95695 | -56.60753 | 2025-05-21 05:06:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5ea0cb55-37fc-3445-aa32-217699509fc2 | -17.75596 | -56.31097 | 2025-05-21 05:06:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2db125fc-00a5-3d29-9087-a523b3106a6b | -23.60554 | -48.29492 | 2025-05-21 05:08:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0a7517b-2203-3228-bea2-7f79d2e24832 | -23.60591 | -48.29044 | 2025-05-21 05:08:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 222d34cb-4b1e-3d2f-a3f9-b3b875b2fe29 | -22.31404 | -53.63042 | 2025-05-21 05:08:00 | NOAA-20 | IVINHEMA | MATO GROSSO DO SUL | Brasil | 5004700 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 314c4001-dd82-3eec-9957-5df15e32caed | -25.19986 | -49.32373 | 2025-05-21 05:08:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82f3fe27-e8e8-3631-93e6-7b443d16c18b | -25.19381 | -49.32767 | 2025-05-21 05:08:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ee7cdc4d-191a-35d7-bb11-a22a25a5435d | -12.2946 | -52.4785 | 2025-05-21 05:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| f9e75e85-9e68-3f7d-9bb3-82dc653b6768 | -11.0901 | -54.7852 | 2025-05-21 05:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4c2e8367-ab02-3f06-b559-80b475f5955c | -12.2946 | -52.4785 | 2025-05-21 05:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9ecf18ce-9ea1-3b0e-94b3-ae9d1e172440 | -11.0901 | -54.7852 | 2025-05-21 05:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 8455c66a-c344-36a1-90bc-ba9ba5a5ccca | -12.2946 | -52.4785 | 2025-05-21 05:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 643267bb-10a5-3686-a190-d6906f170c01 | -11.0901 | -54.7852 | 2025-05-21 05:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c862689d-785e-360d-bc61-daa7a47a7a30 | -11.0901 | -54.7852 | 2025-05-21 05:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c4a138ba-213f-35eb-8da6-26420aaba333 | -12.2946 | -52.4785 | 2025-05-21 05:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 5332859b-0a79-3cfa-a7ea-8320874387cd | -12.2946 | -52.4785 | 2025-05-21 05:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 26c82365-12e8-384b-b924-39afaa90c05d | -11.0901 | -54.7852 | 2025-05-21 05:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 4a616440-8c6d-3190-a568-841d425365d3 | -12.47807 | -57.18771 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0ba2a1dc-9aee-3144-bbd9-4f1e42f4cd6d | -12.68632 | -58.13145 | 2025-05-21 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ec9ecb-ccfa-3bc7-8141-918d7b934a43 | -12.68688 | -58.12628 | 2025-05-21 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01df1ce0-b610-3ece-a3e3-c63ebfe02e20 | -12.69258 | -58.13241 | 2025-05-21 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c98da8f-6059-3a46-81e5-d93a9d93a4c2 | -12.68863 | -58.13017 | 2025-05-21 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2545937e-1f7b-3d7f-bc09-d36d2023b98b | -12.48902 | -57.19094 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4989411-721f-3cb8-b66c-7d925d7afbd1 | -12.68805 | -58.13528 | 2025-05-21 05:55:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7afba88-c624-3969-9e2f-2eb291dfd7ea | -10.05516 | -64.99751 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b967fd93-9b87-36c1-902a-3a66a324546a | -12.48401 | -57.1946 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 50047e72-61e2-3f10-9533-0dc012747b54 | -12.4758 | -57.18905 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0391f700-7f4f-3d7f-aa24-b954b0aa73b0 | -12.48241 | -57.19006 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b418d55-0378-3ad1-8cc7-f82158251726 | -10.05448 | -65.0023 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b1977862-9568-3f86-a1e0-11f044ea411d | -10.05132 | -64.99693 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11436150-1cd5-38d5-bc4c-7576b25e12d4 | -10.14923 | -63.58402 | 2025-05-21 05:55:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77b7b9af-eb58-3204-b7a1-4f09e123a8a6 | -12.49063 | -57.19538 | 2025-05-21 05:55:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4fd4bfa-6c80-3e47-993f-d02485eda40f | -12.2946 | -52.4785 | 2025-05-21 06:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| e1c219bd-e887-35ac-b367-91aac82d65cc | -11.28857 | -53.97366 | 2025-05-21 06:03:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9d625e8a-7b1e-3c9b-b5d4-12b7aa41a046 | -11.07293 | -54.77763 | 2025-05-21 06:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8cbb86ef-ac41-3730-ba2c-950a8163478b | -11.07956 | -54.77515 | 2025-05-21 06:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| afc7e896-9daf-3fff-bfe3-aab8a1927a0e | -11.07139 | -54.78758 | 2025-05-21 06:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 59ca42b1-4f9d-3de4-8aad-e21788fce8a2 | -11.07798 | -54.78509 | 2025-05-21 06:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 8cc9001d-8cb4-3cd2-a318-9a673e433770 | -11.64947 | -48.0946 | 2025-05-21 06:03:00 | AQUA_M-M | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d0c8bbca-eb86-3cb4-8003-09a53300e322 | -11.2979 | -53.9809 | 2025-05-21 06:03:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0691831a-67cd-369e-a890-548896d17368 | -12.36316 | -49.97402 | 2025-05-21 06:03:00 | AQUA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b4903bbe-4d6f-3d02-8ebe-547143510a64 | -11.14006 | -53.92473 | 2025-05-21 06:03:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 19c8f696-4c4d-3392-babd-432654b67e2e | -11.07447 | -54.7677 | 2025-05-21 06:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d0a5d31e-a929-32fd-b409-2190d7413f12 | -11.08115 | -54.76522 | 2025-05-21 06:03:00 | AQUA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 34ac5dc5-5474-3177-a358-823927e44c4f | -12.29275 | -52.4763 | 2025-05-21 06:05:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 930d503c-b1be-3a3a-a2f0-952ef4ac7412 | -12.28258 | -52.48398 | 2025-05-21 06:05:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 8395b1b6-a268-3bc8-82f2-163675e1fd81 | -12.30024 | -52.48664 | 2025-05-21 06:05:00 | AQUA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 606991f4-2e7a-340a-8971-89ec17ab97ed | -12.72356 | -54.96817 | 2025-05-21 06:05:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |


[Clique aqui para ver as próximas entradas](README19.md)
