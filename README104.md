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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6481755-d3dd-3073-a6a3-d17cc0edb2b5 | -6.42133 | -55.20029 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ed024e9e-0c53-3535-9a6a-c6c4751d3b19 | -12.01638 | -43.46568 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1719415a-bd8f-3346-883b-0c94a72d8881 | -10.7719 | -46.56778 | 2026-10-09 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 132d4bbe-e3c7-3f2a-8a17-f6677187b6d7 | -8.08098 | -45.64486 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d77913-647d-3c66-9fa3-e925e2a29eac | -12.22797 | -57.11309 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8071fe5d-6e5b-3fad-a153-b508d677451a | -10.70303 | -44.49473 | 2026-10-09 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f489bc6d-d269-3cf6-b742-5ab5126270a3 | -12.21273 | -57.10693 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 467fe987-27bd-303f-b2d0-514b43442082 | -9.83558 | -44.78745 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 904464c7-92aa-31a9-92de-e3fb8b094d1e | -6.49997 | -55.30669 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60930f66-a062-3432-8b33-7cd1c91db943 | -8.28439 | -45.73782 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96660dcf-d32d-3c5c-b974-8bfc112fc098 | -13.04888 | -47.03893 | 2026-10-09 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b460e43-1d46-3041-bdbb-278caac0db5f | -7.39774 | -44.75662 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d047e1c-37e7-3ce3-b676-98012cffe673 | -8.90941 | -45.22184 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fc3d532f-ba4d-313a-a16f-4f0734afe4ba | -12.30173 | -47.05573 | 2026-10-09 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8c76da34-9dcb-3ca0-8ccb-92e6ed464725 | -7.58395 | -45.65151 | 2026-10-09 04:27:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2be6e71-409d-34f3-a93b-345fee5743eb | -12.01009 | -43.45473 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3429c631-6aab-3c16-9d87-66bc906e3706 | -11.76043 | -44.95763 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 200335e3-0866-3a9e-bbc4-971aed2f23d7 | -11.25094 | -46.27697 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33b19cef-e2f4-38dc-86ce-c061e8050502 | -8.44971 | -44.68421 | 2026-10-09 04:27:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9784ebfc-f3c4-3d35-99ac-294ea13ec00b | -11.78205 | -45.58056 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ca40596-b8b1-3729-a78d-6233db368d0b | -8.91114 | -45.23346 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f68a90b3-0e19-3412-9d09-7b66e25ee447 | -7.48408 | -49.41166 | 2026-10-09 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a3e5e278-27de-3b90-ab6b-067d5493b543 | -9.29921 | -47.46388 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cc904429-4001-3e7f-b584-dcae2835c83f | -11.08834 | -44.05952 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dadbcb6f-1e5c-3e9f-9ca2-8cafaa1123ea | -8.90656 | -45.21761 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c97786e9-ce69-34a4-9536-79d8a46b2bbc | -11.12872 | -46.16939 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 312bd23a-1622-3c8f-af94-ccb30f28d55c | -8.17439 | -46.38917 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bb59527b-c777-3e9c-b789-818a16880d03 | -12.84526 | -50.58406 | 2026-10-09 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f03733ea-1172-3f61-bbc7-1b82c301f720 | -8.19983 | -46.42163 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c0c2d74c-3603-3622-98a9-e981c547f215 | -6.57717 | -53.02708 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af5e0131-3b12-336c-9c98-551774618f14 | -8.90996 | -45.21814 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bc6d2c2-d623-31c5-b7c9-67c96e702dc4 | -13.12928 | -46.3251 | 2026-10-09 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c949f6c-fc54-3b2e-bae8-f168550ff692 | -6.54445 | -56.04196 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 681400a2-c3b6-3416-ac57-423eb8e4342b | -14.78553 | -42.89497 | 2026-10-09 04:27:00 | NOAA-21 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b90688f-eb84-3811-b2bc-e3fa679f06ce | -9.87852 | -50.48866 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fbfca2b8-1fb3-3310-8353-5262684fb4a6 | -7.40855 | -44.75449 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d238f2df-a2b6-3808-aaf0-99e6da7c3fb5 | -9.29697 | -47.43502 | 2026-10-09 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| e54052a1-0d1e-383c-bcb8-b1ab961b2c32 | -7.39886 | -44.74921 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| b7f87751-c0d1-3e8c-8cac-4981094d52a6 | -10.92907 | -45.38087 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6e33c51-84a2-3a5b-93bc-8c858b32a0f6 | -7.08287 | -52.68975 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45e99b6c-4a39-396f-b33a-23f6a0e31f6d | -12.22267 | -57.11217 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 89785307-d182-36b1-8728-911e6bf46833 | -9.88145 | -50.49336 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66e84782-8874-363e-b4a0-c5a0e2a9f9d9 | -6.13102 | -55.6822 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09185230-55f6-3e80-9d6d-76c6ec336cbd | -6.49887 | -55.31289 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 874b4c27-87d8-340e-9cbd-6be23a0f7ad8 | -6.51438 | -55.40726 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b425621-e61b-3a30-bf6e-9a43d3d80017 | -6.43855 | -55.04274 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bb3589c-fd8c-3c01-82ac-0cfc30e83894 | -11.58346 | -43.65734 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 67607b82-443c-3f5e-afa1-c718486fa93f | -9.87354 | -50.49638 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 33084145-d523-3f73-a04b-34c02f39a248 | -11.27684 | -45.18815 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 066f7b4d-b25e-3670-83ff-0ea905fc0f1c | -9.89134 | -44.79589 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09aedb61-ae6c-3c45-91fd-113f33680d5f | -7.40513 | -44.75399 | 2026-10-09 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2375226c-a18f-3337-86c3-17d07eb799c0 | -7.53321 | -45.8707 | 2026-10-09 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe29675b-48f4-326c-9dbd-d8e678e73489 | -12.21748 | -57.13876 | 2026-10-09 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c030434-0e81-3d7c-b58a-3da772c8c39a | -9.89 | -50.48637 | 2026-10-09 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3022111f-6e94-375e-9a8d-1c7e560657ab | -13.81357 | -44.19009 | 2026-10-09 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 72ab8815-20bc-3a6e-9fdc-45797b36241a | -8.00187 | -47.18826 | 2026-10-09 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6c5a5eb-6fe6-3d2b-9e50-a3f78fd43230 | -6.99843 | -59.1044 | 2026-10-09 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e5819ea9-9e79-3916-9b8f-65b6a4faba47 | -6.44736 | -52.6986 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 630acd76-7fe7-3089-ab1f-a49190565bb6 | -5.88912 | -57.75309 | 2026-10-09 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 982c036e-74f2-3ad2-9a35-19ae8d6d5fa0 | -12.00359 | -43.47345 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a22855a-1474-326a-b812-80c02928c037 | -11.08594 | -44.05027 | 2026-10-09 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd76ad92-6bee-3190-ad92-63c0b5cbba48 | -8.79648 | -47.26197 | 2026-10-09 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05c5ffa1-8b0c-349e-9e4c-fc2e9a944067 | -8.90775 | -45.23293 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 85804253-a962-3e42-acb3-c35e5974dfde | -9.0847 | -45.12608 | 2026-10-09 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87a07910-993b-39ef-86f9-154decee3403 | -5.98702 | -55.36324 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96865084-26f9-3760-a995-0a64919f87da | -5.9906 | -55.37375 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 409e98f5-9065-3db6-bf49-009a445da8e1 | -7.38613 | -55.22387 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec0449af-29be-3e20-81b9-164b24601c2c | -5.9627 | -55.37872 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a2126739-0919-3c16-8718-eec76bab9bac | -10.42623 | -47.28466 | 2026-10-09 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| aac86d29-a2e5-3d25-bfe6-526182b2e222 | -11.70553 | -43.42271 | 2026-10-09 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 120048dc-d89d-3a65-91ff-078a7c89c95c | -11.73193 | -46.73652 | 2026-10-09 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b9dda2a-4e2c-373a-85ce-ee0c77fb2655 | -10.91084 | -45.52481 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a16d73bf-508a-36a1-b678-783eceb33c11 | -8.96849 | -45.91264 | 2026-10-09 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ccd618a-54c6-3532-a306-935c167cfc76 | -8.08252 | -45.61221 | 2026-10-09 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 61eb03db-51d4-3f3b-bde0-ae8c7d44da83 | -9.8954 | -44.79258 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04e4edfb-49bf-352f-9162-e0e400aec461 | -13.16669 | -54.35297 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13bfbc3e-9592-3572-9aa7-46aa1f5efcdb | -13.82327 | -39.90491 | 2026-10-09 04:27:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c9e6ee6b-3329-37e7-99b3-6ec79d50d071 | -11.19444 | -45.31398 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f13a5068-0028-3f71-8fe9-f3e592f0c24d | -6.72852 | -48.11237 | 2026-10-09 04:27:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0fb02f21-01db-39ce-9069-2a152b22b146 | -7.51323 | -47.33113 | 2026-10-09 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dbc6bfab-a902-3e44-ab8d-c7bb1f10b8ca | -9.09728 | -59.38947 | 2026-10-09 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4d1334e-abfa-3ed9-bf50-532d24446f5b | -10.73757 | -52.03218 | 2026-10-09 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40cf7838-2b68-3481-b8dd-d819758ac806 | -13.1917 | -48.13826 | 2026-10-09 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 073bfa11-2969-3621-8ea8-e40ad521eced | -11.75528 | -61.06698 | 2026-10-09 04:27:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7636469e-fd33-3898-b5e2-32f5218e18b1 | -6.47054 | -55.4725 | 2026-10-09 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1410d35d-2bd3-3470-bf4d-a9f01b98859b | -12.02646 | -43.47737 | 2026-10-09 04:27:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f737ec0b-3c42-322b-9dd4-21bf5022d720 | -12.21725 | -44.8217 | 2026-10-09 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f317e27c-fbe3-3972-9c4e-6879e33c2a7d | -9.80066 | -44.77057 | 2026-10-09 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4b383cb-0022-3f2f-b90d-af7817f0c1b3 | -8.91265 | -45.17686 | 2026-10-09 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5356ba72-6aef-3390-a94b-0fe30b6e6770 | -11.26596 | -46.26833 | 2026-10-09 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bceb19b7-fb3d-385a-b4d2-8562a7cc7b2a | -7.81994 | -50.21837 | 2026-10-09 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0800c54d-d774-3f15-97cf-f9778e71ad7a | -6.44261 | -55.04947 | 2026-10-09 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9410ea09-7e58-3030-ab09-2b452a34802a | -6.12785 | -53.06133 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7c5ec3fa-a97c-3bb3-9262-7fa17dd399b2 | -9.40064 | -49.00134 | 2026-10-09 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 862d5050-0da3-3df0-a463-41b7642f1580 | -6.4937 | -55.31195 | 2026-10-09 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3a636b9-6ed5-371e-b786-143884763f0c | -6.25716 | -52.8605 | 2026-10-09 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e42caa20-5921-3189-8112-0f3f27610f9c | -9.03021 | -44.38158 | 2026-10-09 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d6d5047-cdb9-3fa8-9691-7efabc3c0b72 | -13.18057 | -54.35867 | 2026-10-09 04:27:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a84a0e21-698a-302d-9006-7af85d7b790d | -7.37802 | -47.02122 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3398f3fa-3c44-35fb-b7f7-9e88f3c01c52 | -11.74284 | -44.95131 | 2026-10-09 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README105.md)
