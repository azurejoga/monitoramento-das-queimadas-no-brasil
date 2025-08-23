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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eafa085f-a8ae-314a-957b-9101a7fcc575 | -2.71559 | -54.61522 | 2025-08-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c293718c-c5ec-32c8-8988-bfdfda8c5882 | -9.17855 | -59.66472 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3719f7a-d7ef-3dc6-ba8a-54c83511588b | -9.17933 | -59.62651 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfef6455-1f00-342c-bf7a-f3ce5692da72 | -9.18873 | -59.62369 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 25ac7227-843a-354d-ae33-0d05652589a2 | -7.31531 | -44.54889 | 2025-08-23 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9ac6dc6-2e1c-3764-bd78-1a96ac2a56b5 | -6.11944 | -44.40343 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72a8aaa9-5f18-34e6-85e4-f91010fb9073 | -5.74332 | -57.59189 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 257530ed-fabc-394e-a047-bfd2d151aeb6 | -8.78519 | -46.74677 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7cfc3fc5-e776-3c92-aa59-9c8a72c4f539 | -6.52358 | -43.86919 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aac47206-f07f-3791-aa09-9fe65a77cc3f | -6.65446 | -55.41702 | 2025-08-23 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 071fea84-bec1-3577-bf78-6a8db7c2ac1c | -7.0321 | -59.91361 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e6352806-b793-3d24-bd00-34d165a66b8f | -5.87376 | -57.75855 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b597348-e6cf-3247-859a-3e66c07345f3 | -6.27847 | -52.82893 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae1d59c4-8911-3d82-b24f-6a21907e9743 | -7.54482 | -63.85699 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d444ee69-5f22-3748-9f32-0c3d7deac389 | -5.32585 | -55.94391 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1087691-6493-3590-9461-c325b7c5db8d | -3.13178 | -58.0429 | 2025-08-23 04:51:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5aebf20e-fff8-34ea-bb28-3802c41a0b10 | -8.30465 | -47.26586 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 786c4bf4-6441-3d7e-b33d-c185888ff7c0 | -6.45738 | -53.39937 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0593b605-74a5-3348-a128-7ecbe2b6cea7 | -5.74441 | -57.60994 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40623370-6340-38bf-84a9-291be7ff4716 | -5.83563 | -45.1787 | 2025-08-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 75167233-10bd-3550-9b70-4bf50bf7baa7 | -6.7241 | -51.97464 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94779d96-5074-3f39-871d-529998f4f804 | -8.2892 | -47.26098 | 2025-08-23 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deb011ad-29a3-3f03-90af-122f478560df | -5.80693 | -59.22041 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87cbb533-e5a6-32d1-8172-7fea630bac4b | -7.606 | -46.27487 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 595d2f0b-7b02-3f84-a8c5-df33e77c4b06 | -7.8146 | -63.55593 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e16a8d2-162c-3bb4-895a-7449fa91a674 | -6.94786 | -59.55577 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a92ce4e7-3f74-3892-ae0d-43f9bb8e62d4 | -6.573 | -59.86855 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4eb8af23-9a6d-3061-b50c-631eb99210d4 | -6.68947 | -58.8636 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 212604cb-f2cd-3c06-a256-0c0303bdeb9e | -9.57694 | -55.35636 | 2025-08-23 04:51:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d9d4cea-c95d-39de-86e4-5cd363a9fbeb | -9.19459 | -59.64993 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 780344fc-c461-30c5-847d-77aa57390107 | -7.8745 | -46.29309 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae9356ea-c262-3387-b8f6-2c730ec08c34 | -5.74507 | -57.58147 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 024354f1-ada9-3a60-8a3a-86bea4779c2a | -6.48282 | -43.45877 | 2025-08-23 04:51:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ffb767a4-f61f-3b74-acb6-48d22ae1b6a5 | -7.82039 | -63.56045 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f35d18c-2d54-32eb-8bec-5d51d518e140 | -6.52063 | -44.42312 | 2025-08-23 04:51:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4cdbb11a-8650-3dfd-a517-b24d49130928 | -7.55071 | -63.8581 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27b1b0a3-09f2-3029-b231-c2f059493448 | -5.76274 | -57.59866 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 635083d4-d3db-3385-8e5c-58687bb4fdff | -4.30506 | -48.09715 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c191d3f8-2ee5-3d8e-a425-351757b2bfd7 | -7.03964 | -44.65808 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a137682f-56c2-331d-b642-d161f3728f99 | -9.22821 | -59.76515 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e93df8a-b98d-3334-80f1-a49c1cc64266 | -10.19122 | -46.84076 | 2025-08-23 04:51:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 725ca301-af53-3aa0-8fd3-dd6db688cc10 | -5.94571 | -44.13717 | 2025-08-23 04:51:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf5678c6-7900-3e4c-82cd-7aadf9fa9c6e | -5.83635 | -45.17365 | 2025-08-23 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| faca6e2d-8e3d-31e0-858e-1504a931ec39 | -6.94339 | -59.55497 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85e7a5ef-21b3-319f-a1d3-2d719eebfa25 | -6.87472 | -59.81616 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a0182ea6-f3d3-3948-b9ba-e41fd5f9a6f0 | -9.17008 | -59.70702 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1097c8bc-485a-3c3d-9c1e-376137964eaf | -6.72742 | -51.97519 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b01db1e-afa0-3d12-b54b-ac3ddd837182 | -5.83219 | -52.06819 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2cc0a4fb-2893-3cad-bc8f-7bdeced086a4 | -6.06054 | -53.88652 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b69635e-225e-3ed7-ba33-e94dbb0fa82b | -7.62329 | -63.48763 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23e87efc-81dd-360f-9c10-1044071d33c7 | -3.51929 | -47.20794 | 2025-08-23 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a6ac66a-7dbb-39fe-bea2-1d5882d422f6 | -6.25372 | -53.67519 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd302e68-1beb-3c1f-8a91-7c4c755b9bdb | -9.17206 | -59.59081 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| df7410cb-be59-3beb-9d5c-b88ba57d37e6 | -9.17539 | -59.70767 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 746c4999-58e1-3502-b5a4-7077a8db7738 | -8.44381 | -48.26131 | 2025-08-23 04:51:00 | NOAA-21 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e424ccda-261e-3f61-b639-6f88972eef59 | -9.18163 | -59.66549 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb35710c-61e2-3167-8dd4-376ffc7ec45e | -6.37225 | -45.54621 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| abc008a6-5665-3da0-bca5-97f7553c87b3 | -7.36397 | -57.63223 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5540ac70-31b5-31f0-bb62-bd51b7ba6480 | -9.18955 | -59.62797 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c7580b29-c256-3233-9483-68ab2468f01c | -7.95102 | -63.04619 | 2025-08-23 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a7d5ca18-3115-3549-81b2-515d12f6f682 | -6.2356 | -47.3153 | 2025-08-23 04:51:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 13d5c200-7934-33aa-b418-3c0459d8dde4 | -6.83362 | -59.88907 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1d37bc35-6d25-3a9d-bc17-389956e844fd | -7.81387 | -63.55996 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3fc1108-fb18-3271-964b-bd2d709d7fd9 | -8.01624 | -45.49373 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 11414ff8-a788-3358-aad2-c2b9a4598053 | -6.28231 | -52.82599 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41908e0d-b2a1-3074-a695-bfb9d56d686c | -5.75358 | -57.60431 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63111606-4c5f-3907-bf4a-c9e5a4e3fd0a | -9.18659 | -59.63627 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92920d61-2227-33b2-b491-49ae394fcaae | -5.23803 | -60.30397 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0d2f191-a809-33a2-a81d-aaf3f485355a | -9.20528 | -59.44817 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8085d49-e209-3be4-8d73-e6db3e9f0e77 | -7.63657 | -45.23284 | 2025-08-23 04:51:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bd7e9ffe-1a3a-385a-bcdf-2995d064b3ba | -5.88881 | -53.63878 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0d15147-d778-3da2-b950-d5739345604b | -6.3687 | -45.55349 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 07c7254d-6bf2-3bdd-a488-c2beb6e62737 | -6.11823 | -44.40649 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15324a28-dfd6-37d7-86f4-e05dc5dc801a | -5.73756 | -57.60172 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7b5ec1d-2eb3-3f8d-afac-fca2452f3f1f | -5.74849 | -57.58556 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8a217c94-0d3c-35de-a52e-ede1f501916b | -5.75817 | -57.60147 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f3c7fd7-3f3a-3aad-a089-434610ae1328 | -9.20389 | -59.4563 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a1228d6-df3d-3eb7-970a-29c9f4f456f9 | -5.8778 | -57.7592 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3ebbe1d6-bf9b-3ac8-a244-c471e7da9248 | -4.31837 | -48.24255 | 2025-08-23 04:51:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 056ad1d3-9743-30b0-a016-8c85f127ba3b | -7.03218 | -44.63941 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b0a44d7f-c1aa-39f1-92af-50376a1c6cfa | -9.21395 | -59.47495 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2965580-bc73-3ba3-ba88-3a65d5bb179e | -9.1852 | -59.62729 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 32b74f93-077f-3d8e-b6e5-8ad2a1c5e4b0 | -5.73656 | -59.88499 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 626c4890-5512-3e0f-8fe5-1ca7c3fd28e7 | -8.90048 | -47.33262 | 2025-08-23 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92d6e0bf-5edd-3b06-b589-5f9ca5e181af | -4.12477 | -48.11356 | 2025-08-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 120cbb01-59b2-3e78-bfe2-325e654901e0 | -8.62158 | -62.63908 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a076537d-6c9c-3c97-9030-64b50fbf0f46 | -6.30993 | -59.88783 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90d66705-a270-3ce1-b1d3-5cf9b89063b3 | -7.62904 | -63.48867 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f7b692a-3b78-3777-8c01-01e1ab1ca64c | -6.76802 | -44.32227 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad793b11-9717-3f49-a384-db8b35cf93c4 | -5.80092 | -59.22876 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 382a3d74-5cdf-3948-bf21-7885cb5607bb | -6.3695 | -45.56632 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0dbb52d9-99e9-3214-a80a-cdd1bd28e658 | -9.19823 | -59.46369 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5926df61-e15f-33ea-8d08-cd422e79e4ab | -9.18439 | -59.62298 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c863cc0-6504-3a31-830f-04c6dbd76044 | -5.74558 | -57.60297 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21bbbd1c-cfee-37c0-ab55-d02919a8988f | -9.1663 | -59.59847 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f651499-752d-323b-944e-d7c57707ad20 | -7.80957 | -63.55086 | 2025-08-23 04:51:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 74110910-b63a-32d1-a5f5-1734b98df5be | -9.18143 | -59.58809 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d7e3fd7-671d-3889-b333-a1c403f65e77 | -6.87847 | -59.8216 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0431ffd7-5e61-3ac0-b621-b7c3a2ded01a | -9.56166 | -48.50525 | 2025-08-23 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 619e6f32-cd43-3586-8d49-26c1b2e5bfc2 | -9.15332 | -59.59624 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
