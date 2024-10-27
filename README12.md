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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ef47227-106b-394d-9f7e-600eac674b2f | -1.1652 | -53.853401 | 2024-10-27 00:15:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73608a96-2734-3bbe-8946-7244b31c48ca | -1.17 | -53.874699 | 2024-10-27 00:15:36 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c25f0408-443e-392d-86c2-dd5fe9762891 | -0.9778 | -53.653702 | 2024-10-27 00:15:38 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7feaea-35e9-3529-8174-ad49c1edd1eb | -0.9824 | -53.674198 | 2024-10-27 00:15:38 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 984071b0-714f-3995-a46f-cc50fbcfdd14 | -0.9584 | -53.657902 | 2024-10-27 00:15:39 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 369c689c-0dca-3901-911b-ac7beff8da2f | -0.9727 | -53.6763 | 2024-10-27 00:15:39 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10207df2-8466-3953-bb67-82c7e694bfe3 | -0.9681 | -53.6558 | 2024-10-27 00:15:39 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f7d725c-42b6-3f5a-bc02-70118ddef217 | -6.8534 | -45.8794 | 2024-10-27 00:15:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 730faba0-d485-3ea8-82bc-3846aff198fc | -6.8722 | -45.8779 | 2024-10-27 00:15:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 21cb2085-cac0-376d-9308-446ee780a61a | -7.2262 | -46.0723 | 2024-10-27 00:15:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 1235c9e5-52fe-3809-ade5-fafc3b859c84 | -7.2264 | -46.0498 | 2024-10-27 00:15:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2b059c0c-c458-3e6e-8286-98893bbb61bd | -7.2452 | -46.0482 | 2024-10-27 00:15:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 17011892-6661-3aea-bfe8-d8f42b5b9007 | 0.3286 | -50.91 | 2024-10-27 00:15:50 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a63f02c5-7313-3ba9-98c7-56a1e303a8c6 | -9.6459 | -36.0668 | 2024-10-27 00:15:59 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.0 |
| f9d6425d-c70b-3c5e-9ccb-962b810d1e28 | -10.5424 | -45.1463 | 2024-10-27 00:16:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| d9ae5c80-974a-3278-98a9-ff792f2e714e | -13.3798 | -45.1382 | 2024-10-27 00:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 079c5359-5c1c-3a5b-950a-3e9f74e7e044 | -13.3803 | -45.1149 | 2024-10-27 00:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 48abcd12-8f63-3d21-a5c8-f0ee2ba2a0ea | -0.9815 | -53.7192 | 2024-10-27 00:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 9db1a068-1572-39b4-a702-0a0ec27d168e | -0.9815 | -53.699 | 2024-10-27 00:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 339.7 |
| f4c7fe70-0c33-3bb4-ba66-053ce2c6bff7 | -0.9815 | -53.6789 | 2024-10-27 00:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1cfe99ad-0ea5-35af-8152-4f1bcf22b965 | -0.9998 | -53.719 | 2024-10-27 00:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 70fc982c-0eb4-34e3-9ed3-4bd9dbaedaca | -0.9998 | -53.6989 | 2024-10-27 00:25:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 340.6 |
| 9924f7a8-098b-34d2-8d56-462a5c862146 | -0.9999 | -53.6788 | 2024-10-27 00:25:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| ce9445e0-753e-3d3a-aa29-7298472bab32 | -1.1831 | -53.8985 | 2024-10-27 00:25:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 4cc11a6f-d6a9-3054-8348-8e100348e3b1 | -1.7874 | -46.4065 | 2024-10-27 00:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c18b2a2a-9877-3a81-b73c-6e5ae6761ed3 | -1.7875 | -46.3844 | 2024-10-27 00:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 8d9a4f5e-ed00-33f9-af82-fea5875cebb4 | -1.8059 | -46.4062 | 2024-10-27 00:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 7b487b1c-9c3a-31e1-9eaa-764f59a65e1a | -1.806 | -46.384 | 2024-10-27 00:25:15 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 3cd064ce-a13a-3f7c-9620-7ed30d9376c7 | -1.906 | -59.9839 | 2024-10-27 00:25:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| c685bc79-6a12-3d07-bca7-4424b84978be | -1.9243 | -59.9837 | 2024-10-27 00:25:16 | GOES-16 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 69d29ea5-3de0-37e8-95fc-d7897161d11f | -2.3578 | -47.6641 | 2024-10-27 00:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| e81112e0-c9fb-386e-a9d7-57ab01f2ce30 | -2.3763 | -47.6636 | 2024-10-27 00:25:19 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 7046995a-d210-33a8-8098-a148a4467524 | -2.4598 | -50.412 | 2024-10-27 00:25:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 89f779f5-88d9-347a-9835-a1417f68fac4 | -2.4786 | -50.2858 | 2024-10-27 00:25:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| c5ce347c-8dd1-345b-a196-18bf974b7830 | -2.486 | -48.0507 | 2024-10-27 00:25:19 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| d16f263b-cc5b-31bc-a20b-60fe7616d187 | -2.6321 | -54.2975 | 2024-10-27 00:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2e5f331b-5bb3-3a3f-b3a8-20baaa7acd0e | -2.6482 | -49.2465 | 2024-10-27 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 346ab7d6-210b-3d06-b3fa-4da57bb456c9 | -2.6483 | -49.2253 | 2024-10-27 00:25:20 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| cfcd3ce0-eecd-3e4d-873f-1b2cba99a264 | -2.6505 | -54.2971 | 2024-10-27 00:25:20 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 35a7cd72-0504-3484-99ed-c212182bc46c | -2.7033 | -49.33 | 2024-10-27 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 120.3 |
| cfe18df3-125e-316e-b33b-d587f24a8921 | -2.7034 | -49.3088 | 2024-10-27 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| 46931d19-6ed3-3246-b2e5-73433e453057 | -2.7611 | -48.7098 | 2024-10-27 00:25:21 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 2856e6b4-cefd-37ef-9770-3bd82aaa47c6 | -2.8329 | -49.2626 | 2024-10-27 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 98e3c9f9-e429-3800-af7f-d2174a6a00de | -2.833 | -49.2413 | 2024-10-27 00:25:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| f9fd7e18-b42f-3920-9827-acf222378ffc | -2.8465 | -45.8666 | 2024-10-27 00:25:21 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 90fce1f2-f3c7-34d0-a1e6-a7e6c0df0f2b | -2.8501 | -45.0131 | 2024-10-27 00:25:21 | GOES-16 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 546.6 |
| 959d0a57-9d45-3e7b-8d55-4bcc96280526 | -2.8502 | -44.9905 | 2024-10-27 00:25:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 497.1 |
| 9f687acc-be9c-33f1-8515-25d0c8b8279a | -2.8422 | -51.8148 | 2024-10-27 00:25:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| d67b53c5-6ff6-370c-be62-6e3ca107f6bd | -2.8423 | -51.7942 | 2024-10-27 00:25:21 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 506e857f-a9c2-3585-b7e6-50cb02ec59ac | -2.8687 | -45.0125 | 2024-10-27 00:25:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 626.8 |
| 2f1cecf8-e560-3385-be73-cef6e824ad1c | -2.8688 | -44.9899 | 2024-10-27 00:25:21 | GOES-16 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 551.2 |
| 4bdeeee7-918a-3b2a-a45e-cd222070c023 | -2.8939 | -47.8439 | 2024-10-27 00:25:22 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d45f2df4-4266-33f8-9cb2-3dbb6737621f | -2.916 | -51.7716 | 2024-10-27 00:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| d83acacf-4768-3a9b-b5a7-2d1042ecff80 | -2.9161 | -51.751 | 2024-10-27 00:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 218510f6-e32a-358f-99fb-bf93cb74cf5d | -2.9214 | -50.295 | 2024-10-27 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6ad6adfb-9a85-3add-91d4-b57e3c2280b5 | -2.9215 | -50.274 | 2024-10-27 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| b8cf0304-94d1-3cb0-867c-c3c364e69632 | -2.9345 | -51.7711 | 2024-10-27 00:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 5cde09bb-1ace-39da-8ffb-6018f818579b | -2.9345 | -51.7505 | 2024-10-27 00:25:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| d53dc80a-9b2b-3925-a782-98f2351f675e | -2.9399 | -50.2735 | 2024-10-27 00:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| fdcd7039-4a97-3140-a80c-c78a76a8ff1f | -2.9669 | -53.0389 | 2024-10-27 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e82268a0-d6e4-33db-a15f-b13111a0e51f | -2.9853 | -53.0384 | 2024-10-27 00:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 20874327-ffd8-36cc-a2d6-917af7b27ccc | -3.0703 | -45.6575 | 2024-10-27 00:25:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ac82f1b9-ba3a-38fd-8509-0cbf4ffd2d30 | -3.0888 | -45.6568 | 2024-10-27 00:25:23 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 4934fde1-b5ef-3830-a7c8-b929893d90f3 | -3.1106 | -44.9809 | 2024-10-27 00:25:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 47edb926-b400-3776-8931-5594571a3774 | -3.1057 | -50.3525 | 2024-10-27 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 227fc357-17f5-36f0-b704-f89a10d2e956 | -3.1292 | -44.9801 | 2024-10-27 00:25:23 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 8c5e5cc4-4d8e-3f9d-b299-daced9a26f84 | -3.1242 | -50.3519 | 2024-10-27 00:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 2bd5579d-cb41-3553-844f-006d7728db79 | -3.1871 | -58.9511 | 2024-10-27 00:25:24 | GOES-16 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 866b5227-4d3a-30dc-bb8e-eaa049e84e8e | -3.3256 | -50.7641 | 2024-10-27 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 61c90aca-9214-362c-a5ce-4107c33aa7cb | -3.3256 | -50.7432 | 2024-10-27 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 9e8811e6-8545-3752-86f9-64897242eddd | -3.344 | -50.7635 | 2024-10-27 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| b72d8842-a85e-3089-853c-457aef6c3a8e | -3.3441 | -50.7426 | 2024-10-27 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 41561c5c-bba7-3ab6-bd5a-2b53c1fff7d7 | -3.5442 | -51.4223 | 2024-10-27 00:25:25 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 77b45701-4dc5-3e1c-9836-d433896ac8b7 | -3.3925 | -52.4358 | 2024-10-27 00:25:25 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ca0f3df5-fc1c-320b-8be3-f750a6f19226 | -3.4392 | -50.0896 | 2024-10-27 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b672ed7b-71fc-3630-830b-d8873dd0fb4b | -3.4762 | -54.5772 | 2024-10-27 00:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 0a73225c-cd61-3fec-9b6f-a3779201c686 | -3.4763 | -54.5572 | 2024-10-27 00:25:25 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| a621c75d-f09c-3346-8f18-0be7ce2083a8 | -3.5202 | -52.7384 | 2024-10-27 00:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 8972a3d5-16ed-301d-8e94-5abe522288b9 | -3.5626 | -51.4217 | 2024-10-27 00:25:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| ef645893-2740-3782-8606-416537b7385d | -3.8149 | -48.8874 | 2024-10-27 00:25:27 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| fbc174bb-bfd8-334c-8a68-5ba8a209bac5 | -4.254 | -63.153 | 2024-10-27 00:25:30 | GOES-16 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5299bf54-7abd-38a2-bbd3-7c3db4049808 | -4.3841 | -49.7571 | 2024-10-27 00:25:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e39ba713-9f6c-38cc-95aa-b27cd7bf3aa6 | -4.4696 | -50.9926 | 2024-10-27 00:25:31 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 2e37141d-9a11-395c-8a5a-616744da1541 | -5.2896 | -60.1632 | 2024-10-27 00:25:36 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c0659492-b75a-3243-9318-2a8ae180c16d | -7.2264 | -46.0498 | 2024-10-27 00:25:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 372575c9-4371-3b07-8292-4ef043639d9d | -7.245 | -46.0707 | 2024-10-27 00:25:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d2502c1a-2536-3c7f-9f5f-e635413ce38f | -7.2452 | -46.0482 | 2024-10-27 00:25:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| de89f662-0651-39d4-b299-49e990ae88e6 | -7.2455 | -46.0258 | 2024-10-27 00:25:46 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 25242463-3840-3ae0-9bb7-6a24dbccf080 | -10.178 | -36.4313 | 2024-10-27 00:26:02 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 72.3 |
| 48a5f652-8d7e-30fc-bc59-6d541ccd72ae | -10.5424 | -45.1463 | 2024-10-27 00:26:05 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 17b484ac-1bb2-3973-9208-273b6b2bc20a | -13.3609 | -45.1181 | 2024-10-27 00:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 78fe58ed-df4a-30b8-b54d-9c2d13c5fe06 | -13.3798 | -45.1382 | 2024-10-27 00:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8b03b5bd-478f-3a4e-a203-26159c85ce21 | -13.3803 | -45.1149 | 2024-10-27 00:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4e0ad672-23c1-3746-9fa1-524b52869033 | -0.9815 | -53.7192 | 2024-10-27 00:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| bb8f56c4-7063-3c80-88f4-e7d5d5c91c93 | -0.9815 | -53.699 | 2024-10-27 00:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 341.8 |
| 94b25fc9-58a7-3871-88cb-088cad5b8a66 | -0.9815 | -53.6789 | 2024-10-27 00:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| f0e336c5-909a-31bb-bce2-d6d2254d2573 | -0.9998 | -53.719 | 2024-10-27 00:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 8db2ac9e-ecb0-3e07-8881-f8b2f6e7153a | -0.9998 | -53.6989 | 2024-10-27 00:35:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 296.3 |
| 9817f24d-a277-3d28-9516-d6ce56adc379 | -0.9999 | -53.6788 | 2024-10-27 00:35:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| dc439188-f364-3bda-ad49-30e1507ed0d0 | -1.1831 | -53.8985 | 2024-10-27 00:35:12 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |


[Clique aqui para ver as próximas entradas](README13.md)
