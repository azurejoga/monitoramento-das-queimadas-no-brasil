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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 55adc8e6-e3ea-3ecd-9a53-223b70682981 | -13.23583 | -44.48782 | 2026-05-02 04:27:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 716b64b7-6abd-32a6-bc36-ae3e091d9aff | -12.39276 | -50.0275 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e146d74-4881-3446-8064-e25a9b74c205 | -10.98886 | -45.08312 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| c09adf9b-07b7-3e49-b2e1-4541a42fc0de | -9.6775 | -43.78918 | 2026-05-02 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b6762a7a-186d-35b5-b95e-bd117af0a272 | -12.37333 | -50.0364 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 4294e99c-b4c0-3f15-b0e8-000ef41af648 | -10.96755 | -45.08844 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 169ba67a-99d5-31dc-a2eb-e4abf3bcbb9e | -10.55967 | -44.33434 | 2026-05-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dfffbc01-aa9e-307d-8b90-76a0e0fcdb2b | -10.70736 | -46.34795 | 2026-05-02 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ad616bd6-8604-3bc4-bef9-69c63f46080f | -13.68514 | -44.29039 | 2026-05-02 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b877129-5f62-3f57-9c5e-c6e54d922542 | -13.78314 | -44.10116 | 2026-05-02 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e39601cb-5c37-3134-91ad-50cc316ac5fb | -10.98485 | -45.0864 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 72bb1fee-d705-3b46-83bf-e85465fce3c5 | -11.43602 | -55.10094 | 2026-05-02 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 02b32a04-08e4-3f45-8e51-ff743bfcbeea | -13.81547 | -43.64852 | 2026-05-02 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e100cd7c-4e1c-3975-845b-d6cc489cb66d | -10.98254 | -45.0782 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8b68fffb-52c0-364c-87c5-12c28d5f231d | -12.38097 | -50.03363 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ecdb29c5-d46f-32a5-b4a6-e17b632e5d67 | -12.37748 | -50.03304 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 49952e07-a640-3e9e-88dc-09b58e8250e5 | -10.97685 | -45.09294 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 79f9e07b-0e5b-3a5f-abba-897f59d651c7 | -9.76889 | -51.72251 | 2026-05-02 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76b658c7-eb07-358e-9c37-4c2cc7541885 | -10.13448 | -42.07067 | 2026-05-02 04:27:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb302dc5-b8a1-31a6-9461-ba39fc895e1b | -10.98085 | -45.08967 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fe773a47-945a-32a9-9098-9339baf92768 | -9.67689 | -43.79337 | 2026-05-02 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57d01318-8a57-361c-a59b-0dd9c25e6845 | -11.43985 | -55.10711 | 2026-05-02 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 61d7238a-3e31-392a-b064-9b2a62f261d2 | -12.37549 | -50.04489 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| dc73213f-1980-3ee3-b842-c9a20d7ed2c9 | -10.97798 | -45.08531 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcc173e4-292f-3bba-9067-5dadaaaffaeb | -10.9791 | -45.07766 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| aa38bf09-523c-3a16-932a-a12447ce1c09 | -12.37616 | -50.04094 | 2026-05-02 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 382f15d8-2e97-3a6e-b6ef-802e66a46a9f | -10.55909 | -44.33837 | 2026-05-02 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1070dd31-8015-3f33-bd7b-198ed5bc17ec | -10.99343 | -45.07601 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e15a8eeb-c147-3906-9fed-4684b1707c2c | -12.92568 | -42.43032 | 2026-05-02 04:27:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2bd97fe3-bec1-34aa-a19e-bedc4d4045de | -13.68525 | -44.29271 | 2026-05-02 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f254e53c-351a-3f72-a06a-c7d1d4d0f3d8 | -10.98999 | -45.07545 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a8d5be8-7ad1-3164-b134-edbd3f2f20fe | -10.97622 | -45.07329 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51885df7-894b-307e-995c-30ef39f28e75 | -10.93202 | -45.09072 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56f9c8c4-06d8-3052-8193-5bf46ed0ddd1 | -10.98542 | -45.08257 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d1f063a0-8d88-3c80-8ddf-9ad22c1f69c1 | -10.97054 | -45.08802 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5d577660-affd-33db-805f-6577d67f53be | -10.98373 | -45.09402 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 58a3a3f8-ff24-31e8-a890-d93c1f7dfd87 | -13.81101 | -43.65274 | 2026-05-02 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 269e5075-859e-3829-bea1-f4bcabaff106 | -11.44562 | -55.10269 | 2026-05-02 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 440f8a9a-97d9-3969-aa3a-e553aa900e34 | -10.98141 | -45.08585 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39c9bb5b-bd66-3afe-81c2-fab1cc0f75da | -11.06345 | -49.50187 | 2026-05-02 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8e8a59e-f4dc-3afe-a1df-eb2d446a61a3 | -11.55354 | -48.26777 | 2026-05-02 04:27:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb2737cd-b4e9-3d05-9737-fae0a82f4be5 | -13.81166 | -43.64796 | 2026-05-02 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c542cc19-eb32-34f7-ab95-1bdf7b1b2464 | -10.96998 | -45.09184 | 2026-05-02 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bc961005-b37e-3b11-b52c-a7b6120e6b6e | -14.38604 | -47.92628 | 2026-05-02 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc131cf8-1d6a-36b9-8d86-2577f9fc8431 | -17.52426 | -45.45667 | 2026-05-02 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09c2af46-4ca4-3498-b4f5-139fac578d78 | -12.29395 | -57.39517 | 2026-05-02 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e3531b7-9324-35cd-a007-7eef4e548880 | -18.16887 | -51.1107 | 2026-05-02 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6e8cbb2-6bc5-3e6b-b119-e451acc9eaa5 | -18.12412 | -49.75559 | 2026-05-02 04:29:00 | NOAA-21 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| b8ce1806-190c-3a57-8123-89f2b078fed2 | -19.77061 | -48.00832 | 2026-05-02 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 843fd98a-3a41-356a-a77f-39b19d6f2796 | -13.99212 | -56.63736 | 2026-05-02 04:29:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f436d970-0d54-3526-bd70-c16064859d8b | -18.48252 | -48.40346 | 2026-05-02 04:29:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efd322dc-c8c5-3d89-bbb4-a32f5dcd23fe | -17.52682 | -45.45492 | 2026-05-02 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ec658d3-37a1-3f8b-9c2e-27da360bc6ca | -15.38304 | -48.95847 | 2026-05-02 04:29:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c680f84a-d5ed-3827-838e-f1eb6cc247af | -13.99331 | -56.63115 | 2026-05-02 04:29:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17d342a2-e48c-3e4d-90c2-06a6c62b8e7d | -14.67356 | -52.35042 | 2026-05-02 04:29:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91d3a896-3ff2-3504-8e18-cec1851834f3 | -12.28847 | -57.39409 | 2026-05-02 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f577eb6-4424-3e0e-b04b-85e6b51efcf8 | -14.38549 | -47.92982 | 2026-05-02 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1fbd37d-e1e7-35f6-89eb-7761d34b8413 | -18.49326 | -51.69081 | 2026-05-02 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e61068d8-4755-3890-b669-498d952a945f | -14.30545 | -49.24998 | 2026-05-02 04:29:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1a0c1ff-42ba-3d7c-92e5-deca7d27c06c | -13.99897 | -56.62906 | 2026-05-02 04:29:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b87f63b-ba8a-3d83-8307-c2f3774145b0 | -17.91483 | -52.90026 | 2026-05-02 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d25c778c-b3f2-35bf-ae95-f15a99aa6a41 | -15.58319 | -46.807 | 2026-05-02 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5874f1e6-e741-376a-a7bf-cdc16e2eb9c8 | -12.29322 | -57.39893 | 2026-05-02 04:29:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 010d7015-ec0e-3aca-be76-99eb9d0f97b9 | -15.00391 | -51.93147 | 2026-05-02 04:29:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55e75a15-85a9-3ba4-b728-f8b744447520 | -18.32352 | -54.52803 | 2026-05-02 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4aa5c0a6-ecce-381f-addd-70194a26a229 | -13.9966 | -56.64145 | 2026-05-02 04:29:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9fddc35f-a108-3263-b129-31e53270507b | -18.49747 | -51.68735 | 2026-05-02 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 622f954b-cf71-3ef0-9476-1af814a93b10 | -14.20729 | -57.4268 | 2026-05-02 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a7b8950-c5b7-37a0-bd36-aa914611da28 | -14.20662 | -57.43017 | 2026-05-02 04:29:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dce6674b-b007-3466-9f54-58a6ea9f4319 | -17.93148 | -52.89364 | 2026-05-02 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 652edd59-9b0f-345b-a0f8-331b8b1579e5 | -17.00559 | -48.28481 | 2026-05-02 04:29:00 | NOAA-21 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db12ffbe-1674-35cf-8b25-11b16b535224 | -14.38219 | -47.92928 | 2026-05-02 04:29:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e780bec5-dc62-3a76-afcb-2617967e498e | -18.48975 | -51.6902 | 2026-05-02 04:29:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88757380-653a-38bd-9026-da4f587c5295 | -17.93524 | -52.89427 | 2026-05-02 04:29:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3acdb66b-9c95-3f0d-99bb-32f64a514e37 | -13.99778 | -56.63529 | 2026-05-02 04:29:00 | NOAA-21 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7f66cd5-d487-3c05-a197-c8c0e45ec177 | -14.30209 | -49.24944 | 2026-05-02 04:29:00 | NOAA-21 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfaae0aa-9df7-3e78-afb9-9e1c807542a7 | -18.49677 | -51.69143 | 2026-05-02 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9160ec0-0f80-3598-b833-3f3e85369567 | -20.1759 | -43.58902 | 2026-05-02 04:29:00 | NOAA-21 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9eba1bc9-a051-3030-848b-5f4d8f8acd24 | -18.31306 | -54.65456 | 2026-05-02 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96f5165e-54e0-3f9d-925d-e8b05351085b | -18.48273 | -51.6889 | 2026-05-02 04:29:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| addc92c3-b3d6-32f2-99af-f8f6d84de3f2 | -15.34031 | -47.356 | 2026-05-02 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d1f1c68-5aa2-3c36-af10-e7d02bea3861 | -18.58274 | -44.48872 | 2026-05-02 04:29:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22497790-b503-3bcc-bdd3-c6132f90053e | -15.586 | -46.81128 | 2026-05-02 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97ac7711-9338-33d7-bf09-03ce0f8ade5f | -15.58263 | -46.81073 | 2026-05-02 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 908bbd64-14d6-38a2-be5a-39e6fa83cacf | -20.27761 | -41.28542 | 2026-05-02 04:29:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4426cb6-d159-3fb0-8e6b-f4779107c1a9 | -15.58656 | -46.80754 | 2026-05-02 04:29:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdf3565c-21cd-362a-80c8-af34b90e253a | -12.3887 | -50.0435 | 2026-05-02 04:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| d56d7203-98ae-3639-8e9d-439d7e59c293 | -12.3696 | -50.0459 | 2026-05-02 04:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7266d0b1-183a-3816-9f0e-79c0e9c6dc73 | -12.3891 | -50.0218 | 2026-05-02 04:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 96b648eb-927e-3106-87d9-9b6b4441a969 | -12.37 | -50.0242 | 2026-05-02 04:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| ed424ca6-5289-31eb-b9a8-288a89a23f72 | -10.9815 | -45.0874 | 2026-05-02 04:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| bb4cb69c-a00a-3d1f-ba51-1051d3a073d0 | -20.28256 | -46.44135 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb9a11f5-5a5d-391f-a79f-2c8718470ce1 | -20.2009 | -46.45553 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b138e52-5f6e-3775-979e-ddb936e66990 | -20.44448 | -53.77489 | 2026-05-02 04:32:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ab677b0-29f3-3d22-99c5-fee0a4ba4d66 | -21.23738 | -44.01297 | 2026-05-02 04:32:00 | NOAA-21 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 81afe2cb-4199-3966-ba57-3d309d7bc51e | -21.151 | -48.47238 | 2026-05-02 04:32:00 | NOAA-21 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 708954c0-5a15-3147-893c-fd4e8cf222cc | -20.44434 | -53.77229 | 2026-05-02 04:32:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0526da84-2162-34e9-b517-6a640273e921 | -20.19871 | -46.44765 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb471657-74ff-3cbd-846d-c26cbf2bcf39 | -20.28195 | -46.44568 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de2ed338-272b-3597-be0e-2b2f0d2c3d36 | -20.1981 | -46.45193 | 2026-05-02 04:32:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
