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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6814e958-2807-3abb-8514-01ea5075d9a4 | -3.44131 | -50.60811 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f3a5a11-875f-33ff-a92b-c391a7011f85 | -2.56838 | -57.51295 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5e33df9-9440-3ec7-86c9-3d8d840ef98b | -7.57093 | -57.68774 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21f07d04-4132-3785-b888-d4b2b9d0421c | -3.07153 | -54.39919 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f0ecb6f-e1a2-3a19-a1f6-d02256746514 | -6.44512 | -59.9724 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 7e8f89e9-2f9a-3c5d-912c-cf92ad41c959 | -5.87852 | -52.0519 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d8765bb-9aa2-355e-8dd9-7ac6e62a9814 | -3.00284 | -54.16957 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99169fd5-b81b-3c57-b21b-bc266da93d6f | -6.18751 | -57.77406 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb4082c1-277d-3a17-b81d-6c106936a493 | -3.75597 | -59.31289 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a94c33-55a6-3cd5-80c5-12e7de1b7806 | -8.79359 | -44.28746 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b0c66f3a-4c67-34a2-b9fb-b55baf77258c | -6.1603 | -49.8829 | 2026-09-22 05:23:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6610d4c-0e30-34e8-90d0-fbdaa8b51b3a | -2.16633 | -47.88285 | 2026-09-22 05:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d36f8cb3-15f7-3ad8-bde1-ec7aaba470f2 | -8.3499 | -50.87365 | 2026-09-22 05:23:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 517835fe-76b6-3695-b63b-79f36311ffc9 | -2.96053 | -52.14313 | 2026-09-22 05:23:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dd83dc3-f979-3d28-9847-038982587f36 | -2.94828 | -51.04156 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f26bb529-dd4a-307d-8be0-8314f60c6c22 | -2.61748 | -51.72931 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a9348bf-c661-3d24-bd36-2235136fee26 | -5.83389 | -52.05236 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 296d3ed5-b23a-359b-bd6a-6503a16ffed9 | -4.45057 | -55.43764 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41dbaf3f-9687-39ed-bd3d-13e6a1a909a6 | -2.79155 | -59.89522 | 2026-09-22 05:23:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 345bb4f1-8837-3f8e-b4a6-58f371e2079d | -6.76561 | -59.62495 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4814ada4-dc54-3ac8-9fbc-47da605ad38d | -6.08167 | -57.62885 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b6bfe7a5-ef04-3a83-9dd9-131e867bee89 | -10.90942 | -53.95653 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 820b1177-8745-3f64-98a4-0f75b8f0cb11 | -6.70624 | -59.00098 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77dc50c7-6409-3a1b-9677-1f394d483646 | -12.80026 | -54.04538 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54831fd9-2e9a-3d49-8fcc-b23208593cea | -4.67933 | -55.62685 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5d581cb4-e2cf-35b8-88d2-7fea5dbb1f49 | -4.35021 | -55.65729 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ec99ff9-f37b-3471-a469-3acb0dadaae6 | -3.46181 | -59.52911 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c68235-cb90-3baa-8eb9-3b394106cbfe | -12.56471 | -45.98133 | 2026-09-22 05:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 9e84d505-d761-3fe2-aa26-1e8edf8dc233 | -4.27194 | -55.44247 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6adeea8e-e852-38b5-8780-0f220c037e52 | -9.62597 | -43.94818 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d409415b-00fa-3fcd-9f0f-f8768f636b21 | -8.22933 | -54.68235 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc78ac6a-3423-3e2e-bfff-9ae096bf296c | -7.00001 | -49.93705 | 2026-09-22 05:23:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 356211a9-399b-3e36-851d-cbe5992d6cc5 | -13.51851 | -51.50799 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 7abc3e2b-4ddd-3f4d-ae98-a97dc475dd90 | -10.87364 | -53.9563 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc3cd8f-b7c1-32a0-97f8-3fb60a0e02de | -6.45218 | -59.97356 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c5ecaa34-ade2-3119-a390-82f7b0d8678a | -6.30984 | -60.00885 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f74dcc9-438f-31eb-8d60-cf38ef9d2d6e | -5.74993 | -45.08742 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| dab30cb6-10ce-3f98-b4f5-91312b5e0486 | -3.48672 | -59.56923 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 009448f0-99a5-3b13-aabf-a463b48548f4 | -9.10727 | -65.38114 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 393c8f1b-cc43-3040-af1a-b1b6eba29fb3 | -5.83351 | -53.51015 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 177da199-aa7b-38ae-a4c9-73099fe9f700 | -3.16335 | -48.07758 | 2026-09-22 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8302a5dd-5125-3152-94de-9a53bd707647 | -9.76688 | -65.06225 | 2026-09-22 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f27841cf-a2d6-30da-b8a1-0264c4f0f16b | -3.97196 | -59.63058 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7ed096f-b8cd-3f93-a146-b2f551f29a8d | -11.68507 | -50.98363 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 279c9a64-3fba-3eb9-b1b7-107a1f5ed31c | -3.00696 | -54.16624 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f15b5165-fd1c-35a7-8b55-dca7bc2e573f | -3.92031 | -56.05331 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f318c39b-49e5-3061-8ae7-a267a6f781e9 | -6.61762 | -59.91051 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2c9b7b23-954d-32e9-b9f8-dd5eef94cba6 | -2.88434 | -54.07677 | 2026-09-22 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1cecc12-f409-3e6f-95fa-5939d740a47c | -6.44446 | -59.97638 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 9fbf84b2-dedd-3036-af1c-85ee96dadbd1 | -10.90337 | -53.97079 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29cc4b08-25f9-3330-8a9a-bf79ec239ea5 | -6.81136 | -55.82625 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5d4a14a-4cef-3378-a6ed-96c519dc9c20 | -3.06912 | -54.41447 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e12656d9-cfb9-342b-8657-3e3a7460228d | -6.35193 | -55.84206 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de2d8e42-5979-352c-b55d-c970d515ffaf | -3.44502 | -50.61295 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c5c6bd5-8f48-3274-bf56-48da29d3ea33 | -6.77745 | -48.66809 | 2026-09-22 05:23:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8b97848-c702-333d-af07-5cd3249bc634 | -5.91219 | -57.67635 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29c29321-2c44-31be-b535-9e80ad51a0e5 | -6.08556 | -57.69005 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 71202ac6-00b4-3928-ab1e-6203372c47e5 | -3.42992 | -61.32282 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27a65b96-f074-3187-a16a-38b2dfa3727c | -5.82071 | -57.74411 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33f3b59e-8247-3225-b97a-bee9a346da7c | -6.75572 | -59.06094 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 660a66b5-26df-33af-b207-f3554c26df87 | -6.66613 | -50.94831 | 2026-09-22 05:23:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32b67410-9e71-392c-b4f1-e8885018e42c | -3.22187 | -61.05387 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e693f889-e796-3d6a-b797-db277c55e105 | -5.81515 | -57.7361 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b00420ee-d83d-3e49-adfe-c29aa36c2bd1 | -12.82379 | -54.02235 | 2026-09-22 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 440e18d8-57e8-3426-acc4-abf3848e0ce6 | -3.73182 | -58.4943 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ec47c2-8a00-3826-881f-b1c2c5951790 | -5.21248 | -56.0739 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 205f0988-86e5-30ac-b5e0-04fa11924822 | -7.6066 | -55.35787 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2cd3cd0-6dbf-3988-9149-77ac58d68044 | -3.34491 | -59.86414 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68da4044-93f7-3a60-81ea-ba8bf4c9bd2a | -4.95888 | -55.82764 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4c65b73-7b85-3df7-8ddd-1b3e03f58af2 | -5.87642 | -52.0661 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b00feab-2d50-388a-8281-b08304f7d14a | -4.20656 | -59.91178 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 995a27d1-046f-311a-a142-ebb08450a05e | -5.75672 | -45.0777 | 2026-09-22 05:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 542ffec1-6704-3661-89e1-1edbb4e134a0 | -2.16454 | -47.8871 | 2026-09-22 05:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07606cfc-9bf5-3568-abd0-0fa57096f4c9 | -3.6857 | -60.59026 | 2026-09-22 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 886e44b9-0b18-3412-8d82-4d37cd12f09f | -3.12977 | -51.60508 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 422f83fd-dc01-346c-b1c1-0eaa38a105a0 | -4.51901 | -55.76318 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5efaa290-6018-3b2c-beab-ed75498a7fb2 | -4.27676 | -56.25557 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de9a785f-9b31-3ee7-b844-67402303a2e2 | -11.01447 | -54.14516 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84cec315-643f-341f-9770-5cb8b18484e9 | -4.78007 | -55.69799 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e32317e4-04b0-347d-b96b-77a76680737f | -4.29623 | -56.26223 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 846074ee-9839-3876-8949-bf02b69f0383 | -5.78448 | -43.7744 | 2026-09-22 05:23:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7a7de7ec-30d4-34a9-bf15-888514d6960c | -4.31025 | -55.59582 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55eeba47-7a3c-35c1-bb18-8cf7dd4122d5 | -11.50416 | -51.5113 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d5eae926-3ca5-39b7-becb-c5a19d6956fb | -3.30903 | -57.85823 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef53e77e-01e6-306d-849b-4707371e6be7 | -6.7854 | -59.13727 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981b2ff7-a93e-3a61-9241-40028bcd43de | -7.87627 | -54.7268 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d3fed4b-f3c1-32e2-bae1-e9f84eb23f9a | -3.48473 | -59.58137 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90da74bc-4987-3711-915c-f6cd73ed8d30 | -9.61959 | -43.93993 | 2026-09-22 05:23:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 66624a02-3d8e-321b-a0eb-257199509e6e | -7.42523 | -49.85425 | 2026-09-22 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f801d79e-220d-36b0-9b8e-202b340b1bb7 | -3.26961 | -54.26423 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c52c2e8d-1cde-36b2-9dca-357b4455b9a1 | -3.93789 | -59.63749 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7464140-b386-3b73-a31e-d8213049df6d | -4.52965 | -54.972 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 817e5d5d-cfa8-3b51-b590-9a868614c18a | -3.4375 | -60.09927 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 711d43aa-ee30-3093-866f-ae2d941f7b47 | -14.7687 | -48.44638 | 2026-09-22 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62bac8ff-e852-34dc-b017-17f19b8f43b8 | -10.89489 | -53.97447 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b91dfe68-9d4d-30de-a5f2-889bfada997e | -11.23737 | -54.11072 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f737541-cab6-3b69-a05b-37bd1796b665 | -6.00676 | -57.67769 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c62e66b4-16fa-3e2f-88d1-c8339e800002 | -6.12219 | -57.76015 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 798c144f-5f01-34fe-9af8-066c21f44e21 | -9.67056 | -66.82875 | 2026-09-22 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbe2340f-f6b0-3d32-bb69-f93fc73acd14 | -3.28404 | -52.59929 | 2026-09-22 05:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README85.md)
