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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 698e53fe-1611-3ac4-807b-c0589fa6bdc0 | -6.37499 | -43.87363 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 336fa6a7-6bd8-39d6-95f7-45b3eef88495 | -6.66168 | -43.86061 | 2025-10-03 04:10:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a1bc9bc-c0a0-3629-832e-bebfe366b207 | -6.55954 | -43.89487 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7feebf9e-07be-3ba0-abc1-2cb8e3e2cc6e | -5.89299 | -44.2604 | 2025-10-03 04:10:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| df3a33a1-9941-342e-b6d4-274c0f537afb | -7.75978 | -46.64806 | 2025-10-03 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b5f4e80-1c51-3f4c-9412-30b824511f6f | -6.09114 | -43.2578 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f5041d2-9910-35f9-8cd0-29871ea70088 | -7.7576 | -42.58725 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4e454b49-7e2c-3f74-9d9a-8a270a93b1c3 | -7.74814 | -42.58212 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 46423085-beee-3d09-8a7d-1cd3da9e811c | -7.49955 | -48.85344 | 2025-10-03 04:10:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3cbfdbba-c8e4-3c4f-be6c-6fc066aba76b | -6.68553 | -43.71213 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73e49f3b-26bf-3f2f-88b7-37604ce5b7ef | -7.7922 | -42.54232 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b49e62a2-26e0-3994-bc11-929abdaf5032 | -7.78572 | -47.37585 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12858c14-2df6-35ba-ba53-a274102c9255 | -7.76327 | -42.53048 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c8ec2369-53e7-3d49-af64-278c0e6d85a5 | -1.08479 | -53.68595 | 2025-10-03 04:10:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dcef88c5-083b-3131-920d-1b575edc84c3 | -5.77791 | -45.76038 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60564d78-b532-3761-8052-6c79d91c5f30 | -5.30361 | -43.76011 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9b8a578b-59fb-3864-b3f5-90e07f30eafa | -2.62857 | -46.83835 | 2025-10-03 04:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90aad3f1-9be9-33cb-8bd1-56ce50298512 | -6.2375 | -44.23085 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e64488d1-d887-331c-a644-e635c5c5cbd4 | -8.05002 | -43.97765 | 2025-10-03 04:10:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5a4c19a-8162-30b4-a574-ae6f87a4d509 | -5.62433 | -43.91818 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e93e29a-9190-31a9-8d55-fd156cbaa2fd | -4.57572 | -46.5008 | 2025-10-03 04:10:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 66efed0b-79ec-34a5-a41d-d098f8e5892b | -8.04371 | -44.11236 | 2025-10-03 04:10:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c30382f-3c13-31ee-9131-3ccb315fe4aa | -5.63328 | -43.90764 | 2025-10-03 04:10:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6103d808-ede1-3742-962b-d5869a45b2a8 | -7.79946 | -42.51828 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3fd426e2-082c-36bd-af44-f49dc071d5f8 | -6.86523 | -39.28143 | 2025-10-03 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee6d5dce-8529-3481-93cd-943733271f44 | -5.09086 | -40.2381 | 2025-10-03 04:10:00 | NPP-375D | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2940e294-e0fb-3b7b-8950-b43f51d13fad | -7.25067 | -49.41199 | 2025-10-03 04:10:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78612ca0-eb1d-31dc-810c-646fe9690ecd | -6.73909 | -44.58573 | 2025-10-03 04:10:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c9d67101-4063-38a6-a014-153a4e917fe2 | -6.65667 | -42.78526 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 59a00e72-3b2f-3736-867b-1d0ca2fd6cd3 | -4.65976 | -45.79125 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e37b8391-d15c-3626-a223-c9e5d639599e | -6.27706 | -44.05441 | 2025-10-03 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 00cf22f9-9810-369e-8e7c-a94b041fb7ae | -6.35621 | -44.76079 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d204512c-d82b-3601-8893-f6d3df6deecd | -5.40248 | -41.3375 | 2025-10-03 04:10:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6ef18f9e-d5a3-3e2d-b60e-600f12d5b0f7 | -7.29832 | -44.1888 | 2025-10-03 04:10:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e29e5e67-bce3-3012-97a6-14dae8adeac2 | -7.76485 | -42.5848 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 22a49fa7-4d25-32f1-a1df-04b5bbcf4709 | -5.90602 | -39.15258 | 2025-10-03 04:10:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 922b3bf5-ff67-3c3a-9b93-e23440f6906c | -6.32865 | -43.89093 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a0866123-77bb-3bb5-90a2-469b1b04423e | -4.87578 | -45.62365 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1555dee-f63d-3401-b174-40539ae1f2ff | -5.94645 | -43.31093 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d2e72e45-08d8-396e-b0d3-92f154d341c4 | -6.40868 | -43.93115 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0be6307d-3bd8-331b-8b29-01ab826b9f2f | -6.64993 | -42.7842 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 757ac63f-0885-32d3-ae97-1a901fa971b5 | -7.44519 | -46.98249 | 2025-10-03 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48adb040-9d13-318d-8368-55236488cbf1 | -9.42557 | -40.71805 | 2025-10-03 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 64639e4a-7a16-392e-be61-cd8ba6fb1eee | -5.24733 | -43.09864 | 2025-10-03 04:10:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8787ce0-37c7-37df-bae5-b269aed2c69a | -7.47784 | -43.04464 | 2025-10-03 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b3ba54f-dfc3-337b-af66-840f7ea53172 | -4.65644 | -45.81124 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f1e63e8-3222-38da-85f0-225270be2e67 | -6.22487 | -44.24123 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c9855788-b16d-3bc7-b9b7-7e69ef5c5d6f | -5.94302 | -43.31038 | 2025-10-03 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| cff8fb33-eed7-37b6-baf2-8603ea246c43 | -6.7077 | -42.81174 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 68aedc3e-4ed9-341e-800d-1ee032347df3 | -7.54484 | -47.19638 | 2025-10-03 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03c29f00-2adc-3215-8bf1-6ac06e698e01 | -7.19675 | -45.38235 | 2025-10-03 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e340078-1f36-3250-97aa-0d4ece9e9379 | -7.26451 | -48.48033 | 2025-10-03 04:10:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2962457-de6a-3d83-acb4-703528054365 | -6.64878 | -42.79134 | 2025-10-03 04:10:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| d97fe28b-4092-3241-bc2b-79c6c7f61420 | -7.74556 | -42.58467 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a883f2cf-920a-38bf-8625-5533bce25efd | -7.87703 | -47.32483 | 2025-10-03 04:10:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02b3357f-facd-3c86-9cec-7c046b89b116 | -7.30681 | -45.2694 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59637dbe-71d3-3b7f-9063-4a59f28828bb | -6.38069 | -43.88262 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88c42b62-0a08-32fb-910c-047ed019a219 | -7.77275 | -42.51402 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d1d910a2-2e33-3419-96d7-a847e92c338e | -0.90605 | -47.54498 | 2025-10-03 04:10:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c18c47e-307e-3725-8ac6-6178b87c6ba9 | -8.17894 | -47.01884 | 2025-10-03 04:10:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07c67bc5-1ac2-372e-b0ea-3875d89e80ff | -6.23954 | -45.3504 | 2025-10-03 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0aaf53e-8ad9-3b88-bfa0-6762c2559b33 | -4.95562 | -45.77316 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4398d52d-df70-33e2-9f7c-e94f47250482 | -5.8276 | -46.36242 | 2025-10-03 04:10:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dea3cc5a-1cd6-37c3-92b4-ef4080d95163 | -6.23197 | -44.24244 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5ba009d-42d1-34fd-8454-6ae1b2e201fa | -5.05421 | -40.95213 | 2025-10-03 04:10:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7e8cab9c-9471-301c-b9f4-0bf3b1777da6 | -2.25387 | -47.88208 | 2025-10-03 04:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d41d647e-d5d4-311e-93ed-e9a6f4a42489 | -7.76315 | -42.59537 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d2ca4241-7af2-38a6-887a-e8945e407112 | -7.73059 | -46.2296 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b04f82a-e233-3c65-b6e4-1bf96884342d | -7.77219 | -42.51752 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cd17662c-4596-311a-aaf1-cfc932721007 | -6.41264 | -43.84031 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9477bfa8-2219-359f-b10e-856b259512b6 | -7.23798 | -42.98851 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5cf004b8-2ae7-3ce9-8b9b-881bfa5dc9c3 | -7.76814 | -42.60704 | 2025-10-03 04:10:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0ec659a3-fe65-3e18-acda-9da0cadc28ac | -7.75217 | -46.2674 | 2025-10-03 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 974db473-34dc-323e-9a3f-5d7c2f37e032 | -3.8431 | -41.57142 | 2025-10-03 04:10:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| de152f1b-3ffc-3de1-a6d1-f1e125d7aae9 | -6.4163 | -43.92841 | 2025-10-03 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| acbd8200-8c55-3dbe-8c44-179e10744461 | -7.75096 | -42.56454 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| da1c20ae-8102-30d1-87d0-53f12cae39d0 | -7.76706 | -42.59239 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9891b81c-bab4-37bb-b7ac-abbf1e24e39e | -7.31775 | -42.88729 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 16f53c24-97a9-36d0-9665-fddc4237e616 | -7.91184 | -43.53474 | 2025-10-03 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83930191-d62f-3972-a836-db56673e9cb6 | -4.93519 | -43.73998 | 2025-10-03 04:10:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6c9fc86f-c2a9-3989-a11c-6c078c1cc42b | -5.34286 | -43.7624 | 2025-10-03 04:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7433c0f-b9c4-37e6-91d3-349e16ae3e00 | -6.72025 | -45.97102 | 2025-10-03 04:10:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f714a71c-f7e2-3353-b023-30588882cec7 | -6.37904 | -44.64454 | 2025-10-03 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37d741b2-1f9c-3248-b405-91a6f8662ee3 | -5.90778 | -43.9056 | 2025-10-03 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 25df8def-6582-3763-8e98-97c9e6cdbcec | -6.55534 | -43.89442 | 2025-10-03 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| efcf8c14-0f8c-398e-a798-47fe6f9fc74b | -7.75821 | -42.5621 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fd3a74c3-2663-3b96-93f6-0ae570c4db2c | -5.61695 | -51.94186 | 2025-10-03 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44d9d513-cfe7-3482-be9e-6aca99819ae1 | -5.17729 | -45.42122 | 2025-10-03 04:10:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac5b73ff-aaa6-326a-9b36-3da2f95b669f | -7.77878 | -42.58343 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 88f2a248-ab0b-3db9-9d11-73bb7a340e64 | -7.44926 | -46.98323 | 2025-10-03 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2addbc8f-03b6-32ff-be0f-df858a6ddc8d | -4.27409 | -42.0052 | 2025-10-03 04:10:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8669bae-2bd4-3750-b43f-063674873308 | -2.922 | -48.31114 | 2025-10-03 04:10:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 41d5400e-508a-30d5-bf9d-49833edb1a34 | -6.86874 | -39.28184 | 2025-10-03 04:10:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d69acdb0-2c8f-32d3-a7ae-61c67e8e0950 | -7.31833 | -42.88372 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 56c3fa39-a47a-39fb-ba81-84af80172572 | -7.77544 | -42.58289 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 353d835a-dd88-3acf-ba66-0c4fefcdcf72 | -7.0584 | -43.30519 | 2025-10-03 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a50028dc-9353-334b-bf19-bcc793fce752 | -7.28607 | -45.25712 | 2025-10-03 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1fd3fbdb-2665-3ebe-b854-d5b889860dd4 | -4.67082 | -45.79791 | 2025-10-03 04:10:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9fb0fa0e-687b-3e14-b2a8-5a85cfe03db9 | -5.16823 | -46.05658 | 2025-10-03 04:10:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b130db0d-5f24-35be-8f15-b95ece2361c1 | -7.78549 | -42.56285 | 2025-10-03 04:10:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |


[Clique aqui para ver as próximas entradas](README51.md)
