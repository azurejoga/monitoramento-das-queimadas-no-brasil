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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 306c5da3-16f8-3131-93d0-d07f872a9912 | -7.91396 | -44.10106 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45017abd-95ed-3741-900d-469a2af827fd | -3.35145 | -48.39059 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a49c8dff-9b57-3992-8aa2-4a38638205a2 | -5.69456 | -51.75844 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e753a097-b76c-36bb-a617-cae6fc2cb54e | -5.99645 | -43.92086 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d70bd129-7c48-3988-b8e1-ce962ef063e7 | -5.1456 | -45.70631 | 2025-09-21 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8053094e-311d-39e0-bdb9-b67e6b94036b | -3.86835 | -43.09334 | 2025-09-21 04:55:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e97ea8c3-4c9c-30e9-a820-85e30501f246 | -3.84293 | -55.59958 | 2025-09-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18906f54-3585-31f9-b977-2195f7d80cec | -5.69459 | -51.7351 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c14d0c9-157d-321c-be97-87e590f78ec2 | -3.51253 | -49.93898 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a846686-7c24-3d88-9688-659042738d05 | -5.52356 | -43.86266 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9d2d338b-93ad-3562-96e7-b8e42645f3ef | -5.6097 | -52.15174 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 930ce2c4-f533-374e-940d-4c64e0bdb59f | -5.62387 | -51.69762 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7a62f15f-5fbc-307f-9d48-0fa1a94e14d2 | -3.35483 | -48.39829 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e1ad5a14-b0a6-3a81-b47b-730a2f2c9d8a | -3.30496 | -48.71393 | 2025-09-21 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 021f28a7-d197-3089-ba74-27c56d995a6a | -5.6435 | -51.70845 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03211093-351a-3a37-b85d-f7ce64fbb980 | -3.59005 | -43.91655 | 2025-09-21 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 332707c3-acfd-3519-98c3-a8d4e6828110 | -3.83079 | -51.1992 | 2025-09-21 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd8038d1-3cc3-3d17-8533-52c6c95422e3 | -6.17065 | -43.69271 | 2025-09-21 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 417034e4-1997-388a-bd59-3587cde7dd46 | -2.01966 | -49.45775 | 2025-09-21 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b008b7cd-92b7-3b8b-9275-c043409120ab | -5.51789 | -43.86168 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3a26db7-0f16-3df0-b636-d89e73301517 | -5.00983 | -45.20824 | 2025-09-21 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a169fa1f-4a4b-38de-96e5-7573bbe0e28d | -4.55178 | -50.23077 | 2025-09-21 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b82707b5-0fd6-3c12-b1c6-9d51b1427b9e | -2.92002 | -48.30054 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e12ca301-2e9d-3624-b498-1279f3885180 | -5.56329 | -42.15454 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 1216b29e-35c4-3da2-9d31-e0f962681d78 | -7.42701 | -44.54396 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dca106fe-2537-3b62-9d73-ac59ce325fdb | -7.71952 | -44.45236 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1986de8e-6419-338e-bb28-60b562ba5d00 | -3.59428 | -58.58889 | 2025-09-21 04:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3cd2ec48-4690-3c96-9152-b8d598c36e88 | -7.42142 | -44.54319 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22aed966-964a-3428-b0e5-7458b044d27f | -3.60819 | -47.53674 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a467e7b0-c390-3f04-b985-bb5aa672eddd | -1.23737 | -54.1621 | 2025-09-21 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0091162e-fd74-30ff-91a7-2409e04a02e1 | -7.73029 | -44.45788 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c9d5c9e4-3fa1-34ef-bbcb-d83c485bf5ab | -3.20644 | -51.59031 | 2025-09-21 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8095a8bf-a16d-3a1f-a429-19ac15b06c67 | -5.55844 | -42.1432 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 12bfe209-be53-3bc9-8e86-ce747f6c1521 | -3.81428 | -49.10394 | 2025-09-21 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df6d997a-ad3f-3ac7-a132-263a5dc70d52 | -5.56069 | -42.14262 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 59a8827b-61fc-3c24-959b-3e6ea1505481 | -7.9134 | -44.10521 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7195828c-cad5-363d-8986-a8c4dc332386 | -4.47756 | -55.08849 | 2025-09-21 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| fc4f8764-49f3-324c-9310-72d8824bda24 | -1.345 | -47.74691 | 2025-09-21 04:55:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a49e858-282c-3347-bb0c-084cebdee690 | -3.69218 | -49.55261 | 2025-09-21 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 568d8f47-80ce-3a71-9552-d98ecc54e164 | -3.32547 | -54.91179 | 2025-09-21 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b456030-fbc8-33c3-9aa9-f3a07b44f14f | -3.84598 | -55.92915 | 2025-09-21 04:55:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15ee5412-b849-39d3-a14d-b1c076ee6986 | -3.75638 | -53.35203 | 2025-09-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 357a6f08-f7ab-3359-b131-3bfde714b26a | -2.26548 | -47.84644 | 2025-09-21 04:55:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3de0fc6f-447c-3a29-bd2f-88e5937a8d0a | -3.35835 | -48.40244 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ceda3b5-015d-310f-b149-e232b7f2b7bf | -3.32667 | -52.54333 | 2025-09-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a651c21-87e1-3833-b482-c4feb45816da | -5.63591 | -45.96141 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 504db8f2-a2b4-3814-be5f-dffcf6a5f269 | -3.75723 | -54.81073 | 2025-09-21 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2c1acdc2-3b76-3d58-84cc-45f00c0a9be4 | -2.93414 | -54.08453 | 2025-09-21 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| acd6010f-6f6f-39e9-b86d-5f7605ea47e7 | -7.71695 | -44.47157 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0914eb95-aff4-3c97-b32a-5c1db0e2e70b | -3.64933 | -58.16004 | 2025-09-21 04:55:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fa453f84-1745-385b-b254-c345c01c09bc | -7.4769 | -46.66322 | 2025-09-21 04:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a14e389-c867-364a-8d94-7c465be46802 | -5.27155 | -44.81614 | 2025-09-21 04:55:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60534fc9-5d1d-3271-9b30-df5bf6f623e7 | 0.7916 | -51.96884 | 2025-09-21 04:55:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba0c7e57-9429-30ea-83ea-981c376d633d | -2.61869 | -46.85256 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0aebec22-388a-33d2-a243-a341866f9ec6 | -5.56196 | -51.80094 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba17e0fd-2b91-3d8b-9af8-7c0e24f73352 | -3.60449 | -47.53204 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91a5a9d8-1057-3f96-b19e-4cf9f8ba3b72 | -2.30244 | -48.14886 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fafbf678-a5ea-3d5c-b732-11d1e740e0cc | -5.99589 | -43.92483 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 958363b1-9a5f-3a39-a844-0712f324e059 | -0.99276 | -47.06302 | 2025-09-21 04:55:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b7e91e0-e213-3312-ad3d-0b13b2175d96 | -5.56477 | -42.14426 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 34a3c204-57a1-3a82-bc33-e2394dc7bf21 | -5.69573 | -51.75086 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77c8d3f9-730e-3764-8bcd-bc90a3065b13 | -2.91946 | -48.3041 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 63bed7ed-dec5-3f2b-b32e-fdd7d6f3c7f3 | -5.34567 | -45.00583 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faf5ccb9-e516-3123-838b-c3bce401b8a1 | -7.61939 | -44.44577 | 2025-09-21 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8113e394-80c3-3cc9-9cce-7d7e83f64e33 | -5.01197 | -45.20667 | 2025-09-21 04:55:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c320ef27-39f1-3dd1-a18b-287e2fa485db | -5.56967 | -42.1553 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3bd749e4-6c5c-3175-817a-674b73cac0b7 | -2.73654 | -49.54685 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd295514-d8e4-3f94-926e-0fd3ba443c55 | -5.33881 | -44.90477 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 66fb2fd9-f2a0-3dfb-9278-0ccb793157f9 | -1.12182 | -54.14103 | 2025-09-21 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 630fc39d-de10-33ef-9c28-75573f655e3f | -5.55998 | -42.14787 | 2025-09-21 04:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 41d6b57c-1b6b-3f70-aa99-d3be3d127cdc | -5.52864 | -43.86766 | 2025-09-21 04:55:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f404a61d-68fd-3137-9e24-810ad06c85e8 | -5.53018 | -43.87096 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a76f24fc-4272-3321-98b2-56c26701e695 | -3.4549 | -52.57045 | 2025-09-21 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d48e51c9-f5dd-3efc-9cec-d7316df2c29a | -7.91751 | -44.1184 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 892736bc-8e8c-3634-9b98-7f40ab06b521 | -2.99642 | -55.96282 | 2025-09-21 04:55:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e41f540-e240-301a-9957-56600b780345 | -2.69067 | -59.42373 | 2025-09-21 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5aadd785-88c6-322c-99fc-a49933f2df58 | -4.32615 | -55.00959 | 2025-09-21 04:55:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ba7dca7-bc9a-3ef4-8f13-082667bd9e60 | -5.69398 | -51.76222 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 34f509f0-ec2a-3fce-a5e3-5dad13f0455f | -2.69591 | -59.42729 | 2025-09-21 04:55:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46a35db8-2bcf-330f-9faa-d7623759a651 | -3.60199 | -47.51916 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb4e970a-84c9-3182-83e4-cec44137241a | -2.13815 | -52.84438 | 2025-09-21 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 73d1cb91-eab2-314c-99bf-23f5d27c0b11 | -5.26872 | -45.05626 | 2025-09-21 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23ce5ac7-2471-3628-a07a-c41422cbfc33 | -3.59769 | -47.5185 | 2025-09-21 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5ea06e9-9d4b-3e46-bd9c-cad2cf5cd3f6 | -5.15014 | -45.71039 | 2025-09-21 04:55:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00c0620b-d35b-3469-be6d-52dbd84e0cc3 | -3.68127 | -43.52166 | 2025-09-21 04:55:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 12e14eae-a069-3f27-bea2-b4a0e3e5138d | -3.58986 | -43.91613 | 2025-09-21 04:55:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b695c65-fc80-3607-8141-432255a446d4 | -5.9375 | -49.53545 | 2025-09-21 04:55:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25173fbf-b87f-369e-b234-4f381e561fc8 | -2.60835 | -48.1359 | 2025-09-21 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae3a9e1d-33fc-3ea2-9da8-e1c507ad0890 | -5.76082 | -44.19987 | 2025-09-21 04:55:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8a6b371-ad4c-3864-ab91-499911f1f9ef | -4.94654 | -49.92656 | 2025-09-21 04:55:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff3dfffc-740d-35b1-8c2b-09d72324a503 | -2.93399 | -48.02147 | 2025-09-21 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4505b88f-a147-30e8-bbfb-6671ef8dbc1f | -2.74041 | -49.55458 | 2025-09-21 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b085935-96e3-3731-8204-98c53df17b8e | -5.69515 | -51.75465 | 2025-09-21 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e3d2866-7075-3439-8066-d0992dc72f26 | -3.35185 | -48.3905 | 2025-09-21 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0c8be8c-daba-3317-a961-1ba0666983aa | -5.62676 | -45.94744 | 2025-09-21 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c55ab26-56a3-38b5-8d9d-3e7c2d5c9944 | -6.13751 | -43.98045 | 2025-09-21 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 121c32cb-6900-3b05-bfa0-eeb8cb6e1b29 | -5.82598 | -49.91593 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 768fa571-6b71-3812-b6d8-4e3cccffd28f | -5.3579 | -49.20654 | 2025-09-21 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ea96f8bb-94a1-35d6-a4bf-8e04156639b7 | -7.92386 | -44.11507 | 2025-09-21 04:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 233dea70-b362-3517-b1e7-e99241402c39 | -6.44929 | -45.69251 | 2025-09-21 04:55:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README36.md)
