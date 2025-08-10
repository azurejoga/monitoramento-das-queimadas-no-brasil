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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28ada1c7-c9f8-300d-921a-2e06f3cb90c8 | -8.91149 | -60.54314 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f29e2dff-5313-3886-a34f-e39b235c58ec | -9.19947 | -59.6665 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79e69c37-c1c7-3ceb-9479-a263a28a3818 | -8.93549 | -60.73941 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7da7de4b-1147-354b-b226-d706980e0b35 | -8.93086 | -60.73513 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cd6c21d8-3f44-361c-a578-32dfc4e1794b | -14.47056 | -47.84331 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15d1d6e4-8b20-3ea5-a6ce-2d27f0b3a8f6 | -7.29726 | -55.3181 | 2025-08-10 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f193ef33-69b9-3634-9922-6b0373ca77b6 | -9.20415 | -49.67526 | 2025-08-10 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad7507d2-6613-3bc4-b02c-f2ef289e0af5 | -8.93489 | -60.74267 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| e143de25-cbfa-3847-8e82-4d84eda7e6cc | -7.40302 | -60.00361 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fadaf92-b109-3351-aa91-6b2364d39aa2 | -18.844 | -50.1274 | 2025-08-10 04:49:00 | NOAA-20 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a65e0b2-8c47-3a77-9bd3-4f0cf7a1bb92 | -15.56771 | -52.41773 | 2025-08-10 04:49:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 212832bc-b3f9-3aca-acef-9d241e2980ea | -19.88692 | -44.42164 | 2025-08-10 04:49:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e6521e44-b7f3-3028-a4ee-e8d62d44b71f | -18.47935 | -47.56918 | 2025-08-10 04:49:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a74a100c-6d40-3e01-b683-5c74afdb766b | -20.17074 | -43.71579 | 2025-08-10 04:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0a880018-0526-358c-aa70-398c60bfc07e | -19.89043 | -44.44067 | 2025-08-10 04:49:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4e4759cf-3c28-37cc-aebe-1d8ec3fc3b9d | -21.31738 | -48.56496 | 2025-08-10 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ee86a9b-0fed-3f71-bed0-f1d3e50576d4 | -19.85349 | -42.30137 | 2025-08-10 04:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e8beefc5-b2c1-37c5-bfd8-5a5c564e5b3f | -20.56361 | -55.57261 | 2025-08-10 04:49:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00b95cc8-c949-38c4-b51a-60b8b5081735 | -19.2 | -42.01744 | 2025-08-10 04:49:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8ac7a62a-c207-3b63-a1ff-83efd2d627e6 | -18.17922 | -46.99629 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f1e6fff-acb3-3e4a-b9fd-a7c514f15ded | -21.48494 | -47.74843 | 2025-08-10 04:49:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e786ea17-d0e0-3f7a-b994-015ad36989f0 | -19.40187 | -43.35493 | 2025-08-10 04:49:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4af03f10-4698-3c68-91d2-effc9aefb13b | -19.08402 | -43.54111 | 2025-08-10 04:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ea063c7c-bcae-3d84-a836-f65b8106e691 | -18.17424 | -46.99976 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c908a94f-5ec8-3e87-bb91-b782e0be8cea | -19.83521 | -45.92345 | 2025-08-10 04:49:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e593215-89bc-301e-b43a-e9d81ea68929 | -18.16694 | -46.9846 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04c9d557-8e05-3316-b9aa-0188547e5f82 | -19.40146 | -43.3592 | 2025-08-10 04:49:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 062951f5-a93a-3b53-b371-c7670b7eb30b | -19.5793 | -47.23866 | 2025-08-10 04:49:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c47b4f3a-0fde-34dd-a543-bb982f660ebf | -21.93396 | -47.80275 | 2025-08-10 04:49:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 4e24375a-5fca-3223-9c6f-bfb058ad8221 | -19.57146 | -47.22776 | 2025-08-10 04:49:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b00362ca-508a-3ea9-b9f5-3ae0c1870509 | -16.30717 | -52.92579 | 2025-08-10 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3ef089d7-cd0f-3da9-84b4-388d25291156 | -19.07798 | -43.54379 | 2025-08-10 04:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a3c7676a-225a-3b3b-bcd5-6aa25083cfe8 | -20.17252 | -43.71429 | 2025-08-10 04:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 19b7cf99-0a81-332a-9e46-11615a59141b | -20.17033 | -43.71989 | 2025-08-10 04:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c4bb7654-3e3a-388f-ab8e-b93f775f4ce9 | -15.5533 | -56.03147 | 2025-08-10 04:49:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04cf639a-5e95-3669-8f09-6c7946362165 | -20.50752 | -54.9084 | 2025-08-10 04:49:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eeb56961-7c94-3617-a003-0f716869f167 | -16.30054 | -52.92468 | 2025-08-10 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6056a542-fcfd-36c8-b8bc-f52f2dc5b155 | -19.1996 | -42.02164 | 2025-08-10 04:49:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2ebed19-7352-3fc7-8d06-0144f0adb672 | -17.62981 | -44.64869 | 2025-08-10 04:49:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1c39506-4c96-3364-ad52-3b0c5464a21a | -16.29167 | -52.93797 | 2025-08-10 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 99e0defe-3a2e-34b8-a98b-80aea191d0a4 | -20.44435 | -53.77438 | 2025-08-10 04:49:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49590d43-d363-3403-ac4b-97121272a1e0 | -21.31264 | -48.5685 | 2025-08-10 04:49:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d0ef0a-c9fd-3b88-b87a-33ab61ab9db8 | -19.83735 | -45.91935 | 2025-08-10 04:49:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 46863dbe-3469-3cec-a875-f366d10f3b44 | -21.47993 | -47.75255 | 2025-08-10 04:49:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3df3b343-4794-313e-8e6b-9a85ebd8cf89 | -19.20588 | -42.02215 | 2025-08-10 04:49:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 34028467-60cb-3e49-91a4-93a2efbde079 | -15.26988 | -56.65492 | 2025-08-10 04:49:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49a40fa6-d582-38a9-9500-44ba4c8dfd86 | -18.17869 | -47.00064 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5a4c5a3c-629e-3fc4-9db0-d32b0c3efda6 | -21.16962 | -48.65047 | 2025-08-10 04:49:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 888e3ffb-d435-30c9-86c7-ff4ff67ae27b | -14.59076 | -58.75248 | 2025-08-10 04:49:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea8ac4fd-173a-36e3-947f-e4baf9b3354d | -19.08357 | -43.54557 | 2025-08-10 04:49:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7e25f464-7209-3065-b15b-62e7d869ed0a | -20.17214 | -43.71844 | 2025-08-10 04:49:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3c41e2a2-5a92-3a96-b7b0-04066bd0f32b | -16.3011 | -52.9211 | 2025-08-10 04:49:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2564388d-83a9-358c-a67e-89e9f7416ad8 | -18.48038 | -47.57067 | 2025-08-10 04:49:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed61ce2-779a-3b46-8c48-8034b5dcb1c9 | -20.65435 | -44.73383 | 2025-08-10 04:49:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4619b88-ed00-368b-9fda-126cdd85bed8 | -20.27166 | -44.2617 | 2025-08-10 04:49:00 | NOAA-20 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8bcba321-9cf7-3b7e-a0f7-f2bd07f3a95a | -20.03774 | -45.55833 | 2025-08-10 04:49:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e5151e2-ca92-3f50-b042-db16f4226dcf | -17.50813 | -41.74456 | 2025-08-10 04:49:00 | NOAA-20 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 09b5eea5-9aac-3c92-926b-639ec7bfb292 | -19.85304 | -42.30632 | 2025-08-10 04:49:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4394e752-9cb9-3b8c-9c3e-d3fb42cab3b4 | -18.53696 | -45.01144 | 2025-08-10 04:49:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c463d9c-2c9c-3f6b-a9dd-6196995fdbcb | -16.75902 | -49.44677 | 2025-08-10 04:49:00 | NOAA-20 | ABADIA DE GOIÁS | GOIÁS | Brasil | 5200050 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e7b9404-49a3-363f-81c3-1be3b825b653 | -20.03807 | -45.55519 | 2025-08-10 04:49:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1c73687-1c79-3563-a254-36d8f1d7236b | -19.57537 | -47.23328 | 2025-08-10 04:49:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07bc7560-7cd2-382f-bca2-d31b12c5e2b2 | -18.17142 | -46.9853 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0244a056-a8de-331f-b973-7ab83677012e | -18.16978 | -46.99892 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2d723f75-ffe5-3b8e-86a4-505ef612ac25 | -19.83674 | -45.92516 | 2025-08-10 04:49:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d76c35e2-af41-35b2-a788-c2bae4ae0c70 | -20.14463 | -52.83699 | 2025-08-10 04:49:00 | NOAA-20 | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea8da0a1-a63c-32b6-a8e7-d378943d1ad3 | -18.24572 | -42.58223 | 2025-08-10 04:49:00 | NOAA-20 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e3d2d89a-c720-3f93-860c-fa0f4d1361f8 | -18.17533 | -46.9907 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| eeb4ce94-e9ca-3849-bedb-851abf566390 | -19.82068 | -46.60654 | 2025-08-10 04:49:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f320e524-0dd8-3853-b2b9-9e346c6f82ab | -18.17085 | -46.99005 | 2025-08-10 04:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fb87289a-382b-302d-ba7a-34025d661b03 | -21.08664 | -45.08257 | 2025-08-10 04:49:00 | NOAA-20 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 288c428b-4662-3bc3-904a-5d54ca613251 | -19.57595 | -47.2285 | 2025-08-10 04:49:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07e9a3c5-ba89-33ab-9181-3d251e7cf8fc | -19.08825 | -47.63686 | 2025-08-10 04:49:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77868a07-8788-3d75-8c08-fff75080e6e6 | -8.9401 | -60.7288 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 082df201-3f67-3e28-a040-c69d1d504ee7 | -9.3808 | -61.5124 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a152e30c-aaf6-32a2-849e-2bd3cb4be60f | -8.9215 | -60.7297 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 32cf361a-6fc6-3b30-a2cf-6000c0993a8a | -9.5015 | -46.2725 | 2025-08-10 04:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0039fb92-f5d1-302b-b4de-e475b8edc975 | -9.362 | -61.5324 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 1ffbbf70-f753-384f-b946-40eb3fe59c7b | -8.9399 | -60.7481 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| c7b642c2-e2c3-3226-a467-fdca615269fa | -8.9213 | -60.7489 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3ef1a7a4-0b7a-36fa-b29d-0c2c68dcf272 | -9.3806 | -61.5315 | 2025-08-10 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| f343abe0-1e06-36e9-a252-e4aa71898052 | -22.72336 | -47.39185 | 2025-08-10 04:51:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 434357c5-14a6-3431-8ab4-24c4c212bb6a | -22.90681 | -45.50306 | 2025-08-10 04:51:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 05137ad9-e827-33bb-bd98-8ab4c34781a5 | -22.81374 | -47.1418 | 2025-08-10 04:51:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0a0944bd-4d0e-3291-b34c-b231cff24c7d | -23.39907 | -47.01022 | 2025-08-10 04:51:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6fd1090d-979e-30a8-b4ed-3f51c770e39c | -22.91208 | -45.50365 | 2025-08-10 04:51:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5416475-037d-3e1b-855d-9b2904e39d3d | -24.67807 | -51.05102 | 2025-08-10 04:51:00 | NOAA-20 | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 206c44b7-01df-33e8-9249-0371edb1a698 | -22.96431 | -49.24784 | 2025-08-10 04:51:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 659c1137-cafd-3077-bbcb-9a4c7c00890f | -25.08569 | -53.17895 | 2025-08-10 04:51:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| be6067a8-c5b7-3bcd-83a5-b239d0f3c671 | -22.52005 | -46.80526 | 2025-08-10 04:51:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 4bf554ca-32d2-3d66-ac57-9183d877a16a | -22.72279 | -47.39702 | 2025-08-10 04:51:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f352c631-9712-3ac4-bafa-ca0d8d697f39 | -22.98587 | -51.19397 | 2025-08-10 04:51:00 | NOAA-20 | BELA VISTA DO PARAÍSO | PARANÁ | Brasil | 4102802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8311f5c8-4176-3930-baca-6c3860e55fce | -22.90648 | -45.50653 | 2025-08-10 04:51:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f4c4c543-6ecf-360c-8709-8843e51216ab | -22.71815 | -47.39637 | 2025-08-10 04:51:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5fc03b63-2124-3cd1-9916-226e0ca7f46d | -22.51975 | -46.8012 | 2025-08-10 04:51:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f6bf2b17-b0a1-386e-9355-1a38cc35cac6 | -22.71871 | -47.39124 | 2025-08-10 04:51:00 | NOAA-20 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cff7032-5f32-3d24-b070-2f03ef5251e7 | -9.4825 | -46.2746 | 2025-08-10 05:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 74c56c5e-3b62-3d4c-8af6-c83fde8b994c | -8.7825 | -46.395 | 2025-08-10 05:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 9dd27bce-7ab8-3ff5-99a8-04af3df1bb08 | -8.9399 | -60.7481 | 2025-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| ade79513-170c-3c0c-a973-c1f5d8f1588f | -8.9215 | -60.7297 | 2025-08-10 05:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |


[Clique aqui para ver as próximas entradas](README26.md)
