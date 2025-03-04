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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d74616cd-457d-3f5e-8ddb-5be62d266c3e | 2.26798 | -60.25607 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 631164a7-2bad-3b6d-a0a9-ea91a1083c33 | 1.13257 | -60.50889 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2daf710f-bf7c-39dd-b040-ac3dbd68eec8 | 2.27455 | -60.2508 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01051102-0876-36fb-9d72-4412f86c0004 | 1.93962 | -60.39698 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0917f26c-18b3-3123-940f-7488207f2e2c | 2.35018 | -61.06586 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 858ad51b-d9d0-31c5-8520-56ac7a9e897c | 2.34895 | -61.05816 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d7f3296f-a010-3add-ad12-7fd443c812ee | 1.93666 | -60.40154 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c62552b-40c8-39eb-9936-47acfc524279 | 1.12599 | -60.51417 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 720e4d0c-278d-3ff6-a7b9-4f6d2c5b602e | 2.36287 | -61.056 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c8a6dc5-03d0-3777-a990-c7d3364a4cc9 | 1.63677 | -60.22689 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da1d671b-ce8a-37d9-b12b-059aedff6b94 | 1.63312 | -60.22747 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 335bca8b-817e-3b92-8661-9aaf7e4753fa | 2.35877 | -61.05267 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8f89cd90-ade6-3624-8d06-3ee6d412548b | 2.33787 | -61.05587 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c4001575-b793-35f9-8c53-39eb567144af | 2.35691 | -61.04111 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 787ce284-0e3f-3681-9a98-36281436148d | 1.12172 | -60.51059 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba6abcd6-6b80-3345-a39b-a6530955c994 | 1.13026 | -60.51774 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| ddfb9640-e451-3d2e-800b-3091add485e5 | 3.41524 | -60.73111 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 115aa7ff-34c6-30a8-b543-9dae72678ab5 | 0.8612 | -60.25402 | 2025-03-04 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ee77e1c-e82c-351c-9eee-50d6d44e58d8 | 1.08469 | -60.67222 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60d181c7-fd8b-3173-96de-b6c0dc650ce4 | 1.93827 | -60.38854 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81483b0a-3187-3234-b02f-bacde7c26930 | 2.34136 | -61.05537 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a71f2dc4-aaec-3514-bf94-71ff25b444f2 | 1.85674 | -60.29794 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53a37687-d9a7-3a68-ac86-b8382a8c2b39 | 1.13554 | -60.50418 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71a8275f-460a-3afb-beb3-b71b9d90d3a0 | 2.41814 | -61.20213 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51890f1c-4d06-38f7-a8ff-4f3e0d79dc74 | 1.08535 | -60.6763 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c30b24c4-d57a-3c84-9006-a5ee2f8a76a0 | 3.53866 | -60.10376 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ff45cfa-02a2-3043-b919-90bab75a9466 | 1.28084 | -60.07554 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 752ee624-2098-3b01-b9f7-5f90fa48ab2e | 2.34259 | -61.063 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3fbd81c8-d03e-3ddc-b5d1-fa53996d487e | 1.13322 | -60.51304 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d7913a7f-4c67-3a9e-9bd9-e5b2358733a8 | 3.4175 | -60.72283 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b1a4d45b-070e-3cec-ad97-cc97b0506471 | 2.35304 | -61.06147 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0692894-df36-30b2-8b2a-c5b3ca1f14ba | 2.42159 | -61.20158 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c20ab534-f7c8-3d3f-8f8c-cedf232e9fd8 | 1.96689 | -60.61328 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38203758-a326-380f-b727-6939aecec409 | 1.08894 | -60.67574 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d590aa8e-7d14-3ceb-acc2-a9db821041d2 | 2.2716 | -60.25553 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cd4002bc-74ae-3918-9dae-348b6454d9a4 | 1.12896 | -60.50946 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 70e93596-47e2-34ba-a160-57a04a76f232 | 1.84585 | -60.53156 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99eb09a7-8738-35ec-a219-b88099ba3534 | 2.33848 | -61.05962 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| af3e9889-3ca4-388e-a307-8e573fed9910 | 3.54225 | -60.10318 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de4aad1e-e407-367d-9148-0721dc34e3cd | 4.05326 | -60.00758 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0ec7e33-3dd1-348f-962d-f21070b188da | 1.28453 | -60.07497 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ca54f8a-c15f-3a00-a884-f0a8401b1e16 | 2.34547 | -61.05871 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c9d7f27f-b427-3841-8f1a-8ca5768f1070 | 1.12664 | -60.51831 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| c14741bb-e33b-3378-96ad-b69f258dac40 | 2.0009 | -61.14442 | 2025-03-04 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 509d5f06-9876-35b1-83d3-074ed66d4bbb | 2.74781 | -60.73212 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae0323c0-9bfb-3963-b282-20793e19453f | 1.88765 | -60.86066 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08359a2c-7782-3888-aa6e-b95d9d5da07f | 3.54518 | -60.09851 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c47b3c5-8cdd-3176-bf67-c115063b53bc | 2.36163 | -61.0483 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c05fcfb6-9b79-345e-b70f-62a82836e304 | 1.13684 | -60.51248 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 069ef4b1-d0f2-3591-a9fd-210b79f9373c | 1.12961 | -60.5136 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 56a9ce9d-7eb3-3215-bf52-f0d1c04567e9 | 3.69847 | -60.62888 | 2025-03-04 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4664e2fc-9d24-3a7e-a8c7-145f71171519 | 2.28227 | -61.23108 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5a05844-622b-3110-bedc-7e5be8f714c2 | 1.93528 | -60.34669 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 773896a5-bc40-3591-b430-43e44ab9668c | 2.35715 | -61.06481 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b2f9f497-f7f7-30cd-b853-24692b9dbaf6 | 1.00948 | -60.57725 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 305c7d40-9925-3507-9bda-bb60a34af0b1 | 2.34957 | -61.06203 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b36637b0-4ac5-37d1-9676-e47d00cf18d3 | 3.41812 | -60.72668 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b606723f-90f3-383f-a9b5-ec0db9a5c8bd | 1.93895 | -60.39278 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f8bad25-d8d3-3d5e-bab7-427bd150eacf | 1.0811 | -60.67278 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2b52e302-a657-347f-9dbf-94cf21af6d3f | 1.28521 | -60.0793 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d306efa-d450-3c9e-ad83-502e9bceae9e | 1.63611 | -60.22268 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dfb72c2-6565-3405-b15b-d4c1f1a0bcd6 | 1.28152 | -60.07989 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7406fb63-31fa-3138-b050-3524a0eeba2e | 1.13192 | -60.50475 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f4626d9d-b0d1-3540-94ed-5fb99d256ec8 | 2.10337 | -61.81779 | 2025-03-04 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e4c8e7d-1869-37fa-80e0-bbe4b5cf5288 | 3.53638 | -60.1125 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c988772-a147-3a9a-b31b-45622e9269a5 | 2.16535 | -61.83442 | 2025-03-04 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6fe009d-82e9-3260-8cb1-609f0e0387ce | 3.43024 | -60.71288 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 66951cfa-a049-3a8f-a514-77bc2f8822b8 | 3.54159 | -60.09909 | 2025-03-04 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 087c85b2-be4b-3101-aad7-4df14708c051 | 2.35467 | -61.04937 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 928f6f47-28ff-3960-953c-5ac7c758086f | 4.2498 | -60.50954 | 2025-03-04 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 14530c4d-d07c-3257-ae86-8dd8914d8ba5 | 2.35652 | -61.06094 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9bc1d1d3-c21e-39f1-aafb-5fe1b4847064 | 1.08176 | -60.67685 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 51364422-3437-3bce-911d-087bb1c5016e | 2.3641 | -61.06372 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 74f62e25-a02a-37d5-96be-72caa4cd6ea9 | 1.12534 | -60.51003 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 13040e4c-a5bd-386e-be41-a3437e1406e0 | 1.94028 | -60.40107 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59467e12-196e-33cd-bfc1-129747c2792d | 2.36225 | -61.05214 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 039d3e91-2ff2-3e57-a25e-0db4789af8e1 | 1.936 | -60.39739 | 2025-03-04 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03b9ae0a-e438-3a81-8339-b28656123795 | 2.35754 | -61.04499 | 2025-03-04 05:40:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 390aaed6-e1ef-3d88-b0de-4a071814bcb4 | 1.13619 | -60.50833 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6c4e3406-5fa2-3494-b032-836dc94770b8 | 1.63246 | -60.22326 | 2025-03-04 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9daef1a4-ddbc-3051-8a38-ebb9c5ad17b4 | 2.84304 | -60.8533 | 2025-03-04 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ac9bc28-0d30-35e0-b8ca-60e44690a668 | 1.13294 | -60.52079 | 2025-03-04 05:59:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 29d734f5-99ab-30fc-bc4f-04dd00587e56 | 2.34541 | -61.03865 | 2025-03-04 05:59:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 8ae36d94-337e-3904-9287-17a4afc61507 | 2.35738 | -61.06627 | 2025-03-04 05:59:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 38.6 |
| c941869c-4ec0-3b4d-9d1c-0d6427df226c | 2.36172 | -61.03505 | 2025-03-04 05:59:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 4e7151c6-ea10-349d-ac5a-5315c4940ee5 | 2.35273 | -61.03262 | 2025-03-04 05:59:00 | AQUA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 41eca623-9658-327c-af1d-3eb30a4ad094 | 1.12668 | -60.51391 | 2025-03-04 05:59:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 9479a246-c867-3152-abbf-9822387bc4c4 | 1.12827 | -60.49006 | 2025-03-04 05:59:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 11009dd9-6736-3d21-9437-6b046df52913 | 2.35105 | -61.05025 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b1989bca-cd87-31f1-a40a-0d7ff9520c85 | 3.54436 | -60.09809 | 2025-03-04 06:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34db1d3e-a936-307f-9780-8177bfc7b5d1 | 2.34992 | -61.0435 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6527828b-e307-3823-ab2c-b82a688d8bda | 2.34756 | -61.0609 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5407ed4f-93c4-3875-862a-f555d6606d4f | 2.3516 | -61.05349 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bdebd7bb-2f42-3e49-915c-95d9577277f9 | 2.4232 | -61.20066 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 753892f8-8302-35a5-9d6d-ad91ecd647bc | 3.21954 | -60.98897 | 2025-03-04 06:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4458c9c8-9cb8-3cc7-b632-36fe38dbffa5 | 2.42369 | -61.20364 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abbf0e0c-66b4-32ac-825e-f4952de54da1 | 2.3614 | -61.04893 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d696ccc-faf5-3925-aea4-6a8eed71f4f5 | 3.5486 | -60.09036 | 2025-03-04 06:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09f04082-5ee9-376b-8a7e-836eba4f5c7a | 2.36034 | -61.04262 | 2025-03-04 06:01:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| cf9de673-d5c1-3bdd-907d-15ba55fb2419 | 2.75041 | -60.73203 | 2025-03-04 06:01:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README9.md)
