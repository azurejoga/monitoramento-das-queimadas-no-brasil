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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 169bdd4e-e32f-3f93-a8cf-9015ae0e4c93 | -14.07014 | -46.31568 | 2026-09-30 06:12:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 93220b6a-6dfe-3f8c-a947-f4757d4dc656 | -13.42169 | -43.80672 | 2026-09-30 06:12:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2276df9b-2b35-388b-bf6b-2b01d99b5ff4 | -13.43235 | -43.80852 | 2026-09-30 06:12:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9d15f54e-e9af-3e3c-ab7d-2239957d98bc | -11.16988 | -44.82697 | 2026-09-30 06:12:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 23d86dcd-364a-3545-970d-e7eda53eaa46 | -7.82821 | -45.82212 | 2026-09-30 06:12:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 9cf75784-f513-3b28-9405-a6348fc269a6 | -10.71719 | -44.41349 | 2026-09-30 06:12:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 2aa42101-b03a-321c-a86d-17284597594f | -5.16414 | -56.0096 | 2026-09-30 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f0356f5-0856-3920-bfaa-da5f70b8f98a | 0.13853 | -60.40538 | 2026-09-30 06:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfef6eb1-d1de-37a5-882d-0dddde2ec82d | -5.1696 | -55.99904 | 2026-09-30 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa660802-5593-314e-953d-db51e0d2c4ab | -5.17302 | -55.9978 | 2026-09-30 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd6cf8e7-7505-32ae-80e6-d9c828f6d4c8 | -3.82975 | -55.79441 | 2026-09-30 06:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ab096115-b8b4-3436-9f09-8c7427fd7f03 | -3.65616 | -58.5535 | 2026-09-30 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffdb6b9c-267f-3b71-ab43-38a4cb3df14d | -3.82693 | -55.79525 | 2026-09-30 06:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 699d4eb7-ffdb-334a-b033-a19563839431 | -3.83411 | -55.79589 | 2026-09-30 06:12:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd1e365d-2ba5-375d-9f41-02f6a4224fa6 | -3.65683 | -58.54906 | 2026-09-30 06:12:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b800fe2-b5f4-3745-86dc-88fbe899b1ed | -5.17049 | -55.99274 | 2026-09-30 06:12:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f41a9ccc-edbc-3770-a2a1-266fd7203e74 | 0.13889 | -60.40614 | 2026-09-30 06:12:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf12af30-135a-3943-8ff4-2a4b3f74a1d5 | -18.8968 | -43.80166 | 2026-09-30 06:14:00 | AQUA_M-M | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 625737f9-dd8f-3969-ae1b-62a2537796e9 | -18.30055 | -43.31452 | 2026-09-30 06:14:00 | AQUA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 33bf1b4f-e3c3-3d4f-b95e-ba7cdca653a3 | -18.50545 | -45.13776 | 2026-09-30 06:14:00 | AQUA_M-M | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 12fa2c16-1b0d-3cec-94bb-5c99066bcfce | -18.10467 | -44.40657 | 2026-09-30 06:14:00 | AQUA_M-M | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c701fef2-bc09-3198-a65d-c81db8882bf0 | -18.29873 | -43.32541 | 2026-09-30 06:14:00 | AQUA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 5137552a-0cf4-3490-86a0-d909aeb63750 | -16.6772 | -41.85361 | 2026-09-30 06:14:00 | AQUA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| cce6b56f-4ab8-314c-86df-ed08d9e3b1cf | -15.63687 | -43.23042 | 2026-09-30 06:14:00 | AQUA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 70365f85-bbb0-31f5-acc7-837712ed37e7 | -16.67877 | -41.84381 | 2026-09-30 06:14:00 | AQUA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 628611e2-4cb0-34b3-b5ba-b2352c302e2a | -6.06862 | -57.61036 | 2026-09-30 06:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 655a2046-0b59-3ff5-8e0d-2c1d91128a9e | -8.60447 | -70.20372 | 2026-09-30 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bd38959-4943-36f4-937e-22395c1304bb | -10.07331 | -63.08266 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bd4cd53f-e491-3433-acea-29168dc47e9c | -9.12026 | -67.83135 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebf11900-c93a-3289-bba1-796385d77561 | -9.1392 | -67.85083 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d413bf97-4107-32c3-a637-6c6abbee6cf6 | -11.88424 | -64.94698 | 2026-09-30 06:14:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18e189f9-e14d-364a-b6f7-bc245eba4a78 | -10.07559 | -63.08596 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8784f99a-5474-34de-85e8-07f87bb7ca1f | -9.35042 | -68.21094 | 2026-09-30 06:14:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 595e1bba-6f50-3d49-9432-281aa1d57f07 | -9.10275 | -68.20733 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaef64b9-84ea-33af-9f33-4a48e3fe3859 | -6.07525 | -57.611 | 2026-09-30 06:14:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8845fa16-1080-3a1b-a5c4-bf3c5612db64 | -8.75128 | -70.26286 | 2026-09-30 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 655909c8-620c-3afa-bd3f-30224722cf75 | -10.20208 | -68.69283 | 2026-09-30 06:14:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f1d193e-b24b-34da-bce8-0d529317dbdc | -9.01469 | -68.57182 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81d7d658-e7c6-3589-901d-dccff778fcd0 | -9.72073 | -67.08834 | 2026-09-30 06:14:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb4d6c09-daa5-38f7-8258-306595af8fa1 | -9.11904 | -67.83947 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5095e8be-74a8-3601-a27f-f9ffad7ec74e | -8.04676 | -71.35075 | 2026-09-30 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| edd22b11-40e0-3153-b064-e3afcacc4b10 | -8.47147 | -70.87751 | 2026-09-30 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 163118d4-9157-3ae7-82ff-39abcfec128f | -9.1226 | -67.84001 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98ec01ea-3f9b-398c-b4ba-604a8d9f60df | -9.07747 | -67.82475 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3034c691-e53d-3311-a065-e996792600e8 | -9.19625 | -67.74992 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35cc2e76-aa7f-324f-bb5f-37e2f91a5ea6 | -8.93992 | -68.6684 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7550111a-705f-3bf2-91ac-4695e4c8d962 | -9.10956 | -67.8297 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed8c4ae6-e897-3c3f-b009-31b95372cb5c | -9.11242 | -67.85912 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e6891d7-3b85-3139-be9b-99e3b231364c | -9.19686 | -67.74581 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ecdcf933-6d80-37cf-bbbd-7eda351aaa84 | -8.78687 | -70.80582 | 2026-09-30 06:14:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f434949-d493-3d28-9615-94665c88aab3 | -8.77755 | -69.49347 | 2026-09-30 06:14:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2716de1-8478-3f33-bbb1-92adb2fab713 | -7.26671 | -72.69305 | 2026-09-30 06:14:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d103a6dc-f9b0-3603-b1c7-809ad4bc6706 | -8.37815 | -71.183 | 2026-09-30 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ffd065c-1ebe-35ed-943f-07f7e5c660a1 | -9.09574 | -68.20625 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5cf1df2-f357-32ae-b4c9-42f3d6293d68 | -9.45602 | -68.71929 | 2026-09-30 06:14:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5af70d9-b9d5-36e8-8060-c6b4743f8cbb | -9.40042 | -68.16609 | 2026-09-30 06:14:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbfa62c6-9200-39de-ba8f-034ba6c3c875 | -9.16947 | -67.6758 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64209967-521c-39fd-87fd-a7575dbcf70f | -10.07635 | -63.08054 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 744cc720-ce55-36d9-9b71-48dc51592ae9 | -10.0726 | -63.08805 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 31849dc2-2a76-35ac-974d-29a594c287e1 | -8.77757 | -69.53735 | 2026-09-30 06:14:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40aeeaf6-9df4-333d-833d-62ca41e41f0a | -9.0141 | -68.5756 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e67ed13-e2f0-3479-b802-340ee3094202 | -9.106 | -67.82914 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7bf0dd4a-306b-376e-93a8-92a586e30182 | -9.12678 | -67.83651 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46c04075-d0de-3abc-8512-88dbd71e6c4f | -8.77421 | -69.53682 | 2026-09-30 06:14:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55046149-9891-3c31-b73a-b590327a6a59 | -9.10895 | -67.83376 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22e44d16-70cf-3c7d-87f9-dcbef7befac2 | -10.06843 | -63.08204 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41a8c096-4892-3645-8bcd-6b82526b24b4 | -9.09925 | -68.20679 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79581e7d-3eb4-3dba-8764-bb6c6db22dba | -9.12199 | -67.84406 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ab9bcbc-79a4-309b-a982-67136bc5df4d | -8.77477 | -69.53324 | 2026-09-30 06:14:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a90a44f3-02e3-3b76-8a0e-321fed19a799 | -8.01853 | -71.07793 | 2026-09-30 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8419787-c2e7-3af0-b96a-740ebe1f9ab3 | -8.09675 | -71.32953 | 2026-09-30 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d2912e9-70dd-38ba-853f-8bf9ff584c7f | -8.39995 | -70.76916 | 2026-09-30 06:14:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11c7146d-a87c-3103-86c8-ebaad6fe73bd | -11.88864 | -64.94762 | 2026-09-30 06:14:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30d14b66-4957-3951-aa32-6478e9d83a5a | -10.07146 | -63.07997 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 88795a38-d6b6-3114-adae-f75c4c1ca881 | -9.11965 | -67.83542 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9adb3a-a67d-3b8c-8fbb-43a62f02b82e | -8.7781 | -69.48989 | 2026-09-30 06:14:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ced942-5ab3-379b-b8f7-dcd9b19f7423 | -9.473 | -66.78365 | 2026-09-30 06:14:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89b38a44-454f-329c-b354-9e5c68ae1786 | -9.12321 | -67.83596 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c48af6b-9c9e-3d2a-921d-329ad839436c | -9.13207 | -67.84974 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c4eab42-ac7e-3ec4-b303-5320a7103117 | -8.93648 | -68.66785 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ca3ea4b-f03d-37c8-8791-915410627a30 | -9.1167 | -67.8308 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b695766-ab19-3cb1-8f69-6ea1120c7046 | -9.13564 | -67.85029 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4752c9c-76a8-3236-b8c1-ad640cda2877 | -9.16852 | -67.73035 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d32a9e3-e1c1-3ac0-8957-b706ef941a33 | -10.07071 | -63.08536 | 2026-09-30 06:14:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f6d766e0-d606-3c89-add8-623575dca8cf | -9.11608 | -67.83486 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a087d9e4-2d9f-38f2-8307-268035c41c78 | -8.84505 | -68.69659 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e386a6-9bdb-3f7b-8097-28c0ffa8769c | -9.12416 | -67.75703 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 962f698c-b5af-3396-a095-941bc14138c4 | -9.10539 | -67.83321 | 2026-09-30 06:14:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2bf6400-577b-31e7-8467-30601b17b40d | -10.20287 | -68.69533 | 2026-09-30 06:33:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89d27ae0-4d00-397c-974c-1f248d29ab3a | -8.01588 | -71.07756 | 2026-09-30 06:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b084ce5e-fe46-3497-9ba1-f805c86fed71 | -7.93196 | -70.68557 | 2026-09-30 06:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c3d9c40a-771e-3a48-a627-412399f3266d | -8.84544 | -68.70004 | 2026-09-30 06:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 231113e0-cfed-3488-b075-51d78237d257 | -8.78569 | -70.80617 | 2026-09-30 06:33:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2446abbf-47a7-3831-a896-ea947615cc06 | -8.01531 | -71.08157 | 2026-09-30 06:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8029aaf9-a31d-32cb-8cb4-6bc78ef827a8 | -7.72562 | -72.47493 | 2026-09-30 06:33:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe28167f-e0e3-33a8-accd-22c09dab78a8 | -8.02693 | -72.3068 | 2026-09-30 06:33:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 918475c0-c108-3f55-b9a2-a248962b77ef | -8.0535 | -71.05836 | 2026-09-30 06:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83a29337-918c-307b-ae13-1700fab4e5db | -7.93279 | -70.6829 | 2026-09-30 06:33:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a3a8de06-4355-398a-a84e-2bb739da68fb | -8.02701 | -72.30408 | 2026-09-30 06:33:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2887fd1a-7028-3060-a135-317bb887eaa2 | -8.84583 | -68.69704 | 2026-09-30 06:33:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README63.md)
