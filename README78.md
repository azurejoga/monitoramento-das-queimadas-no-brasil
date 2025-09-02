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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bae495a0-ba7d-3ba7-aa3f-1da1029d7966 | -9.73557 | -48.97467 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6900d083-b3a0-3dc6-b7e0-5baec297346d | -8.67058 | -62.84803 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7ed51d8-3450-3c06-8f77-b3aa9d23a997 | -7.69532 | -50.2808 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2727ef93-b9c8-3796-a613-67c05d5a8daa | -7.70315 | -61.10051 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7057a560-fab0-3b58-b289-631cf2884760 | -11.64782 | -52.18573 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| fa623446-17ab-3ef4-bc31-29e5e5f48757 | -11.66813 | -52.17036 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f09f9587-96d6-3cdb-a050-a1112d4ac984 | -6.83364 | -59.67803 | 2025-09-02 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e9a4f7b8-f44b-3873-a024-e9b06f3f8d47 | -8.7273 | -62.40259 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c08ddba7-bb8a-3955-b4c2-ad5eabfa626a | -8.86206 | -64.23154 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fed5bca6-2e28-3518-9399-7d2463d11591 | -11.66264 | -52.16495 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1b1c850-7e67-3e0b-b4a8-189f6b46cb70 | -7.54509 | -61.33186 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 32c99fcf-5731-3525-9f5d-5662a8581fa7 | -7.53289 | -63.85365 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acf82819-ddcf-3707-981d-b82b13e2a56a | -7.47527 | -63.82184 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6d82322-8e8f-318e-a161-c01fc47259f3 | -6.82879 | -52.83885 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb8b2ec8-6237-3064-b85b-0eea89e205a9 | -7.45599 | -63.16058 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1c98ad0-f61c-3ff4-b043-e9bad5c9461d | -6.82863 | -52.83277 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09e28722-d76f-347f-9bcf-730c58684689 | -8.71454 | -50.44872 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1547e464-ebdc-316c-83b8-34601382b342 | -8.65451 | -62.92797 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87471673-54da-3026-bf0d-c7ce246d04ee | -7.67672 | -61.09272 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9605e49d-ad18-3eab-8885-33ed8f9fe1c5 | -11.66317 | -52.21066 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| acba50a5-bbcd-3ad1-b24b-ab77b20fabd0 | -6.34116 | -53.4407 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9eed5981-6efd-3690-ad3a-9fa1fd2769e6 | -8.65382 | -62.60912 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4d09470-abe9-375d-99cf-0f84ab3686e3 | -7.47468 | -63.82549 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a094cbec-22c9-372f-b113-98c05366209b | -11.65931 | -52.20681 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4246099f-905f-375b-a138-6356a771f909 | -7.59322 | -60.47915 | 2025-09-02 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2491f623-7509-35a2-a401-ea74ddb590b9 | -8.67741 | -62.39465 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 995dc2fa-f804-3bbb-b60e-f7a0c46860bc | -6.84339 | -52.81302 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cc89595-2324-35be-b53f-d44b10a6a63e | -8.70625 | -62.4064 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e419f326-f293-394b-b1f2-9f5eba2dc753 | -7.45321 | -63.15652 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7205c8c-68f8-3462-8211-050f21bc64c8 | -6.81929 | -52.8273 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b54a3bad-c78c-3f7a-89f2-605afd26bea7 | -7.37564 | -64.36956 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 478e9321-8f76-3303-b0b6-c3c8d7c935a8 | -7.549 | -61.32882 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 124f6843-2c5f-3ecd-8659-f46fc4d4c79d | -6.19432 | -53.76443 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 614cd92d-640c-3947-aaf6-e5198f191cfe | -11.66865 | -52.21599 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 063b13a6-4208-3d03-8451-796db55f3a9a | -11.66208 | -52.16957 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d213af4-de48-30be-903d-9c4c2f0acbbf | -7.69696 | -61.09586 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebaedb6f-043c-3e09-82eb-c3c33e3b2466 | -8.50951 | -63.90881 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e9a0cfb-a716-34ba-9b2d-29a0edcef3a4 | -7.54845 | -61.33237 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1cc02fc5-118d-3f99-b875-b60ae52709c7 | -8.63887 | -62.61747 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3e35d05d-6fb8-3920-85c9-a76988d61f4e | -6.8301 | -52.82252 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9c172ae9-027a-31f7-ad54-d03ab30c8055 | -7.56533 | -63.84716 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05eeacdd-189b-3394-ad43-e164b1e9185c | -7.44186 | -64.51649 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 999b97a4-e3af-33d7-80d8-65deb29d6793 | -7.47748 | -63.82968 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bb97f11-747d-3a9b-9fff-795e551ed020 | -6.81837 | -52.83418 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 48ba20e9-4e36-37f1-b14d-07f84adf7f1d | -11.68071 | -52.21754 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 263764f5-1611-3ee0-aef8-62d7aa465485 | -6.43016 | -55.62066 | 2025-09-02 05:31:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52536072-2d7c-3064-a9b3-03e91ffd203a | -7.55913 | -63.84242 | 2025-09-02 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 371c1df5-8db9-3db7-abcb-a0abdc92e597 | -6.33519 | -58.17616 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 78e225ad-56fb-32ae-8912-ba5b665fad49 | -11.67636 | -52.21833 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 33f1a31d-7bc5-340f-b24c-91b8068abed4 | -11.67523 | -52.21235 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| ddaab7fc-8594-3265-81cd-933e268fa825 | -8.55625 | -63.00907 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 303d9d0b-800b-3648-8123-25f3af9d48d6 | -6.34204 | -58.18185 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e37ff1ef-5f19-3067-8c88-ab6d84f0a819 | -7.28606 | -60.6623 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 785764d2-272b-39a7-8e94-7010682f74de | -8.76095 | -61.43209 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b57de901-1597-35e1-bc2e-5aeb8fc5653f | -7.59645 | -61.63254 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7abfe222-e8ef-3053-a405-dd325e64d120 | -11.94051 | -50.61018 | 2025-09-02 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2768a7c9-9f71-3b23-bdd1-248e3094f751 | -11.67241 | -52.19962 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 43841b6b-5b1b-3606-b5d0-e923ce3bcfa0 | -11.67252 | -52.1846 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| bdd9f9df-1c4d-3751-ab9d-0eff179dcb91 | -11.68127 | -52.21304 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7183a32e-257d-31d0-bfc8-8c2f47f06fca | -6.33965 | -58.1722 | 2025-09-02 05:31:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6c6e1306-df62-3415-8027-3b14713be8bf | -6.8098 | -52.81559 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 422de965-cc49-3d38-9f7d-9d767ff57612 | -11.66794 | -52.18529 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b46fb908-1f5d-3baa-9bd5-ed53e35522c2 | -7.0922 | -63.13544 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0902e400-d3e2-3cf8-a71d-b4f4cf541819 | -8.67631 | -62.40164 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fae25022-1508-3e6a-b49d-b836751dec6e | -6.92647 | -63.13053 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8ae8124b-93ce-38eb-9579-b5b76c62ff73 | -9.741 | -48.96288 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c519c0e1-8323-3b1e-a002-612b8fbc92a4 | -8.97495 | -65.96521 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| daf7be04-e72a-3b63-bb29-20d107f20582 | -11.6533 | -52.1911 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| fb02df92-cc74-311a-b5d8-3a480b4f2e2a | -11.85152 | -51.4794 | 2025-09-02 05:31:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f20a0f75-a8a0-3607-a7d9-3131134bab1d | -6.8227 | -52.83551 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce82a5c7-b56a-315c-b0ca-6baa92465d23 | -6.48033 | -56.01053 | 2025-09-02 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c229c786-35e5-3f94-9c0d-0b7a1621db3b | -9.16584 | -58.89762 | 2025-09-02 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 565fcba0-b352-357b-82fd-b1931dadf02a | -8.72088 | -50.44917 | 2025-09-02 05:31:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5b2472e-a5a4-3ee6-b9ac-0fdab909ec8e | -7.70326 | -50.27081 | 2025-09-02 05:31:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 22cf04a7-6183-3b6a-986d-f4822165bf72 | -10.76116 | -59.84283 | 2025-09-02 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9b70988-44b1-32b4-851d-371fad9fa76c | -11.66152 | -52.17411 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9fd4deaf-b67b-3643-bc2f-0c8f9faa7654 | -9.51096 | -63.5639 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a64610b-3b96-3fa3-9355-11d41a7f28cd | -8.9713 | -65.96459 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62e1c613-40a8-3e14-ae08-92efddec04d8 | -8.9655 | -65.97678 | 2025-09-02 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 9472800e-947b-3807-9a24-8a21800da235 | -9.32854 | -59.57033 | 2025-09-02 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8a2f333-2efd-3b41-9a6f-6b830f4fc484 | -11.65221 | -52.20005 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 938103d0-4551-334d-8c2a-a4fedb548002 | -8.76206 | -61.42493 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f90ef85e-4355-3b76-ae0d-a27c114f2cdf | -9.64203 | -63.11871 | 2025-09-02 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f5c0dbe-561c-3fc5-8756-b447e5650824 | -7.60307 | -61.61199 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83c00332-81ea-30fd-8392-3cc1844c3a46 | -9.73045 | -48.98977 | 2025-09-02 05:31:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 3839e22e-43f4-365d-899c-463b14703871 | -8.75716 | -62.42516 | 2025-09-02 05:31:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20a649aa-125c-3580-9984-333dad1e9f9d | -8.31027 | -55.1014 | 2025-09-02 05:31:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9640c5fe-c5a8-37fc-b899-ce106c527013 | -8.64385 | -62.60753 | 2025-09-02 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e982e7fc-b37f-3034-8ed5-ea67618029ef | -7.4493 | -63.15952 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c1b9b34-8505-388d-9cf0-a52c790d1cca | -7.6964 | -61.09946 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0cebc6c3-a1c9-3d17-b7eb-bc840fffb9b2 | -7.08765 | -63.18554 | 2025-09-02 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5e4e47d-dd2a-3117-961e-843fe2fa87f0 | -11.65987 | -52.18759 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 27cb0098-86c3-35cd-ba31-363c12d925c3 | -11.64837 | -52.18122 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 716acaa9-2ad9-3ffd-9c44-472a7d4f9f64 | -11.64727 | -52.19025 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d2179ccc-d452-3a32-8c82-51c10d8c33a5 | -11.65329 | -52.20592 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 1295b34a-929d-30f9-98a8-8d4e1cbbc5ac | -8.66559 | -62.83652 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4673944-33ee-3d34-a9d8-fbb21aff58f6 | -6.82611 | -52.81161 | 2025-09-02 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65f77f45-42c8-3af9-9e20-0dad083c46f9 | -8.67169 | -62.84105 | 2025-09-02 05:31:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e5e3631-1e2c-312b-aafb-14d18f8a0611 | -7.60083 | -61.60444 | 2025-09-02 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b84ce82-cf49-3c81-92d3-d0e053e76fa2 | -8.30146 | -61.42743 | 2025-09-02 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
