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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8430e01e-b8f9-33d6-87d6-4038021db80e | -6.29748 | -43.07857 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dce6dcbb-8720-3f75-be20-a7057500acc9 | -4.79536 | -47.26218 | 2025-09-06 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b97e0c2f-0f2e-3a32-94ef-eae1523c0b9f | -6.26763 | -43.49437 | 2025-09-06 03:47:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 797cb469-365f-3dbc-9fca-1b69f7f14212 | -3.69432 | -49.57296 | 2025-09-06 03:47:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc30fb2c-f26b-396f-ac06-a01104bc7018 | -5.82747 | -46.36 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 583c2c7e-6c4d-3e88-b36e-b3e0692a0101 | -4.89475 | -41.75483 | 2025-09-06 03:47:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8e45573f-7f9f-3f75-a2c0-ffd51e01e17c | -4.27054 | -48.18505 | 2025-09-06 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a5a28dbf-a832-3bf4-a378-b0cf077210c4 | -4.27141 | -48.18004 | 2025-09-06 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 32fe943e-f01e-302a-bca2-b4d08c16b201 | -5.75498 | -43.1285 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 09234c33-8f72-3ac2-9359-5e08e5803812 | -5.84098 | -44.12289 | 2025-09-06 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 433e82f4-ef0d-37de-8c2c-dd351ac4e4af | -5.63105 | -44.99641 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16a3fc57-24fd-3199-8707-29c6e9b192ba | -2.79057 | -49.62437 | 2025-09-06 03:47:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a562c9d-0557-3146-997d-e018297f4ade | -5.92814 | -43.01167 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2848d94d-d7b0-3efb-8fb0-0dcb7218579a | -5.73208 | -45.3686 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26e9ebda-64e6-3528-853c-2433f37acf48 | -5.55825 | -46.54136 | 2025-09-06 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2a8d1c14-90a8-366f-bea9-88f7270ed55f | -5.87417 | -46.03997 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6300a45-c542-33ec-9700-7f3f2dc5e492 | -4.45533 | -44.13708 | 2025-09-06 03:47:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a7348da-d2e9-3e84-bd64-cce8e4288974 | -5.75425 | -43.13281 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 213bc152-212d-3e09-86d1-2765dc1fdb9c | -6.19086 | -43.35975 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40dbf21e-7cb5-394f-b97a-308bab891f8e | -5.20181 | -43.69546 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2abd4c45-26ab-394a-bc9d-030558548b5a | -5.3383 | -42.78756 | 2025-09-06 03:47:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 27efc29f-b9ed-331b-999f-8759612891c7 | -6.30969 | -44.58112 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3735c19-2781-3b50-9c1c-467aa274854b | -6.38792 | -43.01683 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8408402-77a8-3b99-b35c-0c5e4638c894 | -6.22112 | -43.57829 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c5d53c6-2e40-3f2c-97e1-d6437ad8304d | -3.7948 | -47.58154 | 2025-09-06 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 517b2a50-d921-37cb-b3f9-15271cbcb817 | -6.07027 | -43.29679 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2e8df280-549d-3061-a958-eba40bec6621 | -3.96795 | -43.24023 | 2025-09-06 03:47:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35b1b225-4371-33c3-9190-bdc92533c321 | -5.21594 | -43.69188 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6aaea3f4-1adc-3cd7-b011-63dc1c325c63 | -5.20129 | -43.6944 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3dd90845-2dda-3e34-a99d-d3d577156635 | -5.83798 | -44.1121 | 2025-09-06 03:47:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6ac08d2-96b7-3bad-9502-66cc4ec4ac13 | -5.55298 | -43.06608 | 2025-09-06 03:47:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b6f3a74-3991-3b8e-8bb9-3317ae3023c8 | -5.49351 | -42.15099 | 2025-09-06 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2191d67b-cf30-350b-8c5e-41636cfe37f8 | -3.37876 | -47.61646 | 2025-09-06 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e826a12a-de21-399e-8661-06a6ac3642f8 | -6.22677 | -45.12665 | 2025-09-06 03:47:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17bec033-02a0-3f05-a94f-5163d19012e2 | -4.80206 | -47.25842 | 2025-09-06 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f1884bd-7585-389e-abf4-79c94369e311 | -6.15553 | -43.16491 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 53f1c0e1-b8c3-3718-9759-6b82f0d47d50 | -5.98547 | -44.72519 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 0883438a-6342-386f-ae45-f86f66d45991 | -5.7299 | -43.91342 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc45c67c-0770-3942-85b0-14dfee5232aa | -6.17145 | -43.61353 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c96023b-a4ad-33c3-b722-6930842e78ca | -5.97962 | -43.61247 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| df3aec8b-1606-3889-9d57-ee1b3b4fb499 | -5.94679 | -45.66161 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2bb24cd4-6768-3890-bf0c-1290fec73711 | -5.93179 | -43.0166 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 99b2bae5-1c77-36b8-9299-f09ecd142703 | -5.15964 | -42.8495 | 2025-09-06 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f88ba621-be94-3188-b454-d430b630d055 | -5.74587 | -43.70996 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a46f9f1-cf43-368c-8caf-876ae745c2c1 | -3.98288 | -47.87951 | 2025-09-06 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 582095d9-4336-3455-a62a-6c96c4511f9d | -5.40306 | -42.32626 | 2025-09-06 03:47:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 46095db5-7856-3113-a714-366577855da4 | -5.93248 | -43.01242 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| dfa817e8-c163-3566-b2b6-84593835c8ba | -5.71556 | -43.94137 | 2025-09-06 03:47:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4d5d1ae-5620-3eec-bbee-d2f3d10aa5d3 | -6.19924 | -43.41885 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f243d40-319e-356d-ad08-c9219ef6d38e | -6.55497 | -42.94614 | 2025-09-06 03:47:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a5db938-3341-3032-9838-0385467f0376 | -5.99035 | -44.72601 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 15c21648-0445-33da-bae6-4ee62d122b09 | -6.16927 | -44.31165 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b322fd7d-2313-348a-bb17-ca5dedb199d2 | -5.98059 | -44.72433 | 2025-09-06 03:47:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a20da475-0359-365f-ba60-6c8a5c871f9a | -4.9854 | -42.06807 | 2025-09-06 03:47:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ffb47947-143d-3bee-9b3c-e8e153c836ee | -6.15481 | -43.16934 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 02ddb61c-ea35-3097-b49d-cb39fc875298 | -5.93612 | -43.01739 | 2025-09-06 03:47:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 6c16450c-3a23-34a8-9e39-ccf2126957e0 | -2.65549 | -48.79699 | 2025-09-06 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6e8e6416-a10c-344e-b64e-03c33724de9e | -2.46941 | -47.77234 | 2025-09-06 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55af340e-3fb5-3428-9895-aabe3ec98895 | -5.20258 | -43.69078 | 2025-09-06 03:47:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f5f19647-eb49-30b8-ba13-a8dbb0f6d613 | -2.55144 | -48.38901 | 2025-09-06 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8a991ed9-9283-307e-aa94-b934a24a778d | -6.17012 | -44.30679 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7da3db3-b89a-3c64-afdf-55685356d325 | -4.79988 | -47.26115 | 2025-09-06 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4712c061-8bc6-38ae-b551-0c1849a23275 | -5.8669 | -46.03117 | 2025-09-06 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fee1b74-2edb-37aa-be5a-02aa544e481b | -6.34942 | -43.5429 | 2025-09-06 03:47:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98cae36a-83b5-3967-98ef-ce1b6191f1b7 | -5.73261 | -45.3655 | 2025-09-06 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0edf9fbc-fc98-3877-bb06-4e8186a5dace | -6.15552 | -43.16798 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6ba57bc8-28e1-36eb-bc97-c6f41be9d847 | -6.03439 | -43.70197 | 2025-09-06 03:47:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de6ea7eb-b37c-3913-87e0-ec32b6214dc1 | -5.9804 | -43.60792 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b5dc3f45-a66c-30c1-ad40-9b4f048942c8 | -2.55059 | -48.39045 | 2025-09-06 03:47:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 429b25b0-e8f5-3783-af7d-054d0a0c3a26 | -3.48186 | -43.33099 | 2025-09-06 03:47:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1da28e61-245b-3547-81c3-7c1a21b734bc | -6.20955 | -42.62393 | 2025-09-06 03:47:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f28973ff-5250-32bc-9db1-dc9bebf7d55c | -6.06953 | -43.30117 | 2025-09-06 03:47:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7e3ddbb0-cc71-3377-ab7f-78b28cf646ef | -4.98479 | -42.07182 | 2025-09-06 03:47:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c989be55-06bc-3df1-a317-139aa06d1728 | -6.0629 | -43.34041 | 2025-09-06 03:47:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d949d5d3-fdf9-318d-be00-9aae18e9e082 | -6.16463 | -44.31035 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| affe6e22-db4d-3bc8-9c2f-d0c3135bff93 | -6.1918 | -44.77191 | 2025-09-06 03:47:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b41756ab-fa68-37ef-86ba-9dc3fcc61dae | -5.16033 | -42.84538 | 2025-09-06 03:47:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8bc240c-bc35-33c8-8ab9-ebf1fb886495 | -5.62805 | -43.65195 | 2025-09-06 03:47:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50b5eb15-a94b-393d-938f-4fbe77edb109 | -5.44573 | -42.80901 | 2025-09-06 03:47:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e3fc85ca-ab96-385c-8496-4c02d29b9d40 | -12.6512 | -41.23679 | 2025-09-06 03:49:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bdb9cb74-a7f8-3815-87ee-4234adff4aa6 | -7.32756 | -48.49852 | 2025-09-06 03:49:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cdba9bd8-c174-3956-989a-84c9dfc289b1 | -6.60597 | -43.97409 | 2025-09-06 03:49:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c8838f7-cda2-3fd4-85d5-5bb4c04c8edb | -8.93845 | -48.65262 | 2025-09-06 03:49:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5579553-bb34-397a-95cf-b0b45090392a | -12.9175 | -48.01565 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81f516b4-a16e-3ebc-a306-9760f314b0b0 | -10.76583 | -48.27336 | 2025-09-06 03:49:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e37589c6-6d83-3889-9d5d-059737b4bb5b | -13.36314 | -46.83387 | 2025-09-06 03:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 677fc901-e5f7-3660-92b8-53c47e412be5 | -9.68536 | -51.10321 | 2025-09-06 03:49:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8ba1efd-10a7-3fca-9a73-ce2a98d5832b | -10.06658 | -48.07579 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bfbc0430-6e5d-3456-bf54-42d2591ea7c9 | -12.78662 | -48.1592 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d764d4f-3fa9-3d15-a656-7b09afc1d74c | -13.00235 | -48.05124 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6453155-58b2-30ce-bd08-5f657cdfcdd9 | -9.4089 | -40.31046 | 2025-09-06 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 12e2c4dd-bdc4-3b18-a0be-fee0ac04194a | -6.54559 | -49.50727 | 2025-09-06 03:49:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c59847ee-284c-3dba-a824-5ec2d97837ac | -6.93524 | -44.97143 | 2025-09-06 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 825c276e-9b45-3ef3-b53c-66dc2e9dfacf | -9.83066 | -46.54286 | 2025-09-06 03:49:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da3b19b5-a74e-3717-93da-1d49eefe6d5d | -8.8839 | -47.25687 | 2025-09-06 03:49:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6dd8d4af-1b64-3476-a4ab-6a9e7a8a5300 | -6.64237 | -43.41756 | 2025-09-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01f57bfe-5348-3f9f-93df-466dad2917e6 | -10.03829 | -48.13091 | 2025-09-06 03:49:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 739e6b2c-08f9-3888-94b0-094526992f51 | -6.6475 | -43.41405 | 2025-09-06 03:49:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0363df5b-803c-31d1-ba2c-33a3c112caea | -12.93334 | -48.04908 | 2025-09-06 03:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78742a56-464c-39a8-bff1-e926479f08f2 | -6.87298 | -45.55724 | 2025-09-06 03:49:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |


[Clique aqui para ver as próximas entradas](README22.md)
