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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0968de94-bda1-3fdf-9701-66efa9c62a70 | -22.08968 | -48.99583 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| cdbc9752-5e4c-32b4-8ef7-01cec7936cf5 | -22.08111 | -48.99986 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 9bf42342-09b4-3473-b5c7-740d5eb5dc55 | -22.08443 | -49.00408 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 95d625f2-0676-335a-8344-bcf82924a96d | -22.07999 | -49.00785 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 4027550a-a17a-3d7c-8285-88c2a9cded73 | -21.23034 | -48.61406 | 2026-10-10 04:12:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 473a8a43-cf10-34f6-9651-b44b664e8510 | -22.07669 | -49.00364 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 46f24e85-6a06-3b38-a197-a0f1ed70ea38 | -22.08723 | -49.00937 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| f0ac482a-5ca7-305c-b851-0cc0629d66a8 | -22.08525 | -48.99958 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 86b79c8e-7bcb-3972-9048-0e40414b1cb1 | -22.07952 | -49.00893 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 29.5 |
| a5e01e4a-77e6-3593-9408-78a9e09fda6e | -22.08805 | -49.00484 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0f7b8871-0bc2-3670-b98b-56d156fc7b8a | -22.08278 | -49.01315 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 117ccda5-2f7f-35ce-9a04-a34b1129d59f | -22.08632 | -48.99158 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c958a91c-2315-3686-b6c2-74d1ed48b74a | -21.0999 | -48.5023 | 2026-10-10 04:12:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a50a591e-641b-3a49-9645-3263ddceabe5 | -22.07916 | -49.0124 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be776cd0-fd1e-3718-ab3b-d0c389ebc4d6 | -22.08887 | -49.00033 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 77ff989f-7a79-3706-8124-f3c64486048d | -22.08394 | -49.00514 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 6b0b9123-6ca7-371b-a6f8-1c010265e7f2 | -21.23393 | -48.6148 | 2026-10-10 04:12:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8be0fc14-1e1a-3c66-be22-bd438f5bc67d | -22.07749 | -48.99911 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 766af7c5-829c-371a-aa6e-e1ca426a98db | -21.10069 | -48.49785 | 2026-10-10 04:12:00 | NOAA-21 | TAIAÇU | SÃO PAULO | Brasil | 3553104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a120f0a6-28de-339e-87b3-cae503920510 | -22.07546 | -48.98933 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ba20105-6814-3adf-9a30-73ae641e6d42 | -22.08162 | -48.99882 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3978ef5b-64d4-33af-9f03-803155d90350 | -22.08314 | -49.00969 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 75328287-cefd-3eaa-9c44-abbe6ba5e185 | -22.07636 | -49.00711 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 7314a486-8c9a-3a9d-965c-ba470846e972 | -22.08032 | -49.00438 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 29.5 |
| b4bdaff5-f745-394a-a6ac-1987d99480a4 | -22.07801 | -48.99807 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0face69e-2179-3f98-8ebe-87c7d0bdd963 | -20.30008 | -49.57966 | 2026-10-10 04:12:00 | NOAA-21 | PALESTINA | SÃO PAULO | Brasil | 3535002 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc092f97-8fc3-34cb-80b0-75e3a5aa0fd3 | -22.07719 | -49.00258 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| e15eae87-c337-305e-85e2-caeefc66ec8c | -22.08552 | -48.99611 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 10cfbc67-67c7-366b-a25a-c9c06a110f80 | -22.08244 | -48.99431 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 670ec62b-b315-3482-bc9a-90f3aa06d156 | -22.08081 | -49.00333 | 2026-10-10 04:12:00 | NOAA-21 | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9a4ee3e9-0d98-3acf-9f08-94df3ced43a9 | -7.535 | -45.3006 | 2026-10-10 04:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8a064722-3463-3d74-ab0a-ceca21756201 | -10.8905 | -44.8232 | 2026-10-10 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 2659d325-6fb5-372a-8208-198da352d7e5 | -3.9912 | -59.356 | 2026-10-10 04:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 53e089d9-7f2b-3f38-bf21-2c71b05b0b47 | -10.9097 | -44.8206 | 2026-10-10 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 9e75501a-00fa-3d69-9a60-900f63fe3ba3 | 2.727 | -60.2586 | 2026-10-10 04:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 80e96102-a0e1-3969-95b9-9ead56826cea | -7.0228 | -47.661 | 2026-10-10 04:20:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 65e6a2e9-aee6-30e8-88ff-baf456009b21 | -10.8909 | -44.8001 | 2026-10-10 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b9df7eae-89ae-3d69-9474-1101905b2df6 | -3.2203 | -49.4417 | 2026-10-10 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 77455364-0d31-34d3-9e30-9e514b8b8d83 | -3.2204 | -49.4205 | 2026-10-10 04:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b88c6495-5b50-36ce-b38c-90456dd6a3fb | -7.5162 | -45.3024 | 2026-10-10 04:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 353ba08f-e8a5-3969-a078-60aa1619a3bd | -3.6048 | -54.5936 | 2026-10-10 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 16ec58e1-1183-3f59-9954-3ee2b8de519d | -7.535 | -45.3006 | 2026-10-10 04:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 1e673f8c-d55f-348a-a202-1dfdfd40cece | -4.4025 | -49.7774 | 2026-10-10 04:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ab75ba63-abea-3566-8ece-9f8143e906cd | -3.2203 | -49.4417 | 2026-10-10 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 61680181-1e78-3ebd-bee8-b40c48bdf76c | -10.6012 | -60.4863 | 2026-10-10 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 112.8 |
| d0348d5a-9e43-3ab2-9523-70b3116ac7ef | -10.6013 | -60.4669 | 2026-10-10 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4a76e86c-354f-3d03-91f2-0b8800284212 | 2.727 | -60.2586 | 2026-10-10 04:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 55.5 |
| c3cb0fd0-3c86-332f-b1e2-9e68583e02cb | -3.2204 | -49.4205 | 2026-10-10 04:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 6cb95dda-fdf8-3309-a229-32bb96f5e407 | -10.6199 | -60.4852 | 2026-10-10 04:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 98f37103-17dd-388a-b674-c25d1dc3894e | -10.9097 | -44.8206 | 2026-10-10 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 024eaf3b-42f3-3b0d-9fe0-0c81b1d6c461 | -10.8905 | -44.8232 | 2026-10-10 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 37ca7b49-86b0-3ce0-87a7-39004245eee8 | -6.4566 | -55.5008 | 2026-10-10 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 61702b21-8ccd-3bcd-9116-6e014b8db14f | -8.5053 | -54.6 | 2026-10-10 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 2938c0cf-4cf0-3d38-aaa4-918d369c4e7a | -7.0228 | -47.661 | 2026-10-10 04:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 63db2043-10c1-386b-86b9-3229f7aaa76b | -10.6013 | -60.4669 | 2026-10-10 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 1ee3a813-363c-3963-8295-8af417722d67 | -10.6012 | -60.4863 | 2026-10-10 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 38e37821-6391-3fd3-bb1f-6bd6b25fd729 | -4.4025 | -49.7774 | 2026-10-10 04:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 6a0c4c81-3ee1-3733-a286-c0e173fbdbc0 | -10.6199 | -60.4852 | 2026-10-10 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| f07db368-0ff3-32ff-981a-949d22b0b599 | -8.4867 | -54.6013 | 2026-10-10 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 0b5978a9-7ca9-30b1-a019-b5caccc2bc7f | -8.5051 | -54.6202 | 2026-10-10 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 50403304-d3aa-31dc-8924-1aa0393af05f | -3.5688 | -54.3945 | 2026-10-10 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ee9cc40a-6bb5-3dfb-a0dd-65c3708aac66 | -4.1039 | -54.0164 | 2026-10-10 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| f76de29f-2e16-3105-a457-038d8cf36d69 | -3.2203 | -49.4417 | 2026-10-10 04:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e038c5d1-2116-3afe-b354-1e896bb90b3f | -3.5689 | -54.3745 | 2026-10-10 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| b90434b8-159a-3eb0-a1e5-7f5c53e831e8 | -3.7376 | -58.4965 | 2026-10-10 04:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 94a892f6-215a-3ae0-b0bc-0492e478340f | -8.4865 | -54.6215 | 2026-10-10 04:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 590d0382-a9b2-3369-979a-42273a161f06 | -10.6201 | -60.4658 | 2026-10-10 04:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b1cff071-1fc6-3c82-a6b4-c6892a974050 | 2.81717 | -50.95139 | 2026-10-10 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53268f45-0a8a-37c6-bbc4-c39b42c51fe8 | 3.98067 | -51.63328 | 2026-10-10 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89936919-9507-388a-8dc5-4a45dd7e1c56 | 1.54353 | -50.89619 | 2026-10-10 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d956271b-13b0-395a-860c-2e3156dec85f | 2.81305 | -50.95201 | 2026-10-10 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 434dc582-d493-339c-9045-17af8d7a906a | 1.5395 | -50.89682 | 2026-10-10 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42388fa9-eb94-3a9c-ae32-c02096b32ed5 | 3.73924 | -51.6073 | 2026-10-10 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bfcf9e0-f861-3ee3-a82a-f9203a3beaa8 | 2.41307 | -50.96377 | 2026-10-10 04:42:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0593c49e-77e7-336a-9d31-5998dab80d8c | 1.54005 | -50.9003 | 2026-10-10 04:42:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d4624dc-de80-3a5e-8bb9-d193de8cecb2 | 3.98003 | -51.62903 | 2026-10-10 04:42:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8764eb9-09d6-3007-986a-c012feefbee9 | -1.27442 | -55.76088 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2371c06-ccee-3e3d-8bb3-8210422d9073 | -6.6473 | -47.91535 | 2026-10-10 04:44:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c40cbba6-b2b5-325e-9795-3abcb9478daa | -3.54837 | -54.69268 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b410e4ed-c84e-3708-b0dc-685e1904283c | -5.23561 | -50.68162 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d038edaa-ae19-32e2-9319-977ecc04c677 | -3.00564 | -54.04119 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94139154-8b82-3f32-a766-62243105fb7e | -5.71815 | -53.49411 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6be4288-ddee-3965-8ccd-07a38db62b28 | -4.83353 | -43.34612 | 2026-10-10 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f409ed0b-daa0-37c3-abda-e2c3f65d25f5 | -1.21697 | -55.65706 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31bf6d85-5edc-3f24-af7f-02b72fdbe6d1 | -5.87125 | -53.51209 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa5273af-276d-3c09-be59-3a6bbe03055d | -4.409 | -49.77852 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4a548cfb-de19-3d15-8611-e31d5b62e362 | -6.06438 | -44.66304 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a84432f8-b952-37d4-9451-0d9f923b4f4a | -4.10446 | -54.01703 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8b7655c5-0573-3eb2-92a2-70fa3a83ae9b | -3.35059 | -50.41558 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b3c6c22-afa8-3b26-9080-bdd4eb9d355d | -2.94182 | -54.08027 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1accb74e-c7af-338f-b1d0-1938a4233297 | -3.98568 | -59.36619 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0852ed2d-b17f-3b51-adf5-3dcf7ac43420 | -3.56852 | -54.69071 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5d745b0-7148-396e-a124-ab2405b141e7 | -3.52278 | -50.34079 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e75c3b3c-9dee-362a-bc66-8ef2f41838ef | -1.65075 | -55.1978 | 2026-10-10 04:44:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50be907f-8914-3ab2-b9f7-71ef6e87c9e5 | -4.12931 | -50.83037 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e50a4868-c84f-3621-b8f7-4fbe3e11a602 | -1.25274 | -55.79197 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1377a815-a796-3293-ad49-69e801df59c0 | -3.8569 | -44.04947 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94efb567-02e7-3191-88cf-eee80fd9dcb5 | -3.31048 | -54.00621 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5aa65e29-907d-3898-879b-34946f2128c4 | -5.53435 | -43.05928 | 2026-10-10 04:44:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2592ed9e-48b5-38b3-85b6-9eccef7e89c8 | -3.66908 | -55.54694 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README56.md)
