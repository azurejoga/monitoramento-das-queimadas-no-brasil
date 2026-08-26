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
| abb88d25-99cd-3eb8-a6f3-6df2c862ed3b | -12.12595 | -43.38105 | 2026-08-26 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcac82ed-ddbe-385b-ba20-63d14224be7b | -13.55649 | -43.92101 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 242f550c-b77f-30af-b39f-3832a25f2351 | -7.30869 | -42.98779 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9e734d21-1868-3e60-932b-af564b214c93 | -10.76732 | -54.0327 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1137d953-bedd-3bda-a4fe-6b1c21c4fa10 | -12.67456 | -48.40771 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e55d626b-0335-375b-bff9-61c66295370c | -6.26563 | -53.37415 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1c242882-4a55-3b15-8cb2-98c8b4a9ca4a | -7.2556 | -49.85093 | 2026-08-26 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9f958c06-c1f8-35a2-80fa-3e96d892400e | -13.37389 | -48.21588 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 606d9a9c-910f-3f83-9ec1-8674c884c5cf | -8.30772 | -45.71676 | 2026-08-26 04:08:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d1e9fa1-2dac-3897-afff-0342d9a64b0c | -10.37871 | -48.26976 | 2026-08-26 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00bc977b-e549-36d7-93fa-ea3f7e4f4631 | -7.75657 | -44.76335 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| adc63637-9fac-356e-ad2c-07d644e57018 | -9.60963 | -55.10939 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6efcadb4-bc58-3702-8ecf-9e0c7280e4ad | -10.16293 | -55.30756 | 2026-08-26 04:08:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5696581-38d1-3605-acb0-c3725e47e1b8 | -7.30164 | -42.9633 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 288e7054-4281-30ed-9fd4-0317a56cc736 | -8.94839 | -50.77673 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b0fe531-8098-3d84-bc64-109efb744a49 | -12.02457 | -46.0135 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 372646f7-98ed-3c26-9573-1050cf1e1d94 | -12.69733 | -48.39415 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1db5ed9-57b7-3ace-83bc-206758c5145d | -11.25483 | -47.05556 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d489a41-325c-332d-a483-d29d1ac2b890 | -8.01273 | -51.82813 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 282eb043-f83a-3f86-82b2-5ccb5370567e | -12.66524 | -48.41659 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b4beb249-606d-3bb3-98e6-2a29189af401 | -6.25313 | -53.36515 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5ce1ffb6-2c1a-338a-aff7-99356786fcc3 | -13.37108 | -48.20669 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40053cc5-e3df-3d93-a9eb-9c6262d210df | -11.42468 | -44.54396 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14a3d1f3-094c-30e3-b8ad-63b098954842 | -11.25832 | -47.0604 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31fbbe19-83fa-302c-8453-69ed41a818fe | -7.3177 | -42.97705 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9610fc33-4855-3906-bb30-ce9ea475d07c | -12.67144 | -48.40835 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4173630e-d4ae-39f9-a82f-42177fb9e35b | -9.67132 | -55.09983 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 91a30148-5fa0-3497-9645-1f385eaee22f | -6.9166 | -44.66268 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44f9bf03-6164-3d0e-ad66-8fcd60d700d3 | -6.29837 | -53.58187 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6107e665-2583-3174-83fb-644aabbed691 | -13.36739 | -48.20216 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f30dc1fc-8f0f-3ba2-afca-04fc5d3f7182 | -11.01193 | -45.07041 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 395847e5-7eba-31d6-9373-908a5e83eb64 | -8.11286 | -47.4653 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a33ae93a-ab5c-3dbb-8513-fbd4ca9263d2 | -12.76439 | -46.45905 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 8beb0a4f-ad45-326d-be06-d8101d0c8c3c | -6.25766 | -53.3772 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 597c5a54-e5b0-3763-bb3c-93137849015d | -11.96972 | -45.88908 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7fdbd390-235f-3f94-bc70-77d361baf01a | -7.05264 | -41.50651 | 2026-08-26 04:08:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b028af3d-533b-3644-b241-ddeb37499fbb | -12.62794 | -48.40846 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f22cdb56-e4f0-37be-8f25-13bd25e1f060 | -9.02037 | -50.7818 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ced85af4-31a7-38be-bad2-cdeca68deff9 | -6.8354 | -52.51005 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e084eb8-56cc-32ee-a3b1-3af48852fa4b | -12.69904 | -45.82645 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9671c5e9-249a-3392-8672-76cf340665eb | -12.02069 | -46.01278 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 1bf3b25b-680b-3137-97be-47d70411957e | -13.35378 | -48.2264 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15332002-d411-3c75-86dc-4b20deb7030d | -9.60091 | -55.11536 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d8dc886d-1d3a-3ee7-ac37-b057af49d838 | -7.16524 | -42.80091 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c30ff90a-0540-30d6-8015-f82c5b1c7587 | -6.15511 | -53.69192 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57138889-a7ec-3a08-b97b-2771d62eb089 | -7.8612 | -46.11481 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5cd24fce-8ff1-3214-8759-5818749c7ce4 | -13.3315 | -48.2258 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 729c033e-64be-310d-93a3-76dc77dcd533 | -12.77205 | -44.25814 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b29fedc-9c52-379b-bdf7-43177d70645e | -9.39432 | -45.50389 | 2026-08-26 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b9582107-f652-3b75-88f0-7fd4f0d74cbe | -11.27312 | -47.0753 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d92fdeb3-2594-307e-93d7-6f866310a7a6 | -7.45769 | -46.01581 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ada7de3-20fe-30b6-a278-aed7257066c8 | -7.27955 | -45.35327 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c2b7087-5f5b-323e-8238-fdc3040cc82a | -7.18303 | -42.73596 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0d55eaa8-cf8c-369d-a700-5dbc273f77cb | -7.13479 | -42.76782 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3820b87e-5840-3865-a611-dfdb327afae3 | -12.63772 | -48.40588 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19d5f46e-c9f9-3f5d-a4d5-0a011fb12d10 | -10.74983 | -54.01694 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21e91c20-15ca-3870-8490-d7338b87ee03 | -7.27373 | -45.3632 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f27bfa0-b129-3412-8ba6-fb323cc10055 | -8.08327 | -47.49947 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cad13a2-d9c1-3221-93cf-236fdd9a73a8 | -10.02394 | -46.421 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c6e1260-3af3-3ae1-a530-a8478a7ac0f0 | -11.15806 | -53.99912 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a2b2fdd-fd7f-3dbf-8887-be2ebeb6db48 | -12.76649 | -44.26957 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ef1e72be-a607-31c2-a625-e29679141fb3 | -7.15569 | -42.81533 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2cefed2f-ac3f-3cdd-9195-c047b648bfda | -8.13444 | -47.50358 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d098f65-b214-3fab-b5b0-8dd011f2c1a5 | -12.76229 | -46.4478 | 2026-08-26 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2506c9c-0752-31c8-bcc3-154246e0adf2 | -12.60223 | -47.92802 | 2026-08-26 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92c399d9-f364-3517-8264-4360c98d7bb7 | -11.49807 | -45.0636 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68e11557-781e-33c3-8229-4268e36b52a1 | -10.7685 | -54.02684 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| feca39f4-f6bf-3182-8835-a890deb684c1 | -9.66572 | -55.09076 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f272da49-d11b-3aec-8eec-1e7e1806d1a1 | -7.18938 | -42.74094 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1dd8b76e-baa9-35a1-b90b-c6f5524675e0 | -7.28699 | -45.3582 | 2026-08-26 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71cd1fbc-0312-3bcb-8458-a8e8b71a4757 | -6.09702 | -49.4795 | 2026-08-26 04:08:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b11857a3-7156-3f5d-b8b8-772dbe4ba778 | -7.76053 | -44.75169 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 94923f80-9007-35d4-8d28-dfdbbb3b0392 | -9.02598 | -50.78282 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 150da96d-b34a-3334-b405-3376268bfde1 | -12.43275 | -51.16975 | 2026-08-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349eceab-c804-3142-9039-52f1a36ad5f9 | -9.1699 | -49.97947 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 821b2ccc-3700-3956-9fe0-3a46cd62e4ba | -12.62868 | -48.40445 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1fe4f90-de1a-38a2-ac41-10518b361409 | -13.35191 | -48.2363 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29778412-be04-386d-8c1a-618efcaf95ff | -11.27794 | -47.07249 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01eef322-3774-3b09-98fc-7c9b51d6243d | -9.44412 | -51.67 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c8b914c1-e586-3f54-9999-fadbcbcf8db1 | -8.02739 | -51.81992 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a2820aaa-ff6f-3bfa-ab47-4ecaa902967e | -7.98196 | -45.24602 | 2026-08-26 04:08:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d5b3e8-899f-3393-811a-1d449a1fb970 | -13.35927 | -48.19718 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04e415a4-1a21-33c8-bc20-4f7dbc875f0b | -11.34028 | -42.12598 | 2026-08-26 04:08:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7435dc43-3f3c-38bd-bcb5-5cd7ade9e21f | -11.25555 | -47.05144 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0bd18a12-3698-3783-9af3-b61aa2a7345a | -6.27488 | -53.36267 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6627dde7-98d1-311d-b33a-0362a4ce4a7e | -8.86146 | -49.71808 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 389c3390-eae7-3153-ae52-008cc3229c16 | -6.83602 | -52.50749 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 675e0f3e-e741-3b6e-ac7a-841fe4d2ab4b | -11.79739 | -47.64597 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07e76b99-6e55-31b4-b434-e074c9c17ac6 | -9.60439 | -55.12471 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8c811f7f-2c7f-3133-9cec-e672d23c38cb | -8.77246 | -49.97061 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33f0dafc-319d-3037-88da-56e8767ba695 | -7.75977 | -44.74395 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d1530357-4844-35d2-8901-3fff49c20d3f | -8.0636 | -47.53033 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 88bc8dfc-7e8a-3740-a5de-1e99441358cd | -7.75817 | -44.75363 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| cab837ee-eca2-3fd3-826c-6d87add8195f | -12.00071 | -45.94054 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 656c5804-b4db-3ded-9104-84befbf6df4e | -13.335 | -48.20648 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b448d634-2cb9-3684-96af-c6629290c0f9 | -8.16807 | -46.19835 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9cd1b30c-9d74-3cec-80e8-fb16570fad62 | -7.51664 | -44.95139 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5cf6cd7-f1d5-3918-aa05-88eaae08e625 | -12.76014 | -44.26432 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8fed91d-30e6-388e-b5df-90bb67bd0342 | -12.43206 | -51.17331 | 2026-08-26 04:08:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c3e48d4-1aec-3bc3-ac07-762e494f4e57 | -11.1558 | -54.01043 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
