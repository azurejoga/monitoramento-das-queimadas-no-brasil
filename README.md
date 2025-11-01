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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b994eeb2-7b11-3d41-a84c-a3d6ecaebd99 | -4.1925 | -47.6409 | 2025-11-01 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 0c62b4ba-7423-380d-a265-4d752dd42fc0 | -4.5047 | -54.9247 | 2025-11-01 00:00:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| eacefc71-d92d-3ec4-b241-e25d675de1f4 | -6.9481 | -49.6312 | 2025-11-01 00:00:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0ff1d6c8-cb22-3e2d-931c-8670f78cd242 | -10.6313 | -52.1891 | 2025-11-01 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 8e35228f-ec28-3a79-905d-bc166db9269e | -8.2195 | -46.25 | 2025-11-01 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a7627ba7-0d5b-3cef-9099-617c4a932460 | -17.7752 | -40.2008 | 2025-11-01 00:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| 22093804-eb47-3dd1-9bea-390006428137 | -11.7433 | -47.4741 | 2025-11-01 00:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| a23efb2e-a890-328c-89d1-1e9e7e3b30b5 | -10.6316 | -52.1682 | 2025-11-01 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 69be696f-06c0-3494-b88a-8c63ce85a513 | -7.6965 | -45.963 | 2025-11-01 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| b041e042-2af1-310d-a50c-eeaf99ca30c8 | -4.1924 | -47.6627 | 2025-11-01 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4559bea4-41c7-3238-b35d-54b74a7352c9 | -3.2156 | -50.5795 | 2025-11-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.9 |
| 8545acac-a467-37c8-bb8c-cfafd98d681a | -7.696 | -46.008 | 2025-11-01 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 20e55c81-19ab-3180-a9e0-65d34e22be24 | -10.6502 | -52.1873 | 2025-11-01 00:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 24ca1e4a-c69e-3d72-a8ba-c530648a0825 | -4.1739 | -47.6418 | 2025-11-01 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| f4e97744-cf25-3386-a5af-7359908c496e | -17.776 | -40.1748 | 2025-11-01 00:00:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| a32c0e50-ba75-34f5-85af-44ef5f7ceb28 | -4.1738 | -47.6636 | 2025-11-01 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 82d1cbd9-02d6-3fcc-a46e-6a3bd84f786d | -3.234 | -50.5999 | 2025-11-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 9fd3332d-d44c-304b-9a60-eba08dfb9b65 | -5.8408 | -44.072 | 2025-11-01 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| aee1a999-3d9a-3890-910e-925af75cf371 | -13.3337 | -60.7158 | 2025-11-01 00:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| d13df4b7-2c21-3283-a5e9-d11598a1f505 | -7.6963 | -45.9855 | 2025-11-01 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.4 |
| f947bea1-34a9-3b21-8580-843ed8e17f95 | -5.1166 | -43.3831 | 2025-11-01 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 05e3f77e-c413-3556-836d-da8887851ac2 | -10.6565 | -45.1542 | 2025-11-01 00:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 82876222-ac96-334b-947f-3d5f0241f6c7 | -3.9815 | -48.9019 | 2025-11-01 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6eefc16e-0050-33d8-8856-5c3b7058ffbe | -13.2087 | -43.1162 | 2025-11-01 00:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 99.8 |
| fabdff7b-d3e7-37c2-ab86-aedad7033ecc | -8.2383 | -46.2481 | 2025-11-01 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 51b68276-eed9-3b23-98f9-a7de591e152a | -5.0656 | -45.1078 | 2025-11-01 00:00:00 | GOES-19 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| b0314cb8-b506-3bb4-bb30-c64d43b46eec | -13.2082 | -43.1403 | 2025-11-01 00:00:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 89.2 |
| 1512d7e2-df9f-3d86-944e-44c67817b650 | -7.7151 | -45.9838 | 2025-11-01 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| fb901277-cdc0-3d60-9a72-e8243cdf5c0e | -3.2155 | -50.6004 | 2025-11-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| ba41aef2-75a8-3e6c-85af-85ec9a06f47b | -3.234 | -50.5789 | 2025-11-01 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| 4485b974-d4dd-38f6-be55-3b95aa6be4a3 | -6.8862 | -35.0116 | 2025-11-01 00:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 162.6 |
| edb7e806-4a4b-3bc8-9311-95bb17f24a26 | -3.2156 | -50.5795 | 2025-11-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 0996defc-c9d3-3951-8955-a29e03ebc309 | -3.234 | -50.5999 | 2025-11-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 3c9f50bb-27d2-3866-8012-19a6557020e0 | -4.1924 | -47.6627 | 2025-11-01 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cea5579b-6b64-36f2-80da-166ca90002ee | -8.2383 | -46.2481 | 2025-11-01 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| e8dd5f9e-9689-31e7-8a1c-5240bc38c905 | -4.1925 | -47.6409 | 2025-11-01 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bdbf9d6c-6163-37ef-beb7-0c6bb35d21a2 | -10.6502 | -52.1873 | 2025-11-01 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 3d5978ba-aad8-36a4-8bb8-96f6ca054039 | -8.2386 | -46.2257 | 2025-11-01 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| ae849f71-06ac-3558-a5a3-5ffc28621411 | -6.9481 | -49.6312 | 2025-11-01 00:10:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 25d6ddeb-7f64-3eae-a492-07f6514442b7 | -3.234 | -50.5789 | 2025-11-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| a83a8cd8-771b-3703-a62d-737a89ae15f4 | -6.9295 | -49.6325 | 2025-11-01 00:10:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b53c0bbc-68d9-3a2c-aa0f-3dfce7a24a77 | -3.2155 | -50.6004 | 2025-11-01 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| bc67156d-db56-386a-a7c6-b9dc457a79dc | -13.2087 | -43.1162 | 2025-11-01 00:10:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 05088d77-c3ed-3e78-ab37-194b29b7cdca | -10.6313 | -52.1891 | 2025-11-01 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 5e51fc2e-c2fe-3fa3-87c4-be1cda88b884 | -13.6463 | -44.4149 | 2025-11-01 00:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 4ed3414c-1844-3318-b494-d04de844a9c9 | -4.5047 | -54.9247 | 2025-11-01 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| c9d4a872-2833-30c9-a49d-0eb835b1d59f | -4.1738 | -47.6636 | 2025-11-01 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 0e80bfba-c270-389b-9936-f230bd817684 | -10.6504 | -52.1664 | 2025-11-01 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 2d46cb00-11d5-3db5-a682-c1db6b406821 | -10.6124 | -52.1909 | 2025-11-01 00:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 32bddeef-c0a2-38b7-b7d8-690fff463a04 | -4.1739 | -47.6418 | 2025-11-01 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 283aae41-ca3d-3e8a-b222-1d49f88f7d8f | -8.2195 | -46.25 | 2025-11-01 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 3051f035-118d-3561-9980-6991737870ee | -10.6316 | -52.1682 | 2025-11-01 00:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 99bf02cc-502b-3f10-a99c-edb8303d6fd4 | -7.6963 | -45.9855 | 2025-11-01 00:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 376bf01f-1014-3b6f-9754-93026a72acdd | -13.6657 | -44.4115 | 2025-11-01 00:10:00 | GOES-19 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9ec22b21-476e-30d4-848e-cab1f92ef8ea | -11.7433 | -47.4741 | 2025-11-01 00:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 7610d2b9-92a7-3394-bd56-8db03d017330 | -13.3337 | -60.7158 | 2025-11-01 00:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 80e7f4e2-b1e8-3b9e-9806-acc8f5661149 | -6.9053 | -35.0091 | 2025-11-01 00:10:00 | GOES-19 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 116.3 |
| 8ee2ef0f-72f5-3646-9dae-33873ca1e6a0 | -13.79502 | -43.25401 | 2025-11-01 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 8a65574e-058b-3cec-95da-eefb6805d197 | -13.21557 | -43.12751 | 2025-11-01 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 19.9 |
| db475e73-9294-38bc-b5a3-ca9567539aa9 | -13.12844 | -44.03473 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 2fddd948-3abf-3161-9128-5560d79432a9 | -12.80542 | -43.48686 | 2025-11-01 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2d972c5b-eae0-3df6-b960-53edd067b949 | -13.51448 | -44.2979 | 2025-11-01 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fa8cd364-fbe6-342d-8974-67d32fa9f290 | -15.35751 | -43.03579 | 2025-11-01 00:11:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e6336d1f-13db-3453-87ca-edf26c934b0f | -15.34994 | -43.04624 | 2025-11-01 00:11:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 7ecd5249-811b-3cc5-afc0-95b924aaac47 | -12.05862 | -47.34787 | 2025-11-01 00:11:00 | TERRA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f536e0da-b8b4-35c6-b59b-fb0cebd923a5 | -13.20671 | -43.12884 | 2025-11-01 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 87.4 |
| c154f6d9-98cd-3e68-935f-688c6f592bb2 | -15.11868 | -42.2532 | 2025-11-01 00:11:00 | TERRA_M-M | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 3d0aac4b-1118-35e7-a7e9-9779e8ed8000 | -14.69108 | -42.81642 | 2025-11-01 00:11:00 | TERRA_M-M | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 1b30cf8b-af47-3707-b75c-127189aaf3e9 | -14.07255 | -44.27432 | 2025-11-01 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fbb7dc27-019b-3cef-8c52-6bf89db863a9 | -11.73743 | -47.46387 | 2025-11-01 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 8eb0ed30-7a5e-320a-adfa-bcdfe2696817 | -15.34867 | -43.03712 | 2025-11-01 00:11:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 28.3 |
| 999badd8-f6e8-3aaf-9fd9-08788986186b | -13.86155 | -42.48484 | 2025-11-01 00:11:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6e2571cd-698d-351c-9531-bfcca43fbd4f | -14.97838 | -42.89421 | 2025-11-01 00:11:00 | TERRA_M-M | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| aa3cfe34-ad19-3694-9e46-0e1f56db02ab | -13.65729 | -44.39616 | 2025-11-01 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d85af20e-0134-33e2-a7f1-0bc59b509c87 | -11.88724 | -44.3834 | 2025-11-01 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9944f802-b1e6-3016-8ed4-2cfe00897499 | -15.51934 | -40.72033 | 2025-11-01 00:11:00 | TERRA_M-M | RIBEIRÃO DO LARGO | BAHIA | Brasil | 2926657 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f325a5bf-885b-3743-a09c-4b31c3538ef9 | -15.25546 | -43.09469 | 2025-11-01 00:11:00 | TERRA_M-M | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 6.1 |
| baa2457c-71ae-3df7-8cee-68260c0c863c | -13.2938 | -41.93233 | 2025-11-01 00:11:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 91478238-6047-3800-8a3a-c7eb948cc395 | -14.05739 | -43.95263 | 2025-11-01 00:11:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 99abbde7-73fb-3666-a828-08ed12c9e9a4 | -13.64961 | -44.40674 | 2025-11-01 00:11:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8677c39e-e3e7-3fb8-8ff1-b45d576fdd69 | -13.82865 | -43.02959 | 2025-11-01 00:11:00 | TERRA_M-M | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 03de1b5d-2ad8-3107-9580-918c6e44fb90 | -13.35285 | -43.78996 | 2025-11-01 00:11:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9dd8977f-2306-3f25-9ada-619545f72013 | -14.07381 | -44.28357 | 2025-11-01 00:11:00 | TERRA_M-M | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 52d0f366-4280-3b93-8f99-a9d273d1c3ff | -11.72725 | -47.46525 | 2025-11-01 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 16c10a0a-d47f-3b90-9057-cfd0255457bc | -15.27315 | -43.15714 | 2025-11-01 00:11:00 | TERRA_M-M | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ced630b1-9e68-32be-9474-27a44d94636b | -12.71961 | -43.8059 | 2025-11-01 00:11:00 | TERRA_M-M | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 614052e0-3b39-3a72-b370-0500d011cc41 | -14.15336 | -42.0792 | 2025-11-01 00:11:00 | TERRA_M-M | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6f770b0b-8498-3bb5-9708-6a0f21150ebb | -12.84837 | -43.47128 | 2025-11-01 00:11:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f180a2d6-22ec-3b06-b306-253265a02463 | -13.13568 | -44.00926 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1a60c059-bb9b-3c66-a0ab-f079fffdc04f | -11.91403 | -44.17145 | 2025-11-01 00:11:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| c61dffac-3c28-390a-8e88-fdf10deca55f | -13.1544 | -42.63188 | 2025-11-01 00:11:00 | TERRA_M-M | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| c5a436e8-ac55-3da4-b7b6-c8271abb6fbd | -14.21077 | -42.34925 | 2025-11-01 00:11:00 | TERRA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 2b2c79d9-f069-3b1b-9678-22171057065d | -13.15885 | -42.27697 | 2025-11-01 00:11:00 | TERRA_M-M | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 9.0 |
| c44a68e4-b4f1-380d-957e-7f5ddd068091 | -13.0817 | -44.02309 | 2025-11-01 00:11:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8e59355-4378-3d2b-8b6e-c50c4107f547 | -16.07845 | -40.3706 | 2025-11-01 00:11:00 | TERRA_M-M | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| bec93b8c-8414-3060-b34c-a461dca91753 | -13.21685 | -43.13659 | 2025-11-01 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 924cef7f-0c9b-3f24-aa91-8f0e59344b1d | -13.44003 | -44.4275 | 2025-11-01 00:11:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| c9c07be2-236d-3996-a95a-efecac12030a | -11.97639 | -44.82887 | 2025-11-01 00:11:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 42aafa9f-398d-3737-b4fc-e6984c564483 | -11.52093 | -44.99905 | 2025-11-01 00:11:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0308148c-1a74-3c88-b1e7-b8f4074ddc27 | -13.23637 | -44.61952 | 2025-11-01 00:11:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |


[Clique aqui para ver as próximas entradas](README2.md)
